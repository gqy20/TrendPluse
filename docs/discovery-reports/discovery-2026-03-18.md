# 项目发现报告 (2026-03-18)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 136 |
| 去重移除 | 31 |
| 已在监控 | 20 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
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
| Stars | 127,720 |
| 语言 | Python |
| Forks | 18,045 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个拥有 127K+ Stars 的现象级开源 AI 界面项目，以开箱即用的方式将大语言模型能力带入个人和企业环境。它支持 Ollama、OpenAI 等多种后端，并集成 RAG 和 MCP 等前沿技术，是自托管 AI 应用的首选方案。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，灵活切换无锁定
- RAG 检索增强：内置检索增强生成能力，支持文档上传和知识库构建
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的无缝连接
- 完全自托管：支持本地私有化部署，数据安全可控，无需依赖第三方云服务
- Python 技术栈：基于 Python 开发，易于二次开发和定制扩展

**适用场景**:
- 企业私有化 AI 助手：在内部服务器部署，构建安全可控的企业级 AI 对话平台
- 开发者 LLM 调试工具：快速测试和对比不同模型（Ollama/OpenAI）的输出效果
- 个人知识库问答：结合 RAG 功能，上传文档构建个人智能问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,417 |
| 语言 | Python |
| Forks | 8,444 |
| Issues | 3,121 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（75K+ Stars），独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 构建了卓越的上下文层，同时支持 DeepSeek、Ollama、OpenAI 等多种模型后端，是构建智能知识库和企业级 AI 应用的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力的创新架构，支持 Agentic Workflow 实现自主检索和推理
- 强大的文档理解引擎，支持多格式文档解析与深度语义分析
- 支持 GraphRAG 图谱增强检索，结合 Deep Research 实现深度知识挖掘
- 兼容多种 LLM 后端（OpenAI、Ollama、DeepSeek-R1），支持 MCP 协议实现灵活集成
- 内置 Context Engineering 能力，提供优化的上下文构建和管理机制

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持多格式文档解析与精准检索
- AI 智能客服与助手：基于 RAG+Agent 架构，实现自主工具调用和多轮对话推理
- 深度研究与报告生成：结合 GraphRAG 和 Deep Research 能力，支持复杂信息整合与分析



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,794 |
| 语言 | TypeScript |
| Forks | 6,500 |
| Issues | 219 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的企业级网页数据 API，能够将任意网站自动转换为 LLM 可直接使用的 markdown 或结构化数据，解决了 AI 应用中网页数据采集和预处理的痛点。凭借近 10 万 Star 的高人气，它已成为连接网络数据与大语言模型的重要桥梁工具。

**技术亮点**:
- 支持将任意网站的 HTML 自动转换为 LLM 友好的 Markdown 格式，无需手动清洗数据
- 提供结构化数据提取能力，可智能识别网页内容并输出 JSON 等格式
- 支持 AI 爬虫和 AI 搜索功能，可智能导航和提取目标内容
- 完整的 Web Crawler 引擎，支持深度爬取整个网站而非单页面
- 原生支持多种 AI/LLM 集成场景，提供开箱即用的 API 接口

**适用场景**:
- RAG（检索增强生成）系统的知识库构建：批量抓取企业官网、文档站点转换为 LLM 可用的训练数据
- AI Agent 数据获取：为自主 AI 智能体提供实时的网页内容抓取和信息提取能力
- 企业级数据采集与分析：监控竞品网站、提取行业数据、构建垂直领域数据集



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,136 |
| 语言 | JavaScript |
| Forks | 11,116 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个超高人气的AI代理性能优化系统（85k+ Stars），专注于为Claude Code、Cursor等主流AI编程工具提供技能增强、记忆管理、安全防护和研究驱动的开发能力。它通过统一的harness架构显著提升AI代理的智能水平和生产效率，是开发者充分利用AI编程助手的必备工具。

**技术亮点**:
- 模块化的Agent Harness架构，集成技能、本能、记忆、安全和研究五大核心系统
- 跨平台兼容性，支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具
- 基于MCP（Model Context Protocol）的扩展机制，便于集成自定义功能
- 研究优先的开发模式，通过系统化的知识管理增强AI决策能力
- MIT开源许可，提供灵活的定制和商业化可能性

**适用场景**:
- 企业开发团队希望提升AI编程助手的智能水平和工作效率，需要统一的性能优化方案
- 个人开发者使用Claude Code或Cursor进行日常开发，想要增强AI的上下文记忆和安全能力
- AI工具集成商或平台开发者，需要构建定制化的AI代理增强系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,933 |
| 语言 | Go |
| Forks | 3,731 |
| Issues | 139 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地AI推理平台之一，作为 OpenAI API 的即插即用替代方案，让开发者在无需 GPU 的消费级硬件上就能运行大语言模型、图像生成、语音合成等多种 AI 能力，真正实现了 AI 能力的去中心化和数据隐私保护。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers等）和推理能力（文本、图像、音频、视频生成、语音克隆）
- 零GPU依赖，针对消费级CPU硬件优化，降低部署门槛
- 原生支持分布式和P2P去中心化推理，基于libp2p实现
- OpenAI API 兼容，支持 MCP（Model Context Protocol），易于集成现有应用
- 一体化平台集成多种AI能力：LLM推理、Stable Diffusion、目标检测、TTS、重排序等

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI服务，确保数据不出域，满足合规和隐私要求
- 个人开发者学习与实验：在普通电脑上低成本体验和测试各种开源大模型
- 边缘设备和离线场景：在网络受限或无网络环境中部署AI能力，如IoT设备、移动应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,922 |
| 语言 | TypeScript |
| Forks | 14,799 |
| Issues | 664 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

这是一个功能强大的多智能体协作平台，让用户能够轻松构建、管理和协调多个AI Agent协同工作。它支持主流AI模型（ChatGPT、Claude、Gemini、DeepSeek等），结合知识库和MCP协议，打造了一个集工作与生活于一体的AI智能助手生态系统。

**技术亮点**:
- 多智能体协作架构：支持多个Agent协同工作，实现复杂任务的分工协作
- 全栈TypeScript实现：类型安全、开发体验优秀，代码可维护性强
- 多模型支持：集成OpenAI、Claude、Gemini、DeepSeek等主流AI模型
- 知识库管理：支持构建和管理私有知识库，增强AI响应的准确性
- MCP协议支持：采用Model Context Protocol，实现标准化的模型上下文交互

