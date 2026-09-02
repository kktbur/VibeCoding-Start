# Project Instructions

## Project identity

This project deploys and maintains the local Vibe Engineering Development Standard v1.2. It is a thin, Markdown-and-Git governance layer with a repo-local `project-knowledge` Skill and deterministic document checks.

## First-read order

At the start of a task, read in this order:

1. `docs/INDEX.md`
2. `docs/CURRENT.md`
3. `docs/PRODUCT.md`
4. `docs/ACCEPTANCE.md`
5. `docs/CODEMAP.md`

Read ADRs, plans, worklogs, standards, and `.project-memory/` only when the task needs them.

## Artifact location

All transition files, temporary outputs, test artifacts, and final results for this project must stay under this project directory. Put large raw command/test output in `.project-memory/evidence/` and keep the human-readable conclusion in `docs/worklog/` or `docs/CURRENT.md`.

## Engineering rules

- Document intent before implementation: problem, users, current state, desired state, non-goals, risks, and acceptance.
- Search for an existing project capability, standard library, official SDK/API/tool, mature open-source project, or package before building a general-purpose capability.
- If a material capability is built instead of reused, record the alternatives, adaptation/composition options, maintenance cost, and acceptance method in an ADR.
- Keep changes small and verifiable. Do not add speculative frameworks, abstractions, dependencies, or infrastructure.
- Separate implementation from independent review. The author must not be the final reviewer for an important change.
- Test normal, error, boundary, regression, and recovery paths in proportion to risk.
- Every completion claim requires machine evidence, a plain-language explanation, and a user acceptance method.
- Record version, last-known-good state, backup, rollback, and migration risk before release.
- Preserve raw history and evidence. Curate summaries without deleting the source record.
- Never store API keys, tokens, cookies, private keys, or other secrets in the repository, logs, screenshots, or documents.

## Engineering gates

Use the common language even when a gate is lightweight:

```text
G0 Scope → G1 Intent → G2 Reuse → G3 Plan → G4 Build
→ G5 Adversarial Review → G6 Verification → G7 Human Acceptance
→ G8 Release → G9 Observation
```

For this standards project, run at least the document audit, link audit, and stale-current check after structural changes.

## Local commands

Use PowerShell 7 explicitly. Run the project checks from the repository root
with the Python runtime configured by the host:

```text
pwsh -NoProfile -Command '& python ".agents\skills\project-knowledge\scripts\audit_docs.py" .'
pwsh -NoProfile -Command '& python ".agents\skills\project-knowledge\scripts\check_links.py" .'
pwsh -NoProfile -Command '& python ".agents\skills\project-knowledge\scripts\detect_stale_docs.py" . --as-of 2026-09-02'
```

## Code Review Rules

- Review the diff against `PRODUCT.md`, `ACCEPTANCE.md`, and active ADRs.
- Flag scope drift, duplicated capabilities, unjustified complexity, missing failure/recovery tests, secret exposure, stale documentation, and changes without a rollback path.
- Treat a green automated check as evidence for that check only; do not convert it into a blanket correctness claim.

