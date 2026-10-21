# demo_lib
A minimal Python package template, with editable install, CLI entry, lint, type-check, unit-test, pre-commit and GitHub CI.

## Features
- Modern packaging with `pyproject.toml` + `hatchling` (no `setup.py`)
- Editable development install (`pip install -e ".[dev]"`)
- Command-line script entrypoint
- Code lint & format: **ruff**
- Static type checking: **mypy** (strict mode)
- Unit test: **pytest**
- Local git hook: **pre-commit** (run ruff / mypy / pytest before commit)
- GitHub Actions CI: auto-check on push & pull request

## Project Structure