# 项目发现报告 (2026-03-23)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
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
| Stars | 128,399 |
| 语言 | Python |
| Forks | 18,139 |
| Issues | 286 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama、OpenAI API 等多种后端，部署简单且功能丰富，是快速搭建自托管 AI 助手的最佳选择，特别适合注重隐私和想要完全掌控 AI 数据的用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，灵活性极高
- 完整的 RAG 功能：内置检索增强生成支持，可连接外部知识库增强 AI 回答质量
- MCP 协议支持：支持 Model Context Protocol，实现与外部工具和服务的高级集成
- 开箱即用的 Web UI：提供现代化的响应式界面，支持对话管理、模型切换、文件上传等功能
- 自托管部署：纯 Python 实现，支持 Docker 一键部署，完全私有化，数据不出本地

**适用场景**:
- 企业内部 AI 助手：企业可完全私有化部署 AI 对话系统，保障数据安全，适合处理内部文档、客服、知识库问答等场景
- 个人开发者/AI 爱好者：快速搭建个人 AI 助手，支持本地 Ollama 模型运行，降低 AI 使用成本
- 隐私敏感场景：医疗、金融、法律等行业需要严格数据保护的环境，可完全离线部署使用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,908 |
| 语言 | Python |
| Forks | 8,488 |
| Issues | 3,150 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最受欢迎的开源 RAG 引擎之一（75k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，提供了从文档解析到智能问答的端到端解决方案，特别适合需要构建高质量上下文感知的 LLM 应用的企业和开发者。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 AI Agent 能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel 等）的智能解析和结构化提取，精准切分内容块
- GraphRAG 支持：集成知识图谱增强的检索能力，提升关系推理和复杂查询的效果
- 多 LLM 后端兼容：同时支持 OpenAI、Ollama、DeepSeek 等主流模型，可灵活切换和对比
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业级智能知识库：构建支持自然语言查询的内部文档问答系统，自动理解并从海量文档中检索精准答案
- 智能文档处理平台：对合同、报告、手册等复杂文档进行自动解析、分类和关键信息提取
- AI 应用快速原型开发：开发者可基于 RAGFlow 快速搭建具有深度理解能力的 LLM 上层应用，降低 RAG 系统开发门槛



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,927 |
| 语言 | TypeScript |
| Forks | 6,566 |
| Issues | 232 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前最成熟的 AI 网页数据提取工具，专门解决 LLM 应用获取高质量训练/推理数据的问题，支持一键将任意网站转换为结构化 markdown 或 JSON，96k+ Stars 证明其稳定性和社区认可度。

**技术亮点**:
- 专为 AI/LLM 应用设计的数据管道，支持将网页直接转换为 LLM-ready 的 markdown 格式
- 智能 HTML 到 Markdown 转换引擎，保留关键内容结构同时去除噪音代码
- 支持结构化数据提取（JSON/表格），可自定义提取规则适应不同需求
- 具备反爬虫对抗能力，支持 JavaScript 渲染页面的抓取
- 提供 RESTful API 和多语言 SDK（TypeScript/Python/Go 等），易于集成到现有系统

**适用场景**:
- 构建 RAG（检索增强生成）系统的数据源，从网站批量提取高质量文本用于 LLM 微调或知识问答
- AI 应用开发中需要结构化网页数据的场景，如竞品分析、市场调研、价格监控等数据采集
- 企业知识库构建与文档数字化，将分散的 Web 文档统一转换为可用的 markdown 或结构化数据



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,443 |
| 语言 | JavaScript |
| Forks | 13,211 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化框架，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code 等 AI 编码助手的开发效率，特别适合追求极致 AI 开发工作流的团队。

**技术亮点**:
- 多代理支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一的性能优化接口
- MCP (Model Context Protocol) 集成：标准化的模型上下文协议实现，支持多工具协同和上下文管理
- 记忆系统：内置 Memory 模块实现会话持久化和知识复用，提升长期开发场景的 AI 理解能力
- 安全优先架构：提供沙箱隔离和权限控制机制，确保 AI 操作的安全性
- 研究驱动的开发模式：集成 Research First 理念，支持代码分析和优化建议的智能化生成

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编码工具，优化团队协作流程和代码质量标准
- 个人开发者效率提升：快速构建基于 AI 的开发环境，自动化日常编码任务和代码审查
- AI 代理系统研究：用于研究和实验 LLM 在代码生成场景下的性能优化和行为调优



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,274 |
| 语言 | Go |
| Forks | 3,787 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地AI引擎，支持运行LLM、图像、语音、视频等多种模型，提供了OpenAI兼容的API接口且无需GPU即可部署，是企业和开发者构建私有化AI能力的理想选择。

**技术亮点**:
- 多模型支持：集成了LLM（Llama、Mamba等）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种AI模型能力
- OpenAI API兼容：提供与OpenAI API完全兼容的接口，现有的OpenAI应用可以零成本迁移到本地部署
- Go语言实现：利用Go的高并发特性和优秀的跨平台支持，确保服务性能稳定且易于部署
- 去中心化架构：支持libp2p等分布式技术，可实现去中心化的AI推理网络
- 低门槛部署：无需GPU即可在消费级硬件上运行，大大降低了本地AI部署的硬件要求

