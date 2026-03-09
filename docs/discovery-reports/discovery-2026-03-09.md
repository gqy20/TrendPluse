# 项目发现报告 (2026-03-09)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 132 |
| 去重移除 | 32 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 64 |

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
| Stars | 126,412 |
| 语言 | Python |
| Forks | 17,895 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互平台，以 12.6 万+ Stars 证明了其在开源社区的广泛认可。它统一支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG（检索增强生成）和 MCP（模型上下文协议）等前沿技术，为用户提供了开箱即用的私有化 AI 解决方案。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API 等），实现统一接口管理
- 内置 RAG（检索增强生成）能力，支持与私有文档知识库交互
- 支持 MCP（Model Context Protocol）协议，便于与外部工具和资源集成
- 完全自托管部署，数据隐私安全可控，适合企业级应用
- 基于 Python 开发，提供友好的 Web UI 界面，易于部署和定制

**适用场景**:
- 企业内部私有化 AI 助手部署，保护敏感数据隐私
- 个人开发者搭建本地 LLM 服务，结合 Ollama 实现低成本 AI 应用
- 构建基于私有知识库的智能问答系统（RAG 场景）



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,558 |
| 语言 | Python |
| Forks | 8,317 |
| Issues | 3,065 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个备受认可的顶级开源 RAG 引擎，拥有超过 7.4 万 Star，其独特价值在于将最前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层，是企业级智能问答和知识检索的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力的下一代检索增强生成架构
- 支持 GraphRAG 图谱增强检索，提升复杂推理能力
- 内置强大的文档解析与理解引擎，支持多格式文档处理
- 支持 MCP、Ollama、OpenAI、DeepSeek 等多种 LLM 后端
- 提供 Agentic Workflow 智能工作流编排能力

**适用场景**:
- 企业知识库问答系统：快速构建基于内部文档的智能问答平台
- 智能文档分析：自动化解析和理解复杂业务文档
- AI 搜索与深度研究：构建具备上下文理解的智能搜索引擎



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,134 |
| 语言 | TypeScript |
| Forks | 6,290 |
| Issues | 242 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的 Web 数据提取 API，能够将任意网站转换为 LLM 可直接使用的 markdown 或结构化数据，解决了 AI 开发中最头疼的数据清洗和格式化问题。凭借 9万+ stars 和活跃的开源社区，已成为 AI 数据管道的事实标准工具。

**技术亮点**:
- 一键将完整网站转换为 LLM-ready 的 markdown 格式，无需手动清洗数据
- 支持将网页内容提取为结构化 JSON 数据，便于 AI Agent 消化和处理
- 内置智能爬虫，支持动态渲染、JS 执行和复杂网站抓取
- 提供 Web Data API，可无缝集成到 AI 工作流和 RAG 系统中
- 支持 Web 搜索功能，可直接作为 AI 应用的知识检索层

**适用场景**:
- 构建 RAG（检索增强生成）应用时，快速将企业官网、文档站转为知识库
- AI Agent 开发中需要实时获取网页结构化数据作为上下文输入
- 数据分析和研究场景，批量提取网站内容进行训练数据准备或市场调研



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,940 |
| 语言 | JavaScript |
| Forks | 8,609 |
| Issues | 27 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个性能卓越的AI Agent优化系统，拥有近7万Star证明了其广泛认可度。它通过技能、记忆、安全机制和研究驱动的开发模式，将Claude Code、Cursor等主流AI编码工具的性能发挥到极致，是提升AI辅助开发效率的必备工具。

**技术亮点**:
- Agent Harness架构：统一的性能优化框架，支持Claude Code、Codex、Cursor等多个AI编码平台
- 五大核心能力模块：技能系统(Skills)、本能机制(Instincts)、记忆管理(Memory)、安全防护(Security)和研究优先开发模式
- MCP协议支持：通过Model Context Protocol实现与各种AI工具的无缝集成
- 跨平台兼容性：一套系统适配多个主流AI编码工具，降低学习成本
- MIT开源许可：完全免费且可商用的企业级解决方案

**适用场景**:
- 个人开发者：提升日常编码效率，让AI助手更智能、更懂你的代码风格
- 企业团队：标准化AI辅助开发流程，统一管理团队的知识库和安全策略
- AI工具研究者：研究Agent优化技术，构建更强大的AI应用系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,425 |
| 语言 | Go |
| Forks | 3,656 |
| Issues | 147 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地 AI 解决方案之一，无需 GPU 就能在消费级硬件上运行，提供与 OpenAI API 完全兼容的接口，让开发者能以零成本实现私有化 AI 部署，兼顾隐私保护与成本控制。

**技术亮点**:
- 无需 GPU 支持，在消费级 CPU 硬件上即可运行大语言模型
- 完全兼容 OpenAI API，可作为 Drop-in 替换方案无缝迁移
- 多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、目标检测等
- 支持多种模型格式：GGUF、Transformers、Diffusers、RWKV、Mamba 等
- 支持分布式、P2P 和去中心化推理，具备 MCP 协议支持

**适用场景**:
- 企业内部私有化 AI 服务部署，保护敏感数据不外泄
- 个人开发者在本地电脑搭建低成本 AI 助手，无需云端订阅费用
- 边缘设备或无 GPU 环境下运行 AI 推理服务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,344 |
| 语言 | TypeScript |
| Forks | 14,754 |
| Issues | 644 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI 智能体协作平台，以 73K+ Stars 证明了其在开源社区的受欢迎程度。它将智能体协作推向新高度，支持多智能体协同工作、可视化团队设计，并将智能体作为工作交互的核心单元，是构建 AI 工作流的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI 智能体协同工作，实现复杂任务的分工与配合
- MCP 协议支持：集成 Model Context Protocol，实现与知识库和外部工具的无缝连接
- 多模型兼容：支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，具备出色的模型灵活性
- 可视化智能体设计：提供低代码/无代码方式快速构建智能体团队，降低开发门槛
- 知识库集成：支持构建和管理知识库，增强智能体的上下文理解和专业能力

