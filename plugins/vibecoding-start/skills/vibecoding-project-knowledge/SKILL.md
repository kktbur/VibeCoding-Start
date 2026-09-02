---
name: vibecoding-project-knowledge
description: "Initialize, update, and audit a project's indexed intent, PRD, acceptance, current state, code map, decisions, evidence, and work history. Use when establishing project knowledge or maintaining it after a substantive session; normally coordinate it through vibecoding-start."
---

# VibeCoding Project Knowledge

Keep a project's active truth, decisions, structure, history, and acceptance navigable from one index without turning the workflow into a database or documentation platform.

## Operating boundary

- Work inside the active project root. Preserve valid documentation and connect it from `docs/INDEX.md` instead of creating duplicate sources of truth.
- Every project starts with `AGENTS.md` and six core documents: `docs/INDEX.md`, `PRODUCT.md`, `PRD.md`, `ACCEPTANCE.md`, `CURRENT.md`, and `CODEMAP.md`.
- Keep transition files, raw sessions, evidence, failed attempts, investigations, logs, and test artifacts below the project root.
- `.project-memory/` is local by default and must be ignored by Git except for an optional boundary `README.md`. Publish only intentionally redacted examples under `docs/examples/`.
- Never delete or irreversibly compress raw history merely to make a summary shorter. Curate active truth separately.
- Do not claim completion without machine evidence, a human-readable explanation, and an owner acceptance method.
- This Skill governs Markdown, Git history, and deterministic checks. It does not create a memory database, vector database, search engine, CI platform, deployment engine, testing framework, or observability backend.

## INIT

Use for the first formal development session in a project:

1. Inspect `AGENTS.md`, `README*`, `docs/`, source, tests, CI, and any existing architecture or decision records.
2. Preserve valid existing documents and connect them from `docs/INDEX.md`.
3. Create or complete the six-document skeleton, keeping each document as short as the project allows.
4. Create `.project-memory/README.md` to explain the local-only raw-history boundary; do not populate speculative empty directories.
5. Add `decisions/`, `plans/`, `worklog/`, architecture, testing, operations, release, or incident records only when complexity and risk justify them.
6. Record the initial deployment in a worklog and create an ADR when a material architecture, security, dependency, or release choice was made.

The Hot Context read order is `AGENTS.md`, `docs/INDEX.md`, `docs/CURRENT.md`, `docs/PRODUCT.md`, `docs/PRD.md`, and `docs/ACCEPTANCE.md`. Read `CODEMAP.md` and warm records when needed.

## UPDATE

Use after a substantive session or meaningful change:

1. Preserve raw session details, relevant command output, and test artifacts locally under `.project-memory/`; redact secrets and personal data before retaining them.
2. Curate durable facts into `CURRENT.md`, the relevant active document, and `CODEMAP.md`.
3. If the session changes a requirement, feature, non-goal, constraint, or meaningful user scenario, update `PRD.md` and its acceptance implications.
4. Record material choices in `docs/decisions/` and summarize the useful explanation, rejected approaches, verification, result, and next step in `docs/worklog/`.
5. Update `docs/INDEX.md` whenever navigation, status, or source-of-truth locations change.
6. Promote only redacted, deliberately reusable examples from raw memory into `docs/examples/`.

## AUDIT

Run after major changes or on a regular cadence. Check:

- all six core documents exist and are non-empty;
- `PRD.md` is linked from `docs/INDEX.md` and is not obviously disconnected from `ACCEPTANCE.md`;
- indexes resolve and important active documents are reachable;
- `CURRENT.md` has a recent update date and does not cite cancelled requirements as current truth;
- active ADRs do not contradict the current product, PRD, acceptance, or code map;
- `CODEMAP.md` and the actual source tree are not obviously out of sync;
- raw local history contains no credentials, tokens, cookies, private keys, or unredacted personal data;
- plugin and Skill names remain consistent after a rename.

Use the bundled scripts when applicable:

```text
scripts/audit_docs.py <project-root>
scripts/check_links.py <project-root>
scripts/detect_stale_docs.py <project-root> --max-age-days 30
```

Read only the supporting reference needed for the current mode:

- `references/document-layout.md` — Hot/Warm/Cold layout and artifact locations.
- `references/indexing-rules.md` — index, links, statuses, and source-of-truth rules.
- `references/adr-rules.md` — when and how to create an ADR.
- `references/session-memory.md` — raw history, redaction, promotion, and local-only defaults.
- `references/scaling-rules.md` — Small/Medium/Large depth and gate strength.
