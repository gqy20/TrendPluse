# 项目发现报告 (2026-03-08)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
| 去重移除 | 33 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 63 |

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
| Stars | 126,221 |
| 语言 | Python |
| Forks | 17,870 |
| Issues | 277 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能强大且用户友好的自托管 AI 交互平台，支持 Ollama 和 OpenAI API 等多种后端，让用户能够快速部署私有的 LLM 服务界面。凭借超过 12 万 Stars 的人气和活跃的社区支持，它是目前最流行的开源 AI 界面解决方案之一。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API、OpenAPI 兼容接口），具备出色的兼容性和扩展性
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答，提升 AI 响应准确性
- 原生支持 MCP（Model Context Protocol）协议，便于与外部工具和数据源集成
- 完全自托管架构，数据隐私可控，适合对安全性要求较高的部署环境
- 现代化的 Web UI 设计，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部部署私有 AI 助手，保护敏感数据不外泄
- 个人开发者搭建本地 LLM 服务，配合 Ollama 实现低成本 AI 应用
- 构建基于知识库的智能问答系统，利用 RAG 能力处理企业文档



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,422 |
| 语言 | Python |
| Forks | 8,302 |
| Issues | 3,056 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最顶级的开源 RAG 引擎之一（74k+ Stars），将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文层，是企业级 RAG 应用开发的标杆项目。它不仅支持多种主流 LLM（OpenAI、Ollama、DeepSeek 等），还集成了 GraphRAG、MCP 协议等最新技术，是构建智能检索增强系统的首选方案。

**技术亮点**:
- 融合 RAG + Agent 双引擎：将检索增强生成与智能代理能力结合，支持复杂的多步骤推理和自动化工作流
- 支持 GraphRAG 知识图谱增强：利用图结构进行深度知识关联和推理，提升复杂查询的理解能力
- 深度文档理解引擎：集成先进的文档解析器，支持多种格式文档的精准理解和结构化提取
- 全面生态兼容：支持 OpenAI、DeepSeek-R1、Ollama 等主流 LLM，以及 MCP 协议的标准化集成
- Deep Research 深度研究能力：支持复杂的研究型任务，适合需要多轮检索和综合分析的场景

**适用场景**:
- 企业知识库与智能问答系统：构建基于企业文档、技术手册、政策法规的智能检索和问答平台
- AI 搜索与深度研究：适用于需要进行多文档综合分析、知识图谱关联查询的研究型场景
- Agentic AI 工作流自动化：构建能够自主规划、检索、推理的智能代理，用于复杂业务流程自动化



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,470 |
| 语言 | TypeScript |
| Forks | 6,249 |
| Issues | 225 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个专为 AI 应用设计的 Web 数据 API，能够将整个网站自动转换为 LLM 可用的 Markdown 或结构化数据，解决了 AI 开发者获取高质量网页数据的痛点，被超过 8.9 万个 Star 验证为业界领先的 AI 数据采集解决方案。

**技术亮点**:
- 一站式 Web 数据 API：自动爬取整个网站并转换为 LLM-ready 的 Markdown 格式，无需手动处理 HTML 解析
- 智能数据提取：支持将网页内容转换为结构化数据，方便 AI 模型直接消费
- 多场景支持：涵盖 AI 爬虫、AI 搜索、网页抓取、HTML 转 Markdown 等多种能力
- TypeScript 原生开发：现代化的技术栈，易于集成和扩展
- 专为 AI 时代设计：针对 LLM 和 AI Agents 优化的数据输出格式

**适用场景**:
- 企业级 RAG 系统构建：快速将企业官网、文档站点、知识库转换为 LLM 可理解的结构化数据，用于构建智能问答系统
- AI Agent 数据采集：为自主 AI 智能体提供实时网页数据获取能力，支持网页搜索和内容提取
- 开发者数据管道：个人开发者或团队快速搭建从网页到 AI 模型的数据预处理流程，大幅降低开发成本



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,984 |
| 语言 | JavaScript |
| Forks | 8,341 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具创新性的AI代码助手增强系统，通过技能、直觉、记忆、安全和研究优先开发的完整框架，显著提升Claude Code、Cursor等主流AI编程工具的性能表现。凭借近7万Star的超高人气和MIT开源许可，它已成为开发者优化AI辅助编程体验的首选工具。

**技术亮点**:
- 🧠 智能代理驾驭系统：集成Skills、Instincts、Memory多维度能力，实现AI代理的性能优化与自主进化
- 🔒 安全与研究优先架构：内置安全机制和research-first开发模式，确保代码质量与安全性
- 🛠️ 多平台兼容能力：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一增强
- 📡 MCP协议集成：通过Model Context Protocol实现与LLM的高效交互和上下文管理
- ⚡ 性能优化引擎：针对AI代码生成场景的专项优化，提升开发效率和代码质量

**适用场景**:
- 企业级AI辅助开发：团队可利用此系统统一增强Claude Code、Cursor等工具的代码生成能力，提升整体开发效率30%以上
- 个人开发者AI工具升级：为独立开发者提供开箱即用的AI编程助手增强方案，无需复杂配置即可获得更智能的代码建议
- AI Agent研究与应用开发：研究人员和工程师可基于此框架快速构建和优化定制化的AI代码代理系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,389 |
| 语言 | Go |
| Forks | 3,652 |
| Issues | 144 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的开源替代品，它最大的价值在于让开发者能够在消费级硬件上无需 GPU 即可运行各种 AI 模型（包括文本生成、图像生成、音频生成等），同时支持去中心化和分布式推理，非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 无需 GPU 的本地推理：可在消费级硬件上运行，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：作为 Drop-in replacement，可无缝替换 OpenAI API，降低迁移成本
- 多模态支持：涵盖文本生成、图像生成、音频生成、视频生成、语音克隆、物体检测等多种 AI 能力
- 分布式与去中心化架构：支持 P2P 和分布式推理，具备良好的扩展性
- 支持 MCP (Model Context Protocol) 和多种主流开源模型（LLaMA、Mistral、Gemma、RWKV 等）

