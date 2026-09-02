# Session Memory and Evidence

At the end of a substantial session:

1. Preserve the raw process, relevant command output, and test artifacts under `.project-memory/`.
2. Redact credentials, tokens, cookies, private keys, and personal data before storing output.
3. Curate the current facts into `docs/CURRENT.md`.
4. Move durable decisions into an ADR and structural changes into `docs/CODEMAP.md`.
5. Summarize the useful explanation, rejected approaches, verification, result, and next step in `docs/worklog/`.
6. Update `docs/INDEX.md` if navigation changed.

Worklogs answer “what happened and why.” Raw evidence answers “what exactly did the machine emit.” Do not fill the worklog with unfiltered stdout or pretend a raw log is a human acceptance record.

Use stable dates in filenames: `YYYY-MM-DD-short-description.md`. Keep failed attempts because they prevent repeated work and preserve the reason a route was rejected.

