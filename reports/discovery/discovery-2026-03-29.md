# 项目发现报告 (2026-03-29)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 132 |
| 去重移除 | 29 |
| 已在监控 | 26 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 17 |
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
| Stars | 129,176 |
| 语言 | Python |
| Forks | 18,282 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最成熟的开源 LLM Web 界面之一，支持 Ollama、OpenAI API 等多种后端，12.9 万星标验证了其稳定性和社区认可度，特别适合需要完全掌控数据和隐私的企业级自托管部署。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，统一接口访问不同模型
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，便于扩展和第三方集成
- 现代化 Web UI：响应式设计，支持实时流式输出、对话管理、模型切换等交互功能
- 完全自托管：Docker 一键部署，数据完全本地存储，满足隐私合规需求

**适用场景**:
- 企业自托管 AI 助手：部署私有 LLM 服务，支持敏感数据处理，满足金融、医疗等行业的合规要求
- 个人开发者 AI 工具链：快速搭建本地 AI 开发环境，集成到现有工作流中
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,514 |
| 语言 | Python |
| Forks | 8,573 |
| Issues | 3,180 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档智能解析和多模态检索，配合 MCP 协议和 GraphRAG 能力，为企业级知识库问答和深度研究场景提供了端到端的解决方案。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel 等多格式复杂文档的智能解析和结构化提取，能够处理表格、图表等非结构化内容
- RAG + Agent 融合架构：不仅实现精准检索，还通过 Agent 能力进行多步推理和工具调用，实现动态问答和任务执行
- 多 LLM 和多模态支持：兼容 OpenAI、DeepSeek、Ollama 等主流模型，支持 GraphRAG 和上下文工程，实现更精准的知识检索
- MCP (Model Context Protocol) 协议支持：标准化了模型与外部工具/数据的交互，便于扩展和企业集成
- 可视化配置与调优：提供友好的 Web 界面，支持检索策略、召回参数和模型配置的可视化调整

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档问答等场景
- 深度研究与数据分析：利用 GraphRAG 和 Agent 能力进行多源文档关联分析，支持深度研究场景
- 智能文档处理流水线：自动解析结构化/非结构化文档，提取关键信息并生成摘要，适用于法务、财务等领域



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,415 |
| 语言 | TypeScript |
| Forks | 6,693 |
| Issues | 241 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据提取工具，能将任意网站高质量转换为 LLM-ready 的 markdown 或结构化数据，拥有超过 10 万星的高人气和活跃社区，是构建 AI 数据管道的首选方案。

**技术亮点**:
- AI 智能内容识别：内置智能算法自动识别网页主体内容，过滤导航栏、广告等噪音元素
- HTML 转 Markdown 高保真转换：专业的内容提取引擎保留文本结构、代码块等关键信息
- 支持整站爬取：通过智能链接发现和深度爬取实现全站数据采集
- 多格式输出：同时支持 markdown 纯文本和结构化 JSON 数据格式
- TypeScript/Node.js 原生支持：提供完善的类型定义和 SDK，方便集成到现代 AI 应用架构

**适用场景**:
- RAG 应用数据准备：为检索增强生成系统快速构建高质量的网页知识库，支持私有化部署确保数据安全
- AI 搜索与问答系统：爬取特定领域网站构建垂直搜索索引，为 AI 搜索提供实时数据源
- 市场情报与竞品监控：自动化采集新闻、产品页面等结构化信息，用于商业分析和竞品追踪



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,270 |
| 语言 | JavaScript |
| Forks | 15,125 |
| Issues | 105 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 编程代理性能优化框架之一，通过 Skills、Memory、Security 等多维度增强显著提升 Claude Code 等 AI 编程助手的效果。116k+ Stars 的社区认可度证明了其在实际开发中的有效性。

**技术亮点**:
- 多智能体框架支持：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供一致的性能优化接口
- 模块化架构设计：采用 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等解耦模块，便于扩展和定制
- 研究驱动的开发模式：强调 Research-First 理念，将学术研究成果快速转化为实用功能
- MCP 协议集成：支持 Model Context Protocol，提供标准化的上下文管理和工具调用能力
- 安全防护机制：内置安全审计和防护功能，确保 AI 代理操作的可靠性和安全性

**适用场景**:
- 企业级 AI 辅助开发：团队可基于此框架构建统一的 AI 编程规范和安全策略，提升整体开发效率
- 个人开发者效率提升：通过配置 Skills 和 Memory 模块，让 AI 助手更好地理解项目上下文和个人编码风格
- AI 代理研究与实验：研究者可在此框架基础上快速原型验证新的 AI Agent 技术方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,562 |
| 语言 | Go |
| Forks | 3,818 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的本地化 AI 推理解决方案，支持文本、图像、语音、视频等多模态模型的无 GPU 运行，特别适合需要数据隐私保护、成本敏感或需要离线部署 AI 能力的开发者和企业。

**技术亮点**:
- 多模态统一推理：支持 LLM、图像生成、语音合成、目标检测等多种模型类型，通过统一 API 提供服务
- 硬件无关性：无需 GPU 即可运行主流 AI 模型，支持 CPU 推理，大幅降低部署门槛
- 去中心化架构：集成 libp2p 实现分布式部署能力，支持 P2P 网络中的模型共享与协作
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型生态

**适用场景**:
- 企业私有 AI 部署：在本地环境运行 AI 服务，满足数据安全合规要求，适合金融、医疗、政府等对数据隐私要求严格的场景
- 开发者本地 AI 开发：无需云服务费用即可进行 AI 应用原型开发和测试，支持快速迭代
- 边缘计算与离线场景：在没有稳定网络或无法访问云服务的环境中提供 AI 能力支持



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,475 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 691 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多模型（OpenAI、Claude、Gemini、DeepSeek）和 MCP 协议，具备多 Agent 协作能力，拥有 7.4 万+ Stars 的活跃社区，是构建、测试和部署 AI Agent 解决方案的最佳选择。

