# Local Deployment Mapping

This file maps the v0.1.0 refactor plan to the current repository. The active package source is the Plugin tree; local raw memory is intentionally outside the public Git tree.

| Requirement | Implementation | Status |
|---|---|---|
| PRD-driven knowledge | `docs/PRD.md`, its template, indexes, and audit contract | IMPLEMENTED |
| Active standard | `docs/standards/standard-v1.3.md` and packaged `references/standard-v1.3.md` | IMPLEMENTED |
| v1.2 history | `docs/standards/VIBE-ENGINEERING-DEVELOPMENT-STANDARD-v1.2.md` and `SOURCE-PLAN.md` | PRESERVED; SUPERSEDED |
| Main Skill | `plugins/vibecoding-start/skills/vibecoding-start/` | IMPLEMENTED |
| Project Knowledge Skill | `plugins/vibecoding-start/skills/vibecoding-project-knowledge/` | IMPLEMENTED |
| Single source of truth | No maintained `.agents/skills/` copies | IMPLEMENTED |
| Plugin manifest | `plugins/vibecoding-start/.codex-plugin/plugin.json` | IMPLEMENTED |
| Repo marketplace | `.agents/plugins/marketplace.json` | IMPLEMENTED |
| Raw memory privacy | `.gitignore` plus `.project-memory/README.md` | IMPLEMENTED; raw records remain local and are absent from the public tree |
| Redacted example | `docs/examples/project-memory/README.md` | IMPLEMENTED |
| License | `LICENSE` | IMPLEMENTED; MIT |
| Product README | `README.md` | IMPLEMENTED |
| Document checks | `audit_docs.py`, `check_links.py`, `detect_stale_docs.py` | UPDATED |
| Plugin checks | `tests/validate_plugin.py`, fixture tests, name-drift check, `compileall` | IMPLEMENTED |
| CI | `standards-audit.yml`, `plugin-validation.yml` | IMPLEMENTED; PR #1 runs passed |
| End-to-end fresh-session install | Isolated local marketplace plus fresh Codex CLI session in an empty Git project; INIT/UPDATE/AUDIT and boundary checks passed | PASS |
| GitHub v0.1.0 Release | Tag and Release object | IMPLEMENTED; tag `v0.1.0` points to `48a14a8…` and the [GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.0) is published |
| v0.1.1 M1 maintenance | PR #2, active package version, audit fixtures, LF policy, and post-merge CI | IMPLEMENTED; merged at `38d8c07…`; [Plugin Validation #184](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806721) and [Standards Audit #229](https://github.com/kktbur/VibeCoding-Start/actions/runs/33953806729) passed |
| GitHub v0.1.1 Release | Tag and Release object | PUBLISHED; [`v0.1.1` tag and Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.1.1) target `main` at `f9367395e16af7a8acce57107087af8d3ae11b36`; tag-triggered CI #189/#234 passed |
| v0.2.0 M2 foundation | Bilingual README, small-project example, Cross-Agent notes, and deterministic example test | IMPLEMENTED; merged through PR #4 at `496e12b…`; post-merge Plugin Validation and Standards Audit passed |
| v0.2.0 release | Small/Medium/Large gate depth, Small-project hard constraints, cross-reference contract, version/changelog preparation | PUBLISHED; PR #5 merged at `994b121e1cff0b7eb514ce03ea79b83766d28c28`; [tag and Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.2.0) point to that commit; tag-triggered CI passed |
| v0.3.0 M3 governance candidate | Chinese user README, contributor/security entry points, Issue/PR templates, governance contract, and indexed state | IN PROGRESS; [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6) remains open; PR Plugin Validation and Standards Audit passed; safe isolated fresh-session E2E passed; owner review, merge, tag, Release, and tag-triggered CI remain pending |

Remote review: [PR #1](https://github.com/kktbur/VibeCoding-Start/pull/1), [PR #2](https://github.com/kktbur/VibeCoding-Start/pull/2), [PR #4](https://github.com/kktbur/VibeCoding-Start/pull/4), and [PR #5](https://github.com/kktbur/VibeCoding-Start/pull/5) are merged. The public `v0.2.0` tag and [GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases/tag/v0.2.0) target `994b121e1cff0b7eb514ce03ea79b83766d28c28`; tag-triggered [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703200) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33965703206) passed. [PR #6](https://github.com/kktbur/VibeCoding-Start/pull/6) remains the open v0.3.0 candidate; its recorded [Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319745) and [Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/runs/33969319667) passed, and the safe isolated fresh-session E2E also passed. The first releases deliberately exclude clean-room install, Docker smoke testing, and release automation. M1, G8, the M2 foundation, and the v0.2.0 release are complete; M3 remains active under Plan 007.

