"""Command Line Interface (CLI) for openai-mac."""

import click


@click.command()
def mac():
    """OpenAI MAC CLI application."""
    display_main_menu()


def display_main_menu():
    """Display the main menu."""
    click.clear()
    click.echo(
        """
    =========================================================
                          OpenAI MAC
    =========================================================

    Please select an option:
    [1] Start a new project
    [2] Load existing project
    [3] Help
    [4] Exit
"""
    )
    choice = click.prompt("    Enter your choice", type=str, default='4', show_default=False)
    main_menu_choice(choice)


def new_project():
    """Start a new project."""
    click.echo("New Project Setup")
    pass


def load_project():
    """Load an existing project."""
    click.echo("Load Project")
    pass


def cli_help():
    """Display the help menu."""
    click.echo("Help")
    pass


def main_menu_choice(choice):
    """Process the main menu choice."""
    if choice == '1':
        new_project()
    elif choice == 'new':
        new_project()
    elif choice == 'start':
        new_project()
    elif choice == '2':
        load_project()
    elif choice == '3':
        cli_help()
    elif choice == '4':
        exit()


if __name__ == '__main__':
    mac()
