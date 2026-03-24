# 项目发现报告 (2026-03-24)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 128 |
| 去重移除 | 30 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
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
| Stars | 128,520 |
| 语言 | Python |
| Forks | 18,169 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

作为最受欢迎的 LLM WebUI 开源项目，Open WebUI 提供了开箱即用的用户友好界面，支持多种 LLM 提供商（Ollama、OpenAI 等）和 RAG 能力，适合快速搭建私有化 AI 对话系统。

**技术亮点**:
- 支持多种 LLM 提供商集成：Ollama、OpenAI API、MCP 协议等
- 内置 RAG（检索增强生成）能力，支持文档解析和向量检索
- 提供完整的 Web UI 界面，支持多会话管理、提示词模板
- 支持 Docker 一键部署，开箱即用的自托管解决方案
- 支持多模态交互（文本、图像）和工具调用能力

**适用场景**:
- 企业内部私有化 AI 助手：搭建支持本地部署的对话系统，保护数据隐私
- 个人开发者快速原型开发：无需从零开发 UI，快速接入各类 LLM
- 知识库问答系统：利用 RAG 能力构建基于私有文档的智能问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,022 |
| 语言 | Python |
| Forks | 8,503 |
| Issues | 3,147 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最火热的开源 RAG 引擎之一，拥有 7.6 万+ Stars，通过将 RAG 与 Agent 能力深度融合，配合强大的文档理解能力，为 LLM 提供了更精准的上下文检索层，是构建企业级知识库和智能问答系统的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与 Agent 智能体能力结合，支持复杂推理和多步任务执行
- 深度文档理解：内置强大的文档解析引擎，支持多种格式（PDF、Word、Excel 等）的智能解析和结构化提取
- 多后端 LLM 支持：兼容 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和组合使用
- MCP 协议支持：集成 Model Context Protocol，实现标准化的上下文管理和工具调用
- GraphRAG 能力：支持知识图谱增强的检索，提升复杂关联查询的准确性

**适用场景**:
- 企业知识库智能问答：构建支持复杂文档理解的公司内部知识库，提供精准的检索增强回答
- 深度研究与分析：利用 Agent 能力进行多源信息整合、推理验证的深度研究场景
- 智能文档处理：自动化解析、理解和提取非结构化文档中的关键信息



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,501 |
| 语言 | TypeScript |
| Forks | 6,600 |
| Issues | 234 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的 Web 数据提取工具，能够将任意网站快速转换为 LLM 可直接使用的 Markdown 或结构化数据，极大简化了 AI Agent 获取实时网络信息的流程，是构建 AI 驱动的搜索和数据分析应用的核心基础设施。

**技术亮点**:
- 支持全站抓取和智能内容提取，自动识别并清理无关元素，输出高质量的 LLM 可读文本
- 提供 Markdown 和结构化数据双输出模式，兼容各类 AI 模型和向量数据库
- 内置 JavaScript 渲染支持，能够处理 SPA（单页应用）和动态加载内容
- 提供完整的 API 接口和 SDK，支持快速集成到现有 AI 应用中
- 支持批量抓取和增量更新，具备站点地图解析和深度爬取能力

**适用场景**:
- AI 搜索和问答系统：为 RAG（检索增强生成）应用提供实时网络数据的结构化输入
- 竞品分析和市场调研：批量抓取目标网站内容并转换为可分析的结构化数据
- AI Agent 工具：作为自主代理获取最新网络信息的核心组件，支持实时网页导航和数据提取



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,534 |
| 语言 | JavaScript |
| Forks | 13,591 |
| Issues | 122 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 Claude Code、Codex、Cursor 等主流 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 等核心模块实现智能化开发流程，10万+ Stars 证明了其在 AI 辅助开发领域的高人气和实用价值。

**技术亮点**:
- 统一支持多种 AI 代码助手：Claude Code、Codex、Opencode、Cursor 等主流工具
- 核心模块化设计：Skills（技能）、Instincts（本能）、Memory（记忆）三大支柱
- MCP (Model Context Protocol) 深度集成，提升上下文理解和任务执行能力
- 内置安全机制和权限控制，确保 AI 辅助开发的安全性
- 以研究为导向的开发方法论，持续探索 AI Agent 性能优化前沿

**适用场景**:
- 企业开发团队：建立标准化的 AI 辅助开发流程，提升团队协作效率和代码质量
- 个人开发者：快速构建和优化 AI 代码助手工作流，实现开发效率倍增
- AI Agent 研究者：基于该框架探索 LLM 在软件开发领域的最佳实践和性能瓶颈



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,323 |
| 语言 | Go |
| Forks | 3,789 |
| Issues | 142 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像和视频等多种生成式 AI 模型，无需 GPU 支持，极大地降低了 AI 应用的部署门槛和成本。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和并发处理能力，适合构建可扩展的 AI 服务
- 支持多模态模型：LLM（如 LLaMA、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）和目标检测等
- 去中心化架构设计，支持 libp2p 协议，可实现分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移
- 支持 MCP（Model Context Protocol）协议，实现模型与工具的标准化交互

**适用场景**:
- 本地/私有化 AI 部署：适合需要在本地运行 AI 应用的企业，满足数据隐私合规要求
- 边缘计算场景：在没有强大 GPU 的边缘设备上运行 AI 推理任务
- 成本敏感型应用：个人开发者或小型企业可零成本运行 AI 模型，无需依赖云服务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,245 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 663 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能全面的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，集成 MCP 协议实现标准化扩展，并提供开箱即用的 agent 团队设计和知识库能力，社区活跃（74k+ Stars）是值得信赖的 AI agent 开发框架。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等多种大语言模型无缝切换与对比
- MCP 协议支持：符合 Model Context Protocol 标准，可扩展连接各类数据源和工具生态
- 多 Agent 协作框架：支持设计和管理多个 agent 团队，实现复杂任务的分工协作
- 知识库集成：内置 RAG 能力，让 agent 能够访问和利用结构化知识
- TypeScript 全栈架构：从前端到后端采用 TypeScript 开发，保证类型安全与开发体验

