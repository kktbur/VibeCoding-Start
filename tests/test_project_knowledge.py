#!/usr/bin/env python3
"""Exercise project-knowledge audit contracts with standard-library fixtures."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "plugins" / "vibecoding-start" / "skills" / "vibecoding-project-knowledge" / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"


def run_script(script: str, fixture: str, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / script), str(FIXTURES / fixture), *extra],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class ProjectKnowledgeContractTests(unittest.TestCase):
    def test_valid_small_project_passes(self) -> None:
        audit = run_script("audit_docs.py", "valid-small-project")
        self.assertEqual(audit.returncode, 0, audit.stdout + audit.stderr)
        links = run_script("check_links.py", "valid-small-project")
        self.assertEqual(links.returncode, 0, links.stdout + links.stderr)
        fresh = run_script("detect_stale_docs.py", "valid-small-project", "--as-of", "2026-09-03")
        self.assertEqual(fresh.returncode, 0, fresh.stdout + fresh.stderr)

    def test_missing_prd_fails_document_audit(self) -> None:
        result = run_script("audit_docs.py", "missing-prd")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("PRD.md", result.stdout)

    def test_disconnected_acceptance_fails_requirement_audit(self) -> None:
        result = run_script("audit_docs.py", "disconnected-acceptance")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("REQ-002", result.stdout)

    def test_cancelled_requirement_in_current_fails_audit(self) -> None:
        result = run_script("audit_docs.py", "cancelled-current")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("cancelled requirement", result.stdout)

    def test_broken_index_fails_link_audit(self) -> None:
        result = run_script("check_links.py", "broken-index")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("broken link", result.stdout)

    def test_stale_current_fails_freshness_check(self) -> None:
        result = run_script("detect_stale_docs.py", "stale-current", "--as-of", "2026-09-03")
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("STALE CURRENT.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
