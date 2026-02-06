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
# ===========================================
# 必需配置
# ===========================================
ANTHROPIC_API_KEY=your_zhipu_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

# ===========================================
# 可选配置
# ===========================================
# GitHub Token（提高速率限制）
GITHUB_TOKEN=your_github_token_here

# 飞书通知（可选）
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...
FEISHU_SECRET=your_secret_here
FEISHU_AT_MOBILES=13800138000,13900139000

# 高级配置
MAX_PARALLEL_WORKERS=8
DAILY_TOKEN_BUDGET=100000
```

### 4. 运行分析

```bash
# 运行每日分析
uv run python scripts/run.py

# 或使用 make 命令
make run
```

### 5. 查看报告

报告生成后位于 `reports/` 目录：

```bash
ls reports/daily reports/weekly
# reports/daily/report-2026-01-02.md    # 每日报告（Markdown）
# reports/daily/report-2026-01-02.json  # 每日报告（JSON）
# reports/weekly/weekly-2026-W04.md     # 周报（Markdown）
```

---

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

**推荐使用 PAT**：
- 默认限制：60 次/小时
- 使用 PAT：5000 次/小时

---

## 飞书通知配置（可选）

### 获取 Webhook URL

1. 在飞书群组中添加自定义机器人
2. 选择"自定义机器人" → "添加"
3. 复制 Webhook URL

### 签名验证（可选）

1. 在机器人设置中启用"签名验证"
2. 复制签名密钥到 `FEISHU_SECRET`

### 测试通知

```bash
# 发送今日的飞书通知
uv run python scripts/send_feishu_notification.py

# 或手动触发 GitHub Actions
gh workflow run send-feishu.yml -f report_date=2026-01-12
```

---

## 常用命令

### 开发命令

```bash
# 运行测试
make test
# 或
uv run pytest

# 代码检查
make check
# 或
uv run ruff check .

# 代码格式化
make format
# 或
uv run ruff format .

# 类型检查
make typecheck
# 或
uv run mypy src/trendpluse

# 运行所有检查
make all
```

### 报告生成

```bash
# 运行分析
make run

# 生成报告索引
make gen-index

# 同步仓库列表到文档
make sync-repos
```

### 文档预览

```bash
# 构建文档
make docs

# 预览文档（本地）
make docs-serve
# 访问 http://localhost:8000
```

---

## 添加监控仓库

### 使用脚本添加

```bash
# 添加单个仓库
uv run python scripts/add_repo.py owner/repo

# 批量添加
uv run python scripts/add_repo.py owner/repo1 owner/repo2
```

### 通过环境变量

```bash
export GITHUB_REPOS="org/repo1,org/repo2,org/repo3"
uv run python scripts/run.py
```

### 通过配置文件

编辑 `src/trendpluse/config.py`：

```python
class Settings(BaseSettings):
    github_repos: list[str] = [
        "anthropics/claude-code",
        "your-org/your-repo",  # 添加自定义仓库
    ]
```

---

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

    解决方案：
    - 使用 GitHub Token 提高速率限制
    - 检查网络连接
    - 查看详细日志：`RUST_LOG=debug uv run python scripts/run.py`

!!! question "并行处理失败？"
    降低并行线程数：
    ```bash
    export MAX_PARALLEL_WORKERS=4
    ```

!!! question "飞书通知发送失败？"
    检查配置：
    ```bash
    echo $FEISHU_WEBHOOK_URL
    echo $FEISHU_SECRET
    ```

!!! question "Token 超预算？"
    调整每日预算：
    ```bash
    export DAILY_TOKEN_BUDGET=50000
    ```

---

## 报告格式说明

### Markdown 报告

- 📊 **人类可读**：便于阅读和分享
- 🔧 **折叠面板**：工程信号、研究信号使用折叠面板组织
- 🚀 **AI 总结**：Release 版本带有 AI 生成的中文总结

### JSON 报告

- 🔗 **机器可读**：支持数据分析和 API 调用
- 📊 **结构化数据**：包含完整的信号、活跃度、统计数据
- 🔍 **便于集成**：可用于二次开发和数据可视化

---

## 新功能亮点

### 🚀 Release AI 总结

使用 AI 分析 Release Notes，生成结构化中文总结：

- **变更类型**：feature/fix/improvement/breaking/other
- **关键变更**：3-5 个简洁描述
- **中文总结**：2-3 句话概括
- **影响级别**：1-5 级评分

### ⚡ 并行处理

- 数据采集并行化（提升速度）
- PR 和 Release 分析并行化
- 容错设计：单个失败不影响整体

### 📱 飞书通知优化

- **折叠面板**：信息组织更清晰
- **智能去重**：移除重复的日期信息
- **链接格式化**：Commit SHA、PR 号码自动格式化

### 🔄 自动重试

- LLM 调用失败自动重试（指数退避）
- 最多重试 3 次
- 失败降级：返回默认值，确保流程继续

---

## 下一步

- 📖 阅读 [配置指南](configuration.md)
- 🔧 查看 [功能概述](features.md)
- 📊 访问 [报告归档](reports/index.md)
- 🚀 了解 [GitHub Actions 配置](github-actions-setup.md)
