# 项目发现报告 (2026-03-27)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 29 |
| 已在监控 | 26 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
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
| Stars | 128,972 |
| 语言 | Python |
| Forks | 18,240 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最成熟的开源 LLM Web 界面项目之一，支持 Ollama/OpenAI 等多后端、内置 RAG 和 MCP 扩展能力，自托管部署确保数据隐私，适合企业搭建私有 AI 助手或开发者快速构建本地 LLM 开发环境。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 及任何 OpenAPI 兼容接口，灵活性强
- RAG 检索增强生成：内置向量数据库集成，可连接外部知识库提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于与外部工具和服务集成扩展
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业安全合规要求
- Python 技术栈：基于 FastAPI 等现代 Python 框架构建，便于二次开发和定制

**适用场景**:
- 企业私有 AI 助手：完全自托管部署，企业内部知识库问答、客户支持自动化等场景
- 个人开发者本地 LLM 开发环境：快速搭建本地 AI 测试平台，支持多模型切换和知识库问答
- RAG 应用开发：利用内置 RAG 功能构建垂直领域知识问答系统，如文档检索、技术支持等
- AI 能力集成：作为前端界面，为现有业务系统快速添加 AI 对话能力



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,407 |
| 语言 | Python |
| Forks | 8,557 |
| Issues | 3,170 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前开源 RAG 领域最成熟的项目之一，将检索增强生成与 Agent 能力深度融合，为大语言模型提供高质量的上下文理解层。凭借 76K+ Stars 和 Apache 2.0 开源许可，它是企业构建智能文档问答系统和深度研究应用的绝佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：创新的将传统 RAG 检索能力与 Agent 自主决策能力结合，支持复杂的多跳推理和动态工具调用
- 深度文档理解：内置强大的文档解析引擎，支持 PDF、Word、Excel 等多格式文档的智能解析和结构化提取
- 多 LLM 灵活接入：原生支持 OpenAI、Ollama、DeepSeek 等主流大模型，可根据场景灵活切换，降低部署成本
- GraphRAG 支持：集成图检索增强生成能力，通过知识图谱提升复杂关联查询的效果
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务无缝集成

**适用场景**:
- 企业级智能问答系统：构建基于私有知识库的客服机器人，支持复杂文档检索和多轮对话
- 深度研究辅助：适用于学术研究、市场分析等需要多文档关联分析和深度推理的场景
- 文档智能处理：自动解析和理解合同、报告、技术文档等非结构化内容，提取关键信息



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,346 |
| 语言 | TypeScript |
| Forks | 6,655 |
| Issues | 237 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据提取工具，能将整个网站快速转换为 LLM 可直接使用的 markdown 或结构化数据，拥有近 10 万 Stars 的社区认可，是构建 AI 爬虫和数据管道的首选解决方案。

**技术亮点**:
- 专为 AI/LLM 应用优化，自动提取网页内容并转换为 Markdown 格式，去除噪音和无关代码
- 支持整站抓取（Sitemap 解析），能够递归抓取整个网站的所有页面并保持内容结构
- 提供智能 HTML 转 Markdown 功能，保留关键内容结构同时去除广告、导航栏等干扰元素
- 输出结构化数据，支持 JSON 格式的 API 响应，便于 AI 应用直接解析和使用
- 支持多种高级功能：JavaScript 渲染、代理轮换、速率限制、缓存机制等企业级特性

**适用场景**:
- 构建 AI 知识库和 RAG 系统：从网站、文档中提取内容作为大语言模型的上下文知识
- 开发 AI 代理和数据管道：为 AI Agent 提供可靠的网页数据采集能力，实现自动化信息获取
- 内容聚合和监控：批量抓取多个网站内容，提取结构化数据进行市场调研、竞品分析或新闻聚合



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,031 |
| 语言 | JavaScript |
| Forks | 14,605 |
| Issues | 144 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对主流 AI 编程代理（Claude Code、Cursor 等）的性能优化系统，通过 Skills、Instincts、Memory、Security 等模块化设计显著提升 AI Agent 的开发效率和安全性，Stars 超过 11 万证明了其在开发者社区的高度认可。

**技术亮点**:
- 模块化 Agent 架构：支持 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块，可独立扩展和定制
- 多代理兼容性：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，降低学习和迁移成本
- MCP（Model Context Protocol）深度集成：实现标准化的上下文管理和工具调用，提升 AI 响应的准确性和连贯性
- 研究优先开发模式（Research-First Development）：内置研究和分析工作流，确保 AI 决策基于充分的信息检索
- 安全沙箱机制：提供企业级的安全保障，防止 AI Agent 执行未经授权的操作

**适用场景**:
- 团队协作场景：企业开发团队使用该框架统一管理多个 AI 编程助手，确保代码质量和安全策略一致性
- AI Agent 性能调优：个人开发者或团队针对特定编程任务优化 AI Agent 的响应速度和准确性
- 开发者工具集成：工具厂商基于此框架构建增强型 IDE 插件，扩展 AI 编程能力



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,482 |
| 语言 | Go |
| Forks | 3,811 |
| Issues | 150 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地AI引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，能在任何硬件上无需GPU运行，极大降低了AI应用部署的门槛，非常适合需要数据隐私保护、离线使用或成本控制的场景。

**技术亮点**:
- 多模态支持：同时支持 LLMs (Llama, Mamba)、图像生成 (Stable Diffusion)、音频生成 (MusicGen)、语音合成 (TTS) 等多种模型类型
- 无 GPU 依赖：可在 CPU 环境下运行，降低硬件要求，适合资源受限的场景
- Go 语言实现：高性能、高并发，结合 libp2p 实现去中心化和分布式部署
- API 优先设计：提供统一的 REST API 接口，支持 MCP 协议，便于与现有系统集成
- 丰富的功能覆盖：涵盖文本生成、代理 (Agents)、对象检测、文本重排序 (Rerank) 等多种AI能力

