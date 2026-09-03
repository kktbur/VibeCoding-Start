#!/usr/bin/env python3
"""Check repository-relative Markdown links in curated project files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_markdown(root: Path):
    excluded = {".git", ".venv", "node_modules", "__pycache__", "templates", ".project-memory", "fixtures"}
    for path in root.rglob("*.md"):
        if not excluded.intersection(path.relative_to(root).parts):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()
    broken = 0
    checked = 0

    if not root.is_dir():
        print(f"FAIL project root does not exist: {root}")
        return 1

    for document in iter_markdown(root):
        text = document.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip().split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            checked += 1
            resolved = (document.parent / unquote(target)).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                print(f"FAIL outside project: {document.relative_to(root)} -> {target}")
                broken += 1
                continue
            if not resolved.exists():
                print(f"FAIL broken link: {document.relative_to(root)} -> {target}")
                broken += 1

    if broken:
        print(f"LINK AUDIT FAIL ({broken} broken link(s), {checked} checked)")
        return 1
    print(f"LINK AUDIT PASS ({checked} repository link(s) checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
