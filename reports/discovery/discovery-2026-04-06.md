# 项目发现报告 (2026-04-06)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 16 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
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
| Stars | 130,326 |
| 语言 | Python |
| Forks | 18,469 |
| Issues | 303 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，130k+ Stars 证明了其极高的社区认可度。它支持 Ollama、OpenAI API 等多种后端，集成 RAG 和 MCP 能力，可完全自托管部署，是企业和个人用户构建私有化 AI 助手的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- RAG 增强能力：内置检索增强生成功能，支持知识库问答，提升模型回答准确性
- MCP 协议支持：支持 Model Context Protocol，可扩展更多 AI 工具和插件生态
- 自托管部署：支持 Docker 一键部署，数据完全私有化，适合对隐私有要求的场景
- 现代 Web 界面：提供直观的用户界面，支持对话管理、多模态交互等功能

**适用场景**:
- 企业私有化 AI 助手：企业可自托管部署，内部知识库问答、客户服务自动化等场景
- 个人开发者本地 LLM 测试：开发者可在本地运行各种开源模型（Llama、Mistral 等）进行调试和测试
- 统一 LLM 管理平台：同时接入多个 LLM 服务商，通过统一界面管理和切换，适合 AI 应用开发者



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,241 |
| 语言 | Python |
| Forks | 8,683 |
| Issues | 3,210 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，通过将 RAG 与 Agent 能力深度融合，提供了从文档解析到复杂推理的完整技术栈，特别适合需要构建高质量企业知识库和智能问答系统的团队，其 77k+ stars 和活跃社区证明了其稳定性和实用性。

**技术亮点**:
- RAG + Agent 融合架构：原生集成 Agent 能力，支持复杂多步骤推理和任务规划，相比纯 RAG 具有更强的推理能力
- 文档智能理解引擎：支持 PDF、Word、Excel 等多格式文档的深度解析，包含 OCR 识别、表格结构化、布局分析等能力
- 多索引策略支持：提供向量检索、稀疏检索、图检索（GraphRAG）等多种混合检索方式，可根据场景灵活配置
- MCP 协议支持：集成了 Model Context Protocol，可扩展调用外部工具和数据源，增强 Agent 能力边界
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等云端和本地模型部署，提供统一的调用接口

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持复杂文档理解与精准问答，适用于客服、培训、法务等场景
- Deep Research 深度研究助手：利用 Agent 编排和多步推理能力，实现复杂问题的多源信息检索与综合分析
- 智能文档处理与分析平台：批量处理合同、报告、表格等商业文档，自动提取结构化信息，支持决策分析



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,978 |
| 语言 | TypeScript |
| Forks | 6,854 |
| Issues | 256 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一款专为 AI 应用打造的网页数据抓取平台，能将复杂网页内容高效转换为干净的 Markdown 格式，为 LLM 和 AI 代理提供高质量数据源，拥有近 10.5 万星标，是 AI 数据处理领域的明星开源项目。

**技术亮点**:
- HTML转Markdown专业引擎：深度解析网页结构，将HTML精准转换为干净的Markdown格式，保留关键内容同时去除噪音
- 智能全站爬取能力：支持整站深度爬取，自动发现和抓取相关页面，提供完整的网站数据采集解决方案
- TypeScript原生开发：完整的类型定义和类型安全，提供更可靠的SDK和更好的开发体验
- LLM优化输出：专为大型语言模型设计的输出格式，数据结构清晰、易于理解和处理
- 完整的API接口体系：提供简洁易用的REST API，支持批量操作和自定义配置，便于集成到各类AI应用中

**适用场景**:
- 为RAG（检索增强生成）系统抓取和预处理网页数据，为LLM提供高质量的上下文知识库
- 构建AI代理的网页搜索和数据获取能力，让AI Agent能够实时访问和理解网络内容
- 批量数据采集场景：从企业官网、竞品站点等提取结构化数据用于市场分析、内容聚合或知识库建设



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 142,454 |
| 语言 | JavaScript |
| Forks | 21,655 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于AI代码助手性能优化的开源系统，拥有超过14万stars的高人气，提供了Skills、Instincts、Memory、Security和Research-first五大核心模块，为Claude Code、Codex、Cursor等多个主流AI编程工具提供统一的性能增强框架。

**技术亮点**:
- 多Agent框架支持：兼容Claude Code、Codex、Opencode、Cursor等多个AI编程助手，提供统一的任务执行和优化接口
- 模块化性能优化系统：包含Skills、Instincts、Memory、Security等独立模块，可灵活组合以满足不同场景需求
- 安全机制设计：内置Security模块，提供安全的代码执行和访问控制，保障AI操作的安全性
- 记忆系统实现：通过Memory模块实现上下文持久化和状态管理，提升AI代理的长期任务处理能力
- 研究驱动开发：采用Research-first开发理念，持续优化和迭代，确保技术先进性

**适用场景**:
- 企业级AI开发团队：需要统一管理多个AI编程工具、提升团队开发效率和安全性的企业环境
- 个人开发者效率提升：希望优化个人工作流，获得更智能、更安全的AI辅助编程体验
- AI研究实验：研究人员用于测试和对比不同AI代码助手的性能表现
- DevOps自动化集成：将AI代码助手集成到CI/CD流程中，实现自动化代码审查和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,964 |
| 语言 | Go |
| Forks | 3,863 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源 AI 推理引擎，支持在本地运行 LLM、图像、音频、视频等多种模型，无需 GPU 即可部署，极大降低了 AI 应用的技术门槛和数据隐私风险，尤其适合需要私有化部署 AI 能力的开发者。

**技术亮点**:
- 多模型支持：兼容 Llama、Mamba、Stable Diffusion、MusicGen、GPT-4 等主流开源模型，覆盖文本生成、图像生成、语音合成、目标检测等多种任务
- 无 GPU 限制：支持 CPU 推理，可在普通硬件上运行，降低了 AI 部署的硬件成本和入门门槛
- OpenAI 兼容 API：提供与 OpenAI API 格式兼容的接口，现有基于 OpenAI 的应用可零成本迁移，大幅减少开发工作量
- Go 语言开发：采用 Go 语言实现，具备高并发、低内存占用的优势，适合生产环境部署
- 去中心化架构：支持 libp2p 分布式部署，可构建分布式 AI 推理网络，提供更高的可扩展性和容错能力

