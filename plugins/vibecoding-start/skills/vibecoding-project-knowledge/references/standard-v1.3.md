# Vibe Engineering Development Standard v1.3

- Status: ACTIVE
- Scope: reusable Codex workflow for software projects
- Supersedes: v1.2 for new work

## Purpose

Every project starts with a small, indexable knowledge system. The system grows in depth with risk and complexity, while raw project memory remains local by default. The workflow keeps AI-built software understandable, reusable, reviewable, verifiable, acceptable, releasable, and recoverable.

## Core documents

Every project has these documents from its first formal session:

```text
AGENTS.md
docs/INDEX.md
docs/PRODUCT.md
docs/PRD.md
docs/ACCEPTANCE.md
docs/CURRENT.md
docs/CODEMAP.md
```

Their responsibilities do not overlap:

| Document | Question answered |
|---|---|
| `PRODUCT.md` | Why are we doing this? |
| `PRD.md` | What must the product do? |
| `ACCEPTANCE.md` | How will we prove it? |
| `CURRENT.md` | Where are we now? |
| `CODEMAP.md` | Where does it live? |
| `INDEX.md` | Where should a reader go next? |

Small projects keep each document short. Medium and large projects add decisions, plans, worklogs, architecture, testing, operations, release, and incident records only when justified.

## Source-of-truth and context

Read the project index and Hot Context first. Drill into warm records only as needed. Keep raw sessions, evidence, failed attempts, investigations, logs, and test artifacts in local `.project-memory/` by default. `.gitignore` must prevent accidental publication; only redacted examples intentionally promoted to `docs/examples/` belong in a public repository.

Curated knowledge may be shortened. Raw history must not be irreversibly discarded merely to reduce context. Active product, PRD, acceptance, and ADR records outrank historical worklogs, raw sessions, and chat history.

## Engineering principles

1. Document intent before implementation.
2. Search for existing capabilities before building general-purpose code.
3. Penalize unnecessary complexity, dependencies, abstractions, and infrastructure.
4. Use an independent reviewer for important changes.
5. Seek counterexamples, not only happy-path confirmation.
6. Report machine evidence and owner-readable evidence together.
7. Release progressively and keep a rollback path.

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

### G0 — Scope

Classify work as application/product, integration/adapter, or infrastructure/security/runtime. Reuse and review requirements become stricter as work approaches lower-level infrastructure.

### G1 — Intent

Establish the chain:

```text
PRODUCT (Why) → PRD (What) → ACCEPTANCE (How to prove)
```

Record the problem, users, current state, desired state, requirements, non-goals, constraints, acceptance, and risks.

### G2 — Reuse

For non-trivial general capability, search in this order:

```text
USE → ADAPT → COMPOSE → BUILD → STOP
```

Prefer existing project capability, standard library, official SDK/API/tool, mature open source, established package, thin adapter, or composition. If BUILD wins, record alternatives, rejected reuse paths, maintenance costs, and owner acceptance in an ADR.

### G3 — Plan

Break complex work into milestones with verification after each one. Re-plan when scope or risk materially changes.

### G4 — Build

Make the smallest reversible implementation that meets the active PRD and acceptance criteria. Do not add speculative infrastructure.

### G5 — Adversarial review

An independent reviewer reads the relevant intent, PRD, acceptance, active decisions, code map, diff, and tests. Look for omissions, wrong assumptions, regression risk, duplicated capabilities, over-design, security/data risks, test gaps, and rollback failures. The author is not the final reviewer for an important change.

### G6 — Verification

Cover normal, error, boundary, invalid-input, regression, and recovery paths in proportion to risk. Add integration, E2E, stress, concurrency, fuzz, property, fault-injection, recovery, or performance checks only when their risk-reduction value justifies them.

### G7 — Human acceptance

The owner confirms that the product solves the intended problem and that observable behavior is understandable. Automated checks and independent review do not replace owner acceptance.

### G8 — Release

Record version, last-known-good state, release notes, backup, rollback, migration risk, and release target before real use.

### G9 — Observation

Observe the released system. If healthy, continue; if not, stop and roll back or roll forward. Feed evidence back into tests, worklogs, ADRs, product intent, acceptance, and postmortems.

## Knowledge lifecycle

Use the companion `vibecoding-project-knowledge` workflow:

- `INIT` establishes and indexes the six core documents while preserving existing valid knowledge.
- `UPDATE` preserves local raw history, curates active documents, updates the PRD when requirements change, records decisions, updates the code map, worklog, and indexes.
- `AUDIT` checks required documents, PRD/index/acceptance alignment, links, freshness, ADR conflicts, code-map drift, raw-memory privacy, and naming consistency.

## Distribution boundary

The public VibeCoding Start package is a Skill-only Plugin. The Plugin is the installable distribution unit; the two Skills are its reusable workflows. The repository keeps one source of truth under `plugins/vibecoding-start/skills/` and does not maintain copied Skill sources under a second directory.

This standard does not implement memory databases, vector databases, search engines, testing frameworks, deployment frameworks, CI services, observability backends, or a universal orchestrator.
