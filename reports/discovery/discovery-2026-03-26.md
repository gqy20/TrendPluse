# 项目发现报告 (2026-03-26)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
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
| Stars | 128,835 |
| 语言 | Python |
| Forks | 18,220 |
| Issues | 261 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最完整的开源 LLM Web 界面解决方案，12.9万 Stars 证明了其社区认可度。它同时支持 Ollama 和 OpenAI API 等多种后端，提供了开箱即用的 RAG 检索增强和 MCP 协议扩展能力，让用户能够零成本搭建功能完整的私有 AI 对话平台。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型、OpenAI API、Azure OpenAI 等多种 LLM 服务提供方，灵活性极高
- RAG 检索增强：内置文档解析和向量检索能力，支持上传 PDF、Word、Markdown 等文件进行问答
- MCP 协议集成：支持 Model Context Protocol，可扩展连接各类外部工具和数据源
- 自托管部署：提供 Docker 一键部署方案，数据完全私有，适合对数据安全有要求的企业
- 现代化 Web UI：响应式设计，支持主题定制、对话管理、模型参数调节等功能

**适用场景**:
- 企业私有 AI 助手：部署在企业内部网络中，为员工提供文档问答、知识检索、会议纪要生成等场景的 AI 服务，数据不出内网
- 个人开发者本地 LLM 开发：配合 Ollama 在本地运行开源大模型（如 Llama、Qwen、Mistral），进行 Prompt 工程调试和 AI 应用原型开发
- 知识库智能问答系统：上传产品文档、技术手册、内部 wiki 等资料，构建基于自有知识的 RAG 问答机器人



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,264 |
| 语言 | Python |
| Forks | 8,535 |
| Issues | 3,166 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个功能完备、社区活跃（76k+ stars）的开源 RAG 引擎，通过融合 RAG 与 Agent 能力为 LLM 提供高质量的上下文检索层，特别适合构建企业级智能知识库和复杂文档问答系统。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能 Agent 能力深度结合，实现自主推理和多步查询优化
- 多模态文档解析引擎：内置专业文档解析器，支持复杂结构化文档的智能理解和向量化
- 混合检索能力：支持传统向量检索与 GraphRAG 图检索的融合，提升关系型知识检索效果
- 广泛 LLM 支持：兼容 OpenAI、Ollama、DeepSeek 等多种大模型，提供灵活的模型接入方案
- MCP 协议支持：集成 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业知识库智能问答：构建私有化知识库问答系统，支持复杂文档检索和多轮对话
- 深度研究助手：基于 GraphRAG 和 Agent 能力，实现跨文档关系推理和深度研究分析
- 智能文档处理平台：自动解析理解复杂技术文档、合同、报告等，实现精准信息提取
- RAG 应用开发框架：为开发者提供完整的 RAG 技术栈，快速搭建各类智能问答和检索应用



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,726 |
| 语言 | TypeScript |
| Forks | 6,634 |
| Issues | 239 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据抓取工具，能将任意网站转换为 LLM 可直接使用的 markdown 或结构化数据，支持整站抓取且内置反屏蔽机制，是构建 AI 搜索、数据采集和知识库系统的首选方案。

**技术亮点**:
- 专为 LLM 设计的内容提取引擎，自动将网页 HTML 转换为高质量 markdown，保留关键信息并去除噪音
- 支持整站抓取能力，智能发现并抓取所有相关页面，保持网站结构完整性
- 内置 JavaScript 渲染支持，能够处理 SPA（单页应用）和动态加载内容
- 提供即用的 API 服务，支持分布式抓取，具备反屏蔽机制和速率限制保护
- 支持结构化数据提取，可输出 JSON/HTML/Markdown 多种格式，便于 AI 模型直接消费

**适用场景**:
- AI 应用数据管道：为 LLM/RAG 系统提供实时网络数据抓取和预处理，构建高质量知识库
- 竞品监控与市场调研：自动化抓取目标网站内容，提取产品信息、价格数据用于市场分析
- 智能搜索引擎构建：快速建立垂直领域搜索引擎，将网页内容转换为可索引的标准化格式



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,027 |
| 语言 | JavaScript |
| Forks | 14,357 |
| Issues | 139 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编码助手设计的综合性能优化框架，支持多种主流 AI 编程工具（Claude Code、Cursor、Codex等），通过模块化的 Skills/Instincts/Memory 机制显著提升 AI Agent 的任务完成效率和智能化水平，11万 Stars 的高热度证明了其在 AI 开发工具领域的广泛认可和实用价值。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供跨平台的开发体验
- 模块化 Skills 系统：通过可扩展的技能模块增强 Agent 能力，支持自定义功能扩展
- 本能机制（Instincts）：内置智能响应模式，让 AI Agent 具备更接近人类开发者的直觉判断能力
- 记忆管理系统：提供持久化上下文记忆功能，解决长对话场景下的信息丢失问题
- 安全与隐私保护：内置安全机制，确保 AI 辅助开发过程中的代码安全和数据隐私

**适用场景**:
- AI 辅助编程效率优化：为开发团队提供统一的 AI 编码助手配置和优化方案，提升整体开发效率
- 构建企业级 AI 开发工作流：基于 MCP 协议集成多种 AI 工具，打造企业专属的智能开发平台
- 个人开发者效率提升：通过 Skills 和记忆功能，让 AI 助手更好地理解项目上下文，减少重复沟通成本



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,437 |
| 语言 | Go |
| Forks | 3,797 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是唯一一款支持在任意硬件上本地运行多模态 AI 模型（LLMs、视觉、语音、图像、视频）的开源引擎，无需 GPU 即可部署，为隐私敏感场景和企业私有化 AI 提供了免费且高效的替代方案。

**技术亮点**:
- 基于 Go 语言开发，充分利用 goroutine 实现高效的并发模型推理，支持高并发 API 请求处理
- 支持 llama、mamba、stable-diffusion、musicgen、whisper 等多种主流模型架构，一站式满足文本、图像、音频、视频生成需求
- 去中心化架构设计，支持 libp2p 分布式部署，可在多节点间协同运行 AI 推理任务
- API 优先设计，提供 OpenAI 兼容的 API 接口，降低迁移成本，方便快速集成到现有系统
- MCP (Model Context Protocol) 协议支持，增强 AI Agent 能力，支持更复杂的多模态交互场景

