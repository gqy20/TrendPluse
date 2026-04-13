# 项目发现报告 (2026-04-13)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
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
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 7 |
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
| Stars | 131,629 |
| 语言 | Python |
| Forks | 18,672 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是最受欢迎的开源 LLM Web 界面之一，通过支持 Ollama、OpenAI API 等多后端和 RAG、MCP 等高级功能，为开发者和企业提供了开箱即用、功能完备的本地 AI 部署方案，大幅降低了自托管 AI 应用的门槛，13万+ Stars 证明了其卓越的实用性和社区认可度。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API，提供统一的接口层
- RAG 检索增强生成：内置完整 RAG 功能，支持文档上传、向量检索和上下文增强
- MCP 协议支持：集成 Model Context Protocol，实现与外部工具的标准化连接
- 自托管部署：提供 Docker 一键部署方案，支持完全私有化，数据不离开本地
- 现代 Web 技术栈：基于 Python 构建，提供响应式界面和实时流式响应

**适用场景**:
- 企业私有化 AI 部署：对数据安全有高要求的企业在本地部署私有 LLM 助手
- 开发者本地调试：快速搭建本地 LLM 测试环境，调试 Prompt 和 RAG 流程
- 多模型统一管理：团队需要同时使用多种 LLM 服务，通过统一界面管理



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,935 |
| 语言 | Python |
| Forks | 8,782 |
| Issues | 3,215 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，将深度文档理解与 Agent 智能推理完美融合，提供了从非结构化文档到精准问答的完整 RAG 流程，77k+ stars 证明了其卓越的技术实力和社区认可度。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，实现自主推理与精准检索的协同工作
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel等）的智能解析与结构化提取，提升上下文质量
- GraphRAG 图检索增强：基于知识图谱的语义关联检索，解决传统 RAG 的信息孤岛问题
- MCP（Model Context Protocol）协议支持：标准化的模型上下文交互框架，便于扩展与集成
- 多 LLM 兼容性：无缝支持 OpenAI、Ollama、DeepSeek 等主流大模型，灵活适配不同场景需求

**适用场景**:
- 企业级智能知识库：构建私有化文档问答系统，支持复杂业务文档的深度理解与精准回答
- 复杂文档处理与分析：自动化解析合同、报告、技术文档等，提取关键信息并生成洞察
- 深度研究辅助：基于 GraphRAG 和 Agent 能力，支持多跳推理的复杂研究场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,605 |
| 语言 | TypeScript |
| Forks | 6,977 |
| Issues | 273 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI/LLM 应用设计的网页数据抓取工具，拥有超过10万 Stars，能将任意网页转换为干净的 Markdown 格式，完美解决 AI 代理获取实时网络数据的痛点，是构建 RAG 系统和 AI Agent 的首选数据采集方案。

**技术亮点**:
- AI 优化的数据提取管线：专为 LLM 设计，自动去除广告、导航栏等噪音，输出纯净内容
- HTML 到 Markdown 高质量转换：保留语义结构（标题、列表、代码块、表格等），LLM 可直接理解
- 支持动态渲染页面：可处理 JavaScript 渲染的 SPA 网站和滚动加载内容
- 批量抓取与站点地图生成：支持整站抓取和智能站点地图分析
- 多语言 SDK 与 API 优先设计：提供 TypeScript/Python/Go 等多语言 SDK，便于集成

**适用场景**:
- RAG 和知识库构建：为检索增强生成系统抓取网络文档、新闻、博客等长文本内容
- AI 代理数据采集：为 AI Agent 提供访问任意网页获取信息的能力
- 竞品情报与舆情监控：自动化采集行业网站、电商平台的公开数据
- 内容聚合与数据标注：快速抓取大量网页构建训练数据集



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,223 |
| 语言 | JavaScript |
| Forks | 23,931 |
| Issues | 74 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

一个拥有15万+ Stars 的超高人气 AI Agent 开发框架，为 Claude Code、Cursor 等主流 AI 编程工具提供 Skills、本能、记忆、安全等核心能力扩展，显著提升开发效率

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一抽象层便于迁移
- MCP (Model Context Protocol) 集成：实现工具调用和上下文管理的标准化
- 模块化 Skills & Instincts 系统：提供可复用的技能和本能机制，增强 Agent 任务执行能力
- Memory 持久化机制：内置记忆系统，支持跨会话上下文保持，提升长程任务表现
- Security First 设计：将安全机制内置于核心架构，适合企业级 AI Agent 部署

**适用场景**:
- AI 增强开发团队：构建统一的 AI 编码规范和工具链
- Agent 能力扩展：为 AI 编程工具添加自定义技能、记忆或安全策略
- 企业级 AI 部署：对 AI Agent 有安全性、可审计性要求的企业环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,362 |
| 语言 | Go |
| Forks | 3,942 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，极大降低了 AI 部署门槛，是私有化 AI 解决方案的绝佳选择。

**技术亮点**:
- 纯 CPU 推理支持：无需 GPU 即可运行各类 AI 模型，大大降低部署成本和硬件要求
- 多模型架构兼容：支持 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 统一 API 接口：提供兼容 OpenAI 的 API 服务，方便现有应用快速迁移
- Go 语言实现：高性能、高并发，资源占用优化良好
- 去中心化分布式架构：支持 libp2p 协议，可构建分布式 AI 推理网络

**适用场景**:
- 企业私有 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），需要本地化部署 LLM 和 AI 能力而无需依赖云服务
- 个人开发者/研究者：希望在本地硬件上实验各种开源模型，无需昂贵的 GPU 资源即可体验 AI
- 多模态 AI 应用开发：需要集成文本生成、图像生成、语音合成等多种能力的应用



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,301 |
| 语言 | Python |
| Forks | 10,202 |
| Issues | 3,846 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是 Nous Research 团队开源的多模型 AI Agent 框架，支持 Claude、GPT-4 等主流 LLM，提供灵活的 Agent 编排和工具调用能力，76K+ Stars 表明其在社区中的广泛认可度，适合构建从个人助手到企业级 AI 应用

