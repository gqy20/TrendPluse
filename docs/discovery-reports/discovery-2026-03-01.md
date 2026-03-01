# 项目发现报告 (2026-03-01)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 147 |
| 去重移除 | 35 |
| 已在监控 | 18 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 18 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 14 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 16 |
| 📊 数据/基础设施 | 5 |
| 📚 学习资源 | 8 |
| 📁 其他 | 57 |

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


## 🤖 AI Agents (28 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,300 |
| 语言 | Python |
| Forks | 17,744 |
| Issues | 260 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源AI聊天界面项目之一（12.5万+星标），提供了类似ChatGPT的现代化用户界面，支持Ollama、OpenAI等多种LLM后端。它让用户能够以完全自主可控的方式部署私有AI服务，无需依赖云端API，是构建个人或企业级AI应用的最佳解决方案之一。

**技术亮点**:
- 🔌 多后端支持：无缝集成Ollama、OpenAI API等多种LLM提供商，轻松切换不同模型
- 🔒 完全自托管：所有数据本地存储，支持离线部署，保障数据隐私和安全
- 🎨 现代化界面：提供类似ChatGPT的用户体验，支持流式响应、代码高亮、Markdown渲染
- 🤖 RAG集成：内置检索增强生成功能，支持文档上传和知识库构建
- 🧩 MCP协议支持：原生支持Model Context Protocol，可扩展模型上下文能力

**适用场景**:
- 🏢 **企业私有AI部署**：在企业内部环境中部署安全的AI助手，保护敏感数据不外泄
- 👨‍💻 **开发者本地测试**：配合Ollama在本地测试不同LLM模型，快速验证AI应用原型
- 🎓 **教育与学习场景**：学校或培训机构部署教学用AI平台，为学生提供可控的AI交互环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,950 |
| 语言 | Python |
| Forks | 8,223 |
| Issues | 3,007 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是领先的 RAG 引擎开源项目，深度融合 Agent 能力为大模型构建卓越的上下文层，获得超 7.3 万星标。其独特价值在于将文档解析、GraphRAG、MCP 协议等多种前沿技术一体化，为 LLM 应用提供从数据接入到智能检索的完整解决方案。

**技术亮点**:
- 🔀 融合 RAG 与 Agent 能力，构建 Agentic AI 工作流的上下文层
- 🧠 支持 GraphRAG 知识图谱检索，提供更深层的语义理解能力
- 📄 强大的文档解析引擎（document-parser），支持多种格式文档理解
- 🔌 兼容 MCP 协议与 DeepSeek、Ollama、OpenAI 等主流 LLM 接口
- 🤖 智能上下文工程（context-engineering）优化，支持深度研究场景

**适用场景**:
- 🏢 企业知识库搭建：将企业文档转化为可检索的知识库，为 LLM 提供精准上下文
- 🔍 AI 搜索引擎增强：通过 RAG 技术提升搜索结果的准确性和相关性
- 🤝 Agent 应用开发：为 Agentic AI 应用提供可靠的上下文信息层，支持复杂任务编排



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,698 |
| 语言 | Python |
| Forks | 8,256 |
| Issues | 910 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是ACL 2024论文项目，是当前最全面的LLM/VLM统一微调框架，支持100+大模型的统一高效微调。该项目采用低代码设计理念，通过WebUI界面让零基础用户也能轻松上手，在开源社区获得极高认可度（67K+ stars），是个人开发者和企业进行模型微调的首选工具。

**技术亮点**:
- 统一支持100+种大模型，涵盖GPT、Llama、Qwen、DeepSeek、Gemma、Yi等主流LLM和VLM系列
- 高效微调技术栈完整，支持LoRA、QLoRA、MoE、全量微调等多种PEFT方法及量化技术
- 内置RLHF（人类反馈强化学习）和指令微调能力，可定制化训练垂直领域模型
- 提供WebUI可视化界面和命令行工具，降低AI模型微调的技术门槛，开箱即用
- 支持Agent开发和对话系统集成，可直接将训练好的模型部署为智能助手应用

**适用场景**:
- 企业AI应用落地：快速基于开源模型训练专属行业知识模型（如医疗、法律、金融垂直领域模型）
- 学术研究与实验：研究人员可复现ACL 2024论文方法，对比不同微调策略效果，加速NLP研究进程
- 个人开发者学习AI：通过可视化界面学习LLM微调流程，低成本开发个人AI助手或聊天机器人应用



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,931 |
| 语言 | TypeScript |
| Forks | 6,189 |
| Issues | 200 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前 GitHub 上最受欢迎的 AI 网页数据提取工具（8.6万+ stars），专门为大语言模型优化，能将整个网站转换为 LLM 友好的 Markdown 或结构化数据。该项目解决了 AI 应用开发中最大的痛点——高质量网页数据获取，是构建 AI Agent、RAG 系统和智能搜索引擎的基础设施级工具。

**技术亮点**:
- 一键将整个网站爬取并转换为 LLM-ready 的 Markdown 格式，保留关键语义信息
- 提供强大的 AI 驱动数据提取能力，支持从复杂网页中抽取结构化数据
- 内置智能爬虫系统，能够处理动态内容、JavaScript 渲染页面和反爬机制
- 提供完整的 API 和 SDK 支持（TypeScript/Python），易于集成到现有 AI 应用中
- 支持批量处理和增量爬取，适合大规模网站数据采集需求

**适用场景**:
- 构建 AI Agent 和 RAG 应用：为大语言模型提供高质量的网页知识源，支持智能问答、知识库构建等场景
- 企业数据挖掘与竞争情报：批量抓取竞争对手网站、行业资讯，将非结构化网页转换为结构化数据进行市场分析
- 内容聚合与搜索引擎：开发垂直领域搜索引擎或内容聚合平台，需要高效爬取和处理大量网站数据



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,607 |
| 语言 | JavaScript |
| Forks | 6,835 |
| Issues | 22 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code 的智能代理性能优化系统，集成了技能学习、记忆管理、安全机制和研究驱动开发模式。在 GitHub 上获得超过 5.5 万颗星，证明了其在 AI 辅助开发工具领域的极高价值和实用性，特别适合需要深度集成 Claude 能力的开发者使用。

**技术亮点**:
- 🤖 智能 AI Agent 架构：为 Claude Code、Codex 等提供技能和本能增强系统
- 🧠 持久化记忆管理：实现 Agent 的长期学习和上下文记忆能力
- 🔒 企业级安全机制：内置安全防护层，保障 AI 交互的安全性
- 📊 性能优化系统：专门针对 Agent 性能进行深度优化和调优
- 🔌 MCP 协议支持：基于 Model Context Protocol 实现可扩展的插件生态

**适用场景**:
- 🚀 个人开发者提升效率：作为 AI 编程助手增强工具，加速日常代码开发、调试和重构流程
- 🏢 企业级 AI 研发团队：集成到内部开发工作流，构建智能化的代码审查、文档生成和技术研究系统
- 🛠️ AI Agent 二次开发：基于该项目框架，快速定制和开发专属的 AI 编程助手或自动化工具



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,224 |
| 语言 | JavaScript |
| Forks | 5,967 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款功能最全面的本地 AI 应用平台，完美融合了 RAG、AI Agents、MCP 协议支持和无代码构建器等企业级特性。它支持超过 50 种 LLM 提供商（包括 DeepSeek、Kimi、Llama3、Qwen3 等），提供桌面应用和 Docker 两种部署方式，既能满足个人开发者本地部署需求，也能作为企业级的 AI 应用解决方案，是构建私有化 AI 助手的理想选择。

