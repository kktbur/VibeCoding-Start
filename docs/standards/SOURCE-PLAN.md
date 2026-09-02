可以，这样反而更统一：**所有新项目一律先建立索引文档体系，不再判断“要不要建”，只判断“文档需要写多深”。** 小项目可以每份文档只有几十行，大项目再自然扩展。

# Vibe Engineering Development Standard v1.2

## 0. 目标

这套规范用于约束 Codex 主导的软件开发，避免出现：

- 收到需求直接开写；
- 不查已有方案就重复造轮子；
- 项目不断向底层基础设施下沉；
- 复杂度失控；
- Agent 自己实现、自己测试、自己宣布成功；
- 长会话结束后历史、决策和上下文逐渐丢失；
- 新 Session 每次重新理解项目；
- Owner 无法理解项目当前状态；
- 测试很多，但不知道到底证明了什么；
- 上线后不可观察、不可安全回滚。

核心目标：

> **让每一个项目从创建第一天开始，就成为一个“可索引、可恢复、可审查、可验证、可回滚”的工程项目。**

---

# 1. 六条最高工程原则

## ① 文档驱动

**意图必须留下来。**

重要信息不得只存在于聊天上下文。

任何项目从创建第一天开始，都建立项目知识与索引体系。

编码前明确：

- 为什么做；
- 谁使用；
- 解决什么问题；
- 哪些事情不做；
- 什么叫成功；
- 什么叫失败；
- 如何验收。

---

## ② 复用优先 / 复杂度惩罚

**能不造就不造。**

任何非核心业务能力，自研前优先级：

```text
当前项目已有能力
>
标准库
>
官方 SDK / API / Tool
>
成熟开源项目
>
成熟 Package
>
Thin Adapter / Wrapper
>
Custom Implementation
```

以下能力默认优先使用成熟实现：

- 数据库；
- 身份认证；
- 密码学；
- 支付；
- 消息队列；
- 对象存储；
- 搜索；
- 视频编解码；
- 网络协议；
- 并发基础设施；
- 安全敏感基础组件。

如果最终决定自研，必须说明：

1. 搜索过哪些方案；
2. 为什么不能直接使用；
3. 为什么不能 Adapt；
4. 为什么不能 Compose；
5. 自研增加了哪些长期维护责任；
6. Owner 是否能够理解并验收。

---

## ③ 对抗审查

**作者不能自己给自己签字。**

重要修改必须交给独立 Reviewer。

Reviewer 的任务不是证明实现正确，而是主动寻找：

- 需求遗漏；
- 错误假设；
- Regression；
- 重复造轮子；
- 过度设计；
- 无必要 abstraction；
- 边界条件；
- 数据风险；
- 安全风险；
- 测试漏洞；
- 不可回滚变化。

---

## ④ 暴力测试

**用机器主动寻找反例。**

不能因为：

- 代码看起来正确；
- Agent 说完成了；
- 一组测试绿色；

就认定项目正确。

根据风险覆盖：

```text
正常路径
+
异常路径
+
边界条件
+
历史 Regression
+
错误输入
+
恢复路径
```

必要时加入：

- Integration；
- E2E；
- Stress；
- Concurrency；
- Fuzz；
- Property Testing；
- Fault Injection；
- Recovery；
- Performance。

---

## ⑤ 可观测运行

**上线以后还要知道软件实际上在干什么。**

所有进入真实使用的软件，都应该根据项目规模建立适当的：

```text
日志
→ Error Log
→ Health
→ Metrics
→ Alerts
→ Traces
→ Dashboard
```

至少应该能够回答：

- 现在是否正常；
- 哪里发生了错误；
- 哪个版本导致问题；
- 用户报告问题时如何找到证据；
- 外部依赖是否异常；
- 性能是否明显退化。

---

## ⑥ 渐进发布 + 随时可回滚

**不把一次验证当成永久正确。**

发布尽量遵循：

```text
本地
↓
测试
↓
Beta / 小范围
↓
观察
↓
扩大
↓
Stable
```

发现异常：

```text
Stop
↓
Rollback / Roll Forward
↓
调查
↓
修复
```

重要项目必须知道：

- 当前版本；
- Last Known Good；
- Backup；
- Rollback 方法；
- 数据恢复方式。

---

# 2. 整体治理架构

整套体系分成四层：