**适用场景**:
- 隐私敏感场景：在医疗、法律、金融等需要数据隐私保护的领域，LocalAI 允许模型推理完全在本地完成，数据不出本地，满足合规要求
- 私有化 AI 部署：企业可基于 LocalAI 构建内部的 AI 助手、客服机器人或文档处理系统，无需依赖第三方云服务
- 资源受限环境：面向没有 GPU 的开发者或个人用户，提供在普通电脑或服务器上运行 AI 模型的轻量化解决方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,811 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 639 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 开发平台，提供了完整的多智能体协作框架、内置知识库和 MCP 协议支持，Stars 数超过 7.4 万且持续活跃，是快速构建和部署企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 之间的协作与分工，可构建复杂的 Agent Team 工作流
- MCP (Model Context Protocol) 原生支持：标准化接入外部工具和数据源，便于扩展 Agent 能力
- 多模型统一接入：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- 内置知识库系统：提供 RAG 增强检索能力，支持私有知识库管理与向量检索
- TypeScript/现代化架构：采用 React + TypeScript 全栈开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业智能助手：构建支持多 Agent 协作的企业知识问答、文档处理、业务流程自动化系统
- 开发者 AI 工作台：个人开发者使用 LobeHub 快速原型验证 AI 应用，集成到现有产品中
- AI 应用市场：基于 LobeHub 框架搭建 AI Agent 市场，托管和分享预构建的 Agent 解决方案



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,615 |
| 语言 | Python |
| Forks | 8,484 |
| Issues | 950 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 收录的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供了 LoRA、QLoRA、RLHF 等完整的高效微调方案，是目前最受欢迎的开源 LLM 微调工具之一。

**技术亮点**:
- 统一框架：支持 100+ LLMs（Llama、Qwen、DeepSeek、Gemma 等）和 VLMs 的高效微调
- 高效微调技术：集成 LoRA、QLoRA、AdaLoRA 等 PEFT 方法，大幅降低计算和显存需求
- 完整训练流程：支持 SFT、DPO、PPO、ORPO 等多种训练范式，包括 RLHF 完整流程
- 量化与优化：支持多种量化方法（AWQ、GGUF），集成 FlashAttention 等加速技术
- 丰富的功能特性：支持多模态支持、MoE 架构、梯度累积、DeepSpeed 集成等高级特性

**适用场景**:
- 学术研究：研究人员可快速实验不同大模型的微调效果，验证新方法和训练策略
- 企业应用：团队可基于预训练模型快速构建领域专用模型（如金融、医疗、法律等垂直场景）
- 个人开发者：开发者可利用有限算力通过 QLoRA 等技术微调自己的私有化模型



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,027 |
| 语言 | TypeScript |
| Forks | 7,930 |
| Issues | 51 |
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
| Stars | 45,802 |
| 语言 | TypeScript |
| Forks | 3,489 |
| Issues | 262 |
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
| Stars | 42,796 |
| 语言 | Python |
| Forks | 9,869 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,270 |
| 语言 | TypeScript |
| Forks | 7,188 |
| Issues | 456 |
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
| Stars | 45,742 |
| 语言 | Java |
| Forks | 15,880 |
| Issues | 44 |
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
| Stars | 38,915 |
| 语言 | Python |
| Forks | 6,180 |
| Issues | 96 |
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
| Stars | 33,947 |
| 语言 | Python |
| Forks | 3,915 |
| Issues | 83 |
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
| Stars | 104,636 |
| 语言 | Python |
| Forks | 15,268 |
| Issues | 7 |
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
| Stars | 57,764 |
| 语言 | JavaScript |
| Forks | 6,235 |
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
| Stars | 70,681 |
| 语言 | Python |
| Forks | 8,862 |
| Issues | 366 |
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
| Stars | 48,833 |
| 语言 | TypeScript |
| Forks | 3,850 |
| Issues | 430 |
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
| Stars | 86,245 |
| 语言 | Python |
| Forks | 9,978 |
| Issues | 222 |
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
| Stars | 51,608 |
| 语言 | TypeScript |
| Forks | 24,075 |
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
| Stars | 182,711 |
| 语言 | TypeScript |
| Forks | 56,529 |
| Issues | 1,496 |
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
| Stars | 154,678 |
| 语言 | Java |
| Forks | 46,138 |
| Issues | 66 |
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
| Stars | 146,614 |
| 语言 | Python |
| Forks | 8,712 |
| Issues | 967 |
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
| Stars | 56,055 |
| 语言 | Jupyter Notebook |
| Forks | 19,383 |
| Issues | 25 |
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
| Stars | 72,910 |
| 语言 | MDX |
| Forks | 7,843 |
| Issues | 256 |
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
| Stars | 33,900 |
| 语言 | Python |
| Forks | 2,114 |
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
| Stars | 33,656 |
| 语言 | TypeScript |
| Forks | 3,636 |
| Issues | 286 |
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
| Stars | 33,226 |
| 语言 | Jupyter Notebook |
| Forks | 5,497 |
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
| Stars | 39,708 |
| 语言 | Rust |
| Forks | 2,490 |
| Issues | 453 |
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
| Stars | 130,326 |
| 语言 | Python |
| Forks | 18,469 |
| Issues | 303 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，130k+ Stars 证明了其极高的社区认可度。它支持 Ollama、OpenAI API 等多种后端，集成 RAG 和 MCP 能力，可完全自托管部署，是企业和个人用户构建私有化 AI 助手的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- RAG 增强能力：内置检索增强生成功能，支持知识库问答，提升模型回答准确性
- MCP 协议支持：支持 Model Context Protocol，可扩展更多 AI 工具和插件生态
- 自托管部署：支持 Docker 一键部署，数据完全私有化，适合对隐私有要求的场景
- 现代 Web 界面：提供直观的用户界面，支持对话管理、多模态交互等功能

