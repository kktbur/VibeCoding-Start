# v0.1.0 Deployment Mapping

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
| End-to-end fresh-session install | Codex Plugin installation in a temporary project | OWNER/ENVIRONMENT TEST PENDING |
| GitHub v0.1.0 Release | Tag and Release object | PENDING owner acceptance |

Remote review: [PR #1](https://github.com/kktbur/VibeCoding-Start/pull/1) is open from `release/v0.1.0` to `main`; both configured GitHub Actions checks passed for its current head.
