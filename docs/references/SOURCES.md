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
| Local Codex Plugin Creator schema and CLI help | Host-provided runtime documentation | `.codex-plugin/plugin.json`, repository marketplace shape, validation fields, and current `codex plugin marketplace/add` command syntax used for this refactor |

## Source-quality note

OpenAI and Google entries are first-party documentation for the behavior they describe. The AGENTS.md site is an ecosystem reference. The previous package publication used Exa to locate current official Codex Skill documentation; the Exa connection returned a transport error during this refactor, so no new Exa result is represented as verified. The host-provided Plugin Creator schema and CLI help were used for the local package contract, and the GitHub connector remains the publication path.
