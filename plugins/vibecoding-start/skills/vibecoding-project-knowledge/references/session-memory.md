# Session Memory and Evidence

Raw project memory is local by default. Configure `.gitignore` so `.project-memory/*` is not committed, keep `.project-memory/README.md` as the boundary explanation when a repository needs it, and publish only redacted examples under `docs/examples/`.

At the end of a substantial session:

1. Preserve the raw process, relevant command output, and test artifacts locally under `.project-memory/`.
2. Redact credentials, tokens, cookies, private keys, and personal data before retaining raw output.
3. Curate current facts into `docs/CURRENT.md`; update `docs/PRD.md` when requirements, features, non-goals, constraints, or user scenarios changed.
4. Move durable decisions into an ADR and structural changes into `docs/CODEMAP.md`.
5. Summarize the useful explanation, rejected approaches, verification, result, and next step in `docs/worklog/`.
6. Update `docs/INDEX.md` if navigation or source-of-truth locations changed.

Worklogs answer “what happened and why.” Raw evidence answers “what exactly did the machine emit.” Do not fill the worklog with unfiltered stdout or treat a raw log as a human acceptance record.

Use stable dates in filenames: `YYYY-MM-DD-short-description.md`. Keep failed attempts locally because they prevent repeated work and preserve why a route was rejected. Removing them from Git tracking is a publication-boundary change, not permission to delete the local source record.
