# 项目发现报告 (2026-04-25)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
| 去重移除 | 32 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 23 |
| 🧠 机器学习框架 | 9 |
| 🛠️ 开发工具 | 14 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 66 |

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


## 🤖 AI Agents (29 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,082 |
| 语言 | Python |
| Forks | 19,040 |
| Issues | 258 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最成熟的开源 AI Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供完整的 RAG 和 MCP 支持，且完全支持自托管，在保证数据隐私的同时提供了媲美商业产品的用户体验。超过 13 万的 Stars 和活跃的社区使其成为企业和个人部署私有 AI 助手的首选。

**技术亮点**:
- 多后端兼容: 原生支持 Ollama 和 OpenAI API，可扩展支持各类 LLM 提供商，实现统一的接口管理
- RAG 检索增强生成: 内置文档检索和向量化能力，支持知识库构建，提升 LLM 的知识准确性和实时性
- MCP 协议支持: 支持 Model Context Protocol，可连接外部工具和服务，扩展 AI 能力边界
- 完全自托管: 支持本地部署，数据完全私有，适合对数据安全有严格要求的组织
- 现代化的 Web UI: 提供直观的响应式界面，支持多语言、本地化，开箱即用的用户体验

**适用场景**:
- 企业私有 AI 助手: 在企业内部部署私有 LLM 服务，用于客服、知识管理、文档处理等场景，数据不出内网
- 开发者本地 AI 开发: 开发者和研究人员可在本地快速搭建 AI 实验环境，支持调试和迭代
- 个人隐私保护场景: 对隐私敏感的用户可在本地部署 AI 助手，所有对话和文档处理均在本地完成



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,565 |
| 语言 | Python |
| Forks | 17,180 |
| Issues | 6,991 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源组织 NousResearch 打造的高星标 AI Agent 框架，拥有 11.6 万+ Stars 的社区认可度，支持 Anthropic、OpenAI 等主流 LLM 提供商，可快速构建智能代理应用，适合需要灵活扩展的企业级 AI 开发。

**技术亮点**:
- 支持多 LLM 提供商集成：原生支持 Anthropic Claude、OpenAI GPT 等主流大语言模型，提供统一接口
- 基于 Python 的现代化架构：易于集成和扩展，拥有活跃的社区生态
- 强调 Agent 成长能力：框架设计支持 Agent 在使用过程中持续学习和适应
- 完整的工具调用能力：支持工具/插件系统，方便构建复杂的多步骤任务
- 丰富的 Topic 生态：涵盖 AI Agent、代码执行、多模态等关键领域

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、自动化工作流、智能文档处理等商业应用
- 个人开发者快速原型：利用成熟框架快速验证 AI Agent 概念，缩短开发周期
- 多模型对比与集成：在同一应用中灵活切换不同 LLM 提供商，优化成本和性能
- 复杂任务自动化：利用 Agent 的规划能力和工具调用，实现多步骤复杂任务的自动化执行



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,873 |
| 语言 | JavaScript |
| Forks | 25,881 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个为 Claude Code、Cursor 等主流 AI 代码助手提供性能优化和功能扩展的统一框架，拥有超过 16 万 Stars 的社区认可度，是目前最受欢迎的 AI Agent 开发工具之一。

**技术亮点**:
- 创新的 Skills（技能）+ Instincts（本能）双层架构：允许开发者定义可复用的技能模式和本能反应机制，大幅提升 AI Agent 的响应效率和准确性
- 内置 Memory（记忆）管理系统：为 AI 对话提供持久化上下文记忆能力，解决长会话中的信息遗忘问题
- Security First 安全设计：在 AI Agent 执行敏感操作前提供多层安全防护和权限控制机制
- MCP（Model Context Protocol）协议支持：标准化的上下文协议实现，确保与多种 AI 模型的良好兼容性
- Research-First 开发方法论：融入研究驱动的开发理念，强调在真实场景中验证和迭代 AI Agent 行为

**适用场景**:
- 企业级 AI 代码助手定制：团队可基于此框架构建符合内部开发规范的 AI 编程助手，统一代码风格和安全策略
- 个人开发者效率提升：为 AI 代码助手添加自定义技能、工作流程和上下文记忆，打造个人专属的智能编程伙伴
- AI Agent 研究与实验：研究者可在此框架上快速原型验证新的 Agent 策略、记忆机制和安全方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,822 |
| 语言 | Go |
| Forks | 4,017 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 部署方案，一站式支持文本、图像、音频、视频等多模态模型的本地运行，45k+ Stars 证明其成熟度和社区认可度，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态统一推理引擎：同时支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、TTS、目标检测等多种模型类型，通过统一 API 对外提供服务
- CPU 优先架构：无需 GPU 即可运行各类模型，大幅降低 AI 部署门槛，支持从树莓派到服务器的广泛硬件范围
- 去中心化分布式部署：集成 libp2p 协议支持点对点网络，可构建分布式 AI 服务网络，实现负载均衡和容错
- 丰富的模型兼容性：支持 GGUF、GGML 等量化格式，以及 OpenAI 兼容 API 接口，方便迁移现有应用
- 即插即用的 MCP 支持：集成 Model Context Protocol，可快速接入 AI Agents 和工具生态

**适用场景**:
- 企业级本地 AI 部署：适用于金融、医疗、法律等对数据隐私要求严格的行业，在本地环境运行 AI 应用避免数据外传，同时支持私有化部署满足合规要求
- 个人开发者快速原型开发：开发者无需昂贵的 GPU 资源即可体验和测试各类开源模型，配合 Docker 可在几分钟内完成部署，支持本地调试和迭代
- 去中心化 AI 应用：利用 libp2p 分布式网络构建边缘 AI 服务，适用于物联网边缘计算、社区自建 AI 服务等去中心化场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,641 |
| 语言 | TypeScript |
| Forks | 14,990 |
| Issues | 729 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最成熟的开源 Agent 协作平台之一，提供了完整的 Agent 开发、部署和协作能力，支持 MCP 协议和多模型集成，特别适合需要构建多 Agent 系统的团队。

**技术亮点**:
- 支持 MCP (Model Context Protocol) 协议，实现标准化的 Agent 工具扩展能力
- 多模型支持：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 提供完整的多 Agent 协作框架，支持 Agent 间的任务分配与协作
- 基于 TypeScript/React 的现代化技术栈，具备良好的可扩展性和类型安全
- 内置知识库功能，支持 Agent 的长期记忆和上下文管理

