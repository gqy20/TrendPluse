.PHONY: venv install check format typecheck test test-cov clean all help
.PHONY: docs docs-serve docs-build run gen-index sync-repos

venv:
	uv venv

install: venv
	uv sync --all-dev
	uv run pre-commit install

check:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src/trendpluse

test:
	uv run pytest

test-cov:
	uv run pytest --cov=src/trendpluse --cov-report=html

# 运行主程序
run:
	uv run python scripts/run.py

# 生成报告索引
gen-index:
	uv run python scripts/generate_report_index.py

# 同步仓库列表到文档
sync-repos:
	uv run python scripts/sync_repos_to_docs.py

# 构建文档
docs-build:
	uv run mkdocs build

# 预览文档（本地）
docs-serve:
	uv run mkdocs serve

# 文档命令别名
docs: docs-build

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .coverage htmlcov/ dist/ build/ *.egg-info .venv .mypy_cache

all: check typecheck test

help:
	@echo "常用命令:"
	@echo "  make venv       - 创建虚拟环境"
	@echo "  make install    - 创建虚拟环境并安装依赖"
	@echo "  make check      - 代码检查"
	@echo "  make format     - 格式化代码"
	@echo "  make typecheck  - 类型检查"
	@echo "  make test       - 运行测试"
	@echo "  make test-cov   - 测试 + 覆盖率"
	@echo "  make run        - 运行主程序"
	@echo "  make gen-index  - 生成报告索引"
	@echo "  make sync-repos - 同步仓库列表到文档"
	@echo "  make docs       - 构建文档"
	@echo "  make docs-serve - 预览文档（本地）"
	@echo "  make clean      - 清理缓存（包括虚拟环境）"
	@echo "  make all        - 检查 + 类型检查 + 测试"