**适用场景**:
- 企业私有化 AI 部署：在数据隐私要求严格的金融、医疗、法律等场景中，无需将敏感数据上传至第三方云服务，实现完全的本地化 AI 处理
- 开发者本地 AI 原型开发：个人开发者或团队可在没有 GPU 的开发机器上快速验证 AI 功能，加速产品迭代和原型开发
- 边缘计算与嵌入式 AI：支持在资源受限的边缘设备上部署 AI 推理能力，适用于 IoT 设备、机器人、智能终端等场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,357 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 668 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟度极高的 AI Agent 平台（74K+ Stars），支持多模型集成与多 Agent 协作编排，为开发者和企业提供了开箱即用的 Agent 团队构建能力，是当前 AI Agent 领域最具参考价值的开源项目之一。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的模型调用接口
- 多 Agent 协作引擎：实现 Agent 间通信与任务协作，支持复杂工作流的自动化编排
- 知识库增强系统：内置知识库管理能力，支持 RAG 检索增强，提升 Agent 回答准确性
- MCP 协议支持：遵循 Model Context Protocol 标准，可扩展连接外部工具和服务生态
- TypeScript 全栈架构：基于现代化的前端框架，具备良好的类型安全和可维护性

**适用场景**:
- 企业级智能助手搭建：利用多 Agent 协作能力构建客服、文档助手、数据分析等多种角色的智能团队
- 个人开发者 AI 工作流：通过 Agent 编排实现自动化编程、代码审查、日程管理等效率工具
- 知识密集型应用开发：结合知识库功能开发智能问答、文档检索、培训助手等专业场景应用



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,116 |
| 语言 | Python |
| Forks | 8,429 |
| Issues | 938 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个在 ACL 2024 发表的统一大模型微调框架，支持 100+ 主流 LLM 和 VLM 模型，集成 LoRA/QLoRA/RLHF 等多种高效微调技术，提供 WebUI 和 CLI 两种交互方式，让研究者和开发者能够零门槛快速微调大模型。

**技术亮点**:
- 支持 100+ 预训练模型统一微调，涵盖 Llama/Gemma/Qwen/DeepSeek/Mistral 等主流开源大模型
- 集成多种高效微调算法：LoRA、QLoRA、AdaLoRA、LyCORIS 等 PEFT 方法
- 支持完整的 RLHF 流程：SFT + Reward Model + PPO + DPO
- 内置 4bit/8bit 量化功能（GPTQ/AWQ/GGUF），大幅降低显存需求
- 提供可视化 WebUI 和模块化训练引擎，支持分布式多卡训练

**适用场景**:
- 企业级 AI 应用定制：快速将通用大模型微调为垂直领域专家（如医疗、法律、金融）
- 学术研究与算法实验：低成本验证新的大模型微调方法和 RLHF 策略
- 个人开发者快速原型开发：通过 WebUI 零代码微调小规模模型进行学习和项目验证



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,573 |
| 语言 | Python |
| Forks | 9,864 |
| Issues | 351 |
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
| Stars | 41,020 |
| 语言 | TypeScript |
| Forks | 3,026 |
| Issues | 200 |
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
| Stars | 34,978 |
| 语言 | TypeScript |
| Forks | 7,105 |
| Issues | 462 |
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
| Stars | 33,643 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
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
| Stars | 45,577 |
| 语言 | Java |
| Forks | 15,850 |
| Issues | 80 |
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
| Stars | 38,839 |
| 语言 | Python |
| Forks | 6,162 |
| Issues | 111 |
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
| Stars | 33,434 |
| 语言 | TypeScript |
| Forks | 3,624 |
| Issues | 284 |
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
| Stars | 32,704 |
| 语言 | Jupyter Notebook |
| Forks | 5,422 |
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
| Stars | 56,772 |
| 语言 | JavaScript |
| Forks | 6,136 |
| Issues | 303 |
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
| Stars | 69,833 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 350 |
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
| Stars | 58,321 |
| 语言 | Python |
| Forks | 4,918 |
| Issues | 1,032 |
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
| Stars | 43,804 |
| 语言 | TypeScript |
| Forks | 3,247 |
| Issues | 374 |
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
| Stars | 84,593 |
| 语言 | Python |
| Forks | 9,794 |
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
| Stars | 51,120 |
| 语言 | TypeScript |
| Forks | 23,983 |
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
| Stars | 181,217 |
| 语言 | TypeScript |
| Forks | 56,207 |
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
| Stars | 146,272 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 918 |
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
| Stars | 55,070 |
| 语言 | Jupyter Notebook |
| Forks | 19,029 |
| Issues | 10 |
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
| Stars | 72,294 |
| 语言 | MDX |
| Forks | 7,722 |
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
| Stars | 39,678 |
| 语言 | TypeScript |
| Forks | 6,197 |
| Issues | 79 |
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
| Stars | 103,668 |
| 语言 | Python |
| Forks | 15,129 |
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
| Stars | 33,907 |
| 语言 | Rust |
| Forks | 2,032 |
| Issues | 444 |
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
| Stars | 128,835 |
| 语言 | Python |
| Forks | 18,220 |
| Issues | 261 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最完整的开源 LLM Web 界面解决方案，12.9万 Stars 证明了其社区认可度。它同时支持 Ollama 和 OpenAI API 等多种后端，提供了开箱即用的 RAG 检索增强和 MCP 协议扩展能力，让用户能够零成本搭建功能完整的私有 AI 对话平台。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型、OpenAI API、Azure OpenAI 等多种 LLM 服务提供方，灵活性极高
- RAG 检索增强：内置文档解析和向量检索能力，支持上传 PDF、Word、Markdown 等文件进行问答
- MCP 协议集成：支持 Model Context Protocol，可扩展连接各类外部工具和数据源
- 自托管部署：提供 Docker 一键部署方案，数据完全私有，适合对数据安全有要求的企业
- 现代化 Web UI：响应式设计，支持主题定制、对话管理、模型参数调节等功能

