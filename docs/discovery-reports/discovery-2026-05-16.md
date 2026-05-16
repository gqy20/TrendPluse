# 项目发现报告 (2026-05-16)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 122 |
| 去重移除 | 38 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 62 |

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
| Stars | 153,239 |
| 语言 | Python |
| Forks | 24,415 |
| Issues | 11,649 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高人气智能体框架，拥有 15.3 万颗 Stars，支持 OpenAI、Anthropic Claude 等多平台 LLM 集成，具备可扩展的工具调用和多模态交互能力，是构建企业级 AI Agent 的理想选择。

**技术亮点**:
- 多 LLM 供应商支持：无缝集成 OpenAI GPT 系列、Anthropic Claude 等主流大语言模型，提供统一接口
- 强大的工具调用系统：支持动态函数调用和工具编排，实现复杂任务自动化执行
- 可扩展架构设计：模块化设计支持自定义工具和插件，便于功能扩展和定制开发
- 支持 Claude Code 集成：原生支持 Claude 的代码执行和交互能力，适合代码生成与自动化场景
- 活跃的开源社区：由 NousResearch 维护，拥有庞大社区支持和持续更新

**适用场景**:
- 企业智能助手：构建支持多模型切换的对话式 AI 助手，提升客户服务和内部办公效率
- 代码自动化开发：集成 Claude Code 能力，实现代码生成、审查和自动化编程任务
- 多步骤复杂任务编排：通过工具调用系统编排多个 API 和函数，执行数据分析、内容生成等复杂工作流



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,348 |
| 语言 | Python |
| Forks | 19,598 |
| Issues | 300 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一支持 Ollama 和 OpenAI API 让用户轻松部署私有 LLM 服务，同时内置 RAG 和 MCP 等高级功能，是追求数据隐私和成本控制的开发者的首选 AI 前端框架。

**技术亮点**:
- 多后端统一接口 — 同时兼容 Ollama 和 OpenAI API，实现模型供应商的无缝切换
- 内置 RAG 支持 — 原生支持检索增强生成，可直接上传文档进行知识库问答
- MCP 协议集成 — 支持 Model Context Protocol，扩展 AI 能力边界
- 完全自托管 — 数据完全存储在本地，确保隐私安全，无需依赖云服务
- 开箱即用 — 提供 Docker 一键部署，零配置快速上线 AI 界面

**适用场景**:
- 企业私有化部署 — 需要在防火墙内运行 AI 助手，处理敏感业务数据
- 个人开发者实验 — 希望低成本运行本地 LLM，验证创意想法
- 研究测试环境 — 快速对比不同 LLM 模型的输出效果



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,625 |
| 语言 | Python |
| Forks | 9,219 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个拥有 80,000+ Stars 的领先开源 RAG 引擎，创造性地将 RAG 与 Agent 能力融合，为 LLM 提供 superior context layer，特别适合构建企业级知识问答系统和智能文档检索应用。

**技术亮点**:
- 融合 RAG 与 Agent 能力，实现智能检索增强生成，支持复杂多跳推理
- 提供 Agentic Retrieval 能力，支持 agentic-search 和 agentic-retrieval 高级检索模式
- 专注于 Context Engine 和 Context Management，优化 LLM 应用的上下文质量
- 完整的 Python 技术栈，便于集成到现有 LLM 应用生态
- Apache License 2.0 开源，配套完善的文档和活跃的社区支持

**适用场景**:
- 企业级知识库问答系统：构建私有知识库的智能问答，支持复杂文档理解和多轮对话
- 智能文档检索与分析：实现语义化的文档搜索，自动提取关键信息，支持结构化知识抽取
- LLM 应用开发框架：作为 RAG 能力层，为各类 LLM 应用提供检索增强支持



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,609 |
| 语言 | TypeScript |
| Forks | 7,391 |
| Issues | 324 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 代理打造的网页数据提取工具，能够自动搜索、爬取并清洗网页为 AI-ready 格式（如 Markdown），解决了大模型应用获取高质量结构化网页数据的核心痛点，在 GitHub 上拥有超过 12 万星标，是 AI 数据基础设施领域的明星项目。

**技术亮点**:
- 智能网页清洗：自动去除广告、导航栏、Cookie弹窗等干扰元素，输出干净的 Markdown/HTML 内容
- 深度集成 LLM：专为 AI 代理设计，支持直接提取结构化数据并转换为大模型可用的格式
- 动态网页支持：内置 JavaScript 渲染引擎，可处理 React/Vue 等 SPA 单页应用
- 可扩展的爬取架构：支持异步批量爬取，提供速率限制和错误重试机制，适合大规模数据采集
- 多格式输出：支持 Markdown、HTML、LLM Text、Cleaned HTML 等多种输出格式，满足不同场景需求

**适用场景**:
- AI 代理与 RAG 系统：为检索增强生成系统提供实时、干净的网络数据源，构建 AI 知识库
- 竞品分析与市场调研：批量爬取多个网站内容，进行结构化数据提取和对比分析
- 内容聚合与数据管道：构建自动化内容采集流程，将网页数据转换为结构化数据集供机器学习使用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 184,472 |
| 语言 | JavaScript |
| Forks | 28,475 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合系统，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code、Cursor 等工具的开发效率，获得 18 万+ Stars 证明其在开发者社区的广泛认可。

**技术亮点**:
- 基于 MCP(Model Context Protocol) 的标准化集成架构，支持 Claude Code、Codex、Opencode、Cursor 等多平台
- 创新的 Instincts 机制实现自主决策优化，减少人工干预提升效率
- Memory 系统提供持久化上下文管理，增强长对话场景的连贯性
- Security 模块内置多层次安全防护，保障代码操作安全性
- Skills 系统支持可扩展技能库，灵活适配不同开发场景

