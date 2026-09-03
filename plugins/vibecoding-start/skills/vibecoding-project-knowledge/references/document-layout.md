# Document Layout

The project knowledge system uses three context temperatures. Every project has the same entry point; risk determines how much detail is added behind it.

## Hot Context

Read first for every new session:

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/CURRENT.md`
4. `docs/PRODUCT.md`
5. `docs/PRD.md`
6. `docs/ACCEPTANCE.md`

Keep these files short enough to load together. They describe active truth, intent, requirements, and proof—not the full history.

## Warm Knowledge

Read only when the task needs it:

- `docs/CODEMAP.md`
- `docs/decisions/`
- `docs/plans/`
- `docs/standards/`
- `docs/references/`
- `docs/worklog/`

## Cold Archive

Do not load by default. Use the indexes to drill down:

```text
INDEX
→ active summary
→ detailed document
→ local raw archive or evidence
```

Store raw sessions, investigations, failed attempts, evidence, and test artifacts in local `.project-memory/`. It is ignored by Git by default.

## Artifact rule

All transition files, temporary outputs, test artifacts, and final results stay below the project root. Large raw output belongs in local `.project-memory/evidence/`; the worklog keeps only the durable explanation. Promote only redacted, intentionally reusable examples to `docs/examples/`.
