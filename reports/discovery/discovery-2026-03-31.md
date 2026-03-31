# 项目发现报告 (2026-03-31)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 137 |
| 去重移除 | 28 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
| 📁 其他 | 65 |

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
| Stars | 129,454 |
| 语言 | Python |
| Forks | 18,326 |
| Issues | 305 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，提供现代化的 Web UI 和 RAG 支持，Stars 超过 12 万，是自托管 LLM 界面的首选项目，让用户无需复杂配置即可拥有类似 ChatGPT 的体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、MCP 等多种 LLM 提供商，支持灵活切换
- RAG 增强能力：内置检索增强生成功能，支持文档上传和知识库问答
- 自托管部署：提供 Docker 一键部署，开箱即用，数据完全自主控制
- 开放 API 接口：遵循 OpenAPI 规范，支持二次开发和第三方集成
- 现代前端架构：基于 Web 技术栈，提供流畅的实时对话和流式输出体验

**适用场景**:
- 个人开发者/AI 爱好者：自托管个人 AI 助手，无需依赖第三方服务，保护隐私
- 企业内部使用：构建私有化 LLM 知识库和内部问答系统，支持团队协作
- 技术研究者：快速搭建 LLM 实验环境，支持多模型对比和插件开发



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,736 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 3,183 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，它将 RAG 与 Agent 能力深度融合，支持 DeepSeek、OpenAI、Ollama 等多种 LLM，提供文档智能解析和多跳推理能力，是构建企业级知识库问答系统的最佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，支持复杂多跳推理和工具调用
- 多 LLM 支持：深度集成 DeepSeek-R1、OpenAI、Ollama 等主流大模型，提供灵活的模型切换能力
- 文档智能解析：内置强大的文档理解引擎，支持多种格式文档的结构化提取和语义解析
- GraphRAG 支持：融合知识图谱技术，实现关系感知的上下文检索，提升复杂查询准确性
- MCP 协议扩展：支持 Model Context Protocol，便于与外部工具和服务集成

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库智能问答，支持复杂文档理解和多轮对话
- 复杂文档理解与分析：处理技术文档、合同、报告等长文本，实现精准信息提取
- 深度研究助手：基于 GraphRAG 和 Agent 能力，支持多跳推理的深度研究场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,880 |
| 语言 | TypeScript |
| Forks | 6,747 |
| Issues | 239 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 时代设计的网页数据 API，能够智能抓取整个网站并转换为干净的 Markdown 格式，为 AI Agent 和 LLM 应用提供高质量的结构化网络数据

**技术亮点**:
- AI 优化的数据提取：专为 LLM 应用设计的数据抓取管道，自动将 HTML 转换为干净的 Markdown
- 全站智能爬取：支持整站爬取（Sitemap 模式），智能解析网站结构
- HTML 转 Markdown：保留语义结构的html-to-markdown技术
- 高性能大规模爬取：支持动态页面渲染处理
- 标准化 Web Data API：统一接口设计便于 AI Agent 快速接入

**适用场景**:
- AI Agent 数据供给：为 AI 代理提供实时、准确的网页数据
- LLM 训练数据准备：构建 RAG 系统的知识库
- 企业级数据采集：大规模网页数据采集和分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,889 |
| 语言 | JavaScript |
| Forks | 17,009 |
| Issues | 131 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码 Agent 的性能优化框架，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Instincts、Memory 和安全机制实现开发工作流的深度定制，Stars 高达 125k 证明其在开发者社区的广泛认可。

**技术亮点**:
- 多 Agent 兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供标准化的扩展接口
- Skills 与 Instincts 机制：通过模块化的技能系统和本能响应机制，让 AI Agent 具备可配置的行为模式和专业能力
- Memory 持久化系统：实现 Agent 状态的长期记忆和上下文管理，提升多轮交互的连贯性和智能程度
- Security 安全层：内置安全策略和权限控制机制，确保 AI Agent 在代码修改和系统交互中的安全性
- MCP (Model Context Protocol) 支持：遵循 Anthropic 提出的 MCP 协议标准，实现与外部工具和数据的标准化集成

**适用场景**:
- 个人开发者效率提升：利用项目提供的 Skills 和优化工具扩展 AI 编码助手能力，实现代码生成、审查、重构的自动化
- 团队协作与标准化：企业开发团队可基于该框架构建统一的 AI 开发规范，实现代码质量控制和知识沉淀
- AI Agent 二次开发：开发者可借鉴其架构设计，为特定领域（如安全审计、代码迁移）定制专属的 AI 编程助手



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,631 |
| 语言 | Go |
| Forks | 3,830 |
| Issues | 149 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模态模型，且无需 GPU 即可运行，为开发者和企业提供了隐私友好、低成本的本地 AI 部署方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成、图像生成、音频合成、语音识别、目标检测等多种 AI 任务，通过统一 API 提供一致的使用体验
- Go 语言高性能实现：采用 Go 编写，具备优秀的并发处理能力和跨平台部署能力，支持 RESTful API 和 gRPC 接口
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信，可构建去中心化的 AI 计算网络
- 广泛模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型，支持 GGUF/GGML 格式量化模型
- 边缘计算友好：无需 GPU 即可运行，可在 CPU 和各类边缘设备上部署，降低硬件门槛

**适用场景**:
- 企业隐私 AI 应用：适合金融、医疗、法律等对数据隐私要求严格的行业，在本地运行 AI 服务避免敏感数据上云
- 开发者本地 AI 开发与测试：提供 OpenAI API 兼容接口，开发者可快速将基于 OpenAI 的应用迁移到本地环境进行开发和调试
- 边缘设备 AI 部署：适用于 IoT 设备、嵌入式系统等边缘场景，实现本地化的智能推理能力
- 低成本 AI 服务搭建：无需昂贵 GPU 资源，在普通服务器或工作站上构建私有 AI 服务，大幅降低运营成本
- 去中心化 AI 网络：利用 P2P 分布式架构构建去中心化的 AI 计算网络，实现资源共享和协同推理



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,559 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 594 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 平台之一，支持多 Agent 协作和多模型接入（OpenAI GPT、Claude、DeepSeek、Gemini），让开发者能够轻松构建、管理和编排 AI Agent 团队，极大地降低了构建复杂 AI 应用的门槛。

