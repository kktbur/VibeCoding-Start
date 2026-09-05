#!/usr/bin/env python3
"""Validate the documented gate depth for genuinely small projects."""

from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN_SKILL = ROOT / "plugins" / "vibecoding-start" / "skills" / "vibecoding-start" / "SKILL.md"
COMPANION_SKILL = (
    ROOT
    / "plugins"
    / "vibecoding-start"
    / "skills"
    / "vibecoding-project-knowledge"
    / "SKILL.md"
)
SCALING_RULES = (
    ROOT
    / "plugins"
    / "vibecoding-start"
    / "skills"
    / "vibecoding-project-knowledge"
    / "references"
    / "scaling-rules.md"
)
STANDARD = SCALING_RULES.with_name("standard-v1.3.md")
README = ROOT / "README.md"
VALID_SMALL_PROJECT = ROOT / "docs" / "examples" / "small-project" / "project"

EXPECTED_GATES = (
    ("G0", "Scope"),
    ("G1", "Intent"),
    ("G2", "Reuse"),
    ("G3", "Plan"),
    ("G4", "Build"),
    ("G5", "Review"),
    ("G6", "Verify"),
    ("G7", "Accept"),
    ("G8", "Release"),
    ("G9", "Observe"),
)

SMALL_ARTIFACTS = (
    "AGENTS.md",
    "docs/INDEX.md",
    "docs/PRODUCT.md",
    "docs/PRD.md",
    "docs/ACCEPTANCE.md",
    "docs/CURRENT.md",
    "docs/CODEMAP.md",
)


class SmallPathContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.main_skill = MAIN_SKILL.read_text(encoding="utf-8")
        cls.companion_skill = COMPANION_SKILL.read_text(encoding="utf-8")
        cls.scaling_rules = SCALING_RULES.read_text(encoding="utf-8")
        cls.standard = STANDARD.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")

    def test_main_skill_contains_complete_gate_depth_matrix(self) -> None:
        matrix = self.main_skill.split("### Scale the gates before applying them", 1)[1]
        matrix = matrix.split("For a Small project:", 1)[0]
        self.assertIn("| Gate | Small (local, offline, no persistence) | Medium | Large |", matrix)
        for gate, label in EXPECTED_GATES:
            self.assertEqual(matrix.count(f"| {gate} {label} |"), 1, gate)
        self.assertIn("independent reviewer (not the author) for material changes", matrix)
        self.assertIn(
            "last-known-good, release notes, backup/rollback, migration risk, and exact target",
            matrix,
        )

    def test_main_skill_keeps_small_project_hard_constraints(self) -> None:
        for marker in (
            "Still create `AGENTS.md`",
            "Do not create empty `docs/architecture/`",
            "prefer the standard library",
        ):
            self.assertIn(marker, self.main_skill)

    def test_scaling_reference_describes_small_artifacts(self) -> None:
        for marker in (
            "## Small",
            "local, offline tool with no persistence",
            *tuple(f"`{artifact}`" for artifact in SMALL_ARTIFACTS[1:]),
            "Do not create empty `docs/architecture/`",
        ):
            self.assertIn(marker, self.scaling_rules)

    def test_valid_small_project_matches_artifact_and_depth_contract(self) -> None:
        for artifact in SMALL_ARTIFACTS:
            artifact_path = VALID_SMALL_PROJECT / artifact
            self.assertTrue(artifact_path.is_file(), artifact)
            self.assertLessEqual(
                len(artifact_path.read_text(encoding="utf-8").splitlines()),
                30,
                artifact,
            )
        for directory in ("architecture", "incidents", "operations"):
            self.assertFalse((VALID_SMALL_PROJECT / "docs" / directory).exists(), directory)

    def test_cross_reference_contract_covers_all_active_sources(self) -> None:
        self.assertIn("standard-v1.3.md", self.readme)
        self.assertIn("scaling-rules.md", self.readme)
        self.assertIn("docs/examples/small-project/README.md", self.readme)
        self.assertIn("Standard v1.3", self.main_skill)
        self.assertIn("scaling rules](../vibecoding-project-knowledge/references/scaling-rules.md)", self.main_skill)
        self.assertIn("`vibecoding-start` is the normal entry point", self.companion_skill)
        self.assertIn("owns the indexed-document lifecycle", self.companion_skill)
        self.assertIn("main Skill's gate-depth matrix", self.companion_skill)
        self.assertIn("Small projects keep each document short", self.standard)
        self.assertIn("The author is not the final reviewer", self.standard)
        self.assertIn("Record version, last-known-good state", self.standard)


if __name__ == "__main__":
    unittest.main()

