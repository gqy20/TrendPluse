# 项目发现报告 (2026-04-14)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 7 |
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
| Stars | 131,847 |
| 语言 | Python |
| Forks | 18,709 |
| Issues | 252 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种后端，并集成 RAG 和 MCP 等高级功能。超过 13 万的 Stars 证明了其卓越的稳定性和社区认可度，让用户能够零门槛部署私有化 AI 对话系统。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API 等主流 LLM 提供商，提供统一的对话界面
- RAG 检索增强生成：支持知识库问答，可结合本地文档实现精准的知识检索和问答
- MCP 协议支持：支持 Model Control Protocol，实现更灵活的模型调用和扩展
- 自托管部署：完全开源可私有部署，数据自主掌控，满足企业安全合规需求
- OpenAPI 兼容：提供标准化的 API 接口，便于与现有系统集成和二次开发

**适用场景**:
- 企业私有 AI 助手：适合需要数据隐私保护的企业部署内部 AI 对话系统，支持结合内部知识库的智能问答
- 个人开发者 AI 工具：开发者可快速搭建本地 AI 开发助手，支持自定义扩展和 API 集成
- AI 研究与实验：研究人员可灵活切换不同 LLM 后端进行对比实验，验证模型效果



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,829 |
| 语言 | Python |
| Forks | 11,289 |
| Issues | 4,273 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 开发的企业级 AI Agent 框架，支持 OpenAI、Anthropic、Claude 等多平台 LLM 集成，拥有 8.3 万+ Stars 的高人气，具备强大的工具调用和任务自动化能力，是构建智能助手和自动化工作流的可靠选择。

**技术亮点**:
- 多 LLM 提供商支持：统一集成 OpenAI GPT、Anthropic Claude 等主流大语言模型，便于灵活切换和比较不同模型效果
- 基于 Agent 的任务执行框架：支持复杂任务的分解、规划和自动化执行，具备 ReAct/RePlan 等多种推理策略
- 丰富的工具生态：内置代码执行、API 调用、文件操作等多类型工具，支持自定义工具扩展
- MIT 开源许可：完全开源可商用，代码透明便于审计和定制，社区活跃持续迭代
- 模块化架构设计：核心逻辑与工具解耦，方便开发者快速集成到现有系统或自定义 Agent 行为

**适用场景**:
- 企业智能助手：构建支持多模型的 AI 助手，处理客户咨询、数据分析、报告生成等企业级任务
- 开发者自动化工作流：将重复性开发任务（如代码审查、文档生成、测试编写）自动化，提升研发效率
- 个人 AI 生产力工具：集成到个人工作流，实现邮件处理、日程管理、信息检索等日常任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,038 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 3,135 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，配合 GraphRAG 和深度文档理解能力，能构建真正理解复杂上下文的企业级知识问答系统，特别适合处理结构化文档和需要多跳推理的场景。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态规划检索策略，支持多轮对话式推理和复杂任务分解
- 深度文档理解：内置 OCR、表格识别、版式分析等能力，支持 PDF、Word、Excel 等多格式文档的精准解析
- GraphRAG 支持：融合图检索增强生成技术，实现实体关系推理和全局知识关联分析
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek、通义千问等主流大模型，支持 MCP 协议扩展
- 可视化知识库管理：提供 Web 界面实现向量化配置、检索策略调优和效果评估全流程

**适用场景**:
- 企业智能知识库：构建支持复杂文档理解的内部门知识检索系统，如客服助手、技术文档问答、合规审查等场景
- Deep Research 深度研究：利用 Agent + RAG 实现多源信息聚合分析，适用于市场调研、学术文献综述、投资分析等专业领域
- 智能文档处理流水线：自动解析结构化/非结构化文档并建立知识图谱，赋能 RPA 和业务流程自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,931 |
| 语言 | JavaScript |
| Forks | 24,191 |
| Issues | 95 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为AI编码代理打造的性能优化工具集，Stars超15万证明了其在开发者社区的极高认可度。它通过Skills、Instincts、Memory、Security等模块，为Claude Code、Codex、Cursor等主流AI工具提供统一的能力扩展框架。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，实现AI代理与外部工具的无缝连接
- Skills/Instincts 系统：提供可复用的技能库和本能行为模式
- Memory 管理系统：支持AI代理的上下文保持和长期记忆
- Security 安全框架：确保AI代理操作的安全性和权限控制
- 多代理兼容架构：同时支持 Claude Code、Codex、Opencode、Cursor 等主流AI编码工具

**适用场景**:
- 企业级AI开发团队：统一管理多个AI代理的能力扩展和最佳实践
- 个人开发者：快速为AI编码助手添加自定义技能和工作流
- AI代理研究：基于该框架进行LLM代理行为的实验和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,399 |
| 语言 | Go |
| Forks | 3,952 |
| Issues | 165 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型，无需 GPU 且数据完全本地化处理，非常适合隐私敏感场景和希望避免云服务依赖的开发者和企业。

**技术亮点**:
- 使用 Go 语言开发，具备高效的并发处理能力和优秀的跨平台兼容性
- 支持 OpenAI API 兼容接口，可无缝替换现有基于 OpenAI 的应用
- 支持多种模型架构：LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在边缘设备上运行
- Model Context Protocol (MCP) 支持，便于构建 AI Agent 和自动化工作流

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要数据完全本地处理，避免云端传输风险
- 开发者本地测试与原型开发：在本地快速验证 AI 功能，无需支付云服务费用或担心 API 限流
- 边缘计算与物联网：将 AI 能力部署在资源受限的设备上，实现本地推理
- 企业私有化部署：构建完全自主可控的 AI 基础设施，满足合规要求



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,183 |
| 语言 | TypeScript |
| Forks | 14,918 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是功能完善的 AI Agent 平台，支持多智能体协作、Agent 团队设计和 MCP 协议集成，拥有 75k+ Stars 验证了其成熟度和社区认可度，是构建下一代 AI 应用和工作流的优先选择。