**适用场景**:
- 企业私有化 AI 助手：企业可自托管部署，内部知识库问答、客户服务自动化等场景
- 个人开发者本地 LLM 测试：开发者可在本地运行各种开源模型（Llama、Mistral 等）进行调试和测试
- 统一 LLM 管理平台：同时接入多个 LLM 服务商，通过统一界面管理和切换，适合 AI 应用开发者



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,241 |
| 语言 | Python |
| Forks | 8,683 |
| Issues | 3,210 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，通过将 RAG 与 Agent 能力深度融合，提供了从文档解析到复杂推理的完整技术栈，特别适合需要构建高质量企业知识库和智能问答系统的团队，其 77k+ stars 和活跃社区证明了其稳定性和实用性。

**技术亮点**:
- RAG + Agent 融合架构：原生集成 Agent 能力，支持复杂多步骤推理和任务规划，相比纯 RAG 具有更强的推理能力
- 文档智能理解引擎：支持 PDF、Word、Excel 等多格式文档的深度解析，包含 OCR 识别、表格结构化、布局分析等能力
- 多索引策略支持：提供向量检索、稀疏检索、图检索（GraphRAG）等多种混合检索方式，可根据场景灵活配置
- MCP 协议支持：集成了 Model Context Protocol，可扩展调用外部工具和数据源，增强 Agent 能力边界
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等云端和本地模型部署，提供统一的调用接口

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持复杂文档理解与精准问答，适用于客服、培训、法务等场景
- Deep Research 深度研究助手：利用 Agent 编排和多步推理能力，实现复杂问题的多源信息检索与综合分析
- 智能文档处理与分析平台：批量处理合同、报告、表格等商业文档，自动提取结构化信息，支持决策分析



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,811 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 639 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 开发平台，提供了完整的多智能体协作框架、内置知识库和 MCP 协议支持，Stars 数超过 7.4 万且持续活跃，是快速构建和部署企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 之间的协作与分工，可构建复杂的 Agent Team 工作流
- MCP (Model Context Protocol) 原生支持：标准化接入外部工具和数据源，便于扩展 Agent 能力
- 多模型统一接入：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- 内置知识库系统：提供 RAG 增强检索能力，支持私有知识库管理与向量检索
- TypeScript/现代化架构：采用 React + TypeScript 全栈开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业智能助手：构建支持多 Agent 协作的企业知识问答、文档处理、业务流程自动化系统
- 开发者 AI 工作台：个人开发者使用 LobeHub 快速原型验证 AI 应用，集成到现有产品中
- AI 应用市场：基于 LobeHub 框架搭建 AI Agent 市场，托管和分享预构建的 Agent 解决方案



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,802 |
| 语言 | TypeScript |
| Forks | 3,489 |
| Issues | 262 |
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
| Stars | 45,742 |
| 语言 | Java |
| Forks | 15,880 |
| Issues | 44 |
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
| Stars | 38,915 |
| 语言 | Python |
| Forks | 6,180 |
| Issues | 96 |
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
| Stars | 33,947 |
| 语言 | Python |
| Forks | 3,915 |
| Issues | 83 |
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
| Stars | 104,636 |
| 语言 | Python |
| Forks | 15,268 |
| Issues | 7 |
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
| Stars | 100,344 |
| 语言 | TypeScript |
| Forks | 11,996 |
| Issues | 985 |
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
| Stars | 57,764 |
| 语言 | JavaScript |
| Forks | 6,235 |
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
| Stars | 74,987 |
| 语言 | Python |
| Forks | 10,187 |
| Issues | 254 |
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
| Stars | 51,608 |
| 语言 | TypeScript |
| Forks | 24,075 |
| Issues | 819 |
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
| Stars | 43,621 |
| 语言 | Go |
| Forks | 3,936 |
| Issues | 1,108 |
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
| Stars | 72,910 |
| 语言 | MDX |
| Forks | 7,843 |
| Issues | 256 |
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
| Stars | 33,900 |
| 语言 | Python |
| Forks | 2,114 |
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
| Stars | 33,656 |
| 语言 | TypeScript |
| Forks | 3,636 |
| Issues | 286 |
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
| Stars | 33,226 |
| 语言 | Jupyter Notebook |
| Forks | 5,497 |
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
| Stars | 130,326 |
| 语言 | Python |
| Forks | 18,469 |
| Issues | 303 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，130k+ Stars 证明了其极高的社区认可度。它支持 Ollama、OpenAI API 等多种后端，集成 RAG 和 MCP 能力，可完全自托管部署，是企业和个人用户构建私有化 AI 助手的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- RAG 增强能力：内置检索增强生成功能，支持知识库问答，提升模型回答准确性
- MCP 协议支持：支持 Model Context Protocol，可扩展更多 AI 工具和插件生态
- 自托管部署：支持 Docker 一键部署，数据完全私有化，适合对隐私有要求的场景
- 现代 Web 界面：提供直观的用户界面，支持对话管理、多模态交互等功能

**适用场景**:
- 企业私有化 AI 助手：企业可自托管部署，内部知识库问答、客户服务自动化等场景
- 个人开发者本地 LLM 测试：开发者可在本地运行各种开源模型（Llama、Mistral 等）进行调试和测试
- 统一 LLM 管理平台：同时接入多个 LLM 服务商，通过统一界面管理和切换，适合 AI 应用开发者



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,241 |
| 语言 | Python |
| Forks | 8,683 |
| Issues | 3,210 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 解决方案之一，通过将 RAG 与 Agent 能力深度融合，提供了从文档解析到复杂推理的完整技术栈，特别适合需要构建高质量企业知识库和智能问答系统的团队，其 77k+ stars 和活跃社区证明了其稳定性和实用性。

