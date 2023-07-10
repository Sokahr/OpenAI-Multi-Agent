"""
OpenAI MAC CLI Application Setup.

This file defines the project setup and dependencies for the OpenAI MAC CLI application.
It includes metadata about the project, such as name, version, author, and dependencies.
"""

from setuptools import find_packages, setup

setup(
    name="openai-mac-cli",
    version="1.0.0",
    author="Sokahr",
    description="CLI application OpenAI MAC",
    packages=find_packages(),
    install_requires=[
        "Click>=7.0",
        "pytest>=6.0",
        "ruff>=1.0"
    ],
    entry_points={
        "console_scripts": [
            "openai-mac=cli_app:main"
        ]
    },
)