**技术亮点**:
- 多 Agent 协作架构：支持多 Agent 之间的无缝协作，提供 Agent 团队设计能力，允许定义和管理复杂的 Agent 工作流
- 多模型集成支持：统一接入 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，支持模型间的灵活切换
- MCP (Model Context Protocol) 支持：原生支持 MCP 协议，实现与外部工具和数据源的标准化连接
- 知识库管理：内置 RAG 能力，支持向量检索和知识库构建，让 Agent 拥有持久记忆和专业领域知识
- TypeScript 现代架构：基于 React + TypeScript 构建，提供完整的类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、知识库问答、业务流程自动化等企业应用，支持多 Agent 分工协作处理复杂任务
- AI 原型与研究：快速搭建 AI Agent 实验环境，测试不同模型和提示策略，适合 AI 研究者和产品经理进行快速验证
- 个人 AI 助手搭建：打造个人专属的 AI 工作站，整合日历、文档、邮件等工具，实现工作和生活的高效管理



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,311 |
| 语言 | Python |
| Forks | 8,436 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个被顶会 ACL 2024 收录的统一高效微调框架，支持 100+ 大语言模型和视觉语言模型，提供了从 SFT 到 RLHF 的完整训练流程，是企业和研究者快速定制专属 LLM 的最佳选择。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs，包括 LLaMA、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成 LoRA、QLoRA、PEFT 等高效微调技术，大幅降低显存占用和训练成本
- 提供统一的微调框架，支持 SFT、DPO、ORPO 等多种训练算法
- 内置量化训练支持（AWQ、GPTQ），支持 4-bit/8-bit 量化微调
- 提供 Web UI 和 CLI 界面，支持可视化监控训练过程

**适用场景**:
- 企业定制化场景：金融、医疗、法律等行业利用自有数据微调领域专属模型
- 学术研究与模型实验：快速验证不同微调方法（LoRA vs RLHF）对模型效果的影响
- 个人开发者应用开发：基于开源模型快速构建 AI Agent、聊天机器人或垂直领域助手



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,028 |
| 语言 | TypeScript |
| Forks | 6,917 |
| Issues | 30 |
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
| Stars | 44,008 |
| 语言 | TypeScript |
| Forks | 3,285 |
| Issues | 207 |
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
| Stars | 42,686 |
| 语言 | Python |
| Forks | 9,863 |
| Issues | 351 |
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
| Stars | 45,652 |
| 语言 | Java |
| Forks | 15,861 |
| Issues | 82 |
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
| Stars | 38,889 |
| 语言 | Python |
| Forks | 6,172 |
| Issues | 105 |
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
| Stars | 33,754 |
| 语言 | Python |
| Forks | 2,096 |
| Issues | 89 |
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
| Stars | 33,521 |
| 语言 | TypeScript |
| Forks | 3,632 |
| Issues | 279 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,521 |
| 语言 | Python |
| Forks | 3,680 |
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
| Stars | 104,141 |
| 语言 | Python |
| Forks | 15,189 |
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
| Stars | 57,257 |
| 语言 | JavaScript |
| Forks | 6,194 |
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
| Stars | 70,301 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 346 |
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
| Stars | 45,349 |
| 语言 | TypeScript |
| Forks | 3,376 |
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
| Stars | 85,298 |
| 语言 | Python |
| Forks | 9,886 |
| Issues | 218 |
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
| Stars | 51,300 |
| 语言 | TypeScript |
| Forks | 24,000 |
| Issues | 828 |
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
| Stars | 181,890 |
| 语言 | TypeScript |
| Forks | 56,359 |
| Issues | 1,448 |
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
| Stars | 154,568 |
| 语言 | Java |
| Forks | 46,137 |
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
| Stars | 146,436 |
| 语言 | Python |
| Forks | 8,678 |
| Issues | 944 |
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
| Stars | 72,542 |
| 语言 | MDX |
| Forks | 7,771 |
| Issues | 254 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,028 |
| 语言 | Jupyter Notebook |
| Forks | 5,458 |
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
| Stars | 36,341 |
| 语言 | Rust |
| Forks | 2,168 |
| Issues | 496 |
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
| Stars | 55,560 |
| 语言 | Jupyter Notebook |
| Forks | 19,198 |
| Issues | 16 |
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
| Stars | 129,454 |
| 语言 | Python |
| Forks | 18,326 |
| Issues | 305 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，提供现代化的 Web UI 和 RAG 支持，Stars 超过 12 万，是自托管 LLM 界面的首选项目，让用户无需复杂配置即可拥有类似 ChatGPT 的体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、MCP 等多种 LLM 提供商，支持灵活切换
- RAG 增强能力：内置检索增强生成功能，支持文档上传和知识库问答
- 自托管部署：提供 Docker 一键部署，开箱即用，数据完全自主控制
- 开放 API 接口：遵循 OpenAPI 规范，支持二次开发和第三方集成
- 现代前端架构：基于 Web 技术栈，提供流畅的实时对话和流式输出体验

