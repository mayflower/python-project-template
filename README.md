# Python project template

Starter project for the Coder Python workspaces on the data cluster
(`coder.data.mayflower.zone`). A new workspace clones this repository into
`~/project` and runs `uv sync`, so the virtualenv in `.venv` is ready when VS
Code opens.

- Python 3.14 (`.python-version`), managed by [uv](https://docs.astral.sh/uv/)
- src layout: package `app` in `src/app`, tests in `tests/`
- ruff (lint + format on save), mypy (strict), pytest with coverage

## Commands

```bash
uv run app              # run the entry point
uv run pytest           # tests with coverage
uv run ruff check .     # lint
uv run ruff format .    # format
uv run mypy             # type check
uv add <package>        # add a dependency
```

## Debugging

- `breakpoint()` in code, or the launch configurations in `.vscode/launch.json`
  (current file, `app` module, attach to a running process).
- Attach pdb to a running process (new in 3.14): `python -m pdb -p <PID>`.

## Starting your own project

Rename the package (`app` in `pyproject.toml` and `src/app`), then push to a
new repository. To start a workspace from your own repository instead, set the
"Git repository" parameter when you create it.
