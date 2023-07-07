from setuptools import setup, find_packages

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
