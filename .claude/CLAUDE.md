# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 禁止

- 不要使用 web search 工具，可以使用 jina mcp 或者 web-search-prime mcp

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

# 添加监控仓库
uv run python scripts/add_repo.py owner/repo

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
- `ActivityCollector`: 采集 commit 活跃度数据（GraphQL）
- `ReleaseCollector`: 采集 Release 数据
- `EventFilter`: 筛选候选事件
- `GitHubDetailFetcher`: 获取 PR 详细信息
- 返回格式: `(StructuredData, detailed_list)` 元组
- 并行采集使用 `collectors/parallel.py` 的 `parallel_map()` 和 `parallel_execute()`

**Analyzers** (`analyzers/`): AI 分析
- 所有分析器使用 `instructor` + Pydantic 模型实现结构化输出
- 继承 `BaseLLMAnalyzer` (`analyzers/base.py`)
- `TrendAnalyzer`: 分析 PR 提取信号，支持跨类型聚合
- `CommitAnalyzer`: 分析 commits 提取信号（支持 SHA 精确匹配）
- `ReleaseAnalyzer`: 分析 releases 提取信号
- `ReleaseSummarizer`: 为 releases 生成 AI 总结（变更类型、关键点、影响级别）
- `BreakingChangesDetector`: 检测不兼容变更
- `SignalDeduplicator`: 基于 LLM + 历史记录的信号去重

**Reporters** (`reporters/`): 报告生成
- `MarkdownReporter`: 生成 Markdown 报告（`reports/report-YYYY-MM-DD.md`）
- 同时输出 JSON 格式（`reports/report-YYYY-MM-DD.json`）

**Notifiers** (`notifiers/`): 通知发送
- `FeishuNotifier`: 飞书通知（富文本卡片 + @ 提醒）
- `FeishuFormatter`: 飞书卡片格式化器

**Utils** (`utils/`): 工具模块
- `retry.py`: API 重试装饰器工厂函数（`create_anthropic_retry_decorator`、`create_github_retry_decorator`）
- `formatters.py`: 格式化工具函数

### 数据模型 (`models/signal.py`)

使用 Pydantic BaseModel 定义结构化数据，**使用属性访问**（`activity.total_commits`），不是字典访问。

核心模型：
- `Signal`: 单条趋势信号（包含 `get_type_emoji()` 类方法）
- `DailyReport`: 每日报告
- `ActivityData`: 仓库活跃度汇总
- `ReleasesData`: Release 汇总
- `RepoActivity`: 单仓库活跃度
- `ReleaseInfo`: 单个发布信息
- `ReleaseSummary`: AI 生成的 Release 变更总结

**信号类型** (`type`):
- `capability`: 🚀 新能力/功能
- `abstraction`: 🎨 抽象层改进
- `workflow`: ⚙️ 工作流优化
- `eval`: 📊 评估/基准
- `safety`: 🛡️ 安全性增强
- `performance`: ⚡ 性能优化
- `commit`: 💾 Commit 信号
- `release`: 🎯 Release 信号

**信号分类** (`category`):
- `engineering`: 工程信号（工具链、SDK、框架更新）
- `research`: 研究信号（论文、实验、技术探索）

### 配置管理 (`config.py`)

使用 `pydantic-settings` 从环境变量加载配置。参考 `.env.example` 文件。

**必需配置**:
- `ANTHROPIC_API_KEY`: 智谱 AI API 密钥
- `ANTHROPIC_BASE_URL`: API 基础 URL（默认: `https://open.bigmodel.cn/api/anthropic`）

**可选配置**:
- `GITHUB_TOKEN`: GitHub 访问令牌（提高速率限制）
- `ANTHROPIC_MODEL`: 模型名称（默认: `glm-4.7`）
- `FEISHU_WEBHOOK_URL`: 飞书 Webhook URL
- `FEISHU_SECRET`: 飞书签名验证密钥
- `FEISHU_AT_MOBILES`: 飞书 @ 提醒手机号（**逗号分隔字符串**）
- `FEISHU_MAX_SIGNALS`: 飞书卡片显示信号数量（1-10，默认 5）
- `MAX_PARALLEL_WORKERS`: 并行采集线程数（1-32，默认 8）

### 测试策略

- **TDD 开发**: 先写测试，再实现功能
- **Mock 外部依赖**: 使用 `respx` mock HTTP 请求，`freezegun` mock 时间
- **测试文件组织**: `tests/unit/` 下按模块组织
- pre-commit hooks 包含测试检查