**适用场景**:
- 企业私有 AI 助手：部署在企业内部网络中，为员工提供文档问答、知识检索、会议纪要生成等场景的 AI 服务，数据不出内网
- 个人开发者本地 LLM 开发：配合 Ollama 在本地运行开源大模型（如 Llama、Qwen、Mistral），进行 Prompt 工程调试和 AI 应用原型开发
- 知识库智能问答系统：上传产品文档、技术手册、内部 wiki 等资料，构建基于自有知识的 RAG 问答机器人



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,264 |
| 语言 | Python |
| Forks | 8,535 |
| Issues | 3,166 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个功能完备、社区活跃（76k+ stars）的开源 RAG 引擎，通过融合 RAG 与 Agent 能力为 LLM 提供高质量的上下文检索层，特别适合构建企业级智能知识库和复杂文档问答系统。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能 Agent 能力深度结合，实现自主推理和多步查询优化
- 多模态文档解析引擎：内置专业文档解析器，支持复杂结构化文档的智能理解和向量化
- 混合检索能力：支持传统向量检索与 GraphRAG 图检索的融合，提升关系型知识检索效果
- 广泛 LLM 支持：兼容 OpenAI、Ollama、DeepSeek 等多种大模型，提供灵活的模型接入方案
- MCP 协议支持：集成 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业知识库智能问答：构建私有化知识库问答系统，支持复杂文档检索和多轮对话
- 深度研究助手：基于 GraphRAG 和 Agent 能力，实现跨文档关系推理和深度研究分析
- 智能文档处理平台：自动解析理解复杂技术文档、合同、报告等，实现精准信息提取
- RAG 应用开发框架：为开发者提供完整的 RAG 技术栈，快速搭建各类智能问答和检索应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,357 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 668 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟度极高的 AI Agent 平台（74K+ Stars），支持多模型集成与多 Agent 协作编排，为开发者和企业提供了开箱即用的 Agent 团队构建能力，是当前 AI Agent 领域最具参考价值的开源项目之一。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的模型调用接口
- 多 Agent 协作引擎：实现 Agent 间通信与任务协作，支持复杂工作流的自动化编排
- 知识库增强系统：内置知识库管理能力，支持 RAG 检索增强，提升 Agent 回答准确性
- MCP 协议支持：遵循 Model Context Protocol 标准，可扩展连接外部工具和服务生态
- TypeScript 全栈架构：基于现代化的前端框架，具备良好的类型安全和可维护性

**适用场景**:
- 企业级智能助手搭建：利用多 Agent 协作能力构建客服、文档助手、数据分析等多种角色的智能团队
- 个人开发者 AI 工作流：通过 Agent 编排实现自动化编程、代码审查、日程管理等效率工具
- 知识密集型应用开发：结合知识库功能开发智能问答、文档检索、培训助手等专业场景应用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,020 |
| 语言 | TypeScript |
| Forks | 3,026 |
| Issues | 200 |
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
| Stars | 33,643 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
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
| Stars | 45,577 |
| 语言 | Java |
| Forks | 15,850 |
| Issues | 80 |
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
| Stars | 38,839 |
| 语言 | Python |
| Forks | 6,162 |
| Issues | 111 |
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
| Stars | 33,434 |
| 语言 | TypeScript |
| Forks | 3,624 |
| Issues | 284 |
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
| Stars | 32,704 |
| 语言 | Jupyter Notebook |
| Forks | 5,422 |
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
| Stars | 99,676 |
| 语言 | TypeScript |
| Forks | 11,892 |
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
| Stars | 56,772 |
| 语言 | JavaScript |
| Forks | 6,136 |
| Issues | 303 |
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
| Stars | 51,120 |
| 语言 | TypeScript |
| Forks | 23,983 |
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
| Stars | 73,120 |
| 语言 | Python |
| Forks | 10,035 |
| Issues | 262 |
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
| Stars | 43,490 |
| 语言 | Go |
| Forks | 3,914 |
| Issues | 1,098 |
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
| Stars | 31,795 |
| 语言 | Python |
| Forks | 3,349 |
| Issues | 85 |
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
| Stars | 72,294 |
| 语言 | MDX |
| Forks | 7,722 |
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
| Stars | 103,668 |
| 语言 | Python |
| Forks | 15,129 |
| Issues | 5 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


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
| Stars | 128,835 |
| 语言 | Python |
| Forks | 18,220 |
| Issues | 261 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最完整的开源 LLM Web 界面解决方案，12.9万 Stars 证明了其社区认可度。它同时支持 Ollama 和 OpenAI API 等多种后端，提供了开箱即用的 RAG 检索增强和 MCP 协议扩展能力，让用户能够零成本搭建功能完整的私有 AI 对话平台。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型、OpenAI API、Azure OpenAI 等多种 LLM 服务提供方，灵活性极高
- RAG 检索增强：内置文档解析和向量检索能力，支持上传 PDF、Word、Markdown 等文件进行问答
- MCP 协议集成：支持 Model Context Protocol，可扩展连接各类外部工具和数据源
- 自托管部署：提供 Docker 一键部署方案，数据完全私有，适合对数据安全有要求的企业
- 现代化 Web UI：响应式设计，支持主题定制、对话管理、模型参数调节等功能

**适用场景**:
- 企业私有 AI 助手：部署在企业内部网络中，为员工提供文档问答、知识检索、会议纪要生成等场景的 AI 服务，数据不出内网
- 个人开发者本地 LLM 开发：配合 Ollama 在本地运行开源大模型（如 Llama、Qwen、Mistral），进行 Prompt 工程调试和 AI 应用原型开发
- 知识库智能问答系统：上传产品文档、技术手册、内部 wiki 等资料，构建基于自有知识的 RAG 问答机器人



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,264 |
| 语言 | Python |
| Forks | 8,535 |
| Issues | 3,166 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个功能完备、社区活跃（76k+ stars）的开源 RAG 引擎，通过融合 RAG 与 Agent 能力为 LLM 提供高质量的上下文检索层，特别适合构建企业级智能知识库和复杂文档问答系统。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能 Agent 能力深度结合，实现自主推理和多步查询优化
- 多模态文档解析引擎：内置专业文档解析器，支持复杂结构化文档的智能理解和向量化
- 混合检索能力：支持传统向量检索与 GraphRAG 图检索的融合，提升关系型知识检索效果
- 广泛 LLM 支持：兼容 OpenAI、Ollama、DeepSeek 等多种大模型，提供灵活的模型接入方案
- MCP 协议支持：集成 Model Context Protocol，便于与外部工具和服务进行标准化集成

