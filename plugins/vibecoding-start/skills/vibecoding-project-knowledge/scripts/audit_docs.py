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
REQUIREMENT_HEADING = re.compile(
    r"^\s*#\s+(PRD|产品需求文档|产品需求)\b", re.IGNORECASE | re.MULTILINE
)
REQUIREMENT_ID = re.compile(r"\bREQ-\d+\b", re.IGNORECASE)
CANCELLED_WORD = re.compile(
    r"(?:\b(cancelled|canceled|superseded|removed|no longer active|deprecated)\b|"
    r"已取消|已废弃|已替代|已移除|不再有效|已关闭)",
    re.IGNORECASE,
)
PROJECT_MEMORY_RULES = {
    ".project-memory",
    ".project-memory/",
    ".project-memory/*",
    "/.project-memory",
    "/.project-memory/",
    "/.project-memory/*",
    "**/.project-memory/**",
}


def read_utf8(target: Path, relative_path: str, failures: list[int]) -> str:
    try:
        return target.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"FAIL cannot read {relative_path} as UTF-8")
        failures[0] += 1
        return ""


def protects_project_memory(text: str) -> bool:
    for raw_line in text.splitlines():
        rule = raw_line.split("#", 1)[0].strip()
        if rule.startswith("!"):
            continue
        if (
            rule in PROJECT_MEMORY_RULES
            or rule.endswith(".project-memory/")
        ):
            return True
    return False


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
        failure_count = [failures]
        text = read_utf8(target, relative_path, failure_count)
        failures = failure_count[0]
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
        print("FAIL docs/PRD.md has no PRD or 产品需求 heading")
        failures += 1

    acceptance_text = contents.get("docs/ACCEPTANCE.md", "")
    prd_ids = {value.upper() for value in REQUIREMENT_ID.findall(prd_text)}
    acceptance_ids = {value.upper() for value in REQUIREMENT_ID.findall(acceptance_text)}
    if prd_ids:
        missing_acceptance = sorted(prd_ids - acceptance_ids)
        extra_acceptance = sorted(acceptance_ids - prd_ids)
        if missing_acceptance:
            print(f"FAIL acceptance is missing PRD requirements: {', '.join(missing_acceptance)}")
            failures += 1
        if extra_acceptance:
            print(f"FAIL acceptance contains requirements absent from PRD: {', '.join(extra_acceptance)}")
            failures += 1

    current_text = contents.get("docs/CURRENT.md", "")
    cancelled_ids = set()
    for line in prd_text.splitlines():
        if CANCELLED_WORD.search(line):
            cancelled_ids.update(value.upper() for value in REQUIREMENT_ID.findall(line))
    for line in current_text.splitlines():
        current_ids = {value.upper() for value in REQUIREMENT_ID.findall(line)}
        for cancelled_id in sorted(current_ids & cancelled_ids):
            if not CANCELLED_WORD.search(line):
                print(f"FAIL CURRENT.md presents cancelled requirement as current: {cancelled_id}")
                failures += 1

    gitignore = root / ".gitignore"
    if (root / ".project-memory").exists():
        failure_count = [failures]
        gitignore_text = (
            read_utf8(gitignore, ".gitignore", failure_count)
            if gitignore.is_file()
            else ""
        )
        failures = failure_count[0]
        if not protects_project_memory(gitignore_text):
            print("FAIL .gitignore does not protect local .project-memory records")
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
