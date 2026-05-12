# TASK-001 CLI-skelett med konfigurationsläsning

## Status

todo

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

- [ ] `butler --help` skriver ut en kommandolista utan fel
- [ ] `ButlerConfig` läser korrekt från `[tool.butler]` i `pyproject.toml`
- [ ] Saknad `[tool.butler]`-sektion returnerar alla defaults
- [ ] `make lint` och `make test` passerar

## Branch

**Switch/create:** `git checkout -b task/001-cli-skeleton`

## Completion

**Stage:** `git add src/butler/cli.py src/butler/config.py tests/test_config.py pyproject.toml CHANGELOG.md docs/tasks/TASK-001-cli-skeleton.md`
**Commit:** `git commit -m "Add CLI skeleton with config loading"`
