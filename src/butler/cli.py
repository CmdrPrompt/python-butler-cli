"""Butler CLI root group."""

import click

from butler.commands.dev import fix, install, lint, setup, stage, test_cmd
from butler.commands.sync import sync
from butler.commands.task import task


@click.group()
def app() -> None:
    """Butler CLI."""


app.add_command(lint)
app.add_command(fix)
app.add_command(stage)
app.add_command(test_cmd, name="test")
app.add_command(install)
app.add_command(setup)
app.add_command(sync)
app.add_command(task)


if __name__ == "__main__":
    app()
