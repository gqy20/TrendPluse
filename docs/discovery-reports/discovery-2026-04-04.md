# 项目发现报告 (2026-04-04)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 10 |
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
| Stars | 130,028 |
| 语言 | Python |
| Forks | 18,407 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13 万星标证明了其极高的社区认可度，非常适合需要自托管 AI 界面的企业和个人用户。

**技术亮点**:
- 支持多种 LLM 后端集成：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互界面
- 内置 RAG（检索增强生成）能力：支持文档导入和知识库检索，增强模型回答的准确性
- 支持 MCP（Model Context Protocol）协议：可扩展性强，便于与外部工具和服务集成
- 完全自托管部署：数据完全私有化，支持 Docker 一键部署，保障数据安全
- Web UI 现代化界面：提供直观的聊天界面、模型管理、提示词模板等功能

**适用场景**:
- 企业内部 AI 助手：企业可完全自托管部署，数据不出本地，适合处理敏感业务数据和内部知识库问答
- 本地 LLM 开发测试：开发者可在本地运行开源大模型（如 Llama、Qwen 等）配合 Web 界面进行快速原型开发
- 个人隐私 AI 助手：注重隐私保护的用户可以在本地部署自己的 AI 界面，所有对话数据完全私有



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,115 |
| 语言 | Python |
| Forks | 8,671 |
| Issues | 3,201 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的国产开源 RAG 引擎之一，77K+ Stars 验证了其技术实力和社区认可度。它创新性地将 RAG 与 Agent 能力融合，配合深度文档理解和 GraphRAG 支持，为企业构建智能知识库和复杂问答系统提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地融合检索增强生成与 AI Agent 能力，支持复杂多跳推理和工具调用，实现从简单问答到复杂任务的跨越
- 深度文档理解：支持 PDF、Word、Excel 等多格式文档的智能解析与向量化，自动提取结构化信息，显著提升检索质量
- GraphRAG 图谱增强检索：基于知识图谱的上下文关联检索能力，能够捕捉实体关系和语义链路，提升答案的完整性和准确性
- 多模态 LLM 支持：兼容 OpenAI、Claude、DeepSeek、Ollama 等主流大模型，支持本地部署，满足不同企业的合规和数据安全需求
- MCP 协议集成：支持 Model Context Protocol 标准，便于与外部工具和数据源集成，扩展性强

**适用场景**:
- 企业级智能知识库：构建内部文档问答系统，支持员工快速检索政策、流程、技术文档等知识，提升工作效率
- 智能客服与支持系统：基于私有知识库打造精准的客服机器人，能够处理复杂的产品咨询和技术支持问题
- 深度研究分析助手：支持多文档综合分析、跨知识源关联推理，适用于市场调研、竞品分析、学术研究等专业场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,038 |
| 语言 | TypeScript |
| Forks | 6,816 |
| Issues | 251 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据抓取工具，提供了开箱即用的 API，能够将网页内容转换为 LLM 友好的 Markdown 格式，解决了 AI 代理获取干净、结构化网页数据的核心痛点。

**技术亮点**:
- 提供简洁的 API 接口，支持批量抓取和单个 URL 抓取，降低集成门槛
- 内置 HTML 到 Markdown 的智能转换，确保输出数据对 LLM 友好
- 支持大规模网页爬取，具备去重、增量更新等企业级特性
- 提供多种数据格式输出（Markdown、HTML、JSON），满足不同场景需求
- 支持动态渲染页面的抓取，可处理 JavaScript 渲染的现代 Web 应用

**适用场景**:
- AI 代理（Agent）开发：作为 AI Agent 的数据采集层，为 Agent 提供可靠的网页信息来源
- LLM 应用数据预处理：将网页内容转换为 Markdown 后供大语言模型使用，适用于 RAG 系统或知识库构建
- AI 搜索引擎构建：为 AI 搜索产品提供实时的网页数据抓取和索引支持



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,511 |
| 语言 | JavaScript |
| Forks | 20,424 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流 AI 编码助手（Claude Code、Cursor 等）的性能优化框架，拥有超过 13 万 Stars 的高人气，通过 Skills/Instincts/Memory 等模块显著提升 AI Agent 的开发效率和稳定性，是 AI 辅助编程领域不可错过的标杆项目。

**技术亮点**:
- 模块化架构设计：Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等独立模块，支持灵活组合和扩展
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的优化框架
- 研究优先开发模式：采用 research-first 开发理念，确保功能经过科学验证而非盲目迭代
- MCP（Model Context Protocol）深度集成：提供标准化的上下文管理协议，增强 AI 理解能力
- 企业级安全特性：内置安全模块，在提升生产力的同时保障代码和数据安全

**适用场景**:
- 个人开发者提升编码效率：为个人开发者提供 AI 辅助编程的优化配置，最大化 AI 工具的效能
- 企业团队 AI 编码标准化：帮助企业团队建立统一的 AI 编程规范和安全策略，提升整体开发效率
- AI Agent 研究与实验：作为研究平台，用于实验不同 AI Agent 策略和性能优化方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,876 |
| 语言 | Go |
| Forks | 3,856 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，非常适合隐私敏感场景和企业私有化部署，44k+ Stars 证明了其极高的社区认可度。

**技术亮点**:
- 支持多模态 AI 模型：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、TTS/语音识别、目标检测等
- 基于 Go 语言开发，性能优异且跨平台兼容性强，支持在各类硬件上本地运行
- 去中心化架构设计，支持 libp2p 分布式部署，适合边缘计算和分布式场景
- 提供 OpenAI 兼容的 API 接口，降低迁移成本，便于与现有应用集成
- 支持 MCP（Model Context Protocol）和 Agents，可构建复杂的 AI 工作流和自动化代理

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要在本地处理敏感数据，满足合规要求
- 企业私有化 AI 部署：无需依赖云服务，降低成本并完全掌控数据和模型
- 开发者本地 AI 开发与测试：提供便捷的本地推理环境，支持快速原型验证和迭代



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,729 |
| 语言 | TypeScript |
| Forks | 14,853 |
| Issues | 619 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多 Agent 团队协作、MCP 协议和多种大模型集成，拥有 7.4 万+ Stars 的活跃社区，适合企业和开发者快速搭建企业级 AI 应用。

