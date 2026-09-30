#!/usr/bin/env python3
"""Small, dependency-free bootstrap repository verifier."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED = {
    ".codex/config.toml",
    ".agent/PLANS.md",
    "AGENTS.md",
    "PROJECT.md",
    "PROJECT_STATE.md",
    "README.md",
    "docs/AI_WORKFLOW.md",
    "docs/ARCHITECTURE.md",
    "docs/DECISIONS.md",
    "docs/RESEARCH.md",
    "docs/RESPONSIBLE_RESEARCH.md",
    "docs/SOURCES.md",
    "docs/THREAT_MODEL.md",
    "docs/setup/CHATGPT_PROJECT_SETUP.md",
    "experiments/TEMPLATE.md",
    "scripts/doctor.ps1",
}
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
SECRET = re.compile(
    r"(?:gh[opsu]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
)


def main() -> int:
    errors: list[str] = []
    for relative in sorted(REQUIRED):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    tracked_text = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix.lower() in {".md", ".toml", ".py", ".ps1", ".example"}
    ]
    for path in tracked_text:
        content = path.read_text(encoding="utf-8")
        if SECRET.search(content):
            errors.append(f"possible secret in {path.relative_to(ROOT)}")
        if path.suffix.lower() != ".md":
            continue
        for target in LINK.findall(content):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists():
                errors.append(f"broken link in {path.relative_to(ROOT)}: {target}")

    try:
        branch = subprocess.run(
            ["git", "-C", str(ROOT), "branch", "--show-current"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        if branch != "main":
            errors.append(f"expected branch main, found {branch or '<none>'}")
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append(f"git check failed: {exc}")

    if errors:
        print("Repository verification failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Repository verification passed ({len(tracked_text)} text files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