**适用场景**:
- 企业私有化AI：构建企业内部的AI服务平台，数据完全本地化，满足金融、医疗等高隐私合规要求的行业
- 开发测试环境：为开发者提供本地化的AI API服务，降低开发成本，支持离线开发和快速迭代
- 个人AI助手：个人用户在本地运行各种AI模型，构建隐私保护的个性化AI助手，支持语音对话、图像生成等功能



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,174 |
| 语言 | TypeScript |
| Forks | 14,826 |
| Issues | 661 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发平台，提供了多 Agent 协作、知识库管理、MCP 协议支持等企业级特性，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，适合快速构建和部署生产级 AI 应用，尤其适合需要多 Agent 协作的企业级场景。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供标准化接口
- 多 Agent 协作框架：支持 Agent 间的协作与通信，实现复杂任务的分工处理
- MCP (Model Context Protocol) 协议支持：标准化的模型上下文交互协议，便于扩展和集成
- 知识库系统：内置知识库管理功能，支持 RAG 增强检索能力
- TypeScript 全栈架构：使用 TypeScript 构建，保证类型安全和代码可维护性

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务流程自动化系统
- AI 应用快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 MVP
- 智能助手平台搭建：构建集成了多种 AI 能力的统一对话和任务执行平台



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,938 |
| 语言 | Python |
| Forks | 8,400 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 通过统一接口封装了 LoRA、QLoRA、RLHF 等多种高效微调技术，支持 100+ 主流开源大模型和视觉语言模型的指令微调，极大降低了 LLM 自定义训练的门槛和计算成本，被 ACL 2024 录用并获得 68,938 Stars 的广泛认可

**技术亮点**:
- 多模型统一支持：覆盖 Llama、Qwen、Gemma、DeepSeek、Mistral 等 100+ 主流开源大模型及视觉语言模型
- 多种高效微调范式：集成 LoRA、QLoRA、Full-tuning 等 PEFT 方法，支持 RLHF、DPO、GRPO 等强化学习微调
- 量化与加速优化：支持 4-bit/8-bit 量化训练，大幅降低显存占用，支持单卡微调
- 一键式训练流程：提供 CLI 和 Web UI，简化数据预处理、训练监控、模型导出全流程
- 丰富的数据集支持：内置多种公开指令微调数据集，支持自定义数据格式导入

**适用场景**:
- 企业私有化部署：微调领域专属模型用于客服、知识库问答、业务流程自动化等场景
- 学术研究与模型对比：快速复现不同微调方法在各类模型上的效果，降低实验门槛
- 个人开发者定制 AI：无需深厚 ML 背景即可构建个性化 AI 应用如写作助手、代码生成工具
- 多模态模型训练：支持 VLMs 微调，适用于图文理解、视觉问答等视觉-语言任务



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,430 |
| 语言 | Python |
| Forks | 9,851 |
| Issues | 350 |
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
| Stars | 39,829 |
| 语言 | TypeScript |
| Forks | 2,924 |
| Issues | 170 |
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
| Stars | 36,959 |
| 语言 | TypeScript |
| Forks | 5,874 |
| Issues | 73 |
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
| Stars | 34,880 |
| 语言 | TypeScript |
| Forks | 7,073 |
| Issues | 448 |
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
| Stars | 33,585 |
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
| Stars | 45,527 |
| 语言 | Java |
| Forks | 15,847 |
| Issues | 58 |
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
| Stars | 38,824 |
| 语言 | Python |
| Forks | 6,160 |
| Issues | 140 |
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
| Stars | 32,613 |
| 语言 | Jupyter Notebook |
| Forks | 5,406 |
| Issues | 124 |
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
| Stars | 103,276 |
| 语言 | Python |
| Forks | 15,076 |
| Issues | 4 |
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
| Stars | 56,629 |
| 语言 | JavaScript |
| Forks | 6,121 |
| Issues | 304 |
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
| Stars | 69,617 |
| 语言 | Python |
| Forks | 8,731 |
| Issues | 338 |
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
| Stars | 57,769 |
| 语言 | Python |
| Forks | 4,872 |
| Issues | 1,034 |
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
| Stars | 42,796 |
| 语言 | TypeScript |
| Forks | 3,177 |
| Issues | 432 |
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
| Stars | 83,498 |
| 语言 | Python |
| Forks | 9,717 |
| Issues | 216 |
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
| Stars | 51,017 |
| 语言 | TypeScript |
| Forks | 23,982 |
| Issues | 809 |
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
| Stars | 180,686 |
| 语言 | TypeScript |
| Forks | 56,088 |
| Issues | 1,430 |
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
| Stars | 146,109 |
| 语言 | Python |
| Forks | 8,643 |
| Issues | 905 |
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
| Stars | 54,787 |
| 语言 | Jupyter Notebook |
| Forks | 18,956 |
| Issues | 6 |
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
| Stars | 72,153 |
| 语言 | MDX |
| Forks | 7,703 |
| Issues | 249 |
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
| Stars | 33,350 |
| 语言 | TypeScript |
| Forks | 3,613 |
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
| Stars | 32,285 |
| 语言 | Rust |
| Forks | 1,942 |
| Issues | 485 |
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
| Stars | 128,399 |
| 语言 | Python |
| Forks | 18,139 |
| Issues | 286 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama、OpenAI API 等多种后端，部署简单且功能丰富，是快速搭建自托管 AI 助手的最佳选择，特别适合注重隐私和想要完全掌控 AI 数据的用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，灵活性极高
- 完整的 RAG 功能：内置检索增强生成支持，可连接外部知识库增强 AI 回答质量
- MCP 协议支持：支持 Model Context Protocol，实现与外部工具和服务的高级集成
- 开箱即用的 Web UI：提供现代化的响应式界面，支持对话管理、模型切换、文件上传等功能
- 自托管部署：纯 Python 实现，支持 Docker 一键部署，完全私有化，数据不出本地

