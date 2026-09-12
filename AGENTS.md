# Repository Guidelines

## Project Structure & Module Organization
- `src/trendpluse/`: core application code (collectors, analyzers, reporters, notifiers).
  - `src/trendpluse/prompts/`: LLM prompt templates (YAML + jinja2, rendered via `render_prompt`).
- `scripts/`: runnable entry points (e.g., `scripts/run-daily-cron.sh`).
- `tests/`: pytest suite (primarily `tests/unit/`; golden fixtures in `tests/fixtures/prompts/`).
- `reports/`: generated Markdown/JSON trend reports (JSON is the source of truth; MD is a derived view).
- `docs/`: project documentation (e.g., `docs/ROADMAP.md`).
- `data/`: runtime state (history index, issue snapshots, discovery intermediates) — gitignored.
- `web/`: Astro + Tailwind + GSAP frontend, deployed to GitHub Pages subpath `/TrendPluse/`.

## Build, Test, and Development Commands
Use `uv` and the Makefile for standard tasks:
- `make install`: create venv + install dev deps.
- `make check`: run Ruff linting.
- `make format`: run Ruff formatter.
- `make typecheck`: run `mypy` on `src/trendpluse`.
- `make test`: run pytest.
- `make test-cov`: pytest with coverage report (`htmlcov/`).
- `make run`: run daily analysis (`scripts/run.py`).
- Frontend: `cd web && pnpm check` (type check) / `pnpm build` (site build).

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
