# VibeCoding Start

Stop vibe coding from turning into unmaintainable AI-generated messes.

VibeCoding Start is a skill-only Codex Plugin that adds a lightweight engineering system from the first project session:

- PRD before code
- Search before build
- Indexed project knowledge
- Independent review
- Adversarial verification
- Human-readable acceptance
- Rollback-aware release
- Local-first raw project memory

## Why it exists

Without an engineering workflow, an AI-built project often grows like this:

```text
Idea → Prompt → Code → More Code → Context Lost → Unmaintainable mess
```

With VibeCoding Start:

```text
Idea → PRODUCT → PRD → ACCEPTANCE → Reuse → Plan
→ Build → Review → Verify → Accept → Release → Observe
```

The project always has a small knowledge skeleton. Small projects keep it short; larger projects earn deeper decisions, plans, testing, operations, release, and incident records.

## What it includes

This repository is the single public source of truth for the `vibecoding-start` Plugin:

```text
plugins/vibecoding-start/
├── .codex-plugin/plugin.json
└── skills/
    ├── vibecoding-start/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └── (main workflow)
    └── vibecoding-project-knowledge/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/ (including standard-v1.3.md)
        ├── templates/
        └── scripts/
```

The companion Skill manages `INIT`, `UPDATE`, and `AUDIT` for project knowledge. It is explicit-only in the UI so it does not compete with the main workflow's implicit invocation.

## Installation

The repository includes a local marketplace manifest at `.agents/plugins/marketplace.json`. After the release branch is merged into `main`, the current Codex CLI help supports this Git marketplace flow:

```text
codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref main
codex plugin add vibecoding-start@personal
```

While reviewing the release branch before that merge, replace `--ref main` with `--ref release/v0.1.0`.

For a local checkout, replace the first source with the path to the cloned repository:

```text
codex plugin marketplace add ./VibeCoding-Start
codex plugin add vibecoding-start@personal
```

Start a new Codex session after installation, then invoke:

```text
$vibecoding-start
I want to build a small local file-renaming tool.
```

The CLI command shape was checked against the available Codex CLI help. The repository's static checks validate the package; the final installation result still depends on the Codex host and its configured access to the selected marketplace.

## Quick start behavior

For a new project, the workflow establishes:

```text
AGENTS.md
docs/
├── INDEX.md
├── PRODUCT.md
├── PRD.md
├── ACCEPTANCE.md
├── CURRENT.md
└── CODEMAP.md
```

It then applies the risk-scaled G0-G9 gates. The first implementation question for a general capability is whether an existing project capability, standard library, official tool, mature package, adapter, or composition can be used. Custom implementation is the last option, not the default.

## Project memory and privacy

Raw sessions, command output, failed attempts, investigations, and test artifacts stay in local `.project-memory/` and are ignored by Git by default. Durable facts go to `docs/`; reusable public examples go to `docs/examples/` only after redaction and human review. This package does not create a memory database, vector database, search engine, testing framework, deployment framework, CI service, or observability backend.

## Compatibility and maintenance

The package uses the standard Codex Skill layout (`SKILL.md`, optional `agents/openai.yaml`, and focused references) inside a `.codex-plugin/plugin.json` distribution unit. When the standard changes, update the active v1.3 reference and workflow, run the local audits and fixture tests, review the diff independently, and record the release/rollback state before publishing.

## License

MIT. See [LICENSE](LICENSE).
