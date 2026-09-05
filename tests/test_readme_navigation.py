#!/usr/bin/env python3
"""Validate the README's English-first bilingual navigation contract."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXAMPLE_ROOT = ROOT / "docs" / "examples" / "small-project"


class ReadmeNavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.content = README.read_text(encoding="utf-8")

    def test_language_navigation_and_order(self) -> None:
        english_anchor = '<a name="vibecoding-start-english"></a>'
        chinese_anchor = '<a name="vibecoding-start-chinese"></a>'

        self.assertIn("[English](#vibecoding-start-english)", self.content)
        self.assertIn("[中文](#vibecoding-start-chinese)", self.content)
        self.assertLess(self.content.index(english_anchor), self.content.index(chinese_anchor))
        self.assertEqual(self.content.count(english_anchor), 1)
        self.assertEqual(self.content.count(chinese_anchor), 1)

    def test_pinned_and_development_install_paths_are_explicit(self) -> None:
        pinned = "codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref v0.1.1"
        development = "codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref main"

        self.assertEqual(self.content.count(pinned), 2)
        self.assertEqual(self.content.count(development), 2)
        self.assertEqual(self.content.count("codex plugin add vibecoding-start@kktbur"), 6)

    def test_small_project_example_is_redacted_markdown_only(self) -> None:
        files = [path for path in EXAMPLE_ROOT.rglob("*") if path.is_file()]
        unexpected = [path for path in files if path.suffix.lower() != ".md"]
        self.assertEqual(unexpected, [], f"unexpected non-Markdown example files: {unexpected}")

        forbidden = [
            re.compile(r"-----BEGIN [^-]*PRIVATE KEY-----", re.IGNORECASE),
            re.compile(
                r"\b(?:api[_ -]?key|access[_ -]?token|secret|password|cookie)\b\s*[:=]\s*\S+",
                re.IGNORECASE,
            ),
            re.compile(r"(?:[A-Z]:\\|\\\\[A-Za-z])", re.IGNORECASE),
            re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"),
        ]
        violations = []
        for path in files:
            content = path.read_text(encoding="utf-8")
            for pattern in forbidden:
                if pattern.search(content):
                    violations.append(str(path.relative_to(ROOT)))
                    break
        self.assertEqual(violations, [], f"possible sensitive data in example: {violations}")


if __name__ == "__main__":
    unittest.main()

