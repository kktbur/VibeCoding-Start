#!/usr/bin/env python3
"""Validate the required public small-project example skeleton."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "docs" / "examples" / "small-project" / "project"


class PublicExampleTests(unittest.TestCase):
    def test_small_project_has_required_skeleton(self) -> None:
        required = [
            EXAMPLE / "AGENTS.md",
            EXAMPLE / "docs" / "INDEX.md",
            EXAMPLE / "docs" / "PRODUCT.md",
            EXAMPLE / "docs" / "PRD.md",
            EXAMPLE / "docs" / "ACCEPTANCE.md",
            EXAMPLE / "docs" / "CURRENT.md",
            EXAMPLE / "docs" / "CODEMAP.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [], f"missing example files: {missing}")

    def test_small_project_is_documentation_only(self) -> None:
        source_files = [
            path
            for path in EXAMPLE.rglob("*")
            if path.is_file() and path.suffix not in {".md", ".txt"}
        ]
        self.assertEqual(source_files, [], f"unexpected example source files: {source_files}")


if __name__ == "__main__":
    unittest.main()

