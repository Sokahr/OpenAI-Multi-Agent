"""
This module implements the main menu functionality for the OpenAI MAC application.
It provides a command-line interface (CLI) with options for starting a new project, loading an existing project,
accessing help, and exiting the program.
"""

import click


class MainMenu:
    """
    The main menu of the OpenAI MAC application.
    """

    @staticmethod
    def display_menu():
        """
        Display the main menu options on the terminal screen.
        """
        click.clear()  # Clear the terminal screen
        click.echo(click.style("=========================================================", fg="green"))
        click.echo(click.style("                      OpenAI MAC                      ", fg="green"))
        click.echo(click.style("=========================================================", fg="green"))
        click.echo()
        click.echo("Please select an option:")
        click.echo("[1] Start a new project")
        click.echo("[2] Load existing project")
        click.echo("[3] Help")
        click.echo("[4] Exit")
        click.echo()

    @staticmethod
    def receive_user_input():
        """
        Prompt the user to enter their choice and return it.
        """
        return click.prompt("Enter your choice", type=int)

    def execute_command(self, choice):
        """
        Execute the appropriate command based on the user's choice.

        Args:
            choice (int): The user's choice representing the selected option.
        """
        if choice == 1:
            self.start_new_project()
        elif choice == 2:
            self.load_existing_project()
        elif choice == 3:
            self.display_help()
        elif choice == 4:
            self.exit_program()
        else:
            click.echo(click.style("Invalid option. Please enter a valid option.", fg="red"))

    @staticmethod
    def start_new_project():
        """
        Start a new project.
        """
        click.echo("Starting a new project...")
        # Add the logic to handle starting a new project here

    @staticmethod
    def load_existing_project():
        """
        Load an existing project.
        """
        click.echo("Loading an existing project...")
        # Add the logic to handle loading an existing project here

    @staticmethod
    def display_help():
        """
        Display help information.
        """
        click.echo("Displaying help...")
        # Add the logic to display help information here

    @staticmethod
    def exit_program():
        """
        Exit the program.
        """
        click.echo("Exiting the program...")
        # Add the logic to exit the program here

    def handle_main_menu(self):
        """
        Handle the main menu functionality.

        This method displays the main menu, receives user input, and executes the corresponding command based on the input.
        It continues to loop until the user chooses to exit the program.
        """
        while True:
            self.display_menu()
            choice = self.receive_user_input()
            self.execute_command(choice)


# Create an instance of the MainMenu class
main_menu = MainMenu()
main_menu.handle_main_menu()
