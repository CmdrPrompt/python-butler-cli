"""Task workflow commands — proxies to Makefile targets (REQ-02)."""

from __future__ import annotations

import re
import subprocess  # nosec B404 — subprocess is the intended mechanism for proxying make
import sys

import click

from butler.config import find_project_root

_BRANCH_PATTERN = re.compile(r"^task/(\d+)-")


def _current_branch() -> str:
    result = subprocess.run(  # nosec B603 B607
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _task_id_from_branch(branch: str) -> str | None:
    m = _BRANCH_PATTERN.match(branch)
    if m:
        return f"TASK-{m.group(1).zfill(3)}"
    return None


def _resolve_task_id(task_id: str | None) -> str:
    if task_id:
        return task_id
    branch = _current_branch()
    derived = _task_id_from_branch(branch)
    if not derived:
        raise click.ClickException(
            f"Cannot derive task ID from branch '{branch}'. "
            "Pass an explicit TASK-NNN argument or switch to a task branch."
        )
    return derived


def _run_make(*args: str) -> None:
    root = find_project_root()
    result = subprocess.run(["make", *args], cwd=root)  # nosec B603 B607 — args are hardcoded strings
    sys.exit(result.returncode)


@click.group()
def task() -> None:
    """Manage task branches and commits."""


@task.command()
@click.argument("task_id", required=False, metavar="TASK-NNN")
def branch(task_id: str | None) -> None:
    """Create or switch to a task branch (make branch-task)."""
    tid = _resolve_task_id(task_id)
    _run_make("branch-task", f"f={tid}")


@task.command()
@click.argument("task_id", required=False, metavar="TASK-NNN")
def stage(task_id: str | None) -> None:
    """Stage files for a task (make stage-task)."""
    tid = _resolve_task_id(task_id)
    _run_make("stage-task", f"f={tid}")


@task.command()
def commit() -> None:
    """Commit using message from task file (make commit-current-task)."""
    _run_make("commit-current-task")


@task.command()
def pr() -> None:
    """Open a GitHub PR for the current task (make pr-current-task)."""
    _run_make("pr-current-task")


@task.command()
def merge() -> None:
    """Squash-merge the current task PR (make merge-current-task)."""
    _run_make("merge-current-task")