**适用场景**:
- 企业私有化部署：对数据隐私要求高的企业可在内网环境部署，避免敏感数据上传到云端
- 个人开发者低成本 AI 应用开发：无需昂贵的 GPU 服务器，在普通电脑上即可开发和测试 AI 应用
- 边缘计算和离线场景：适合网络受限或需要离线运行的环境，如物联网设备、移动应用等



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,281 |
| 语言 | TypeScript |
| Forks | 14,748 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的明星级 AI Agent 平台，将 AI 智能体协作推向新高度。它不仅支持多智能体协同工作，还创新性地将 Agent 作为工作交互的基本单元，让用户能够轻松构建、设计和管理与自身共同成长的 AI 团队伙伴。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工合作
- 广泛模型兼容性：支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流 AI 模型
- 知识库集成：内置知识管理能力，支持 MCP (Model Context Protocol) 协议
- TypeScript 全栈架构：采用现代前端技术栈，提供优秀的开发体验和类型安全
- Agent Harness 下一代设计：提供可视化 Agent 团队设计工具，降低 AI 应用开发门槛

**适用场景**:
- 企业智能客服与业务流程自动化：企业可构建多 Agent 协作系统处理复杂业务场景
- 个人 AI 助手定制与知识管理：个人用户可打造专属 AI 工作伙伴，整合个人知识库
- AI 应用快速原型开发：开发者可利用平台快速搭建和测试多 Agent 应用场景



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,048 |
| 语言 | Python |
| Forks | 8,296 |
| Issues | 923 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个获得 ACL 2024 认可的大模型微调一站式解决方案，支持 100+ 主流大语言模型和多模态模型的统一高效微调，包括 LLaMA、Qwen、DeepSeek、GPT、Gemma 等热门模型，是目前社区中最全面、最受欢迎的 LLM 微调工具之一。

**技术亮点**:
- 支持 100+ 大语言模型和多模态模型（VLM）的统一微调框架，覆盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化技术，大幅降低训练资源门槛
- 支持全栈微调方法：指令微调（Instruction Tuning）、RLHF 人类反馈强化学习、MoE 模型微调
- 内置模型量化能力，支持在有限显存条件下训练和部署大模型
- Agent 能力支持，可训练具备工具调用和推理能力的智能体模型

**适用场景**:
- 企业级场景：快速定制行业专属大模型，基于开源模型进行垂直领域微调（如客服、医疗、法律等）
- 个人开发者/研究者：低资源环境下微调大模型，仅需单卡 GPU 即可完成 7B-70B 模型的 LoRA/QLoRA 微调
- AI 应用开发：构建具备特定能力的智能体（Agent），如工具调用、知识问答、多模态理解等应用



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,361 |
| 语言 | Java |
| Forks | 15,831 |
| Issues | 50 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot是一个融合AI能力的低代码开发平台，通过"低代码+零代码"双模驱动，结合AI应用、知识库、流程编排等智能化特性，让开发者无需手写代码即可快速构建企业级应用，大幅提升开发效率的同时保持业务灵活性。

**技术亮点**:
- 基于Spring Boot 3 + Spring Cloud微服务架构，采用Vue3 + Ant Design Vue前后端分离技术栈
- 集成LangChain4j、Spring AI等主流AI框架，支持LLM大模型、RAG知识检索、AI Agent智能体
- 内置强大的代码生成器，实现前后端代码一键生成，支持MyBatis-Plus数据持久层
- 支持Flowable/Activiti工作流引擎和AIFlow AI流程编排，满足复杂业务流程需求
- 提供MCP协议和插件扩展机制，支持聊天式业务操作和AI应用快速集成

**适用场景**:
- 企业级管理系统快速开发：如ERP、CRM、OA等业务系统的快速搭建与定制
- AI应用开发：构建企业AI聊天助手、知识库问答、智能客服等AI应用场景
- 业务流程数字化：结合工作流引擎实现审批流程、业务编排等流程自动化



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,009 |
| 语言 | Python |
| Forks | 9,801 |
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
| Stars | 34,436 |
| 语言 | TypeScript |
| Forks | 6,955 |
| Issues | 434 |
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
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 2,302 |
| Issues | 87 |
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
| Stars | 33,287 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 96 |
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
| Stars | 38,653 |
| 语言 | Python |
| Forks | 6,123 |
| Issues | 193 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,860 |
| 语言 | Python |
| Forks | 14,661 |
| Issues | 5 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,903 |
| 语言 | JavaScript |
| Forks | 6,041 |
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
| Stars | 68,758 |
| 语言 | Python |
| Forks | 8,593 |
| Issues | 367 |
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
| Stars | 38,092 |
| 语言 | TypeScript |
| Forks | 2,871 |
| Issues | 359 |
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
| Stars | 79,914 |
| 语言 | Python |
| Forks | 9,444 |
| Issues | 228 |
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
| Stars | 50,521 |
| 语言 | TypeScript |
| Forks | 23,896 |
| Issues | 806 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,664 |
| 语言 | Python |
| Forks | 3,364 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,127 |
| 语言 | TypeScript |
| Forks | 55,554 |
| Issues | 1,402 |
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
| Stars | 145,351 |
| 语言 | Python |
| Forks | 8,532 |
| Issues | 891 |
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
| Stars | 53,391 |
| 语言 | Jupyter Notebook |
| Forks | 18,543 |
| Issues | 2 |
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
| Stars | 71,274 |
| 语言 | MDX |
| Forks | 7,595 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,220 |
| 语言 | TypeScript |
| Forks | 3,458 |
| Issues | 260 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,134 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,925 |
| 语言 | Python |
| Forks | 4,175 |
| Issues | 260 |
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
| Stars | 126,221 |
| 语言 | Python |
| Forks | 17,870 |
| Issues | 277 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能强大且用户友好的自托管 AI 交互平台，支持 Ollama 和 OpenAI API 等多种后端，让用户能够快速部署私有的 LLM 服务界面。凭借超过 12 万 Stars 的人气和活跃的社区支持，它是目前最流行的开源 AI 界面解决方案之一。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API、OpenAPI 兼容接口），具备出色的兼容性和扩展性
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答，提升 AI 响应准确性
- 原生支持 MCP（Model Context Protocol）协议，便于与外部工具和数据源集成
- 完全自托管架构，数据隐私可控，适合对安全性要求较高的部署环境
- 现代化的 Web UI 设计，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部部署私有 AI 助手，保护敏感数据不外泄
- 个人开发者搭建本地 LLM 服务，配合 Ollama 实现低成本 AI 应用
- 构建基于知识库的智能问答系统，利用 RAG 能力处理企业文档



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,422 |
| 语言 | Python |
| Forks | 8,302 |
| Issues | 3,056 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最顶级的开源 RAG 引擎之一（74k+ Stars），将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文层，是企业级 RAG 应用开发的标杆项目。它不仅支持多种主流 LLM（OpenAI、Ollama、DeepSeek 等），还集成了 GraphRAG、MCP 协议等最新技术，是构建智能检索增强系统的首选方案。

