---
name: project-knowledge
description: "Initialize, update, and audit a repository's indexed project knowledge, engineering decisions, evidence, and current state. Use when starting a project, completing a substantial session, changing architecture, or checking documentation drift."
---

# Project Knowledge

Use this skill to keep project intent, acceptance, current state, code structure, decisions, plans, worklogs, and raw evidence navigable from one index.

## Operating boundary

- Work inside the active project root. Preserve existing valid documentation and connect it from `docs/INDEX.md` instead of creating duplicate sources of truth.
- Keep transition files, raw evidence, and result artifacts inside the project directory unless the user explicitly requests another destination.
- Do not delete or irreversibly compress raw sessions, investigations, failed attempts, evidence, or test artifacts.
- Do not claim completion without machine evidence, a human-readable explanation, and an owner acceptance method.
- This skill governs Markdown, Git history, and deterministic checks. It does not create a memory database, vector database, search engine, CI platform, deployment engine, or observability backend.

## Modes

### INIT

Use for the first formal development session in a project.

1. Identify the project root and inspect existing `AGENTS.md`, `README*`, `docs/`, source, tests, and CI files.
2. Preserve valid existing documents and link them from the project index.
3. Ensure the minimum skeleton exists: `AGENTS.md`, `docs/INDEX.md`, `PRODUCT.md`, `ACCEPTANCE.md`, `CURRENT.md`, and `CODEMAP.md`.
4. Add only the scaling directories justified by project complexity.
5. Record the initial deployment in a worklog and, when a material architecture or process choice was made, an ADR.

### UPDATE

Use after a substantial session or a meaningful change.

1. Save raw session details and large command/test output under `.project-memory/`.
2. Curate durable facts into `CURRENT.md`, the relevant active document, and `CODEMAP.md`.
3. Record material choices in `docs/decisions/` and summarize the session in `docs/worklog/`.
4. Update `docs/INDEX.md` whenever navigation or document status changes.

### AUDIT

Run after major changes or on a regular cadence.

- Required project documents exist and are non-empty.
- Index links resolve and important documents are not isolated.
- `CURRENT.md` has a recent update date.
- Active ADRs do not contradict the current project truth.
- `CODEMAP.md` and the actual source tree are not obviously out of sync.
- Raw history contains no credentials or unredacted secrets.

Use the bundled scripts when applicable:

```text
scripts/audit_docs.py <project-root>
scripts/check_links.py <project-root>
scripts/detect_stale_docs.py <project-root>
```

Read the supporting reference only when the task needs it:

- `references/document-layout.md` — Hot/Warm/Cold layout and artifact locations.
- `references/indexing-rules.md` — index, links, statuses, and source-of-truth rules.
- `references/adr-rules.md` — when and how to create an ADR.
- `references/session-memory.md` — raw history, evidence, redaction, and update flow.
- `references/scaling-rules.md` — Small/Medium/Large depth and gate strength.

