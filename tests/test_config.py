"""Tests for butler configuration loading."""

from pathlib import Path

from butler.config import load_config


def test_missing_section_returns_all_defaults(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'my-project'\n")
    cfg = load_config(tmp_path)
    assert cfg.src_dir == "src"
    assert cfg.tests_dir == "tests"
    assert cfg.tasks_dir == "docs/tasks"
    assert cfg.project_description == "Describe your project here."
    assert cfg.requirements_path == "docs/REQUIREMENTS.md"
    assert cfg.project_make_target == "make help"


def test_missing_section_uses_directory_name_as_project_name(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'my-project'\n")
    cfg = load_config(tmp_path)
    assert cfg.project_name == tmp_path.name


def test_partial_section_merges_with_defaults(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[tool.butler]\nsrc_dir = 'app'\n")
    cfg = load_config(tmp_path)
    assert cfg.src_dir == "app"
    assert cfg.tests_dir == "tests"
    assert cfg.tasks_dir == "docs/tasks"


def test_all_known_keys_override_defaults(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text(
        "[tool.butler]\n"
        "src_dir = 'app'\n"
        "tests_dir = 'spec'\n"
        "tasks_dir = 'work/tasks'\n"
        "project_name = 'my-app'\n"
        "project_description = 'My app.'\n"
        "requirements_path = 'docs/REQ.md'\n"
        "project_make_target = 'make run'\n"
    )
    cfg = load_config(tmp_path)
    assert cfg.src_dir == "app"
    assert cfg.tests_dir == "spec"
    assert cfg.tasks_dir == "work/tasks"
    assert cfg.project_name == "my-app"
    assert cfg.project_description == "My app."
    assert cfg.requirements_path == "docs/REQ.md"
    assert cfg.project_make_target == "make run"


def test_unknown_keys_are_ignored(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[tool.butler]\nunknown_key = 'value'\n")
    cfg = load_config(tmp_path)
    assert not hasattr(cfg, "unknown_key")
    assert cfg.src_dir == "src"


def test_no_pyproject_returns_defaults(tmp_path: Path) -> None:
    cfg = load_config(tmp_path)
    assert cfg.src_dir == "src"
    assert cfg.project_name == tmp_path.name
