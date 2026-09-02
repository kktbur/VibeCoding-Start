# Software Engineering Development and Standards — Knowledge Index

This is the only required starting point for project knowledge. It separates active truth from historical evidence and keeps navigation explicit.

## Hot Context

| Document | Purpose | Status |
|---|---|---|
| [Project instructions](../AGENTS.md) | Codex working rules and gate language | ACTIVE |
| [Product](PRODUCT.md) | Why this deployment exists, users, scope, and non-goals | ACTIVE |
| [Acceptance](ACCEPTANCE.md) | Machine and owner acceptance criteria | ACTIVE |
| [Current state](CURRENT.md) | What is deployed, evidence, risks, and next step | ACTIVE |
| [Code map](CODEMAP.md) | Where the skill, scripts, docs, and workflow live | ACTIVE |

## Warm Knowledge

| Area | Entry point | Read when |
|---|---|---|
| Normative standard | [Vibe Engineering Standard v1.2](standards/VIBE-ENGINEERING-DEVELOPMENT-STANDARD-v1.2.md) | Applying the rules or deciding gate strength |
| Deployment mapping | [Local deployment](standards/LOCAL-DEPLOYMENT.md) | Auditing how the plan maps to files |
| Source plan | [Original supplied plan](standards/SOURCE-PLAN.md) | Checking exact source wording |
| Published Skill | [Vibe Engineering Development Standard Skill](../.agents/skills/vibe-engineering-development-standard/SKILL.md) | Applying the reusable Skill workflow |
| Sources | [External sources](references/SOURCES.md) | Verifying external claims |
| Decisions | [ADR index](decisions/INDEX.md) | Reviewing material choices |
| Plans | [Plan index](plans/INDEX.md) | Continuing staged work |
| Worklog | [Worklog index](worklog/INDEX.md) | Understanding recent progress |

## Cold Archive

- [Session archive](../.project-memory/sessions/INDEX.md)
- [Raw evidence](../.project-memory/evidence/INDEX.md)
- [Failed attempts](../.project-memory/failed-attempts/2026-09-02-folder-create-parameter.md)
- [Test artifacts](../.project-memory/test-artifacts/INDEX.md)
- [Public package README](../README.md)

## Maintenance loop

```text
Task End → preserve raw evidence → update CURRENT
→ update active docs / CODEMAP → write ADR when material
→ update worklog → update this index → audit
```

Last reviewed: 2026-09-02