**适用场景**:
- 企业内部 AI 助手：企业可完全私有化部署 AI 对话系统，保障数据安全，适合处理内部文档、客服、知识库问答等场景
- 个人开发者/AI 爱好者：快速搭建个人 AI 助手，支持本地 Ollama 模型运行，降低 AI 使用成本
- 隐私敏感场景：医疗、金融、法律等行业需要严格数据保护的环境，可完全离线部署使用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,908 |
| 语言 | Python |
| Forks | 8,488 |
| Issues | 3,150 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最受欢迎的开源 RAG 引擎之一（75k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，提供了从文档解析到智能问答的端到端解决方案，特别适合需要构建高质量上下文感知的 LLM 应用的企业和开发者。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 AI Agent 能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel 等）的智能解析和结构化提取，精准切分内容块
- GraphRAG 支持：集成知识图谱增强的检索能力，提升关系推理和复杂查询的效果
- 多 LLM 后端兼容：同时支持 OpenAI、Ollama、DeepSeek 等主流模型，可灵活切换和对比
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业级智能知识库：构建支持自然语言查询的内部文档问答系统，自动理解并从海量文档中检索精准答案
- 智能文档处理平台：对合同、报告、手册等复杂文档进行自动解析、分类和关键信息提取
- AI 应用快速原型开发：开发者可基于 RAGFlow 快速搭建具有深度理解能力的 LLM 上层应用，降低 RAG 系统开发门槛



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,174 |
| 语言 | TypeScript |
| Forks | 14,826 |
| Issues | 661 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发平台，提供了多 Agent 协作、知识库管理、MCP 协议支持等企业级特性，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，适合快速构建和部署生产级 AI 应用，尤其适合需要多 Agent 协作的企业级场景。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供标准化接口
- 多 Agent 协作框架：支持 Agent 间的协作与通信，实现复杂任务的分工处理
- MCP (Model Context Protocol) 协议支持：标准化的模型上下文交互协议，便于扩展和集成
- 知识库系统：内置知识库管理功能，支持 RAG 增强检索能力
- TypeScript 全栈架构：使用 TypeScript 构建，保证类型安全和代码可维护性

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务流程自动化系统
- AI 应用快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 MVP
- 智能助手平台搭建：构建集成了多种 AI 能力的统一对话和任务执行平台



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,829 |
| 语言 | TypeScript |
| Forks | 2,924 |
| Issues | 170 |
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
| Stars | 33,585 |
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
| Stars | 45,527 |
| 语言 | Java |
| Forks | 15,847 |
| Issues | 58 |
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
| Stars | 38,824 |
| 语言 | Python |
| Forks | 6,160 |
| Issues | 140 |
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
| Stars | 32,613 |
| 语言 | Jupyter Notebook |
| Forks | 5,406 |
| Issues | 124 |
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
| Stars | 103,276 |
| 语言 | Python |
| Forks | 15,076 |
| Issues | 4 |
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
| Stars | 99,538 |
| 语言 | TypeScript |
| Forks | 11,865 |
| Issues | 961 |
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
| Stars | 56,629 |
| 语言 | JavaScript |
| Forks | 6,121 |
| Issues | 304 |
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
| Stars | 51,017 |
| 语言 | TypeScript |
| Forks | 23,982 |
| Issues | 809 |
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
| Stars | 72,880 |
| 语言 | Python |
| Forks | 10,015 |
| Issues | 256 |
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
| Stars | 43,472 |
| 语言 | Go |
| Forks | 3,911 |
| Issues | 1,096 |
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
| Stars | 31,716 |
| 语言 | Python |
| Forks | 3,345 |
| Issues | 81 |
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
| Stars | 72,153 |
| 语言 | MDX |
| Forks | 7,703 |
| Issues | 249 |
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
| Stars | 33,350 |
| 语言 | TypeScript |
| Forks | 3,613 |
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
| Stars | 128,399 |
| 语言 | Python |
| Forks | 18,139 |
| Issues | 286 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama、OpenAI API 等多种后端，部署简单且功能丰富，是快速搭建自托管 AI 助手的最佳选择，特别适合注重隐私和想要完全掌控 AI 数据的用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，灵活性极高
- 完整的 RAG 功能：内置检索增强生成支持，可连接外部知识库增强 AI 回答质量
- MCP 协议支持：支持 Model Context Protocol，实现与外部工具和服务的高级集成
- 开箱即用的 Web UI：提供现代化的响应式界面，支持对话管理、模型切换、文件上传等功能
- 自托管部署：纯 Python 实现，支持 Docker 一键部署，完全私有化，数据不出本地

**适用场景**:
- 企业内部 AI 助手：企业可完全私有化部署 AI 对话系统，保障数据安全，适合处理内部文档、客服、知识库问答等场景
- 个人开发者/AI 爱好者：快速搭建个人 AI 助手，支持本地 Ollama 模型运行，降低 AI 使用成本
- 隐私敏感场景：医疗、金融、法律等行业需要严格数据保护的环境，可完全离线部署使用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,908 |
| 语言 | Python |
| Forks | 8,488 |
| Issues | 3,150 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最受欢迎的开源 RAG 引擎之一（75k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，提供了从文档解析到智能问答的端到端解决方案，特别适合需要构建高质量上下文感知的 LLM 应用的企业和开发者。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 AI Agent 能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel 等）的智能解析和结构化提取，精准切分内容块
- GraphRAG 支持：集成知识图谱增强的检索能力，提升关系推理和复杂查询的效果
- 多 LLM 后端兼容：同时支持 OpenAI、Ollama、DeepSeek 等主流模型，可灵活切换和对比
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业级智能知识库：构建支持自然语言查询的内部文档问答系统，自动理解并从海量文档中检索精准答案
- 智能文档处理平台：对合同、报告、手册等复杂文档进行自动解析、分类和关键信息提取
- AI 应用快速原型开发：开发者可基于 RAGFlow 快速搭建具有深度理解能力的 LLM 上层应用，降低 RAG 系统开发门槛



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,443 |
| 语言 | JavaScript |
| Forks | 13,211 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化框架，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code 等 AI 编码助手的开发效率，特别适合追求极致 AI 开发工作流的团队。

