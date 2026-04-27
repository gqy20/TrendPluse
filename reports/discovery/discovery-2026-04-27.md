# 项目发现报告 (2026-04-27)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 128 |
| 去重移除 | 33 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 22 |
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


## 🤖 AI Agents (28 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,467 |
| 语言 | Python |
| Forks | 19,111 |
| Issues | 281 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面项目，拥有超过 13 万星标，支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG 和 MCP 等企业级功能，特别适合需要私有化部署、注重数据隐私的企业和开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 等多种 LLM 服务，提供统一的 Web 交互界面
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的深度集成
- 自托管部署：完全开源可私有部署，数据不离开本地环境，保障隐私安全
- OpenAPI 兼容：提供标准 REST API，方便与现有系统集成和二次开发

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有要求、需要定制化 AI 助手的企业环境
- 开发者快速构建 AI 应用：提供完整的 UI 和 API，可快速集成到现有产品中
- 个人 AI 助手搭建：支持本地部署，用户可拥有完全控制权的私人 AI 界面



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,370 |
| 语言 | Python |
| Forks | 17,882 |
| Issues | 6,831 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-Agent 是由知名开源 AI 研究组织 NousResearch 打造的生产级 AI Agent 框架，拥有超过 12 万 Stars 的高人气，支持 Claude、GPT 等多主流 LLM 接入，具备高度模块化和可扩展性，适合快速构建企业级智能代理应用。

**技术亮点**:
- 多模型统一接入：支持 Anthropic Claude、OpenAI GPT 等多种大语言模型，提供统一接口，灵活切换不同 AI 提供商
- 模块化 Agent 架构：采用可插拔设计，工具调用、任务规划、记忆管理等核心模块解耦，便于二次开发和定制
- 活跃开源生态：12 万 + Stars 验证其成熟度和社区活跃度，持续迭代维护，问题响应迅速
- MIT 许可证：完全开源，商用友好，降低企业使用门槛
- 专注于 Claude Code 集成：深度整合 Claude 的代码能力，支持自动化编程和代码分析场景

**适用场景**:
- 企业智能客服与自动化流程：快速集成到现有业务系统，实现多轮对话、任务自动化处理
- AI 辅助编程与代码分析：利用 Claude Code 能力构建代码审查、自动化测试、代码生成等开发工具
- 个人开发者构建 AI 原生应用：借助成熟框架快速原型验证，聚焦业务逻辑而非底层实现



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 168,287 |
| 语言 | JavaScript |
| Forks | 26,080 |
| Issues | 172 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码助手的性能优化系统，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，Stars 高达 168k 证明了其在开发者社区的广泛认可和实用性。

**技术亮点**:
- 提供 Skills 和 Instincts 机制，支持开发者自定义 AI 助手的技能和行为模式
- 内置 Memory 模块，实现跨会话的上下文保持和知识复用
- 安全沙箱机制，保障 AI Agent 操作的安全性和可控性
- 支持多平台 AI 编码助手（Claude Code, Codex, Cursor, Opencode）
- 采用 Research-First 开发理念，融入前沿 AI Agent 研究成果

**适用场景**:
- 个人开发者提升编程效率 - 通过自定义 Skills 和 Instincts 优化个人工作流
- 企业团队 AI 编码规范落地 - 利用 Memory 模块统一团队级上下文和编码规范
- AI Agent 安全审计与优化 - 在生产环境中部署前进行安全沙箱测试



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,877 |
| 语言 | Go |
| Forks | 4,030 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 部署解决方案，支持 LLM、视觉、语音、图像、视频等多模态模型，无需 GPU 即可在普通硬件上运行，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、图像生成、语音合成、目标检测、音乐生成等多种模型类型
- 零 GPU 依赖：可在 CPU 和普通硬件上运行，降低 AI 部署门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用快速迁移
- Go 语言实现：利用 Go 的高性能和并发特性，支持高吞吐量推理

**适用场景**:
- 本地隐私敏感场景：医疗、金融、法律等需要数据不出本地的行业，可用 LocalAI 构建私有化 AI 应用
- 边缘设备部署：在没有强大 GPU 的边缘设备或嵌入式系统上运行 AI 推理任务
- 开发测试环境：开发者可在本地快速验证 AI 应用，无需依赖云服务或支付 API 费用
- MCP 协议实现：支持 Model Context Protocol，用于构建 AI Agents 和自动化工作流



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,731 |
| 语言 | TypeScript |
| Forks | 15,020 |
| Issues | 744 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度成熟的多 Agent 协作平台，拥有超过 7.5 万 Stars 的活跃社区支持。它不仅支持 GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，还提供了开箱即用的 Agent 团队设计和 MCP 协议集成，是构建下一代 AI 应用的首选框架。

**技术亮点**:
- 多 Agent 协作框架：支持多智能体协同工作，实现复杂任务的分工与协作
- 多模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：符合 Model Context Protocol 标准，便于扩展和集成第三方工具
- Agent 团队设计工具：提供可视化的方式设计和编排多个 Agent 的协作流程
- 知识库集成：内置 RAG 能力，支持 Agent 访问和利用私有知识库

**适用场景**:
- 企业 AI 自动化办公：构建多 Agent 团队处理文档分析、数据报告生成、会议纪要等办公任务
- 智能客服系统：利用 Agent 协作实现复杂问题的分流处理和精准回复
- 个人 AI 助手套件：打造具备多种专业能力的个人 AI 团队，涵盖写作、编程、研究等场景



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,674 |
| 语言 | Python |
| Forks | 8,634 |
| Issues | 992 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 顶会接收的大模型微调框架，提供统一高效的 100+ LLM/VLM 微调方案，其模块化设计让 LoRA、QLoRA、RLHF 等前沿技术开箱即用，大幅降低了大模型定制化的门槛。

