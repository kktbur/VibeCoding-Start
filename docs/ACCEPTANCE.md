# Acceptance Criteria

## Requirement coverage

- REQ-001: Plugin manifest, declared Skill paths, and the repository marketplace entry validate successfully.
- REQ-002: The main Skill is `vibecoding-start` with implicit invocation enabled; the companion is `vibecoding-project-knowledge` with implicit invocation disabled.
- REQ-003: The PRD-driven `PRODUCT` → `PRD` → `ACCEPTANCE` chain is indexed and audited.
- REQ-004: Raw `.project-memory` remains local by default, with only its boundary README and redacted examples public.
- REQ-005: Deterministic documentation, link, freshness, name-drift, package, fixture, and compilation checks are available.
- REQ-006: The README explains the product, installation shape, quick start, privacy boundary, compatibility, and license.
- REQ-007: Release, rollback, backup, migration, acceptance, and observation status are recorded explicitly.

## Machine evidence

- [x] Required project-document audit passes and requires `docs/PRD.md`.
- [x] Repository-relative link audit passes on curated files.
- [x] `CURRENT.md` freshness check passes without a hard-coded date in the normal command.
- [x] Plugin manifest and marketplace entry validate as JSON and resolve their declared paths.
- [x] Both Skill frontmatters and UI metadata validate; names match their directories.
- [x] Python helper scripts compile without syntax errors.
- [x] Fixture tests show valid projects pass, missing PRD fails, broken index fails link validation, disconnected acceptance fails requirement validation, cancelled-current drift fails, and stale current state fails freshness validation.
- [x] Active package and public documentation contain no old invocation names or duplicate Skill source paths.
- [x] `.project-memory` raw records are not tracked except for its boundary `README.md`.
- [x] The target GitHub repository's `release/v0.1.0` branch contains the current Plugin package and the README after publication.

## Owner evidence

- [ ] A new user can understand the product from the README first screen.
- [ ] A fresh Codex session can install or select the Plugin and invoke `$vibecoding-start`.
- [ ] A new project receives `AGENTS.md`, `INDEX`, `PRODUCT`, `PRD`, `ACCEPTANCE`, `CURRENT`, and `CODEMAP`.
- [ ] A material requirement change has a visible path from PRD to acceptance and verification.
- [ ] Raw session data is not included in a normal Git commit.
- [ ] The owner confirms the package is ready for the `v0.1.0` tag and Release.

## Failure and recovery

- Failure: package validation fails. Recovery: stop publication, fix the manifest or package path, rerun validation, and preserve the failing evidence locally.
- Failure: PRD is missing or disconnected. Recovery: run the companion Skill's INIT/UPDATE mode, update the index and acceptance mapping, then rerun audits.
- Failure: raw memory is unexpectedly tracked. Recovery: stop publication, scan for secrets, de-index the raw files without deleting local copies, and publish only redacted examples.
- Failure: old Skill names remain in active package files. Recovery: update the active source and metadata; retain old names only in explicitly historical records.
- Failure: fresh-session installation or runtime discovery fails. Recovery: preserve package evidence, inspect the host's configured marketplace and cache, and do not claim installation success.
- Failure: remote CI or Release has not been verified. Recovery: keep package readiness separate from remote workflow/Release status and verify those resources before announcing them.

## Release record

- Version: `0.1.0`
- Last known good: local `main` commit `837cf49` (v1.2 repository-local package)
- Backup/snapshot: remote `main` commit `0b570c1` and local `main` commit `837cf49` are retained as recoverable pre-refactor states.
- Release notes: [Plan 003 release notes](plans/003-v0.1.0-refactor.md#release-notes)
- Rollback: retain the v1.2 commit and restore the prior package tree only by an intentional revert or branch decision; do not rewrite history by default.
- Migration note: consumers move from the old repository-local path to the installed `vibecoding-start` Plugin.
- Owner acceptance: pending until a fresh-session install and repository review are completed.
