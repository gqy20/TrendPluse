# 配置指南

## 环境变量配置

### 必需配置

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `ANTHROPIC_API_KEY` | 智谱 AI API 密钥 | `your_api_key_here` |
| `ANTHROPIC_BASE_URL` | API 基础 URL | `https://open.bigmodel.cn/api/anthropic` |

### 可选配置

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `GITHUB_TOKEN` | GitHub 访问令牌 | 无（匿名访问） |
| `ANTHROPIC_MODEL` | 使用的模型 | `glm-4.7` |
| `GITHUB_REPOS` | 追踪的仓库列表（逗号分隔） | 见下方默认值 |
| `MAX_CANDIDATES` | 最大候选事件数 | 20 |
| `DAYS_TO_LOOKBACK` | PR 和 Release 回溯天数 | 7 |
| `MAX_PARALLEL_WORKERS` | 并行采集线程数（1-32） | 8 |
| `DAILY_TOKEN_BUDGET` | 每日 Token 预算 | 100000 |

### 飞书通知配置

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `FEISHU_WEBHOOK_URL` | 飞书机器人 Webhook URL | 无（不发送通知） |
| `FEISHU_SECRET` | 飞书签名验证密钥 | 无 |
| `FEISHU_AT_MOBILES` | 飞��� @ 提醒手机号（逗号分隔） | 无 |
| `FEISHU_MAX_SIGNALS` | 飞书卡片显示信号数量（1-10） | 5 |

### Release 监控配置

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `INCLUDE_PRERELEASES` | 是否包含预发布版本 | false |

## 默认追踪仓库

默认追踪 50+ AI 编程工具和 Agent 框架仓库，包括：

### Anthropic 官方
- `anthropics/claude-code` - Claude Code 编程助手
- `anthropics/skills` - Claude Agent 技能库
- `anthropics/claude-cookbooks` - Claude 食谱示例
- `anthropics/claude-quickstarts` - Claude 快速开始示例
- `anthropics/courses` - Claude 课程
- `anthropics/prompt-eng-interactive-tutorial` - Prompt 工程交互教程

### SDK & Agent
- `anthropics/claude-agent-sdk-python` - Claude Agent SDK (Python)
- `anthropics/claude-agent-sdk-typescript` - Claude Agent SDK (TypeScript)
- `anthropics/claude-agent-sdk-demos` - Claude Agent SDK 示例
- `anthropics/anthropic-sdk-python` - Anthropic SDK (Python)
- `anthropics/anthropic-sdk-typescript` - Anthropic SDK (TypeScript)
- `anthropics/anthropic-sdk-go` - Anthropic SDK (Go)
- `anthropics/anthropic-sdk-java` - Anthropic SDK (Java)

### 工具与集成
- `anthropics/claude-code-action` - Claude Code GitHub Action
- `anthropics/claude-code-security-review` - Claude Code 安全审查
- `anthropics/claude-plugins-official` - Claude 官方插件
- `anthropics/devcontainer-features` - DevContainer 特性

### 研究与评估
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
- `openai/swarm` - OpenAI 多代理编排
- `openai/codex` - 终端编程代理
- `crewAIInc/crewAI` - 角色扮演多代理框架
- `huggingface/smolagents` - 代码驱动代理
- `ruvnet/claude-flow` - Claude Agent 平台
- `bytedance/deer-flow` - 深度研究框架
- `langchain-ai/deepagents` - 深度代理

### AI 工具
- `openai/openai-python` - OpenAI Python SDK
- `openai/openai-quickstart-python` - OpenAI Quickstart
- `danielmiessler/fabric` - AI 工作流工具
- `ErikBjare/gptme` - AI 终端助手

### 其他
- `mem0ai/mem0` - 内存管理框架

## 配置文件

### 方式 1: 使用 .env 文件

创建项目根目录下的 `.env` 文件：

```bash
# .env
# ===========================================
# 必需配置
# ===========================================
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

# ===========================================
# 可选配置
# ===========================================
# GitHub Token（提高速率限制）
GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# 模型配置
ANTHROPIC_MODEL=glm-4.7

# 飞书通知（可选）
FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...
FEISHU_SECRET=your_secret_here
FEISHU_AT_MOBILES=13800138000,13900139000
FEISHU_MAX_SIGNALS=5

# Release 监控
INCLUDE_PRERELEASES=false

# 高级配置
MAX_CANDIDATES=20
DAYS_TO_LOOKBACK=7
MAX_PARALLEL_WORKERS=8
DAILY_TOKEN_BUDGET=100000
```

### 方式 2: 使用系统环境变量

