# ADR-0001: Adopt the Local Vibe Engineering Development Standard

- Status: ACTIVE
- Date: 2026-09-02
- Owners: Project Owner and Codex

## Context

The project needs a repeatable way to preserve intent, current state, decisions, evidence, and acceptance across Codex sessions. The supplied plan requires a uniform minimum document skeleton, adaptive depth, reuse-before-build, independent review, risk-based verification, and rollback-aware release language.

## Options considered

1. Keep the standard only in chat history or a README.
2. Build a custom documentation/memory/search platform.
3. Use a thin, project-local `AGENTS.md`, indexed Markdown, Git, a repo-local Skill, and deterministic checks.

## Decision

Adopt option 3. Every project task in this directory begins from `docs/INDEX.md` and the Hot Context documents. The current `vibecoding-project-knowledge` Skill provides INIT, UPDATE, and AUDIT modes inside the Skill-only Plugin. Raw history remains local under `.project-memory/`; durable facts and decisions are curated into active documents.

## Consequences

- Positive: future sessions have a predictable entry point and can distinguish active truth from history.
- Positive: checks are local, deterministic, and dependency-light.
- Cost: contributors must update knowledge after substantive work.
- Cost: the checks do not prove application correctness; owner acceptance and risk-appropriate testing remain necessary.
- Boundary: the existing global Codex `AGENTS.md` is not overwritten; this project uses a project-local instruction layer.

## Evidence and links

- [Supplied source plan](../standards/SOURCE-PLAN.md)
- [Local deployment mapping](../standards/LOCAL-DEPLOYMENT.md)
- [External sources](../references/SOURCES.md)
