# ADR-0006: Small-Project Gate Depth and Release Boundary

- Status: ACTIVE
- Date: 2026-09-05
- Scope: v0.2.0 release-candidate preparation

## Context

The M2 documentation foundation is merged into the public repository. The original roadmap also requires a concrete short path for genuinely small local tools and a final cross-reference check before the `v0.2.0` release. A qualitative Small/Medium/Large description alone leaves too much room for either skipped documents or unnecessary large-project ceremony.

## Decision

- Put the normative ten-gate depth matrix and the Small-project hard constraints in the main `vibecoding-start` Skill.
- Put concrete Small-project artifact minimums and practical scaling guidance in the companion `scaling-rules.md` reference.
- Keep `vibecoding-start` as the normal entry point and let `vibecoding-project-knowledge` own `INIT`, `UPDATE`, and `AUDIT`; make that ownership explicit in both Skills.
- Protect the contract with a standard-library-only deterministic test.
- Prepare the package as `0.2.0`, but keep the stable README installation pin on the existing `v0.1.1` tag until a `v0.2.0` tag and Release are independently created and verified.

## Consequences

Small projects keep the required seven-file project skeleton while avoiding empty architecture, operations, or incident directories. Medium and Large projects can add depth when their actual persistence, integrations, or operational risk requires it. The release boundary remains honest: package readiness, merge, tag, Release, and tag-triggered CI are separate facts.

## Evidence

- [Plan 006](../plans/006-v0.2.0-release-candidate.md)
- [Small-project gate-depth test](../../tests/test_small_path_contract.py)
- [M2 public example](../examples/small-project/README.md)