**技术亮点**:
- 多代理支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一的性能优化接口
- MCP (Model Context Protocol) 集成：标准化的模型上下文协议实现，支持多工具协同和上下文管理
- 记忆系统：内置 Memory 模块实现会话持久化和知识复用，提升长期开发场景的 AI 理解能力
- 安全优先架构：提供沙箱隔离和权限控制机制，确保 AI 操作的安全性
- 研究驱动的开发模式：集成 Research First 理念，支持代码分析和优化建议的智能化生成

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编码工具，优化团队协作流程和代码质量标准
- 个人开发者效率提升：快速构建基于 AI 的开发环境，自动化日常编码任务和代码审查
- AI 代理系统研究：用于研究和实验 LLM 在代码生成场景下的性能优化和行为调优



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,174 |
| 语言 | TypeScript |
| Forks | 14,826 |
| Issues | 661 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发平台，提供了多 Agent 协作、知识库管理、MCP 协议支持等企业级特性，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，适合快速构建和部署生产级 AI 应用，尤其适合需要多 Agent 协作的企业级场景。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供标准化接口
- 多 Agent 协作框架：支持 Agent 间的协作与通信，实现复杂任务的分工处理
- MCP (Model Context Protocol) 协议支持：标准化的模型上下文交互协议，便于扩展和集成
- 知识库系统：内置知识库管理功能，支持 RAG 增强检索能力
- TypeScript 全栈架构：使用 TypeScript 构建，保证类型安全和代码可维护性

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务流程自动化系统
- AI 应用快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 MVP
- 智能助手平台搭建：构建集成了多种 AI 能力的统一对话和任务执行平台



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,006 |
| 语言 | HTML |
| Forks | 20,247 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词开源项目，拥有超过 15 万 Stars，汇集了全球社区贡献的高质量提示词，支持自托管部署保护隐私，适合所有希望提升 AI 对话效率和质量的个人用户及企业团队。

**技术亮点**:
- 基于 Next.js 14 + TypeScript 构建，具备优秀的开发体验和类型安全
- 支持多种主流 LLM 平台集成，包括 ChatGPT、Claude、Gemini、GPT-4 等
- 开源且支持自托管部署，提供完整隐私保护，适合企业内网使用
- CC0 1.0 Universal 许可证，完全免费可商用，无任何使用限制
- 现代化的 Web 界面，支持提示词的浏览、搜索和社区贡献功能

**适用场景**:
- 个人用户快速查找和收藏高质量 AI 提示词，提升日常工作效率
- 企业自建提示词库，保护敏感数据同时利用社区最佳实践
- AI 开发者和 Prompt Engineer 学习参考，借鉴优秀提示词设计思路



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,085 |
| 语言 | Jupyter Notebook |
| Forks | 13,597 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是零基础学习LLM内部原理的绝佳资源，作者Sebastian Raschka通过89K+ Stars证明其教学实力。项目采用手把手教学方式，用PyTorch从矩阵乘法开始构建ChatGPT级别的LLM，彻底消除对黑盒框架的依赖，真正理解大模型的工作机制。

**技术亮点**:
- 从零实现无黑盒依赖：不使用Hugging Face Transformers等高层库，从张量运算开始手写注意力机制
- 渐进式学习路径设计：章节按难度递进，数据编码→Tokenization→Transformer架构→GPT训练→RLHF
- 完整覆盖现代LLM核心技术栈：包括Multi-Head Attention、Positional Encoding、Layer Normalization、BPE分词等
- Jupyter Notebook交互式教学：每行代码都附带详细注释和可视化，适合边学边实践的教学模式
- 涵盖指令微调与RLHF：包含完整的ChatGPT类模型的训练流程，包括人类反馈强化学习部分

**适用场景**:
- AI/ML研究人员与学生：系统性理解LLM架构细节，为科研或论文复现打下坚实基础
- 企业AI工程师：需要深度定制LLM或优化推理性能时，理解底层实现至关重要
- 个人开发者与AI爱好者：想从应用层进阶到模型层的开发者，通过此项目建立完整的LLM知识体系



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,430 |
| 语言 | Python |
| Forks | 9,851 |
| Issues | 350 |
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
| Stars | 39,829 |
| 语言 | TypeScript |
| Forks | 2,924 |
| Issues | 170 |
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
| Stars | 36,959 |
| 语言 | TypeScript |
| Forks | 5,874 |
| Issues | 73 |
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
| Stars | 34,880 |
| 语言 | TypeScript |
| Forks | 7,073 |
| Issues | 448 |
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
| Stars | 33,585 |
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
| Stars | 56,629 |
| 语言 | JavaScript |
| Forks | 6,121 |
| Issues | 304 |
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
| Stars | 69,617 |
| 语言 | Python |
| Forks | 8,731 |
| Issues | 338 |
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
| Stars | 57,769 |
| 语言 | Python |
| Forks | 4,872 |
| Issues | 1,034 |
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
| Stars | 42,796 |
| 语言 | TypeScript |
| Forks | 3,177 |
| Issues | 432 |
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
| Stars | 51,017 |
| 语言 | TypeScript |
| Forks | 23,982 |
| Issues | 809 |
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
| Stars | 34,891 |
| 语言 | HTML |
| Forks | 5,618 |
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
| Stars | 74,083 |
| 语言 | Python |
| Forks | 14,671 |
| Issues | 3,848 |
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
| Stars | 39,095 |
| 语言 | TypeScript |
| Forks | 3,954 |
| Issues | 1,086 |
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
| Stars | 146,109 |
| 语言 | Python |
| Forks | 8,643 |
| Issues | 905 |
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
| Stars | 165,961 |
| 语言 | Go |
| Forks | 15,116 |
| Issues | 2,705 |
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
| Stars | 72,153 |
| 语言 | MDX |
| Forks | 7,703 |
| Issues | 249 |
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
| Stars | 46,963 |
| 语言 | Rust |
| Forks | 9,262 |
| Issues | 2 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,936 |
| 语言 | Python |
| Forks | 5,477 |
| Issues | 483 |
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
| Stars | 48,863 |
| 语言 | Python |
| Forks | 4,735 |
| Issues | 87 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,861 |
| 语言 | Python |
| Forks | 2,571 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 68,938 |
| 语言 | Python |
| Forks | 8,400 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 通过统一接口封装了 LoRA、QLoRA、RLHF 等多种高效微调技术，支持 100+ 主流开源大模型和视觉语言模型的指令微调，极大降低了 LLM 自定义训练的门槛和计算成本，被 ACL 2024 录用并获得 68,938 Stars 的广泛认可

