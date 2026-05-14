# 项目发现报告 (2026-05-14)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
| 去重移除 | 35 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 63 |

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


## 🤖 AI Agents (28 个项目) { #ai-agents }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,177 |
| 语言 | Python |
| Forks | 23,772 |
| Issues | 11,297 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI研究组织 NousResearch 开发的智能代理框架，拥有超过15万星标，支持 Claude、ChatGPT、Codex 等多种主流大语言模型，具备高度可扩展的 Agent 架构，非常适合构建企业级 AI 应用和个人 AI 助手。

**技术亮点**:
- 多模型集成支持：同时支持 Anthropic Claude、OpenAI ChatGPT、Codex 等多种大语言模型 API，实现模型无关的灵活切换
- 成熟的 Agent 架构：基于成熟的 AI Agent 设计模式，支持任务规划、工具调用、长期记忆等核心能力
- NousResearch 背书：源自知名的开源 AI 研究组织，代码质量和社区支持有保障
- 丰富的集成生态：涵盖 clawdbot、moltbot 等多个配套项目，形成完整的 AI Agent 工具链
- MIT 开源许可：完全开源且采用宽松许可证，便于商业化和二次开发

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、办公自动化助手、业务流程智能化等企业应用
- 个人开发者 AI 助手：开发个人效率工具、智能编码助手、知识管理系统等个人项目
- AI Agent 研究与实验：作为基础框架进行 AI Agent 相关的研究、实验和原型开发



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,079 |
| 语言 | Python |
| Forks | 19,538 |
| Issues | 262 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最流行的开源 LLM Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供类似 ChatGPT 的友好体验，特别适合快速搭建私有化 AI 助手，兼顾易用性与灵活性。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 及兼容 OpenAI API 协议的服务商，实现统一的 AI 交互接口
- RAG 增强检索：内置检索增强生成功能，支持文档上传和知识库问答，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展更多 AI 工具和插件生态
- 现代化 Web 界面：提供直观的用户界面，支持会话管理、模型切换、图片上传等功能
- 自托管部署：支持完全私有化部署，数据留在本地，满足企业安全和合规要求

**适用场景**:
- 企业私有化 AI 助手：在内网部署 AI 对话系统，满足数据安全和隐私合规要求
- 开发者本地 LLM 开发：本地运行开源模型，进行测试、调试和 Prompt 工程实验
- 知识库智能问答：结合 RAG 功能构建企业知识库、文档助手、产品手册问答机器人



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,508 |
| 语言 | Python |
| Forks | 9,190 |
| Issues | 3,024 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的顶级开源 RAG 项目之一，它创新性地将 RAG 与 Agent 能力深度融合，为 LLM 应用提供智能化的上下文检索层。凭借 8 万+ Stars 的社区认可和 Apache 2.0 许可证，是构建企业级知识问答和智能文档处理系统的理想选择。

**技术亮点**:
- RAG + Agent 融合架构：突破传统 RAG 的被动检索模式，实现智能化的主动检索与推理
- 多场景 AI Agent 支持：内置 agentic-ai、agentic-retrieval 等能力，支持复杂任务的自主规划与执行
- 专业的上下文管理：提供 context-engine 和 context-management 模块，优化长文本处理和上下文利用效率
- 完整的 RAG Pipeline：端到端的检索、增强、生成流程，开箱即用
- 广泛的大模型兼容：支持对接多种 LLM 提供商，便于企业根据需求灵活选择

**适用场景**:
- 企业级智能知识库：构建支持复杂文档理解、多轮对话的企业知识问答系统
- 智能客服与文档助手：实现基于私有知识库的 AI 客服，可处理产品文档、技术手册等垂直领域问答
- AI 应用开发框架：个人开发者可用于快速搭建 LLM 应用，结合 Agent 能力开发智能助手、工作流自动化等应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 182,155 |
| 语言 | JavaScript |
| Forks | 28,060 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，通过 Skills、Memory、Security 等机制显著提升 AI Agent 的开发效率和安全性。

**技术亮点**:
- 跨平台 AI Agent 支持：统一集成 Claude Code、Codex、Opencode、Cursor 等多个主流 AI 编码工具框架
- 性能优化系统：提供 agent harness 机制，优化 AI 代理的执行效率和响应速度
- Memory 记忆系统：实现持久化上下文管理，让 AI Agent 保持长期记忆和状态
- Security 安全机制：内置安全防护层，确保 AI 代理操作的可靠性和数据安全
- Research-First 开发理念：采用研究优先的开发方法论，提升 AI 决策质量

**适用场景**:
- 个人开发者使用 AI 编码助手：提升编程效率，获得统一的 AI Agent 管理体验
- 企业级 AI 开发团队：统一管理多个 AI 代理，规范开发流程，保障代码安全
- AI 研究与实验：为 AI Agent 性能调优和功能扩展提供实验平台



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,262 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案，通过 OpenAI 兼容 API 让开发者零成本迁移现有应用，同时支持 llama、mamba、stable-diffusion 等多种模型架构，可在 CPU 上运行LLM和多模态任务，非常适合隐私敏感或需要降本的企业场景。

**技术亮点**:
- Go 语言实现：高性能、高并发、低内存占用，适合生产环境部署
- 多模态支持：覆盖文本生成、图像生成、语音合成(TTS)、音乐生成、目标检测等全场景
- 无需 GPU：支持纯 CPU 推理，大幅降低硬件门槛
- OpenAI API 兼容：可直接替换 OpenAI 服务，现有应用无缝迁移
- 模型多样性：支持 llama、mamba、stable-diffusion、musicgen 等主流模型架构

**适用场景**:
- 企业私有化部署：对数据隐私要求严格的金融、医疗、法务等行业，本地运行避免数据外传
- 个人开发者/独立开发者：低成本构建 AI 应用原型，在个人电脑上开发和测试
- 边缘计算/物联网：资源受限环境下的 AI 推理任务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,078 |
| 语言 | TypeScript |
| Forks | 15,172 |
| Issues | 789 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个面向未来的多智能体协作平台，拥有 77k+ Stars 的高人气，采用 TypeScript 全栈开发，支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，并创新性地引入 MCP 协议实现多 Agent 团队协作设计，为个人开发者和企业提供了开箱即用的 AI Agent 工作空间。

