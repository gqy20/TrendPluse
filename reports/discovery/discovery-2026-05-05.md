# 项目发现报告 (2026-05-05)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 122 |
| 去重移除 | 32 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 14 |
| 💬 LLM 界面 | 21 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 16 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 68 |

## 📑 快速导航

### 按技术分类
- [🤖 AI Agents](#ai-agents)
- [🔍 RAG/检索](#rag-检索)
- [💬 LLM 界面](#llm-界面)
- [🧠 机器学习框架](#机器学习框架)
- [🛠️ 开发工具](#开发工具)
- [⚙️ DevOps/基础设施](#devops-基础设施)
- [📈 监控/观测](#监控-观测)
- [🌐 Web 框架](#web-框架)
- [📊 数据/基础设施](#数据-基础设施)
- [📚 学习资源](#学习资源)
- [📁 其他](#其他)


## 🤖 AI Agents (27 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,635 |
| 语言 | Python |
| Forks | 19,302 |
| Issues | 343 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能强大的开源 AI 聊天界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13.5 万 Stars，是当前最受欢迎的 LLM WebUI 解决方案之一。它提供开箱即用的 RAG 和 MCP 支持，适合希望快速部署私有化 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端兼容: 同时支持 Ollama 本地模型和 OpenAI API，提供统一的交互接口
- RAG 检索增强: 内置知识库增强功能，支持文档导入和语义检索，提升回答质量
- MCP 协议支持: 支持 Model Context Protocol，可扩展连接多种数据源和工具
- 自托管友好: 提供 Docker 一键部署方案，数据完全自主掌控
- OpenAPI 兼容: 完整的 RESTful API 接口，便于与现有系统集成

**适用场景**:
- 企业私有化部署: 需要在内部网络中部署 AI 助手，保护敏感数据
- 本地 LLM 开发调试: 开发者在本地运行开源模型时需要一个友好的调试界面
- 团队协作与知识管理: 利用 RAG 功能构建团队知识库，实现文档问答
- 个性化 AI 定制: 根据特定需求定制 AI 助手的行为和功能



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,981 |
| 语言 | Python |
| Forks | 20,432 |
| Issues | 8,370 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高质量 AI Agent 框架，凭借超过 13 万 Stars 成为最受欢迎的 AI Agent 项目之一，支持 Claude、ChatGPT 等多主流 LLM，提供灵活的 Agent 编排和工具调用能力，适合构建从简单助手到复杂自动化工作流的各类 AI 应用。

**技术亮点**:
- 多 LLM 后端支持：统一集成 Anthropic Claude、OpenAI ChatGPT 等主流大语言模型，提供灵活的模型切换机制
- 模块化 Agent 架构：采用可扩展的模块设计，支持自定义工具、工具链和工作流编排
- 强大的工具调用能力：内置 ReAct、Tool Use 等 Agent 范式，支持复杂的多步推理和任务执行
- MIT 许可证开源：完全开放源代码，商业友好，便于企业级项目采用和二次开发
- 活跃的社区生态：依托 NousResearch 研究组织，持续更新迭代，拥有丰富的文档和示例

**适用场景**:
- 个人开发者：快速构建 AI 助手、自动化脚本、智能写作工具和个性化工作流
- 企业应用：开发智能客服系统、业务流程自动化、知识库问答和数据分析代理
- AI 研究与原型开发：用于实验新的 Agent 范式、工具调用策略和多模型协作机制



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,841 |
| 语言 | JavaScript |
| Forks | 26,923 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手打造的性能优化系统，汇聚了 Skills、Instincts、Memory 等核心模块，173k+ Stars 证明了其在开发者社区的高度认可，能显著提升 Claude Code、Cursor 等工具的开发效率和智能化水平。

**技术亮点**:
- 统一优化框架：支持 Claude Code、Codex、Opencode、Cursor 等多款主流 AI 编程助手的性能调优
- Skills 机制：模块化技能系统，扩展 AI Agent 的任务处理能力和专业领域
- Memory 模块：持久化上下文管理，优化长对话和多轮交互场景下的表现
- Security 安全层：内置安全机制，确保 AI Agent 操作的可信度和代码质量
- Research-first 理念：研究驱动的开发模式，持续探索前沿优化技术

**适用场景**:
- 企业开发团队：规模化部署 AI 编程工具，优化团队协作效率和代码质量标准
- 个人开发者：提升日常编码效率，获得更智能的代码补全、重构和调试辅助
- AI Agent 研究：作为性能优化实验平台，探索 LLM 与开发工具深度集成的最佳实践



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
| 语言 | Go |
| Forks | 4,057 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持文本生成、图像、音频、视频等多种模型类型，且可在无 GPU 环境下运行，API 兼容 OpenAI 大幅降低了从云端 AI 到本地部署的迁移成本，特别适合隐私敏感和成本敏感的场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、语音合成（TTS）和目标检测等多种模型类型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低硬件门槛和部署成本
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移至本地部署
- Go 语言高性能架构：采用 Go 开发，具备优秀的并发处理能力和跨平台部署能力
- 去中心化架构：支持 libp2p 分布式网络，可构建去中心化的 AI 服务网络

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等行业需要本地处理敏感数据，避免数据上传到第三方云服务
- 成本优化场景：中小企业或个人开发者希望降低 AI API 调用成本，实现自有模型的本地化部署
- 私有化 AI 服务：企业需要部署私有的 AI 能力，支持定制化模型和内网隔离部署



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,063 |
| 语言 | TypeScript |
| Forks | 15,069 |
| Issues | 762 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI智能体协作平台，拥有76K+ Stars的超高人气，支持多模型集成和多智能体协作设计，特别适合需要快速构建AI工作流的团队使用，是目前最成熟的Agent Harness开源实现之一。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一的API抽象层
- MCP协议支持：完整实现 Model Context Protocol，实现智能体与外部工具/数据源的标准化连接
- 多智能体协作框架：支持多Agent协同工作，Agent可作为基本工作交互单元设计复杂工作流
- 知识库集成：内置RAG能力，支持向量检索和知识管理，实现私有知识增强
- TypeScript全栈架构：现代化技术栈，便于二次开发和定制化扩展

**适用场景**:
- 企业AI工作流自动化：通过多Agent协作处理复杂业务流程，如客服自动化、文档处理、数据分析等
- 个人开发者AI应用开发：快速搭建对话助手、知识问答系统、研究辅助工具等原型应用
- 团队协作与知识管理：构建团队专属的AI知识库，支持多人共享和持续学习的Agent teammate



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,424 |
| 语言 | TypeScript |
| Forks | 6,216 |
| Issues | 74 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 解决了 AI 编码助手缺乏长期记忆的核心痛点，通过自动捕获、压缩和检索历史上下文，让 Claude Code 在新会话中"记住"之前的开发进展和决策，大幅提升开发效率。

**技术亮点**:
- 智能 AI 压缩：基于 Claude Agent SDK 实现会话内容自动压缩，有效控制记忆存储体积
- 多存储后端支持：集成 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储方案
- RAG 检索增强：采用 Embeddings 和 RAG 技术实现语义级别的上下文检索
- TypeScript 原生开发：完整的类型安全保证，良好的 IDE 支持和可维护性
- 无缝插件集成：作为 Claude Code 插件直接集成，开箱即用的用户体验

**适用场景**:
- 大型项目的持续开发：开发者可以在多日或数周的项目中保持上下文连贯，无需重复解释项目背景
- 代码审查与重构：Claude 能检索历史设计决策，理解代码演变过程，提供更准确的建议
- 团队知识传承：项目成员可快速了解项目历史、技术选型理由和过去的踩坑记录



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,942 |
| 语言 | Python |
| Forks | 8,667 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架之一，支持 100+ 主流语言模型的一站式微调，集成 LoRA/QLoRA/RLHF 等多种高效微调技术，ACL 2024 学术顶会认证，特别适合需要快速定制垂直领域大模型的企业和个人开发者。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 模型，包括 LLaMA3、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成多种 PEFT 技术：LoRA、Lora++、QLoRA、Adapter、Prefix Tuning 等，支持模型高效微调
- 内置 RLHF 全流程支持，包括 DPO、PPO、KTO 等强化学习微调算法
- 支持 INT4/INT8/FP8 量化训练，大幅降低 GPU 显存占用，单卡即可微调大模型
- 提供 WebUI、CLI、Python API 三种使用方式，支持分布式多卡训练和 Gradio 可视化监控

**适用场景**:
- 企业垂直领域定制：基于 LlamaFactory 微调行业专属大模型，如医疗问答、金融分析、法律文档处理
- 个人开发者/研究者：低成本快速实验新模型和微调方法，支持单卡训练降低门槛
- 模型能力增强：对开源基础模型进行指令微调、对话微调或 RLHF 对齐，提升模型实用性和安全性



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,141 |
| 语言 | HTML |
| Forks | 5,087 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,024 |
| 语言 | Python |
| Forks | 10,048 |
| Issues | 357 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,074 |
| 语言 | Java |
| Forks | 15,966 |
| Issues | 17 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,648 |
| 语言 | Python |
| Forks | 5,154 |
| Issues | 102 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,106 |
| 语言 | Python |
| Forks | 6,196 |
| Issues | 74 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,301 |
| 语言 | TypeScript |
| Forks | 4,831 |
| Issues | 508 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,492 |
| 语言 | TypeScript |
| Forks | 7,262 |
| Issues | 305 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,547 |
| 语言 | JavaScript |
| Forks | 6,436 |
| Issues | 345 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,670 |
| 语言 | Python |
| Forks | 9,191 |
| Issues | 418 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,927 |
| 语言 | TypeScript |
| Forks | 4,545 |
| Issues | 685 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,881 |
| 语言 | Python |
| Forks | 16,100 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,251 |
| 语言 | Python |
| Forks | 10,471 |
| Issues | 227 |
| Topics | ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,560 |
| 语言 | TypeScript |
| Forks | 24,267 |
| Issues | 832 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 186,784 |
| 语言 | TypeScript |
| Forks | 57,374 |
| Issues | 1,444 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,418 |
| 语言 | Java |
| Forks | 46,152 |
| Issues | 63 |
| Topics | agent, context-engineering, interview, java, jvm, mcp, mysql, redis, redisson, skills, spring, system, system-design |
| 许可证 | Apache License 2.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,720 |
| 语言 | Python |
| Forks | 8,907 |
| Issues | 935 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### microsoft/ai-agents-for-beginners

**描述**: 12 Lessons to Get Started Building AI Agents

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,555 |
| 语言 | Jupyter Notebook |
| Forks | 20,505 |
| Issues | 5 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,113 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,209 |
| 语言 | TypeScript |
| Forks | 9,553 |
| Issues | 115 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,783 |
| 语言 | Rust |
| Forks | 3,897 |
| Issues | 736 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (14 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,635 |
| 语言 | Python |
| Forks | 19,302 |
| Issues | 343 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能强大的开源 AI 聊天界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13.5 万 Stars，是当前最受欢迎的 LLM WebUI 解决方案之一。它提供开箱即用的 RAG 和 MCP 支持，适合希望快速部署私有化 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端兼容: 同时支持 Ollama 本地模型和 OpenAI API，提供统一的交互接口
- RAG 检索增强: 内置知识库增强功能，支持文档导入和语义检索，提升回答质量
- MCP 协议支持: 支持 Model Context Protocol，可扩展连接多种数据源和工具
- 自托管友好: 提供 Docker 一键部署方案，数据完全自主掌控
- OpenAPI 兼容: 完整的 RESTful API 接口，便于与现有系统集成

**适用场景**:
- 企业私有化部署: 需要在内部网络中部署 AI 助手，保护敏感数据
- 本地 LLM 开发调试: 开发者在本地运行开源模型时需要一个友好的调试界面
- 团队协作与知识管理: 利用 RAG 功能构建团队知识库，实现文档问答
- 个性化 AI 定制: 根据特定需求定制 AI 助手的行为和功能



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,063 |
| 语言 | TypeScript |
| Forks | 15,069 |
| Issues | 762 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI智能体协作平台，拥有76K+ Stars的超高人气，支持多模型集成和多智能体协作设计，特别适合需要快速构建AI工作流的团队使用，是目前最成熟的Agent Harness开源实现之一。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一的API抽象层
- MCP协议支持：完整实现 Model Context Protocol，实现智能体与外部工具/数据源的标准化连接
- 多智能体协作框架：支持多Agent协同工作，Agent可作为基本工作交互单元设计复杂工作流
- 知识库集成：内置RAG能力，支持向量检索和知识管理，实现私有知识增强
- TypeScript全栈架构：现代化技术栈，便于二次开发和定制化扩展

**适用场景**:
- 企业AI工作流自动化：通过多Agent协作处理复杂业务流程，如客服自动化、文档处理、数据分析等
- 个人开发者AI应用开发：快速搭建对话助手、知识问答系统、研究辅助工具等原型应用
- 团队协作与知识管理：构建团队专属的AI知识库，支持多人共享和持续学习的Agent teammate



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,424 |
| 语言 | TypeScript |
| Forks | 6,216 |
| Issues | 74 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 解决了 AI 编码助手缺乏长期记忆的核心痛点，通过自动捕获、压缩和检索历史上下文，让 Claude Code 在新会话中"记住"之前的开发进展和决策，大幅提升开发效率。

**技术亮点**:
- 智能 AI 压缩：基于 Claude Agent SDK 实现会话内容自动压缩，有效控制记忆存储体积
- 多存储后端支持：集成 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储方案
- RAG 检索增强：采用 Embeddings 和 RAG 技术实现语义级别的上下文检索
- TypeScript 原生开发：完整的类型安全保证，良好的 IDE 支持和可维护性
- 无缝插件集成：作为 Claude Code 插件直接集成，开箱即用的用户体验

**适用场景**:
- 大型项目的持续开发：开发者可以在多日或数周的项目中保持上下文连贯，无需重复解释项目背景
- 代码审查与重构：Claude 能检索历史设计决策，理解代码演变过程，提供更准确的建议
- 团队知识传承：项目成员可快速了解项目历史、技术选型理由和过去的踩坑记录



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,074 |
| 语言 | Java |
| Forks | 15,966 |
| Issues | 17 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,648 |
| 语言 | Python |
| Forks | 5,154 |
| Issues | 102 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,106 |
| 语言 | Python |
| Forks | 6,196 |
| Issues | 74 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,896 |
| 语言 | TypeScript |
| Forks | 12,307 |
| Issues | 992 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,547 |
| 语言 | JavaScript |
| Forks | 6,436 |
| Issues | 345 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,881 |
| 语言 | Python |
| Forks | 16,100 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,115 |
| 语言 | Python |
| Forks | 10,366 |
| Issues | 204 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,560 |
| 语言 | TypeScript |
| Forks | 24,267 |
| Issues | 832 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### safishamsi/graphify

**描述**: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,217 |
| 语言 | Python |
| Forks | 4,716 |
| Issues | 231 |
| Topics | antigravity, claude-code, codex, gemini, graphrag, knowledge-graph, leiden, openclaw, rag, skills, tree-sitter |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,116 |
| 语言 | Go |
| Forks | 3,988 |
| Issues | 1,072 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### HKUDS/LightRAG

**描述**: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,772 |
| 语言 | Python |
| Forks | 4,926 |
| Issues | 228 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (21 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,635 |
| 语言 | Python |
| Forks | 19,302 |
| Issues | 343 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能强大的开源 AI 聊天界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13.5 万 Stars，是当前最受欢迎的 LLM WebUI 解决方案之一。它提供开箱即用的 RAG 和 MCP 支持，适合希望快速部署私有化 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端兼容: 同时支持 Ollama 本地模型和 OpenAI API，提供统一的交互接口
- RAG 检索增强: 内置知识库增强功能，支持文档导入和语义检索，提升回答质量
- MCP 协议支持: 支持 Model Context Protocol，可扩展连接多种数据源和工具
- 自托管友好: 提供 Docker 一键部署方案，数据完全自主掌控
- OpenAPI 兼容: 完整的 RESTful API 接口，便于与现有系统集成

**适用场景**:
- 企业私有化部署: 需要在内部网络中部署 AI 助手，保护敏感数据
- 本地 LLM 开发调试: 开发者在本地运行开源模型时需要一个友好的调试界面
- 团队协作与知识管理: 利用 RAG 功能构建团队知识库，实现文档问答
- 个性化 AI 定制: 根据特定需求定制 AI 助手的行为和功能



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,981 |
| 语言 | Python |
| Forks | 20,432 |
| Issues | 8,370 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高质量 AI Agent 框架，凭借超过 13 万 Stars 成为最受欢迎的 AI Agent 项目之一，支持 Claude、ChatGPT 等多主流 LLM，提供灵活的 Agent 编排和工具调用能力，适合构建从简单助手到复杂自动化工作流的各类 AI 应用。

**技术亮点**:
- 多 LLM 后端支持：统一集成 Anthropic Claude、OpenAI ChatGPT 等主流大语言模型，提供灵活的模型切换机制
- 模块化 Agent 架构：采用可扩展的模块设计，支持自定义工具、工具链和工作流编排
- 强大的工具调用能力：内置 ReAct、Tool Use 等 Agent 范式，支持复杂的多步推理和任务执行
- MIT 许可证开源：完全开放源代码，商业友好，便于企业级项目采用和二次开发
- 活跃的社区生态：依托 NousResearch 研究组织，持续更新迭代，拥有丰富的文档和示例

**适用场景**:
- 个人开发者：快速构建 AI 助手、自动化脚本、智能写作工具和个性化工作流
- 企业应用：开发智能客服系统、业务流程自动化、知识库问答和数据分析代理
- AI 研究与原型开发：用于实验新的 Agent 范式、工具调用策略和多模型协作机制



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,841 |
| 语言 | JavaScript |
| Forks | 26,923 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手打造的性能优化系统，汇聚了 Skills、Instincts、Memory 等核心模块，173k+ Stars 证明了其在开发者社区的高度认可，能显著提升 Claude Code、Cursor 等工具的开发效率和智能化水平。

**技术亮点**:
- 统一优化框架：支持 Claude Code、Codex、Opencode、Cursor 等多款主流 AI 编程助手的性能调优
- Skills 机制：模块化技能系统，扩展 AI Agent 的任务处理能力和专业领域
- Memory 模块：持久化上下文管理，优化长对话和多轮交互场景下的表现
- Security 安全层：内置安全机制，确保 AI Agent 操作的可信度和代码质量
- Research-first 理念：研究驱动的开发模式，持续探索前沿优化技术

**适用场景**:
- 企业开发团队：规模化部署 AI 编程工具，优化团队协作效率和代码质量标准
- 个人开发者：提升日常编码效率，获得更智能的代码补全、重构和调试辅助
- AI Agent 研究：作为性能优化实验平台，探索 LLM 与开发工具深度集成的最佳实践



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,063 |
| 语言 | TypeScript |
| Forks | 15,069 |
| Issues | 762 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI智能体协作平台，拥有76K+ Stars的超高人气，支持多模型集成和多智能体协作设计，特别适合需要快速构建AI工作流的团队使用，是目前最成熟的Agent Harness开源实现之一。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一的API抽象层
- MCP协议支持：完整实现 Model Context Protocol，实现智能体与外部工具/数据源的标准化连接
- 多智能体协作框架：支持多Agent协同工作，Agent可作为基本工作交互单元设计复杂工作流
- 知识库集成：内置RAG能力，支持向量检索和知识管理，实现私有知识增强
- TypeScript全栈架构：现代化技术栈，便于二次开发和定制化扩展

**适用场景**:
- 企业AI工作流自动化：通过多Agent协作处理复杂业务流程，如客服自动化、文档处理、数据分析等
- 个人开发者AI应用开发：快速搭建对话助手、知识问答系统、研究辅助工具等原型应用
- 团队协作与知识管理：构建团队专属的AI知识库，支持多人共享和持续学习的Agent teammate



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,424 |
| 语言 | TypeScript |
| Forks | 6,216 |
| Issues | 74 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 解决了 AI 编码助手缺乏长期记忆的核心痛点，通过自动捕获、压缩和检索历史上下文，让 Claude Code 在新会话中"记住"之前的开发进展和决策，大幅提升开发效率。

**技术亮点**:
- 智能 AI 压缩：基于 Claude Agent SDK 实现会话内容自动压缩，有效控制记忆存储体积
- 多存储后端支持：集成 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储方案
- RAG 检索增强：采用 Embeddings 和 RAG 技术实现语义级别的上下文检索
- TypeScript 原生开发：完整的类型安全保证，良好的 IDE 支持和可维护性
- 无缝插件集成：作为 Claude Code 插件直接集成，开箱即用的用户体验

**适用场景**:
- 大型项目的持续开发：开发者可以在多日或数周的项目中保持上下文连贯，无需重复解释项目背景
- 代码审查与重构：Claude 能检索历史设计决策，理解代码演变过程，提供更准确的建议
- 团队知识传承：项目成员可快速了解项目历史、技术选型理由和过去的踩坑记录



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,610 |
| 语言 | HTML |
| Forks | 21,079 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是全球最大的开源 ChatGPT 提示词库之一，拥有超过 16 万 Stars 的社区认可，支持自托管部署保护隐私，是 AI 时代必备的提示词资源集合和实践工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代全栈架构，提供良好的开发体验和类型安全
- 支持多模型平台集成（ChatGPT、Claude、Gemini、GPT-4），适配多种 LLM 接口
- 提供完整的自托管部署方案，企业可完全私有化部署保障数据安全
- 社区驱动的提示词贡献机制，持续更新高质量提示词库
- 采用响应式设计，支持 Web 端和移动端访问

**适用场景**:
- 个人开发者：寻找高质量提示词灵感，提升 AI 应用开发效率
- 企业自托管：私有化部署企业级提示词管理系统，保护内部知识资产
- AI学习者：学习提示词工程最佳实践，掌握与 LLM 高效交互技巧



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,430 |
| 语言 | Python |
| Forks | 2,975 |
| Issues | 182 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过"穴居人语言"风格实现高达 65% 的 token 消耗削减，在 LLM 应用成本日益重要的背景下，这种简单而有效的 prompt 工程技巧对于追求效率和成本优化的开发者来说具有极高的实用价值。

**技术亮点**:
- Token 优化算法：通过语言风格转换实现 token 消耗大幅降低，核心基于简化和压缩 prompt 的工程实践
- Claude Code 集成：作为官方支持的 Claude Code skill 实现，可无缝集成到开发工作流中
- Python 实现：采用 Python 编写，便于理解和二次开发，生态兼容性强
- Prompt 工程创新：开创性地将 meme 文化与 LLM 优化结合，展示了提示词设计的无限可能
- 性能提升：在保持输出质量的同时显著减少 token 数量，降低延迟并提升响应速度

**适用场景**:
- 成本敏感型应用：企业和个人开发者在大量使用 Claude API 时，用于降低订阅费用和 API 调用成本
- 追求高效率的开发团队：需要快速迭代的项目，通过减少 token 传输量来缩短响应等待时间
- Claude Code 重度用户：日常使用 Claude 进行代码编写、调试和重构的开发者，优化个人工作流效率



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,141 |
| 语言 | HTML |
| Forks | 5,087 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,024 |
| 语言 | Python |
| Forks | 10,048 |
| Issues | 357 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,547 |
| 语言 | JavaScript |
| Forks | 6,436 |
| Issues | 345 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,670 |
| 语言 | Python |
| Forks | 9,191 |
| Issues | 418 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,927 |
| 语言 | TypeScript |
| Forks | 4,545 |
| Issues | 685 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,560 |
| 语言 | TypeScript |
| Forks | 24,267 |
| Issues | 832 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,091 |
| 语言 | Python |
| Forks | 16,437 |
| Issues | 4,800 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,720 |
| 语言 | Python |
| Forks | 8,907 |
| Issues | 935 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,113 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,772 |
| 语言 | Go |
| Forks | 15,993 |
| Issues | 3,172 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 91,983 |
| 语言 | Jupyter Notebook |
| Forks | 14,202 |
| Issues | 8 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,209 |
| 语言 | TypeScript |
| Forks | 9,553 |
| Issues | 115 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,459 |
| 语言 | Rust |
| Forks | 9,709 |
| Issues | 1 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 120,694 |
| 语言 | Python |
| Forks | 8,065 |
| Issues | 625 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (8 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,942 |
| 语言 | Python |
| Forks | 8,667 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架之一，支持 100+ 主流语言模型的一站式微调，集成 LoRA/QLoRA/RLHF 等多种高效微调技术，ACL 2024 学术顶会认证，特别适合需要快速定制垂直领域大模型的企业和个人开发者。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 模型，包括 LLaMA3、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成多种 PEFT 技术：LoRA、Lora++、QLoRA、Adapter、Prefix Tuning 等，支持模型高效微调
- 内置 RLHF 全流程支持，包括 DPO、PPO、KTO 等强化学习微调算法
- 支持 INT4/INT8/FP8 量化训练，大幅降低 GPU 显存占用，单卡即可微调大模型
- 提供 WebUI、CLI、Python API 三种使用方式，支持分布式多卡训练和 Gradio 可视化监控

**适用场景**:
- 企业垂直领域定制：基于 LlamaFactory 微调行业专属大模型，如医疗问答、金融分析、法律文档处理
- 个人开发者/研究者：低成本快速实验新模型和微调方法，支持单卡训练降低门槛
- 模型能力增强：对开源基础模型进行指令微调、对话微调或 RLHF 对齐，提升模型实用性和安全性



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,053 |
| 语言 | Python |
| Forks | 6,713 |
| Issues | 77 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，整合了股票、加密货币、期权、固定收益等多类型金融数据，并内置 AI 和机器学习分析能力，非常适合量化分析师和金融 AI 应用开发者使用，能够显著提升金融数据分析效率。

**技术亮点**:
- 统一的数据 API 接口：提供标准化的数据访问接口，整合多个数据源，简化金融数据获取流程
- 全面的金融数据类型覆盖：支持股票、加密货币、期权、衍生品、固定收益、经济数据等多维度金融分析
- AI 与机器学习集成：内置 AI Agent 支持，可结合机器学习模型进行智能金融分析和预测
- 开源可扩展架构：采用模块化设计，支持自定义扩展和数据源集成，便于企业级定制开发
- 丰富的分析工具集：提供技术分析、基本面分析、量化回测等完整的金融分析工具链

**适用场景**:
- 量化交易研究：用于获取市场数据、进行策略回测和量化分析
- 金融数据分析：整合多市场数据源，进行综合金融研究和投资分析
- AI 金融应用开发：基于平台 API 构建智能投顾、风险预测等 AI 金融应用
- 投资组合管理与风险分析：支持多资产类别的投资组合构建和风险评估



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,610 |
| 语言 | HTML |
| Forks | 21,079 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是全球最大的开源 ChatGPT 提示词库之一，拥有超过 16 万 Stars 的社区认可，支持自托管部署保护隐私，是 AI 时代必备的提示词资源集合和实践工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代全栈架构，提供良好的开发体验和类型安全
- 支持多模型平台集成（ChatGPT、Claude、Gemini、GPT-4），适配多种 LLM 接口
- 提供完整的自托管部署方案，企业可完全私有化部署保障数据安全
- 社区驱动的提示词贡献机制，持续更新高质量提示词库
- 采用响应式设计，支持 Web 端和移动端访问

**适用场景**:
- 个人开发者：寻找高质量提示词灵感，提升 AI 应用开发效率
- 企业自托管：私有化部署企业级提示词管理系统，保护内部知识资产
- AI学习者：学习提示词工程最佳实践，掌握与 LLM 高效交互技巧



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,278 |
| 语言 | Python |
| Forks | 33,116 |
| Issues | 2,341 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,091 |
| 语言 | Python |
| Forks | 16,437 |
| Issues | 4,800 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### Comfy-Org/ComfyUI

**描述**: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 111,464 |
| 语言 | Python |
| Forks | 13,017 |
| Issues | 3,985 |
| Topics | ai, comfy, comfyui, python, pytorch, stable-diffusion |
| 许可证 | GNU General Public License v3.0 |


### pytorch/pytorch

**描述**: Tensors and Dynamic neural networks in Python with strong GPU acceleration

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,664 |
| 语言 | Python |
| Forks | 27,674 |
| Issues | 18,598 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 91,983 |
| 语言 | Jupyter Notebook |
| Forks | 14,202 |
| Issues | 8 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


## 🛠️ 开发工具 (16 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,841 |
| 语言 | JavaScript |
| Forks | 26,923 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手打造的性能优化系统，汇聚了 Skills、Instincts、Memory 等核心模块，173k+ Stars 证明了其在开发者社区的高度认可，能显著提升 Claude Code、Cursor 等工具的开发效率和智能化水平。

**技术亮点**:
- 统一优化框架：支持 Claude Code、Codex、Opencode、Cursor 等多款主流 AI 编程助手的性能调优
- Skills 机制：模块化技能系统，扩展 AI Agent 的任务处理能力和专业领域
- Memory 模块：持久化上下文管理，优化长对话和多轮交互场景下的表现
- Security 安全层：内置安全机制，确保 AI Agent 操作的可信度和代码质量
- Research-first 理念：研究驱动的开发模式，持续探索前沿优化技术

**适用场景**:
- 企业开发团队：规模化部署 AI 编程工具，优化团队协作效率和代码质量标准
- 个人开发者：提升日常编码效率，获得更智能的代码补全、重构和调试辅助
- AI Agent 研究：作为性能优化实验平台，探索 LLM 与开发工具深度集成的最佳实践



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
| 语言 | Go |
| Forks | 4,057 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持文本生成、图像、音频、视频等多种模型类型，且可在无 GPU 环境下运行，API 兼容 OpenAI 大幅降低了从云端 AI 到本地部署的迁移成本，特别适合隐私敏感和成本敏感的场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、语音合成（TTS）和目标检测等多种模型类型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低硬件门槛和部署成本
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移至本地部署
- Go 语言高性能架构：采用 Go 开发，具备优秀的并发处理能力和跨平台部署能力
- 去中心化架构：支持 libp2p 分布式网络，可构建去中心化的 AI 服务网络

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等行业需要本地处理敏感数据，避免数据上传到第三方云服务
- 成本优化场景：中小企业或个人开发者希望降低 AI API 调用成本，实现自有模型的本地化部署
- 私有化 AI 服务：企业需要部署私有的 AI 能力，支持定制化模型和内网隔离部署



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,074 |
| 语言 | Java |
| Forks | 15,966 |
| Issues | 17 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,670 |
| 语言 | Python |
| Forks | 9,191 |
| Issues | 418 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,927 |
| 语言 | TypeScript |
| Forks | 4,545 |
| Issues | 685 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 186,784 |
| 语言 | TypeScript |
| Forks | 57,374 |
| Issues | 1,444 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,113 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 432,139 |
| 语言 | Python |
| Forks | 47,225 |
| Issues | 1,326 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,677 |
| 语言 | Python |
| Forks | 13,340 |
| Issues | 2,505 |
| Topics | cli, downloader, python, sponsorblock, youtube-dl, youtube-downloader, yt-dlp |
| 许可证 | The Unlicense |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,910 |
| 语言 | Python |
| Forks | 9,206 |
| Issues | 185 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


### sherlock-project/sherlock

**描述**: Hunt down social media accounts by username across social networks

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,947 |
| 语言 | Python |
| Forks | 9,676 |
| Issues | 260 |
| Topics | cli, cti, cybersecurity, forensics, hacktoberfest, information-gathering, infosec, linux, osint, pentesting, python, python3, reconnaissance, redteam, sherlock, tools |
| 许可证 | MIT License |


### microsoft/vscode

**描述**: Visual Studio Code

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 184,586 |
| 语言 | TypeScript |
| Forks | 39,648 |
| Issues | 17,196 |
| Topics | editor, electron, microsoft, typescript, visual-studio-code |
| 许可证 | MIT License |


### puppeteer/puppeteer

**描述**: JavaScript API for Chrome and Firefox

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,245 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 305 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### hoppscotch/hoppscotch

**描述**: Open-Source API Development Ecosystem • https://hoppscotch.io • Offline, On-Prem & Cloud • Web, Desktop & CLI • Open-Source Alternative to Postman, Insomnia

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,109 |
| 语言 | TypeScript |
| Forks | 5,855 |
| Issues | 701 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,997 |
| 语言 | Go |
| Forks | 2,800 |
| Issues | 315 |
| Topics | bash, cli, fish, fzf, go, neovim, tmux, unix, vim, zsh |
| 许可证 | MIT License |


### jesseduffield/lazygit

**描述**: simple terminal UI for git commands

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,463 |
| 语言 | Go |
| Forks | 2,811 |
| Issues | 956 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,927 |
| 语言 | TypeScript |
| Forks | 4,545 |
| Issues | 685 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 186,784 |
| 语言 | TypeScript |
| Forks | 57,374 |
| Issues | 1,444 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,113 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,668 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 241 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


### kubernetes/kubernetes

**描述**: Production-Grade Container Scheduling and Management

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 122,074 |
| 语言 | Go |
| Forks | 42,969 |
| Issues | 2,648 |
| Topics | cncf, containers, go, kubernetes |
| 许可证 | Apache License 2.0 |


### moby/moby

**描述**: The Moby Project - a collaborative project for the container ecosystem to assemble container-based systems

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,518 |
| 语言 | Go |
| Forks | 18,927 |
| Issues | 3,818 |
| Topics | containers, docker, go, golang |
| 许可证 | Apache License 2.0 |


### go-gitea/gitea

**描述**: Git with a cup of tea! Painless self-hosted all-in-one software development service, including Git hosting, code review, team collaboration, package registry and CI/CD

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,379 |
| 语言 | Go |
| Forks | 6,661 |
| Issues | 2,779 |
| Topics | bitbucket, cicd, devops, docker-registry-v2, git, git-gui, git-lfs, git-server, gitea, github, github-actions, gitlab, go, golang, hacktoberfest, maven-server, npm-registry, self-hosted, typescript, vue |
| 许可证 | MIT License |


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,485 |
| 语言 | Go |
| Forks | 5,058 |
| Issues | 982 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
| 许可证 | MIT License |


### puppeteer/puppeteer

**描述**: JavaScript API for Chrome and Firefox

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,245 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 305 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### Stirling-Tools/Stirling-PDF

**描述**: #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,220 |
| 语言 | TypeScript |
| Forks | 6,847 |
| Issues | 414 |
| Topics | docker, hacktoberfest, java, pdf, pdf-converter, pdf-editor, pdf-manipulation, pdf-merger, pdf-ocr, pdf-tools, pdf-web-apps, pdfmerger, self-hosted |
| 许可证 | Other |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,255 |
| 语言 | JavaScript |
| Forks | 7,782 |
| Issues | 732 |
| Topics | docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring, webapp, websocket |
| 许可证 | MIT License |


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,163 |
| 语言 | Go |
| Forks | 1,918 |
| Issues | 325 |
| Topics | ci, devops, github-actions, golang |
| 许可证 | MIT License |


### traefik/traefik

**描述**: The Cloud Native Application Proxy

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,997 |
| 语言 | Go |
| Forks | 5,967 |
| Issues | 784 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### usememos/memos

**描述**: Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,376 |
| 语言 | Go |
| Forks | 4,328 |
| Issues | 22 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,862 |
| 语言 | Go |
| Forks | 7,472 |
| Issues | 81 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


## 📈 监控/观测 (2 个项目) { #监控-观测 }


### 🌟 高优先级


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,255 |
| 语言 | JavaScript |
| Forks | 7,782 |
| Issues | 732 |
| Topics | docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring, webapp, websocket |
| 许可证 | MIT License |


### prometheus/prometheus

**描述**: The Prometheus monitoring system and time series database.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,913 |
| 语言 | Go |
| Forks | 10,374 |
| Issues | 762 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (12 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
| 语言 | Go |
| Forks | 4,057 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持文本生成、图像、音频、视频等多种模型类型，且可在无 GPU 环境下运行，API 兼容 OpenAI 大幅降低了从云端 AI 到本地部署的迁移成本，特别适合隐私敏感和成本敏感的场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、语音合成（TTS）和目标检测等多种模型类型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低硬件门槛和部署成本
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移至本地部署
- Go 语言高性能架构：采用 Go 开发，具备优秀的并发处理能力和跨平台部署能力
- 去中心化架构：支持 libp2p 分布式网络，可构建去中心化的 AI 服务网络

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等行业需要本地处理敏感数据，避免数据上传到第三方云服务
- 成本优化场景：中小企业或个人开发者希望降低 AI API 调用成本，实现自有模型的本地化部署
- 私有化 AI 服务：企业需要部署私有的 AI 能力，支持定制化模型和内网隔离部署



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 432,139 |
| 语言 | Python |
| Forks | 47,225 |
| Issues | 1,326 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,910 |
| 语言 | Python |
| Forks | 9,206 |
| Issues | 185 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


### django/django

**描述**: The Web framework for perfectionists with deadlines.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,410 |
| 语言 | Python |
| Forks | 33,838 |
| Issues | 431 |
| Topics | apps, django, framework, models, orm, python, templates, views, web |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### angular/angular

**描述**: Deliver web apps with confidence 🚀

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,046 |
| 语言 | TypeScript |
| Forks | 27,188 |
| Issues | 1,153 |
| Topics | angular, javascript, pwa, typescript, web, web-framework, web-performance |
| 许可证 | MIT License |


### hoppscotch/hoppscotch

**描述**: Open-Source API Development Ecosystem • https://hoppscotch.io • Offline, On-Prem & Cloud • Web, Desktop & CLI • Open-Source Alternative to Postman, Insomnia

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,109 |
| 语言 | TypeScript |
| Forks | 5,855 |
| Issues | 701 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,990 |
| 语言 | JavaScript |
| Forks | 23,245 |
| Issues | 209 |
| Topics | express, javascript, nodejs, server |
| 许可证 | MIT License |


### gatsbyjs/gatsby

**描述**: React-based framework with performance, scalability, and security built in.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,203 |
| Issues | 369 |
| Topics | blog, compiler, gatsby, graphql, react, static-site-generator, web-app |
| 许可证 | MIT License |


### prettier/prettier

**描述**: Prettier is an opinionated code formatter.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,845 |
| 语言 | JavaScript |
| Forks | 4,713 |
| Issues | 1,474 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,110 |
| 语言 | Go |
| Forks | 4,714 |
| Issues | 244 |
| Topics | acme, automatic-https, caddy, caddyfile, go, golang, http, http-server, http3, https, privacy, reverse-proxy, security, tls, web-server |
| 许可证 | Apache License 2.0 |


### pocketbase/pocketbase

**描述**: Open Source realtime backend in 1 file

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,140 |
| 语言 | Go |
| Forks | 3,347 |
| Issues | 17 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,417 |
| 语言 | Go |
| Forks | 8,598 |
| Issues | 683 |
| Topics | framework, gin, go, middleware, performance, router, server |
| 许可证 | MIT License |


## 📊 数据/基础设施 (4 个项目) { #数据-基础设施 }


### 🌟 高优先级


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,896 |
| 语言 | TypeScript |
| Forks | 12,307 |
| Issues | 992 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,547 |
| 语言 | JavaScript |
| Forks | 6,436 |
| Issues | 345 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,116 |
| 语言 | Go |
| Forks | 3,988 |
| Issues | 1,072 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,668 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 241 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,610 |
| 语言 | HTML |
| Forks | 21,079 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是全球最大的开源 ChatGPT 提示词库之一，拥有超过 16 万 Stars 的社区认可，支持自托管部署保护隐私，是 AI 时代必备的提示词资源集合和实践工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代全栈架构，提供良好的开发体验和类型安全
- 支持多模型平台集成（ChatGPT、Claude、Gemini、GPT-4），适配多种 LLM 接口
- 提供完整的自托管部署方案，企业可完全私有化部署保障数据安全
- 社区驱动的提示词贡献机制，持续更新高质量提示词库
- 采用响应式设计，支持 Web 端和移动端访问

**适用场景**:
- 个人开发者：寻找高质量提示词灵感，提升 AI 应用开发效率
- 企业自托管：私有化部署企业级提示词管理系统，保护内部知识资产
- AI学习者：学习提示词工程最佳实践，掌握与 LLM 高效交互技巧



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,430 |
| 语言 | Python |
| Forks | 2,975 |
| Issues | 182 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过"穴居人语言"风格实现高达 65% 的 token 消耗削减，在 LLM 应用成本日益重要的背景下，这种简单而有效的 prompt 工程技巧对于追求效率和成本优化的开发者来说具有极高的实用价值。

**技术亮点**:
- Token 优化算法：通过语言风格转换实现 token 消耗大幅降低，核心基于简化和压缩 prompt 的工程实践
- Claude Code 集成：作为官方支持的 Claude Code skill 实现，可无缝集成到开发工作流中
- Python 实现：采用 Python 编写，便于理解和二次开发，生态兼容性强
- Prompt 工程创新：开创性地将 meme 文化与 LLM 优化结合，展示了提示词设计的无限可能
- 性能提升：在保持输出质量的同时显著减少 token 数量，降低延迟并提升响应速度

**适用场景**:
- 成本敏感型应用：企业和个人开发者在大量使用 Claude API 时，用于降低订阅费用和 API 调用成本
- 追求高效率的开发团队：需要快速迭代的项目，通过减少 token 传输量来缩短响应等待时间
- Claude Code 重度用户：日常使用 Claude 进行代码编写、调试和重构的开发者，优化个人工作流效率



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,648 |
| 语言 | Python |
| Forks | 5,154 |
| Issues | 102 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,209 |
| 语言 | TypeScript |
| Forks | 9,553 |
| Issues | 115 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,853 |
| 语言 | TypeScript |
| Forks | 10,038 |
| Issues | 2,269 |
| Topics | angular, components, design-systems, documentation, html, javascript, react, react-native, stories, storybook, styleguide, svelte, testing, typescript, ui, vite, vue, web-components, webpack, workshop |
| 许可证 | MIT License |


### mermaid-js/mermaid

**描述**: Generation of diagrams like flowcharts or sequence diagrams from text in a similar manner as markdown

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,814 |
| 语言 | TypeScript |
| Forks | 8,933 |
| Issues | 1,662 |
| Topics | diagrams, diagrams-as-code, documentation, flowchart, javascript, mindmap, typescript, uml-diagrams |
| 许可证 | MIT License |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,897 |
| 语言 | Go |
| Forks | 13,190 |
| Issues | 183 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


### ⭐ 中优先级


### Chalarangelo/30-seconds-of-code

**描述**: Coding articles to level up your development skills

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 127,697 |
| 语言 | JavaScript |
| Forks | 12,481 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (68 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,743 |
| 语言 | Unknown |
| Forks | 34,144 |
| Issues | 136 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,714 |
| 语言 | Python |
| Forks | 9,061 |
| Issues | 3,010 |
| Topics | llm-app |
| 许可证 | Apache License 2.0 |


### mattpocock/skills

**描述**: Skills for Real Engineers. Straight from my .claude directory.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,635 |
| 语言 | Shell |
| Forks | 5,235 |
| Issues | 15 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,661 |
| 语言 | Python |
| Forks | 8,024 |
| Issues | 527 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,651 |
| 语言 | Python |
| Forks | 13,466 |
| Issues | 117 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
| 许可证 | GNU Affero General Public License v3.0 |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 387,740 |
| 语言 | Python |
| Forks | 66,230 |
| Issues | 77 |
| Topics | books, education, hacktoberfest, list, resource |
| 许可证 | Creative Commons Attribution 4.0 International |


### iptv-org/iptv

**描述**: Collection of publicly available IPTV channels from all over the world

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,950 |
| 语言 | TypeScript |
| Forks | 6,089 |
| Issues | 26 |
| Topics | iptv, m3u, playlist, streams, tv |
| 许可证 | The Unlicense |


### clash-verge-rev/clash-verge-rev

**描述**: A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,825 |
| 语言 | TypeScript |
| Forks | 8,446 |
| Issues | 304 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,712 |
| 语言 | TypeScript |
| Forks | 13,242 |
| Issues | 514 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,180 |
| 语言 | JavaScript |
| Forks | 5,128 |
| Issues | 36 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,334 |
| 语言 | Go |
| Forks | 10,338 |
| Issues | 1,895 |
| Topics | cloud, cloud-management, graph, infrastructure-as-code, terraform |
| 许可证 | Other |


### ggml-org/llama.cpp

**描述**: LLM inference in C/C++

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,423 |
| 语言 | C++ |
| Forks | 17,804 |
| Issues | 1,584 |
| Topics | ggml |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,349 |
| 语言 | Python |
| Forks | 1,636 |
| Issues | 36 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### abhigyanpatwari/GitNexus

**描述**: GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,887 |
| 语言 | TypeScript |
| Forks | 4,082 |
| Issues | 363 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 296,073 |
| 语言 | Python |
| Forks | 27,822 |
| Issues | 18 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 220,781 |
| 语言 | Python |
| Forks | 50,539 |
| Issues | 950 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,916 |
| 语言 | Python |
| Forks | 37,413 |
| Issues | 3,825 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### tensorflow/models

**描述**: Models and examples built with TensorFlow

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,667 |
| 语言 | Python |
| Forks | 45,103 |
| Issues | 1,286 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,202 |
| 语言 | TypeScript |
| Forks | 44,466 |
| Issues | 176 |
| Topics | careers, certification, community, curriculum, d3, education, freecodecamp, javascript, learn-to-code, math, nodejs, nonprofits, programming, react, teachers |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### nilbuild/developer-roadmap

**描述**: Interactive roadmaps, guides and other educational content to help developers grow in their careers.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 354,228 |
| 语言 | TypeScript |
| Forks | 44,026 |
| Issues | 17 |
| Topics | angular-roadmap, backend-roadmap, blockchain-roadmap, computer-science, dba-roadmap, developer-roadmap, devops-roadmap, frontend-roadmap, go-roadmap, java-roadmap, javascript-roadmap, nodejs-roadmap, python-roadmap, qa-roadmap, react-roadmap, roadmap, software-architect-roadmap, vue-roadmap |
| 许可证 | Other |


### excalidraw/excalidraw

**描述**: Virtual whiteboard for sketching hand-drawn like diagrams

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 122,550 |
| 语言 | TypeScript |
| Forks | 13,526 |
| Issues | 3,027 |
| Topics | canvas, collaboration, diagrams, drawing, hacktoberfest, productivity, whiteboard |
| 许可证 | MIT License |


### shadcn-ui/ui

**描述**: A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 113,605 |
| 语言 | TypeScript |
| Forks | 8,732 |
| Issues | 1,847 |
| Topics | base-ui, components, laravel, nextjs, radix-ui, react, shadcn, tailwindcss, tanstack, ui, vite |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,755 |
| 语言 | TypeScript |
| Forks | 13,383 |
| Issues | 5,033 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,751 |
| 语言 | TypeScript |
| Forks | 5,538 |
| Issues | 702 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,923 |
| 语言 | TypeScript |
| Forks | 54,596 |
| Issues | 1,366 |
| Topics | ant-design, antd, design-systems, react, typescript, ui-kit, ui-library |
| 许可证 | MIT License |


### tailwindlabs/tailwindcss

**描述**: A utility-first CSS framework for rapid UI development.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,844 |
| 语言 | TypeScript |
| Forks | 5,219 |
| Issues | 92 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,400 |
| 语言 | TypeScript |
| Forks | 8,128 |
| Issues | 752 |
| Topics | build-tool, dev-server, frontend, hmr, vite |
| 许可证 | MIT License |


### facebook/react

**描述**: The library for web and native user interfaces.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 244,819 |
| 语言 | JavaScript |
| Forks | 50,995 |
| Issues | 1,276 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,039 |
| 语言 | JavaScript |
| Forks | 35,479 |
| Issues | 2,652 |
| Topics | javascript, js, linux, macos, mit, node, nodejs, runtime, windows |
| 许可证 | Other |


### mrdoob/three.js

**描述**: JavaScript 3D Library.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,322 |
| 语言 | JavaScript |
| Forks | 36,358 |
| Issues | 505 |
| Topics | 3d, augmented-reality, canvas, html5, javascript, svg, virtual-reality, webaudio, webgl, webgl2, webgpu, webxr |
| 许可证 | MIT License |


### axios/axios

**描述**: Promise based HTTP client for the browser and node.js

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,024 |
| 语言 | JavaScript |
| Forks | 11,663 |
| Issues | 153 |
| Topics | hacktoberfest, http-client, javascript, nodejs, promise |
| 许可证 | MIT License |


### Anduin2017/HowToCook

**描述**: 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only).

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,767 |
| 语言 | JavaScript |
| Forks | 10,932 |
| Issues | 473 |
| Topics | chinese, cookbook, cooking, dishes, recipes |
| 许可证 | The Unlicense |


### mui/material-ui

**描述**: Material UI: Comprehensive React component library that implements Google's Material Design. Free forever.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,283 |
| 语言 | JavaScript |
| Forks | 32,652 |
| Issues | 1,535 |
| Topics | design-system, material-design, material-ui, react, react-components |
| 许可证 | MIT License |


### sveltejs/svelte

**描述**: web development for the rest of us

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,474 |
| 语言 | JavaScript |
| Forks | 4,902 |
| Issues | 998 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,816 |
| 语言 | JavaScript |
| Forks | 4,555 |
| Issues | 101 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,758 |
| 语言 | JavaScript |
| Forks | 9,356 |
| Issues | 199 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,417 |
| 语言 | JavaScript |
| Forks | 4,093 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,885 |
| 语言 | JavaScript |
| Forks | 5,658 |
| Issues | 65 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,840 |
| 语言 | JavaScript |
| Forks | 20,455 |
| Issues | 92 |
| Topics | jquery |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,253 |
| 语言 | JavaScript |
| Forks | 10,607 |
| Issues | 444 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,740 |
| 语言 | JavaScript |
| Forks | 11,527 |
| Issues | 241 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,741 |
| 语言 | Go |
| Forks | 18,962 |
| Issues | 10,099 |
| Topics | go, golang, language, programming-language |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 106,244 |
| 语言 | Go |
| Forks | 15,030 |
| Issues | 40 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### gohugoio/hugo

**描述**: The world’s fastest framework for building websites.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,914 |
| 语言 | Go |
| Forks | 8,252 |
| Issues | 241 |
| Topics | blog-engine, cms, content-management-system, documentation-tool, go, hugo, static-site-generator |
| 许可证 | Apache License 2.0 |


### syncthing/syncthing

**描述**: Open Source Continuous File Synchronization

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,575 |
| 语言 | Go |
| Forks | 5,150 |
| Issues | 387 |
| Topics | go, p2p, peer-to-peer, synchronization |
| 许可证 | Mozilla Public License 2.0 |


### base/node

**描述**: Everything required to run your own Base node

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,584 |
| 语言 | Go |
| Forks | 3,227 |
| Issues | 13 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,014 |
| 语言 | Go |
| Forks | 5,075 |
| Issues | 1,170 |
| Topics | azure-blob, azure-blob-storage, azure-files, backblaze-b2, cloud-storage, dropbox, encryption, ftp, fuse-filesystem, go, golang, google-cloud-storage, google-drive, onedrive, openstack-swift, rclone, s3, sftp, sync, webdav |
| 许可证 | MIT License |


### ethereum/go-ethereum

**描述**: Go implementation of the Ethereum protocol

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,018 |
| 语言 | Go |
| Forks | 21,894 |
| Issues | 406 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 93,497 |
| 语言 | Shell |
| Forks | 15,385 |
| Issues | 120 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,908 |
| 语言 | Python |
| Forks | 11,814 |
| Issues | 353 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 113,581 |
| 语言 | Unknown |
| Forks | 11,346 |
| Issues | 84 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 98,946 |
| 语言 | Python |
| Forks | 12,144 |
| Issues | 122 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,585 |
| 语言 | Python |
| Forks | 7,261 |
| Issues | 488 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,488 |
| 语言 | Python |
| Forks | 16,922 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,341 |
| 语言 | TypeScript |
| Forks | 16,556 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,088 |
| 语言 | TypeScript |
| Forks | 10,603 |
| Issues | 413 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,377 |
| 语言 | TypeScript |
| Forks | 7,609 |
| Issues | 36 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,112 |
| 语言 | JavaScript |
| Forks | 26,693 |
| Issues | 159 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 95,713 |
| 语言 | JavaScript |
| Forks | 15,458 |
| Issues | 52 |
| Topics | css, curriculum, education, html, javascript, learning, microsoft-for-beginners, tutorials |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,128 |
| 语言 | JavaScript |
| Forks | 16,796 |
| Issues | 897 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,395 |
| 语言 | JavaScript |
| Forks | 11,955 |
| Issues | 560 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,367 |
| 语言 | JavaScript |
| Forks | 9,183 |
| Issues | 3 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,221 |
| 语言 | JavaScript |
| Forks | 7,154 |
| Issues | 141 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,438 |
| 语言 | JavaScript |
| Forks | 12,306 |
| Issues | 28 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,909 |
| 语言 | Go |
| Forks | 1,609 |
| Issues | 274 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,427 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 567 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,844 |
| 语言 | Go |
| Forks | 8,857 |
| Issues | 17 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,220 |
| 语言 | Go |
| Forks | 3,814 |
| Issues | 82 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
