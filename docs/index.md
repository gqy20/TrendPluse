# TrendPulse GitHub 趋势报告

<section class="tp-hero">
  <div class="tp-hero__content">
    <p class="tp-eyebrow">Signal Console / 2026</p>
    <h1>给 AI 编程生态做一块干净的情报屏</h1>
    <p class="tp-hero__lead">
      这里只保留有用的东西: 趋势、发布、故障、项目发现。
      不在前端堆产品说明，不在页面里灌架构废话。
    </p>
    <div class="tp-hero__actions">
      <a class="md-button md-button--primary" href="reports/index.md">阅读最新趋势</a>
      <a class="md-button" href="discovery.md">查看项目发现</a>
      <a class="md-button" href="https://github.com/gqy20/TrendPluse">查看源码</a>
    </div>
  </div>
  <div class="tp-hero__panel">
    <div class="tp-live-card">
      <div class="tp-live-card__label">TL;DR</div>
      <div class="tp-terminal-lines">
        <div><span>$</span> daily report</div>
        <div><span>&gt;</span> 看当天最高价值变化</div>
        <div><span>$</span> weekly digest</div>
        <div><span>&gt;</span> 判断是否形成持续趋势</div>
        <div><span>$</span> discovery</div>
        <div><span>&gt;</span> 决定是否扩充监控池</div>
      </div>
    </div>
  </div>
</section>

<div class="stats-dashboard">
  <div class="stat-dashboard-card">
    <div class="stat-value">51</div>
    <div class="stat-label">监控仓库</div>
    <div class="stat-trend">多源追踪 AI Coding / Agent / SDK</div>
  </div>
  <div class="stat-dashboard-card">
    <div class="stat-value">Daily</div>
    <div class="stat-label">日报更新</div>
    <div class="stat-trend">压缩当天高影响信号</div>
  </div>
  <div class="stat-dashboard-card">
    <div class="stat-value">Weekly</div>
    <div class="stat-label">周报聚合</div>
    <div class="stat-trend">识别连续演进，而不是孤立噪音</div>
  </div>
  <div class="stat-dashboard-card">
    <div class="stat-value">Issue</div>
    <div class="stat-label">问题洞察</div>
    <div class="stat-trend">把用户故障和抱怨收成可读结论</div>
  </div>
</div>
<p class="tp-stats-timestamp">最新日报: <a href="reports/report-2026-03-05.md">2026-03-05</a> · 最新发现: <a href="discovery-reports/discovery-2026-03-06.md">2026-03-06</a></p>

## 核心入口

<div class="tp-entry-grid">
  <a class="tp-entry-card" href="reports/index.md">
    <span class="tp-entry-card__icon">📈</span>
    <strong>趋势报告</strong>
    <p>直接进入日报、周报和今日聚焦。这里是主入口。</p>
    <span class="tp-entry-card__meta">默认先看这里</span>
  </a>
  <a class="tp-entry-card" href="discovery.md">
    <span class="tp-entry-card__icon">🧭</span>
    <strong>项目发现</strong>
    <p>看新仓库、分类分布和高优先级候选，用于补充监控池。</p>
    <span class="tp-entry-card__meta">用于扩充观察面</span>
  </a>
  <a class="tp-entry-card" href="https://github.com/gqy20/TrendPluse">
    <span class="tp-entry-card__icon">🔗</span>
    <strong>GitHub 仓库</strong>
    <p>实现细节、配置和自动化流程都回源码仓库，不在站点里堆文档。</p>
    <span class="tp-entry-card__meta">说明文档退出前台</span>
  </a>
</div>

## 关注什么

<div class="tp-signal-grid">
  <div class="tp-signal-tile">
    <h3>🔧 工程信号</h3>
    <p>SDK、工作流、性能、平台化、安全。</p>
  </div>
  <div class="tp-signal-tile">
    <h3>🔬 研究信号</h3>
    <p>评测、实验、能力边界、方法演进。</p>
  </div>
  <div class="tp-signal-tile">
    <h3>🎯 Release 动态</h3>
    <p>正式发布、重大升级、破坏性变更。</p>
  </div>
  <div class="tp-signal-tile">
    <h3>🧠 Issue 洞察</h3>
    <p>高频故障、失败样例、用户真实抱怨。</p>
  </div>
</div>

<!-- monitored-repos-section:start -->
## 监控范围概览

当前监控 **51** 个 GitHub 仓库，覆盖 **9** 个主要方向：

<div class="tp-coverage-grid">
  <div class="tp-coverage-pill">Anthropic 核心产品</div>
  <div class="tp-coverage-pill">Anthropic SDK & Agent</div>
  <div class="tp-coverage-pill">Anthropic 工具与集成</div>
  <div class="tp-coverage-pill">Anthropic 研究与评估</div>
  <div class="tp-coverage-pill">AI 编程助手</div>
  <div class="tp-coverage-pill">Agent 框架</div>
  <div class="tp-coverage-pill">自主 AI 编程</div>
  <div class="tp-coverage-pill">AI 编程模型</div>
  <div class="tp-coverage-pill">其他工具</div>
</div>

<details class="tp-details-card">
<summary><strong>展开查看完整监控仓库清单</strong></summary>

