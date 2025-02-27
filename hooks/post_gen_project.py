import json
from pathlib import Path

ctx_out = Path("project.d/cc-ctx.json")
ctx_out.parent.mkdir(parents=True, exist_ok=True)

with ctx_out.open("w") as fd_out:
    fd_out.write("""{{ cookiecutter | jsonify }}\n""")

if '{{ cookiecutter.enable_cli}}' == "False":
    Path("src/{{ cookiecutter.pkg_slug }}/cli.py").unlink()
