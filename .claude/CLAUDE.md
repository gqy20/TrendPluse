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
- **AI 集成**: 使用 `instructor` + Pydantic 实现结构化输出，支持智谱 AI (glm-4.7) 和 Anthropic Claude

## 常用命令

```bash
# 创建虚拟环境并安装依赖（包含 pre-commit hooks）
make install

# 代码检查
make check

# 格式化代码
make format

# 类型检查
make typecheck

# 测试
make test

# 运行单个测试
uv run pytest tests/unit/test_pipeline.py::TestTrendPulsePipeline::test_run_daily -v

# 测试 + 覆盖率
make test-cov

# 运行主程序（每日趋势分析）
make run

# 生成报告索引
make gen-index

# 同步仓库列表到文档
make sync-repos

# 构建文档
make docs

# 预览文档（本地）
make docs-serve

# 运行所有检查（check + typecheck + test）
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
- 容错设计：AI 分析失败不会阻断整个流程，至少生成包含活跃度数据的报告

**Collectors** (`collectors/`): 数据采集
- `GitHubEventsCollector`: 获取 PR 事件
- `ActivityCollector`: 采集 commit 活跃度数据
- `ReleaseCollector`: 采集 Release 数据
- `EventFilter`: 筛选候选事件
- `GitHubDetailFetcher`: 获取 PR 详细信息
- 返回格式: `(StructuredData, detailed_list)` 元组

**Analyzers** (`analyzers/`): AI 分析
- 所有分析器使用 `instructor` + Pydantic 模型实现结构化输出
- `TrendAnalyzer`: 分析 PR 提取信号，支持跨类型聚合
- `CommitAnalyzer`: 分析 commits 提取信号（支持 SHA 精确匹配）
- `ReleaseAnalyzer`: 分析 releases 提取信号
- `BreakingChangesDetector`: 检测不兼容变更
- `SignalDeduplicator`: 基于 LLM + 历史记录的信号去重

**Reporters** (`reporters/`): 报告生成
- `MarkdownReporter`: 生成 Markdown 报告

**Notifiers** (`notifiers/`): 通知发送
- `FeishuNotifier`: 飞书通知（富文本卡片 + @ 提醒）
- `FeishuFormatter`: 飞书卡片格式化器

### 数据模型 (`models/signal.py`)

使用 Pydantic BaseModel 定义结构化数据：

- `Signal`: 单条趋势信号（包含 `get_type_emoji()` 类方法）
- `DailyReport`: 每日报告
- `ActivityData`: 仓库活跃度汇总
- `ReleasesData`: Release 汇总
- `RepoActivity`: 单仓库活跃度
- `ReleaseInfo`: 单个发布信息

**重要**: 所有模型使用属性访问（`activity.total_commits`），不是字典访问（`activity.get("total_commits")`）。

### 配置管理 (`config.py`)

使用 `pydantic-settings` 从环境变量加载配置：

**必需配置**:
- `ANTHROPIC_API_KEY`: 智谱 AI API 密钥（获取: https://open.bigmodel.cn/usercenter/apikeys）
- `ANTHROPIC_BASE_URL`: API 基础 URL（默认: `https://open.bigmodel.cn/api/anthropic`）

**可选配置**:
- `GITHUB_TOKEN`: GitHub 访问令牌（提高速率限制）
- `ANTHROPIC_MODEL`: 模型名称（默认: `glm-4.7`）
- `FEISHU_WEBHOOK_URL`: 飞书 Webhook URL
- `FEISHU_SECRET`: 飞书签名验证密钥
- `FEISHU_AT_MOBILES`: 飞书 @ 提醒手机号（**逗号分隔字符串**，不是 JSON 数组）
- `FEISHU_MAX_SIGNALS`: 飞书卡片显示信号数量（1-10，默认 5）
- `INCLUDE_PRERELEASES`: 是否包含预发布版本（默认 false）
- `MAX_CANDIDATES`: 最大候选事件数（默认 20）
- `DAYS_TO_LOOKBACK`: PR 和 Release 回溯天数（默认 7）

### 测试策略

- **TDD 开发**: 先写测试，再实现功能
- **Mock 外部依赖**: 使用 `respx` mock HTTP 请求，`freezegun` mock 时间
- **测试文件组织**: `tests/unit/` 下按模块组织
- pre-commit hooks 包含测试检查

### 关键实现细节

#### 跨类型信号聚合
`TrendAnalyzer.aggregate_and_generate_report()` 使用 LLM 识别跨 PR、Commit、Release 的高层次趋势模式，而不仅仅是分类汇总。

#### SHA 精确匹配
`CommitAnalyzer` 支持通过 commit SHA 精确匹配 LLM 返回的信号与原始 commit，避免索引错位问题。使用 `search_commits_by_sha()` 方法。

#### 信号去重机制
`SignalDeduplicator` 使用 LLM + 历史记录（`data/signal_history.json`）智能去重，可配置 `days_to_lookback` 参数控制回溯天数。

#### 容错设计
Pipeline 在各环节失败时优雅降级，确保至少生成包含活跃度数据的报告。AI 分析失败不会阻断整个流程。

#### Pre-commit Hooks
项目配置了 pre-commit hooks：
- `ruff` --fix --exit-non-zero-on-fix: 自动修复代码问题
- `ruff-format`: 格式化代码
- `mypy`: 类型检查
- `actionlint`: GitHub Actions 工作流检查
- `sync-repos-to-docs`: 自动同步仓库列表到文档（`make install` 时安装）

### 项目结构

```
src/trendpluse/
├── __init__.py       # 包初始化，导出公共 API
├── core.py           # 核心基础函数（add, greet）
├── logger.py         # 日志系统（rich）
├── config.py         # 配置管理（主入口）
├── pipeline.py       # 主流程
├── main.py           # 命令行入口
│
├── collectors/       # 数据采集器
│   ├── github_events.py
│   ├── activity.py
│   ├── releases.py
│   ├── filter.py
│   └── github_api.py
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
├── add_repo.py               # 添加监控仓库
├── send_feishu_notification.py  # 飞书通知脚本
└── repos_doc_generator.py    # 仓库文档生成器

docs/                        # MkDocs 文档源
├── index.md
├── reports/                  # 报告目录
│   └── index.md
└── stylesheets/

reports/                     # 生成的趋势报告
data/                        # 数据文件
├── signal_history.json      # 信号历史记录
└── snapshots/               # 数据快照
```

## 扩展开发

### 添加新 Collector
1. 在 `collectors/` 下创建新文件
2. 实现数据采集逻辑，返回 `(StructuredData, detailed_list)` 元组
3. 在 `pipeline.py` 的 `TrendPulsePipeline.__init__()` 中初始化
4. 在 `run_daily()` 方法中集成调用

### 添加新 Analyzer
1. 在 `analyzers/` 下创建新文件
2. 使用 `instructor` + Pydantic 模型实现结构化输出
3. 参考 `TrendAnalyzer` 的模式，支持 `api_key`、`model`、`base_url` 参数
4. 在 `pipeline.py` 中集成调用
5. 如需去重，在 `SignalDeduplicator` 中添加逻辑

### 添加新 Notifier
1. 继承 `BaseNotifier` (在 `notifiers/base.py`)
2. 实现 `send_report()` 方法
3. 在 `pipeline.py` 的 `__init__()` 中根据配置条件初始化
4. 在 `_send_notification()` 中调用