**适用场景**:
- 企业知识库智能问答：构建私有化知识库问答系统，支持复杂文档检索和多轮对话
- 深度研究助手：基于 GraphRAG 和 Agent 能力，实现跨文档关系推理和深度研究分析
- 智能文档处理平台：自动解析理解复杂技术文档、合同、报告等，实现精准信息提取
- RAG 应用开发框架：为开发者提供完整的 RAG 技术栈，快速搭建各类智能问答和检索应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,027 |
| 语言 | JavaScript |
| Forks | 14,357 |
| Issues | 139 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编码助手设计的综合性能优化框架，支持多种主流 AI 编程工具（Claude Code、Cursor、Codex等），通过模块化的 Skills/Instincts/Memory 机制显著提升 AI Agent 的任务完成效率和智能化水平，11万 Stars 的高热度证明了其在 AI 开发工具领域的广泛认可和实用价值。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供跨平台的开发体验
- 模块化 Skills 系统：通过可扩展的技能模块增强 Agent 能力，支持自定义功能扩展
- 本能机制（Instincts）：内置智能响应模式，让 AI Agent 具备更接近人类开发者的直觉判断能力
- 记忆管理系统：提供持久化上下文记忆功能，解决长对话场景下的信息丢失问题
- 安全与隐私保护：内置安全机制，确保 AI 辅助开发过程中的代码安全和数据隐私

**适用场景**:
- AI 辅助编程效率优化：为开发团队提供统一的 AI 编码助手配置和优化方案，提升整体开发效率
- 构建企业级 AI 开发工作流：基于 MCP 协议集成多种 AI 工具，打造企业专属的智能开发平台
- 个人开发者效率提升：通过 Skills 和记忆功能，让 AI 助手更好地理解项目上下文，减少重复沟通成本



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,357 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 668 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟度极高的 AI Agent 平台（74K+ Stars），支持多模型集成与多 Agent 协作编排，为开发者和企业提供了开箱即用的 Agent 团队构建能力，是当前 AI Agent 领域最具参考价值的开源项目之一。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的模型调用接口
- 多 Agent 协作引擎：实现 Agent 间通信与任务协作，支持复杂工作流的自动化编排
- 知识库增强系统：内置知识库管理能力，支持 RAG 检索增强，提升 Agent 回答准确性
- MCP 协议支持：遵循 Model Context Protocol 标准，可扩展连接外部工具和服务生态
- TypeScript 全栈架构：基于现代化的前端框架，具备良好的类型安全和可维护性

**适用场景**:
- 企业级智能助手搭建：利用多 Agent 协作能力构建客服、文档助手、数据分析等多种角色的智能团队
- 个人开发者 AI 工作流：通过 Agent 编排实现自动化编程、代码审查、日程管理等效率工具
- 知识密集型应用开发：结合知识库功能开发智能问答、文档检索、培训助手等专业场景应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,333 |
| 语言 | HTML |
| Forks | 20,276 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最受欢迎的 AI 提示词开源社区项目，拥有超过 15 万 Stars，提供超过 500+ 精选提示词，支持 ChatGPT、Claude、Gemini 等多平台，且可完全私有化部署，是个人和团队提升 AI 使用效率的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的开源代码和可扩展架构
- 支持多平台 LLM 集成：ChatGPT、Claude、Gemini、GPT-4 等主流模型
- 采用 Creative Commons Zero (CC0) 许可证，完全无版权限制可商用
- 提供一键复制提示词功能，支持快速导入到各类 AI 助手
- 社区驱动模式，持续更新高质量提示词，涵盖写作、编程、创意等场景

**适用场景**:
- 个人用户：快速找到高质量提示词，提升与 AI 助手的交互效率
- 企业自托管：部署私有化版本，保护商业敏感数据，符合数据合规要求
- 开发者集成：基于开源代码二次开发，构建企业内部提示词管理系统



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,289 |
| 语言 | Jupyter Notebook |
| Forks | 13,627 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 亲自维护的从零实现 GPT 类 LLM 的权威教程项目，89K+ Stars 验证了其极高的学习价值，通过纯 PyTorch 代码深入剖析 LLM 核心架构（Attention、Positional Encoding 等），而非依赖现成库的黑盒调用。

**技术亮点**:
- 纯 PyTorch 从零实现，不依赖 Hugging Face Transformers 等高层封装，深入理解底层机制
- 完整涵盖数据预处理、Tokenization、Multi-Head Self-Attention、Positional Encoding 等核心组件
- 采用 Jupyter Notebook 交互式教学，代码可即时运行和调试
- 包含完整的预训练和指令微调流程，配套书籍《Build a Large Language Model (From Scratch)》
- 代码注释详尽，配有可视化图表辅助理解复杂概念

