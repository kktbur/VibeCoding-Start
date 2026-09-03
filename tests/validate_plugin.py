#!/usr/bin/env python3
"""Validate the repository's Skill-only Plugin using the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL {message}")


def parse_frontmatter(path: Path, failures: list[str]) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path}: {exc}", failures)
        return {}
    match = FRONTMATTER.match(text)
    if not match:
        fail(f"{path} has no YAML frontmatter", failures)
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    for key in ("name", "description"):
        if not values.get(key):
            fail(f"{path} frontmatter lacks {key}", failures)
    return values


def check_skill(skill_dir: Path, failures: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"missing {skill_file}", failures)
        return
    metadata = parse_frontmatter(skill_file, failures)
    if metadata.get("name") != skill_dir.name:
        fail(f"{skill_file} name does not match directory", failures)
    ui_file = skill_dir / "agents" / "openai.yaml"
    if not ui_file.is_file():
        fail(f"missing {ui_file}", failures)
    else:
        ui_text = ui_file.read_text(encoding="utf-8")
        for field in ("display_name", "short_description", "default_prompt", "allow_implicit_invocation"):
            if re.search(rf"^\s*{re.escape(field)}\s*:", ui_text, re.MULTILINE) is None:
                fail(f"{ui_file} lacks {field}", failures)

        expected_policy = "false" if skill_dir.name == "vibecoding-project-knowledge" else "true"
        policy = re.search(r"^\s*allow_implicit_invocation\s*:\s*(true|false)\s*$", ui_text, re.MULTILINE)
        if not policy or policy.group(1) != expected_policy:
            fail(f"{ui_file} has unexpected implicit-invocation policy", failures)

    for path in skill_dir.rglob("*"):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"{path} is not UTF-8 text", failures)
            continue
        if "[TODO:" in text:
            fail(f"{path} contains an unfinished TODO placeholder", failures)
    text = skill_file.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        if not (skill_dir / target).resolve().is_file():
            fail(f"{skill_file} has a broken package link to {target}", failures)


def check_plugin(plugin_dir: Path, failures: list[str]) -> dict:
    manifest_path = plugin_dir / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        fail(f"missing {manifest_path}", failures)
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid plugin manifest: {exc}", failures)
        return {}

    for key in ("name", "version", "description", "author", "license", "skills", "interface"):
        if key not in manifest:
            fail(f"plugin manifest lacks {key}", failures)
    if manifest.get("name") != plugin_dir.name:
        fail("plugin name does not match directory", failures)
    if not SEMVER.match(str(manifest.get("version", ""))):
        fail("plugin version is not strict semantic versioning", failures)
    if not isinstance(manifest.get("author"), dict) or not manifest["author"].get("name"):
        fail("plugin author.name is missing", failures)
    if manifest.get("license") != "MIT":
        fail("plugin license is not MIT", failures)
    if not (plugin_dir.parent.parent / "LICENSE").is_file():
        fail("repository LICENSE is missing", failures)
    interface = manifest.get("interface")
    if not isinstance(interface, dict):
        fail("plugin interface is not an object", failures)
    else:
        for key in ("displayName", "shortDescription", "longDescription", "category", "defaultPrompt"):
            if key not in interface:
                fail(f"plugin interface lacks {key}", failures)
        prompts = interface.get("defaultPrompt")
        if not isinstance(prompts, list) or not prompts or len(prompts) > 3:
            fail("plugin interface defaultPrompt must be a list of one to three prompts", failures)
    skills_value = manifest.get("skills")
    if not isinstance(skills_value, str) or not skills_value.startswith("./"):
        fail("plugin skills must be a relative ./ path", failures)
        return manifest
    skills_dir = (plugin_dir / skills_value[2:]).resolve()
    if not skills_dir.is_dir():
        fail(f"plugin skills path does not resolve: {skills_value}", failures)
    else:
        skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
        expected = {"vibecoding-start", "vibecoding-project-knowledge"}
        actual = {path.name for path in skill_dirs}
        if actual != expected:
            fail(f"packaged Skill directories are {sorted(actual)}, expected {sorted(expected)}", failures)
        for skill_dir in skill_dirs:
            check_skill(skill_dir, failures)
    return manifest


def check_marketplace(path: Path, failures: list[str]) -> None:
    if not path.is_file():
        fail(f"missing marketplace manifest {path}", failures)
        return
    try:
        marketplace = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid marketplace manifest: {exc}", failures)
        return
    if marketplace.get("name") != "personal":
        fail("repo marketplace name must be personal for this package", failures)
    entries = [entry for entry in marketplace.get("plugins", []) if entry.get("name") == "vibecoding-start"]
    if len(entries) != 1:
        fail("marketplace must contain exactly one vibecoding-start entry", failures)
        return
    entry = entries[0]
    if entry.get("source", {}).get("path") != "./plugins/vibecoding-start":
        fail("marketplace source path is incorrect", failures)
    policy = entry.get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail("marketplace policy is not the default available/on-install policy", failures)
    if not entry.get("category"):
        fail("marketplace entry lacks category", failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin_root", nargs="?", default="plugins/vibecoding-start")
    parser.add_argument("--marketplace", default=".agents/plugins/marketplace.json")
    args = parser.parse_args()
    failures: list[str] = []
    plugin_dir = Path(args.plugin_root).resolve()
    check_plugin(plugin_dir, failures)
    check_marketplace(Path(args.marketplace).resolve(), failures)
    if failures:
        print(f"PLUGIN FAIL ({len(failures)} issue(s))")
        return 1
    print("PLUGIN PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