**技术亮点**:
- 多 Agent 协作框架：支持构建和管理多个 AI Agent 团队，实现 Agent 间的协作与分工
- 多模型集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型
- MCP 协议支持：内置 Model Context Protocol，实现标准化的 Agent 与外部工具/数据源连接
- TypeScript/Next.js 技术栈：现代化全栈架构，提供良好的开发体验和类型安全
- 知识库集成：内置 RAG 知识库功能，支持文档检索和上下文增强

**适用场景**:
- 企业 AI 助手平台：构建支持多业务场景的智能助手，支持团队协作和知识管理
- AI 工作流自动化：通过多 Agent 协作编排复杂的业务流程和任务
- 开发者 AI 工具：作为基础框架快速开发自定义 AI 应用和 Agent



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,516 |
| 语言 | Python |
| Forks | 8,460 |
| Issues | 945 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架，通过统一平台支持 100+ 大语言模型和多模态模型的高效微调，融合 LoRA、QLoRA、RLHF 等先进技术，让个人开发者和企业都能以最低计算成本完成模型定制化训练。

**技术亮点**:
- 统一微调框架：支持 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流开源 LLMs 和 VLMs，一个框架满足多样化需求
- 多技术融合：集成 LoRA、QLoRA、PEFT 等参数高效微调技术，以及 RLHF 实现模型对齐优化
- 多模态支持：不仅支持纯语言模型，还支持视觉语言模型（VLMs）的微调，覆盖更广泛的应用场景
- 量化与 MoE 支持：内置量化技术降低显存占用，支持混合专家（MoE）架构模型
- ACL 2024 顶会认证：该项目被国际顶级学术会议 ACL 2024 接收，技术实力得到学术界认可

**适用场景**:
- 个人开发者与 AI 爱好者：拥有 6GB 以上显存的消费级 GPU，即可对开源大模型进行定制化微调，打造个人专属 AI 助手或垂直领域应用
- 企业与行业应用：利用其高效微调能力和多模型支持，快速构建面向特定行业的 AI 解决方案，如客服机器人、文档分析工具等
- 学术研究与模型探索：为 NLP 研究人员提供便捷的实验平台，方便开展指令微调、对齐技术、模型压缩等方向的深入研究



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,190 |
| 语言 | TypeScript |
| Forks | 7,760 |
| Issues | 45 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,153 |
| 语言 | TypeScript |
| Forks | 3,426 |
| Issues | 248 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,756 |
| 语言 | Python |
| Forks | 9,866 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,728 |
| 语言 | Java |
| Forks | 15,876 |
| Issues | 35 |
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
| Stars | 38,906 |
| 语言 | Python |
| Forks | 6,176 |
| Issues | 99 |
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
| Stars | 33,611 |
| 语言 | Python |
| Forks | 3,861 |
| Issues | 79 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,478 |
| 语言 | Python |
| Forks | 15,243 |
| Issues | 11 |
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
| Stars | 57,632 |
| 语言 | JavaScript |
| Forks | 6,226 |
| Issues | 301 |
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
| Stars | 70,565 |
| 语言 | Python |
| Forks | 8,844 |
| Issues | 370 |
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
| Stars | 48,146 |
| 语言 | TypeScript |
| Forks | 3,751 |
| Issues | 409 |
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
| Stars | 86,010 |
| 语言 | Python |
| Forks | 9,947 |
| Issues | 228 |
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
| Stars | 51,531 |
| 语言 | TypeScript |
| Forks | 24,052 |
| Issues | 820 |
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
| Stars | 182,440 |
| 语言 | TypeScript |
| Forks | 56,475 |
| Issues | 1,477 |
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
| Stars | 154,656 |
| 语言 | Java |
| Forks | 46,136 |
| Issues | 69 |
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
| Stars | 146,572 |
| 语言 | Python |
| Forks | 8,696 |
| Issues | 955 |
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
| Stars | 72,799 |
| 语言 | MDX |
| Forks | 7,804 |
| Issues | 255 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,867 |
| 语言 | Python |
| Forks | 2,112 |
| Issues | 94 |
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
| Stars | 33,618 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 283 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,148 |
| 语言 | Jupyter Notebook |
| Forks | 5,480 |
| Issues | 125 |
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
| Stars | 38,840 |
| 语言 | Rust |
| Forks | 2,407 |
| Issues | 433 |
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
| Stars | 55,910 |
| 语言 | Jupyter Notebook |
| Forks | 19,324 |
| Issues | 21 |
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
| Stars | 130,028 |
| 语言 | Python |
| Forks | 18,407 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13 万星标证明了其极高的社区认可度，非常适合需要自托管 AI 界面的企业和个人用户。

**技术亮点**:
- 支持多种 LLM 后端集成：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互界面
- 内置 RAG（检索增强生成）能力：支持文档导入和知识库检索，增强模型回答的准确性
- 支持 MCP（Model Context Protocol）协议：可扩展性强，便于与外部工具和服务集成
- 完全自托管部署：数据完全私有化，支持 Docker 一键部署，保障数据安全
- Web UI 现代化界面：提供直观的聊天界面、模型管理、提示词模板等功能

**适用场景**:
- 企业内部 AI 助手：企业可完全自托管部署，数据不出本地，适合处理敏感业务数据和内部知识库问答
- 本地 LLM 开发测试：开发者可在本地运行开源大模型（如 Llama、Qwen 等）配合 Web 界面进行快速原型开发
- 个人隐私 AI 助手：注重隐私保护的用户可以在本地部署自己的 AI 界面，所有对话数据完全私有



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,115 |
| 语言 | Python |
| Forks | 8,671 |
| Issues | 3,201 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的国产开源 RAG 引擎之一，77K+ Stars 验证了其技术实力和社区认可度。它创新性地将 RAG 与 Agent 能力融合，配合深度文档理解和 GraphRAG 支持，为企业构建智能知识库和复杂问答系统提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地融合检索增强生成与 AI Agent 能力，支持复杂多跳推理和工具调用，实现从简单问答到复杂任务的跨越
- 深度文档理解：支持 PDF、Word、Excel 等多格式文档的智能解析与向量化，自动提取结构化信息，显著提升检索质量
- GraphRAG 图谱增强检索：基于知识图谱的上下文关联检索能力，能够捕捉实体关系和语义链路，提升答案的完整性和准确性
- 多模态 LLM 支持：兼容 OpenAI、Claude、DeepSeek、Ollama 等主流大模型，支持本地部署，满足不同企业的合规和数据安全需求
- MCP 协议集成：支持 Model Context Protocol 标准，便于与外部工具和数据源集成，扩展性强