**技术亮点**:
- 多模型集成：无缝支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型，提供统一的 Agent 开发体验
- MCP (Model Context Protocol) 协议支持：标准化的工具调用和上下文管理框架，便于扩展和集成第三方服务
- 多 Agent 协作框架：支持设计和管理 Agent 团队，实现复杂任务的多 Agent 协同工作流
- 知识库集成：内置 RAG 能力，支持向量检索和知识管理，增强 Agent 的领域知识
- TypeScript/现代前端架构：基于 React 和 TypeScript 构建，提供良好的开发体验和类型安全

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 协作框架构建复杂的业务流程自动化系统，如客户服务 agent 团队
- AI Agent 研究与原型开发：开发者可快速构建和测试 Agent 概念，验证多模型组合的效果
- 个人 AI 助手搭建：利用知识库集成功能构建个人知识管理和问答系统，支持多模型切换



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,210 |
| 语言 | Python |
| Forks | 8,432 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的大模型微调平台，支持100+种LLM和VLM模型，集成LORA、QLORA、RLHF等主流微调技术，提供了开箱即用的WebUI和CLI界面，让研究者和开发者能够高效便捷地对大模型进行指令微调和领域适配，大幅降低了LLM微调的门槛。

**技术亮点**:
- 统一支持100+大语言模型和视觉语言模型，包括LLaMA、LLaMA3、Qwen、DeepSeek、Gemma等主流架构
- 集成多种高效微调技术：LORA、QLORA、Prefix Tuning、Prompt Tuning、Loatham等PEFT方法
- 支持完整的RLHF训练流程，包括PPO、DPO、KTO等强化学习对齐算法
- 提供WebUI可视化界面和CLI命令行工具，支持一键启动训练，降低使用门槛
- 支持模型量化（AWQ、GPTQ）、分布式训练和多硬件平台适配

**适用场景**:
- 企业场景：利用私有数据对开源大模型进行领域微调，构建专属AI助手或行业垂直应用
- 学术研究：快速实验不同微调方法在大模型上的效果，支持对比实验和消融研究
- 个人开发者：基于预训练模型进行指令微调，打造个性化的本地AI应用或聊天机器人



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,626 |
| 语言 | Python |
| Forks | 9,861 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,576 |
| 语言 | TypeScript |
| Forks | 6,566 |
| Issues | 23 |
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
| Stars | 42,391 |
| 语言 | TypeScript |
| Forks | 3,168 |
| Issues | 201 |
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
| Stars | 35,044 |
| 语言 | TypeScript |
| Forks | 7,118 |
| Issues | 470 |
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
| Stars | 45,611 |
| 语言 | Java |
| Forks | 15,856 |
| Issues | 83 |
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
| Stars | 38,865 |
| 语言 | Python |
| Forks | 6,169 |
| Issues | 111 |
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
| Stars | 33,677 |
| 语言 | Python |
| Forks | 2,088 |
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
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 3,630 |
| Issues | 283 |
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
| Stars | 32,896 |
| 语言 | Jupyter Notebook |
| Forks | 5,446 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,844 |
| 语言 | Python |
| Forks | 3,605 |
| Issues | 73 |
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
| Stars | 103,936 |
| 语言 | Python |
| Forks | 15,167 |
| Issues | 2 |
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
| Stars | 57,074 |
| 语言 | JavaScript |
| Forks | 6,172 |
| Issues | 305 |
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
| Stars | 70,113 |
| 语言 | Python |
| Forks | 8,782 |
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
| Stars | 44,625 |
| 语言 | TypeScript |
| Forks | 3,328 |
| Issues | 360 |
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
| Stars | 84,929 |
| 语言 | Python |
| Forks | 9,832 |
| Issues | 207 |
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
| Stars | 51,223 |
| 语言 | TypeScript |
| Forks | 23,999 |
| Issues | 829 |
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
| Stars | 181,607 |
| 语言 | TypeScript |
| Forks | 56,279 |
| Issues | 1,435 |
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
| Stars | 146,381 |
| 语言 | Python |
| Forks | 8,666 |
| Issues | 940 |
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
| Stars | 72,429 |
| 语言 | MDX |
| Forks | 7,755 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,117 |
| 语言 | Rust |
| Forks | 2,095 |
| Issues | 463 |
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
| Stars | 55,312 |
| 语言 | Jupyter Notebook |
| Forks | 19,106 |
| Issues | 14 |
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
| Stars | 129,176 |
| 语言 | Python |
| Forks | 18,282 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最成熟的开源 LLM Web 界面之一，支持 Ollama、OpenAI API 等多种后端，12.9 万星标验证了其稳定性和社区认可度，特别适合需要完全掌控数据和隐私的企业级自托管部署。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，统一接口访问不同模型
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，便于扩展和第三方集成
- 现代化 Web UI：响应式设计，支持实时流式输出、对话管理、模型切换等交互功能
- 完全自托管：Docker 一键部署，数据完全本地存储，满足隐私合规需求