```text
              ~/.codex/AGENTS.md
               Global Constitution
                       │
                       ▼
              Engineering Skills
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
Project Knowledge   Search Before    Coding /
Skill                Build            Architecture
       │
       ▼
              PROJECT/AGENTS.md
                       │
                       ▼
                Project Knowledge
                       │
                       ▼
             Code / Test / CI / Release
```

职责：

```text
Global AGENTS
= 所有项目必须遵守什么

Skills
= 具体怎么执行

Project AGENTS
= 当前项目在哪里执行

Project Docs
= 当前项目的事实、历史和证据
```

---

# 3. 第一阶段：建立 Global AGENTS

位置：

```text
~/.codex/AGENTS.md
```

Global AGENTS 只保存跨项目长期有效的规则。

主要包括：

## Owner Model

默认用户是 Product Owner。

不假定用户可以阅读复杂源码。

技术结果必须同时提供：

- Machine Evidence；
- Human-readable Explanation；
- User Acceptance Method。

---

## Document Before Build

所有新项目都必须建立项目文档和索引体系。

不得因为项目“小”而完全依赖聊天记录、README 或模型记忆。

区别只在于：

> **小项目文档可以很短，大项目文档可以很深。**

---

## Reuse Before Build

通用工程能力必须先查成熟实现。

---

## Infrastructure Boundary

越接近底层基础设施：

> 越应该复用成熟专业方案。

---

## Complexity Budget

新增以下机制必须证明真实必要性：

- abstraction；
- protocol；
- state machine；
- custom verifier；
- dependency；
- adapter；
- configuration layer；
- framework。

---

## Small Changes

复杂功能必须拆成小的可验证 Milestone。

---

## Independent Review

重要实现不得由同一个 Agent Context 最终审核。

---

## Evidence Before Claim

没有证据，不允许声明完成。

---

## Project Knowledge Governance

所有新项目必须：

1. 建立项目索引；
2. 建立项目目标文档；
3. 建立验收标准；
4. 建立代码地图；
5. 开发过程中持续维护；
6. 重要 Session 保存历史记录；
7. 不可逆压缩不得删除原始项目历史。

---

# 4. 第二阶段：所有新项目一律初始化知识体系

```text
New Project
↓
Project Knowledge INIT
↓
立即建立统一骨架
↓
根据项目增长自然扩展内容深度
```

> **“有没有文档体系”不再是变量。**

变量只有：

> **“文档需要多详细”。**

---

# 5. 所有项目统一最低骨架

任何新项目建立时，一律至少创建：

```text
PROJECT/
│
├── AGENTS.md
│
└── docs/
    ├── INDEX.md
    ├── PRODUCT.md
    ├── ACCEPTANCE.md
    ├── CURRENT.md
    └── CODEMAP.md
```

这是最小强制结构。

哪怕项目只需要开发一天，也创建。

但内容可以非常简单。

例如小工具的 `CODEMAP.md` 完全可以只有：

```text
main.py
→ 程序入口

downloader.py
→ 下载核心

config.py
→ 用户配置
```

不需要为了满足模板写十页文字。

---

# 6. 项目复杂度决定“内容深度”

可以判断项目规模，但它只用于：

> **控制文档深度、Gate 强度和需要增加哪些扩展目录。**

例如：

## Small

特点通常是：

- 单一功能；
- 少量模块；
- 几天开发完成；
- 低风险；
- 状态简单。

仍然存在：

```text
AGENTS
INDEX
PRODUCT
ACCEPTANCE
CURRENT
CODEMAP
```

但每份文件保持极简。

---

## Medium

随着项目出现：

- 多个模块；
- 长期开发；
- 数据持久化；
- GUI + backend 等多个部分；
- 多个外部依赖；
- 长期维护；

再自然增加：

```text
docs/
├── decisions/
│   └── INDEX.md
├── plans/
│   └── INDEX.md
└── worklog/
    └── INDEX.md
```

以及：

```text
.project-memory/
└── sessions/
```

---

## Large

随着项目继续增长，再增加：

```text
docs/
├── architecture/
├── testing/
├── operations/
│   └── OBSERVABILITY.md
├── release/
│   └── ROLLBACK.md
└── incidents/
```

以及：

```text
.project-memory/
├── sessions/
├── investigations/
├── failed-attempts/
├── evidence/
└── test-artifacts/
```

所以实际上是：

```text
统一骨架
↓
自然生长
```

而不是：

```text
三套互不相同的模板
```

---

