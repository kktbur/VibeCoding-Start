# Code Map

| Path | Role | Read when |
|---|---|---|
| `AGENTS.md` | Repository instructions, privacy boundary, and local checks | Starting any task |
| `docs/INDEX.md` | Canonical project knowledge navigation | Finding the right document |
| `docs/PRODUCT.md` | Product intent, scope, and non-goals | Clarifying why this exists |
| `docs/PRD.md` | Released v0.2.0 baseline and v0.3.0 governance candidate requirements | Checking what must be delivered |
| `docs/ACCEPTANCE.md` | Machine, owner, release, and recovery criteria | Checking proof and readiness |
| `docs/CURRENT.md` | Active state, limits, evidence, and next step | Resuming work |
| `docs/standards/` | Active v1.3 standard and superseded v1.2 history | Checking normative rules |
| `docs/decisions/` | Material process and package decisions | Understanding why a choice was made |
| `docs/plans/` | Staged implementation and release plan | Continuing the refactor |
| `docs/worklog/` | Curated session summaries | Reviewing recent work |
| `docs/examples/` | Redacted public examples, including the small-project skeleton | Explaining reusable patterns |
| `docs/CROSS-AGENT.md` | Repository-local handoff contract for coding agents | Resuming work in another agent |
| `README.zh-CN.md` | User-facing Chinese README; points to the English normative standard | Serving Chinese-speaking users |
| `CONTRIBUTING.md` | Contribution workflow, checks, review, rollback, and privacy rules | Preparing or reviewing a PR |
| `SECURITY.md` | Private vulnerability reporting and secret-handling policy | Reporting or triaging security concerns |
| `scripts/check.sh` | Unix-like wrapper for the standard-library repository checks | Running the complete local check set |
| `plugins/vibecoding-start/.codex-plugin/plugin.json` | Installable Plugin manifest | Validating distribution metadata |
| `plugins/vibecoding-start/skills/vibecoding-start/` | Main workflow Skill, gate-depth matrix, and UI metadata | Applying G0-G9 at the smallest justified depth |
| `plugins/vibecoding-start/skills/vibecoding-project-knowledge/` | Companion INIT/UPDATE/AUDIT Skill, v1.3 reference, templates, and scripts | Maintaining project knowledge |
| `.agents/plugins/marketplace.json` | Repo-local marketplace catalog | Adding the Plugin to a Codex marketplace |
| `.github/workflows/standards-audit.yml` | Curated-document CI checks | Reviewing standard repository health |
| `.github/workflows/plugin-validation.yml` | Plugin, fixture, name, and Python validation | Reviewing package readiness |
| `.github/ISSUE_TEMPLATE/` | Bug, Skill behavior, and documentation intake templates | Opening a safe public Issue |
| `.github/PULL_REQUEST_TEMPLATE.md` | Requirement traceability, verification, privacy, and rollback prompts | Opening a PR |
| `tests/check_version_consistency.py` | Plugin/CHANGELOG version contract | Checking release metadata |
| `tests/check_line_endings.py` | Tracked text-file LF contract | Checking cross-platform formatting |
| `tests/test_public_examples.py` | Small-project example skeleton check | Verifying the M2 public example |
| `tests/test_readme_navigation.py` | English-first bilingual README contract | Verifying language anchors and install paths |
| `tests/test_governance_docs.py` | Public governance file, language, template, and privacy contract | Verifying the v0.3.0 candidate |
| `tests/test_small_path_contract.py` | Small-project gate-depth contract | Verifying the M2 shortest path documentation |
| `tests/fixtures/` | Standard-library validation fixtures, including Chinese and ignore-rule variants | Running deterministic tests |
| `.project-memory/README.md` | Local raw-memory publication boundary | Checking privacy rules |

The active Skill source of truth is `plugins/vibecoding-start/skills/`. Do not recreate a second maintained copy under `.agents/skills/`.