**技术亮点**:
- 多模型集成支持：原生支持 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 及 Nous Research 自研模型
- 模块化 Agent 架构：可扩展设计，支持工具调用、任务规划和多轮对话
- Python 生态深度整合：便于与 LangChain、HuggingFace 等框架协同工作
- 开源 MIT 许可证：允许商业使用，降低企业采纳门槛
- 配套完善：与 hermes、moltbot、openclaw 等项目形成开源生态

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、文档处理助手、数据分析代理等业务流程自动化
- 开发者效率工具：集成到 IDE 或 CI/CD 流程，实现 AI 辅助编程和代码审查
- 个人 AI 助手搭建：开发私有化智能助手，支持自定义工作流程和知识库集成



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,135 |
| 语言 | TypeScript |
| Forks | 14,913 |
| Issues | 655 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级多代理协作平台，集成多种主流 AI 模型（GPT/Claude/DeepSeek/Gemini），提供 MCP 协议支持，75k+ Stars 验证了其技术成熟度和社区认可度，是构建现代 AI 应用和多代理系统的理想选择。

**技术亮点**:
- 多模型统一集成：无缝支持 OpenAI GPT、Claude、DeepSeek、 Gemini 等主流大模型，提供标准化的 API 抽象层
- 多代理协作框架：支持多智能体协作和团队设计，代理可作为工作交互的基本单元
- MCP (Model Context Protocol) 协议支持：遵循标准化模型上下文协议，实现模型与应用的高效交互
- TypeScript 全栈开发：从前端界面到后端逻辑采用 TypeScript，确保类型安全和开发效率
- 知识库集成能力：内置知识库管理功能，支持 RAG 场景下的文档检索和应用

**适用场景**:
- 企业级 AI 应用开发：构建支持多模型切换的智能客服、文档分析、知识问答等企业应用
- 多代理协作系统：设计代理团队进行复杂任务分解、协作执行，如自动化工作流、代码审查
- AI 应用原型快速开发：开发者可基于该项目快速搭建 AI 应用原型，集成多种模型能力



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,041 |
| 语言 | Python |
| Forks | 8,561 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架之一，支持 100+ 主流大模型统一高效微调，集成 LoRA/QLoRA/RLHF 等多种技术，已被 ACL 2024 收录，适合需要快速落地大模型应用的开发者和企业。

**技术亮点**:
- 统一微调框架：支持 Llama、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及视觉语言模型 VLMs
- 多种高效微调技术：内置 LoRA、QLoRA、Freeze、RLHF（PPO/DPO/KTO）、MoE 等先进方法
- 量化与推理优化：支持 GPTQ/AWQ/BitWise 等多种量化方式，降低部署成本
- ACL 2024 顶会论文验证：技术方案经过学术认可，具备良好的理论基础
- 友好的训练监控：提供 Web UI 界面，支持实时监控训练过程和日志可视化

**适用场景**:
- 企业级 LLM 定制：企业可基于 LlamaFactory 快速微调私有大模型，应用于客服、知识库问答、业务自动化等场景
- AI 研究与实验：研究人员利用其统一接口对比不同微调方法（LoRA vs RLHF）和模型架构的效果，加速论文实验
- 个人开发者微调：开发者可低成本微调开源模型构建垂直领域助手，如法律、医疗、代码生成等专业化应用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,828 |
| 语言 | TypeScript |
| Forks | 4,204 |
| Issues | 235 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,753 |
| 语言 | TypeScript |
| Forks | 8,638 |
| Issues | 79 |
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
| Stars | 43,094 |
| 语言 | Python |
| Forks | 9,901 |
| Issues | 357 |
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
| Stars | 39,367 |
| 语言 | Python |
| Forks | 6,884 |
| Issues | 938 |
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
| Stars | 45,833 |
| 语言 | Java |
| Forks | 15,903 |
| Issues | 41 |
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
| Stars | 38,970 |
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
| Stars | 35,881 |
| 语言 | Python |
| Forks | 4,239 |
| Issues | 93 |
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
| Stars | 33,729 |
| 语言 | TypeScript |
| Forks | 3,650 |
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
| Stars | 105,311 |
| 语言 | Python |
| Forks | 15,377 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,245 |
| 语言 | JavaScript |
| Forks | 6,297 |
| Issues | 324 |
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
| Stars | 71,129 |
| 语言 | Python |
| Forks | 8,937 |
| Issues | 400 |
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
| Stars | 51,258 |
| 语言 | TypeScript |
| Forks | 4,112 |
| Issues | 512 |
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
| Stars | 87,622 |
| 语言 | Python |
| Forks | 10,077 |
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
| Stars | 51,859 |
| 语言 | TypeScript |
| Forks | 24,130 |
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
| Stars | 183,867 |
| 语言 | TypeScript |
| Forks | 56,753 |
| Issues | 1,474 |
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
| Stars | 154,917 |
| 语言 | Java |
| Forks | 46,157 |
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
| Stars | 146,897 |
| 语言 | Python |
| Forks | 8,759 |
| Issues | 956 |
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
| Stars | 56,605 |
| 语言 | Jupyter Notebook |
| Forks | 19,579 |
| Issues | 4 |
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
| Stars | 34,055 |
| 语言 | Python |
| Forks | 2,131 |
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
| Stars | 33,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,532 |
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
| Stars | 44,060 |
| 语言 | Rust |
| Forks | 2,776 |
| Issues | 479 |
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
| Stars | 131,629 |
| 语言 | Python |
| Forks | 18,672 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是最受欢迎的开源 LLM Web 界面之一，通过支持 Ollama、OpenAI API 等多后端和 RAG、MCP 等高级功能，为开发者和企业提供了开箱即用、功能完备的本地 AI 部署方案，大幅降低了自托管 AI 应用的门槛，13万+ Stars 证明了其卓越的实用性和社区认可度。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API，提供统一的接口层
- RAG 检索增强生成：内置完整 RAG 功能，支持文档上传、向量检索和上下文增强
- MCP 协议支持：集成 Model Context Protocol，实现与外部工具的标准化连接
- 自托管部署：提供 Docker 一键部署方案，支持完全私有化，数据不离开本地
- 现代 Web 技术栈：基于 Python 构建，提供响应式界面和实时流式响应

