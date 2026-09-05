#!/usr/bin/env python3
"""Reject old active Skill names and duplicate source paths."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ACTIVE_FILES = (
    "AGENTS.md",
    "README.md",
    "README.zh-CN.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "scripts/check.sh",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug-report.md",
    ".github/ISSUE_TEMPLATE/skill-behavior.md",
    ".github/ISSUE_TEMPLATE/documentation.md",
    "docs/INDEX.md",
    "docs/PRODUCT.md",
    "docs/PRD.md",
    "docs/ACCEPTANCE.md",
    "docs/CURRENT.md",
    "docs/CODEMAP.md",
    "docs/standards/INDEX.md",
    "docs/standards/standard-v1.3.md",
    "docs/standards/LOCAL-DEPLOYMENT.md",
)
ACTIVE_PATTERNS = (
    "$vibe-engineering-development-standard",
    "$project-knowledge",
    ".agents/skills/vibe-engineering-development-standard",
    ".agents/skills/project-knowledge",
    "name: vibe-engineering-development-standard",
    "name: project-knowledge",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    failures = 0

    old_root = root / ".agents" / "skills"
    if old_root.is_dir() and any(old_root.rglob("*")):
        print(f"FAIL duplicate maintained Skill source exists under {old_root.relative_to(root)}")
        failures += 1

    files = [root / path for path in ACTIVE_FILES]
    files.extend(
        path
        for path in (root / "plugins").rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}
    )
    for path in files:
        if not path.is_file():
            print(f"FAIL active file is missing: {path.relative_to(root)}")
            failures += 1
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in ACTIVE_PATTERNS:
            if pattern in text:
                print(f"FAIL old active name/path {pattern!r} remains in {path.relative_to(root)}")
                failures += 1

    if failures:
        print(f"NAME DRIFT FAIL ({failures} issue(s))")
        return 1
    print("NAME DRIFT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
