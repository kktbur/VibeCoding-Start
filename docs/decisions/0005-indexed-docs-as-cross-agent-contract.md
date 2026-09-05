# ADR-0005: Use Indexed Project Documents as the Cross-Agent Contract

- Status: ACTIVE
- Date: 2026-09-05

## Context

The owner wants VibeCoding Start to support a practical handoff between coding agents while preserving the local-first privacy boundary. A runtime coordination service would add infrastructure and a new failure surface that the Plugin does not need.

## Constraints

- Keep the Plugin Skill-only.
- Keep durable project truth inspectable in the repository.
- Keep raw sessions and credentials out of public files.
- Make handoffs usable by an agent that did not see the previous chat.

## Options considered

1. Rely on chat history or hidden agent memory.
2. Add an MCP/App-backed coordination service.
3. Use indexed project documents, reviewable Git changes, and a short handoff template.

## Decision

Choose option 3. `AGENTS.md`, `docs/INDEX.md`, the Hot Context documents, plans, ADRs, `CODEMAP.md`, worklogs, and reviewable Git history form the cross-Agent contract. The contract is explicit and repository-local; it is not a claim of native runtime communication between agents.

## Consequences

- A new agent can resume from durable project facts instead of replaying chat.
- Owners can inspect, review, revert, or transfer a handoff through normal repository artifacts.
- Agents must update the indexed documents when a material change alters current truth.
- Real-time coordination, shared hidden memory, and external orchestration remain out of scope.

## Evidence

- [Cross-Agent usage notes](../CROSS-AGENT.md)
- [Project knowledge index](../INDEX.md)
- [Active project state](../CURRENT.md)

