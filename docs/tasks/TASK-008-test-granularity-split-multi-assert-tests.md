# TASK-008 Testgranularitet: dela upp multi-assertion-tester

## Status

todo

## Description

**Test quality improvement:** Dela upp `test_all_known_keys_override_defaults` i
per-nyckel-tester (eller `@pytest.mark.parametrize`) och ersätt OR-assertion i
`test_task_branch_fails_without_id_on_non_task_branch` med exakt förväntad sträng.

**Property:** Granular
**Current blended score:** 7.0
**Target score:** 8.5
**Evidence:** `tests/test_config.py:33`, `tests/test_task_commands.py:71`

### Problem 1 — `test_config.py:33`

`test_all_known_keys_override_defaults` innehåller 7 separata `assert`-satser för
7 olika config-nycklar. Om ett assert misslyckas visas bara `AssertionError` och
man måste läsa koden för att förstå vilken nyckel som är trasig.

Åtgärd: parametrisera med `@pytest.mark.parametrize("key,value", [...])` eller
dela upp i sju separata testfunktioner.

### Problem 2 — `test_task_commands.py:71`

```python
assert "task ID" in result.output or "TASK" in result.output
```

OR-betingelsen accepterar vilket felmeddelande som helst som råkar innehålla
antingen "task ID" eller "TASK". Specifikationen är otydlig om exakt vilket
meddelande som ska produceras.

Åtgärd: fastställ det exakta felmeddelandet i `_resolve_task_id` och
assertera mot det strängen direkt.

## Branch

**Branch name:** `task/008-test-granularity-split-multi-assert-tests`
**Switch/create:** `git checkout -b task/008-test-granularity-split-multi-assert-tests`
**Make target:** `make branch-task f=TASK-008`

## Files

- `tests/test_config.py` — dela upp eller parametrisera `test_all_known_keys_override_defaults`
- `tests/test_task_commands.py` — ersätt OR-assertion med exakt sträng
- `src/butler/commands/task.py` — ev. justera felmeddelande för att vara testdrivbart

## Acceptance criteria

- [ ] Identifierade tester refaktorerade för att adressera fyndet
- [ ] `test_all_known_keys_override_defaults` ersatt med parametriserat test eller per-nyckel-tester
- [ ] OR-assertion i `test_task_branch_fails_without_id_on_non_task_branch` ersatt med
      exakt strängjämförelse
- [ ] Farley Index re-evalueras — blended score för Granular är inte lägre än 7.0
- [ ] `make lint && make test` passerar
- [ ] CHANGELOG.md uppdaterad

## Completion

<!-- fylls i när tasken är klar -->