**技术亮点**:
- 多智能体协作系统：支持 Multi-Agent Collaboration，实现多个 Agent 之间的无缝协作与任务分配
- 多模型统一接入：兼容 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：集成 Model Context Protocol，实现标准化的大模型上下文管理和工具调用
- Agent 团队设计：提供可视化/低代码方式设计 Agent 团队拓扑，定义角色职责和交互流程
- 知识库集成：内置 Knowledge Base 功能，支持 RAG 增强检索和上下文管理

**适用场景**:
- 企业智能助手搭建：使用多 Agent 协作构建客服、HR 助手、财务助手等垂直领域 AI 应用
- 团队工作流自动化：设计 Agent 团队处理复杂业务流程，如项目管理、数据分析、报告生成等
- AI 应用快速开发：开发者基于现有 Agent 框架快速构建和部署 AI 产品，降低开发成本



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,099 |
| 语言 | Python |
| Forks | 8,571 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的大模型微调框架之一，支持100+主流LLM/VLM的高效微调，通过统一接口整合了LoRA、QLoRA、RLHF等多种微调技术，ACL 2024官方收录，社区活跃度高，是企业级LLM定制和学术研究的最佳选择。

**技术亮点**:
- 统一微调框架：支持LLaMA、Bloom、Qwen、ChatGLM等100+开源模型的LoRA/QLoRA/RLHF微调
- 高效量化技术：集成4bit/8bit量化，结合QLoRA大幅降低显存占用，单卡可微调70B模型
- 多模态支持：统一处理语言模型(LLaM)和视觉语言模型(VLM)的微调流程
- 丰富的训练策略：支持全参数微调、LoRA、Prefix-Tuning、ptune等多种PEFT方法
- ACL 2024论文支撑，项目经过学术验证并持续维护更新

**适用场景**:
- 企业级LLM定制：企业可根据业务需求对开源大模型进行领域适配和垂直场景优化
- 学术研究与实验：研究人员可快速对比不同微调方法（LoRA vs RLHF等）在各模型上的效果
- 个人开发者微调：开发者可在消费级GPU上使用QLoRA对中小模型进行指令微调



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,412 |
| 语言 | TypeScript |
| Forks | 4,446 |
| Issues | 259 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和 AI 压缩技术为 Claude Code 赋予长期记忆能力，解决了 AI 编码助手无法跨会话保持上下文的核心痛点，让开发者能够在长时间项目中保持连续的工作状态和上下文一致性。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，使用 ChromaDB 向量数据库存储和检索记忆嵌入
- 集成 Claude Agent SDK 实现智能上下文压缩，优化记忆存储效率
- 自动捕获和索引所有编码会话活动，支持 SQLite 本地持久化存储
- 采用 Mem0/mem0 记忆引擎，提供成熟的长期记忆管理方案
- 作为 Claude Code 原生插件架构，无缝集成到现有开发工作流