**适用场景**:
- 私有化 AI 部署：企业或开发者需要在本地运行 AI 模型，保护数据隐私，避免云端 API 费用
- 边缘计算与物联网：将 AI 能力部署到边缘设备或嵌入式系统中，实现离线智能
- 个人开发者与学习研究：在没有高端 GPU 的环境下学习和实验各种 AI 模型，零成本探索 AI 技术
- 快速原型开发：通过统一 API 快速集成多种 AI 能力到应用中，支持Agents、图像生成等多种场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,403 |
| 语言 | TypeScript |
| Forks | 14,840 |
| Issues | 673 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的多智能体协作平台，提供了完整的 Agent 团队设计框架和 MCP 协议支持，能够帮助开发者和企业快速构建、部署和管理 AI Agent 工作流，特别适合需要多 Agent 协作复杂业务场景的团队。

**技术亮点**:
- 基于 MCP (Model Context Protocol) 协议，支持扩展性强的基础设施连接
- 内置多 Agent 协作框架，支持 Agent 团队设计与动态编排
- 支持主流大模型：OpenAI GPT、Claude、DeepSeek、Gemini 等
- 提供完整的知识库系统，支持 RAG 增强检索能力
- TypeScript/React 技术栈，提供现代化 Web UI 和完整的 API 接口

**适用场景**:
- 企业级智能助手：构建支持多部门协作的 AI Agent 团队，实现业务流程自动化
- 开发者快速原型：利用现成的 Agent 框架和 MCP 扩展，快速搭建 AI 应用原型
- 个人知识管理：通过知识库 + Agent 协作打造个人 AI 助手，提升工作效率
- 复杂任务分解：使用多 Agent 协作处理需要多步骤推理的复杂任务



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,155 |
| 语言 | Python |
| Forks | 8,434 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的统一大模型微调框架，支持 100+ 主流 LLMs 和 VLMs，通过集成 LoRA/QLoRA/RLHF 等多种高效微调技术，将原本复杂的模型定制流程压缩到极简程度，是目前最成熟的开源 LLM 微调解决方案。

**技术亮点**:
- 统一微调框架：支持 Llama/Gemma/Qwen/DeepSeek 等 100+ 主流大模型，以及视觉语言模型，覆盖业界最广泛的开源模型生态
- 多种高效微调技术：内置 LoRA、QLoRA、Prefix-Tuning、Ptuning 等 PEFT 方法，支持 RLHF、DPO、KTO 等对齐算法
- 量化与 MoE 支持：支持 AWQ/GPTQ/BitsAndBytes 等多种量化方案，以及混合专家模型（MoE）的微调
- 一键训练部署：提供 WebUI 和 CLI 界面，支持从数据处理到模型训练、推理的完整流程，降低使用门槛
- ACL 2024 顶会收录：经过学术验证的框架设计，具备完整的实验复现性和性能基准

**适用场景**:
- 企业 AI 定制：快速将通用 LLM 微调为垂直领域助手（如金融客服、医疗问答、法律咨询），结合量化技术实现低成本部署
- 学术研究实验：研究人员可便捷对比不同微调方法（LoRA vs RLHF vs DPO）在各类模型上的效果差异，加速论文实验迭代
- AI 产品原型验证：创业团队或个人开发者快速验证 LLM 应用想法，支持私有化部署和定制化训练，无需深入理解底层技术细节



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,588 |
| 语言 | Python |
| Forks | 9,866 |
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
| Stars | 41,526 |
| 语言 | TypeScript |
| Forks | 3,074 |
| Issues | 207 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,008 |
| 语言 | TypeScript |
| Forks | 7,107 |
| Issues | 466 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,594 |
| 语言 | Java |
| Forks | 15,853 |
| Issues | 81 |
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
| Stars | 38,845 |
| 语言 | Python |
| Forks | 6,165 |
| Issues | 108 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,656 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,450 |
| 语言 | TypeScript |
| Forks | 3,627 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,743 |
| 语言 | Jupyter Notebook |
| Forks | 5,427 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,886 |
| 语言 | JavaScript |
| Forks | 6,150 |
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
| Stars | 69,932 |
| 语言 | Python |
| Forks | 8,763 |
| Issues | 345 |
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
| Stars | 44,131 |
| 语言 | TypeScript |
| Forks | 3,279 |
| Issues | 342 |
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
| Stars | 84,744 |
| 语言 | Python |
| Forks | 9,811 |
| Issues | 191 |
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
| Stars | 51,152 |
| 语言 | TypeScript |
| Forks | 23,990 |
| Issues | 819 |
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
| Stars | 181,395 |
| 语言 | TypeScript |
| Forks | 56,234 |
| Issues | 1,418 |
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
| Stars | 146,313 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 925 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,324 |
| 语言 | MDX |
| Forks | 7,733 |
| Issues | 251 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 40,785 |
| 语言 | TypeScript |
| Forks | 6,339 |
| Issues | 82 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 103,771 |
| 语言 | Python |
| Forks | 15,145 |
| Issues | 5 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,443 |
| 语言 | Rust |
| Forks | 2,060 |
| Issues | 464 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### microsoft/ai-agents-for-beginners

**描述**: 12 Lessons to Get Started Building AI Agents

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,147 |
| 语言 | Jupyter Notebook |
| Forks | 19,044 |
| Issues | 12 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
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
| Stars | 128,972 |
| 语言 | Python |
| Forks | 18,240 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最成熟的开源 LLM Web 界面项目之一，支持 Ollama/OpenAI 等多后端、内置 RAG 和 MCP 扩展能力，自托管部署确保数据隐私，适合企业搭建私有 AI 助手或开发者快速构建本地 LLM 开发环境。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 及任何 OpenAPI 兼容接口，灵活性强
- RAG 检索增强生成：内置向量数据库集成，可连接外部知识库提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于与外部工具和服务集成扩展
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业安全合规要求
- Python 技术栈：基于 FastAPI 等现代 Python 框架构建，便于二次开发和定制