**适用场景**:
- 系统学习 LLM 架构原理：适合 AI/ML 研究者和工程师深入理解 GPT 等模型的内部工作原理
- 教学与课程资源：适合高校/培训机构作为深度学习自然语言处理课程的实践教材
- 企业定制化 LLM 开发：帮助团队基于 PyTorch 构建和微调自有 LLM 模型



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,573 |
| 语言 | Python |
| Forks | 9,864 |
| Issues | 351 |
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
| Stars | 41,020 |
| 语言 | TypeScript |
| Forks | 3,026 |
| Issues | 200 |
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
| Stars | 34,978 |
| 语言 | TypeScript |
| Forks | 7,105 |
| Issues | 462 |
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
| Stars | 33,643 |
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
| Stars | 56,772 |
| 语言 | JavaScript |
| Forks | 6,136 |
| Issues | 303 |
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
| Stars | 69,833 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 350 |
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
| Stars | 58,321 |
| 语言 | Python |
| Forks | 4,918 |
| Issues | 1,032 |
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
| Stars | 43,804 |
| 语言 | TypeScript |
| Forks | 3,247 |
| Issues | 374 |
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
| Stars | 51,120 |
| 语言 | TypeScript |
| Forks | 23,983 |
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
| Stars | 35,056 |
| 语言 | HTML |
| Forks | 5,638 |
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
| Stars | 74,426 |
| 语言 | Python |
| Forks | 14,820 |
| Issues | 3,924 |
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
| Stars | 51,665 |
| 语言 | Python |
| Forks | 4,982 |
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
| Stars | 39,136 |
| 语言 | TypeScript |
| Forks | 3,962 |
| Issues | 1,087 |
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
| Stars | 146,272 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 918 |
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
| Stars | 166,234 |
| 语言 | Go |
| Forks | 15,181 |
| Issues | 2,734 |
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
| Stars | 72,294 |
| 语言 | MDX |
| Forks | 7,722 |
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
| Stars | 47,026 |
| 语言 | Rust |
| Forks | 9,301 |
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
| Stars | 39,678 |
| 语言 | TypeScript |
| Forks | 6,197 |
| Issues | 79 |
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
| Stars | 36,921 |
| 语言 | Python |
| Forks | 2,578 |
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
| Stars | 92,585 |
| 语言 | Python |
| Forks | 5,550 |
| Issues | 485 |
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
| Stars | 69,116 |
| 语言 | Python |
| Forks | 8,429 |
| Issues | 938 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个在 ACL 2024 发表的统一大模型微调框架，支持 100+ 主流 LLM 和 VLM 模型，集成 LoRA/QLoRA/RLHF 等多种高效微调技术，提供 WebUI 和 CLI 两种交互方式，让研究者和开发者能够零门槛快速微调大模型。

**技术亮点**:
- 支持 100+ 预训练模型统一微调，涵盖 Llama/Gemma/Qwen/DeepSeek/Mistral 等主流开源大模型
- 集成多种高效微调算法：LoRA、QLoRA、AdaLoRA、LyCORIS 等 PEFT 方法
- 支持完整的 RLHF 流程：SFT + Reward Model + PPO + DPO
- 内置 4bit/8bit 量化功能（GPTQ/AWQ/GGUF），大幅降低显存需求
- 提供可视化 WebUI 和模块化训练引擎，支持分布式多卡训练

**适用场景**:
- 企业级 AI 应用定制：快速将通用大模型微调为垂直领域专家（如医疗、法律、金融）
- 学术研究与算法实验：低成本验证新的大模型微调方法和 RLHF 策略
- 个人开发者快速原型开发：通过 WebUI 零代码微调小规模模型进行学习和项目验证



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,601 |
| 语言 | Python |
| Forks | 6,259 |
| Issues | 71 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，汇集了股票、固定收益、期权、加密货币等多类资产的数据和分析能力，并且原生支持 AI 和机器学习集成，特别适合需要快速构建量化策略和金融分析应用的开发者。

**技术亮点**:
- 覆盖多资产类别：支持股票、期权、加密货币、固定收益、衍生品等金融产品的数据获取和分析
- AI/ML 原生集成：内置机器学习支持，可用于预测模型构建和智能投顾开发
- 模块化架构设计：提供标准化的数据接口和可扩展的分析模块，便于二次开发和定制
- 丰富的量化金融工具：包含统计分析、技术指标、风险管理等专业量化分析功能
- 活跃的开源社区：6.3 万+ Stars，跨多个金融领域持续更新和维护

**适用场景**:
- 量化交易策略开发：构建基于技术指标和机器学习的量化交易系统
- 金融数据分析与研究：整合多源金融数据进行投资研究和市场分析
- AI 金融应用开发：为 AI 代理和智能投顾提供可靠的市场数据和交易接口
- 企业级金融平台搭建：基于模块化架构构建内部资产管理或风险监控系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,333 |
| 语言 | HTML |
| Forks | 20,276 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最受欢迎的 AI 提示词开源社区项目，拥有超过 15 万 Stars，提供超过 500+ 精选提示词，支持 ChatGPT、Claude、Gemini 等多平台，且可完全私有化部署，是个人和团队提升 AI 使用效率的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的开源代码和可扩展架构
- 支持多平台 LLM 集成：ChatGPT、Claude、Gemini、GPT-4 等主流模型
- 采用 Creative Commons Zero (CC0) 许可证，完全无版权限制可商用
- 提供一键复制提示词功能，支持快速导入到各类 AI 助手
- 社区驱动模式，持续更新高质量提示词，涵盖写作、编程、创意等场景

**适用场景**:
- 个人用户：快速找到高质量提示词，提升与 AI 助手的交互效率
- 企业自托管：部署私有化版本，保护商业敏感数据，符合数据合规要求
- 开发者集成：基于开源代码二次开发，构建企业内部提示词管理系统



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,289 |
| 语言 | Jupyter Notebook |
| Forks | 13,627 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka 亲自维护的从零实现 GPT 类 LLM 的权威教程项目，89K+ Stars 验证了其极高的学习价值，通过纯 PyTorch 代码深入剖析 LLM 核心架构（Attention、Positional Encoding 等），而非依赖现成库的黑盒调用。

**技术亮点**:
- 纯 PyTorch 从零实现，不依赖 Hugging Face Transformers 等高层封装，深入理解底层机制
- 完整涵盖数据预处理、Tokenization、Multi-Head Self-Attention、Positional Encoding 等核心组件
- 采用 Jupyter Notebook 交互式教学，代码可即时运行和调试
- 包含完整的预训练和指令微调流程，配套书籍《Build a Large Language Model (From Scratch)》
- 代码注释详尽，配有可视化图表辅助理解复杂概念