**适用场景**:
- 企业自托管 AI 助手：部署私有 LLM 服务，支持敏感数据处理，满足金融、医疗等行业的合规要求
- 个人开发者 AI 工具链：快速搭建本地 AI 开发环境，集成到现有工作流中
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,514 |
| 语言 | Python |
| Forks | 8,573 |
| Issues | 3,180 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档智能解析和多模态检索，配合 MCP 协议和 GraphRAG 能力，为企业级知识库问答和深度研究场景提供了端到端的解决方案。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel 等多格式复杂文档的智能解析和结构化提取，能够处理表格、图表等非结构化内容
- RAG + Agent 融合架构：不仅实现精准检索，还通过 Agent 能力进行多步推理和工具调用，实现动态问答和任务执行
- 多 LLM 和多模态支持：兼容 OpenAI、DeepSeek、Ollama 等主流模型，支持 GraphRAG 和上下文工程，实现更精准的知识检索
- MCP (Model Context Protocol) 协议支持：标准化了模型与外部工具/数据的交互，便于扩展和企业集成
- 可视化配置与调优：提供友好的 Web 界面，支持检索策略、召回参数和模型配置的可视化调整

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档问答等场景
- 深度研究与数据分析：利用 GraphRAG 和 Agent 能力进行多源文档关联分析，支持深度研究场景
- 智能文档处理流水线：自动解析结构化/非结构化文档，提取关键信息并生成摘要，适用于法务、财务等领域



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,475 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 691 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多模型（OpenAI、Claude、Gemini、DeepSeek）和 MCP 协议，具备多 Agent 协作能力，拥有 7.4 万+ Stars 的活跃社区，是构建、测试和部署 AI Agent 解决方案的最佳选择。

**技术亮点**:
- 多模型集成：无缝支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型，提供统一的 Agent 开发体验
- MCP (Model Context Protocol) 协议支持：标准化的工具调用和上下文管理框架，便于扩展和集成第三方服务
- 多 Agent 协作框架：支持设计和管理 Agent 团队，实现复杂任务的多 Agent 协同工作流
- 知识库集成：内置 RAG 能力，支持向量检索和知识管理，增强 Agent 的领域知识
- TypeScript/现代前端架构：基于 React 和 TypeScript 构建，提供良好的开发体验和类型安全

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 协作框架构建复杂的业务流程自动化系统，如客户服务 agent 团队
- AI Agent 研究与原型开发：开发者可快速构建和测试 Agent 概念，验证多模型组合的效果
- 个人 AI 助手搭建：利用知识库集成功能构建个人知识管理和问答系统，支持多模型切换



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,391 |
| 语言 | TypeScript |
| Forks | 3,168 |
| Issues | 201 |
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
| Stars | 45,611 |
| 语言 | Java |
| Forks | 15,856 |
| Issues | 83 |
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
| Stars | 38,865 |
| 语言 | Python |
| Forks | 6,169 |
| Issues | 111 |
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
| Stars | 33,677 |
| 语言 | Python |
| Forks | 2,088 |
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
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 3,630 |
| Issues | 283 |
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
| Stars | 32,896 |
| 语言 | Jupyter Notebook |
| Forks | 5,446 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,844 |
| 语言 | Python |
| Forks | 3,605 |
| Issues | 73 |
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
| Stars | 103,936 |
| 语言 | Python |
| Forks | 15,167 |
| Issues | 2 |
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
| Stars | 99,794 |
| 语言 | TypeScript |
| Forks | 11,920 |
| Issues | 995 |
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
| Stars | 57,074 |
| 语言 | JavaScript |
| Forks | 6,172 |
| Issues | 305 |
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
| Stars | 51,223 |
| 语言 | TypeScript |
| Forks | 23,999 |
| Issues | 829 |
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
| Stars | 73,272 |
| 语言 | Python |
| Forks | 10,044 |
| Issues | 261 |
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
| Stars | 43,487 |
| 语言 | Go |
| Forks | 3,919 |
| Issues | 1,095 |
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
| Stars | 72,429 |
| 语言 | MDX |
| Forks | 7,755 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
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
| Stars | 129,176 |
| 语言 | Python |
| Forks | 18,282 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最成熟的开源 LLM Web 界面之一，支持 Ollama、OpenAI API 等多种后端，12.9 万星标验证了其稳定性和社区认可度，特别适合需要完全掌控数据和隐私的企业级自托管部署。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，统一接口访问不同模型
- RAG 支持：内置检索增强生成功能，可连接外部知识库提升回答质量
- MCP 协议集成：支持 Model Context Protocol，便于扩展和第三方集成
- 现代化 Web UI：响应式设计，支持实时流式输出、对话管理、模型切换等交互功能
- 完全自托管：Docker 一键部署，数据完全本地存储，满足隐私合规需求

**适用场景**:
- 企业自托管 AI 助手：部署私有 LLM 服务，支持敏感数据处理，满足金融、医疗等行业的合规要求
- 个人开发者 AI 工具链：快速搭建本地 AI 开发环境，集成到现有工作流中
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,514 |
| 语言 | Python |
| Forks | 8,573 |
| Issues | 3,180 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档智能解析和多模态检索，配合 MCP 协议和 GraphRAG 能力，为企业级知识库问答和深度研究场景提供了端到端的解决方案。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel 等多格式复杂文档的智能解析和结构化提取，能够处理表格、图表等非结构化内容
- RAG + Agent 融合架构：不仅实现精准检索，还通过 Agent 能力进行多步推理和工具调用，实现动态问答和任务执行
- 多 LLM 和多模态支持：兼容 OpenAI、DeepSeek、Ollama 等主流模型，支持 GraphRAG 和上下文工程，实现更精准的知识检索
- MCP (Model Context Protocol) 协议支持：标准化了模型与外部工具/数据的交互，便于扩展和企业集成
- 可视化配置与调优：提供友好的 Web 界面，支持检索策略、召回参数和模型配置的可视化调整

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档问答等场景
- 深度研究与数据分析：利用 GraphRAG 和 Agent 能力进行多源文档关联分析，支持深度研究场景
- 智能文档处理流水线：自动解析结构化/非结构化文档，提取关键信息并生成摘要，适用于法务、财务等领域



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,270 |
| 语言 | JavaScript |
| Forks | 15,125 |
| Issues | 105 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 编程代理性能优化框架之一，通过 Skills、Memory、Security 等多维度增强显著提升 Claude Code 等 AI 编程助手的效果。116k+ Stars 的社区认可度证明了其在实际开发中的有效性。

