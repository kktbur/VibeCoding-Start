# Code Map

| Path | Role | Read when |
|---|---|---|
| `AGENTS.md` | Project-local Codex instructions and gate rules | Starting any task |
| `docs/INDEX.md` | Canonical project knowledge navigation | You need to find a document |
| `docs/PRODUCT.md` | Product intent, scope, non-goals, and risks | Clarifying what to build |
| `docs/ACCEPTANCE.md` | Machine and owner acceptance | Defining or checking success |
| `docs/CURRENT.md` | Active status and next step | Resuming work |
| `docs/standards/` | Normative standard and deployment mapping | Applying or auditing the plan |
| `docs/decisions/` | Material architecture/process decisions | Reviewing why a choice was made |
| `docs/plans/` | Staged implementation plans | Continuing unfinished work |
| `docs/worklog/` | Curated session summaries | Reviewing recent progress |
| `.project-memory/` | Cold raw history, evidence, and test artifacts | Investigating or reproducing a past result |
| `.agents/skills/project-knowledge/SKILL.md` | Reusable INIT/UPDATE/AUDIT workflow | Maintaining project knowledge |
| `.agents/skills/project-knowledge/references/` | Mode-specific guidance | Need detailed rules |
| `.agents/skills/project-knowledge/templates/` | Starting templates for project docs and ADRs | Initializing another project |
| `.agents/skills/project-knowledge/scripts/` | Deterministic audit helpers | Verifying structure, links, or freshness |
| `.agents/skills/vibe-engineering-development-standard/SKILL.md` | Reusable Vibe Engineering workflow and G0-G9 gates | Applying the standard to a project |
| `.agents/skills/vibe-engineering-development-standard/references/standard-v1.2.md` | Verbatim supplied v1.2 plan | Checking normative source wording |
| `README.md` | Public package entry point and quick start | Using this repository from GitHub |
| `.github/workflows/standards-audit.yml` | Optional CI entry point | Running checks on GitHub |

The map must be updated when the source tree, scripts, or deployment paths change materially.