**适用场景**:
- 企业私有 AI 助手：完全自托管部署，企业内部知识库问答、客户支持自动化等场景
- 个人开发者本地 LLM 开发环境：快速搭建本地 AI 测试平台，支持多模型切换和知识库问答
- RAG 应用开发：利用内置 RAG 功能构建垂直领域知识问答系统，如文档检索、技术支持等
- AI 能力集成：作为前端界面，为现有业务系统快速添加 AI 对话能力



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,407 |
| 语言 | Python |
| Forks | 8,557 |
| Issues | 3,170 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前开源 RAG 领域最成熟的项目之一，将检索增强生成与 Agent 能力深度融合，为大语言模型提供高质量的上下文理解层。凭借 76K+ Stars 和 Apache 2.0 开源许可，它是企业构建智能文档问答系统和深度研究应用的绝佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：创新的将传统 RAG 检索能力与 Agent 自主决策能力结合，支持复杂的多跳推理和动态工具调用
- 深度文档理解：内置强大的文档解析引擎，支持 PDF、Word、Excel 等多格式文档的智能解析和结构化提取
- 多 LLM 灵活接入：原生支持 OpenAI、Ollama、DeepSeek 等主流大模型，可根据场景灵活切换，降低部署成本
- GraphRAG 支持：集成图检索增强生成能力，通过知识图谱提升复杂关联查询的效果
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务无缝集成

**适用场景**:
- 企业级智能问答系统：构建基于私有知识库的客服机器人，支持复杂文档检索和多轮对话
- 深度研究辅助：适用于学术研究、市场分析等需要多文档关联分析和深度推理的场景
- 文档智能处理：自动解析和理解合同、报告、技术文档等非结构化内容，提取关键信息



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,403 |
| 语言 | TypeScript |
| Forks | 14,840 |
| Issues | 673 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的多智能体协作平台，提供了完整的 Agent 团队设计框架和 MCP 协议支持，能够帮助开发者和企业快速构建、部署和管理 AI Agent 工作流，特别适合需要多 Agent 协作复杂业务场景的团队。

**技术亮点**:
- 基于 MCP (Model Context Protocol) 协议，支持扩展性强的基础设施连接
- 内置多 Agent 协作框架，支持 Agent 团队设计与动态编排
- 支持主流大模型：OpenAI GPT、Claude、DeepSeek、Gemini 等
- 提供完整的知识库系统，支持 RAG 增强检索能力
- TypeScript/React 技术栈，提供现代化 Web UI 和完整的 API 接口

