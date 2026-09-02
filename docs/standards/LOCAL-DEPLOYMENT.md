# Local Deployment Mapping

This file maps the supplied plan to the current project. It is an implementation record, not a replacement for the source plan.

| Plan requirement | Local implementation | Status |
|---|---|---|
| Project-local `AGENTS.md` | `AGENTS.md` | DEPLOYED |
| Minimum indexed document skeleton | `docs/INDEX.md`, `PRODUCT.md`, `ACCEPTANCE.md`, `CURRENT.md`, `CODEMAP.md` | DEPLOYED |
| Hot/Warm/Cold context | `docs/INDEX.md`, `.project-memory/` indexes, Skill reference | DEPLOYED |
| Project Knowledge Skill | `.agents/skills/project-knowledge/` | DEPLOYED |
| INIT / UPDATE / AUDIT modes | `SKILL.md` | DEPLOYED |
| Document layout and indexing guidance | Skill `references/` | DEPLOYED |
| ADR governance | `docs/decisions/`, `references/adr-rules.md`, ADR-0001 | DEPLOYED |
| Staged plans and worklog | `docs/plans/`, `docs/worklog/` | DEPLOYED |
| Raw sessions and evidence | `.project-memory/sessions/`, `evidence/`, `failed-attempts/`, `test-artifacts/` | DEPLOYED |
| Deterministic document checks | `scripts/audit_docs.py`, `check_links.py`, `detect_stale_docs.py` | DEPLOYED |
| Git-backed history | Local repository on `main` | DEPLOYED |
| GitHub Actions integration point | `.github/workflows/standards-audit.yml` | PREPARED; no remote configured |
| Global Codex policy | Concise section appended to existing global `AGENTS.md`; project rules remain local and more specific | DEPLOYED |
| User-level Skill installation | User-level Codex skills directory | INSTALLED; owner confirmed fresh-session discovery |

## Reuse decision

The implementation is intentionally thin. It uses Codex's existing `AGENTS.md` and local Skill discovery, ordinary Markdown, Git, Python standard library, and GitHub Actions rather than adding a new platform or database.

## Verification boundary

The scripts prove document-structure invariants only. They do not prove that a future application is correct, secure, performant, or suitable for release.

