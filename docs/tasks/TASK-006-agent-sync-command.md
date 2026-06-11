# TASK-006 Agent sync command

## Status
done

## Description

Implementera `butler sync` — ett kommando som kopierar paketets inbyggda agentfiler
till `.claude/agents/` och `.github/agents/` i det konsumerande projektet.

Agentfilerna lagras som paketresurser under `src/butler/agents/` och läses via
`importlib.resources`. Kommandot är idempotent: filer som redan är identiska
(checksumma) skrivs inte om.

**Resursplacering:** `src/butler/agents/` (kopieras med paketet via `package_data`)

## Branch
**Branch name:** `task/006-agent-sync-command`
**Switch/create:** `git checkout -b task/006-agent-sync-command`
**Make target:** `make branch-task f=TASK-006`

## Acceptance criteria
- [ ] `src/butler/agents/` skapas och innehåller minst en agentfil (workflow-guardian eller liknande)
- [ ] `butler sync` kopierar filer till `.claude/agents/` och `.github/agents/` i CWD
- [ ] Idempotent: redan identiska filer skrivs inte om, output visar "unchanged"
- [ ] Uppdaterade filer skrivs och output visar "updated"
- [ ] Nya filer skapas och output visar "created"
- [ ] `package_data` i `pyproject.toml` inkluderar `butler/agents/*`
- [ ] Tester täcker created/updated/unchanged-scenarierna
- [ ] `make lint && make test` passerar
- [ ] Täckning ≥ 93 %
- [ ] `CHANGELOG.md` uppdaterad

## Completion
**Date:** 2026-06-11
**Summary:** Implementerade `butler sync` med `importlib.resources`, idempotent checksumma-jämförelse och output per fil. Inkluderade 8 agentfiler i paketet under `src/butler/agents/`. 14 nya tester, täckning 94 %.
**Files changed:**
- `src/butler/agents/__init__.py` — skapad (gör katalogen till paketresurs)
- `src/butler/agents/*.agent.md` — 8 agentfiler inkluderade i paketet
- `src/butler/commands/sync.py` — skapad
- `tests/test_sync_command.py` — skapad
- `src/butler/cli.py` — registrerar sync-kommandot
- `pyproject.toml` — lägger till package-data för butler.agents
- `CHANGELOG.md` — uppdaterad
**Branch:** `git checkout task/006-agent-sync-command`
**Stage:** `git add src/butler/agents/ src/butler/commands/sync.py tests/test_sync_command.py src/butler/cli.py pyproject.toml CHANGELOG.md docs/tasks/TASK-006-agent-sync-command.md .github/agents/test-design-reviewer.agent.md`
**Commit:** `git commit -m "Add butler sync command for agent distribution (REQ-05)"`