**适用场景**:
- 个人开发者使用 AI 编程助手提升日常编码效率，适用于快速原型开发和代码补全
- 企业团队集成 AI Agent 系统到开发工作流，实现代码审查和自动化任务处理
- AI 研究人员基于该框架进行 LLM 编程能力评估和性能基准测试



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,292 |
| 语言 | Go |
| Forks | 4,084 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是本地 AI 部署的终极解决方案，支持在无 GPU 环境下运行 LLM、图像生成、语音合成等多模态模型，兼容 OpenAI API 的设计让应用迁移零成本，是企业私有化部署和个人开发者的首选开源项目。

**技术亮点**:
- 多模态统一推理引擎：支持 Llama、Mamba、Stable Diffusion、MusicGen 等主流模型，一个 API 接口覆盖文本、图像、音频、视频处理
- CPU 优先优化：专为无 GPU 场景设计，在消费级硬件上实现高效推理，大幅降低 AI 部署门槛
- OpenAI API 兼容层：提供与 OpenAI 完全兼容的 REST API，支持无缝迁移现有应用
- 去中心化架构：基于 libp2p 构建 P2P 网络，支持分布式推理和边缘计算部署
- 生产级 Go 实现：高并发、低内存占用，适合微服务集成和大规模部署

**适用场景**:
- 企业 AI 私有化：金融、医疗、法律等对数据隐私敏感的行业需要本地部署 AI 能力
- 边缘计算与物联网：在没有稳定网络连接的远程环境中运行 AI 推理
- 开发者快速原型：利用 OpenAI 兼容 API 快速构建和测试 AI 应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,160 |
| 语言 | TypeScript |
| Forks | 15,189 |
| Issues | 803 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的多智能体协作平台，提供了完整的 Agent Harness 解决方案，支持多模型集成（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，特别适合需要构建智能体团队和复杂 AI 工作流的开发者和企业。

**技术亮点**:
- 多智能体协作框架：支持构建和管理多个 AI 智能体组成的团队，实现智能体间的协同工作
- 多模型统一接入：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一接口
- MCP (Model Context Protocol) 支持：遵循 AI 领域的上下文协议标准，便于扩展和集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，提升智能体回答质量
- 完整的 Agent 设计工具：提供可视化或低代码方式设计智能体行为和工作流

**适用场景**:
- 企业团队协作自动化：构建多智能体团队处理客户服务、文档处理、数据分析等复杂工作流
- AI 应用快速开发：开发者使用现成的 Agent 框架快速构建和部署 AI 应用，降低开发门槛
- 知识问答与文档助手：利用知识库集成构建企业知识库问答系统或智能文档助手



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,153 |
| 语言 | TypeScript |
| Forks | 6,537 |
| Issues | 100 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

Claude-Mem 通过 AI 压缩和 RAG 检索技术解决了 AI Agent 跨会话"失忆"的核心痛点，为多种主流 Agent 提供统一的长期记忆管理，是构建企业级智能应用的关键基础设施

**技术亮点**:
- 多 Agent 统一记忆架构：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等 10+ 种主流 AI Agent，提供统一的记忆管理接口
- AI 驱动的智能压缩：采用先进的压缩算法处理会话记忆，在保持关键信息的同时大幅降低存储成本
- RAG + 向量嵌入检索：基于 ChromaDB 构建向量数据库，利用语义嵌入技术实现精准的上下文召回
- 混合持久化存储：结合 SQLite（结构化数据）和 ChromaDB（向量数据）的优势，兼顾速度与检索能力
- 无缝上下文注入：通过智能调度机制，将相关历史上下文自动注入新会话的 prompt 中

**适用场景**:
- 企业级 AI Agent 部署：为客服机器人、代码助手等需要记住用户偏好和交互历史的 Agent 提供长期记忆能力
- 复杂多步骤任务处理：支持需要跨多个会话累积上下文的项目，如大型代码重构、长期研究任务
- 个人开发者构建智能助手：开发者可基于此项目快速为自定义 AI 助手添加记忆功能
- 多 Agent 协作系统：在需要多个 AI Agent 共享上下文的企业场景中作为统一的记忆中枢



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,320 |
| 语言 | Python |
| Forks | 8,713 |
| Issues | 1,016 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调工具，支持 100+ LLMs 和 VLMs，提供统一的微调框架大幅降低训练成本，已被 ACL 2024 收录，是企业部署私有化大模型的理想选择。

**技术亮点**:
- 支持 100+ 预训练模型：Llama、Qwen、Gemma、DeepSeek、Mistral 等主流大模型
- 集成多种高效微调技术：LoRA、QLoRA、Full-parameter、RLHF (DPO/KTO) 等
- 支持视觉-语言模型 (VLM) 微调，可处理多模态任务
- 提供一键式 WebUI 和 CLI 工具，降低使用门槛
- 内置分布式训练优化，支持多 GPU 并行和量化训练

