# Contributing to VibeCoding Start

Thank you for helping improve this Skill-only Codex Plugin. Keep contributions small, evidence-based, and compatible with the repository's local-first privacy boundary.

## Before you change anything

Read the project instructions and active documentation in this order:

1. [`AGENTS.md`](AGENTS.md)
2. [`docs/INDEX.md`](docs/INDEX.md)
3. [`docs/CURRENT.md`](docs/CURRENT.md)
4. [`docs/PRODUCT.md`](docs/PRODUCT.md)
5. [`docs/PRD.md`](docs/PRD.md)
6. [`docs/ACCEPTANCE.md`](docs/ACCEPTANCE.md)

For a Skill or standard change, also read the relevant files in [`docs/CODEMAP.md`](docs/CODEMAP.md) and the active [`standard-v1.3.md`](plugins/vibecoding-start/skills/vibecoding-project-knowledge/references/standard-v1.3.md).

## Local verification

Use Python 3 and run the repository checks from the project root. On macOS or Linux, the complete wrapper is:

```sh
bash scripts/check.sh
```

The wrapper calls the same standard-library checks individually; it does not install dependencies. On Windows, invoke PowerShell 7 explicitly:

```text
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\audit_docs.py" .'
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\check_links.py" .'
pwsh -NoProfile -Command '& python "plugins\vibecoding-start\skills\vibecoding-project-knowledge\scripts\detect_stale_docs.py" . --max-age-days 30'
pwsh -NoProfile -Command '& python "tests\validate_plugin.py" "plugins\vibecoding-start" --marketplace ".agents\plugins\marketplace.json"'
pwsh -NoProfile -Command '& python "tests\test_project_knowledge.py"'
pwsh -NoProfile -Command '& python "tests\test_public_examples.py"'
pwsh -NoProfile -Command '& python "tests\test_readme_navigation.py"'
pwsh -NoProfile -Command '& python "tests\test_governance_docs.py"'
pwsh -NoProfile -Command '& python "tests\test_small_path_contract.py"'
pwsh -NoProfile -Command '& python "tests\check_version_consistency.py"'
pwsh -NoProfile -Command '& python "tests\check_line_endings.py" .'
pwsh -NoProfile -Command '& python "tests\check_name_drift.py" .'
pwsh -NoProfile -Command '& python -m compileall -q "plugins\vibecoding-start\skills"'
```

The CI workflows are [`Plugin Validation`](.github/workflows/plugin-validation.yml) and [`Standards Audit`](.github/workflows/standards-audit.yml). A PR that changes the package, documentation, or governance surface should leave all relevant checks green.

## Change expectations

- Search for an existing project capability, standard-library feature, official tool, mature package, or composition before adding general-purpose infrastructure.
- Keep the active source of truth under `plugins/vibecoding-start/skills/`; do not maintain a second Skill copy under `.agents/skills/`.
- If requirements, scope, or behavior changes, update `PRODUCT.md`, `PRD.md`, `ACCEPTANCE.md`, `CURRENT.md`, and the relevant index or worklog.
- A material architecture, security, dependency, publication, or release decision needs an ADR.
- Skill wording changes need an independent reviewer because the author should not be the final G5 reviewer of their own change.
- Include normal, error, boundary, or recovery evidence appropriate to the change. Green CI proves only the checks that ran.

## Pull request checklist

Before requesting review, make sure the PR explains:

- the user problem and intended outcome;
- which `PRODUCT`, `PRD`, and `ACCEPTANCE` entries it changes;
- exact local test commands and their results;
- the independent review or review request;
- the rollback or recovery method;
- any migration or compatibility impact;
- why no secret, credential, cookie, private key, password, or unnecessary personal data is included.

Do not paste raw `.project-memory` sessions, command logs, screenshots containing secrets, or private project paths into an Issue or PR. Use a short redacted reproduction instead.

## CLA and licensing

This project does not require a Contributor License Agreement. Contributions are accepted under the repository's [MIT License](LICENSE).
