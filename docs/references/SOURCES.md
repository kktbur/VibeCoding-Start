# External Sources

These sources were read to validate the deployment shape. They are guidance sources, not a substitute for the user-supplied standard.

| Source | Type | Applied point |
|---|---|---|
| [OpenAI: Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md) | Official OpenAI documentation | Global/project instruction layering, project-local precedence, and verification approach |
| [OpenAI: Building skills](https://learn.chatgpt.com/zh-Hans/docs/build-skills) | Official OpenAI documentation | A Skill is a directory with `SKILL.md`; repo-local skills use `.agents/skills`; scripts/references are optional resources |
| [OpenAI: Agent Skills — Codex](https://developers.openai.com/codex/skills) | Official OpenAI documentation | Progressive disclosure, required `SKILL.md` metadata, repository skill discovery, optional references, and implicit invocation |
| [OpenAI: Customization — Codex](https://developers.openai.com/codex/concepts/customization) | Official OpenAI documentation | Repository-local Skills are appropriate for workflows scoped to a project; global Skills are for cross-repository use |
| [OpenAI Codex repository: `docs/agents_md.md`](https://github.com/openai/codex/blob/main/docs/agents_md.md) | Official GitHub repository | GitHub-backed confirmation that Codex's AGENTS guidance points to the official documentation |
| [AGENTS.md](https://agents.md/) | Open ecosystem specification site | AGENTS.md complements human-facing README content with agent-facing build, test, convention, and security context |
| [Google Cloud: Architecture decision records overview](https://docs.cloud.google.com/architecture/architecture-decision-records) | Official technical documentation | ADRs capture context, options, decisions, consequences, and history close to code in Markdown/source control |

## Source-quality note

OpenAI and Google entries are first-party documentation for the behavior they describe. The AGENTS.md site is an ecosystem reference. Exa was used to locate the current official Codex Skill documentation, and the GitHub connector was used to inspect the requested target repository before the explicitly authorized publication.

