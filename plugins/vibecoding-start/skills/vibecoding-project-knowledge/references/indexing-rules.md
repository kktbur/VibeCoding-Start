# Indexing Rules

`docs/INDEX.md` is the canonical navigation entry point.

The six core documents have fixed responsibilities:

| Document | Responsibility |
|---|---|
| `PRODUCT.md` | Why the project exists |
| `PRD.md` | What the project must do |
| `ACCEPTANCE.md` | How to prove it works |
| `CURRENT.md` | Where the project is now |
| `CODEMAP.md` | Where the implementation lives |
| `INDEX.md` | Where to read the knowledge |

Every important curated document should be reachable from an index. Each entry should state its path, purpose, status (`PROPOSED`, `ACTIVE`, `SUPERSEDED`, or `ARCHIVED` where applicable), and when to read it.

Use relative Markdown links so the project remains portable. Do not link to an ignored raw-memory file from public documentation; link to `.project-memory/README.md` for the local boundary or to a deliberately redacted `docs/examples/` artifact.

Source-of-truth priority:

```text
PRODUCT / PRD / ACCEPTANCE
→ ACTIVE ADR
→ Architecture / CODEMAP
→ CURRENT
→ Worklog
→ Raw session
→ Chat history
```

Historical documents remain useful evidence but cannot silently override active documents. When a decision changes, update its status and add a forward link rather than deleting the old record.

Avoid isolated documents, duplicate active facts, and indexes that list files without explaining their role.