**适用场景**:
- 企业私有化部署：使用自有数据微调 Llama/Qwen 等开源模型，构建垂直领域 AI 助手
- 学术研究与模型实验：快速验证不同微调方法（LoRA vs RLHF）对模型效果的影响
- 多模态应用开发：微调视觉语言模型用于图像描述、视觉问答等任务



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,122 |
| 语言 | Python |
| Forks | 14,814 |
| Issues | 345 |
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
| Stars | 60,809 |
| 语言 | TypeScript |
| Forks | 9,948 |
| Issues | 126 |
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
| Stars | 53,286 |
| 语言 | HTML |
| Forks | 5,333 |
| Issues | 15 |
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
| Stars | 50,113 |
| 语言 | Python |
| Forks | 6,044 |
| Issues | 115 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,288 |
| 语言 | Java |
| Forks | 15,997 |
| Issues | 20 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,871 |
| 语言 | TypeScript |
| Forks | 5,843 |
| Issues | 542 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,128 |
| 语言 | JavaScript |
| Forks | 6,503 |
| Issues | 369 |
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
| Stars | 73,755 |
| 语言 | Python |
| Forks | 9,334 |
| Issues | 414 |
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
| Stars | 58,113 |
| 语言 | TypeScript |
| Forks | 4,714 |
| Issues | 556 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,177 |
| 语言 | Python |
| Forks | 6,208 |
| Issues | 82 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,660 |
| 语言 | Python |
| Forks | 16,399 |
| Issues | 6 |
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
| Stars | 94,185 |
| 语言 | Python |
| Forks | 10,641 |
| Issues | 230 |
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
| Stars | 52,855 |
| 语言 | TypeScript |
| Forks | 24,347 |
| Issues | 860 |
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
| Stars | 188,170 |
| 语言 | TypeScript |
| Forks | 57,690 |
| Issues | 1,496 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,726 |
| 语言 | JavaScript |
| Forks | 46,137 |
| Issues | 61 |
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
| Stars | 148,238 |
| 语言 | Python |
| Forks | 8,997 |
| Issues | 916 |
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
| Stars | 61,682 |
| 语言 | Jupyter Notebook |
| Forks | 20,883 |
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
| Stars | 72,606 |
| 语言 | Rust |
| Forks | 4,703 |
| Issues | 871 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,123 |
| 语言 | Python |
| Forks | 6,542 |
| Issues | 640 |
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
| Stars | 137,348 |
| 语言 | Python |
| Forks | 19,598 |
| Issues | 300 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一支持 Ollama 和 OpenAI API 让用户轻松部署私有 LLM 服务，同时内置 RAG 和 MCP 等高级功能，是追求数据隐私和成本控制的开发者的首选 AI 前端框架。

**技术亮点**:
- 多后端统一接口 — 同时兼容 Ollama 和 OpenAI API，实现模型供应商的无缝切换
- 内置 RAG 支持 — 原生支持检索增强生成，可直接上传文档进行知识库问答
- MCP 协议集成 — 支持 Model Context Protocol，扩展 AI 能力边界
- 完全自托管 — 数据完全存储在本地，确保隐私安全，无需依赖云服务
- 开箱即用 — 提供 Docker 一键部署，零配置快速上线 AI 界面

**适用场景**:
- 企业私有化部署 — 需要在防火墙内运行 AI 助手，处理敏感业务数据
- 个人开发者实验 — 希望低成本运行本地 LLM，验证创意想法
- 研究测试环境 — 快速对比不同 LLM 模型的输出效果



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,625 |
| 语言 | Python |
| Forks | 9,219 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个拥有 80,000+ Stars 的领先开源 RAG 引擎，创造性地将 RAG 与 Agent 能力融合，为 LLM 提供 superior context layer，特别适合构建企业级知识问答系统和智能文档检索应用。

**技术亮点**:
- 融合 RAG 与 Agent 能力，实现智能检索增强生成，支持复杂多跳推理
- 提供 Agentic Retrieval 能力，支持 agentic-search 和 agentic-retrieval 高级检索模式
- 专注于 Context Engine 和 Context Management，优化 LLM 应用的上下文质量
- 完整的 Python 技术栈，便于集成到现有 LLM 应用生态
- Apache License 2.0 开源，配套完善的文档和活跃的社区支持

**适用场景**:
- 企业级知识库问答系统：构建私有知识库的智能问答，支持复杂文档理解和多轮对话
- 智能文档检索与分析：实现语义化的文档搜索，自动提取关键信息，支持结构化知识抽取
- LLM 应用开发框架：作为 RAG 能力层，为各类 LLM 应用提供检索增强支持



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,160 |
| 语言 | TypeScript |
| Forks | 15,189 |
| Issues | 803 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的多智能体协作平台，提供了完整的 Agent Harness 解决方案，支持多模型集成（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，特别适合需要构建智能体团队和复杂 AI 工作流的开发者和企业。

**技术亮点**:
- 多智能体协作框架：支持构建和管理多个 AI 智能体组成的团队，实现智能体间的协同工作
- 多模型统一接入：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一接口
- MCP (Model Context Protocol) 支持：遵循 AI 领域的上下文协议标准，便于扩展和集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，提升智能体回答质量
- 完整的 Agent 设计工具：提供可视化或低代码方式设计智能体行为和工作流

**适用场景**:
- 企业团队协作自动化：构建多智能体团队处理客户服务、文档处理、数据分析等复杂工作流
- AI 应用快速开发：开发者使用现成的 Agent 框架快速构建和部署 AI 应用，降低开发门槛
- 知识问答与文档助手：利用知识库集成构建企业知识库问答系统或智能文档助手



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,153 |
| 语言 | TypeScript |
| Forks | 6,537 |
| Issues | 100 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

Claude-Mem 通过 AI 压缩和 RAG 检索技术解决了 AI Agent 跨会话"失忆"的核心痛点，为多种主流 Agent 提供统一的长期记忆管理，是构建企业级智能应用的关键基础设施

**技术亮点**:
- 多 Agent 统一记忆架构：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等 10+ 种主流 AI Agent，提供统一的记忆管理接口
- AI 驱动的智能压缩：采用先进的压缩算法处理会话记忆，在保持关键信息的同时大幅降低存储成本
- RAG + 向量嵌入检索：基于 ChromaDB 构建向量数据库，利用语义嵌入技术实现精准的上下文召回
- 混合持久化存储：结合 SQLite（结构化数据）和 ChromaDB（向量数据）的优势，兼顾速度与检索能力
- 无缝上下文注入：通过智能调度机制，将相关历史上下文自动注入新会话的 prompt 中