**Fixtures** (`tests/conftest.py`):
- `sample_data`, `sample_numbers`: 示例数据
- `temp_file`, `temp_dir`: 临时文件/目录（自动清理）
- `capture_logs`: 日志捕获
- `clean_env`: 环境变量管理
- `mock_console`: Rich 控制台模拟
- `mock_env_vars`: Mock 必需环境变量

### 关键实现细节

#### 并行采集框架
`collectors/parallel.py`:
- `parallel_map()`: 并行执行并保持顺序
- `parallel_execute()`: 并行执行，忽略错误
- 单个任务失败不影响整体流程

#### LLM 分析器基类
`BaseLLMAnalyzer` (`analyzers/base.py`):
- 统一 Anthropic 客户端初始化
- `_extract_text_from_response()`: 提取文本内容
- `_validate_and_create_signal()`: 验证并创建信号对象
- 使用 `@create_anthropic_retry_decorator()` 添加重试机制

#### 重试机制
`utils/retry.py` 使用 `tenacity`:
- `create_anthropic_retry_decorator()`: LLM API 重试（3次，1s→2s→4s→10s）
- `create_github_retry_decorator()`: GitHub API 重试（3次，4s→8s→16s→60s）

#### 容错设计
Pipeline 在各环节失败时**优雅降级**，确保至少生成包含活跃度数据的报告。

### GitHub Actions 工作流

- **CI** (`.github/workflows/ci.yml`): PR/push 时运行测试和代码检查
- **每日分析** (`.github/workflows/run-daily.yml`): 每天 UTC 0:10 运行（北京时间 8:10）
- **飞书通知** (`.github/workflows/send-feishu.yml`): 手动触发，用于重发通知

### 扩展开发

**添加新 Collector**:
1. 在 `collectors/` 下创建新文件
2. 实现数据采集逻辑，返回 `(StructuredData, detailed_list)` 元组
3. 在 `pipeline.py` 的 `__init__()` 中初始化
4. 在 `run_daily()` 中集成调用，使用 `parallel_map()` 或 `parallel_execute()`

**添加新 Analyzer**:
1. 在 `analyzers/` 下创建新文件
2. 继承 `BaseLLMAnalyzer` 基类
3. 使用 `instructor` + Pydantic 模型实现结构化输出
4. 使用 `_validate_and_create_signal()` 验证 LLM 返回的数据
5. 在 `pipeline.py` 中集成调用
6. 如需去重，在 `SignalDeduplicator` 中添加逻辑
7. 使用 `@create_anthropic_retry_decorator()` 添加重试机制

**添加新 Notifier**:
1. 继承 `BaseNotifier` (`notifiers/base.py`)
2. 实现 `send_report()` 方法
3. 在 `pipeline.py` 的 `__init__()` 中根据配置条件初始化
4. 在 `_send_notification()` 中调用

### 项目结构

```
src/trendpluse/
├── __init__.py              # 包初始化，导出公共 API
├── logger.py                # 日志系统（rich）
├── config.py                # 配置管理
├── pipeline.py              # 主流程协调器
├── main.py                  # 命令行入口
├── collectors/              # 数据采集器
│   ├── base.py              # BaseGitHubCollector 基类
│   ├── github_events.py     # GitHub 事件采集
│   ├── activity.py          # 活跃度采集（GraphQL）
│   ├── releases.py          # Release 采集
│   ├── filter.py            # 事件筛选
│   ├── github_api.py        # GitHub API 封装
│   └── parallel.py          # 并行采集框架
├── analyzers/               # AI 分析器
│   ├── base.py              # BaseLLMAnalyzer 基类
│   ├── trend_analyzer.py    # PR 趋势分析
│   ├── commit_analyzer.py   # Commit 分析
│   ├── release_analyzer.py  # Release 分析
│   ├── release_summarizer.py
│   ├── breaking_changes_detector.py
│   └── signal_deduplicator.py
├── models/                  # 数据模型
│   └── signal.py            # 信号和报告模型
├── reporters/               # 报告生成器
│   └── markdown_reporter.py
├── notifiers/               # 通知发送
│   ├── base.py
│   ├── feishu.py
│   └── formatters/
│       └── feishu.py
└── utils/                   # 工具模块
    ├── retry.py
    └── formatters.py

scripts/
├── run.py
├── generate_report_index.py
├── sync_repos_to_docs.py
├── add_repo.py
├── send_feishu_notification.py
└── repos_doc_generator.py

docs/                        # MkDocs 文档源
reports/                     # 生成的报告（report-YYYY-MM-DD.md/json）
data/                        # 数据文件（signal_history.json, snapshots/）
```
