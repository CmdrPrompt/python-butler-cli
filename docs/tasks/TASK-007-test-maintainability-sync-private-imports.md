# TASK-007 Testunderhållbarhet: ersätt privata importer i sync-tester

## Status

todo

## Description

**Test quality improvement:** Ersätt direktimport av privata funktioner `_sync_file` och
`_sync_agents` med tester som använder det publika CLI-gränssnittet och verifierar
observerbara filsystemsutfall.

**Property:** Maintainable
**Current blended score:** 6.0
**Target score:** 8.0
**Evidence:** `tests/test_sync_command.py:12`

Idag importerar `test_sync_command.py` de privata funktionerna `_sync_file` och
`_sync_agents` direkt. Det betyder att ett enkelt internt namnbyte bryter 12 av 14
sync-tester (38 % av sviten) utan att något beteende faktiskt ändrats. Testerna
ska i stället driva mot det publika kontraktet:

- `_sync_file`-tester: kalla `runner.invoke(app, ["sync"])` och kontrollera att filer
  skapas/uppdateras/lämnas oförändrade i `tmp_path`. Alternativt behåll enhetstest
  för `_sync_file` men via ett eget `conftest`-fixture som inte binder sig till
  modulnamnet.
- `_sync_agents`-tester: driv via CLI-kommandot och verifiera filsystemsutfall och
  stdout — inte via intern anrop.

## Branch

**Branch name:** `task/007-test-maintainability-sync-private-imports`
**Switch/create:** `git checkout -b task/007-test-maintainability-sync-private-imports`
**Make target:** `make branch-task f=TASK-007`

## Files

- `tests/test_sync_command.py` — refaktorera bort privata importer

## Acceptance criteria

- [ ] Identifierade tester refaktorerade för att adressera fyndet
- [ ] `from butler.commands.sync import _sync_agents, _sync_file` tas bort från testfilen
- [ ] Alla befintliga beteenden (created/updated/unchanged, filtrering av icke-.md-filer,
      synkning till båda target-dirs) täcks fortfarande
- [ ] Farley Index re-evalueras — blended score för Maintainable är inte lägre än 6.0
- [ ] `make lint && make test` passerar
- [ ] CHANGELOG.md uppdaterad

## Completion

<!-- fylls i när tasken är klar -->
