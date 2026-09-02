# Vibe Engineering Development Standard v1.2

This document is the local normative summary of the supplied plan. The exact supplied source is preserved in [SOURCE-PLAN.md](SOURCE-PLAN.md).

## Goal

Every project should be indexable, recoverable, reviewable, verifiable, observable at the appropriate depth, and safely reversible. Chat history is useful context, not the only project record.

## Six highest principles

1. **Document before build.** Record intent, users, scope, non-goals, success, failure, and acceptance.
2. **Reuse before build.** Prefer existing project capability, standard library, official SDK/API/tool, mature open source, package, adapter, or composition before custom implementation.
3. **Adversarial review.** Important changes receive an independent review that looks for omissions, wrong assumptions, regressions, duplicated capability, over-design, boundary failures, data/security risks, test gaps, and rollback problems.
4. **Active counterexamples.** Cover normal, error, boundary, regression, invalid-input, and recovery paths; add integration, E2E, stress, concurrency, fuzz, property, fault-injection, recovery, or performance checks when risk requires them.
5. **Observable operation.** A real-use system should have an appropriate level of logs, error evidence, health checks, metrics, alerts, traces, and dashboards.
6. **Progressive release and rollback.** Move from local to tested to beta/small scope to observed to stable; record the current version, last-known-good version, backup, rollback, and data recovery path.

## Four governance layers

```text
Global AGENTS
→ cross-project rules

Engineering Skills
→ repeatable execution

Project AGENTS
→ current project instructions and navigation

Project Knowledge
→ facts, history, decisions, evidence, and acceptance
```

This deployment keeps the existing global file intact and makes the current project rules explicit in its own `AGENTS.md`.

## Minimum project skeleton

```text
PROJECT/
├── AGENTS.md
├── docs/
│   ├── INDEX.md
│   ├── PRODUCT.md
│   ├── ACCEPTANCE.md
│   ├── CURRENT.md
│   └── CODEMAP.md
└── .project-memory/
```

The content depth scales with risk. A Small project stays short; a Medium project adds decisions, plans, worklogs, and session memory; a Large project adds architecture, testing, operations, release, incidents, investigations, and richer evidence.

## Context temperatures

- **Hot:** `AGENTS.md`, `docs/INDEX.md`, `CURRENT.md`, `PRODUCT.md`, `ACCEPTANCE.md`.
- **Warm:** code map, standards, ADRs, plans, worklogs, testing, operations, and release notes as needed.
- **Cold:** raw sessions, investigations, failed attempts, evidence, and test artifacts under `.project-memory/`.

Curated knowledge can be shortened; raw history and evidence must not be irreversibly lost. Active truth outranks historical records and chat history.

## Engineering gates

```text
G0 Scope
→ G1 Intent
→ G2 Reuse
→ G3 Plan
→ G4 Build
→ G5 Adversarial Review
→ G6 Verification
→ G7 Human Acceptance
→ G8 Release
→ G9 Observation
```

Gate strength is risk-adjusted, but the vocabulary remains consistent. Important changes must provide both machine evidence and owner-readable evidence.

## Knowledge modes

- **INIT:** inspect and preserve existing knowledge, establish the minimum skeleton, populate intent/acceptance/current/code map, and index it.
- **UPDATE:** preserve the raw session, curate current state, update active documents, record material decisions, update the code map and index.
- **AUDIT:** check required files, links, isolated documents, current freshness, ADR conflicts, code-map drift, and whether raw history contains knowledge that should be promoted.

## Thin implementation boundary

The deployment uses Markdown, Git, Codex repository reading, and small deterministic scripts. It does not implement a memory engine, search engine, verifier platform, deployment engine, CI service, or observability backend.

