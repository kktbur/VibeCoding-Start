# Indexing Rules

`docs/INDEX.md` is the canonical navigation entry point.

Every important document should be reachable from an index. Each index entry should state:

- document path;
- purpose;
- status (`PROPOSED`, `ACTIVE`, `SUPERSEDED`, or `ARCHIVED` where applicable);
- when to read it.

Use relative Markdown links so the project remains portable. Do not link to a generated local path when a repository-relative path is available.

Source-of-truth priority:

```text
PRODUCT / ACCEPTANCE
→ ACTIVE ADR
→ Architecture / CODEMAP
→ CURRENT
→ Worklog
→ Raw session
→ Chat history
```

Historical documents remain useful evidence but cannot silently override active documents. When a decision changes, update the status and add a forward link rather than deleting the old record.

Avoid isolated documents, duplicate active facts, and indexes that list files without explaining their role.

