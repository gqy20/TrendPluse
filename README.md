# TrendPluse



[![CI](https://img.shields.io/badge/GitHub-Actions-blue)](https://github.com/gqy20/trendpluse/actions)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/gqy20/trendpluse/branch/main/graph/badge.svg)](https://codecov.io/gh/gqy20/trendpluse)
[![type checking](https://img.shields.io/badge/mypy-checked-blue.svg)](https://mypy.readthedocs.io/)

## 概述

现代 Python 项目脚手架，使用 `uv` + `ruff` + `rich` 构建。

**核心特性：**
- 📦 **uv** - 极速包管理器
- 🏗️ **src layout** - 标准项目结构
- ⚡ **ruff** - 代码检查和格式化
- ✅ **pytest** - 测试框架
- 📝 **rich** - 美观的日志和终端输出
- 🪝 **pre-commit** - 提交前检查
- 🔄 **CI/CD** - GitHub Actions


## 快速开始

**前置要求：**
- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

```bash
# 创建虚拟环境
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安装依赖
uv pip install -e ".[dev]"

# 安装 pre-commit 钩子
pre-commit install

# 运行检查
python scripts/check.py
```

## 项目结构

```
trendpluse/
├── src/trendpluse/
│   ├── __init__.py
│   ├── core.py
│   ├── logger.py

│   └── main.py
├── tests/
├── docs/
├── scripts/
└── pyproject.toml
```

## 常用命令

### 代码检查
```bash
ruff check .              # 代码检查
ruff format .             # 格式化
mypy src/trendpluse # 类型检查
```

### 测试
```bash
pytest
pytest --cov=src/trendpluse
```



## 代码规范

1. **语言**：注释和文档使用**中文**
2. **命名**：函数和类使用英文
3. **类型注解**：必需
4. **文档字符串**：Google 风格

## 许可证

MIT

Copyright © 2026 gqy20
