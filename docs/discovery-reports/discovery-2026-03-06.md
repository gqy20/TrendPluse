# 项目发现报告 (2026-03-06)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 140 |
| 去重移除 | 40 |
| 已在监控 | 20 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 18 |
| 💬 LLM 界面 | 22 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 3 |
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 6 |
| 📚 学习资源 | 6 |
| 📁 其他 | 52 |

## 📑 快速导航

### 按技术分类
- [🤖 AI Agents](#ai agents)
- [🔍 RAG/检索](#rag-检索)
- [💬 LLM 界面](#llm 界面)
- [🧠 机器学习框架](#机器学习框架)
- [🛠️ 开发工具](#开发工具)
- [⚙️ DevOps/基础设施](#devops-基础设施)
- [📈 监控/观测](#监控-观测)
- [🌐 Web 框架](#web 框架)
- [📊 数据/基础设施](#数据-基础设施)
- [📚 学习资源](#学习资源)
- [📁 其他](#其他)


## 🤖 AI Agents (30 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,952 |
| 语言 | Python |
| Forks | 17,821 |
| Issues | 326 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是一个功能强大且用户友好的自托管AI聊天界面，支持多种LLM后端（Ollama、OpenAI API等）。作为目前最受欢迎的开源LLM Web UI之一（超过12.5万星标），它提供了类似ChatGPT的现代化界面，支持RAG、模型切换、代码高亮等企业级功能，是构建私有化AI对话平台的理想选择。

**技术亮点**:
- 🤖 多后端支持：集成Ollama、OpenAI API等多种LLM服务，实现模型灵活切换
- 🔍 RAG集成：内置检索增强生成能力，支持文档上传和知识库构建
- 🎨 现代化Web界面：提供类似ChatGPT的流畅用户体验，支持代码语法高亮和Markdown渲染
- 🔐 完全自托管：支持本地部署，数据完全可控，适合企业内网和隐私敏感场景
- 🔌 MCP协议支持：集成Model Context Protocol，扩展AI交互能力

**适用场景**:
- 企业私有化部署：为公司内部搭建安全可控的AI助手平台，保护敏感数据不外泄
- 个人开发者环境：在本地或私有服务器上运行，通过Ollama等工具使用开源模型（如Llama、Qwen）
- AI应用快速原型：作为AI聊天应用的前端模板，快速集成自定义LLM功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,273 |
| 语言 | Python |
| Forks | 8,268 |
| Issues | 3,048 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一个领先的检索增强生成(RAG)开源引擎，创新性地融合了RAG技术与Agent能力，为大语言模型构建卓越的上下文层。拥有74K+ Stars和活跃社区，采用Apache 2.0许可，是构建企业级AI应用和智能搜索的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，提供强大的上下文工程和智能工作流
- 支持文档解析与理解，结合GraphRAG实现深度研究
- 兼容主流LLM生态，包括OpenAI、Ollama、DeepSeek等
- 提供MCP协议支持，增强Agent互操作性
- 企业级AI搜索引擎架构，专注高精度上下文检索

**适用场景**:
- 企业知识库构建与智能问答系统：快速部署基于企业文档的AI助手，实现精准的文档理解和知识检索
- Agent智能工作流开发：构建能够自主进行深度研究和多步骤推理的AI Agent应用
- 私有化LLM应用部署：结合本地模型(Ollama)实现数据隐私可控的企业级AI解决方案



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,966 |
| 语言 | Python |
| Forks | 8,290 |
| Issues | 919 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一款被 ACL 2024 收录的统一高效微调框架，支持 100+ 大语言模型和视觉语言模型。该项目凭借 6.7万+ GitHub Stars 的极高人气，提供了从微调到部署的一站式解决方案，是个人开发者和企业进行 LLM 定制的首选工具之一。

**技术亮点**:
- 统一支持 100+ LLMs & VLMs，涵盖 Llama3、Gemma、Qwen、DeepSeek 等主流模型
- 集 LoRA、QLoRA、PEFT、全量微调等多种高效训练方法于一体
- 支持 RLHF（人类反馈强化学习）、指令微调和 Agent 训练等多种训练范式
- 提供模型量化（Quantization）和 MoE（混合专家）等优化技术
- 零代码 Web UI 界面，让非技术用户也能轻松进行模型微调

**适用场景**:
- 企业 AI 应用定制：快速微调领域专用大模型（如客服、金融、医疗等垂直场景）
- 个人开发者研究：低成本实验不同微调方法（LoRA/QLoRA）和模型对比
- 教学与学习：作为学习 LLM 微调技术的最佳实践平台



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,742 |
| 语言 | TypeScript |
| Forks | 6,227 |
| Issues | 196 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个专为 AI 应用打造的全能网页数据采集解决方案，能将任意网站转换为 LLM 可用的 Markdown 或结构化数据。该项目拥有接近 9 万星的高人气，凭借 AI 原生设计、强大的爬取能力和易于集成的 API，成为构建 AI Agent、RAG 系统和数据分析应用的理想基础设施。

**技术亮点**:
- AI 原生架构，专门优化输出格式为 LLM 友好的 Markdown 和结构化数据
- 支持完整的网站爬取，可处理动态 JavaScript 内容和复杂网页结构
- 提供简洁的 Web API 接口，便于快速集成到各类 AI 应用和工作流中
- 具备强大的 HTML 到 Markdown 转换能力，保留文档语义和格式
- 兼容多种数据提取场景，支持批量处理和大规模数据采集

**适用场景**:
- AI Agent 和 RAG 系统开发：为 LLM 应用提供高质量、结构化的网页知识源
- 企业数据采集与分析：将目标网站内容转换为可分析的结构化数据，用于市场研究、竞争分析等
- 内容聚合平台：快速构建垂直领域的知识库或内容聚合系统，自动采集和标准化网页内容



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,176 |
| 语言 | TypeScript |
| Forks | 14,732 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个获得 7.3 万+ Star 的现象级 AI Agent 开源项目，它开创性地将多智能体协作（multi-agent collaboration）和团队化设计（agent team design）作为核心能力，填补了 AI Agent 领域缺少系统性协作框架的空白。项目完美整合了 ChatGPT、Claude、Gemini、DeepSeek 等主流大模型，支持 MCP 协议和知识库功能，为企业构建智能工作流和开发者实现 AI Agent 应用提供了开箱即用的完整解决方案。

**技术亮点**:
- 【TypeScript 全栈架构】基于 TypeScript 开发的现代化技术栈，提供类型安全和优秀的开发体验，便于企业级应用扩展与维护
- 【多智能体协作系统】支持 Multi-Agent 协作模式，可实现智能体之间的任务分配、信息共享和协同工作，大幅提升复杂问题解决能力
- 【统一模型接入】同时支持 ChatGPT、Claude、Gemini、DeepSeek 等多家大模型，灵活切换避免供应商锁定
- 【MCP 协议集成】原生支持 MCP（Model Context Protocol）标准，可轻松扩展插件生态和工具集成能力
- 【智能体团队设计】提供可视化的 Agent Team 设计能力，将智能体作为工作交互的基本单元，支持零门槛构建智能工作流

**适用场景**:
- 【企业智能工作流搭建】企业可基于 LobeHub 快速构建客服、销售、研发等跨部门的 AI Agent 团队，实现业务流程自动化和智能化
- 【个人知识管理与助手】个人用户可集成知识库，打造专属的 AI 研究助手、学习伙伴或生活管家，支持文档处理、信息检索和创意生成
- 【开发者 Agent 应用开发】开发者可利用框架的扩展能力快速定制特定领域的 AI Agent 应用，如代码审查、数据分析、内容创作等场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,446 |
| 语言 | JavaScript |
| Forks | 7,738 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 代码助手打造的性能优化与能力增强系统，通过集成技能管理、记忆机制和安全防护，将 Claude Code 等工具从简单的代码生成器升级为具备自主学习和适应能力的智能开发伙伴。项目拥有超高人气（62K+ stars）和活跃的社区支持，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 多工具兼容性：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- 智能记忆系统：持久化存储上下文和学习数据，让 AI 能够记住项目历史和开发偏好
- 安全增强机制：内置企业级安全防护，确保 AI 代码生成符合安全规范和最佳实践
- 研究优先开发：采用实验性方法持续优化，紧跟 LLM 和 AI Agent 最新技术进展
- MCP 集成：原生支持 Model Context Protocol，实现与 AI 模型的深度协同

**适用场景**:
- 企业级 AI 开发团队：统一团队的 AI 编程助手配置，确保代码安全性和开发规范的统一执行
- 个人开发者效率提升：通过持久化记忆和技能定制，打造个性化的 AI 编程助手，大幅减少重复性工作
- AI Agent 研究与实验：为研究者和早期采用者提供测试平台，探索 AI Agent 在软件开发中的前沿应用



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,324 |
| 语言 | Go |
| Forks | 3,641 |
| Issues | 143 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 和 Claude 的开源替代方案，支持在消费级硬件上本地运行多种AI模型（无需GPU），为开发者和企业提供成本效益极高的AI解决方案。项目采用 Go 语言实现高性能推理服务，具备去中心化推理能力，已获得超过 4.3 万颗星，是构建私有化 AI 应用的理想选择。

**技术亮点**:
- 无需 GPU 即可在消费级硬件上运行，大幅降低 AI 部署成本
- 支持多种模型格式（gguf、transformers、diffusers）和主流模型（Llama、Mistral、Stable Diffusion 等）
- 提供与 OpenAI 兼容的 API 接口，实现零成本迁移
- 具备分布式、P2P 和去中心化推理能力，可横向扩展
- 集成 MCP（Model Context Protocol）协议，支持多模态生成（文本、音频、视频、图像、语音克隆）

**适用场景**:
- 企业内部私有化 AI 部署：在本地服务器部署 AI 服务，保障数据隐私和安全，避免敏感数据外泄至第三方 API
- 个人开发者本地开发环境：在个人电脑上构建和测试 AI 应用，无需承担 API 调用费用，支持离线开发
- 边缘计算和嵌入式场景：在资源受限设备上部署 AI 能力，利用无 GPU 优势实现本地化推理



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,344 |
| 语言 | Java |
| Forks | 15,829 |
| Issues | 49 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot是一款创新的"低代码+零代码+AI"三位一体开发平台，通过集成LLM、RAG、LangChain4j等前沿AI技术，为企业提供从传统业务系统快速开发到AI应用构建的完整解决方案，代码生成器可一键生成前后端代码，显著提升开发效率。

**技术亮点**:
- AI驱动的低代码平台：集成LLM、RAG、LangChain4j、DeepSeek等技术，支持AI应用构建、知识库管理、AI流程编排和聊天式业务操作
- 强大代码生成器：前后端代码一键生成，支持SpringBoot3、MyBatis-Plus、Vue3、Ant Design Vue等主流技术栈，无需手写代码
- 智能工作流引擎：集成Flowable/Activiti流程引擎，支持业务流程可视化配置和AI流程编排
- 现代化技术架构：基于SpringBoot3、SpringCloud微服务架构，采用Vue3前端框架，支持MCP协议和插件扩展
- 双模驱动开发：提供低代码和零代码两种开发模式，满足不同技术背景用户需求，灵活性与效率兼备

**适用场景**:
- 企业数字化转型：中大型企业快速构建OA、ERP、CRM等管理系统，通过AI能力增强业务流程智能化
- AI应用快速开发：企业开发者或独立开发者构建AI助手、知识库问答、智能客服、RAG检索等AI应用场景
- 政务及SaaS平台：政府部门或SaaS服务商需要快速搭建行业解决方案，结合AI能力提供智能化服务



### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,644 |
| 语言 | Python |
| Forks | 6,119 |
| Issues | 195 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,938 |
| 语言 | Python |
| Forks | 9,790 |
| Issues | 351 |
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
| Stars | 34,388 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 430 |
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
| Stars | 33,184 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,121 |
| 语言 | TypeScript |
| Forks | 2,258 |
| Issues | 78 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,294 |
| 语言 | TypeScript |
| Forks | 6,948 |
| Issues | 172 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### yamadashy/repomix

**描述**: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,260 |
| 语言 | TypeScript |
| Forks | 1,031 |
| Issues | 147 |
| Topics | ai, anthropic, artificial-intelligence, chatbot, chatgpt, claude, deepseek, developer-tools, gemini, genai, generative-ai, gpt, javascript, language-model, llama, llm, mcp, nodejs, openai, typescript |
| 许可证 | MIT License |


### oraios/serena

**描述**: A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 21,080 |
| 语言 | Python |
| Forks | 1,424 |
| Issues | 83 |
| Topics | agent, ai, ai-coding, claude, claude-code, language-server, llms, mcp-server, programming, vibe-coding |
| 许可证 | MIT License |


### datawhalechina/happy-llm

**描述**: 📚 从零开始的大语言模型原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,918 |
| 语言 | Jupyter Notebook |
| Forks | 2,490 |
| Issues | 48 |
| Topics | agent, llm, rag |
| 许可证 | Other |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,853 |
| 语言 | TypeScript |
| Forks | 3,390 |
| Issues | 178 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### chroma-core/chroma

**描述**: Open-source search and retrieval database for AI applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,488 |
| 语言 | Rust |
| Forks | 2,090 |
| Issues | 506 |
| Topics | agents, ai, ai-agents, database, document-retrieval, embeddings, llm, llms, rag, rust, rust-lang, vector-database |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,652 |
| 语言 | Python |
| Forks | 8,570 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,710 |
| 语言 | JavaScript |
| Forks | 6,023 |
| Issues | 299 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,460 |
| 语言 | TypeScript |
| Forks | 2,815 |
| Issues | 340 |
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
| Stars | 79,751 |
| 语言 | Python |
| Forks | 9,424 |
| Issues | 233 |
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
| Stars | 50,428 |
| 语言 | TypeScript |
| Forks | 23,875 |
| Issues | 796 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### upstash/context7

**描述**: Context7 MCP Server -- Up-to-date code documentation for LLMs and AI code editors

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,901 |
| 语言 | TypeScript |
| Forks | 2,263 |
| Issues | 176 |
| Topics | llm, mcp, mcp-server, vibe-coding |
| 许可证 | MIT License |


### BloopAI/vibe-kanban

**描述**: Get 10X more out of Claude Code, Codex or any coding agent

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,505 |
| 语言 | Rust |
| Forks | 2,190 |
| Issues | 405 |
| Topics | agent, ai-agents, kanban, management, task-manager |
| 许可证 | Apache License 2.0 |


### sickn33/antigravity-awesome-skills

**描述**: The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 20,755 |
| 语言 | Python |
| Forks | 3,614 |
| Issues | 4 |
| Topics | agentic-skills, ai-agents, antigravity, autonomous-coding, claude-code, mcp, react-patterns, security-auditing |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 177,840 |
| 语言 | TypeScript |
| Forks | 55,477 |
| Issues | 1,411 |
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
| Stars | 145,308 |
| 语言 | Python |
| Forks | 8,522 |
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
| Stars | 53,173 |
| 语言 | Jupyter Notebook |
| Forks | 18,464 |
| Issues | 1 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


## 🔍 RAG/检索 (18 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,952 |
| 语言 | Python |
| Forks | 17,821 |
| Issues | 326 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是一个功能强大且用户友好的自托管AI聊天界面，支持多种LLM后端（Ollama、OpenAI API等）。作为目前最受欢迎的开源LLM Web UI之一（超过12.5万星标），它提供了类似ChatGPT的现代化界面，支持RAG、模型切换、代码高亮等企业级功能，是构建私有化AI对话平台的理想选择。

**技术亮点**:
- 🤖 多后端支持：集成Ollama、OpenAI API等多种LLM服务，实现模型灵活切换
- 🔍 RAG集成：内置检索增强生成能力，支持文档上传和知识库构建
- 🎨 现代化Web界面：提供类似ChatGPT的流畅用户体验，支持代码语法高亮和Markdown渲染
- 🔐 完全自托管：支持本地部署，数据完全可控，适合企业内网和隐私敏感场景
- 🔌 MCP协议支持：集成Model Context Protocol，扩展AI交互能力

**适用场景**:
- 企业私有化部署：为公司内部搭建安全可控的AI助手平台，保护敏感数据不外泄
- 个人开发者环境：在本地或私有服务器上运行，通过Ollama等工具使用开源模型（如Llama、Qwen）
- AI应用快速原型：作为AI聊天应用的前端模板，快速集成自定义LLM功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,273 |
| 语言 | Python |
| Forks | 8,268 |
| Issues | 3,048 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一个领先的检索增强生成(RAG)开源引擎，创新性地融合了RAG技术与Agent能力，为大语言模型构建卓越的上下文层。拥有74K+ Stars和活跃社区，采用Apache 2.0许可，是构建企业级AI应用和智能搜索的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，提供强大的上下文工程和智能工作流
- 支持文档解析与理解，结合GraphRAG实现深度研究
- 兼容主流LLM生态，包括OpenAI、Ollama、DeepSeek等
- 提供MCP协议支持，增强Agent互操作性
- 企业级AI搜索引擎架构，专注高精度上下文检索

**适用场景**:
- 企业知识库构建与智能问答系统：快速部署基于企业文档的AI助手，实现精准的文档理解和知识检索
- Agent智能工作流开发：构建能够自主进行深度研究和多步骤推理的AI Agent应用
- 私有化LLM应用部署：结合本地模型(Ollama)实现数据隐私可控的企业级AI解决方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,176 |
| 语言 | TypeScript |
| Forks | 14,732 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个获得 7.3 万+ Star 的现象级 AI Agent 开源项目，它开创性地将多智能体协作（multi-agent collaboration）和团队化设计（agent team design）作为核心能力，填补了 AI Agent 领域缺少系统性协作框架的空白。项目完美整合了 ChatGPT、Claude、Gemini、DeepSeek 等主流大模型，支持 MCP 协议和知识库功能，为企业构建智能工作流和开发者实现 AI Agent 应用提供了开箱即用的完整解决方案。

**技术亮点**:
- 【TypeScript 全栈架构】基于 TypeScript 开发的现代化技术栈，提供类型安全和优秀的开发体验，便于企业级应用扩展与维护
- 【多智能体协作系统】支持 Multi-Agent 协作模式，可实现智能体之间的任务分配、信息共享和协同工作，大幅提升复杂问题解决能力
- 【统一模型接入】同时支持 ChatGPT、Claude、Gemini、DeepSeek 等多家大模型，灵活切换避免供应商锁定
- 【MCP 协议集成】原生支持 MCP（Model Context Protocol）标准，可轻松扩展插件生态和工具集成能力
- 【智能体团队设计】提供可视化的 Agent Team 设计能力，将智能体作为工作交互的基本单元，支持零门槛构建智能工作流

**适用场景**:
- 【企业智能工作流搭建】企业可基于 LobeHub 快速构建客服、销售、研发等跨部门的 AI Agent 团队，实现业务流程自动化和智能化
- 【个人知识管理与助手】个人用户可集成知识库，打造专属的 AI 研究助手、学习伙伴或生活管家，支持文档处理、信息检索和创意生成
- 【开发者 Agent 应用开发】开发者可利用框架的扩展能力快速定制特定领域的 AI Agent 应用，如代码审查、数据分析、内容创作等场景



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,344 |
| 语言 | Java |
| Forks | 15,829 |
| Issues | 49 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot是一款创新的"低代码+零代码+AI"三位一体开发平台，通过集成LLM、RAG、LangChain4j等前沿AI技术，为企业提供从传统业务系统快速开发到AI应用构建的完整解决方案，代码生成器可一键生成前后端代码，显著提升开发效率。

**技术亮点**:
- AI驱动的低代码平台：集成LLM、RAG、LangChain4j、DeepSeek等技术，支持AI应用构建、知识库管理、AI流程编排和聊天式业务操作
- 强大代码生成器：前后端代码一键生成，支持SpringBoot3、MyBatis-Plus、Vue3、Ant Design Vue等主流技术栈，无需手写代码
- 智能工作流引擎：集成Flowable/Activiti流程引擎，支持业务流程可视化配置和AI流程编排
- 现代化技术架构：基于SpringBoot3、SpringCloud微服务架构，采用Vue3前端框架，支持MCP协议和插件扩展
- 双模驱动开发：提供低代码和零代码两种开发模式，满足不同技术背景用户需求，灵活性与效率兼备

**适用场景**:
- 企业数字化转型：中大型企业快速构建OA、ERP、CRM等管理系统，通过AI能力增强业务流程智能化
- AI应用快速开发：企业开发者或独立开发者构建AI助手、知识库问答、智能客服、RAG检索等AI应用场景
- 政务及SaaS平台：政府部门或SaaS服务商需要快速搭建行业解决方案，结合AI能力提供智能化服务



### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,644 |
| 语言 | Python |
| Forks | 6,119 |
| Issues | 195 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,184 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,121 |
| 语言 | TypeScript |
| Forks | 2,258 |
| Issues | 78 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,294 |
| 语言 | TypeScript |
| Forks | 6,948 |
| Issues | 172 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### datawhalechina/happy-llm

**描述**: 📚 从零开始的大语言模型原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,918 |
| 语言 | Jupyter Notebook |
| Forks | 2,490 |
| Issues | 48 |
| Topics | agent, llm, rag |
| 许可证 | Other |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,853 |
| 语言 | TypeScript |
| Forks | 3,390 |
| Issues | 178 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### chroma-core/chroma

**描述**: Open-source search and retrieval database for AI applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,488 |
| 语言 | Rust |
| Forks | 2,090 |
| Issues | 506 |
| Topics | agents, ai, ai-agents, database, document-retrieval, embeddings, llm, llms, rag, rust, rust-lang, vector-database |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,606 |
| 语言 | TypeScript |
| Forks | 11,718 |
| Issues | 967 |
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
| Stars | 55,710 |
| 语言 | JavaScript |
| Forks | 6,023 |
| Issues | 299 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,676 |
| 语言 | Python |
| Forks | 9,902 |
| Issues | 265 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,428 |
| 语言 | TypeScript |
| Forks | 23,875 |
| Issues | 796 |
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
| Stars | 43,164 |
| 语言 | Go |
| Forks | 3,869 |
| Issues | 1,049 |
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
| Stars | 31,267 |
| 语言 | Python |
| Forks | 3,299 |
| Issues | 70 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### HKUDS/LightRAG

**描述**: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 29,023 |
| 语言 | Python |
| Forks | 4,157 |
| Issues | 189 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (22 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,952 |
| 语言 | Python |
| Forks | 17,821 |
| Issues | 326 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是一个功能强大且用户友好的自托管AI聊天界面，支持多种LLM后端（Ollama、OpenAI API等）。作为目前最受欢迎的开源LLM Web UI之一（超过12.5万星标），它提供了类似ChatGPT的现代化界面，支持RAG、模型切换、代码高亮等企业级功能，是构建私有化AI对话平台的理想选择。

**技术亮点**:
- 🤖 多后端支持：集成Ollama、OpenAI API等多种LLM服务，实现模型灵活切换
- 🔍 RAG集成：内置检索增强生成能力，支持文档上传和知识库构建
- 🎨 现代化Web界面：提供类似ChatGPT的流畅用户体验，支持代码语法高亮和Markdown渲染
- 🔐 完全自托管：支持本地部署，数据完全可控，适合企业内网和隐私敏感场景
- 🔌 MCP协议支持：集成Model Context Protocol，扩展AI交互能力

**适用场景**:
- 企业私有化部署：为公司内部搭建安全可控的AI助手平台，保护敏感数据不外泄
- 个人开发者环境：在本地或私有服务器上运行，通过Ollama等工具使用开源模型（如Llama、Qwen）
- AI应用快速原型：作为AI聊天应用的前端模板，快速集成自定义LLM功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,273 |
| 语言 | Python |
| Forks | 8,268 |
| Issues | 3,048 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一个领先的检索增强生成(RAG)开源引擎，创新性地融合了RAG技术与Agent能力，为大语言模型构建卓越的上下文层。拥有74K+ Stars和活跃社区，采用Apache 2.0许可，是构建企业级AI应用和智能搜索的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，提供强大的上下文工程和智能工作流
- 支持文档解析与理解，结合GraphRAG实现深度研究
- 兼容主流LLM生态，包括OpenAI、Ollama、DeepSeek等
- 提供MCP协议支持，增强Agent互操作性
- 企业级AI搜索引擎架构，专注高精度上下文检索

**适用场景**:
- 企业知识库构建与智能问答系统：快速部署基于企业文档的AI助手，实现精准的文档理解和知识检索
- Agent智能工作流开发：构建能够自主进行深度研究和多步骤推理的AI Agent应用
- 私有化LLM应用部署：结合本地模型(Ollama)实现数据隐私可控的企业级AI解决方案



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,176 |
| 语言 | TypeScript |
| Forks | 14,732 |
| Issues | 669 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个获得 7.3 万+ Star 的现象级 AI Agent 开源项目，它开创性地将多智能体协作（multi-agent collaboration）和团队化设计（agent team design）作为核心能力，填补了 AI Agent 领域缺少系统性协作框架的空白。项目完美整合了 ChatGPT、Claude、Gemini、DeepSeek 等主流大模型，支持 MCP 协议和知识库功能，为企业构建智能工作流和开发者实现 AI Agent 应用提供了开箱即用的完整解决方案。

**技术亮点**:
- 【TypeScript 全栈架构】基于 TypeScript 开发的现代化技术栈，提供类型安全和优秀的开发体验，便于企业级应用扩展与维护
- 【多智能体协作系统】支持 Multi-Agent 协作模式，可实现智能体之间的任务分配、信息共享和协同工作，大幅提升复杂问题解决能力
- 【统一模型接入】同时支持 ChatGPT、Claude、Gemini、DeepSeek 等多家大模型，灵活切换避免供应商锁定
- 【MCP 协议集成】原生支持 MCP（Model Context Protocol）标准，可轻松扩展插件生态和工具集成能力
- 【智能体团队设计】提供可视化的 Agent Team 设计能力，将智能体作为工作交互的基本单元，支持零门槛构建智能工作流

**适用场景**:
- 【企业智能工作流搭建】企业可基于 LobeHub 快速构建客服、销售、研发等跨部门的 AI Agent 团队，实现业务流程自动化和智能化
- 【个人知识管理与助手】个人用户可集成知识库，打造专属的 AI 研究助手、学习伙伴或生活管家，支持文档处理、信息检索和创意生成
- 【开发者 Agent 应用开发】开发者可利用框架的扩展能力快速定制特定领域的 AI Agent 应用，如代码审查、数据分析、内容创作等场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,446 |
| 语言 | JavaScript |
| Forks | 7,738 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 代码助手打造的性能优化与能力增强系统，通过集成技能管理、记忆机制和安全防护，将 Claude Code 等工具从简单的代码生成器升级为具备自主学习和适应能力的智能开发伙伴。项目拥有超高人气（62K+ stars）和活跃的社区支持，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 多工具兼容性：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- 智能记忆系统：持久化存储上下文和学习数据，让 AI 能够记住项目历史和开发偏好
- 安全增强机制：内置企业级安全防护，确保 AI 代码生成符合安全规范和最佳实践
- 研究优先开发：采用实验性方法持续优化，紧跟 LLM 和 AI Agent 最新技术进展
- MCP 集成：原生支持 Model Context Protocol，实现与 AI 模型的深度协同

**适用场景**:
- 企业级 AI 开发团队：统一团队的 AI 编程助手配置，确保代码安全性和开发规范的统一执行
- 个人开发者效率提升：通过持久化记忆和技能定制，打造个性化的 AI 编程助手，大幅减少重复性工作
- AI Agent 研究与实验：为研究者和早期采用者提供测试平台，探索 AI Agent 在软件开发中的前沿应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,307 |
| 语言 | HTML |
| Forks | 19,744 |
| Issues | 12 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,938 |
| 语言 | Python |
| Forks | 9,790 |
| Issues | 351 |
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
| Stars | 34,388 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 430 |
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
| Stars | 33,184 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,121 |
| 语言 | TypeScript |
| Forks | 2,258 |
| Issues | 78 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,294 |
| 语言 | TypeScript |
| Forks | 6,948 |
| Issues | 172 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,531 |
| 语言 | Python |
| Forks | 1,666 |
| Issues | 74 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### yamadashy/repomix

**描述**: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,260 |
| 语言 | TypeScript |
| Forks | 1,031 |
| Issues | 147 |
| Topics | ai, anthropic, artificial-intelligence, chatbot, chatgpt, claude, deepseek, developer-tools, gemini, genai, generative-ai, gpt, javascript, language-model, llama, llm, mcp, nodejs, openai, typescript |
| 许可证 | MIT License |


### oraios/serena

**描述**: A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 21,080 |
| 语言 | Python |
| Forks | 1,424 |
| Issues | 83 |
| Topics | agent, ai, ai-coding, claude, claude-code, language-server, llms, mcp-server, programming, vibe-coding |
| 许可证 | MIT License |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,853 |
| 语言 | TypeScript |
| Forks | 3,390 |
| Issues | 178 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,652 |
| 语言 | Python |
| Forks | 8,570 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,710 |
| 语言 | JavaScript |
| Forks | 6,023 |
| Issues | 299 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,460 |
| 语言 | TypeScript |
| Forks | 2,815 |
| Issues | 340 |
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
| Stars | 50,428 |
| 语言 | TypeScript |
| Forks | 23,875 |
| Issues | 796 |
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
| Stars | 72,208 |
| 语言 | Python |
| Forks | 14,015 |
| Issues | 3,524 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### davila7/claude-code-templates

**描述**: CLI tool for configuring and monitoring Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,211 |
| 语言 | Python |
| Forks | 2,105 |
| Issues | 103 |
| Topics | anthropic, anthropic-claude, claude, claude-code |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,308 |
| 语言 | Python |
| Forks | 8,522 |
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
| Stars | 164,260 |
| 语言 | Go |
| Forks | 14,795 |
| Issues | 2,576 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


## 🧠 机器学习框架 (11 个项目)


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,966 |
| 语言 | Python |
| Forks | 8,290 |
| Issues | 919 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一款被 ACL 2024 收录的统一高效微调框架，支持 100+ 大语言模型和视觉语言模型。该项目凭借 6.7万+ GitHub Stars 的极高人气，提供了从微调到部署的一站式解决方案，是个人开发者和企业进行 LLM 定制的首选工具之一。

**技术亮点**:
- 统一支持 100+ LLMs & VLMs，涵盖 Llama3、Gemma、Qwen、DeepSeek 等主流模型
- 集 LoRA、QLoRA、PEFT、全量微调等多种高效训练方法于一体
- 支持 RLHF（人类反馈强化学习）、指令微调和 Agent 训练等多种训练范式
- 提供模型量化（Quantization）和 MoE（混合专家）等优化技术
- 零代码 Web UI 界面，让非技术用户也能轻松进行模型微调

**适用场景**:
- 企业 AI 应用定制：快速微调领域专用大模型（如客服、金融、医疗等垂直场景）
- 个人开发者研究：低成本实验不同微调方法（LoRA/QLoRA）和模型对比
- 教学与学习：作为学习 LLM 微调技术的最佳实践平台



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,619 |
| 语言 | Python |
| Forks | 6,126 |
| Issues | 59 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是金融数据平台领域的开源标杆，拥有超6.2万星标。它为分析师、量化交易员和AI开发者提供统一的金融数据访问接口，聚合股票、债券、加密货币、衍生品等全品类金融数据，显著降低了金融数据获取的技术门槛，是构建金融应用和AI Agent的理想基础设施。

**技术亮点**:
- 基于 Python 构建的一体化金融数据平台，支持股票、期权、固定收益、加密货币等全资产类别
- 专为 AI Agent 和量化分析设计，提供标准化的数据接口，便于与机器学习模型集成
- 提供命令行工具和 Python SDK 双重使用方式，支持灵活的数据获取和处理
- 开源生态系统覆盖经济学、衍生品、机器学习等多个金融技术领域
- 经过大规模验证的生产级项目（62k+ stars），活跃的社区和企业级支持

**适用场景**:
- 金融分析师和量化研究员构建数据驱动的投资策略和回测系统
- AI 开发者构建金融智能体和数据分析应用，提供标准化金融数据源
- 个人投资者进行市场分析和资产配置研究，无需昂贵的数据终端订阅



### lutzroeder/netron

**描述**: Visualizer for neural network, deep learning and machine learning models

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,529 |
| 语言 | JavaScript |
| Forks | 3,086 |
| Issues | 19 |
| Topics | ai, coreml, deep-learning, deeplearning, keras, machine-learning, machinelearning, ml, neural-network, numpy, onnx, pytorch, safetensors, tensorflow, tensorflow-lite, visualizer |
| 许可证 | MIT License |

---

Netron 是一个功能强大且跨平台的神经网络模型可视化工具，支持 ONNX、TensorFlow、PyTorch、Keras 等 20+ 种主流模型格式。其独特价值在于纯前端实现、无需安装依赖、离线可用，是深度学习开发者和研究人员调试和解释模型的首选工具。

**技术亮点**:
- 跨平台支持：提供 Web 应用、桌面应用（Windows/macOS/Linux）以及 VS Code 插件多种使用方式
- 丰富的格式兼容：支持 ONNX、TensorFlow、Keras、PyTorch、Core ML、Caffe、MXNet、Safetensors 等多种模型格式
- 纯前端实现：基于 JavaScript/TypeScript 开发，无需后端服务，可直接在浏览器中本地打开模型文件
- 可视化能力：提供模型结构图、层信息、张量形状、权重等多维度可视化展示
- 开源免费：MIT 许可证，代码完全开源，支持自定义和二次开发

**适用场景**:
- 模型调试与分析：开发者可以快速查看神经网络的层结构、参数配置和数据流向，帮助调试模型架构问题
- 模型文档与分享：通过可视化图形向团队或客户展示模型架构，便于技术交流和文档说明
- 模型格式转换验证：在不同框架间迁移模型时，验证转换后的结构是否正确无误



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,307 |
| 语言 | HTML |
| Forks | 19,744 |
| Issues | 12 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,483 |
| 语言 | Python |
| Forks | 32,307 |
| Issues | 2,278 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### photoprism/photoprism

**描述**: AI-Powered Photos App for the Decentralized Web 🌈💎✨

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,420 |
| 语言 | Go |
| Forks | 2,215 |
| Issues | 435 |
| Topics | ai, golang, google-photos, machine-learning, photography, private-cloud, self-hosted, tensorflow |
| 许可证 | Other |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,208 |
| 语言 | Python |
| Forks | 14,015 |
| Issues | 3,524 |
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
| Stars | 105,006 |
| 语言 | Python |
| Forks | 12,037 |
| Issues | 3,790 |
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
| Stars | 97,991 |
| 语言 | Python |
| Forks | 27,087 |
| Issues | 18,089 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### scikit-learn/scikit-learn

**描述**: scikit-learn: machine learning in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,306 |
| 语言 | Python |
| Forks | 26,749 |
| Issues | 2,133 |
| Topics | data-analysis, data-science, machine-learning, python, statistics |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### keras-team/keras

**描述**: Deep Learning for humans

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,912 |
| 语言 | Python |
| Forks | 19,713 |
| Issues | 277 |
| Topics | data-science, deep-learning, jax, machine-learning, neural-networks, python, pytorch, tensorflow |
| 许可证 | Apache License 2.0 |


## 🛠️ 开发工具 (18 个项目)


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,446 |
| 语言 | JavaScript |
| Forks | 7,738 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 代码助手打造的性能优化与能力增强系统，通过集成技能管理、记忆机制和安全防护，将 Claude Code 等工具从简单的代码生成器升级为具备自主学习和适应能力的智能开发伙伴。项目拥有超高人气（62K+ stars）和活跃的社区支持，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 多工具兼容性：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- 智能记忆系统：持久化存储上下文和学习数据，让 AI 能够记住项目历史和开发偏好
- 安全增强机制：内置企业级安全防护，确保 AI 代码生成符合安全规范和最佳实践
- 研究优先开发：采用实验性方法持续优化，紧跟 LLM 和 AI Agent 最新技术进展
- MCP 集成：原生支持 Model Context Protocol，实现与 AI 模型的深度协同

**适用场景**:
- 企业级 AI 开发团队：统一团队的 AI 编程助手配置，确保代码安全性和开发规范的统一执行
- 个人开发者效率提升：通过持久化记忆和技能定制，打造个性化的 AI 编程助手，大幅减少重复性工作
- AI Agent 研究与实验：为研究者和早期采用者提供测试平台，探索 AI Agent 在软件开发中的前沿应用



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,324 |
| 语言 | Go |
| Forks | 3,641 |
| Issues | 143 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 和 Claude 的开源替代方案，支持在消费级硬件上本地运行多种AI模型（无需GPU），为开发者和企业提供成本效益极高的AI解决方案。项目采用 Go 语言实现高性能推理服务，具备去中心化推理能力，已获得超过 4.3 万颗星，是构建私有化 AI 应用的理想选择。

**技术亮点**:
- 无需 GPU 即可在消费级硬件上运行，大幅降低 AI 部署成本
- 支持多种模型格式（gguf、transformers、diffusers）和主流模型（Llama、Mistral、Stable Diffusion 等）
- 提供与 OpenAI 兼容的 API 接口，实现零成本迁移
- 具备分布式、P2P 和去中心化推理能力，可横向扩展
- 集成 MCP（Model Context Protocol）协议，支持多模态生成（文本、音频、视频、图像、语音克隆）

**适用场景**:
- 企业内部私有化 AI 部署：在本地服务器部署 AI 服务，保障数据隐私和安全，避免敏感数据外泄至第三方 API
- 个人开发者本地开发环境：在个人电脑上构建和测试 AI 应用，无需承担 API 调用费用，支持离线开发
- 边缘计算和嵌入式场景：在资源受限设备上部署 AI 能力，利用无 GPU 优势实现本地化推理



### yamadashy/repomix

**描述**: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,260 |
| 语言 | TypeScript |
| Forks | 1,031 |
| Issues | 147 |
| Topics | ai, anthropic, artificial-intelligence, chatbot, chatgpt, claude, deepseek, developer-tools, gemini, genai, generative-ai, gpt, javascript, language-model, llama, llm, mcp, nodejs, openai, typescript |
| 许可证 | MIT License |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,652 |
| 语言 | Python |
| Forks | 8,570 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,460 |
| 语言 | TypeScript |
| Forks | 2,815 |
| Issues | 340 |
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
| Stars | 177,840 |
| 语言 | TypeScript |
| Forks | 55,477 |
| Issues | 1,411 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,941 |
| 语言 | Python |
| Forks | 8,789 |
| Issues | 144 |
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
| Stars | 73,409 |
| 语言 | Python |
| Forks | 8,711 |
| Issues | 202 |
| Topics | cli, cti, cybersecurity, forensics, hacktoberfest, information-gathering, infosec, linux, osint, pentesting, python, python3, reconnaissance, redteam, sherlock, tools |
| 许可证 | MIT License |


### localstack/localstack

**描述**: 💻 A fully functional local AWS cloud stack. Develop and test your cloud & Serverless apps offline

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,565 |
| 语言 | Python |
| Forks | 4,589 |
| Issues | 326 |
| Topics | aws, cloud, continuous-integration, developer-tools, localstack, python, testing |
| 许可证 | Other |


### microsoft/vscode

**描述**: Visual Studio Code

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 182,351 |
| 语言 | TypeScript |
| Forks | 38,314 |
| Issues | 14,704 |
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
| Stars | 93,726 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 286 |
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
| Stars | 78,178 |
| 语言 | TypeScript |
| Forks | 5,620 |
| Issues | 679 |
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
| Stars | 76,503 |
| 语言 | TypeScript |
| Forks | 6,538 |
| Issues | 169 |
| Topics | browser-ide, dev-tools, development-environment, ide, remote-work, vscode, vscode-remote |
| 许可证 | MIT License |


### microsoft/monaco-editor

**描述**: A browser based code editor

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,676 |
| 语言 | JavaScript |
| Forks | 3,999 |
| Issues | 822 |
| Topics | browser, editor, monaco-editor, typescript, vscode |
| 许可证 | MIT License |


### usebruno/bruno

**描述**: Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,445 |
| 语言 | JavaScript |
| Forks | 2,171 |
| Issues | 1,743 |
| Topics | api-client, api-testing, automation, developer-tools, git, graphql-client, http-client, javascript, openapi, openapi3, opensource, rest-api, testing, testing-tools |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,339 |
| 语言 | Go |
| Forks | 2,701 |
| Issues | 319 |
| Topics | bash, cli, fish, fzf, go, neovim, tmux, unix, vim, zsh |
| 许可证 | MIT License |


### cli/cli

**描述**: GitHub’s official command line tool

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,931 |
| 语言 | Go |
| Forks | 8,025 |
| Issues | 926 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ccxt/ccxt

**描述**: A cryptocurrency trading API with more than 100 exchanges in JavaScript / TypeScript / Python / C# / PHP / Go 

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,214 |
| 语言 | Go |
| Forks | 8,530 |
| Issues | 1,363 |
| Topics | altcoin, api, arbitrage, bitcoin, bot, btc, crypto, cryptocurrencies, cryptocurrency, eth, ethereum, exchange, invest, library, market-data, memecoin, merchant, strategy, trade, trading |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目)


### 🌟 高优先级


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,853 |
| 语言 | TypeScript |
| Forks | 3,390 |
| Issues | 178 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,460 |
| 语言 | TypeScript |
| Forks | 2,815 |
| Issues | 340 |
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
| Stars | 177,840 |
| 语言 | TypeScript |
| Forks | 55,477 |
| Issues | 1,411 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ToolJet/ToolJet

**描述**: ToolJet is the open-source foundation of ToolJet AI - the AI-native platform for building internal tools, dashboard, business applications, workflows and AI agents 🚀

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,548 |
| 语言 | JavaScript |
| Forks | 4,962 |
| Issues | 951 |
| Topics | ai-app-builder, docker, hacktoberfest, internal-applications, internal-project, internal-tool, internal-tools, javascript, kubernetes, low-code, low-code-development-platform, low-code-framework, no-code, nodejs, reactjs, self-hosted, typescript, web-development-tools, workflow-automation |
| 许可证 | GNU Affero General Public License v3.0 |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,617 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 223 |
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
| Stars | 120,955 |
| 语言 | Go |
| Forks | 42,602 |
| Issues | 2,683 |
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
| Stars | 71,483 |
| 语言 | Go |
| Forks | 18,913 |
| Issues | 3,788 |
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
| Stars | 54,123 |
| 语言 | Go |
| Forks | 6,427 |
| Issues | 2,849 |
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
| Stars | 93,726 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 286 |
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
| Stars | 83,607 |
| 语言 | TypeScript |
| Forks | 5,235 |
| Issues | 608 |
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
| Stars | 75,005 |
| 语言 | TypeScript |
| Forks | 6,358 |
| Issues | 410 |
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
| Stars | 83,671 |
| 语言 | JavaScript |
| Forks | 7,479 |
| Issues | 704 |
| Topics | docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring, webapp, websocket |
| 许可证 | MIT License |


### usebruno/bruno

**描述**: Opensource IDE For Exploring and Testing API's (lightweight alternative to Postman/Insomnia)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,445 |
| 语言 | JavaScript |
| Forks | 2,171 |
| Issues | 1,743 |
| Topics | api-client, api-testing, automation, developer-tools, git, graphql-client, http-client, javascript, openapi, openapi3, opensource, rest-api, testing, testing-tools |
| 许可证 | MIT License |


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,169 |
| 语言 | Go |
| Forks | 1,871 |
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
| Stars | 62,058 |
| 语言 | Go |
| Forks | 5,858 |
| Issues | 765 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### usememos/memos

**描述**: An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,522 |
| 语言 | Go |
| Forks | 4,154 |
| Issues | 19 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### istio/istio

**描述**: Connect, secure, control, and observe services.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,078 |
| 语言 | Go |
| Forks | 8,259 |
| Issues | 497 |
| Topics | api-management, circuit-breaker, consul, enforce-policies, envoy, fault-injection, kubernetes, lyft-envoy, microservice, microservices, nomad, polyglot-microservices, proxies, request-routing, resiliency, service-mesh |
| 许可证 | Apache License 2.0 |


## 📈 监控/观测 (3 个项目)


### 🌟 高优先级


### grafana/grafana

**描述**: The open and composable observability and data visualization platform. Visualize metrics, logs, and traces from multiple sources like Prometheus, Loki, Elasticsearch, InfluxDB, Postgres and many more. 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,514 |
| 语言 | TypeScript |
| Forks | 13,510 |
| Issues | 3,830 |
| Topics | alerting, analytics, business-intelligence, dashboard, data-visualization, elasticsearch, go, grafana, hacktoberfest, influxdb, metrics, monitoring, mysql, postgres, prometheus |
| 许可证 | GNU Affero General Public License v3.0 |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,671 |
| 语言 | JavaScript |
| Forks | 7,479 |
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
| Stars | 63,071 |
| 语言 | Go |
| Forks | 10,212 |
| Issues | 753 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (13 个项目)


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,324 |
| 语言 | Go |
| Forks | 3,641 |
| Issues | 143 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 和 Claude 的开源替代方案，支持在消费级硬件上本地运行多种AI模型（无需GPU），为开发者和企业提供成本效益极高的AI解决方案。项目采用 Go 语言实现高性能推理服务，具备去中心化推理能力，已获得超过 4.3 万颗星，是构建私有化 AI 应用的理想选择。

**技术亮点**:
- 无需 GPU 即可在消费级硬件上运行，大幅降低 AI 部署成本
- 支持多种模型格式（gguf、transformers、diffusers）和主流模型（Llama、Mistral、Stable Diffusion 等）
- 提供与 OpenAI 兼容的 API 接口，实现零成本迁移
- 具备分布式、P2P 和去中心化推理能力，可横向扩展
- 集成 MCP（Model Context Protocol）协议，支持多模态生成（文本、音频、视频、图像、语音克隆）

**适用场景**:
- 企业内部私有化 AI 部署：在本地服务器部署 AI 服务，保障数据隐私和安全，避免敏感数据外泄至第三方 API
- 个人开发者本地开发环境：在个人电脑上构建和测试 AI 应用，无需承担 API 调用费用，支持离线开发
- 边缘计算和嵌入式场景：在资源受限设备上部署 AI 能力，利用无 GPU 优势实现本地化推理



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,941 |
| 语言 | Python |
| Forks | 8,789 |
| Issues | 144 |
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
| Stars | 86,983 |
| 语言 | Python |
| Forks | 33,717 |
| Issues | 426 |
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
| Stars | 100,072 |
| 语言 | TypeScript |
| Forks | 27,099 |
| Issues | 1,129 |
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
| Stars | 78,178 |
| 语言 | TypeScript |
| Forks | 5,620 |
| Issues | 679 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### nestjs/nest

**描述**: A progressive Node.js framework for building efficient, scalable, and enterprise-grade server-side applications with TypeScript/JavaScript 🚀

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,868 |
| 语言 | TypeScript |
| Forks | 8,231 |
| Issues | 37 |
| Topics | framework, hacktoberfest, javascript, javascript-framework, microservices, nest, nestjs, node, nodejs, nodejs-framework, typescript, typescript-framework, websockets |
| 许可证 | MIT License |


### gatsbyjs/gatsby

**描述**: React-based framework with performance, scalability, and security built in.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,945 |
| 语言 | JavaScript |
| Forks | 10,219 |
| Issues | 343 |
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
| Stars | 51,732 |
| 语言 | JavaScript |
| Forks | 4,662 |
| Issues | 1,444 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### meteor/meteor

**描述**: Meteor, the JavaScript App Platform

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,779 |
| 语言 | JavaScript |
| Forks | 5,266 |
| Issues | 365 |
| Topics | build-system, framework, hacktoberfest, javascript, meteor, mongodb, nodejs, npm, react, reactive-programming, realtime, rpc, zero-configuration |
| 许可证 | Other |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,612 |
| 语言 | Go |
| Forks | 4,658 |
| Issues | 230 |
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
| Stars | 56,576 |
| 语言 | Go |
| Forks | 3,164 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ccxt/ccxt

**描述**: A cryptocurrency trading API with more than 100 exchanges in JavaScript / TypeScript / Python / C# / PHP / Go 

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,214 |
| 语言 | Go |
| Forks | 8,530 |
| Issues | 1,363 |
| Topics | altcoin, api, arbitrage, bitcoin, bot, btc, crypto, cryptocurrencies, cryptocurrency, eth, ethereum, exchange, invest, library, market-data, memecoin, merchant, strategy, trade, trading |
| 许可证 | MIT License |


### gofiber/fiber

**描述**: ⚡️ Express inspired web framework written in Go

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,338 |
| 语言 | Go |
| Forks | 1,961 |
| Issues | 43 |
| Topics | express, expressjs, fast, fiber, flexible, framework, friendly, go, golang, hacktoberfest, hacktoberfest2020, nodejs, performance, rest-api, web |
| 许可证 | MIT License |


## 📊 数据/基础设施 (6 个项目)


### 🌟 高优先级


### chroma-core/chroma

**描述**: Open-source search and retrieval database for AI applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,488 |
| 语言 | Rust |
| Forks | 2,090 |
| Issues | 506 |
| Topics | agents, ai, ai-agents, database, document-retrieval, embeddings, llm, llms, rag, rust, rust-lang, vector-database |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,606 |
| 语言 | TypeScript |
| Forks | 11,718 |
| Issues | 967 |
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
| Stars | 55,710 |
| 语言 | JavaScript |
| Forks | 6,023 |
| Issues | 299 |
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
| Stars | 43,164 |
| 语言 | Go |
| Forks | 3,869 |
| Issues | 1,049 |
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
| Stars | 51,617 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 223 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


### pingcap/tidb

**描述**: TiDB - the open-source, cloud-native, distributed SQL database designed for modern applications.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,872 |
| 语言 | Go |
| Forks | 6,125 |
| Issues | 5,763 |
| Topics | cloud-native, database, distributed-database, distributed-transactions, go, hacktoberfest, htap, mysql, mysql-compatibility, scale, serverless, sql, tidb |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (6 个项目)


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,307 |
| 语言 | HTML |
| Forks | 19,744 |
| Issues | 12 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,531 |
| 语言 | Python |
| Forks | 1,666 |
| Issues | 74 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,369 |
| 语言 | TypeScript |
| Forks | 9,883 |
| Issues | 2,238 |
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
| Stars | 86,512 |
| 语言 | TypeScript |
| Forks | 8,698 |
| Issues | 1,621 |
| Topics | diagrams, diagrams-as-code, documentation, flowchart, javascript, mindmap, typescript, uml-diagrams |
| 许可证 | MIT License |


### jaywcjlove/awesome-mac

**描述**:  Now we have become very big, Different from the original idea. Collect premium software in various categories.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,580 |
| 语言 | JavaScript |
| Forks | 7,448 |
| Issues | 203 |
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
| Stars | 166,678 |
| 语言 | Go |
| Forks | 13,014 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (52 个项目)


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 128,730 |
| 语言 | Unknown |
| Forks | 32,818 |
| Issues | 126 |
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
| Stars | 40,874 |
| 语言 | TypeScript |
| Forks | 3,769 |
| Issues | 665 |
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
| Stars | 268,910 |
| 语言 | TypeScript |
| Forks | 51,378 |
| Issues | 12,818 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### danielmiessler/Fabric

**描述**: Fabric is an open-source framework for augmenting humans using AI. It provides a modular system for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,528 |
| 语言 | Go |
| Forks | 3,947 |
| Issues | 23 |
| Topics | ai, augmentation, flourishing, life, work |
| 许可证 | MIT License |


### ansible/ansible

**描述**: Ansible is a radically simple IT automation platform that makes your applications and systems easier to deploy and maintain. Automate everything from code deployment to network configuration to cloud management, in a language that approaches plain English, using SSH, with no agents to install on remote systems. https://docs.ansible.com.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,212 |
| 语言 | Python |
| Forks | 24,179 |
| Issues | 826 |
| Topics | ansible, python |
| 许可证 | GNU General Public License v3.0 |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,447 |
| 语言 | Python |
| Forks | 6,273 |
| Issues | 272 |
| 许可证 | Apache License 2.0 |


### opendatalab/MinerU

**描述**: Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,600 |
| 语言 | Python |
| Forks | 4,606 |
| Issues | 191 |
| Topics | ai4science, document-analysis, extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-extractor-llm, pdf-extractor-pretrain, pdf-extractor-rag, pdf-parser, python |
| 许可证 | GNU Affero General Public License v3.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,515 |
| 语言 | Python |
| Forks | 6,357 |
| Issues | 633 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,501 |
| 语言 | Python |
| Forks | 1,611 |
| Issues | 36 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### iptv-org/iptv

**描述**: Collection of publicly available IPTV channels from all over the world

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,460 |
| 语言 | TypeScript |
| Forks | 5,675 |
| Issues | 298 |
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
| Stars | 100,772 |
| 语言 | TypeScript |
| Forks | 7,332 |
| Issues | 173 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### abi/screenshot-to-code

**描述**: Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue)

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,802 |
| 语言 | TypeScript |
| Forks | 8,859 |
| Issues | 117 |
| 许可证 | MIT License |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,889 |
| 语言 | Go |
| Forks | 10,235 |
| Issues | 1,913 |
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
| Stars | 96,908 |
| 语言 | C++ |
| Forks | 15,266 |
| Issues | 1,206 |
| Topics | ggml |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,167 |
| 语言 | Python |
| Forks | 36,918 |
| Issues | 3,513 |
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
| Forks | 45,255 |
| Issues | 1,282 |
| 许可证 | Other |


### python/cpython

**描述**: The Python programming language

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,856 |
| 语言 | Python |
| Forks | 34,182 |
| Issues | 9,285 |
| 许可证 | Other |


### commaai/openpilot

**描述**: openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,235 |
| 语言 | Python |
| Forks | 10,674 |
| Issues | 278 |
| Topics | advanced-driver-assistance-systems, driver-assistance-systems, robotics |
| 许可证 | MIT License |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 437,833 |
| 语言 | TypeScript |
| Forks | 43,522 |
| Issues | 277 |
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
| Stars | 350,289 |
| 语言 | TypeScript |
| Forks | 43,739 |
| Issues | 40 |
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
| Stars | 118,127 |
| 语言 | TypeScript |
| Forks | 12,754 |
| Issues | 2,843 |
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
| Stars | 107,808 |
| 语言 | TypeScript |
| Forks | 8,014 |
| Issues | 1,763 |
| Topics | base-ui, components, nextjs, radix-ui, react, shadcn, tailwindcss, ui |
| 许可证 | MIT License |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,676 |
| 语言 | TypeScript |
| Forks | 54,549 |
| Issues | 1,378 |
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
| Stars | 94,124 |
| 语言 | TypeScript |
| Forks | 5,016 |
| Issues | 654 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,927 |
| 语言 | TypeScript |
| Forks | 7,572 |
| Issues | 38 |
| 许可证 | MIT License |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,629 |
| 语言 | TypeScript |
| Forks | 7,880 |
| Issues | 629 |
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
| Stars | 243,660 |
| 语言 | JavaScript |
| Forks | 50,654 |
| Issues | 1,148 |
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
| Stars | 138,178 |
| 语言 | JavaScript |
| Forks | 30,556 |
| Issues | 3,422 |
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
| Stars | 116,102 |
| 语言 | JavaScript |
| Forks | 34,938 |
| Issues | 2,504 |
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
| Stars | 111,197 |
| 语言 | JavaScript |
| Forks | 36,281 |
| Issues | 597 |
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
| Stars | 108,588 |
| 语言 | JavaScript |
| Forks | 11,534 |
| Issues | 349 |
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
| Stars | 98,009 |
| 语言 | JavaScript |
| Forks | 32,714 |
| Issues | 1,721 |
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
| Stars | 95,390 |
| 语言 | JavaScript |
| Forks | 15,202 |
| Issues | 37 |
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
| Stars | 86,007 |
| 语言 | JavaScript |
| Forks | 4,793 |
| Issues | 976 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,023 |
| 语言 | JavaScript |
| Forks | 9,306 |
| Issues | 206 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,930 |
| 语言 | JavaScript |
| Forks | 10,587 |
| Issues | 484 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,973 |
| 语言 | JavaScript |
| Forks | 11,354 |
| Issues | 361 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### parcel-bundler/parcel

**描述**: The zero configuration build tool for the web. 📦🚀

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,048 |
| 语言 | JavaScript |
| Forks | 2,277 |
| Issues | 591 |
| Topics | assets, build-tool, commonjs, compiler, css, es6, html, javascript, module-bundler, modules, web |
| 许可证 | MIT License |


### nwjs/nw.js

**描述**: Call all Node.js modules directly from DOM/WebWorker and enable a new way of writing applications with all Web technologies.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,565 |
| 语言 | JavaScript |
| Forks | 3,871 |
| Issues | 959 |
| Topics | desktop, javascript, node-webkit, nodejs, nwjs, web-application-framework |
| 许可证 | MIT License |


### dcloudio/uni-app

**描述**: A cross-platform framework using Vue.js

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,446 |
| 语言 | JavaScript |
| Forks | 3,717 |
| Issues | 716 |
| Topics | android, cross-platform, crossplatform, hbuilderx, ios, javascript, miniprogram, uni, uni-app, uniapp, vue, vue3 |
| 许可证 | Apache License 2.0 |


### zen-browser/desktop

**描述**: Welcome to a calmer internet

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,484 |
| 语言 | JavaScript |
| Forks | 1,358 |
| Issues | 529 |
| Topics | firefox, firefox-based, firefox-browser, zen-browser |
| 许可证 | Mozilla Public License 2.0 |


### HeyPuter/puter

**描述**: 🌐 The Internet Computer! Free, Open-Source, and Self-Hostable.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,816 |
| 语言 | JavaScript |
| Forks | 3,527 |
| Issues | 193 |
| Topics | cloud, cloud-os, cloud-storage, desktop, desktop-environment, dropbox, good-first-issue, gui, javascript, nas, open-source, operating-system, os, osjs, puter, remote-desktop, storage, web-desktop, web-os, webtop |
| 许可证 | GNU Affero General Public License v3.0 |


### phaserjs/phaser

**描述**: Phaser is a fun, free and fast 2D game framework for making HTML5 games for desktop and mobile web browsers, supporting Canvas and WebGL rendering.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,129 |
| 语言 | JavaScript |
| Forks | 7,129 |
| Issues | 114 |
| Topics | canvas, discord-activities, facebook-instant-games, game-development, game-frameworks, gamedev, html5-game-development, javascript, phaser, phaser-development, phaserjs, webgl, youtube-playables |
| 许可证 | MIT License |


### fastify/fastify

**描述**: Fast and low overhead web framework, for Node.js

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,755 |
| 语言 | JavaScript |
| Forks | 2,607 |
| Issues | 125 |
| Topics | hacktoberfest, nodejs, performance, speed, webframework |
| 许可证 | MIT License |


### sahat/hackathon-starter

**描述**: A boilerplate for Node.js web applications

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,211 |
| 语言 | JavaScript |
| Forks | 8,180 |
| Issues | 1 |
| Topics | boilerplate, hackathon, hacktoberfest, nodejs, oauth2, starter-kit |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,914 |
| 语言 | Go |
| Forks | 18,842 |
| Issues | 9,826 |
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
| Stars | 104,921 |
| 语言 | Go |
| Forks | 14,921 |
| Issues | 40 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### syncthing/syncthing

**描述**: Open Source Continuous File Synchronization

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,551 |
| 语言 | Go |
| Forks | 4,947 |
| Issues | 403 |
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
| Stars | 68,707 |
| 语言 | Go |
| Forks | 3,215 |
| Issues | 15 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,874 |
| 语言 | Go |
| Forks | 4,946 |
| Issues | 1,130 |
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
| Stars | 50,892 |
| 语言 | Go |
| Forks | 21,827 |
| Issues | 390 |
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
| Stars | 49,114 |
| 语言 | Go |
| Forks | 7,983 |
| Issues | 577 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |
