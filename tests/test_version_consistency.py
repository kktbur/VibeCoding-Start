#!/usr/bin/env python3
"""Exercise the version-consistency check with repository and temporary cases."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tests" / "check_version_consistency.py"


class VersionConsistencyTests(unittest.TestCase):
    def run_check(self, plugin_root: Path, changelog: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--plugin-root",
                str(plugin_root),
                "--changelog",
                str(changelog),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_repository_versions_pass(self) -> None:
        result = self.run_check(
            ROOT / "plugins" / "vibecoding-start", ROOT / "CHANGELOG.md"
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_mismatched_plugin_version_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manifest_dir = root / ".codex-plugin"
            manifest_dir.mkdir()
            (manifest_dir / "plugin.json").write_text(
                json.dumps({"version": "9.9.9"}), encoding="utf-8"
            )
            changelog = root / "CHANGELOG.md"
            changelog.write_text(
                "# Changelog\n\n## [Unreleased]\n\n## [0.1.1] - 2026-09-05\n\n## [0.1.0] - 2026-09-03\n",
                encoding="utf-8",
            )
            result = self.run_check(root, changelog)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("does not match latest changelog version", result.stdout)


if __name__ == "__main__":
    unittest.main()

