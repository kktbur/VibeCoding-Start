# ADR-0004: Keep Raw Project Memory Local by Default

- Status: ACTIVE
- Date: 2026-09-03

## Context

The repository previously tracked raw sessions, evidence, failed attempts, and test-artifact indexes. These records are useful during local work but can include local paths, account metadata, or accidental private data and are not required for a public Plugin package.

## Options considered

1. Keep all raw memory in public Git.
2. Rewrite all history immediately.
3. Ignore `.project-memory/*` for new commits, preserve local files, retain only a boundary README, and promote redacted examples deliberately.

## Decision

Choose option 3. Scan existing local records before publication; do not rewrite history without confirmed secret exposure. Remove raw records from the current Git tree while keeping them on disk.

## Consequences

- Public documentation must not depend on ignored raw files.
- Curated worklogs and `docs/examples/` carry the reusable explanation.
- Local investigations remain recoverable to the owner.

## Evidence

- [Local memory boundary](../../.project-memory/README.md)
- [Redacted example](../examples/project-memory/README.md)
- [Product privacy scope](../PRODUCT.md)