**适用场景**:
- 企业智能团队：构建多 agent 团队自动处理客户支持、数据分析、内容创作等分工协作任务
- 开发者 AI 应用开发：基于 lobehub 框架快速搭建私有化 AI 应用，定制 agent 行为和工作流
- 个人生产力助手：作为强大的 AI 工作站，集成的 chat、agent、知识库能力可提升个人工作效率



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,995 |
| 语言 | Python |
| Forks | 8,411 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的开源大模型微调工具之一，通过统一框架整合了 LoRA、QLoRA、RLHF 等主流微调技术，支持 100+ 主流大模型，让研究者和开发者能以最低成本和最高效率完成模型定制化训练，是企业落地 AI 应用和个人学习大模型微调的理想选择。

**技术亮点**:
- 支持 100+ 语言模型和视觉语言模型（VLMs）的统一微调框架，包括 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成 LoRA、QLoRA、PEFT 等参数高效微调方法，配合量化技术，可在消费级 GPU 上微调大模型，大幅降低显存占用
- 支持 RLHF（人类反馈强化学习）和完整的 Instruction Tuning 训练流水线，以及 MoE（混合专家）架构模型的微调
- 基于 Transformers 生态，提供统一的 API 接口和丰富的训练策略配置，开箱即用，工程化成熟度高
- ACL 2024 学术顶会认可的开源项目，Apache License 2.0 许可证，商业友好

**适用场景**:
- 企业级 AI 应用开发：快速将开源大模型适配到特定业务场景（客服、文档分析、私域知识库等），降低模型定制化成本，加速 AI 产品落地
- 学术研究与算法实验：对比不同微调方法（LoRA vs QLoRA vs RLHF）或在不同模型架构上的效果，统一的框架设计让实验对比更加便捷
- 个人开发者与 AI 爱好者：学习大模型微调技术，在有限硬件资源下（如 3090/4090 显卡）微调专属模型，低门槛高效率



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,471 |
| 语言 | Python |
| Forks | 9,857 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,208 |
| 语言 | TypeScript |
| Forks | 2,947 |
| Issues | 179 |
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
| Stars | 37,928 |
| 语言 | TypeScript |
| Forks | 5,990 |
| Issues | 75 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,918 |
| 语言 | TypeScript |
| Forks | 7,085 |
| Issues | 454 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,608 |
| 语言 | Python |
| Forks | 2,079 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,547 |
| 语言 | Java |
| Forks | 15,848 |
| Issues | 60 |
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
| Stars | 38,830 |
| 语言 | Python |
| Forks | 6,161 |
| Issues | 134 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,654 |
| 语言 | Jupyter Notebook |
| Forks | 5,416 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 103,419 |
| 语言 | Python |
| Forks | 15,090 |
| Issues | 5 |
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
| Stars | 56,673 |
| 语言 | JavaScript |
| Forks | 6,124 |
| Issues | 298 |
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
| Stars | 69,679 |
| 语言 | Python |
| Forks | 8,729 |
| Issues | 337 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### unslothai/unsloth

**描述**: Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,000 |
| 语言 | Python |
| Forks | 4,892 |
| Issues | 1,030 |
| Topics | agent, deepseek, fine-tuning, gemma, gemma3, gpt-oss, llama, llama3, llm, llms, mistral, openai, qwen, reinforcement-learning, self-hosted, text-to-speech, tts, ui, unsloth |
| 许可证 | Apache License 2.0 |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,106 |
| 语言 | TypeScript |
| Forks | 3,196 |
| Issues | 397 |
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
| Stars | 84,194 |
| 语言 | Python |
| Forks | 9,763 |
| Issues | 224 |
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
| Stars | 51,044 |
| 语言 | TypeScript |
| Forks | 23,976 |
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
| Stars | 180,857 |
| 语言 | TypeScript |
| Forks | 56,113 |
| Issues | 1,432 |
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
| Stars | 146,169 |
| 语言 | Python |
| Forks | 8,649 |
| Issues | 907 |
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
| Stars | 54,880 |
| 语言 | Jupyter Notebook |
| Forks | 18,970 |
| Issues | 7 |
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
| Stars | 72,202 |
| 语言 | MDX |
| Forks | 7,709 |
| Issues | 250 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,381 |
| 语言 | TypeScript |
| Forks | 3,619 |
| Issues | 288 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,846 |
| 语言 | Rust |
| Forks | 1,974 |
| Issues | 502 |
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
| Stars | 128,520 |
| 语言 | Python |
| Forks | 18,169 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

作为最受欢迎的 LLM WebUI 开源项目，Open WebUI 提供了开箱即用的用户友好界面，支持多种 LLM 提供商（Ollama、OpenAI 等）和 RAG 能力，适合快速搭建私有化 AI 对话系统。

**技术亮点**:
- 支持多种 LLM 提供商集成：Ollama、OpenAI API、MCP 协议等
- 内置 RAG（检索增强生成）能力，支持文档解析和向量检索
- 提供完整的 Web UI 界面，支持多会话管理、提示词模板
- 支持 Docker 一键部署，开箱即用的自托管解决方案
- 支持多模态交互（文本、图像）和工具调用能力

**适用场景**:
- 企业内部私有化 AI 助手：搭建支持本地部署的对话系统，保护数据隐私
- 个人开发者快速原型开发：无需从零开发 UI，快速接入各类 LLM
- 知识库问答系统：利用 RAG 能力构建基于私有文档的智能问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,022 |
| 语言 | Python |
| Forks | 8,503 |
| Issues | 3,147 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最火热的开源 RAG 引擎之一，拥有 7.6 万+ Stars，通过将 RAG 与 Agent 能力深度融合，配合强大的文档理解能力，为 LLM 提供了更精准的上下文检索层，是构建企业级知识库和智能问答系统的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与 Agent 智能体能力结合，支持复杂推理和多步任务执行
- 深度文档理解：内置强大的文档解析引擎，支持多种格式（PDF、Word、Excel 等）的智能解析和结构化提取
- 多后端 LLM 支持：兼容 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和组合使用
- MCP 协议支持：集成 Model Context Protocol，实现标准化的上下文管理和工具调用
- GraphRAG 能力：支持知识图谱增强的检索，提升复杂关联查询的准确性