**技术亮点**:
- 融合 RAG + Agent 双引擎：将检索增强生成与智能代理能力结合，支持复杂的多步骤推理和自动化工作流
- 支持 GraphRAG 知识图谱增强：利用图结构进行深度知识关联和推理，提升复杂查询的理解能力
- 深度文档理解引擎：集成先进的文档解析器，支持多种格式文档的精准理解和结构化提取
- 全面生态兼容：支持 OpenAI、DeepSeek-R1、Ollama 等主流 LLM，以及 MCP 协议的标准化集成
- Deep Research 深度研究能力：支持复杂的研究型任务，适合需要多轮检索和综合分析的场景

**适用场景**:
- 企业知识库与智能问答系统：构建基于企业文档、技术手册、政策法规的智能检索和问答平台
- AI 搜索与深度研究：适用于需要进行多文档综合分析、知识图谱关联查询的研究型场景
- Agentic AI 工作流自动化：构建能够自主规划、检索、推理的智能代理，用于复杂业务流程自动化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,281 |
| 语言 | TypeScript |
| Forks | 14,748 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的明星级 AI Agent 平台，将 AI 智能体协作推向新高度。它不仅支持多智能体协同工作，还创新性地将 Agent 作为工作交互的基本单元，让用户能够轻松构建、设计和管理与自身共同成长的 AI 团队伙伴。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工合作
- 广泛模型兼容性：支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流 AI 模型
- 知识库集成：内置知识管理能力，支持 MCP (Model Context Protocol) 协议
- TypeScript 全栈架构：采用现代前端技术栈，提供优秀的开发体验和类型安全
- Agent Harness 下一代设计：提供可视化 Agent 团队设计工具，降低 AI 应用开发门槛

**适用场景**:
- 企业智能客服与业务流程自动化：企业可构建多 Agent 协作系统处理复杂业务场景
- 个人 AI 助手定制与知识管理：个人用户可打造专属 AI 工作伙伴，整合个人知识库
- AI 应用快速原型开发：开发者可利用平台快速搭建和测试多 Agent 应用场景



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,361 |
| 语言 | Java |
| Forks | 15,831 |
| Issues | 50 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot是一个融合AI能力的低代码开发平台，通过"低代码+零代码"双模驱动，结合AI应用、知识库、流程编排等智能化特性，让开发者无需手写代码即可快速构建企业级应用，大幅提升开发效率的同时保持业务灵活性。

**技术亮点**:
- 基于Spring Boot 3 + Spring Cloud微服务架构，采用Vue3 + Ant Design Vue前后端分离技术栈
- 集成LangChain4j、Spring AI等主流AI框架，支持LLM大模型、RAG知识检索、AI Agent智能体
- 内置强大的代码生成器，实现前后端代码一键生成，支持MyBatis-Plus数据持久层
- 支持Flowable/Activiti工作流引擎和AIFlow AI流程编排，满足复杂业务流程需求
- 提供MCP协议和插件扩展机制，支持聊天式业务操作和AI应用快速集成

**适用场景**:
- 企业级管理系统快速开发：如ERP、CRM、OA等业务系统的快速搭建与定制
- AI应用开发：构建企业AI聊天助手、知识库问答、智能客服等AI应用场景
- 业务流程数字化：结合工作流引擎实现审批流程、业务编排等流程自动化



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 2,302 |
| Issues | 87 |
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
| Stars | 33,287 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 96 |
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
| Stars | 38,653 |
| 语言 | Python |
| Forks | 6,123 |
| Issues | 193 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,860 |
| 语言 | Python |
| Forks | 14,661 |
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
| Stars | 98,711 |
| 语言 | TypeScript |
| Forks | 11,739 |
| Issues | 966 |
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
| Stars | 55,903 |
| 语言 | JavaScript |
| Forks | 6,041 |
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
| Stars | 50,521 |
| 语言 | TypeScript |
| Forks | 23,896 |
| Issues | 806 |
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
| Stars | 71,823 |
| 语言 | Python |
| Forks | 9,921 |
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
| Stars | 43,197 |
| 语言 | Go |
| Forks | 3,876 |
| Issues | 1,042 |
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
| Stars | 31,301 |
| 语言 | Python |
| Forks | 3,305 |
| Issues | 76 |
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
| Stars | 71,274 |
| 语言 | MDX |
| Forks | 7,595 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,220 |
| 语言 | TypeScript |
| Forks | 3,458 |
| Issues | 260 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,134 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
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
| Stars | 126,221 |
| 语言 | Python |
| Forks | 17,870 |
| Issues | 277 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能强大且用户友好的自托管 AI 交互平台，支持 Ollama 和 OpenAI API 等多种后端，让用户能够快速部署私有的 LLM 服务界面。凭借超过 12 万 Stars 的人气和活跃的社区支持，它是目前最流行的开源 AI 界面解决方案之一。

