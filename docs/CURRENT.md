# Current State

Last updated: 2026-09-05

## Status

RELEASED v0.2.0 BASELINE + v0.3.0 M3 CANDIDATE PR OPEN — v0.1.1 M1 maintenance changes were squash-merged into public `main` at `38d8c074a90a404ee6455d56693392e2f0eccd67`; the public `v0.1.1` tag and GitHub Release remain published from `f9367395e16af7a8acce57107087af8d3ae11b36`, and their post-release checks passed. M2 was merged through [PR #4](https://github.com/kktbur/VibeCoding-Start/pull/4), and the v0.2.0 candidate was reviewed and merged through [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5) at `994b121e1cff0b7eb514ce03ea79b83766d28c28`. The public `v0.2.0` tag and GitHub Release now target that merge commit; both tag-triggered checks passed. The v0.3.0 governance candidate is open as [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6); at the latest evidence capture, remote head `de94f16b6b4aca62c3ef03b88e5b7ab8ab055d23` passed [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319745) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319667). Merge, tag, and Release remain pending. The owner confirmed publication and authorized the owner-directed v0.3.0 governance continuation; no external user feedback is being claimed for this scope.

## Completed

- Preserved the v1.2 source plan and prior baseline history.
- Created the local `release/v0.1.0` branch from the v1.2 package state.
- Scaffolded a repo-local marketplace and a Skill-only Plugin manifest.
- Moved the two maintained Skill sources under `plugins/vibecoding-start/skills/`.
- Added the active v1.3 standard, an independent PRD, MIT License, product README, local raw-memory boundary, validation scripts, and test fixtures.
- Kept the existing 9 September 3 local installation/uninstallation records in the working tree; they remain local raw/history material and will not be published as raw memory.
- Published a 99-file remote release branch with the same public file set as the local release branch; sensitive historical worklogs and raw project memory are absent from that branch.
- Opened [PR #1](https://github.com/kktbur/VibeCoding-Start/pull/1) from `release/v0.1.0` to `main`; GitHub Actions `Plugin Validation` and `Standards Audit` both passed for the PR head.
- Installed the package from an isolated local marketplace in a fresh Codex CLI session and invoked `$vibecoding-start` in an empty Git project.
- Completed INIT, UPDATE, and AUDIT in that empty project: all six core documents plus `AGENTS.md` were generated, the raw-memory boundary passed, and no application source or Git commit was created.
- Squash-merged PR #1 into `main` at commit `48a14a895a8a71ded7fc2927a8a92db1c7bc302f`; post-merge `Plugin Validation` run #168 and `Standards Audit` run #213 both passed.
- Created the public `v0.1.0` tag and [GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.0) from the verified merge commit.
- Added the public README cover at `assets/vibecoding-start-cover.png` on `main`.
- Implemented M1 WP-11 through WP-16 on [PR #2](https://github.com/kktbur/VibeCoding-Start/pull/2), including README, CHANGELOG/version gates, audit fixtures, LF policy, marketplace rename, and cross-platform check documentation.
- Passed PR #2 CI after correcting the remote fixture boundary and normalizing the inherited `docs/standards/SOURCE-PLAN.md` blob to LF.
- Squash-merged PR #2 into `main` at `38d8c074a90a404ee6455d56693392e2f0eccd67`; post-merge [Plugin Validation #184](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806721) and [Standards Audit #229](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806729) passed.
- Published the public [`v0.1.1` tag and GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.1) at `f9367395e16af7a8acce57107087af8d3ae11b36`; the Release is published, non-draft, and targets `main`.
- Verified the tagged Plugin manifest remains version `0.1.1`, the marketplace identifier is `kktbur`, and the tag and `main` resolve to the same commit.
- Started the owner-directed M2 foundation: bilingual README navigation, pinned release installation, a redacted small-project example, Cross-Agent usage notes, and deterministic public-example validation.
- Merged M2 through PR #4 and verified that the public README now shows visible `English` and `中文` controls below the cover.
- Started the v0.2.0 release candidate: Small/Medium/Large gate-depth matrix, Small-project hard constraints, concrete scaling artifacts, cross-reference ownership, and a deterministic Small-path contract test.
- Completed independent standards/spec review, fixed the three review gaps, published the candidate as [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5), and verified all four candidate CI runs passed.
- Closed the v0.2.0 release boundary: PR #5 was merged, `main` and `v0.2.0` resolve to `994b121e1cff0b7eb514ce03ea79b83766d28c28`, the Release is published, and tag-triggered Plugin Validation and Standards Audit passed.
- Started the owner-directed v0.3.0 M3 governance candidate: Chinese user README, contribution entry points, Issue/PR templates, security policy, governance contract test, and indexed release-state refresh.
- Opened [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6) for the v0.3.0 governance candidate; at the latest evidence capture, remote head `de94f16b6b4aca62c3ef03b88e5b7ab8ab055d23` passed [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319745) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319667).

## Active requirements

- `REQ-001` through `REQ-014` in [PRD.md](PRD.md); REQ-012 through REQ-014 are the active v0.3.0 governance requirements.

## Evidence

- Local raw output remains under `.project-memory/` and is ignored except for its boundary README; the complete E2E record is retained under `.project-memory/e2e/`.
- Local document, link, freshness, package, fixture, name-drift, compilation, and external Plugin/Skill validators pass; the remote release tree has matching file paths and core-file content after newline normalization.
- M1 local verification passes: 16 unit tests, document audit, 53-link audit, freshness, Plugin validation, version consistency, LF line endings, name drift, and compilation.
- Final E2E output: `INIT_RESULT=PASS`, `UPDATE_RESULT=PASS`, `FINAL_AUDIT_RESULT=PASS`; raw evidence is ignored, the boundary README is not ignored, and the empty project has zero commits and zero application source files.
- Remote release evidence: [`v0.1.1` tag](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.1) and `refs/heads/main` both resolve to `f9367395e16af7a8acce57107087af8d3ae11b36`; Release ID `383184751` is published, and tag-triggered [Plugin Validation #189](https://github.com/kktbur/VibeCoding-Start/actions/runs/33955438453) plus [Standards Audit #234](https://github.com/kktbur/VibeCoding-Start/actions/runs/33955438540) passed.
- M2 merge evidence: [PR #4](https://github.com/kktbur/VibeCoding-Start/pull/4) merged at `496e12b2705e1a9e67272c1f475987ea85850770`; post-merge [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33959750140) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33959750176) passed.
- v0.2.0 release evidence: [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5) merged at `994b121e1cff0b7eb514ce03ea79b83766d28c28`; `refs/heads/main` and `refs/tags/v0.2.0` both resolve to that commit. Release ID `383238263` is published at [VibeCoding Start v0.2.0](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.2.0); tag-triggered [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703200) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703206) passed.
- The v0.3.0 governance scope is recorded in [Plan 007](plans/007-v0.3.0-ecosystem-governance.md) and [ADR-0007](decisions/0007-v0.3.0-public-governance-surface.md); at the latest evidence capture, [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6) head `de94f16b6b4aca62c3ef03b88e5b7ab8ab055d23` had [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319745) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319667) both conclude `success`. No v0.3.0 merge, tag, or Release is claimed yet.
- The v0.3.0 fresh-session E2E is still pending: the first isolated CLI attempt loaded the candidate but stopped at the host Windows sandbox helper (`helper_unknown_error: setup refresh had errors`) before generating files; no unrestricted retry was used.

## Known limits

- The E2E used a temporary local marketplace and temporary Plugin installation; both were removed after the test, while the local evidence was retained.
- The first releases intentionally do not include clean-room installation, Docker smoke testing, or release automation; those remain outside v0.2.0 and require a separate evidence-based decision.
- Remote Actions are verified as passing for the M1 PR head, merged `main` commits, the published `v0.1.1` and `v0.2.0` tags, the v0.2.0 candidate PR/push head, and the v0.3.0 candidate PR head; the v0.1.0 release metadata remains valid and unchanged.
- The current GitHub connector still cannot create Release objects; the owner-created public Release was verified through GitHub API and the public release page.
- The v0.1.0 Release metadata and tag target are valid; its body still contains historical pre-publication wording and should be cleaned up when Release-edit access is available.

## Next step

Complete owner review of the rendered v0.3.0 governance surface and the pending fresh-session E2E, then decide whether to merge [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6). Keep merge, tag, GitHub Release, and tag-triggered CI as separate checkpoints; until those are verified, keep `v0.2.0` as the stable install pin and rollback package. Keep the optional standard filename migration, clean-room installation, Docker smoke testing, release automation, and further infrastructure behind separate decisions.
