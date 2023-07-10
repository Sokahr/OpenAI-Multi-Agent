import pytest
from click.testing import CliRunner
from src.main_menu import MainMenu


@pytest.fixture
def runner():
    return CliRunner()


def test_display_menu(runner):
    main_menu = MainMenu()
    result = runner.invoke(main_menu.display_menu)
    assert result.exit_code == 0
    assert "Please select an option:" in result.output


def test_start_new_project(runner):
    main_menu = MainMenu()
    result = runner.invoke(main_menu.start_new_project)
    assert result.exit_code == 0
    assert "Starting a new project..." in result.output


def test_invalid_option(runner):
    main_menu = MainMenu()
    result = runner.invoke(main_menu.execute_command, ["5"])
    assert result.exit_code == 0
    assert "Invalid option. Please enter a valid option." in result.output

# Add more test functions to cover other scenarios and functionalities