**适用场景**:
- 企业级 AI Agent 部署：为客服机器人、代码助手等需要记住用户偏好和交互历史的 Agent 提供长期记忆能力
- 复杂多步骤任务处理：支持需要跨多个会话累积上下文的项目，如大型代码重构、长期研究任务
- 个人开发者构建智能助手：开发者可基于此项目快速为自定义 AI 助手添加记忆功能
- 多 Agent 协作系统：在需要多个 AI Agent 共享上下文的企业场景中作为统一的记忆中枢



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,113 |
| 语言 | Python |
| Forks | 6,044 |
| Issues | 115 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,288 |
| 语言 | Java |
| Forks | 15,997 |
| Issues | 20 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 102,449 |
| 语言 | TypeScript |
| Forks | 12,416 |
| Issues | 1,010 |
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
| Stars | 60,128 |
| 语言 | JavaScript |
| Forks | 6,503 |
| Issues | 369 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,177 |
| 语言 | Python |
| Forks | 6,208 |
| Issues | 82 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,660 |
| 语言 | Python |
| Forks | 16,399 |
| Issues | 6 |
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
| Stars | 77,955 |
| 语言 | Python |
| Forks | 10,439 |
| Issues | 207 |
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
| Stars | 52,855 |
| 语言 | TypeScript |
| Forks | 24,347 |
| Issues | 860 |
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
| Stars | 48,541 |
| 语言 | Python |
| Forks | 5,270 |
| Issues | 250 |
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
| Stars | 44,325 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 889 |
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
| Stars | 35,278 |
| 语言 | Python |
| Forks | 4,993 |
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
| Stars | 153,239 |
| 语言 | Python |
| Forks | 24,415 |
| Issues | 11,649 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高人气智能体框架，拥有 15.3 万颗 Stars，支持 OpenAI、Anthropic Claude 等多平台 LLM 集成，具备可扩展的工具调用和多模态交互能力，是构建企业级 AI Agent 的理想选择。

**技术亮点**:
- 多 LLM 供应商支持：无缝集成 OpenAI GPT 系列、Anthropic Claude 等主流大语言模型，提供统一接口
- 强大的工具调用系统：支持动态函数调用和工具编排，实现复杂任务自动化执行
- 可扩展架构设计：模块化设计支持自定义工具和插件，便于功能扩展和定制开发
- 支持 Claude Code 集成：原生支持 Claude 的代码执行和交互能力，适合代码生成与自动化场景
- 活跃的开源社区：由 NousResearch 维护，拥有庞大社区支持和持续更新

**适用场景**:
- 企业智能助手：构建支持多模型切换的对话式 AI 助手，提升客户服务和内部办公效率
- 代码自动化开发：集成 Claude Code 能力，实现代码生成、审查和自动化编程任务
- 多步骤复杂任务编排：通过工具调用系统编排多个 API 和函数，执行数据分析、内容生成等复杂工作流



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,348 |
| 语言 | Python |
| Forks | 19,598 |
| Issues | 300 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一支持 Ollama 和 OpenAI API 让用户轻松部署私有 LLM 服务，同时内置 RAG 和 MCP 等高级功能，是追求数据隐私和成本控制的开发者的首选 AI 前端框架。

**技术亮点**:
- 多后端统一接口 — 同时兼容 Ollama 和 OpenAI API，实现模型供应商的无缝切换
- 内置 RAG 支持 — 原生支持检索增强生成，可直接上传文档进行知识库问答
- MCP 协议集成 — 支持 Model Context Protocol，扩展 AI 能力边界
- 完全自托管 — 数据完全存储在本地，确保隐私安全，无需依赖云服务
- 开箱即用 — 提供 Docker 一键部署，零配置快速上线 AI 界面

**适用场景**:
- 企业私有化部署 — 需要在防火墙内运行 AI 助手，处理敏感业务数据
- 个人开发者实验 — 希望低成本运行本地 LLM，验证创意想法
- 研究测试环境 — 快速对比不同 LLM 模型的输出效果



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 184,472 |
| 语言 | JavaScript |
| Forks | 28,475 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合系统，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code、Cursor 等工具的开发效率，获得 18 万+ Stars 证明其在开发者社区的广泛认可。

**技术亮点**:
- 基于 MCP(Model Context Protocol) 的标准化集成架构，支持 Claude Code、Codex、Opencode、Cursor 等多平台
- 创新的 Instincts 机制实现自主决策优化，减少人工干预提升效率
- Memory 系统提供持久化上下文管理，增强长对话场景的连贯性
- Security 模块内置多层次安全防护，保障代码操作安全性
- Skills 系统支持可扩展技能库，灵活适配不同开发场景

**适用场景**:
- 个人开发者使用 AI 编程助手提升日常编码效率，适用于快速原型开发和代码补全
- 企业团队集成 AI Agent 系统到开发工作流，实现代码审查和自动化任务处理
- AI 研究人员基于该框架进行 LLM 编程能力评估和性能基准测试



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,985 |
| 语言 | JavaScript |
| Forks | 3,396 |
| Issues | 206 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 是一个极具创意的 Claude Code 技能，通过模仿原始人的简洁表达风格实现高达 65% 的 token 消耗削减，在保持 AI 交互效果的同时显著降低使用成本，适合所有希望优化 LLM 成本和效率的开发者。

**技术亮点**:
- 采用「 caveman speak 」风格的极简提示词策略，将复杂表达压缩为简短原始的语句，大幅降低 token 消耗
- 实现 65% 的 token 用量削减，效果经过实际验证
- 作为 Claude Code 原生技能集成，安装即可使用，操作简便
- 基于 prompt engineering 最佳实践，通过语义压缩而非语义丢失来优化交互
- 开源 MIT 许可证，可自由使用、修改和商业化

**适用场景**:
- AI 应用开发成本优化：对于需要频繁调用 LLM API 的应用（如代码生成、自动化脚本），使用 caveman 风格提示可显著降低 API 调用成本
- 高频 Claude Code 使用场景：频繁使用 Claude Code 进行代码编写和调试的开发者，通过 token 削减可在相同预算下完成更多任务
- 资源受限环境：在 token 限额严格的 API 服务或需要控制输出长度的场景下，保持核心功能的同时减少资源占用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,160 |
| 语言 | TypeScript |
| Forks | 15,189 |
| Issues | 803 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的多智能体协作平台，提供了完整的 Agent Harness 解决方案，支持多模型集成（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，特别适合需要构建智能体团队和复杂 AI 工作流的开发者和企业。

