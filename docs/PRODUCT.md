# Product Definition

## Problem

AI-assisted projects can accumulate code faster than they preserve intent, requirements, decisions, evidence, and current state. The result is difficult for both the owner and a later Codex session to understand, review, verify, or safely change.

## Users and owner

- Owner: the maintainer of VibeCoding Start.
- Primary users: people using Codex to build and maintain software.
- Secondary users: future Codex sessions, reviewers, and contributors who need a concise project map.

## Desired outcome

VibeCoding Start should be a small, installable, reusable Codex Plugin that gives AI-built projects a uniform knowledge entry point, a PRD-driven workflow, reuse-before-build decisions, independent review, counterexample-focused verification, human acceptance, and rollback-aware release.

## In scope

- A Skill-only Plugin named `vibecoding-start`.
- A companion Skill named `vibecoding-project-knowledge` for INIT, UPDATE, and AUDIT.
- Vibe Engineering Development Standard v1.3 as the active normative reference, with v1.2 retained as superseded history.
- Six core project documents: `INDEX`, `PRODUCT`, `PRD`, `ACCEPTANCE`, `CURRENT`, and `CODEMAP`.
- Local-first raw project memory with intentionally redacted public examples.
- MIT licensing, a product-oriented README, deterministic package/document checks, and a GitHub Actions validation path.

## Non-goals

- Memory databases, vector databases, search engines, custom testing frameworks, deployment frameworks, observability backends, MCP servers, or a universal orchestrator.
- Maintaining copied Skill sources under both `.agents/skills/` and the Plugin package.
- Claiming that documentation or package checks prove an application is correct.
- Publishing private raw sessions or automatically publishing future repository changes.

## Risks

- Plugin installation behavior can vary by Codex host and requires a fresh session after installation or update.
- Existing public history contains the earlier repository-local layout; the active source of truth moves to `plugins/vibecoding-start/` without rewriting history.
- Raw memory previously tracked in the repository must be removed from the current tree while being preserved locally; history rewrite is reserved for confirmed secret exposure.
- A GitHub Actions workflow can be present and syntactically valid without its remote run having completed; remote execution must be verified separately.