**技术亮点**:
- RAG + Agent 融合架构：原生集成 Agent 能力，支持复杂多步骤推理和任务规划，相比纯 RAG 具有更强的推理能力
- 文档智能理解引擎：支持 PDF、Word、Excel 等多格式文档的深度解析，包含 OCR 识别、表格结构化、布局分析等能力
- 多索引策略支持：提供向量检索、稀疏检索、图检索（GraphRAG）等多种混合检索方式，可根据场景灵活配置
- MCP 协议支持：集成了 Model Context Protocol，可扩展调用外部工具和数据源，增强 Agent 能力边界
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等云端和本地模型部署，提供统一的调用接口

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持复杂文档理解与精准问答，适用于客服、培训、法务等场景
- Deep Research 深度研究助手：利用 Agent 编排和多步推理能力，实现复杂问题的多源信息检索与综合分析
- 智能文档处理与分析平台：批量处理合同、报告、表格等商业文档，自动提取结构化信息，支持决策分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 142,454 |
| 语言 | JavaScript |
| Forks | 21,655 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于AI代码助手性能优化的开源系统，拥有超过14万stars的高人气，提供了Skills、Instincts、Memory、Security和Research-first五大核心模块，为Claude Code、Codex、Cursor等多个主流AI编程工具提供统一的性能增强框架。

**技术亮点**:
- 多Agent框架支持：兼容Claude Code、Codex、Opencode、Cursor等多个AI编程助手，提供统一的任务执行和优化接口
- 模块化性能优化系统：包含Skills、Instincts、Memory、Security等独立模块，可灵活组合以满足不同场景需求
- 安全机制设计：内置Security模块，提供安全的代码执行和访问控制，保障AI操作的安全性
- 记忆系统实现：通过Memory模块实现上下文持久化和状态管理，提升AI代理的长期任务处理能力
- 研究驱动开发：采用Research-first开发理念，持续优化和迭代，确保技术先进性

**适用场景**:
- 企业级AI开发团队：需要统一管理多个AI编程工具、提升团队开发效率和安全性的企业环境
- 个人开发者效率提升：希望优化个人工作流，获得更智能、更安全的AI辅助编程体验
- AI研究实验：研究人员用于测试和对比不同AI代码助手的性能表现
- DevOps自动化集成：将AI代码助手集成到CI/CD流程中，实现自动化代码审查和优化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,811 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 639 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 开发平台，提供了完整的多智能体协作框架、内置知识库和 MCP 协议支持，Stars 数超过 7.4 万且持续活跃，是快速构建和部署企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 之间的协作与分工，可构建复杂的 Agent Team 工作流
- MCP (Model Context Protocol) 原生支持：标准化接入外部工具和数据源，便于扩展 Agent 能力
- 多模型统一接入：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- 内置知识库系统：提供 RAG 增强检索能力，支持私有知识库管理与向量检索
- TypeScript/现代化架构：采用 React + TypeScript 全栈开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业智能助手：构建支持多 Agent 协作的企业知识问答、文档处理、业务流程自动化系统
- 开发者 AI 工作台：个人开发者使用 LobeHub 快速原型验证 AI 应用，集成到现有产品中
- AI 应用市场：基于 LobeHub 框架搭建 AI Agent 市场，托管和分享预构建的 Agent 解决方案



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,677 |
| 语言 | HTML |
| Forks | 20,640 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词集合项目，拥有超过 15 万星标和丰富的社区贡献，支持 ChatGPT/Claude/Gemini 等多平台，且完全开源可自托管，是 AI 时代必备的提示词资源库和团队协作工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，提供良好的开发体验和类型安全
- 支持多 LLM 平台（ChatGPT、Claude、Gemini、GPT-4 等），统一管理不同模型的提示词
- 开源可自托管设计，支持企业部署以确保数据隐私和安全性
- 社区驱动的提示词收集机制，持续更新高质量prompt资源
- TypeScript 类型定义完善，便于二次开发和扩展定制

**适用场景**:
- 个人开发者/用户：快速查找和复用经过验证的高质量 AI 提示词，提升日常工作和生活中的 AI 使用效率
- 企业团队：自部署私有化提示词库，保护商业敏感信息的同时实现团队内部 prompt 共享和标准化
- AI 应用开发者：参考项目架构和提示词设计模式，开发类似的提示词管理平台或集成到现有产品中



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,141 |
| 语言 | Jupyter Notebook |
| Forks | 13,797 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 亲自操刀，通过 Jupyter Notebook 逐步讲解如何从零实现 ChatGPT 级别的 LLM，配合详细图解和代码注释，是目前最系统、最深入的大语言模型学习资源。

**技术亮点**:
- 从零实现 Transformer 完整架构：多头注意力机制、前馈网络、位置编码等核心组件
- 涵盖现代 LLM 技术：Flash Attention、RMSNorm、SwiGLU 激活函数、RoPE 旋转位置编码等
- 使用纯 PyTorch 实现，无外部 LLM 库依赖，便于深入理解底层机制
- 提供 GPT-2 权重加载和微调示例，支持实际模型训练
- 分步骤讲解 + 可视化图解 + Jupyter Notebook 交互式学习体验

**适用场景**:
- LLM 入门学习：系统学习大语言模型架构原理和实现细节的最佳实践课程
- 企业培训：作为团队 AI 能力提升的内部培训教材
- 模型定制开发：基于教程理解原理后进行垂直领域 LLM 微调或从头训练



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,027 |
| 语言 | TypeScript |
| Forks | 7,930 |
| Issues | 51 |
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
| Stars | 45,802 |
| 语言 | TypeScript |
| Forks | 3,489 |
| Issues | 262 |
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
| Stars | 42,796 |
| 语言 | Python |
| Forks | 9,869 |
| Issues | 353 |
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
| Stars | 36,919 |
| 语言 | Python |
| Forks | 2,929 |
| Issues | 176 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,270 |
| 语言 | TypeScript |
| Forks | 7,188 |
| Issues | 456 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,764 |
| 语言 | JavaScript |
| Forks | 6,235 |
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
| Stars | 70,681 |
| 语言 | Python |
| Forks | 8,862 |
| Issues | 366 |
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
| Stars | 48,833 |
| 语言 | TypeScript |
| Forks | 3,850 |
| Issues | 430 |
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
| Stars | 51,608 |
| 语言 | TypeScript |
| Forks | 24,075 |
| Issues | 819 |
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
| Stars | 37,588 |
| 语言 | Unknown |
| Forks | 6,194 |
| Issues | 21 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,470 |
| 语言 | Python |
| Forks | 15,234 |
| Issues | 4,094 |
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
| Stars | 59,840 |
| 语言 | Python |
| Forks | 5,938 |
| Issues | 77 |
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
| Stars | 39,301 |
| 语言 | TypeScript |
| Forks | 4,008 |
| Issues | 1,094 |
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
| Stars | 146,614 |
| 语言 | Python |
| Forks | 8,712 |
| Issues | 967 |
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
| Stars | 167,601 |
| 语言 | Go |
| Forks | 15,382 |
| Issues | 2,860 |
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
| Stars | 72,910 |
| 语言 | MDX |
| Forks | 7,843 |
| Issues | 256 |
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
| Stars | 47,604 |
| 语言 | Rust |
| Forks | 9,468 |
| Issues | 3 |
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
| Stars | 33,900 |
| 语言 | Python |
| Forks | 2,114 |
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
| Stars | 93,399 |
| 语言 | Python |
| Forks | 5,645 |
| Issues | 511 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
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
| Stars | 69,615 |
| 语言 | Python |
| Forks | 8,484 |
| Issues | 950 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 收录的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供了 LoRA、QLoRA、RLHF 等完整的高效微调方案，是目前最受欢迎的开源 LLM 微调工具之一。

