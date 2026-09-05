<p align="center">
  <img src="assets/vibecoding-start-cover.png" alt="VibeCoding Start cover" width="1200">
</p>

<p align="center">
  <strong>Language / 语言</strong><br>
  <a href="#vibecoding-start-english"><kbd>English</kbd></a>
  &nbsp;|&nbsp;
  <a href="#vibecoding-start-chinese"><kbd>中文</kbd></a>
  &nbsp;|&nbsp;
  <a href="README.zh-CN.md"><kbd>中文 README</kbd></a>
</p>

<a name="vibecoding-start-english"></a>

# VibeCoding Start

[![Plugin Validation](https://github.com/kktbur/VibeCoding-Start/actions/workflows/plugin-validation.yml/badge.svg?branch=main)](https://github.com/kktbur/VibeCoding-Start/actions/workflows/plugin-validation.yml)
[![Standards Audit](https://github.com/kktbur/VibeCoding-Start/actions/workflows/standards-audit.yml/badge.svg?branch=main)](https://github.com/kktbur/VibeCoding-Start/actions/workflows/standards-audit.yml)
[![License: MIT](https://img.shields.io/github/license/kktbur/VibeCoding-Start)](LICENSE)

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

## Documentation

- [Project knowledge index](docs/INDEX.md) — the repository's active documentation map
- [Small-project path](docs/examples/small-project/README.md) — a compact example for a new project
- [Engineering standard](plugins/vibecoding-start/skills/vibecoding-project-knowledge/references/standard-v1.3.md) — normative G0-G9 rules
- [Scaling rules](plugins/vibecoding-start/skills/vibecoding-project-knowledge/references/scaling-rules.md) — Small/Medium/Large depth and artifact minimums
- [Cross-Agent usage notes](docs/CROSS-AGENT.md) — how multiple coding agents share project truth safely
- [Chinese user README](README.zh-CN.md) — user-facing Chinese installation, privacy, and usage guide
- [Contributing](CONTRIBUTING.md) — local checks, PR expectations, and safe evidence boundaries
- [Security](SECURITY.md) — private vulnerability reporting and secret-handling policy
- [Changelog](CHANGELOG.md) — version history and migration notes
- [GitHub Releases](https://github.com/kktbur/VibeCoding-Start/releases) — pinned public release records

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

Add this repository as a Codex plugin marketplace, then install the Plugin. The pinned release command below uses the published `v0.2.0`; use `main` only when you intentionally want the latest development state.

```bash
codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref v0.2.0
codex plugin add vibecoding-start@kktbur
```

For the latest development state:

```bash
codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref main
codex plugin add vibecoding-start@kktbur
```

For a local checkout:

```bash
codex plugin marketplace add ./VibeCoding-Start
codex plugin add vibecoding-start@kktbur
```

Start a **new** Codex session after installation, then invoke:

```text
$vibecoding-start
I want to build a small local file-renaming tool.
```

### Troubleshooting

- Restart Codex in a new session if `$vibecoding-start` is unknown after installation.
- Confirm the marketplace name in `.agents/plugins/marketplace.json` matches the `@name` in `codex plugin add`.
- Run `codex plugin marketplace list` to confirm that the repository source is configured.
- This package does not install a memory database, CI system, or hosted observability backend.

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

---

<a name="vibecoding-start-chinese"></a>

# VibeCoding Start（中文）

<p align="center">
  <strong>Language / 语言</strong><br>
  <a href="#vibecoding-start-english"><kbd>English</kbd></a>
  &nbsp;|&nbsp;
  <a href="#vibecoding-start-chinese"><kbd>中文</kbd></a>
</p>

不要让 Vibe Coding 最终变成难以维护的 AI 生成代码堆。

VibeCoding Start 是一个仅由 Skills 组成的 Codex Plugin，从项目第一次会话开始提供轻量级工程系统：

- 先写 PRD，再写代码
- 先搜索，再构建
- 建立索引化项目知识
- 独立评审
- 面向反例的验证
- 人类可读的验收
- 具备回滚意识的发布
- 本地优先的原始项目记忆

## 为什么需要它

没有工程工作流时，一个 AI 构建的项目通常会这样增长：

```text
想法 → Prompt → 代码 → 更多代码 → 上下文丢失 → 难以维护的混乱项目
```

使用 VibeCoding Start 后：

```text
想法 → PRODUCT → PRD → ACCEPTANCE → Reuse → Plan
→ Build → Review → Verify → Accept → Release → Observe
```

项目始终会有一套小型知识骨架。小项目保持简短；只有当项目复杂度确实需要时，才增加更深入的决策、计划、测试、运维、发布和事故记录。

## 文档

- [Project knowledge index](docs/INDEX.md) — 仓库的主动文档索引
- [Small-project path](docs/examples/small-project/README.md) — 新项目的紧凑示例
- [Engineering standard](plugins/vibecoding-start/skills/vibecoding-project-knowledge/references/standard-v1.3.md) — G0-G9 规范规则
- [Scaling rules](plugins/vibecoding-start/skills/vibecoding-project-knowledge/references/scaling-rules.md) — Small/Medium/Large 深度和文件最低要求
- [Cross-Agent usage notes](docs/CROSS-AGENT.md) — 多个 coding agent 如何安全共享项目事实
- [中文用户 README](README.zh-CN.md) — 面向使用者的中文安装、隐私和使用说明
- [Contributing](CONTRIBUTING.md) — 本地检查、PR 要求和安全证据边界
- [Security](SECURITY.md) — 私密漏洞报告和敏感信息处理政策
- [Changelog](CHANGELOG.md) — 版本历史和迁移说明
- [GitHub Releases](https://github.com/kktbur/VibeCoding-Start/releases) — 固定版本的公开发布记录

## 包含内容

本仓库是 `vibecoding-start` Plugin 的唯一公开事实来源：

```text
plugins/vibecoding-start/
├── .codex-plugin/plugin.json
└── skills/
    ├── vibecoding-start/
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   └──（主工作流）
    └── vibecoding-project-knowledge/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/（包括 standard-v1.3.md）
        ├── templates/
        └── scripts/
```

配套 Skill 负责项目知识的 `INIT`、`UPDATE` 和 `AUDIT`。在 UI 中它只支持显式调用，因此不会与主工作流的隐式调用相互竞争。

## 安装

先把这个仓库添加为 Codex Plugin marketplace，再安装 Plugin。下面的固定版本命令使用已经发布的 `v0.2.0`；只有在你明确需要最新开发状态时，才使用 `main`。

```bash
codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref v0.2.0
codex plugin add vibecoding-start@kktbur
```

如果需要最新开发状态：

```bash
codex plugin marketplace add https://github.com/kktbur/VibeCoding-Start --ref main
codex plugin add vibecoding-start@kktbur
```

如果使用本地 checkout：

```bash
codex plugin marketplace add ./VibeCoding-Start
codex plugin add vibecoding-start@kktbur
```

安装后请启动一个**新的** Codex session，然后调用：

```text
$vibecoding-start
I want to build a small local file-renaming tool.
```

### 故障排查

- 安装后如果 `$vibecoding-start` 未知，请在新 session 中重新启动 Codex。
- 确认 `.agents/plugins/marketplace.json` 中的 marketplace name 与 `codex plugin add` 中的 `@name` 一致。
- 运行 `codex plugin marketplace list`，确认仓库来源已经配置。
- 这个 package 不会安装 memory database、CI system 或 hosted observability backend。

## 快速开始时的行为

对于新项目，工作流会建立：

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

随后它会应用按风险缩放的 G0-G9 gates。对于通用能力，第一次实现问题应该是：是否可以使用现有项目能力、standard library、official tool、成熟 package、adapter 或 composition。自定义实现是最后选项，而不是默认选项。

## 项目记忆与隐私

原始 session、命令输出、失败尝试、调查记录和测试产物保存在本地 `.project-memory/` 中，默认由 Git 忽略。稳定事实写入 `docs/`；可复用的公开示例只有在完成脱敏并经过人工审查后，才放入 `docs/examples/`。这个 package 不会创建 memory database、vector database、search engine、testing framework、deployment framework、CI service 或 observability backend。

## 兼容性与维护

这个 package 使用标准 Codex Skill layout（`SKILL.md`、可选的 `agents/openai.yaml` 和聚焦的 references），并通过 `.codex-plugin/plugin.json` 组成 distribution unit。标准发生变化时，应更新 active v1.3 reference 和 workflow，运行本地 audits 与 fixture tests，独立 review diff，并在发布前记录 release/rollback 状态。

## License

MIT。参见 [LICENSE](LICENSE)。

