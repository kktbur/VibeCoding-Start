# Changelog

All notable changes to VibeCoding Start are documented here.

## [Unreleased]

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

