# Scaling Rules

Every project receives the same minimum skeleton. Complexity changes the depth of content and the strength of gates, not whether a project has knowledge files.

## Small

Use the six core documents and a short `AGENTS.md`. A short PRD and a few acceptance checks are enough. Add only the directories needed for the current work.

## Medium

Add `docs/decisions/`, `docs/plans/`, and `docs/worklog/` when the project has multiple modules, persistence, external dependencies, or ongoing maintenance. Keep raw sessions and evidence local.

## Large

Add architecture, testing, operations, release, incidents, investigations, failed-attempts, evidence, and test-artifact indexes. Add independent review, integration/E2E, recovery, performance, and release gates according to risk.

Do not create empty directories merely to look complete. Each added directory must have a current purpose and an index.
