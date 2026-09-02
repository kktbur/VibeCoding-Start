# Product Definition

## Problem

Software projects started in Codex can lose intent, decisions, evidence, and current state when those facts exist only in chat history. The supplied Vibe Engineering Development Standard v1.2 defines a repeatable local structure to make each project indexable, recoverable, reviewable, verifiable, and rollback-aware from its first day.

## Owner and users

- Owner: Product Owner of this local project.
- Primary user: the project owner working with Codex.
- Secondary users: future Codex sessions or reviewers who need to understand the project without replaying the entire chat.

## Desired outcome

Provide one project-local knowledge entry point, reusable `project-knowledge` and Vibe Engineering Standard Skills, lightweight engineering gates, preserved raw evidence, deterministic checks, and a public GitHub package that makes the standard reusable and auditable.

## In scope

- Project-level `AGENTS.md` and indexed Hot/Warm/Cold documentation.
- A repo-local `.agents/skills/project-knowledge` Skill with INIT, UPDATE, and AUDIT modes.
- A repo-local `.agents/skills/vibe-engineering-development-standard` Skill that turns the supplied v1.2 plan into an operational workflow, with the exact plan preserved as a reference.
- Templates and deterministic checks for required documents, links, and stale current-state data.
- Git history initialized for this project and a GitHub Actions workflow that can run the checks if the repository is later hosted on GitHub.
- Publication of this package to the explicitly requested public repository `kktbur/VibeCoding-Start`.
- A traceable record of the supplied plan and the external sources used to validate the deployment shape.

## Non-goals

- Building a memory database, vector database, search engine, documentation platform, deployment engine, observability backend, or custom CI server.
- Automatically publishing future changes without a new explicit request.
- Overwriting the existing global Codex `AGENTS.md`.
- Claiming that documentation checks prove application correctness; they only prove the checked invariants.

## Risks

- The project is now published to the requested public repository; GitHub Actions is present but its execution status depends on the remote workflow run.
- Codex instruction discovery can depend on the current working directory and the next session restart; the project-local file is the source for this project.
- Documentation can drift from future code unless the UPDATE and AUDIT modes are used at the end of substantive work.
- The public repository contains the standard package and project documentation; future changes must retain the same evidence and rollback discipline.

