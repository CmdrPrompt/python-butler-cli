# TASK-005 Uppgiftsflödeskommandon (butler task)

## Status

done

## Description

Implementera `butler task`-underkommandon som proxierar Makefile-targets för
task-arbetsflödet. Levererar REQ-02.

| Kommando | Proxierat target |
|---|---|
| `butler task branch [TASK-NNN]` | `make branch-task f=TASK-NNN` |
| `butler task stage  [TASK-NNN]` | `make stage-task f=TASK-NNN` |
| `butler task commit [TASK-NNN]` | `make commit-current-task` |
| `butler task pr     [TASK-NNN]` | `make pr-current-task` |
| `butler task merge  [TASK-NNN]` | `make merge-current-task` |

Om `TASK-NNN` utelämnas härleds task-ID från aktuell branch (`task/NNN-...`).
Om branch-namn inte matchar mönstret och inget argument ges, avbryts med tydligt felmeddelande.

## Branch

**Branch name:** `task/005-task-workflow-commands`
**Switch/create:** `git checkout -b task/005-task-workflow-commands`
**Make target:** `make branch-task f=TASK-005`

## Files

- `src/butler/commands/task.py` — ny fil med Click-grupp och fem underkommandon
- `src/butler/cli.py` — registrera task-gruppen
- `src/butler/config.py` — ev. `current_task_id()` hjälpfunktion
- `tests/test_task_commands.py` — ny testfil

## Acceptance criteria

- [x] `butler task branch TASK-005` kör `make branch-task f=TASK-005`
- [x] `butler task branch` (utan argument) härleder task-ID från branch-namn
- [x] `butler task stage TASK-005` kör `make stage-task f=TASK-005`
- [x] `butler task stage` (utan argument) härleder task-ID
- [x] `butler task commit` kör `make commit-current-task`
- [x] `butler task pr` kör `make pr-current-task`
- [x] `butler task merge` kör `make merge-current-task`
- [x] Om branch inte matchar `task/NNN-...` och inget argument ges → tydligt fel, exit 1
- [x] Alla kommandon strömmar output direkt och propagerar exit-kod
- [x] Enhetstester täcker alla kommandon och felfall (TDD)
- [x] `make lint && make test` passerar
- [x] CHANGELOG.md är uppdaterad

## Completion

**Date:** 2026-05-13
**Summary:** Lade till `src/butler/commands/task.py` med Click-grupp `task` och fem
underkommandon. Task-ID härleds från branch-namn via regex om argument saknas; tydligt
fel vid icke-matchande branch. Registrerade gruppen i `cli.py`. 17 tester skrivna
TDD-style. 41 tester totalt, lint passerar.
**Files changed:**

- `src/butler/commands/task.py` — created
- `src/butler/cli.py` — modified
- `tests/test_task_commands.py` — created
- `docs/tasks/TASK-005-task-workflow-commands.md` — modified
- `CHANGELOG.md` — modified

**Branch:** `git checkout task/005-task-workflow-commands`
**Stage:** `git add src/butler/commands/task.py src/butler/cli.py tests/test_task_commands.py docs/tasks/TASK-005-task-workflow-commands.md docs/tasks/TASK-004-gemini-code-assist-agents.md CHANGELOG.md`
**Commit:** `git commit -m "Add butler task subcommands for task workflow (REQ-02)"`