**适用场景**:
- 长时间项目开发：在跨周甚至跨月的项目开发中保持上下文连续性，无需重复解释项目背景和之前的技术决策
- 复杂代码库维护：帮助 AI 理解历史修改意图和架构决策，便于后续的代码优化和重构
- 团队协作场景：在不同开发阶段或人员变动时，保持项目上下文的一致传递



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,307 |
| 语言 | TypeScript |
| Forks | 8,748 |
| Issues | 82 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,178 |
| 语言 | Python |
| Forks | 9,917 |
| Issues | 351 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,507 |
| 语言 | Python |
| Forks | 6,920 |
| Issues | 925 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,842 |
| 语言 | Java |
| Forks | 15,910 |
| Issues | 37 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,980 |
| 语言 | Python |
| Forks | 6,187 |
| Issues | 74 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,449 |
| 语言 | Python |
| Forks | 4,305 |
| Issues | 94 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,740 |
| 语言 | TypeScript |
| Forks | 3,651 |
| Issues | 294 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,513 |
| 语言 | Python |
| Forks | 15,409 |
| Issues | 12 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,029 |
| 语言 | TypeScript |
| Forks | 6,988 |
| Issues | 277 |
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
| Stars | 58,321 |
| 语言 | JavaScript |
| Forks | 6,313 |
| Issues | 327 |
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
| Stars | 71,199 |
| 语言 | Python |
| Forks | 8,946 |
| Issues | 403 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,561 |
| 语言 | TypeScript |
| Forks | 4,138 |
| Issues | 540 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,799 |
| 语言 | Python |
| Forks | 10,093 |
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
| Stars | 51,902 |
| 语言 | TypeScript |
| Forks | 24,138 |
| Issues | 808 |
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
| Stars | 184,038 |
| 语言 | TypeScript |
| Forks | 56,790 |
| Issues | 1,459 |
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
| Stars | 154,949 |
| 语言 | Java |
| Forks | 46,157 |
| Issues | 65 |
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
| Stars | 146,934 |
| 语言 | Python |
| Forks | 8,763 |
| Issues | 949 |
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
| Stars | 56,676 |
| 语言 | Jupyter Notebook |
| Forks | 19,613 |
| Issues | 5 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,070 |
| 语言 | Python |
| Forks | 2,134 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,529 |
| 语言 | Jupyter Notebook |
| Forks | 5,536 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,678 |
| 语言 | Rust |
| Forks | 2,822 |
| Issues | 494 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (17 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 131,847 |
| 语言 | Python |
| Forks | 18,709 |
| Issues | 252 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种后端，并集成 RAG 和 MCP 等高级功能。超过 13 万的 Stars 证明了其卓越的稳定性和社区认可度，让用户能够零门槛部署私有化 AI 对话系统。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API 等主流 LLM 提供商，提供统一的对话界面
- RAG 检索增强生成：支持知识库问答，可结合本地文档实现精准的知识检索和问答
- MCP 协议支持：支持 Model Control Protocol，实现更灵活的模型调用和扩展
- 自托管部署：完全开源可私有部署，数据自主掌控，满足企业安全合规需求
- OpenAPI 兼容：提供标准化的 API 接口，便于与现有系统集成和二次开发

**适用场景**:
- 企业私有 AI 助手：适合需要数据隐私保护的企业部署内部 AI 对话系统，支持结合内部知识库的智能问答
- 个人开发者 AI 工具：开发者可快速搭建本地 AI 开发助手，支持自定义扩展和 API 集成
- AI 研究与实验：研究人员可灵活切换不同 LLM 后端进行对比实验，验证模型效果



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,038 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 3,135 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，配合 GraphRAG 和深度文档理解能力，能构建真正理解复杂上下文的企业级知识问答系统，特别适合处理结构化文档和需要多跳推理的场景。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态规划检索策略，支持多轮对话式推理和复杂任务分解
- 深度文档理解：内置 OCR、表格识别、版式分析等能力，支持 PDF、Word、Excel 等多格式文档的精准解析
- GraphRAG 支持：融合图检索增强生成技术，实现实体关系推理和全局知识关联分析
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek、通义千问等主流大模型，支持 MCP 协议扩展
- 可视化知识库管理：提供 Web 界面实现向量化配置、检索策略调优和效果评估全流程

**适用场景**:
- 企业智能知识库：构建支持复杂文档理解的内部门知识检索系统，如客服助手、技术文档问答、合规审查等场景
- Deep Research 深度研究：利用 Agent + RAG 实现多源信息聚合分析，适用于市场调研、学术文献综述、投资分析等专业领域
- 智能文档处理流水线：自动解析结构化/非结构化文档并建立知识图谱，赋能 RPA 和业务流程自动化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,183 |
| 语言 | TypeScript |
| Forks | 14,918 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是功能完善的 AI Agent 平台，支持多智能体协作、Agent 团队设计和 MCP 协议集成，拥有 75k+ Stars 验证了其成熟度和社区认可度，是构建下一代 AI 应用和工作流的优先选择。

**技术亮点**:
- 多智能体协作系统：支持 Multi-Agent Collaboration，实现多个 Agent 之间的无缝协作与任务分配
- 多模型统一接入：兼容 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：集成 Model Context Protocol，实现标准化的大模型上下文管理和工具调用
- Agent 团队设计：提供可视化/低代码方式设计 Agent 团队拓扑，定义角色职责和交互流程
- 知识库集成：内置 Knowledge Base 功能，支持 RAG 增强检索和上下文管理

**适用场景**:
- 企业智能助手搭建：使用多 Agent 协作构建客服、HR 助手、财务助手等垂直领域 AI 应用
- 团队工作流自动化：设计 Agent 团队处理复杂业务流程，如项目管理、数据分析、报告生成等
- AI 应用快速开发：开发者基于现有 Agent 框架快速构建和部署 AI 产品，降低开发成本



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,412 |
| 语言 | TypeScript |
| Forks | 4,446 |
| Issues | 259 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和 AI 压缩技术为 Claude Code 赋予长期记忆能力，解决了 AI 编码助手无法跨会话保持上下文的核心痛点，让开发者能够在长时间项目中保持连续的工作状态和上下文一致性。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，使用 ChromaDB 向量数据库存储和检索记忆嵌入
- 集成 Claude Agent SDK 实现智能上下文压缩，优化记忆存储效率
- 自动捕获和索引所有编码会话活动，支持 SQLite 本地持久化存储
- 采用 Mem0/mem0 记忆引擎，提供成熟的长期记忆管理方案
- 作为 Claude Code 原生插件架构，无缝集成到现有开发工作流

**适用场景**:
- 长时间项目开发：在跨周甚至跨月的项目开发中保持上下文连续性，无需重复解释项目背景和之前的技术决策
- 复杂代码库维护：帮助 AI 理解历史修改意图和架构决策，便于后续的代码优化和重构
- 团队协作场景：在不同开发阶段或人员变动时，保持项目上下文的一致传递



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,842 |
| 语言 | Java |
| Forks | 15,910 |
| Issues | 37 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,980 |
| 语言 | Python |
| Forks | 6,187 |
| Issues | 74 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,449 |
| 语言 | Python |
| Forks | 4,305 |
| Issues | 94 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,740 |
| 语言 | TypeScript |
| Forks | 3,651 |
| Issues | 294 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,513 |
| 语言 | Python |
| Forks | 15,409 |
| Issues | 12 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,834 |
| 语言 | TypeScript |
| Forks | 12,080 |
| Issues | 973 |
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
| Stars | 58,321 |
| 语言 | JavaScript |
| Forks | 6,313 |
| Issues | 327 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,580 |
| 语言 | Python |
| Forks | 10,236 |
| Issues | 235 |
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
| Stars | 51,902 |
| 语言 | TypeScript |
| Forks | 24,138 |
| Issues | 808 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,799 |
| 语言 | Go |
| Forks | 3,963 |
| Issues | 1,177 |
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
| Stars | 33,217 |
| 语言 | Python |
| Forks | 4,718 |
| Issues | 206 |
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
| Stars | 34,070 |
| 语言 | Python |
| Forks | 2,134 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,529 |
| 语言 | Jupyter Notebook |
| Forks | 5,536 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (24 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 131,847 |
| 语言 | Python |
| Forks | 18,709 |
| Issues | 252 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一款功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种后端，并集成 RAG 和 MCP 等高级功能。超过 13 万的 Stars 证明了其卓越的稳定性和社区认可度，让用户能够零门槛部署私有化 AI 对话系统。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API 等主流 LLM 提供商，提供统一的对话界面
- RAG 检索增强生成：支持知识库问答，可结合本地文档实现精准的知识检索和问答
- MCP 协议支持：支持 Model Control Protocol，实现更灵活的模型调用和扩展
- 自托管部署：完全开源可私有部署，数据自主掌控，满足企业安全合规需求
- OpenAPI 兼容：提供标准化的 API 接口，便于与现有系统集成和二次开发

**适用场景**:
- 企业私有 AI 助手：适合需要数据隐私保护的企业部署内部 AI 对话系统，支持结合内部知识库的智能问答
- 个人开发者 AI 工具：开发者可快速搭建本地 AI 开发助手，支持自定义扩展和 API 集成
- AI 研究与实验：研究人员可灵活切换不同 LLM 后端进行对比实验，验证模型效果



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,829 |
| 语言 | Python |
| Forks | 11,289 |
| Issues | 4,273 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 开发的企业级 AI Agent 框架，支持 OpenAI、Anthropic、Claude 等多平台 LLM 集成，拥有 8.3 万+ Stars 的高人气，具备强大的工具调用和任务自动化能力，是构建智能助手和自动化工作流的可靠选择。

**技术亮点**:
- 多 LLM 提供商支持：统一集成 OpenAI GPT、Anthropic Claude 等主流大语言模型，便于灵活切换和比较不同模型效果
- 基于 Agent 的任务执行框架：支持复杂任务的分解、规划和自动化执行，具备 ReAct/RePlan 等多种推理策略
- 丰富的工具生态：内置代码执行、API 调用、文件操作等多类型工具，支持自定义工具扩展
- MIT 开源许可：完全开源可商用，代码透明便于审计和定制，社区活跃持续迭代
- 模块化架构设计：核心逻辑与工具解耦，方便开发者快速集成到现有系统或自定义 Agent 行为

**适用场景**:
- 企业智能助手：构建支持多模型的 AI 助手，处理客户咨询、数据分析、报告生成等企业级任务
- 开发者自动化工作流：将重复性开发任务（如代码审查、文档生成、测试编写）自动化，提升研发效率
- 个人 AI 生产力工具：集成到个人工作流，实现邮件处理、日程管理、信息检索等日常任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,038 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 3,135 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，配合 GraphRAG 和深度文档理解能力，能构建真正理解复杂上下文的企业级知识问答系统，特别适合处理结构化文档和需要多跳推理的场景。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态规划检索策略，支持多轮对话式推理和复杂任务分解
- 深度文档理解：内置 OCR、表格识别、版式分析等能力，支持 PDF、Word、Excel 等多格式文档的精准解析
- GraphRAG 支持：融合图检索增强生成技术，实现实体关系推理和全局知识关联分析
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek、通义千问等主流大模型，支持 MCP 协议扩展
- 可视化知识库管理：提供 Web 界面实现向量化配置、检索策略调优和效果评估全流程

**适用场景**:
- 企业智能知识库：构建支持复杂文档理解的内部门知识检索系统，如客服助手、技术文档问答、合规审查等场景
- Deep Research 深度研究：利用 Agent + RAG 实现多源信息聚合分析，适用于市场调研、学术文献综述、投资分析等专业领域
- 智能文档处理流水线：自动解析结构化/非结构化文档并建立知识图谱，赋能 RPA 和业务流程自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,931 |
| 语言 | JavaScript |
| Forks | 24,191 |
| Issues | 95 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为AI编码代理打造的性能优化工具集，Stars超15万证明了其在开发者社区的极高认可度。它通过Skills、Instincts、Memory、Security等模块，为Claude Code、Codex、Cursor等主流AI工具提供统一的能力扩展框架。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，实现AI代理与外部工具的无缝连接
- Skills/Instincts 系统：提供可复用的技能库和本能行为模式
- Memory 管理系统：支持AI代理的上下文保持和长期记忆
- Security 安全框架：确保AI代理操作的安全性和权限控制
- 多代理兼容架构：同时支持 Claude Code、Codex、Opencode、Cursor 等主流AI编码工具

**适用场景**:
- 企业级AI开发团队：统一管理多个AI代理的能力扩展和最佳实践
- 个人开发者：快速为AI编码助手添加自定义技能和工作流
- AI代理研究：基于该框架进行LLM代理行为的实验和优化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,183 |
| 语言 | TypeScript |
| Forks | 14,918 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是功能完善的 AI Agent 平台，支持多智能体协作、Agent 团队设计和 MCP 协议集成，拥有 75k+ Stars 验证了其成熟度和社区认可度，是构建下一代 AI 应用和工作流的优先选择。

**技术亮点**:
- 多智能体协作系统：支持 Multi-Agent Collaboration，实现多个 Agent 之间的无缝协作与任务分配
- 多模型统一接入：兼容 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：集成 Model Context Protocol，实现标准化的大模型上下文管理和工具调用
- Agent 团队设计：提供可视化/低代码方式设计 Agent 团队拓扑，定义角色职责和交互流程
- 知识库集成：内置 Knowledge Base 功能，支持 RAG 增强检索和上下文管理

**适用场景**:
- 企业智能助手搭建：使用多 Agent 协作构建客服、HR 助手、财务助手等垂直领域 AI 应用
- 团队工作流自动化：设计 Agent 团队处理复杂业务流程，如项目管理、数据分析、报告生成等
- AI 应用快速开发：开发者基于现有 Agent 框架快速构建和部署 AI 产品，降低开发成本



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,412 |
| 语言 | TypeScript |
| Forks | 4,446 |
| Issues | 259 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和 AI 压缩技术为 Claude Code 赋予长期记忆能力，解决了 AI 编码助手无法跨会话保持上下文的核心痛点，让开发者能够在长时间项目中保持连续的工作状态和上下文一致性。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，使用 ChromaDB 向量数据库存储和检索记忆嵌入
- 集成 Claude Agent SDK 实现智能上下文压缩，优化记忆存储效率
- 自动捕获和索引所有编码会话活动，支持 SQLite 本地持久化存储
- 采用 Mem0/mem0 记忆引擎，提供成熟的长期记忆管理方案
- 作为 Claude Code 原生插件架构，无缝集成到现有开发工作流

**适用场景**:
- 长时间项目开发：在跨周甚至跨月的项目开发中保持上下文连续性，无需重复解释项目背景和之前的技术决策
- 复杂代码库维护：帮助 AI 理解历史修改意图和架构决策，便于后续的代码优化和重构
- 团队协作场景：在不同开发阶段或人员变动时，保持项目上下文的一致传递



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,704 |
| 语言 | HTML |
| Forks | 20,914 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最受欢迎的AI提示词聚合平台之一，拥有超过15万stars的社区验证，支持ChatGPT、Claude、Gemini等多模型，并提供完整的企业级自托管方案，在保护隐私的同时实现团队协作。

**技术亮点**:
- 基于 Next.js + TypeScript 全栈架构，采用现代化的React生态系统和类型安全开发
- 支持多LLM模型集成，包括GPT-4、Claude和Gemini等主流大语言模型
- 提供一键自托管部署方案，支持Docker容器化部署，满足企业级隐私需求
- 社区驱动的提示词收集与审核机制，持续更新高质量prompt资源库
- 响应式Web界面设计，支持多设备访问和使用体验优化

**适用场景**:
- 个人开发者快速查找和复用经过验证的高质量AI提示词，提升开发效率
- 企业团队私有化部署专属提示词平台，完全数据自主可控，适合对数据安全有要求的组织
- AI爱好者探索和学习不同场景下的prompt engineering最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,766 |
| 语言 | Jupyter Notebook |
| Forks | 13,928 |
| Issues | 5 |
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
| Stars | 53,307 |
| 语言 | TypeScript |
| Forks | 8,748 |
| Issues | 82 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,178 |
| 语言 | Python |
| Forks | 9,917 |
| Issues | 351 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,507 |
| 语言 | Python |
| Forks | 6,920 |
| Issues | 925 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,321 |
| 语言 | JavaScript |
| Forks | 6,313 |
| Issues | 327 |
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
| Stars | 71,199 |
| 语言 | Python |
| Forks | 8,946 |
| Issues | 403 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,561 |
| 语言 | TypeScript |
| Forks | 4,138 |
| Issues | 540 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,537 |
| 语言 | HTML |
| Forks | 4,161 |
| Issues | 11 |
| Topics | agentic-engineering, anthropic, best-practices, boris, boris-cherny, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, vibe-coding |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,902 |
| 语言 | TypeScript |
| Forks | 24,138 |
| Issues | 808 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,592 |
| 语言 | Python |
| Forks | 15,574 |
| Issues | 4,237 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,447 |
| 语言 | TypeScript |
| Forks | 4,006 |
| Issues | 1,107 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 146,934 |
| 语言 | Python |
| Forks | 8,763 |
| Issues | 949 |
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
| Stars | 168,985 |
| 语言 | Go |
| Forks | 15,587 |
| Issues | 2,938 |
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
| Stars | 47,767 |
| 语言 | Rust |
| Forks | 9,517 |
| Issues | 1 |
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
| Stars | 34,070 |
| 语言 | Python |
| Forks | 2,134 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 64,927 |
| 语言 | Python |
| Forks | 6,560 |
| Issues | 94 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
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
| Stars | 108,275 |
| 语言 | Python |
| Forks | 6,852 |
| Issues | 594 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (10 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,099 |
| 语言 | Python |
| Forks | 8,571 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的大模型微调框架之一，支持100+主流LLM/VLM的高效微调，通过统一接口整合了LoRA、QLoRA、RLHF等多种微调技术，ACL 2024官方收录，社区活跃度高，是企业级LLM定制和学术研究的最佳选择。

**技术亮点**:
- 统一微调框架：支持LLaMA、Bloom、Qwen、ChatGLM等100+开源模型的LoRA/QLoRA/RLHF微调
- 高效量化技术：集成4bit/8bit量化，结合QLoRA大幅降低显存占用，单卡可微调70B模型
- 多模态支持：统一处理语言模型(LLaM)和视觉语言模型(VLM)的微调流程
- 丰富的训练策略：支持全参数微调、LoRA、Prefix-Tuning、ptune等多种PEFT方法
- ACL 2024论文支撑，项目经过学术验证并持续维护更新

**适用场景**:
- 企业级LLM定制：企业可根据业务需求对开源大模型进行领域适配和垂直场景优化
- 学术研究与实验：研究人员可快速对比不同微调方法（LoRA vs RLHF等）在各模型上的效果
- 个人开发者微调：开发者可在消费级GPU上使用QLoRA对中小模型进行指令微调



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,877 |
| 语言 | Python |
| Forks | 6,554 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是最受欢迎的 Python 金融开源项目之一，通过统一接口整合股票、加密货币、期权等多元金融数据，并内置 AI/ML 支持，是分析师和量化开发者快速构建金融应用的理想基础。

**技术亮点**:
- 统一的数据访问层：提供标准化 API，同时支持 CLI、Python SDK 和 Terminal，覆盖 100+ 数据源
- 全品类金融数据覆盖：涵盖股票、加密货币、期权、期货、固定收益、宏观经济等完整金融生态
- 原生 AI/ML 集成：内置 LangChain 等 AI 框架支持，可构建智能投研助手和自动化分析代理
- 模块化架构设计：数据提取、标准化、终端展示三层分离，便于扩展自定义数据源和功能
- 活跃的社区生态：6.5万+ Stars、持续更新的功能、丰富的文档和教程资源

**适用场景**:
- 量化策略研究与回测：获取历史价格、财务数据、期权链等构建因子模型和回测系统
- 智能投研助手开发：结合 LLM 构建对话式金融分析 Agent，自动完成数据查询和报告生成
- 投资组合监控与分析：实时追踪多资产组合表现，生成风险收益分析报告
- 金融数据管道搭建：作为数据中台整合多源金融数据，供下游应用消费



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,704 |
| 语言 | HTML |
| Forks | 20,914 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最受欢迎的AI提示词聚合平台之一，拥有超过15万stars的社区验证，支持ChatGPT、Claude、Gemini等多模型，并提供完整的企业级自托管方案，在保护隐私的同时实现团队协作。

**技术亮点**:
- 基于 Next.js + TypeScript 全栈架构，采用现代化的React生态系统和类型安全开发
- 支持多LLM模型集成，包括GPT-4、Claude和Gemini等主流大语言模型
- 提供一键自托管部署方案，支持Docker容器化部署，满足企业级隐私需求
- 社区驱动的提示词收集与审核机制，持续更新高质量prompt资源库
- 响应式Web界面设计，支持多设备访问和使用体验优化

**适用场景**:
- 个人开发者快速查找和复用经过验证的高质量AI提示词，提升开发效率
- 企业团队私有化部署专属提示词平台，完全数据自主可控，适合对数据安全有要求的组织
- AI爱好者探索和学习不同场景下的prompt engineering最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,766 |
| 语言 | Jupyter Notebook |
| Forks | 13,928 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,740 |
| 语言 | TypeScript |
| Forks | 3,651 |
| Issues | 294 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,373 |
| 语言 | Python |
| Forks | 32,869 |
| Issues | 2,358 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,592 |
| 语言 | Python |
| Forks | 15,574 |
| Issues | 4,237 |
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
| Stars | 108,780 |
| 语言 | Python |
| Forks | 12,627 |
| Issues | 3,975 |
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
| Stars | 99,123 |
| 语言 | Python |
| Forks | 27,483 |
| Issues | 18,507 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,529 |
| 语言 | Jupyter Notebook |
| Forks | 5,536 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 155,931 |
| 语言 | JavaScript |
| Forks | 24,191 |
| Issues | 95 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为AI编码代理打造的性能优化工具集，Stars超15万证明了其在开发者社区的极高认可度。它通过Skills、Instincts、Memory、Security等模块，为Claude Code、Codex、Cursor等主流AI工具提供统一的能力扩展框架。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，实现AI代理与外部工具的无缝连接
- Skills/Instincts 系统：提供可复用的技能库和本能行为模式
- Memory 管理系统：支持AI代理的上下文保持和长期记忆
- Security 安全框架：确保AI代理操作的安全性和权限控制
- 多代理兼容架构：同时支持 Claude Code、Codex、Opencode、Cursor 等主流AI编码工具

**适用场景**:
- 企业级AI开发团队：统一管理多个AI代理的能力扩展和最佳实践
- 个人开发者：快速为AI编码助手添加自定义技能和工作流
- AI代理研究：基于该框架进行LLM代理行为的实验和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,399 |
| 语言 | Go |
| Forks | 3,952 |
| Issues | 165 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型，无需 GPU 且数据完全本地化处理，非常适合隐私敏感场景和希望避免云服务依赖的开发者和企业。

**技术亮点**:
- 使用 Go 语言开发，具备高效的并发处理能力和优秀的跨平台兼容性
- 支持 OpenAI API 兼容接口，可无缝替换现有基于 OpenAI 的应用
- 支持多种模型架构：LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在边缘设备上运行
- Model Context Protocol (MCP) 支持，便于构建 AI Agent 和自动化工作流

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要数据完全本地处理，避免云端传输风险
- 开发者本地测试与原型开发：在本地快速验证 AI 功能，无需支付云服务费用或担心 API 限流
- 边缘计算与物联网：将 AI 能力部署在资源受限的设备上，实现本地推理
- 企业私有化部署：构建完全自主可控的 AI 基础设施，满足合规要求



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,199 |
| 语言 | Python |
| Forks | 8,946 |
| Issues | 403 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,561 |
| 语言 | TypeScript |
| Forks | 4,138 |
| Issues | 540 |
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
| Stars | 184,038 |
| 语言 | TypeScript |
| Forks | 56,790 |
| Issues | 1,459 |
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
| Stars | 156,852 |
| 语言 | Python |
| Forks | 12,916 |
| Issues | 2,471 |
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
| Stars | 97,197 |
| 语言 | Python |
| Forks | 9,072 |
| Issues | 171 |
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
| Stars | 81,069 |
| 语言 | Python |
| Forks | 9,423 |
| Issues | 254 |
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
| Stars | 183,830 |
| 语言 | TypeScript |
| Forks | 39,186 |
| Issues | 16,430 |
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
| Stars | 94,118 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 299 |
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
| Stars | 78,915 |
| 语言 | TypeScript |
| Forks | 5,797 |
| Issues | 765 |
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
| Stars | 77,109 |
| 语言 | TypeScript |
| Forks | 6,605 |
| Issues | 140 |
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
| Stars | 79,477 |
| 语言 | Go |
| Forks | 2,768 |
| Issues | 314 |
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
| Stars | 76,423 |
| 语言 | Go |
| Forks | 2,754 |
| Issues | 954 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### cli/cli

**描述**: GitHub’s official command line tool

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,821 |
| 语言 | Go |
| Forks | 8,257 |
| Issues | 951 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### charmbracelet/bubbletea

**描述**: A powerful little TUI framework 🏗

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,557 |
| 语言 | Go |
| Forks | 1,191 |
| Issues | 167 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
| 许可证 | MIT License |


### ⭐ 中优先级


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 421,800 |
| 语言 | Python |
| Forks | 45,942 |
| Issues | 1,246 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,579 |
| 语言 | JavaScript |
| Forks | 7,282 |
| Issues | 713 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (13 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,561 |
| 语言 | TypeScript |
| Forks | 4,138 |
| Issues | 540 |
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
| Stars | 184,038 |
| 语言 | TypeScript |
| Forks | 56,790 |
| Issues | 1,459 |
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
| Stars | 51,625 |
| 语言 | Go |
| Forks | 10,317 |
| Issues | 236 |
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
| Stars | 121,709 |
| 语言 | Go |
| Forks | 42,855 |
| Issues | 2,745 |
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
| Stars | 71,493 |
| 语言 | Go |
| Forks | 18,913 |
| Issues | 3,797 |
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
| Stars | 54,898 |
| 语言 | Go |
| Forks | 6,570 |
| Issues | 2,826 |
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
| Stars | 94,118 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 299 |
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
| Stars | 76,741 |
| 语言 | TypeScript |
| Forks | 6,640 |
| Issues | 404 |
| Topics | docker, hacktoberfest, java, pdf, pdf-converter, pdf-editor, pdf-manipulation, pdf-merger, pdf-ocr, pdf-tools, pdf-web-apps, pdfmerger |
| 许可证 | Other |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,248 |
| 语言 | JavaScript |
| Forks | 7,641 |
| Issues | 719 |
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
| Stars | 69,857 |
| 语言 | Go |
| Forks | 1,909 |
| Issues | 320 |
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
| Stars | 62,693 |
| 语言 | Go |
| Forks | 5,912 |
| Issues | 778 |
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
| Stars | 58,861 |
| 语言 | Go |
| Forks | 4,270 |
| Issues | 27 |
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
| Stars | 47,500 |
| 语言 | Go |
| Forks | 5,043 |
| Issues | 980 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
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
| Stars | 85,248 |
| 语言 | JavaScript |
| Forks | 7,641 |
| Issues | 719 |
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
| Stars | 63,587 |
| 语言 | Go |
| Forks | 10,331 |
| Issues | 745 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (14 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,399 |
| 语言 | Go |
| Forks | 3,952 |
| Issues | 165 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型，无需 GPU 且数据完全本地化处理，非常适合隐私敏感场景和希望避免云服务依赖的开发者和企业。

**技术亮点**:
- 使用 Go 语言开发，具备高效的并发处理能力和优秀的跨平台兼容性
- 支持 OpenAI API 兼容接口，可无缝替换现有基于 OpenAI 的应用
- 支持多种模型架构：LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在边缘设备上运行
- Model Context Protocol (MCP) 支持，便于构建 AI Agent 和自动化工作流

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要数据完全本地处理，避免云端传输风险
- 开发者本地测试与原型开发：在本地快速验证 AI 功能，无需支付云服务费用或担心 API 限流
- 边缘计算与物联网：将 AI 能力部署在资源受限的设备上，实现本地推理
- 企业私有化部署：构建完全自主可控的 AI 基础设施，满足合规要求



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,197 |
| 语言 | Python |
| Forks | 9,072 |
| Issues | 171 |
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
| Stars | 87,265 |
| 语言 | Python |
| Forks | 33,810 |
| Issues | 429 |
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
| Stars | 100,054 |
| 语言 | TypeScript |
| Forks | 27,154 |
| Issues | 1,122 |
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
| Stars | 78,915 |
| 语言 | TypeScript |
| Forks | 5,797 |
| Issues | 765 |
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
| Stars | 68,934 |
| 语言 | JavaScript |
| Forks | 23,118 |
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
| Stars | 55,961 |
| 语言 | JavaScript |
| Forks | 10,215 |
| Issues | 361 |
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
| Stars | 51,794 |
| 语言 | JavaScript |
| Forks | 4,701 |
| Issues | 1,470 |
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
| Stars | 88,316 |
| 语言 | Go |
| Forks | 8,571 |
| Issues | 672 |
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
| Stars | 71,536 |
| 语言 | Go |
| Forks | 4,695 |
| Issues | 248 |
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
| Stars | 57,615 |
| 语言 | Go |
| Forks | 3,286 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### charmbracelet/bubbletea

**描述**: A powerful little TUI framework 🏗

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,557 |
| 语言 | Go |
| Forks | 1,191 |
| Issues | 167 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
| 许可证 | MIT License |


### ⭐ 中优先级


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 421,800 |
| 语言 | Python |
| Forks | 45,942 |
| Issues | 1,246 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,579 |
| 语言 | JavaScript |
| Forks | 7,282 |
| Issues | 713 |
| Topics | api, fake, frontend, json, mock, rest, test |
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
| Stars | 100,834 |
| 语言 | TypeScript |
| Forks | 12,080 |
| Issues | 973 |
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
| Stars | 58,321 |
| 语言 | JavaScript |
| Forks | 6,313 |
| Issues | 327 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,799 |
| 语言 | Go |
| Forks | 3,963 |
| Issues | 1,177 |
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
| Stars | 51,625 |
| 语言 | Go |
| Forks | 10,317 |
| Issues | 236 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (7 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,704 |
| 语言 | HTML |
| Forks | 20,914 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最受欢迎的AI提示词聚合平台之一，拥有超过15万stars的社区验证，支持ChatGPT、Claude、Gemini等多模型，并提供完整的企业级自托管方案，在保护隐私的同时实现团队协作。

**技术亮点**:
- 基于 Next.js + TypeScript 全栈架构，采用现代化的React生态系统和类型安全开发
- 支持多LLM模型集成，包括GPT-4、Claude和Gemini等主流大语言模型
- 提供一键自托管部署方案，支持Docker容器化部署，满足企业级隐私需求
- 社区驱动的提示词收集与审核机制，持续更新高质量prompt资源库
- 响应式Web界面设计，支持多设备访问和使用体验优化

**适用场景**:
- 个人开发者快速查找和复用经过验证的高质量AI提示词，提升开发效率
- 企业团队私有化部署专属提示词平台，完全数据自主可控，适合对数据安全有要求的组织
- AI爱好者探索和学习不同场景下的prompt engineering最佳实践



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,307 |
| 语言 | TypeScript |
| Forks | 8,748 |
| Issues | 82 |
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
| Stars | 36,449 |
| 语言 | Python |
| Forks | 4,305 |
| Issues | 94 |
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
| Stars | 89,706 |
| 语言 | TypeScript |
| Forks | 10,003 |
| Issues | 2,227 |
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
| Stars | 87,367 |
| 语言 | TypeScript |
| Forks | 8,868 |
| Issues | 1,648 |
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
| Stars | 127,461 |
| 语言 | JavaScript |
| Forks | 12,477 |
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
| Stars | 169,963 |
| 语言 | Go |
| Forks | 13,140 |
| Issues | 177 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,913 |
| 语言 | Shell |
| Forks | 12,750 |
| Issues | 90 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,985 |
| 语言 | Python |
| Forks | 6,559 |
| Issues | 68 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,552 |
| 语言 | Python |
| Forks | 13,165 |
| Issues | 121 |
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
| Stars | 87,971 |
| 语言 | Python |
| Forks | 7,563 |
| Issues | 630 |
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
| Stars | 135,171 |
| 语言 | Unknown |
| Forks | 33,976 |
| Issues | 145 |
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
| Stars | 385,532 |
| 语言 | Python |
| Forks | 66,106 |
| Issues | 79 |
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
| Stars | 114,597 |
| 语言 | TypeScript |
| Forks | 5,909 |
| Issues | 34 |
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
| Stars | 110,595 |
| 语言 | TypeScript |
| Forks | 8,043 |
| Issues | 263 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,895 |
| 语言 | JavaScript |
| Forks | 4,417 |
| Issues | 43 |
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
| Stars | 48,143 |
| 语言 | Go |
| Forks | 10,287 |
| Issues | 1,886 |
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
| Stars | 103,662 |
| 语言 | C++ |
| Forks | 16,834 |
| Issues | 1,498 |
| Topics | ggml |
| 许可证 | MIT License |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,339 |
| 语言 | TypeScript |
| Forks | 10,197 |
| Issues | 346 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,525 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 292,302 |
| 语言 | Python |
| Forks | 27,672 |
| Issues | 20 |
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
| Stars | 219,602 |
| 语言 | Python |
| Forks | 50,328 |
| Issues | 926 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,747 |
| 语言 | Python |
| Forks | 12,035 |
| Issues | 120 |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,027 |
| 语言 | Python |
| Forks | 37,243 |
| Issues | 3,627 |
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
| Stars | 77,676 |
| 语言 | Python |
| Forks | 45,153 |
| Issues | 1,279 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,890 |
| 语言 | Python |
| Forks | 16,846 |
| Issues | 22 |
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
| Stars | 442,888 |
| 语言 | TypeScript |
| Forks | 44,284 |
| Issues | 207 |
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
| Stars | 352,931 |
| 语言 | TypeScript |
| Forks | 43,917 |
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
| Stars | 121,036 |
| 语言 | TypeScript |
| Forks | 13,270 |
| Issues | 2,966 |
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
| Stars | 112,322 |
| 语言 | TypeScript |
| Forks | 8,520 |
| Issues | 1,812 |
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
| Stars | 108,545 |
| 语言 | TypeScript |
| Forks | 13,348 |
| Issues | 5,023 |
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
| Stars | 97,846 |
| 语言 | TypeScript |
| Forks | 5,380 |
| Issues | 704 |
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
| Stars | 97,765 |
| 语言 | TypeScript |
| Forks | 54,588 |
| Issues | 1,352 |
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
| Stars | 94,566 |
| 语言 | TypeScript |
| Forks | 5,190 |
| Issues | 112 |
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
| Stars | 83,740 |
| 语言 | TypeScript |
| Forks | 10,381 |
| Issues | 565 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,102 |
| 语言 | TypeScript |
| Forks | 7,584 |
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
| Stars | 79,916 |
| 语言 | TypeScript |
| Forks | 8,058 |
| Issues | 708 |
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
| Stars | 244,503 |
| 语言 | JavaScript |
| Forks | 50,923 |
| Issues | 1,222 |
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
| Stars | 116,734 |
| 语言 | JavaScript |
| Forks | 35,341 |
| Issues | 2,609 |
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
| Stars | 111,925 |
| 语言 | JavaScript |
| Forks | 36,325 |
| Issues | 547 |
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
| Stars | 109,011 |
| 语言 | JavaScript |
| Forks | 11,630 |
| Issues | 267 |
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
| Stars | 98,154 |
| 语言 | JavaScript |
| Forks | 32,684 |
| Issues | 1,611 |
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
| Stars | 95,589 |
| 语言 | JavaScript |
| Forks | 15,355 |
| Issues | 63 |
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
| Stars | 86,302 |
| 语言 | JavaScript |
| Forks | 4,888 |
| Issues | 983 |
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
| Stars | 70,991 |
| 语言 | JavaScript |
| Forks | 16,812 |
| Issues | 893 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,314 |
| 语言 | JavaScript |
| Forks | 9,188 |
| Issues | 0 |
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
| Stars | 65,838 |
| 语言 | JavaScript |
| Forks | 9,375 |
| Issues | 204 |
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
| Stars | 62,750 |
| 语言 | JavaScript |
| Forks | 4,008 |
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
| Stars | 60,430 |
| 语言 | JavaScript |
| Forks | 5,649 |
| Issues | 70 |
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
| Stars | 59,846 |
| 语言 | JavaScript |
| Forks | 20,476 |
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
| Stars | 57,426 |
| 语言 | JavaScript |
| Forks | 12,309 |
| Issues | 25 |
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
| Stars | 53,129 |
| 语言 | JavaScript |
| Forks | 10,601 |
| Issues | 453 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,502 |
| 语言 | JavaScript |
| Forks | 11,469 |
| Issues | 234 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,260 |
| 语言 | JavaScript |
| Forks | 10,342 |
| Issues | 132 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,626 |
| 语言 | JavaScript |
| Forks | 2,428 |
| Issues | 1,208 |
| Topics | date, date-formatting, datetime, dayjs, moment, time |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,471 |
| 语言 | Go |
| Forks | 18,915 |
| Issues | 9,936 |
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
| Stars | 105,895 |
| 语言 | Go |
| Forks | 14,991 |
| Issues | 44 |
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
| Stars | 87,594 |
| 语言 | Go |
| Forks | 8,243 |
| Issues | 266 |
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
| Stars | 81,721 |
| 语言 | Go |
| Forks | 4,992 |
| Issues | 392 |
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
| Stars | 68,628 |
| 语言 | Go |
| Forks | 3,217 |
| Issues | 20 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,639 |
| 语言 | Go |
| Forks | 5,029 |
| Issues | 1,162 |
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
| Stars | 50,981 |
| 语言 | Go |
| Forks | 21,888 |
| Issues | 389 |
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
| Stars | 49,313 |
| 语言 | Go |
| Forks | 7,954 |
| Issues | 556 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,779 |
| 语言 | Python |
| Forks | 55,384 |
| Issues | 527 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,018 |
| 语言 | Python |
| Forks | 7,214 |
| Issues | 484 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,742 |
| 语言 | TypeScript |
| Forks | 16,496 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,038 |
| 语言 | JavaScript |
| Forks | 32,555 |
| Issues | 278 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,324 |
| 语言 | JavaScript |
| Forks | 7,133 |
| Issues | 141 |
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
| Stars | 50,642 |
| 语言 | Go |
| Forks | 1,596 |
| Issues | 267 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 151,109 |
| 语言 | Python |
| Forks | 11,506 |
| Issues | 326 |
| Topics | awesome, github, hellogithub, python |