**技术亮点**:
- 多模型统一接入层：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等多家人工智能厂商的模型，提供标准化的 API 抽象层，降低模型切换成本
- MCP 协议支持：遵循 Model Context Protocol 标准，实现 Agent 之间的标准化通信与上下文共享，支持复杂的多智能体协作场景
- 知识库增强系统：内置 RAG（检索增强生成）能力，支持文档上传与语义检索，为 AI Agent 提供持久化记忆与领域知识注入
- TypeScript 全栈架构：从前端界面到后端服务全面采用 TypeScript 开发，保证类型安全与开发体验的一致性
- Agent 团队编排引擎：提供可视化的 Agent 协作流程设计器，支持定义 Agent 角色、职责分工与协作规则，实现复杂任务的多 Agent 分工处理

**适用场景**:
- 企业智能办公场景：构建客服机器人、销售助手、内容审核系统等企业级 AI 应用，通过多 Agent 协作处理复杂业务流程
- 个人开发者 AI 原生应用开发：基于 LobeHub 快速搭建 AI 应用原型，学习 Agent 协作与 MCP 协议的最佳实践
- 知识管理与智能问答系统：利用内置知识库功能构建企业知识库、AI 助手、教育答疑机器人等需要精准上下文理解的应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,740 |
| 语言 | TypeScript |
| Forks | 6,503 |
| Issues | 82 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 自动压缩和智能检索技术，为各种 AI Coding Agent 提供跨会话的持久化记忆能力，解决了长项目周期中 Agent「失忆」的痛点，让每次新会话都能快速获取历史上下文，大幅提升开发效率。

**技术亮点**:
- 采用 AI 驱动的智能压缩算法，自动精简历史上下文，有效节省 Token 消耗
- 结合 SQLite 本地存储与 ChromaDB 向量数据库的混合架构，平衡了轻量级持久化与高效语义检索
- 支持 RAG 检索增强生成技术，通过 Embeddings 实现精准的上下文召回
- 基于 TypeScript 开发，与主流 AI Agent（Claude Code、Copilot、Codex 等）无缝集成
- 提供语义化的长期记忆管理，让 Agent 能够理解并利用历史会话中的隐含信息

**适用场景**:
- 长期软件项目开发：维护大型代码库时，Agent 能记住之前的架构决策、设计模式和未解决的问题，避免重复沟通
- 多轮问题解决场景：复杂 bug 排查或功能迭代时，Agent 可快速回溯之前的调试思路和尝试方案
- 企业级 AI 辅助开发：团队成员交接或跨session工作时，新成员能快速获取项目的历史上下文和决策脉络



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,259 |
| 语言 | Python |
| Forks | 8,703 |
| Issues | 1,012 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 顶会验证的高效微调框架，支持 100+ 大语言模型和多模态模型，提供了统一的 LoRA/QLoRA/RLHF 等微调方案，让研究者和企业能够以最低的计算成本快速定制化自己的专属模型。

**技术亮点**:
- 支持 100+ LLMs（Llama/Gemma/Qwen/DeepSeek 等）和 VLMs，支持 MoE 混合专家架构
- 集成多种微调方法：LoRA、QLoRA、P-tuning、SFT、DPO、ORPO、GRPO 等 RLHF 算法
- 支持 8-bit/4-bit 量化（GPTQ/AWQ/GGUF），大幅降低显存占用
- 提供 Web UI 和 CLI 工具，支持分布式多卡训练和梯度累积
- ACL 2024 顶会论文背书，代码质量经过学术验证

**适用场景**:
- 企业场景：利用量化微调快速部署私有化定制大模型，降低 GPU 成本 60% 以上
- 学术研究：对比实验不同微调方法（LoRA vs DPO vs GRPO），快速验证新算法
- 个人开发者：使用 Web UI 无需代码即可微调自己的小模型，应用于本地知识库或 AI 助手



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,433 |
| 语言 | Python |
| Forks | 14,686 |
| Issues | 342 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,471 |
| 语言 | TypeScript |
| Forks | 9,893 |
| Issues | 124 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,014 |
| 语言 | HTML |
| Forks | 5,298 |
| Issues | 14 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,424 |
| 语言 | Python |
| Forks | 5,955 |
| Issues | 111 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,249 |
| 语言 | Java |
| Forks | 15,991 |
| Issues | 22 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,167 |
| 语言 | Python |
| Forks | 6,204 |
| Issues | 80 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,957 |
| 语言 | TypeScript |
| Forks | 5,708 |
| Issues | 547 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 119,835 |
| 语言 | TypeScript |
| Forks | 7,371 |
| Issues | 323 |
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
| Stars | 60,041 |
| 语言 | JavaScript |
| Forks | 6,491 |
| Issues | 361 |
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
| Stars | 73,535 |
| 语言 | Python |
| Forks | 9,290 |
| Issues | 422 |
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
| Stars | 57,774 |
| 语言 | TypeScript |
| Forks | 4,687 |
| Issues | 639 |
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
| Stars | 110,293 |
| 语言 | Python |
| Forks | 16,331 |
| Issues | 12 |
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
| Stars | 93,927 |
| 语言 | Python |
| Forks | 10,612 |
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
| Stars | 52,817 |
| 语言 | TypeScript |
| Forks | 24,333 |
| Issues | 843 |
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
| Stars | 187,849 |
| 语言 | TypeScript |
| Forks | 57,625 |
| Issues | 1,465 |
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
| Stars | 155,677 |
| 语言 | Java |
| Forks | 46,137 |
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
| Stars | 148,090 |
| 语言 | Python |
| Forks | 8,977 |
| Issues | 924 |
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
| Stars | 61,458 |
| 语言 | Jupyter Notebook |
| Forks | 20,818 |
| Issues | 8 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.io

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,771 |
| 语言 | Rust |
| Forks | 4,540 |
| Issues | 863 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,823 |
| 语言 | Python |
| Forks | 6,494 |
| Issues | 622 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