**技术亮点**:
- 多模型统一支持：覆盖 Llama、Qwen、Gemma、DeepSeek、Mistral 等 100+ 主流开源大模型及视觉语言模型
- 多种高效微调范式：集成 LoRA、QLoRA、Full-tuning 等 PEFT 方法，支持 RLHF、DPO、GRPO 等强化学习微调
- 量化与加速优化：支持 4-bit/8-bit 量化训练，大幅降低显存占用，支持单卡微调
- 一键式训练流程：提供 CLI 和 Web UI，简化数据预处理、训练监控、模型导出全流程
- 丰富的数据集支持：内置多种公开指令微调数据集，支持自定义数据格式导入

**适用场景**:
- 企业私有化部署：微调领域专属模型用于客服、知识库问答、业务流程自动化等场景
- 学术研究与模型对比：快速复现不同微调方法在各类模型上的效果，降低实验门槛
- 个人开发者定制 AI：无需深厚 ML 背景即可构建个性化 AI 应用如写作助手、代码生成工具
- 多模态模型训练：支持 VLMs 微调，适用于图文理解、视觉问答等视觉-语言任务



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,491 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 67 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有 63k+ Stars，专注于为分析师、量化交易员和 AI 代理提供统一的数据获取和分析能力。项目覆盖股票、加密货币、期权、衍生品、固定收益等多资产类别，并原生集成 AI/机器学习支持，是构建智能金融应用或量化交易系统的理想基础。

**技术亮点**:
- 统一数据 API：整合多个金融数据源，提供标准化的数据接口，简化数据获取流程
- AI/ML 原生支持：内置机器学习集成能力，支持构建 AI 驱动的交易策略和智能分析代理
- 多资产类别覆盖：支持股票、加密货币、期权、衍生品、固定收益等广泛金融产品
- 丰富的分析工具：提供技术分析、基本面分析、情绪分析等内置功能
- Python 优先设计：纯 Python 实现，生态友好，易于与现有数据科学生态系统集成

**适用场景**:
- 量化交易系统开发：为量化交易员提供数据获取、因子计算、策略回测的一站式解决方案
- AI 金融代理构建：基于项目提供的 API 和分析工具，开发智能投顾、交易机器人等 AI 应用
- 投资研究与分析：分析师可用于快速获取多市场数据、生成研报、进行跨资产比较分析
- 企业级金融数据平台：作为内部金融数据基础设施，为投行、资管公司等提供标准化数据服务



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,006 |
| 语言 | HTML |
| Forks | 20,247 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词开源项目，拥有超过 15 万 Stars，汇集了全球社区贡献的高质量提示词，支持自托管部署保护隐私，适合所有希望提升 AI 对话效率和质量的个人用户及企业团队。

**技术亮点**:
- 基于 Next.js 14 + TypeScript 构建，具备优秀的开发体验和类型安全
- 支持多种主流 LLM 平台集成，包括 ChatGPT、Claude、Gemini、GPT-4 等
- 开源且支持自托管部署，提供完整隐私保护，适合企业内网使用
- CC0 1.0 Universal 许可证，完全免费可商用，无任何使用限制
- 现代化的 Web 界面，支持提示词的浏览、搜索和社区贡献功能

**适用场景**:
- 个人用户快速查找和收藏高质量 AI 提示词，提升日常工作效率
- 企业自建提示词库，保护敏感数据同时利用社区最佳实践
- AI 开发者和 Prompt Engineer 学习参考，借鉴优秀提示词设计思路



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,085 |
| 语言 | Jupyter Notebook |
| Forks | 13,597 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是零基础学习LLM内部原理的绝佳资源，作者Sebastian Raschka通过89K+ Stars证明其教学实力。项目采用手把手教学方式，用PyTorch从矩阵乘法开始构建ChatGPT级别的LLM，彻底消除对黑盒框架的依赖，真正理解大模型的工作机制。

**技术亮点**:
- 从零实现无黑盒依赖：不使用Hugging Face Transformers等高层库，从张量运算开始手写注意力机制
- 渐进式学习路径设计：章节按难度递进，数据编码→Tokenization→Transformer架构→GPT训练→RLHF
- 完整覆盖现代LLM核心技术栈：包括Multi-Head Attention、Positional Encoding、Layer Normalization、BPE分词等
- Jupyter Notebook交互式教学：每行代码都附带详细注释和可视化，适合边学边实践的教学模式
- 涵盖指令微调与RLHF：包含完整的ChatGPT类模型的训练流程，包括人类反馈强化学习部分

**适用场景**:
- AI/ML研究人员与学生：系统性理解LLM架构细节，为科研或论文复现打下坚实基础
- 企业AI工程师：需要深度定制LLM或优化推理性能时，理解底层实现至关重要
- 个人开发者与AI爱好者：想从应用层进阶到模型层的开发者，通过此项目建立完整的LLM知识体系



### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,613 |
| 语言 | Jupyter Notebook |
| Forks | 5,406 |
| Issues | 124 |
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
| Stars | 158,306 |
| 语言 | Python |
| Forks | 32,584 |
| Issues | 2,292 |
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
| Stars | 74,083 |
| 语言 | Python |
| Forks | 14,671 |
| Issues | 3,848 |
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
| Stars | 106,749 |
| 语言 | Python |
| Forks | 12,296 |
| Issues | 3,882 |
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
| Stars | 98,531 |
| 语言 | Python |
| Forks | 27,281 |
| Issues | 18,091 |
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
| Stars | 72,153 |
| 语言 | MDX |
| Forks | 7,703 |
| Issues | 249 |
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
| Stars | 33,350 |
| 语言 | TypeScript |
| Forks | 3,613 |
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
| Stars | 161,975 |
| 语言 | Python |
| Forks | 30,193 |
| Issues | 2,469 |
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
| Stars | 101,443 |
| 语言 | JavaScript |
| Forks | 13,211 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化框架，通过 Skills、Instincts、Memory 等核心模块显著提升 Claude Code 等 AI 编码助手的开发效率，特别适合追求极致 AI 开发工作流的团队。

