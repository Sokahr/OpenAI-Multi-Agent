"""Tasks to invoke."""
from invoke import task


@task
def test(ctx):
    """Run pytest tests."""
    ctx.run("pytest ./")


@task
def lint(ctx):
    """Run the ruff linter."""
    ctx.run("ruff ./")


@task
def fix(ctx):
    """Run the ruff linter with the --fix flag."""
    ctx.run("ruff ./ --fix")