**适用场景**:
- 企业级 AI 助手团队构建：企业可快速搭建客服、数据分析、内容创作等多角色智能体团队，实现业务流程自动化
- 个人开发者 AI 工作流搭建：个人用户可创建个性化的 AI 工作空间，整合多个智能体处理日常工作和生活任务
- 智能体应用原型开发：开发者可快速验证多智能体协作方案，加速 AI 应用的从概念到落地的过程



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,106 |
| 语言 | Python |
| Forks | 8,309 |
| Issues | 925 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前 GitHub 上最受欢迎的 LLM 微调框架之一（68K+ Stars），它将原本分散复杂的模型微调流程统一到一个易用平台中，支持 100+ 主流大语言模型和多模态模型，包括 DeepSeek、GPT、Llama3、Qwen 等热门模型，大幅降低了企业和开发者进行模型定制化训练的技术门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，涵盖主流开源和商业模型，一站式解决方案
- 多样化微调方法：集成 LoRA、QLoRA、PEFT、RLHF、Instruction Tuning 等先进微调技术
- 高效量化支持：支持模型量化和 MoE（混合专家）架构，显著降低训练和部署资源需求
- Agent 能力集成：支持 AI Agent 开发，便于构建具备工具调用能力的智能应用
- 生产级方案：ACL 2024 发表，Apache 2.0 开源许可，企业级可用性保障

**适用场景**:
- 企业私有化部署：针对行业数据微调专属大模型，如客服、知识库问答、文档处理等垂直场景
- 学术研究实验：快速验证不同微调策略（LoRA/QLoRA/RLHF）在各类模型上的效果对比
- AI 应用开发：个人开发者或创业团队低成本定制模型，构建智能对话、内容生成等应用



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,366 |
| 语言 | Java |
| Forks | 15,829 |
| Issues | 46 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个成熟的企业级AI低代码平台，融合了"低代码+零代码"双模开发模式，集成AI能力（AI聊天助手、知识库、AI流程编排、MCP等），让开发者既能通过强大的代码生成器实现前后端一键生成快速交付，又能在需要时灵活手写代码定制，完美平衡了开发效率与灵活性。

**技术亮点**:
- 【双模开发引擎】支持低代码和零代码两种模式，前后端代码一键生成，无需手写代码即可完成业务开发
- 【AI能力全面集成】内置AI应用、AI模型管理、AI聊天助手、知识库(RAG)、AI流程编排(AI Flow)、MCP协议和插件体系，支持 LangChain4j 和 Spring AI
- 【现代技术栈】基于 SpringBoot3 + SpringCloud 微服务架构，前端采用 Vue3 + Ant Design Vue，持久层使用 MyBatis-Plus，工作流支持 Flowable/Activiti
- 【AI Agent 能力】支持聊天式业务操作，结合 DeepSeek 等大模型实现智能化交互，Agent 可自主编排业务流程
- 【企业级特性】45K+ Stars 验证的成熟方案，支持工作流引擎、代码生成器、微服务架构，适合企业级复杂业务场景

**适用场景**:
- 【企业快速开发】企业内部管理系统、ERP、CRM、OA等业务系统快速搭建，大幅缩短开发周期
- 【AI应用构建】构建企业级AI应用，如智能客服、知识库问答、AI工作流自动化、智能助手等
- 【创业项目MVP】初创团队快速验证商业想法，利用低代码能力快速交付产品原型和最小可行产品



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,065 |
| 语言 | Python |
| Forks | 9,807 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,472 |
| 语言 | TypeScript |
| Forks | 6,961 |
| Issues | 444 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,686 |
| 语言 | TypeScript |
| Forks | 2,333 |
| Issues | 98 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,308 |
| 语言 | Python |
| Forks | 2,047 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,659 |
| 语言 | Python |
| Forks | 6,122 |
| Issues | 193 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,441 |
| 语言 | TypeScript |
| Forks | 3,486 |
| Issues | 264 |
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
| Stars | 101,154 |
| 语言 | Python |
| Forks | 14,714 |
| Issues | 8 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,970 |
| 语言 | JavaScript |
| Forks | 6,046 |
| Issues | 300 |
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
| Stars | 68,824 |
| 语言 | Python |
| Forks | 8,607 |
| Issues | 362 |
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
| Stars | 38,419 |
| 语言 | TypeScript |
| Forks | 2,898 |
| Issues | 338 |
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
| Stars | 80,021 |
| 语言 | Python |
| Forks | 9,451 |
| Issues | 220 |
| Topics | ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 23,902 |
| Issues | 795 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,799 |
| 语言 | Python |
| Forks | 3,380 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,327 |
| 语言 | TypeScript |
| Forks | 55,591 |
| Issues | 1,410 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,425 |
| 语言 | Python |
| Forks | 8,538 |
| Issues | 892 |
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
| Stars | 53,499 |
| 语言 | Jupyter Notebook |
| Forks | 18,586 |
| Issues | 2 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,346 |
| 语言 | MDX |
| Forks | 7,608 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,587 |
| 语言 | Jupyter Notebook |
| Forks | 5,154 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 42,284 |
| 语言 | Python |
| Forks | 4,208 |
| Issues | 267 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


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
| Stars | 126,412 |
| 语言 | Python |
| Forks | 17,895 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互平台，以 12.6 万+ Stars 证明了其在开源社区的广泛认可。它统一支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG（检索增强生成）和 MCP（模型上下文协议）等前沿技术，为用户提供了开箱即用的私有化 AI 解决方案。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API 等），实现统一接口管理
- 内置 RAG（检索增强生成）能力，支持与私有文档知识库交互
- 支持 MCP（Model Context Protocol）协议，便于与外部工具和资源集成
- 完全自托管部署，数据隐私安全可控，适合企业级应用
- 基于 Python 开发，提供友好的 Web UI 界面，易于部署和定制

