# Code Map

| Path | Role | Read when |
|---|---|---|
| `AGENTS.md` | Repository instructions, privacy boundary, and local checks | Starting any task |
| `docs/INDEX.md` | Canonical project knowledge navigation | Finding the right document |
| `docs/PRODUCT.md` | Product intent, scope, and non-goals | Clarifying why this exists |
| `docs/PRD.md` | v0.1.0 requirements and constraints | Checking what must be delivered |
| `docs/ACCEPTANCE.md` | Machine, owner, release, and recovery criteria | Checking proof and readiness |
| `docs/CURRENT.md` | Active state, limits, evidence, and next step | Resuming work |
| `docs/standards/` | Active v1.3 standard and superseded v1.2 history | Checking normative rules |
| `docs/decisions/` | Material process and package decisions | Understanding why a choice was made |
| `docs/plans/` | Staged implementation and release plan | Continuing the refactor |
| `docs/worklog/` | Curated session summaries | Reviewing recent work |
| `docs/examples/` | Redacted public examples | Explaining reusable patterns |
| `plugins/vibecoding-start/.codex-plugin/plugin.json` | Installable Plugin manifest | Validating distribution metadata |
| `plugins/vibecoding-start/skills/vibecoding-start/` | Main workflow Skill and UI metadata | Applying G0-G9 |
| `plugins/vibecoding-start/skills/vibecoding-project-knowledge/` | Companion INIT/UPDATE/AUDIT Skill, v1.3 reference, templates, and scripts | Maintaining project knowledge |
| `.agents/plugins/marketplace.json` | Repo-local marketplace catalog | Adding the Plugin to a Codex marketplace |
| `.github/workflows/standards-audit.yml` | Curated-document CI checks | Reviewing standard repository health |
| `.github/workflows/plugin-validation.yml` | Plugin, fixture, name, and Python validation | Reviewing package readiness |
| `tests/` | Standard-library validation scripts and fixtures | Running deterministic tests |
| `.project-memory/README.md` | Local raw-memory publication boundary | Checking privacy rules |

The active Skill source of truth is `plugins/vibecoding-start/skills/`. Do not recreate a second maintained copy under `.agents/skills/`.