**适用场景**:
- 系统学习 LLM 架构原理：适合 AI/ML 研究者和工程师深入理解 GPT 等模型的内部工作原理
- 教学与课程资源：适合高校/培训机构作为深度学习自然语言处理课程的实践教材
- 企业定制化 LLM 开发：帮助团队基于 PyTorch 构建和微调自有 LLM 模型



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,434 |
| 语言 | TypeScript |
| Forks | 3,624 |
| Issues | 284 |
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
| Stars | 32,704 |
| 语言 | Jupyter Notebook |
| Forks | 5,422 |
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
| Stars | 158,448 |
| 语言 | Python |
| Forks | 32,622 |
| Issues | 2,293 |
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
| Stars | 74,426 |
| 语言 | Python |
| Forks | 14,820 |
| Issues | 3,924 |
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
| Stars | 107,042 |
| 语言 | Python |
| Forks | 12,336 |
| Issues | 3,895 |
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
| Stars | 98,599 |
| 语言 | Python |
| Forks | 27,313 |
| Issues | 18,114 |
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
| Stars | 72,294 |
| 语言 | MDX |
| Forks | 7,722 |
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
| Stars | 162,013 |
| 语言 | Python |
| Forks | 30,206 |
| Issues | 2,471 |
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
| Stars | 110,027 |
| 语言 | JavaScript |
| Forks | 14,357 |
| Issues | 139 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编码助手设计的综合性能优化框架，支持多种主流 AI 编程工具（Claude Code、Cursor、Codex等），通过模块化的 Skills/Instincts/Memory 机制显著提升 AI Agent 的任务完成效率和智能化水平，11万 Stars 的高热度证明了其在 AI 开发工具领域的广泛认可和实用价值。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供跨平台的开发体验
- 模块化 Skills 系统：通过可扩展的技能模块增强 Agent 能力，支持自定义功能扩展
- 本能机制（Instincts）：内置智能响应模式，让 AI Agent 具备更接近人类开发者的直觉判断能力
- 记忆管理系统：提供持久化上下文记忆功能，解决长对话场景下的信息丢失问题
- 安全与隐私保护：内置安全机制，确保 AI 辅助开发过程中的代码安全和数据隐私

**适用场景**:
- AI 辅助编程效率优化：为开发团队提供统一的 AI 编码助手配置和优化方案，提升整体开发效率
- 构建企业级 AI 开发工作流：基于 MCP 协议集成多种 AI 工具，打造企业专属的智能开发平台
- 个人开发者效率提升：通过 Skills 和记忆功能，让 AI 助手更好地理解项目上下文，减少重复沟通成本



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,437 |
| 语言 | Go |
| Forks | 3,797 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是唯一一款支持在任意硬件上本地运行多模态 AI 模型（LLMs、视觉、语音、图像、视频）的开源引擎，无需 GPU 即可部署，为隐私敏感场景和企业私有化 AI 提供了免费且高效的替代方案。

**技术亮点**:
- 基于 Go 语言开发，充分利用 goroutine 实现高效的并发模型推理，支持高并发 API 请求处理
- 支持 llama、mamba、stable-diffusion、musicgen、whisper 等多种主流模型架构，一站式满足文本、图像、音频、视频生成需求
- 去中心化架构设计，支持 libp2p 分布式部署，可在多节点间协同运行 AI 推理任务
- API 优先设计，提供 OpenAI 兼容的 API 接口，降低迁移成本，方便快速集成到现有系统
- MCP (Model Context Protocol) 协议支持，增强 AI Agent 能力，支持更复杂的多模态交互场景

**适用场景**:
- 企业私有化 AI 部署：在数据隐私要求严格的金融、医疗、法律等场景中，无需将敏感数据上传至第三方云服务，实现完全的本地化 AI 处理
- 开发者本地 AI 原型开发：个人开发者或团队可在没有 GPU 的开发机器上快速验证 AI 功能，加速产品迭代和原型开发
- 边缘计算与嵌入式 AI：支持在资源受限的边缘设备上部署 AI 推理能力，适用于 IoT 设备、机器人、智能终端等场景



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,833 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 350 |
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
| Stars | 43,804 |
| 语言 | TypeScript |
| Forks | 3,247 |
| Issues | 374 |
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
| Stars | 181,217 |
| 语言 | TypeScript |
| Forks | 56,207 |
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
| Stars | 153,427 |
| 语言 | Python |
| Forks | 12,444 |
| Issues | 2,408 |
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
| Stars | 96,599 |
| 语言 | Python |
| Forks | 8,942 |
| Issues | 166 |
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
| Stars | 74,101 |
| 语言 | Python |
| Forks | 8,801 |
| Issues | 203 |
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
| Stars | 183,109 |
| 语言 | TypeScript |
| Forks | 38,780 |
| Issues | 15,651 |
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
| Stars | 93,943 |
| 语言 | TypeScript |
| Forks | 9,404 |
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
| Stars | 78,636 |
| 语言 | TypeScript |
| Forks | 5,728 |
| Issues | 731 |
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
| Stars | 76,850 |
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
| Stars | 75,679 |
| 语言 | JavaScript |
| Forks | 7,268 |
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
| Stars | 79,014 |
| 语言 | Go |
| Forks | 2,737 |
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
| Stars | 75,072 |
| 语言 | Go |
| Forks | 2,640 |
| Issues | 949 |
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
| Stars | 36,921 |
| 语言 | Python |
| Forks | 2,578 |
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
| Stars | 54,736 |
| 语言 | JavaScript |
| Forks | 4,060 |
| Issues | 1,415 |
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
| Stars | 416,455 |
| 语言 | Python |
| Forks | 45,143 |
| Issues | 1,091 |
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
| Stars | 43,804 |
| 语言 | TypeScript |
| Forks | 3,247 |
| Issues | 374 |
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
| Stars | 181,217 |
| 语言 | TypeScript |
| Forks | 56,207 |
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
| Stars | 51,710 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 224 |
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
| Stars | 121,371 |
| 语言 | Go |
| Forks | 42,735 |
| Issues | 2,639 |
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
| Stars | 71,567 |
| 语言 | Go |
| Forks | 18,912 |
| Issues | 3,798 |
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
| Stars | 54,511 |
| 语言 | Go |
| Forks | 6,492 |
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
| Stars | 93,943 |
| 语言 | TypeScript |
| Forks | 9,404 |
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
| Stars | 75,818 |
| 语言 | TypeScript |
| Forks | 6,453 |
| Issues | 436 |
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
| Stars | 84,530 |
| 语言 | JavaScript |
| Forks | 7,571 |
| Issues | 710 |
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
| Stars | 69,533 |
| 语言 | Go |
| Forks | 1,889 |
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
| Stars | 62,382 |
| 语言 | Go |
| Forks | 5,889 |
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
| Stars | 58,223 |
| 语言 | Go |
| Forks | 4,211 |
| Issues | 31 |
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
| Stars | 47,603 |
| 语言 | Go |
| Forks | 5,067 |
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
| Stars | 84,530 |
| 语言 | JavaScript |
| Forks | 7,571 |
| Issues | 710 |
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
| Stars | 63,303 |
| 语言 | Go |
| Forks | 10,273 |
| Issues | 759 |
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
| Stars | 44,437 |
| 语言 | Go |
| Forks | 3,797 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是唯一一款支持在任意硬件上本地运行多模态 AI 模型（LLMs、视觉、语音、图像、视频）的开源引擎，无需 GPU 即可部署，为隐私敏感场景和企业私有化 AI 提供了免费且高效的替代方案。

