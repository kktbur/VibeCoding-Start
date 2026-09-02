# VibeCoding-Start

`VibeCoding-Start` packages the Vibe Engineering Development Standard v1.2 as a reusable, repository-local Codex Skill.

Public repository: [github.com/kktbur/VibeCoding-Start](https://github.com/kktbur/VibeCoding-Start)

## What this repository provides

- `.agents/skills/vibe-engineering-development-standard/SKILL.md` — the concise operational entry point.
- `.agents/skills/vibe-engineering-development-standard/references/standard-v1.2.md` — the supplied plan preserved verbatim.
- `.agents/skills/project-knowledge/` — the indexed project-knowledge workflow used by this repository.
- `docs/` and `.project-memory/` — the project's active knowledge, decisions, work history, and evidence.

The Skill applies indexed project knowledge, risk-scaled documentation, G0-G9 engineering gates, reuse-before-build decisions, independent review, evidence-based verification, human acceptance, rollback-aware release, and post-release observation.

## Quick start

1. Clone or copy this repository into the project that should use the standard.
2. Keep the Skill under the project's `.agents/skills/` directory so Codex can discover it as a repository Skill.
3. In Codex, explicitly invoke `$vibe-engineering-development-standard`, or let Codex select it when the request matches its description.
4. At project start, use the `INIT` workflow; after a substantive session, use `UPDATE`; after a material change, use `AUDIT`.

The Skill is intentionally repository-local and does not require a custom memory database, search engine, testing framework, deployment engine, or observability backend.

## Source and maintenance

The normative source is [Vibe Engineering Development Standard v1.2](docs/standards/SOURCE-PLAN.md). The public Skill entry point is kept short and routes detailed wording to its reference file, following the [Codex Agent Skills documentation](https://developers.openai.com/codex/skills).

When the standard changes, update the verbatim reference, revise the operational entry point only where the workflow changes, run the Skill and project audits, record the change in `docs/`, and preserve the previous evidence in `.project-memory/`.

