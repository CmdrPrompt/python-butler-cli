"""Tests for butler sync command (REQ-05)."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner

from butler.cli import app
from butler.commands.sync import _sync_agents, _sync_file


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def _fake_pkg(*entries: tuple[str, bytes]) -> MagicMock:
    resources: list[MagicMock] = []
    for name, content in entries:
        r: MagicMock = MagicMock()
        r.name = name
        r.read_bytes.return_value = content
        resources.append(r)
    pkg: MagicMock = MagicMock()
    pkg.iterdir.return_value = resources
    return pkg


class TestSyncFile:
    def test_creates_new_file(self, tmp_path: Path) -> None:
        dest = tmp_path / "agents" / "file.md"
        assert _sync_file(dest, b"content") == "created"
        assert dest.read_bytes() == b"content"

    def test_unchanged_when_identical(self, tmp_path: Path) -> None:
        dest = tmp_path / "file.md"
        dest.write_bytes(b"content")
        assert _sync_file(dest, b"content") == "unchanged"

    def test_updates_when_different(self, tmp_path: Path) -> None:
        dest = tmp_path / "file.md"
        dest.write_bytes(b"old")
        assert _sync_file(dest, b"new") == "updated"
        assert dest.read_bytes() == b"new"

    def test_creates_parent_dirs(self, tmp_path: Path) -> None:
        dest = tmp_path / "deep" / "nested" / "file.md"
        _sync_file(dest, b"content")
        assert dest.exists()

    def test_unchanged_does_not_modify_file(self, tmp_path: Path) -> None:
        dest = tmp_path / "file.md"
        dest.write_bytes(b"content")
        mtime = dest.stat().st_mtime_ns
        _sync_file(dest, b"content")
        assert dest.stat().st_mtime_ns == mtime


class TestSyncAgents:
    def test_copies_to_both_target_dirs(self, tmp_path: Path) -> None:
        pkg = _fake_pkg(("agent.md", b"# Agent"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        assert (tmp_path / ".claude" / "agents" / "agent.md").exists()
        assert (tmp_path / ".github" / "agents" / "agent.md").exists()

    def test_skips_non_md_files(self, tmp_path: Path) -> None:
        pkg = _fake_pkg(("readme.txt", b"text"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        assert not (tmp_path / ".claude" / "agents" / "readme.txt").exists()

    def test_updated_when_different(self, tmp_path: Path) -> None:
        for d in [".claude/agents", ".github/agents"]:
            (tmp_path / d).mkdir(parents=True)
            (tmp_path / d / "agent.md").write_bytes(b"old")
        pkg = _fake_pkg(("agent.md", b"new"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        assert (tmp_path / ".claude" / "agents" / "agent.md").read_bytes() == b"new"
        assert (tmp_path / ".github" / "agents" / "agent.md").read_bytes() == b"new"

    def test_output_created(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        pkg = _fake_pkg(("agent.md", b"# Agent"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        assert "created" in capsys.readouterr().out

    def test_output_unchanged(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        content = b"# Agent"
        for d in [".claude/agents", ".github/agents"]:
            (tmp_path / d).mkdir(parents=True)
            (tmp_path / d / "agent.md").write_bytes(content)
        pkg = _fake_pkg(("agent.md", content))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        out = capsys.readouterr().out
        assert "unchanged" in out
        assert "created" not in out

    def test_output_updated(self, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
        for d in [".claude/agents", ".github/agents"]:
            (tmp_path / d).mkdir(parents=True)
            (tmp_path / d / "agent.md").write_bytes(b"old")
        pkg = _fake_pkg(("agent.md", b"new"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        assert "updated" in capsys.readouterr().out

    def test_multiple_files_all_synced(self, tmp_path: Path) -> None:
        pkg = _fake_pkg(("a.md", b"A"), ("b.md", b"B"))
        with patch("butler.commands.sync.files", return_value=pkg):
            _sync_agents(tmp_path)
        for name in ("a.md", "b.md"):
            assert (tmp_path / ".claude" / "agents" / name).exists()
            assert (tmp_path / ".github" / "agents" / name).exists()


class TestSyncCli:
    def test_exit_code_zero(self, runner: CliRunner) -> None:
        with patch("butler.commands.sync._sync_agents"):
            result = runner.invoke(app, ["sync"])
        assert result.exit_code == 0

    def test_calls_sync_agents_once(self, runner: CliRunner) -> None:
        calls: list[Path] = []
        with patch("butler.commands.sync._sync_agents", side_effect=calls.append):
            runner.invoke(app, ["sync"])
        assert len(calls) == 1