**适用场景**:
- 企业私有化 AI 部署：对数据安全有高要求的企业在本地部署私有 LLM 助手
- 开发者本地调试：快速搭建本地 LLM 测试环境，调试 Prompt 和 RAG 流程
- 多模型统一管理：团队需要同时使用多种 LLM 服务，通过统一界面管理



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,935 |
| 语言 | Python |
| Forks | 8,782 |
| Issues | 3,215 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，将深度文档理解与 Agent 智能推理完美融合，提供了从非结构化文档到精准问答的完整 RAG 流程，77k+ stars 证明了其卓越的技术实力和社区认可度。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，实现自主推理与精准检索的协同工作
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel等）的智能解析与结构化提取，提升上下文质量
- GraphRAG 图检索增强：基于知识图谱的语义关联检索，解决传统 RAG 的信息孤岛问题
- MCP（Model Context Protocol）协议支持：标准化的模型上下文交互框架，便于扩展与集成
- 多 LLM 兼容性：无缝支持 OpenAI、Ollama、DeepSeek 等主流大模型，灵活适配不同场景需求

**适用场景**:
- 企业级智能知识库：构建私有化文档问答系统，支持复杂业务文档的深度理解与精准回答
- 复杂文档处理与分析：自动化解析合同、报告、技术文档等，提取关键信息并生成洞察
- 深度研究辅助：基于 GraphRAG 和 Agent 能力，支持多跳推理的复杂研究场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,135 |
| 语言 | TypeScript |
| Forks | 14,913 |
| Issues | 655 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级多代理协作平台，集成多种主流 AI 模型（GPT/Claude/DeepSeek/Gemini），提供 MCP 协议支持，75k+ Stars 验证了其技术成熟度和社区认可度，是构建现代 AI 应用和多代理系统的理想选择。

**技术亮点**:
- 多模型统一集成：无缝支持 OpenAI GPT、Claude、DeepSeek、 Gemini 等主流大模型，提供标准化的 API 抽象层
- 多代理协作框架：支持多智能体协作和团队设计，代理可作为工作交互的基本单元
- MCP (Model Context Protocol) 协议支持：遵循标准化模型上下文协议，实现模型与应用的高效交互
- TypeScript 全栈开发：从前端界面到后端逻辑采用 TypeScript，确保类型安全和开发效率
- 知识库集成能力：内置知识库管理功能，支持 RAG 场景下的文档检索和应用

**适用场景**:
- 企业级 AI 应用开发：构建支持多模型切换的智能客服、文档分析、知识问答等企业应用
- 多代理协作系统：设计代理团队进行复杂任务分解、协作执行，如自动化工作流、代码审查
- AI 应用原型快速开发：开发者可基于该项目快速搭建 AI 应用原型，集成多种模型能力



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,828 |
| 语言 | TypeScript |
| Forks | 4,204 |
| Issues | 235 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,833 |
| 语言 | Java |
| Forks | 15,903 |
| Issues | 41 |
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
| Stars | 38,970 |
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
| Stars | 35,881 |
| 语言 | Python |
| Forks | 4,239 |
| Issues | 93 |
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
| Stars | 33,729 |
| 语言 | TypeScript |
| Forks | 3,650 |
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
| Stars | 105,311 |
| 语言 | Python |
| Forks | 15,377 |
| Issues | 9 |
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
| Stars | 100,783 |
| 语言 | TypeScript |
| Forks | 12,067 |
| Issues | 970 |
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
| Stars | 58,245 |
| 语言 | JavaScript |
| Forks | 6,297 |
| Issues | 324 |
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
| Stars | 75,509 |
| 语言 | Python |
| Forks | 10,232 |
| Issues | 238 |
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
| Stars | 51,859 |
| 语言 | TypeScript |
| Forks | 24,130 |
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
| Stars | 43,775 |
| 语言 | Go |
| Forks | 3,960 |
| Issues | 1,175 |
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
| Stars | 33,113 |
| 语言 | Python |
| Forks | 4,711 |
| Issues | 205 |
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
| Stars | 34,055 |
| 语言 | Python |
| Forks | 2,131 |
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
| Stars | 33,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,532 |
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
| Stars | 131,629 |
| 语言 | Python |
| Forks | 18,672 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是最受欢迎的开源 LLM Web 界面之一，通过支持 Ollama、OpenAI API 等多后端和 RAG、MCP 等高级功能，为开发者和企业提供了开箱即用、功能完备的本地 AI 部署方案，大幅降低了自托管 AI 应用的门槛，13万+ Stars 证明了其卓越的实用性和社区认可度。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API，提供统一的接口层
- RAG 检索增强生成：内置完整 RAG 功能，支持文档上传、向量检索和上下文增强
- MCP 协议支持：集成 Model Context Protocol，实现与外部工具的标准化连接
- 自托管部署：提供 Docker 一键部署方案，支持完全私有化，数据不离开本地
- 现代 Web 技术栈：基于 Python 构建，提供响应式界面和实时流式响应