**技术亮点**:
- 内置完整的 RAG 引擎，支持文档解析、向量化存储和智能检索
- 支持 MCP (Model Context Protocol) 协议，可扩展连接 700+ MCP 服务器
- 无代码 Agent 构建器，可视化创建自定义 AI 智能体
- 多模态能力支持，兼容 50+ LLM 提供商（Ollama、LM Studio、LocalAI 等）
- 提供 Web Scraping 和 Vector Database 集成，支持多数据源接入

**适用场景**:
- 企业级私有化 AI 知识库与客服系统搭建
- 个人开发者在本地环境构建和调试 AI Agent 应用
- 快速构建基于 RAG 的智能文档问答和内容分析工具



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,162 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 151 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 的免费开源替代方案，无需 GPU 即可在消费级硬件上运行，支持本地部署多种 AI 模型（包括 LLM、图像生成、音频生成等），为企业提供数据隐私和成本控制的双重优势。作为 drop-in replacement，它与 OpenAI API 完全兼容，同时支持分布式和 P2P 推理，实现去中心化的 AI 能力部署。

**技术亮点**:
- Drop-in replacement for OpenAI API：无需修改代码即可从 OpenAI 迁移到本地部署，降低迁移成本
- 多模型架构支持：支持 GGUF、Transformers、Diffusers 等多种模型格式，涵盖 Llama、Mistral、Gemma、Stable Diffusion、Whisper 等主流模型
- 零 GPU 需求：CPU 即可运行推理任务，降低硬件门槛和部署成本，适合普通开发者和中小企业
- 分布式与 P2P 推理：基于 libp2p 实现去中心化推理，支持多节点协同处理，提升可扩展性
- 多模态能力：支持文本、图像、音频、视频生成，以及语音克隆、目标检测、Rerank 等丰富功能，并提供 MCP 协议支持

**适用场景**:
- 企业内部 AI 能力部署：金融、医疗、法律等行业对数据敏感的企业可在本地或私有云部署 AI 服务，确保数据不外泄，同时避免 API 调用成本；可集成到现有业务系统中提供智能客服、文档分析、内容生成等能力
- 个人开发者与初创公司：在消费级硬件上快速搭建本地 AI 开发环境，进行模型测试、应用原型开发，无需承担高昂的 GPU 和云服务成本
- 离线与边缘计算场景：支持在无网络环境或边缘设备上运行 AI 推理，适合工业现场、野外作业、物联网设备等场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,826 |
| 语言 | TypeScript |
| Forks | 14,695 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开创性的多智能体协作平台，革新了人机交互模式，将"智能体"作为工作交互的基本单元。该项目在 GitHub 上获得 7.2 万+ stars，集成了 ChatGPT、Claude、DeepSeek 等主流 AI 模型，为用户提供了构建、管理和与 AI 智能体团队协作的一站式解决方案。

**技术亮点**:
- 多智能体协作架构：支持多个 AI agent 协同工作，实现复杂的任务自动化和智能编排
- Agent-First 设计理念：将智能体作为工作交互的核心单元，提供可视化的团队设计能力
- 多模型集成支持：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 知识库与 MCP 协议支持：内置知识库管理，支持 Model Context Protocol 实现上下文增强
- TypeScript 技术栈：使用现代化技术构建，确保代码质量和可维护性

**适用场景**:
- 企业级 AI 助手团队：为企业构建智能客服、数据分析、内容创作等 AI 智能体团队，提升团队协作效率
- 个人开发者 AI 工作流：个人用户可定制专属 AI 助手组合，用于代码开发、文档编写、学习辅导等日常任务
- 知识管理与问答系统：利用知识库功能构建企业知识库或学习助手，实现智能信息检索和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,959 |
| 语言 | MDX |
| Forks | 7,554 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是 GitHub 上最受欢迎的 Prompt Engineering 资源库（超过 7 万 stars），由 dair-ai 团队维护，系统性地整理了提示词工程、RAG、AI Agents 等前沿 AI 技术的完整学习体系，涵盖了从入门教程到最新研究论文的全链路内容，是开发者快速掌握 AI 应用开发核心技能的权威指南。

**技术亮点**:
- 全栈式覆盖：整合 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 多模态学习资源：包含指南文档、学术论文、实践课程、Jupyter Notebook 等多种形式的学习材料
- 紧跟技术前沿：涵盖 LLMs、OpenAI、ChatGPT、Generative AI 等最新技术栈和深度学习应用
- 技术标签全面：覆盖 agent、rag、prompt-engineering、llms 等热门 AI 开发关键词体系

**适用场景**:
- AI 应用开发者：需要系统学习提示词工程、RAG 检索增强生成、AI 智能体开发等核心技术的工程师
- 企业 AI 转型团队：寻找到大语言模型落地方案，需要参考最佳实践和架构设计的技术团队
- AI 研究人员和学生：跟踪最新论文和技术进展，深入学习生成式 AI 原理的学术群体



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,304 |
| 语言 | Java |
| Forks | 15,824 |
| Issues | 54 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,602 |
| 语言 | Python |
| Forks | 6,116 |
| Issues | 191 |
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
| Stars | 41,661 |
| 语言 | Python |
| Forks | 9,778 |
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
| Stars | 34,223 |
| 语言 | TypeScript |
| Forks | 6,909 |
| Issues | 423 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,948 |
| 语言 | TypeScript |
| Forks | 2,181 |
| Issues | 61 |
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
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
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
| Stars | 22,157 |
| 语言 | TypeScript |
| Forks | 1,027 |
| Issues | 146 |
| Topics | ai, anthropic, artificial-intelligence, chatbot, chatgpt, claude, deepseek, developer-tools, gemini, genai, generative-ai, gpt, javascript, language-model, llama, llm, mcp, nodejs, openai, typescript |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,916 |
| 语言 | Jupyter Notebook |
| Forks | 5,033 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,768 |
| 语言 | TypeScript |
| Forks | 3,373 |
| Issues | 170 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### datawhalechina/happy-llm

**描述**: 📚 从零开始的大语言模型原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,394 |
| 语言 | Jupyter Notebook |
| Forks | 2,450 |
| Issues | 42 |
| Topics | agent, llm, rag |
| 许可证 | Other |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,352 |
| 语言 | Python |
| Forks | 8,530 |
| Issues | 361 |
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
| Stars | 35,719 |
| 语言 | TypeScript |
| Forks | 2,706 |
| Issues | 276 |
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
| Stars | 79,262 |
| 语言 | Python |
| Forks | 9,373 |
| Issues | 267 |
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
| Stars | 49,440 |
| 语言 | TypeScript |
| Forks | 23,763 |
| Issues | 778 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### BloopAI/vibe-kanban

**描述**: Get 10X more out of Claude Code, Codex or any coding agent

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,120 |
| 语言 | Rust |
| Forks | 2,124 |
| Issues | 402 |
| Topics | agent, ai-agents, kanban, management, task-manager |
| 许可证 | Apache License 2.0 |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 176,967 |
| 语言 | TypeScript |
| Forks | 55,289 |
| Issues | 1,416 |
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
| Stars | 145,165 |
| 语言 | Python |
| Forks | 8,500 |
| Issues | 1,073 |
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
| Stars | 51,932 |
| 语言 | Jupyter Notebook |
| Forks | 18,180 |
| Issues | 1 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,067 |
| 语言 | TypeScript |
| Forks | 1,354 |
| Issues | 276 |
| Topics | ai-tools, claude-code, codex, desktop-app, kimi-k2-thiking, mcp, minimax, open-source, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
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
| Stars | 125,300 |
| 语言 | Python |
| Forks | 17,744 |
| Issues | 260 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源AI聊天界面项目之一（12.5万+星标），提供了类似ChatGPT的现代化用户界面，支持Ollama、OpenAI等多种LLM后端。它让用户能够以完全自主可控的方式部署私有AI服务，无需依赖云端API，是构建个人或企业级AI应用的最佳解决方案之一。

