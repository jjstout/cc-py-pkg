from invoke import Collection, task

REMOTE_BRANCHES = ["main", "develop"]

@task
def bumpversion(ctx, part):
    """Bump the version number, by major, minor or patch/hotfix"""
    part = "patch" if part == "hotfix" else part

    ctx.run(f"bump-my-version bump {part}")

@task
def clean(ctx):
    """Delete build, dist, cache and other generated files."""
    patterns = [
        "build/",
        "dist/",
        ".mypy_cache/",
        ".pytest_cache/",
        ".ruff_cache/",
    ]

    for pattern in patterns:
        ctx.run(f"rm -rf {pattern}")

    ctx.run("find . -name '__pycache__' -exec rm -rf {} +")

@task
def init(ctx):
    """Initialize git repository. Run this task after cloning the repository."""  
    ctx.run("git flow init -d")
    ctx.run("uv sync")

@task
def push(ctx):
    """Push all remote branches and tags to the remote repository."""
    for branch in REMOTE_BRANCHES:
        ctx.run(f"git push origin {branch}")

    ctx.run("git push --tags")

ns = Collection(bumpversion, clean, init, push)