# 7. 文档结构必须遵循“索引优先”

任何文档都不应该变成孤岛。

项目的核心入口永远是：

```text
docs/INDEX.md
```

它回答：

> 我现在想了解某件事，应该去哪读？

例如：

```text
项目目标
→ PRODUCT.md

当前开发状态
→ CURRENT.md

验收要求
→ ACCEPTANCE.md

代码结构
→ CODEMAP.md

架构决定
→ decisions/INDEX.md

最近工作
→ worklog/INDEX.md

运行和故障
→ operations/
```

---

# 8. 项目知识采用三层上下文结构

## 第一层：Hot Context

新 Session 最优先读取：

```text
AGENTS.md
docs/INDEX.md
docs/CURRENT.md
docs/PRODUCT.md
docs/ACCEPTANCE.md
```

保持短小。

---

## 第二层：Warm Knowledge

根据任务按需读取：

```text
CODEMAP
Architecture
ADR
Plans
Testing
Operations
```

Agent 不应该默认把所有内容加载进上下文。

---

## 第三层：Cold Archive

完整历史：

```text
.project-memory/
```

包括：

- Sessions；
- Investigations；
- Failed Attempts；
- Raw Evidence；
- Test Artifacts。

默认不读取。

需要追溯时：

```text
INDEX
↓
Active Summary
↓
Detailed Doc
↓
Raw Archive
```

逐级下钻。

---

# 9. 上下文保留原则

采用：

```text
Raw History
     │
     │ 永久保留
     ▼
Curated Knowledge
     │
     │ 可以整理
     ▼
Index
     │
     │ 保持极简
     ▼
Current Context
```

核心规则：

> **上下文窗口可以压缩，项目历史不能被不可逆压缩。**

允许 compact：

- 重复描述；
- Active Knowledge；
- 导航文本。

不应删除：

- 原始 Session；
- 原始调查；
- 失败实验；
- 测试证据；
- 重大决策原始原因。

---

# 10. History 不等于 Truth

知识优先级：

```text
当前 PRODUCT / ACCEPTANCE
>
ACTIVE ADR
>
当前 Architecture / CODEMAP
>
CURRENT
>
Worklog
>
Raw Session
>
聊天历史
```

历史决策必须标状态：

```text
PROPOSED
ACTIVE
SUPERSEDED
ARCHIVED
```

旧事实可以存在。

但是不能因为搜索到了旧 Session，就覆盖当前 Active Knowledge。

---

# 11. 统一项目知识体系做成独立 Skill

建立：

```text
project-knowledge/
├── SKILL.md
│
├── references/
│   ├── document-layout.md
│   ├── indexing-rules.md
│   ├── adr-rules.md
│   ├── session-memory.md
│   └── scaling-rules.md
│
├── templates/
│   ├── INDEX.md
│   ├── PRODUCT.md
│   ├── ACCEPTANCE.md
│   ├── CURRENT.md
│   ├── CODEMAP.md
│   └── ADR.md
│
└── scripts/
    ├── audit_docs.py
    ├── check_links.py
    └── detect_stale_docs.py
```

这个 Skill 不造：

- Memory Database；
- Vector Database；
- Search Engine；
- Documentation Platform。

核心仍然是：

```text
Markdown
+
Git
+
Codex repo reading
+
简单确定性检查
```

---

# 12. Project Knowledge Skill 三个 Mode

## INIT

所有新项目第一次正式开发时自动执行。

流程：

```text
扫描项目
↓
读取现有 README / Docs / Code
↓
保留已有有效文档结构
↓
建立统一知识入口
↓
INDEX
↓
PRODUCT
↓
ACCEPTANCE
↓
CURRENT
↓
CODEMAP
```

如果项目已经存在：

```text
ARCHITECTURE.md
ADR/
docs/design/
```

不重复造一套。

而是把它们接入新的 INDEX。

---

## UPDATE

重要 Session 结束后：

```text
Raw Session
        │
        ├─ 原始过程
        │      ↓
        │  Raw Archive
        │
        ├─ 当前状态
        │      ↓
        │   CURRENT
        │
        ├─ 长期知识
        │      ↓
        │ Active Docs
        │
        ├─ 重大决定
        │      ↓
        │     ADR
        │
        ├─ 代码结构变化
        │      ↓
        │   CODEMAP
        │
        └─ 导航变化
               ↓
             INDEX
```

---

## AUDIT

定期或重大修改后检查：