**适用场景**:
- 企业级AI工作流自动化：构建多Agent协作系统处理复杂业务流程，如客服、数据分析、内容创作等
- 个人AI助手生态：打造个性化的智能工作空间，集成多种AI能力提升日常工作效率
- AI应用快速原型开发：开发者可基于该平台快速搭建和测试多Agent应用，降低AI应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,868 |
| 语言 | MDX |
| Forks | 7,677 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有超过7万星标的开源项目，汇集了提示词工程、RAG和AI Agent领域最全面的学习资源和实践指南，由DAIR.AI团队精心维护，适合从初学者到高级开发者系统性地掌握大模型应用开发的核心技能。

**技术亮点**:
- 涵盖Prompt Engineering、Context Engineering、RAG和AI Agents四大核心领域的完整知识体系
- 提供可交互的Jupyter Notebooks和实践教程，支持动手学习
- 包含最新LLM技术论文、最佳实践和社区资源汇总
- 基于MDX格式，支持Markdown与React组件结合，便于构建交互式文档
- MIT开源协议，内容持续更新，紧跟AI技术前沿发展

**适用场景**:
- AI应用开发者学习Prompt Engineering和RAG技术，提升大模型应用效果
- 企业团队培训和技术沉淀，建立内部AI开发最佳实践规范
- 研究人员快速了解AI Agents和上下文工程领域的最新进展和技术路线



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,655 |
| 语言 | Python |
| Forks | 8,366 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个ACL 2024收录的明星项目，以68K+ Stars证明了其在LLM生态中的重要地位。它提供了统一的高效微调框架，支持100多种大语言模型和视觉语言模型，让开发者和企业能够快速定制化自己的AI模型，而无需从零开始训练。

**技术亮点**:
- 支持100+主流LLM/VLM模型（Llama3、GPT、Qwen、DeepSeek、Gemma等），提供开箱即用的统一微调接口
- 集成多种高效微调技术：LoRA、QLoRA、PEFT等参数高效微调方法，以及4-bit/8-bit量化训练
- 支持多阶段训练范式：指令微调(Instruction Tuning)、RLHF人类反馈强化学习、MoE混合专家模型
- 提供Web UI和CLI两种操作界面，支持Agent智能体开发，降低使用门槛
- Apache 2.0开源许可，活跃的社区维护，与Transformers生态深度集成

**适用场景**:
- 企业级大模型定制：快速在私有数据上微调开源大模型，打造垂直领域的专属AI助手
- 学术研究与实验：支持多种前沿微调方法对比实验，加速论文复现和算法迭代
- 个人开发者学习：通过Web UI零代码体验LLM微调全流程，理解指令微调、RLHF等核心概念
- 多模态应用开发：支持VLM视觉语言模型微调，构建图文理解、多模态对话等应用



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,443 |
| 语言 | Java |
| Forks | 15,842 |
| Issues | 59 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 技术的企业级低代码开发平台，通过"零代码"和"代码生成"双模式创新，让开发者只需一句话即可快速搭建系统或自动生成完整的前后端代码。它解决了 Java 企业开发中 80% 的重复工作，在保证高效的同时不失灵活性，是目前 AI 时代下极具前瞻性的开源解决方案。

**技术亮点**:
- 集成 LangChain4j、Spring AI 等主流 AI 框架，内置 AI 聊天助手、大模型与 RAG 知识库能力
- 支持 MCP 协议与插件体系，具备 AI 流程编排（AIFlow）和一句话生成流程图/表单能力
- 基于 SpringBoot3 + Vue3 + MyBatis-Plus 现代技术栈，兼容 SpringCloud 微服务架构
- 内置 Flowable/Activiti 工作流引擎，支持复杂业务流程自动化
- 零代码模式 + 代码生成模式双引擎驱动，既可一句话建系统，也可生成可运行的完整代码

**适用场景**:
- 企业内部管理系统快速开发：OA、CRM、ERP 等业务系统可通过零代码或代码生成快速交付
- AI 应用开发平台：快速构建带有 AI 聊天、知识库、智能流程的企业级 AI 应用
- Java 团队提效工具：大幅减少 CRUD 重复编码工作，让开发者专注于业务创新



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,277 |
| 语言 | Python |
| Forks | 9,837 |
| Issues | 348 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,049 |
| 语言 | TypeScript |
| Forks | 2,737 |
| Issues | 122 |
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
| Stars | 34,747 |
| 语言 | TypeScript |
| Forks | 7,032 |
| Issues | 460 |
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
| Stars | 33,476 |
| 语言 | Python |
| Forks | 2,066 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,067 |
| 语言 | TypeScript |
| Forks | 5,316 |
| Issues | 52 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,784 |
| 语言 | Python |
| Forks | 6,145 |
| Issues | 183 |
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
| Stars | 32,257 |
| 语言 | Jupyter Notebook |
| Forks | 5,324 |
| Issues | 123 |
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
| Stars | 102,717 |
| 语言 | Python |
| Forks | 14,978 |
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
| Stars | 56,414 |
| 语言 | JavaScript |
| Forks | 6,097 |
| Issues | 302 |
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
| Stars | 69,350 |
| 语言 | Python |
| Forks | 8,694 |
| Issues | 328 |
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
| Stars | 41,169 |
| 语言 | TypeScript |
| Forks | 3,083 |
| Issues | 408 |
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
| Stars | 81,217 |
| 语言 | Python |
| Forks | 9,595 |
| Issues | 222 |
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
| Stars | 50,875 |
| 语言 | TypeScript |
| Forks | 23,969 |
| Issues | 815 |
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
| Stars | 179,827 |
| 语言 | TypeScript |
| Forks | 55,923 |
| Issues | 1,434 |
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
| Stars | 145,837 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 900 |
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
| Stars | 54,373 |
| 语言 | Jupyter Notebook |
| Forks | 18,824 |
| Issues | 3 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,113 |
| 语言 | TypeScript |
| Forks | 3,565 |
| Issues | 281 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 45,685 |
| 语言 | Python |
| Forks | 4,636 |
| Issues | 329 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


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
| Stars | 127,720 |
| 语言 | Python |
| Forks | 18,045 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个拥有 127K+ Stars 的现象级开源 AI 界面项目，以开箱即用的方式将大语言模型能力带入个人和企业环境。它支持 Ollama、OpenAI 等多种后端，并集成 RAG 和 MCP 等前沿技术，是自托管 AI 应用的首选方案。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，灵活切换无锁定
- RAG 检索增强：内置检索增强生成能力，支持文档上传和知识库构建
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的无缝连接
- 完全自托管：支持本地私有化部署，数据安全可控，无需依赖第三方云服务
- Python 技术栈：基于 Python 开发，易于二次开发和定制扩展