**技术亮点**:
- 多智能体框架支持：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供一致的性能优化接口
- 模块化架构设计：采用 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等解耦模块，便于扩展和定制
- 研究驱动的开发模式：强调 Research-First 理念，将学术研究成果快速转化为实用功能
- MCP 协议集成：支持 Model Context Protocol，提供标准化的上下文管理和工具调用能力
- 安全防护机制：内置安全审计和防护功能，确保 AI 代理操作的可靠性和安全性

**适用场景**:
- 企业级 AI 辅助开发：团队可基于此框架构建统一的 AI 编程规范和安全策略，提升整体开发效率
- 个人开发者效率提升：通过配置 Skills 和 Memory 模块，让 AI 助手更好地理解项目上下文和个人编码风格
- AI 代理研究与实验：研究者可在此框架基础上快速原型验证新的 AI Agent 技术方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,475 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 691 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多模型（OpenAI、Claude、Gemini、DeepSeek）和 MCP 协议，具备多 Agent 协作能力，拥有 7.4 万+ Stars 的活跃社区，是构建、测试和部署 AI Agent 解决方案的最佳选择。

**技术亮点**:
- 多模型集成：无缝支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型，提供统一的 Agent 开发体验
- MCP (Model Context Protocol) 协议支持：标准化的工具调用和上下文管理框架，便于扩展和集成第三方服务
- 多 Agent 协作框架：支持设计和管理 Agent 团队，实现复杂任务的多 Agent 协同工作流
- 知识库集成：内置 RAG 能力，支持向量检索和知识管理，增强 Agent 的领域知识
- TypeScript/现代前端架构：基于 React 和 TypeScript 构建，提供良好的开发体验和类型安全

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 协作框架构建复杂的业务流程自动化系统，如客户服务 agent 团队
- AI Agent 研究与原型开发：开发者可快速构建和测试 Agent 概念，验证多模型组合的效果
- 个人 AI 助手搭建：利用知识库集成功能构建个人知识管理和问答系统，支持多模型切换



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,603 |
| 语言 | HTML |
| Forks | 20,302 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是 AI 提示词工程领域最受欢迎的社区项目之一，汇聚超过 15 万星标和海量精选提示词，支持 ChatGPT/Claude/Gemini 等多模型，开源可自托管，是个人开发者和企业提升 AI 生产力的必备资源库

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用
- 采用 CC0 许可证，商用和私有部署无法律风险
- 支持企业自托管部署，数据完全自主可控
- 支持多种主流大语言模型（GPT-4/Claude/Gemini）
- 活跃开源社区持续更新高质量提示词

**适用场景**:
- 个人开发者：快速获取高质量 AI 提示词，提升 GPT/Claude 使用效率
- 企业团队：自托管私有提示词库，保护敏感业务数据
- AI 应用开发：二次开发构建企业级提示词管理平台



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,470 |
| 语言 | Jupyter Notebook |
| Forks | 13,660 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个从零开始手把手实现类ChatGPT大语言模型的教育项目，通过Jupyter Notebook以循序渐进的方式深入剖析LLM的每个核心组件，帮助开发者彻底理解Transformer架构、自注意力机制、GPT训练流程等底层原理，而非仅停留在API调用层面。

**技术亮点**:
- 完全基于PyTorch从零实现，不依赖Hugging Face Transformers等高级库，直接构建Embedding、Attention、Feed-Forward等核心模块
- 采用Jupyter Notebook形式，每个步骤都有详细代码、注释和可视化解释，适合交互式学习
- 完整覆盖LLM训练流程：数据预处理→Tokenization→Pretraining→Instruction Fine-tuning→RLHF
- 详细讲解GPT架构的核心技术细节，包括位置编码、因果掩码、Causal Attention等关键机制
- 包含GPT模型权重加载和文本生成推理的完整实现，可直接运行测试效果

**适用场景**:
- 系统学习大语言模型架构原理：适合AI/ML方向学生、研究人员和工程师建立扎实的LLM理论基础
- 企业内部培训与教学：用于团队内部开展大模型技术培训，降低学习曲线
- 个人项目与实验：开发者可基于此项目进行魔改实验，如替换注意力机制、尝试新Tokenizer或训练自定义GPT变体
- 面试准备与技术分享：作为深入理解Transformer和GPT的技术资料，可用于技术分享或面试准备



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,626 |
| 语言 | Python |
| Forks | 9,861 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,576 |
| 语言 | TypeScript |
| Forks | 6,566 |
| Issues | 23 |
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
| Stars | 42,391 |
| 语言 | TypeScript |
| Forks | 3,168 |
| Issues | 201 |
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
| Stars | 35,044 |
| 语言 | TypeScript |
| Forks | 7,118 |
| Issues | 470 |
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
| Stars | 33,677 |
| 语言 | Python |
| Forks | 2,088 |
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
| Stars | 57,074 |
| 语言 | JavaScript |
| Forks | 6,172 |
| Issues | 305 |
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
| Stars | 70,113 |
| 语言 | Python |
| Forks | 8,782 |
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
| Stars | 44,625 |
| 语言 | TypeScript |
| Forks | 3,328 |
| Issues | 360 |
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
| Stars | 51,223 |
| 语言 | TypeScript |
| Forks | 23,999 |
| Issues | 829 |
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
| Stars | 35,188 |
| 语言 | HTML |
| Forks | 5,656 |
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
| Stars | 74,640 |
| 语言 | Python |
| Forks | 14,923 |
| Issues | 3,979 |
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
| Stars | 54,093 |
| 语言 | Python |
| Forks | 5,251 |
| Issues | 69 |
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
| Stars | 39,176 |
| 语言 | TypeScript |
| Forks | 3,969 |
| Issues | 1,085 |
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
| Stars | 146,381 |
| 语言 | Python |
| Forks | 8,666 |
| Issues | 940 |
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
| Stars | 166,405 |
| 语言 | Go |
| Forks | 15,216 |
| Issues | 2,748 |
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
| Stars | 72,429 |
| 语言 | MDX |
| Forks | 7,755 |
| Issues | 252 |
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
| Stars | 47,311 |
| 语言 | Rust |
| Forks | 9,363 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,965 |
| 语言 | Python |
| Forks | 2,581 |
| Issues | 65 |
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
| Stars | 92,816 |
| 语言 | Python |
| Forks | 5,585 |
| Issues | 491 |
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
| Stars | 69,210 |
| 语言 | Python |
| Forks | 8,432 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的大模型微调平台，支持100+种LLM和VLM模型，集成LORA、QLORA、RLHF等主流微调技术，提供了开箱即用的WebUI和CLI界面，让研究者和开发者能够高效便捷地对大模型进行指令微调和领域适配，大幅降低了LLM微调的门槛。