**技术亮点**:
- 支持多种 LLM 后端（Ollama、OpenAI API、OpenAPI 兼容接口），具备出色的兼容性和扩展性
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答，提升 AI 响应准确性
- 原生支持 MCP（Model Context Protocol）协议，便于与外部工具和数据源集成
- 完全自托管架构，数据隐私可控，适合对安全性要求较高的部署环境
- 现代化的 Web UI 设计，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部部署私有 AI 助手，保护敏感数据不外泄
- 个人开发者搭建本地 LLM 服务，配合 Ollama 实现低成本 AI 应用
- 构建基于知识库的智能问答系统，利用 RAG 能力处理企业文档



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,422 |
| 语言 | Python |
| Forks | 8,302 |
| Issues | 3,056 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最顶级的开源 RAG 引擎之一（74k+ Stars），将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供卓越的上下文层，是企业级 RAG 应用开发的标杆项目。它不仅支持多种主流 LLM（OpenAI、Ollama、DeepSeek 等），还集成了 GraphRAG、MCP 协议等最新技术，是构建智能检索增强系统的首选方案。

**技术亮点**:
- 融合 RAG + Agent 双引擎：将检索增强生成与智能代理能力结合，支持复杂的多步骤推理和自动化工作流
- 支持 GraphRAG 知识图谱增强：利用图结构进行深度知识关联和推理，提升复杂查询的理解能力
- 深度文档理解引擎：集成先进的文档解析器，支持多种格式文档的精准理解和结构化提取
- 全面生态兼容：支持 OpenAI、DeepSeek-R1、Ollama 等主流 LLM，以及 MCP 协议的标准化集成
- Deep Research 深度研究能力：支持复杂的研究型任务，适合需要多轮检索和综合分析的场景

**适用场景**:
- 企业知识库与智能问答系统：构建基于企业文档、技术手册、政策法规的智能检索和问答平台
- AI 搜索与深度研究：适用于需要进行多文档综合分析、知识图谱关联查询的研究型场景
- Agentic AI 工作流自动化：构建能够自主规划、检索、推理的智能代理，用于复杂业务流程自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,984 |
| 语言 | JavaScript |
| Forks | 8,341 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具创新性的AI代码助手增强系统，通过技能、直觉、记忆、安全和研究优先开发的完整框架，显著提升Claude Code、Cursor等主流AI编程工具的性能表现。凭借近7万Star的超高人气和MIT开源许可，它已成为开发者优化AI辅助编程体验的首选工具。

**技术亮点**:
- 🧠 智能代理驾驭系统：集成Skills、Instincts、Memory多维度能力，实现AI代理的性能优化与自主进化
- 🔒 安全与研究优先架构：内置安全机制和research-first开发模式，确保代码质量与安全性
- 🛠️ 多平台兼容能力：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一增强
- 📡 MCP协议集成：通过Model Context Protocol实现与LLM的高效交互和上下文管理
- ⚡ 性能优化引擎：针对AI代码生成场景的专项优化，提升开发效率和代码质量

**适用场景**:
- 企业级AI辅助开发：团队可利用此系统统一增强Claude Code、Cursor等工具的代码生成能力，提升整体开发效率30%以上
- 个人开发者AI工具升级：为独立开发者提供开箱即用的AI编程助手增强方案，无需复杂配置即可获得更智能的代码建议
- AI Agent研究与应用开发：研究人员和工程师可基于此框架快速构建和优化定制化的AI代码代理系统



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,281 |
| 语言 | TypeScript |
| Forks | 14,748 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的明星级 AI Agent 平台，将 AI 智能体协作推向新高度。它不仅支持多智能体协同工作，还创新性地将 Agent 作为工作交互的基本单元，让用户能够轻松构建、设计和管理与自身共同成长的 AI 团队伙伴。

**技术亮点**:
- 多智能体协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工合作
- 广泛模型兼容性：支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流 AI 模型
- 知识库集成：内置知识管理能力，支持 MCP (Model Context Protocol) 协议
- TypeScript 全栈架构：采用现代前端技术栈，提供优秀的开发体验和类型安全
- Agent Harness 下一代设计：提供可视化 Agent 团队设计工具，降低 AI 应用开发门槛

**适用场景**:
- 企业智能客服与业务流程自动化：企业可构建多 Agent 协作系统处理复杂业务场景
- 个人 AI 助手定制与知识管理：个人用户可打造专属 AI 工作伙伴，整合个人知识库
- AI 应用快速原型开发：开发者可利用平台快速搭建和测试多 Agent 应用场景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,807 |
| 语言 | HTML |
| Forks | 19,816 |
| Issues | 13 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有15万+ Stars的现象级开源项目，汇集了社区贡献的优质AI提示词，帮助用户快速掌握提示工程技巧。项目支持私有化部署，让企业能在保护隐私的前提下构建内部提示词知识库，极大提升AI工具的使用效率。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 构建的现代化 Web 应用，技术栈成熟稳定
- 采用开源架构设计，支持组织内部私有化部署，确保数据完全自主可控
- 社区驱动的提示词收集机制，汇集海量经过验证的高质量 Prompt 模板
- 支持多种主流 LLM 平台（ChatGPT、Claude、Gemini、GPT-4），兼容性强
- CC0 许可证完全开放，允许自由使用、修改和商业应用