- INDEX 是否完整；
- 是否存在死链接；
- 是否存在孤立文档；
- CODEMAP 是否与代码明显漂移；
- CURRENT 是否过期；
- Active ADR 是否冲突；
- 已 Superseded ADR 是否仍影响当前工作；
- Raw History 中是否存在需要提升为正式知识的信息；
- 文档之间是否出现互相矛盾。

---

# 13. Global AGENTS、Skill、Project AGENTS 三层分工

## Global AGENTS

负责：

> 所有项目都必须建立并维护 Project Knowledge。

---

## Project Knowledge Skill

负责：

> 怎么 INIT、UPDATE、AUDIT。

---

## Project AGENTS

负责：

> 当前项目具体去哪读取这些知识。

例如：

```text
Project index:
docs/INDEX.md

Current state:
docs/CURRENT.md

Product truth:
docs/PRODUCT.md

Acceptance:
docs/ACCEPTANCE.md

Code map:
docs/CODEMAP.md

Architecture decisions:
docs/decisions/

Raw history:
.project-memory/
```

---

# 14. 第三阶段：建立 Engineering Gates

非简单开发统一使用：

```text
Idea
 ↓
G0 Scope
 ↓
G1 Intent
 ↓
G2 Reuse
 ↓
G3 Plan
 ↓
G4 Build
 ↓
G5 Adversarial Review
 ↓
G6 Verification
 ↓
G7 Human Acceptance
 ↓
G8 Release
 ↓
G9 Observation
```

Gate 的强度仍然根据实际风险调整。

但所有项目都拥有同样的总体流程语言。

---

# 15. G0 Scope Gate

先判断：

```text
Product / Business / UI / Workflow
→ 应用层

Integration / Adapter
→ 集成层

Database / Auth / Protocol / Security / Runtime
→ 基础设施层
```

越向底层：

> Reuse Gate 越严格。

---

# 16. G1 Intent Gate

编码前明确：

- Problem；
- User；
- Current State；
- Desired State；
- Non-goals；
- Acceptance；
- Risks。

写入：

```text
PRODUCT.md
ACCEPTANCE.md
```

---

# 17. G2 Reuse Gate

任何非平凡通用能力：

```text
Search Before Build
↓
USE
ADAPT
COMPOSE
BUILD
STOP
```

如果重要能力最终选择 BUILD：

> 写 ADR。

---

# 18. G3 Plan Gate

复杂任务拆成：

```text
Milestone 1
→ Verify

Milestone 2
→ Verify

Milestone 3
→ Verify
```

禁止一个 Agent 一次吞掉整个复杂系统。

---

# 19. G4 Build Gate

开发阶段利用已有工具：

```text
Karpathy Guidelines
→ 简单、小改、避免过度设计

Matt Pocock Engineering
→ 架构、领域、ADR

成熟语言工具链
→ lint / type / test
```

---

# 20. G5 Adversarial Review

重要实现交给 Fresh Reviewer。

Reviewer读取：

```text
PRODUCT
ACCEPTANCE
Active ADR
Relevant Architecture
Diff
Tests
```

并主动寻找反例和问题。

---

# 21. G6 Verification

至少验证：

- 正常路径；
- 错误路径；
- 边界条件；
- Regression；
- Recovery。

重要系统再增加高级测试。

---

# 22. 测试结果必须同时提供两种表达

## Machine Evidence

例如：

```text
pytest 286 passed
CI passed
stress test passed
```

## Owner Evidence

例如：

```text
断网恢复：通过

重复点击：
不会创建重复任务

异常退出：
重新打开可以恢复

历史 Bug：
没有重新出现
```

Owner 不应该只能看到一堆命令。

---

# 23. G7 Human Acceptance

最终完成需要：

```text
Automated Verification
+
Independent Review
+
Human Acceptance
```

Owner 判断：

> 这个产品是不是自己真正需要的东西？

---

# 24. G8 Release

进入真实使用前记录：

- Version；
- Last Known Good；
- Release Notes；
- Backup；
- Rollback；
- Migration 风险。

---

# 25. G9 Observation

上线后：

```text
Deploy
↓
Observe
↓
Healthy?
├─ Yes → Continue
└─ No  → Stop / Rollback
```

生产反馈必须重新进入：

- Tests；
- Worklog；
- ADR；
- PRODUCT；
- ACCEPTANCE；
- Postmortem。

---