**技术亮点**:
- 多智能体协作框架：支持构建和管理多个 AI 智能体组成的团队，实现智能体间的协同工作
- 多模型统一接入：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供统一接口
- MCP (Model Context Protocol) 支持：遵循 AI 领域的上下文协议标准，便于扩展和集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，提升智能体回答质量
- 完整的 Agent 设计工具：提供可视化或低代码方式设计智能体行为和工作流

**适用场景**:
- 企业团队协作自动化：构建多智能体团队处理客户服务、文档处理、数据分析等复杂工作流
- AI 应用快速开发：开发者使用现成的 Agent 框架快速构建和部署 AI 应用，降低开发门槛
- 知识问答与文档助手：利用知识库集成构建企业知识库问答系统或智能文档助手



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,153 |
| 语言 | TypeScript |
| Forks | 6,537 |
| Issues | 100 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

Claude-Mem 通过 AI 压缩和 RAG 检索技术解决了 AI Agent 跨会话"失忆"的核心痛点，为多种主流 Agent 提供统一的长期记忆管理，是构建企业级智能应用的关键基础设施

**技术亮点**:
- 多 Agent 统一记忆架构：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等 10+ 种主流 AI Agent，提供统一的记忆管理接口
- AI 驱动的智能压缩：采用先进的压缩算法处理会话记忆，在保持关键信息的同时大幅降低存储成本
- RAG + 向量嵌入检索：基于 ChromaDB 构建向量数据库，利用语义嵌入技术实现精准的上下文召回
- 混合持久化存储：结合 SQLite（结构化数据）和 ChromaDB（向量数据）的优势，兼顾速度与检索能力
- 无缝上下文注入：通过智能调度机制，将相关历史上下文自动注入新会话的 prompt 中

**适用场景**:
- 企业级 AI Agent 部署：为客服机器人、代码助手等需要记住用户偏好和交互历史的 Agent 提供长期记忆能力
- 复杂多步骤任务处理：支持需要跨多个会话累积上下文的项目，如大型代码重构、长期研究任务
- 个人开发者构建智能助手：开发者可基于此项目快速为自定义 AI 助手添加记忆功能
- 多 Agent 协作系统：在需要多个 AI Agent 共享上下文的企业场景中作为统一的记忆中枢



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,360 |
| 语言 | HTML |
| Forks | 21,138 |
| Issues | 45 |
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
| Stars | 94,930 |
| 语言 | Jupyter Notebook |
| Forks | 14,540 |
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
| Stars | 60,809 |
| 语言 | TypeScript |
| Forks | 9,948 |
| Issues | 126 |
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
| Stars | 53,286 |
| 语言 | HTML |
| Forks | 5,333 |
| Issues | 15 |
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
| Stars | 60,128 |
| 语言 | JavaScript |
| Forks | 6,503 |
| Issues | 369 |
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
| Stars | 73,755 |
| 语言 | Python |
| Forks | 9,334 |
| Issues | 414 |
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
| Stars | 58,113 |
| 语言 | TypeScript |
| Forks | 4,714 |
| Issues | 556 |
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
| Stars | 52,855 |
| 语言 | TypeScript |
| Forks | 24,347 |
| Issues | 860 |
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
| Stars | 80,196 |
| 语言 | Python |
| Forks | 16,854 |
| Issues | 4,962 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### ChatGPTNextWeb/NextChat

**描述**: ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android |  Linux | Windows

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,006 |
| 语言 | TypeScript |
| Forks | 59,713 |
| Issues | 824 |
| Topics | calclaude, chatgpt, claude, cross-platform, desktop, fe, gemini, gemini-pro, gemini-server, gemini-ultra, gpt-4o, groq, nextjs, ollama, react, tauri, tauri-app, vercel, webui |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,238 |
| 语言 | Python |
| Forks | 8,997 |
| Issues | 916 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,535 |
| 语言 | Go |
| Forks | 16,150 |
| Issues | 3,265 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,123 |
| 语言 | Python |
| Forks | 6,542 |
| Issues | 640 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 123,400 |
| 语言 | Python |
| Forks | 8,338 |
| Issues | 653 |
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
| Stars | 71,320 |
| 语言 | Python |
| Forks | 8,713 |
| Issues | 1,016 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调工具，支持 100+ LLMs 和 VLMs，提供统一的微调框架大幅降低训练成本，已被 ACL 2024 收录，是企业部署私有化大模型的理想选择。

**技术亮点**:
- 支持 100+ 预训练模型：Llama、Qwen、Gemma、DeepSeek、Mistral 等主流大模型
- 集成多种高效微调技术：LoRA、QLoRA、Full-parameter、RLHF (DPO/KTO) 等
- 支持视觉-语言模型 (VLM) 微调，可处理多模态任务
- 提供一键式 WebUI 和 CLI 工具，降低使用门槛
- 内置分布式训练优化，支持多 GPU 并行和量化训练

