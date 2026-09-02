# Global Engineering Development Standard

For every new or materially changed project:

- Establish a project-local `AGENTS.md` and an indexed documentation skeleton: `docs/INDEX.md`, `PRODUCT.md`, `ACCEPTANCE.md`, `CURRENT.md`, and `CODEMAP.md`.
- Use the `project-knowledge` Skill when available for INIT, UPDATE, and AUDIT. Keep document depth proportional to project complexity; do not omit the index because a project is small.
- Preserve intent, decisions, worklogs, raw sessions, evidence, and test artifacts. Curate active documents without irreversibly deleting raw history.
- Search for existing project capabilities, standard-library features, official tools, mature open-source solutions, or packages before building general-purpose infrastructure.
- Important changes require independent review, risk-appropriate verification, owner-readable evidence, and a documented release/rollback path.
- Keep transition files, temporary outputs, and final results inside the active project directory unless the user explicitly requests another destination.
- Never store credentials, tokens, cookies, private keys, or other secrets in source files, documents, logs, or screenshots.

The project-local `AGENTS.md` remains the source for repository-specific rules and may narrow these defaults.

