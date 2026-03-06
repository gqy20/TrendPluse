# TrendPulse

[![CI](https://img.shields.io/badge/GitHub-Actions-blue)](https://github.com/gqy20/TrendPluse/actions)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/gh/gqy20/TrendPluse/branch/main/graph/badge.svg)](https://codecov.io/gh/gqy20/TrendPluse)
[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-success?label=docs)](https://home.gqy20.top/TrendPluse/)

## 概述

**TrendPulse** 是一个智能的 GitHub 趋势分析工具，专注于追踪 **AI 编程工具和智能体**的最新动态。

它使用 AI 自动分析 GitHub 活动，提取重要的技术趋势和创新点，并以结构化的报告展示。

### 核心特性

- 🔍 **智能采集**: 使用 GitHub API 实时获取 PR、Issue、Release
- 🤖 **AI 分析**: 使用 glm-4.7 提取趋势信号和关键洞察
- 📊 **每日报告**: 自动生成结构化的 Markdown 和 JSON 趋势分析报告
- 🧠 **Issue 洞察**: 基于 Issue Agent 的三轮分析提取用户痛点，并输出质量分
- 🧭 **项目发现**: 自动发现候选项目并按质量分层推荐（discovery 报告）
- 📆 **周报聚合**: 聚合近 7 天日报生成 weekly 报告
- 🎯 **多维分类**: 工程实践、研究成果、生态动向等分类
- 🌐 **自动发布**: GitHub Pages 自动展示报告
- ⚡ **TDD 开发**: 测试驱动开发，代码质量有保障
- 🚀 **并行处理**: 数据采集和 AI 分析并行化，提升处理效率
- 📱 **飞书通知**: 支持飞书机器人推送趋势报告（可选）

### 报告分类

| 分类 | 说明 | 示例 |
|------|------|------|
| 🔧 **工程信号** | Claude 工具链、SDK、框架更新 | 新增 API、性能优化、Bug 修复 |
| 🔬 **研究信号** | 论文、实验、技术探索 | 新模型、评估方法、基准测试 |

## 快速开始

### 前置要求

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) - 极速包管理器
- 智谱 AI API Key

### 安装

```bash
# 克隆仓库
git clone https://github.com/gqy20/TrendPluse.git
cd TrendPluse

# 安装依赖
uv sync --extra dev

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入 ANTHROPIC_API_KEY
```

### 配置

创建 `.env` 文件：

```bash
# 必需配置
ANTHROPIC_API_KEY=your_zhipu_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

# 可选配置（提高 GitHub API 速率限制）
GITHUB_TOKEN=your_github_token_here

# 飞书通知（可选）
FEISHU_WEBHOOK_URL=your_feishu_webhook_url
FEISHU_SECRET=your_feishu_secret
FEISHU_AT_MOBILES=13800138000,13900139000
```

### 获取 API Key

1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
2. 注册/登录账号
3. 进入 API Keys 页面
4. 创建新的 API Key

### 运行

```bash
# 运行每日趋势分析
uv run trendpluse-run

# 查看生成的报告
ls reports/daily reports/weekly
# reports/daily/report-2026-01-02.md
# reports/weekly/weekly-2026-W04.md
```

## 项目结构

```text
src/trendpluse/
  cli/         # 命令入口与参数解析
  automation/  # 可复用批处理实现
  collectors/  # 数据采集与材料构建
  analyzers/   # LLM 分析、去重、聚合
  workflows/   # 日报/周报/issue/output 工作流
  models/      # 结构化模型
  discovery/   # 项目发现子系统
  notifiers/   # 飞书通知
  pipeline.py  # 总编排入口
```

## 常用命令

### 代码检查

```bash
# 代码检查
make check
# 或: uv run ruff check .

# 代码格式化
make format
# 或: uv run ruff format .

# 类型检查
make typecheck
# 或: uv run mypy src/trendpluse

# 运行所有检查
make all
```

### 测试

```bash
# 运行测试
make test
# 或: uv run pytest

# 运行测试并生成覆盖率报告
make test-cov
# 或: uv run pytest --cov=src/trendpluse --cov-report=html

# 关键异步/主流程回归
uv run pytest tests/unit/test_async_analyzers.py tests/unit/test_pipeline.py -q
```

### 运行主程序

```bash
# 运行每日趋势分析
make run
# 或: uv run trendpluse-run

# 运行周报聚合（仅 GitHub Actions 环境）
uv run trendpluse-run-weekly

# 运行项目发现
uv run trendpluse-discover-projects --days 30 --min-quality 60 --output-dir reports

# 生成报告索引
make gen-index
# 或: uv run trendpluse-generate-report-index

# 同步仓库列表到文档
make sync-repos
# 或: uv run trendpluse-sync-repos-to-docs
```

### 文档

```bash
# 构建文档
make docs
# 或: uv run python -m mkdocs build

# 预览文档（本地）
make docs-serve
# 或: uv run python -m mkdocs serve
```

## GitHub Actions

项目配置了自动化工作流：
- **CI** - 每次 PR/push 时运行测试和代码检查
- **每日分析** - 每天 UTC 0:10 自动生成趋势报告（北京时间 8:10）
- **每周报告** - 定时聚合日报生成周报
- **项目发现** - 定时发现候选项目并生成 discovery 报告
- **Issue 仓库分析** - 在 issue/comment 中通过 `@claude` 触发仓库分析
- **新增仓库请求** - 通过 workflow 自动处理仓库新增请求
- **文档部署** - 报告更新后自动部署到 GitHub Pages
- **飞书通知** - 可选的飞书机器人推送（日报/周报）

详见 [`.github/workflows/`](./.github/workflows/)

## 能力索引

- 每日分析主入口：`trendpluse-run`
- 周报生成：`trendpluse-run-weekly`
- 项目发现：`trendpluse-discover-projects`
- Issue Agent 分析：`trendpluse-analyze-issues`
- 报告索引生成：`trendpluse-generate-report-index`
- 仓库同步文档：`trendpluse-sync-repos-to-docs`
- 统计归一化工具：`trendpluse-normalize-daily-stats`

## 报告展示

每日生成的报告会自动发布到 GitHub Pages：

👉 **[查看在线报告](https://home.gqy20.top/TrendPluse/)**

报告包含：
- 📊 当日趋势总览
- 🔧 工程信号详情（折叠面板）
- 🔬 研究信号详情（折叠面板）
- 🚀 Release AI 总结
- 📈 活跃度统计
- 🔗 完整 JSON 数据（机器可读）

## 开发指南

### 代码规范

1. **语言**：注释和文档使用**中文**
2. **命名**：函数和类使用英文
3. **类型注解**：必需
4. **文档字符串**：Google 风格中文文档
5. **提交规范**：feat/fix/docs/refactor/test/chore

### TDD 开发流程

```bash
# 1. 编写测试
vim tests/unit/test_feature.py

# 2. 运行测试（失败）
uv run pytest tests/unit/test_feature.py

# 3. 实现功能
vim src/trendpluse/feature.py

# 4. 运行测试（通过）
uv run pytest tests/unit/test_feature.py

# 5. 代码检查
make check
make format

# 6. 提交
git add .
git commit -m "feat: add new feature"
```

## 支持的仓库

默认追踪以下仓库：

### Anthropic 官方

#### 核心产品
- `anthropics/claude-code` - Claude Code 编程助手
- `anthropics/skills` - Claude Agent 技能库
- `anthropics/claude-cookbooks` - Claude 食谱示例
- `anthropics/claude-quickstarts` - Claude 快速开始示例
- `anthropics/courses` - Claude 课程
- `anthropics/prompt-eng-interactive-tutorial` - Prompt 工程交互教程

#### SDK & Agent
- `anthropics/claude-agent-sdk-python` - Claude Agent SDK (Python)
- `anthropics/claude-agent-sdk-typescript` - Claude Agent SDK (TypeScript)
- `anthropics/claude-agent-sdk-demos` - Claude Agent SDK 示例
- `anthropics/anthropic-sdk-python` - Anthropic SDK (Python)
- `anthropics/anthropic-sdk-typescript` - Anthropic SDK (TypeScript)
- `anthropics/anthropic-sdk-go` - Anthropic SDK (Go)
- `anthropics/anthropic-sdk-java` - Anthropic SDK (Java)

#### 工具与集成
- `anthropics/claude-code-action` - Claude Code GitHub Action
- `anthropics/claude-code-security-review` - Claude Code 安全审查
- `anthropics/claude-plugins-official` - Claude 官方插件
- `anthropics/devcontainer-features` - DevContainer 特性

#### 研究与评估
- `anthropics/evals` - Anthropic 评估工具
- `anthropics/political-neutrality-eval` - 政治中立性评估
- `anthropics/hh-rlhf` - HH-RLHF 研究

### AI 编程助手
- `cline/cline` - Autonomous coding agent
- `paul-gauthier/aider` - AI pair programming tool
- `continuedev/continue` - AI code assistant
- `AndyMik90/Auto-Claude` - 自主多会话 AI 编程
- `anomalyco/opencode` - 开源 Claude Code 替代
- `openinterpreter/open-interpreter` - 代码解释器
- `TabbyML/tabby` - 自托管代码补全
- `zed-industries/zed` - AI 原生编辑器

### AI 工具
- `openai/openai-python` - OpenAI Python SDK
- `openai/openai-quickstart-python` - OpenAI Quickstart
- `danielmiessler/fabric` - AI 工作流工具
- `ErikBjare/gptme` - AI 终端助手

### Agent 框架
- `langchain-ai/langchain` - LangChain 框架
- `langchain-ai/langgraph` - 图状态多代理系统
- `langgenius/dify` - Dify LLM 应用开发平台
- `run-llama/llama_index` - LlamaIndex 数据框架
- `microsoft/autogen` - Microsoft AutoGen
- `microsoft/semantic-kernel` - 企业级 SDK
- `TransformerOptimus/SuperAGI` - SuperAGI 框架
- `Significant-Gravitas/AutoGPT` - AutoGPT
- `OpenDevin/OpenDevin` - OpenDevin
- `google-gemini/gemini-cli` - Gemini CLI 工具
- `agentscope-ai/agentscope` - AgentScope 框架
- `agno-agi/agno` - 多代理框架

#### Agentic AI 核心框架
- `openai/swarm` - OpenAI 多代理编排
- `openai/codex` - 终端编程代理
- `crewAIInc/crewAI` - 角色扮演多代理框架
- `huggingface/smolagents` - 代码驱动代理
- `ruvnet/claude-flow` - Claude Agent 平台
- `bytedance/deer-flow` - 深度研究框架
- `langchain-ai/deepagents` - 深度代理

推荐修改仓库根目录的 `repos.json`，或通过环境变量覆盖：

```bash
export GITHUB_REPOS="anthropics/claude-code,your-org/your-repo"
```

## 测试策略

- 顶层 `tests/test_*.py` 覆盖基础模块与包级行为
- `tests/unit/` 覆盖 collectors、analyzers、workflows、CLI 和配置
- CLI 收口通过 [test_cli_help_smoke.py](/home/qy113/workspace/project/2603/TrendPluse/tests/unit/test_cli_help_smoke.py) 做冒烟保护
- 配置测试会显式清理环境变量，避免受本机或 CI 环境污染

## 故障排查

### 分析失败

**问题**: 运行 `trendpluse-run` 失败

**解决方案**:
```bash
# 检查环境变量
echo $ANTHROPIC_API_KEY
echo $ANTHROPIC_BASE_URL

# 查看详细日志
RUST_LOG=debug uv run trendpluse-run
```

### 没有生成报告

**问题**: `reports/` 目录为空

**可能原因**:
- 当日没有符合条件的 PR
- GitHub API 速率限制
- 网络连接问题

**解决方案**:
- 使用 GitHub Token 提高速率限制
- 检查网络连接
- 查看日志输出

### GitHub Actions 失败

**问题**: Workflow 运行失败

**解决方案**:
```bash
# 查看 workflow 运行日志
gh run list
gh run view <run_id> --log-failed

# 检查 secrets 配置
gh secret list
```

### 飞书通知发送失败

**问题**: 报告生成成功但未收到飞书通知

**可能原因**:
- `FEISHU_WEBHOOK_URL` 配置错误
- `FEISHU_SECRET` 验证失败
- 网络连接问题

**解决方案**:
```bash
# 检查环境变量配置
echo $FEISHU_WEBHOOK_URL
echo $FEISHU_SECRET

# 手动发送通知测试
uv run trendpluse-send-feishu

# 查看飞书卡片内容
cat feishu_card.json
```

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: add AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

MIT License

Copyright © 2026 gqy20

---

**[项目文档](https://home.gqy20.top/TrendPluse/)** | **[在线报告](https://home.gqy20.top/TrendPluse/reports/)** | **[GitHub 仓库](https://github.com/gqy20/TrendPluse)**
