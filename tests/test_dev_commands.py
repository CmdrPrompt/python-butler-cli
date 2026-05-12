"""Tests for daily developer commands (REQ-01)."""

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


@pytest.mark.parametrize(
    ("subcommand", "expected_target"),
    [
        ("lint", "lint"),
        ("fix", "fix"),
        ("stage", "stage-current-task"),
        ("test", "test"),
        ("install", "install"),
        ("setup", "setup"),
    ],
)
def test_command_calls_correct_make_target(
    runner: CliRunner,
    fake_root: Path,
    subcommand: str,
    expected_target: str,
) -> None:
    with (
        patch("butler.commands.dev.find_project_root", return_value=fake_root),
        patch("butler.commands.dev.subprocess.run", return_value=_mock_run()) as mock_run,
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, [subcommand])

    mock_run.assert_called_once_with(["make", expected_target], cwd=fake_root)


@pytest.mark.parametrize(
    "subcommand",
    ["lint", "fix", "stage", "test", "install", "setup"],
)
def test_command_does_not_capture_output(
    runner: CliRunner,
    fake_root: Path,
    subcommand: str,
) -> None:
    with (
        patch("butler.commands.dev.find_project_root", return_value=fake_root),
        patch("butler.commands.dev.subprocess.run", return_value=_mock_run()) as mock_run,
        patch.object(sys, "exit"),
    ):
        runner.invoke(app, [subcommand])

    _, kwargs = mock_run.call_args
    assert kwargs.get("capture_output") is not True
    assert "stdout" not in kwargs
    assert "stderr" not in kwargs


@pytest.mark.parametrize(
    "subcommand",
    ["lint", "fix", "stage", "test", "install", "setup"],
)
def test_command_exits_with_make_returncode(
    runner: CliRunner,
    fake_root: Path,
    subcommand: str,
) -> None:
    captured: list[int] = []
    with (
        patch("butler.commands.dev.find_project_root", return_value=fake_root),
        patch("butler.commands.dev.subprocess.run", return_value=_mock_run(returncode=2)),
        patch.object(sys, "exit", side_effect=captured.append),
    ):
        runner.invoke(app, [subcommand])

    assert captured[0] == 2
