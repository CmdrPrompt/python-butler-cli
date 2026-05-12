# TASK-001 CLI-skelett med konfigurationsläsning

## Status

done

## Description

Sätt upp det minsta möjliga CLI-skelettet så att `butler --help` fungerar och
konfigurationsläsning från `[tool.butler]` i `pyproject.toml` är på plats.
Ingen faktisk funktionalitet implementeras i denna task — bara grundstrukturen
som alla efterföljande kommandon bygger på.

Levererar:

- `click`-baserad entry point `butler` registrerad i `pyproject.toml`
- `src/butler/cli.py` — rot-grupp med `--help`
- `src/butler/config.py` — läser `[tool.butler]` och returnerar ett
  `ButlerConfig`-objekt med defaults för alla REQ-03-nycklar
- Tester för `config.py`: saknad sektion ger defaults, partiell sektion
  mergar med defaults, okända nycklar ignoreras

## Acceptance criteria

- [x] `butler --help` skriver ut en kommandolista utan fel
- [x] `ButlerConfig` läser korrekt från `[tool.butler]` i `pyproject.toml`
- [x] Saknad `[tool.butler]`-sektion returnerar alla defaults
- [x] `make lint` och `make test` passerar

## Branch

**Switch/create:** `git checkout -b task/001-cli-skeleton`

## Completion

**Date:** 2026-05-12
**Summary:** Skapade `butler` CLI-skelett med Click-grupp och `--help`. Lade till `src/butler/config.py` som läser `[tool.butler]` från `pyproject.toml` och returnerar `ButlerConfig` med defaults för alla REQ-03-nycklar. 6 tester täcker saknad sektion, partiell sektion, alla nycklar och okända nycklar. Täckning 81%.
**Files changed:**

- `pyproject.toml` — modified
- `src/butler/cli.py` — created
- `src/butler/config.py` — created
- `tests/__init__.py` — created
- `tests/test_config.py` — created
- `CHANGELOG.md` — created

**Branch:** `git checkout task/001-cli-skeleton`
**Stage:** `git add src/butler/cli.py src/butler/config.py tests/__init__.py tests/test_config.py pyproject.toml CHANGELOG.md docs/tasks/TASK-001-cli-skeleton.md`
**Commit:** `git commit -m "Add CLI skeleton with config loading"`
