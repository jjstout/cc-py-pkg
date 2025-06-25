# cc-py-pkg

A simple cookiecutter template for Python Packages and Tools.

## Host Dependencies
* uv
* git
* git-flow

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

# Initialize new project
$ cd <repo-slug>
$ uv sync
$ source .venv/bin/activate
$ inv init
$ inv push
```

## Notes

1. project_type: tool includes a CLI template, while package does not
2. git is configured to use https and not ssh for repo access
3. common cookie cutter options can be set in ~/.cookiecutterrc