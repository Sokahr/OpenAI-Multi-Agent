"""Tasks to invoke."""
from invoke import task

def _run(ctx, cmd, **kwargs):
    ctx.run(cmd, echo=True, **kwargs)

@task("lint")
def lint(ctx):
    """Lint code."""
    _run(ctx, "ruff --check")