**技术亮点**:
- 统一支持100+大语言模型和视觉语言模型，包括LLaMA、LLaMA3、Qwen、DeepSeek、Gemma等主流架构
- 集成多种高效微调技术：LORA、QLORA、Prefix Tuning、Prompt Tuning、Loatham等PEFT方法
- 支持完整的RLHF训练流程，包括PPO、DPO、KTO等强化学习对齐算法
- 提供WebUI可视化界面和CLI命令行工具，支持一键启动训练，降低使用门槛
- 支持模型量化（AWQ、GPTQ）、分布式训练和多硬件平台适配

**适用场景**:
- 企业场景：利用私有数据对开源大模型进行领域微调，构建专属AI助手或行业垂直应用
- 学术研究：快速实验不同微调方法在大模型上的效果，支持对比实验和消融研究
- 个人开发者：基于预训练模型进行指令微调，打造个性化的本地AI应用或聊天机器人



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,932 |
| 语言 | Python |
| Forks | 6,299 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是开源金融数据平台领域的标杆项目，凭借 63K+ Stars 的社区认可度，整合了股票、加密货币、期权、衍生品、固定收益等多品类金融数据，并原生集成 AI/ML 能力，为分析师、量化交易员和 AI 代理提供一站式数据获取与分析解决方案，大幅降低了金融数据获取和分析的技术门槛。

**技术亮点**:
- 多资产类别统一覆盖：无缝整合股票、加密货币、期权、期货、固定收益、外汇等多品类金融数据源
- AI 原生架构设计：内置机器学习模型与 AI Agent 支持，支持自然语言查询金融数据
- 模块化扩展框架：采用插件化架构设计，支持轻松扩展自定义数据源和组件
- 标准化数据管道：提供一致的 API 接口和数据预处理流程，简化数据清洗与特征工程
- 活跃的 Python 生态系统：与 pandas、numpy、scikit-learn 等主流数据科学库无缝集成

**适用场景**:
- 量化投资研究：用于策略回测、因子分析、风险建模等量化分析任务
- 金融数据分析与可视化：为投资机构、分析师提供一站式数据探索与报告生成能力
- AI 金融应用开发：为 AI Agent 和智能投顾应用提供实时金融数据接入与处理能力



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,603 |
| 语言 | HTML |
| Forks | 20,302 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是 AI 提示词工程领域最受欢迎的社区项目之一，汇聚超过 15 万星标和海量精选提示词，支持 ChatGPT/Claude/Gemini 等多模型，开源可自托管，是个人开发者和企业提升 AI 生产力的必备资源库

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用
- 采用 CC0 许可证，商用和私有部署无法律风险
- 支持企业自托管部署，数据完全自主可控
- 支持多种主流大语言模型（GPT-4/Claude/Gemini）
- 活跃开源社区持续更新高质量提示词

**适用场景**:
- 个人开发者：快速获取高质量 AI 提示词，提升 GPT/Claude 使用效率
- 企业团队：自托管私有提示词库，保护敏感业务数据
- AI 应用开发：二次开发构建企业级提示词管理平台



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,470 |
| 语言 | Jupyter Notebook |
| Forks | 13,660 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个从零开始手把手实现类ChatGPT大语言模型的教育项目，通过Jupyter Notebook以循序渐进的方式深入剖析LLM的每个核心组件，帮助开发者彻底理解Transformer架构、自注意力机制、GPT训练流程等底层原理，而非仅停留在API调用层面。

**技术亮点**:
- 完全基于PyTorch从零实现，不依赖Hugging Face Transformers等高级库，直接构建Embedding、Attention、Feed-Forward等核心模块
- 采用Jupyter Notebook形式，每个步骤都有详细代码、注释和可视化解释，适合交互式学习
- 完整覆盖LLM训练流程：数据预处理→Tokenization→Pretraining→Instruction Fine-tuning→RLHF
- 详细讲解GPT架构的核心技术细节，包括位置编码、因果掩码、Causal Attention等关键机制
- 包含GPT模型权重加载和文本生成推理的完整实现，可直接运行测试效果

