# Repository Guidelines

## Project Structure & Module Organization
- `src/trendpluse/`: core application code (collectors, analyzers, reporters, notifiers).
- `scripts/`: runnable entry points (e.g., `scripts/run.py`, `scripts/generate_report_index.py`).
- `tests/`: pytest suite (primarily `tests/unit/`).
- `reports/`: generated Markdown/JSON trend reports.
- `docs/` and `mkdocs.yml`: documentation sources and MkDocs config.
- `data/` and `templates/`: input data, snapshots, and Jinja templates.

## Build, Test, and Development Commands
Use `uv` and the Makefile for standard tasks:
- `make install`: create venv + install dev deps.
- `make check`: run Ruff linting.
- `make format`: run Ruff formatter.
- `make typecheck`: run `mypy` on `src/trendpluse`.
- `make test`: run pytest.
- `make test-cov`: pytest with coverage report (`htmlcov/`).
- `make run`: run daily analysis (`scripts/run.py`).
- `make gen-index`: generate report index.
- `make docs` / `make docs-serve`: build or serve MkDocs.

## Coding Style & Naming Conventions
- Python 3.13+, `src/` layout.
- Formatting/linting via Ruff (`line-length = 88`, double quotes).
- Type annotations are required in production code.
- Docstrings use Google style and **Chinese** text; function/class names are English.

## Testing Guidelines
- Framework: `pytest` (+ `pytest-asyncio`, `pytest-cov`).
- Naming: files `test_*.py`, classes `Test*`, functions `test_*`.
- Run all tests: `make test`. Focused test: `uv run pytest tests/unit/test_feature.py`.

## Commit & Pull Request Guidelines
- Commit style follows Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`.
- PRs should include:
  - A concise description of changes and motivation.
  - Linked issue or context (if applicable).
  - Test status and any new/updated tests.
  - Screenshots or report excerpts if docs/output change.

## Configuration & Secrets
- `.env` is required for API keys (see `.env.example`).
- Do not commit secrets; prefer environment variables for `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, and Feishu settings.

## Agent Instructions
- 永远用中文回答。
