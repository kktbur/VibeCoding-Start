#!/usr/bin/env python3
"""Validate the v0.3.0 public governance surface."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GovernanceDocumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.chinese_readme = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")
        cls.contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        cls.security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        cls.check_script = (ROOT / "scripts" / "check.sh").read_text(encoding="utf-8")
        cls.workflow = (ROOT / ".github" / "workflows" / "plugin-validation.yml").read_text(
            encoding="utf-8"
        )
        cls.pr_template = (ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(
            encoding="utf-8"
        )

    def test_required_governance_files_exist(self) -> None:
        required = [
            ROOT / "README.zh-CN.md",
            ROOT / "CONTRIBUTING.md",
            ROOT / "SECURITY.md",
            ROOT / "scripts" / "check.sh",
            ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
            ROOT / ".github" / "ISSUE_TEMPLATE" / "bug-report.md",
            ROOT / ".github" / "ISSUE_TEMPLATE" / "skill-behavior.md",
            ROOT / ".github" / "ISSUE_TEMPLATE" / "documentation.md",
        ]
        missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
        self.assertEqual(missing, [])

    def test_language_switch_and_normative_standard_boundary(self) -> None:
        self.assertIn("README.zh-CN.md", self.readme)
        self.assertIn("README.md", self.chinese_readme)
        self.assertIn("standard-v1.3.md", self.chinese_readme)
        self.assertRegex(
            self.chinese_readme,
            re.compile(r"英文.*standard-v1\.3\.md.*(?:规范|准)", re.IGNORECASE | re.DOTALL),
        )
        self.assertIn("--ref v0.3.0", self.readme)
        self.assertIn("--ref v0.3.0", self.chinese_readme)

    def test_contributor_and_security_boundaries_are_explicit(self) -> None:
        for content in (self.contributing, self.security, self.pr_template):
            self.assertIn(".project-memory", content)
            self.assertRegex(
                content,
                re.compile(r"token|secret|private key|password|cookie", re.IGNORECASE),
            )
        self.assertIn("independent", self.contributing.lower())
        self.assertIn("rollback", self.contributing.lower())
        self.assertIn("PRODUCT", self.pr_template)
        self.assertIn("PRD", self.pr_template)
        self.assertIn("ACCEPTANCE", self.pr_template)
        self.assertIn("private", self.security.lower())
        self.assertIn("README.md#project-memory-and-privacy", self.security)
        self.assertIn("security/advisories/new", self.security)
        self.assertIn("bash scripts/check.sh", self.contributing)
        self.assertIn("Plugin Validation", self.contributing)
        self.assertIn("Standards Audit", self.contributing)

    def test_check_wrapper_calls_repository_checks(self) -> None:
        self.assertTrue(self.check_script.startswith("#!/usr/bin/env bash\n"))
        for path in (
            "tests/test_governance_docs.py",
            "tests/test_readme_navigation.py",
            "tests/test_small_path_contract.py",
            "tests/check_name_drift.py",
            "tests/check_line_endings.py",
        ):
            self.assertIn(path, self.check_script)
        self.assertIn("bash scripts/check.sh", self.workflow)

    def test_templates_have_github_frontmatter(self) -> None:
        template_root = ROOT / ".github" / "ISSUE_TEMPLATE"
        for path in sorted(template_root.glob("*.md")):
            content = path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"), path.name)
            self.assertIn("name:", content, path.name)
            self.assertIn("about:", content, path.name)
            self.assertIn("title:", content, path.name)


if __name__ == "__main__":
    unittest.main()

