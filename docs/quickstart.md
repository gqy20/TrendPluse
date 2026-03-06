# 快速开始

## 环境准备

!!! requirement "前置要求"
    - Python 3.13+
    - `uv`
    - 智谱 AI API Key

## 安装

```bash
git clone https://github.com/gqy20/TrendPluse.git
cd TrendPluse
uv sync --all-dev
```

## 配置

创建 `.env`：

```bash
ANTHROPIC_API_KEY=your_zhipu_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

# 可选：提升 GitHub API 额度
GITHUB_TOKEN=your_github_token_here

# 可选：飞书通知
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...
FEISHU_SECRET=your_secret_here
FEISHU_AT_MOBILES=13800138000,13900139000
```

默认会从仓库根目录的 `repos.json` 读取监控仓库列表；也可以用环境变量覆盖：

```bash
export GITHUB_REPOS="anthropics/claude-code,openai/codex"
```

## 常用命令

```bash
# 每日趋势分析
uv run trendpluse-run

# 周报聚合
uv run trendpluse-run-weekly

# 项目发现
uv run trendpluse-discover-projects --days 30 --min-quality 60

# 发送飞书日报
uv run trendpluse-send-feishu

# 发送飞书周报
uv run trendpluse-send-weekly-feishu
```

## 报告输出

```text
reports/
  daily/       # 日报 md/json
  weekly/      # 周报 md/json
  discovery/   # discovery 报告 md/json
```

文档站点中的同步产物位于：

```text
docs/
  reports/
  discovery-reports/
```

## 开发常用命令

```bash
make check
make format
make typecheck
make test
make test-cov
make docs
make docs-serve
```

## 常见问题

!!! question "没有生成报告？"
    先检查 `ANTHROPIC_API_KEY`、`GITHUB_TOKEN` 和 `repos.json` 是否有效，再执行 `uv run trendpluse-run`。

!!! question "飞书通知失败？"
    检查 `FEISHU_WEBHOOK_URL`、`FEISHU_SECRET` 和 `FEISHU_AT_MOBILES`。

!!! question "如何只跑某一类能力？"
    直接使用 CLI 入口，例如 `trendpluse-discover-projects`、`trendpluse-analyze-issues`、`trendpluse-generate-report-index`。