**技术亮点**:
- 🔌 多后端支持：无缝集成Ollama、OpenAI API等多种LLM提供商，轻松切换不同模型
- 🔒 完全自托管：所有数据本地存储，支持离线部署，保障数据隐私和安全
- 🎨 现代化界面：提供类似ChatGPT的用户体验，支持流式响应、代码高亮、Markdown渲染
- 🤖 RAG集成：内置检索增强生成功能，支持文档上传和知识库构建
- 🧩 MCP协议支持：原生支持Model Context Protocol，可扩展模型上下文能力

**适用场景**:
- 🏢 **企业私有AI部署**：在企业内部环境中部署安全的AI助手，保护敏感数据不外泄
- 👨‍💻 **开发者本地测试**：配合Ollama在本地测试不同LLM模型，快速验证AI应用原型
- 🎓 **教育与学习场景**：学校或培训机构部署教学用AI平台，为学生提供可控的AI交互环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,950 |
| 语言 | Python |
| Forks | 8,223 |
| Issues | 3,007 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是领先的 RAG 引擎开源项目，深度融合 Agent 能力为大模型构建卓越的上下文层，获得超 7.3 万星标。其独特价值在于将文档解析、GraphRAG、MCP 协议等多种前沿技术一体化，为 LLM 应用提供从数据接入到智能检索的完整解决方案。

**技术亮点**:
- 🔀 融合 RAG 与 Agent 能力，构建 Agentic AI 工作流的上下文层
- 🧠 支持 GraphRAG 知识图谱检索，提供更深层的语义理解能力
- 📄 强大的文档解析引擎（document-parser），支持多种格式文档理解
- 🔌 兼容 MCP 协议与 DeepSeek、Ollama、OpenAI 等主流 LLM 接口
- 🤖 智能上下文工程（context-engineering）优化，支持深度研究场景

**适用场景**:
- 🏢 企业知识库搭建：将企业文档转化为可检索的知识库，为 LLM 提供精准上下文
- 🔍 AI 搜索引擎增强：通过 RAG 技术提升搜索结果的准确性和相关性
- 🤝 Agent 应用开发：为 Agentic AI 应用提供可靠的上下文信息层，支持复杂任务编排



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,224 |
| 语言 | JavaScript |
| Forks | 5,967 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款功能最全面的本地 AI 应用平台，完美融合了 RAG、AI Agents、MCP 协议支持和无代码构建器等企业级特性。它支持超过 50 种 LLM 提供商（包括 DeepSeek、Kimi、Llama3、Qwen3 等），提供桌面应用和 Docker 两种部署方式，既能满足个人开发者本地部署需求，也能作为企业级的 AI 应用解决方案，是构建私有化 AI 助手的理想选择。

**技术亮点**:
- 内置完整的 RAG 引擎，支持文档解析、向量化存储和智能检索
- 支持 MCP (Model Context Protocol) 协议，可扩展连接 700+ MCP 服务器
- 无代码 Agent 构建器，可视化创建自定义 AI 智能体
- 多模态能力支持，兼容 50+ LLM 提供商（Ollama、LM Studio、LocalAI 等）
- 提供 Web Scraping 和 Vector Database 集成，支持多数据源接入

**适用场景**:
- 企业级私有化 AI 知识库与客服系统搭建
- 个人开发者在本地环境构建和调试 AI Agent 应用
- 快速构建基于 RAG 的智能文档问答和内容分析工具



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,826 |
| 语言 | TypeScript |
| Forks | 14,695 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开创性的多智能体协作平台，革新了人机交互模式，将"智能体"作为工作交互的基本单元。该项目在 GitHub 上获得 7.2 万+ stars，集成了 ChatGPT、Claude、DeepSeek 等主流 AI 模型，为用户提供了构建、管理和与 AI 智能体团队协作的一站式解决方案。

**技术亮点**:
- 多智能体协作架构：支持多个 AI agent 协同工作，实现复杂的任务自动化和智能编排
- Agent-First 设计理念：将智能体作为工作交互的核心单元，提供可视化的团队设计能力
- 多模型集成支持：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 知识库与 MCP 协议支持：内置知识库管理，支持 Model Context Protocol 实现上下文增强
- TypeScript 技术栈：使用现代化技术构建，确保代码质量和可维护性

**适用场景**:
- 企业级 AI 助手团队：为企业构建智能客服、数据分析、内容创作等 AI 智能体团队，提升团队协作效率
- 个人开发者 AI 工作流：个人用户可定制专属 AI 助手组合，用于代码开发、文档编写、学习辅导等日常任务
- 知识管理与问答系统：利用知识库功能构建企业知识库或学习助手，实现智能信息检索和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,959 |
| 语言 | MDX |
| Forks | 7,554 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是 GitHub 上最受欢迎的 Prompt Engineering 资源库（超过 7 万 stars），由 dair-ai 团队维护，系统性地整理了提示词工程、RAG、AI Agents 等前沿 AI 技术的完整学习体系，涵盖了从入门教程到最新研究论文的全链路内容，是开发者快速掌握 AI 应用开发核心技能的权威指南。

**技术亮点**:
- 全栈式覆盖：整合 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 多模态学习资源：包含指南文档、学术论文、实践课程、Jupyter Notebook 等多种形式的学习材料
- 紧跟技术前沿：涵盖 LLMs、OpenAI、ChatGPT、Generative AI 等最新技术栈和深度学习应用
- 技术标签全面：覆盖 agent、rag、prompt-engineering、llms 等热门 AI 开发关键词体系

**适用场景**:
- AI 应用开发者：需要系统学习提示词工程、RAG 检索增强生成、AI 智能体开发等核心技术的工程师
- 企业 AI 转型团队：寻找到大语言模型落地方案，需要参考最佳实践和架构设计的技术团队
- AI 研究人员和学生：跟踪最新论文和技术进展，深入学习生成式 AI 原理的学术群体



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,304 |
| 语言 | Java |
| Forks | 15,824 |
| Issues | 54 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,602 |
| 语言 | Python |
| Forks | 6,116 |
| Issues | 191 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,948 |
| 语言 | TypeScript |
| Forks | 2,181 |
| Issues | 61 |
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
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,916 |
| 语言 | Jupyter Notebook |
| Forks | 5,033 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,768 |
| 语言 | TypeScript |
| Forks | 3,373 |
| Issues | 170 |
| Topics | agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation, chatbot, deepseek, gemini, low-code, nextjs, no-code, openai, rag, react, typescript |
| 许可证 | Apache License 2.0 |


### datawhalechina/happy-llm