**适用场景**:
- 个人开发者/AI 爱好者：自托管个人 AI 助手，无需依赖第三方服务，保护隐私
- 企业内部使用：构建私有化 LLM 知识库和内部问答系统，支持团队协作
- 技术研究者：快速搭建 LLM 实验环境，支持多模型对比和插件开发



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,736 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 3,183 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，它将 RAG 与 Agent 能力深度融合，支持 DeepSeek、OpenAI、Ollama 等多种 LLM，提供文档智能解析和多跳推理能力，是构建企业级知识库问答系统的最佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，支持复杂多跳推理和工具调用
- 多 LLM 支持：深度集成 DeepSeek-R1、OpenAI、Ollama 等主流大模型，提供灵活的模型切换能力
- 文档智能解析：内置强大的文档理解引擎，支持多种格式文档的结构化提取和语义解析
- GraphRAG 支持：融合知识图谱技术，实现关系感知的上下文检索，提升复杂查询准确性
- MCP 协议扩展：支持 Model Context Protocol，便于与外部工具和服务集成

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库智能问答，支持复杂文档理解和多轮对话
- 复杂文档理解与分析：处理技术文档、合同、报告等长文本，实现精准信息提取
- 深度研究助手：基于 GraphRAG 和 Agent 能力，支持多跳推理的深度研究场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,559 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 594 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 平台之一，支持多 Agent 协作和多模型接入（OpenAI GPT、Claude、DeepSeek、Gemini），让开发者能够轻松构建、管理和编排 AI Agent 团队，极大地降低了构建复杂 AI 应用的门槛。