**适用场景**:
- 企业私有化 AI 助手：在内部服务器部署，构建安全可控的企业级 AI 对话平台
- 开发者 LLM 调试工具：快速测试和对比不同模型（Ollama/OpenAI）的输出效果
- 个人知识库问答：结合 RAG 功能，上传文档构建个人智能问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,417 |
| 语言 | Python |
| Forks | 8,444 |
| Issues | 3,121 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（75K+ Stars），独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 构建了卓越的上下文层，同时支持 DeepSeek、Ollama、OpenAI 等多种模型后端，是构建智能知识库和企业级 AI 应用的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力的创新架构，支持 Agentic Workflow 实现自主检索和推理
- 强大的文档理解引擎，支持多格式文档解析与深度语义分析
- 支持 GraphRAG 图谱增强检索，结合 Deep Research 实现深度知识挖掘
- 兼容多种 LLM 后端（OpenAI、Ollama、DeepSeek-R1），支持 MCP 协议实现灵活集成
- 内置 Context Engineering 能力，提供优化的上下文构建和管理机制

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持多格式文档解析与精准检索
- AI 智能客服与助手：基于 RAG+Agent 架构，实现自主工具调用和多轮对话推理
- 深度研究与报告生成：结合 GraphRAG 和 Deep Research 能力，支持复杂信息整合与分析



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,922 |
| 语言 | TypeScript |
| Forks | 14,799 |
| Issues | 664 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

这是一个功能强大的多智能体协作平台，让用户能够轻松构建、管理和协调多个AI Agent协同工作。它支持主流AI模型（ChatGPT、Claude、Gemini、DeepSeek等），结合知识库和MCP协议，打造了一个集工作与生活于一体的AI智能助手生态系统。

**技术亮点**:
- 多智能体协作架构：支持多个Agent协同工作，实现复杂任务的分工协作
- 全栈TypeScript实现：类型安全、开发体验优秀，代码可维护性强
- 多模型支持：集成OpenAI、Claude、Gemini、DeepSeek等主流AI模型
- 知识库管理：支持构建和管理私有知识库，增强AI响应的准确性
- MCP协议支持：采用Model Context Protocol，实现标准化的模型上下文交互

**适用场景**:
- 企业级AI工作流自动化：构建多Agent协作系统处理复杂业务流程，如客服、数据分析、内容创作等
- 个人AI助手生态：打造个性化的智能工作空间，集成多种AI能力提升日常工作效率
- AI应用快速原型开发：开发者可基于该平台快速搭建和测试多Agent应用，降低AI应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,868 |
| 语言 | MDX |
| Forks | 7,677 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有超过7万星标的开源项目，汇集了提示词工程、RAG和AI Agent领域最全面的学习资源和实践指南，由DAIR.AI团队精心维护，适合从初学者到高级开发者系统性地掌握大模型应用开发的核心技能。

**技术亮点**:
- 涵盖Prompt Engineering、Context Engineering、RAG和AI Agents四大核心领域的完整知识体系
- 提供可交互的Jupyter Notebooks和实践教程，支持动手学习
- 包含最新LLM技术论文、最佳实践和社区资源汇总
- 基于MDX格式，支持Markdown与React组件结合，便于构建交互式文档
- MIT开源协议，内容持续更新，紧跟AI技术前沿发展

**适用场景**:
- AI应用开发者学习Prompt Engineering和RAG技术，提升大模型应用效果
- 企业团队培训和技术沉淀，建立内部AI开发最佳实践规范
- 研究人员快速了解AI Agents和上下文工程领域的最新进展和技术路线



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,443 |
| 语言 | Java |
| Forks | 15,842 |
| Issues | 59 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 技术的企业级低代码开发平台，通过"零代码"和"代码生成"双模式创新，让开发者只需一句话即可快速搭建系统或自动生成完整的前后端代码。它解决了 Java 企业开发中 80% 的重复工作，在保证高效的同时不失灵活性，是目前 AI 时代下极具前瞻性的开源解决方案。

**技术亮点**:
- 集成 LangChain4j、Spring AI 等主流 AI 框架，内置 AI 聊天助手、大模型与 RAG 知识库能力
- 支持 MCP 协议与插件体系，具备 AI 流程编排（AIFlow）和一句话生成流程图/表单能力
- 基于 SpringBoot3 + Vue3 + MyBatis-Plus 现代技术栈，兼容 SpringCloud 微服务架构
- 内置 Flowable/Activiti 工作流引擎，支持复杂业务流程自动化
- 零代码模式 + 代码生成模式双引擎驱动，既可一句话建系统，也可生成可运行的完整代码

