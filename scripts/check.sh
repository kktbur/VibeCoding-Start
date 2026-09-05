#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "${SCRIPT_DIR}/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "${PROJECT_ROOT}"

"${PYTHON_BIN}" "plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/audit_docs.py" .
"${PYTHON_BIN}" "plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/check_links.py" .
"${PYTHON_BIN}" "plugins/vibecoding-start/skills/vibecoding-project-knowledge/scripts/detect_stale_docs.py" . --max-age-days 30
"${PYTHON_BIN}" "tests/validate_plugin.py" "plugins/vibecoding-start" --marketplace ".agents/plugins/marketplace.json"
"${PYTHON_BIN}" "tests/test_project_knowledge.py"
"${PYTHON_BIN}" "tests/test_public_examples.py"
"${PYTHON_BIN}" "tests/test_readme_navigation.py"
"${PYTHON_BIN}" "tests/test_governance_docs.py"
"${PYTHON_BIN}" "tests/test_small_path_contract.py"
"${PYTHON_BIN}" "tests/test_version_consistency.py"
"${PYTHON_BIN}" "tests/check_version_consistency.py"
"${PYTHON_BIN}" "tests/check_line_endings.py" .
"${PYTHON_BIN}" "tests/check_name_drift.py" .
"${PYTHON_BIN}" -m compileall -q "plugins/vibecoding-start/skills"