**适用场景**:
- 企业私有化 AI 部署：对数据安全有高要求的企业在本地部署私有 LLM 助手
- 开发者本地调试：快速搭建本地 LLM 测试环境，调试 Prompt 和 RAG 流程
- 多模型统一管理：团队需要同时使用多种 LLM 服务，通过统一界面管理



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,935 |
| 语言 | Python |
| Forks | 8,782 |
| Issues | 3,215 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，将深度文档理解与 Agent 智能推理完美融合，提供了从非结构化文档到精准问答的完整 RAG 流程，77k+ stars 证明了其卓越的技术实力和社区认可度。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，实现自主推理与精准检索的协同工作
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel等）的智能解析与结构化提取，提升上下文质量
- GraphRAG 图检索增强：基于知识图谱的语义关联检索，解决传统 RAG 的信息孤岛问题
- MCP（Model Context Protocol）协议支持：标准化的模型上下文交互框架，便于扩展与集成
- 多 LLM 兼容性：无缝支持 OpenAI、Ollama、DeepSeek 等主流大模型，灵活适配不同场景需求

**适用场景**:
- 企业级智能知识库：构建私有化文档问答系统，支持复杂业务文档的深度理解与精准回答
- 复杂文档处理与分析：自动化解析合同、报告、技术文档等，提取关键信息并生成洞察
- 深度研究辅助：基于 GraphRAG 和 Agent 能力，支持多跳推理的复杂研究场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,223 |
| 语言 | JavaScript |
| Forks | 23,931 |
| Issues | 74 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

一个拥有15万+ Stars 的超高人气 AI Agent 开发框架，为 Claude Code、Cursor 等主流 AI 编程工具提供 Skills、本能、记忆、安全等核心能力扩展，显著提升开发效率

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一抽象层便于迁移
- MCP (Model Context Protocol) 集成：实现工具调用和上下文管理的标准化
- 模块化 Skills & Instincts 系统：提供可复用的技能和本能机制，增强 Agent 任务执行能力
- Memory 持久化机制：内置记忆系统，支持跨会话上下文保持，提升长程任务表现
- Security First 设计：将安全机制内置于核心架构，适合企业级 AI Agent 部署

**适用场景**:
- AI 增强开发团队：构建统一的 AI 编码规范和工具链
- Agent 能力扩展：为 AI 编程工具添加自定义技能、记忆或安全策略
- 企业级 AI 部署：对 AI Agent 有安全性、可审计性要求的企业环境



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,301 |
| 语言 | Python |
| Forks | 10,202 |
| Issues | 3,846 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是 Nous Research 团队开源的多模型 AI Agent 框架，支持 Claude、GPT-4 等主流 LLM，提供灵活的 Agent 编排和工具调用能力，76K+ Stars 表明其在社区中的广泛认可度，适合构建从个人助手到企业级 AI 应用

**技术亮点**:
- 多模型集成支持：原生支持 Anthropic (Claude)、OpenAI (ChatGPT/Codex) 及 Nous Research 自研模型
- 模块化 Agent 架构：可扩展设计，支持工具调用、任务规划和多轮对话
- Python 生态深度整合：便于与 LangChain、HuggingFace 等框架协同工作
- 开源 MIT 许可证：允许商业使用，降低企业采纳门槛
- 配套完善：与 hermes、moltbot、openclaw 等项目形成开源生态

**适用场景**:
- 企业级 AI 应用开发：构建客服机器人、文档处理助手、数据分析代理等业务流程自动化
- 开发者效率工具：集成到 IDE 或 CI/CD 流程，实现 AI 辅助编程和代码审查
- 个人 AI 助手搭建：开发私有化智能助手，支持自定义工作流程和知识库集成



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,135 |
| 语言 | TypeScript |
| Forks | 14,913 |
| Issues | 655 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级多代理协作平台，集成多种主流 AI 模型（GPT/Claude/DeepSeek/Gemini），提供 MCP 协议支持，75k+ Stars 验证了其技术成熟度和社区认可度，是构建现代 AI 应用和多代理系统的理想选择。

**技术亮点**:
- 多模型统一集成：无缝支持 OpenAI GPT、Claude、DeepSeek、 Gemini 等主流大模型，提供标准化的 API 抽象层
- 多代理协作框架：支持多智能体协作和团队设计，代理可作为工作交互的基本单元
- MCP (Model Context Protocol) 协议支持：遵循标准化模型上下文协议，实现模型与应用的高效交互
- TypeScript 全栈开发：从前端界面到后端逻辑采用 TypeScript，确保类型安全和开发效率
- 知识库集成能力：内置知识库管理功能，支持 RAG 场景下的文档检索和应用

**适用场景**:
- 企业级 AI 应用开发：构建支持多模型切换的智能客服、文档分析、知识问答等企业应用
- 多代理协作系统：设计代理团队进行复杂任务分解、协作执行，如自动化工作流、代码审查
- AI 应用原型快速开发：开发者可基于该项目快速搭建 AI 应用原型，集成多种模型能力



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,594 |
| 语言 | HTML |
| Forks | 20,910 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万星标，汇集了超过 5000 条精选提示词，覆盖 ChatGPT、Claude、Gemini 等多款主流 AI 助手，支持自托管部署，是个人和团队提升 AI 生产力的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和高类型安全性
- 支持多模型兼容：ChatGPT、Claude、Gemini 等，可灵活切换不同 AI 助手
- 支持自托管部署，提供完整的隐私保护，适合企业内网使用
- 采用开源模式，社区驱动的提示词贡献机制，内容持续迭代更新
- 响应式 Web 应用设计，基于 HTML/CSS/JS 技术栈，部署简单轻量

