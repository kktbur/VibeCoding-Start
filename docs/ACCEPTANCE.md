# Acceptance Criteria

## Requirement coverage

- REQ-001: Plugin manifest, declared Skill paths, and the repository marketplace entry validate successfully.
- REQ-002: The main Skill is `vibecoding-start` with implicit invocation enabled; the companion is `vibecoding-project-knowledge` with implicit invocation disabled.
- REQ-003: The PRD-driven `PRODUCT` → `PRD` → `ACCEPTANCE` chain is indexed and audited.
- REQ-004: Raw `.project-memory` remains local by default, with only its boundary README and redacted examples public.
- REQ-005: Deterministic documentation, link, freshness, name-drift, package, fixture, and compilation checks are available.
- REQ-006: The README explains the product, installation shape, quick start, privacy boundary, compatibility, and license.
- REQ-007: Release, rollback, backup, migration, acceptance, and observation status are recorded explicitly.
- REQ-008: PowerShell 7 and Unix-like check commands are documented, and repository text files use the shared LF policy.
- REQ-009: A redacted small-project example shows the required project-document skeleton without claiming an application implementation.
- REQ-010: Cross-Agent usage notes define repository-local handoff fields, read order, change protocol, and the no-hidden-orchestrator boundary.

- REQ-011: The main Skill and scaling reference define Small/Medium/Large gate depth and preserve the Small-project skeleton without empty governance directories.
- REQ-012: The Chinese user README is linked from the English README, covers the user-facing path, and states that the English standard is normative.
- REQ-013: The contribution guide, three Issue templates, and PR template define traceability, verification, independent review, rollback, and redacted evidence without requiring a CLA.
- REQ-014: The security policy defines private reporting, secret handling, and the no-project-memory-upload boundary without inventing a maintainer email address.

## Machine evidence


- [x] Required project-document audit passes and requires `docs/PRD.md`.
- [x] Repository-relative link audit passes on curated files.
- [x] `CURRENT.md` freshness check passes without a hard-coded date in the normal command.
- [x] Plugin manifest and marketplace entry validate as JSON and resolve their declared paths.
- [x] Both Skill frontmatters and UI metadata validate; names match their directories.
- [x] Python helper scripts compile without syntax errors.
- [x] Fixture tests show valid projects pass, missing PRD fails, broken index fails link validation, disconnected acceptance fails requirement validation, cancelled-current drift fails, and stale current state fails freshness validation.
- [x] Version consistency and tracked-text line-ending checks are available in the Plugin validation path.
- [x] PRD subtitle, Chinese heading, Chinese lifecycle-state, directory-form `.project-memory` ignore, and invalid-UTF-8 fixture cases are covered.
- [x] Active package and public documentation contain no old invocation names or duplicate Skill source paths.
- [x] `.project-memory` raw records are not tracked except for its boundary `README.md`.
- [x] The v0.3.0 governance contract checks the Chinese README, contributor/security entry points, Issue/PR templates, language links, normative-standard boundary, and privacy wording.
- [x] A new v0.3.0 fresh Codex session completes the empty-project `$vibecoding-start` E2E; a safe isolated retry completed `INIT → UPDATE → AUDIT`, generated the required knowledge skeleton, passed the bundled audits, kept raw evidence ignored, and created no commit or application source.
- [x] The target GitHub repository's `release/v0.1.0` branch contains the current Plugin package and the README after publication.
- [x] The v0.2.0 candidate's local full gate run and independent standards/spec reviews pass; PR #5 remote Plugin Validation and Standards Audit pass for both push and pull_request events.

## Owner evidence

- [ ] A new user can understand the product from the README first screen.
- [x] A fresh Codex CLI session installed the isolated package, selected `$vibecoding-start`, and completed the first-session workflow.
- [x] A new empty project received `AGENTS.md`, `INDEX`, `PRODUCT`, `PRD`, `ACCEPTANCE`, `CURRENT`, and `CODEMAP`.
- [x] The material REQ-008 change has a visible path from PRD to acceptance, deterministic checks, and the M1 worklog.
- [x] Raw session data was not included in the empty project's Git index or commit history.
- [x] The owner requested merge, tag, and Release after the listed E2E checks passed; the release record is maintained below.
- [x] The owner published `v0.1.1`; the public tag, Release page, target commit, and tag-triggered CI are verified below.
- [x] The owner explicitly authorized M2 continuation without treating the work as external-user feedback.
- [x] The owner confirmed that `v0.2.0` was published and authorized the owner-directed M3 continuation.

## E2E evidence

- [x] `$vibecoding-start` was invoked in a fresh Codex CLI session against an empty Git project.
- [x] INIT created the required project-document skeleton; UPDATE preserved raw evidence and curated the current state; AUDIT passed.
- [x] The final audit passed document structure, repository-relative links, freshness, and the `.project-memory` boundary.
- [x] The raw E2E record is retained locally under `.project-memory/e2e/` and is intentionally excluded from the public Git tree.
- [x] The tested empty project remained on `main` with zero commits, zero indexed files, and zero application source files.
- [x] The public small-project example contains the required skeleton and is validated as documentation-only.
- [x] The Cross-Agent contract documents read order, handoff fields, change protocol, evidence boundary, and its non-orchestrator scope.
- [x] The English-first/Chinese-second README uses stable GitHub custom anchors and pins the stable installation command to the published `v0.2.0` release; it links the dedicated Chinese README.
- [x] The owner accepts the rendered bilingual README and the M2 example/handoff documentation on the public repository by authorizing continuation after the public merge.
- [x] The owner authorizes the Small-project gate-depth and v0.2.0 release-candidate continuation.
- [x] The v0.2.0 candidate was separately closed: PR #5 merged, `main` and `v0.2.0` resolve to the same commit, the Release is published, and tag-triggered CI passed.
- [ ] The owner accepts the rendered v0.3.0 Chinese README and governance templates on [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6).