**技术亮点**:
- 基于 Go 语言开发，充分利用 goroutine 实现高效的并发模型推理，支持高并发 API 请求处理
- 支持 llama、mamba、stable-diffusion、musicgen、whisper 等多种主流模型架构，一站式满足文本、图像、音频、视频生成需求
- 去中心化架构设计，支持 libp2p 分布式部署，可在多节点间协同运行 AI 推理任务
- API 优先设计，提供 OpenAI 兼容的 API 接口，降低迁移成本，方便快速集成到现有系统
- MCP (Model Context Protocol) 协议支持，增强 AI Agent 能力，支持更复杂的多模态交互场景

**适用场景**:
- 企业私有化 AI 部署：在数据隐私要求严格的金融、医疗、法律等场景中，无需将敏感数据上传至第三方云服务，实现完全的本地化 AI 处理
- 开发者本地 AI 原型开发：个人开发者或团队可在没有 GPU 的开发机器上快速验证 AI 功能，加速产品迭代和原型开发
- 边缘计算与嵌入式 AI：支持在资源受限的边缘设备上部署 AI 推理能力，适用于 IoT 设备、机器人、智能终端等场景



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,599 |
| 语言 | Python |
| Forks | 8,942 |
| Issues | 166 |
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
| Stars | 87,131 |
| 语言 | Python |
| Forks | 33,796 |
| Issues | 422 |
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
| Stars | 100,139 |
| 语言 | TypeScript |
| Forks | 27,140 |
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
| Stars | 78,636 |
| 语言 | TypeScript |
| Forks | 5,728 |
| Issues | 731 |
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
| Stars | 75,679 |
| 语言 | JavaScript |
| Forks | 7,268 |
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
| Stars | 55,950 |
| 语言 | JavaScript |
| Forks | 10,215 |
| Issues | 363 |
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
| Stars | 88,323 |
| 语言 | Go |
| Forks | 8,570 |
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
| Stars | 71,122 |
| 语言 | Go |
| Forks | 4,690 |
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
| Stars | 57,149 |
| 语言 | Go |
| Forks | 3,220 |
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
| Stars | 36,921 |
| 语言 | Python |
| Forks | 2,578 |
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
| Stars | 416,455 |
| 语言 | Python |
| Forks | 45,143 |
| Issues | 1,091 |
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
| Forks | 22,921 |
| Issues | 196 |
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
| Stars | 99,676 |
| 语言 | TypeScript |
| Forks | 11,892 |
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
| Stars | 56,772 |
| 语言 | JavaScript |
| Forks | 6,136 |
| Issues | 303 |
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
| Stars | 43,490 |
| 语言 | Go |
| Forks | 3,914 |
| Issues | 1,098 |
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
| Stars | 51,710 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 224 |
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
| Stars | 154,333 |
| 语言 | HTML |
| Forks | 20,276 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最受欢迎的 AI 提示词开源社区项目，拥有超过 15 万 Stars，提供超过 500+ 精选提示词，支持 ChatGPT、Claude、Gemini 等多平台，且可完全私有化部署，是个人和团队提升 AI 使用效率的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的开源代码和可扩展架构
- 支持多平台 LLM 集成：ChatGPT、Claude、Gemini、GPT-4 等主流模型
- 采用 Creative Commons Zero (CC0) 许可证，完全无版权限制可商用
- 提供一键复制提示词功能，支持快速导入到各类 AI 助手
- 社区驱动模式，持续更新高质量提示词，涵盖写作、编程、创意等场景

**适用场景**:
- 个人用户：快速找到高质量提示词，提升与 AI 助手的交互效率
- 企业自托管：部署私有化版本，保护商业敏感数据，符合数据合规要求
- 开发者集成：基于开源代码二次开发，构建企业内部提示词管理系统



### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,056 |
| 语言 | HTML |
| Forks | 5,638 |
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
| Stars | 72,294 |
| 语言 | MDX |
| Forks | 7,722 |
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
| Stars | 39,678 |
| 语言 | TypeScript |
| Forks | 6,197 |
| Issues | 79 |
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
| Stars | 89,529 |
| 语言 | TypeScript |
| Forks | 9,953 |
| Issues | 2,214 |
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
| Stars | 86,935 |
| 语言 | TypeScript |
| Forks | 8,773 |
| Issues | 1,622 |
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
| Stars | 127,229 |
| 语言 | JavaScript |
| Forks | 12,462 |
| Issues | 5 |
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
| Stars | 100,934 |
| 语言 | JavaScript |
| Forks | 7,535 |
| Issues | 234 |
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
| Stars | 168,336 |
| 语言 | Go |
| Forks | 13,096 |
| Issues | 171 |
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
| Stars | 62,656 |
| 语言 | Python |
| Forks | 6,394 |
| Issues | 38 |
| 许可证 | Apache License 2.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,598 |
| 语言 | Python |
| Forks | 7,057 |
| Issues | 633 |
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
| Stars | 80,634 |
| 语言 | Python |
| Forks | 11,772 |
| Issues | 102 |
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
| Stars | 133,344 |
| 语言 | Unknown |
| Forks | 33,646 |
| Issues | 140 |
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
| Stars | 384,616 |
| 语言 | Python |
| Forks | 66,063 |
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
| Stars | 113,896 |
| 语言 | TypeScript |
| Forks | 5,811 |
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
| Stars | 105,623 |
| 语言 | TypeScript |
| Forks | 7,675 |
| Issues | 205 |
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
| Forks | 10,258 |
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
| Stars | 99,466 |
| 语言 | C++ |
| Forks | 15,848 |
| Issues | 1,296 |
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
| Stars | 62,715 |
| 语言 | Python |
| Forks | 1,626 |
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
| Stars | 49,502 |
| 语言 | TypeScript |
| Forks | 6,294 |
| Issues | 204 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,519 |
| 语言 | JavaScript |
| Forks | 3,440 |
| Issues | 23 |
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
| Stars | 340,312 |
| 语言 | Python |
| Forks | 55,047 |
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
| Stars | 289,145 |
| 语言 | Python |
| Forks | 27,486 |
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
| Stars | 219,076 |
| 语言 | Python |
| Forks | 50,250 |
| Issues | 894 |
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
| Stars | 85,857 |
| 语言 | Python |
| Forks | 37,089 |
| Issues | 3,459 |
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
| Stars | 85,557 |
| 语言 | Python |
| Forks | 7,187 |
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
| Forks | 45,201 |
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
| Stars | 438,867 |
| 语言 | TypeScript |
| Forks | 43,786 |
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
| Stars | 351,718 |
| 语言 | TypeScript |
| Forks | 43,870 |
| Issues | 33 |
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
| Stars | 138,384 |
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
| Stars | 119,624 |
| 语言 | TypeScript |
| Forks | 13,013 |
| Issues | 2,884 |
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
| Stars | 110,802 |
| 语言 | TypeScript |
| Forks | 8,317 |
| Issues | 1,790 |
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
| Stars | 108,302 |
| 语言 | TypeScript |
| Forks | 13,306 |
| Issues | 5,000 |
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
| Stars | 97,779 |
| 语言 | TypeScript |
| Forks | 54,569 |
| Issues | 1,356 |
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
| Stars | 95,761 |
| 语言 | TypeScript |
| Forks | 5,185 |
| Issues | 657 |
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
| Stars | 94,196 |
| 语言 | TypeScript |
| Forks | 5,129 |
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
| Forks | 7,581 |
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
| Stars | 82,197 |
| 语言 | TypeScript |
| Forks | 10,086 |
| Issues | 601 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,378 |
| 语言 | TypeScript |
| Forks | 7,966 |
| Issues | 681 |
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
| Stars | 244,222 |
| 语言 | JavaScript |
| Forks | 50,861 |
| Issues | 1,181 |
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
| Stars | 116,447 |
| 语言 | JavaScript |
| Forks | 35,174 |
| Issues | 2,576 |
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
| Stars | 111,580 |
| 语言 | JavaScript |
| Forks | 36,316 |
| Issues | 583 |
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
| Stars | 108,649 |
| 语言 | JavaScript |
| Forks | 11,564 |
| Issues | 357 |
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
| Stars | 98,035 |
| 语言 | JavaScript |
| Forks | 32,690 |
| Issues | 1,717 |
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
| Stars | 95,471 |
| 语言 | JavaScript |
| Forks | 15,299 |
| Issues | 53 |
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
| Stars | 86,140 |
| 语言 | JavaScript |
| Forks | 4,832 |
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
| Stars | 78,889 |
| 语言 | JavaScript |
| Forks | 31,628 |
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
| Stars | 70,863 |
| 语言 | JavaScript |
| Forks | 16,811 |
| Issues | 889 |
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
| Stars | 66,294 |
| 语言 | JavaScript |
| Forks | 9,191 |
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
| Stars | 66,014 |
| 语言 | JavaScript |
| Forks | 9,351 |
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
| Stars | 62,326 |
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
| Stars | 61,575 |
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
| Stars | 60,058 |
| 语言 | JavaScript |
| Forks | 5,630 |
| Issues | 66 |
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
| Stars | 59,871 |
| 语言 | JavaScript |
| Forks | 20,474 |
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
| Stars | 57,411 |
| 语言 | JavaScript |
| Forks | 12,301 |
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
| Stars | 53,038 |
| 语言 | JavaScript |
| Forks | 10,607 |
| Issues | 472 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,153 |
| 语言 | JavaScript |
| Forks | 11,393 |
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
| Stars | 133,182 |
| 语言 | Go |
| Forks | 18,883 |
| Issues | 9,888 |
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
| Stars | 105,620 |
| 语言 | Go |
| Forks | 14,963 |
| Issues | 51 |
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
| Stars | 87,301 |
| 语言 | Go |
| Forks | 8,224 |
| Issues | 257 |
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
| Stars | 81,162 |
| 语言 | Go |
| Forks | 4,973 |
| Issues | 410 |
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
| Stars | 68,667 |
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
| Stars | 56,278 |
| 语言 | Go |
| Forks | 4,994 |
| Issues | 1,156 |
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
| Stars | 50,955 |
| 语言 | Go |
| Forks | 21,883 |
| Issues | 384 |
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
| Stars | 49,225 |
| 语言 | Go |
| Forks | 7,968 |
| Issues | 558 |
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
| Stars | 63,201 |
| 语言 | Shell |
| Forks | 9,504 |
| Issues | 113 |
| 许可证 | MIT License |


### ⭐ 中优先级


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,379 |
| 语言 | Python |
| Forks | 16,792 |
| Issues | 20 |
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
| Stars | 148,112 |
| 语言 | JavaScript |
| Forks | 26,752 |
| Issues | 190 |
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
| Stars | 67,307 |
| 语言 | JavaScript |
| Forks | 11,970 |
| Issues | 539 |
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
| Stars | 50,391 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 265 |
| 许可证 | MIT License |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,979 |
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
| Stars | 45,679 |
| 语言 | Go |
| Forks | 3,777 |
| Issues | 82 |
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
| Stars | 147,545 |
| 语言 | Python |
| Forks | 11,262 |
| Issues | 310 |
| Topics | awesome, github, hellogithub, python |
