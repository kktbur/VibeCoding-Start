# ADR-0003: Package a Skill-only Plugin and Rename the Skills

- Status: ACTIVE
- Date: 2026-09-03

## Context

The prior repository exposed two maintained sources under a repository-local Skill directory. Public distribution needs one installable unit, a stable brand, and a namespace unlikely to collide with unrelated Skills.

## Options considered

1. Keep repository-local sources as the public package and document manual copying.
2. Maintain both repository-local and Plugin copies.
3. Make `plugins/vibecoding-start/` the sole source of truth for a Skill-only Plugin containing `vibecoding-start` and `vibecoding-project-knowledge`.

## Decision

Choose option 3. The main Skill allows implicit invocation; the companion Skill is explicit-only and is coordinated by the main workflow. The repository marketplace points to the Plugin root.

## Consequences

- Contributors edit one package source.
- Existing public history retains the prior layout, but active files and names no longer drift.
- Installation requires a fresh Codex session and a configured Plugin marketplace.

## Evidence

- [Plugin manifest](../../plugins/vibecoding-start/.codex-plugin/plugin.json)
- [Main Skill](../../plugins/vibecoding-start/skills/vibecoding-start/SKILL.md)
- [Companion Skill](../../plugins/vibecoding-start/skills/vibecoding-project-knowledge/SKILL.md)