**描述**: 📚 从零开始的大语言模型原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,394 |
| 语言 | Jupyter Notebook |
| Forks | 2,450 |
| Issues | 42 |
| Topics | agent, llm, rag |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,343 |
| 语言 | TypeScript |
| Forks | 11,674 |
| Issues | 1,006 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,385 |
| 语言 | Python |
| Forks | 9,875 |
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
| Stars | 49,440 |
| 语言 | TypeScript |
| Forks | 23,763 |
| Issues | 778 |
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
| Stars | 43,056 |
| 语言 | Go |
| Forks | 3,859 |
| Issues | 1,031 |
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
| Stars | 31,151 |
| 语言 | Python |
| Forks | 3,279 |
| Issues | 60 |
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
| Stars | 28,846 |
| 语言 | Python |
| Forks | 4,129 |
| Issues | 193 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (24 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,300 |
| 语言 | Python |
| Forks | 17,744 |
| Issues | 260 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源AI聊天界面项目之一（12.5万+星标），提供了类似ChatGPT的现代化用户界面，支持Ollama、OpenAI等多种LLM后端。它让用户能够以完全自主可控的方式部署私有AI服务，无需依赖云端API，是构建个人或企业级AI应用的最佳解决方案之一。

**技术亮点**:
- 🔌 多后端支持：无缝集成Ollama、OpenAI API等多种LLM提供商，轻松切换不同模型
- 🔒 完全自托管：所有数据本地存储，支持离线部署，保障数据隐私和安全
- 🎨 现代化界面：提供类似ChatGPT的用户体验，支持流式响应、代码高亮、Markdown渲染
- 🤖 RAG集成：内置检索增强生成功能，支持文档上传和知识库构建
- 🧩 MCP协议支持：原生支持Model Context Protocol，可扩展模型上下文能力

**适用场景**:
- 🏢 **企业私有AI部署**：在企业内部环境中部署安全的AI助手，保护敏感数据不外泄
- 👨‍💻 **开发者本地测试**：配合Ollama在本地测试不同LLM模型，快速验证AI应用原型
- 🎓 **教育与学习场景**：学校或培训机构部署教学用AI平台，为学生提供可控的AI交互环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,950 |
| 语言 | Python |
| Forks | 8,223 |
| Issues | 3,007 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是领先的 RAG 引擎开源项目，深度融合 Agent 能力为大模型构建卓越的上下文层，获得超 7.3 万星标。其独特价值在于将文档解析、GraphRAG、MCP 协议等多种前沿技术一体化，为 LLM 应用提供从数据接入到智能检索的完整解决方案。

**技术亮点**:
- 🔀 融合 RAG 与 Agent 能力，构建 Agentic AI 工作流的上下文层
- 🧠 支持 GraphRAG 知识图谱检索，提供更深层的语义理解能力
- 📄 强大的文档解析引擎（document-parser），支持多种格式文档理解
- 🔌 兼容 MCP 协议与 DeepSeek、Ollama、OpenAI 等主流 LLM 接口
- 🤖 智能上下文工程（context-engineering）优化，支持深度研究场景

**适用场景**:
- 🏢 企业知识库搭建：将企业文档转化为可检索的知识库，为 LLM 提供精准上下文
- 🔍 AI 搜索引擎增强：通过 RAG 技术提升搜索结果的准确性和相关性
- 🤝 Agent 应用开发：为 Agentic AI 应用提供可靠的上下文信息层，支持复杂任务编排



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,607 |
| 语言 | JavaScript |
| Forks | 6,835 |
| Issues | 22 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code 的智能代理性能优化系统，集成了技能学习、记忆管理、安全机制和研究驱动开发模式。在 GitHub 上获得超过 5.5 万颗星，证明了其在 AI 辅助开发工具领域的极高价值和实用性，特别适合需要深度集成 Claude 能力的开发者使用。

**技术亮点**:
- 🤖 智能 AI Agent 架构：为 Claude Code、Codex 等提供技能和本能增强系统
- 🧠 持久化记忆管理：实现 Agent 的长期学习和上下文记忆能力
- 🔒 企业级安全机制：内置安全防护层，保障 AI 交互的安全性
- 📊 性能优化系统：专门针对 Agent 性能进行深度优化和调优
- 🔌 MCP 协议支持：基于 Model Context Protocol 实现可扩展的插件生态

**适用场景**:
- 🚀 个人开发者提升效率：作为 AI 编程助手增强工具，加速日常代码开发、调试和重构流程
- 🏢 企业级 AI 研发团队：集成到内部开发工作流，构建智能化的代码审查、文档生成和技术研究系统
- 🛠️ AI Agent 二次开发：基于该项目框架，快速定制和开发专属的 AI 编程助手或自动化工具



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,224 |
| 语言 | JavaScript |
| Forks | 5,967 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款功能最全面的本地 AI 应用平台，完美融合了 RAG、AI Agents、MCP 协议支持和无代码构建器等企业级特性。它支持超过 50 种 LLM 提供商（包括 DeepSeek、Kimi、Llama3、Qwen3 等），提供桌面应用和 Docker 两种部署方式，既能满足个人开发者本地部署需求，也能作为企业级的 AI 应用解决方案，是构建私有化 AI 助手的理想选择。

**技术亮点**:
- 内置完整的 RAG 引擎，支持文档解析、向量化存储和智能检索
- 支持 MCP (Model Context Protocol) 协议，可扩展连接 700+ MCP 服务器
- 无代码 Agent 构建器，可视化创建自定义 AI 智能体
- 多模态能力支持，兼容 50+ LLM 提供商（Ollama、LM Studio、LocalAI 等）
- 提供 Web Scraping 和 Vector Database 集成，支持多数据源接入

**适用场景**:
- 企业级私有化 AI 知识库与客服系统搭建
- 个人开发者在本地环境构建和调试 AI Agent 应用
- 快速构建基于 RAG 的智能文档问答和内容分析工具



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,826 |
| 语言 | TypeScript |
| Forks | 14,695 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开创性的多智能体协作平台，革新了人机交互模式，将"智能体"作为工作交互的基本单元。该项目在 GitHub 上获得 7.2 万+ stars，集成了 ChatGPT、Claude、DeepSeek 等主流 AI 模型，为用户提供了构建、管理和与 AI 智能体团队协作的一站式解决方案。

**技术亮点**:
- 多智能体协作架构：支持多个 AI agent 协同工作，实现复杂的任务自动化和智能编排
- Agent-First 设计理念：将智能体作为工作交互的核心单元，提供可视化的团队设计能力
- 多模型集成支持：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大语言模型
- 知识库与 MCP 协议支持：内置知识库管理，支持 Model Context Protocol 实现上下文增强
- TypeScript 技术栈：使用现代化技术构建，确保代码质量和可维护性

**适用场景**:
- 企业级 AI 助手团队：为企业构建智能客服、数据分析、内容创作等 AI 智能体团队，提升团队协作效率
- 个人开发者 AI 工作流：个人用户可定制专属 AI 助手组合，用于代码开发、文档编写、学习辅导等日常任务
- 知识管理与问答系统：利用知识库功能构建企业知识库或学习助手，实现智能信息检索和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,959 |
| 语言 | MDX |
| Forks | 7,554 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是 GitHub 上最受欢迎的 Prompt Engineering 资源库（超过 7 万 stars），由 dair-ai 团队维护，系统性地整理了提示词工程、RAG、AI Agents 等前沿 AI 技术的完整学习体系，涵盖了从入门教程到最新研究论文的全链路内容，是开发者快速掌握 AI 应用开发核心技能的权威指南。

**技术亮点**:
- 全栈式覆盖：整合 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 多模态学习资源：包含指南文档、学术论文、实践课程、Jupyter Notebook 等多种形式的学习材料
- 紧跟技术前沿：涵盖 LLMs、OpenAI、ChatGPT、Generative AI 等最新技术栈和深度学习应用
- 技术标签全面：覆盖 agent、rag、prompt-engineering、llms 等热门 AI 开发关键词体系

**适用场景**:
- AI 应用开发者：需要系统学习提示词工程、RAG 检索增强生成、AI 智能体开发等核心技术的工程师
- 企业 AI 转型团队：寻找到大语言模型落地方案，需要参考最佳实践和架构设计的技术团队
- AI 研究人员和学生：跟踪最新论文和技术进展，深入学习生成式 AI 原理的学术群体



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,416 |
| 语言 | HTML |
| Forks | 19,638 |
| Issues | 18 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,508 |
| 语言 | Jupyter Notebook |
| Forks | 13,133 |
| Issues | 0 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,661 |
| 语言 | Python |
| Forks | 9,778 |
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
| Stars | 34,223 |
| 语言 | TypeScript |
| Forks | 6,909 |
| Issues | 423 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,948 |
| 语言 | TypeScript |
| Forks | 2,181 |
| Issues | 61 |
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
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
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
| Stars | 25,643 |
| 语言 | Python |
| Forks | 1,577 |
| Issues | 71 |
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
| Stars | 22,157 |
| 语言 | TypeScript |
| Forks | 1,027 |
| Issues | 146 |
| Topics | ai, anthropic, artificial-intelligence, chatbot, chatgpt, claude, deepseek, developer-tools, gemini, genai, generative-ai, gpt, javascript, language-model, llama, llm, mcp, nodejs, openai, typescript |
| 许可证 | MIT License |


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,768 |
| 语言 | TypeScript |
| Forks | 3,373 |
| Issues | 170 |
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
| Stars | 68,352 |
| 语言 | Python |
| Forks | 8,530 |
| Issues | 361 |
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
| Stars | 35,719 |
| 语言 | TypeScript |
| Forks | 2,706 |
| Issues | 276 |
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
| Stars | 49,440 |
| 语言 | TypeScript |
| Forks | 23,763 |
| Issues | 778 |
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
| Stars | 71,563 |
| 语言 | Python |
| Forks | 13,815 |
| Issues | 3,490 |
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
| Stars | 35,827 |
| 语言 | Python |
| Forks | 3,512 |
| Issues | 60 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### davila7/claude-code-templates

**描述**: CLI tool for configuring and monitoring Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 21,666 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 102 |
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
| Stars | 145,165 |
| 语言 | Python |
| Forks | 8,500 |
| Issues | 1,073 |
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
| Stars | 163,748 |
| 语言 | Go |
| Forks | 14,713 |
| Issues | 2,528 |
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
| Stars | 46,030 |
| 语言 | Rust |
| Forks | 9,045 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


## 🧠 机器学习框架 (14 个项目)


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,698 |
| 语言 | Python |
| Forks | 8,256 |
| Issues | 910 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是ACL 2024论文项目，是当前最全面的LLM/VLM统一微调框架，支持100+大模型的统一高效微调。该项目采用低代码设计理念，通过WebUI界面让零基础用户也能轻松上手，在开源社区获得极高认可度（67K+ stars），是个人开发者和企业进行模型微调的首选工具。

**技术亮点**:
- 统一支持100+种大模型，涵盖GPT、Llama、Qwen、DeepSeek、Gemma、Yi等主流LLM和VLM系列
- 高效微调技术栈完整，支持LoRA、QLoRA、MoE、全量微调等多种PEFT方法及量化技术
- 内置RLHF（人类反馈强化学习）和指令微调能力，可定制化训练垂直领域模型
- 提供WebUI可视化界面和命令行工具，降低AI模型微调的技术门槛，开箱即用
- 支持Agent开发和对话系统集成，可直接将训练好的模型部署为智能助手应用

**适用场景**:
- 企业AI应用落地：快速基于开源模型训练专属行业知识模型（如医疗、法律、金融垂直领域模型）
- 学术研究与实验：研究人员可复现ACL 2024论文方法，对比不同微调策略效果，加速NLP研究进程
- 个人开发者学习AI：通过可视化界面学习LLM微调流程，低成本开发个人AI助手或聊天机器人应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,355 |
| 语言 | Python |
| Forks | 6,081 |
| Issues | 65 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个强大的金融数据平台，为分析师、量化交易者和 AI 智能体提供统一的金融数据访问接口，涵盖股票、加密货币、固定收益、衍生品等多个金融领域，在金融科技领域具有极高的实用价值和学习价值。

**技术亮点**:
- 提供统一的 API 接口访问多种金融数据源（股票、加密货币、衍生品、固定收益等）
- 集成机器学习和 AI 能力，支持 AI 智能体直接调用金融数据
- 开源且免费，降低金融数据获取门槛，支持 Python 生态系统
- 涵盖经济学、量化金融等多个专业领域，提供专业的金融分析工具
- 拥有 62k+ 星标，是 GitHub 上最受欢迎的金融数据平台之一

**适用场景**:
- 量化交易策略研发：获取股票、加密货币等市场数据，构建和回测交易策略
- 金融分析报告生成：为分析师提供多维度金融数据，支持财务建模和投资决策分析
- AI 驱动的金融应用开发：集成到 AI 智能体或金融科技应用中，提供实时数据支持



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,959 |
| 语言 | MDX |
| Forks | 7,554 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是 GitHub 上最受欢迎的 Prompt Engineering 资源库（超过 7 万 stars），由 dair-ai 团队维护，系统性地整理了提示词工程、RAG、AI Agents 等前沿 AI 技术的完整学习体系，涵盖了从入门教程到最新研究论文的全链路内容，是开发者快速掌握 AI 应用开发核心技能的权威指南。

**技术亮点**:
- 全栈式覆盖：整合 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 多模态学习资源：包含指南文档、学术论文、实践课程、Jupyter Notebook 等多种形式的学习材料
- 紧跟技术前沿：涵盖 LLMs、OpenAI、ChatGPT、Generative AI 等最新技术栈和深度学习应用
- 技术标签全面：覆盖 agent、rag、prompt-engineering、llms 等热门 AI 开发关键词体系

**适用场景**:
- AI 应用开发者：需要系统学习提示词工程、RAG 检索增强生成、AI 智能体开发等核心技术的工程师
- 企业 AI 转型团队：寻找到大语言模型落地方案，需要参考最佳实践和架构设计的技术团队
- AI 研究人员和学生：跟踪最新论文和技术进展，深入学习生成式 AI 原理的学术群体



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,416 |
| 语言 | HTML |
| Forks | 19,638 |
| Issues | 18 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,508 |
| 语言 | Jupyter Notebook |
| Forks | 13,133 |
| Issues | 0 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,916 |
| 语言 | Jupyter Notebook |
| Forks | 5,033 |
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
| Stars | 157,156 |
| 语言 | Python |
| Forks | 32,248 |
| Issues | 2,307 |
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
| Stars | 39,402 |
| 语言 | Go |
| Forks | 2,210 |
| Issues | 450 |
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
| Stars | 71,563 |
| 语言 | Python |
| Forks | 13,815 |
| Issues | 3,490 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,398 |
| 语言 | Python |
| Forks | 30,092 |
| Issues | 2,463 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


### Comfy-Org/ComfyUI

**描述**: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,562 |
| 语言 | Python |
| Forks | 11,969 |
| Issues | 3,780 |
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
| Stars | 97,847 |
| 语言 | Python |
| Forks | 27,023 |
| Issues | 18,047 |
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
| Stars | 65,252 |
| 语言 | Python |
| Forks | 26,734 |
| Issues | 2,150 |
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
| Stars | 63,882 |
| 语言 | Python |
| Forks | 19,714 |
| Issues | 288 |
| Topics | data-science, deep-learning, jax, machine-learning, neural-networks, python, pytorch, tensorflow |
| 许可证 | Apache License 2.0 |


## 🛠️ 开发工具 (18 个项目)


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,607 |
| 语言 | JavaScript |
| Forks | 6,835 |
| Issues | 22 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code 的智能代理性能优化系统，集成了技能学习、记忆管理、安全机制和研究驱动开发模式。在 GitHub 上获得超过 5.5 万颗星，证明了其在 AI 辅助开发工具领域的极高价值和实用性，特别适合需要深度集成 Claude 能力的开发者使用。

**技术亮点**:
- 🤖 智能 AI Agent 架构：为 Claude Code、Codex 等提供技能和本能增强系统
- 🧠 持久化记忆管理：实现 Agent 的长期学习和上下文记忆能力
- 🔒 企业级安全机制：内置安全防护层，保障 AI 交互的安全性
- 📊 性能优化系统：专门针对 Agent 性能进行深度优化和调优
- 🔌 MCP 协议支持：基于 Model Context Protocol 实现可扩展的插件生态

**适用场景**:
- 🚀 个人开发者提升效率：作为 AI 编程助手增强工具，加速日常代码开发、调试和重构流程
- 🏢 企业级 AI 研发团队：集成到内部开发工作流，构建智能化的代码审查、文档生成和技术研究系统
- 🛠️ AI Agent 二次开发：基于该项目框架，快速定制和开发专属的 AI 编程助手或自动化工具



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,162 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 151 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 的免费开源替代方案，无需 GPU 即可在消费级硬件上运行，支持本地部署多种 AI 模型（包括 LLM、图像生成、音频生成等），为企业提供数据隐私和成本控制的双重优势。作为 drop-in replacement，它与 OpenAI API 完全兼容，同时支持分布式和 P2P 推理，实现去中心化的 AI 能力部署。

**技术亮点**:
- Drop-in replacement for OpenAI API：无需修改代码即可从 OpenAI 迁移到本地部署，降低迁移成本
- 多模型架构支持：支持 GGUF、Transformers、Diffusers 等多种模型格式，涵盖 Llama、Mistral、Gemma、Stable Diffusion、Whisper 等主流模型
- 零 GPU 需求：CPU 即可运行推理任务，降低硬件门槛和部署成本，适合普通开发者和中小企业
- 分布式与 P2P 推理：基于 libp2p 实现去中心化推理，支持多节点协同处理，提升可扩展性
- 多模态能力：支持文本、图像、音频、视频生成，以及语音克隆、目标检测、Rerank 等丰富功能，并提供 MCP 协议支持

**适用场景**:
- 企业内部 AI 能力部署：金融、医疗、法律等行业对数据敏感的企业可在本地或私有云部署 AI 服务，确保数据不外泄，同时避免 API 调用成本；可集成到现有业务系统中提供智能客服、文档分析、内容生成等能力
- 个人开发者与初创公司：在消费级硬件上快速搭建本地 AI 开发环境，进行模型测试、应用原型开发，无需承担高昂的 GPU 和云服务成本
- 离线与边缘计算场景：支持在无网络环境或边缘设备上运行 AI 推理，适合工业现场、野外作业、物联网设备等场景



### yamadashy/repomix

**描述**: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file. Perfect for when you need to feed your codebase to Large Language Models (LLMs) or other AI tools like Claude, ChatGPT, DeepSeek, Perplexity, Gemini, Gemma, Llama, Grok, and more.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,157 |
| 语言 | TypeScript |
| Forks | 1,027 |
| Issues | 146 |
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
| Stars | 68,352 |
| 语言 | Python |
| Forks | 8,530 |
| Issues | 361 |
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
| Stars | 35,719 |
| 语言 | TypeScript |
| Forks | 2,706 |
| Issues | 276 |
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
| Stars | 176,967 |
| 语言 | TypeScript |
| Forks | 55,289 |
| Issues | 1,416 |
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
| Stars | 149,106 |
| 语言 | Python |
| Forks | 12,085 |
| Issues | 2,340 |
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
| Stars | 95,719 |
| 语言 | Python |
| Forks | 8,765 |
| Issues | 154 |
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
| Stars | 73,254 |
| 语言 | Python |
| Forks | 8,685 |
| Issues | 201 |
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
| Stars | 64,509 |
| 语言 | Python |
| Forks | 4,578 |
| Issues | 337 |
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
| Stars | 182,183 |
| 语言 | TypeScript |
| Forks | 38,219 |
| Issues | 14,421 |
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
| Stars | 93,679 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 293 |
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
| Stars | 77,959 |
| 语言 | TypeScript |
| Forks | 5,603 |
| Issues | 661 |
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
| Stars | 76,422 |
| 语言 | TypeScript |
| Forks | 6,529 |
| Issues | 189 |
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
| Stars | 75,629 |
| 语言 | JavaScript |
| Forks | 7,267 |
| Issues | 705 |
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
| Stars | 78,229 |
| 语言 | Go |
| Forks | 2,698 |
| Issues | 320 |
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
| Stars | 42,820 |
| 语言 | Go |
| Forks | 8,001 |
| Issues | 973 |
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
| Stars | 40,053 |
| 语言 | Go |
| Forks | 1,098 |
| Issues | 154 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目)


