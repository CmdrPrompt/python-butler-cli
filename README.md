# python-butler-cli

CLI distribution of python-butler — spec-driven, TDD development workflow as a `butler` command.

Install once, run everywhere. No git subtree required.

## What's included

- **`butler` CLI** — linting, testing, and task workflow commands built on [uv](https://github.com/astral-sh/uv)
- **8 governance agents** — synced to `.claude/agents/` and `.github/agents/` in your project
- **Zero config defaults** — works out of the box, override via `[tool.butler]` in `pyproject.toml`

## Prerequisites

- [uv](https://github.com/astral-sh/uv) — install once with `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [gh](https://cli.github.com) — needed for `butler task pr` and `butler task merge`

## Adopting in a new project

```bash
# 1. Add butler as a dev dependency
uv add --dev "python-butler-cli @ git+https://github.com/CmdrPrompt/python-butler-cli.git"

# 2. Sync governance agents to your project
butler sync

# 3. Install dependencies and activate pre-commit hooks
butler install
```

`butler sync` copies 8 agent files to `.claude/agents/` and `.github/agents/`. It is idempotent — re-run it whenever you want to pull updated agents from a newer version of butler.

## Adopting in an existing project

Same steps as above. If you already have agent files, `butler sync` reports each file as `created`, `updated`, or `unchanged` — it will not silently overwrite files that are already up to date.

## Keeping butler up to date

```bash
uv add --dev "python-butler-cli @ git+https://github.com/CmdrPrompt/python-butler-cli.git"
butler sync   # pull updated agents into your project
```

Pin to a specific release for reproducible builds:

```bash
uv add --dev "python-butler-cli @ git+https://github.com/CmdrPrompt/python-butler-cli.git@v1.0.0"
```

## Daily commands

```bash
butler lint     # ruff check + format check + mypy + bandit + pymarkdown + complexipy
butler fix      # ruff fix + ruff format + pymarkdown fix
butler stage    # auto-fix and re-stage currently staged files
butler test     # pytest with coverage
butler install  # create venv, install dependencies, activate pre-commit
butler setup    # install uv if missing
```

## Task workflow

```bash
butler task branch [TASK-NNN]  # create / switch to task branch
# implement, then update CHANGELOG.md and task file
butler task stage [TASK-NNN]   # auto-fix and stage files listed in task file
butler task commit             # commit using message from task file
butler task pr                 # open GitHub PR
butler task merge              # squash-merge when ready, pull main
```

The task ID is derived automatically from the branch name (`task/NNN-...`) if no argument is given.

## Configuration

Override defaults in your project's `pyproject.toml`:

```toml
[tool.butler]
src_dir             = "src"           # default: "src"
tests_dir           = "tests"         # default: "tests"
tasks_dir           = "docs/tasks"    # default: "docs/tasks"
project_name        = "my-project"    # default: directory name
project_description = "My project."  # default: "Describe your project here."
requirements_path   = "docs/REQUIREMENTS.md"
project_make_target = "make help"
```

## Agents

Eight agents cover the full development workflow, available in both Claude Code and GitHub Copilot.

```
requirements-drafter → workflow-guardian → implementation-worker → pr-reviewer → merge
                               ↑
             bug-triage ───────┤
 characterization-test-writer ─┘
             dependency-auditor  (periodic / pre-release)
             test-design-reviewer (on demand)
```

| Agent | When | Purpose |
|---|---|---|
| `requirements-drafter` | Before coding | Turns vague ideas into confirmed, testable requirements |
| `workflow-guardian` | Gate | Enforces task branches, TDD, and commit discipline |
| `implementation-worker` | Coding | Implements approved work, runs lint/test, commits |
| `pr-reviewer` | Before merge | Checks scope, tests, changelog, and acceptance criteria |
| `bug-triage` | On demand | Finds bugs without fixing — produces task files |
| `characterization-test-writer` | Before refactoring | Documents existing behavior with tests |
| `dependency-auditor` | Periodic | Audits for CVEs, outdated packages, license issues |
| `test-design-reviewer` | On demand | Evaluates test quality and generates Farley Index reports |

### Invoking agents

**Claude Code** — type `@agent-name` in chat, or describe your task and Claude suggests one automatically.

**GitHub Copilot (VS Code 1.101+)** — use the **dropdown** at the bottom of the Copilot Chat panel to select an agent.

## Conventions

- Tasks live in `docs/tasks/TASK-<NNN>-short-description.md`
- Every task runs on its own `task/<NNN>-short-description` branch
- Always commit via `butler task commit`, never `git commit` directly

## License

[MIT](LICENSE)
