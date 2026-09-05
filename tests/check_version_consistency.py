#!/usr/bin/env python3
"""Check that the Plugin version agrees with the repository changelog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
VERSION_HEADING = re.compile(r"^##\s+\[([^\]]+)\]", re.MULTILINE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--plugin-root", default="plugins/vibecoding-start", help="Plugin directory"
    )
    parser.add_argument(
        "--changelog", default="CHANGELOG.md", help="Keep a Changelog file"
    )
    args = parser.parse_args()

    plugin_root = Path(args.plugin_root).resolve()
    changelog_path = Path(args.changelog).resolve()
    failures: list[str] = []

    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        failures.append(f"cannot read plugin manifest: {exc}")
        manifest = {}

    plugin_version = str(manifest.get("version", ""))
    if not SEMVER.fullmatch(plugin_version):
        failures.append(f"plugin version is not valid semver: {plugin_version!r}")

    try:
        changelog = changelog_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        failures.append(f"cannot read changelog: {exc}")
        changelog = ""

    versions = [
        version
        for version in VERSION_HEADING.findall(changelog)
        if version.lower() != "unreleased"
    ]
    if not versions:
        failures.append("changelog has no dated semantic-version heading")
    elif versions[0] != plugin_version:
        failures.append(
            f"plugin version {plugin_version} does not match latest changelog version {versions[0]}"
        )
    if "0.1.0" not in versions:
        failures.append("changelog must retain the 0.1.0 release entry")

    for version in versions:
        if not SEMVER.fullmatch(version):
            failures.append(f"changelog heading is not valid semver: {version!r}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"VERSION FAIL ({len(failures)} issue(s))")
        return 1

    print(f"PASS plugin version {plugin_version}")
    print(f"PASS changelog versions {', '.join(versions)}")
    print("VERSION PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