### 🌟 高优先级


### simstudioai/sim

**描述**: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 26,768 |
| 语言 | TypeScript |
| Forks | 3,373 |
| Issues | 170 |
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
| Stars | 35,719 |
| 语言 | TypeScript |
| Forks | 2,706 |
| Issues | 276 |
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
| Stars | 176,967 |
| 语言 | TypeScript |
| Forks | 55,289 |
| Issues | 1,416 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ToolJet/ToolJet

**描述**: ToolJet is the open-source foundation of ToolJet AI - the AI-native platform for building internal tools, dashboard, business applications, workflows and AI agents 🚀

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,523 |
| 语言 | JavaScript |
| Forks | 4,956 |
| Issues | 938 |
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
| Stars | 51,584 |
| 语言 | Go |
| Forks | 10,328 |
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
| Stars | 120,841 |
| 语言 | Go |
| Forks | 42,563 |
| Issues | 2,671 |
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
| Stars | 71,455 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,792 |
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
| Stars | 53,982 |
| 语言 | Go |
| Forks | 6,413 |
| Issues | 2,835 |
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
| Stars | 93,679 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 293 |
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
| Stars | 83,241 |
| 语言 | TypeScript |
| Forks | 5,210 |
| Issues | 610 |
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
| Stars | 74,679 |
| 语言 | TypeScript |
| Forks | 6,334 |
| Issues | 417 |
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
| Stars | 83,406 |
| 语言 | JavaScript |
| Forks | 7,458 |
| Issues | 696 |
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
| Stars | 69,074 |
| 语言 | Go |
| Forks | 1,863 |
| Issues | 289 |
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
| Stars | 61,985 |
| 语言 | Go |
| Forks | 5,849 |
| Issues | 772 |
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
| Stars | 57,374 |
| 语言 | Go |
| Forks | 4,144 |
| Issues | 43 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