**技术亮点**:
- 支持 100+ 大语言模型和视觉语言模型统一微调，涵盖 Llama、Qwen、Gemma、DeepSeek 等主流架构
- 集成 LoRA、QLoRA、Prefix-Tuning 等 PEFT 技术，支持 RLHF (PPO/DPO/KTO) 强化学习训练
- 支持 MoE 混合专家架构和 INT4/INT8/FP8 量化压缩，显著降低显存占用
- 提供模块化训练流程设计，支持预训练、指令微调、奖励建模、PPO 训练等完整生命周期
- 兼容 Transformers 生态，提供 WebUI 和 CLI 工具链，降低使用门槛

**适用场景**:
- 企业级 LLM 定制：利用自有数据快速微调领域专用模型（如金融、医疗、法律）
- 个人开发者：使用 QLoRA 在消费级 GPU 上微调大模型，降低 AI 应用开发成本
- AI 研究：快速复现和对比不同微调方法（LoRA vs RLHF vs MoE）的效果差异
- 多模态应用：支持 LLaVA 等视觉语言模型的微调，构建视觉问答或图像理解系统



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,480 |
| 语言 | TypeScript |
| Forks | 5,832 |
| Issues | 16 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这个项目为 Claude Code 用户提供了缺失已久的长期记忆能力，通过自动捕获、压缩和检索编码上下文，解决了 AI 编码助手"每次会话从零开始"的核心痛点。基于 68,480 Stars 的热度验证，它已成为 AI 辅助编程领域的基础设施级项目，特别适合处理复杂的多会话项目开发场景。

**技术亮点**:
- 智能记忆压缩引擎: 利用 Claude 自身的 agent-sdk 实现 AI 驱动的上下文压缩，将冗长的会话历史提炼为精简但保留关键信息的记忆片段
- ChromaDB 向量检索系统: 采用 ChromaDB 作为向量数据库，通过语义 embeddings 技术实现精准的记忆检索，确保从海量历史上下文中提取最相关的内容
- 多框架协同架构: 融合了 Mem0、OpenMemory、Supermemory 等先进记忆框架的设计理念，构建了 RAG + 长期记忆的混合架构
- SQLite 本地持久化存储: 使用轻量级 SQLite 作为存储后端，既保证了数据隐私性，又提供了可靠的跨会话持久化能力
- 零侵入式插件集成: 作为 Claude Code 插件形式交付，无需修改现有工作流即可无缝增强 AI 编程体验

**适用场景**:
- 复杂项目的长期开发: 大型代码库或长期维护项目中，Claude 能够自动记住设计决策、API 用法、曾遇到的问题和解决方案，避免重复探索
- 多会话上下文保持: 需要数天甚至数周完成的复杂功能开发中，自动保留之前的实现思路、重构记录和技术选型理由，确保上下文连贯性
- 团队知识传承: 开发者之间的项目交接变得顺畅，接手者可以获得前人的编码上下文和决策历史，大幅缩短上手时间



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,575 |
| 语言 | HTML |
| Forks | 4,792 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个专注于Claude Code实践的权威指南库，拥有近5万Star的超高人气，从vibe coding入门到agentic engineering进阶提供了完整的学习路径，帮助开发者快速掌握AI辅助编程的最佳实践和方法论。

**技术亮点**:
- 提供了丰富的Claude Code命令和技巧集合，涵盖日常开发高频场景
- 系统性地讲解了Context Engineering（上下文工程）的实践方法，提升AI理解代码能力
- 包含Agentic Workflow（智能体工作流）的设计模式和最佳实践
- 整理了从基础vibe coding到高级agentic engineering的渐进式学习路径
- 涵盖了多个实战主题如AI agents、多智能体协作等前沿技术

**适用场景**:
- 个人开发者学习AI辅助编程，提升开发效率和代码质量
- 企业团队建立AI编程规范，推广Claude Code的最佳实践
- 学习agentic engineering和智能体开发的方法论和实战技巧



### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,773 |
| 语言 | Python |
| Forks | 10,000 |
| Issues | 353 |
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
| Stars | 45,990 |
| 语言 | Java |
| Forks | 15,951 |
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
| Stars | 41,165 |
| 语言 | Python |
| Forks | 4,955 |
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
| Stars | 39,064 |
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
| Stars | 112,650 |
| 语言 | TypeScript |
| Forks | 7,178 |
| Issues | 293 |
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
| Stars | 59,101 |
| 语言 | JavaScript |
| Forks | 6,384 |
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
| Stars | 72,189 |
| 语言 | Python |
| Forks | 9,116 |
| Issues | 413 |
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
| Stars | 54,522 |
| 语言 | TypeScript |
| Forks | 4,423 |
| Issues | 653 |
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
| Stars | 107,788 |
| 语言 | Python |
| Forks | 15,869 |
| Issues | 3 |
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
| Stars | 90,734 |
| 语言 | Python |
| Forks | 10,346 |
| Issues | 223 |
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
| Stars | 52,321 |
| 语言 | TypeScript |
| Forks | 24,231 |
| Issues | 825 |
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
| Stars | 185,845 |
| 语言 | TypeScript |
| Forks | 57,180 |
| Issues | 1,556 |
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
| Stars | 155,252 |
| 语言 | Java |
| Forks | 46,153 |
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
| Stars | 147,426 |
| 语言 | Python |
| Forks | 8,862 |
| Issues | 952 |
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
| Stars | 59,839 |
| 语言 | Jupyter Notebook |
| Forks | 20,249 |
| Issues | 3 |
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
| Stars | 56,656 |
| 语言 | Python |
| Forks | 6,102 |
| Issues | 561 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,951 |
| 语言 | TypeScript |
| Forks | 9,361 |
| Issues | 107 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,015 |
| 语言 | TypeScript |
| Forks | 3,705 |
| Issues | 299 |
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
| Stars | 33,697 |
| 语言 | TypeScript |
| Forks | 3,817 |
| Issues | 494 |
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
| Stars | 52,774 |
| 语言 | Rust |
| Forks | 3,413 |
| Issues | 634 |
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
| Stars | 134,467 |
| 语言 | Python |
| Forks | 19,111 |
| Issues | 281 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面项目，拥有超过 13 万星标，支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG 和 MCP 等企业级功能，特别适合需要私有化部署、注重数据隐私的企业和开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 等多种 LLM 服务，提供统一的 Web 交互界面
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的深度集成
- 自托管部署：完全开源可私有部署，数据不离开本地环境，保障隐私安全
- OpenAPI 兼容：提供标准 REST API，方便与现有系统集成和二次开发

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有要求、需要定制化 AI 助手的企业环境
- 开发者快速构建 AI 应用：提供完整的 UI 和 API，可快速集成到现有产品中
- 个人 AI 助手搭建：支持本地部署，用户可拥有完全控制权的私人 AI 界面



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,731 |
| 语言 | TypeScript |
| Forks | 15,020 |
| Issues | 744 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度成熟的多 Agent 协作平台，拥有超过 7.5 万 Stars 的活跃社区支持。它不仅支持 GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，还提供了开箱即用的 Agent 团队设计和 MCP 协议集成，是构建下一代 AI 应用的首选框架。

