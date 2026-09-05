# Security Policy

## Scope

VibeCoding Start is a local-first, Skill-only Codex Plugin. Its public scope is the Plugin package, documentation, repository checks, fixtures, and GitHub workflow files. It is not a hosted service and does not need access to a project's raw memory to provide its documented workflow.

## Supported versions

Use the [latest published GitHub Release](https://github.com/kktbur/VibeCoding-Start/releases) for the supported package baseline. Development changes on `main` may be incomplete until they are reviewed, merged, tagged, and released.

## Reporting a vulnerability

Please do not open a public Issue for an undisclosed vulnerability and do not include secrets in an Issue, PR, screenshot, or log.

Use the repository's [private vulnerability reporting page](https://github.com/kktbur/VibeCoding-Start/security/advisories/new) when GitHub makes that option available. If the private form is unavailable, contact the repository owner through a private contact method shown on the [kktbur GitHub profile](https://github.com/kktbur) and provide only the minimum redacted details needed to reproduce the problem. Do not use a public Issue or PR as a fallback.

There is no guaranteed response-time SLA. Reports are reviewed according to maintainer availability and severity. Please allow the maintainer to coordinate disclosure before publishing exploit details.

## Secret handling

- Never commit API keys, access tokens, cookies, private keys, passwords, or other credentials.
- Never paste raw `.project-memory` sessions or unredacted command output into public Issues or PRs.
- The Skill does not intentionally upload project memory. Keep local raw records under `.project-memory/`, which is ignored by Git by default.
- If a secret is exposed, revoke or rotate it first, then report the incident privately with a redacted description. Do not assume deleting the file removes it from Git history.

See the README's [Project memory and privacy](README.md#project-memory-and-privacy) section for the user-facing privacy boundary. For ordinary documentation, installation, or behavior questions, use the repository's normal Issue templates instead of the security channel.
