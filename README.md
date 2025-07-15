# cc-py-pkg

A simple cookiecutter template for Python Packages and Tools.

## Features
* uv and project.toml for project management
* invoke for project automation
* ruff for linting and formatting
* pytest
* ty static type checker

## Host Dependencies
* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* git
* git-flow (optional)

## Quickstart

* Create a new repo but do not initialize it with a README file.
* Create a access token with write_repo permissions

```shell
# Configure HTTPS credentials
TOKEN="<token>"
USER="<user name>"
HOST="github.com"   # or SCM of choice

echo "https://${USER}:${TOKEN}@${HOST}" >> .config/git/credentials

# Create new project from template
$ cd ~/dev
$ uvx cookiecutter gh:jjstout/cc-py-pkg
```
**Cookie Cutter Variables:**
* **enable_gitflow** - Use the Gitflow branching model
* **project_type**
  * tool - Include CLI interface
  * package - No CLI interface
* **enable_publish** - Push package to configured package repository (default = https://pypi.org)

```shell
# Initialize new project
$ cd <repo-slug>
$ uv sync
$ source .venv/bin/activate
$ inv init
$ inv push
```

## Notes

1. git is configured to use https and not ssh for repo access
2. common cookie cutter options can be set in ~/.cookiecutterrc