**适用场景**:
- 企业知识库智能问答：构建支持复杂文档理解的公司内部知识库，提供精准的检索增强回答
- 深度研究与分析：利用 Agent 能力进行多源信息整合、推理验证的深度研究场景
- 智能文档处理：自动化解析、理解和提取非结构化文档中的关键信息



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,245 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 663 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能全面的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，集成 MCP 协议实现标准化扩展，并提供开箱即用的 agent 团队设计和知识库能力，社区活跃（74k+ Stars）是值得信赖的 AI agent 开发框架。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等多种大语言模型无缝切换与对比
- MCP 协议支持：符合 Model Context Protocol 标准，可扩展连接各类数据源和工具生态
- 多 Agent 协作框架：支持设计和管理多个 agent 团队，实现复杂任务的分工协作
- 知识库集成：内置 RAG 能力，让 agent 能够访问和利用结构化知识
- TypeScript 全栈架构：从前端到后端采用 TypeScript 开发，保证类型安全与开发体验

**适用场景**:
- 企业智能团队：构建多 agent 团队自动处理客户支持、数据分析、内容创作等分工协作任务
- 开发者 AI 应用开发：基于 lobehub 框架快速搭建私有化 AI 应用，定制 agent 行为和工作流
- 个人生产力助手：作为强大的 AI 工作站，集成的 chat、agent、知识库能力可提升个人工作效率



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,208 |
| 语言 | TypeScript |
| Forks | 2,947 |
| Issues | 179 |
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
| Stars | 33,608 |
| 语言 | Python |
| Forks | 2,079 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,547 |
| 语言 | Java |
| Forks | 15,848 |
| Issues | 60 |
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
| Stars | 38,830 |
| 语言 | Python |
| Forks | 6,161 |
| Issues | 134 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,654 |
| 语言 | Jupyter Notebook |
| Forks | 5,416 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 103,419 |
| 语言 | Python |
| Forks | 15,090 |
| Issues | 5 |
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
| Stars | 99,558 |
| 语言 | TypeScript |
| Forks | 11,875 |
| Issues | 957 |
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
| Stars | 56,673 |
| 语言 | JavaScript |
| Forks | 6,124 |
| Issues | 298 |
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
| Stars | 51,044 |
| 语言 | TypeScript |
| Forks | 23,976 |
| Issues | 808 |
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
| Stars | 72,987 |
| 语言 | Python |
| Forks | 10,021 |
| Issues | 255 |
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
| Stars | 43,452 |
| 语言 | Go |
| Forks | 3,910 |
| Issues | 1,102 |
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
| Stars | 31,756 |
| 语言 | Python |
| Forks | 3,346 |
| Issues | 82 |
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
| Stars | 72,202 |
| 语言 | MDX |
| Forks | 7,709 |
| Issues | 250 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,381 |
| 语言 | TypeScript |
| Forks | 3,619 |
| Issues | 288 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
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
| Stars | 128,520 |
| 语言 | Python |
| Forks | 18,169 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

作为最受欢迎的 LLM WebUI 开源项目，Open WebUI 提供了开箱即用的用户友好界面，支持多种 LLM 提供商（Ollama、OpenAI 等）和 RAG 能力，适合快速搭建私有化 AI 对话系统。

**技术亮点**:
- 支持多种 LLM 提供商集成：Ollama、OpenAI API、MCP 协议等
- 内置 RAG（检索增强生成）能力，支持文档解析和向量检索
- 提供完整的 Web UI 界面，支持多会话管理、提示词模板
- 支持 Docker 一键部署，开箱即用的自托管解决方案
- 支持多模态交互（文本、图像）和工具调用能力

**适用场景**:
- 企业内部私有化 AI 助手：搭建支持本地部署的对话系统，保护数据隐私
- 个人开发者快速原型开发：无需从零开发 UI，快速接入各类 LLM
- 知识库问答系统：利用 RAG 能力构建基于私有文档的智能问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,022 |
| 语言 | Python |
| Forks | 8,503 |
| Issues | 3,147 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最火热的开源 RAG 引擎之一，拥有 7.6 万+ Stars，通过将 RAG 与 Agent 能力深度融合，配合强大的文档理解能力，为 LLM 提供了更精准的上下文检索层，是构建企业级知识库和智能问答系统的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与 Agent 智能体能力结合，支持复杂推理和多步任务执行
- 深度文档理解：内置强大的文档解析引擎，支持多种格式（PDF、Word、Excel 等）的智能解析和结构化提取
- 多后端 LLM 支持：兼容 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和组合使用
- MCP 协议支持：集成 Model Context Protocol，实现标准化的上下文管理和工具调用
- GraphRAG 能力：支持知识图谱增强的检索，提升复杂关联查询的准确性

**适用场景**:
- 企业知识库智能问答：构建支持复杂文档理解的公司内部知识库，提供精准的检索增强回答
- 深度研究与分析：利用 Agent 能力进行多源信息整合、推理验证的深度研究场景
- 智能文档处理：自动化解析、理解和提取非结构化文档中的关键信息



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,534 |
| 语言 | JavaScript |
| Forks | 13,591 |
| Issues | 122 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 Claude Code、Codex、Cursor 等主流 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 等核心模块实现智能化开发流程，10万+ Stars 证明了其在 AI 辅助开发领域的高人气和实用价值。

**技术亮点**:
- 统一支持多种 AI 代码助手：Claude Code、Codex、Opencode、Cursor 等主流工具
- 核心模块化设计：Skills（技能）、Instincts（本能）、Memory（记忆）三大支柱
- MCP (Model Context Protocol) 深度集成，提升上下文理解和任务执行能力
- 内置安全机制和权限控制，确保 AI 辅助开发的安全性
- 以研究为导向的开发方法论，持续探索 AI Agent 性能优化前沿