**技术亮点**:
- 多 Agent 协作框架：支持多智能体协同工作，实现复杂任务的分工与协作
- 多模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：符合 Model Context Protocol 标准，便于扩展和集成第三方工具
- Agent 团队设计工具：提供可视化的方式设计和编排多个 Agent 的协作流程
- 知识库集成：内置 RAG 能力，支持 Agent 访问和利用私有知识库

**适用场景**:
- 企业 AI 自动化办公：构建多 Agent 团队处理文档分析、数据报告生成、会议纪要等办公任务
- 智能客服系统：利用 Agent 协作实现复杂问题的分流处理和精准回复
- 个人 AI 助手套件：打造具备多种专业能力的个人 AI 团队，涵盖写作、编程、研究等场景



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,480 |
| 语言 | TypeScript |
| Forks | 5,832 |
| Issues | 16 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这个项目为 Claude Code 用户提供了缺失已久的长期记忆能力，通过自动捕获、压缩和检索编码上下文，解决了 AI 编码助手"每次会话从零开始"的核心痛点。基于 68,480 Stars 的热度验证，它已成为 AI 辅助编程领域的基础设施级项目，特别适合处理复杂的多会话项目开发场景。

**技术亮点**:
- 智能记忆压缩引擎: 利用 Claude 自身的 agent-sdk 实现 AI 驱动的上下文压缩，将冗长的会话历史提炼为精简但保留关键信息的记忆片段
- ChromaDB 向量检索系统: 采用 ChromaDB 作为向量数据库，通过语义 embeddings 技术实现精准的记忆检索，确保从海量历史上下文中提取最相关的内容
- 多框架协同架构: 融合了 Mem0、OpenMemory、Supermemory 等先进记忆框架的设计理念，构建了 RAG + 长期记忆的混合架构
- SQLite 本地持久化存储: 使用轻量级 SQLite 作为存储后端，既保证了数据隐私性，又提供了可靠的跨会话持久化能力
- 零侵入式插件集成: 作为 Claude Code 插件形式交付，无需修改现有工作流即可无缝增强 AI 编程体验

**适用场景**:
- 复杂项目的长期开发: 大型代码库或长期维护项目中，Claude 能够自动记住设计决策、API 用法、曾遇到的问题和解决方案，避免重复探索
- 多会话上下文保持: 需要数天甚至数周完成的复杂功能开发中，自动保留之前的实现思路、重构记录和技术选型理由，确保上下文连贯性
- 团队知识传承: 开发者之间的项目交接变得顺畅，接手者可以获得前人的编码上下文和决策历史，大幅缩短上手时间



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,990 |
| 语言 | Java |
| Forks | 15,951 |
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
| Stars | 41,165 |
| 语言 | Python |
| Forks | 4,955 |
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
| Stars | 39,064 |
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
| Stars | 101,497 |
| 语言 | TypeScript |
| Forks | 12,196 |
| Issues | 963 |
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
| Stars | 59,101 |
| 语言 | JavaScript |
| Forks | 6,384 |
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
| Stars | 107,788 |
| 语言 | Python |
| Forks | 15,869 |
| Issues | 3 |
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
| Stars | 76,693 |
| 语言 | Python |
| Forks | 10,328 |
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
| Stars | 52,321 |
| 语言 | TypeScript |
| Forks | 24,231 |
| Issues | 825 |
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
| Stars | 44,011 |
| 语言 | Go |
| Forks | 3,980 |
| Issues | 1,099 |
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
| Stars | 34,409 |
| 语言 | Python |
| Forks | 4,860 |
| Issues | 216 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### microsoft/graphrag