**适用场景**:
- 企业级 AI 应用开发：使用 LobeHub 构建多 Agent 协作的工作流自动化系统
- AI 产品快速原型：快速搭建和测试新的 Agent 概念和产品形态
- 团队协作与知识管理：构建共享的 Agent 团队，实现跨部门的 AI 能力复用



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,603 |
| 语言 | Python |
| Forks | 8,630 |
| Issues | 995 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的统一大模型微调框架，支持 100+ 主流 LLMs 和 VLMs 的高效微调，提供从数据处理到模型部署的完整闭环，让研究者和开发者能够以极低门槛快速适配 LLaMA、Qwen、DeepSeek、Gemma 等明星模型到特定业务场景。

**技术亮点**:
- 统一的微调框架：集成 LoRA、QLoRA、PeFT 等多种 PEFT 方法，支持全参数微调与高效参数微调的灵活切换
- 广泛模型支持：覆盖 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及视觉语言模型(VLMs)
- 完整的 RLHF 流程支持：内置 SFT、RLHF、DPO、ORPO 等训练范式，覆盖监督微调到强化学习全链路
- 推理优化与部署：支持 INT4/INT8 量化、MoE 架构加速，提供一键导出部署能力，降低生产环境门槛
- 工程化完善：提供可视化训练界面、实验记录管理、断点续训等企业级功能

**适用场景**:
- 企业场景：快速将开源大模型适配到垂直领域（如金融、医疗、法律），构建私有化部署的领域专属 AI 助手
- 学术研究：便捷对比不同模型架构（MoE vs 密集模型）、不同微调方法（LoRA vs RLHF）的效果差异，加速论文实验迭代
- 开发者实践：个人开发者可利用 QLoRA 在消费级 GPU（24GB显存）上微调 70B 参数规模模型，降低大模型定制化门槛



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,392 |
| 语言 | TypeScript |
| Forks | 5,736 |
| Issues | 111 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 为 Claude Code 提供长期记忆能力，通过 AI 自动压缩编码上下文并在后续会话中智能注入，解决了大模型上下文窗口限制导致的"记忆丧失"问题，非常适合长期项目的持续开发。

**技术亮点**:
- 智能上下文压缩：集成 Claude agent-sdk，利用 AI 能力自动压缩历史会话内容，提取关键信息并丢弃冗余细节
- RAG + 向量检索：采用 ChromaDB 和嵌入技术构建记忆检索系统，支持语义相似度搜索，精确定位相关历史上下文
- 混合存储架构：结合 SQLite 本地存储与向量数据库，兼顾数据持久化和高效语义查询
- 插件化设计：作为 Claude Code 原生插件运行，无缝集成开发工作流，开箱即用
- 记忆生命周期管理：提供上下文注入 API，支持选择性召回记忆，实现精准的上下文增强

**适用场景**:
- 长期项目开发：维护大型代码库的架构上下文，让 AI 记住模块依赖、设计模式和历史决策，适合企业级应用或开源项目长期维护
- 个人开发者效率提升：为频繁切换项目的开发者提供连续记忆，避免每次会话都要重新解释项目背景和代码规范
- 知识密集型编码：涉及复杂业务逻辑、多框架集成的项目，通过记忆系统保留调试经验、重构记录和测试策略等有价值上下文



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,008 |
| 语言 | HTML |
| Forks | 4,740 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个拥有 48k+ Stars 的 Claude Code 官方推荐最佳实践项目，汇集了 AI 辅助编程的核心方法论，从 vibe coding 到 agentic engineering 的完整进阶路径，适合希望深度掌握 Claude Code 的开发者

**技术亮点**:
- 覆盖从 Vibe Coding 到 Agentic Engineering 的完整学习路径，帮助开发者从初学者进阶为 AI 编程专家
- 深度涵盖 Context Engineering 最佳实践，优化与 AI 模型的交互效果
- 提供大量实用的 Claude Code 命令和技巧，提升开发效率
- 包含 Agentic Workflow 和 Agentic AI 的工程实践指南
- 持续更新的 Claude Code 最新功能和命令参考手册

**适用场景**:
- 个人开发者学习 AI 辅助编程工具的最佳入门和进阶指南
- 团队建立 AI 编程规范和最佳实践的参考标准
- 企业培训开发者使用 Claude Code 提升研发效率



### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,710 |
| 语言 | Python |
| Forks | 9,990 |
| Issues | 355 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,981 |
| 语言 | Java |
| Forks | 15,948 |
| Issues | 14 |
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
| Stars | 40,602 |
| 语言 | Python |
| Forks | 4,868 |
| Issues | 101 |
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
| Stars | 39,052 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 71 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,195 |
| 语言 | TypeScript |
| Forks | 7,152 |
| Issues | 294 |
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
| Stars | 58,980 |
| 语言 | JavaScript |
| Forks | 6,366 |
| Issues | 339 |
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
| Stars | 72,071 |
| 语言 | Python |
| Forks | 9,089 |
| Issues | 410 |
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
| Stars | 54,116 |
| 语言 | TypeScript |
| Forks | 4,393 |
| Issues | 651 |
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
| Stars | 107,462 |
| 语言 | Python |
| Forks | 15,811 |
| Issues | 10 |
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
| Stars | 90,251 |
| 语言 | Python |
| Forks | 10,306 |
| Issues | 226 |
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
| Stars | 52,269 |
| 语言 | TypeScript |
| Forks | 24,214 |
| Issues | 826 |
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
| Stars | 185,575 |
| 语言 | TypeScript |
| Forks | 57,117 |
| Issues | 1,573 |
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
| Stars | 155,211 |
| 语言 | Java |
| Forks | 46,151 |
| Issues | 64 |
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
| Stars | 147,350 |
| 语言 | Python |
| Forks | 8,849 |
| Issues | 955 |
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
| Stars | 59,332 |
| 语言 | Jupyter Notebook |
| Forks | 20,124 |
| Issues | 10 |
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
| Stars | 56,235 |
| 语言 | Python |
| Forks | 6,045 |
| Issues | 558 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,448 |
| 语言 | TypeScript |
| Forks | 9,289 |
| Issues | 108 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,247 |
| 语言 | Python |
| Forks | 2,170 |
| Issues | 99 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,977 |
| 语言 | TypeScript |
| Forks | 3,690 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,312 |
| 语言 | TypeScript |
| Forks | 3,768 |
| Issues | 485 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,289 |
| 语言 | Rust |
| Forks | 3,300 |
| Issues | 590 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


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
| Stars | 134,082 |
| 语言 | Python |
| Forks | 19,040 |
| Issues | 258 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最成熟的开源 AI Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供完整的 RAG 和 MCP 支持，且完全支持自托管，在保证数据隐私的同时提供了媲美商业产品的用户体验。超过 13 万的 Stars 和活跃的社区使其成为企业和个人部署私有 AI 助手的首选。