**适用场景**:
- 企业级智能知识库：构建内部文档问答系统，支持员工快速检索政策、流程、技术文档等知识，提升工作效率
- 智能客服与支持系统：基于私有知识库打造精准的客服机器人，能够处理复杂的产品咨询和技术支持问题
- 深度研究分析助手：支持多文档综合分析、跨知识源关联推理，适用于市场调研、竞品分析、学术研究等专业场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,729 |
| 语言 | TypeScript |
| Forks | 14,853 |
| Issues | 619 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多 Agent 团队协作、MCP 协议和多种大模型集成，拥有 7.4 万+ Stars 的活跃社区，适合企业和开发者快速搭建企业级 AI 应用。

**技术亮点**:
- 多 Agent 协作框架：支持构建和管理多个 AI Agent 团队，实现 Agent 间的协作与分工
- 多模型集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型
- MCP 协议支持：内置 Model Context Protocol，实现标准化的 Agent 与外部工具/数据源连接
- TypeScript/Next.js 技术栈：现代化全栈架构，提供良好的开发体验和类型安全
- 知识库集成：内置 RAG 知识库功能，支持文档检索和上下文增强

**适用场景**:
- 企业 AI 助手平台：构建支持多业务场景的智能助手，支持团队协作和知识管理
- AI 工作流自动化：通过多 Agent 协作编排复杂的业务流程和任务
- 开发者 AI 工具：作为基础框架快速开发自定义 AI 应用和 Agent



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,153 |
| 语言 | TypeScript |
| Forks | 3,426 |
| Issues | 248 |
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
| Stars | 45,728 |
| 语言 | Java |
| Forks | 15,876 |
| Issues | 35 |
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
| Stars | 38,906 |
| 语言 | Python |
| Forks | 6,176 |
| Issues | 99 |
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
| Stars | 33,611 |
| 语言 | Python |
| Forks | 3,861 |
| Issues | 79 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,478 |
| 语言 | Python |
| Forks | 15,243 |
| Issues | 11 |
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
| Stars | 100,231 |
| 语言 | TypeScript |
| Forks | 11,965 |
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
| Stars | 57,632 |
| 语言 | JavaScript |
| Forks | 6,226 |
| Issues | 301 |
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
| Stars | 74,881 |
| 语言 | Python |
| Forks | 10,177 |
| Issues | 257 |
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
| Stars | 51,531 |
| 语言 | TypeScript |
| Forks | 24,052 |
| Issues | 820 |
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
| Stars | 43,600 |
| 语言 | Go |
| Forks | 3,935 |
| Issues | 1,103 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,799 |
| 语言 | MDX |
| Forks | 7,804 |
| Issues | 255 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,867 |
| 语言 | Python |
| Forks | 2,112 |
| Issues | 94 |
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
| Stars | 33,618 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 283 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,148 |
| 语言 | Jupyter Notebook |
| Forks | 5,480 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 130,028 |
| 语言 | Python |
| Forks | 18,407 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 13 万星标证明了其极高的社区认可度，非常适合需要自托管 AI 界面的企业和个人用户。

**技术亮点**:
- 支持多种 LLM 后端集成：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互界面
- 内置 RAG（检索增强生成）能力：支持文档导入和知识库检索，增强模型回答的准确性
- 支持 MCP（Model Context Protocol）协议：可扩展性强，便于与外部工具和服务集成
- 完全自托管部署：数据完全私有化，支持 Docker 一键部署，保障数据安全
- Web UI 现代化界面：提供直观的聊天界面、模型管理、提示词模板等功能

**适用场景**:
- 企业内部 AI 助手：企业可完全自托管部署，数据不出本地，适合处理敏感业务数据和内部知识库问答
- 本地 LLM 开发测试：开发者可在本地运行开源大模型（如 Llama、Qwen 等）配合 Web 界面进行快速原型开发
- 个人隐私 AI 助手：注重隐私保护的用户可以在本地部署自己的 AI 界面，所有对话数据完全私有



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,115 |
| 语言 | Python |
| Forks | 8,671 |
| Issues | 3,201 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的国产开源 RAG 引擎之一，77K+ Stars 验证了其技术实力和社区认可度。它创新性地将 RAG 与 Agent 能力融合，配合深度文档理解和 GraphRAG 支持，为企业构建智能知识库和复杂问答系统提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地融合检索增强生成与 AI Agent 能力，支持复杂多跳推理和工具调用，实现从简单问答到复杂任务的跨越
- 深度文档理解：支持 PDF、Word、Excel 等多格式文档的智能解析与向量化，自动提取结构化信息，显著提升检索质量
- GraphRAG 图谱增强检索：基于知识图谱的上下文关联检索能力，能够捕捉实体关系和语义链路，提升答案的完整性和准确性
- 多模态 LLM 支持：兼容 OpenAI、Claude、DeepSeek、Ollama 等主流大模型，支持本地部署，满足不同企业的合规和数据安全需求
- MCP 协议集成：支持 Model Context Protocol 标准，便于与外部工具和数据源集成，扩展性强

**适用场景**:
- 企业级智能知识库：构建内部文档问答系统，支持员工快速检索政策、流程、技术文档等知识，提升工作效率
- 智能客服与支持系统：基于私有知识库打造精准的客服机器人，能够处理复杂的产品咨询和技术支持问题
- 深度研究分析助手：支持多文档综合分析、跨知识源关联推理，适用于市场调研、竞品分析、学术研究等专业场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,511 |
| 语言 | JavaScript |
| Forks | 20,424 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流 AI 编码助手（Claude Code、Cursor 等）的性能优化框架，拥有超过 13 万 Stars 的高人气，通过 Skills/Instincts/Memory 等模块显著提升 AI Agent 的开发效率和稳定性，是 AI 辅助编程领域不可错过的标杆项目。