**适用场景**:
- 企业内部管理系统快速开发：OA、CRM、ERP 等业务系统可通过零代码或代码生成快速交付
- AI 应用开发平台：快速构建带有 AI 聊天、知识库、智能流程的企业级 AI 应用
- Java 团队提效工具：大幅减少 CRUD 重复编码工作，让开发者专注于业务创新



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,049 |
| 语言 | TypeScript |
| Forks | 2,737 |
| Issues | 122 |
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
| Stars | 33,476 |
| 语言 | Python |
| Forks | 2,066 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,784 |
| 语言 | Python |
| Forks | 6,145 |
| Issues | 183 |
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
| Stars | 32,257 |
| 语言 | Jupyter Notebook |
| Forks | 5,324 |
| Issues | 123 |
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
| Stars | 102,717 |
| 语言 | Python |
| Forks | 14,978 |
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
| Stars | 99,206 |
| 语言 | TypeScript |
| Forks | 11,827 |
| Issues | 946 |
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
| Stars | 56,414 |
| 语言 | JavaScript |
| Forks | 6,097 |
| Issues | 302 |
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
| Stars | 50,875 |
| 语言 | TypeScript |
| Forks | 23,969 |
| Issues | 815 |
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
| Stars | 72,564 |
| 语言 | Python |
| Forks | 9,998 |
| Issues | 249 |
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
| Stars | 43,369 |
| 语言 | Go |
| Forks | 3,903 |
| Issues | 1,087 |
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
| Stars | 31,589 |
| 语言 | Python |
| Forks | 3,329 |
| Issues | 79 |
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
| Stars | 33,113 |
| 语言 | TypeScript |
| Forks | 3,565 |
| Issues | 281 |
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
| Stars | 127,720 |
| 语言 | Python |
| Forks | 18,045 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个拥有 127K+ Stars 的现象级开源 AI 界面项目，以开箱即用的方式将大语言模型能力带入个人和企业环境。它支持 Ollama、OpenAI 等多种后端，并集成 RAG 和 MCP 等前沿技术，是自托管 AI 应用的首选方案。

**技术亮点**:
- 多后端支持：兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 提供商，灵活切换无锁定
- RAG 检索增强：内置检索增强生成能力，支持文档上传和知识库构建
- MCP 协议集成：支持 Model Context Protocol，实现与外部工具和数据的无缝连接
- 完全自托管：支持本地私有化部署，数据安全可控，无需依赖第三方云服务
- Python 技术栈：基于 Python 开发，易于二次开发和定制扩展

**适用场景**:
- 企业私有化 AI 助手：在内部服务器部署，构建安全可控的企业级 AI 对话平台
- 开发者 LLM 调试工具：快速测试和对比不同模型（Ollama/OpenAI）的输出效果
- 个人知识库问答：结合 RAG 功能，上传文档构建个人智能问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,417 |
| 语言 | Python |
| Forks | 8,444 |
| Issues | 3,121 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（75K+ Stars），独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 构建了卓越的上下文层，同时支持 DeepSeek、Ollama、OpenAI 等多种模型后端，是构建智能知识库和企业级 AI 应用的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力的创新架构，支持 Agentic Workflow 实现自主检索和推理
- 强大的文档理解引擎，支持多格式文档解析与深度语义分析
- 支持 GraphRAG 图谱增强检索，结合 Deep Research 实现深度知识挖掘
- 兼容多种 LLM 后端（OpenAI、Ollama、DeepSeek-R1），支持 MCP 协议实现灵活集成
- 内置 Context Engineering 能力，提供优化的上下文构建和管理机制

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持多格式文档解析与精准检索
- AI 智能客服与助手：基于 RAG+Agent 架构，实现自主工具调用和多轮对话推理
- 深度研究与报告生成：结合 GraphRAG 和 Deep Research 能力，支持复杂信息整合与分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,136 |
| 语言 | JavaScript |
| Forks | 11,116 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个超高人气的AI代理性能优化系统（85k+ Stars），专注于为Claude Code、Cursor等主流AI编程工具提供技能增强、记忆管理、安全防护和研究驱动的开发能力。它通过统一的harness架构显著提升AI代理的智能水平和生产效率，是开发者充分利用AI编程助手的必备工具。

**技术亮点**:
- 模块化的Agent Harness架构，集成技能、本能、记忆、安全和研究五大核心系统
- 跨平台兼容性，支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具
- 基于MCP（Model Context Protocol）的扩展机制，便于集成自定义功能
- 研究优先的开发模式，通过系统化的知识管理增强AI决策能力
- MIT开源许可，提供灵活的定制和商业化可能性

**适用场景**:
- 企业开发团队希望提升AI编程助手的智能水平和工作效率，需要统一的性能优化方案
- 个人开发者使用Claude Code或Cursor进行日常开发，想要增强AI的上下文记忆和安全能力
- AI工具集成商或平台开发者，需要构建定制化的AI代理增强系统



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,922 |
| 语言 | TypeScript |
| Forks | 14,799 |
| Issues | 664 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

这是一个功能强大的多智能体协作平台，让用户能够轻松构建、管理和协调多个AI Agent协同工作。它支持主流AI模型（ChatGPT、Claude、Gemini、DeepSeek等），结合知识库和MCP协议，打造了一个集工作与生活于一体的AI智能助手生态系统。

**技术亮点**:
- 多智能体协作架构：支持多个Agent协同工作，实现复杂任务的分工协作
- 全栈TypeScript实现：类型安全、开发体验优秀，代码可维护性强
- 多模型支持：集成OpenAI、Claude、Gemini、DeepSeek等主流AI模型
- 知识库管理：支持构建和管理私有知识库，增强AI响应的准确性
- MCP协议支持：采用Model Context Protocol，实现标准化的模型上下文交互

**适用场景**:
- 企业级AI工作流自动化：构建多Agent协作系统处理复杂业务流程，如客服、数据分析、内容创作等
- 个人AI助手生态：打造个性化的智能工作空间，集成多种AI能力提升日常工作效率
- AI应用快速原型开发：开发者可基于该平台快速搭建和测试多Agent应用，降低AI应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,868 |
| 语言 | MDX |
| Forks | 7,677 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有超过7万星标的开源项目，汇集了提示词工程、RAG和AI Agent领域最全面的学习资源和实践指南，由DAIR.AI团队精心维护，适合从初学者到高级开发者系统性地掌握大模型应用开发的核心技能。

**技术亮点**:
- 涵盖Prompt Engineering、Context Engineering、RAG和AI Agents四大核心领域的完整知识体系
- 提供可交互的Jupyter Notebooks和实践教程，支持动手学习
- 包含最新LLM技术论文、最佳实践和社区资源汇总
- 基于MDX格式，支持Markdown与React组件结合，便于构建交互式文档
- MIT开源协议，内容持续更新，紧跟AI技术前沿发展