**适用场景**:
- 企业开发团队：建立标准化的 AI 辅助开发流程，提升团队协作效率和代码质量
- 个人开发者：快速构建和优化 AI 代码助手工作流，实现开发效率倍增
- AI Agent 研究者：基于该框架探索 LLM 在软件开发领域的最佳实践和性能瓶颈



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,245 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 663 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能全面的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，集成 MCP 协议实现标准化扩展，并提供开箱即用的 agent 团队设计和知识库能力，社区活跃（74k+ Stars）是值得信赖的 AI agent 开发框架。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等多种大语言模型无缝切换与对比
- MCP 协议支持：符合 Model Context Protocol 标准，可扩展连接各类数据源和工具生态
- 多 Agent 协作框架：支持设计和管理多个 agent 团队，实现复杂任务的分工协作
- 知识库集成：内置 RAG 能力，让 agent 能够访问和利用结构化知识
- TypeScript 全栈架构：从前端到后端采用 TypeScript 开发，保证类型安全与开发体验

**适用场景**:
- 企业智能团队：构建多 agent 团队自动处理客户支持、数据分析、内容创作等分工协作任务
- 开发者 AI 应用开发：基于 lobehub 框架快速搭建私有化 AI 应用，定制 agent 行为和工作流
- 个人生产力助手：作为强大的 AI 工作站，集成的 chat、agent、知识库能力可提升个人工作效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,137 |
| 语言 | HTML |
| Forks | 20,256 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、最活跃的 AI 提示词开源社区项目，拥有超过 15 万星标，汇集了数千个经过验证的高质量提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，可免费自托管部署，非常适合个人和团队构建私有化的提示词库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态站点生成
- 支持多 LLM 平台提示词：OpenAI GPT-4、Claude、Gemini 等主流模型
- 提供 Docker 一键部署方案，支持企业私有化自托管，完全数据自主
- 社区驱动的提示词贡献机制，包含角色扮演、代码助手、内容创作等丰富分类
- CC0 许可证声明，完全开源可商用，无需任何依赖或 API 密钥成本

**适用场景**:
- 个人用户：发现、收藏和分享各类 AI 助手的优质提示词，提升日常工作和创作效率
- 企业团队：自托管部署私有提示词库，保护内部数据隐私，适合对数据安全有要求的组织
- 开发者：参考和借鉴高质量提示词的设计模式，用于构建自己的 AI 应用或提示词管理工具



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,162 |
| 语言 | Jupyter Notebook |
| Forks | 13,595 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个极其优质的 LLM 从零实现教程项目，以 89k+ Stars 证明了其在 AI 教育领域的标杆地位。项目通过 Jupyter Notebook 逐行代码讲解 ChatGPT 类 LLM 的完整实现，无需依赖 Hugging Face 等高级库，是深入理解大语言模型内部原理的最佳实践资源。

**技术亮点**:
- 从零实现 GPT 架构 - 不依赖任何高级 LLM 库，使用纯 PyTorch 构建完整语言模型
- 逐行代码详解 - 每个组件（Embedding、注意力机制、前馈网络等）都有详尽注释和解释
- 完整训练流程覆盖 - 包含数据预处理、tokenization、训练循环、模型评估的端到端实现
- 深入注意力机制 - 从零实现 Multi-Head Attention、RoPE 等先进注意力变体
- 教学导向设计 - 配套书籍《Build a Large Language Model (From Scratch)》系统化学习路径

**适用场景**:
- LLM/Deep Learning 学习者 - 系统学习 Transformer 架构和 LLM 内部工作原理的入门到进阶路径
- AI 教育者/讲师 - 作为课程教材或实验项目，用于教授大语言模型基础知识
- PyTorch 开发者 - 理解如何从底层实现一个生产级别的语言模型，提升工程能力



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,471 |
| 语言 | Python |
| Forks | 9,857 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,208 |
| 语言 | TypeScript |
| Forks | 2,947 |
| Issues | 179 |
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
| Stars | 37,928 |
| 语言 | TypeScript |
| Forks | 5,990 |
| Issues | 75 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,918 |
| 语言 | TypeScript |
| Forks | 7,085 |
| Issues | 454 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,608 |
| 语言 | Python |
| Forks | 2,079 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,673 |
| 语言 | JavaScript |
| Forks | 6,124 |
| Issues | 298 |
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
| Stars | 69,679 |
| 语言 | Python |
| Forks | 8,729 |
| Issues | 337 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### unslothai/unsloth

**描述**: Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,000 |
| 语言 | Python |
| Forks | 4,892 |
| Issues | 1,030 |
| Topics | agent, deepseek, fine-tuning, gemma, gemma3, gpt-oss, llama, llama3, llm, llms, mistral, openai, qwen, reinforcement-learning, self-hosted, text-to-speech, tts, ui, unsloth |
| 许可证 | Apache License 2.0 |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,106 |
| 语言 | TypeScript |
| Forks | 3,196 |
| Issues | 397 |
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
| Stars | 51,044 |
| 语言 | TypeScript |
| Forks | 23,976 |
| Issues | 808 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,949 |
| 语言 | HTML |
| Forks | 5,621 |
| Issues | 18 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,178 |
| 语言 | Python |
| Forks | 14,726 |
| Issues | 3,903 |
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
| Stars | 49,674 |
| 语言 | Python |
| Forks | 4,801 |
| Issues | 77 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 146,169 |
| 语言 | Python |
| Forks | 8,649 |
| Issues | 907 |
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
| Stars | 166,041 |
| 语言 | Go |
| Forks | 15,137 |
| Issues | 2,716 |
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
| Stars | 72,202 |
| 语言 | MDX |
| Forks | 7,709 |
| Issues | 250 |
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
| Stars | 46,983 |
| 语言 | Rust |
| Forks | 9,278 |
| Issues | 2 |
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
| Stars | 39,107 |
| 语言 | TypeScript |
| Forks | 3,954 |
| Issues | 1,086 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,872 |
| 语言 | Python |
| Forks | 2,573 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 92,065 |
| 语言 | Python |
| Forks | 5,493 |
| Issues | 484 |
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
| Stars | 68,995 |
| 语言 | Python |
| Forks | 8,411 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的开源大模型微调工具之一，通过统一框架整合了 LoRA、QLoRA、RLHF 等主流微调技术，支持 100+ 主流大模型，让研究者和开发者能以最低成本和最高效率完成模型定制化训练，是企业落地 AI 应用和个人学习大模型微调的理想选择。

