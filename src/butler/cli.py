"""Butler CLI root group."""

import click

from butler.commands.dev import fix, install, lint, setup, stage, test_cmd


@click.group()
def app() -> None:
    """Butler CLI."""


app.add_command(lint)
app.add_command(fix)
app.add_command(stage)
app.add_command(test_cmd, name="test")
app.add_command(install)
app.add_command(setup)


if __name__ == "__main__":
    app()
