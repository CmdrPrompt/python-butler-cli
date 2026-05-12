"""Butler CLI root group."""

import click


@click.group()
def app() -> None:
    """Butler CLI."""


if __name__ == "__main__":
    app()