**适用场景**:
- 企业私有化部署：使用自有数据微调 Llama/Qwen 等开源模型，构建垂直领域 AI 助手
- 学术研究与模型实验：快速验证不同微调方法（LoRA vs RLHF）对模型效果的影响
- 多模态应用开发：微调视觉语言模型用于图像描述、视觉问答等任务



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,636 |
| 语言 | Python |
| Forks | 6,803 |
| Issues | 81 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,360 |
| 语言 | HTML |
| Forks | 21,138 |
| Issues | 45 |
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
| Stars | 94,930 |
| 语言 | Jupyter Notebook |
| Forks | 14,540 |
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
| Stars | 160,665 |
| 语言 | Python |
| Forks | 33,232 |
| Issues | 2,349 |
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
| Stars | 80,196 |
| 语言 | Python |
| Forks | 16,854 |
| Issues | 4,962 |
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
| Stars | 113,177 |
| 语言 | Python |
| Forks | 13,258 |
| Issues | 4,008 |
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
| Stars | 99,947 |
| 语言 | Python |
| Forks | 27,804 |
| Issues | 18,524 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (17 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 184,472 |
| 语言 | JavaScript |
| Forks | 28,475 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合系统，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code、Cursor 等工具的开发效率，获得 18 万+ Stars 证明其在开发者社区的广泛认可。

**技术亮点**:
- 基于 MCP(Model Context Protocol) 的标准化集成架构，支持 Claude Code、Codex、Opencode、Cursor 等多平台
- 创新的 Instincts 机制实现自主决策优化，减少人工干预提升效率
- Memory 系统提供持久化上下文管理，增强长对话场景的连贯性
- Security 模块内置多层次安全防护，保障代码操作安全性
- Skills 系统支持可扩展技能库，灵活适配不同开发场景

**适用场景**:
- 个人开发者使用 AI 编程助手提升日常编码效率，适用于快速原型开发和代码补全
- 企业团队集成 AI Agent 系统到开发工作流，实现代码审查和自动化任务处理
- AI 研究人员基于该框架进行 LLM 编程能力评估和性能基准测试



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,292 |
| 语言 | Go |
| Forks | 4,084 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是本地 AI 部署的终极解决方案，支持在无 GPU 环境下运行 LLM、图像生成、语音合成等多模态模型，兼容 OpenAI API 的设计让应用迁移零成本，是企业私有化部署和个人开发者的首选开源项目。

**技术亮点**:
- 多模态统一推理引擎：支持 Llama、Mamba、Stable Diffusion、MusicGen 等主流模型，一个 API 接口覆盖文本、图像、音频、视频处理
- CPU 优先优化：专为无 GPU 场景设计，在消费级硬件上实现高效推理，大幅降低 AI 部署门槛
- OpenAI API 兼容层：提供与 OpenAI 完全兼容的 REST API，支持无缝迁移现有应用
- 去中心化架构：基于 libp2p 构建 P2P 网络，支持分布式推理和边缘计算部署
- 生产级 Go 实现：高并发、低内存占用，适合微服务集成和大规模部署

**适用场景**:
- 企业 AI 私有化：金融、医疗、法律等对数据隐私敏感的行业需要本地部署 AI 能力
- 边缘计算与物联网：在没有稳定网络连接的远程环境中运行 AI 推理
- 开发者快速原型：利用 OpenAI 兼容 API 快速构建和测试 AI 应用



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,288 |
| 语言 | Java |
| Forks | 15,997 |
| Issues | 20 |
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
| Stars | 73,755 |
| 语言 | Python |
| Forks | 9,334 |
| Issues | 414 |
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
| Stars | 58,113 |
| 语言 | TypeScript |
| Forks | 4,714 |
| Issues | 556 |
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
| Stars | 188,170 |
| 语言 | TypeScript |
| Forks | 57,690 |
| Issues | 1,496 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,134 |
| 语言 | JavaScript |
| Forks | 4,207 |
| Issues | 1,308 |
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
| Stars | 435,307 |
| 语言 | Python |
| Forks | 47,711 |
| Issues | 1,331 |
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
| Stars | 162,614 |
| 语言 | Python |
| Forks | 13,632 |
| Issues | 2,506 |
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
| Stars | 98,259 |
| 语言 | Python |
| Forks | 9,302 |
| Issues | 206 |
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
| Stars | 83,402 |
| 语言 | Python |
| Forks | 9,724 |
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
| Stars | 184,986 |
| 语言 | TypeScript |
| Forks | 39,889 |
| Issues | 17,556 |
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
| Stars | 94,331 |
| 语言 | TypeScript |
| Forks | 9,416 |
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
| Stars | 79,192 |
| 语言 | TypeScript |
| Forks | 5,875 |
| Issues | 726 |
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
| Stars | 80,294 |
| 语言 | Go |
| Forks | 2,806 |
| Issues | 319 |
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
| Stars | 78,018 |
| 语言 | Go |
| Forks | 2,835 |
| Issues | 961 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,123 |
| 语言 | Python |
| Forks | 6,542 |
| Issues | 640 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


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
| Stars | 58,113 |
| 语言 | TypeScript |
| Forks | 4,714 |
| Issues | 556 |
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
| Stars | 188,170 |
| 语言 | TypeScript |
| Forks | 57,690 |
| Issues | 1,496 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


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
| Forks | 10,355 |
| Issues | 239 |
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
| Stars | 122,303 |
| 语言 | Go |
| Forks | 43,080 |
| Issues | 2,700 |
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
| Stars | 71,559 |
| 语言 | Go |
| Forks | 18,951 |
| Issues | 3,783 |
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
| Stars | 55,719 |
| 语言 | Go |
| Forks | 6,705 |
| Issues | 2,792 |
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
| Stars | 94,331 |
| 语言 | TypeScript |
| Forks | 9,416 |
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
| Stars | 78,829 |
| 语言 | TypeScript |
| Forks | 6,902 |
| Issues | 398 |
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
| Stars | 86,871 |
| 语言 | JavaScript |
| Forks | 7,859 |
| Issues | 746 |
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
| Stars | 70,299 |
| 语言 | Go |
| Forks | 1,919 |
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
| Stars | 63,179 |
| 语言 | Go |
| Forks | 5,993 |
| Issues | 817 |
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
| Stars | 59,676 |
| 语言 | Go |
| Forks | 4,368 |
| Issues | 26 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,123 |
| 语言 | Python |
| Forks | 6,542 |
| Issues | 640 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,520 |
| 语言 | Go |
| Forks | 5,063 |
| Issues | 994 |
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
| Stars | 60,937 |
| 语言 | Go |
| Forks | 7,502 |
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
| Stars | 86,871 |
| 语言 | JavaScript |
| Forks | 7,859 |
| Issues | 746 |
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
| Stars | 64,069 |
| 语言 | Go |
| Forks | 10,409 |
| Issues | 771 |
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
| Stars | 46,292 |
| 语言 | Go |
| Forks | 4,084 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是本地 AI 部署的终极解决方案，支持在无 GPU 环境下运行 LLM、图像生成、语音合成等多模态模型，兼容 OpenAI API 的设计让应用迁移零成本，是企业私有化部署和个人开发者的首选开源项目。

**技术亮点**:
- 多模态统一推理引擎：支持 Llama、Mamba、Stable Diffusion、MusicGen 等主流模型，一个 API 接口覆盖文本、图像、音频、视频处理
- CPU 优先优化：专为无 GPU 场景设计，在消费级硬件上实现高效推理，大幅降低 AI 部署门槛
- OpenAI API 兼容层：提供与 OpenAI 完全兼容的 REST API，支持无缝迁移现有应用
- 去中心化架构：基于 libp2p 构建 P2P 网络，支持分布式推理和边缘计算部署
- 生产级 Go 实现：高并发、低内存占用，适合微服务集成和大规模部署

**适用场景**:
- 企业 AI 私有化：金融、医疗、法律等对数据隐私敏感的行业需要本地部署 AI 能力
- 边缘计算与物联网：在没有稳定网络连接的远程环境中运行 AI 推理
- 开发者快速原型：利用 OpenAI 兼容 API 快速构建和测试 AI 应用



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,307 |
| 语言 | Python |
| Forks | 47,711 |
| Issues | 1,331 |
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
| Stars | 98,259 |
| 语言 | Python |
| Forks | 9,302 |
| Issues | 206 |
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
| Stars | 87,493 |
| 语言 | Python |
| Forks | 33,879 |
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
| Stars | 100,116 |
| 语言 | TypeScript |
| Forks | 27,215 |
| Issues | 1,148 |
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
| Stars | 79,192 |
| 语言 | TypeScript |
| Forks | 5,875 |
| Issues | 726 |
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
| Stars | 69,024 |
| 语言 | JavaScript |
| Forks | 23,340 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,197 |
| Issues | 375 |
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
| Stars | 88,516 |
| 语言 | Go |
| Forks | 8,609 |
| Issues | 686 |
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
| Stars | 72,501 |
| 语言 | Go |
| Forks | 4,738 |
| Issues | 249 |
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
| Stars | 58,365 |
| 语言 | Go |
| Forks | 3,373 |
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
| Stars | 102,449 |
| 语言 | TypeScript |
| Forks | 12,416 |
| Issues | 1,010 |
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
| Stars | 60,128 |
| 语言 | JavaScript |
| Forks | 6,503 |
| Issues | 369 |
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
| Stars | 44,325 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 889 |
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
| Forks | 10,355 |
| Issues | 239 |
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
| Stars | 60,985 |
| 语言 | JavaScript |
| Forks | 3,396 |
| Issues | 206 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 是一个极具创意的 Claude Code 技能，通过模仿原始人的简洁表达风格实现高达 65% 的 token 消耗削减，在保持 AI 交互效果的同时显著降低使用成本，适合所有希望优化 LLM 成本和效率的开发者。

**技术亮点**:
- 采用「 caveman speak 」风格的极简提示词策略，将复杂表达压缩为简短原始的语句，大幅降低 token 消耗
- 实现 65% 的 token 用量削减，效果经过实际验证
- 作为 Claude Code 原生技能集成，安装即可使用，操作简便
- 基于 prompt engineering 最佳实践，通过语义压缩而非语义丢失来优化交互
- 开源 MIT 许可证，可自由使用、修改和商业化

**适用场景**:
- AI 应用开发成本优化：对于需要频繁调用 LLM API 的应用（如代码生成、自动化脚本），使用 caveman 风格提示可显著降低 API 调用成本
- 高频 Claude Code 使用场景：频繁使用 Claude Code 进行代码编写和调试的开发者，通过 token 削减可在相同预算下完成更多任务
- 资源受限环境：在 token 限额严格的 API 服务或需要控制输出长度的场景下，保持核心功能的同时减少资源占用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,360 |
| 语言 | HTML |
| Forks | 21,138 |
| Issues | 45 |
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
| Stars | 60,809 |
| 语言 | TypeScript |
| Forks | 9,948 |
| Issues | 126 |
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
| Stars | 50,113 |
| 语言 | Python |
| Forks | 6,044 |
| Issues | 115 |
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
| Stars | 89,914 |
| 语言 | TypeScript |
| Forks | 10,061 |
| Issues | 2,209 |
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
| Stars | 88,083 |
| 语言 | TypeScript |
| Forks | 8,982 |
| Issues | 1,670 |
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
| Stars | 127,830 |
| 语言 | JavaScript |
| Forks | 12,490 |
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
| Stars | 172,815 |
| 语言 | Go |
| Forks | 13,214 |
| Issues | 185 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,486 |
| 语言 | Unknown |
| Forks | 34,247 |
| Issues | 142 |
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
| Stars | 86,650 |
| 语言 | Shell |
| Forks | 7,534 |
| Issues | 35 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,817 |
| 语言 | Python |
| Forks | 8,821 |
| Issues | 423 |
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
| Stars | 93,058 |
| 语言 | Python |
| Forks | 13,544 |
| Issues | 112 |
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
| Stars | 388,416 |
| 语言 | Python |
| Forks | 66,302 |
| Issues | 79 |
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
| Stars | 118,552 |
| 语言 | TypeScript |
| Forks | 8,626 |
| Issues | 320 |
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
| Stars | 116,254 |
| 语言 | TypeScript |
| Forks | 6,139 |
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
| Stars | 97,965 |
| 语言 | TypeScript |
| Forks | 14,574 |
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
| Stars | 62,560 |
| 语言 | JavaScript |
| Forks | 5,317 |
| Issues | 54 |
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
| Stars | 48,408 |
| 语言 | Go |
| Forks | 10,351 |
| Issues | 1,897 |
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
| Stars | 110,450 |
| 语言 | C++ |
| Forks | 18,279 |
| Issues | 1,631 |
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
| Stars | 63,307 |
| 语言 | Python |
| Forks | 1,672 |
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
| Stars | 38,626 |
| 语言 | TypeScript |
| Forks | 4,422 |
| Issues | 303 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 297,985 |
| 语言 | Python |
| Forks | 27,918 |
| Issues | 16 |
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
| Stars | 87,079 |
| 语言 | Python |
| Forks | 37,486 |
| Issues | 4,097 |
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
| Stars | 77,662 |
| 语言 | Python |
| Forks | 45,092 |
| Issues | 1,287 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,927 |
| 语言 | TypeScript |
| Forks | 44,598 |
| Issues | 184 |
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
| Stars | 354,883 |
| 语言 | TypeScript |
| Forks | 44,078 |
| Issues | 14 |
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
| Stars | 123,359 |
| 语言 | TypeScript |
| Forks | 13,666 |
| Issues | 3,061 |
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
| Stars | 114,490 |
| 语言 | TypeScript |
| Forks | 8,821 |
| Issues | 1,912 |
| Topics | base-ui, components, laravel, nextjs, radix-ui, react, shadcn, tailwindcss, tanstack, ui, vite |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,765 |
| 语言 | TypeScript |
| Forks | 5,621 |
| Issues | 662 |
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
| Stars | 98,050 |
| 语言 | TypeScript |
| Forks | 54,612 |
| Issues | 1,364 |
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
| Stars | 95,027 |
| 语言 | TypeScript |
| Forks | 5,243 |
| Issues | 92 |
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
| Stars | 85,756 |
| 语言 | TypeScript |
| Forks | 10,713 |
| Issues | 459 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,444 |
| 语言 | TypeScript |
| Forks | 7,607 |
| Issues | 35 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,643 |
| 语言 | TypeScript |
| Forks | 8,180 |
| Issues | 731 |
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
| Stars | 245,061 |
| 语言 | JavaScript |
| Forks | 51,048 |
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
| Stars | 117,254 |
| 语言 | JavaScript |
| Forks | 35,542 |
| Issues | 2,673 |
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
| Stars | 112,521 |
| 语言 | JavaScript |
| Forks | 36,376 |
| Issues | 466 |
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
| Stars | 109,063 |
| 语言 | JavaScript |
| Forks | 11,692 |
| Issues | 157 |
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
| Stars | 98,351 |
| 语言 | JavaScript |
| Forks | 32,639 |
| Issues | 1,536 |
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
| Stars | 95,760 |
| 语言 | JavaScript |
| Forks | 15,486 |
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
| Stars | 86,577 |
| 语言 | JavaScript |
| Forks | 4,913 |
| Issues | 1,006 |
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
| Stars | 66,426 |
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
| Forks | 9,357 |
| Issues | 200 |
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
| Stars | 64,720 |
| 语言 | JavaScript |
| Forks | 4,112 |
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
| Stars | 61,130 |
| 语言 | JavaScript |
| Forks | 5,674 |
| Issues | 62 |
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
| Stars | 59,844 |
| 语言 | JavaScript |
| Forks | 20,437 |
| Issues | 93 |
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
| Stars | 57,437 |
| 语言 | JavaScript |
| Forks | 12,306 |
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
| Stars | 53,318 |
| 语言 | JavaScript |
| Forks | 10,618 |
| Issues | 449 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,915 |
| 语言 | Go |
| Forks | 19,017 |
| Issues | 10,143 |
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
| Stars | 106,573 |
| 语言 | Go |
| Forks | 15,045 |
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
| Stars | 88,086 |
| 语言 | Go |
| Forks | 8,265 |
| Issues | 234 |
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
| Stars | 84,071 |
| 语言 | Go |
| Forks | 5,189 |
| Issues | 385 |
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
| Stars | 68,569 |
| 语言 | Go |
| Forks | 3,234 |
| Issues | 49 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,217 |
| 语言 | Go |
| Forks | 5,091 |
| Issues | 1,179 |
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
| Stars | 51,046 |
| 语言 | Go |
| Forks | 21,917 |
| Issues | 400 |
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
| Stars | 49,480 |
| 语言 | Go |
| Forks | 7,942 |
| Issues | 563 |
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
| Stars | 132,340 |
| 语言 | Unknown |
| Forks | 13,479 |
| Issues | 90 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 221,116 |
| 语言 | Python |
| Forks | 50,637 |
| Issues | 974 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,868 |
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
| Stars | 77,743 |
| 语言 | Python |
| Forks | 16,967 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 108,872 |
| 语言 | TypeScript |
| Forks | 13,396 |
| Issues | 5,039 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,127 |
| 语言 | JavaScript |
| Forks | 26,684 |
| Issues | 159 |
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
| Stars | 71,220 |
| 语言 | JavaScript |
| Forks | 16,802 |
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
| Stars | 68,452 |
| 语言 | JavaScript |
| Forks | 4,608 |
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
| Stars | 67,418 |
| 语言 | JavaScript |
| Forks | 11,949 |
| Issues | 564 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,228 |
| 语言 | JavaScript |
| Forks | 7,164 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,051 |
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
| Stars | 46,847 |
| 语言 | Go |
| Forks | 8,853 |
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
| Stars | 46,392 |
| 语言 | Go |
| Forks | 3,825 |
| Issues | 85 |
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
| Stars | 157,183 |
| 语言 | Python |
| Forks | 11,983 |
| Issues | 372 |
| Topics | awesome, github, hellogithub, python |
