"""Agent sync command — copies package agent files to project directories (REQ-05)."""

from __future__ import annotations

import hashlib
from importlib.resources import files
from pathlib import Path

import click


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _content_hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _sync_file(dest: Path, content: bytes) -> str:
    """Write content to dest if needed. Returns 'created', 'updated', or 'unchanged'."""
    if dest.exists():
        if _file_hash(dest) == _content_hash(content):
            return "unchanged"
        dest.write_bytes(content)
        return "updated"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(content)
    return "created"


def _sync_agents(cwd: Path) -> None:
    targets = [cwd / ".claude" / "agents", cwd / ".github" / "agents"]
    agents_pkg = files("butler.agents")
    for resource in agents_pkg.iterdir():
        name = resource.name
        if not name.endswith(".md"):
            continue
        content = resource.read_bytes()
        for target_dir in targets:
            dest = target_dir / name
            status = _sync_file(dest, content)
            click.echo(f"{status}: {dest.relative_to(cwd)}")


@click.command()
def sync() -> None:
    """Copy built-in agent files to .claude/agents/ and .github/agents/ (REQ-05)."""
    _sync_agents(Path.cwd())