**适用场景**:
- AI应用开发者学习Prompt Engineering和RAG技术，提升大模型应用效果
- 企业团队培训和技术沉淀，建立内部AI开发最佳实践规范
- 研究人员快速了解AI Agents和上下文工程领域的最新进展和技术路线



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,199 |
| 语言 | HTML |
| Forks | 20,162 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,277 |
| 语言 | Python |
| Forks | 9,837 |
| Issues | 348 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,049 |
| 语言 | TypeScript |
| Forks | 2,737 |
| Issues | 122 |
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
| Stars | 34,747 |
| 语言 | TypeScript |
| Forks | 7,032 |
| Issues | 460 |
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
| Stars | 33,476 |
| 语言 | Python |
| Forks | 2,066 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,067 |
| 语言 | TypeScript |
| Forks | 5,316 |
| Issues | 52 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,414 |
| 语言 | JavaScript |
| Forks | 6,097 |
| Issues | 302 |
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
| Stars | 69,350 |
| 语言 | Python |
| Forks | 8,694 |
| Issues | 328 |
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
| Stars | 41,169 |
| 语言 | TypeScript |
| Forks | 3,083 |
| Issues | 408 |
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
| Stars | 50,875 |
| 语言 | TypeScript |
| Forks | 23,969 |
| Issues | 815 |
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
| Stars | 34,612 |
| 语言 | HTML |
| Forks | 5,567 |
| Issues | 17 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,555 |
| 语言 | Python |
| Forks | 14,507 |
| Issues | 3,792 |
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
| Stars | 39,017 |
| 语言 | TypeScript |
| Forks | 3,946 |
| Issues | 1,077 |
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
| Stars | 145,837 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 900 |
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
| Stars | 165,471 |
| 语言 | Go |
| Forks | 15,037 |
| Issues | 2,680 |
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
| Stars | 88,643 |
| 语言 | Jupyter Notebook |
| Forks | 13,530 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,726 |
| 语言 | Rust |
| Forks | 9,143 |
| Issues | 0 |
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
| Stars | 90,940 |
| 语言 | Python |
| Forks | 5,377 |
| Issues | 472 |
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
| Stars | 44,969 |
| 语言 | Python |
| Forks | 4,322 |
| Issues | 76 |
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
| Stars | 36,752 |
| 语言 | Python |
| Forks | 2,571 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 45,685 |
| 语言 | Python |
| Forks | 4,636 |
| Issues | 329 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


## 🧠 机器学习框架 (12 个项目) { #机器学习框架 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,868 |
| 语言 | MDX |
| Forks | 7,677 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有超过7万星标的开源项目，汇集了提示词工程、RAG和AI Agent领域最全面的学习资源和实践指南，由DAIR.AI团队精心维护，适合从初学者到高级开发者系统性地掌握大模型应用开发的核心技能。

**技术亮点**:
- 涵盖Prompt Engineering、Context Engineering、RAG和AI Agents四大核心领域的完整知识体系
- 提供可交互的Jupyter Notebooks和实践教程，支持动手学习
- 包含最新LLM技术论文、最佳实践和社区资源汇总
- 基于MDX格式，支持Markdown与React组件结合，便于构建交互式文档
- MIT开源协议，内容持续更新，紧跟AI技术前沿发展

**适用场景**:
- AI应用开发者学习Prompt Engineering和RAG技术，提升大模型应用效果
- 企业团队培训和技术沉淀，建立内部AI开发最佳实践规范
- 研究人员快速了解AI Agents和上下文工程领域的最新进展和技术路线



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,655 |
| 语言 | Python |
| Forks | 8,366 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个ACL 2024收录的明星项目，以68K+ Stars证明了其在LLM生态中的重要地位。它提供了统一的高效微调框架，支持100多种大语言模型和视觉语言模型，让开发者和企业能够快速定制化自己的AI模型，而无需从零开始训练。

**技术亮点**:
- 支持100+主流LLM/VLM模型（Llama3、GPT、Qwen、DeepSeek、Gemma等），提供开箱即用的统一微调接口
- 集成多种高效微调技术：LoRA、QLoRA、PEFT等参数高效微调方法，以及4-bit/8-bit量化训练
- 支持多阶段训练范式：指令微调(Instruction Tuning)、RLHF人类反馈强化学习、MoE混合专家模型
- 提供Web UI和CLI两种操作界面，支持Agent智能体开发，降低使用门槛
- Apache 2.0开源许可，活跃的社区维护，与Transformers生态深度集成

**适用场景**:
- 企业级大模型定制：快速在私有数据上微调开源大模型，打造垂直领域的专属AI助手
- 学术研究与实验：支持多种前沿微调方法对比实验，加速论文复现和算法迭代
- 个人开发者学习：通过Web UI零代码体验LLM微调全流程，理解指令微调、RLHF等核心概念
- 多模态应用开发：支持VLM视觉语言模型微调，构建图文理解、多模态对话等应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,278 |
| 语言 | Python |
| Forks | 6,223 |
| Issues | 66 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是一个开源的金融数据平台，拥有超过6.3万Stars，是目前GitHub上最受欢迎的金融分析工具之一。它将股票、加密货币、衍生品、期权、固定收益等多种金融数据源整合到统一平台，为分析师、量化交易员和AI代理提供一站式数据访问和机器学习能力，解决了金融数据分散、获取成本高的痛点。

**技术亮点**:
- 基于Python构建，提供统一的API接口，可整合股票、加密货币、衍生品、期权、固定收益、宏观经济等多维度金融数据源
- 原生支持AI代理集成，可将金融数据直接喂给AI模型进行智能分析和决策
- 内置机器学习和量化金融分析工具，支持从数据获取到策略开发的全流程
- 覆盖全面的金融工具链，包括股票、ETF、期权、加密货币、经济指标等多种资产类别
- 开源架构允许用户自定义数据源扩展和功能模块开发