## 🔍 RAG/检索 (15 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,079 |
| 语言 | Python |
| Forks | 19,538 |
| Issues | 262 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最流行的开源 LLM Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供类似 ChatGPT 的友好体验，特别适合快速搭建私有化 AI 助手，兼顾易用性与灵活性。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 及兼容 OpenAI API 协议的服务商，实现统一的 AI 交互接口
- RAG 增强检索：内置检索增强生成功能，支持文档上传和知识库问答，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展更多 AI 工具和插件生态
- 现代化 Web 界面：提供直观的用户界面，支持会话管理、模型切换、图片上传等功能
- 自托管部署：支持完全私有化部署，数据留在本地，满足企业安全和合规要求

**适用场景**:
- 企业私有化 AI 助手：在内网部署 AI 对话系统，满足数据安全和隐私合规要求
- 开发者本地 LLM 开发：本地运行开源模型，进行测试、调试和 Prompt 工程实验
- 知识库智能问答：结合 RAG 功能构建企业知识库、文档助手、产品手册问答机器人



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,508 |
| 语言 | Python |
| Forks | 9,190 |
| Issues | 3,024 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的顶级开源 RAG 项目之一，它创新性地将 RAG 与 Agent 能力深度融合，为 LLM 应用提供智能化的上下文检索层。凭借 8 万+ Stars 的社区认可和 Apache 2.0 许可证，是构建企业级知识问答和智能文档处理系统的理想选择。

**技术亮点**:
- RAG + Agent 融合架构：突破传统 RAG 的被动检索模式，实现智能化的主动检索与推理
- 多场景 AI Agent 支持：内置 agentic-ai、agentic-retrieval 等能力，支持复杂任务的自主规划与执行
- 专业的上下文管理：提供 context-engine 和 context-management 模块，优化长文本处理和上下文利用效率
- 完整的 RAG Pipeline：端到端的检索、增强、生成流程，开箱即用
- 广泛的大模型兼容：支持对接多种 LLM 提供商，便于企业根据需求灵活选择

**适用场景**:
- 企业级智能知识库：构建支持复杂文档理解、多轮对话的企业知识问答系统
- 智能客服与文档助手：实现基于私有知识库的 AI 客服，可处理产品文档、技术手册等垂直领域问答
- AI 应用开发框架：个人开发者可用于快速搭建 LLM 应用，结合 Agent 能力开发智能助手、工作流自动化等应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,078 |
| 语言 | TypeScript |
| Forks | 15,172 |
| Issues | 789 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个面向未来的多智能体协作平台，拥有 77k+ Stars 的高人气，采用 TypeScript 全栈开发，支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，并创新性地引入 MCP 协议实现多 Agent 团队协作设计，为个人开发者和企业提供了开箱即用的 AI Agent 工作空间。

**技术亮点**:
- 多模型统一接入层：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等多家人工智能厂商的模型，提供标准化的 API 抽象层，降低模型切换成本
- MCP 协议支持：遵循 Model Context Protocol 标准，实现 Agent 之间的标准化通信与上下文共享，支持复杂的多智能体协作场景
- 知识库增强系统：内置 RAG（检索增强生成）能力，支持文档上传与语义检索，为 AI Agent 提供持久化记忆与领域知识注入
- TypeScript 全栈架构：从前端界面到后端服务全面采用 TypeScript 开发，保证类型安全与开发体验的一致性
- Agent 团队编排引擎：提供可视化的 Agent 协作流程设计器，支持定义 Agent 角色、职责分工与协作规则，实现复杂任务的多 Agent 分工处理

**适用场景**:
- 企业智能办公场景：构建客服机器人、销售助手、内容审核系统等企业级 AI 应用，通过多 Agent 协作处理复杂业务流程
- 个人开发者 AI 原生应用开发：基于 LobeHub 快速搭建 AI 应用原型，学习 Agent 协作与 MCP 协议的最佳实践
- 知识管理与智能问答系统：利用内置知识库功能构建企业知识库、AI 助手、教育答疑机器人等需要精准上下文理解的应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,740 |
| 语言 | TypeScript |
| Forks | 6,503 |
| Issues | 82 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 自动压缩和智能检索技术，为各种 AI Coding Agent 提供跨会话的持久化记忆能力，解决了长项目周期中 Agent「失忆」的痛点，让每次新会话都能快速获取历史上下文，大幅提升开发效率。

**技术亮点**:
- 采用 AI 驱动的智能压缩算法，自动精简历史上下文，有效节省 Token 消耗
- 结合 SQLite 本地存储与 ChromaDB 向量数据库的混合架构，平衡了轻量级持久化与高效语义检索
- 支持 RAG 检索增强生成技术，通过 Embeddings 实现精准的上下文召回
- 基于 TypeScript 开发，与主流 AI Agent（Claude Code、Copilot、Codex 等）无缝集成
- 提供语义化的长期记忆管理，让 Agent 能够理解并利用历史会话中的隐含信息

