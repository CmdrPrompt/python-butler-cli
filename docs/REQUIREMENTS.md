# python-butler-cli — Kravspecifikation

## Syfte

`python-butler-cli` är ett pip-installerbart Python-paket som exponerar
butlerns arbetsflöde som ett `butler`-CLI-kommando. Det är ett komplement
till `python-butler` (subtree-varianten) och avsett för projekt som vill
slippa git subtree-koppling.

## Icke-mål

- Ersätter inte `python-butler` — befintliga subtree-projekt berörs inte.
- Publiceras inte nödvändigtvis på PyPI; distribution via git-URL räcker.

---

## REQ-01 Daglig utveckling

**Som** en utvecklare i ett projekt som använder butler-cli
**vill jag** kunna köra lint, fix, stage och test via `butler`-kommandon
**så att** jag inte behöver känna till underliggande verktyg (ruff, mypy, bandit etc.)

### Användningsfall

- `butler lint` — kör ruff check, ruff format --check, mypy, bandit,
  pymarkdown och complexipy mot projektet
- `butler fix` — kör ruff check --fix, ruff format, pymarkdown fix
- `butler stage` — kör fix och re-stagear redan stagade filer
- `butler test` — kör pytest med coverage
- `butler install` — skapar venv, installerar beroenden, aktiverar pre-commit
- `butler setup` — installerar uv om det saknas

---

## REQ-02 Uppgiftsflöde

**Som** en utvecklare som följer butler-arbetsflödet
**vill jag** hantera task-branchar och commits via `butler task`-kommandon
**så att** arbetsflödet är identiskt oavsett om projektet använder subtree eller CLI

### Användningsfall

- `butler task branch [TASK-NNN]` — skapar/byter till task-branch
- `butler task stage  [TASK-NNN]` — kör fix och stagear filer listade i task-filen
- `butler task commit [TASK-NNN]` — committar med meddelande från task-filen
- `butler task pr     [TASK-NNN]` — öppnar GitHub PR
- `butler task merge  [TASK-NNN]` — squash-mergar PR och pullar main

Om TASK-NNN utelämnas härleds task-ID från aktuell branch (`task/NNN-...`).

---

## REQ-03 Konfiguration

**Som** en projektägare
**vill jag** konfigurera butlers beteende per projekt i `pyproject.toml`
**så att** jag inte behöver hårdkoda projektspecifika värden i kommandon

### Konfigurationsnycklar (`[tool.butler]`)

| Nyckel | Default | Motsvarar |
|---|---|---|
| `src_dir` | `"src"` | `SRC_DIR` |
| `tests_dir` | `"tests"` | `TESTS_DIR` |
| `tasks_dir` | `"docs/tasks"` | `TASKS_DIR` |
| `project_name` | katalogens namn | `PROJECT_NAME` |
| `project_description` | `"Describe your project here."` | `PROJECT_DESCRIPTION` |
| `requirements_path` | `"docs/REQUIREMENTS.md"` | `REQUIREMENTS_PATH` |
| `project_make_target` | `"make help"` | `PROJECT_MAKE_TARGET` |

---

## REQ-04 Scaffolding

**Som** en utvecklare som startar ett nytt projekt
**vill jag** generera styrningsfiler interaktivt via butler
**så att** jag får CLAUDE.md, agentfiler och projektkonfiguration på ett ställe

### Användningsfall

- `butler init` — interaktiv scaffolding (motsvarar `make init-project`)
- `butler generate governance` — genererar CLAUDE.md, copilot-instructions.md
  och agentfiler från mallar
- `butler generate pyproject` — genererar pyproject.toml från mall
- `butler generate gitignore` — genererar .gitignore från mall
- `butler generate pre-commit` — genererar .pre-commit-config.yaml från mall

Alla `generate`-kommandon avbryter om målfilen redan finns, såvida inte
`--force` anges.

---

## REQ-05 Agentdistribution

**Som** en projektägare
**vill jag** att butler kopierar ut agentfiler till rätt platser i projektet
**så att** Claude Code och GitHub Copilot har tillgång till dem utan manuellt arbete

### Användningsfall

- `butler sync` — kopierar agentfiler till `.claude/agents/` och `.github/agents/`
  utifrån paketets inbyggda mallar; idempotent och jämför checksummor

---

## REQ-06 Versionshantering

**Som** en projektägare
**vill jag** kunna kontrollera om butler-cli är uppdaterat
**så att** jag inte kör föråldrade agenter eller arbetsflöden

### Användningsfall

- `butler check` — jämför installerad paketversion med senaste release på GitHub
- `butler update` — instruerar användaren att köra `uv add --dev
  "python-butler-cli @ git+..."` med senaste version (uppdaterar inte själv)

---

## Distributionsmodell

Paketet distribueras via git-URL och kräver inte PyPI:

```bash
uv add --dev \
  "python-butler-cli @ git+https://github.com/CmdrPrompt/python-butler-cli.git"
```

Versionspin med tagg:

```bash
uv add --dev \
  "python-butler-cli @ git+https://github.com/CmdrPrompt/python-butler-cli.git@v1.0.0"
```