**适用场景**:
- 个人投资者和金融分析师进行市场研究、资产配置和投资决策支持
- 量化交易团队开发和回测交易策略，获取多源金融数据进行因子分析
- AI/ML工程师构建金融智能应用，如智能投顾、风险评估模型和市场预测系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,199 |
| 语言 | HTML |
| Forks | 20,162 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,257 |
| 语言 | Jupyter Notebook |
| Forks | 5,324 |
| Issues | 123 |
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
| Stars | 158,031 |
| 语言 | Python |
| Forks | 32,527 |
| Issues | 2,283 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,555 |
| 语言 | Python |
| Forks | 14,507 |
| Issues | 3,792 |
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
| Stars | 106,237 |
| 语言 | Python |
| Forks | 12,231 |
| Issues | 3,849 |
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
| Stars | 98,354 |
| 语言 | Python |
| Forks | 27,243 |
| Issues | 18,059 |
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
| Stars | 88,643 |
| 语言 | Jupyter Notebook |
| Forks | 13,530 |
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
| Stars | 33,113 |
| 语言 | TypeScript |
| Forks | 3,565 |
| Issues | 281 |
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
| Stars | 161,841 |
| 语言 | Python |
| Forks | 30,188 |
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
| Stars | 85,136 |
| 语言 | JavaScript |
| Forks | 11,116 |
| Issues | 101 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个超高人气的AI代理性能优化系统（85k+ Stars），专注于为Claude Code、Cursor等主流AI编程工具提供技能增强、记忆管理、安全防护和研究驱动的开发能力。它通过统一的harness架构显著提升AI代理的智能水平和生产效率，是开发者充分利用AI编程助手的必备工具。

**技术亮点**:
- 模块化的Agent Harness架构，集成技能、本能、记忆、安全和研究五大核心系统
- 跨平台兼容性，支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具
- 基于MCP（Model Context Protocol）的扩展机制，便于集成自定义功能
- 研究优先的开发模式，通过系统化的知识管理增强AI决策能力
- MIT开源许可，提供灵活的定制和商业化可能性

