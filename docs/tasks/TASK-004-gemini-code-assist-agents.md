# TASK-004 Gemini Code Assist agent-generering

## Status

backlog

> **Prioritet: Låg — utökning.**
> Hanteras efter att grundfunktionaliteten i REQ-01 — REQ-06 är komplett och stabil.
> Inget blockerar övrig utveckling.

## Description

Lägg till stöd för att generera agentfiler anpassade för Gemini Code Assist,
parallellt med de befintliga Claude Code- och GitHub Copilot-agenterna.

Idag hanterar butler två agentuppsättningar med identisk logik men
plattformsspecifika verktygsnamn:

- `.claude/agents/` — Claude Code (verktyg: `read, search, edit, execute, todo, agent`)
- `.github/agents/` — GitHub Copilot (verktyg: `codebase, terminal, changes, githubRepo`)

Denna task lägger till en tredje:

- `.gemini/agents/` — Gemini Code Assist (verktyg: `read_file, write_file,
  search_files, run_terminal_cmd`, m.fl.)

Generering sker via `butler sync` (REQ-05) och `butler generate governance` (REQ-04),
med mallar i det inbyggda paketets mallkatalog.

## Krav som berörs

Kräver ett nytt krav i `docs/REQUIREMENTS.md` — förslag: **REQ-07 Gemini Code Assist-stöd**:

> **Som** en projektägare som använder Gemini Code Assist
> **vill jag** att `butler sync` och `butler generate governance` även genererar agentfiler
> i `.gemini/agents/`
> **så att** Gemini Code Assist har tillgång till samma arbetsflödesagenter som
> Claude Code och GitHub Copilot.

### Användningsfall

- `butler sync` — kopierar även Gemini-agenter till `.gemini/agents/`
- `butler generate governance` — inkluderar `.gemini/agents/` i genererade filer
- Konfigurationsnyckel `gemini_enabled` (default: `false`) i `[tool.butler]`
  styr om Gemini-filer genereras

## Branch

**Branch name:** `task/004-gemini-code-assist-agents`
**Switch/create:** `git checkout -b task/004-gemini-code-assist-agents`
**Make target:** `make branch-task f=TASK-004`

## Acceptance criteria

- [ ] `docs/REQUIREMENTS.md` innehåller REQ-07 med godkänt kravtext
- [ ] Mallarna för samtliga sju agenter finns som Gemini-varianter i paketets mallkatalog
- [ ] `butler sync` genererar `.gemini/agents/*.agent.md` när `gemini_enabled = true`
- [ ] `butler generate governance` inkluderar Gemini-filer
- [ ] `ButlerConfig` har ett nytt fält `gemini_enabled: bool = False`
- [ ] Alla befintliga tester passerar; Gemini-stödet täcks av nya enhetstester
- [ ] `make lint` passerar
- [ ] CHANGELOG.md är uppdaterad

## Beroenden

- REQ-04 (scaffolding) måste vara implementerat
- REQ-05 (agentdistribution via `butler sync`) måste vara implementerat
- REQ-06 (versionshantering) behöver inte vara klart

## Anteckningar

Gemini Code Assists agentformat och exakta verktygsnamn bör verifieras mot
aktuell Gemini Code Assist-dokumentation när tasken påbörjas — formatet kan
ha ändrats sedan detta skrevs (2026-05-13).
