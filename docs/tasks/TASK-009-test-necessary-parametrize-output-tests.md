# TASK-009 Testnödvändighet: slå ihop duplicerade output-tester

## Status

todo

## Description

**Test quality improvement:** Slå ihop `test_output_created`, `test_output_unchanged`
och `test_output_updated` i `TestSyncAgents` till ett enda `@pytest.mark.parametrize`-test.

**Property:** Necessary
**Current blended score:** 7.6
**Target score:** 8.5
**Evidence:** `tests/test_sync_command.py:86–111`

De tre testerna har identisk struktur:
1. Sätt upp initialtillstånd (tomt / identisk fil / annan fil)
2. Kör `_sync_agents` med fake-pkg
3. Assertera att ett specifikt ord finns i stdout

Enda variabeln är `(initial_content, new_content, expected_keyword)`. Att underhålla
tre kopior ökar risken att en ändring uppdaterar ett test men glömmer de andra.

Åtgärd: ersätt de tre metoderna med ett parametriserat test:

```python
@pytest.mark.parametrize(
    ("initial", "new_content", "expected"),
    [
        (None,    b"# Agent", "created"),
        (b"# Agent", b"# Agent", "unchanged"),
        (b"old",  b"new",    "updated"),
    ],
)
def test_output_status(self, tmp_path, capsys, initial, new_content, expected): ...
```

## Branch

**Branch name:** `task/009-test-necessary-parametrize-output-tests`
**Switch/create:** `git checkout -b task/009-test-necessary-parametrize-output-tests`
**Make target:** `make branch-task f=TASK-009`

## Files

- `tests/test_sync_command.py` — ersätt tre output-tester med ett parametriserat test

## Acceptance criteria

- [ ] Identifierade tester refaktorerade för att adressera fyndet
- [ ] `test_output_created`, `test_output_unchanged` och `test_output_updated` ersatta
      med ett `@pytest.mark.parametrize`-test
- [ ] Alla tre scenarion (created/unchanged/updated) täcks fortfarande
- [ ] Farley Index re-evalueras — blended score för Necessary är inte lägre än 7.6
- [ ] `make lint && make test` passerar
- [ ] CHANGELOG.md uppdaterad

## Completion

<!-- fylls i när tasken är klar -->