**技术亮点**:
- 模块化架构设计：Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等独立模块，支持灵活组合和扩展
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的优化框架
- 研究优先开发模式：采用 research-first 开发理念，确保功能经过科学验证而非盲目迭代
- MCP（Model Context Protocol）深度集成：提供标准化的上下文管理协议，增强 AI 理解能力
- 企业级安全特性：内置安全模块，在提升生产力的同时保障代码和数据安全

**适用场景**:
- 个人开发者提升编码效率：为个人开发者提供 AI 辅助编程的优化配置，最大化 AI 工具的效能
- 企业团队 AI 编码标准化：帮助企业团队建立统一的 AI 编程规范和安全策略，提升整体开发效率
- AI Agent 研究与实验：作为研究平台，用于实验不同 AI Agent 策略和性能优化方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,729 |
| 语言 | TypeScript |
| Forks | 14,853 |
| Issues | 619 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多 Agent 团队协作、MCP 协议和多种大模型集成，拥有 7.4 万+ Stars 的活跃社区，适合企业和开发者快速搭建企业级 AI 应用。

**技术亮点**:
- 多 Agent 协作框架：支持构建和管理多个 AI Agent 团队，实现 Agent 间的协作与分工
- 多模型集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型
- MCP 协议支持：内置 Model Context Protocol，实现标准化的 Agent 与外部工具/数据源连接
- TypeScript/Next.js 技术栈：现代化全栈架构，提供良好的开发体验和类型安全
- 知识库集成：内置 RAG 知识库功能，支持文档检索和上下文增强

**适用场景**:
- 企业 AI 助手平台：构建支持多业务场景的智能助手，支持团队协作和知识管理
- AI 工作流自动化：通过多 Agent 协作编排复杂的业务流程和任务
- 开发者 AI 工具：作为基础框架快速开发自定义 AI 应用和 Agent



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,433 |
| 语言 | HTML |
| Forks | 20,619 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

拥有超过15.7万Stars的知名AI提示词社区平台，采用CC0公共领域许可可自由商用，基于Next.js + TypeScript现代化技术栈构建，支持ChatGPT、Claude、Gemini等多款主流LLM，并提供完整的企业自托管方案，是目前最值得推荐的提示词资源库之一。

**技术亮点**:
- 现代化全栈架构：基于 Next.js 14 + TypeScript 构建，采用 App Router 和服务端组件，支持 Edge Runtime，拥有优秀的 SEO 和首屏加载性能
- 多模型支持：兼容 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，可灵活切换和对比不同模型的提示词效果
- 隐私优先的企业部署：提供完整的自托管方案，企业可在自有基础设施上部署，完全掌控数据，满足金融、医疗等高合规要求场景
- 社区驱动的提示词生态：超过5000+精心策划的提示词库，支持分类检索、收藏和自定义导入，持续由社区贡献更新
- TypeScript类型安全：全项目严格类型定义，提供完整的类型提示和类型检查，提升开发体验和代码可靠性

**适用场景**:
- 企业AI助手集成：企业可自托管部署，定制化企业专属提示词库，赋能客服、文档生成等业务流程，同时确保数据不出境
- 个人效率提升：用户可浏览、收藏和复用社区优秀提示词，快速提升在写作、编程、分析等场景的AI交互效率
- Prompt Engineering研究：开发者可研究学习优质提示词的设计模式，结合开源代码理解LLM应用开发最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,957 |
| 语言 | Jupyter Notebook |
| Forks | 13,757 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 博士（知名 AI 教育家）亲自编写的 LLM 实战教程，通过 4 个阶段、300+ 页 Jupyter Notebook 逐步实现完整 GPT 模型，是目前最系统、最深入的 LLM 从零理解教程，特别适合想深入理解大模型内部机制而非仅调 API 的开发者。

**技术亮点**:
- 完整实现 GPT-2 架构：包含 Multi-Head Attention、Feed-Forward、Positional Encoding 等核心组件的逐行代码实现
- 涵盖 LLM 训练全流程：从数据预处理（Tiktoken）、Tokenization 到模型微调、RLHF 完整流程
- 深入讲解 Transformer 关键技术：Byte Pair Encoding、Dropout、Layer Normalization、Residual Connections
- 基于 PyTorch 原生实现：零依赖外部深度学习框架的预训练模型，所有层均为手工搭建
- 包含优化技巧：混合精度训练、梯度累积、Flash Attention 等现代 LLM 训练技术

**适用场景**:
- 个人学习：系统理解 LLM 工作原理，为研究或在生产环境中微调/部署模型奠定基础
- 企业培训：作为 AI 教育培训教材，帮助工程团队从源码层面掌握大模型技术
- AI 教育：教育机构用于深度学习、自然语言处理课程的项目实践
- 技术面试准备：理解 LLM 面试常见问题的最佳源码级参考资料



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,190 |
| 语言 | TypeScript |
| Forks | 7,760 |
| Issues | 45 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,153 |
| 语言 | TypeScript |
| Forks | 3,426 |
| Issues | 248 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,756 |
| 语言 | Python |
| Forks | 9,866 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,440 |
| 语言 | Python |
| Forks | 2,866 |
| Issues | 165 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,632 |
| 语言 | JavaScript |
| Forks | 6,226 |
| Issues | 301 |
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
| Stars | 70,565 |
| 语言 | Python |
| Forks | 8,844 |
| Issues | 370 |
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
| Stars | 48,146 |
| 语言 | TypeScript |
| Forks | 3,751 |
| Issues | 409 |
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
| Stars | 51,531 |
| 语言 | TypeScript |
| Forks | 24,052 |
| Issues | 820 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,208 |
| 语言 | Unknown |
| Forks | 6,144 |
| Issues | 19 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,246 |
| 语言 | Python |
| Forks | 15,161 |
| Issues | 4,095 |
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
| Stars | 58,290 |
| 语言 | Python |
| Forks | 5,753 |
| Issues | 72 |
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
| Stars | 39,266 |
| 语言 | TypeScript |
| Forks | 4,005 |
| Issues | 1,093 |
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
| Stars | 146,572 |
| 语言 | Python |
| Forks | 8,696 |
| Issues | 955 |
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
| Stars | 167,149 |
| 语言 | Go |
| Forks | 15,316 |
| Issues | 2,857 |
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
| Stars | 72,799 |
| 语言 | MDX |
| Forks | 7,804 |
| Issues | 255 |
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
| Stars | 47,554 |
| 语言 | Rust |
| Forks | 9,452 |
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
| Stars | 33,867 |
| 语言 | Python |
| Forks | 2,112 |
| Issues | 94 |
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
| Stars | 93,279 |
| 语言 | Python |
| Forks | 5,624 |
| Issues | 500 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 37,088 |
| 语言 | Python |
| Forks | 2,584 |
| Issues | 65 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


