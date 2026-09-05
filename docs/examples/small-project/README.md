# Small Project Example: Local File Renamer

- Status: REDACTED EXAMPLE
- Purpose: Show the smallest useful project-document skeleton produced by `vibecoding-start`.

This example describes a local file-renaming tool. It contains no application source, real user files, account data, or external service credentials. Treat the content as a shape to adapt, not as a production specification.

## Example project

The complete example project is under [`project/`](project/):

```text
project/
├── AGENTS.md
└── docs/
    ├── INDEX.md
    ├── PRODUCT.md
    ├── PRD.md
    ├── ACCEPTANCE.md
    ├── CURRENT.md
    └── CODEMAP.md
```

## First-session path

1. Start a new Codex session and invoke `$vibecoding-start`.
2. Let `INIT` establish the small project skeleton.
3. Describe the file-renaming behavior in `PRODUCT.md` and `PRD.md`.
4. Define human-readable checks in `ACCEPTANCE.md` before implementation.
5. Use `CURRENT.md` to record what is true now and `CODEMAP.md` to show where future code belongs.
6. After a material change, run `UPDATE`, review the diff independently, verify counterexamples, and run `AUDIT`.

## Small-project rule

Keep each document short while it is small. Add deeper plans, ADRs, testing, operations, release, and incident records only when the risk or complexity justifies them. The skeleton is always present; its depth scales with the project.

## Related guidance

- [Cross-Agent usage notes](../../CROSS-AGENT.md)
- [Project knowledge index](../../INDEX.md)
- [Project memory example](../project-memory/README.md)