**技术亮点**:
- 多 Agent 协作架构：支持多 Agent 之间的无缝协作，提供 Agent 团队设计能力，允许定义和管理复杂的 Agent 工作流
- 多模型集成支持：统一接入 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，支持模型间的灵活切换
- MCP (Model Context Protocol) 支持：原生支持 MCP 协议，实现与外部工具和数据源的标准化连接
- 知识库管理：内置 RAG 能力，支持向量检索和知识库构建，让 Agent 拥有持久记忆和专业领域知识
- TypeScript 现代架构：基于 React + TypeScript 构建，提供完整的类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、知识库问答、业务流程自动化等企业应用，支持多 Agent 分工协作处理复杂任务
- AI 原型与研究：快速搭建 AI Agent 实验环境，测试不同模型和提示策略，适合 AI 研究者和产品经理进行快速验证
- 个人 AI 助手搭建：打造个人专属的 AI 工作站，整合日历、文档、邮件等工具，实现工作和生活的高效管理



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,008 |
| 语言 | TypeScript |
| Forks | 3,285 |
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
| Stars | 45,652 |
| 语言 | Java |
| Forks | 15,861 |
| Issues | 82 |
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
| Stars | 38,889 |
| 语言 | Python |
| Forks | 6,172 |
| Issues | 105 |
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
| Stars | 33,754 |
| 语言 | Python |
| Forks | 2,096 |
| Issues | 89 |
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
| Stars | 33,521 |
| 语言 | TypeScript |
| Forks | 3,632 |
| Issues | 279 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,521 |
| 语言 | Python |
| Forks | 3,680 |
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
| Stars | 104,141 |
| 语言 | Python |
| Forks | 15,189 |
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
| Stars | 99,926 |
| 语言 | TypeScript |
| Forks | 11,941 |
| Issues | 979 |
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
| Stars | 57,257 |
| 语言 | JavaScript |
| Forks | 6,194 |
| Issues | 300 |
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
| Stars | 74,061 |
| 语言 | Python |
| Forks | 10,107 |
| Issues | 260 |
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
| Stars | 51,300 |
| 语言 | TypeScript |
| Forks | 24,000 |
| Issues | 828 |
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
| Stars | 43,541 |
| 语言 | Go |
| Forks | 3,923 |
| Issues | 1,093 |
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
| Stars | 72,542 |
| 语言 | MDX |
| Forks | 7,771 |
| Issues | 254 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,028 |
| 语言 | Jupyter Notebook |
| Forks | 5,458 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (24 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 129,454 |
| 语言 | Python |
| Forks | 18,326 |
| Issues | 305 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持 Ollama、OpenAI API 等多种 LLM 后端，提供现代化的 Web UI 和 RAG 支持，Stars 超过 12 万，是自托管 LLM 界面的首选项目，让用户无需复杂配置即可拥有类似 ChatGPT 的体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、MCP 等多种 LLM 提供商，支持灵活切换
- RAG 增强能力：内置检索增强生成功能，支持文档上传和知识库问答
- 自托管部署：提供 Docker 一键部署，开箱即用，数据完全自主控制
- 开放 API 接口：遵循 OpenAPI 规范，支持二次开发和第三方集成
- 现代前端架构：基于 Web 技术栈，提供流畅的实时对话和流式输出体验

**适用场景**:
- 个人开发者/AI 爱好者：自托管个人 AI 助手，无需依赖第三方服务，保护隐私
- 企业内部使用：构建私有化 LLM 知识库和内部问答系统，支持团队协作
- 技术研究者：快速搭建 LLM 实验环境，支持多模型对比和插件开发



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,736 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 3,183 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，它将 RAG 与 Agent 能力深度融合，支持 DeepSeek、OpenAI、Ollama 等多种 LLM，提供文档智能解析和多跳推理能力，是构建企业级知识库问答系统的最佳选择。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，支持复杂多跳推理和工具调用
- 多 LLM 支持：深度集成 DeepSeek-R1、OpenAI、Ollama 等主流大模型，提供灵活的模型切换能力
- 文档智能解析：内置强大的文档理解引擎，支持多种格式文档的结构化提取和语义解析
- GraphRAG 支持：融合知识图谱技术，实现关系感知的上下文检索，提升复杂查询准确性
- MCP 协议扩展：支持 Model Context Protocol，便于与外部工具和服务集成

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库智能问答，支持复杂文档理解和多轮对话
- 复杂文档理解与分析：处理技术文档、合同、报告等长文本，实现精准信息提取
- 深度研究助手：基于 GraphRAG 和 Agent 能力，支持多跳推理的深度研究场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,889 |
| 语言 | JavaScript |
| Forks | 17,009 |
| Issues | 131 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码 Agent 的性能优化框架，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Instincts、Memory 和安全机制实现开发工作流的深度定制，Stars 高达 125k 证明其在开发者社区的广泛认可。

**技术亮点**:
- 多 Agent 兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供标准化的扩展接口
- Skills 与 Instincts 机制：通过模块化的技能系统和本能响应机制，让 AI Agent 具备可配置的行为模式和专业能力
- Memory 持久化系统：实现 Agent 状态的长期记忆和上下文管理，提升多轮交互的连贯性和智能程度
- Security 安全层：内置安全策略和权限控制机制，确保 AI Agent 在代码修改和系统交互中的安全性
- MCP (Model Context Protocol) 支持：遵循 Anthropic 提出的 MCP 协议标准，实现与外部工具和数据的标准化集成

**适用场景**:
- 个人开发者效率提升：利用项目提供的 Skills 和优化工具扩展 AI 编码助手能力，实现代码生成、审查、重构的自动化
- 团队协作与标准化：企业开发团队可基于该框架构建统一的 AI 开发规范，实现代码质量控制和知识沉淀
- AI Agent 二次开发：开发者可借鉴其架构设计，为特定领域（如安全审计、代码迁移）定制专属的 AI 编程助手



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,559 |
| 语言 | TypeScript |
| Forks | 14,835 |
| Issues | 594 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 平台之一，支持多 Agent 协作和多模型接入（OpenAI GPT、Claude、DeepSeek、Gemini），让开发者能够轻松构建、管理和编排 AI Agent 团队，极大地降低了构建复杂 AI 应用的门槛。

**技术亮点**:
- 多 Agent 协作架构：支持多 Agent 之间的无缝协作，提供 Agent 团队设计能力，允许定义和管理复杂的 Agent 工作流
- 多模型集成支持：统一接入 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，支持模型间的灵活切换
- MCP (Model Context Protocol) 支持：原生支持 MCP 协议，实现与外部工具和数据源的标准化连接
- 知识库管理：内置 RAG 能力，支持向量检索和知识库构建，让 Agent 拥有持久记忆和专业领域知识
- TypeScript 现代架构：基于 React + TypeScript 构建，提供完整的类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、知识库问答、业务流程自动化等企业应用，支持多 Agent 分工协作处理复杂任务
- AI 原型与研究：快速搭建 AI Agent 实验环境，测试不同模型和提示策略，适合 AI 研究者和产品经理进行快速验证
- 个人 AI 助手搭建：打造个人专属的 AI 工作站，整合日历、文档、邮件等工具，实现工作和生活的高效管理



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,257 |
| 语言 | HTML |
| Forks | 20,390 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、开源且社区驱动的 AI 提示词库，拥有超过 15 万 Stars，汇集了数千个经过验证的优质提示词，支持自托管部署，是个人和企业提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持自托管部署，配备完整的 Docker 和 Vercel 部署方案
- 采用响应式 HTML 设计，跨设备体验一致
- 开放的贡献机制，社区可持续丰富提示词库
- 支持多种主流 LLM（ChatGPT、Claude、Gemini、GPT-4）提示词格式

**适用场景**:
- 个人用户发现和收藏高质量 AI 提示词，提升日常 AI 交互效率
- 企业自托管部署，在享受开源免费的同时保证数据隐私和合规性
- 开发者学习 prompt engineering 最佳实践，或基于此项目构建自己的提示词平台
- AI 研究者和爱好者交流分享创新的提示词工程技巧



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,634 |
| 语言 | Jupyter Notebook |
| Forks | 13,691 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个近乎9万星的教育级项目，从零手写实现ChatGPT级别的LLM，没有任何高层封装的"魔法代码"，真正做到了对底层原理的完全透明，非常适合想深入理解大语言模型内部机制的学习者。

**技术亮点**:
- 纯PyTorch从零实现，不依赖Hugging Face等高层框架，每一行代码都可追溯
- Jupyter Notebook形式呈现，代码与讲解深度融合，边学边调试
- 涵盖完整的LLM训练流程：数据预处理、Tokenization、模型架构、训练循环、推理
- 循序渐进的设计：从简单MLP到Transformer再到GPT，步步为营
- 包含实用的训练技巧：学习率调度、梯度裁剪、模型评估等最佳实践

**适用场景**:
- LLM/深度学习学习者：通过完整源码理解大模型的工作原理，而非仅会调用API
- 教育机构：作为AI/ML课程的实践教材，从理论到代码的桥梁
- 研究人员：快速验证新想法或理解最新LLM论文的实现细节



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,028 |
| 语言 | TypeScript |
| Forks | 6,917 |
| Issues | 30 |
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
| Stars | 44,008 |
| 语言 | TypeScript |
| Forks | 3,285 |
| Issues | 207 |
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
| Stars | 42,686 |
| 语言 | Python |
| Forks | 9,863 |
| Issues | 351 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,754 |
| 语言 | Python |
| Forks | 2,096 |
| Issues | 89 |
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
| Stars | 57,257 |
| 语言 | JavaScript |
| Forks | 6,194 |
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
| Stars | 70,301 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 346 |
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
| Stars | 45,349 |
| 语言 | TypeScript |
| Forks | 3,376 |
| Issues | 374 |
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
| Stars | 51,300 |
| 语言 | TypeScript |
| Forks | 24,000 |
| Issues | 828 |
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
| Stars | 35,307 |
| 语言 | HTML |
| Forks | 5,687 |
| Issues | 18 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,839 |
| 语言 | Python |
| Forks | 15,001 |
| Issues | 3,996 |
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
| Stars | 55,804 |
| 语言 | Python |
| Forks | 5,430 |
| Issues | 71 |
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
| Stars | 39,208 |
| 语言 | TypeScript |
| Forks | 3,990 |
| Issues | 1,088 |
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
| Stars | 146,436 |
| 语言 | Python |
| Forks | 8,678 |
| Issues | 944 |
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
| Stars | 166,603 |
| 语言 | Go |
| Forks | 15,256 |
| Issues | 2,780 |
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
| Stars | 72,542 |
| 语言 | MDX |
| Forks | 7,771 |
| Issues | 254 |
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
| Stars | 47,457 |
| 语言 | Rust |
| Forks | 9,403 |
| Issues | 1 |
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
| Stars | 92,976 |
| 语言 | Python |
| Forks | 5,601 |
| Issues | 496 |
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
| Stars | 37,013 |
| 语言 | Python |
| Forks | 2,587 |
| Issues | 65 |
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
| Stars | 69,311 |
| 语言 | Python |
| Forks | 8,436 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个被顶会 ACL 2024 收录的统一高效微调框架，支持 100+ 大语言模型和视觉语言模型，提供了从 SFT 到 RLHF 的完整训练流程，是企业和研究者快速定制专属 LLM 的最佳选择。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs，包括 LLaMA、Qwen、DeepSeek、Gemma 等主流开源模型
- 集成 LoRA、QLoRA、PEFT 等高效微调技术，大幅降低显存占用和训练成本
- 提供统一的微调框架，支持 SFT、DPO、ORPO 等多种训练算法
- 内置量化训练支持（AWQ、GPTQ），支持 4-bit/8-bit 量化微调
- 提供 Web UI 和 CLI 界面，支持可视化监控训练过程

**适用场景**:
- 企业定制化场景：金融、医疗、法律等行业利用自有数据微调领域专属模型
- 学术研究与模型实验：快速验证不同微调方法（LoRA vs RLHF）对模型效果的影响
- 个人开发者应用开发：基于开源模型快速构建 AI Agent、聊天机器人或垂直领域助手



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,808 |
| 语言 | Python |
| Forks | 6,366 |
| Issues | 79 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过6.4万Stars的活跃社区支持，为分析师、量化交易员和AI代理提供了一站式的数据获取与分析解决方案，特别适合需要整合多源金融数据进行投资研究和自动化交易的用户。

**技术亮点**:
- 基于Python生态，支持pandas、numpy等主流数据科学库，便于与现有量化交易系统集成
- 覆盖股票、加密货币、期权、衍生品、固定收益等多品类金融数据源
- 内置机器学习支持，可用于因子挖掘、预测模型和风险建模等AI驱动分析
- 提供CLI、SDK和API多种接入方式，支持快速原型开发和生产环境部署
- 支持AI代理集成，可构建自动化投资研究助手和智能交易机器人

**适用场景**:
- 量化交易研究：用于获取历史行情、财务数据、技术指标，进行策略回测和因子分析
- 投资组合分析与风险管理：整合多资产类别数据进行组合优化、风险评估和绩效归因
- AI金融应用开发：结合LLM构建智能投研助手，实现自然语言查询金融数据和自动化报告生成
- 金融数据管道构建：作为数据中台，为企业内部系统提供标准化的金融市场数据API



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,257 |
| 语言 | HTML |
| Forks | 20,390 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、开源且社区驱动的 AI 提示词库，拥有超过 15 万 Stars，汇集了数千个经过验证的优质提示词，支持自托管部署，是个人和企业提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持自托管部署，配备完整的 Docker 和 Vercel 部署方案
- 采用响应式 HTML 设计，跨设备体验一致
- 开放的贡献机制，社区可持续丰富提示词库
- 支持多种主流 LLM（ChatGPT、Claude、Gemini、GPT-4）提示词格式

**适用场景**:
- 个人用户发现和收藏高质量 AI 提示词，提升日常 AI 交互效率
- 企业自托管部署，在享受开源免费的同时保证数据隐私和合规性
- 开发者学习 prompt engineering 最佳实践，或基于此项目构建自己的提示词平台
- AI 研究者和爱好者交流分享创新的提示词工程技巧



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,634 |
| 语言 | Jupyter Notebook |
| Forks | 13,691 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个近乎9万星的教育级项目，从零手写实现ChatGPT级别的LLM，没有任何高层封装的"魔法代码"，真正做到了对底层原理的完全透明，非常适合想深入理解大语言模型内部机制的学习者。

**技术亮点**:
- 纯PyTorch从零实现，不依赖Hugging Face等高层框架，每一行代码都可追溯
- Jupyter Notebook形式呈现，代码与讲解深度融合，边学边调试
- 涵盖完整的LLM训练流程：数据预处理、Tokenization、模型架构、训练循环、推理
- 循序渐进的设计：从简单MLP到Transformer再到GPT，步步为营
- 包含实用的训练技巧：学习率调度、梯度裁剪、模型评估等最佳实践

**适用场景**:
- LLM/深度学习学习者：通过完整源码理解大模型的工作原理，而非仅会调用API
- 教育机构：作为AI/ML课程的实践教材，从理论到代码的桥梁
- 研究人员：快速验证新想法或理解最新LLM论文的实现细节



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,521 |
| 语言 | TypeScript |
| Forks | 3,632 |
| Issues | 279 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,603 |
| 语言 | Python |
| Forks | 32,698 |
| Issues | 2,323 |
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
| Stars | 74,839 |
| 语言 | Python |
| Forks | 15,001 |
| Issues | 3,996 |
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
| Stars | 107,419 |
| 语言 | Python |
| Forks | 12,399 |
| Issues | 3,914 |
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
| Stars | 98,694 |
| 语言 | Python |
| Forks | 27,367 |
| Issues | 18,175 |
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
| Stars | 72,542 |
| 语言 | MDX |
| Forks | 7,771 |
| Issues | 254 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,028 |
| 语言 | Jupyter Notebook |
| Forks | 5,458 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 162,060 |
| 语言 | Python |
| Forks | 30,210 |
| Issues | 2,473 |
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
| Stars | 125,889 |
| 语言 | JavaScript |
| Forks | 17,009 |
| Issues | 131 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编码 Agent 的性能优化框架，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Instincts、Memory 和安全机制实现开发工作流的深度定制，Stars 高达 125k 证明其在开发者社区的广泛认可。

**技术亮点**:
- 多 Agent 兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供标准化的扩展接口
- Skills 与 Instincts 机制：通过模块化的技能系统和本能响应机制，让 AI Agent 具备可配置的行为模式和专业能力
- Memory 持久化系统：实现 Agent 状态的长期记忆和上下文管理，提升多轮交互的连贯性和智能程度
- Security 安全层：内置安全策略和权限控制机制，确保 AI Agent 在代码修改和系统交互中的安全性
- MCP (Model Context Protocol) 支持：遵循 Anthropic 提出的 MCP 协议标准，实现与外部工具和数据的标准化集成

**适用场景**:
- 个人开发者效率提升：利用项目提供的 Skills 和优化工具扩展 AI 编码助手能力，实现代码生成、审查、重构的自动化
- 团队协作与标准化：企业开发团队可基于该框架构建统一的 AI 开发规范，实现代码质量控制和知识沉淀
- AI Agent 二次开发：开发者可借鉴其架构设计，为特定领域（如安全审计、代码迁移）定制专属的 AI 编程助手



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,631 |
| 语言 | Go |
| Forks | 3,830 |
| Issues | 149 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模态模型，且无需 GPU 即可运行，为开发者和企业提供了隐私友好、低成本的本地 AI 部署方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成、图像生成、音频合成、语音识别、目标检测等多种 AI 任务，通过统一 API 提供一致的使用体验
- Go 语言高性能实现：采用 Go 编写，具备优秀的并发处理能力和跨平台部署能力，支持 RESTful API 和 gRPC 接口
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信，可构建去中心化的 AI 计算网络
- 广泛模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型，支持 GGUF/GGML 格式量化模型
- 边缘计算友好：无需 GPU 即可运行，可在 CPU 和各类边缘设备上部署，降低硬件门槛

**适用场景**:
- 企业隐私 AI 应用：适合金融、医疗、法律等对数据隐私要求严格的行业，在本地运行 AI 服务避免敏感数据上云
- 开发者本地 AI 开发与测试：提供 OpenAI API 兼容接口，开发者可快速将基于 OpenAI 的应用迁移到本地环境进行开发和调试
- 边缘设备 AI 部署：适用于 IoT 设备、嵌入式系统等边缘场景，实现本地化的智能推理能力
- 低成本 AI 服务搭建：无需昂贵 GPU 资源，在普通服务器或工作站上构建私有 AI 服务，大幅降低运营成本
- 去中心化 AI 网络：利用 P2P 分布式架构构建去中心化的 AI 计算网络，实现资源共享和协同推理



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,301 |
| 语言 | Python |
| Forks | 8,797 |
| Issues | 346 |
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
| Stars | 45,349 |
| 语言 | TypeScript |
| Forks | 3,376 |
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
| Stars | 181,890 |
| 语言 | TypeScript |
| Forks | 56,359 |
| Issues | 1,448 |
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
| Stars | 154,149 |
| 语言 | Python |
| Forks | 12,529 |
| Issues | 2,431 |
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
| Stars | 96,723 |
| 语言 | Python |
| Forks | 8,978 |
| Issues | 169 |
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
| Stars | 75,378 |
| 语言 | Python |
| Forks | 8,875 |
| Issues | 216 |
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
| Stars | 183,248 |
| 语言 | TypeScript |
| Forks | 38,862 |
| Issues | 15,831 |
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
| Stars | 93,986 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Stars | 78,724 |
| 语言 | TypeScript |
| Forks | 5,748 |
| Issues | 722 |
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
| Stars | 76,911 |
| 语言 | TypeScript |
| Forks | 6,575 |
| Issues | 171 |
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
| Stars | 79,141 |
| 语言 | Go |
| Forks | 2,746 |
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
| Stars | 75,344 |
| 语言 | Go |
| Forks | 2,659 |
| Issues | 934 |
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
| Stars | 37,013 |
| 语言 | Python |
| Forks | 2,587 |
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
| Stars | 54,806 |
| 语言 | JavaScript |
| Forks | 4,070 |
| Issues | 1,417 |
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
| Stars | 417,820 |
| 语言 | Python |
| Forks | 45,371 |
| Issues | 1,167 |
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
| Stars | 75,667 |
| 语言 | JavaScript |
| Forks | 7,277 |
| Issues | 711 |
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
| Stars | 45,349 |
| 语言 | TypeScript |
| Forks | 3,376 |
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
| Stars | 181,890 |
| 语言 | TypeScript |
| Forks | 56,359 |
| Issues | 1,448 |
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
| Stars | 51,674 |
| 语言 | Go |
| Forks | 10,338 |
| Issues | 211 |
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
| Stars | 121,419 |
| 语言 | Go |
| Forks | 42,759 |
| Issues | 2,672 |
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
| Stars | 71,553 |
| 语言 | Go |
| Forks | 18,912 |
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
| Stars | 54,634 |
| 语言 | Go |
| Forks | 6,517 |
| Issues | 2,862 |
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
| Stars | 47,580 |
| 语言 | Go |
| Forks | 5,064 |
| Issues | 972 |
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
| Stars | 93,986 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Stars | 76,002 |
| 语言 | TypeScript |
| Forks | 6,481 |
| Issues | 451 |
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
| Stars | 84,687 |
| 语言 | JavaScript |
| Forks | 7,587 |
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
| Stars | 69,651 |
| 语言 | Go |
| Forks | 1,896 |
| Issues | 312 |
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
| Stars | 62,417 |
| 语言 | Go |
| Forks | 5,896 |
| Issues | 772 |
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
| Stars | 58,423 |
| 语言 | Go |
| Forks | 4,238 |
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
| Stars | 84,687 |
| 语言 | JavaScript |
| Forks | 7,587 |
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
| Stars | 63,329 |
| 语言 | Go |
| Forks | 10,291 |
| Issues | 760 |
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
| Stars | 44,631 |
| 语言 | Go |
| Forks | 3,830 |
| Issues | 149 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模态模型，且无需 GPU 即可运行，为开发者和企业提供了隐私友好、低成本的本地 AI 部署方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成、图像生成、音频合成、语音识别、目标检测等多种 AI 任务，通过统一 API 提供一致的使用体验
- Go 语言高性能实现：采用 Go 编写，具备优秀的并发处理能力和跨平台部署能力，支持 RESTful API 和 gRPC 接口
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信，可构建去中心化的 AI 计算网络
- 广泛模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型，支持 GGUF/GGML 格式量化模型
- 边缘计算友好：无需 GPU 即可运行，可在 CPU 和各类边缘设备上部署，降低硬件门槛

**适用场景**:
- 企业隐私 AI 应用：适合金融、医疗、法律等对数据隐私要求严格的行业，在本地运行 AI 服务避免敏感数据上云
- 开发者本地 AI 开发与测试：提供 OpenAI API 兼容接口，开发者可快速将基于 OpenAI 的应用迁移到本地环境进行开发和调试
- 边缘设备 AI 部署：适用于 IoT 设备、嵌入式系统等边缘场景，实现本地化的智能推理能力
- 低成本 AI 服务搭建：无需昂贵 GPU 资源，在普通服务器或工作站上构建私有 AI 服务，大幅降低运营成本
- 去中心化 AI 网络：利用 P2P 分布式架构构建去中心化的 AI 计算网络，实现资源共享和协同推理



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,723 |
| 语言 | Python |
| Forks | 8,978 |
| Issues | 169 |
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
| Stars | 87,135 |
| 语言 | Python |
| Forks | 33,816 |
| Issues | 425 |
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
| Stars | 100,104 |
| 语言 | TypeScript |
| Forks | 27,149 |
| Issues | 1,124 |
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
| Stars | 78,724 |
| 语言 | TypeScript |
| Forks | 5,748 |
| Issues | 722 |
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
| Stars | 68,886 |
| 语言 | JavaScript |
| Forks | 22,985 |
| Issues | 202 |
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
| Issues | 366 |
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
| Stars | 51,742 |
| 语言 | JavaScript |
| Forks | 4,695 |
| Issues | 1,469 |
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
| Stars | 47,721 |
| 语言 | JavaScript |
| Forks | 1,580 |
| Issues | 658 |
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
| Stars | 88,310 |
| 语言 | Go |
| Forks | 8,574 |
| Issues | 663 |
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
| Stars | 71,198 |
| 语言 | Go |
| Forks | 4,692 |
| Issues | 244 |
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
| Stars | 57,265 |
| 语言 | Go |
| Forks | 3,236 |
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
| Stars | 37,013 |
| 语言 | Python |
| Forks | 2,587 |
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
| Stars | 417,820 |
| 语言 | Python |
| Forks | 45,371 |
| Issues | 1,167 |
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
| Stars | 75,667 |
| 语言 | JavaScript |
| Forks | 7,277 |
| Issues | 711 |
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
| Stars | 99,926 |
| 语言 | TypeScript |
| Forks | 11,941 |
| Issues | 979 |
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
| Stars | 57,257 |
| 语言 | JavaScript |
| Forks | 6,194 |
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
| Stars | 43,541 |
| 语言 | Go |
| Forks | 3,923 |
| Issues | 1,093 |
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
| Stars | 51,674 |
| 语言 | Go |
| Forks | 10,338 |
| Issues | 211 |
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
| Stars | 155,257 |
| 语言 | HTML |
| Forks | 20,390 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是目前最全面、开源且社区驱动的 AI 提示词库，拥有超过 15 万 Stars，汇集了数千个经过验证的优质提示词，支持自托管部署，是个人和企业提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持自托管部署，配备完整的 Docker 和 Vercel 部署方案
- 采用响应式 HTML 设计，跨设备体验一致
- 开放的贡献机制，社区可持续丰富提示词库
- 支持多种主流 LLM（ChatGPT、Claude、Gemini、GPT-4）提示词格式

**适用场景**:
- 个人用户发现和收藏高质量 AI 提示词，提升日常 AI 交互效率
- 企业自托管部署，在享受开源免费的同时保证数据隐私和合规性
- 开发者学习 prompt engineering 最佳实践，或基于此项目构建自己的提示词平台
- AI 研究者和爱好者交流分享创新的提示词工程技巧



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,028 |
| 语言 | TypeScript |
| Forks | 6,917 |
| Issues | 30 |
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
| Stars | 32,521 |
| 语言 | Python |
| Forks | 3,680 |
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
| Stars | 35,307 |
| 语言 | HTML |
| Forks | 5,687 |
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
| Stars | 72,542 |
| 语言 | MDX |
| Forks | 7,771 |
| Issues | 254 |
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
| Stars | 89,588 |
| 语言 | TypeScript |
| Forks | 9,969 |
| Issues | 2,218 |
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
| Stars | 87,015 |
| 语言 | TypeScript |
| Forks | 8,806 |
| Issues | 1,640 |
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
| Stars | 127,291 |
| 语言 | JavaScript |
| Forks | 12,465 |
| Issues | 4 |
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
| Stars | 168,741 |
| 语言 | Go |
| Forks | 13,096 |
| Issues | 171 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (65 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,869 |
| 语言 | Unknown |
| Forks | 33,728 |
| Issues | 142 |
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
| Stars | 67,360 |
| 语言 | Shell |
| Forks | 10,179 |
| Issues | 92 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,006 |
| 语言 | Python |
| Forks | 6,430 |
| Issues | 48 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,957 |
| 语言 | Python |
| Forks | 12,614 |
| Issues | 110 |
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
| Stars | 84,100 |
| 语言 | Python |
| Forks | 7,188 |
| Issues | 647 |
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
| Stars | 384,758 |
| 语言 | Python |
| Forks | 66,072 |
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
| Stars | 114,080 |
| 语言 | TypeScript |
| Forks | 5,844 |
| Issues | 333 |
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
| Stars | 106,668 |
| 语言 | TypeScript |
| Forks | 7,740 |
| Issues | 216 |
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
| Stars | 48,011 |
| 语言 | Go |
| Forks | 10,256 |
| Issues | 1,889 |
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
| Stars | 100,404 |
| 语言 | C++ |
| Forks | 16,089 |
| Issues | 1,322 |
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
| Stars | 63,185 |
| 语言 | Python |
| Forks | 1,629 |
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
| Stars | 59,338 |
| 语言 | TypeScript |
| Forks | 7,770 |
| Issues | 313 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,936 |
| 语言 | JavaScript |
| Forks | 3,707 |
| Issues | 119 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 289,929 |
| 语言 | Python |
| Forks | 27,531 |
| Issues | 16 |
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
| Stars | 219,171 |
| 语言 | Python |
| Forks | 50,288 |
| Issues | 910 |
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
| Stars | 96,956 |
| 语言 | Python |
| Forks | 11,952 |
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
| Stars | 85,906 |
| 语言 | Python |
| Forks | 37,117 |
| Issues | 3,501 |
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
| Stars | 85,667 |
| 语言 | Python |
| Forks | 7,195 |
| Issues | 479 |
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
| Stars | 77,682 |
| 语言 | Python |
| Forks | 45,188 |
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
| Stars | 440,220 |
| 语言 | TypeScript |
| Forks | 43,930 |
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
| Stars | 351,935 |
| 语言 | TypeScript |
| Forks | 43,863 |
| Issues | 2 |
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
| Stars | 119,942 |
| 语言 | TypeScript |
| Forks | 13,066 |
| Issues | 2,916 |
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
| Stars | 111,143 |
| 语言 | TypeScript |
| Forks | 8,374 |
| Issues | 1,792 |
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
| Stars | 108,364 |
| 语言 | TypeScript |
| Forks | 13,314 |
| Issues | 5,003 |
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
| Stars | 97,757 |
| 语言 | TypeScript |
| Forks | 54,573 |
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
| Stars | 96,056 |
| 语言 | TypeScript |
| Forks | 5,224 |
| Issues | 677 |
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
| Stars | 94,235 |
| 语言 | TypeScript |
| Forks | 5,148 |
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
| Stars | 83,043 |
| 语言 | TypeScript |
| Forks | 7,576 |
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
| Stars | 82,632 |
| 语言 | TypeScript |
| Forks | 10,140 |
| Issues | 627 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,477 |
| 语言 | TypeScript |
| Forks | 7,970 |
| Issues | 696 |
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
| Stars | 244,291 |
| 语言 | JavaScript |
| Forks | 50,872 |
| Issues | 1,189 |
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
| Stars | 116,486 |
| 语言 | JavaScript |
| Forks | 35,233 |
| Issues | 2,579 |
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
| Stars | 111,684 |
| 语言 | JavaScript |
| Forks | 36,319 |
| Issues | 568 |
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
| Stars | 108,707 |
| 语言 | JavaScript |
| Forks | 11,570 |
| Issues | 364 |
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
| Stars | 98,015 |
| 语言 | JavaScript |
| Forks | 32,694 |
| Issues | 1,668 |
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
| Stars | 95,491 |
| 语言 | JavaScript |
| Forks | 15,319 |
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
| Stars | 86,139 |
| 语言 | JavaScript |
| Forks | 4,840 |
| Issues | 972 |
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
| Stars | 78,938 |
| 语言 | JavaScript |
| Forks | 31,925 |
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
| Stars | 70,896 |
| 语言 | JavaScript |
| Forks | 16,811 |
| Issues | 891 |
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
| Stars | 66,300 |
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
| Stars | 65,959 |
| 语言 | JavaScript |
| Forks | 9,380 |
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
| Stars | 62,429 |
| 语言 | JavaScript |
| Forks | 3,991 |
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
| Stars | 61,528 |
| 语言 | JavaScript |
| Forks | 7,124 |
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
| Stars | 60,134 |
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
| Stars | 59,861 |
| 语言 | JavaScript |
| Forks | 20,464 |
| Issues | 93 |
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
| Stars | 57,419 |
| 语言 | JavaScript |
| Forks | 12,299 |
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
| Stars | 53,059 |
| 语言 | JavaScript |
| Forks | 10,602 |
| Issues | 466 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,281 |
| 语言 | JavaScript |
| Forks | 11,410 |
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
| Stars | 133,214 |
| 语言 | Go |
| Forks | 18,889 |
| Issues | 9,919 |
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
| Stars | 105,692 |
| 语言 | Go |
| Forks | 14,972 |
| Issues | 45 |
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
| Stars | 87,358 |
| 语言 | Go |
| Forks | 8,231 |
| Issues | 272 |
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
| Stars | 81,292 |
| 语言 | Go |
| Forks | 4,979 |
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
| Stars | 68,658 |
| 语言 | Go |
| Forks | 3,230 |
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
| Stars | 56,397 |
| 语言 | Go |
| Forks | 5,001 |
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
| Stars | 50,964 |
| 语言 | Go |
| Forks | 21,887 |
| Issues | 383 |
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
| Stars | 49,242 |
| 语言 | Go |
| Forks | 7,963 |
| Issues | 560 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### instructkr/claw-code

**描述**: Better Harness Tools, not merely storing the archive of leaked Claude Code but also make real things done. Now rewriting in Rust.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,319 |
| 语言 | Rust |
| Forks | 56,271 |
| Issues | 2,104 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,203 |
| 语言 | Python |
| Forks | 11,276 |
| Issues | 318 |
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
| Stars | 340,822 |
| 语言 | Python |
| Forks | 55,129 |
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
| Stars | 76,511 |
| 语言 | Python |
| Forks | 16,807 |
| Issues | 21 |
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
| Stars | 138,463 |
| 语言 | TypeScript |
| Forks | 16,488 |
| Issues | 45 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 48,622 |
| 语言 | JavaScript |
| Forks | 2,427 |
| Issues | 1,202 |
| Topics | date, date-formatting, datetime, dayjs, moment, time |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,465 |
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
| Stars | 46,958 |
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
| Stars | 45,732 |
| 语言 | Go |
| Forks | 3,776 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