**适用场景**:
- 企业内部私有化 AI 助手部署，保护敏感数据隐私
- 个人开发者搭建本地 LLM 服务，结合 Ollama 实现低成本 AI 应用
- 构建基于私有知识库的智能问答系统（RAG 场景）



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,558 |
| 语言 | Python |
| Forks | 8,317 |
| Issues | 3,065 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个备受认可的顶级开源 RAG 引擎，拥有超过 7.4 万 Star，其独特价值在于将最前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层，是企业级智能问答和知识检索的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力的下一代检索增强生成架构
- 支持 GraphRAG 图谱增强检索，提升复杂推理能力
- 内置强大的文档解析与理解引擎，支持多格式文档处理
- 支持 MCP、Ollama、OpenAI、DeepSeek 等多种 LLM 后端
- 提供 Agentic Workflow 智能工作流编排能力

**适用场景**:
- 企业知识库问答系统：快速构建基于内部文档的智能问答平台
- 智能文档分析：自动化解析和理解复杂业务文档
- AI 搜索与深度研究：构建具备上下文理解的智能搜索引擎



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,344 |
| 语言 | TypeScript |
| Forks | 14,754 |
| Issues | 644 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI 智能体协作平台，以 73K+ Stars 证明了其在开源社区的受欢迎程度。它将智能体协作推向新高度，支持多智能体协同工作、可视化团队设计，并将智能体作为工作交互的核心单元，是构建 AI 工作流的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI 智能体协同工作，实现复杂任务的分工与配合
- MCP 协议支持：集成 Model Context Protocol，实现与知识库和外部工具的无缝连接
- 多模型兼容：支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，具备出色的模型灵活性
- 可视化智能体设计：提供低代码/无代码方式快速构建智能体团队，降低开发门槛
- 知识库集成：支持构建和管理知识库，增强智能体的上下文理解和专业能力

**适用场景**:
- 企业级 AI 助手团队构建：企业可快速搭建客服、数据分析、内容创作等多角色智能体团队，实现业务流程自动化
- 个人开发者 AI 工作流搭建：个人用户可创建个性化的 AI 工作空间，整合多个智能体处理日常工作和生活任务
- 智能体应用原型开发：开发者可快速验证多智能体协作方案，加速 AI 应用的从概念到落地的过程



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,366 |
| 语言 | Java |
| Forks | 15,829 |
| Issues | 46 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个成熟的企业级AI低代码平台，融合了"低代码+零代码"双模开发模式，集成AI能力（AI聊天助手、知识库、AI流程编排、MCP等），让开发者既能通过强大的代码生成器实现前后端一键生成快速交付，又能在需要时灵活手写代码定制，完美平衡了开发效率与灵活性。

**技术亮点**:
- 【双模开发引擎】支持低代码和零代码两种模式，前后端代码一键生成，无需手写代码即可完成业务开发
- 【AI能力全面集成】内置AI应用、AI模型管理、AI聊天助手、知识库(RAG)、AI流程编排(AI Flow)、MCP协议和插件体系，支持 LangChain4j 和 Spring AI
- 【现代技术栈】基于 SpringBoot3 + SpringCloud 微服务架构，前端采用 Vue3 + Ant Design Vue，持久层使用 MyBatis-Plus，工作流支持 Flowable/Activiti
- 【AI Agent 能力】支持聊天式业务操作，结合 DeepSeek 等大模型实现智能化交互，Agent 可自主编排业务流程
- 【企业级特性】45K+ Stars 验证的成熟方案，支持工作流引擎、代码生成器、微服务架构，适合企业级复杂业务场景

**适用场景**:
- 【企业快速开发】企业内部管理系统、ERP、CRM、OA等业务系统快速搭建，大幅缩短开发周期
- 【AI应用构建】构建企业级AI应用，如智能客服、知识库问答、AI工作流自动化、智能助手等
- 【创业项目MVP】初创团队快速验证商业想法，利用低代码能力快速交付产品原型和最小可行产品



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,686 |
| 语言 | TypeScript |
| Forks | 2,333 |
| Issues | 98 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,308 |
| 语言 | Python |
| Forks | 2,047 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,659 |
| 语言 | Python |
| Forks | 6,122 |
| Issues | 193 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,441 |
| 语言 | TypeScript |
| Forks | 3,486 |
| Issues | 264 |
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
| Stars | 101,154 |
| 语言 | Python |
| Forks | 14,714 |
| Issues | 8 |
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
| Stars | 98,787 |
| 语言 | TypeScript |
| Forks | 11,748 |
| Issues | 969 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,970 |
| 语言 | JavaScript |
| Forks | 6,046 |
| Issues | 300 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 23,902 |
| Issues | 795 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,917 |
| 语言 | Python |
| Forks | 9,925 |
| Issues | 252 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,269 |
| 语言 | Go |
| Forks | 3,879 |
| Issues | 1,066 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### microsoft/graphrag

