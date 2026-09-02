#!/usr/bin/env python3
"""Audit the required project-knowledge skeleton without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    "AGENTS.md",
    "docs/INDEX.md",
    "docs/PRODUCT.md",
    "docs/PRD.md",
    "docs/ACCEPTANCE.md",
    "docs/CURRENT.md",
    "docs/CODEMAP.md",
)
INDEX_REFERENCES = (
    "PRODUCT.md",
    "PRD.md",
    "ACCEPTANCE.md",
    "CURRENT.md",
    "CODEMAP.md",
)
REQUIREMENT_HEADING = re.compile(r"^\s*#\s+PRD\s*$", re.IGNORECASE | re.MULTILINE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    failures = 0

    if not root.is_dir():
        print(f"FAIL project root does not exist: {root}")
        return 1

    contents: dict[str, str] = {}
    for relative_path in REQUIRED_FILES:
        target = root / relative_path
        if not target.is_file():
            print(f"FAIL missing {relative_path}")
            failures += 1
            continue
        text = target.read_text(encoding="utf-8")
        contents[relative_path] = text
        if not text.strip():
            print(f"FAIL empty {relative_path}")
            failures += 1
        else:
            print(f"PASS {relative_path}")

    index_text = contents.get("docs/INDEX.md", "")
    for required_link in INDEX_REFERENCES:
        if required_link not in index_text:
            print(f"FAIL docs/INDEX.md does not mention {required_link}")
            failures += 1

    prd_text = contents.get("docs/PRD.md", "")
    if prd_text and not REQUIREMENT_HEADING.search(prd_text):
        print("FAIL docs/PRD.md has no '# PRD' heading")
        failures += 1

    agents_text = contents.get("AGENTS.md", "")
    if agents_text and "PRD.md" not in agents_text:
        print("FAIL AGENTS.md does not include PRD.md in its project-knowledge guidance")
        failures += 1

    if failures:
        print(f"AUDIT FAIL ({failures} issue(s))")
        return 1
    print("AUDIT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
