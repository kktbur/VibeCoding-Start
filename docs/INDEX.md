# VibeCoding Start Knowledge Index

This is the canonical starting point for the repository. It separates active product truth from implementation detail, history, and local raw memory.

## Hot Context

| Document | Purpose | Status |
|---|---|---|
| [Project instructions](../AGENTS.md) | Repository rules, privacy boundary, and local checks | ACTIVE |
| [Current state](CURRENT.md) | What is implemented, verified, and next | ACTIVE |
| [Product](PRODUCT.md) | Why VibeCoding Start exists and who it serves | ACTIVE |
| [PRD](PRD.md) | Released v0.3.0 baseline and post-release observation requirements | ACTIVE |
| [Acceptance](ACCEPTANCE.md) | Machine, owner, release, and recovery criteria | ACTIVE |

## Warm Knowledge

| Area | Entry point | Read when |
|---|---|---|
| Code map | [CODEMAP.md](CODEMAP.md) | Inspecting package, tests, or workflow structure |
| Plugin manifest | [plugin.json](../plugins/vibecoding-start/.codex-plugin/plugin.json) | Checking distribution metadata |
| Main Skill | [vibecoding-start/SKILL.md](../plugins/vibecoding-start/skills/vibecoding-start/SKILL.md) | Applying the G0-G9 workflow |
| Project Knowledge Skill | [vibecoding-project-knowledge/SKILL.md](../plugins/vibecoding-start/skills/vibecoding-project-knowledge/SKILL.md) | Running INIT, UPDATE, or AUDIT |
| Active standard | [standards/INDEX.md](standards/INDEX.md) | Checking version and normative status |
| Decisions | [decisions/INDEX.md](decisions/INDEX.md) | Reviewing material choices |
| Plans | [plans/INDEX.md](plans/INDEX.md) | Continuing staged work |
| Worklog | [worklog/INDEX.md](worklog/INDEX.md) | Understanding recent changes |
| Changelog | [CHANGELOG.md](../CHANGELOG.md) | Reviewing release differences |
| Cross-Agent contract | [CROSS-AGENT.md](CROSS-AGENT.md) | Preparing a repository-local handoff between coding agents |
| Chinese user README | [README.zh-CN.md](../README.zh-CN.md) | Serving Chinese-speaking users |
| Contributing guide | [CONTRIBUTING.md](../CONTRIBUTING.md) | Preparing a contribution |
| Security policy | [SECURITY.md](../SECURITY.md) | Reporting a vulnerability |
| Public example | [Project memory example](examples/project-memory/README.md) | Explaining the local raw-memory boundary |
| Small-project example | [Local File Renamer](examples/small-project/README.md) | Seeing the minimum project-document skeleton |

## Cold Archive Boundary

[Local raw-memory policy](../.project-memory/README.md) explains where raw sessions, evidence, failed attempts, investigations, logs, and test artifacts belong. Those records are ignored by Git by default and are not part of the public package.

## Maintenance loop

```text
Task End → preserve local raw memory → update CURRENT / PRD / active docs
→ update CODEMAP / ADR / worklog as needed → update this index → audit
```

Last reviewed: 2026-09-05

