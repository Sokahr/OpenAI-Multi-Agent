"""Test cases for the OpenAI MAC CLI application."""

import unittest

from click.testing import CliRunner

from src.cli import mac


class MainMenuTestCase(unittest.TestCase):
    """Test case for the main menu functionality of the OpenAI MAC CLI application."""

    def setUp(self):
        """Set up the test case by creating a CliRunner instance."""
        self.runner = CliRunner()

    def test_main_menu_display(self):
        """`mac` should display the main menu."""
        result = self.runner.invoke(mac)

        expected_output = """
    =========================================================
                          OpenAI MAC
    =========================================================

    Please select an option:
    [1] Start a new project
    [2] Load existing project
    [3] Help
    [4] Exit

    Enter your choice:"""
        assert result.output.strip() == expected_output.strip()

    def test_new_project_option_number_choice(self):
        """`mac` should display the new project menu when the user selects option 1."""
        result = self.runner.invoke(mac, input="1")

        assert 'New Project Setup' in result.output.strip()

    def test_new_project_option_text_choice_new(self):
        """`mac` should display the new project menu when the user selects option 'new'."""
        result = self.runner.invoke(mac, input="new")

        assert 'New Project Setup' in result.output.strip()

    def test_new_project_option_text_choice_start(self):
        """`mac` should display the new project menu when the user selects option 'start'."""
        result = self.runner.invoke(mac, input="start")

        assert 'New Project Setup' in result.output.strip()

    def test_load_project_option_number_choice(self):
        """`mac` should display the load project menu when the user selects option 2."""
        result = self.runner.invoke(mac, input="2")

        assert 'Load Project' in result.output.strip()

    def test_show_help_option_number_choice(self):
        """`mac` should display the help menu when the user selects option 3."""
        result = self.runner.invoke(mac, input="3")

        assert 'Help' in result.output.strip()

    def test_exit_option_number_choice(self):
        """`mac` should exit when the user selects option 4."""
        result = self.runner.invoke(mac, input="4")

        assert result.exit_code == 0


if __name__ == '__main__':
    unittest.main()