**适用场景**:
- 企业内部搭建私有提示词库，沉淀团队 AI 使用经验，提升整体工作效率
- 个人开发者学习和参考优质提示词范例，快速掌握提示工程技巧
- AI 应用开发者获取灵感，为自己的产品设计和优化 Prompt 策略



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,427 |
| 语言 | Jupyter Notebook |
| Forks | 13,300 |
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
| Stars | 42,009 |
| 语言 | Python |
| Forks | 9,801 |
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
| Stars | 34,436 |
| 语言 | TypeScript |
| Forks | 6,955 |
| Issues | 434 |
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
| Stars | 33,466 |
| 语言 | TypeScript |
| Forks | 2,302 |
| Issues | 87 |
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
| Stars | 33,287 |
| 语言 | Python |
| Forks | 2,046 |
| Issues | 96 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,903 |
| 语言 | JavaScript |
| Forks | 6,041 |
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
| Stars | 68,758 |
| 语言 | Python |
| Forks | 8,593 |
| Issues | 367 |
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
| Stars | 38,092 |
| 语言 | TypeScript |
| Forks | 2,871 |
| Issues | 359 |
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
| Stars | 50,521 |
| 语言 | TypeScript |
| Forks | 23,896 |
| Issues | 806 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,664 |
| 语言 | Python |
| Forks | 3,364 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,994 |
| 语言 | HTML |
| Forks | 5,433 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,431 |
| 语言 | Python |
| Forks | 14,096 |
| Issues | 3,556 |
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
| Stars | 38,460 |
| 语言 | Python |
| Forks | 3,729 |
| Issues | 63 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,482 |
| 语言 | Python |
| Forks | 2,551 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,351 |
| 语言 | Python |
| Forks | 8,532 |
| Issues | 891 |
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
| Stars | 164,447 |
| 语言 | Go |
| Forks | 14,836 |
| Issues | 2,609 |
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
| Stars | 71,274 |
| 语言 | MDX |
| Forks | 7,595 |
| Issues | 248 |
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
| Stars | 46,518 |
| 语言 | Rust |
| Forks | 9,094 |
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
| Stars | 38,829 |
| 语言 | TypeScript |
| Forks | 3,926 |
| Issues | 1,063 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,925 |
| 语言 | Python |
| Forks | 4,175 |
| Issues | 260 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 90,367 |
| 语言 | Python |
| Forks | 5,320 |
| Issues | 461 |
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
| Stars | 68,048 |
| 语言 | Python |
| Forks | 8,296 |
| Issues | 923 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个获得 ACL 2024 认可的大模型微调一站式解决方案，支持 100+ 主流大语言模型和多模态模型的统一高效微调，包括 LLaMA、Qwen、DeepSeek、GPT、Gemma 等热门模型，是目前社区中最全面、最受欢迎的 LLM 微调工具之一。

**技术亮点**:
- 支持 100+ 大语言模型和多模态模型（VLM）的统一微调框架，覆盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化技术，大幅降低训练资源门槛
- 支持全栈微调方法：指令微调（Instruction Tuning）、RLHF 人类反馈强化学习、MoE 模型微调
- 内置模型量化能力，支持在有限显存条件下训练和部署大模型
- Agent 能力支持，可训练具备工具调用和推理能力的智能体模型

**适用场景**:
- 企业级场景：快速定制行业专属大模型，基于开源模型进行垂直领域微调（如客服、医疗、法律等）
- 个人开发者/研究者：低资源环境下微调大模型，仅需单卡 GPU 即可完成 7B-70B 模型的 LoRA/QLoRA 微调
- AI 应用开发：构建具备特定能力的智能体（Agent），如工具调用、知识问答、多模态理解等应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,706 |
| 语言 | Python |
| Forks | 6,138 |
| Issues | 61 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是目前 GitHub 上最受欢迎的开源金融数据平台，拥有超过 6.2 万 Stars，为金融分析师、量化研究员和 AI 应用提供统一的数据接入层。它将股票、加密货币、期权、衍生品、宏观经济等多维度金融数据整合到一个 Python 平台中，显著降低了金融数据获取的门槛和成本。

**技术亮点**:
- 支持多资产类别数据整合：涵盖股票、加密货币、期权、衍生品、固定收益和宏观经济数据
- 专为 AI Agent 设计：提供结构化金融数据接口，方便构建金融领域的 AI 应用和智能分析工具
- Python 原生支持：提供简洁的 Python API，便于量化分析师和开发者快速集成
- 机器学习友好：内置 ML 相关功能，支持量化金融策略开发和回测
- 开放架构设计：可扩展的数据源插件系统，支持自定义数据源接入

**适用场景**:
- 量化交易策略研究：个人量化开发者可快速获取多市场数据进行策略开发和回测
- 金融 AI 应用开发：为 AI Agent 和大模型应用提供结构化的金融数据支撑
- 企业级金融分析平台：金融机构可基于此构建内部数据分析工具，降低商业数据终端成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,807 |
| 语言 | HTML |
| Forks | 19,816 |
| Issues | 13 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有15万+ Stars的现象级开源项目，汇集了社区贡献的优质AI提示词，帮助用户快速掌握提示工程技巧。项目支持私有化部署，让企业能在保护隐私的前提下构建内部提示词知识库，极大提升AI工具的使用效率。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 构建的现代化 Web 应用，技术栈成熟稳定
- 采用开源架构设计，支持组织内部私有化部署，确保数据完全自主可控
- 社区驱动的提示词收集机制，汇集海量经过验证的高质量 Prompt 模板
- 支持多种主流 LLM 平台（ChatGPT、Claude、Gemini、GPT-4），兼容性强
- CC0 许可证完全开放，允许自由使用、修改和商业应用

**适用场景**:
- 企业内部搭建私有提示词库，沉淀团队 AI 使用经验，提升整体工作效率
- 个人开发者学习和参考优质提示词范例，快速掌握提示工程技巧
- AI 应用开发者获取灵感，为自己的产品设计和优化 Prompt 策略



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,427 |
| 语言 | Jupyter Notebook |
| Forks | 13,300 |
| Issues | 0 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,560 |
| 语言 | Python |
| Forks | 32,327 |
| Issues | 2,294 |
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
| Stars | 72,431 |
| 语言 | Python |
| Forks | 14,096 |
| Issues | 3,556 |
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
| Stars | 161,556 |
| 语言 | Python |
| Forks | 30,137 |
| Issues | 2,467 |
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
| Stars | 105,211 |
| 语言 | Python |
| Forks | 12,066 |
| Issues | 3,797 |
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
| Stars | 98,047 |
| 语言 | Python |
| Forks | 27,112 |
| Issues | 18,080 |
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
| Stars | 71,274 |
| 语言 | MDX |
| Forks | 7,595 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,220 |
| 语言 | TypeScript |
| Forks | 3,458 |
| Issues | 260 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,490 |
| 语言 | Jupyter Notebook |
| Forks | 5,134 |
| Issues | 124 |
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
| Stars | 66,984 |
| 语言 | JavaScript |
| Forks | 8,341 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具创新性的AI代码助手增强系统，通过技能、直觉、记忆、安全和研究优先开发的完整框架，显著提升Claude Code、Cursor等主流AI编程工具的性能表现。凭借近7万Star的超高人气和MIT开源许可，它已成为开发者优化AI辅助编程体验的首选工具。

