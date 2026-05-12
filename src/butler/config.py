"""Butler configuration loaded from [tool.butler] in pyproject.toml."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

_KNOWN_KEYS = {
    "src_dir",
    "tests_dir",
    "tasks_dir",
    "project_name",
    "project_description",
    "requirements_path",
    "project_make_target",
}


@dataclass
class ButlerConfig:
    src_dir: str = "src"
    tests_dir: str = "tests"
    tasks_dir: str = "docs/tasks"
    project_name: str = ""
    project_description: str = "Describe your project here."
    requirements_path: str = "docs/REQUIREMENTS.md"
    project_make_target: str = "make help"


def find_project_root(start: Path | None = None) -> Path:
    """Walk up from *start* (default: cwd) to find the directory containing pyproject.toml."""
    current = (start or Path.cwd()).resolve()
    for directory in (current, *current.parents):
        if (directory / "pyproject.toml").is_file():
            return directory
    raise FileNotFoundError(f"No pyproject.toml found in {current} or any parent directory")


def load_config(project_root: Path | None = None) -> ButlerConfig:
    if project_root is None:
        project_root = Path.cwd()

    cfg = ButlerConfig(project_name=project_root.name)

    pyproject = project_root / "pyproject.toml"
    if not pyproject.exists():
        return cfg

    with pyproject.open("rb") as f:
        data = tomllib.load(f)

    for key, value in data.get("tool", {}).get("butler", {}).items():
        if key in _KNOWN_KEYS:
            setattr(cfg, key, value)

    return cfg