## 🧠 机器学习框架 (11 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,516 |
| 语言 | Python |
| Forks | 8,460 |
| Issues | 945 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的开源 LLM 微调框架，通过统一平台支持 100+ 大语言模型和多模态模型的高效微调，融合 LoRA、QLoRA、RLHF 等先进技术，让个人开发者和企业都能以最低计算成本完成模型定制化训练。

**技术亮点**:
- 统一微调框架：支持 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流开源 LLMs 和 VLMs，一个框架满足多样化需求
- 多技术融合：集成 LoRA、QLoRA、PEFT 等参数高效微调技术，以及 RLHF 实现模型对齐优化
- 多模态支持：不仅支持纯语言模型，还支持视觉语言模型（VLMs）的微调，覆盖更广泛的应用场景
- 量化与 MoE 支持：内置量化技术降低显存占用，支持混合专家（MoE）架构模型
- ACL 2024 顶会认证：该项目被国际顶级学术会议 ACL 2024 接收，技术实力得到学术界认可

**适用场景**:
- 个人开发者与 AI 爱好者：拥有 6GB 以上显存的消费级 GPU，即可对开源大模型进行定制化微调，打造个人专属 AI 助手或垂直领域应用
- 企业与行业应用：利用其高效微调能力和多模型支持，快速构建面向特定行业的 AI 解决方案，如客服机器人、文档分析工具等
- 学术研究与模型探索：为 NLP 研究人员提供便捷的实验平台，方便开展指令微调、对齐技术、模型压缩等方向的深入研究



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,325 |
| 语言 | Python |
| Forks | 6,467 |
| Issues | 72 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过65K Stars并获得广泛社区认可，为分析师、量化交易员和AI开发者提供统一的数据接口和分析工具，降低了金融数据分析的技术门槛。

**技术亮点**:
- 模块化架构设计，支持股票、加密货币、期权、固收等多品类金融数据的统一访问
- 深度集成AI/机器学习能力，支持智能投研分析和预测模型构建
- 提供标准化的Python API，简化量化策略开发和回测流程
- 开源可扩展，支持自定义数据源和分析模块集成
- 支持数据导出和可视化，便于生成专业投研报告

**适用场景**:
- 量化投资研究：用于量化分析师构建和回测交易策略，获取市场数据
- AI驱动投研：集成AI代理能力，辅助投资决策和风险分析
- 个人理财分析：为个人投资者提供股票、加密货币等资产的综合分析工具



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,433 |
| 语言 | HTML |
| Forks | 20,619 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

拥有超过15.7万Stars的知名AI提示词社区平台，采用CC0公共领域许可可自由商用，基于Next.js + TypeScript现代化技术栈构建，支持ChatGPT、Claude、Gemini等多款主流LLM，并提供完整的企业自托管方案，是目前最值得推荐的提示词资源库之一。

**技术亮点**:
- 现代化全栈架构：基于 Next.js 14 + TypeScript 构建，采用 App Router 和服务端组件，支持 Edge Runtime，拥有优秀的 SEO 和首屏加载性能
- 多模型支持：兼容 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，可灵活切换和对比不同模型的提示词效果
- 隐私优先的企业部署：提供完整的自托管方案，企业可在自有基础设施上部署，完全掌控数据，满足金融、医疗等高合规要求场景
- 社区驱动的提示词生态：超过5000+精心策划的提示词库，支持分类检索、收藏和自定义导入，持续由社区贡献更新
- TypeScript类型安全：全项目严格类型定义，提供完整的类型提示和类型检查，提升开发体验和代码可靠性

**适用场景**:
- 企业AI助手集成：企业可自托管部署，定制化企业专属提示词库，赋能客服、文档生成等业务流程，同时确保数据不出境
- 个人效率提升：用户可浏览、收藏和复用社区优秀提示词，快速提升在写作、编程、分析等场景的AI交互效率
- Prompt Engineering研究：开发者可研究学习优质提示词的设计模式，结合开源代码理解LLM应用开发最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,957 |
| 语言 | Jupyter Notebook |
| Forks | 13,757 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 博士（知名 AI 教育家）亲自编写的 LLM 实战教程，通过 4 个阶段、300+ 页 Jupyter Notebook 逐步实现完整 GPT 模型，是目前最系统、最深入的 LLM 从零理解教程，特别适合想深入理解大模型内部机制而非仅调 API 的开发者。

**技术亮点**:
- 完整实现 GPT-2 架构：包含 Multi-Head Attention、Feed-Forward、Positional Encoding 等核心组件的逐行代码实现
- 涵盖 LLM 训练全流程：从数据预处理（Tiktoken）、Tokenization 到模型微调、RLHF 完整流程
- 深入讲解 Transformer 关键技术：Byte Pair Encoding、Dropout、Layer Normalization、Residual Connections
- 基于 PyTorch 原生实现：零依赖外部深度学习框架的预训练模型，所有层均为手工搭建
- 包含优化技巧：混合精度训练、梯度累积、Flash Attention 等现代 LLM 训练技术

