# PRD

- Status: ACTIVE
- Release target: `v0.1.1`
- Product: VibeCoding Start Skill-only Plugin

## Problem

The previous repository package worked as a repository-local Skill but did not yet present a stable public Plugin boundary, an independent PRD, a local-only raw-memory policy, or a complete package validation contract.

## Users

- A Codex user starting a new software project.
- A maintainer improving an existing AI-built project.
- A reviewer or contributor who needs to understand the repository without replaying chat history.

## User scenarios

1. A user installs the Plugin, starts a new Codex session, and invokes `$vibecoding-start` for a new project.
2. The workflow establishes the six core documents before substantive implementation.
3. A material change updates the PRD, records a reuse decision, passes independent review and risk-appropriate verification, and presents an owner-readable result.
4. Raw sessions and machine output remain local while durable knowledge and redacted examples remain safe to publish.
5. A contributor can run deterministic checks and receive a clear failure when the PRD, package manifest, links, names, or fixtures are broken.

## Functional requirements

### REQ-001 — Installable Plugin boundary

The repository MUST contain one valid Skill-only Plugin at `plugins/vibecoding-start/` with a `.codex-plugin/plugin.json` manifest and two packaged Skills.

### REQ-002 — Unified Skill names

The main Skill MUST be named `vibecoding-start`. The companion Skill MUST be named `vibecoding-project-knowledge`, with implicit invocation disabled for the companion and enabled for the main workflow.

### REQ-003 — PRD-driven project knowledge

The project knowledge workflow MUST create and maintain `docs/PRD.md`, link it from `docs/INDEX.md`, and keep `PRODUCT.md`, `PRD.md`, and `ACCEPTANCE.md` as separate responsibilities.

### REQ-004 — Local-first raw memory

`.project-memory/*` MUST be ignored by Git by default, except for an optional boundary `README.md`. Public raw-looking examples MUST be redacted and placed under `docs/examples/`.

### REQ-005 — Deterministic validation

The repository MUST validate the Plugin manifest, both Skill packages, the project-document contract, repository links, current-state freshness, Python syntax, fixture behavior, active-name consistency, version consistency, and tracked text-file line endings without third-party test infrastructure.

### REQ-006 — Public usability

The README MUST explain the problem, workflow, installation shape, privacy boundary, compatibility limits, and license to a user who has not seen the implementation history.

### REQ-007 — Release readiness

The repository MUST record the active version, last-known-good state, release notes, rollback guidance, owner acceptance, and the boundary between package readiness and an actual GitHub Release.

### REQ-008 — Cross-platform maintenance

The repository MUST document reproducible checks for both PowerShell 7 and Unix-like shells, and MUST use repository-level text encoding and line-ending rules that keep review diffs portable.

## Non-goals

- Implementing infrastructure named in the original plan as explicitly out of scope.
- Rewriting public Git history when no confirmed secret exposure requires it.
- Treating static validation as a substitute for a fresh-session installation test or owner acceptance.

## Constraints

- Keep the package Skill-only; do not add MCP or App dependencies.
- Keep the active source of truth under `plugins/vibecoding-start/skills/`.
- Use Python standard library for repository tests and helpers.
- Keep local raw memory and transition artifacts under this project directory.
- Do not write unverified installation claims or expose local credentials and paths.

## Dependencies

- Codex Plugin/Skill support on the target host.
- Python 3 for deterministic checks.
- GitHub Actions for remote CI when enabled by the repository.

## Risks

- Runtime Skill discovery and Plugin installation must be confirmed in a fresh session on the target host.
- Existing consumers of the v1.2 repository-local path need the new package installation path.
- Current GitHub connector publication can update repository contents but does not by itself prove a completed GitHub Actions run or Release object.

## Open Questions

- Should a future release add a contribution guide, security policy, or issue templates?
- Should v0.2.0 add the small-project example and cross-Agent usage notes after the v0.1.1 maintenance release is observed?