**技术亮点**:
- 🧠 智能代理驾驭系统：集成Skills、Instincts、Memory多维度能力，实现AI代理的性能优化与自主进化
- 🔒 安全与研究优先架构：内置安全机制和research-first开发模式，确保代码质量与安全性
- 🛠️ 多平台兼容能力：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一增强
- 📡 MCP协议集成：通过Model Context Protocol实现与LLM的高效交互和上下文管理
- ⚡ 性能优化引擎：针对AI代码生成场景的专项优化，提升开发效率和代码质量

**适用场景**:
- 企业级AI辅助开发：团队可利用此系统统一增强Claude Code、Cursor等工具的代码生成能力，提升整体开发效率30%以上
- 个人开发者AI工具升级：为独立开发者提供开箱即用的AI编程助手增强方案，无需复杂配置即可获得更智能的代码建议
- AI Agent研究与应用开发：研究人员和工程师可基于此框架快速构建和优化定制化的AI代码代理系统



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,389 |
| 语言 | Go |
| Forks | 3,652 |
| Issues | 144 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的开源替代品，它最大的价值在于让开发者能够在消费级硬件上无需 GPU 即可运行各种 AI 模型（包括文本生成、图像生成、音频生成等），同时支持去中心化和分布式推理，非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 无需 GPU 的本地推理：可在消费级硬件上运行，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：作为 Drop-in replacement，可无缝替换 OpenAI API，降低迁移成本
- 多模态支持：涵盖文本生成、图像生成、音频生成、视频生成、语音克隆、物体检测等多种 AI 能力
- 分布式与去中心化架构：支持 P2P 和分布式推理，具备良好的扩展性
- 支持 MCP (Model Context Protocol) 和多种主流开源模型（LLaMA、Mistral、Gemma、RWKV 等）

**适用场景**:
- 企业私有化部署：对数据隐私要求高的企业可在内网环境部署，避免敏感数据上传到云端
- 个人开发者低成本 AI 应用开发：无需昂贵的 GPU 服务器，在普通电脑上即可开发和测试 AI 应用
- 边缘计算和离线场景：适合网络受限或需要离线运行的环境，如物联网设备、移动应用等



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,758 |
| 语言 | Python |
| Forks | 8,593 |
| Issues | 367 |
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
| Stars | 38,092 |
| 语言 | TypeScript |
| Forks | 2,871 |
| Issues | 359 |
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
| Stars | 178,127 |
| 语言 | TypeScript |
| Forks | 55,554 |
| Issues | 1,402 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,482 |
| 语言 | Python |
| Forks | 2,551 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,184 |
| 语言 | Python |
| Forks | 12,174 |
| Issues | 2,372 |
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
| Stars | 96,006 |
| 语言 | Python |
| Forks | 8,806 |
| Issues | 148 |
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
| Stars | 73,479 |
| 语言 | Python |
| Forks | 8,722 |
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
| Stars | 182,442 |
| 语言 | TypeScript |
| Forks | 38,359 |
| Issues | 14,758 |
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
| Stars | 93,749 |
| 语言 | TypeScript |
| Forks | 9,382 |
| Issues | 288 |
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
| Stars | 78,231 |
| 语言 | TypeScript |
| Forks | 5,628 |
| Issues | 685 |
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
| Stars | 76,540 |
| 语言 | TypeScript |
| Forks | 6,538 |
| Issues | 169 |
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
| Stars | 78,408 |
| 语言 | Go |
| Forks | 2,703 |
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
| Stars | 73,730 |
| 语言 | Go |
| Forks | 2,569 |
| Issues | 906 |
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
| Stars | 405,449 |
| 语言 | Python |
| Forks | 43,785 |
| Issues | 943 |
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
| Stars | 75,638 |
| 语言 | JavaScript |
| Forks | 7,265 |
| Issues | 708 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,092 |
| 语言 | TypeScript |
| Forks | 2,871 |
| Issues | 359 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 30,664 |
| 语言 | Python |
| Forks | 3,364 |
| Issues | 3 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,127 |
| 语言 | TypeScript |
| Forks | 55,554 |
| Issues | 1,402 |
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
| Stars | 51,631 |
| 语言 | Go |
| Forks | 10,336 |
| Issues | 229 |
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
| Stars | 120,998 |
| 语言 | Go |
| Forks | 42,621 |
| Issues | 2,712 |
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
| Stars | 71,487 |
| 语言 | Go |
| Forks | 18,912 |
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
| Stars | 54,174 |
| 语言 | Go |
| Forks | 6,438 |
| Issues | 2,846 |
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
| Stars | 47,551 |
| 语言 | Go |
| Forks | 5,064 |
| Issues | 964 |
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
| Stars | 93,749 |
| 语言 | TypeScript |
| Forks | 9,382 |
| Issues | 288 |
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
| Stars | 83,741 |
| 语言 | TypeScript |
| Forks | 5,247 |
| Issues | 606 |
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
| Stars | 75,072 |
| 语言 | TypeScript |
| Forks | 6,367 |
| Issues | 428 |
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
| Stars | 83,800 |
| 语言 | JavaScript |
| Forks | 7,489 |
| Issues | 703 |
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
| Stars | 69,200 |
| 语言 | Go |
| Forks | 1,871 |
| Issues | 291 |
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
| Stars | 62,087 |
| 语言 | Go |
| Forks | 5,865 |
| Issues | 766 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### usememos/memos

**描述**: An open-source, self-hosted note-taking tool. Capture thoughts instantly, own them completely — no tracking, no ads, no subscription fees.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,572 |
| 语言 | Go |
| Forks | 4,159 |
| Issues | 17 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,925 |
| 语言 | Python |
| Forks | 4,175 |
| Issues | 260 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,449 |
| 语言 | Go |
| Forks | 7,198 |
| Issues | 80 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


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
| Stars | 83,800 |
| 语言 | JavaScript |
| Forks | 7,489 |
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
| Stars | 63,101 |
| 语言 | Go |
| Forks | 10,222 |
| Issues | 763 |
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
| Stars | 43,389 |
| 语言 | Go |
| Forks | 3,652 |
| Issues | 144 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的开源替代品，它最大的价值在于让开发者能够在消费级硬件上无需 GPU 即可运行各种 AI 模型（包括文本生成、图像生成、音频生成等），同时支持去中心化和分布式推理，非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 无需 GPU 的本地推理：可在消费级硬件上运行，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：作为 Drop-in replacement，可无缝替换 OpenAI API，降低迁移成本
- 多模态支持：涵盖文本生成、图像生成、音频生成、视频生成、语音克隆、物体检测等多种 AI 能力
- 分布式与去中心化架构：支持 P2P 和分布式推理，具备良好的扩展性
- 支持 MCP (Model Context Protocol) 和多种主流开源模型（LLaMA、Mistral、Gemma、RWKV 等）

