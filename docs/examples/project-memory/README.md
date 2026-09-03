# Project Memory Example

This is a deliberately redacted example of the local raw-memory boundary used by VibeCoding Start.

```text
.project-memory/              # local by default, ignored by Git
├── sessions/                  # raw session records
├── evidence/                  # command and test output
├── failed-attempts/           # rejected routes and their reasons
└── test-artifacts/            # local test artifacts
```

The public package keeps only this explanation. A real project may retain the raw records locally, then curate stable facts into `docs/CURRENT.md`, `docs/PRD.md`, an ADR, a worklog, or another indexed document. Publish a raw-looking example only after redaction and human review.