### Anthropic 核心产品

- **[anthropics/claude-code](https://github.com/anthropics/claude-code)**: Anthropic 的 CLI 编码代理工具。
- **[anthropics/skills](https://github.com/anthropics/skills)**: Anthropic 官方技能与工作流示例集合。
- **[anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)**: Claude 的实践食谱与集成示例。
- **[anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)**: Claude 快速上手示例项目。
- **[anthropics/courses](https://github.com/anthropics/courses)**: Anthropic 官方课程与教学材料。
- **[anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)**: Prompt Engineering 交互式教程。

### Anthropic SDK & Agent

- **[anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)**: Claude Agent SDK Python 版。
- **[anthropics/claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript)**: Claude Agent SDK TypeScript 版。
- **[anthropics/claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos)**: Claude Agent SDK 演示与示例。
- **[anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python)**: Anthropic Python 官方 SDK。
- **[anthropics/anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript)**: Anthropic TypeScript 官方 SDK。
- **[anthropics/anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go)**: Anthropic Go 官方 SDK。
- **[anthropics/anthropic-sdk-java](https://github.com/anthropics/anthropic-sdk-java)**: Anthropic Java 官方 SDK。

### Anthropic 工具与集成

- **[anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)**: Claude Code 的 GitHub Action 集成。
- **[anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review)**: Claude Code 安全审查工具。
- **[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)**: Anthropic 官方插件仓库。
- **[anthropics/devcontainer-features](https://github.com/anthropics/devcontainer-features)**: Anthropic 开发容器功能集合。

### Anthropic 研究与评估

- **[anthropics/evals](https://github.com/anthropics/evals)**: Anthropic 模型评测与评估工具。
- **[anthropics/political-neutrality-eval](https://github.com/anthropics/political-neutrality-eval)**: 政治中立性评测项目。
- **[anthropics/hh-rlhf](https://github.com/anthropics/hh-rlhf)**: Anthropic HH-RLHF 数据与研究仓库。

### AI 编程助手

- **[cline/cline](https://github.com/cline/cline)**: 面向开发者的开源 AI 编码助手。
- **[paul-gauthier/aider](https://github.com/paul-gauthier/aider)**: 终端中的 AI 结对编程工具。
- **[continuedev/continue](https://github.com/continuedev/continue)**: IDE 内的 AI 开发助手。
- **[openai/openai-python](https://github.com/openai/openai-python)**: OpenAI Python 官方 SDK。
- **[openai/openai-quickstart-python](https://github.com/openai/openai-quickstart-python)**: OpenAI Python 快速开始示例。
- **[danielmiessler/fabric](https://github.com/danielmiessler/fabric)**: 面向提示与工作流的知识自动化工具。
- **[ErikBjare/gptme](https://github.com/ErikBjare/gptme)**: 终端中的个人 AI 助手。

### Agent 框架

- **[TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI)**: 多代理自动化框架。
- **[Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)**: 经典自主代理框架。
- **[OpenDevin/OpenDevin](https://github.com/OpenDevin/OpenDevin)**: 面向软件工程任务的开放代理平台。
- **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)**: LLM 应用开发框架。
- **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)**: 多步骤、多代理编排框架。
- **[langgenius/dify](https://github.com/langgenius/dify)**: LLM 应用开发与运营平台。
- **[run-llama/llama\_index](https://github.com/run-llama/llama_index)**: 数据增强与检索式应用框架。
- **[microsoft/autogen](https://github.com/microsoft/autogen)**: 微软的多代理协作框架。
- **[microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)**: 语义内核与 AI 编排 SDK。
- **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)**: Gemini 的命令行工具。
- **[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope)**: 面向智能体应用的开发框架。
- **[agno-agi/agno](https://github.com/agno-agi/agno)**: Agent 构建与运行框架。
- **[openai/swarm](https://github.com/openai/swarm)**: 轻量级多代理实验框架。
- **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)**: 以角色协作为核心的多代理框架。
- **[huggingface/smolagents](https://github.com/huggingface/smolagents)**: Hugging Face 的轻量智能体框架。
- **[langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)**: LangChain 的深度代理实验项目。

### 自主 AI 编程

- **[AndyMik90/Auto-Claude](https://github.com/AndyMik90/Auto-Claude)**: 围绕 Claude 的自主编码代理项目。
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)**: 面向开发流程的开源 AI 编码工具。
- **[zed-industries/zed](https://github.com/zed-industries/zed)**: 面向协作与 AI 的现代编辑器。

### AI 编程模型

- **[openai/codex](https://github.com/openai/codex)**: OpenAI 代码代理相关项目。
- **[TabbyML/tabby](https://github.com/TabbyML/tabby)**: 自托管代码补全与助手平台。

### 其他工具

- **[ruvnet/claude-flow](https://github.com/ruvnet/claude-flow)**: Claude 工作流与代理编排项目。
- **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)**: 字节跳动开源的工作流项目。
- **[openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter)**: 可执行系统命令的开放解释器代理。

</details>
<!-- monitored-repos-section:end -->

**项目仓库**: [gqy20/TrendPluse](https://github.com/gqy20/TrendPluse)