**技术亮点**:
- 多代理支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供统一的性能优化接口
- MCP (Model Context Protocol) 集成：标准化的模型上下文协议实现，支持多工具协同和上下文管理
- 记忆系统：内置 Memory 模块实现会话持久化和知识复用，提升长期开发场景的 AI 理解能力
- 安全优先架构：提供沙箱隔离和权限控制机制，确保 AI 操作的安全性
- 研究驱动的开发模式：集成 Research First 理念，支持代码分析和优化建议的智能化生成

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编码工具，优化团队协作流程和代码质量标准
- 个人开发者效率提升：快速构建基于 AI 的开发环境，自动化日常编码任务和代码审查
- AI 代理系统研究：用于研究和实验 LLM 在代码生成场景下的性能优化和行为调优



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,274 |
| 语言 | Go |
| Forks | 3,787 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地AI引擎，支持运行LLM、图像、语音、视频等多种模型，提供了OpenAI兼容的API接口且无需GPU即可部署，是企业和开发者构建私有化AI能力的理想选择。

**技术亮点**:
- 多模型支持：集成了LLM（Llama、Mamba等）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种AI模型能力
- OpenAI API兼容：提供与OpenAI API完全兼容的接口，现有的OpenAI应用可以零成本迁移到本地部署
- Go语言实现：利用Go的高并发特性和优秀的跨平台支持，确保服务性能稳定且易于部署
- 去中心化架构：支持libp2p等分布式技术，可实现去中心化的AI推理网络
- 低门槛部署：无需GPU即可在消费级硬件上运行，大大降低了本地AI部署的硬件要求

**适用场景**:
- 企业私有化AI：构建企业内部的AI服务平台，数据完全本地化，满足金融、医疗等高隐私合规要求的行业
- 开发测试环境：为开发者提供本地化的AI API服务，降低开发成本，支持离线开发和快速迭代
- 个人AI助手：个人用户在本地运行各种AI模型，构建隐私保护的个性化AI助手，支持语音对话、图像生成等功能



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,617 |
| 语言 | Python |
| Forks | 8,731 |
| Issues | 338 |
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
| Stars | 42,796 |
| 语言 | TypeScript |
| Forks | 3,177 |
| Issues | 432 |
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
| Stars | 180,686 |
| 语言 | TypeScript |
| Forks | 56,088 |
| Issues | 1,430 |
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
| Stars | 415,140 |
| 语言 | Python |
| Forks | 44,973 |
| Issues | 1,068 |
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
| Stars | 152,867 |
| 语言 | Python |
| Forks | 12,394 |
| Issues | 2,395 |
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
| Stars | 96,521 |
| 语言 | Python |
| Forks | 8,920 |
| Issues | 163 |
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
| Stars | 74,014 |
| 语言 | Python |
| Forks | 8,789 |
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
| Stars | 183,001 |
| 语言 | TypeScript |
| Forks | 38,711 |
| Issues | 15,514 |
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
| Stars | 93,911 |
| 语言 | TypeScript |
| Forks | 9,399 |
| Issues | 294 |
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
| Stars | 78,575 |
| 语言 | TypeScript |
| Forks | 5,721 |
| Issues | 729 |
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
| Stars | 76,799 |
| 语言 | TypeScript |
| Forks | 6,566 |
| Issues | 167 |
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
| Stars | 75,674 |
| 语言 | JavaScript |
| Forks | 7,273 |
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
| Stars | 78,926 |
| 语言 | Go |
| Forks | 2,738 |
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
| Stars | 74,924 |
| 语言 | Go |
| Forks | 2,633 |
| Issues | 948 |
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
| Stars | 36,861 |
| 语言 | Python |
| Forks | 2,571 |
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
| Forks | 4,047 |
| Issues | 1,412 |
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
| Stars | 42,796 |
| 语言 | TypeScript |
| Forks | 3,177 |
| Issues | 432 |
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
| Stars | 180,686 |
| 语言 | TypeScript |
| Forks | 56,088 |
| Issues | 1,430 |
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
| Stars | 51,726 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 215 |
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
| Stars | 121,333 |
| 语言 | Go |
| Forks | 42,720 |
| Issues | 2,625 |
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
| Forks | 18,914 |
| Issues | 3,800 |
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
| Stars | 54,443 |
| 语言 | Go |
| Forks | 6,489 |
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
| Stars | 93,911 |
| 语言 | TypeScript |
| Forks | 9,399 |
| Issues | 294 |
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
| Stars | 75,700 |
| 语言 | TypeScript |
| Forks | 6,443 |
| Issues | 439 |
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
| Stars | 84,389 |
| 语言 | JavaScript |
| Forks | 7,557 |
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
| Stars | 69,492 |
| 语言 | Go |
| Forks | 1,888 |
| Issues | 305 |
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
| Stars | 62,363 |
| 语言 | Go |
| Forks | 5,887 |
| Issues | 779 |
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
| Stars | 58,146 |
| 语言 | Go |
| Forks | 4,211 |
| Issues | 23 |
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
| Stars | 47,596 |
| 语言 | Go |
| Forks | 5,069 |
| Issues | 964 |
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
| Stars | 84,389 |
| 语言 | JavaScript |
| Forks | 7,557 |
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
| Stars | 63,298 |
| 语言 | Go |
| Forks | 10,263 |
| Issues | 754 |
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
| Stars | 44,274 |
| 语言 | Go |
| Forks | 3,787 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地AI引擎，支持运行LLM、图像、语音、视频等多种模型，提供了OpenAI兼容的API接口且无需GPU即可部署，是企业和开发者构建私有化AI能力的理想选择。

