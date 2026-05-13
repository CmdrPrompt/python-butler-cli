"""Tests for butler task subcommands (REQ-02)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from butler.cli import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture()
def fake_root(tmp_path: Path) -> Path:
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'test'\n")
    return tmp_path


def _mock_run(returncode: int = 0) -> subprocess.CompletedProcess[bytes]:
    return subprocess.CompletedProcess(args=[], returncode=returncode)


# ---------------------------------------------------------------------------
# branch
# ---------------------------------------------------------------------------


def test_task_branch_with_explicit_id(runner: CliRunner, fake_root: Path) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, ["task", "branch", "TASK-005"])

    mock_run.assert_called_once_with(["make", "branch-task", "f=TASK-005"], cwd=fake_root)


def test_task_branch_derives_id_from_branch_name(runner: CliRunner, fake_root: Path) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch(
            "butler.commands.task._current_branch",
            return_value="task/005-task-workflow-commands",
        ),
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, ["task", "branch"])

    mock_run.assert_called_once_with(["make", "branch-task", "f=TASK-005"], cwd=fake_root)


def test_task_branch_fails_without_id_on_non_task_branch(
    runner: CliRunner, fake_root: Path
) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task._current_branch", return_value="main"),
    ):
        result = runner.invoke(app, ["task", "branch"])

    assert result.exit_code != 0
    assert "task ID" in result.output or "TASK" in result.output


# ---------------------------------------------------------------------------
# stage
# ---------------------------------------------------------------------------


def test_task_stage_with_explicit_id(runner: CliRunner, fake_root: Path) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, ["task", "stage", "TASK-005"])

    mock_run.assert_called_once_with(["make", "stage-task", "f=TASK-005"], cwd=fake_root)


def test_task_stage_derives_id_from_branch_name(runner: CliRunner, fake_root: Path) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch(
            "butler.commands.task._current_branch",
            return_value="task/005-task-workflow-commands",
        ),
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, ["task", "stage"])

    mock_run.assert_called_once_with(["make", "stage-task", "f=TASK-005"], cwd=fake_root)


def test_task_stage_fails_without_id_on_non_task_branch(runner: CliRunner, fake_root: Path) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task._current_branch", return_value="main"),
    ):
        result = runner.invoke(app, ["task", "stage"])

    assert result.exit_code != 0


# ---------------------------------------------------------------------------
# commit / pr / merge  (no task-id argument)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("subcommand", "expected_target"),
    [
        ("commit", "commit-current-task"),
        ("pr", "pr-current-task"),
        ("merge", "merge-current-task"),
    ],
)
def test_task_simple_commands(
    runner: CliRunner,
    fake_root: Path,
    subcommand: str,
    expected_target: str,
) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, ["task", subcommand])

    mock_run.assert_called_once_with(["make", expected_target], cwd=fake_root)


# ---------------------------------------------------------------------------
# exit code propagation
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "subcommand",
    ["commit", "pr", "merge"],
)
def test_task_simple_commands_propagate_exit_code(
    runner: CliRunner,
    fake_root: Path,
    subcommand: str,
) -> None:
    captured: list[int] = []
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run(returncode=2)),
        patch.object(sys, "exit", side_effect=captured.append),
    ):
        runner.invoke(app, ["task", subcommand])

    assert captured[0] == 2


# ---------------------------------------------------------------------------
# no capture_output
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("args", "branch"),
    [
        (["task", "branch", "TASK-005"], "main"),
        (["task", "stage", "TASK-005"], "main"),
        (["task", "commit"], "main"),
        (["task", "pr"], "main"),
        (["task", "merge"], "main"),
    ],
)
def test_task_commands_do_not_capture_output(
    runner: CliRunner,
    fake_root: Path,
    args: list[str],
    branch: str,
) -> None:
    with (
        patch("butler.commands.task.find_project_root", return_value=fake_root),
        patch("butler.commands.task.subprocess.run", return_value=_mock_run()) as mock_run,
        patch("butler.commands.task._current_branch", return_value=branch),
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, args)

    _, kwargs = mock_run.call_args
    assert kwargs.get("capture_output") is not True
    assert "stdout" not in kwargs
    assert "stderr" not in kwargs
