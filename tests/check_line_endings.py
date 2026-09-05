#!/usr/bin/env python3
"""Reject non-LF line endings in tracked text files after LF policy adoption."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.project_root).resolve()

    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--eol", "-z"],
        text=False,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        print(f"FAIL git ls-files --eol failed: {result.stderr.decode(errors='replace').strip()}")
        return 1

    failures: list[tuple[str, str]] = []
    for raw_entry in result.stdout.split(b"\0"):
        if not raw_entry:
            continue
        try:
            entry = raw_entry.decode("utf-8")
        except UnicodeDecodeError:
            failures.append(("<invalid UTF-8 path>", "path encoding"))
            continue
        metadata, relative_path = entry.split("\t", 1)
        if any(marker in metadata for marker in ("i/crlf", "i/mixed", "w/crlf", "w/mixed")):
            failures.append((relative_path, metadata))

    if failures:
        for path, metadata in failures:
            print(f"FAIL non-LF tracked text file: {path} ({metadata})")
        print(f"LINE ENDINGS FAIL ({len(failures)} file(s))")
        return 1
    print("LINE ENDINGS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
