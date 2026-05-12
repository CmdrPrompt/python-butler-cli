"""Daily developer commands — proxies to Makefile targets (REQ-01)."""

from __future__ import annotations

import subprocess  # nosec B404 — subprocess is the intended mechanism for proxying make
import sys

import click

from butler.config import find_project_root


def _run_make(target: str) -> None:
    root = find_project_root()
    result = subprocess.run(["make", target], cwd=root)  # nosec B603 B607 — target is a hardcoded string, not user input
    sys.exit(result.returncode)


@click.command()
def lint() -> None:
    """Run linters (make lint)."""
    _run_make("lint")


@click.command()
def fix() -> None:
    """Auto-fix lint issues (make fix)."""
    _run_make("fix")


@click.command()
def stage() -> None:
    """Stage files for current task (make stage-current-task)."""
    _run_make("stage-current-task")


@click.command(name="test")
def test_cmd() -> None:
    """Run test suite (make test)."""
    _run_make("test")


@click.command()
def install() -> None:
    """Install project dependencies (make install)."""
    _run_make("install")


@click.command()
def setup() -> None:
    """Set up the project environment (make setup)."""
    _run_make("setup")