**技术亮点**:
- 多模型支持：集成了LLM（Llama、Mamba等）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种AI模型能力
- OpenAI API兼容：提供与OpenAI API完全兼容的接口，现有的OpenAI应用可以零成本迁移到本地部署
- Go语言实现：利用Go的高并发特性和优秀的跨平台支持，确保服务性能稳定且易于部署
- 去中心化架构：支持libp2p等分布式技术，可实现去中心化的AI推理网络
- 低门槛部署：无需GPU即可在消费级硬件上运行，大大降低了本地AI部署的硬件要求

**适用场景**:
- 企业私有化AI：构建企业内部的AI服务平台，数据完全本地化，满足金融、医疗等高隐私合规要求的行业
- 开发测试环境：为开发者提供本地化的AI API服务，降低开发成本，支持离线开发和快速迭代
- 个人AI助手：个人用户在本地运行各种AI模型，构建隐私保护的个性化AI助手，支持语音对话、图像生成等功能



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 415,140 |
| 语言 | Python |
| Forks | 44,973 |
| Issues | 1,068 |
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
| Stars | 96,521 |
| 语言 | Python |
| Forks | 8,920 |
| Issues | 163 |
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
| Stars | 87,140 |
| 语言 | Python |
| Forks | 33,787 |
| Issues | 439 |
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
| Stars | 100,157 |
| 语言 | TypeScript |
| Forks | 27,136 |
| Issues | 1,102 |
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
| Stars | 78,575 |
| 语言 | TypeScript |
| Forks | 5,721 |
| Issues | 729 |
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
| Stars | 75,674 |
| 语言 | JavaScript |
| Forks | 7,273 |
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
| Stars | 55,954 |
| 语言 | JavaScript |
| Forks | 10,218 |
| Issues | 353 |
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
| Stars | 88,322 |
| 语言 | Go |
| Forks | 8,571 |
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
| Stars | 71,067 |
| 语言 | Go |
| Forks | 4,688 |
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
| Stars | 57,049 |
| 语言 | Go |
| Forks | 3,210 |
| Issues | 25 |
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
| Stars | 36,861 |
| 语言 | Python |
| Forks | 2,571 |
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
| Stars | 68,921 |
| 语言 | JavaScript |
| Forks | 22,900 |
| Issues | 194 |
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
| Stars | 99,538 |
| 语言 | TypeScript |
| Forks | 11,865 |
| Issues | 961 |
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
| Stars | 56,629 |
| 语言 | JavaScript |
| Forks | 6,121 |
| Issues | 304 |
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
| Stars | 43,472 |
| 语言 | Go |
| Forks | 3,911 |
| Issues | 1,096 |
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
| Stars | 51,726 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 215 |
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
| Stars | 154,006 |
| 语言 | HTML |
| Forks | 20,247 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词开源项目，拥有超过 15 万 Stars，汇集了全球社区贡献的高质量提示词，支持自托管部署保护隐私，适合所有希望提升 AI 对话效率和质量的个人用户及企业团队。

**技术亮点**:
- 基于 Next.js 14 + TypeScript 构建，具备优秀的开发体验和类型安全
- 支持多种主流 LLM 平台集成，包括 ChatGPT、Claude、Gemini、GPT-4 等
- 开源且支持自托管部署，提供完整隐私保护，适合企业内网使用
- CC0 1.0 Universal 许可证，完全免费可商用，无任何使用限制
- 现代化的 Web 界面，支持提示词的浏览、搜索和社区贡献功能