**技术亮点**:
- 统一框架：支持 100+ LLMs（Llama、Qwen、DeepSeek、Gemma 等）和 VLMs 的高效微调
- 高效微调技术：集成 LoRA、QLoRA、AdaLoRA 等 PEFT 方法，大幅降低计算和显存需求
- 完整训练流程：支持 SFT、DPO、PPO、ORPO 等多种训练范式，包括 RLHF 完整流程
- 量化与优化：支持多种量化方法（AWQ、GGUF），集成 FlashAttention 等加速技术
- 丰富的功能特性：支持多模态支持、MoE 架构、梯度累积、DeepSpeed 集成等高级特性

**适用场景**:
- 学术研究：研究人员可快速实验不同大模型的微调效果，验证新方法和训练策略
- 企业应用：团队可基于预训练模型快速构建领域专用模型（如金融、医疗、法律等垂直场景）
- 个人开发者：开发者可利用有限算力通过 QLoRA 等技术微调自己的私有化模型



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,488 |
| 语言 | Python |
| Forks | 6,486 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据分析平台，提供标准化API接口，支持股票、期权、加密货币、固定收益等多类资产的数据获取与可视化，其模块化架构和AI代理集成能力使其成为个人投资者和量化团队的首选工具。

**技术亮点**:
- 统一的Python SDK和CLI工具链，提供标准化的金融数据访问接口
- 支持实时市场数据、宏观经济指标、财务报表等多维度数据源集成
- 内置技术指标计算、量化因子库和技术分析可视化功能
- 集成AI/ML能力，支持自然语言查询和智能投顾代理开发
- 模块化架构设计，支持自定义扩展和数据源插件开发

**适用场景**:
- 量化投资研究：用于构建量化策略、回测系统和因子分析，支持Jupyter Notebook集成
- 投资组合分析与风险管理：实时监控持仓、分析风险敞口、执行技术分析和基本面分析
- AI金融代理开发：为AI代理提供金融数据工具调用接口，支持构建智能投顾和自动化交易系统
- 金融数据工程：搭建企业级金融数据管道，整合多数据源并提供统一的数据服务



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,677 |
| 语言 | HTML |
| Forks | 20,640 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词集合项目，拥有超过 15 万星标和丰富的社区贡献，支持 ChatGPT/Claude/Gemini 等多平台，且完全开源可自托管，是 AI 时代必备的提示词资源库和团队协作工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，提供良好的开发体验和类型安全
- 支持多 LLM 平台（ChatGPT、Claude、Gemini、GPT-4 等），统一管理不同模型的提示词
- 开源可自托管设计，支持企业部署以确保数据隐私和安全性
- 社区驱动的提示词收集机制，持续更新高质量prompt资源
- TypeScript 类型定义完善，便于二次开发和扩展定制

**适用场景**:
- 个人开发者/用户：快速查找和复用经过验证的高质量 AI 提示词，提升日常工作和生活中的 AI 使用效率
- 企业团队：自部署私有化提示词库，保护商业敏感信息的同时实现团队内部 prompt 共享和标准化
- AI 应用开发者：参考项目架构和提示词设计模式，开发类似的提示词管理平台或集成到现有产品中



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,141 |
| 语言 | Jupyter Notebook |
| Forks | 13,797 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 亲自操刀，通过 Jupyter Notebook 逐步讲解如何从零实现 ChatGPT 级别的 LLM，配合详细图解和代码注释，是目前最系统、最深入的大语言模型学习资源。

**技术亮点**:
- 从零实现 Transformer 完整架构：多头注意力机制、前馈网络、位置编码等核心组件
- 涵盖现代 LLM 技术：Flash Attention、RMSNorm、SwiGLU 激活函数、RoPE 旋转位置编码等
- 使用纯 PyTorch 实现，无外部 LLM 库依赖，便于深入理解底层机制
- 提供 GPT-2 权重加载和微调示例，支持实际模型训练
- 分步骤讲解 + 可视化图解 + Jupyter Notebook 交互式学习体验

