# TASK-002 Daily dev commands

## Status

done

## Description

Implementera sex dagliga dev-kommandon i butler CLI som proxierar Makefile-targets.
Varje kommando strömmar output direkt till stdout/stderr och returnerar samma exit-kod
som `make`. Projektrot löses från cwd via `find_project_root()` i config-modulen.

| Kommando       | Proxierat target        |
|----------------|-------------------------|
| butler lint    | make lint               |
| butler fix     | make fix                |
| butler stage   | make stage-current-task |
| butler test    | make test               |
| butler install | make install            |
| butler setup   | make setup              |

## Branch

**Branch name:** `task/002-daily-dev-commands`
**Switch/create:** `git checkout -b task/002-daily-dev-commands`
**Make target:** `make branch-task f=TASK-002`

## Acceptance criteria

- [x] `butler lint` proxierar `make lint` och returnerar samma exit-kod
- [x] `butler fix` proxierar `make fix` och returnerar samma exit-kod
- [x] `butler stage` proxierar `make stage-current-task` och returnerar samma exit-kod
- [x] `butler test` proxierar `make test` och returnerar samma exit-kod
- [x] `butler install` proxierar `make install` och returnerar samma exit-kod
- [x] `butler setup` proxierar `make setup` och returnerar samma exit-kod
- [x] Output strömmas direkt (ingen capture_output)
- [x] Projektrot löses via `find_project_root()` (fungerar från underkatalog)
- [x] Enhetstester med mockad subprocess täcker alla sex kommandon (TDD)
- [x] `make lint && make test` passerar

## Completion

**Date:** 2026-05-12
**Summary:** Lade till `find_project_root()` i config.py och sex Click-kommandon i `commands/dev.py` som proxierar `make lint/fix/stage-current-task/test/install/setup`. Kommandona strömmar output direkt och propagerar exit-kod via sys.exit. 18 tester skrivna TDD-style (röd → grön). Täckning 81% → 90%. `make lint && make test` passerar med 24 tester.
**Files changed:**

- `src/butler/commands/__init__.py` — created
- `src/butler/commands/dev.py` — created
- `src/butler/config.py` — modified
- `src/butler/cli.py` — modified
- `tests/test_dev_commands.py` — created
- `docs/tasks/TASK-002-daily-dev-commands.md` — modified
- `CHANGELOG.md` — modified

**Branch:** `git checkout task/002-daily-dev-commands`
**Stage:** `git add src/butler/commands/__init__.py src/butler/commands/dev.py src/butler/config.py src/butler/cli.py tests/test_dev_commands.py docs/tasks/TASK-002-daily-dev-commands.md CHANGELOG.md`
**Commit:** `Add daily dev commands: lint, fix, stage, test, install, setup`
