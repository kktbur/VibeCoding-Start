# PRD

- Status: ACTIVE — redacted example
- Product: Local File Renamer

## Requirements

- REQ-001: The tool MUST preview every proposed rename before changing a file.
- REQ-002: The owner MUST explicitly confirm a preview before changes are applied.
- REQ-003: The tool MUST leave files outside the selected directory unchanged.
- REQ-004: The tool MUST report conflicts and invalid names without applying a partial silent rename.

## Constraints

- Operate on local files only.
- Keep behavior deterministic for the same directory snapshot and naming rule.
- Preserve a rollback or recovery path appropriate to the eventual implementation.

## Non-goals

- No network service, account, analytics, or background watcher.
- No bulk deletion or overwrite behavior in the first example.

