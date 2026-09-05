# Scaling Rules

Every project receives the same minimum skeleton. Complexity changes the depth of content and the strength of gates, not whether a project has knowledge files.

## Small

Use this path for a local, offline tool with no persistence or external service dependency. The minimum output is:

| Artifact | Small-path minimum |
|---|---|
| `AGENTS.md` | Short project rules, privacy boundary, and the checks needed to resume |
| `docs/INDEX.md` | Links to every active project document |
| `docs/PRODUCT.md` | Problem, intended user, and one or two non-goals |
| `docs/PRD.md` | One scenario, the smallest useful requirements, and constraints |
| `docs/ACCEPTANCE.md` | One normal-path check and one failure-path check |
| `docs/CURRENT.md` | Current state, last check, and next step |
| `docs/CODEMAP.md` | Where the source and documents live |

Keep each document short, but create all seven files. For G0-G9, use the Small column in the main Skill's gate matrix: search the standard library first, keep the diff small, verify one normal and one failure path, and record the version and rollback action. A plan may be summarized in `CURRENT.md` when the project is genuinely small; do not add `docs/plans/` only to imitate a larger project.

Do not create empty `docs/architecture/`, `docs/incidents/`, `docs/operations/`, or similar directories merely to look complete. Add an ADR only when a decision about reuse, behavior, acceptance, or rollback needs to remain durable.

## Medium

Use `docs/decisions/`, `docs/plans/`, and `docs/worklog/` when the project has multiple modules, persistence, external dependencies, or ongoing maintenance. Keep raw sessions and evidence local. Use fixtures and regression checks for behavior that is likely to drift.

## Large

Add architecture, testing, operations, release, incidents, investigations, failed-attempts, evidence, and test-artifact indexes when their current purpose is justified. Add independent review, integration/E2E, recovery, performance, and release gates according to risk.

Each added directory must have a current purpose and an index. The depth decision is evidence-driven; project size alone does not justify infrastructure.

