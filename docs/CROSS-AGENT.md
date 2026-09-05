# Cross-Agent Usage Notes

- Status: ACTIVE — M2 documentation contract
- Scope: Share project truth safely across coding agents without adding a runtime orchestrator.

## Purpose

Different coding agents can work on the same repository when they read and update the same indexed project documents. This document defines the handoff contract; it does not claim that agents share hidden memory, sessions, credentials, or a live coordination service.

## Read order

At the start of a task, read the repository instructions and active project truth in this order:

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/CURRENT.md`
4. `docs/PRODUCT.md`
5. `docs/PRD.md`
6. `docs/ACCEPTANCE.md`
7. The relevant plan, ADR, `CODEMAP.md`, worklog, and tests

The active documents describe the current project. Chat history and local raw sessions are supporting evidence, not the source of truth.

## Handoff contract

Every handoff should contain enough information for the next agent to resume without replaying the previous conversation:

```text
Task:
Scope:
Current state:
Requirements:
Files to inspect:
Decisions and rejected routes:
Verification already run:
Known risks:
Next safe action:
```

Use repository-relative paths in the handoff. Do not put tokens, cookies, private keys, passwords, or unnecessary personal data into the handoff.

## Change protocol

- Make the smallest change that satisfies the stated requirement.
- Update the PRD, plan, or acceptance mapping before a material scope change.
- Keep one branch or reviewable change per independent workstream when parallel work is used.
- Do not let one agent silently overwrite another agent's unreviewed changes.
- Run the checks appropriate to the risk, then request independent review for important changes.
- Use `UPDATE` to curate `CURRENT.md`, the relevant worklog, and structural documents before handing work back.
- Use `AUDIT` before claiming that the handoff is complete.

## Evidence boundary

Shared durable facts belong in `docs/`. Raw sessions, command output, failed attempts, investigations, and test artifacts remain local under `.project-memory/` by default. Publish only intentionally redacted examples under `docs/examples/`.

## What this does not provide

These notes do not create a message bus, task queue, shared vector store, MCP server, App integration, or universal agent orchestrator. Agents coordinate through the repository's explicit documents, branches, commits, pull requests, and owner decisions.