## 📈 监控/观测 (2 个项目)


### 🌟 高优先级


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,406 |
| 语言 | JavaScript |
| Forks | 7,458 |
| Issues | 696 |
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
| Stars | 62,979 |
| 语言 | Go |
| Forks | 10,208 |
| Issues | 759 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (16 个项目)


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,162 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 151 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI 的免费开源替代方案，无需 GPU 即可在消费级硬件上运行，支持本地部署多种 AI 模型（包括 LLM、图像生成、音频生成等），为企业提供数据隐私和成本控制的双重优势。作为 drop-in replacement，它与 OpenAI API 完全兼容，同时支持分布式和 P2P 推理，实现去中心化的 AI 能力部署。

**技术亮点**:
- Drop-in replacement for OpenAI API：无需修改代码即可从 OpenAI 迁移到本地部署，降低迁移成本
- 多模型架构支持：支持 GGUF、Transformers、Diffusers 等多种模型格式，涵盖 Llama、Mistral、Gemma、Stable Diffusion、Whisper 等主流模型
- 零 GPU 需求：CPU 即可运行推理任务，降低硬件门槛和部署成本，适合普通开发者和中小企业
- 分布式与 P2P 推理：基于 libp2p 实现去中心化推理，支持多节点协同处理，提升可扩展性
- 多模态能力：支持文本、图像、音频、视频生成，以及语音克隆、目标检测、Rerank 等丰富功能，并提供 MCP 协议支持

