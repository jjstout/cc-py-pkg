import json
from pathlib import Path

from dotenv import dotenv_values
from invoke import Collection, Failure, task

REMOTE_BRANCHES = ["main"]

with Path("project.d/cc-ctx.json").open() as fd_in:
    CC_CTX = json.load(fd_in)
    CFG = {
        **dotenv_values("../.config/env.global"),
        **dotenv_values(f"../.config/{CC_CTX['scm_slug']}/env.project"),
    }

    CFG = CFG | CC_CTX
    CFG["pkg_idx_url"] = CFG["PYPI_TEST_URL"]
    CFG["pkg_idx_user"] = CFG["PYPI_TEST_USER"]
    CFG["pkg_idx_passwd"] = CFG["PYPI_TEST_PASSWD"]
    
    if CFG.get("enable_gitflow", False):
        REMOTE_BRANCHES.extend(["develop"])


@task
def pp_cfg(ctx):
    """Pretty print the project configuration."""
    from pprint import pprint as pp
    pp(CFG)
    pp(REMOTE_BRANCHES)


ns = Collection(pp_cfg)
