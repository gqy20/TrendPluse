.PHONY: venv install check format typecheck test test-cov clean all help

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
	uv run pytest --cov=src/trendpluse

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
	@echo "  make clean      - 清理缓存（包括虚拟环境）"
	@echo "  make all        - 检查 + 类型检查 + 测试"
