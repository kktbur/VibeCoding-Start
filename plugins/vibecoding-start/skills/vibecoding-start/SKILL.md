---
name: vibecoding-start
description: "Apply a risk-scaled engineering workflow to AI-built software projects: establish indexed knowledge, write or update a PRD, reuse mature capabilities before custom code, run G0-G9 gates, obtain independent review, verify counterexamples, and release with rollback evidence. Use when starting a project, making a material change, or preparing an important release; do not use for a trivial edit with no project-state impact."
---

# VibeCoding Start

Use this Skill to give Codex a lightweight engineering system from the first project session through release and observation. The desired result is a project that a later session can understand, review, verify, accept, and safely continue without replaying the entire chat.

Do not invoke this workflow for a typo-only README edit or a color-only UI edit when the project state, behavior, and acceptance surface do not change. Make that surgical edit directly and keep the project gates out of the task.

## First action

Read the project's `AGENTS.md`, then follow this Hot Context order:

1. `docs/INDEX.md`
2. `docs/CURRENT.md`
3. `docs/PRODUCT.md`
4. `docs/PRD.md`
5. `docs/ACCEPTANCE.md`

Read `docs/CODEMAP.md`, active ADRs, plans, worklogs, standards, and local raw evidence only when the task needs them. If the six-document skeleton is missing, use the companion `vibecoding-project-knowledge` Skill's `INIT` mode before implementation.

## Non-negotiable project boundary

- Every project receives the same minimum skeleton: `AGENTS.md`, `docs/INDEX.md`, `PRODUCT.md`, `PRD.md`, `ACCEPTANCE.md`, `CURRENT.md`, and `CODEMAP.md`.
- Complexity changes document depth and gate strength; it does not remove the skeleton.
- `PRODUCT.md` explains why, `PRD.md` explains what, and `ACCEPTANCE.md` explains how to prove it. Do not silently merge these responsibilities.
- Update `PRD.md` when the session changes a requirement, feature, non-goal, constraint, or meaningful user scenario.
- Keep raw sessions, logs, failed attempts, investigations, and evidence local by default under `.project-memory/`. Promote only redacted, intentionally curated examples to `docs/examples/`.
- Prefer existing project capabilities, the standard library, official SDKs/APIs/tools, mature open-source projects, packages, adapters, or composition before custom infrastructure.
- Do not build a memory database, vector database, search engine, testing framework, deployment framework, CI service, or observability backend as part of this workflow.

## Engineering gates

Use the same vocabulary for every project while scaling the depth to risk:

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

### Scale the gates before applying them

Choose the smallest depth that matches the risk. A small local tool can keep every gate short, but it must not skip the project-document skeleton or invent empty governance directories.

| Gate | Small (local, offline, no persistence) | Medium | Large |
|---|---|---|---|
| G0 Scope | One sentence: application, not infrastructure | A paragraph | Explicit threat model |
| G1 Intent | All six documents; each may be under 30 lines | PRD with REQ IDs | Complete scenarios and non-goals |
| G2 Reuse | Search the standard library first; BUILD requires an ADR | ADR required | Compare multiple reuse paths |
| G3 Plan | May combine the plan with `CURRENT.md` in five lines | Use `docs/plans/` | Milestone-level acceptance |
| G4 Build | Small diff; no new framework | Clear module boundaries | Layered design |
| G5 Review | Author checklist; independent reviewer (not the author) for material changes; owner reads the diff | Independent reviewer | Independent reviewer plus security review |
| G6 Verify | One normal path and one failure path | Fixtures and regression checks | Recovery, boundary, and performance checks by risk |
| G7 Accept | Owner can restate the behavior | Check `ACCEPTANCE.md` | Explicit sign-off |
| G8 Release | Version, run instructions, last-known-good, release notes, backup/rollback, migration risk, and exact target | Backup and rollback | Migration plan |
| G9 Observe | Confirm it still opens and runs next time | Logs and metrics | Alerts and operational ownership |

For a Small project:

- Still create `AGENTS.md`, `docs/INDEX.md`, `docs/PRODUCT.md`, `docs/PRD.md`, `docs/ACCEPTANCE.md`, `docs/CURRENT.md`, and `docs/CODEMAP.md`, even when each file is short.
- Do not create empty `docs/architecture/`, `docs/incidents/`, `docs/operations/`, or similar directories merely to look complete.
- Keep the implementation diff small, prefer the standard library, and record only decisions that affect reuse, behavior, acceptance, or rollback.

### G0 Scope

Classify the work as application/product, integration/adapter, or infrastructure/security/runtime. The closer it is to infrastructure, the stronger the reuse, review, and recovery evidence must be.

### G1 Intent

Make the chain explicit:

```text
PRODUCT (Why) → PRD (What) → ACCEPTANCE (How to prove)
```

Record the problem, users, current and desired states, functional requirements, non-goals, constraints, acceptance, and risks before implementation.

### G2 Reuse

For any non-trivial general capability, search before building and decide in this order:

```text
USE → ADAPT → COMPOSE → BUILD → STOP
```

If BUILD is selected, record searched alternatives, rejected reuse paths, maintenance responsibility, and the owner's acceptance method in an ADR. A model's ability to write code is not evidence that custom code is the right choice.

### G3 Plan

Break complex work into small milestones with a verification point after each milestone. Stop and re-plan when scope, architecture, or risk changes materially.

### G4 Build

Keep implementation small and reversible. Use the existing toolchain and avoid speculative abstractions, dependencies, and infrastructure.

### G5 Adversarial Review

An independent reviewer examines `PRODUCT.md`, `PRD.md`, `ACCEPTANCE.md`, active decisions, relevant structure, the diff, and tests. Look for omissions, wrong assumptions, regressions, duplicated capability, over-design, security/data risks, test gaps, and rollback failures. The author must not be the final reviewer for an important change.

### G6 Verification

Cover normal, error, boundary, invalid-input, regression, and recovery paths in proportion to risk. Report machine evidence and an owner-readable explanation; a green check proves only the invariant that it actually checks.

### G7 Human Acceptance

The owner confirms that the result is the intended product and that its observable behavior is understandable. Automated checks and independent review do not replace this step.

### G8 Release

Record the version, last-known-good state, release notes, backup, rollback method, migration risk, and exact release target before real use.

### G9 Observation

After release, observe health and user evidence. Continue only when healthy; stop and roll back or roll forward when evidence shows a problem. Feed the result back into tests, worklog, ADR, product intent, acceptance, or a postmortem as appropriate.

## Knowledge closeout

At the end of every substantive session, use the companion `vibecoding-project-knowledge` Skill's `UPDATE` mode:

1. Preserve raw session details and large output in the local `.project-memory/` directory.
2. Curate `CURRENT.md` and the relevant active documents.
3. Update `CODEMAP.md` when structure changes.
4. Update `PRD.md` when requirements, features, non-goals, constraints, or user scenarios change.
5. Record material choices in an ADR.
6. Update indexes and the worklog.
7. Run the relevant deterministic audits.

Do not claim completion without machine evidence, a human-readable explanation, and an owner acceptance method.

## References

- Read [Standard v1.3](../vibecoding-project-knowledge/references/standard-v1.3.md) for the normative rules and release boundary.
- Read [scaling rules](../vibecoding-project-knowledge/references/scaling-rules.md) for the concrete Small/Medium/Large document depth and artifact minimums.
- Read the companion `vibecoding-project-knowledge` Skill for `INIT`, `UPDATE`, or `AUDIT` procedures.