**适用场景**:
- LLM 入门学习：系统学习大语言模型架构原理和实现细节的最佳实践课程
- 企业培训：作为团队 AI 能力提升的内部培训教材
- 模型定制开发：基于教程理解原理后进行垂直领域 LLM 微调或从头训练



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,889 |
| 语言 | Python |
| Forks | 32,754 |
| Issues | 2,360 |
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
| Stars | 75,470 |
| 语言 | Python |
| Forks | 15,234 |
| Issues | 4,094 |
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
| Stars | 107,919 |
| 语言 | Python |
| Forks | 12,488 |
| Issues | 3,940 |
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
| Stars | 98,851 |
| 语言 | Python |
| Forks | 27,415 |
| Issues | 18,229 |
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
| Stars | 72,910 |
| 语言 | MDX |
| Forks | 7,843 |
| Issues | 256 |
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
| Stars | 33,656 |
| 语言 | TypeScript |
| Forks | 3,636 |
| Issues | 286 |
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
| Stars | 33,226 |
| 语言 | Jupyter Notebook |
| Forks | 5,497 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 🛠️ 开发工具 (16 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 142,454 |
| 语言 | JavaScript |
| Forks | 21,655 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于AI代码助手性能优化的开源系统，拥有超过14万stars的高人气，提供了Skills、Instincts、Memory、Security和Research-first五大核心模块，为Claude Code、Codex、Cursor等多个主流AI编程工具提供统一的性能增强框架。

**技术亮点**:
- 多Agent框架支持：兼容Claude Code、Codex、Opencode、Cursor等多个AI编程助手，提供统一的任务执行和优化接口
- 模块化性能优化系统：包含Skills、Instincts、Memory、Security等独立模块，可灵活组合以满足不同场景需求
- 安全机制设计：内置Security模块，提供安全的代码执行和访问控制，保障AI操作的安全性
- 记忆系统实现：通过Memory模块实现上下文持久化和状态管理，提升AI代理的长期任务处理能力
- 研究驱动开发：采用Research-first开发理念，持续优化和迭代，确保技术先进性

**适用场景**:
- 企业级AI开发团队：需要统一管理多个AI编程工具、提升团队开发效率和安全性的企业环境
- 个人开发者效率提升：希望优化个人工作流，获得更智能、更安全的AI辅助编程体验
- AI研究实验：研究人员用于测试和对比不同AI代码助手的性能表现
- DevOps自动化集成：将AI代码助手集成到CI/CD流程中，实现自动化代码审查和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,964 |
| 语言 | Go |
| Forks | 3,863 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源 AI 推理引擎，支持在本地运行 LLM、图像、音频、视频等多种模型，无需 GPU 即可部署，极大降低了 AI 应用的技术门槛和数据隐私风险，尤其适合需要私有化部署 AI 能力的开发者。

**技术亮点**:
- 多模型支持：兼容 Llama、Mamba、Stable Diffusion、MusicGen、GPT-4 等主流开源模型，覆盖文本生成、图像生成、语音合成、目标检测等多种任务
- 无 GPU 限制：支持 CPU 推理，可在普通硬件上运行，降低了 AI 部署的硬件成本和入门门槛
- OpenAI 兼容 API：提供与 OpenAI API 格式兼容的接口，现有基于 OpenAI 的应用可零成本迁移，大幅减少开发工作量
- Go 语言开发：采用 Go 语言实现，具备高并发、低内存占用的优势，适合生产环境部署
- 去中心化架构：支持 libp2p 分布式部署，可构建分布式 AI 推理网络，提供更高的可扩展性和容错能力

**适用场景**:
- 隐私敏感场景：在医疗、法律、金融等需要数据隐私保护的领域，LocalAI 允许模型推理完全在本地完成，数据不出本地，满足合规要求
- 私有化 AI 部署：企业可基于 LocalAI 构建内部的 AI 助手、客服机器人或文档处理系统，无需依赖第三方云服务
- 资源受限环境：面向没有 GPU 的开发者或个人用户，提供在普通电脑或服务器上运行 AI 模型的轻量化解决方案



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,681 |
| 语言 | Python |
| Forks | 8,862 |
| Issues | 366 |
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
| Stars | 48,833 |
| 语言 | TypeScript |
| Forks | 3,850 |
| Issues | 430 |
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
| Stars | 182,711 |
| 语言 | TypeScript |
| Forks | 56,529 |
| Issues | 1,496 |
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
| Stars | 155,167 |
| 语言 | Python |
| Forks | 12,694 |
| Issues | 2,441 |
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
| Stars | 96,898 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 167 |
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
| Stars | 80,032 |
| 语言 | Python |
| Forks | 9,304 |
| Issues | 244 |
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
| Stars | 183,485 |
| 语言 | TypeScript |
| Forks | 39,059 |
| Issues | 16,126 |
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
| Stars | 94,026 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 305 |
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
| Stars | 78,819 |
| 语言 | TypeScript |
| Forks | 5,761 |
| Issues | 734 |
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
| Stars | 76,974 |
| 语言 | TypeScript |
| Forks | 6,592 |
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
| Stars | 79,302 |
| 语言 | Go |
| Forks | 2,751 |
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
| Stars | 75,683 |
| 语言 | Go |
| Forks | 2,691 |
| Issues | 937 |
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
| Stars | 419,666 |
| 语言 | Python |
| Forks | 45,656 |
| Issues | 1,200 |
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
| Stars | 75,668 |
| 语言 | JavaScript |
| Forks | 7,274 |
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
| Stars | 48,833 |
| 语言 | TypeScript |
| Forks | 3,850 |
| Issues | 430 |
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
| Stars | 182,711 |
| 语言 | TypeScript |
| Forks | 56,529 |
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
| Stars | 51,693 |
| 语言 | Go |
| Forks | 10,342 |
| Issues | 219 |
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
| Stars | 121,537 |
| 语言 | Go |
| Forks | 42,801 |
| Issues | 2,717 |
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
| Stars | 71,569 |
| 语言 | Go |
| Forks | 18,913 |
| Issues | 3,780 |
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
| Stars | 54,754 |
| 语言 | Go |
| Forks | 6,534 |
| Issues | 2,831 |
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
| Stars | 47,600 |
| 语言 | Go |
| Forks | 5,066 |
| Issues | 979 |
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
| Stars | 94,026 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 305 |
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
| Stars | 76,328 |
| 语言 | TypeScript |
| Forks | 6,551 |
| Issues | 407 |
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
| Stars | 84,917 |
| 语言 | JavaScript |
| Forks | 7,602 |
| Issues | 714 |
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
| Stars | 69,730 |
| 语言 | Go |
| Forks | 1,902 |
| Issues | 319 |
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
| Stars | 62,501 |
| 语言 | Go |
| Forks | 5,901 |
| Issues | 774 |
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
| Stars | 58,594 |
| 语言 | Go |
| Forks | 4,247 |
| Issues | 28 |
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
| Stars | 84,917 |
| 语言 | JavaScript |
| Forks | 7,602 |
| Issues | 714 |
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
| Stars | 63,418 |
| 语言 | Go |
| Forks | 10,309 |
| Issues | 767 |
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
| Stars | 44,964 |
| 语言 | Go |
| Forks | 3,863 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源 AI 推理引擎，支持在本地运行 LLM、图像、音频、视频等多种模型，无需 GPU 即可部署，极大降低了 AI 应用的技术门槛和数据隐私风险，尤其适合需要私有化部署 AI 能力的开发者。

**技术亮点**:
- 多模型支持：兼容 Llama、Mamba、Stable Diffusion、MusicGen、GPT-4 等主流开源模型，覆盖文本生成、图像生成、语音合成、目标检测等多种任务
- 无 GPU 限制：支持 CPU 推理，可在普通硬件上运行，降低了 AI 部署的硬件成本和入门门槛
- OpenAI 兼容 API：提供与 OpenAI API 格式兼容的接口，现有基于 OpenAI 的应用可零成本迁移，大幅减少开发工作量
- Go 语言开发：采用 Go 语言实现，具备高并发、低内存占用的优势，适合生产环境部署
- 去中心化架构：支持 libp2p 分布式部署，可构建分布式 AI 推理网络，提供更高的可扩展性和容错能力

**适用场景**:
- 隐私敏感场景：在医疗、法律、金融等需要数据隐私保护的领域，LocalAI 允许模型推理完全在本地完成，数据不出本地，满足合规要求
- 私有化 AI 部署：企业可基于 LocalAI 构建内部的 AI 助手、客服机器人或文档处理系统，无需依赖第三方云服务
- 资源受限环境：面向没有 GPU 的开发者或个人用户，提供在普通电脑或服务器上运行 AI 模型的轻量化解决方案



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,898 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 167 |
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
| Stars | 87,178 |
| 语言 | Python |
| Forks | 33,806 |
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
| Stars | 100,106 |
| 语言 | TypeScript |
| Forks | 27,143 |
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
| Stars | 78,819 |
| 语言 | TypeScript |
| Forks | 5,761 |
| Issues | 734 |
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
| Stars | 68,891 |
| 语言 | JavaScript |
| Forks | 23,038 |
| Issues | 210 |
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
| Stars | 55,947 |
| 语言 | JavaScript |
| Forks | 10,210 |
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
| Stars | 51,726 |
| 语言 | JavaScript |
| Forks | 4,695 |
| Issues | 1,480 |
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
| Stars | 47,749 |
| 语言 | JavaScript |
| Forks | 1,583 |
| Issues | 662 |
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
| Stars | 88,340 |
| 语言 | Go |
| Forks | 8,569 |
| Issues | 666 |
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
| Stars | 71,317 |
| 语言 | Go |
| Forks | 4,691 |
| Issues | 259 |
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
| Stars | 57,416 |
| 语言 | Go |
| Forks | 3,260 |
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
| Stars | 419,666 |
| 语言 | Python |
| Forks | 45,656 |
| Issues | 1,200 |
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
| Stars | 75,668 |
| 语言 | JavaScript |
| Forks | 7,274 |
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
| Stars | 100,344 |
| 语言 | TypeScript |
| Forks | 11,996 |
| Issues | 985 |
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
| Stars | 57,764 |
| 语言 | JavaScript |
| Forks | 6,235 |
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
| Stars | 43,621 |
| 语言 | Go |
| Forks | 3,936 |
| Issues | 1,108 |
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
| Issues | 219 |
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
| Stars | 157,677 |
| 语言 | HTML |
| Forks | 20,640 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最受欢迎的 AI 提示词集合项目，拥有超过 15 万星标和丰富的社区贡献，支持 ChatGPT/Claude/Gemini 等多平台，且完全开源可自托管，是 AI 时代必备的提示词资源库和团队协作工具。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，提供良好的开发体验和类型安全
- 支持多 LLM 平台（ChatGPT、Claude、Gemini、GPT-4 等），统一管理不同模型的提示词
- 开源可自托管设计，支持企业部署以确保数据隐私和安全性
- 社区驱动的提示词收集机制，持续更新高质量prompt资源
- TypeScript 类型定义完善，便于二次开发和扩展定制

**适用场景**:
- 个人开发者/用户：快速查找和复用经过验证的高质量 AI 提示词，提升日常工作和生活中的 AI 使用效率
- 企业团队：自部署私有化提示词库，保护商业敏感信息的同时实现团队内部 prompt 共享和标准化
- AI 应用开发者：参考项目架构和提示词设计模式，开发类似的提示词管理平台或集成到现有产品中



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,027 |
| 语言 | TypeScript |
| Forks | 7,930 |
| Issues | 51 |
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
| Stars | 36,919 |
| 语言 | Python |
| Forks | 2,929 |
| Issues | 176 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,947 |
| 语言 | Python |
| Forks | 3,915 |
| Issues | 83 |
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
| Stars | 37,588 |
| 语言 | Unknown |
| Forks | 6,194 |
| Issues | 21 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,910 |
| 语言 | MDX |
| Forks | 7,843 |
| Issues | 256 |
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
| Stars | 89,636 |
| 语言 | TypeScript |
| Forks | 9,978 |
| Issues | 2,226 |
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
| Stars | 87,145 |
| 语言 | TypeScript |
| Forks | 8,820 |
| Issues | 1,641 |
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
| Stars | 127,337 |
| 语言 | JavaScript |
| Forks | 12,465 |
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
| Stars | 169,237 |
| 语言 | Go |
| Forks | 13,113 |
| Issues | 170 |
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
| Stars | 63,472 |
| 语言 | Python |
| Forks | 6,491 |
| Issues | 59 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,081 |
| 语言 | Python |
| Forks | 12,939 |
| Issues | 114 |
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
| Stars | 85,662 |
| 语言 | Python |
| Forks | 7,358 |
| Issues | 621 |
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
| Stars | 134,561 |
| 语言 | Unknown |
| Forks | 33,876 |
| Issues | 144 |
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
| Stars | 385,097 |
| 语言 | Python |
| Forks | 66,089 |
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
| Stars | 114,276 |
| 语言 | TypeScript |
| Forks | 5,870 |
| Issues | 314 |
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
| Stars | 108,123 |
| 语言 | TypeScript |
| Forks | 7,860 |
| Issues | 232 |
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
| Stars | 48,364 |
| 语言 | JavaScript |
| Forks | 3,999 |
| Issues | 16 |
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
| Stars | 48,046 |
| 语言 | Go |
| Forks | 10,265 |
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
| Stars | 101,943 |
| 语言 | C++ |
| Forks | 16,455 |
| Issues | 1,404 |
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
| Stars | 63,415 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 31 |
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
| Stars | 65,369 |
| 语言 | TypeScript |
| Forks | 8,939 |
| Issues | 326 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 291,003 |
| 语言 | Python |
| Forks | 27,587 |
| Issues | 21 |
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
| Stars | 219,317 |
| 语言 | Python |
| Forks | 50,305 |
| Issues | 918 |
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
| Stars | 86,014 |
| 语言 | Python |
| Forks | 37,170 |
| Issues | 3,560 |
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
| Stars | 77,674 |
| 语言 | Python |
| Forks | 45,172 |
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
| Stars | 441,921 |
| 语言 | TypeScript |
| Forks | 44,141 |
| Issues | 219 |
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
| Stars | 352,376 |
| 语言 | TypeScript |
| Forks | 43,874 |
| Issues | 2 |
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
| Stars | 138,583 |
| 语言 | TypeScript |
| Forks | 16,490 |
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
| Stars | 120,373 |
| 语言 | TypeScript |
| Forks | 13,154 |
| Issues | 2,927 |
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
| Stars | 111,646 |
| 语言 | TypeScript |
| Forks | 8,443 |
| Issues | 1,799 |
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
| Stars | 108,433 |
| 语言 | TypeScript |
| Forks | 13,324 |
| Issues | 5,014 |
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
| Stars | 97,771 |
| 语言 | TypeScript |
| Forks | 54,570 |
| Issues | 1,360 |
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
| Stars | 96,757 |
| 语言 | TypeScript |
| Forks | 5,280 |
| Issues | 671 |
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
| Stars | 94,369 |
| 语言 | TypeScript |
| Forks | 5,176 |
| Issues | 106 |
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
| Stars | 83,061 |
| 语言 | TypeScript |
| Forks | 7,577 |
| Issues | 33 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,622 |
| 语言 | TypeScript |
| Forks | 8,014 |
| Issues | 721 |
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
| Stars | 244,433 |
| 语言 | JavaScript |
| Forks | 50,979 |
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
| Stars | 116,561 |
| 语言 | JavaScript |
| Forks | 35,268 |
| Issues | 2,605 |
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
| Stars | 111,791 |
| 语言 | JavaScript |
| Forks | 36,321 |
| Issues | 564 |
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
| Stars | 109,042 |
| 语言 | JavaScript |
| Forks | 11,601 |
| Issues | 331 |
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
| Stars | 98,020 |
| 语言 | JavaScript |
| Forks | 32,689 |
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
| Stars | 95,529 |
| 语言 | JavaScript |
| Forks | 15,321 |
| Issues | 56 |
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
| Stars | 86,190 |
| 语言 | JavaScript |
| Forks | 4,866 |
| Issues | 977 |
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
| Stars | 78,973 |
| 语言 | JavaScript |
| Forks | 32,207 |
| Issues | 275 |
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
| Stars | 70,936 |
| 语言 | JavaScript |
| Forks | 16,812 |
| Issues | 892 |
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
| Stars | 65,933 |
| 语言 | JavaScript |
| Forks | 9,379 |
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
| Stars | 62,564 |
| 语言 | JavaScript |
| Forks | 3,996 |
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
| Stars | 61,519 |
| 语言 | JavaScript |
| Forks | 7,127 |
| Issues | 136 |
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
| Stars | 60,259 |
| 语言 | JavaScript |
| Forks | 5,646 |
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
| Forks | 20,460 |
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
| Stars | 57,426 |
| 语言 | JavaScript |
| Forks | 12,299 |
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
| Stars | 53,086 |
| 语言 | JavaScript |
| Forks | 10,606 |
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
| Stars | 52,403 |
| 语言 | JavaScript |
| Forks | 11,429 |
| Issues | 236 |
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
| Stars | 48,630 |
| 语言 | JavaScript |
| Forks | 2,426 |
| Issues | 1,207 |
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
| Stars | 133,286 |
| 语言 | Go |
| Forks | 18,967 |
| Issues | 9,935 |
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
| Stars | 87,439 |
| 语言 | Go |
| Forks | 8,237 |
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
| Stars | 81,469 |
| 语言 | Go |
| Forks | 4,987 |
| Issues | 393 |
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
| Stars | 68,639 |
| 语言 | Go |
| Forks | 3,212 |
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
| Stars | 56,498 |
| 语言 | Go |
| Forks | 5,009 |
| Issues | 1,160 |
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
| Stars | 50,967 |
| 语言 | Go |
| Forks | 21,879 |
| Issues | 399 |
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
| Stars | 49,258 |
| 语言 | Go |
| Forks | 7,955 |
| Issues | 560 |
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
| Stars | 72,973 |
| 语言 | Shell |
| Forks | 11,364 |
| Issues | 100 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,153 |
| 语言 | Python |
| Forks | 11,313 |
| Issues | 323 |
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
| Stars | 341,631 |
| 语言 | Python |
| Forks | 55,226 |
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
| Stars | 97,254 |
| 语言 | Python |
| Forks | 11,986 |
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
| Stars | 85,821 |
| 语言 | Python |
| Forks | 7,203 |
| Issues | 482 |
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
| Stars | 76,676 |
| 语言 | Python |
| Forks | 16,830 |
| Issues | 20 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,083 |
| 语言 | TypeScript |
| Forks | 10,227 |
| Issues | 680 |
| 许可证 | Other |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,302 |
| 语言 | JavaScript |
| Forks | 9,183 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,841 |
| 语言 | Go |
| Forks | 14,976 |
| Issues | 45 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,540 |
| 语言 | Go |
| Forks | 1,593 |
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
| Stars | 46,965 |
| 语言 | Go |
| Forks | 8,866 |
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
| Stars | 45,826 |
| 语言 | Go |
| Forks | 3,779 |
| Issues | 85 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