**描述**: A modular graph-based Retrieval-Augmented Generation (RAG) system

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,547 |
| 语言 | Python |
| Forks | 3,430 |
| Issues | 104 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,015 |
| 语言 | TypeScript |
| Forks | 3,705 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (22 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,467 |
| 语言 | Python |
| Forks | 19,111 |
| Issues | 281 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面项目，拥有超过 13 万星标，支持 Ollama、OpenAI API 等多种 LLM 后端，并集成 RAG 和 MCP 等企业级功能，特别适合需要私有化部署、注重数据隐私的企业和开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 等多种 LLM 服务，提供统一的 Web 交互界面
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的深度集成
- 自托管部署：完全开源可私有部署，数据不离开本地环境，保障隐私安全
- OpenAPI 兼容：提供标准 REST API，方便与现有系统集成和二次开发

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有要求、需要定制化 AI 助手的企业环境
- 开发者快速构建 AI 应用：提供完整的 UI 和 API，可快速集成到现有产品中
- 个人 AI 助手搭建：支持本地部署，用户可拥有完全控制权的私人 AI 界面



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,370 |
| 语言 | Python |
| Forks | 17,882 |
| Issues | 6,831 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-Agent 是由知名开源 AI 研究组织 NousResearch 打造的生产级 AI Agent 框架，拥有超过 12 万 Stars 的高人气，支持 Claude、GPT 等多主流 LLM 接入，具备高度模块化和可扩展性，适合快速构建企业级智能代理应用。

**技术亮点**:
- 多模型统一接入：支持 Anthropic Claude、OpenAI GPT 等多种大语言模型，提供统一接口，灵活切换不同 AI 提供商
- 模块化 Agent 架构：采用可插拔设计，工具调用、任务规划、记忆管理等核心模块解耦，便于二次开发和定制
- 活跃开源生态：12 万 + Stars 验证其成熟度和社区活跃度，持续迭代维护，问题响应迅速
- MIT 许可证：完全开源，商用友好，降低企业使用门槛
- 专注于 Claude Code 集成：深度整合 Claude 的代码能力，支持自动化编程和代码分析场景

**适用场景**:
- 企业智能客服与自动化流程：快速集成到现有业务系统，实现多轮对话、任务自动化处理
- AI 辅助编程与代码分析：利用 Claude Code 能力构建代码审查、自动化测试、代码生成等开发工具
- 个人开发者构建 AI 原生应用：借助成熟框架快速原型验证，聚焦业务逻辑而非底层实现



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 168,287 |
| 语言 | JavaScript |
| Forks | 26,080 |
| Issues | 172 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码助手的性能优化系统，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，Stars 高达 168k 证明了其在开发者社区的广泛认可和实用性。

**技术亮点**:
- 提供 Skills 和 Instincts 机制，支持开发者自定义 AI 助手的技能和行为模式
- 内置 Memory 模块，实现跨会话的上下文保持和知识复用
- 安全沙箱机制，保障 AI Agent 操作的安全性和可控性
- 支持多平台 AI 编码助手（Claude Code, Codex, Cursor, Opencode）
- 采用 Research-First 开发理念，融入前沿 AI Agent 研究成果

**适用场景**:
- 个人开发者提升编程效率 - 通过自定义 Skills 和 Instincts 优化个人工作流
- 企业团队 AI 编码规范落地 - 利用 Memory 模块统一团队级上下文和编码规范
- AI Agent 安全审计与优化 - 在生产环境中部署前进行安全沙箱测试



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,731 |
| 语言 | TypeScript |
| Forks | 15,020 |
| Issues | 744 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度成熟的多 Agent 协作平台，拥有超过 7.5 万 Stars 的活跃社区支持。它不仅支持 GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，还提供了开箱即用的 Agent 团队设计和 MCP 协议集成，是构建下一代 AI 应用的首选框架。

**技术亮点**:
- 多 Agent 协作框架：支持多智能体协同工作，实现复杂任务的分工与协作
- 多模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 LLM 提供商
- MCP 协议支持：符合 Model Context Protocol 标准，便于扩展和集成第三方工具
- Agent 团队设计工具：提供可视化的方式设计和编排多个 Agent 的协作流程
- 知识库集成：内置 RAG 能力，支持 Agent 访问和利用私有知识库

**适用场景**:
- 企业 AI 自动化办公：构建多 Agent 团队处理文档分析、数据报告生成、会议纪要等办公任务
- 智能客服系统：利用 Agent 协作实现复杂问题的分流处理和精准回复
- 个人 AI 助手套件：打造具备多种专业能力的个人 AI 团队，涵盖写作、编程、研究等场景



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,480 |
| 语言 | TypeScript |
| Forks | 5,832 |
| Issues | 16 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这个项目为 Claude Code 用户提供了缺失已久的长期记忆能力，通过自动捕获、压缩和检索编码上下文，解决了 AI 编码助手"每次会话从零开始"的核心痛点。基于 68,480 Stars 的热度验证，它已成为 AI 辅助编程领域的基础设施级项目，特别适合处理复杂的多会话项目开发场景。

**技术亮点**:
- 智能记忆压缩引擎: 利用 Claude 自身的 agent-sdk 实现 AI 驱动的上下文压缩，将冗长的会话历史提炼为精简但保留关键信息的记忆片段
- ChromaDB 向量检索系统: 采用 ChromaDB 作为向量数据库，通过语义 embeddings 技术实现精准的记忆检索，确保从海量历史上下文中提取最相关的内容
- 多框架协同架构: 融合了 Mem0、OpenMemory、Supermemory 等先进记忆框架的设计理念，构建了 RAG + 长期记忆的混合架构
- SQLite 本地持久化存储: 使用轻量级 SQLite 作为存储后端，既保证了数据隐私性，又提供了可靠的跨会话持久化能力
- 零侵入式插件集成: 作为 Claude Code 插件形式交付，无需修改现有工作流即可无缝增强 AI 编程体验

**适用场景**:
- 复杂项目的长期开发: 大型代码库或长期维护项目中，Claude 能够自动记住设计决策、API 用法、曾遇到的问题和解决方案，避免重复探索
- 多会话上下文保持: 需要数天甚至数周完成的复杂功能开发中，自动保留之前的实现思路、重构记录和技术选型理由，确保上下文连贯性
- 团队知识传承: 开发者之间的项目交接变得顺畅，接手者可以获得前人的编码上下文和决策历史，大幅缩短上手时间



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,908 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

16万星标的提示词宝库，前身是知名Awesome ChatGPT Prompts项目，支持多LLM平台和自托管部署，适合个人和企业追求隐私保护的场景。

**技术亮点**:
- 多LLM平台支持：兼容ChatGPT、Claude、Gemini、GPT-4等主流大语言模型
- 现代化技术栈：基于Next.js + TypeScript构建，具备良好开发体验和类型安全
- 自托管部署：提供完整开源代码，支持私有化部署确保数据隐私
- 社区驱动：活跃的开源社区持续贡献高质量提示词
- 丰富的Topics覆盖：包含AI、机器学习、提示词工程等多个相关领域

**适用场景**:
- 个人开发者快速获取高质量提示词，提升AI工具使用效率
- 企业团队自托管部署实现完全私有化，避免敏感数据外泄
- AI爱好者学习提示词工程技巧，探索不同LLM的最佳实践



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,575 |
| 语言 | HTML |
| Forks | 4,792 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个专注于Claude Code实践的权威指南库，拥有近5万Star的超高人气，从vibe coding入门到agentic engineering进阶提供了完整的学习路径，帮助开发者快速掌握AI辅助编程的最佳实践和方法论。

**技术亮点**:
- 提供了丰富的Claude Code命令和技巧集合，涵盖日常开发高频场景
- 系统性地讲解了Context Engineering（上下文工程）的实践方法，提升AI理解代码能力
- 包含Agentic Workflow（智能体工作流）的设计模式和最佳实践
- 整理了从基础vibe coding到高级agentic engineering的渐进式学习路径
- 涵盖了多个实战主题如AI agents、多智能体协作等前沿技术

**适用场景**:
- 个人开发者学习AI辅助编程，提升开发效率和代码质量
- 企业团队建立AI编程规范，推广Claude Code的最佳实践
- 学习agentic engineering和智能体开发的方法论和实战技巧



### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,773 |
| 语言 | Python |
| Forks | 10,000 |
| Issues | 353 |
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
| Stars | 59,101 |
| 语言 | JavaScript |
| Forks | 6,384 |
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
| Stars | 72,189 |
| 语言 | Python |
| Forks | 9,116 |
| Issues | 413 |
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
| Stars | 54,522 |
| 语言 | TypeScript |
| Forks | 4,423 |
| Issues | 653 |
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
| Stars | 52,321 |
| 语言 | TypeScript |
| Forks | 24,231 |
| Issues | 825 |
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
| Stars | 78,325 |
| 语言 | Python |
| Forks | 16,161 |
| Issues | 4,549 |
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
| Stars | 147,426 |
| 语言 | Python |
| Forks | 8,862 |
| Issues | 952 |
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
| Stars | 56,656 |
| 语言 | Python |
| Forks | 6,102 |
| Issues | 561 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,161 |
| 语言 | Go |
| Forks | 15,842 |
| Issues | 3,085 |
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
| Stars | 91,587 |
| 语言 | Jupyter Notebook |
| Forks | 14,100 |
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
| Stars | 56,951 |
| 语言 | TypeScript |
| Forks | 9,361 |
| Issues | 107 |
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
| Stars | 48,190 |
| 语言 | Rust |
| Forks | 9,645 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 48,005 |
| 语言 | Python |
| Forks | 2,541 |
| Issues | 163 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,885 |
| 语言 | Python |
| Forks | 7,748 |
| Issues | 640 |
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
| Stars | 71,301 |
| 语言 | Python |
| Forks | 7,333 |
| Issues | 136 |
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
| Stars | 70,674 |
| 语言 | Python |
| Forks | 8,634 |
| Issues | 992 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 顶会接收的大模型微调框架，提供统一高效的 100+ LLM/VLM 微调方案，其模块化设计让 LoRA、QLoRA、RLHF 等前沿技术开箱即用，大幅降低了大模型定制化的门槛。

**技术亮点**:
- 支持 100+ 大语言模型和视觉语言模型统一微调，涵盖 Llama、Qwen、Gemma、DeepSeek 等主流架构
- 集成 LoRA、QLoRA、Prefix-Tuning 等 PEFT 技术，支持 RLHF (PPO/DPO/KTO) 强化学习训练
- 支持 MoE 混合专家架构和 INT4/INT8/FP8 量化压缩，显著降低显存占用
- 提供模块化训练流程设计，支持预训练、指令微调、奖励建模、PPO 训练等完整生命周期
- 兼容 Transformers 生态，提供 WebUI 和 CLI 工具链，降低使用门槛

**适用场景**:
- 企业级 LLM 定制：利用自有数据快速微调领域专用模型（如金融、医疗、法律）
- 个人开发者：使用 QLoRA 在消费级 GPU 上微调大模型，降低 AI 应用开发成本
- AI 研究：快速复现和对比不同微调方法（LoRA vs RLHF vs MoE）的效果差异
- 多模态应用：支持 LLaVA 等视觉语言模型的微调，构建视觉问答或图像理解系统



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,605 |
| 语言 | Python |
| Forks | 6,654 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是当前最完整的开源金融数据平台之一，拥有超过 66k Stars，专为量化分析师、交易员和 AI 代理设计，支持股票、加密货币、期权等多元化资产类别的一站式数据获取与技术分析，大幅提升投资研究效率。

**技术亮点**:
- 多数据源聚合引擎：整合多个免费和付费数据源（Yahoo Finance、CoinGecko、FRED 等），提供统一的数据 API 访问接口
- AI/ML 原生集成：内置机器学习模型支持，支持情感分析、预测模型等 AI 辅助功能，可作为 AI Agent 的金融数据后端
- 全资产类别覆盖：支持股票、加密货币、期权、期货、固定收益、外汇等多个市场的高质量数据获取与处理
- 模块化架构设计：采用插件式扩展系统，支持社区贡献的数据源和分析工具，便于企业级定制与集成
- 专业量化工具集：提供技术指标计算、因子分析、组合优化等专业量化金融功能，开箱即用

**适用场景**:
- 量化研究与投资分析：分析师和宽客可快速获取多市场数据、进行技术分析和回测，加速投资策略开发流程
- AI 量化交易系统开发：开发者可作为数据后端为 AI 交易代理提供实时金融数据支持，构建自动化交易机器人
- 金融数据中台搭建：企业可基于 OpenBB 构建内部金融数据平台，整合多数据源提供统一的数据服务



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,908 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

16万星标的提示词宝库，前身是知名Awesome ChatGPT Prompts项目，支持多LLM平台和自托管部署，适合个人和企业追求隐私保护的场景。

**技术亮点**:
- 多LLM平台支持：兼容ChatGPT、Claude、Gemini、GPT-4等主流大语言模型
- 现代化技术栈：基于Next.js + TypeScript构建，具备良好开发体验和类型安全
- 自托管部署：提供完整开源代码，支持私有化部署确保数据隐私
- 社区驱动：活跃的开源社区持续贡献高质量提示词
- 丰富的Topics覆盖：包含AI、机器学习、提示词工程等多个相关领域

**适用场景**:
- 个人开发者快速获取高质量提示词，提升AI工具使用效率
- 企业团队自托管部署实现完全私有化，避免敏感数据外泄
- AI爱好者学习提示词工程技巧，探索不同LLM的最佳实践



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,996 |
| 语言 | Python |
| Forks | 33,034 |
| Issues | 2,333 |
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
| Stars | 78,325 |
| 语言 | Python |
| Forks | 16,161 |
| Issues | 4,549 |
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
| Stars | 110,329 |
| 语言 | Python |
| Forks | 12,869 |
| Issues | 3,997 |
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
| Stars | 99,482 |
| 语言 | Python |
| Forks | 27,606 |
| Issues | 18,562 |
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
| Stars | 91,587 |
| 语言 | Jupyter Notebook |
| Forks | 14,100 |
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
| Stars | 34,015 |
| 语言 | TypeScript |
| Forks | 3,705 |
| Issues | 299 |
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
| Stars | 168,287 |
| 语言 | JavaScript |
| Forks | 26,080 |
| Issues | 172 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码助手的性能优化系统，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，Stars 高达 168k 证明了其在开发者社区的广泛认可和实用性。

**技术亮点**:
- 提供 Skills 和 Instincts 机制，支持开发者自定义 AI 助手的技能和行为模式
- 内置 Memory 模块，实现跨会话的上下文保持和知识复用
- 安全沙箱机制，保障 AI Agent 操作的安全性和可控性
- 支持多平台 AI 编码助手（Claude Code, Codex, Cursor, Opencode）
- 采用 Research-First 开发理念，融入前沿 AI Agent 研究成果

**适用场景**:
- 个人开发者提升编程效率 - 通过自定义 Skills 和 Instincts 优化个人工作流
- 企业团队 AI 编码规范落地 - 利用 Memory 模块统一团队级上下文和编码规范
- AI Agent 安全审计与优化 - 在生产环境中部署前进行安全沙箱测试



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,877 |
| 语言 | Go |
| Forks | 4,030 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 部署解决方案，支持 LLM、视觉、语音、图像、视频等多模态模型，无需 GPU 即可在普通硬件上运行，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、图像生成、语音合成、目标检测、音乐生成等多种模型类型
- 零 GPU 依赖：可在 CPU 和普通硬件上运行，降低 AI 部署门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用快速迁移
- Go 语言实现：利用 Go 的高性能和并发特性，支持高吞吐量推理

**适用场景**:
- 本地隐私敏感场景：医疗、金融、法律等需要数据不出本地的行业，可用 LocalAI 构建私有化 AI 应用
- 边缘设备部署：在没有强大 GPU 的边缘设备或嵌入式系统上运行 AI 推理任务
- 开发测试环境：开发者可在本地快速验证 AI 应用，无需依赖云服务或支付 API 费用
- MCP 协议实现：支持 Model Context Protocol，用于构建 AI Agents 和自动化工作流



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,990 |
| 语言 | Java |
| Forks | 15,951 |
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
| Stars | 72,189 |
| 语言 | Python |
| Forks | 9,116 |
| Issues | 413 |
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
| Stars | 54,522 |
| 语言 | TypeScript |
| Forks | 4,423 |
| Issues | 653 |
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
| Stars | 185,845 |
| 语言 | TypeScript |
| Forks | 57,180 |
| Issues | 1,556 |
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
| Stars | 158,912 |
| 语言 | Python |
| Forks | 13,149 |
| Issues | 2,489 |
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
| Stars | 97,697 |
| 语言 | Python |
| Forks | 9,164 |
| Issues | 177 |
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
| Stars | 82,512 |
| 语言 | Python |
| Forks | 9,625 |
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
| Stars | 184,321 |
| 语言 | TypeScript |
| Forks | 39,489 |
| Issues | 16,791 |
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
| Stars | 94,205 |
| 语言 | TypeScript |
| Forks | 9,411 |
| Issues | 304 |
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
| Stars | 79,040 |
| 语言 | TypeScript |
| Forks | 5,836 |
| Issues | 775 |
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
| Stars | 79,828 |
| 语言 | Go |
| Forks | 2,792 |
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
| Stars | 77,115 |
| 语言 | Go |
| Forks | 2,794 |
| Issues | 951 |
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
| Stars | 54,522 |
| 语言 | TypeScript |
| Forks | 4,423 |
| Issues | 653 |
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
| Stars | 185,845 |
| 语言 | TypeScript |
| Forks | 57,180 |
| Issues | 1,556 |
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
| Stars | 56,656 |
| 语言 | Python |
| Forks | 6,102 |
| Issues | 561 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,643 |
| 语言 | Go |
| Forks | 10,324 |
| Issues | 233 |
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
| Stars | 121,968 |
| 语言 | Go |
| Forks | 42,934 |
| Issues | 2,669 |
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
| Stars | 71,508 |
| 语言 | Go |
| Forks | 18,922 |
| Issues | 3,801 |
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
| Stars | 55,145 |
| 语言 | Go |
| Forks | 6,624 |
| Issues | 2,774 |
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
| Stars | 47,499 |
| 语言 | Go |
| Forks | 5,053 |
| Issues | 985 |
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
| Stars | 94,205 |
| 语言 | TypeScript |
| Forks | 9,411 |
| Issues | 304 |
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
| Stars | 77,881 |
| 语言 | TypeScript |
| Forks | 6,806 |
| Issues | 432 |
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
| Stars | 85,987 |
| 语言 | JavaScript |
| Forks | 7,732 |
| Issues | 731 |
| Topics | docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring, webapp, websocket |
| 许可证 | MIT License |


### traefik/traefik

**描述**: The Cloud Native Application Proxy

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,897 |
| 语言 | Go |
| Forks | 5,940 |
| Issues | 779 |
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
| Stars | 60,808 |
| 语言 | Go |
| Forks | 7,421 |
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
| Stars | 59,222 |
| 语言 | Go |
| Forks | 4,308 |
| Issues | 23 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,055 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 321 |
| Topics | ci, devops, github-actions, golang |
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
| Stars | 85,987 |
| 语言 | JavaScript |
| Forks | 7,732 |
| Issues | 731 |
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
| Stars | 63,814 |
| 语言 | Go |
| Forks | 10,366 |
| Issues | 748 |
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
| Stars | 45,877 |
| 语言 | Go |
| Forks | 4,030 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 部署解决方案，支持 LLM、视觉、语音、图像、视频等多模态模型，无需 GPU 即可在普通硬件上运行，特别适合需要数据隐私保护或降低 AI 部署成本的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、图像生成、语音合成、目标检测、音乐生成等多种模型类型
- 零 GPU 依赖：可在 CPU 和普通硬件上运行，降低 AI 部署门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用快速迁移
- Go 语言实现：利用 Go 的高性能和并发特性，支持高吞吐量推理

**适用场景**:
- 本地隐私敏感场景：医疗、金融、法律等需要数据不出本地的行业，可用 LocalAI 构建私有化 AI 应用
- 边缘设备部署：在没有强大 GPU 的边缘设备或嵌入式系统上运行 AI 推理任务
- 开发测试环境：开发者可在本地快速验证 AI 应用，无需依赖云服务或支付 API 费用
- MCP 协议实现：支持 Model Context Protocol，用于构建 AI Agents 和自动化工作流



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,697 |
| 语言 | Python |
| Forks | 9,164 |
| Issues | 177 |
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
| Stars | 87,341 |
| 语言 | Python |
| Forks | 33,830 |
| Issues | 435 |
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
| Forks | 27,189 |
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
| Stars | 79,040 |
| 语言 | TypeScript |
| Forks | 5,836 |
| Issues | 775 |
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
| Stars | 68,981 |
| 语言 | JavaScript |
| Forks | 23,183 |
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
| Stars | 55,951 |
| 语言 | JavaScript |
| Forks | 10,208 |
| Issues | 368 |
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
| Stars | 51,830 |
| 语言 | JavaScript |
| Forks | 4,708 |
| Issues | 1,473 |
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
| Stars | 88,395 |
| 语言 | Go |
| Forks | 8,585 |
| Issues | 680 |
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
| Stars | 71,879 |
| 语言 | Go |
| Forks | 4,702 |
| Issues | 238 |
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
| Stars | 58,004 |
| 语言 | Go |
| Forks | 3,333 |
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
| Stars | 101,497 |
| 语言 | TypeScript |
| Forks | 12,196 |
| Issues | 963 |
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
| Stars | 59,101 |
| 语言 | JavaScript |
| Forks | 6,384 |
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
| Stars | 44,011 |
| 语言 | Go |
| Forks | 3,980 |
| Issues | 1,099 |
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
| Stars | 51,643 |
| 语言 | Go |
| Forks | 10,324 |
| Issues | 233 |
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
| Stars | 160,908 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

16万星标的提示词宝库，前身是知名Awesome ChatGPT Prompts项目，支持多LLM平台和自托管部署，适合个人和企业追求隐私保护的场景。

**技术亮点**:
- 多LLM平台支持：兼容ChatGPT、Claude、Gemini、GPT-4等主流大语言模型
- 现代化技术栈：基于Next.js + TypeScript构建，具备良好开发体验和类型安全
- 自托管部署：提供完整开源代码，支持私有化部署确保数据隐私
- 社区驱动：活跃的开源社区持续贡献高质量提示词
- 丰富的Topics覆盖：包含AI、机器学习、提示词工程等多个相关领域

**适用场景**:
- 个人开发者快速获取高质量提示词，提升AI工具使用效率
- 企业团队自托管部署实现完全私有化，避免敏感数据外泄
- AI爱好者学习提示词工程技巧，探索不同LLM的最佳实践



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,165 |
| 语言 | Python |
| Forks | 4,955 |
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
| Stars | 56,951 |
| 语言 | TypeScript |
| Forks | 9,361 |
| Issues | 107 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 48,005 |
| 语言 | Python |
| Forks | 2,541 |
| Issues | 163 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,805 |
| 语言 | TypeScript |
| Forks | 10,032 |
| Issues | 2,258 |
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
| Stars | 87,666 |
| 语言 | TypeScript |
| Forks | 8,913 |
| Issues | 1,646 |
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
| Stars | 127,599 |
| 语言 | JavaScript |
| Forks | 12,480 |
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
| Stars | 171,154 |
| 语言 | Go |
| Forks | 13,175 |
| Issues | 183 |
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
| Stars | 79,112 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 2,981 |
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
| Stars | 92,373 |
| 语言 | Python |
| Forks | 13,412 |
| Issues | 115 |
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
| Stars | 91,224 |
| 语言 | Python |
| Forks | 7,881 |
| Issues | 636 |
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
| Stars | 136,217 |
| 语言 | Unknown |
| Forks | 34,072 |
| Issues | 135 |
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
| Stars | 386,275 |
| 语言 | Python |
| Forks | 66,143 |
| Issues | 76 |
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
| Stars | 115,519 |
| 语言 | TypeScript |
| Forks | 6,039 |
| Issues | 13 |
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
| Stars | 113,906 |
| 语言 | TypeScript |
| Forks | 8,329 |
| Issues | 299 |
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
| Stars | 85,143 |
| 语言 | TypeScript |
| Forks | 12,442 |
| Issues | 468 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,963 |
| 语言 | JavaScript |
| Forks | 4,910 |
| Issues | 14 |
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
| Stars | 48,268 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 1,893 |
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
| Stars | 106,970 |
| 语言 | C++ |
| Forks | 17,447 |
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
| Stars | 63,393 |
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
| Stars | 93,665 |
| 语言 | Unknown |
| Forks | 9,014 |
| Issues | 74 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 294,682 |
| 语言 | Python |
| Forks | 27,784 |
| Issues | 17 |
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
| Stars | 86,801 |
| 语言 | Python |
| Forks | 37,380 |
| Issues | 3,784 |
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
| Stars | 77,669 |
| 语言 | Python |
| Forks | 45,116 |
| Issues | 1,286 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,287 |
| 语言 | Python |
| Forks | 16,896 |
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
| Stars | 443,725 |
| 语言 | TypeScript |
| Forks | 44,408 |
| Issues | 178 |
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
| Stars | 353,759 |
| 语言 | TypeScript |
| Forks | 43,975 |
| Issues | 15 |
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
| Stars | 122,066 |
| 语言 | TypeScript |
| Forks | 13,440 |
| Issues | 3,014 |
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
| Stars | 113,104 |
| 语言 | TypeScript |
| Forks | 8,660 |
| Issues | 1,861 |
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
| Stars | 108,682 |
| 语言 | TypeScript |
| Forks | 13,373 |
| Issues | 5,029 |
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
| Stars | 98,756 |
| 语言 | TypeScript |
| Forks | 5,496 |
| Issues | 696 |
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
| Stars | 97,869 |
| 语言 | TypeScript |
| Forks | 54,596 |
| Issues | 1,368 |
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
| Stars | 94,776 |
| 语言 | TypeScript |
| Forks | 5,210 |
| Issues | 100 |
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
| Stars | 80,265 |
| 语言 | TypeScript |
| Forks | 8,101 |
| Issues | 725 |
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
| Stars | 244,726 |
| 语言 | JavaScript |
| Forks | 50,985 |
| Issues | 1,254 |
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
| Stars | 116,942 |
| 语言 | JavaScript |
| Forks | 35,445 |
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
| Stars | 112,206 |
| 语言 | JavaScript |
| Forks | 36,348 |
| Issues | 521 |
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
| Stars | 109,032 |
| 语言 | JavaScript |
| Forks | 11,656 |
| Issues | 188 |
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
| Stars | 98,241 |
| 语言 | JavaScript |
| Forks | 32,653 |
| Issues | 1,539 |
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
| Stars | 95,689 |
| 语言 | JavaScript |
| Forks | 15,417 |
| Issues | 48 |
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
| Stars | 86,432 |
| 语言 | JavaScript |
| Forks | 4,898 |
| Issues | 1,002 |
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
| Stars | 71,081 |
| 语言 | JavaScript |
| Forks | 16,807 |
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
| Stars | 65,784 |
| 语言 | JavaScript |
| Forks | 9,361 |
| Issues | 206 |
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
| Stars | 63,145 |
| 语言 | JavaScript |
| Forks | 4,037 |
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
| Stars | 61,260 |
| 语言 | JavaScript |
| Forks | 7,151 |
| Issues | 141 |
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
| Stars | 60,723 |
| 语言 | JavaScript |
| Forks | 5,660 |
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
| Forks | 20,455 |
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
| Stars | 57,434 |
| 语言 | JavaScript |
| Forks | 12,307 |
| Issues | 28 |
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
| Stars | 53,201 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 447 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,686 |
| 语言 | JavaScript |
| Forks | 11,514 |
| Issues | 250 |
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
| Stars | 133,654 |
| 语言 | Go |
| Forks | 18,951 |
| Issues | 9,980 |
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
| Stars | 106,131 |
| 语言 | Go |
| Forks | 15,023 |
| Issues | 37 |
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
| Stars | 87,798 |
| 语言 | Go |
| Forks | 8,252 |
| Issues | 239 |
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
| Stars | 83,195 |
| 语言 | Go |
| Forks | 5,127 |
| Issues | 383 |
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
| Stars | 68,604 |
| 语言 | Go |
| Forks | 3,225 |
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
| Stars | 56,888 |
| 语言 | Go |
| Forks | 5,058 |
| Issues | 1,174 |
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
| Stars | 51,000 |
| 语言 | Go |
| Forks | 21,895 |
| Issues | 417 |
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
| Stars | 49,373 |
| 语言 | Go |
| Forks | 7,948 |
| Issues | 565 |
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
| Stars | 46,851 |
| 语言 | Go |
| Forks | 8,856 |
| Issues | 20 |
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
| Stars | 87,716 |
| 语言 | Shell |
| Forks | 14,132 |
| Issues | 111 |
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
| Stars | 220,309 |
| 语言 | Python |
| Forks | 50,442 |
| Issues | 934 |
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
| Stars | 98,511 |
| 语言 | Python |
| Forks | 12,110 |
| Issues | 123 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,354 |
| 语言 | Python |
| Forks | 7,248 |
| Issues | 487 |
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
| Stars | 139,054 |
| 语言 | TypeScript |
| Forks | 16,529 |
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
| Stars | 84,636 |
| 语言 | TypeScript |
| Forks | 10,518 |
| Issues | 388 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,289 |
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
| Stars | 148,128 |
| 语言 | JavaScript |
| Forks | 26,705 |
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
| Stars | 79,184 |
| 语言 | JavaScript |
| Forks | 32,645 |
| Issues | 278 |
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
| Stars | 67,393 |
| 语言 | JavaScript |
| Forks | 11,954 |
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
| Stars | 66,350 |
| 语言 | JavaScript |
| Forks | 9,194 |
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
| Stars | 51,323 |
| 语言 | JavaScript |
| Forks | 10,358 |
| Issues | 134 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,825 |
| 语言 | Go |
| Forks | 1,608 |
| Issues | 273 |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,123 |
| 语言 | Go |
| Forks | 3,798 |
| Issues | 83 |
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
| Stars | 153,467 |
| 语言 | Python |
| Forks | 11,713 |
| Issues | 348 |
| Topics | awesome, github, hellogithub, python |
