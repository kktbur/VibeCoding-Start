---
name: vibe-engineering-development-standard
description: "Apply the Vibe Engineering Development Standard to software projects by initializing indexed project knowledge, scaling documentation to risk, running G0-G9 engineering gates, requiring reuse evidence, independent review, verification, human acceptance, and rollback-aware release. Use when starting a project or making a substantive change under this standard."
---

# Vibe Engineering Development Standard

Apply this skill when a project is being started, a substantive change is being planned, or the owner explicitly asks for the Vibe Engineering Development Standard. The supplied v1.2 plan is preserved verbatim in [references/standard-v1.2.md](references/standard-v1.2.md); read it when an interpretation, gate, or scaling decision needs the complete normative wording.

## Intended outcome

Keep every project indexable, recoverable, reviewable, verifiable, observable, and rollback-aware from its first formal development session. Use the lightest documentation and gate strength that is sufficient for the project's risk, while never removing the minimum project knowledge entry point.

## Operating boundary

- Work in the active project root and keep transition files, raw evidence, test artifacts, and result files inside that project unless the owner explicitly chooses another location.
- Preserve valid existing documentation. Connect it from the canonical project index instead of creating duplicate sources of truth.
- Prefer Markdown, Git, repository reading, existing tools, and deterministic checks. This skill does not create a memory database, vector database, search engine, testing framework, deployment engine, CI server, or observability backend.
- Do not modify global agent configuration or publish to an external repository unless the owner explicitly authorizes that mutation. A repository-local application is the default.
- Never store credentials, tokens, cookies, private keys, or other secrets in source files, documents, evidence, screenshots, or logs.

## Project knowledge first

For every new project, ensure this minimum structure exists before substantive implementation:

```text
PROJECT/
├── AGENTS.md
└── docs/
    ├── INDEX.md
    ├── PRODUCT.md
    ├── ACCEPTANCE.md
    ├── CURRENT.md
    └── CODEMAP.md
```

Use the `project-knowledge` Skill's `INIT`, `UPDATE`, and `AUDIT` modes when that Skill is available. Otherwise, apply the same rules directly:

- `docs/INDEX.md` is the only required navigation entry point.
- Keep `AGENTS.md`, `INDEX`, `CURRENT`, `PRODUCT`, and `ACCEPTANCE` short enough to serve as Hot Context.
- Read `CODEMAP`, architecture, decisions, plans, testing, operations, and release material only when the task needs them.
- Preserve raw sessions, investigations, failed attempts, evidence, and test artifacts under `.project-memory/`; curate summaries without deleting the source record.
- At the end of every substantive session, update current state, relevant active documents, the code map, worklog, and index, then rerun the relevant audits.

Scale depth rather than deciding whether documentation exists:

- **Small:** keep the six required files concise; do not create empty expansion directories.
- **Medium:** add indexed `docs/decisions/`, `docs/plans/`, `docs/worklog/`, and `.project-memory/sessions/` when the project gains multiple modules, persistence, external dependencies, or long-lived work.
- **Large:** add only the justified `architecture/`, `testing/`, `operations/`, `release/`, `incidents/`, and corresponding investigation/evidence/test-artifact archives.

## Engineering gates

Use this language for every meaningful change. A gate may be lightweight, but it must not be silently skipped when its risk is material.

```text
G0 Scope → G1 Intent → G2 Reuse → G3 Plan → G4 Build
→ G5 Adversarial Review → G6 Verification → G7 Human Acceptance
→ G8 Release → G9 Observation
```

### G0-G3: decide before building

1. **G0 Scope:** classify the work as application, integration/adapter, or infrastructure. Tighten the reuse and review requirements as the work moves closer to database, authentication, protocol, security, runtime, or other foundational boundaries.
2. **G1 Intent:** record the problem, user, current state, desired state, non-goals, acceptance conditions, and risks in `PRODUCT.md` and `ACCEPTANCE.md` before coding.
3. **G2 Reuse:** search the existing project, standard library, official SDK/API/tool, mature open source, and mature packages before implementing general-purpose capability. Decide in this order: `USE → ADAPT → COMPOSE → BUILD → STOP`. If an important capability is built or a mature option is rejected, record the alternatives, rejection reasons, maintenance cost, and owner acceptance method in an ADR.
4. **G3 Plan:** split complex work into small milestones, each with a concrete verification point. Do not ask one agent context to absorb an entire complex system in one unverified change.

### G4-G7: implement and prove

5. **G4 Build:** make the smallest coherent change that satisfies the current milestone. Avoid speculative abstractions, frameworks, dependencies, protocols, state machines, configuration layers, and custom verifiers unless the intent and reuse evidence justify them.
6. **G5 Adversarial Review:** for important changes, use an independent fresh reviewer or review context. Give it the relevant product and acceptance documents, active ADRs, architecture/code map, diff, and tests. Ask it to find omissions, bad assumptions, regression, duplicate capability, over-design, boundary/data/security risk, test gaps, and rollback problems. The implementer must not be the final reviewer for a material change.
7. **G6 Verification:** cover normal, error, boundary, regression, and recovery paths in proportion to risk. Add integration, end-to-end, stress, concurrency, fuzz/property, fault-injection, recovery, or performance checks only when the risk warrants them.
8. **G7 Human Acceptance:** report both machine evidence and owner-readable behavior. A green test is evidence for that test only; it is not a blanket correctness claim. The owner must have a concrete acceptance method for the product outcome.

### G8-G9: release and observe

9. **G8 Release:** before real use, record the version, last-known-good state, release notes, backup, rollback method, and migration risk.
10. **G9 Observation:** choose observability proportional to real use and risk, starting with useful logs, error evidence, and health checks before adding metrics, alerts, traces, or dashboards. If a failure appears, stop or roll back safely, investigate, and feed the result back into tests, worklog, ADR, product, and acceptance documents.

## Completion and stop rules

Do not claim completion until the relevant evidence exists for:

- the requested scope and current state;
- the documented intent and acceptance conditions;
- reuse research or the ADR explaining why a custom implementation was necessary;
- independent review when the change is material;
- automated verification and the owner-readable result;
- release and rollback information when the change is released;
- the next observation or maintenance step.

Stop and surface the issue when a required project document is missing, an index link is broken, active documents contradict one another, a general capability is being built without a reuse decision, a material change lacks independent review or a recovery path, or an external mutation lacks explicit owner authorization.

## Required session closeout

Separate concise worklog from raw evidence:

- Worklog: what changed, why, options rejected, problems, verification, current result, and next step.
- Raw evidence: large command output, test output, screenshots, and investigation material, with secrets redacted.

Preserve the raw record. Update the active summaries and indexes without treating old history as current truth. The final handoff should name the changed files, machine checks, unresolved risks, and owner acceptance method.