**适用场景**:
- 企业内部 AI 能力部署：金融、医疗、法律等行业对数据敏感的企业可在本地或私有云部署 AI 服务，确保数据不外泄，同时避免 API 调用成本；可集成到现有业务系统中提供智能客服、文档分析、内容生成等能力
- 个人开发者与初创公司：在消费级硬件上快速搭建本地 AI 开发环境，进行模型测试、应用原型开发，无需承担高昂的 GPU 和云服务成本
- 离线与边缘计算场景：支持在无网络环境或边缘设备上运行 AI 推理，适合工业现场、野外作业、物联网设备等场景



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,719 |
| 语言 | Python |
| Forks | 8,765 |
| Issues | 154 |
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
| Stars | 86,951 |
| 语言 | Python |
| Forks | 33,706 |
| Issues | 423 |
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
| Stars | 100,035 |
| 语言 | TypeScript |
| Forks | 27,094 |
| Issues | 1,120 |
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
| Stars | 77,959 |
| 语言 | TypeScript |
| Forks | 5,603 |
| Issues | 661 |
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
| Stars | 74,812 |
| 语言 | TypeScript |
| Forks | 8,233 |
| Issues | 54 |
| Topics | framework, hacktoberfest, javascript, javascript-framework, microservices, nest, nestjs, node, nodejs, nodejs-framework, typescript, typescript-framework, websockets |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,629 |
| 语言 | JavaScript |
| Forks | 7,267 |
| Issues | 705 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,836 |
| 语言 | JavaScript |
| Forks | 22,682 |
| Issues | 190 |
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
| Stars | 55,950 |
| 语言 | JavaScript |
| Forks | 10,227 |
| Issues | 346 |
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
| Stars | 51,704 |
| 语言 | JavaScript |
| Forks | 4,659 |
| Issues | 1,443 |
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
| Stars | 47,524 |
| 语言 | JavaScript |
| Forks | 1,568 |
| Issues | 664 |
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
| Stars | 88,166 |
| 语言 | Go |
| Forks | 8,559 |
| Issues | 640 |
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
| Stars | 70,477 |
| 语言 | Go |
| Forks | 4,654 |
| Issues | 257 |
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
| Stars | 56,469 |
| 语言 | Go |
| Forks | 3,154 |
| Issues | 23 |
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
| Stars | 40,053 |
| 语言 | Go |
| Forks | 1,098 |
| Issues | 154 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
| 许可证 | MIT License |


### gofiber/fiber

**描述**: ⚡️ Express inspired web framework written in Go

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,315 |
| 语言 | Go |
| Forks | 1,958 |
| Issues | 49 |
| Topics | express, expressjs, fast, fiber, flexible, framework, friendly, go, golang, hacktoberfest, hacktoberfest2020, nodejs, performance, rest-api, web |
| 许可证 | MIT License |


## 📊 数据/基础设施 (5 个项目)


### 🌟 高优先级


### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,224 |
| 语言 | JavaScript |
| Forks | 5,967 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款功能最全面的本地 AI 应用平台，完美融合了 RAG、AI Agents、MCP 协议支持和无代码构建器等企业级特性。它支持超过 50 种 LLM 提供商（包括 DeepSeek、Kimi、Llama3、Qwen3 等），提供桌面应用和 Docker 两种部署方式，既能满足个人开发者本地部署需求，也能作为企业级的 AI 应用解决方案，是构建私有化 AI 助手的理想选择。

**技术亮点**:
- 内置完整的 RAG 引擎，支持文档解析、向量化存储和智能检索
- 支持 MCP (Model Context Protocol) 协议，可扩展连接 700+ MCP 服务器
- 无代码 Agent 构建器，可视化创建自定义 AI 智能体
- 多模态能力支持，兼容 50+ LLM 提供商（Ollama、LM Studio、LocalAI 等）
- 提供 Web Scraping 和 Vector Database 集成，支持多数据源接入

**适用场景**:
- 企业级私有化 AI 知识库与客服系统搭建
- 个人开发者在本地环境构建和调试 AI Agent 应用
- 快速构建基于 RAG 的智能文档问答和内容分析工具



### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,343 |
| 语言 | TypeScript |
| Forks | 11,674 |
| Issues | 1,006 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,056 |
| 语言 | Go |
| Forks | 3,859 |
| Issues | 1,031 |
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
| Stars | 51,584 |
| 语言 | Go |
| Forks | 10,328 |
| Issues | 217 |
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
| Stars | 39,862 |
| 语言 | Go |
| Forks | 6,126 |
| Issues | 5,717 |
| Topics | cloud-native, database, distributed-database, distributed-transactions, go, hacktoberfest, htap, mysql, mysql-compatibility, scale, serverless, sql, tidb |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目)


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,959 |
| 语言 | MDX |
| Forks | 7,554 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是 GitHub 上最受欢迎的 Prompt Engineering 资源库（超过 7 万 stars），由 dair-ai 团队维护，系统性地整理了提示词工程、RAG、AI Agents 等前沿 AI 技术的完整学习体系，涵盖了从入门教程到最新研究论文的全链路内容，是开发者快速掌握 AI 应用开发核心技能的权威指南。

**技术亮点**:
- 全栈式覆盖：整合 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 多模态学习资源：包含指南文档、学术论文、实践课程、Jupyter Notebook 等多种形式的学习材料
- 紧跟技术前沿：涵盖 LLMs、OpenAI、ChatGPT、Generative AI 等最新技术栈和深度学习应用
- 技术标签全面：覆盖 agent、rag、prompt-engineering、llms 等热门 AI 开发关键词体系

**适用场景**:
- AI 应用开发者：需要系统学习提示词工程、RAG 检索增强生成、AI 智能体开发等核心技术的工程师
- 企业 AI 转型团队：寻找到大语言模型落地方案，需要参考最佳实践和架构设计的技术团队
- AI 研究人员和学生：跟踪最新论文和技术进展，深入学习生成式 AI 原理的学术群体



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,416 |
| 语言 | HTML |
| Forks | 19,638 |
| Issues | 18 |
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
| Stars | 25,643 |
| 语言 | Python |
| Forks | 1,577 |
| Issues | 71 |
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
| Stars | 89,339 |
| 语言 | TypeScript |
| Forks | 9,876 |
| Issues | 2,237 |
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
| Stars | 86,362 |
| 语言 | TypeScript |
| Forks | 8,667 |
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
| Stars | 126,906 |
| 语言 | JavaScript |
| Forks | 12,440 |
| Issues | 2 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### jaywcjlove/awesome-mac

**描述**:  Now we have become very big, Different from the original idea. Collect premium software in various categories.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,397 |
| 语言 | JavaScript |
| Forks | 7,441 |
| Issues | 194 |
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
| Stars | 166,285 |
| 语言 | Go |
| Forks | 12,994 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (57 个项目)


### 🌟 高优先级


### CherryHQ/cherry-studio

