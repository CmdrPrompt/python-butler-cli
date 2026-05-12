# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- Sex dagliga dev-kommandon (`butler lint`, `butler fix`, `butler stage`, `butler test`, `butler install`, `butler setup`) som proxierar rätt Makefile-target, strömmar output direkt till terminalen och löser projektrot automatiskt från valfri underkatalog (TASK-002)
- `butler` CLI entry point (Click-grupp) med `--help` och konfigurerbar projektstruktur via `[tool.butler]` i `pyproject.toml` (TASK-001)
