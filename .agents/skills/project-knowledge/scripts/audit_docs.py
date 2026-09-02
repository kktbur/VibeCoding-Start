#!/usr/bin/env python3
"""Audit the minimum project-knowledge skeleton without external dependencies."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "docs/INDEX.md",
    "docs/PRODUCT.md",
    "docs/ACCEPTANCE.md",
    "docs/CURRENT.md",
    "docs/CODEMAP.md",
    ".agents/skills/project-knowledge/SKILL.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    failures = 0

    if not root.is_dir():
        print(f"FAIL project root does not exist: {root}")
        return 1

    for relative_path in REQUIRED_FILES:
        target = root / relative_path
        if not target.is_file():
            print(f"FAIL missing {relative_path}")
            failures += 1
        elif not target.read_text(encoding="utf-8").strip():
            print(f"FAIL empty {relative_path}")
            failures += 1
        else:
            print(f"PASS {relative_path}")

    index_text = (root / "docs/INDEX.md").read_text(encoding="utf-8") if (root / "docs/INDEX.md").is_file() else ""
    for required_link in ("PRODUCT.md", "ACCEPTANCE.md", "CURRENT.md", "CODEMAP.md"):
        if required_link not in index_text:
            print(f"FAIL docs/INDEX.md does not mention {required_link}")
            failures += 1

    if failures:
        print(f"AUDIT FAIL ({failures} issue(s))")
        return 1
    print("AUDIT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

