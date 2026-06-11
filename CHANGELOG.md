# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- `butler sync` kopierar paketets inbyggda agentfiler (8 styrningsagenter) till `.claude/agents/` och `.github/agents/` i det konsumerande projektet; idempotent med checksumma-jämförelse och rapporterar `created`, `updated` eller `unchanged` per fil (TASK-006)
- `butler task`-underkommandon (`branch`, `stage`, `commit`, `pr`, `merge`) som proxierar Makefile-targets för uppgiftsarbetsflödet; task-ID härleds automatiskt från branch-namn om inget argument ges (TASK-005)
- Förtydligat i `workflow-guardian.agent.md` och `CLAUDE.md` att ett `@`-omnämnande i Claude Code innebär att Claude agerar som agenten i huvudkonversationen och ska spawna Implementation Worker (inte sig själv) för kodningsfasen (TASK-003)
- Sex dagliga dev-kommandon (`butler lint`, `butler fix`, `butler stage`, `butler test`, `butler install`, `butler setup`) som proxierar rätt Makefile-target, strömmar output direkt till terminalen och löser projektrot automatiskt från valfri underkatalog (TASK-002)
- `butler` CLI entry point (Click-grupp) med `--help` och konfigurerbar projektstruktur via `[tool.butler]` i `pyproject.toml` (TASK-001)
