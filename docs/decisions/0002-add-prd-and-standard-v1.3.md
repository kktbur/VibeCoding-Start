# ADR-0002: Add PRD and Activate Standard v1.3

- Status: ACTIVE
- Date: 2026-09-03
- Supersedes: the v1.2 active interpretation for new work

## Context

The previous minimum skeleton separated product intent from acceptance but had no independent requirements document. The v0.1.0 plan requires `PRODUCT` → `PRD` → `ACCEPTANCE` to make requirements explicit without building a traceability platform.

## Options considered

1. Keep requirements mixed into `PRODUCT.md` or chat history.
2. Build a full requirement/code/test tracking system.
3. Add a short `docs/PRD.md`, a template, index/audit checks, and a focused v1.3 standard.

## Decision

Choose option 3. v1.2 remains as superseded history; v1.3 is the active standard and keeps requirement IDs optional in depth but available for traceable projects.

## Consequences

- New projects always have a short PRD.
- Small projects do not need a heavyweight traceability system.
- Existing v1.2 records remain readable and are not rewritten.

## Evidence

- [PRD](../PRD.md)
- [Active standard](../standards/standard-v1.3.md)
- [Acceptance criteria](../ACCEPTANCE.md)