**适用场景**:
- 企业内部自托管：企业可在私有服务器部署，保护敏感数据，满足合规要求
- AI 应用开发：开发者可参考海量优质提示词优化 LLM 应用和 Prompt Engineering
- 个人效率提升：用户可搜索和使用社区贡献的专业提示词，提升写作、编程、分析等任务效率
- AI 学习研究：研究人员可分析提示词模式，研究人机交互和提示工程最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,669 |
| 语言 | Jupyter Notebook |
| Forks | 13,916 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,828 |
| 语言 | TypeScript |
| Forks | 4,204 |
| Issues | 235 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,753 |
| 语言 | TypeScript |
| Forks | 8,638 |
| Issues | 79 |
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
| Stars | 43,094 |
| 语言 | Python |
| Forks | 9,901 |
| Issues | 357 |
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
| Stars | 39,367 |
| 语言 | Python |
| Forks | 6,884 |
| Issues | 938 |
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
| Stars | 58,245 |
| 语言 | JavaScript |
| Forks | 6,297 |
| Issues | 324 |
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
| Stars | 71,129 |
| 语言 | Python |
| Forks | 8,937 |
| Issues | 400 |
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
| Stars | 51,258 |
| 语言 | TypeScript |
| Forks | 4,112 |
| Issues | 512 |
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
| Stars | 51,859 |
| 语言 | TypeScript |
| Forks | 24,130 |
| Issues | 808 |
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
| Stars | 76,435 |
| 语言 | Python |
| Forks | 15,535 |
| Issues | 4,208 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### shanraisshan/claude-code-best-practice

**描述**: practice made claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,356 |
| 语言 | HTML |
| Forks | 3,918 |
| Issues | 10 |
| Topics | agentic-engineering, anthropic, best-practices, boris, boris-cherny, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, vibe-coding |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,430 |
| 语言 | TypeScript |
| Forks | 4,006 |
| Issues | 1,102 |
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
| Stars | 146,897 |
| 语言 | Python |
| Forks | 8,759 |
| Issues | 956 |
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
| Stars | 168,843 |
| 语言 | Go |
| Forks | 15,572 |
| Issues | 2,927 |
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
| Stars | 47,738 |
| 语言 | Rust |
| Forks | 9,513 |
| Issues | 0 |
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
| Stars | 34,055 |
| 语言 | Python |
| Forks | 2,131 |
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
| Stars | 64,280 |
| 语言 | Python |
| Forks | 6,469 |
| Issues | 90 |
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
| Stars | 106,731 |
| 语言 | Python |
| Forks | 6,714 |
| Issues | 575 |
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
| Stars | 70,041 |
| 语言 | Python |
| Forks | 8,561 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架之一，支持 100+ 主流大模型统一高效微调，集成 LoRA/QLoRA/RLHF 等多种技术，已被 ACL 2024 收录，适合需要快速落地大模型应用的开发者和企业。

**技术亮点**:
- 统一微调框架：支持 Llama、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及视觉语言模型 VLMs
- 多种高效微调技术：内置 LoRA、QLoRA、Freeze、RLHF（PPO/DPO/KTO）、MoE 等先进方法
- 量化与推理优化：支持 GPTQ/AWQ/BitWise 等多种量化方式，降低部署成本
- ACL 2024 顶会论文验证：技术方案经过学术认可，具备良好的理论基础
- 友好的训练监控：提供 Web UI 界面，支持实时监控训练过程和日志可视化

**适用场景**:
- 企业级 LLM 定制：企业可基于 LlamaFactory 快速微调私有大模型，应用于客服、知识库问答、业务自动化等场景
- AI 研究与实验：研究人员利用其统一接口对比不同微调方法（LoRA vs RLHF）和模型架构的效果，加速论文实验
- 个人开发者微调：开发者可低成本微调开源模型构建垂直领域助手，如法律、医疗、代码生成等专业化应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,825 |
| 语言 | Python |
| Forks | 6,545 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，汇聚了股票、加密货币、期权等多元化金融数据源，并深度集成 AI/ML 能力，为量化分析师和 AI 开发者提供一站式的数据获取与处理解决方案。

**技术亮点**:
- 支持多品类金融数据整合，涵盖股票、加密货币、期权、衍生品、固定收益及宏观经济指标
- 内置 AI 和机器学习能力，支持智能化的金融数据分析和预测建模
- 提供标准化的 Python API 接口，便于与现有量化交易系统无缝集成
- 活跃的开源社区支撑，持续更新维护，已获超过 65,000 Stars 验证其可靠性
- 模块化架构设计，支持自定义数据源和分析流程扩展

**适用场景**:
- 量化交易研究：利用标准化数据接口快速获取市场数据，进行回测和策略开发
- 金融数据分析与可视化：整合多数据源进行投资组合分析、风险评估和收益归因
- AI 金融应用开发：构建智能投顾、情感分析、预测模型等 AI 驱动的金融服务
- 企业级金融数据平台：搭建内部研究系统，统一管理金融数据和分析流程



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,594 |
| 语言 | HTML |
| Forks | 20,910 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万星标，汇集了超过 5000 条精选提示词，覆盖 ChatGPT、Claude、Gemini 等多款主流 AI 助手，支持自托管部署，是个人和团队提升 AI 生产力的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和高类型安全性
- 支持多模型兼容：ChatGPT、Claude、Gemini 等，可灵活切换不同 AI 助手
- 支持自托管部署，提供完整的隐私保护，适合企业内网使用
- 采用开源模式，社区驱动的提示词贡献机制，内容持续迭代更新
- 响应式 Web 应用设计，基于 HTML/CSS/JS 技术栈，部署简单轻量

**适用场景**:
- 企业内部自托管：企业可在私有服务器部署，保护敏感数据，满足合规要求
- AI 应用开发：开发者可参考海量优质提示词优化 LLM 应用和 Prompt Engineering
- 个人效率提升：用户可搜索和使用社区贡献的专业提示词，提升写作、编程、分析等任务效率
- AI 学习研究：研究人员可分析提示词模式，研究人机交互和提示工程最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,669 |
| 语言 | Jupyter Notebook |
| Forks | 13,916 |
| Issues | 4 |
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
| Stars | 33,729 |
| 语言 | TypeScript |
| Forks | 3,650 |
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
| Stars | 159,309 |
| 语言 | Python |
| Forks | 32,860 |
| Issues | 2,354 |
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
| Stars | 76,435 |
| 语言 | Python |
| Forks | 15,535 |
| Issues | 4,208 |
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
| Stars | 108,660 |
| 语言 | Python |
| Forks | 12,616 |
| Issues | 3,970 |
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
| Stars | 99,095 |
| 语言 | Python |
| Forks | 27,478 |
| Issues | 18,490 |
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
| Stars | 33,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,532 |
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
| Stars | 154,223 |
| 语言 | JavaScript |
| Forks | 23,931 |
| Issues | 74 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