```bash
# Linux/Mac
export ANTHROPIC_API_KEY="your_api_key_here"
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your_api_key_here"
$env:ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"
```

### 方式 3: GitHub Secrets（CI/CD）

在 GitHub 仓库设置中添加 Secrets：

1. 进入仓库 Settings
2. 选择 Secrets and variables → Actions
3. 点击 New repository secret
4. 添加以下 secrets：
   - `ANTHROPIC_API_KEY`（必需）
   - `ANTHROPIC_BASE_URL`（可选）
   - `GITHUB_TOKEN`（可选）
   - `FEISHU_WEBHOOK_URL`（可选，用于飞书通知）
   - `FEISHU_SECRET`（可选，飞书签名验证）
   - `FEISHU_AT_MOBILES`（可选，逗号分隔的手机号）

## 高级配置

### 自定义追踪仓库

编辑 `src/trendpluse/config.py`：

```python
class Settings(BaseSettings):
    github_repos: list[str] = [
        "anthropics/anthropic-sdk-python",
        "your-org/your-repo",  # 添加自定义仓库
    ]
```

或通过环境变量覆盖：

```bash
export GITHUB_REPOS="org/repo1,org/repo2,org/repo3"
```

### 并行处理配置

控制数据采集和 AI 分析的并行度：

```bash
# 并行采集线程数（1-32，默认 8）
# 较高的值可以提升处理速度，但可能增加 GitHub API 速率限制风险
export MAX_PARALLEL_WORKERS=8
```

### Token 预算控制

控制每日 API 调用成本：

```bash
# 每日 Token 预算（默认 100000）
export DAILY_TOKEN_BUDGET=100000
```

### 调整分析参数

编辑 `src/trendpluse/config.py`：

```python
class Settings(BaseSettings):
    # 影响评分阈值
    impact_threshold: int = 4

    # 最大候选事件数
    max_candidates: int = 20

    # PR 和 Release 回溯天数
    days_to_lookback: int = 7
```

### GitHub Actions 配置

编辑 `.github/workflows/run-daily.yml`：

```yaml
- name: Run TrendPulse analysis
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL || 'https://open.bigmodel.cn/api/anthropic' }}
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: uv run python scripts/run.py
```

### 飞书通知配置

#### 获取 Webhook URL

1. 在飞书群组中添加自定义机器人
2. 选择"自定义机器人" → "添加"
3. 复制 Webhook URL

#### 签名验证（可选）

1. 在机器人设置中启用"签名验证"
2. 复制签名密钥到 `FEISHU_SECRET`

#### @ 提醒配置

```bash
# 逗号分隔的手机号列表
export FEISHU_AT_MOBILES="13800138000,13900139000"
```

## 日志配置

### 调试模式

```bash
# 启用详细日志
export RUST_LOG=debug
uv run python scripts/run.py
```

### 日志级别

- `ERROR`: 仅错误
- `WARN`: 警告和错误
- `INFO`: 一般信息（默认）
- `DEBUG`: 详细调试信息

## 验证配置

运行以下命令验证配置是否正确：

```bash
# 检查环境变量
uv run python -c "from trendpluse.config import Settings; s = Settings(); print(s)"

# 测试 API 连接
uv run python -c "from trendpluse.config import Settings; from anthropic import Anthropic; s = Settings(); client = Anthropic(api_key=s.anthropic_api_key, base_url=s.anthropic_base_url); print('API 连接成功')"

# 测试 GitHub 连接
uv run python -c "from trendpluse.config import Settings; from github import Github; s = Settings(); g = Github(s.github_token); print('GitHub 连接成功')"
```

## 添加监控仓库

使用提供的脚本添加新仓库：

```bash
# 添加单个仓库
uv run python scripts/add_repo.py owner/repo

# 批量添加
uv run python scripts/add_repo.py owner/repo1 owner/repo2
```

## 故障排查

!!! error "API 认证失败"
    检查 API Key 是否正确：
    ```bash
    echo $ANTHROPIC_API_KEY
    ```

!!! error "GitHub 速率限制"
    使用 Personal Access Token 提高限制：
    - 默认: 60次/小时
    - 使用 Token: 5000次/小时

!!! error "报告未生成"
    检查日志输出，确认是否有符合条件的 PR

!!! error "并行处理失败"
    降低并行线程数：
    ```bash
    export MAX_PARALLEL_WORKERS=4
    ```

!!! error "飞书通知发送失败"
    检查 Webhook URL 和签名配置：
    ```bash
    echo $FEISHU_WEBHOOK_URL
    echo $FEISHU_SECRET
    ```