**适用场景**:
- 系统学习大语言模型架构原理：适合AI/ML方向学生、研究人员和工程师建立扎实的LLM理论基础
- 企业内部培训与教学：用于团队内部开展大模型技术培训，降低学习曲线
- 个人项目与实验：开发者可基于此项目进行魔改实验，如替换注意力机制、尝试新Tokenizer或训练自定义GPT变体
- 面试准备与技术分享：作为深入理解Transformer和GPT的技术资料，可用于技术分享或面试准备



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 3,630 |
| Issues | 283 |
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
| Stars | 32,896 |
| 语言 | Jupyter Notebook |
| Forks | 5,446 |
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
| Stars | 158,525 |
| 语言 | Python |
| Forks | 32,667 |
| Issues | 2,322 |
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
| Stars | 74,640 |
| 语言 | Python |
| Forks | 14,923 |
| Issues | 3,979 |
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
| Stars | 107,247 |
| 语言 | Python |
| Forks | 12,375 |
| Issues | 3,909 |
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
| Stars | 98,623 |
| 语言 | Python |
| Forks | 27,333 |
| Issues | 18,123 |
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
| Stars | 72,429 |
| 语言 | MDX |
| Forks | 7,755 |
| Issues | 252 |
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
| Stars | 162,015 |
| 语言 | Python |
| Forks | 30,209 |
| Issues | 2,472 |
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
| Stars | 116,270 |
| 语言 | JavaScript |
| Forks | 15,125 |
| Issues | 105 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 编程代理性能优化框架之一，通过 Skills、Memory、Security 等多维度增强显著提升 Claude Code 等 AI 编程助手的效果。116k+ Stars 的社区认可度证明了其在实际开发中的有效性。

**技术亮点**:
- 多智能体框架支持：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供一致的性能优化接口
- 模块化架构设计：采用 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）等解耦模块，便于扩展和定制
- 研究驱动的开发模式：强调 Research-First 理念，将学术研究成果快速转化为实用功能
- MCP 协议集成：支持 Model Context Protocol，提供标准化的上下文管理和工具调用能力
- 安全防护机制：内置安全审计和防护功能，确保 AI 代理操作的可靠性和安全性

**适用场景**:
- 企业级 AI 辅助开发：团队可基于此框架构建统一的 AI 编程规范和安全策略，提升整体开发效率
- 个人开发者效率提升：通过配置 Skills 和 Memory 模块，让 AI 助手更好地理解项目上下文和个人编码风格
- AI 代理研究与实验：研究者可在此框架基础上快速原型验证新的 AI Agent 技术方案



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,562 |
| 语言 | Go |
| Forks | 3,818 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的本地化 AI 推理解决方案，支持文本、图像、语音、视频等多模态模型的无 GPU 运行，特别适合需要数据隐私保护、成本敏感或需要离线部署 AI 能力的开发者和企业。

**技术亮点**:
- 多模态统一推理：支持 LLM、图像生成、语音合成、目标检测等多种模型类型，通过统一 API 提供服务
- 硬件无关性：无需 GPU 即可运行主流 AI 模型，支持 CPU 推理，大幅降低部署门槛
- 去中心化架构：集成 libp2p 实现分布式部署能力，支持 P2P 网络中的模型共享与协作
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型生态

**适用场景**:
- 企业私有 AI 部署：在本地环境运行 AI 服务，满足数据安全合规要求，适合金融、医疗、政府等对数据隐私要求严格的场景
- 开发者本地 AI 开发：无需云服务费用即可进行 AI 应用原型开发和测试，支持快速迭代
- 边缘计算与离线场景：在没有稳定网络或无法访问云服务的环境中提供 AI 能力支持



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,113 |
| 语言 | Python |
| Forks | 8,782 |
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
| Stars | 44,625 |
| 语言 | TypeScript |
| Forks | 3,328 |
| Issues | 360 |
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
| Stars | 181,607 |
| 语言 | TypeScript |
| Forks | 56,279 |
| Issues | 1,435 |
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
| Stars | 153,841 |
| 语言 | Python |
| Forks | 12,486 |
| Issues | 2,427 |
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
| Stars | 96,664 |
| 语言 | Python |
| Forks | 8,966 |
| Issues | 170 |
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
| Stars | 183,161 |
| 语言 | TypeScript |
| Forks | 38,821 |
| Issues | 15,661 |
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
| Stars | 93,967 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Stars | 78,689 |
| 语言 | TypeScript |
| Forks | 5,741 |
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
| Stars | 76,891 |
| 语言 | TypeScript |
| Forks | 6,568 |
| Issues | 171 |
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
| Stars | 75,686 |
| 语言 | JavaScript |
| Forks | 7,275 |
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
| Stars | 79,094 |
| 语言 | Go |
| Forks | 2,740 |
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
| Stars | 75,200 |
| 语言 | Go |
| Forks | 2,651 |
| Issues | 951 |
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
| Stars | 36,965 |
| 语言 | Python |
| Forks | 2,581 |
| Issues | 65 |
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
| Stars | 54,753 |
| 语言 | JavaScript |
| Forks | 4,069 |
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
| Stars | 417,283 |
| 语言 | Python |
| Forks | 45,298 |
| Issues | 1,125 |
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
| Stars | 44,625 |
| 语言 | TypeScript |
| Forks | 3,328 |
| Issues | 360 |
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
| Stars | 181,607 |
| 语言 | TypeScript |
| Forks | 56,279 |
| Issues | 1,435 |
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
| Stars | 51,702 |
| 语言 | Go |
| Forks | 10,345 |
| Issues | 217 |
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
| Stars | 121,382 |
| 语言 | Go |
| Forks | 42,747 |
| Issues | 2,651 |
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
| Stars | 71,576 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,794 |
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
| Stars | 54,580 |
| 语言 | Go |
| Forks | 6,508 |
| Issues | 2,867 |
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
| Stars | 93,967 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Stars | 75,909 |
| 语言 | TypeScript |
| Forks | 6,470 |
| Issues | 454 |
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
| Stars | 84,639 |
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
| Stars | 69,601 |
| 语言 | Go |
| Forks | 1,894 |
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
| Stars | 62,392 |
| 语言 | Go |
| Forks | 5,894 |
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
| Stars | 58,334 |
| 语言 | Go |
| Forks | 4,225 |
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
| Stars | 47,602 |
| 语言 | Go |
| Forks | 5,068 |
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
| Stars | 84,639 |
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
| Stars | 63,304 |
| 语言 | Go |
| Forks | 10,281 |
| Issues | 765 |
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
| Stars | 44,562 |
| 语言 | Go |
| Forks | 3,818 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的本地化 AI 推理解决方案，支持文本、图像、语音、视频等多模态模型的无 GPU 运行，特别适合需要数据隐私保护、成本敏感或需要离线部署 AI 能力的开发者和企业。