一个拥有15万+ Stars 的超高人气 AI Agent 开发框架，为 Claude Code、Cursor 等主流 AI 编程工具提供 Skills、本能、记忆、安全等核心能力扩展，显著提升开发效率

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一抽象层便于迁移
- MCP (Model Context Protocol) 集成：实现工具调用和上下文管理的标准化
- 模块化 Skills & Instincts 系统：提供可复用的技能和本能机制，增强 Agent 任务执行能力
- Memory 持久化机制：内置记忆系统，支持跨会话上下文保持，提升长程任务表现
- Security First 设计：将安全机制内置于核心架构，适合企业级 AI Agent 部署

**适用场景**:
- AI 增强开发团队：构建统一的 AI 编码规范和工具链
- Agent 能力扩展：为 AI 编程工具添加自定义技能、记忆或安全策略
- 企业级 AI 部署：对 AI Agent 有安全性、可审计性要求的企业环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,362 |
| 语言 | Go |
| Forks | 3,942 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，极大降低了 AI 部署门槛，是私有化 AI 解决方案的绝佳选择。

**技术亮点**:
- 纯 CPU 推理支持：无需 GPU 即可运行各类 AI 模型，大大降低部署成本和硬件要求
- 多模型架构兼容：支持 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 统一 API 接口：提供兼容 OpenAI 的 API 服务，方便现有应用快速迁移
- Go 语言实现：高性能、高并发，资源占用优化良好
- 去中心化分布式架构：支持 libp2p 协议，可构建分布式 AI 推理网络

