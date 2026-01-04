# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

**TrendPulse** 是一个智能的 GitHub 趋势分析工具，使用 AI 分析 GitHub 活动（PR、Release、Commits），自动提取技术趋势信号并生成结构化报告。

- **Python 版本**: 3.13+
- **包管理**: uv（极速包管理器）
- **项目结构**: src layout
- **代码规范**: ruff（检查 + 格式化）+ mypy（类型检查）
- **测试框架**: pytest
- **日志系统**: rich

## 常用命令

```bash
# 创建虚拟环境并安装依赖
make install

# 代码检查
make check
# 或: uv run ruff check .

# 格式化
make format
# 或: uv run ruff format .

# 类型检查
make typecheck
# 或: uv run mypy src/trendpluse

# 测试
make test
# 或: uv run pytest

# 运行单个测试
uv run pytest tests/unit/test_pipeline.py::TestTrendPulsePipeline::test_run_daily -v

# 测试 + 覆盖率
make test-cov

# 运行主程序
make run
# 或: uv run python scripts/run.py

# 运行所有检查
make all
```

## 代码规范

1. **语言**: 所有注释、文档字符串使用**中文**
2. **命名**: 函数和类使用英文（遵循 PEP 8）
3. **类型注解**: 必需
4. **文档字符串**: Google 风格中文文档
5. **提交规范**: feat/fix/docs/refactor/test/chore

## 架构概览

### 数据流

```
GitHub API → Collectors → Analyzers (AI) → Pipeline → Reporters → Markdown Report
                                              ↓
                                         Notifiers (Feishu)
```

### 核心组件

**Pipeline (`pipeline.py`)**: 主流程协调器
- 初始化所有组件（collectors、analyzers、reporters、notifiers）
- `run_daily()` 执行每日分析流程
- 返回 `DailyReport` 对象

**Collectors** (`collectors/`): 数据采集
- `GitHubEventsCollector`: 获取 PR 事件
- `ActivityCollector`: 采集 commit 活跃度数据
- `ReleaseCollector`: 采集 Release 数据
- 返回格式: `(StructuredData, detailed_list)` 元组

**Analyzers** (`analyzers/`): AI 分析
- `TrendAnalyzer`: 分析 PR 提取信号
- `CommitAnalyzer`: 分析 commits 提取信号
- `ReleaseAnalyzer`: 分析 releases 提取信号
- `BreakingChangesDetector`: 检测不兼容变更
- `SignalDeduplicator`: 基于 LLM 的信号去重

**Reporters** (`reporters/`): 报告生成
- `MarkdownReporter`: 生成 Markdown 报告

**Notifiers** (`notifiers/`): 通知发送
- `FeishuNotifier`: 飞书通知（富文本卡片 + @ 提醒）
- `FeishuFormatter`: 飞书卡片格式化器

### 数据模型 (`models/signal.py`)

使用 Pydantic BaseModel 定义结构化数据：

- `Signal`: 单条趋势信号
- `DailyReport`: 每日报告
- `ActivityData`: 仓库活跃度汇总
- `ReleasesData`: Release 汇总

**重要**: 所有模型使用属性访问（`activity.total_commits`），不是字典访问（`activity.get("total_commits")`）。

### 配置管理 (`config.py`)

使用 `pydantic-settings` 从环境变量加载配置：

**必需配置**:
- `ANTHROPIC_API_KEY`: 智谱 AI API 密钥
- `ANTHROPIC_BASE_URL`: API 基础 URL（默认: `https://open.bigmodel.cn/api/anthropic`）

**可选配置**:
- `GITHUB_TOKEN`: GitHub 访问令牌（提高速率限制）
- `FEISHU_WEBHOOK_URL`: 飞书 Webhook URL
- `FEISHU_SECRET`: 飞书签名验证密钥
- `FEISHU_AT_MOBILES`: 飞书 @ 提醒手机号（**逗号分隔字符串**，不是 JSON 数组）
- `FEISHU_MAX_SIGNALS`: 飞书卡片显示信号数量（1-10，默认 5）
- `INCLUDE_PRERELEASES`: 是否包含预发布版本（默认 false）

### 测试策略

- **TDD 开发**: 先写测试，再实现功能
- **Mock 外部依赖**: 使用 `respx` mock HTTP 请求，`freezegun` mock 时间
- **测试文件组织**: `tests/unit/` 下按模块组织

### 项目结构

```
src/trendpluse/
├── __init__.py       # 包初始化，导出公共 API
├── core.py           # 核心基础函数（add, greet）
├── logger.py         # 日志系统
├── config.py         # 配置管理（主入口）
├── pipeline.py       # 主流程
├── main.py           # 命令行入口
├── api.py            # API 接口定义
│
├── collectors/       # 数据采集器
│   ├── github_events.py
│   ├── activity.py
│   ├── releases.py
│   └── filter.py
│
├── analyzers/        # AI 分析器
│   ├── trend_analyzer.py
│   ├── commit_analyzer.py
│   ├── release_analyzer.py
│   ├── breaking_changes_detector.py
│   └── signal_deduplicator.py
│
├── models/           # 数据模型
│   └── signal.py
│
├── reporters/        # 报告生成器
│   └── markdown_reporter.py
│
└── notifiers/        # 通知发送
    ├── base.py
    ├── feishu.py
    └── formatters/
        └── feishu.py

scripts/
├── run.py                    # 主程序入口
├── generate_report_index.py  # 生成报告索引
├── sync_repos_to_docs.py     # 同步仓库列表到文档
└── send_feishu_notification.py  # 飞书通知脚本
```