**技术亮点**:
- 多模态统一推理：支持 LLM、图像生成、语音合成、目标检测等多种模型类型，通过统一 API 提供服务
- 硬件无关性：无需 GPU 即可运行主流 AI 模型，支持 CPU 推理，大幅降低部署门槛
- 去中心化架构：集成 libp2p 实现分布式部署能力，支持 P2P 网络中的模型共享与协作
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型生态

**适用场景**:
- 企业私有 AI 部署：在本地环境运行 AI 服务，满足数据安全合规要求，适合金融、医疗、政府等对数据隐私要求严格的场景
- 开发者本地 AI 开发：无需云服务费用即可进行 AI 应用原型开发和测试，支持快速迭代
- 边缘计算与离线场景：在没有稳定网络或无法访问云服务的环境中提供 AI 能力支持



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,664 |
| 语言 | Python |
| Forks | 8,966 |
| Issues | 170 |
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
| Stars | 100,117 |
| 语言 | TypeScript |
| Forks | 27,150 |
| Issues | 1,123 |
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
| Stars | 78,689 |
| 语言 | TypeScript |
| Forks | 5,741 |
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
| Stars | 75,686 |
| 语言 | JavaScript |
| Forks | 7,275 |
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
| Forks | 10,213 |
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
| Stars | 51,738 |
| 语言 | JavaScript |
| Forks | 4,690 |
| Issues | 1,465 |
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
| Stars | 71,161 |
| 语言 | Go |
| Forks | 4,690 |
| Issues | 245 |
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
| Stars | 57,199 |
| 语言 | Go |
| Forks | 3,226 |
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
| Stars | 36,965 |
| 语言 | Python |
| Forks | 2,581 |
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
| Stars | 417,283 |
| 语言 | Python |
| Forks | 45,298 |
| Issues | 1,125 |
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
| Stars | 68,873 |
| 语言 | JavaScript |
| Forks | 22,950 |
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
| Stars | 99,794 |
| 语言 | TypeScript |
| Forks | 11,920 |
| Issues | 995 |
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
| Stars | 57,074 |
| 语言 | JavaScript |
| Forks | 6,172 |
| Issues | 305 |
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
| Stars | 43,487 |
| 语言 | Go |
| Forks | 3,919 |
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
| Stars | 51,702 |
| 语言 | Go |
| Forks | 10,345 |
| Issues | 217 |
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
| Stars | 154,603 |
| 语言 | HTML |
| Forks | 20,302 |
| Issues | 39 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是 AI 提示词工程领域最受欢迎的社区项目之一，汇聚超过 15 万星标和海量精选提示词，支持 ChatGPT/Claude/Gemini 等多模型，开源可自托管，是个人开发者和企业提升 AI 生产力的必备资源库

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用
- 采用 CC0 许可证，商用和私有部署无法律风险
- 支持企业自托管部署，数据完全自主可控
- 支持多种主流大语言模型（GPT-4/Claude/Gemini）
- 活跃开源社区持续更新高质量提示词