**适用场景**:
- 企业级智能助手：构建支持多部门协作的 AI Agent 团队，实现业务流程自动化
- 开发者快速原型：利用现成的 Agent 框架和 MCP 扩展，快速搭建 AI 应用原型
- 个人知识管理：通过知识库 + Agent 协作打造个人 AI 助手，提升工作效率
- 复杂任务分解：使用多 Agent 协作处理需要多步骤推理的复杂任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,526 |
| 语言 | TypeScript |
| Forks | 3,074 |
| Issues | 207 |
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
| Stars | 45,594 |
| 语言 | Java |
| Forks | 15,853 |
| Issues | 81 |
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
| Stars | 38,845 |
| 语言 | Python |
| Forks | 6,165 |
| Issues | 108 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,656 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,450 |
| 语言 | TypeScript |
| Forks | 3,627 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,743 |
| 语言 | Jupyter Notebook |
| Forks | 5,427 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,755 |
| 语言 | TypeScript |
| Forks | 11,909 |
| Issues | 977 |
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
| Stars | 56,886 |
| 语言 | JavaScript |
| Forks | 6,150 |
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
| Stars | 51,152 |
| 语言 | TypeScript |
| Forks | 23,990 |
| Issues | 819 |
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
| Stars | 73,197 |
| 语言 | Python |
| Forks | 10,042 |
| Issues | 263 |
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
| Stars | 43,503 |
| 语言 | Go |
| Forks | 3,915 |
| Issues | 1,095 |
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
| Stars | 31,812 |
| 语言 | Python |
| Forks | 3,352 |
| Issues | 84 |
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
| Stars | 72,324 |
| 语言 | MDX |
| Forks | 7,733 |
| Issues | 251 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 103,771 |
| 语言 | Python |
| Forks | 15,145 |
| Issues | 5 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 💬 LLM 界面 (25 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 128,972 |
| 语言 | Python |
| Forks | 18,240 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最成熟的开源 LLM Web 界面项目之一，支持 Ollama/OpenAI 等多后端、内置 RAG 和 MCP 扩展能力，自托管部署确保数据隐私，适合企业搭建私有 AI 助手或开发者快速构建本地 LLM 开发环境。

**技术亮点**:
- 多后端兼容：同时支持 Ollama、OpenAI API 及任何 OpenAPI 兼容接口，灵活性强
- RAG 检索增强生成：内置向量数据库集成，可连接外部知识库提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于与外部工具和服务集成扩展
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业安全合规要求
- Python 技术栈：基于 FastAPI 等现代 Python 框架构建，便于二次开发和定制

**适用场景**:
- 企业私有 AI 助手：完全自托管部署，企业内部知识库问答、客户支持自动化等场景
- 个人开发者本地 LLM 开发环境：快速搭建本地 AI 测试平台，支持多模型切换和知识库问答
- RAG 应用开发：利用内置 RAG 功能构建垂直领域知识问答系统，如文档检索、技术支持等
- AI 能力集成：作为前端界面，为现有业务系统快速添加 AI 对话能力



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,407 |
| 语言 | Python |
| Forks | 8,557 |
| Issues | 3,170 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前开源 RAG 领域最成熟的项目之一，将检索增强生成与 Agent 能力深度融合，为大语言模型提供高质量的上下文理解层。凭借 76K+ Stars 和 Apache 2.0 开源许可，它是企业构建智能文档问答系统和深度研究应用的绝佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：创新的将传统 RAG 检索能力与 Agent 自主决策能力结合，支持复杂的多跳推理和动态工具调用
- 深度文档理解：内置强大的文档解析引擎，支持 PDF、Word、Excel 等多格式文档的智能解析和结构化提取
- 多 LLM 灵活接入：原生支持 OpenAI、Ollama、DeepSeek 等主流大模型，可根据场景灵活切换，降低部署成本
- GraphRAG 支持：集成图检索增强生成能力，通过知识图谱提升复杂关联查询的效果
- MCP 协议集成：支持 Model Context Protocol，便于与外部工具和服务无缝集成

**适用场景**:
- 企业级智能问答系统：构建基于私有知识库的客服机器人，支持复杂文档检索和多轮对话
- 深度研究辅助：适用于学术研究、市场分析等需要多文档关联分析和深度推理的场景
- 文档智能处理：自动解析和理解合同、报告、技术文档等非结构化内容，提取关键信息



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,031 |
| 语言 | JavaScript |
| Forks | 14,605 |
| Issues | 144 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对主流 AI 编程代理（Claude Code、Cursor 等）的性能优化系统，通过 Skills、Instincts、Memory、Security 等模块化设计显著提升 AI Agent 的开发效率和安全性，Stars 超过 11 万证明了其在开发者社区的高度认可。

**技术亮点**:
- 模块化 Agent 架构：支持 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块，可独立扩展和定制
- 多代理兼容性：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，降低学习和迁移成本
- MCP（Model Context Protocol）深度集成：实现标准化的上下文管理和工具调用，提升 AI 响应的准确性和连贯性
- 研究优先开发模式（Research-First Development）：内置研究和分析工作流，确保 AI 决策基于充分的信息检索
- 安全沙箱机制：提供企业级的安全保障，防止 AI Agent 执行未经授权的操作

**适用场景**:
- 团队协作场景：企业开发团队使用该框架统一管理多个 AI 编程助手，确保代码质量和安全策略一致性
- AI Agent 性能调优：个人开发者或团队针对特定编程任务优化 AI Agent 的响应速度和准确性
- 开发者工具集成：工具厂商基于此框架构建增强型 IDE 插件，扩展 AI 编程能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,403 |
| 语言 | TypeScript |
| Forks | 14,840 |
| Issues | 673 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的多智能体协作平台，提供了完整的 Agent 团队设计框架和 MCP 协议支持，能够帮助开发者和企业快速构建、部署和管理 AI Agent 工作流，特别适合需要多 Agent 协作复杂业务场景的团队。

**技术亮点**:
- 基于 MCP (Model Context Protocol) 协议，支持扩展性强的基础设施连接
- 内置多 Agent 协作框架，支持 Agent 团队设计与动态编排
- 支持主流大模型：OpenAI GPT、Claude、DeepSeek、Gemini 等
- 提供完整的知识库系统，支持 RAG 增强检索能力
- TypeScript/React 技术栈，提供现代化 Web UI 和完整的 API 接口

**适用场景**:
- 企业级智能助手：构建支持多部门协作的 AI Agent 团队，实现业务流程自动化
- 开发者快速原型：利用现成的 Agent 框架和 MCP 扩展，快速搭建 AI 应用原型
- 个人知识管理：通过知识库 + Agent 协作打造个人 AI 助手，提升工作效率
- 复杂任务分解：使用多 Agent 协作处理需要多步骤推理的复杂任务



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,415 |
| 语言 | HTML |
| Forks | 20,284 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的提示词开源项目，拥有超过15万星标，提供超过5000条精选提示词模板，支持完全私有化部署，是个人学习提示词工程和企业保护数据隐私的最佳选择。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态生成
- 采用 Creative Commons Zero (CC0) 许可证，代码和内容完全开源无版权限制
- 支持多 AI 平台（ChatGPT、Claude、Gemini 等）的提示词格式
- 提供完整的自托管部署方案，支持 Docker 一键部署
- 内置隐私保护机制，企业可完全控制数据和 API 调用

**适用场景**:
- 个人开发者学习提示词工程，快速获取高质量的 ChatGPT/GPT-4 使用模板
- 企业私有化部署，在保护 API 密钥和敏感数据的前提下使用 AI 服务
- AI 应用开发者集成提示词库到自己的产品中，提升用户体验



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,351 |
| 语言 | Jupyter Notebook |
| Forks | 13,639 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个非常适合深入学习 LLM 内部工作原理的开源项目，通过 Jupyter Notebook 从零开始逐步实现 ChatGPT 风格的 GPT 模型，帮助开发者建立对大语言模型核心技术的完整认知。

**技术亮点**:
- 使用 PyTorch 从零实现 Transformer 架构，包括自注意力机制、多头注意力、前馈网络等核心组件
- 完整实现 GPT-2 风格的模型，包括词嵌入、位置编码、层归一化和残差连接
- 基于 Jupyter Notebook 的教学设计，每一步都有详细的代码解释和可视化
- 实现文本生成功能，包括温度采样、top-k 和 top-p 采样策略
- 涵盖从数据预处理、模型训练到推理的完整 LLM 开发流程

**适用场景**:
- AI/ML 教育：适合高校课程、培训项目或自学，帮助理解 LLM 的底层原理和实现细节
- LLM 研究与实验：开发者可基于此项目进行模型架构修改、实验对比和算法创新
- 企业技术培训：用于团队内部技术分享，提升对生成式 AI 技术的理解深度



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,588 |
| 语言 | Python |
| Forks | 9,866 |
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
| Stars | 41,526 |
| 语言 | TypeScript |
| Forks | 3,074 |
| Issues | 207 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,008 |
| 语言 | TypeScript |
| Forks | 7,107 |
| Issues | 466 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,656 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
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
| Stars | 56,886 |
| 语言 | JavaScript |
| Forks | 6,150 |
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
| Stars | 69,932 |
| 语言 | Python |
| Forks | 8,763 |
| Issues | 345 |
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
| Stars | 44,131 |
| 语言 | TypeScript |
| Forks | 3,279 |
| Issues | 342 |
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
| Stars | 51,152 |
| 语言 | TypeScript |
| Forks | 23,990 |
| Issues | 819 |
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
| Stars | 35,109 |
| 语言 | HTML |
| Forks | 5,648 |
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
| Stars | 74,529 |
| 语言 | Python |
| Forks | 14,856 |
| Issues | 3,953 |
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
| Stars | 52,634 |
| 语言 | Python |
| Forks | 5,071 |
| Issues | 78 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,153 |
| 语言 | TypeScript |
| Forks | 3,962 |
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
| Stars | 146,313 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 925 |
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
| Stars | 166,310 |
| 语言 | Go |
| Forks | 15,195 |
| Issues | 2,737 |
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
| Stars | 72,324 |
| 语言 | MDX |
| Forks | 7,733 |
| Issues | 251 |
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
| Stars | 47,230 |
| 语言 | Rust |
| Forks | 9,331 |
| Issues | 3 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 40,785 |
| 语言 | TypeScript |
| Forks | 6,339 |
| Issues | 82 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,934 |
| 语言 | Python |
| Forks | 2,580 |
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
| Stars | 92,696 |
| 语言 | Python |
| Forks | 5,567 |
| Issues | 488 |
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
| Stars | 69,155 |
| 语言 | Python |
| Forks | 8,434 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的统一大模型微调框架，支持 100+ 主流 LLMs 和 VLMs，通过集成 LoRA/QLoRA/RLHF 等多种高效微调技术，将原本复杂的模型定制流程压缩到极简程度，是目前最成熟的开源 LLM 微调解决方案。

**技术亮点**:
- 统一微调框架：支持 Llama/Gemma/Qwen/DeepSeek 等 100+ 主流大模型，以及视觉语言模型，覆盖业界最广泛的开源模型生态
- 多种高效微调技术：内置 LoRA、QLoRA、Prefix-Tuning、Ptuning 等 PEFT 方法，支持 RLHF、DPO、KTO 等对齐算法
- 量化与 MoE 支持：支持 AWQ/GPTQ/BitsAndBytes 等多种量化方案，以及混合专家模型（MoE）的微调
- 一键训练部署：提供 WebUI 和 CLI 界面，支持从数据处理到模型训练、推理的完整流程，降低使用门槛
- ACL 2024 顶会收录：经过学术验证的框架设计，具备完整的实验复现性和性能基准

**适用场景**:
- 企业 AI 定制：快速将通用 LLM 微调为垂直领域助手（如金融客服、医疗问答、法律咨询），结合量化技术实现低成本部署
- 学术研究实验：研究人员可便捷对比不同微调方法（LoRA vs RLHF vs DPO）在各类模型上的效果差异，加速论文实验迭代
- AI 产品原型验证：创业团队或个人开发者快速验证 LLM 应用想法，支持私有化部署和定制化训练，无需深入理解底层技术细节



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,645 |
| 语言 | Python |
| Forks | 6,270 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，整合了股票、加密货币、期权、固定收益等多类资产的数据源和分析工具，同时原生支持 AI Agents 开发，是金融分析师、量化交易员和 AI 应用开发者的理想选择。

**技术亮点**:
- 统一的数据访问层：整合多个金融数据源（股票、加密货币、期权、固收等），提供标准化的 API 接口
- AI/ML 原生支持：内置机器学习模块，专为 AI Agents 设计，支持自动化金融分析流程
- 量化分析工具集：提供回测、技术指标、衍生品定价等量化金融常用功能
- 模块化架构设计：支持自定义扩展和数据源接入，便于构建定制化金融应用
- 活跃的开源社区：63K+ Stars，持续更新，文档完善，社区生态丰富

**适用场景**:
- 量化交易研究：用于量化分析师进行策略回测、技术分析和衍生品定价
- 金融数据分析：帮助分析师快速获取和可视化多资产类别的市场数据
- AI 金融应用开发：为构建 AI 驱动的投资顾问、交易机器人和金融预测模型提供基础设施
- 投资组合管理：支持投资组合构建、风险评估和固定收益分析



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,415 |
| 语言 | HTML |
| Forks | 20,284 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的提示词开源项目，拥有超过15万星标，提供超过5000条精选提示词模板，支持完全私有化部署，是个人学习提示词工程和企业保护数据隐私的最佳选择。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态生成
- 采用 Creative Commons Zero (CC0) 许可证，代码和内容完全开源无版权限制
- 支持多 AI 平台（ChatGPT、Claude、Gemini 等）的提示词格式
- 提供完整的自托管部署方案，支持 Docker 一键部署
- 内置隐私保护机制，企业可完全控制数据和 API 调用

**适用场景**:
- 个人开发者学习提示词工程，快速获取高质量的 ChatGPT/GPT-4 使用模板
- 企业私有化部署，在保护 API 密钥和敏感数据的前提下使用 AI 服务
- AI 应用开发者集成提示词库到自己的产品中，提升用户体验



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,351 |
| 语言 | Jupyter Notebook |
| Forks | 13,639 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个非常适合深入学习 LLM 内部工作原理的开源项目，通过 Jupyter Notebook 从零开始逐步实现 ChatGPT 风格的 GPT 模型，帮助开发者建立对大语言模型核心技术的完整认知。

**技术亮点**:
- 使用 PyTorch 从零实现 Transformer 架构，包括自注意力机制、多头注意力、前馈网络等核心组件
- 完整实现 GPT-2 风格的模型，包括词嵌入、位置编码、层归一化和残差连接
- 基于 Jupyter Notebook 的教学设计，每一步都有详细的代码解释和可视化
- 实现文本生成功能，包括温度采样、top-k 和 top-p 采样策略
- 涵盖从数据预处理、模型训练到推理的完整 LLM 开发流程

**适用场景**:
- AI/ML 教育：适合高校课程、培训项目或自学，帮助理解 LLM 的底层原理和实现细节
- LLM 研究与实验：开发者可基于此项目进行模型架构修改、实验对比和算法创新
- 企业技术培训：用于团队内部技术分享，提升对生成式 AI 技术的理解深度



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,450 |
| 语言 | TypeScript |
| Forks | 3,627 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,743 |
| 语言 | Jupyter Notebook |
| Forks | 5,427 |
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
| Stars | 158,495 |
| 语言 | Python |
| Forks | 32,644 |
| Issues | 2,297 |
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
| Stars | 74,529 |
| 语言 | Python |
| Forks | 14,856 |
| Issues | 3,953 |
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
| Stars | 107,146 |
| 语言 | Python |
| Forks | 12,347 |
| Issues | 3,902 |
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
| Stars | 98,629 |
| 语言 | Python |
| Forks | 27,323 |
| Issues | 18,113 |
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
| Stars | 72,324 |
| 语言 | MDX |
| Forks | 7,733 |
| Issues | 251 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 162,028 |
| 语言 | Python |
| Forks | 30,205 |
| Issues | 2,471 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


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
| Stars | 112,031 |
| 语言 | JavaScript |
| Forks | 14,605 |
| Issues | 144 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对主流 AI 编程代理（Claude Code、Cursor 等）的性能优化系统，通过 Skills、Instincts、Memory、Security 等模块化设计显著提升 AI Agent 的开发效率和安全性，Stars 超过 11 万证明了其在开发者社区的高度认可。

**技术亮点**:
- 模块化 Agent 架构：支持 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块，可独立扩展和定制
- 多代理兼容性：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，降低学习和迁移成本
- MCP（Model Context Protocol）深度集成：实现标准化的上下文管理和工具调用，提升 AI 响应的准确性和连贯性
- 研究优先开发模式（Research-First Development）：内置研究和分析工作流，确保 AI 决策基于充分的信息检索
- 安全沙箱机制：提供企业级的安全保障，防止 AI Agent 执行未经授权的操作

**适用场景**:
- 团队协作场景：企业开发团队使用该框架统一管理多个 AI 编程助手，确保代码质量和安全策略一致性
- AI Agent 性能调优：个人开发者或团队针对特定编程任务优化 AI Agent 的响应速度和准确性
- 开发者工具集成：工具厂商基于此框架构建增强型 IDE 插件，扩展 AI 编程能力



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,482 |
| 语言 | Go |
| Forks | 3,811 |
| Issues | 150 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地AI引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，能在任何硬件上无需GPU运行，极大降低了AI应用部署的门槛，非常适合需要数据隐私保护、离线使用或成本控制的场景。

**技术亮点**:
- 多模态支持：同时支持 LLMs (Llama, Mamba)、图像生成 (Stable Diffusion)、音频生成 (MusicGen)、语音合成 (TTS) 等多种模型类型
- 无 GPU 依赖：可在 CPU 环境下运行，降低硬件要求，适合资源受限的场景
- Go 语言实现：高性能、高并发，结合 libp2p 实现去中心化和分布式部署
- API 优先设计：提供统一的 REST API 接口，支持 MCP 协议，便于与现有系统集成
- 丰富的功能覆盖：涵盖文本生成、代理 (Agents)、对象检测、文本重排序 (Rerank) 等多种AI能力

**适用场景**:
- 私有化 AI 部署：企业或开发者需要在本地运行 AI 模型，保护数据隐私，避免云端 API 费用
- 边缘计算与物联网：将 AI 能力部署到边缘设备或嵌入式系统中，实现离线智能
- 个人开发者与学习研究：在没有高端 GPU 的环境下学习和实验各种 AI 模型，零成本探索 AI 技术
- 快速原型开发：通过统一 API 快速集成多种 AI 能力到应用中，支持Agents、图像生成等多种场景



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,932 |
| 语言 | Python |
| Forks | 8,763 |
| Issues | 345 |
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
| Stars | 44,131 |
| 语言 | TypeScript |
| Forks | 3,279 |
| Issues | 342 |
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
| Stars | 181,395 |
| 语言 | TypeScript |
| Forks | 56,234 |
| Issues | 1,418 |
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
| Stars | 153,553 |
| 语言 | Python |
| Forks | 12,451 |
| Issues | 2,411 |
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
| Stars | 96,649 |
| 语言 | Python |
| Forks | 8,955 |
| Issues | 168 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


### microsoft/vscode

**描述**: Visual Studio Code

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 183,151 |
| 语言 | TypeScript |
| Forks | 38,785 |
| Issues | 15,540 |
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
| Stars | 93,957 |
| 语言 | TypeScript |
| Forks | 9,403 |
| Issues | 298 |
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
| Stars | 78,658 |
| 语言 | TypeScript |
| Forks | 5,732 |
| Issues | 732 |
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
| Stars | 76,865 |
| 语言 | TypeScript |
| Forks | 6,569 |
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
| Stars | 75,684 |
| 语言 | JavaScript |
| Forks | 7,270 |
| Issues | 710 |
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
| Stars | 79,052 |
| 语言 | Go |
| Forks | 2,737 |
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
| Stars | 75,131 |
| 语言 | Go |
| Forks | 2,643 |
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
| Stars | 36,934 |
| 语言 | Python |
| Forks | 2,580 |
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
| Stars | 54,755 |
| 语言 | JavaScript |
| Forks | 4,064 |
| Issues | 1,416 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 416,752 |
| 语言 | Python |
| Forks | 45,202 |
| Issues | 1,102 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
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
| Stars | 44,131 |
| 语言 | TypeScript |
| Forks | 3,279 |
| Issues | 342 |
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
| Stars | 181,395 |
| 语言 | TypeScript |
| Forks | 56,234 |
| Issues | 1,418 |
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
| Stars | 51,717 |
| 语言 | Go |
| Forks | 10,340 |
| Issues | 221 |
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
| Stars | 121,397 |
| 语言 | Go |
| Forks | 42,747 |
| Issues | 2,647 |
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
| Stars | 71,566 |
| 语言 | Go |
| Forks | 18,910 |
| Issues | 3,795 |
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
| Stars | 54,530 |
| 语言 | Go |
| Forks | 6,496 |
| Issues | 2,872 |
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
| Stars | 93,957 |
| 语言 | TypeScript |
| Forks | 9,403 |
| Issues | 298 |
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
| Stars | 75,840 |
| 语言 | TypeScript |
| Forks | 6,456 |
| Issues | 440 |
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
| Stars | 84,570 |
| 语言 | JavaScript |
| Forks | 7,568 |
| Issues | 713 |
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
| Stars | 69,544 |
| 语言 | Go |
| Forks | 1,892 |
| Issues | 307 |
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
| Stars | 62,407 |
| 语言 | Go |
| Forks | 5,894 |
| Issues | 777 |
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
| Stars | 58,258 |
| 语言 | Go |
| Forks | 4,215 |
| Issues | 32 |
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
| Stars | 47,604 |
| 语言 | Go |
| Forks | 5,069 |
| Issues | 970 |
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
| Stars | 84,570 |
| 语言 | JavaScript |
| Forks | 7,568 |
| Issues | 713 |
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
| Stars | 63,315 |
| 语言 | Go |
| Forks | 10,272 |
| Issues | 760 |
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
| Stars | 44,482 |
| 语言 | Go |
| Forks | 3,811 |
| Issues | 150 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地AI引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，能在任何硬件上无需GPU运行，极大降低了AI应用部署的门槛，非常适合需要数据隐私保护、离线使用或成本控制的场景。

**技术亮点**:
- 多模态支持：同时支持 LLMs (Llama, Mamba)、图像生成 (Stable Diffusion)、音频生成 (MusicGen)、语音合成 (TTS) 等多种模型类型
- 无 GPU 依赖：可在 CPU 环境下运行，降低硬件要求，适合资源受限的场景
- Go 语言实现：高性能、高并发，结合 libp2p 实现去中心化和分布式部署
- API 优先设计：提供统一的 REST API 接口，支持 MCP 协议，便于与现有系统集成
- 丰富的功能覆盖：涵盖文本生成、代理 (Agents)、对象检测、文本重排序 (Rerank) 等多种AI能力

**适用场景**:
- 私有化 AI 部署：企业或开发者需要在本地运行 AI 模型，保护数据隐私，避免云端 API 费用
- 边缘计算与物联网：将 AI 能力部署到边缘设备或嵌入式系统中，实现离线智能
- 个人开发者与学习研究：在没有高端 GPU 的环境下学习和实验各种 AI 模型，零成本探索 AI 技术
- 快速原型开发：通过统一 API 快速集成多种 AI 能力到应用中，支持Agents、图像生成等多种场景



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,649 |
| 语言 | Python |
| Forks | 8,955 |
| Issues | 168 |
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
| Stars | 87,139 |
| 语言 | Python |
| Forks | 33,797 |
| Issues | 424 |
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
| Stars | 100,143 |
| 语言 | TypeScript |
| Forks | 27,144 |
| Issues | 1,113 |
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
| Stars | 78,658 |
| 语言 | TypeScript |
| Forks | 5,732 |
| Issues | 732 |
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
| Stars | 75,684 |
| 语言 | JavaScript |
| Forks | 7,270 |
| Issues | 710 |
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
| Stars | 55,955 |
| 语言 | JavaScript |
| Forks | 10,214 |
| Issues | 364 |
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
| Stars | 51,765 |
| 语言 | JavaScript |
| Forks | 4,686 |
| Issues | 1,464 |
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
| Stars | 88,343 |
| 语言 | Go |
| Forks | 8,575 |
| Issues | 654 |
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
| Stars | 71,143 |
| 语言 | Go |
| Forks | 4,690 |
| Issues | 251 |
| Topics | acme, automatic-https, caddy, caddyfile, go, golang, http, http-server, http3, https, privacy, reverse-proxy, security, tls, web-server |
| 许可证 | Apache License 2.0 |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,934 |
| 语言 | Python |
| Forks | 2,580 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 416,752 |
| 语言 | Python |
| Forks | 45,202 |
| Issues | 1,102 |
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
| Stars | 68,889 |
| 语言 | JavaScript |
| Forks | 22,929 |
| Issues | 196 |
| Topics | express, javascript, nodejs, server |
| 许可证 | MIT License |


### pocketbase/pocketbase

**描述**: Open Source realtime backend in 1 file

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,172 |
| 语言 | Go |
| Forks | 3,222 |
| Issues | 24 |
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
| Stars | 99,755 |
| 语言 | TypeScript |
| Forks | 11,909 |
| Issues | 977 |
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
| Stars | 56,886 |
| 语言 | JavaScript |
| Forks | 6,150 |
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
| Stars | 43,503 |
| 语言 | Go |
| Forks | 3,915 |
| Issues | 1,095 |
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
| Stars | 51,717 |
| 语言 | Go |
| Forks | 10,340 |
| Issues | 221 |
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
| Stars | 154,415 |
| 语言 | HTML |
| Forks | 20,284 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的提示词开源项目，拥有超过15万星标，提供超过5000条精选提示词模板，支持完全私有化部署，是个人学习提示词工程和企业保护数据隐私的最佳选择。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态生成
- 采用 Creative Commons Zero (CC0) 许可证，代码和内容完全开源无版权限制
- 支持多 AI 平台（ChatGPT、Claude、Gemini 等）的提示词格式
- 提供完整的自托管部署方案，支持 Docker 一键部署
- 内置隐私保护机制，企业可完全控制数据和 API 调用

**适用场景**:
- 个人开发者学习提示词工程，快速获取高质量的 ChatGPT/GPT-4 使用模板
- 企业私有化部署，在保护 API 密钥和敏感数据的前提下使用 AI 服务
- AI 应用开发者集成提示词库到自己的产品中，提升用户体验



### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,109 |
| 语言 | HTML |
| Forks | 5,648 |
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
| Stars | 72,324 |
| 语言 | MDX |
| Forks | 7,733 |
| Issues | 251 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 40,785 |
| 语言 | TypeScript |
| Forks | 6,339 |
| Issues | 82 |
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
| Stars | 89,546 |
| 语言 | TypeScript |
| Forks | 9,957 |
| Issues | 2,202 |
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
| Stars | 86,962 |
| 语言 | TypeScript |
| Forks | 8,778 |
| Issues | 1,625 |
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
| Stars | 127,244 |
| 语言 | JavaScript |
| Forks | 12,464 |
| Issues | 6 |
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
| Stars | 100,989 |
| 语言 | JavaScript |
| Forks | 7,536 |
| Issues | 232 |
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
| Stars | 168,436 |
| 语言 | Go |
| Forks | 13,097 |
| Issues | 170 |
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
| Stars | 133,456 |
| 语言 | Unknown |
| Forks | 33,668 |
| Issues | 141 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,198 |
| 语言 | Shell |
| Forks | 9,679 |
| Issues | 77 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,730 |
| 语言 | Python |
| Forks | 6,400 |
| Issues | 41 |
| 许可证 | Apache License 2.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,964 |
| 语言 | Python |
| Forks | 7,088 |
| Issues | 628 |
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
| Stars | 82,751 |
| 语言 | Python |
| Forks | 12,092 |
| Issues | 101 |
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
| Stars | 384,656 |
| 语言 | Python |
| Forks | 66,065 |
| Issues | 82 |
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
| Stars | 113,925 |
| 语言 | TypeScript |
| Forks | 5,814 |
| Issues | 317 |
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
| Stars | 105,841 |
| 语言 | TypeScript |
| Forks | 7,687 |
| Issues | 206 |
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
| Stars | 48,025 |
| 语言 | Go |
| Forks | 10,257 |
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
| Stars | 99,593 |
| 语言 | C++ |
| Forks | 15,898 |
| Issues | 1,297 |
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
| Stars | 62,834 |
| 语言 | Python |
| Forks | 1,629 |
| Issues | 30 |
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
| Stars | 52,120 |
| 语言 | TypeScript |
| Forks | 6,719 |
| Issues | 240 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,328 |
| 语言 | JavaScript |
| Forks | 3,480 |
| Issues | 36 |
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
| Stars | 340,412 |
| 语言 | Python |
| Forks | 55,065 |
| Issues | 519 |
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
| Stars | 289,301 |
| 语言 | Python |
| Forks | 27,497 |
| Issues | 19 |
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
| Stars | 219,101 |
| 语言 | Python |
| Forks | 50,255 |
| Issues | 902 |
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
| Stars | 96,742 |
| 语言 | Python |
| Forks | 11,932 |
| Issues | 118 |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,879 |
| 语言 | Python |
| Forks | 37,098 |
| Issues | 3,478 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,576 |
| 语言 | Python |
| Forks | 7,188 |
| Issues | 476 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### tensorflow/models

**描述**: Models and examples built with TensorFlow

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,687 |
| 语言 | Python |
| Forks | 45,198 |
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
| Stars | 438,918 |
| 语言 | TypeScript |
| Forks | 43,792 |
| Issues | 220 |
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
| Stars | 351,772 |
| 语言 | TypeScript |
| Forks | 43,869 |
| Issues | 37 |
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
| Stars | 138,395 |
| 语言 | TypeScript |
| Forks | 16,487 |
| Issues | 45 |
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
| Stars | 119,687 |
| 语言 | TypeScript |
| Forks | 13,026 |
| Issues | 2,907 |
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
| Stars | 110,884 |
| 语言 | TypeScript |
| Forks | 8,335 |
| Issues | 1,793 |
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
| Stars | 108,326 |
| 语言 | TypeScript |
| Forks | 13,309 |
| Issues | 5,001 |
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
| Stars | 97,793 |
| 语言 | TypeScript |
| Forks | 54,578 |
| Issues | 1,353 |
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
| Stars | 95,827 |
| 语言 | TypeScript |
| Forks | 5,204 |
| Issues | 658 |
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
| Stars | 94,215 |
| 语言 | TypeScript |
| Forks | 5,133 |
| Issues | 100 |
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
| Stars | 83,043 |
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
| Stars | 82,291 |
| 语言 | TypeScript |
| Forks | 10,103 |
| Issues | 608 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,403 |
| 语言 | TypeScript |
| Forks | 7,963 |
| Issues | 679 |
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
| Stars | 244,241 |
| 语言 | JavaScript |
| Forks | 50,861 |
| Issues | 1,188 |
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
| Stars | 116,461 |
| 语言 | JavaScript |
| Forks | 35,181 |
| Issues | 2,582 |
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
| Stars | 111,616 |
| 语言 | JavaScript |
| Forks | 36,314 |
| Issues | 576 |
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
| Stars | 108,656 |
| 语言 | JavaScript |
| Forks | 11,568 |
| Issues | 358 |
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
| Stars | 98,042 |
| 语言 | JavaScript |
| Forks | 32,689 |
| Issues | 1,718 |
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
| Stars | 95,475 |
| 语言 | JavaScript |
| Forks | 15,300 |
| Issues | 52 |
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
| Stars | 86,159 |
| 语言 | JavaScript |
| Forks | 4,832 |
| Issues | 978 |
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
| Stars | 78,909 |
| 语言 | JavaScript |
| Forks | 31,694 |
| Issues | 267 |
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
| Stars | 70,870 |
| 语言 | JavaScript |
| Forks | 16,811 |
| Issues | 890 |
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
| Stars | 66,301 |
| 语言 | JavaScript |
| Forks | 9,190 |
| Issues | 2 |
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
| Stars | 66,016 |
| 语言 | JavaScript |
| Forks | 9,357 |
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
| Stars | 62,354 |
| 语言 | JavaScript |
| Forks | 3,987 |
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
| Stars | 61,576 |
| 语言 | JavaScript |
| Forks | 7,125 |
| Issues | 134 |
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
| Stars | 60,072 |
| 语言 | JavaScript |
| Forks | 5,633 |
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
| Stars | 59,872 |
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
| Stars | 57,415 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 12 |
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
| Stars | 53,046 |
| 语言 | JavaScript |
| Forks | 10,605 |
| Issues | 468 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,166 |
| 语言 | JavaScript |
| Forks | 11,395 |
| Issues | 359 |
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
| Stars | 133,207 |
| 语言 | Go |
| Forks | 18,884 |
| Issues | 9,889 |
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
| Stars | 105,640 |
| 语言 | Go |
| Forks | 14,964 |
| Issues | 50 |
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
| Stars | 87,314 |
| 语言 | Go |
| Forks | 8,223 |
| Issues | 261 |
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
| Stars | 81,203 |
| 语言 | Go |
| Forks | 4,973 |
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
| Stars | 68,665 |
| 语言 | Go |
| Forks | 3,225 |
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
| Stars | 56,300 |
| 语言 | Go |
| Forks | 4,998 |
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
| Stars | 50,956 |
| 语言 | Go |
| Forks | 21,881 |
| Issues | 387 |
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
| Stars | 49,231 |
| 语言 | Go |
| Forks | 7,968 |
| Issues | 558 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,652 |
| 语言 | Python |
| Forks | 11,262 |
| Issues | 311 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,390 |
| 语言 | Python |
| Forks | 16,794 |
| Issues | 19 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,311 |
| 语言 | JavaScript |
| Forks | 11,973 |
| Issues | 540 |
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
| Stars | 50,411 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 266 |
| 许可证 | MIT License |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,978 |
| 语言 | Go |
| Forks | 8,869 |
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
| Stars | 45,693 |
| 语言 | Go |
| Forks | 3,778 |
| Issues | 82 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