**技术亮点**:
- 支持 100+ 语言模型和视觉语言模型（VLMs）的统一微调框架，包括 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成 LoRA、QLoRA、PEFT 等参数高效微调方法，配合量化技术，可在消费级 GPU 上微调大模型，大幅降低显存占用
- 支持 RLHF（人类反馈强化学习）和完整的 Instruction Tuning 训练流水线，以及 MoE（混合专家）架构模型的微调
- 基于 Transformers 生态，提供统一的 API 接口和丰富的训练策略配置，开箱即用，工程化成熟度高
- ACL 2024 学术顶会认可的开源项目，Apache License 2.0 许可证，商业友好

**适用场景**:
- 企业级 AI 应用开发：快速将开源大模型适配到特定业务场景（客服、文档分析、私域知识库等），降低模型定制化成本，加速 AI 产品落地
- 学术研究与算法实验：对比不同微调方法（LoRA vs QLoRA vs RLHF）或在不同模型架构上的效果，统一的框架设计让实验对比更加便捷
- 个人开发者与 AI 爱好者：学习大模型微调技术，在有限硬件资源下（如 3090/4090 显卡）微调专属模型，低门槛高效率



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,525 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 66 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个成熟的开源金融数据分析平台，拥有超过 63,000 Stars，被广泛应用于量化研究和投资分析。它整合了股票、加密货币、期权、固定收益等多品类金融数据，并支持 AI Agents 和机器学习集成，是构建智能投研系统的理想选择。

**技术亮点**:
- 模块化架构设计：采用插件化数据源系统，支持灵活扩展和自定义数据源接入
- AI Agents 原生支持：内置 AI 代理框架，便于构建智能投研助手和自动化分析流程
- 全品类金融覆盖：整合股票、加密货币、期权、衍生品、固定收益等多市场数据
- Python SDK + API + CLI 多接口：提供 SDK、REST API 和命令行工具，满足不同开发场景需求
- 内置量化分析工具：支持技术指标计算、回测框架和金融模型构建

**适用场景**:
- 量化交易研究：用于获取市场数据、计算技术指标、执行回测和构建交易策略
- 智能投研平台开发：结合 AI Agents 构建智能投研助手，实现自动化研报生成和数据分析
- 投资组合管理与分析：整合多品类资产数据进行投资组合分析、风险评估和业绩归因
- 金融数据 API 服务：基于 OpenBB API 构建金融数据服务，为内部系统或第三方应用提供数据支持



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,137 |
| 语言 | HTML |
| Forks | 20,256 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、最活跃的 AI 提示词开源社区项目，拥有超过 15 万星标，汇集了数千个经过验证的高质量提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，可免费自托管部署，非常适合个人和团队构建私有化的提示词库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态站点生成
- 支持多 LLM 平台提示词：OpenAI GPT-4、Claude、Gemini 等主流模型
- 提供 Docker 一键部署方案，支持企业私有化自托管，完全数据自主
- 社区驱动的提示词贡献机制，包含角色扮演、代码助手、内容创作等丰富分类
- CC0 许可证声明，完全开源可商用，无需任何依赖或 API 密钥成本

**适用场景**:
- 个人用户：发现、收藏和分享各类 AI 助手的优质提示词，提升日常工作和创作效率
- 企业团队：自托管部署私有提示词库，保护内部数据隐私，适合对数据安全有要求的组织
- 开发者：参考和借鉴高质量提示词的设计模式，用于构建自己的 AI 应用或提示词管理工具



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,162 |
| 语言 | Jupyter Notebook |
| Forks | 13,595 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个极其优质的 LLM 从零实现教程项目，以 89k+ Stars 证明了其在 AI 教育领域的标杆地位。项目通过 Jupyter Notebook 逐行代码讲解 ChatGPT 类 LLM 的完整实现，无需依赖 Hugging Face 等高级库，是深入理解大语言模型内部原理的最佳实践资源。

**技术亮点**:
- 从零实现 GPT 架构 - 不依赖任何高级 LLM 库，使用纯 PyTorch 构建完整语言模型
- 逐行代码详解 - 每个组件（Embedding、注意力机制、前馈网络等）都有详尽注释和解释
- 完整训练流程覆盖 - 包含数据预处理、tokenization、训练循环、模型评估的端到端实现
- 深入注意力机制 - 从零实现 Multi-Head Attention、RoPE 等先进注意力变体
- 教学导向设计 - 配套书籍《Build a Large Language Model (From Scratch)》系统化学习路径

**适用场景**:
- LLM/Deep Learning 学习者 - 系统学习 Transformer 架构和 LLM 内部工作原理的入门到进阶路径
- AI 教育者/讲师 - 作为课程教材或实验项目，用于教授大语言模型基础知识
- PyTorch 开发者 - 理解如何从底层实现一个生产级别的语言模型，提升工程能力



### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,654 |
| 语言 | Jupyter Notebook |
| Forks | 5,416 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,337 |
| 语言 | Python |
| Forks | 32,590 |
| Issues | 2,282 |
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
| Stars | 74,178 |
| 语言 | Python |
| Forks | 14,726 |
| Issues | 3,903 |
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
| Stars | 106,831 |
| 语言 | Python |
| Forks | 12,301 |
| Issues | 3,884 |
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
| Stars | 98,536 |
| 语言 | Python |
| Forks | 27,289 |
| Issues | 18,122 |
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
| Stars | 72,202 |
| 语言 | MDX |
| Forks | 7,709 |
| Issues | 250 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,381 |
| 语言 | TypeScript |
| Forks | 3,619 |
| Issues | 288 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,977 |
| 语言 | Python |
| Forks | 30,200 |
| Issues | 2,473 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


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
| Stars | 104,534 |
| 语言 | JavaScript |
| Forks | 13,591 |
| Issues | 122 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 Claude Code、Codex、Cursor 等主流 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 等核心模块实现智能化开发流程，10万+ Stars 证明了其在 AI 辅助开发领域的高人气和实用价值。

**技术亮点**:
- 统一支持多种 AI 代码助手：Claude Code、Codex、Opencode、Cursor 等主流工具
- 核心模块化设计：Skills（技能）、Instincts（本能）、Memory（记忆）三大支柱
- MCP (Model Context Protocol) 深度集成，提升上下文理解和任务执行能力
- 内置安全机制和权限控制，确保 AI 辅助开发的安全性
- 以研究为导向的开发方法论，持续探索 AI Agent 性能优化前沿

**适用场景**:
- 企业开发团队：建立标准化的 AI 辅助开发流程，提升团队协作效率和代码质量
- 个人开发者：快速构建和优化 AI 代码助手工作流，实现开发效率倍增
- AI Agent 研究者：基于该框架探索 LLM 在软件开发领域的最佳实践和性能瓶颈



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,323 |
| 语言 | Go |
| Forks | 3,789 |
| Issues | 142 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像和视频等多种生成式 AI 模型，无需 GPU 支持，极大地降低了 AI 应用的部署门槛和成本。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和并发处理能力，适合构建可扩展的 AI 服务
- 支持多模态模型：LLM（如 LLaMA、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）和目标检测等
- 去中心化架构设计，支持 libp2p 协议，可实现分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移
- 支持 MCP（Model Context Protocol）协议，实现模型与工具的标准化交互

