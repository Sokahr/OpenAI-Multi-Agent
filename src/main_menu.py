import click


class MainMenu:

    @staticmethod
    def display_menu():
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
        return click.prompt("Enter your choice", type=int)

    def execute_command(self, choice):
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
        click.echo("Starting a new project...")
        # Add the logic to handle starting a new project here

    @staticmethod
    def load_existing_project():
        click.echo("Loading an existing project...")
        # Add the logic to handle loading an existing project here

    @staticmethod
    def display_help():
        click.echo("Displaying help...")
        # Add the logic to display help information here

    @staticmethod
    def exit_program():
        click.echo("Exiting the program...")
        # Add the logic to exit the program here

    def handle_main_menu(self):
        while True:
            self.display_menu()
            choice = self.receive_user_input()
            self.execute_command(choice)


# Create an instance of the MainMenu class
main_menu = MainMenu()
main_menu.handle_main_menu()