**描述**: AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,445 |
| 语言 | TypeScript |
| Forks | 3,733 |
| Issues | 659 |
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
| Stars | 242,148 |
| 语言 | TypeScript |
| Forks | 46,797 |
| Issues | 9,858 |
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
| Stars | 39,398 |
| 语言 | Go |
| Forks | 3,930 |
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
| Stars | 68,143 |
| 语言 | Python |
| Forks | 24,192 |
| Issues | 825 |
| Topics | ansible, python |
| 许可证 | GNU General Public License v3.0 |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,179 |
| 语言 | Python |
| Forks | 6,254 |
| Issues | 256 |
| 许可证 | Apache License 2.0 |


### opendatalab/MinerU

**描述**: Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,211 |
| 语言 | Python |
| Forks | 4,577 |
| Issues | 191 |
| Topics | ai4science, document-analysis, extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-extractor-llm, pdf-extractor-pretrain, pdf-extractor-rag, pdf-parser, python |
| 许可证 | GNU Affero General Public License v3.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,728 |
| 语言 | Python |
| Forks | 11,624 |
| Issues | 128 |
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
| Stars | 72,943 |
| 语言 | Python |
| Forks | 6,263 |
| Issues | 632 |
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
| Stars | 383,419 |
| 语言 | Python |
| Forks | 65,988 |
| Issues | 71 |
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
| Stars | 112,254 |
| 语言 | TypeScript |
| Forks | 5,655 |
| Issues | 389 |
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
| Stars | 99,605 |
| 语言 | TypeScript |
| Forks | 7,260 |
| Issues | 167 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### serverless/serverless

**描述**: ⚡ Serverless Framework – Effortlessly build apps that auto-scale, incur zero costs when idle, and require minimal maintenance using AWS Lambda and other managed cloud services.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,949 |
| 语言 | JavaScript |
| Forks | 5,735 |
| Issues | 1,220 |
| Topics | aws, aws-dynamodb, aws-lambda, azure-functions, google-cloud-functions, microservice, serverless, serverless-architectures, serverless-framework |
| 许可证 | Other |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,841 |
| 语言 | Go |
| Forks | 10,229 |
| Issues | 1,909 |
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
| Stars | 96,220 |
| 语言 | C++ |
| Forks | 15,141 |
| Issues | 1,156 |
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
| Stars | 59,564 |
| 语言 | Python |
| Forks | 1,609 |
| Issues | 33 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 22,603 |
| 语言 | JavaScript |
| Forks | 1,953 |
| Issues | 218 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,072 |
| 语言 | Python |
| Forks | 36,878 |
| Issues | 3,442 |
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
| Forks | 45,269 |
| Issues | 1,278 |
| 许可证 | Other |


### python/cpython

**描述**: The Python programming language

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,761 |
| 语言 | Python |
| Forks | 34,146 |
| Issues | 9,306 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 437,630 |
| 语言 | TypeScript |
| Forks | 43,483 |
| Issues | 321 |
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
| Stars | 349,925 |
| 语言 | TypeScript |
| Forks | 43,716 |
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
| Stars | 117,742 |
| 语言 | TypeScript |
| Forks | 12,694 |
| Issues | 2,830 |
| Topics | canvas, collaboration, diagrams, drawing, hacktoberfest, productivity, whiteboard |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,981 |
| 语言 | TypeScript |
| Forks | 13,241 |
| Issues | 5,477 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### shadcn-ui/ui

**描述**: A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,503 |
| 语言 | TypeScript |
| Forks | 7,978 |
| Issues | 1,775 |
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
| Stars | 97,639 |
| 语言 | TypeScript |
| Forks | 54,528 |
| Issues | 1,373 |
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
| Stars | 93,849 |
| 语言 | TypeScript |
| Forks | 5,089 |
| Issues | 79 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,769 |
| 语言 | TypeScript |
| Forks | 4,985 |
| Issues | 689 |
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
| Stars | 82,890 |
| 语言 | TypeScript |
| Forks | 7,564 |
| Issues | 42 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,763 |
| 语言 | TypeScript |
| Forks | 9,705 |
| Issues | 394 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,502 |
| 语言 | TypeScript |
| Forks | 7,862 |
| Issues | 631 |
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
| Stars | 243,387 |
| 语言 | JavaScript |
| Forks | 50,621 |
| Issues | 1,144 |
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
| Stars | 138,059 |
| 语言 | JavaScript |
| Forks | 30,518 |
| Issues | 3,411 |
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
| Stars | 116,005 |
| 语言 | JavaScript |
| Forks | 34,892 |
| Issues | 2,508 |
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
| Stars | 111,121 |
| 语言 | JavaScript |
| Forks | 36,282 |
| Issues | 605 |
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
| Stars | 108,576 |
| 语言 | JavaScript |
| Forks | 11,538 |
| Issues | 343 |
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
| Stars | 97,978 |
| 语言 | JavaScript |
| Forks | 32,722 |
| Issues | 1,730 |
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
| Stars | 95,360 |
| 语言 | JavaScript |
| Forks | 15,182 |
| Issues | 64 |
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
| Stars | 85,940 |
| 语言 | JavaScript |
| Forks | 4,784 |
| Issues | 970 |
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
| Stars | 78,568 |
| 语言 | JavaScript |
| Forks | 31,101 |
| Issues | 269 |
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
| Stars | 70,651 |
| 语言 | JavaScript |
| Forks | 16,799 |
| Issues | 888 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,202 |
| 语言 | JavaScript |
| Forks | 11,991 |
| Issues | 536 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,262 |
| 语言 | JavaScript |
| Forks | 9,186 |
| Issues | 1 |
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
| Stars | 66,011 |
| 语言 | JavaScript |
| Forks | 9,287 |
| Issues | 210 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,847 |
| 语言 | JavaScript |
| Forks | 20,479 |
| Issues | 99 |
| Topics | jquery |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,601 |
| 语言 | JavaScript |
| Forks | 5,593 |
| Issues | 62 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,394 |
| 语言 | JavaScript |
| Forks | 12,312 |
| Issues | 23 |
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
| Stars | 52,902 |
| 语言 | JavaScript |
| Forks | 10,587 |
| Issues | 490 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,939 |
| 语言 | JavaScript |
| Forks | 11,347 |
| Issues | 352 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### poteto/hiring-without-whiteboards

**描述**: ⭐️  Companies that don't have a broken hiring process

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,472 |
| 语言 | JavaScript |
| Forks | 3,885 |
| Issues | 38 |
| Topics | airtable, hiring, hiring-without-whiteboards, interview, jobs, tech, whiteboard |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,815 |
| 语言 | Go |
| Forks | 18,833 |
| Issues | 9,815 |
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
| Stars | 86,845 |
| 语言 | Go |
| Forks | 8,200 |
| Issues | 267 |
| Topics | blog-engine, cms, content-management-system, documentation-tool, go, hugo, static-site-generator |
| 许可证 | Apache License 2.0 |


### base/node

**描述**: Everything required to run your own Base node

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,720 |
| 语言 | Go |
| Forks | 3,213 |
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
| Stars | 55,797 |
| 语言 | Go |
| Forks | 4,936 |
| Issues | 1,125 |
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
| Stars | 50,875 |
| 语言 | Go |
| Forks | 21,815 |
| Issues | 380 |
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
| Stars | 49,081 |
| 语言 | Go |
| Forks | 7,984 |
| Issues | 583 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,124 |
| 语言 | Go |
| Forks | 3,733 |
| Issues | 99 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 144,278 |
| 语言 | Python |
| Forks | 11,142 |
| Issues | 279 |
| Topics | awesome, github, hellogithub, python |
