# TASK-010 Testläsbarhet: lägg till assertion-meddelanden

## Status

todo

## Description

**Test quality improvement:** Lägg till tydliga felmeddelanden på de 7 assertions i
`test_all_known_keys_override_defaults` (eller på de parametriserade tester som
ersätter det, se TASK-008).

**Property:** Understandable
**Current blended score:** 8.0
**Target score:** 9.0
**Evidence:** `tests/test_config.py:33`

När ett test med flera assertions misslyckas visar pytest bara `AssertionError`.
Med ett explicit meddelande — t.ex. `assert cfg.src_dir == "app", "src_dir should
be overridden by [tool.butler]"` — kan en ny teammedlem förstå kravet direkt från
felinformationen utan att behöva läsa koden.

OBS: Om TASK-008 genomförs och testet ersätts med parametriserade per-nyckel-tester
är parametriserade testnamnet (`test_...[src_dir-app]`) tillräckligt diagnostiskt
och assertion-meddelanden behövs inte. I det fallet stängs denna task som löst av
TASK-008.

## Branch

**Branch name:** `task/010-test-understandable-assertion-messages`
**Switch/create:** `git checkout -b task/010-test-understandable-assertion-messages`
**Make target:** `make branch-task f=TASK-010`

## Files

- `tests/test_config.py` — lägg till assertion-meddelanden, eller stäng som löst av TASK-008

## Acceptance criteria

- [ ] Identifierade tester refaktorerade för att adressera fyndet
- [ ] Varje assertion i ett test med flera assertions har ett beskrivande felmeddelande,
      ELLER testet är uppdelat i per-nyckel-tester (TASK-008) som gör meddelanden onödiga
- [ ] Farley Index re-evalueras — blended score för Understandable är inte lägre än 8.0
- [ ] `make lint && make test` passerar
- [ ] CHANGELOG.md uppdaterad

## Completion

<!-- fylls i när tasken är klar -->