**适用场景**:
- 个人开发者：快速获取高质量 AI 提示词，提升 GPT/Claude 使用效率
- 企业团队：自托管私有提示词库，保护敏感业务数据
- AI 应用开发：二次开发构建企业级提示词管理平台



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,576 |
| 语言 | TypeScript |
| Forks | 6,566 |
| Issues | 23 |
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
| Stars | 31,844 |
| 语言 | Python |
| Forks | 3,605 |
| Issues | 73 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,188 |
| 语言 | HTML |
| Forks | 5,656 |
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
| Stars | 72,429 |
| 语言 | MDX |
| Forks | 7,755 |
| Issues | 252 |
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
| Stars | 89,563 |
| 语言 | TypeScript |
| Forks | 9,965 |
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
| Stars | 86,961 |
| 语言 | TypeScript |
| Forks | 8,788 |
| Issues | 1,631 |
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
| Stars | 127,265 |
| 语言 | JavaScript |
| Forks | 12,468 |
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
| Stars | 101,073 |
| 语言 | JavaScript |
| Forks | 7,544 |
| Issues | 235 |
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
| Stars | 168,558 |
| 语言 | Go |
| Forks | 13,099 |
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
| Stars | 133,627 |
| 语言 | Unknown |
| Forks | 33,690 |
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
| Stars | 65,468 |
| 语言 | Shell |
| Forks | 9,896 |
| Issues | 87 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,854 |
| 语言 | Python |
| Forks | 6,406 |
| Issues | 49 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,109 |
| 语言 | Python |
| Forks | 12,409 |
| Issues | 106 |
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
| Stars | 83,399 |
| 语言 | Python |
| Forks | 7,134 |
| Issues | 637 |
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
| Stars | 384,692 |
| 语言 | Python |
| Forks | 66,064 |
| Issues | 91 |
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
| Stars | 113,982 |
| 语言 | TypeScript |
| Forks | 5,829 |
| Issues | 315 |
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
| Stars | 106,191 |
| 语言 | TypeScript |
| Forks | 7,705 |
| Issues | 210 |
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
| Stars | 48,005 |
| 语言 | Go |
| Forks | 10,255 |
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
| Stars | 99,870 |
| 语言 | C++ |
| Forks | 15,997 |
| Issues | 1,301 |
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
| Stars | 63,106 |
| 语言 | Python |
| Forks | 1,628 |
| Issues | 31 |
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
| Stars | 55,360 |
| 语言 | TypeScript |
| Forks | 7,217 |
| Issues | 272 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,539 |
| 语言 | JavaScript |
| Forks | 3,610 |
| Issues | 77 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 289,595 |
| 语言 | Python |
| Forks | 27,514 |
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
| Stars | 219,111 |
| 语言 | Python |
| Forks | 50,270 |
| Issues | 907 |
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
| Stars | 96,849 |
| 语言 | Python |
| Forks | 11,942 |
| Issues | 117 |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,904 |
| 语言 | Python |
| Forks | 37,105 |
| Issues | 3,486 |
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
| Stars | 85,617 |
| 语言 | Python |
| Forks | 7,189 |
| Issues | 478 |
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
| Stars | 77,688 |
| 语言 | Python |
| Forks | 45,190 |
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
| Stars | 439,164 |
| 语言 | TypeScript |
| Forks | 43,842 |
| Issues | 233 |
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
| Stars | 351,823 |
| 语言 | TypeScript |
| Forks | 43,865 |
| Issues | 39 |
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
| Stars | 119,755 |
| 语言 | TypeScript |
| Forks | 13,036 |
| Issues | 2,909 |
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
| Stars | 110,985 |
| 语言 | TypeScript |
| Forks | 8,358 |
| Issues | 1,796 |
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
| Stars | 108,348 |
| 语言 | TypeScript |
| Forks | 13,308 |
| Issues | 5,006 |
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
| Stars | 97,772 |
| 语言 | TypeScript |
| Forks | 54,573 |
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
| Stars | 95,919 |
| 语言 | TypeScript |
| Forks | 5,215 |
| Issues | 670 |
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
| Stars | 94,205 |
| 语言 | TypeScript |
| Forks | 5,137 |
| Issues | 101 |
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
| Stars | 83,047 |
| 语言 | TypeScript |
| Forks | 7,577 |
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
| Stars | 82,418 |
| 语言 | TypeScript |
| Forks | 10,119 |
| Issues | 611 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,407 |
| 语言 | TypeScript |
| Forks | 7,967 |
| Issues | 688 |
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
| Stars | 244,253 |
| 语言 | JavaScript |
| Forks | 50,873 |
| Issues | 1,185 |
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
| Stars | 116,451 |
| 语言 | JavaScript |
| Forks | 35,207 |
| Issues | 2,588 |
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
| Stars | 111,644 |
| 语言 | JavaScript |
| Forks | 36,317 |
| Issues | 577 |
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
| Stars | 108,655 |
| 语言 | JavaScript |
| Forks | 11,569 |
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
| Stars | 98,022 |
| 语言 | JavaScript |
| Forks | 32,695 |
| Issues | 1,711 |
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
| Stars | 95,478 |
| 语言 | JavaScript |
| Forks | 15,311 |
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
| Stars | 86,130 |
| 语言 | JavaScript |
| Forks | 4,833 |
| Issues | 977 |
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
| Stars | 70,880 |
| 语言 | JavaScript |
| Forks | 16,812 |
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
| Forks | 9,193 |
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
| Stars | 65,983 |
| 语言 | JavaScript |
| Forks | 9,366 |
| Issues | 212 |
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
| Stars | 62,394 |
| 语言 | JavaScript |
| Forks | 3,990 |
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
| Stars | 61,573 |
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
| Stars | 60,094 |
| 语言 | JavaScript |
| Forks | 5,635 |
| Issues | 64 |
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
| Stars | 59,865 |
| 语言 | JavaScript |
| Forks | 20,469 |
| Issues | 98 |
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
| Stars | 57,417 |
| 语言 | JavaScript |
| Forks | 12,302 |
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
| Stars | 53,050 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 463 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,208 |
| 语言 | JavaScript |
| Forks | 11,403 |
| Issues | 360 |
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
| Stars | 133,195 |
| 语言 | Go |
| Forks | 18,881 |
| Issues | 9,914 |
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
| Stars | 105,675 |
| 语言 | Go |
| Forks | 14,967 |
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
| Stars | 87,331 |
| 语言 | Go |
| Forks | 8,229 |
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
| Stars | 81,248 |
| 语言 | Go |
| Forks | 4,976 |
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
| Stars | 68,661 |
| 语言 | Go |
| Forks | 3,227 |
| Issues | 6 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,340 |
| 语言 | Go |
| Forks | 4,999 |
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
| Stars | 50,970 |
| 语言 | Go |
| Forks | 21,887 |
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
| Stars | 49,235 |
| 语言 | Go |
| Forks | 7,968 |
| Issues | 560 |
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
| Stars | 147,892 |
| 语言 | Python |
| Forks | 11,266 |
| Issues | 311 |
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
| Stars | 340,581 |
| 语言 | Python |
| Forks | 55,096 |
| Issues | 521 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,436 |
| 语言 | Python |
| Forks | 16,798 |
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
| Stars | 138,435 |
| 语言 | TypeScript |
| Forks | 16,487 |
| Issues | 45 |
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
| Stars | 78,928 |
| 语言 | JavaScript |
| Forks | 31,797 |
| Issues | 267 |
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
| Stars | 67,314 |
| 语言 | JavaScript |
| Forks | 11,971 |
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
| Stars | 50,438 |
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
| Stars | 45,713 |
| 语言 | Go |
| Forks | 3,775 |
| Issues | 82 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
