# Document Layout

The project knowledge system uses three context temperatures.

## Hot Context

Read first for every new session:

1. `AGENTS.md`
2. `docs/INDEX.md`
3. `docs/CURRENT.md`
4. `docs/PRODUCT.md`
5. `docs/ACCEPTANCE.md`

Keep these files short enough to load together. They describe the active truth, not the full history.

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
→ raw archive or evidence
```

Store raw sessions, investigations, failed attempts, evidence, and test artifacts in `.project-memory/`.

## Artifact rule

All transition files, temporary outputs, test artifacts, and final results for this project stay below the project root. Large raw output belongs in `.project-memory/evidence/`; the worklog keeps only the durable explanation.