**适用场景**:
- 个人用户快速查找和收藏高质量 AI 提示词，提升日常工作效率
- 企业自建提示词库，保护敏感数据同时利用社区最佳实践
- AI 开发者和 Prompt Engineer 学习参考，借鉴优秀提示词设计思路



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,959 |
| 语言 | TypeScript |
| Forks | 5,874 |
| Issues | 73 |
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
| Stars | 34,891 |
| 语言 | HTML |
| Forks | 5,618 |
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
| Stars | 72,153 |
| 语言 | MDX |
| Forks | 7,703 |
| Issues | 249 |
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
| Forks | 9,940 |
| Issues | 2,215 |
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
| Stars | 86,901 |
| 语言 | TypeScript |
| Forks | 8,756 |
| Issues | 1,617 |
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
| Stars | 127,202 |
| 语言 | JavaScript |
| Forks | 12,466 |
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
| Stars | 100,742 |
| 语言 | JavaScript |
| Forks | 7,527 |
| Issues | 226 |
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
| Stars | 168,067 |
| 语言 | Go |
| Forks | 13,082 |
| Issues | 172 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (64 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,558 |
| 语言 | Shell |
| Forks | 9,089 |
| Issues | 101 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,458 |
| 语言 | Python |
| Forks | 6,383 |
| Issues | 45 |
| 许可证 | Apache License 2.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,405 |
| 语言 | Python |
| Forks | 6,941 |
| Issues | 623 |
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
| Stars | 80,281 |
| 语言 | Python |
| Forks | 11,718 |
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
| Stars | 132,875 |
| 语言 | Unknown |
| Forks | 33,589 |
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
| Stars | 384,496 |
| 语言 | Python |
| Forks | 66,049 |
| Issues | 78 |
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
| Stars | 113,492 |
| 语言 | TypeScript |
| Forks | 5,776 |
| Issues | 320 |
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
| Stars | 104,853 |
| 语言 | TypeScript |
| Forks | 7,623 |
| Issues | 195 |
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
| Stars | 48,022 |
| 语言 | Go |
| Forks | 10,255 |
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
| Stars | 99,091 |
| 语言 | C++ |
| Forks | 15,732 |
| Issues | 1,293 |
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
| Stars | 62,170 |
| 语言 | Python |
| Forks | 1,618 |
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
| Stars | 41,457 |
| 语言 | TypeScript |
| Forks | 5,155 |
| Issues | 166 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,714 |
| 语言 | JavaScript |
| Forks | 3,231 |
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
| Stars | 339,985 |
| 语言 | Python |
| Forks | 55,007 |
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
| Stars | 288,675 |
| 语言 | Python |
| Forks | 27,470 |
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
| Stars | 85,789 |
| 语言 | Python |
| Forks | 37,078 |
| Issues | 3,568 |
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
| Stars | 77,693 |
| 语言 | Python |
| Forks | 45,213 |
| Issues | 1,281 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,301 |
| 语言 | Python |
| Forks | 16,780 |
| Issues | 19 |
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
| Stars | 438,775 |
| 语言 | TypeScript |
| Forks | 43,754 |
| Issues | 227 |
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
| Stars | 351,556 |
| 语言 | TypeScript |
| Forks | 43,839 |
| Issues | 29 |
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
| Stars | 138,333 |
| 语言 | TypeScript |
| Forks | 16,477 |
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
| Stars | 119,432 |
| 语言 | TypeScript |
| Forks | 12,974 |
| Issues | 2,877 |
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
| Stars | 110,531 |
| 语言 | TypeScript |
| Forks | 8,283 |
| Issues | 1,788 |
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
| Stars | 108,258 |
| 语言 | TypeScript |
| Forks | 13,309 |
| Issues | 5,498 |
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
| Stars | 97,783 |
| 语言 | TypeScript |
| Forks | 54,580 |
| Issues | 1,368 |
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
| Stars | 95,542 |
| 语言 | TypeScript |
| Forks | 5,171 |
| Issues | 680 |
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
| Stars | 94,191 |
| 语言 | TypeScript |
| Forks | 5,124 |
| Issues | 98 |
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
| Stars | 83,032 |
| 语言 | TypeScript |
| Forks | 7,578 |
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
| Stars | 81,868 |
| 语言 | TypeScript |
| Forks | 10,044 |
| Issues | 572 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,329 |
| 语言 | TypeScript |
| Forks | 7,959 |
| Issues | 676 |
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
| Stars | 244,168 |
| 语言 | JavaScript |
| Forks | 50,857 |
| Issues | 1,182 |
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
| Stars | 116,427 |
| 语言 | JavaScript |
| Forks | 35,155 |
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
| Stars | 111,521 |
| 语言 | JavaScript |
| Forks | 36,310 |
| Issues | 586 |
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
| Stars | 108,660 |
| 语言 | JavaScript |
| Forks | 11,563 |
| Issues | 347 |
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
| Stars | 98,074 |
| 语言 | JavaScript |
| Forks | 32,696 |
| Issues | 1,727 |
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
| Stars | 95,459 |
| 语言 | JavaScript |
| Forks | 15,282 |
| Issues | 49 |
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
| Stars | 86,146 |
| 语言 | JavaScript |
| Forks | 4,822 |
| Issues | 967 |
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
| Stars | 78,851 |
| 语言 | JavaScript |
| Forks | 31,593 |
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
| Stars | 70,835 |
| 语言 | JavaScript |
| Forks | 16,808 |
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
| Stars | 66,030 |
| 语言 | JavaScript |
| Forks | 9,345 |
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
| Stars | 62,276 |
| 语言 | JavaScript |
| Forks | 3,985 |
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
| Stars | 59,869 |
| 语言 | JavaScript |
| Forks | 20,473 |
| Issues | 99 |
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
| Stars | 57,406 |
| 语言 | JavaScript |
| Forks | 12,302 |
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
| Stars | 53,015 |
| 语言 | JavaScript |
| Forks | 10,602 |
| Issues | 476 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,122 |
| 语言 | JavaScript |
| Forks | 11,387 |
| Issues | 376 |
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
| Stars | 133,164 |
| 语言 | Go |
| Forks | 18,872 |
| Issues | 9,880 |
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
| Stars | 105,523 |
| 语言 | Go |
| Forks | 14,960 |
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
| Stars | 87,230 |
| 语言 | Go |
| Forks | 8,221 |
| Issues | 251 |
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
| Stars | 81,055 |
| 语言 | Go |
| Forks | 4,969 |
| Issues | 407 |
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
| Stars | 68,671 |
| 语言 | Go |
| Forks | 3,223 |
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
| Stars | 56,209 |
| 语言 | Go |
| Forks | 4,991 |
| Issues | 1,151 |
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
| Stars | 50,948 |
| 语言 | Go |
| Forks | 21,874 |
| Issues | 377 |
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
| Stars | 50,314 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 264 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,211 |
| 语言 | Go |
| Forks | 7,975 |
| Issues | 568 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 219,011 |
| 语言 | Python |
| Forks | 50,246 |
| Issues | 889 |
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
| Stars | 85,487 |
| 语言 | Python |
| Forks | 7,179 |
| Issues | 478 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


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
| Forks | 26,760 |
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
| Stars | 67,299 |
| 语言 | JavaScript |
| Forks | 11,974 |
| Issues | 538 |
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
| Stars | 66,297 |
| 语言 | JavaScript |
| Forks | 9,195 |
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
| Stars | 61,576 |
| 语言 | JavaScript |
| Forks | 7,126 |
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
| Stars | 59,977 |
| 语言 | JavaScript |
| Forks | 5,623 |
| Issues | 66 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,971 |
| 语言 | Go |
| Forks | 8,875 |
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
| Stars | 45,609 |
| 语言 | Go |
| Forks | 3,776 |
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
| Stars | 147,161 |
| 语言 | Python |
| Forks | 11,253 |
| Issues | 306 |
| Topics | awesome, github, hellogithub, python |
