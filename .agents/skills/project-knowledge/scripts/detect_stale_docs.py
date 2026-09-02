#!/usr/bin/env python3
"""Warn when CURRENT.md has not been updated within the configured window."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


DATE_PATTERN = re.compile(r"(?:Last updated|最后更新)\s*:\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    parser.add_argument("--max-age-days", type=int, default=30)
    parser.add_argument("--as-of", help="YYYY-MM-DD, useful for deterministic checks")
    args = parser.parse_args()
    current_path = Path(args.project_root).resolve() / "docs" / "CURRENT.md"

    if not current_path.is_file():
        print("FAIL docs/CURRENT.md is missing")
        return 1
    match = DATE_PATTERN.search(current_path.read_text(encoding="utf-8"))
    if not match:
        print("FAIL docs/CURRENT.md has no Last updated: YYYY-MM-DD line")
        return 1

    updated = dt.date.fromisoformat(match.group(1))
    as_of = dt.date.fromisoformat(args.as_of) if args.as_of else dt.date.today()
    age = (as_of - updated).days
    if age < 0:
        print(f"WARN CURRENT.md date is in the future: {updated.isoformat()}")
        return 0
    if age > args.max_age_days:
        print(f"STALE CURRENT.md: {age} day(s) old; threshold is {args.max_age_days}")
        return 2
    print(f"FRESH CURRENT.md: {age} day(s) old; threshold is {args.max_age_days}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

