# Project Instructions

## Project identity

This repository is the source and public package for VibeCoding Start: a skill-only Codex Plugin containing `vibecoding-start` and `vibecoding-project-knowledge`. The published `v0.2.0` release is the current stable package; the `v0.3.0` candidate adds user-facing Chinese guidance and public contribution/security entry points without adding infrastructure.

## First-read order

At the start of a task, read in this order:

1. `docs/INDEX.md`
2. `docs/CURRENT.md`
3. `docs/PRODUCT.md`
4. `docs/PRD.md`
5. `docs/ACCEPTANCE.md`

Read `docs/CODEMAP.md`, active ADRs, plans, worklogs, standards, tests, and package files only when the task needs them.

## Artifact location and privacy

All transition files, temporary outputs, test artifacts, and final results for this project stay under the project directory. Raw sessions, command output, investigations, failed attempts, and test artifacts belong in local `.project-memory/`, which is ignored by Git except for its boundary `README.md`. Publish only redacted examples under `docs/examples/`.

Never store API keys, tokens, cookies, private keys, passwords, or unnecessary personal data in the repository, raw memory, screenshots, or logs. Preserve local raw history; do not rewrite Git history unless a real secret exposure requires a separately approved remediation.

## Engineering rules

- Document intent before implementation: problem, users, current state, desired state, requirements, non-goals, constraints, risks, and acceptance.
- Search for an existing project capability, standard library, official SDK/API/tool, mature open-source project, package, adapter, or composition before building a general capability.
- If a material capability is built instead of reused, record alternatives, rejection reasons, maintenance cost, and acceptance in an ADR.
- Keep changes small and verifiable. Do not add speculative frameworks, abstractions, dependencies, or infrastructure.
- Separate implementation from independent review. The author must not be the final reviewer for an important change.
- Test normal, error, boundary, invalid-input, regression, and recovery paths in proportion to risk.
- Every completion claim requires machine evidence, a plain-language explanation, and an owner acceptance method.
- Record version, last-known-good state, backup, rollback, and migration risk before release.

## Engineering gates

Use the common language even when a gate is lightweight:

```text
G0 Scope → G1 Intent → G2 Reuse → G3 Plan → G4 Build
→ G5 Adversarial Review → G6 Verification → G7 Human Acceptance
→ G8 Release → G9 Observation
```

## Local checks

Use PowerShell 7 explicitly. Run checks from the repository root with the configured Python runtime:

```text
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\audit_docs.py" .'
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\check_links.py" .'
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\detect_stale_docs.py" . --max-age-days 30'
pwsh -NoProfile -Command '& python "tests\validate_plugin.py" "plugins\vibecoding-start" --marketplace ".agents\plugins\marketplace.json"'
pwsh -NoProfile -Command '& python "tests\test_project_knowledge.py"'
pwsh -NoProfile -Command '& python "tests\test_public_examples.py"'
pwsh -NoProfile -Command '& python "tests\test_readme_navigation.py"'
pwsh -NoProfile -Command '& python "tests\test_governance_docs.py"'
pwsh -NoProfile -Command '& python "tests\test_small_path_contract.py"'
pwsh -NoProfile -Command '& python "tests\test_version_consistency.py"'
pwsh -NoProfile -Command '& python "tests\check_version_consistency.py"'
pwsh -NoProfile -Command '& python "tests\check_line_endings.py" .'
pwsh -NoProfile -Command '& python "tests\check_name_drift.py" .'
pwsh -NoProfile -Command '& python -m compileall -q "plugins\vibecoding-start\skills"'
```

Use `--as-of YYYY-MM-DD` only for deterministic fixture checks, not for the normal freshness command.

On macOS or Linux, run the equivalent checks from the repository root with Python 3:

```sh
bash scripts/check.sh

python3 tests/validate_plugin.py plugins/vibecoding-start --marketplace .agents/plugins/marketplace.json
python3 tests/test_project_knowledge.py
python3 tests/test_public_examples.py
python3 tests/test_readme_navigation.py
python3 tests/test_governance_docs.py
python3 tests/test_small_path_contract.py
python3 tests/test_version_consistency.py
python3 tests/check_line_endings.py .
python3 tests/check_name_drift.py .
python3 -m compileall -q plugins/vibecoding-start/skills
python3 plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/audit_docs.py .
python3 plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/check_links.py .
python3 plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/detect_stale_docs.py . --max-age-days 30
```

## Code review rules

- Review the diff against `docs/PRODUCT.md`, `docs/PRD.md`, `docs/ACCEPTANCE.md`, the active v1.3 standard, and active ADRs.
- Flag scope drift, duplicated Skill sources, unjustified complexity, missing failure/recovery tests, secret exposure, stale documentation, broken links, name drift, and changes without a rollback path.
- Treat a green automated check as evidence for that check only; do not convert it into a blanket correctness claim.