**技术亮点**:
- 多后端兼容: 原生支持 Ollama 和 OpenAI API，可扩展支持各类 LLM 提供商，实现统一的接口管理
- RAG 检索增强生成: 内置文档检索和向量化能力，支持知识库构建，提升 LLM 的知识准确性和实时性
- MCP 协议支持: 支持 Model Context Protocol，可连接外部工具和服务，扩展 AI 能力边界
- 完全自托管: 支持本地部署，数据完全私有，适合对数据安全有严格要求的组织
- 现代化的 Web UI: 提供直观的响应式界面，支持多语言、本地化，开箱即用的用户体验

**适用场景**:
- 企业私有 AI 助手: 在企业内部部署私有 LLM 服务，用于客服、知识管理、文档处理等场景，数据不出内网
- 开发者本地 AI 开发: 开发者和研究人员可在本地快速搭建 AI 实验环境，支持调试和迭代
- 个人隐私保护场景: 对隐私敏感的用户可在本地部署 AI 助手，所有对话和文档处理均在本地完成



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,641 |
| 语言 | TypeScript |
| Forks | 14,990 |
| Issues | 729 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最成熟的开源 Agent 协作平台之一，提供了完整的 Agent 开发、部署和协作能力，支持 MCP 协议和多模型集成，特别适合需要构建多 Agent 系统的团队。

**技术亮点**:
- 支持 MCP (Model Context Protocol) 协议，实现标准化的 Agent 工具扩展能力
- 多模型支持：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 提供完整的多 Agent 协作框架，支持 Agent 间的任务分配与协作
- 基于 TypeScript/React 的现代化技术栈，具备良好的可扩展性和类型安全
- 内置知识库功能，支持 Agent 的长期记忆和上下文管理

**适用场景**:
- 企业级 AI 应用开发：使用 LobeHub 构建多 Agent 协作的工作流自动化系统
- AI 产品快速原型：快速搭建和测试新的 Agent 概念和产品形态
- 团队协作与知识管理：构建共享的 Agent 团队，实现跨部门的 AI 能力复用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,392 |
| 语言 | TypeScript |
| Forks | 5,736 |
| Issues | 111 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 为 Claude Code 提供长期记忆能力，通过 AI 自动压缩编码上下文并在后续会话中智能注入，解决了大模型上下文窗口限制导致的"记忆丧失"问题，非常适合长期项目的持续开发。

**技术亮点**:
- 智能上下文压缩：集成 Claude agent-sdk，利用 AI 能力自动压缩历史会话内容，提取关键信息并丢弃冗余细节
- RAG + 向量检索：采用 ChromaDB 和嵌入技术构建记忆检索系统，支持语义相似度搜索，精确定位相关历史上下文
- 混合存储架构：结合 SQLite 本地存储与向量数据库，兼顾数据持久化和高效语义查询
- 插件化设计：作为 Claude Code 原生插件运行，无缝集成开发工作流，开箱即用
- 记忆生命周期管理：提供上下文注入 API，支持选择性召回记忆，实现精准的上下文增强