**适用场景**:
- 企业私有 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），需要本地化部署 LLM 和 AI 能力而无需依赖云服务
- 个人开发者/研究者：希望在本地硬件上实验各种开源模型，无需昂贵的 GPU 资源即可体验 AI
- 多模态 AI 应用开发：需要集成文本生成、图像生成、语音合成等多种能力的应用



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,129 |
| 语言 | Python |
| Forks | 8,937 |
| Issues | 400 |
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
| Stars | 51,258 |
| 语言 | TypeScript |
| Forks | 4,112 |
| Issues | 512 |
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
| Stars | 183,867 |
| 语言 | TypeScript |
| Forks | 56,753 |
| Issues | 1,474 |
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
| Stars | 156,629 |
| 语言 | Python |
| Forks | 12,891 |
| Issues | 2,468 |
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
| Stars | 97,159 |
| 语言 | Python |
| Forks | 9,068 |
| Issues | 169 |
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
| Stars | 80,923 |
| 语言 | Python |
| Forks | 9,393 |
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
| Stars | 183,786 |
| 语言 | TypeScript |
| Forks | 39,156 |
| Issues | 16,375 |
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
| Stars | 94,108 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 303 |
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
| Stars | 78,901 |
| 语言 | TypeScript |
| Forks | 5,792 |
| Issues | 761 |
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
| Stars | 77,091 |
| 语言 | TypeScript |
| Forks | 6,602 |
| Issues | 138 |
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
| Stars | 79,446 |
| 语言 | Go |
| Forks | 2,767 |
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
| Stars | 76,346 |
| 语言 | Go |
| Forks | 2,750 |
| Issues | 953 |
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
| Stars | 43,799 |
| 语言 | Go |
| Forks | 8,250 |
| Issues | 958 |
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
| Stars | 41,535 |
| 语言 | Go |
| Forks | 1,188 |
| Issues | 168 |
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
| Stars | 421,386 |
| 语言 | Python |
| Forks | 45,886 |
| Issues | 1,239 |
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
| Stars | 75,577 |
| 语言 | JavaScript |
| Forks | 7,281 |
| Issues | 712 |
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
| Stars | 51,258 |
| 语言 | TypeScript |
| Forks | 4,112 |
| Issues | 512 |
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
| Stars | 183,867 |
| 语言 | TypeScript |
| Forks | 56,753 |
| Issues | 1,474 |
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
| Stars | 51,621 |
| 语言 | Go |
| Forks | 10,317 |
| Issues | 232 |
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
| Stars | 121,696 |
| 语言 | Go |
| Forks | 42,845 |
| Issues | 2,739 |
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
| Stars | 71,488 |
| 语言 | Go |
| Forks | 18,915 |
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
| Stars | 54,869 |
| 语言 | Go |
| Forks | 6,568 |
| Issues | 2,825 |
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
| Stars | 47,501 |
| 语言 | Go |
| Forks | 5,043 |
| Issues | 980 |
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
| Stars | 94,108 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 303 |
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
| Stars | 76,691 |
| 语言 | TypeScript |
| Forks | 6,624 |
| Issues | 402 |
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
| Stars | 85,199 |
| 语言 | JavaScript |
| Forks | 7,635 |
| Issues | 718 |
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
| Stars | 69,835 |
| 语言 | Go |
| Forks | 1,909 |
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
| Stars | 62,676 |
| 语言 | Go |
| Forks | 5,907 |
| Issues | 775 |
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
| Stars | 58,824 |
| 语言 | Go |
| Forks | 4,266 |
| Issues | 25 |
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
| Stars | 85,199 |
| 语言 | JavaScript |
| Forks | 7,635 |
| Issues | 718 |
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
| Stars | 63,575 |
| 语言 | Go |
| Forks | 10,332 |
| Issues | 755 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (15 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,362 |
| 语言 | Go |
| Forks | 3,942 |
| Issues | 166 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，极大降低了 AI 部署门槛，是私有化 AI 解决方案的绝佳选择。

**技术亮点**:
- 纯 CPU 推理支持：无需 GPU 即可运行各类 AI 模型，大大降低部署成本和硬件要求
- 多模型架构兼容：支持 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 统一 API 接口：提供兼容 OpenAI 的 API 服务，方便现有应用快速迁移
- Go 语言实现：高性能、高并发，资源占用优化良好
- 去中心化分布式架构：支持 libp2p 协议，可构建分布式 AI 推理网络

**适用场景**:
- 企业私有 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），需要本地化部署 LLM 和 AI 能力而无需依赖云服务
- 个人开发者/研究者：希望在本地硬件上实验各种开源模型，无需昂贵的 GPU 资源即可体验 AI
- 多模态 AI 应用开发：需要集成文本生成、图像生成、语音合成等多种能力的应用



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,159 |
| 语言 | Python |
| Forks | 9,068 |
| Issues | 169 |
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
| Stars | 87,262 |
| 语言 | Python |
| Forks | 33,810 |
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
| Stars | 100,044 |
| 语言 | TypeScript |
| Forks | 27,152 |
| Issues | 1,121 |
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
| Stars | 78,901 |
| 语言 | TypeScript |
| Forks | 5,792 |
| Issues | 761 |
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
| Stars | 68,929 |
| 语言 | JavaScript |
| Forks | 23,105 |
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
| Stars | 55,958 |
| 语言 | JavaScript |
| Forks | 10,214 |
| Issues | 365 |
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
| Stars | 51,788 |
| 语言 | JavaScript |
| Forks | 4,701 |
| Issues | 1,465 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### bigskysoftware/htmx

**描述**: </> htmx - high power tools for HTML

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,809 |
| 语言 | JavaScript |
| Forks | 1,584 |
| Issues | 658 |
| Topics | hateoas, html, htmx, hyperscript, javascript, rest |
| 许可证 | Other |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,302 |
| 语言 | Go |
| Forks | 8,572 |
| Issues | 673 |
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
| Stars | 71,510 |
| 语言 | Go |
| Forks | 4,694 |
| Issues | 254 |
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
| Stars | 57,590 |
| 语言 | Go |
| Forks | 3,282 |
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
| Stars | 41,535 |
| 语言 | Go |
| Forks | 1,188 |
| Issues | 168 |
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
| Stars | 421,386 |
| 语言 | Python |
| Forks | 45,886 |
| Issues | 1,239 |
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
| Stars | 75,577 |
| 语言 | JavaScript |
| Forks | 7,281 |
| Issues | 712 |
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
| Stars | 100,783 |
| 语言 | TypeScript |
| Forks | 12,067 |
| Issues | 970 |
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
| Stars | 58,245 |
| 语言 | JavaScript |
| Forks | 6,297 |
| Issues | 324 |
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
| Stars | 43,775 |
| 语言 | Go |
| Forks | 3,960 |
| Issues | 1,175 |
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
| Stars | 51,621 |
| 语言 | Go |
| Forks | 10,317 |
| Issues | 232 |
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
| Stars | 159,594 |
| 语言 | HTML |
| Forks | 20,910 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万星标，汇集了超过 5000 条精选提示词，覆盖 ChatGPT、Claude、Gemini 等多款主流 AI 助手，支持自托管部署，是个人和团队提升 AI 生产力的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和高类型安全性
- 支持多模型兼容：ChatGPT、Claude、Gemini 等，可灵活切换不同 AI 助手
- 支持自托管部署，提供完整的隐私保护，适合企业内网使用
- 采用开源模式，社区驱动的提示词贡献机制，内容持续迭代更新
- 响应式 Web 应用设计，基于 HTML/CSS/JS 技术栈，部署简单轻量

**适用场景**:
- 企业内部自托管：企业可在私有服务器部署，保护敏感数据，满足合规要求
- AI 应用开发：开发者可参考海量优质提示词优化 LLM 应用和 Prompt Engineering
- 个人效率提升：用户可搜索和使用社区贡献的专业提示词，提升写作、编程、分析等任务效率
- AI 学习研究：研究人员可分析提示词模式，研究人机交互和提示工程最佳实践



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,753 |
| 语言 | TypeScript |
| Forks | 8,638 |
| Issues | 79 |
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
| Stars | 35,881 |
| 语言 | Python |
| Forks | 4,239 |
| Issues | 93 |
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
| Stars | 89,694 |
| 语言 | TypeScript |
| Forks | 10,001 |
| Issues | 2,233 |
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
| Stars | 87,327 |
| 语言 | TypeScript |
| Forks | 8,862 |
| Issues | 1,649 |
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
| Stars | 127,450 |
| 语言 | JavaScript |
| Forks | 12,471 |
| Issues | 2 |
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
| Stars | 169,889 |
| 语言 | Go |
| Forks | 13,138 |
| Issues | 175 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,375 |
| 语言 | Shell |
| Forks | 12,660 |
| Issues | 89 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,928 |
| 语言 | Python |
| Forks | 6,551 |
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
| Stars | 90,163 |
| 语言 | Python |
| Forks | 13,118 |
| Issues | 120 |
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
| Stars | 87,620 |
| 语言 | Python |
| Forks | 7,530 |
| Issues | 632 |
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
| Stars | 135,080 |
| 语言 | Unknown |
| Forks | 33,960 |
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
| Stars | 385,470 |
| 语言 | Python |
| Forks | 66,107 |
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
| Stars | 114,570 |
| 语言 | TypeScript |
| Forks | 5,904 |
| Issues | 128 |
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
| Stars | 110,327 |
| 语言 | TypeScript |
| Forks | 8,020 |
| Issues | 259 |
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
| Stars | 51,974 |
| 语言 | JavaScript |
| Forks | 4,361 |
| Issues | 24 |
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
| Stars | 48,133 |
| 语言 | Go |
| Forks | 10,283 |
| Issues | 1,891 |
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
| Stars | 103,502 |
| 语言 | C++ |
| Forks | 16,797 |
| Issues | 1,484 |
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
| Stars | 71,445 |
| 语言 | TypeScript |
| Forks | 10,059 |
| Issues | 336 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,541 |
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
| Stars | 292,119 |
| 语言 | Python |
| Forks | 27,666 |
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
| Stars | 219,571 |
| 语言 | Python |
| Forks | 50,319 |
| Issues | 921 |
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
| Stars | 86,018 |
| 语言 | Python |
| Forks | 37,231 |
| Issues | 3,632 |
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
| Stars | 77,677 |
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
| Stars | 76,863 |
| 语言 | Python |
| Forks | 16,842 |
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
| Stars | 442,798 |
| 语言 | TypeScript |
| Forks | 44,274 |
| Issues | 200 |
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
| Stars | 352,848 |
| 语言 | TypeScript |
| Forks | 43,907 |
| Issues | 7 |
| Topics | angular-roadmap, backend-roadmap, blockchain-roadmap, computer-science, dba-roadmap, developer-roadmap, devops-roadmap, frontend-roadmap, go-roadmap, java-roadmap, javascript-roadmap, nodejs-roadmap, python-roadmap, qa-roadmap, react-roadmap, roadmap, software-architect-roadmap, vue-roadmap |
| 许可证 | Other |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,707 |
| 语言 | TypeScript |
| Forks | 16,495 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### excalidraw/excalidraw

**描述**: Virtual whiteboard for sketching hand-drawn like diagrams

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,957 |
| 语言 | TypeScript |
| Forks | 13,256 |
| Issues | 2,959 |
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
| Stars | 112,251 |
| 语言 | TypeScript |
| Forks | 8,511 |
| Issues | 1,813 |
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
| Stars | 108,535 |
| 语言 | TypeScript |
| Forks | 13,346 |
| Issues | 5,028 |
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
| Stars | 97,786 |
| 语言 | TypeScript |
| Forks | 5,374 |
| Issues | 712 |
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
| Stars | 97,761 |
| 语言 | TypeScript |
| Forks | 54,588 |
| Issues | 1,355 |
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
| Stars | 94,541 |
| 语言 | TypeScript |
| Forks | 5,190 |
| Issues | 110 |
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
| Stars | 79,888 |
| 语言 | TypeScript |
| Forks | 8,054 |
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
| Stars | 244,457 |
| 语言 | JavaScript |
| Forks | 50,911 |
| Issues | 1,219 |
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
| Stars | 116,699 |
| 语言 | JavaScript |
| Forks | 35,334 |
| Issues | 2,602 |
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
| Stars | 111,904 |
| 语言 | JavaScript |
| Forks | 36,326 |
| Issues | 558 |
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
| Stars | 108,999 |
| 语言 | JavaScript |
| Forks | 11,626 |
| Issues | 261 |
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
| Stars | 98,140 |
| 语言 | JavaScript |
| Forks | 32,688 |
| Issues | 1,671 |
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
| Stars | 95,585 |
| 语言 | JavaScript |
| Forks | 15,351 |
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
| Stars | 86,296 |
| 语言 | JavaScript |
| Forks | 4,888 |
| Issues | 980 |
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
| Stars | 70,984 |
| 语言 | JavaScript |
| Forks | 16,811 |
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
| Stars | 66,312 |
| 语言 | JavaScript |
| Forks | 9,187 |
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
| Stars | 65,837 |
| 语言 | JavaScript |
| Forks | 9,377 |
| Issues | 204 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,404 |
| 语言 | JavaScript |
| Forks | 5,649 |
| Issues | 71 |
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
| Forks | 20,475 |
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
| Stars | 57,429 |
| 语言 | JavaScript |
| Forks | 12,308 |
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
| Stars | 53,120 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 456 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,482 |
| 语言 | JavaScript |
| Forks | 11,466 |
| Issues | 238 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,624 |
| 语言 | JavaScript |
| Forks | 2,428 |
| Issues | 1,210 |
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
| Stars | 133,461 |
| 语言 | Go |
| Forks | 18,915 |
| Issues | 9,976 |
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
| Stars | 105,858 |
| 语言 | Go |
| Forks | 14,985 |
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
| Stars | 87,568 |
| 语言 | Go |
| Forks | 8,240 |
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
| Stars | 81,687 |
| 语言 | Go |
| Forks | 4,993 |
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
| Stars | 68,629 |
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
| Stars | 56,616 |
| 语言 | Go |
| Forks | 5,023 |
| Issues | 1,159 |
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
| Stars | 50,979 |
| 语言 | Go |
| Forks | 21,884 |
| Issues | 395 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,607 |
| 语言 | Python |
| Forks | 55,353 |
| Issues | 526 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 97,682 |
| 语言 | Python |
| Forks | 12,033 |
| Issues | 119 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,993 |
| 语言 | Python |
| Forks | 7,210 |
| Issues | 484 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,662 |
| 语言 | TypeScript |
| Forks | 10,367 |
| Issues | 734 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,085 |
| 语言 | TypeScript |
| Forks | 7,581 |
| Issues | 34 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,028 |
| 语言 | JavaScript |
| Forks | 32,499 |
| Issues | 278 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 62,731 |
| 语言 | JavaScript |
| Forks | 4,009 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,323 |
| 语言 | JavaScript |
| Forks | 7,130 |
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
| Stars | 50,626 |
| 语言 | Go |
| Forks | 1,595 |
| Issues | 267 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,302 |
| 语言 | Go |
| Forks | 7,957 |
| Issues | 563 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 150,882 |
| 语言 | Python |
| Forks | 11,487 |
| Issues | 326 |
| Topics | awesome, github, hellogithub, python |
