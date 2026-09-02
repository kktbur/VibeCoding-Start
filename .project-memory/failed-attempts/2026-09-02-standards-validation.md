# Failed Attempt: First Standards Validation

- Date: 2026-09-02
- Scope: first run of the local structure and Skill checks

## Findings

1. The link checker ran before the final evidence file existed, so the CURRENT evidence link was correctly reported as missing.
2. The link checker treated reusable template links as links relative to the template directory. Those links are intentionally written for the document's eventual destination, not for the template directory.
3. The official Skill validator could not import PyYAML from the bundled Python environment, then failed to decode UTF-8 with the Windows default codec after a temporary validation dependency was supplied.

## Recovery

- Exclude the Skill's reusable `templates/` directory from repository-link checking.
- Generate the final evidence file before the final link audit.
- Run the official validator with the bundled Python in UTF-8 mode and record the result.

This record preserves the false-positive and environment failures so they are not mistaken for a successful first pass.