**适用场景**:
- 长期软件项目开发：维护大型代码库时，Agent 能记住之前的架构决策、设计模式和未解决的问题，避免重复沟通
- 多轮问题解决场景：复杂 bug 排查或功能迭代时，Agent 可快速回溯之前的调试思路和尝试方案
- 企业级 AI 辅助开发：团队成员交接或跨session工作时，新成员能快速获取项目的历史上下文和决策脉络



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,424 |
| 语言 | Python |
| Forks | 5,955 |
| Issues | 111 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,249 |
| 语言 | Java |
| Forks | 15,991 |
| Issues | 22 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,167 |
| 语言 | Python |
| Forks | 6,204 |
| Issues | 80 |
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
| Stars | 102,336 |
| 语言 | TypeScript |
| Forks | 12,387 |
| Issues | 1,015 |
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
| Stars | 60,041 |
| 语言 | JavaScript |
| Forks | 6,491 |
| Issues | 361 |
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
| Stars | 110,293 |
| 语言 | Python |
| Forks | 16,331 |
| Issues | 12 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,836 |
| 语言 | Python |
| Forks | 10,433 |
| Issues | 203 |
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
| Stars | 52,817 |
| 语言 | TypeScript |
| Forks | 24,333 |
| Issues | 843 |
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
| Stars | 47,952 |
| 语言 | Python |
| Forks | 5,210 |
| Issues | 251 |
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
| Stars | 44,293 |
| 语言 | Go |
| Forks | 3,997 |
| Issues | 894 |
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
| Stars | 35,204 |
| 语言 | Python |
| Forks | 4,990 |
| Issues | 230 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (20 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,177 |
| 语言 | Python |
| Forks | 23,772 |
| Issues | 11,297 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI研究组织 NousResearch 开发的智能代理框架，拥有超过15万星标，支持 Claude、ChatGPT、Codex 等多种主流大语言模型，具备高度可扩展的 Agent 架构，非常适合构建企业级 AI 应用和个人 AI 助手。

**技术亮点**:
- 多模型集成支持：同时支持 Anthropic Claude、OpenAI ChatGPT、Codex 等多种大语言模型 API，实现模型无关的灵活切换
- 成熟的 Agent 架构：基于成熟的 AI Agent 设计模式，支持任务规划、工具调用、长期记忆等核心能力
- NousResearch 背书：源自知名的开源 AI 研究组织，代码质量和社区支持有保障
- 丰富的集成生态：涵盖 clawdbot、moltbot 等多个配套项目，形成完整的 AI Agent 工具链
- MIT 开源许可：完全开源且采用宽松许可证，便于商业化和二次开发

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、办公自动化助手、业务流程智能化等企业应用
- 个人开发者 AI 助手：开发个人效率工具、智能编码助手、知识管理系统等个人项目
- AI Agent 研究与实验：作为基础框架进行 AI Agent 相关的研究、实验和原型开发



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,079 |
| 语言 | Python |
| Forks | 19,538 |
| Issues | 262 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最流行的开源 LLM Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供类似 ChatGPT 的友好体验，特别适合快速搭建私有化 AI 助手，兼顾易用性与灵活性。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 及兼容 OpenAI API 协议的服务商，实现统一的 AI 交互接口
- RAG 增强检索：内置检索增强生成功能，支持文档上传和知识库问答，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展更多 AI 工具和插件生态
- 现代化 Web 界面：提供直观的用户界面，支持会话管理、模型切换、图片上传等功能
- 自托管部署：支持完全私有化部署，数据留在本地，满足企业安全和合规要求

**适用场景**:
- 企业私有化 AI 助手：在内网部署 AI 对话系统，满足数据安全和隐私合规要求
- 开发者本地 LLM 开发：本地运行开源模型，进行测试、调试和 Prompt 工程实验
- 知识库智能问答：结合 RAG 功能构建企业知识库、文档助手、产品手册问答机器人



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 182,155 |
| 语言 | JavaScript |
| Forks | 28,060 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，通过 Skills、Memory、Security 等机制显著提升 AI Agent 的开发效率和安全性。

**技术亮点**:
- 跨平台 AI Agent 支持：统一集成 Claude Code、Codex、Opencode、Cursor 等多个主流 AI 编码工具框架
- 性能优化系统：提供 agent harness 机制，优化 AI 代理的执行效率和响应速度
- Memory 记忆系统：实现持久化上下文管理，让 AI Agent 保持长期记忆和状态
- Security 安全机制：内置安全防护层，确保 AI 代理操作的可靠性和数据安全
- Research-First 开发理念：采用研究优先的开发方法论，提升 AI 决策质量

**适用场景**:
- 个人开发者使用 AI 编码助手：提升编程效率，获得统一的 AI Agent 管理体验
- 企业级 AI 开发团队：统一管理多个 AI 代理，规范开发流程，保障代码安全
- AI 研究与实验：为 AI Agent 性能调优和功能扩展提供实验平台



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,172 |
| 语言 | JavaScript |
| Forks | 3,332 |
| Issues | 198 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"原始人语言"风格的提示词优化，将 Claude Code 的 token 消耗降低 65%，在保持输出质量的同时显著节省成本和提升响应速度，非常适合频繁使用 AI 编程助手的开发者。

**技术亮点**:
- 基于 Anthropic Claude Code 的 Skill 扩展，可直接集成到开发工作流中
- 创新的提示词工程方法，通过语言简化实现 65% 的 token 节省
- 极简实现思路：用更少的词汇表达相同的语义意图
- MIT 开源许可，代码可自由使用和二次开发
- 纯 JavaScript 实现，部署和使用门槛低

**适用场景**:
- AI 编程成本优化 — 适合需要频繁调用 Claude API 的开发者或团队，显著降低 API 费用
- 快速原型开发 — 当需要快速迭代代码片段时使用，减少等待时间和 token 消耗
- 个人开发者助手 — 日常编程辅助场景，提升开发效率同时控制成本



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,078 |
| 语言 | TypeScript |
| Forks | 15,172 |
| Issues | 789 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个面向未来的多智能体协作平台，拥有 77k+ Stars 的高人气，采用 TypeScript 全栈开发，支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，并创新性地引入 MCP 协议实现多 Agent 团队协作设计，为个人开发者和企业提供了开箱即用的 AI Agent 工作空间。

**技术亮点**:
- 多模型统一接入层：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等多家人工智能厂商的模型，提供标准化的 API 抽象层，降低模型切换成本
- MCP 协议支持：遵循 Model Context Protocol 标准，实现 Agent 之间的标准化通信与上下文共享，支持复杂的多智能体协作场景
- 知识库增强系统：内置 RAG（检索增强生成）能力，支持文档上传与语义检索，为 AI Agent 提供持久化记忆与领域知识注入
- TypeScript 全栈架构：从前端界面到后端服务全面采用 TypeScript 开发，保证类型安全与开发体验的一致性
- Agent 团队编排引擎：提供可视化的 Agent 协作流程设计器，支持定义 Agent 角色、职责分工与协作规则，实现复杂任务的多 Agent 分工处理

**适用场景**:
- 企业智能办公场景：构建客服机器人、销售助手、内容审核系统等企业级 AI 应用，通过多 Agent 协作处理复杂业务流程
- 个人开发者 AI 原生应用开发：基于 LobeHub 快速搭建 AI 应用原型，学习 Agent 协作与 MCP 协议的最佳实践
- 知识管理与智能问答系统：利用内置知识库功能构建企业知识库、AI 助手、教育答疑机器人等需要精准上下文理解的应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,740 |
| 语言 | TypeScript |
| Forks | 6,503 |
| Issues | 82 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 自动压缩和智能检索技术，为各种 AI Coding Agent 提供跨会话的持久化记忆能力，解决了长项目周期中 Agent「失忆」的痛点，让每次新会话都能快速获取历史上下文，大幅提升开发效率。

**技术亮点**:
- 采用 AI 驱动的智能压缩算法，自动精简历史上下文，有效节省 Token 消耗
- 结合 SQLite 本地存储与 ChromaDB 向量数据库的混合架构，平衡了轻量级持久化与高效语义检索
- 支持 RAG 检索增强生成技术，通过 Embeddings 实现精准的上下文召回
- 基于 TypeScript 开发，与主流 AI Agent（Claude Code、Copilot、Codex 等）无缝集成
- 提供语义化的长期记忆管理，让 Agent 能够理解并利用历史会话中的隐含信息

**适用场景**:
- 长期软件项目开发：维护大型代码库时，Agent 能记住之前的架构决策、设计模式和未解决的问题，避免重复沟通
- 多轮问题解决场景：复杂 bug 排查或功能迭代时，Agent 可快速回溯之前的调试思路和尝试方案
- 企业级 AI 辅助开发：团队成员交接或跨session工作时，新成员能快速获取项目的历史上下文和决策脉络



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,235 |
| 语言 | HTML |
| Forks | 21,122 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,758 |
| 语言 | Jupyter Notebook |
| Forks | 14,506 |
| Issues | 6 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,471 |
| 语言 | TypeScript |
| Forks | 9,893 |
| Issues | 124 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,014 |
| 语言 | HTML |
| Forks | 5,298 |
| Issues | 14 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,041 |
| 语言 | JavaScript |
| Forks | 6,491 |
| Issues | 361 |
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
| Stars | 73,535 |
| 语言 | Python |
| Forks | 9,290 |
| Issues | 422 |
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
| Stars | 57,774 |
| 语言 | TypeScript |
| Forks | 4,687 |
| Issues | 639 |
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
| Stars | 52,817 |
| 语言 | TypeScript |
| Forks | 24,333 |
| Issues | 843 |
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
| Stars | 80,012 |
| 语言 | Python |
| Forks | 16,810 |
| Issues | 4,959 |
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
| Stars | 148,090 |
| 语言 | Python |
| Forks | 8,977 |
| Issues | 924 |
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
| Stars | 59,823 |
| 语言 | Python |
| Forks | 6,494 |
| Issues | 622 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,400 |
| 语言 | Go |
| Forks | 16,116 |
| Issues | 3,250 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,704 |
| 语言 | Rust |
| Forks | 9,818 |
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
| Stars | 123,171 |
| 语言 | Python |
| Forks | 8,325 |
| Issues | 642 |
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
| Stars | 71,259 |
| 语言 | Python |
| Forks | 8,703 |
| Issues | 1,012 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 顶会验证的高效微调框架，支持 100+ 大语言模型和多模态模型，提供了统一的 LoRA/QLoRA/RLHF 等微调方案，让研究者和企业能够以最低的计算成本快速定制化自己的专属模型。

**技术亮点**:
- 支持 100+ LLMs（Llama/Gemma/Qwen/DeepSeek 等）和 VLMs，支持 MoE 混合专家架构
- 集成多种微调方法：LoRA、QLoRA、P-tuning、SFT、DPO、ORPO、GRPO 等 RLHF 算法
- 支持 8-bit/4-bit 量化（GPTQ/AWQ/GGUF），大幅降低显存占用
- 提供 Web UI 和 CLI 工具，支持分布式多卡训练和梯度累积
- ACL 2024 顶会论文背书，代码质量经过学术验证

**适用场景**:
- 企业场景：利用量化微调快速部署私有化定制大模型，降低 GPU 成本 60% 以上
- 学术研究：对比实验不同微调方法（LoRA vs DPO vs GRPO），快速验证新算法
- 个人开发者：使用 Web UI 无需代码即可微调自己的小模型，应用于本地知识库或 AI 助手



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,577 |
| 语言 | Python |
| Forks | 6,789 |
| Issues | 79 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过67K Stars的高人气，提供了涵盖股票、加密货币、期权、固定收益等多领域的统一数据访问接口，特别适合需要快速构建量化分析系统和AI金融应用的开发者。

**技术亮点**:
- 基于 Python 的模块化架构，支持数据源插件化和扩展，方便集成自定义数据提供商
- 内置丰富的金融分析工具，包括技术指标、衍生品定价、固收分析等量化计算功能
- 深度集成 AI/ML 能力，支持大语言模型(LLM)驱动的自然语言金融查询和分析
- 提供标准化 API 和 CLI 工具，支持 Jupyter Notebook 交互式分析工作流
- 支持实时市场数据和历史回测，兼容 pandas.DataFrame 数据格式便于数据处理

**适用场景**:
- 量化交易策略开发：用于获取市场数据、计算技术指标、执行回测和因子分析
- AI 金融助手构建：集成 LLM 能力开发智能投研问答系统和自动化报告生成
- 投资组合分析与风险管理：进行多资产配置分析、风险评估和固定收益定价



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,235 |
| 语言 | HTML |
| Forks | 21,122 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,758 |
| 语言 | Jupyter Notebook |
| Forks | 14,506 |
| Issues | 6 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,618 |
| 语言 | Python |
| Forks | 33,210 |
| Issues | 2,348 |
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
| Stars | 80,012 |
| 语言 | Python |
| Forks | 16,810 |
| Issues | 4,959 |
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
| Stars | 112,925 |
| 语言 | Python |
| Forks | 13,209 |
| Issues | 4,002 |
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
| Stars | 99,909 |
| 语言 | Python |
| Forks | 27,783 |
| Issues | 18,454 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (18 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 182,155 |
| 语言 | JavaScript |
| Forks | 28,060 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，通过 Skills、Memory、Security 等机制显著提升 AI Agent 的开发效率和安全性。

**技术亮点**:
- 跨平台 AI Agent 支持：统一集成 Claude Code、Codex、Opencode、Cursor 等多个主流 AI 编码工具框架
- 性能优化系统：提供 agent harness 机制，优化 AI 代理的执行效率和响应速度
- Memory 记忆系统：实现持久化上下文管理，让 AI Agent 保持长期记忆和状态
- Security 安全机制：内置安全防护层，确保 AI 代理操作的可靠性和数据安全
- Research-First 开发理念：采用研究优先的开发方法论，提升 AI 决策质量

**适用场景**:
- 个人开发者使用 AI 编码助手：提升编程效率，获得统一的 AI Agent 管理体验
- 企业级 AI 开发团队：统一管理多个 AI 代理，规范开发流程，保障代码安全
- AI 研究与实验：为 AI Agent 性能调优和功能扩展提供实验平台



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,262 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案，通过 OpenAI 兼容 API 让开发者零成本迁移现有应用，同时支持 llama、mamba、stable-diffusion 等多种模型架构，可在 CPU 上运行LLM和多模态任务，非常适合隐私敏感或需要降本的企业场景。

**技术亮点**:
- Go 语言实现：高性能、高并发、低内存占用，适合生产环境部署
- 多模态支持：覆盖文本生成、图像生成、语音合成(TTS)、音乐生成、目标检测等全场景
- 无需 GPU：支持纯 CPU 推理，大幅降低硬件门槛
- OpenAI API 兼容：可直接替换 OpenAI 服务，现有应用无缝迁移
- 模型多样性：支持 llama、mamba、stable-diffusion、musicgen 等主流模型架构

**适用场景**:
- 企业私有化部署：对数据隐私要求严格的金融、医疗、法务等行业，本地运行避免数据外传
- 个人开发者/独立开发者：低成本构建 AI 应用原型，在个人电脑上开发和测试
- 边缘计算/物联网：资源受限环境下的 AI 推理任务



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,249 |
| 语言 | Java |
| Forks | 15,991 |
| Issues | 22 |
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
| Stars | 73,535 |
| 语言 | Python |
| Forks | 9,290 |
| Issues | 422 |
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
| Stars | 57,774 |
| 语言 | TypeScript |
| Forks | 4,687 |
| Issues | 639 |
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
| Stars | 187,849 |
| 语言 | TypeScript |
| Forks | 57,625 |
| Issues | 1,465 |
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
| Stars | 59,823 |
| 语言 | Python |
| Forks | 6,494 |
| Issues | 622 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,077 |
| 语言 | JavaScript |
| Forks | 4,199 |
| Issues | 1,314 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,015 |
| 语言 | Python |
| Forks | 47,665 |
| Issues | 1,327 |
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
| Stars | 98,205 |
| 语言 | Python |
| Forks | 9,289 |
| Issues | 200 |
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
| Stars | 83,331 |
| 语言 | Python |
| Forks | 9,721 |
| Issues | 268 |
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
| Stars | 184,926 |
| 语言 | TypeScript |
| Forks | 39,839 |
| Issues | 17,588 |
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
| Stars | 94,321 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 256 |
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
| Stars | 79,186 |
| 语言 | TypeScript |
| Forks | 5,869 |
| Issues | 715 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### coder/code-server

**描述**: VS Code in the browser

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,544 |
| 语言 | TypeScript |
| Forks | 6,669 |
| Issues | 155 |
| Topics | browser-ide, dev-tools, development-environment, ide, remote-work, vscode, vscode-remote |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,251 |
| 语言 | Go |
| Forks | 2,805 |
| Issues | 317 |
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
| Stars | 77,936 |
| 语言 | Go |
| Forks | 2,834 |
| Issues | 961 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### ⭐ 中优先级


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 162,275 |
| 语言 | Python |
| Forks | 13,586 |
| Issues | 2,498 |
| Topics | cli, downloader, python, sponsorblock, youtube-dl, youtube-downloader, yt-dlp |
| 许可证 | The Unlicense |


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
| Stars | 57,774 |
| 语言 | TypeScript |
| Forks | 4,687 |
| Issues | 639 |
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
| Stars | 187,849 |
| 语言 | TypeScript |
| Forks | 57,625 |
| Issues | 1,465 |
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
| Stars | 59,823 |
| 语言 | Python |
| Forks | 6,494 |
| Issues | 622 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,702 |
| 语言 | Go |
| Forks | 10,352 |
| Issues | 237 |
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
| Stars | 122,265 |
| 语言 | Go |
| Forks | 43,062 |
| Issues | 2,704 |
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
| Stars | 71,549 |
| 语言 | Go |
| Forks | 18,950 |
| Issues | 3,782 |
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
| Stars | 55,676 |
| 语言 | Go |
| Forks | 6,696 |
| Issues | 2,801 |
| Topics | bitbucket, cicd, devops, docker-registry-v2, git, git-gui, git-lfs, git-server, gitea, github, github-actions, gitlab, go, golang, hacktoberfest, maven-server, npm-registry, self-hosted, typescript, vue |
| 许可证 | MIT License |


### puppeteer/puppeteer

**描述**: JavaScript API for Chrome and Firefox

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,321 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 256 |
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
| Stars | 78,746 |
| 语言 | TypeScript |
| Forks | 6,899 |
| Issues | 394 |
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
| Stars | 86,746 |
| 语言 | JavaScript |
| Forks | 7,840 |
| Issues | 744 |
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
| Stars | 70,281 |
| 语言 | Go |
| Forks | 1,920 |
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
| Stars | 63,168 |
| 语言 | Go |
| Forks | 5,985 |
| Issues | 814 |
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
| Stars | 59,605 |
| 语言 | Go |
| Forks | 4,353 |
| Issues | 24 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,513 |
| 语言 | Go |
| Forks | 5,062 |
| Issues | 993 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,931 |
| 语言 | Go |
| Forks | 7,493 |
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
| Stars | 86,746 |
| 语言 | JavaScript |
| Forks | 7,840 |
| Issues | 744 |
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
| Stars | 64,037 |
| 语言 | Go |
| Forks | 10,407 |
| Issues | 768 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (11 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,262 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案，通过 OpenAI 兼容 API 让开发者零成本迁移现有应用，同时支持 llama、mamba、stable-diffusion 等多种模型架构，可在 CPU 上运行LLM和多模态任务，非常适合隐私敏感或需要降本的企业场景。

**技术亮点**:
- Go 语言实现：高性能、高并发、低内存占用，适合生产环境部署
- 多模态支持：覆盖文本生成、图像生成、语音合成(TTS)、音乐生成、目标检测等全场景
- 无需 GPU：支持纯 CPU 推理，大幅降低硬件门槛
- OpenAI API 兼容：可直接替换 OpenAI 服务，现有应用无缝迁移
- 模型多样性：支持 llama、mamba、stable-diffusion、musicgen 等主流模型架构

**适用场景**:
- 企业私有化部署：对数据隐私要求严格的金融、医疗、法务等行业，本地运行避免数据外传
- 个人开发者/独立开发者：低成本构建 AI 应用原型，在个人电脑上开发和测试
- 边缘计算/物联网：资源受限环境下的 AI 推理任务



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,015 |
| 语言 | Python |
| Forks | 47,665 |
| Issues | 1,327 |
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
| Stars | 98,205 |
| 语言 | Python |
| Forks | 9,289 |
| Issues | 200 |
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
| Stars | 87,485 |
| 语言 | Python |
| Forks | 33,869 |
| Issues | 427 |
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
| Stars | 100,109 |
| 语言 | TypeScript |
| Forks | 27,215 |
| Issues | 1,142 |
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
| Stars | 79,186 |
| 语言 | TypeScript |
| Forks | 5,869 |
| Issues | 715 |
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
| Stars | 69,022 |
| 语言 | JavaScript |
| Forks | 23,321 |
| Issues | 212 |
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
| Stars | 55,951 |
| 语言 | JavaScript |
| Forks | 10,198 |
| Issues | 373 |
| Topics | blog, compiler, gatsby, graphql, react, static-site-generator, web-app |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,508 |
| 语言 | Go |
| Forks | 8,609 |
| Issues | 685 |
| Topics | framework, gin, go, middleware, performance, router, server |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,444 |
| 语言 | Go |
| Forks | 4,732 |
| Issues | 243 |
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
| Stars | 58,324 |
| 语言 | Go |
| Forks | 3,374 |
| Issues | 17 |
| Topics | authentication, backend, golang, realtime |
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
| Stars | 102,336 |
| 语言 | TypeScript |
| Forks | 12,387 |
| Issues | 1,015 |
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
| Stars | 60,041 |
| 语言 | JavaScript |
| Forks | 6,491 |
| Issues | 361 |
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
| Stars | 44,293 |
| 语言 | Go |
| Forks | 3,997 |
| Issues | 894 |
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
| Stars | 51,702 |
| 语言 | Go |
| Forks | 10,352 |
| Issues | 237 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,172 |
| 语言 | JavaScript |
| Forks | 3,332 |
| Issues | 198 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"原始人语言"风格的提示词优化，将 Claude Code 的 token 消耗降低 65%，在保持输出质量的同时显著节省成本和提升响应速度，非常适合频繁使用 AI 编程助手的开发者。

**技术亮点**:
- 基于 Anthropic Claude Code 的 Skill 扩展，可直接集成到开发工作流中
- 创新的提示词工程方法，通过语言简化实现 65% 的 token 节省
- 极简实现思路：用更少的词汇表达相同的语义意图
- MIT 开源许可，代码可自由使用和二次开发
- 纯 JavaScript 实现，部署和使用门槛低

**适用场景**:
- AI 编程成本优化 — 适合需要频繁调用 Claude API 的开发者或团队，显著降低 API 费用
- 快速原型开发 — 当需要快速迭代代码片段时使用，减少等待时间和 token 消耗
- 个人开发者助手 — 日常编程辅助场景，提升开发效率同时控制成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,235 |
| 语言 | HTML |
| Forks | 21,122 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,471 |
| 语言 | TypeScript |
| Forks | 9,893 |
| Issues | 124 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,424 |
| 语言 | Python |
| Forks | 5,955 |
| Issues | 111 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,906 |
| 语言 | TypeScript |
| Forks | 10,058 |
| Issues | 2,195 |
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
| Stars | 88,047 |
| 语言 | TypeScript |
| Forks | 8,973 |
| Issues | 1,665 |
| Topics | diagrams, diagrams-as-code, documentation, flowchart, javascript, mindmap, typescript, uml-diagrams |
| 许可证 | MIT License |


### Chalarangelo/30-seconds-of-code

**描述**: Coding articles to level up your development skills

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,804 |
| 语言 | JavaScript |
| Forks | 12,485 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 172,645 |
| 语言 | Go |
| Forks | 13,208 |
| Issues | 185 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,385 |
| 语言 | Unknown |
| Forks | 34,233 |
| Issues | 141 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### mattpocock/skills

**描述**: Skills for Real Engineers. Straight from my .claude directory.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,937 |
| 语言 | Shell |
| Forks | 7,066 |
| Issues | 27 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,342 |
| 语言 | Python |
| Forks | 8,648 |
| Issues | 410 |
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
| Stars | 93,009 |
| 语言 | Python |
| Forks | 13,540 |
| Issues | 113 |
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
| Stars | 388,297 |
| 语言 | Python |
| Forks | 66,300 |
| Issues | 80 |
| Topics | books, education, hacktoberfest, list, resource |
| 许可证 | Creative Commons Attribution 4.0 International |


### clash-verge-rev/clash-verge-rev

**描述**: A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,107 |
| 语言 | TypeScript |
| Forks | 8,602 |
| Issues | 316 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### iptv-org/iptv

**描述**: Collection of publicly available IPTV channels from all over the world

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,214 |
| 语言 | TypeScript |
| Forks | 6,130 |
| Issues | 47 |
| Topics | iptv, m3u, playlist, streams, tv |
| 许可证 | The Unlicense |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,607 |
| 语言 | TypeScript |
| Forks | 14,364 |
| Issues | 494 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,214 |
| 语言 | JavaScript |
| Forks | 5,277 |
| Issues | 50 |
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
| Stars | 48,396 |
| 语言 | Go |
| Forks | 10,347 |
| Issues | 1,896 |
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
| Stars | 110,128 |
| 语言 | C++ |
| Forks | 18,193 |
| Issues | 1,613 |
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
| Stars | 63,320 |
| 语言 | Python |
| Forks | 1,670 |
| Issues | 38 |
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
| Stars | 38,340 |
| 语言 | TypeScript |
| Forks | 4,388 |
| Issues | 298 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 297,642 |
| 语言 | Python |
| Forks | 27,904 |
| Issues | 19 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,058 |
| 语言 | Python |
| Forks | 37,479 |
| Issues | 4,036 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,732 |
| 语言 | TypeScript |
| Forks | 44,562 |
| Issues | 191 |
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
| Stars | 354,762 |
| 语言 | TypeScript |
| Forks | 44,075 |
| Issues | 11 |
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
| Stars | 123,217 |
| 语言 | TypeScript |
| Forks | 13,650 |
| Issues | 3,050 |
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
| Stars | 114,355 |
| 语言 | TypeScript |
| Forks | 8,799 |
| Issues | 1,888 |
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
| Stars | 108,854 |
| 语言 | TypeScript |
| Forks | 13,396 |
| Issues | 5,036 |
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
| Stars | 100,573 |
| 语言 | TypeScript |
| Forks | 5,594 |
| Issues | 663 |
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
| Stars | 98,031 |
| 语言 | TypeScript |
| Forks | 54,611 |
| Issues | 1,365 |
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
| Stars | 95,014 |
| 语言 | TypeScript |
| Forks | 5,239 |
| Issues | 89 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,646 |
| 语言 | TypeScript |
| Forks | 10,690 |
| Issues | 452 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,438 |
| 语言 | TypeScript |
| Forks | 7,609 |
| Issues | 36 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,605 |
| 语言 | TypeScript |
| Forks | 8,175 |
| Issues | 726 |
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
| Stars | 245,021 |
| 语言 | JavaScript |
| Forks | 51,037 |
| Issues | 1,301 |
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
| Stars | 117,213 |
| 语言 | JavaScript |
| Forks | 35,531 |
| Issues | 2,682 |
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
| Stars | 112,477 |
| 语言 | JavaScript |
| Forks | 36,373 |
| Issues | 475 |
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
| Stars | 109,056 |
| 语言 | JavaScript |
| Forks | 11,688 |
| Issues | 153 |
| Topics | hacktoberfest, http-client, javascript, nodejs, promise |
| 许可证 | MIT License |


### mui/material-ui

**描述**: Material UI: Comprehensive React component library that implements Google's Material Design. Free forever.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,340 |
| 语言 | JavaScript |
| Forks | 32,641 |
| Issues | 1,537 |
| Topics | design-system, material-design, material-ui, react, react-components |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,750 |
| 语言 | JavaScript |
| Forks | 15,479 |
| Issues | 60 |
| Topics | css, curriculum, education, html, javascript, learning, microsoft-for-beginners, tutorials |
| 许可证 | MIT License |


### sveltejs/svelte

**描述**: web development for the rest of us

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,566 |
| 语言 | JavaScript |
| Forks | 4,915 |
| Issues | 1,003 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,418 |
| 语言 | JavaScript |
| Forks | 9,189 |
| Issues | 4 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,766 |
| 语言 | JavaScript |
| Forks | 9,356 |
| Issues | 202 |
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
| Stars | 64,673 |
| 语言 | JavaScript |
| Forks | 4,108 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,227 |
| 语言 | JavaScript |
| Forks | 7,163 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,102 |
| 语言 | JavaScript |
| Forks | 5,674 |
| Issues | 63 |
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
| Stars | 59,842 |
| 语言 | JavaScript |
| Forks | 20,439 |
| Issues | 95 |
| Topics | jquery |
| 许可证 | MIT License |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,434 |
| 语言 | JavaScript |
| Forks | 12,310 |
| Issues | 27 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,314 |
| 语言 | JavaScript |
| Forks | 10,616 |
| Issues | 449 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,795 |
| 语言 | JavaScript |
| Forks | 11,550 |
| Issues | 269 |
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
| Stars | 133,880 |
| 语言 | Go |
| Forks | 19,008 |
| Issues | 10,139 |
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
| Stars | 106,531 |
| 语言 | Go |
| Forks | 15,044 |
| Issues | 43 |
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
| Stars | 88,049 |
| 语言 | Go |
| Forks | 8,266 |
| Issues | 233 |
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
| Stars | 84,006 |
| 语言 | Go |
| Forks | 5,183 |
| Issues | 384 |
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
| Stars | 68,574 |
| 语言 | Go |
| Forks | 3,235 |
| Issues | 46 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,184 |
| 语言 | Go |
| Forks | 5,090 |
| Issues | 1,182 |
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
| Stars | 51,040 |
| 语言 | Go |
| Forks | 21,912 |
| Issues | 397 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,469 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 575 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### multica-ai/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 129,547 |
| 语言 | Unknown |
| Forks | 13,139 |
| Issues | 89 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 221,045 |
| 语言 | Python |
| Forks | 50,627 |
| Issues | 973 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,490 |
| 语言 | Python |
| Forks | 12,185 |
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
| Stars | 86,825 |
| 语言 | Python |
| Forks | 7,288 |
| Issues | 492 |
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
| Stars | 77,704 |
| 语言 | Python |
| Forks | 16,962 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,126 |
| 语言 | JavaScript |
| Forks | 26,686 |
| Issues | 160 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,211 |
| 语言 | JavaScript |
| Forks | 16,804 |
| Issues | 897 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,142 |
| 语言 | JavaScript |
| Forks | 4,579 |
| Issues | 102 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,415 |
| 语言 | JavaScript |
| Forks | 11,951 |
| Issues | 564 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,038 |
| 语言 | Go |
| Forks | 1,612 |
| Issues | 274 |
| 许可证 | MIT License |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,853 |
| 语言 | Go |
| Forks | 8,855 |
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
| Stars | 46,358 |
| 语言 | Go |
| Forks | 3,822 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 156,830 |
| 语言 | Python |
| Forks | 11,958 |
| Issues | 366 |
| Topics | awesome, github, hellogithub, python |
