# TASK-003 Clarify agent invocation context

## Status

done

## Description

Förtydliga i `workflow-guardian.agent.md` och `CLAUDE.md` att ett `@`-omnämnande
i Claude Code laddar agentinstruktionerna i huvudkonversationen — Claude agerar
SOM Workflow Guardian, spawnar inte en ny instans. Workflow Guardian ska spawna
Implementation Worker (inte sig själv) för kodningsfasen.

## Branch

**Branch name:** `task/003-clarify-agent-invocation`
**Switch/create:** `git checkout -b task/003-clarify-agent-invocation`
**Make target:** `make branch-task f=TASK-003`

## Acceptance criteria

- [x] `workflow-guardian.agent.md` har en ny sektion "Invocation Context" som förklarar `@`-omnämnande vs Agent tool spawn
- [x] `CLAUDE.md` har en ny sektion "Agent Invocation" med samma kärnbudskap
- [x] Båda filerna är uppdaterade i `.claude/agents/` och `.github/agents/`
- [x] `make lint` passerar

## Completion

**Date:** 2026-05-12
**Summary:** Lade till "Invocation Context"-sektion i workflow-guardian.agent.md (både .claude/agents/ och .github/agents/) och "Agent Invocation"-sektion i CLAUDE.md. Förklarar att @-omnämnande i Claude Code innebär att Claude agerar som agenten direkt — inte spawnar en ny instans — och att Implementation Worker ska delegeras för kodning.
**Files changed:**

- `.claude/agents/workflow-guardian.agent.md` — modified
- `.github/agents/workflow-guardian.agent.md` — modified
- `CLAUDE.md` — modified
- `docs/tasks/TASK-003-clarify-agent-invocation.md` — modified
- `CHANGELOG.md` — modified

**Branch:** `git checkout task/003-clarify-agent-invocation`
**Stage:** `git add .claude/agents/workflow-guardian.agent.md .github/agents/workflow-guardian.agent.md CLAUDE.md docs/tasks/TASK-003-clarify-agent-invocation.md CHANGELOG.md`
**Commit:** `git commit -m "Clarify agent invocation context in Workflow Guardian and CLAUDE.md"`