**适用场景**:
- 本地/私有化 AI 部署：适合需要在本地运行 AI 应用的企业，满足数据隐私合规要求
- 边缘计算场景：在没有强大 GPU 的边缘设备上运行 AI 推理任务
- 成本敏感型应用：个人开发者或小型企业可零成本运行 AI 模型，无需依赖云服务



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,679 |
| 语言 | Python |
| Forks | 8,729 |
| Issues | 337 |
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
| Stars | 43,106 |
| 语言 | TypeScript |
| Forks | 3,196 |
| Issues | 397 |
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
| Stars | 180,857 |
| 语言 | TypeScript |
| Forks | 56,113 |
| Issues | 1,432 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 415,686 |
| 语言 | Python |
| Forks | 45,050 |
| Issues | 1,089 |
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
| Stars | 153,084 |
| 语言 | Python |
| Forks | 12,402 |
| Issues | 2,400 |
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
| Stars | 96,525 |
| 语言 | Python |
| Forks | 8,922 |
| Issues | 161 |
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
| Stars | 74,044 |
| 语言 | Python |
| Forks | 8,790 |
| Issues | 201 |
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
| Stars | 183,025 |
| 语言 | TypeScript |
| Forks | 38,725 |
| Issues | 15,491 |
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
| Stars | 93,924 |
| 语言 | TypeScript |
| Forks | 9,398 |
| Issues | 295 |
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
| Stars | 78,593 |
| 语言 | TypeScript |
| Forks | 5,720 |
| Issues | 733 |
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
| Stars | 76,817 |
| 语言 | TypeScript |
| Forks | 6,568 |
| Issues | 168 |
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
| Stars | 75,673 |
| 语言 | JavaScript |
| Forks | 7,266 |
| Issues | 707 |
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
| Stars | 78,916 |
| 语言 | Go |
| Forks | 2,733 |
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
| Stars | 74,975 |
| 语言 | Go |
| Forks | 2,631 |
| Issues | 945 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,872 |
| 语言 | Python |
| Forks | 2,573 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### ⭐ 中优先级


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 54,672 |
| 语言 | JavaScript |
| Forks | 4,053 |
| Issues | 1,413 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
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
| Stars | 43,106 |
| 语言 | TypeScript |
| Forks | 3,196 |
| Issues | 397 |
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
| Stars | 180,857 |
| 语言 | TypeScript |
| Forks | 56,113 |
| Issues | 1,432 |
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
| Stars | 51,693 |
| 语言 | Go |
| Forks | 10,342 |
| Issues | 216 |
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
| Stars | 121,327 |
| 语言 | Go |
| Forks | 42,721 |
| Issues | 2,626 |
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
| Stars | 71,561 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,799 |
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
| Stars | 54,460 |
| 语言 | Go |
| Forks | 6,490 |
| Issues | 2,869 |
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
| Stars | 93,924 |
| 语言 | TypeScript |
| Forks | 9,398 |
| Issues | 295 |
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
| Stars | 75,742 |
| 语言 | TypeScript |
| Forks | 6,448 |
| Issues | 433 |
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
| Stars | 84,430 |
| 语言 | JavaScript |
| Forks | 7,559 |
| Issues | 701 |
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
| Stars | 69,509 |
| 语言 | Go |
| Forks | 1,886 |
| Issues | 302 |
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
| Stars | 62,346 |
| 语言 | Go |
| Forks | 5,888 |
| Issues | 776 |
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
| Stars | 58,153 |
| 语言 | Go |
| Forks | 4,207 |
| Issues | 30 |
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
| Stars | 47,600 |
| 语言 | Go |
| Forks | 5,069 |
| Issues | 969 |
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
| Stars | 84,430 |
| 语言 | JavaScript |
| Forks | 7,559 |
| Issues | 701 |
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
| Stars | 63,285 |
| 语言 | Go |
| Forks | 10,265 |
| Issues | 758 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (13 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,323 |
| 语言 | Go |
| Forks | 3,789 |
| Issues | 142 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像和视频等多种生成式 AI 模型，无需 GPU 支持，极大地降低了 AI 应用的部署门槛和成本。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和并发处理能力，适合构建可扩展的 AI 服务
- 支持多模态模型：LLM（如 LLaMA、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）和目标检测等
- 去中心化架构设计，支持 libp2p 协议，可实现分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移
- 支持 MCP（Model Context Protocol）协议，实现模型与工具的标准化交互

**适用场景**:
- 本地/私有化 AI 部署：适合需要在本地运行 AI 应用的企业，满足数据隐私合规要求
- 边缘计算场景：在没有强大 GPU 的边缘设备上运行 AI 推理任务
- 成本敏感型应用：个人开发者或小型企业可零成本运行 AI 模型，无需依赖云服务



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 415,686 |
| 语言 | Python |
| Forks | 45,050 |
| Issues | 1,089 |
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
| Stars | 96,525 |
| 语言 | Python |
| Forks | 8,922 |
| Issues | 161 |
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
| Stars | 87,111 |
| 语言 | Python |
| Forks | 33,782 |
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
| Stars | 100,125 |
| 语言 | TypeScript |
| Forks | 27,131 |
| Issues | 1,116 |
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
| Stars | 78,593 |
| 语言 | TypeScript |
| Forks | 5,720 |
| Issues | 733 |
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
| Stars | 75,673 |
| 语言 | JavaScript |
| Forks | 7,266 |
| Issues | 707 |
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
| Stars | 55,948 |
| 语言 | JavaScript |
| Forks | 10,212 |
| Issues | 353 |
| Topics | blog, compiler, gatsby, graphql, react, static-site-generator, web-app |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,068 |
| 语言 | Go |
| Forks | 4,689 |
| Issues | 252 |
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
| Stars | 57,091 |
| 语言 | Go |
| Forks | 3,213 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,872 |
| 语言 | Python |
| Forks | 2,573 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### ⭐ 中优先级


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,884 |
| 语言 | JavaScript |
| Forks | 22,907 |
| Issues | 194 |
| Topics | express, javascript, nodejs, server |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,305 |
| 语言 | Go |
| Forks | 8,570 |
| Issues | 649 |
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
| Stars | 99,558 |
| 语言 | TypeScript |
| Forks | 11,875 |
| Issues | 957 |
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
| Stars | 56,673 |
| 语言 | JavaScript |
| Forks | 6,124 |
| Issues | 298 |
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
| Stars | 43,452 |
| 语言 | Go |
| Forks | 3,910 |
| Issues | 1,102 |
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
| Stars | 51,693 |
| 语言 | Go |
| Forks | 10,342 |
| Issues | 216 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (9 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,137 |
| 语言 | HTML |
| Forks | 20,256 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、最活跃的 AI 提示词开源社区项目，拥有超过 15 万星标，汇集了数千个经过验证的高质量提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，可免费自托管部署，非常适合个人和团队构建私有化的提示词库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态站点生成
- 支持多 LLM 平台提示词：OpenAI GPT-4、Claude、Gemini 等主流模型
- 提供 Docker 一键部署方案，支持企业私有化自托管，完全数据自主
- 社区驱动的提示词贡献机制，包含角色扮演、代码助手、内容创作等丰富分类
- CC0 许可证声明，完全开源可商用，无需任何依赖或 API 密钥成本

**适用场景**:
- 个人用户：发现、收藏和分享各类 AI 助手的优质提示词，提升日常工作和创作效率
- 企业团队：自托管部署私有提示词库，保护内部数据隐私，适合对数据安全有要求的组织
- 开发者：参考和借鉴高质量提示词的设计模式，用于构建自己的 AI 应用或提示词管理工具



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,928 |
| 语言 | TypeScript |
| Forks | 5,990 |
| Issues | 75 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,949 |
| 语言 | HTML |
| Forks | 5,621 |
| Issues | 18 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,202 |
| 语言 | MDX |
| Forks | 7,709 |
| Issues | 250 |
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
| Stars | 89,509 |
| 语言 | TypeScript |
| Forks | 9,937 |
| Issues | 2,221 |
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
| Stars | 86,891 |
| 语言 | TypeScript |
| Forks | 8,757 |
| Issues | 1,618 |
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
| Stars | 127,207 |
| 语言 | JavaScript |
| Forks | 12,458 |
| Issues | 4 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### jaywcjlove/awesome-mac

**描述**:  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy search and use.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,812 |
| 语言 | JavaScript |
| Forks | 7,528 |
| Issues | 228 |
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
| Stars | 168,139 |
| 语言 | Go |
| Forks | 13,088 |
| Issues | 174 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (64 个项目) { #其他 }


### 🌟 高优先级


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,509 |
| 语言 | Python |
| Forks | 6,389 |
| Issues | 39 |
| 许可证 | Apache License 2.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,863 |
| 语言 | Python |
| Forks | 6,986 |
| Issues | 625 |
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
| Stars | 80,309 |
| 语言 | Python |
| Forks | 11,717 |
| Issues | 101 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
| 许可证 | GNU Affero General Public License v3.0 |


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 133,057 |
| 语言 | Unknown |
| Forks | 33,609 |
| Issues | 138 |
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
| Stars | 384,534 |
| 语言 | Python |
| Forks | 66,052 |
| Issues | 72 |
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
| Stars | 113,801 |
| 语言 | TypeScript |
| Forks | 5,799 |
| Issues | 352 |
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
| Stars | 105,112 |
| 语言 | TypeScript |
| Forks | 7,639 |
| Issues | 199 |
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
| Stars | 48,000 |
| 语言 | Go |
| Forks | 10,257 |
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
| Stars | 99,185 |
| 语言 | C++ |
| Forks | 15,769 |
| Issues | 1,292 |
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
| Stars | 62,324 |
| 语言 | Python |
| Forks | 1,621 |
| Issues | 38 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,630 |
| 语言 | TypeScript |
| Forks | 5,596 |
| Issues | 186 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,687 |
| 语言 | JavaScript |
| Forks | 3,304 |
| Issues | 7 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 340,086 |
| 语言 | Python |
| Forks | 55,014 |
| Issues | 518 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 288,794 |
| 语言 | Python |
| Forks | 27,475 |
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
| Stars | 85,814 |
| 语言 | Python |
| Forks | 37,091 |
| Issues | 3,523 |
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
| Stars | 77,691 |
| 语言 | Python |
| Forks | 45,209 |
| Issues | 1,281 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 438,784 |
| 语言 | TypeScript |
| Forks | 43,756 |
| Issues | 224 |
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
| Stars | 351,606 |
| 语言 | TypeScript |
| Forks | 43,851 |
| Issues | 31 |
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
| Stars | 138,348 |
| 语言 | TypeScript |
| Forks | 16,483 |
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
| Stars | 119,484 |
| 语言 | TypeScript |
| Forks | 12,988 |
| Issues | 2,876 |
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
| Stars | 110,620 |
| 语言 | TypeScript |
| Forks | 8,292 |
| Issues | 1,787 |
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
| Stars | 108,271 |
| 语言 | TypeScript |
| Forks | 13,301 |
| Issues | 5,499 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,758 |
| 语言 | TypeScript |
| Forks | 54,575 |
| Issues | 1,362 |
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
| Stars | 95,607 |
| 语言 | TypeScript |
| Forks | 5,169 |
| Issues | 684 |
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
| Stars | 94,180 |
| 语言 | TypeScript |
| Forks | 5,125 |
| Issues | 96 |
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
| Stars | 83,035 |
| 语言 | TypeScript |
| Forks | 7,579 |
| Issues | 32 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,959 |
| 语言 | TypeScript |
| Forks | 10,057 |
| Issues | 584 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,322 |
| 语言 | TypeScript |
| Forks | 7,960 |
| Issues | 682 |
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
| Stars | 244,156 |
| 语言 | JavaScript |
| Forks | 50,853 |
| Issues | 1,176 |
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
| Stars | 116,408 |
| 语言 | JavaScript |
| Forks | 35,149 |
| Issues | 2,565 |
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
| Stars | 111,541 |
| 语言 | JavaScript |
| Forks | 36,308 |
| Issues | 587 |
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
| Stars | 108,657 |
| 语言 | JavaScript |
| Forks | 11,558 |
| Issues | 346 |
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
| Stars | 98,028 |
| 语言 | JavaScript |
| Forks | 32,691 |
| Issues | 1,714 |
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
| Stars | 95,455 |
| 语言 | JavaScript |
| Forks | 15,286 |
| Issues | 50 |
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
| Stars | 86,129 |
| 语言 | JavaScript |
| Forks | 4,824 |
| Issues | 971 |
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
| Stars | 78,860 |
| 语言 | JavaScript |
| Forks | 31,598 |
| Issues | 268 |
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
| Stars | 70,849 |
| 语言 | JavaScript |
| Forks | 16,806 |
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
| Stars | 66,015 |
| 语言 | JavaScript |
| Forks | 9,346 |
| Issues | 196 |
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
| Stars | 62,300 |
| 语言 | JavaScript |
| Forks | 3,987 |
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
| Stars | 59,867 |
| 语言 | JavaScript |
| Forks | 20,473 |
| Issues | 96 |
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
| Stars | 57,408 |
| 语言 | JavaScript |
| Forks | 12,301 |
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
| Stars | 53,023 |
| 语言 | JavaScript |
| Forks | 10,601 |
| Issues | 480 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,133 |
| 语言 | JavaScript |
| Forks | 11,386 |
| Issues | 369 |
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
| Stars | 133,143 |
| 语言 | Go |
| Forks | 18,877 |
| Issues | 9,879 |
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
| Stars | 105,552 |
| 语言 | Go |
| Forks | 14,957 |
| Issues | 47 |
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
| Stars | 87,254 |
| 语言 | Go |
| Forks | 8,223 |
| Issues | 254 |
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
| Stars | 81,088 |
| 语言 | Go |
| Forks | 4,968 |
| Issues | 409 |
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
| Stars | 68,670 |
| 语言 | Go |
| Forks | 3,222 |
| Issues | 7 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,237 |
| 语言 | Go |
| Forks | 4,991 |
| Issues | 1,154 |
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
| Stars | 50,952 |
| 语言 | Go |
| Forks | 21,878 |
| Issues | 377 |
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
| Stars | 61,486 |
| 语言 | Shell |
| Forks | 9,242 |
| Issues | 105 |
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
| Stars | 219,016 |
| 语言 | Python |
| Forks | 50,240 |
| Issues | 891 |
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
| Stars | 85,510 |
| 语言 | Python |
| Forks | 7,180 |
| Issues | 478 |
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
| Stars | 76,325 |
| 语言 | Python |
| Forks | 16,780 |
| Issues | 19 |
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
| Stars | 148,118 |
| 语言 | JavaScript |
| Forks | 26,755 |
| Issues | 189 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,300 |
| 语言 | JavaScript |
| Forks | 11,974 |
| Issues | 539 |
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
| Stars | 66,291 |
| 语言 | JavaScript |
| Forks | 9,189 |
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
| Stars | 61,575 |
| 语言 | JavaScript |
| Forks | 7,125 |
| Issues | 136 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,010 |
| 语言 | JavaScript |
| Forks | 5,626 |
| Issues | 66 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,340 |
| 语言 | Go |
| Forks | 1,592 |
| Issues | 264 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,219 |
| 语言 | Go |
| Forks | 7,971 |
| Issues | 566 |
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
| Stars | 46,973 |
| 语言 | Go |
| Forks | 8,873 |
| Issues | 8 |
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
| Stars | 45,630 |
| 语言 | Go |
| Forks | 3,775 |
| Issues | 95 |
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
| Stars | 147,285 |
| 语言 | Python |
| Forks | 11,253 |
| Issues | 306 |
| Topics | awesome, github, hellogithub, python |