**描述**: A modular graph-based Retrieval-Augmented Generation (RAG) system

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,328 |
| 语言 | Python |
| Forks | 3,308 |
| Issues | 76 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,346 |
| 语言 | MDX |
| Forks | 7,608 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,587 |
| 语言 | Jupyter Notebook |
| Forks | 5,154 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (26 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 126,412 |
| 语言 | Python |
| Forks | 17,895 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互平台，以 12.6 万+ Stars 证明了其在开源社区的广泛认可。它统一支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG（检索增强生成）和 MCP（模型上下文协议）等前沿技术，为用户提供了开箱即用的私有化 AI 解决方案。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API 等），实现统一接口管理
- 内置 RAG（检索增强生成）能力，支持与私有文档知识库交互
- 支持 MCP（Model Context Protocol）协议，便于与外部工具和资源集成
- 完全自托管部署，数据隐私安全可控，适合企业级应用
- 基于 Python 开发，提供友好的 Web UI 界面，易于部署和定制

**适用场景**:
- 企业内部私有化 AI 助手部署，保护敏感数据隐私
- 个人开发者搭建本地 LLM 服务，结合 Ollama 实现低成本 AI 应用
- 构建基于私有知识库的智能问答系统（RAG 场景）



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,558 |
| 语言 | Python |
| Forks | 8,317 |
| Issues | 3,065 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个备受认可的顶级开源 RAG 引擎，拥有超过 7.4 万 Star，其独特价值在于将最前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层，是企业级智能问答和知识检索的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力的下一代检索增强生成架构
- 支持 GraphRAG 图谱增强检索，提升复杂推理能力
- 内置强大的文档解析与理解引擎，支持多格式文档处理
- 支持 MCP、Ollama、OpenAI、DeepSeek 等多种 LLM 后端
- 提供 Agentic Workflow 智能工作流编排能力

**适用场景**:
- 企业知识库问答系统：快速构建基于内部文档的智能问答平台
- 智能文档分析：自动化解析和理解复杂业务文档
- AI 搜索与深度研究：构建具备上下文理解的智能搜索引擎



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,940 |
| 语言 | JavaScript |
| Forks | 8,609 |
| Issues | 27 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个性能卓越的AI Agent优化系统，拥有近7万Star证明了其广泛认可度。它通过技能、记忆、安全机制和研究驱动的开发模式，将Claude Code、Cursor等主流AI编码工具的性能发挥到极致，是提升AI辅助开发效率的必备工具。

**技术亮点**:
- Agent Harness架构：统一的性能优化框架，支持Claude Code、Codex、Cursor等多个AI编码平台
- 五大核心能力模块：技能系统(Skills)、本能机制(Instincts)、记忆管理(Memory)、安全防护(Security)和研究优先开发模式
- MCP协议支持：通过Model Context Protocol实现与各种AI工具的无缝集成
- 跨平台兼容性：一套系统适配多个主流AI编码工具，降低学习成本
- MIT开源许可：完全免费且可商用的企业级解决方案

**适用场景**:
- 个人开发者：提升日常编码效率，让AI助手更智能、更懂你的代码风格
- 企业团队：标准化AI辅助开发流程，统一管理团队的知识库和安全策略
- AI工具研究者：研究Agent优化技术，构建更强大的AI应用系统



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,344 |
| 语言 | TypeScript |
| Forks | 14,754 |
| Issues | 644 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI 智能体协作平台，以 73K+ Stars 证明了其在开源社区的受欢迎程度。它将智能体协作推向新高度，支持多智能体协同工作、可视化团队设计，并将智能体作为工作交互的核心单元，是构建 AI 工作流的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI 智能体协同工作，实现复杂任务的分工与配合
- MCP 协议支持：集成 Model Context Protocol，实现与知识库和外部工具的无缝连接
- 多模型兼容：支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，具备出色的模型灵活性
- 可视化智能体设计：提供低代码/无代码方式快速构建智能体团队，降低开发门槛
- 知识库集成：支持构建和管理知识库，增强智能体的上下文理解和专业能力

**适用场景**:
- 企业级 AI 助手团队构建：企业可快速搭建客服、数据分析、内容创作等多角色智能体团队，实现业务流程自动化
- 个人开发者 AI 工作流搭建：个人用户可创建个性化的 AI 工作空间，整合多个智能体处理日常工作和生活任务
- 智能体应用原型开发：开发者可快速验证多智能体协作方案，加速 AI 应用的从概念到落地的过程



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,136 |
| 语言 | HTML |
| Forks | 19,857 |
| Issues | 15 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源提示词社区平台，为AI用户提供海量精选prompt模板资源。其最大价值在于支持完全自托管，企业可在保护隐私的前提下构建内部提示词知识库，是AI应用落地的重要基础设施。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 的现代全栈架构，支持SSR和良好的SEO优化
- 完全开源且支持自托管部署，企业可私有化部署保障数据隐私安全
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流LLM平台的提示词，具有广泛的模型兼容性
- 采用CC0许可协议，内容完全开放，支持社区协作和自由分发
- 集合 prompt engineering 最佳实践，是学习提示词工程的优质资源库

**适用场景**:
- 企业内部部署私有提示词库，沉淀AI应用最佳实践，保护核心业务prompt资产
- AI开发者和提示词工程师学习、收集和测试各类高质量prompt模板
- 团队协作共享AI工具使用经验，快速复用成熟提示词提升工作效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,533 |
| 语言 | Jupyter Notebook |
| Forks | 13,323 |
| Issues | 0 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,065 |
| 语言 | Python |
| Forks | 9,807 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,472 |
| 语言 | TypeScript |
| Forks | 6,961 |
| Issues | 444 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,686 |
| 语言 | TypeScript |
| Forks | 2,333 |
| Issues | 98 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,308 |
| 语言 | Python |
| Forks | 2,047 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,970 |
| 语言 | JavaScript |
| Forks | 6,046 |
| Issues | 300 |
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
| Stars | 68,824 |
| 语言 | Python |
| Forks | 8,607 |
| Issues | 362 |
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
| Stars | 38,419 |
| 语言 | TypeScript |
| Forks | 2,898 |
| Issues | 338 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 23,902 |
| Issues | 795 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,799 |
| 语言 | Python |
| Forks | 3,380 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,052 |
| 语言 | HTML |
| Forks | 5,444 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,597 |
| 语言 | Python |
| Forks | 14,131 |
| Issues | 3,593 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,972 |
| 语言 | Python |
| Forks | 3,764 |
| Issues | 66 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,503 |
| 语言 | Python |
| Forks | 2,549 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,425 |
| 语言 | Python |
| Forks | 8,538 |
| Issues | 892 |
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
| Stars | 164,635 |
| 语言 | Go |
| Forks | 14,859 |
| Issues | 2,621 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,346 |
| 语言 | MDX |
| Forks | 7,608 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,539 |
| 语言 | Rust |
| Forks | 9,099 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 38,849 |
| 语言 | TypeScript |
| Forks | 3,927 |
| Issues | 1,066 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 42,284 |
| 语言 | Python |
| Forks | 4,208 |
| Issues | 267 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 90,438 |
| 语言 | Python |
| Forks | 5,327 |
| Issues | 461 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (12 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,106 |
| 语言 | Python |
| Forks | 8,309 |
| Issues | 925 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前 GitHub 上最受欢迎的 LLM 微调框架之一（68K+ Stars），它将原本分散复杂的模型微调流程统一到一个易用平台中，支持 100+ 主流大语言模型和多模态模型，包括 DeepSeek、GPT、Llama3、Qwen 等热门模型，大幅降低了企业和开发者进行模型定制化训练的技术门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，涵盖主流开源和商业模型，一站式解决方案
- 多样化微调方法：集成 LoRA、QLoRA、PEFT、RLHF、Instruction Tuning 等先进微调技术
- 高效量化支持：支持模型量化和 MoE（混合专家）架构，显著降低训练和部署资源需求
- Agent 能力集成：支持 AI Agent 开发，便于构建具备工具调用能力的智能应用
- 生产级方案：ACL 2024 发表，Apache 2.0 开源许可，企业级可用性保障

**适用场景**:
- 企业私有化部署：针对行业数据微调专属大模型，如客服、知识库问答、文档处理等垂直场景
- 学术研究实验：快速验证不同微调策略（LoRA/QLoRA/RLHF）在各类模型上的效果对比
- AI 应用开发：个人开发者或创业团队低成本定制模型，构建智能对话、内容生成等应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,747 |
| 语言 | Python |
| Forks | 6,145 |
| Issues | 62 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是全球最热门的开源金融数据分析平台，为分析师、量化交易员和AI智能体提供统一的金融数据接入方案。它打破了传统金融数据的高成本壁垒，将股票、加密货币、衍生品、宏观经济等多维度数据整合到一个Python平台中，是构建量化策略和金融AI应用的理想基础设施。

**技术亮点**:
- 一站式多资产数据整合：支持股票、加密货币、期权、衍生品、固定收益、宏观经济等全品类金融数据接入
- AI原生设计：专门为AI agents优化，支持大语言模型直接调用进行金融分析和决策
- 模块化可扩展架构：Python生态深度集成，支持自定义数据源和功能扩展
- 量化分析工具集：内置机器学习和量化分析功能，支持策略回测和因子分析
- 开源社区驱动：62K+ stars活跃社区，持续更新维护，文档完善

**适用场景**:
- 量化交易策略研发：为量化研究员提供免费的数据获取和策略回测平台，快速验证交易想法
- 金融AI应用开发：为AI工程师构建金融智能助手、投资顾问机器人提供数据基础设施
- 投资分析与研究报告：为个人投资者和分析师提供专业级的金融数据分析工具，降低数据获取门槛



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,136 |
| 语言 | HTML |
| Forks | 19,857 |
| Issues | 15 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源提示词社区平台，为AI用户提供海量精选prompt模板资源。其最大价值在于支持完全自托管，企业可在保护隐私的前提下构建内部提示词知识库，是AI应用落地的重要基础设施。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 的现代全栈架构，支持SSR和良好的SEO优化
- 完全开源且支持自托管部署，企业可私有化部署保障数据隐私安全
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流LLM平台的提示词，具有广泛的模型兼容性
- 采用CC0许可协议，内容完全开放，支持社区协作和自由分发
- 集合 prompt engineering 最佳实践，是学习提示词工程的优质资源库

**适用场景**:
- 企业内部部署私有提示词库，沉淀AI应用最佳实践，保护核心业务prompt资产
- AI开发者和提示词工程师学习、收集和测试各类高质量prompt模板
- 团队协作共享AI工具使用经验，快速复用成熟提示词提升工作效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,533 |
| 语言 | Jupyter Notebook |
| Forks | 13,323 |
| Issues | 0 |
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
| Stars | 32,441 |
| 语言 | TypeScript |
| Forks | 3,486 |
| Issues | 264 |
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
| Stars | 157,655 |
| 语言 | Python |
| Forks | 32,334 |
| Issues | 2,258 |
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
| Stars | 72,597 |
| 语言 | Python |
| Forks | 14,131 |
| Issues | 3,593 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,613 |
| 语言 | Python |
| Forks | 30,139 |
| Issues | 2,467 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


### Comfy-Org/ComfyUI

**描述**: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,378 |
| 语言 | Python |
| Forks | 12,083 |
| Issues | 3,802 |
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
| Stars | 98,115 |
| 语言 | Python |
| Forks | 27,120 |
| Issues | 18,101 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,346 |
| 语言 | MDX |
| Forks | 7,608 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,587 |
| 语言 | Jupyter Notebook |
| Forks | 5,154 |
| Issues | 124 |
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
| Stars | 68,940 |
| 语言 | JavaScript |
| Forks | 8,609 |
| Issues | 27 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个性能卓越的AI Agent优化系统，拥有近7万Star证明了其广泛认可度。它通过技能、记忆、安全机制和研究驱动的开发模式，将Claude Code、Cursor等主流AI编码工具的性能发挥到极致，是提升AI辅助开发效率的必备工具。

**技术亮点**:
- Agent Harness架构：统一的性能优化框架，支持Claude Code、Codex、Cursor等多个AI编码平台
- 五大核心能力模块：技能系统(Skills)、本能机制(Instincts)、记忆管理(Memory)、安全防护(Security)和研究优先开发模式
- MCP协议支持：通过Model Context Protocol实现与各种AI工具的无缝集成
- 跨平台兼容性：一套系统适配多个主流AI编码工具，降低学习成本
- MIT开源许可：完全免费且可商用的企业级解决方案

**适用场景**:
- 个人开发者：提升日常编码效率，让AI助手更智能、更懂你的代码风格
- 企业团队：标准化AI辅助开发流程，统一管理团队的知识库和安全策略
- AI工具研究者：研究Agent优化技术，构建更强大的AI应用系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,425 |
| 语言 | Go |
| Forks | 3,656 |
| Issues | 147 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地 AI 解决方案之一，无需 GPU 就能在消费级硬件上运行，提供与 OpenAI API 完全兼容的接口，让开发者能以零成本实现私有化 AI 部署，兼顾隐私保护与成本控制。

**技术亮点**:
- 无需 GPU 支持，在消费级 CPU 硬件上即可运行大语言模型
- 完全兼容 OpenAI API，可作为 Drop-in 替换方案无缝迁移
- 多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、目标检测等
- 支持多种模型格式：GGUF、Transformers、Diffusers、RWKV、Mamba 等
- 支持分布式、P2P 和去中心化推理，具备 MCP 协议支持

**适用场景**:
- 企业内部私有化 AI 服务部署，保护敏感数据不外泄
- 个人开发者在本地电脑搭建低成本 AI 助手，无需云端订阅费用
- 边缘设备或无 GPU 环境下运行 AI 推理服务



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,824 |
| 语言 | Python |
| Forks | 8,607 |
| Issues | 362 |
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
| Stars | 38,419 |
| 语言 | TypeScript |
| Forks | 2,898 |
| Issues | 338 |
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
| Stars | 178,327 |
| 语言 | TypeScript |
| Forks | 55,591 |
| Issues | 1,410 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,503 |
| 语言 | Python |
| Forks | 2,549 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,365 |
| 语言 | JavaScript |
| Forks | 4,018 |
| Issues | 1,398 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,350 |
| 语言 | Python |
| Forks | 12,180 |
| Issues | 2,378 |
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
| Stars | 96,070 |
| 语言 | Python |
| Forks | 8,807 |
| Issues | 147 |
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
| Stars | 73,525 |
| 语言 | Python |
| Forks | 8,726 |
| Issues | 200 |
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
| Stars | 182,520 |
| 语言 | TypeScript |
| Forks | 38,388 |
| Issues | 14,780 |
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
| Stars | 93,774 |
| 语言 | TypeScript |
| Forks | 9,385 |
| Issues | 290 |
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
| Stars | 78,252 |
| 语言 | TypeScript |
| Forks | 5,632 |
| Issues | 688 |
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
| Stars | 76,554 |
| 语言 | TypeScript |
| Forks | 6,541 |
| Issues | 169 |
| Topics | browser-ide, dev-tools, development-environment, ide, remote-work, vscode, vscode-remote |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,643 |
| 语言 | JavaScript |
| Forks | 7,264 |
| Issues | 709 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,495 |
| 语言 | Go |
| Forks | 2,705 |
| Issues | 318 |
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
| Stars | 73,824 |
| 语言 | Go |
| Forks | 2,568 |
| Issues | 908 |
| Topics | cli, git, terminal |
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
| Stars | 405,935 |
| 语言 | Python |
| Forks | 43,833 |
| Issues | 950 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,419 |
| 语言 | TypeScript |
| Forks | 2,898 |
| Issues | 338 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,799 |
| 语言 | Python |
| Forks | 3,380 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,327 |
| 语言 | TypeScript |
| Forks | 55,591 |
| Issues | 1,410 |
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
| Stars | 51,675 |
| 语言 | Go |
| Forks | 10,336 |
| Issues | 222 |
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
| Stars | 121,058 |
| 语言 | Go |
| Forks | 42,633 |
| Issues | 2,706 |
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
| Stars | 71,498 |
| 语言 | Go |
| Forks | 18,916 |
| Issues | 3,792 |
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
| Stars | 54,197 |
| 语言 | Go |
| Forks | 6,447 |
| Issues | 2,847 |
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
| Stars | 47,557 |
| 语言 | Go |
| Forks | 5,066 |
| Issues | 964 |
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
| Stars | 93,774 |
| 语言 | TypeScript |
| Forks | 9,385 |
| Issues | 290 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### microsoft/playwright

**描述**: Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,835 |
| 语言 | TypeScript |
| Forks | 5,258 |
| Issues | 612 |
| Topics | automation, chrome, chromium, e2e-testing, electron, end-to-end-testing, firefox, javascript, playwright, test, test-automation, testing, testing-tools, web, webkit |
| 许可证 | Apache License 2.0 |


### Stirling-Tools/Stirling-PDF

**描述**: #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,112 |
| 语言 | TypeScript |
| Forks | 6,373 |
| Issues | 428 |
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
| Stars | 83,855 |
| 语言 | JavaScript |
| Forks | 7,496 |
| Issues | 704 |
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
| Stars | 69,212 |
| 语言 | Go |
| Forks | 1,872 |
| Issues | 290 |
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
| Stars | 62,156 |
| 语言 | Go |
| Forks | 5,868 |
| Issues | 765 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### usememos/memos

**描述**: An open-source, self-hosted note-taking tool. Capture thoughts instantly, own them completely — no tracking, no ads, no subscription fees.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,603 |
| 语言 | Go |
| Forks | 4,164 |
| Issues | 17 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 42,284 |
| 语言 | Python |
| Forks | 4,208 |
| Issues | 267 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,446 |
| 语言 | Go |
| Forks | 7,207 |
| Issues | 80 |
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
| Stars | 83,855 |
| 语言 | JavaScript |
| Forks | 7,496 |
| Issues | 704 |
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
| Stars | 63,151 |
| 语言 | Go |
| Forks | 10,224 |
| Issues | 765 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (13 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,425 |
| 语言 | Go |
| Forks | 3,656 |
| Issues | 147 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地 AI 解决方案之一，无需 GPU 就能在消费级硬件上运行，提供与 OpenAI API 完全兼容的接口，让开发者能以零成本实现私有化 AI 部署，兼顾隐私保护与成本控制。

**技术亮点**:
- 无需 GPU 支持，在消费级 CPU 硬件上即可运行大语言模型
- 完全兼容 OpenAI API，可作为 Drop-in 替换方案无缝迁移
- 多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、目标检测等
- 支持多种模型格式：GGUF、Transformers、Diffusers、RWKV、Mamba 等
- 支持分布式、P2P 和去中心化推理，具备 MCP 协议支持

**适用场景**:
- 企业内部私有化 AI 服务部署，保护敏感数据不外泄
- 个人开发者在本地电脑搭建低成本 AI 助手，无需云端订阅费用
- 边缘设备或无 GPU 环境下运行 AI 推理服务



### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,503 |
| 语言 | Python |
| Forks | 2,549 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,070 |
| 语言 | Python |
| Forks | 8,807 |
| Issues | 147 |
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
| Stars | 87,057 |
| 语言 | Python |
| Forks | 33,728 |
| Issues | 437 |
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
| Stars | 100,137 |
| 语言 | TypeScript |
| Forks | 27,106 |
| Issues | 1,145 |
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
| Stars | 78,252 |
| 语言 | TypeScript |
| Forks | 5,632 |
| Issues | 688 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,643 |
| 语言 | JavaScript |
| Forks | 7,264 |
| Issues | 709 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### gatsbyjs/gatsby

**描述**: React-based framework with performance, scalability, and security built in.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,938 |
| 语言 | JavaScript |
| Forks | 10,221 |
| Issues | 345 |
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
| Stars | 88,271 |
| 语言 | Go |
| Forks | 8,569 |
| Issues | 649 |
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
| Stars | 70,747 |
| 语言 | Go |
| Forks | 4,664 |
| Issues | 234 |
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
| Stars | 56,633 |
| 语言 | Go |
| Forks | 3,170 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
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
| Stars | 405,935 |
| 语言 | Python |
| Forks | 43,833 |
| Issues | 950 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,926 |
| 语言 | JavaScript |
| Forks | 22,760 |
| Issues | 190 |
| Topics | express, javascript, nodejs, server |
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
| Stars | 98,787 |
| 语言 | TypeScript |
| Forks | 11,748 |
| Issues | 969 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,970 |
| 语言 | JavaScript |
| Forks | 6,046 |
| Issues | 300 |
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
| Stars | 43,269 |
| 语言 | Go |
| Forks | 3,879 |
| Issues | 1,066 |
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
| Stars | 51,675 |
| 语言 | Go |
| Forks | 10,336 |
| Issues | 222 |
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
| Stars | 151,136 |
| 语言 | HTML |
| Forks | 19,857 |
| Issues | 15 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源提示词社区平台，为AI用户提供海量精选prompt模板资源。其最大价值在于支持完全自托管，企业可在保护隐私的前提下构建内部提示词知识库，是AI应用落地的重要基础设施。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 的现代全栈架构，支持SSR和良好的SEO优化
- 完全开源且支持自托管部署，企业可私有化部署保障数据隐私安全
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流LLM平台的提示词，具有广泛的模型兼容性
- 采用CC0许可协议，内容完全开放，支持社区协作和自由分发
- 集合 prompt engineering 最佳实践，是学习提示词工程的优质资源库

**适用场景**:
- 企业内部部署私有提示词库，沉淀AI应用最佳实践，保护核心业务prompt资产
- AI开发者和提示词工程师学习、收集和测试各类高质量prompt模板
- 团队协作共享AI工具使用经验，快速复用成熟提示词提升工作效率



### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,052 |
| 语言 | HTML |
| Forks | 5,444 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,346 |
| 语言 | MDX |
| Forks | 7,608 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,404 |
| 语言 | TypeScript |
| Forks | 9,898 |
| Issues | 2,234 |
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
| Stars | 86,597 |
| 语言 | TypeScript |
| Forks | 8,701 |
| Issues | 1,627 |
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
| Stars | 127,007 |
| 语言 | JavaScript |
| Forks | 12,444 |
| Issues | 3 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### jaywcjlove/awesome-mac

**描述**:  Now we have become very big, Different from the original idea. Collect premium software in various categories.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,745 |
| 语言 | JavaScript |
| Forks | 7,460 |
| Issues | 208 |
| Topics | app, apple, application, apps, awesome, awesome-list, awesome-lists, awesome-mac, desktop-app, desktop-application, desktop-apps, list, mac, mac-osx, macos, macos-app, macos-apps, macosx, software |
| 许可证 | Creative Commons Zero v1.0 Universal |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,998 |
| 语言 | Go |
| Forks | 13,033 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (64 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 129,794 |
| 语言 | Unknown |
| Forks | 33,067 |
| Issues | 127 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### CherryHQ/cherry-studio

**描述**: AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,104 |
| 语言 | TypeScript |
| Forks | 3,792 |
| Issues | 672 |
| Topics | ai-agent, claude-code, code-agent, codex, openclaw, opencode, shannon, skills, superpowers, superpowers-core-skills, vibe-coding |
| 许可证 | GNU Affero General Public License v3.0 |


### openclaw/openclaw

**描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 289,437 |
| 语言 | TypeScript |
| Forks | 54,900 |
| Issues | 11,726 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,597 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 39 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,922 |
| 语言 | Python |
| Forks | 11,646 |
| Issues | 127 |
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
| Stars | 75,260 |
| 语言 | Python |
| Forks | 6,412 |
| Issues | 620 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 383,860 |
| 语言 | Python |
| Forks | 66,011 |
| Issues | 70 |
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
| Stars | 112,646 |
| 语言 | TypeScript |
| Forks | 5,692 |
| Issues | 397 |
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
| Stars | 101,495 |
| 语言 | TypeScript |
| Forks | 7,393 |
| Issues | 177 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,952 |
| 语言 | Go |
| Forks | 10,236 |
| Issues | 1,898 |
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
| Stars | 97,367 |
| 语言 | C++ |
| Forks | 15,345 |
| Issues | 1,228 |
| Topics | ggml |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,453 |
| 语言 | Python |
| Forks | 1,609 |
| Issues | 37 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 338,176 |
| 语言 | Python |
| Forks | 54,771 |
| Issues | 522 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 286,389 |
| 语言 | Python |
| Forks | 27,340 |
| Issues | 19 |
| Topics | awesome, collections, python, python-framework, python-library, python-resources |
| 许可证 | Other |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 218,510 |
| 语言 | Python |
| Forks | 50,135 |
| Issues | 899 |
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
| Stars | 85,236 |
| 语言 | Python |
| Forks | 36,953 |
| Issues | 3,555 |
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
| Stars | 77,692 |
| 语言 | Python |
| Forks | 45,249 |
| Issues | 1,283 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,897 |
| 语言 | Python |
| Forks | 16,735 |
| Issues | 15 |
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
| Stars | 437,966 |
| 语言 | TypeScript |
| Forks | 43,551 |
| Issues | 285 |
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
| Stars | 350,611 |
| 语言 | TypeScript |
| Forks | 43,764 |
| Issues | 16 |
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
| Stars | 118,385 |
| 语言 | TypeScript |
| Forks | 12,803 |
| Issues | 2,827 |
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
| Stars | 109,056 |
| 语言 | TypeScript |
| Forks | 8,101 |
| Issues | 1,804 |
| Topics | base-ui, components, nextjs, radix-ui, react, shadcn, tailwindcss, ui |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,074 |
| 语言 | TypeScript |
| Forks | 13,272 |
| Issues | 5,479 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### mui/material-ui

**描述**: Material UI: Comprehensive React component library that implements Google's Material Design. Free forever.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,057 |
| 语言 | TypeScript |
| Forks | 32,707 |
| Issues | 1,724 |
| Topics | design-system, material-design, material-ui, react, react-components |
| 许可证 | MIT License |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,731 |
| 语言 | TypeScript |
| Forks | 54,543 |
| Issues | 1,363 |
| Topics | ant-design, antd, design-systems, react, typescript, ui-kit, ui-library |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,423 |
| 语言 | TypeScript |
| Forks | 5,051 |
| Issues | 655 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### tailwindlabs/tailwindcss

**描述**: A utility-first CSS framework for rapid UI development.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,011 |
| 语言 | TypeScript |
| Forks | 5,103 |
| Issues | 86 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,958 |
| 语言 | TypeScript |
| Forks | 7,578 |
| Issues | 37 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,627 |
| 语言 | TypeScript |
| Forks | 9,833 |
| Issues | 440 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,729 |
| 语言 | TypeScript |
| Forks | 7,889 |
| Issues | 623 |
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
| Stars | 243,813 |
| 语言 | JavaScript |
| Forks | 50,688 |
| Issues | 1,153 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### vercel/next.js

**描述**: The React Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,265 |
| 语言 | JavaScript |
| Forks | 30,595 |
| Issues | 3,433 |
| Topics | blog, browser, compiler, components, hybrid, nextjs, node, react, server-rendering, ssg, static, static-site-generator, universal, vercel |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,197 |
| 语言 | JavaScript |
| Forks | 34,970 |
| Issues | 2,511 |
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
| Stars | 111,257 |
| 语言 | JavaScript |
| Forks | 36,290 |
| Issues | 600 |
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
| Stars | 108,618 |
| 语言 | JavaScript |
| Forks | 11,539 |
| Issues | 348 |
| Topics | hacktoberfest, http-client, javascript, nodejs, promise |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,401 |
| 语言 | JavaScript |
| Forks | 15,225 |
| Issues | 42 |
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
| Stars | 86,078 |
| 语言 | JavaScript |
| Forks | 4,801 |
| Issues | 974 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,663 |
| 语言 | JavaScript |
| Forks | 31,438 |
| Issues | 271 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,690 |
| 语言 | JavaScript |
| Forks | 16,802 |
| Issues | 889 |
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
| Stars | 66,079 |
| 语言 | JavaScript |
| Forks | 9,315 |
| Issues | 203 |
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
| Stars | 61,991 |
| 语言 | JavaScript |
| Forks | 3,967 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,862 |
| 语言 | JavaScript |
| Forks | 20,471 |
| Issues | 98 |
| Topics | jquery |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,737 |
| 语言 | JavaScript |
| Forks | 5,600 |
| Issues | 63 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,022 |
| 语言 | Go |
| Forks | 18,854 |
| Issues | 9,833 |
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
| Stars | 105,039 |
| 语言 | Go |
| Forks | 14,927 |
| Issues | 41 |
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
| Stars | 86,981 |
| 语言 | Go |
| Forks | 8,200 |
| Issues | 268 |
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
| Stars | 80,653 |
| 语言 | Go |
| Forks | 4,946 |
| Issues | 406 |
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
| Stars | 68,706 |
| 语言 | Go |
| Forks | 3,216 |
| Issues | 11 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,929 |
| 语言 | Go |
| Forks | 4,956 |
| Issues | 1,135 |
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
| Stars | 50,903 |
| 语言 | Go |
| Forks | 21,832 |
| Issues | 382 |
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
| Stars | 49,136 |
| 语言 | Go |
| Forks | 7,978 |
| Issues | 572 |
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
| Stars | 46,932 |
| 语言 | Go |
| Forks | 8,886 |
| Issues | 8 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,327 |
| 语言 | Go |
| Forks | 3,754 |
| Issues | 91 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,833 |
| 语言 | Python |
| Forks | 10,603 |
| Issues | 4,118 |
| 许可证 | The Unlicense |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,077 |
| 语言 | Python |
| Forks | 7,160 |
| Issues | 474 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,801 |
| 语言 | JavaScript |
| Forks | 31,110 |
| Issues | 392 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
| 许可证 | MIT License |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,108 |
| 语言 | JavaScript |
| Forks | 26,772 |
| Issues | 187 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### FortAwesome/Font-Awesome

**描述**: The iconic SVG, font, and CSS toolkit

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,404 |
| 语言 | JavaScript |
| Forks | 12,244 |
| Issues | 317 |
| Topics | css, font, fontawesome, icons, svg-icons, svg-sprites, webfont |
| 许可证 | Other |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,236 |
| 语言 | JavaScript |
| Forks | 11,986 |
| Issues | 536 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,777 |
| 语言 | JavaScript |
| Forks | 4,465 |
| Issues | 94 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,268 |
| 语言 | JavaScript |
| Forks | 9,180 |
| Issues | 1 |
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
| Stars | 61,580 |
| 语言 | JavaScript |
| Forks | 7,126 |
| Issues | 128 |
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
| Stars | 57,402 |
| 语言 | JavaScript |
| Forks | 12,311 |
| Issues | 23 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 145,432 |
| 语言 | Python |
| Forks | 11,187 |
| Issues | 289 |
| Topics | awesome, github, hellogithub, python |