**适用场景**:
- 企业开发团队希望提升AI编程助手的智能水平和工作效率，需要统一的性能优化方案
- 个人开发者使用Claude Code或Cursor进行日常开发，想要增强AI的上下文记忆和安全能力
- AI工具集成商或平台开发者，需要构建定制化的AI代理增强系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,933 |
| 语言 | Go |
| Forks | 3,731 |
| Issues | 139 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地AI推理平台之一，作为 OpenAI API 的即插即用替代方案，让开发者在无需 GPU 的消费级硬件上就能运行大语言模型、图像生成、语音合成等多种 AI 能力，真正实现了 AI 能力的去中心化和数据隐私保护。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers等）和推理能力（文本、图像、音频、视频生成、语音克隆）
- 零GPU依赖，针对消费级CPU硬件优化，降低部署门槛
- 原生支持分布式和P2P去中心化推理，基于libp2p实现
- OpenAI API 兼容，支持 MCP（Model Context Protocol），易于集成现有应用
- 一体化平台集成多种AI能力：LLM推理、Stable Diffusion、目标检测、TTS、重排序等

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI服务，确保数据不出域，满足合规和隐私要求
- 个人开发者学习与实验：在普通电脑上低成本体验和测试各种开源大模型
- 边缘设备和离线场景：在网络受限或无网络环境中部署AI能力，如IoT设备、移动应用



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,350 |
| 语言 | Python |
| Forks | 8,694 |
| Issues | 328 |
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
| Stars | 41,169 |
| 语言 | TypeScript |
| Forks | 3,083 |
| Issues | 408 |
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
| Stars | 179,827 |
| 语言 | TypeScript |
| Forks | 55,923 |
| Issues | 1,434 |
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
| Stars | 411,864 |
| 语言 | Python |
| Forks | 44,550 |
| Issues | 1,015 |
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
| Stars | 151,904 |
| 语言 | Python |
| Forks | 12,319 |
| Issues | 2,368 |
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
| Stars | 96,319 |
| 语言 | Python |
| Forks | 8,877 |
| Issues | 164 |
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
| Stars | 73,829 |
| 语言 | Python |
| Forks | 8,769 |
| Issues | 199 |
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
| Stars | 182,792 |
| 语言 | TypeScript |
| Forks | 38,582 |
| Issues | 15,430 |
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
| Stars | 93,866 |
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
| Stars | 78,517 |
| 语言 | TypeScript |
| Forks | 5,708 |
| Issues | 720 |
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
| Stars | 76,715 |
| 语言 | TypeScript |
| Forks | 6,562 |
| Issues | 174 |
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
| Stars | 75,667 |
| 语言 | JavaScript |
| Forks | 7,276 |
| Issues | 708 |
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
| Stars | 78,705 |
| 语言 | Go |
| Forks | 2,736 |
| Issues | 316 |
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
| Stars | 74,576 |
| 语言 | Go |
| Forks | 2,620 |
| Issues | 936 |
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
| Stars | 36,752 |
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
| Stars | 54,512 |
| 语言 | JavaScript |
| Forks | 4,032 |
| Issues | 1,404 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,169 |
| 语言 | TypeScript |
| Forks | 3,083 |
| Issues | 408 |
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
| Stars | 179,827 |
| 语言 | TypeScript |
| Forks | 55,923 |
| Issues | 1,434 |
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
| Stars | 51,656 |
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
| Stars | 121,199 |
| 语言 | Go |
| Forks | 42,690 |
| Issues | 2,604 |
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
| Stars | 71,539 |
| 语言 | Go |
| Forks | 18,920 |
| Issues | 3,796 |
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
| Stars | 54,357 |
| 语言 | Go |
| Forks | 6,485 |
| Issues | 2,860 |
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
| Stars | 47,582 |
| 语言 | Go |
| Forks | 5,070 |
| Issues | 962 |
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
| Stars | 93,866 |
| 语言 | TypeScript |
| Forks | 9,399 |
| Issues | 294 |
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
| Stars | 84,510 |
| 语言 | TypeScript |
| Forks | 5,311 |
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
| Stars | 75,492 |
| 语言 | TypeScript |
| Forks | 6,427 |
| Issues | 437 |
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
| Stars | 84,223 |
| 语言 | JavaScript |
| Forks | 7,544 |
| Issues | 703 |
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
| Stars | 62,234 |
| 语言 | Go |
| Forks | 5,883 |
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
| Stars | 58,002 |
| 语言 | Go |
| Forks | 4,209 |
| Issues | 22 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 45,685 |
| 语言 | Python |
| Forks | 4,636 |
| Issues | 329 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 69,421 |
| 语言 | Go |
| Forks | 1,882 |
| Issues | 296 |
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
| Stars | 84,223 |
| 语言 | JavaScript |
| Forks | 7,544 |
| Issues | 703 |
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
| Stars | 63,201 |
| 语言 | Go |
| Forks | 10,247 |
| Issues | 756 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (14 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,933 |
| 语言 | Go |
| Forks | 3,731 |
| Issues | 139 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是最成熟的开源本地AI推理平台之一，作为 OpenAI API 的即插即用替代方案，让开发者在无需 GPU 的消费级硬件上就能运行大语言模型、图像生成、语音合成等多种 AI 能力，真正实现了 AI 能力的去中心化和数据隐私保护。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers等）和推理能力（文本、图像、音频、视频生成、语音克隆）
- 零GPU依赖，针对消费级CPU硬件优化，降低部署门槛
- 原生支持分布式和P2P去中心化推理，基于libp2p实现
- OpenAI API 兼容，支持 MCP（Model Context Protocol），易于集成现有应用
- 一体化平台集成多种AI能力：LLM推理、Stable Diffusion、目标检测、TTS、重排序等

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI服务，确保数据不出域，满足合规和隐私要求
- 个人开发者学习与实验：在普通电脑上低成本体验和测试各种开源大模型
- 边缘设备和离线场景：在网络受限或无网络环境中部署AI能力，如IoT设备、移动应用



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 411,864 |
| 语言 | Python |
| Forks | 44,550 |
| Issues | 1,015 |
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
| Stars | 96,319 |
| 语言 | Python |
| Forks | 8,877 |
| Issues | 164 |
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
| Stars | 87,064 |
| 语言 | Python |
| Forks | 33,765 |
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
| Stars | 100,095 |
| 语言 | TypeScript |
| Forks | 27,136 |
| Issues | 1,112 |
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
| Stars | 78,517 |
| 语言 | TypeScript |
| Forks | 5,708 |
| Issues | 720 |
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
| Stars | 74,945 |
| 语言 | TypeScript |
| Forks | 8,259 |
| Issues | 36 |
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
| Stars | 75,667 |
| 语言 | JavaScript |
| Forks | 7,276 |
| Issues | 708 |
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
| Stars | 55,945 |
| 语言 | JavaScript |
| Forks | 10,226 |
| Issues | 355 |
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
| Stars | 88,259 |
| 语言 | Go |
| Forks | 8,572 |
| Issues | 646 |
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
| Stars | 70,901 |
| 语言 | Go |
| Forks | 4,683 |
| Issues | 247 |
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
| Stars | 56,808 |
| 语言 | Go |
| Forks | 3,179 |
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
| Stars | 36,752 |
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
| Stars | 68,886 |
| 语言 | JavaScript |
| Forks | 22,850 |
| Issues | 191 |
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
| Stars | 99,206 |
| 语言 | TypeScript |
| Forks | 11,827 |
| Issues | 946 |
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
| Stars | 56,414 |
| 语言 | JavaScript |
| Forks | 6,097 |
| Issues | 302 |
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
| Stars | 43,369 |
| 语言 | Go |
| Forks | 3,903 |
| Issues | 1,087 |
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
| Stars | 51,656 |
| 语言 | Go |
| Forks | 10,340 |
| Issues | 221 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (9 个项目) { #学习资源 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,868 |
| 语言 | MDX |
| Forks | 7,677 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有超过7万星标的开源项目，汇集了提示词工程、RAG和AI Agent领域最全面的学习资源和实践指南，由DAIR.AI团队精心维护，适合从初学者到高级开发者系统性地掌握大模型应用开发的核心技能。

**技术亮点**:
- 涵盖Prompt Engineering、Context Engineering、RAG和AI Agents四大核心领域的完整知识体系
- 提供可交互的Jupyter Notebooks和实践教程，支持动手学习
- 包含最新LLM技术论文、最佳实践和社区资源汇总
- 基于MDX格式，支持Markdown与React组件结合，便于构建交互式文档
- MIT开源协议，内容持续更新，紧跟AI技术前沿发展

**适用场景**:
- AI应用开发者学习Prompt Engineering和RAG技术，提升大模型应用效果
- 企业团队培训和技术沉淀，建立内部AI开发最佳实践规范
- 研究人员快速了解AI Agents和上下文工程领域的最新进展和技术路线



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,199 |
| 语言 | HTML |
| Forks | 20,162 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,067 |
| 语言 | TypeScript |
| Forks | 5,316 |
| Issues | 52 |
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
| Stars | 34,612 |
| 语言 | HTML |
| Forks | 5,567 |
| Issues | 17 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,481 |
| 语言 | TypeScript |
| Forks | 9,930 |
| Issues | 2,201 |
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
| Stars | 86,737 |
| 语言 | TypeScript |
| Forks | 8,746 |
| Issues | 1,601 |
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
| Stars | 127,124 |
| 语言 | JavaScript |
| Forks | 12,459 |
| Issues | 4 |
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
| Stars | 100,407 |
| 语言 | JavaScript |
| Forks | 7,501 |
| Issues | 222 |
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
| Stars | 167,652 |
| 语言 | Go |
| Forks | 13,068 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (66 个项目) { #其他 }


### 🌟 高优先级


### openclaw/openclaw

**描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 322,705 |
| 语言 | TypeScript |
| Forks | 62,128 |
| Issues | 14,629 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,788 |
| 语言 | Shell |
| Forks | 8,038 |
| Issues | 69 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,183 |
| 语言 | Python |
| Forks | 6,345 |
| Issues | 30 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,143 |
| 语言 | Python |
| Forks | 11,691 |
| Issues | 102 |
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
| Stars | 78,204 |
| 语言 | Python |
| Forks | 6,632 |
| Issues | 632 |
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
| Stars | 131,902 |
| 语言 | Unknown |
| Forks | 33,432 |
| Issues | 131 |
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
| Stars | 384,169 |
| 语言 | Python |
| Forks | 66,025 |
| Issues | 73 |
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
| Stars | 113,030 |
| 语言 | TypeScript |
| Forks | 5,736 |
| Issues | 451 |
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
| Stars | 103,715 |
| 语言 | TypeScript |
| Forks | 7,545 |
| Issues | 189 |
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
| Stars | 47,945 |
| 语言 | Go |
| Forks | 10,248 |
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
| Stars | 98,460 |
| 语言 | C++ |
| Forks | 15,599 |
| Issues | 1,280 |
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
| Stars | 60,647 |
| 语言 | Python |
| Forks | 1,609 |
| Issues | 37 |
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
| Stars | 34,623 |
| 语言 | JavaScript |
| Forks | 2,859 |
| Issues | 179 |
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
| Stars | 339,303 |
| 语言 | Python |
| Forks | 54,938 |
| Issues | 518 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 287,800 |
| 语言 | Python |
| Forks | 27,429 |
| Issues | 19 |
| Topics | awesome, collections, python, python-framework, python-library, python-resources |
| 许可证 | Other |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 218,791 |
| 语言 | Python |
| Forks | 50,225 |
| Issues | 889 |
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
| Stars | 85,432 |
| 语言 | Python |
| Forks | 37,004 |
| Issues | 3,565 |
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
| Stars | 85,360 |
| 语言 | Python |
| Forks | 7,170 |
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
| Stars | 77,688 |
| 语言 | Python |
| Forks | 45,228 |
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
| Stars | 76,146 |
| 语言 | Python |
| Forks | 16,759 |
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
| Stars | 438,427 |
| 语言 | TypeScript |
| Forks | 43,690 |
| Issues | 236 |
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
| Stars | 351,110 |
| 语言 | TypeScript |
| Forks | 43,804 |
| Issues | 30 |
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
| Stars | 119,026 |
| 语言 | TypeScript |
| Forks | 12,916 |
| Issues | 2,849 |
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
| Stars | 109,977 |
| 语言 | TypeScript |
| Forks | 8,250 |
| Issues | 1,795 |
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
| Stars | 108,196 |
| 语言 | TypeScript |
| Forks | 13,306 |
| Issues | 5,490 |
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
| Stars | 97,728 |
| 语言 | TypeScript |
| Forks | 54,576 |
| Issues | 1,371 |
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
| Stars | 95,063 |
| 语言 | TypeScript |
| Forks | 5,138 |
| Issues | 660 |
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
| Stars | 94,096 |
| 语言 | TypeScript |
| Forks | 5,125 |
| Issues | 99 |
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
| Stars | 83,011 |
| 语言 | TypeScript |
| Forks | 7,580 |
| Issues | 34 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,430 |
| 语言 | TypeScript |
| Forks | 9,962 |
| Issues | 533 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,141 |
| 语言 | TypeScript |
| Forks | 7,930 |
| Issues | 668 |
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
| Stars | 244,025 |
| 语言 | JavaScript |
| Forks | 50,828 |
| Issues | 1,180 |
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
| Stars | 138,348 |
| 语言 | JavaScript |
| Forks | 30,660 |
| Issues | 3,499 |
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
| Stars | 116,300 |
| 语言 | JavaScript |
| Forks | 35,094 |
| Issues | 2,525 |
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
| Stars | 111,438 |
| 语言 | JavaScript |
| Forks | 36,310 |
| Issues | 592 |
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
| Stars | 108,653 |
| 语言 | JavaScript |
| Forks | 11,560 |
| Issues | 348 |
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
| Stars | 98,019 |
| 语言 | JavaScript |
| Forks | 32,706 |
| Issues | 1,723 |
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
| Stars | 95,429 |
| 语言 | JavaScript |
| Forks | 15,263 |
| Issues | 46 |
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
| Stars | 86,072 |
| 语言 | JavaScript |
| Forks | 4,811 |
| Issues | 971 |
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
| Stars | 70,779 |
| 语言 | JavaScript |
| Forks | 16,806 |
| Issues | 888 |
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
| Stars | 66,009 |
| 语言 | JavaScript |
| Forks | 9,330 |
| Issues | 200 |
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
| Stars | 62,160 |
| 语言 | JavaScript |
| Forks | 3,982 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,898 |
| 语言 | JavaScript |
| Forks | 5,615 |
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
| Forks | 20,473 |
| Issues | 97 |
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
| Stars | 57,401 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 24 |
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
| Stars | 52,994 |
| 语言 | JavaScript |
| Forks | 10,599 |
| Issues | 479 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,081 |
| 语言 | Go |
| Forks | 18,864 |
| Issues | 9,874 |
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
| Stars | 105,373 |
| 语言 | Go |
| Forks | 14,956 |
| Issues | 48 |
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
| Stars | 87,145 |
| 语言 | Go |
| Forks | 8,214 |
| Issues | 265 |
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
| Stars | 80,926 |
| 语言 | Go |
| Forks | 4,966 |
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
| Stars | 68,678 |
| 语言 | Go |
| Forks | 3,220 |
| Issues | 8 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,099 |
| 语言 | Go |
| Forks | 4,979 |
| Issues | 1,146 |
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
| Stars | 50,923 |
| 语言 | Go |
| Forks | 21,865 |
| Issues | 374 |
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
| Stars | 50,201 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 258 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,176 |
| 语言 | Go |
| Forks | 7,975 |
| Issues | 566 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### opendatalab/MinerU

**描述**: Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,508 |
| 语言 | Python |
| Forks | 4,684 |
| Issues | 194 |
| Topics | ai4science, document-analysis, extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-extractor-llm, pdf-extractor-pretrain, pdf-extractor-rag, pdf-parser, python |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,904 |
| 语言 | Python |
| Forks | 10,604 |
| Issues | 4,118 |
| 许可证 | The Unlicense |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,756 |
| 语言 | JavaScript |
| Forks | 31,115 |
| Issues | 398 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
| 许可证 | MIT License |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,120 |
| 语言 | JavaScript |
| Forks | 26,775 |
| Issues | 189 |
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
| Stars | 78,787 |
| 语言 | JavaScript |
| Forks | 31,561 |
| Issues | 272 |
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
| Stars | 67,276 |
| 语言 | JavaScript |
| Forks | 11,979 |
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
| Stars | 66,290 |
| 语言 | JavaScript |
| Forks | 9,194 |
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
| Stars | 61,580 |
| 语言 | JavaScript |
| Forks | 7,127 |
| Issues | 132 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


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
| Forks | 8,878 |
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
| Stars | 45,516 |
| 语言 | Go |
| Forks | 3,774 |
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
| Stars | 146,628 |
| 语言 | Python |
| Forks | 11,245 |
| Issues | 301 |
| Topics | awesome, github, hellogithub, python |