**适用场景**:
- 企业私有化部署：对数据隐私要求高的企业可在内网环境部署，避免敏感数据上传到云端
- 个人开发者低成本 AI 应用开发：无需昂贵的 GPU 服务器，在普通电脑上即可开发和测试 AI 应用
- 边缘计算和离线场景：适合网络受限或需要离线运行的环境，如物联网设备、移动应用等



### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,482 |
| 语言 | Python |
| Forks | 2,551 |
| Issues | 61 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,006 |
| 语言 | Python |
| Forks | 8,806 |
| Issues | 148 |
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
| Stars | 87,010 |
| 语言 | Python |
| Forks | 33,727 |
| Issues | 433 |
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
| Stars | 100,084 |
| 语言 | TypeScript |
| Forks | 27,100 |
| Issues | 1,140 |
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
| Stars | 78,231 |
| 语言 | TypeScript |
| Forks | 5,628 |
| Issues | 685 |
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
| Stars | 74,881 |
| 语言 | TypeScript |
| Forks | 8,236 |
| Issues | 44 |
| Topics | framework, hacktoberfest, javascript, javascript-framework, microservices, nest, nestjs, node, nodejs, nodejs-framework, typescript, typescript-framework, websockets |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,878 |
| 语言 | JavaScript |
| Forks | 22,751 |
| Issues | 189 |
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
| Stars | 55,938 |
| 语言 | JavaScript |
| Forks | 10,219 |
| Issues | 345 |
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
| Stars | 88,225 |
| 语言 | Go |
| Forks | 8,568 |
| Issues | 647 |
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
| Stars | 70,666 |
| 语言 | Go |
| Forks | 4,662 |
| Issues | 232 |
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
| Stars | 56,616 |
| 语言 | Go |
| Forks | 3,164 |
| Issues | 25 |
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
| Stars | 405,449 |
| 语言 | Python |
| Forks | 43,785 |
| Issues | 943 |
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
| Stars | 75,638 |
| 语言 | JavaScript |
| Forks | 7,265 |
| Issues | 708 |
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
| Stars | 98,711 |
| 语言 | TypeScript |
| Forks | 11,739 |
| Issues | 966 |
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
| Stars | 55,903 |
| 语言 | JavaScript |
| Forks | 6,041 |
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
| Stars | 43,197 |
| 语言 | Go |
| Forks | 3,876 |
| Issues | 1,042 |
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
| Stars | 51,631 |
| 语言 | Go |
| Forks | 10,336 |
| Issues | 229 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,807 |
| 语言 | HTML |
| Forks | 19,816 |
| Issues | 13 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有15万+ Stars的现象级开源项目，汇集了社区贡献的优质AI提示词，帮助用户快速掌握提示工程技巧。项目支持私有化部署，让企业能在保护隐私的前提下构建内部提示词知识库，极大提升AI工具的使用效率。

**技术亮点**:
- 基于 Next.js + TypeScript + HTML 构建的现代化 Web 应用，技术栈成熟稳定
- 采用开源架构设计，支持组织内部私有化部署，确保数据完全自主可控
- 社区驱动的提示词收集机制，汇集海量经过验证的高质量 Prompt 模板
- 支持多种主流 LLM 平台（ChatGPT、Claude、Gemini、GPT-4），兼容性强
- CC0 许可证完全开放，允许自由使用、修改和商业应用

**适用场景**:
- 企业内部搭建私有提示词库，沉淀团队 AI 使用经验，提升整体工作效率
- 个人开发者学习和参考优质提示词范例，快速掌握提示工程技巧
- AI 应用开发者获取灵感，为自己的产品设计和优化 Prompt 策略



### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,994 |
| 语言 | HTML |
| Forks | 5,433 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,274 |
| 语言 | MDX |
| Forks | 7,595 |
| Issues | 248 |
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
| Stars | 89,393 |
| 语言 | TypeScript |
| Forks | 9,893 |
| Issues | 2,229 |
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
| Stars | 86,544 |
| 语言 | TypeScript |
| Forks | 8,698 |
| Issues | 1,627 |
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
| Stars | 126,989 |
| 语言 | JavaScript |
| Forks | 12,444 |
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
| Stars | 99,696 |
| 语言 | JavaScript |
| Forks | 7,455 |
| Issues | 204 |
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
| Stars | 166,881 |
| 语言 | Go |
| Forks | 13,027 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 129,522 |
| 语言 | Unknown |
| Forks | 33,023 |
| Issues | 129 |
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
| Stars | 41,015 |
| 语言 | TypeScript |
| Forks | 3,784 |
| Issues | 674 |
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
| Stars | 279,964 |
| 语言 | TypeScript |
| Forks | 53,429 |
| Issues | 11,073 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,537 |
| 语言 | Python |
| Forks | 6,285 |
| Issues | 37 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,899 |
| 语言 | Python |
| Forks | 11,642 |
| Issues | 127 |
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
| Stars | 74,975 |
| 语言 | Python |
| Forks | 6,394 |
| Issues | 638 |
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
| Stars | 383,766 |
| 语言 | Python |
| Forks | 66,012 |
| Issues | 74 |
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
| Stars | 112,592 |
| 语言 | TypeScript |
| Forks | 5,684 |
| Issues | 455 |
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
| Stars | 101,230 |
| 语言 | TypeScript |
| Forks | 7,371 |
| Issues | 172 |
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
| Stars | 47,905 |
| 语言 | Go |
| Forks | 10,238 |
| Issues | 1,915 |
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
| Stars | 97,187 |
| 语言 | C++ |
| Forks | 15,322 |
| Issues | 1,218 |
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
| Stars | 59,468 |
| 语言 | Python |
| Forks | 1,610 |
| Issues | 36 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 286,206 |
| 语言 | Python |
| Forks | 27,329 |
| Issues | 22 |
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
| Stars | 218,434 |
| 语言 | Python |
| Forks | 50,132 |
| Issues | 928 |
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
| Stars | 85,217 |
| 语言 | Python |
| Forks | 36,943 |
| Issues | 3,554 |
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
| Stars | 77,690 |
| 语言 | Python |
| Forks | 45,251 |
| Issues | 1,283 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,865 |
| 语言 | Python |
| Forks | 16,722 |
| Issues | 14 |
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
| Stars | 437,910 |
| 语言 | TypeScript |
| Forks | 43,542 |
| Issues | 283 |
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
| Stars | 350,485 |
| 语言 | TypeScript |
| Forks | 43,751 |
| Issues | 45 |
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
| Stars | 118,272 |
| 语言 | TypeScript |
| Forks | 12,790 |
| Issues | 2,824 |
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
| Stars | 108,564 |
| 语言 | TypeScript |
| Forks | 8,068 |
| Issues | 1,796 |
| Topics | base-ui, components, nextjs, radix-ui, react, shadcn, tailwindcss, ui |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,065 |
| 语言 | TypeScript |
| Forks | 13,267 |
| Issues | 5,479 |
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
| Stars | 97,686 |
| 语言 | TypeScript |
| Forks | 54,538 |
| Issues | 1,366 |
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
| Stars | 94,291 |
| 语言 | TypeScript |
| Forks | 5,038 |
| Issues | 663 |
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
| Stars | 93,960 |
| 语言 | TypeScript |
| Forks | 5,102 |
| Issues | 87 |
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
| Stars | 82,947 |
| 语言 | TypeScript |
| Forks | 7,575 |
| Issues | 37 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,503 |
| 语言 | TypeScript |
| Forks | 9,813 |
| Issues | 433 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,666 |
| 语言 | TypeScript |
| Forks | 7,886 |
| Issues | 624 |
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
| Stars | 243,722 |
| 语言 | JavaScript |
| Forks | 50,674 |
| Issues | 1,152 |
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
| Stars | 138,213 |
| 语言 | JavaScript |
| Forks | 30,583 |
| Issues | 3,431 |
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
| Stars | 116,142 |
| 语言 | JavaScript |
| Forks | 34,949 |
| Issues | 2,510 |
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
| Stars | 111,240 |
| 语言 | JavaScript |
| Forks | 36,288 |
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
| Stars | 108,603 |
| 语言 | JavaScript |
| Forks | 11,538 |
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
| Stars | 98,016 |
| 语言 | JavaScript |
| Forks | 32,707 |
| Issues | 1,725 |
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
| Stars | 95,394 |
| 语言 | JavaScript |
| Forks | 15,218 |
| Issues | 42 |
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
| Stars | 86,024 |
| 语言 | JavaScript |
| Forks | 4,799 |
| Issues | 976 |
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
| Stars | 78,654 |
| 语言 | JavaScript |
| Forks | 31,405 |
| Issues | 271 |
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
| Stars | 70,682 |
| 语言 | JavaScript |
| Forks | 16,801 |
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
| Stars | 66,268 |
| 语言 | JavaScript |
| Forks | 9,180 |
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
| Stars | 66,038 |
| 语言 | JavaScript |
| Forks | 9,312 |
| Issues | 201 |
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
| Stars | 61,968 |
| 语言 | JavaScript |
| Forks | 3,966 |
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
| Stars | 59,858 |
| 语言 | JavaScript |
| Forks | 20,470 |
| Issues | 98 |
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
| Stars | 59,717 |
| 语言 | JavaScript |
| Forks | 5,600 |
| Issues | 63 |
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
| Stars | 57,398 |
| 语言 | JavaScript |
| Forks | 12,311 |
| Issues | 24 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,964 |
| 语言 | Go |
| Forks | 18,850 |
| Issues | 9,834 |
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
| Stars | 104,992 |
| 语言 | Go |
| Forks | 14,924 |
| Issues | 42 |
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
| Stars | 86,964 |
| 语言 | Go |
| Forks | 8,197 |
| Issues | 269 |
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
| Stars | 80,619 |
| 语言 | Go |
| Forks | 4,946 |
| Issues | 405 |
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
| Stars | 68,706 |
| 语言 | Go |
| Forks | 3,216 |
| Issues | 11 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,911 |
| 语言 | Go |
| Forks | 4,953 |
| Issues | 1,134 |
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
| Stars | 50,904 |
| 语言 | Go |
| Forks | 21,829 |
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
| Stars | 49,130 |
| 语言 | Go |
| Forks | 7,980 |
| Issues | 571 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,930 |
| 语言 | Go |
| Forks | 8,885 |
| Issues | 6 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,296 |
| 语言 | Go |
| Forks | 3,751 |
| Issues | 91 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,820 |
| 语言 | Python |
| Forks | 10,602 |
| Issues | 4,118 |
| 许可证 | The Unlicense |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,042 |
| 语言 | Python |
| Forks | 7,155 |
| Issues | 474 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,748 |
| 语言 | JavaScript |
| Forks | 31,105 |
| Issues | 393 |
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
| Stars | 148,101 |
| 语言 | JavaScript |
| Forks | 26,776 |
| Issues | 187 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### FortAwesome/Font-Awesome

**描述**: The iconic SVG, font, and CSS toolkit

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,402 |
| 语言 | JavaScript |
| Forks | 12,243 |
| Issues | 316 |
| Topics | css, font, fontawesome, icons, svg-icons, svg-sprites, webfont |
| 许可证 | Other |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,232 |
| 语言 | JavaScript |
| Forks | 11,987 |
| Issues | 536 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,767 |
| 语言 | JavaScript |
| Forks | 4,466 |
| Issues | 94 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,581 |
| 语言 | JavaScript |
| Forks | 7,124 |
| Issues | 127 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 145,283 |
| 语言 | Python |
| Forks | 11,181 |
| Issues | 287 |
| Topics | awesome, github, hellogithub, python |