**适用场景**:
- 个人学习：系统理解 LLM 工作原理，为研究或在生产环境中微调/部署模型奠定基础
- 企业培训：作为 AI 教育培训教材，帮助工程团队从源码层面掌握大模型技术
- AI 教育：教育机构用于深度学习、自然语言处理课程的项目实践
- 技术面试准备：理解 LLM 面试常见问题的最佳源码级参考资料



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,803 |
| 语言 | Python |
| Forks | 32,730 |
| Issues | 2,355 |
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
| Stars | 75,246 |
| 语言 | Python |
| Forks | 15,161 |
| Issues | 4,095 |
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
| Stars | 107,761 |
| 语言 | Python |
| Forks | 12,457 |
| Issues | 3,923 |
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
| Stars | 98,799 |
| 语言 | Python |
| Forks | 27,399 |
| Issues | 18,242 |
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
| Stars | 72,799 |
| 语言 | MDX |
| Forks | 7,804 |
| Issues | 255 |
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
| Stars | 33,618 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 283 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,148 |
| 语言 | Jupyter Notebook |
| Forks | 5,480 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 137,511 |
| 语言 | JavaScript |
| Forks | 20,424 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流 AI 编码助手（Claude Code、Cursor 等）的性能优化框架，拥有超过 13 万 Stars 的高人气，通过 Skills/Instincts/Memory 等模块显著提升 AI Agent 的开发效率和稳定性，是 AI 辅助编程领域不可错过的标杆项目。

**技术亮点**:
- 模块化架构设计：Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等独立模块，支持灵活组合和扩展
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的优化框架
- 研究优先开发模式：采用 research-first 开发理念，确保功能经过科学验证而非盲目迭代
- MCP（Model Context Protocol）深度集成：提供标准化的上下文管理协议，增强 AI 理解能力
- 企业级安全特性：内置安全模块，在提升生产力的同时保障代码和数据安全

**适用场景**:
- 个人开发者提升编码效率：为个人开发者提供 AI 辅助编程的优化配置，最大化 AI 工具的效能
- 企业团队 AI 编码标准化：帮助企业团队建立统一的 AI 编程规范和安全策略，提升整体开发效率
- AI Agent 研究与实验：作为研究平台，用于实验不同 AI Agent 策略和性能优化方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,876 |
| 语言 | Go |
| Forks | 3,856 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，非常适合隐私敏感场景和企业私有化部署，44k+ Stars 证明了其极高的社区认可度。

**技术亮点**:
- 支持多模态 AI 模型：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、TTS/语音识别、目标检测等
- 基于 Go 语言开发，性能优异且跨平台兼容性强，支持在各类硬件上本地运行
- 去中心化架构设计，支持 libp2p 分布式部署，适合边缘计算和分布式场景
- 提供 OpenAI 兼容的 API 接口，降低迁移成本，便于与现有应用集成
- 支持 MCP（Model Context Protocol）和 Agents，可构建复杂的 AI 工作流和自动化代理

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要在本地处理敏感数据，满足合规要求
- 企业私有化 AI 部署：无需依赖云服务，降低成本并完全掌控数据和模型
- 开发者本地 AI 开发与测试：提供便捷的本地推理环境，支持快速原型验证和迭代



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,565 |
| 语言 | Python |
| Forks | 8,844 |
| Issues | 370 |
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
| Stars | 48,146 |
| 语言 | TypeScript |
| Forks | 3,751 |
| Issues | 409 |
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
| Stars | 182,440 |
| 语言 | TypeScript |
| Forks | 56,475 |
| Issues | 1,477 |
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
| Stars | 154,792 |
| 语言 | Python |
| Forks | 12,653 |
| Issues | 2,444 |
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
| Stars | 96,832 |
| 语言 | Python |
| Forks | 8,998 |
| Issues | 165 |
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
| Stars | 79,213 |
| 语言 | Python |
| Forks | 9,237 |
| Issues | 238 |
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
| Stars | 183,425 |
| 语言 | TypeScript |
| Forks | 38,957 |
| Issues | 16,015 |
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
| Stars | 94,017 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 301 |
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
| Stars | 78,792 |
| 语言 | TypeScript |
| Forks | 5,756 |
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
| Stars | 76,957 |
| 语言 | TypeScript |
| Forks | 6,590 |
| Issues | 181 |
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
| Stars | 79,253 |
| 语言 | Go |
| Forks | 2,750 |
| Issues | 313 |
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
| Stars | 75,578 |
| 语言 | Go |
| Forks | 2,673 |
| Issues | 941 |
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
| Stars | 37,088 |
| 语言 | Python |
| Forks | 2,584 |
| Issues | 65 |
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
| Stars | 419,066 |
| 语言 | Python |
| Forks | 45,576 |
| Issues | 1,185 |
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
| Stars | 75,675 |
| 语言 | JavaScript |
| Forks | 7,277 |
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
| Stars | 48,146 |
| 语言 | TypeScript |
| Forks | 3,751 |
| Issues | 409 |
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
| Stars | 182,440 |
| 语言 | TypeScript |
| Forks | 56,475 |
| Issues | 1,477 |
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
| Stars | 51,677 |
| 语言 | Go |
| Forks | 10,338 |
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
| Stars | 121,487 |
| 语言 | Go |
| Forks | 42,793 |
| Issues | 2,702 |
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
| Stars | 71,563 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,777 |
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
| Stars | 54,734 |
| 语言 | Go |
| Forks | 6,536 |
| Issues | 2,830 |
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
| Stars | 47,591 |
| 语言 | Go |
| Forks | 5,066 |
| Issues | 977 |
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
| Stars | 94,017 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 301 |
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
| Stars | 76,201 |
| 语言 | TypeScript |
| Forks | 6,529 |
| Issues | 400 |
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
| Stars | 84,842 |
| 语言 | JavaScript |
| Forks | 7,596 |
| Issues | 717 |
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
| Stars | 69,704 |
| 语言 | Go |
| Forks | 1,901 |
| Issues | 316 |
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
| Stars | 62,464 |
| 语言 | Go |
| Forks | 5,897 |
| Issues | 773 |
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
| Stars | 58,545 |
| 语言 | Go |
| Forks | 4,246 |
| Issues | 27 |
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
| Stars | 84,842 |
| 语言 | JavaScript |
| Forks | 7,596 |
| Issues | 717 |
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
| Stars | 63,383 |
| 语言 | Go |
| Forks | 10,304 |
| Issues | 761 |
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
| Stars | 44,876 |
| 语言 | Go |
| Forks | 3,856 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，非常适合隐私敏感场景和企业私有化部署，44k+ Stars 证明了其极高的社区认可度。