**适用场景**:
- 长期项目开发：维护大型代码库的架构上下文，让 AI 记住模块依赖、设计模式和历史决策，适合企业级应用或开源项目长期维护
- 个人开发者效率提升：为频繁切换项目的开发者提供连续记忆，避免每次会话都要重新解释项目背景和代码规范
- 知识密集型编码：涉及复杂业务逻辑、多框架集成的项目，通过记忆系统保留调试经验、重构记录和测试策略等有价值上下文



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,981 |
| 语言 | Java |
| Forks | 15,948 |
| Issues | 14 |
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
| Stars | 40,602 |
| 语言 | Python |
| Forks | 4,868 |
| Issues | 101 |
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
| Stars | 39,052 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 71 |
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
| Stars | 101,418 |
| 语言 | TypeScript |
| Forks | 12,175 |
| Issues | 954 |
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
| Stars | 58,980 |
| 语言 | JavaScript |
| Forks | 6,366 |
| Issues | 339 |
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
| Stars | 107,462 |
| 语言 | Python |
| Forks | 15,811 |
| Issues | 10 |
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
| Stars | 76,537 |
| 语言 | Python |
| Forks | 10,316 |
| Issues | 242 |
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
| Stars | 52,269 |
| 语言 | TypeScript |
| Forks | 24,214 |
| Issues | 826 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,980 |
| 语言 | Go |
| Forks | 3,977 |
| Issues | 1,093 |
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
| Stars | 34,257 |
| 语言 | Python |
| Forks | 4,841 |
| Issues | 217 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,247 |
| 语言 | Python |
| Forks | 2,170 |
| Issues | 99 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,977 |
| 语言 | TypeScript |
| Forks | 3,690 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (23 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,082 |
| 语言 | Python |
| Forks | 19,040 |
| Issues | 258 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最成熟的开源 AI Web 界面解决方案，支持 Ollama、OpenAI API 等多种后端，提供完整的 RAG 和 MCP 支持，且完全支持自托管，在保证数据隐私的同时提供了媲美商业产品的用户体验。超过 13 万的 Stars 和活跃的社区使其成为企业和个人部署私有 AI 助手的首选。

**技术亮点**:
- 多后端兼容: 原生支持 Ollama 和 OpenAI API，可扩展支持各类 LLM 提供商，实现统一的接口管理
- RAG 检索增强生成: 内置文档检索和向量化能力，支持知识库构建，提升 LLM 的知识准确性和实时性
- MCP 协议支持: 支持 Model Context Protocol，可连接外部工具和服务，扩展 AI 能力边界
- 完全自托管: 支持本地部署，数据完全私有，适合对数据安全有严格要求的组织
- 现代化的 Web UI: 提供直观的响应式界面，支持多语言、本地化，开箱即用的用户体验

**适用场景**:
- 企业私有 AI 助手: 在企业内部部署私有 LLM 服务，用于客服、知识管理、文档处理等场景，数据不出内网
- 开发者本地 AI 开发: 开发者和研究人员可在本地快速搭建 AI 实验环境，支持调试和迭代
- 个人隐私保护场景: 对隐私敏感的用户可在本地部署 AI 助手，所有对话和文档处理均在本地完成



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,565 |
| 语言 | Python |
| Forks | 17,180 |
| Issues | 6,991 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源组织 NousResearch 打造的高星标 AI Agent 框架，拥有 11.6 万+ Stars 的社区认可度，支持 Anthropic、OpenAI 等主流 LLM 提供商，可快速构建智能代理应用，适合需要灵活扩展的企业级 AI 开发。

**技术亮点**:
- 支持多 LLM 提供商集成：原生支持 Anthropic Claude、OpenAI GPT 等主流大语言模型，提供统一接口
- 基于 Python 的现代化架构：易于集成和扩展，拥有活跃的社区生态
- 强调 Agent 成长能力：框架设计支持 Agent 在使用过程中持续学习和适应
- 完整的工具调用能力：支持工具/插件系统，方便构建复杂的多步骤任务
- 丰富的 Topic 生态：涵盖 AI Agent、代码执行、多模态等关键领域

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、自动化工作流、智能文档处理等商业应用
- 个人开发者快速原型：利用成熟框架快速验证 AI Agent 概念，缩短开发周期
- 多模型对比与集成：在同一应用中灵活切换不同 LLM 提供商，优化成本和性能
- 复杂任务自动化：利用 Agent 的规划能力和工具调用，实现多步骤复杂任务的自动化执行



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,873 |
| 语言 | JavaScript |
| Forks | 25,881 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个为 Claude Code、Cursor 等主流 AI 代码助手提供性能优化和功能扩展的统一框架，拥有超过 16 万 Stars 的社区认可度，是目前最受欢迎的 AI Agent 开发工具之一。

**技术亮点**:
- 创新的 Skills（技能）+ Instincts（本能）双层架构：允许开发者定义可复用的技能模式和本能反应机制，大幅提升 AI Agent 的响应效率和准确性
- 内置 Memory（记忆）管理系统：为 AI 对话提供持久化上下文记忆能力，解决长会话中的信息遗忘问题
- Security First 安全设计：在 AI Agent 执行敏感操作前提供多层安全防护和权限控制机制
- MCP（Model Context Protocol）协议支持：标准化的上下文协议实现，确保与多种 AI 模型的良好兼容性
- Research-First 开发方法论：融入研究驱动的开发理念，强调在真实场景中验证和迭代 AI Agent 行为

**适用场景**:
- 企业级 AI 代码助手定制：团队可基于此框架构建符合内部开发规范的 AI 编程助手，统一代码风格和安全策略
- 个人开发者效率提升：为 AI 代码助手添加自定义技能、工作流程和上下文记忆，打造个人专属的智能编程伙伴
- AI Agent 研究与实验：研究者可在此框架上快速原型验证新的 Agent 策略、记忆机制和安全方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,641 |
| 语言 | TypeScript |
| Forks | 14,990 |
| Issues | 729 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最成熟的开源 Agent 协作平台之一，提供了完整的 Agent 开发、部署和协作能力，支持 MCP 协议和多模型集成，特别适合需要构建多 Agent 系统的团队。

**技术亮点**:
- 支持 MCP (Model Context Protocol) 协议，实现标准化的 Agent 工具扩展能力
- 多模型支持：集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 提供完整的多 Agent 协作框架，支持 Agent 间的任务分配与协作
- 基于 TypeScript/React 的现代化技术栈，具备良好的可扩展性和类型安全
- 内置知识库功能，支持 Agent 的长期记忆和上下文管理

**适用场景**:
- 企业级 AI 应用开发：使用 LobeHub 构建多 Agent 协作的工作流自动化系统
- AI 产品快速原型：快速搭建和测试新的 Agent 概念和产品形态
- 团队协作与知识管理：构建共享的 Agent 团队，实现跨部门的 AI 能力复用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,392 |
| 语言 | TypeScript |
| Forks | 5,736 |
| Issues | 111 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 为 Claude Code 提供长期记忆能力，通过 AI 自动压缩编码上下文并在后续会话中智能注入，解决了大模型上下文窗口限制导致的"记忆丧失"问题，非常适合长期项目的持续开发。

**技术亮点**:
- 智能上下文压缩：集成 Claude agent-sdk，利用 AI 能力自动压缩历史会话内容，提取关键信息并丢弃冗余细节
- RAG + 向量检索：采用 ChromaDB 和嵌入技术构建记忆检索系统，支持语义相似度搜索，精确定位相关历史上下文
- 混合存储架构：结合 SQLite 本地存储与向量数据库，兼顾数据持久化和高效语义查询
- 插件化设计：作为 Claude Code 原生插件运行，无缝集成开发工作流，开箱即用
- 记忆生命周期管理：提供上下文注入 API，支持选择性召回记忆，实现精准的上下文增强

**适用场景**:
- 长期项目开发：维护大型代码库的架构上下文，让 AI 记住模块依赖、设计模式和历史决策，适合企业级应用或开源项目长期维护
- 个人开发者效率提升：为频繁切换项目的开发者提供连续记忆，避免每次会话都要重新解释项目背景和代码规范
- 知识密集型编码：涉及复杂业务逻辑、多框架集成的项目，通过记忆系统保留调试经验、重构记录和测试策略等有价值上下文



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,653 |
| 语言 | HTML |
| Forks | 21,012 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万 Stars 的顶级开源 Prompt 工程平台，汇集了社区精选的优质提示词，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署实现完全隐私保护，是个人开发者和企业提升 AI 生产力的必备资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代 Web 技术栈，支持 SSR/SSG 混合渲染模式
- 支持多 LLM 平台集成（OpenAI GPT-4、Claude、Gemini 等），统一提示词格式适配
- 提供完整的自托管部署方案，支持 Docker 一键部署，保障数据隐私
- 采用响应式设计，支持暗色/亮色主题切换，提供优秀的跨设备体验
- 开源社区驱动，支持 GitHub OAuth 登录和社区贡献机制

**适用场景**:
- 企业自建私有 Prompt 知识库，团队内部共享高效提示词模板，提升协作效率
- 个人开发者收藏管理优质 Prompt，构建个人 AI 工具箱，支持分类检索
- 安全敏感行业（金融、医疗、法律）自托管部署，在不泄露数据的前提下使用 AI
- AI 爱好者学习 Prompt Engineering 最佳实践，参考社区高手的提示词设计



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,008 |
| 语言 | HTML |
| Forks | 4,740 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个拥有 48k+ Stars 的 Claude Code 官方推荐最佳实践项目，汇集了 AI 辅助编程的核心方法论，从 vibe coding 到 agentic engineering 的完整进阶路径，适合希望深度掌握 Claude Code 的开发者

**技术亮点**:
- 覆盖从 Vibe Coding 到 Agentic Engineering 的完整学习路径，帮助开发者从初学者进阶为 AI 编程专家
- 深度涵盖 Context Engineering 最佳实践，优化与 AI 模型的交互效果
- 提供大量实用的 Claude Code 命令和技巧，提升开发效率
- 包含 Agentic Workflow 和 Agentic AI 的工程实践指南
- 持续更新的 Claude Code 最新功能和命令参考手册

**适用场景**:
- 个人开发者学习 AI 辅助编程工具的最佳入门和进阶指南
- 团队建立 AI 编程规范和最佳实践的参考标准
- 企业培训开发者使用 Claude Code 提升研发效率



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,410 |
| 语言 | Python |
| Forks | 2,431 |
| Issues | 149 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,710 |
| 语言 | Python |
| Forks | 9,990 |
| Issues | 355 |
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
| Stars | 58,980 |
| 语言 | JavaScript |
| Forks | 6,366 |
| Issues | 339 |
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
| Stars | 72,071 |
| 语言 | Python |
| Forks | 9,089 |
| Issues | 410 |
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
| Stars | 54,116 |
| 语言 | TypeScript |
| Forks | 4,393 |
| Issues | 651 |
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
| Stars | 52,269 |
| 语言 | TypeScript |
| Forks | 24,214 |
| Issues | 826 |
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
| Stars | 78,116 |
| 语言 | Python |
| Forks | 16,071 |
| Issues | 4,460 |
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
| Stars | 147,350 |
| 语言 | Python |
| Forks | 8,849 |
| Issues | 955 |
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
| Stars | 56,235 |
| 语言 | Python |
| Forks | 6,045 |
| Issues | 558 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,986 |
| 语言 | Go |
| Forks | 15,800 |
| Issues | 3,061 |
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
| Stars | 91,420 |
| 语言 | Jupyter Notebook |
| Forks | 14,074 |
| Issues | 5 |
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
| Stars | 56,448 |
| 语言 | TypeScript |
| Forks | 9,289 |
| Issues | 108 |
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
| Stars | 48,150 |
| 语言 | Rust |
| Forks | 9,631 |
| Issues | 2 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,247 |
| 语言 | Python |
| Forks | 2,170 |
| Issues | 99 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,906 |
| 语言 | Python |
| Forks | 7,660 |
| Issues | 639 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,424 |
| 语言 | Python |
| Forks | 7,216 |
| Issues | 123 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


## 🧠 机器学习框架 (9 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,603 |
| 语言 | Python |
| Forks | 8,630 |
| Issues | 995 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的统一大模型微调框架，支持 100+ 主流 LLMs 和 VLMs 的高效微调，提供从数据处理到模型部署的完整闭环，让研究者和开发者能够以极低门槛快速适配 LLaMA、Qwen、DeepSeek、Gemma 等明星模型到特定业务场景。

**技术亮点**:
- 统一的微调框架：集成 LoRA、QLoRA、PeFT 等多种 PEFT 方法，支持全参数微调与高效参数微调的灵活切换
- 广泛模型支持：覆盖 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及视觉语言模型(VLMs)
- 完整的 RLHF 流程支持：内置 SFT、RLHF、DPO、ORPO 等训练范式，覆盖监督微调到强化学习全链路
- 推理优化与部署：支持 INT4/INT8 量化、MoE 架构加速，提供一键导出部署能力，降低生产环境门槛
- 工程化完善：提供可视化训练界面、实验记录管理、断点续训等企业级功能

**适用场景**:
- 企业场景：快速将开源大模型适配到垂直领域（如金融、医疗、法律），构建私有化部署的领域专属 AI 助手
- 学术研究：便捷对比不同模型架构（MoE vs 密集模型）、不同微调方法（LoRA vs RLHF）的效果差异，加速论文实验迭代
- 开发者实践：个人开发者可利用 QLoRA 在消费级 GPU（24GB显存）上微调 70B 参数规模模型，降低大模型定制化门槛



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,498 |
| 语言 | Python |
| Forks | 6,641 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个成熟的开源金融数据平台，拥有 66K+ Stars 和活跃的社区支持，提供从数据获取到分析的一站式解决方案，特别适合需要快速构建量化交易系统和 AI 投研应用的开发者。

**技术亮点**:
- 统一的数据 API 接口：提供标准化的方式访问股票、加密货币、期权、固收等多种金融数据源
- AI/机器学习原生支持：内置 ML 集成能力，支持构建智能投研和量化分析系统
- 模块化架构设计：采用插件化设计，数据源和处理模块可独立扩展和替换
- 丰富的量化分析工具：内置技术指标、衍生品分析、固定收益计算等专业功能
- 支持 AI Agent 集成：专为 AI 代理设计的接口，便于构建自动化交易和研究工作流

**适用场景**:
- 量化交易系统开发：构建算法交易策略、回测框架和实盘交易系统
- 投研分析平台：集成到现有投研流程，实现自动化数据收集和初步分析
- AI 金融应用开发：作为数据层，为 AI Agent 或大模型应用提供金融数据能力



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,653 |
| 语言 | HTML |
| Forks | 21,012 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万 Stars 的顶级开源 Prompt 工程平台，汇集了社区精选的优质提示词，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署实现完全隐私保护，是个人开发者和企业提升 AI 生产力的必备资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代 Web 技术栈，支持 SSR/SSG 混合渲染模式
- 支持多 LLM 平台集成（OpenAI GPT-4、Claude、Gemini 等），统一提示词格式适配
- 提供完整的自托管部署方案，支持 Docker 一键部署，保障数据隐私
- 采用响应式设计，支持暗色/亮色主题切换，提供优秀的跨设备体验
- 开源社区驱动，支持 GitHub OAuth 登录和社区贡献机制

**适用场景**:
- 企业自建私有 Prompt 知识库，团队内部共享高效提示词模板，提升协作效率
- 个人开发者收藏管理优质 Prompt，构建个人 AI 工具箱，支持分类检索
- 安全敏感行业（金融、医疗、法律）自托管部署，在不泄露数据的前提下使用 AI
- AI 爱好者学习 Prompt Engineering 最佳实践，参考社区高手的提示词设计



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,922 |
| 语言 | Python |
| Forks | 33,012 |
| Issues | 2,357 |
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
| Stars | 78,116 |
| 语言 | Python |
| Forks | 16,071 |
| Issues | 4,460 |
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
| Stars | 110,057 |
| 语言 | Python |
| Forks | 12,832 |
| Issues | 3,982 |
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
| Stars | 99,435 |
| 语言 | Python |
| Forks | 27,593 |
| Issues | 18,574 |
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
| Stars | 91,420 |
| 语言 | Jupyter Notebook |
| Forks | 14,074 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,977 |
| 语言 | TypeScript |
| Forks | 3,690 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 🛠️ 开发工具 (14 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,873 |
| 语言 | JavaScript |
| Forks | 25,881 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个为 Claude Code、Cursor 等主流 AI 代码助手提供性能优化和功能扩展的统一框架，拥有超过 16 万 Stars 的社区认可度，是目前最受欢迎的 AI Agent 开发工具之一。

**技术亮点**:
- 创新的 Skills（技能）+ Instincts（本能）双层架构：允许开发者定义可复用的技能模式和本能反应机制，大幅提升 AI Agent 的响应效率和准确性
- 内置 Memory（记忆）管理系统：为 AI 对话提供持久化上下文记忆能力，解决长会话中的信息遗忘问题
- Security First 安全设计：在 AI Agent 执行敏感操作前提供多层安全防护和权限控制机制
- MCP（Model Context Protocol）协议支持：标准化的上下文协议实现，确保与多种 AI 模型的良好兼容性
- Research-First 开发方法论：融入研究驱动的开发理念，强调在真实场景中验证和迭代 AI Agent 行为

**适用场景**:
- 企业级 AI 代码助手定制：团队可基于此框架构建符合内部开发规范的 AI 编程助手，统一代码风格和安全策略
- 个人开发者效率提升：为 AI 代码助手添加自定义技能、工作流程和上下文记忆，打造个人专属的智能编程伙伴
- AI Agent 研究与实验：研究者可在此框架上快速原型验证新的 Agent 策略、记忆机制和安全方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,822 |
| 语言 | Go |
| Forks | 4,017 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 部署方案，一站式支持文本、图像、音频、视频等多模态模型的本地运行，45k+ Stars 证明其成熟度和社区认可度，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态统一推理引擎：同时支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、TTS、目标检测等多种模型类型，通过统一 API 对外提供服务
- CPU 优先架构：无需 GPU 即可运行各类模型，大幅降低 AI 部署门槛，支持从树莓派到服务器的广泛硬件范围
- 去中心化分布式部署：集成 libp2p 协议支持点对点网络，可构建分布式 AI 服务网络，实现负载均衡和容错
- 丰富的模型兼容性：支持 GGUF、GGML 等量化格式，以及 OpenAI 兼容 API 接口，方便迁移现有应用
- 即插即用的 MCP 支持：集成 Model Context Protocol，可快速接入 AI Agents 和工具生态

**适用场景**:
- 企业级本地 AI 部署：适用于金融、医疗、法律等对数据隐私要求严格的行业，在本地环境运行 AI 应用避免数据外传，同时支持私有化部署满足合规要求
- 个人开发者快速原型开发：开发者无需昂贵的 GPU 资源即可体验和测试各类开源模型，配合 Docker 可在几分钟内完成部署，支持本地调试和迭代
- 去中心化 AI 应用：利用 libp2p 分布式网络构建边缘 AI 服务，适用于物联网边缘计算、社区自建 AI 服务等去中心化场景



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,981 |
| 语言 | Java |
| Forks | 15,948 |
| Issues | 14 |
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
| Stars | 72,071 |
| 语言 | Python |
| Forks | 9,089 |
| Issues | 410 |
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
| Stars | 54,116 |
| 语言 | TypeScript |
| Forks | 4,393 |
| Issues | 651 |
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
| Stars | 185,575 |
| 语言 | TypeScript |
| Forks | 57,117 |
| Issues | 1,573 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,566 |
| 语言 | Python |
| Forks | 13,120 |
| Issues | 2,487 |
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
| Stars | 97,642 |
| 语言 | Python |
| Forks | 9,155 |
| Issues | 172 |
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
| Stars | 81,918 |
| 语言 | Python |
| Forks | 9,537 |
| Issues | 259 |
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
| Stars | 184,254 |
| 语言 | TypeScript |
| Forks | 39,425 |
| Issues | 16,660 |
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
| Stars | 94,194 |
| 语言 | TypeScript |
| Forks | 9,409 |
| Issues | 307 |
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
| Stars | 79,030 |
| 语言 | TypeScript |
| Forks | 5,828 |
| Issues | 778 |
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
| Stars | 79,780 |
| 语言 | Go |
| Forks | 2,789 |
| Issues | 312 |
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
| Stars | 77,022 |
| 语言 | Go |
| Forks | 2,788 |
| Issues | 960 |
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
| Stars | 54,116 |
| 语言 | TypeScript |
| Forks | 4,393 |
| Issues | 651 |
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
| Stars | 185,575 |
| 语言 | TypeScript |
| Forks | 57,117 |
| Issues | 1,573 |
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
| Stars | 56,235 |
| 语言 | Python |
| Forks | 6,045 |
| Issues | 558 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,638 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 234 |
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
| Stars | 121,920 |
| 语言 | Go |
| Forks | 42,917 |
| Issues | 2,677 |
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
| Stars | 71,490 |
| 语言 | Go |
| Forks | 18,920 |
| Issues | 3,806 |
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
| Stars | 55,103 |
| 语言 | Go |
| Forks | 6,615 |
| Issues | 2,764 |
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
| Stars | 47,495 |
| 语言 | Go |
| Forks | 5,048 |
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
| Stars | 94,194 |
| 语言 | TypeScript |
| Forks | 9,409 |
| Issues | 307 |
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
| Stars | 77,808 |
| 语言 | TypeScript |
| Forks | 6,794 |
| Issues | 413 |
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
| Stars | 85,896 |
| 语言 | JavaScript |
| Forks | 7,727 |
| Issues | 729 |
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
| Stars | 70,031 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 321 |
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
| Stars | 62,870 |
| 语言 | Go |
| Forks | 5,940 |
| Issues | 773 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,800 |
| 语言 | Go |
| Forks | 7,412 |
| Issues | 82 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


### usememos/memos

**描述**: Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,173 |
| 语言 | Go |
| Forks | 4,301 |
| Issues | 26 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


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
| Stars | 85,896 |
| 语言 | JavaScript |
| Forks | 7,727 |
| Issues | 729 |
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
| Stars | 63,775 |
| 语言 | Go |
| Forks | 10,360 |
| Issues | 752 |
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
| Stars | 45,822 |
| 语言 | Go |
| Forks | 4,017 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 部署方案，一站式支持文本、图像、音频、视频等多模态模型的本地运行，45k+ Stars 证明其成熟度和社区认可度，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态统一推理引擎：同时支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、音频/音乐生成（MusicGen）、TTS、目标检测等多种模型类型，通过统一 API 对外提供服务
- CPU 优先架构：无需 GPU 即可运行各类模型，大幅降低 AI 部署门槛，支持从树莓派到服务器的广泛硬件范围
- 去中心化分布式部署：集成 libp2p 协议支持点对点网络，可构建分布式 AI 服务网络，实现负载均衡和容错
- 丰富的模型兼容性：支持 GGUF、GGML 等量化格式，以及 OpenAI 兼容 API 接口，方便迁移现有应用
- 即插即用的 MCP 支持：集成 Model Context Protocol，可快速接入 AI Agents 和工具生态

**适用场景**:
- 企业级本地 AI 部署：适用于金融、医疗、法律等对数据隐私要求严格的行业，在本地环境运行 AI 应用避免数据外传，同时支持私有化部署满足合规要求
- 个人开发者快速原型开发：开发者无需昂贵的 GPU 资源即可体验和测试各类开源模型，配合 Docker 可在几分钟内完成部署，支持本地调试和迭代
- 去中心化 AI 应用：利用 libp2p 分布式网络构建边缘 AI 服务，适用于物联网边缘计算、社区自建 AI 服务等去中心化场景



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,642 |
| 语言 | Python |
| Forks | 9,155 |
| Issues | 172 |
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
| Stars | 87,333 |
| 语言 | Python |
| Forks | 33,832 |
| Issues | 434 |
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
| Stars | 100,055 |
| 语言 | TypeScript |
| Forks | 27,186 |
| Issues | 1,128 |
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
| Stars | 79,030 |
| 语言 | TypeScript |
| Forks | 5,828 |
| Issues | 778 |
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
| Stars | 68,977 |
| 语言 | JavaScript |
| Forks | 23,174 |
| Issues | 208 |
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
| Stars | 55,955 |
| 语言 | JavaScript |
| Forks | 10,211 |
| Issues | 367 |
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
| Stars | 51,826 |
| 语言 | JavaScript |
| Forks | 4,707 |
| Issues | 1,468 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,378 |
| 语言 | Go |
| Forks | 8,583 |
| Issues | 679 |
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
| Stars | 71,834 |
| 语言 | Go |
| Forks | 4,704 |
| Issues | 241 |
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
| Stars | 57,957 |
| 语言 | Go |
| Forks | 3,330 |
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
| Stars | 101,418 |
| 语言 | TypeScript |
| Forks | 12,175 |
| Issues | 954 |
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
| Stars | 58,980 |
| 语言 | JavaScript |
| Forks | 6,366 |
| Issues | 339 |
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
| Stars | 43,980 |
| 语言 | Go |
| Forks | 3,977 |
| Issues | 1,093 |
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
| Stars | 51,638 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 234 |
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
| Stars | 160,653 |
| 语言 | HTML |
| Forks | 21,012 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万 Stars 的顶级开源 Prompt 工程平台，汇集了社区精选的优质提示词，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署实现完全隐私保护，是个人开发者和企业提升 AI 生产力的必备资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代 Web 技术栈，支持 SSR/SSG 混合渲染模式
- 支持多 LLM 平台集成（OpenAI GPT-4、Claude、Gemini 等），统一提示词格式适配
- 提供完整的自托管部署方案，支持 Docker 一键部署，保障数据隐私
- 采用响应式设计，支持暗色/亮色主题切换，提供优秀的跨设备体验
- 开源社区驱动，支持 GitHub OAuth 登录和社区贡献机制

**适用场景**:
- 企业自建私有 Prompt 知识库，团队内部共享高效提示词模板，提升协作效率
- 个人开发者收藏管理优质 Prompt，构建个人 AI 工具箱，支持分类检索
- 安全敏感行业（金融、医疗、法律）自托管部署，在不泄露数据的前提下使用 AI
- AI 爱好者学习 Prompt Engineering 最佳实践，参考社区高手的提示词设计



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,410 |
| 语言 | Python |
| Forks | 2,431 |
| Issues | 149 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,602 |
| 语言 | Python |
| Forks | 4,868 |
| Issues | 101 |
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
| Stars | 56,448 |
| 语言 | TypeScript |
| Forks | 9,289 |
| Issues | 108 |
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
| Stars | 89,796 |
| 语言 | TypeScript |
| Forks | 10,029 |
| Issues | 2,264 |
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
| Stars | 87,632 |
| 语言 | TypeScript |
| Forks | 8,907 |
| Issues | 1,635 |
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
| Stars | 127,575 |
| 语言 | JavaScript |
| Forks | 12,479 |
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
| Stars | 170,981 |
| 语言 | Go |
| Forks | 13,174 |
| Issues | 180 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (66 个项目) { #其他 }


### 🌟 高优先级


### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,993 |
| 语言 | Python |
| Forks | 8,939 |
| Issues | 2,983 |
| Topics | llm-app |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,288 |
| 语言 | Python |
| Forks | 13,403 |
| Issues | 108 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
| 许可证 | GNU Affero General Public License v3.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,841 |
| 语言 | Python |
| Forks | 7,839 |
| Issues | 629 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 136,076 |
| 语言 | Unknown |
| Forks | 34,065 |
| Issues | 137 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 386,029 |
| 语言 | Python |
| Forks | 66,126 |
| Issues | 75 |
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
| Stars | 115,142 |
| 语言 | TypeScript |
| Forks | 6,001 |
| Issues | 38 |
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
| Stars | 113,428 |
| 语言 | TypeScript |
| Forks | 8,291 |
| Issues | 302 |
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
| Stars | 83,191 |
| 语言 | TypeScript |
| Forks | 12,121 |
| Issues | 448 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,313 |
| 语言 | JavaScript |
| Forks | 4,858 |
| Issues | 33 |
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
| Stars | 48,251 |
| 语言 | Go |
| Forks | 10,327 |
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
| Stars | 106,526 |
| 语言 | C++ |
| Forks | 17,356 |
| Issues | 1,540 |
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
| Stars | 63,408 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 28 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,126 |
| 语言 | Unknown |
| Forks | 8,310 |
| Issues | 72 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 294,349 |
| 语言 | Python |
| Forks | 27,773 |
| Issues | 24 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,285 |
| 语言 | Python |
| Forks | 7,244 |
| Issues | 487 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,225 |
| 语言 | Python |
| Forks | 37,343 |
| Issues | 3,797 |
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
| Stars | 77,666 |
| 语言 | Python |
| Forks | 45,116 |
| Issues | 1,280 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,187 |
| 语言 | Python |
| Forks | 16,887 |
| Issues | 26 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 443,545 |
| 语言 | TypeScript |
| Forks | 44,383 |
| Issues | 176 |
| Topics | careers, certification, community, curriculum, d3, education, freecodecamp, javascript, learn-to-code, math, nodejs, nonprofits, programming, react, teachers |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### kamranahmedse/developer-roadmap

**描述**: Interactive roadmaps, guides and other educational content to help developers grow in their careers.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 353,617 |
| 语言 | TypeScript |
| Forks | 43,969 |
| Issues | 10 |
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
| Stars | 121,948 |
| 语言 | TypeScript |
| Forks | 13,428 |
| Issues | 3,010 |
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
| Stars | 112,990 |
| 语言 | TypeScript |
| Forks | 8,637 |
| Issues | 1,845 |
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
| Stars | 108,662 |
| 语言 | TypeScript |
| Forks | 13,368 |
| Issues | 5,031 |
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
| Stars | 98,600 |
| 语言 | TypeScript |
| Forks | 5,478 |
| Issues | 686 |
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
| Stars | 97,841 |
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
| Stars | 94,753 |
| 语言 | TypeScript |
| Forks | 5,211 |
| Issues | 106 |
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
| Stars | 84,520 |
| 语言 | TypeScript |
| Forks | 10,499 |
| Issues | 382 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,216 |
| 语言 | TypeScript |
| Forks | 8,093 |
| Issues | 718 |
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
| Stars | 244,671 |
| 语言 | JavaScript |
| Forks | 50,980 |
| Issues | 1,243 |
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
| Stars | 116,897 |
| 语言 | JavaScript |
| Forks | 35,429 |
| Issues | 2,647 |
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
| Stars | 112,173 |
| 语言 | JavaScript |
| Forks | 36,343 |
| Issues | 517 |
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
| Stars | 109,030 |
| 语言 | JavaScript |
| Forks | 11,653 |
| Issues | 210 |
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
| Stars | 98,231 |
| 语言 | JavaScript |
| Forks | 32,660 |
| Issues | 1,535 |
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
| Stars | 95,672 |
| 语言 | JavaScript |
| Forks | 15,402 |
| Issues | 47 |
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
| Stars | 86,422 |
| 语言 | JavaScript |
| Forks | 4,895 |
| Issues | 997 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,069 |
| 语言 | JavaScript |
| Forks | 16,808 |
| Issues | 894 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,786 |
| 语言 | JavaScript |
| Forks | 9,361 |
| Issues | 207 |
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
| Stars | 62,992 |
| 语言 | JavaScript |
| Forks | 4,025 |
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
| Stars | 61,257 |
| 语言 | JavaScript |
| Forks | 7,149 |
| Issues | 140 |
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
| Stars | 60,686 |
| 语言 | JavaScript |
| Forks | 5,657 |
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
| Stars | 59,839 |
| 语言 | JavaScript |
| Forks | 20,458 |
| Issues | 89 |
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
| Stars | 57,430 |
| 语言 | JavaScript |
| Forks | 12,307 |
| Issues | 26 |
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
| Stars | 53,191 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 451 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,660 |
| 语言 | JavaScript |
| Forks | 11,512 |
| Issues | 245 |
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
| Stars | 133,636 |
| 语言 | Go |
| Forks | 18,951 |
| Issues | 9,974 |
| Topics | go, golang, language, programming-language |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### gohugoio/hugo

**描述**: The world’s fastest framework for building websites.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,771 |
| 语言 | Go |
| Forks | 8,248 |
| Issues | 240 |
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
| Stars | 83,102 |
| 语言 | Go |
| Forks | 5,116 |
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
| Stars | 68,612 |
| 语言 | Go |
| Forks | 3,221 |
| Issues | 16 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,843 |
| 语言 | Go |
| Forks | 5,054 |
| Issues | 1,173 |
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
| Stars | 50,998 |
| 语言 | Go |
| Forks | 21,897 |
| Issues | 416 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,801 |
| 语言 | Go |
| Forks | 1,608 |
| Issues | 272 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,370 |
| 语言 | Go |
| Forks | 7,947 |
| Issues | 564 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,845 |
| 语言 | Go |
| Forks | 8,856 |
| Issues | 17 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,862 |
| 语言 | Shell |
| Forks | 13,963 |
| Issues | 110 |
| 许可证 | MIT License |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,193 |
| 语言 | Python |
| Forks | 50,418 |
| Issues | 929 |
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
| Stars | 98,383 |
| 语言 | Python |
| Forks | 12,098 |
| Issues | 122 |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,023 |
| 语言 | TypeScript |
| Forks | 16,528 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,271 |
| 语言 | TypeScript |
| Forks | 7,599 |
| Issues | 35 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,132 |
| 语言 | JavaScript |
| Forks | 26,712 |
| Issues | 159 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,164 |
| 语言 | JavaScript |
| Forks | 32,635 |
| Issues | 279 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,388 |
| 语言 | JavaScript |
| Forks | 11,956 |
| Issues | 554 |
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
| Stars | 66,341 |
| 语言 | JavaScript |
| Forks | 9,192 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,315 |
| 语言 | JavaScript |
| Forks | 10,352 |
| Issues | 134 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 106,087 |
| 语言 | Go |
| Forks | 15,017 |
| Issues | 38 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,097 |
| 语言 | Go |
| Forks | 3,798 |
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
| Stars | 153,053 |
| 语言 | Python |
| Forks | 11,668 |
| Issues | 346 |
| Topics | awesome, github, hellogithub, python |
