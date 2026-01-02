# 快速开始

## 本地运行

### 1. 环境准备

!!! requirement "系统要求"
    - Python 3.13 或更高版本
    - uv 包管理器
    - 智谱 AI API Key

### 2. 安装依赖

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆仓库
git clone https://github.com/gqy20/TrendPluse.git
cd TrendPluse

# 安装项目依赖
uv sync --extra dev
```

### 3. 配置环境变量

创建 `.env` 文件：

```bash
# 必需配置
ANTHROPIC_API_KEY=your_zhipu_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

# 可选配置
GITHUB_TOKEN=your_github_token_here  # 用于更高速率限制
```

### 4. 运行分析

```bash
# 运行每日分析
uv run python scripts/run.py

# 运行测试
uv run pytest tests/unit/ -v

# 代码检查
uv run ruff check .
uv run ruff format .
```

## 获取 API Key

### 智谱 AI

1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
2. 注册/登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key
5. 复制 Key 并配置到环境变量

### GitHub Token（可选）

```bash
# 使用 GitHub CLI 生成
gh auth token

# 或访问 GitHub 设置
# https://github.com/settings/tokens
```

## 查看报告

报告生成后位于 `reports/` 目录：

```bash
ls reports/
# report-2026-01-02.md
# report-2026-01-01.md
```

## 常见问题

!!! question "运行失败？"
    检查环境变量是否正确配置：
    ```bash
    echo $ANTHROPIC_API_KEY
    echo $ANTHROPIC_BASE_URL
    ```

!!! question "没有生成报告？"
    可能原因：
    - 当日没有符合条件的 PR
    - GitHub API 速率限制
    - 网络连接问题

!!! question "如何添加更多仓库？"
    编辑配置文件或设置环境变量：
    ```bash
    export GITHUB_REPOS="anthropics/claude-docs,anthropics/typescript-sdk"
    ```

## 下一步

- 📖 阅读 [配置指南](configuration.md)
- 🔧 查看 [功能概述](features.md)
- 📊 访问 [报告归档](reports/index.md)