**技术亮点**:
- 支持多模态 AI 模型：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、TTS/语音识别、目标检测等
- 基于 Go 语言开发，性能优异且跨平台兼容性强，支持在各类硬件上本地运行
- 去中心化架构设计，支持 libp2p 分布式部署，适合边缘计算和分布式场景
- 提供 OpenAI 兼容的 API 接口，降低迁移成本，便于与现有应用集成
- 支持 MCP（Model Context Protocol）和 Agents，可构建复杂的 AI 工作流和自动化代理

**适用场景**:
- 隐私敏感的 AI 应用场景：医疗、金融、法律等领域需要在本地处理敏感数据，满足合规要求
- 企业私有化 AI 部署：无需依赖云服务，降低成本并完全掌控数据和模型
- 开发者本地 AI 开发与测试：提供便捷的本地推理环境，支持快速原型验证和迭代



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,832 |
| 语言 | Python |
| Forks | 8,998 |
| Issues | 165 |
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
| Stars | 87,170 |
| 语言 | Python |
| Forks | 33,802 |
| Issues | 419 |
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
| Stars | 100,097 |
| 语言 | TypeScript |
| Forks | 27,146 |
| Issues | 1,130 |
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
| Stars | 78,792 |
| 语言 | TypeScript |
| Forks | 5,756 |
| Issues | 732 |
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
| Stars | 68,887 |
| 语言 | JavaScript |
| Forks | 23,036 |
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
| Forks | 10,213 |
| Issues | 362 |
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
| Stars | 51,726 |
| 语言 | JavaScript |
| Forks | 4,694 |
| Issues | 1,470 |
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
| Stars | 47,739 |
| 语言 | JavaScript |
| Forks | 1,582 |
| Issues | 666 |
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
| Stars | 88,325 |
| 语言 | Go |
| Forks | 8,569 |
| Issues | 665 |
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
| Stars | 71,275 |
| 语言 | Go |
| Forks | 4,690 |
| Issues | 260 |
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
| Stars | 57,347 |
| 语言 | Go |
| Forks | 3,249 |
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
| Stars | 37,088 |
| 语言 | Python |
| Forks | 2,584 |
| Issues | 65 |
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
| Stars | 419,066 |
| 语言 | Python |
| Forks | 45,576 |
| Issues | 1,185 |
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
| Stars | 75,675 |
| 语言 | JavaScript |
| Forks | 7,277 |
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
| Stars | 100,231 |
| 语言 | TypeScript |
| Forks | 11,965 |
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
| Stars | 57,632 |
| 语言 | JavaScript |
| Forks | 6,226 |
| Issues | 301 |
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
| Stars | 43,600 |
| 语言 | Go |
| Forks | 3,935 |
| Issues | 1,103 |
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
| Stars | 51,677 |
| 语言 | Go |
| Forks | 10,338 |
| Issues | 215 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (10 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,433 |
| 语言 | HTML |
| Forks | 20,619 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

拥有超过15.7万Stars的知名AI提示词社区平台，采用CC0公共领域许可可自由商用，基于Next.js + TypeScript现代化技术栈构建，支持ChatGPT、Claude、Gemini等多款主流LLM，并提供完整的企业自托管方案，是目前最值得推荐的提示词资源库之一。

**技术亮点**:
- 现代化全栈架构：基于 Next.js 14 + TypeScript 构建，采用 App Router 和服务端组件，支持 Edge Runtime，拥有优秀的 SEO 和首屏加载性能
- 多模型支持：兼容 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，可灵活切换和对比不同模型的提示词效果
- 隐私优先的企业部署：提供完整的自托管方案，企业可在自有基础设施上部署，完全掌控数据，满足金融、医疗等高合规要求场景
- 社区驱动的提示词生态：超过5000+精心策划的提示词库，支持分类检索、收藏和自定义导入，持续由社区贡献更新
- TypeScript类型安全：全项目严格类型定义，提供完整的类型提示和类型检查，提升开发体验和代码可靠性

**适用场景**:
- 企业AI助手集成：企业可自托管部署，定制化企业专属提示词库，赋能客服、文档生成等业务流程，同时确保数据不出境
- 个人效率提升：用户可浏览、收藏和复用社区优秀提示词，快速提升在写作、编程、分析等场景的AI交互效率
- Prompt Engineering研究：开发者可研究学习优质提示词的设计模式，结合开源代码理解LLM应用开发最佳实践



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,190 |
| 语言 | TypeScript |
| Forks | 7,760 |
| Issues | 45 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,440 |
| 语言 | Python |
| Forks | 2,866 |
| Issues | 165 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,611 |
| 语言 | Python |
| Forks | 3,861 |
| Issues | 79 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,208 |
| 语言 | Unknown |
| Forks | 6,144 |
| Issues | 19 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,799 |
| 语言 | MDX |
| Forks | 7,804 |
| Issues | 255 |
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
| Stars | 89,624 |
| 语言 | TypeScript |
| Forks | 9,972 |
| Issues | 2,223 |
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
| Stars | 87,115 |
| 语言 | TypeScript |
| Forks | 8,818 |
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
| Stars | 127,319 |
| 语言 | JavaScript |
| Forks | 12,466 |
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
| Stars | 169,072 |
| 语言 | Go |
| Forks | 13,107 |
| Issues | 171 |
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
| Stars | 134,325 |
| 语言 | Unknown |
| Forks | 33,842 |
| Issues | 143 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,370 |
| 语言 | Python |
| Forks | 6,472 |
| Issues | 54 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,347 |
| 语言 | Python |
| Forks | 12,818 |
| Issues | 113 |
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
| Stars | 85,254 |
| 语言 | Python |
| Forks | 7,332 |
| Issues | 627 |
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
| Stars | 384,996 |
| 语言 | Python |
| Forks | 66,086 |
| Issues | 77 |
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
| Stars | 114,196 |
| 语言 | TypeScript |
| Forks | 5,860 |
| Issues | 375 |
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
| Stars | 107,738 |
| 语言 | TypeScript |
| Forks | 7,822 |
| Issues | 224 |
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
| Stars | 47,725 |
| 语言 | JavaScript |
| Forks | 3,922 |
| Issues | 12 |
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
| Stars | 48,019 |
| 语言 | Go |
| Forks | 10,261 |
| Issues | 1,890 |
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
| Stars | 101,347 |
| 语言 | C++ |
| Forks | 16,348 |
| Issues | 1,373 |
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
| Stars | 63,361 |
| 语言 | Python |
| Forks | 1,629 |
| Issues | 30 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,890 |
| 语言 | TypeScript |
| Forks | 8,649 |
| Issues | 317 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 290,675 |
| 语言 | Python |
| Forks | 27,575 |
| Issues | 17 |
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
| Stars | 219,278 |
| 语言 | Python |
| Forks | 50,304 |
| Issues | 914 |
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
| Stars | 97,149 |
| 语言 | Python |
| Forks | 11,977 |
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
| Stars | 85,987 |
| 语言 | Python |
| Forks | 37,154 |
| Issues | 3,574 |
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
| Stars | 77,684 |
| 语言 | Python |
| Forks | 45,176 |
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
| Stars | 440,941 |
| 语言 | TypeScript |
| Forks | 44,048 |
| Issues | 210 |
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
| Stars | 352,196 |
| 语言 | TypeScript |
| Forks | 43,860 |
| Issues | 3 |
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
| Stars | 120,247 |
| 语言 | TypeScript |
| Forks | 13,130 |
| Issues | 2,921 |
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
| Stars | 111,488 |
| 语言 | TypeScript |
| Forks | 8,416 |
| Issues | 1,803 |
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
| Stars | 108,403 |
| 语言 | TypeScript |
| Forks | 13,323 |
| Issues | 5,010 |
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
| Stars | 97,766 |
| 语言 | TypeScript |
| Forks | 54,572 |
| Issues | 1,361 |
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
| Stars | 96,305 |
| 语言 | TypeScript |
| Forks | 5,251 |
| Issues | 666 |
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
| Stars | 94,330 |
| 语言 | TypeScript |
| Forks | 5,154 |
| Issues | 103 |
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
| Stars | 83,052 |
| 语言 | TypeScript |
| Forks | 7,577 |
| Issues | 33 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,970 |
| 语言 | TypeScript |
| Forks | 10,198 |
| Issues | 665 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,555 |
| 语言 | TypeScript |
| Forks | 7,987 |
| Issues | 712 |
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
| Stars | 244,395 |
| 语言 | JavaScript |
| Forks | 50,889 |
| Issues | 1,210 |
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
| Stars | 116,552 |
| 语言 | JavaScript |
| Forks | 35,250 |
| Issues | 2,599 |
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
| Stars | 111,757 |
| 语言 | JavaScript |
| Forks | 36,314 |
| Issues | 563 |
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
| Stars | 109,027 |
| 语言 | JavaScript |
| Forks | 11,594 |
| Issues | 353 |
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
| Stars | 98,014 |
| 语言 | JavaScript |
| Forks | 32,689 |
| Issues | 1,663 |
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
| Stars | 95,527 |
| 语言 | JavaScript |
| Forks | 15,318 |
| Issues | 54 |
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
| Stars | 86,160 |
| 语言 | JavaScript |
| Forks | 4,843 |
| Issues | 979 |
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
| Stars | 78,961 |
| 语言 | JavaScript |
| Forks | 32,108 |
| Issues | 270 |
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
| Stars | 70,931 |
| 语言 | JavaScript |
| Forks | 16,811 |
| Issues | 891 |
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
| Stars | 65,939 |
| 语言 | JavaScript |
| Forks | 9,382 |
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
| Stars | 62,514 |
| 语言 | JavaScript |
| Forks | 3,994 |
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
| Stars | 61,516 |
| 语言 | JavaScript |
| Forks | 7,126 |
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
| Stars | 60,214 |
| 语言 | JavaScript |
| Forks | 5,641 |
| Issues | 67 |
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
| Stars | 59,853 |
| 语言 | JavaScript |
| Forks | 20,461 |
| Issues | 94 |
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
| Stars | 57,423 |
| 语言 | JavaScript |
| Forks | 12,300 |
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
| Stars | 53,073 |
| 语言 | JavaScript |
| Forks | 10,605 |
| Issues | 459 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,362 |
| 语言 | JavaScript |
| Forks | 11,426 |
| Issues | 364 |
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
| Stars | 48,628 |
| 语言 | JavaScript |
| Forks | 2,427 |
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
| Stars | 133,283 |
| 语言 | Go |
| Forks | 18,893 |
| Issues | 9,929 |
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
| Stars | 105,806 |
| 语言 | Go |
| Forks | 14,972 |
| Issues | 46 |
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
| Stars | 87,416 |
| 语言 | Go |
| Forks | 8,232 |
| Issues | 264 |
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
| Stars | 81,404 |
| 语言 | Go |
| Forks | 4,979 |
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
| Stars | 68,641 |
| 语言 | Go |
| Forks | 3,214 |
| Issues | 9 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,460 |
| 语言 | Go |
| Forks | 5,007 |
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
| Stars | 50,966 |
| 语言 | Go |
| Forks | 21,878 |
| Issues | 396 |
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
| Stars | 49,251 |
| 语言 | Go |
| Forks | 7,957 |
| Issues | 559 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,981 |
| 语言 | Shell |
| Forks | 10,945 |
| Issues | 104 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,825 |
| 语言 | Python |
| Forks | 11,300 |
| Issues | 322 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 341,372 |
| 语言 | Python |
| Forks | 55,199 |
| Issues | 526 |
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
| Stars | 85,762 |
| 语言 | Python |
| Forks | 7,197 |
| Issues | 481 |
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
| Stars | 76,618 |
| 语言 | Python |
| Forks | 16,822 |
| Issues | 20 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,548 |
| 语言 | TypeScript |
| Forks | 16,490 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,300 |
| 语言 | JavaScript |
| Forks | 9,187 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,520 |
| 语言 | Go |
| Forks | 1,592 |
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
| Stars | 46,963 |
| 语言 | Go |
| Forks | 8,867 |
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
| Stars | 45,800 |
| 语言 | Go |
| Forks | 3,779 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
