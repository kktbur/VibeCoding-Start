# Changelog

All notable changes to VibeCoding Start are documented here.

## [Unreleased]

## [0.3.0] - 2026-09-05

### Added

- Add a user-facing `README.zh-CN.md` while keeping the English README and English standard as canonical normative sources.
- Add `CONTRIBUTING.md`, bug/Skill-behavior/documentation Issue templates, and a pull request template.
- Add `SECURITY.md` with private reporting and local project-memory handling guidance.
- Add deterministic validation for the public governance surface.

### Changed

- Pin the stable README installation path to the published `v0.2.0` release.
- Refresh the indexed project state and release mapping for the v0.3.0 candidate.

## [0.2.0] - 2026-09-05

### Added

- Add an English-first, Chinese-second README with visible language navigation and a pinned `v0.1.1` installation path.
- Add a redacted small-project example and repository-local Cross-Agent usage notes.
- Add a Small/Medium/Large gate-depth matrix and a concrete Small-project artifact path.
- Add deterministic validation for the public example, README navigation, and Small-project gate depth.
- Clarify the ownership boundary between `vibecoding-start`, `vibecoding-project-knowledge`, and the scaling reference.

## [0.1.1] - 2026-09-05

### Fixed

- Make project-document auditing tolerant of PRD subtitles, Chinese headings, Chinese lifecycle states, and common `.project-memory` ignore rules.
- Report invalid UTF-8 project documents as audit failures instead of terminating with a traceback.

### Changed

- Replace the repository marketplace identifier `personal` with the public identifier `kktbur`.
- Normalize repository text-file conventions with `.gitattributes` and `.editorconfig`.
- Add version-consistency and line-ending checks to the deterministic validation path.

### Documentation

- Rewrite the public installation path so it contains final user instructions rather than release-process notes.
- Add CI and license badges, the project knowledge index, and release links to the README.
- Add a small-project improvement plan and refresh the repository's active release state.

## [0.1.0] - 2026-09-03

### Added

- First public Skill-only Codex Plugin distribution.
- `vibecoding-start` engineering workflow with G0-G9 gates.
- `vibecoding-project-knowledge` INIT/UPDATE/AUDIT workflow.
- PRD-driven indexed project knowledge and local-first raw project memory.
- Reuse-before-build guidance, independent review, adversarial verification, human acceptance, and rollback-aware release guidance.
- MIT License, package validation, fixtures, and GitHub Actions checks.
- Fresh-session E2E verification in an empty Git project.

