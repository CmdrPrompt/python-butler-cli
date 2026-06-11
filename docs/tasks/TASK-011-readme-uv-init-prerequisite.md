# TASK-011 README: förtydliga uv init-förutsättning för nya projekt

## Status

done

## Description

`uv add` kräver att en `pyproject.toml` redan finns i projektet — till
skillnad från t.ex. `npm install` skapar `uv add` inget nytt projekt åt dig.
En användare som följer README:ns "Adopting in a new project" i ett helt
tomt projekt får felet:

```text
error: No `pyproject.toml` found in current directory or any parent directory
```

Lägg till ett förtydligande steg 0 (`uv init`) i README:ns avsnitt
"Adopting in a new project" samt en motsvarande not i
`docs/REQUIREMENTS.md` under "Distributionsmodell", som beskriver att
projektet måste ha en `pyproject.toml` (t.ex. via `uv init`) innan
`uv add` kan köras.

Detta är en dokumentationsändring — ingen kod eller tester berörs.

## Branch

**Branch name:** `task/011-readme-uv-init-prerequisite`
**Switch/create:** `git checkout -b task/011-readme-uv-init-prerequisite`
**Make target:** `make branch-task f=TASK-011`

## Files

- `README.md` — lägg till steg 0 (`uv init`) i "Adopting in a new project"
- `docs/REQUIREMENTS.md` — lägg till förutsättning i "Distributionsmodell"
- `CHANGELOG.md` — dokumentera ändringen

## Acceptance criteria

- [ ] README.md "Adopting in a new project" innehåller ett steg 0 som
      förklarar att `uv init` behövs för helt nya projekt utan `pyproject.toml`
- [ ] docs/REQUIREMENTS.md "Distributionsmodell" nämner samma förutsättning
- [ ] CHANGELOG.md uppdaterad
- [ ] `make lint` passerar (pymarkdown m.fl.)

## Completion

<!-- fylls i när tasken är klar -->