# 26. 每个重要 Session 必须做知识收尾

```text
Task End
↓
保存 Raw Session / Evidence
↓
Project Knowledge UPDATE
↓
更新 CURRENT
↓
更新相关 Docs
↓
必要时更新 CODEMAP
↓
必要时写 ADR
↓
更新 INDEX
```

---

# 27. Worklog 与 Raw Evidence 分开

Worklog 只记录人真正值得以后读的信息：

- 做什么；
- 为什么；
- 用了什么方案；
- 哪些方案被拒绝；
- 出现什么问题；
- 怎么验证；
- 当前结果；
- 下一步。

大量：

```text
commands
stdout
stderr
test raw output
```

进入：

```text
.project-memory/evidence/
```

---

# 28. ADR 只记录重大决定

满足以下至少一项才创建：

- 难以逆转；
- 改变主要架构；
- 改变数据模型；
- 新增重要 dependency；
- 改变公共 API；
- 改变安全边界；
- 改变发布方式；
- 自研重要通用能力；
- 拒绝明显成熟方案；
- 显著增加系统复杂度。

---

# 29. 最终工具组合

```text
Global Policy
→ ~/.codex/AGENTS.md

Project Knowledge
→ project-knowledge Skill

Reuse Research
→ Search Before Build

Coding Discipline
→ Karpathy Guidelines

Architecture
→ Matt Pocock Skills

Review
→ Fresh Reviewer Agent

Testing
→ 成熟测试工具链

CI
→ GitHub Actions / Existing CI

Release
→ Git + 成熟发布平台

Observability
→ 成熟监控方案
```

---

# 30. 不再开发超级工程框架

最多保留一个非常薄的：

```text
vibe-engineering-governor
```

负责：

```text
检查 Project Knowledge
↓
判断任务风险
↓
调用对应 Skill
↓
检查 Gate
```

不重新实现：

- Memory Engine；
- Search Engine；
- Testing Framework；
- Deployment Engine；
- CI；
- Verifier；
- Observability Backend。

---

# 31. 最终新项目启动流程

以后任何项目统一：

```text
New Project
     │
     ▼
Project Knowledge INIT
     │
     ▼
AGENTS
INDEX
PRODUCT
ACCEPTANCE
CURRENT
CODEMAP
     │
     ▼
明确需求
     │
     ▼
Search Before Build
     │
     ▼
USE / ADAPT / COMPOSE / BUILD
     │
     ▼
Engineering Gates
     │
     ▼
项目自然增长
     │
     ▼
文档体系同步自然增长
```

---

# 32. 小项目和大项目的区别最终只剩一个

不是：

```text
小项目
→ 没文档

大项目
→ 有文档
```

而是：

```text
小项目
→ 小而完整的知识体系

中项目
→ 更丰富的知识体系

大项目
→ 深度知识体系 + Operations + Release + Incidents
```

即：

> **结构统一，深度自适应。**

---

# 33. 最终日常循环

```text
新需求
  │
  ▼
INDEX / CURRENT
  │
  ▼
Intent
  │
  ▼
Reuse
  │
  ▼
Plan
  │
  ▼
Build
  │
  ▼
Independent Review
  │
  ▼
Verification
  │
  ▼
Human Acceptance
  │
  ▼
Release
  │
  ▼
Observe
  │
  ├───────────────┐
  ▼               ▼
Healthy         Failure
  │               │
  ▼               ▼
Knowledge       Rollback
Update            │
  │               ▼
  ▼           Postmortem
Next Change
```

---

# 34. 最终原则

### 第一条

> **所有项目从第一天开始都有索引和项目知识体系。**

### 第二条

> **小项目不是不写文档，而是写更短、更简单、更聚焦的文档。**

### 第三条

> **项目越复杂，知识结构自然生长，而不是第一天创建几十份空文档。**

### 第四条

> **当前知识可以整理压缩，原始历史和证据不得不可逆丢失。**

### 第五条

> **成熟能力能复用就复用，AI 能写并不等于应该自己写。**

### 第六条

> **实现者不能成为自己的最终裁判。**

### 第七条

> **只要 Owner 还能快速知道项目是什么、现在做到哪里、为什么这样设计、怎么证明它正确，项目就仍然处于可控状态。**

我认为这一版比上一版更适合长期执行：**完全取消“要不要建知识体系”的判断成本，所有仓库默认都有同一入口；复杂度只决定内容量，不决定有没有。**