## Failure and recovery

- Failure: package validation fails. Recovery: stop publication, fix the manifest or package path, rerun validation, and preserve the failing evidence locally.
- Failure: PRD is missing or disconnected. Recovery: run the companion Skill's INIT/UPDATE mode, update the index and acceptance mapping, then rerun audits.
- Failure: raw memory is unexpectedly tracked. Recovery: stop publication, scan for secrets, de-index the raw files without deleting local copies, and publish only redacted examples.
- Failure: old Skill names remain in active package files. Recovery: update the active source and metadata; retain old names only in explicitly historical records.
- Failure: fresh-session installation or runtime discovery fails. Recovery: preserve package evidence, inspect the host's configured marketplace and cache, and do not claim installation success.
- Failure: remote CI or Release has not been verified. Recovery: keep package readiness separate from remote workflow/Release status and verify those resources before announcing them.
- Failure: the fresh-session E2E runner fails before writing the isolated project. Recovery: preserve the failed attempt, rerun with the normal restricted `workspace-write` sandbox in a writable isolated project, and keep the published v0.2.0 package as rollback; do not grant a nested agent unrestricted filesystem access merely to force the test through.

## Release record

- Version: `0.3.0` candidate (M3 governance surface in preparation; no `v0.3.0` tag or Release yet)
- Last known good: public [`v0.2.0` tag](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.2.0) at commit `994b121e1cff0b7eb514ce03ea79b83766d28c28`; the public `v0.1.1` tag at `f9367395e16af7a8acce57107087af8d3ae11b36` remains the previous rollback package.
- Backup/snapshot: remote `main` commit `0b570c1` and local `main` commit `837cf49` are retained as recoverable pre-refactor states.
- Release notes: [Plan 003 release notes](plans/003-v0.1.0-refactor.md#release-notes)
- M1 release notes: [Plan 004](plans/004-v0.1.1-improvement.md) and the [v0.1.1 GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.1)
- Previous release: [v0.1.0 GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.0)
- Rollback: for the v0.3.0 candidate, revert the candidate PR/commit and retain the public v0.2.0 tag as the last-known-good rollback package; keep v0.1.1 and v0.1.0 as earlier recovery packages and do not rewrite history by default.
- Migration note: consumers move from the old repository-local path to the installed `vibecoding-start` Plugin.
- Merge evidence: PR #1 was squash-merged into `main` at commit `48a14a895a8a71ded7fc2927a8a92db1c7bc302f`; PR #2 was squash-merged at `38d8c074a90a404ee6455d56693392e2f0eccd67`; post-merge M1 CI runs [#184](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806721) and [#229](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806729) passed.
- Release closeout evidence: public `main` and `v0.1.1` both resolve to `f9367395e16af7a8acce57107087af8d3ae11b36`; tag-triggered [Plugin Validation #189](https://github.com/kktbur/VibeCoding-Start/actions/runs/33955438453) and [Standards Audit #234](https://github.com/kktbur/VibeCoding-Start/actions/runs/33955438540) passed.
- Tag/Release status: `v0.1.1` is published as [VibeCoding Start v0.1.1](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.1), non-draft and non-prerelease, targeting `main`.
- M2 merge evidence: [PR #4](https://github.com/kktbur/VibeCoding-Start/pull/4) merged at `496e12b2705e1a9e67272c1f475987ea85850770`; post-merge [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33959750140) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33959750176) passed.
- v0.2.0 merge evidence: [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5) merged at `994b121e1cff0b7eb514ce03ea79b83766d28c28`; `refs/heads/main` and `refs/tags/v0.2.0` both resolve to that commit.
- v0.2.0 Release evidence: [VibeCoding Start v0.2.0](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.2.0) is Release ID `383238263`, published, non-draft, and non-prerelease.
- v0.2.0 tag-triggered CI: [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703200) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703206) completed with conclusion `success` for tag `v0.2.0` at the release commit.
- Owner acceptance: the owner confirmed the v0.2.0 Release and authorized the owner-directed v0.3.0 M3 candidate; rendered acceptance of the new governance files remains pending on PR #6.
- Historical v0.2.0 candidate review evidence: [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5) was reviewed at head `fa1a1209fc3f2fb713b9ff3f7d9381e9ea85c5c5`; [Plugin Validation PR](https://github.com/kktbur/VibeCoding-Start/actions/runs/33962069628), [Standards Audit PR](https://github.com/kktbur/VibeCoding-Start/actions/runs/33962069831), [Plugin Validation push](https://github.com/kktbur/VibeCoding-Start/actions/runs/33962047841), and [Standards Audit push](https://github.com/kktbur/VibeCoding-Start/actions/runs/33962047900) all passed before the merge.
- v0.3.0 candidate evidence: [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6) remains open and its recorded remote [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319745) plus [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319667) concluded `success`. The fresh-session E2E now passes in the local isolated retry; no v0.3.0 merge, tag, or Release is claimed.

