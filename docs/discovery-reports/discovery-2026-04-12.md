# 项目发现报告 (2026-04-12)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
| 去重移除 | 30 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 62 |

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
| Stars | 131,448 |
| 语言 | Python |
| Forks | 18,654 |
| Issues | 335 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 LLM 界面平台，支持 Ollama 和 OpenAI API 等多种后端，拥有超过 13 万 Stars，其最大的独特价值在于提供开箱即用的自托管解决方案，让用户完全掌控自己的 AI 数据和隐私，特别适合需要在本地部署企业级 AI 助手的场景。

**技术亮点**:
- 支持多种 LLM 后端集成：原生支持 Ollama 和 OpenAI API，同时兼容 OpenAPI 规范，便于扩展更多模型服务
- 内置 RAG（检索增强生成）系统，支持文档上传和向量检索，提升问答准确率
- 支持 MCP（Model Context Protocol）协议，可连接外部工具和数据源扩展能力
- 基于 Python 构建，提供完整的 Web UI 界面，开源可自部署，数据完全本地存储
- 功能丰富：支持对话管理、模型切换、多用户系统、图片上传等企业级特性

**适用场景**:
- 企业私有 AI 助手部署：需要保障数据隐私、不希望将敏感信息发送给第三方 API 的企业场景
- 个人开发者/研究者本地实验：需要便捷地测试和比较不同 LLM 模型效果，同时希望完全控制数据
- 构建内部知识库问答系统：利用 RAG 功能上传文档构建私有知识库，实现精准的知识检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,847 |
| 语言 | Python |
| Forks | 8,762 |
| Issues | 3,235 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，它将 RAG 与 Agent 能力深度融合，支持文档智能理解、多模态检索和 Deep Research，已在生产环境中验证，适合构建企业级知识问答系统和深度研究应用。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力增强检索-生成链路，支持复杂推理和工具调用
- 深度文档理解：内置 OCR、表格识别、版面分析等能力，支持 PDF、Word、Excel 等多格式文档处理
- GraphRAG 支持：基于知识图谱的检索增强，提升复杂关联查询效果
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型接入
- MCP 协议集成：支持 Model Context Protocol，便于扩展工具和外部系统集成

**适用场景**:
- 企业知识库问答：构建内部文档、FAQ、技术手册的智能问答系统
- 智能文档分析：自动解析合同、报告、技术文档，提取关键信息并回答相关问题
- Deep Research 助手：支持深度研究场景，通过 Agent 编排实现复杂问题的多步骤推理和跨文档综合分析



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,046 |
| 语言 | TypeScript |
| Forks | 6,966 |
| Issues | 268 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据抓取工具，能够将网页内容转换为 LLM 友好的 Markdown 格式，支持复杂网站的智能抓取，是构建 AI agents 和 RAG 系统的首选数据管道。

**技术亮点**:
- TypeScript 原生实现，提供完整的类型安全和 IDE 支持
- HTML-to-Markdown 转换引擎，专为 LLM 处理优化，输出结构化清洗的数据
- 支持复杂 JavaScript 渲染页面的抓取，绕过反爬机制
- 提供 RESTful API 接口，易于集成到现有 AI 应用架构
- 支持批量抓取网站地图（Sitemap）和多页面深度抓取

**适用场景**:
- 为 LLM/RAG 应用提供高质量的网页数据源，抓取文档、研究报告等转换为 Markdown 格式
- AI Agents 的数据获取层，为智能代理提供实时网页信息查询能力
- 构建 AI 搜索和问答系统，快速从目标网站提取结构化内容



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,439 |
| 语言 | JavaScript |
| Forks | 23,642 |
| Issues | 78 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 代码助手的综合性能优化框架，通过 Skills、Instincts、Memory 等模块显著提升 Claude Code、Cursor 等工具的响应效率和任务完成质量，是当前 AI 编程辅助领域star数最高的项目之一（152k+），社区活跃度极高。

**技术亮点**:
- 多平台 AI 代理支持：统一兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手框架
- Skills & Instincts 系统：提供可扩展的技能库和本能反应机制，增强 AI 代理的决策能力
- Memory 记忆管理模块：实现上下文持久化和高效检索，减少重复交互开销
- Security 安全模块：内置安全策略和权限控制，保障代码操作安全性
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于扩展和第三方集成

**适用场景**:
- 个人开发者优化 AI 编程效率：通过 Skills 和 Instincts 系统，让 AI 代码助手更准确地理解开发者意图，减少无效交互
- 企业级 AI 开发辅助平台：基于该框架构建统一的 AI 代码审核、自动化测试和代码生成流水线
- 安全敏感型代码开发：利用内置 Security 模块，在金融、医疗等高安全要求场景下规范 AI 代码操作



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,311 |
| 语言 | Go |
| Forks | 3,931 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最全面的开源本地 AI 推理平台，一站式支持 LLM、图像、音频、视频等多种模型，配合去中心化架构设计，特别适合需要数据隐私保护或降低云服务依赖的企业和开发者，无需 GPU 即可运行复杂的 AI 工作负载。

**技术亮点**:
- 多模态统一推理引擎 - 同时支持 LLMs (Llama/Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、TTS、对象检测等十余种模型类型
- 去中心化分布式架构 - 基于 libp2p 构建，支持分布式部署和 P2P 通信，适合边缘计算和去中心化应用场景
- API 优先设计 - 提供 OpenAI 兼容的 REST API，可无缝替代云端 AI 服务，便于现有应用迁移
- 硬件无关运行 - 支持 CPU 推理，无强制 GPU 要求，降低部署门槛，同时兼容 GPU 加速
- MCP (Model Context Protocol) 支持 - 集成最新的模型上下文协议，支持 AI Agents 和工具调用能力

**适用场景**:
- 企业私有化 AI 部署 - 对数据隐私敏感的场景（如医疗、金融、法律），需要完全控制数据和模型
- 本地开发与测试 - 开发者本地构建 AI 原型应用，无需付费订阅云服务，支持快速迭代
- 边缘设备 AI 推理 - 在资源受限的边缘节点部署 AI 能力，支持离线工作和低延迟响应



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,087 |
| 语言 | TypeScript |
| Forks | 14,906 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 平台，拥有超过 75k Stars，集成多模型支持（MCP、OpenAI、Claude、Gemini、DeepSeek）和知识库能力，特别适合需要构建多智能体协作系统的企业和开发者。其"Agents as the unit of work"理念和低门槛的 Agent 团队设计，使复杂 AI 工作流搭建变得简单高效。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，通过统一接口实现模型切换
- MCP (Model Context Protocol) 原生支持：标准化 AI 模型上下文交互协议，便于扩展和集成第三方工具
- 多智能体协作框架：支持构建 Agent Team，实现多 Agent 间的任务分解与协作
- 企业级知识库集成：内置 RAG 能力，支持文档检索和知识管理
- TypeScript 全栈架构：前后端均采用 TypeScript 开发，保证类型安全与代码可维护性

**适用场景**:
- 企业级智能助手团队：为中大型企业构建多业务领域的 AI Agent 团队，实现客户服务、文档处理、数据分析等场景的自动化
- AI 应用快速开发：开发者利用现成的 Agent 框架和 UI 组件，快速搭建聊天机器人、智能客服、知识问答系统
- 团队协作与知识管理：利用知识库功能构建企业文档库，结合多 Agent 实现智能检索和内容生成



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,969 |
| 语言 | Python |
| Forks | 8,545 |
| Issues | 966 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的大模型微调框架之一，通过统一接口支持100+ LLMs和VLMs的高效微调，基于ACL 2024学术认可和7万Stars的社区验证，为研究者和开发者提供了从实验到部署的一站式解决方案，特别适合需要在有限算力下快速定制大模型的企业团队和学术机构。

**技术亮点**:
- 统一微调框架：支持100+预训练模型（LLaMA、LLaMA3、Qwen、DeepSeek、Gemma等）和视觉语言模型，提供标准化API降低学习成本
- 高效微调技术：集成LORA、QLORA、PEFT等轻量化微调方法，支持Int4/Int8量化，显著降低GPU显存占用
- 完整训练流程：覆盖预训练、指令微调、RLHF（基于人类反馈的强化学习）等全链路训练范式
- 多模态能力：同时支持语言模型和多模态视觉语言模型的微调，适应AI多模态发展趋势
- ACL 2024顶会论文验证：学术背书保证了方法的先进性和工程实现的可靠性

**适用场景**:
- 企业AI应用：企业可利用LlamaFactory快速将开源大模型微调至特定领域（如金融、医疗、法律），构建专属AI助手或垂直应用
- 学术研究与实验：研究人员能在统一框架下快速对比不同模型和微调方法的效果，加速NLP/ML领域的研究迭代
- 个人开发者定制：个人开发者借助量化技术，在消费级GPU（如RTX 3090/4090）上即可完成7B-70B模型的微调，实现低成本AI创新



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,517 |
| 语言 | Python |
| Forks | 8,755 |
| Issues | 3,481 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高星 AI Agent 框架，支持多种主流 LLM 提供商（OpenAI、Anthropic、Claude 等），具有成熟的 Agent 架构和工具调用能力，适合构建智能化的 AI 应用。

**技术亮点**:
- 多模型支持：集成 OpenAI GPT、Anthropic Claude 等多种主流大语言模型，提供统一的 Agent 接口
- 成熟的 Agent 框架：实现了规划、推理、工具调用等核心 Agent 能力，支持复杂任务分解
- 工具调用系统：内置 MCP（Model Context Protocol）支持，可扩展的工具生态
- 代码生成能力：通过 Claude Code 集成支持高质量代码生成和自动化编程
- 开源可定制：MIT 许可证，代码透明可审计，便于企业级定制和私有化部署

**适用场景**:
- 企业 AI 助手开发：构建企业内部智能助手，集成到现有工作流程提升效率
- 智能代码助手：基于 Claude Code 能力开发代码审查、自动化生成、调试辅助工具
- AI Agent 应用：开发自动化任务执行、多步骤推理、工具编排等复杂 Agent 应用



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,162 |
| 语言 | TypeScript |
| Forks | 8,524 |
| Issues | 78 |
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
| Stars | 49,341 |
| 语言 | TypeScript |
| Forks | 3,876 |
| Issues | 204 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,008 |
| 语言 | Python |
| Forks | 9,896 |
| Issues | 358 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,197 |
| 语言 | Python |
| Forks | 6,846 |
| Issues | 952 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,820 |
| 语言 | Java |
| Forks | 15,900 |
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
| Stars | 38,962 |
| 语言 | Python |
| Forks | 6,185 |
| Issues | 75 |
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
| Stars | 35,537 |
| 语言 | Python |
| Forks | 4,182 |
| Issues | 93 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,720 |
| 语言 | TypeScript |
| Forks | 3,649 |
| Issues | 292 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,159 |
| 语言 | JavaScript |
| Forks | 6,284 |
| Issues | 320 |
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
| Stars | 71,071 |
| 语言 | Python |
| Forks | 8,926 |
| Issues | 395 |
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
| Stars | 50,883 |
| 语言 | TypeScript |
| Forks | 4,078 |
| Issues | 499 |
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
| Stars | 87,427 |
| 语言 | Python |
| Forks | 10,063 |
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
| Stars | 51,825 |
| 语言 | TypeScript |
| Forks | 24,125 |
| Issues | 806 |
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
| Stars | 183,725 |
| 语言 | TypeScript |
| Forks | 56,724 |
| Issues | 1,469 |
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
| Stars | 154,861 |
| 语言 | Java |
| Forks | 46,150 |
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
| Stars | 146,857 |
| 语言 | Python |
| Forks | 8,756 |
| Issues | 950 |
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
| Stars | 56,518 |
| 语言 | Jupyter Notebook |
| Forks | 19,545 |
| Issues | 3 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,033 |
| 语言 | Python |
| Forks | 2,131 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,459 |
| 语言 | Jupyter Notebook |
| Forks | 5,528 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,230 |
| 语言 | Python |
| Forks | 15,356 |
| Issues | 9 |
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
| Stars | 43,396 |
| 语言 | Rust |
| Forks | 2,732 |
| Issues | 469 |
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
| Stars | 131,448 |
| 语言 | Python |
| Forks | 18,654 |
| Issues | 335 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 LLM 界面平台，支持 Ollama 和 OpenAI API 等多种后端，拥有超过 13 万 Stars，其最大的独特价值在于提供开箱即用的自托管解决方案，让用户完全掌控自己的 AI 数据和隐私，特别适合需要在本地部署企业级 AI 助手的场景。

**技术亮点**:
- 支持多种 LLM 后端集成：原生支持 Ollama 和 OpenAI API，同时兼容 OpenAPI 规范，便于扩展更多模型服务
- 内置 RAG（检索增强生成）系统，支持文档上传和向量检索，提升问答准确率
- 支持 MCP（Model Context Protocol）协议，可连接外部工具和数据源扩展能力
- 基于 Python 构建，提供完整的 Web UI 界面，开源可自部署，数据完全本地存储
- 功能丰富：支持对话管理、模型切换、多用户系统、图片上传等企业级特性

**适用场景**:
- 企业私有 AI 助手部署：需要保障数据隐私、不希望将敏感信息发送给第三方 API 的企业场景
- 个人开发者/研究者本地实验：需要便捷地测试和比较不同 LLM 模型效果，同时希望完全控制数据
- 构建内部知识库问答系统：利用 RAG 功能上传文档构建私有知识库，实现精准的知识检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,847 |
| 语言 | Python |
| Forks | 8,762 |
| Issues | 3,235 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，它将 RAG 与 Agent 能力深度融合，支持文档智能理解、多模态检索和 Deep Research，已在生产环境中验证，适合构建企业级知识问答系统和深度研究应用。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力增强检索-生成链路，支持复杂推理和工具调用
- 深度文档理解：内置 OCR、表格识别、版面分析等能力，支持 PDF、Word、Excel 等多格式文档处理
- GraphRAG 支持：基于知识图谱的检索增强，提升复杂关联查询效果
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型接入
- MCP 协议集成：支持 Model Context Protocol，便于扩展工具和外部系统集成

**适用场景**:
- 企业知识库问答：构建内部文档、FAQ、技术手册的智能问答系统
- 智能文档分析：自动解析合同、报告、技术文档，提取关键信息并回答相关问题
- Deep Research 助手：支持深度研究场景，通过 Agent 编排实现复杂问题的多步骤推理和跨文档综合分析



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,087 |
| 语言 | TypeScript |
| Forks | 14,906 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 平台，拥有超过 75k Stars，集成多模型支持（MCP、OpenAI、Claude、Gemini、DeepSeek）和知识库能力，特别适合需要构建多智能体协作系统的企业和开发者。其"Agents as the unit of work"理念和低门槛的 Agent 团队设计，使复杂 AI 工作流搭建变得简单高效。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，通过统一接口实现模型切换
- MCP (Model Context Protocol) 原生支持：标准化 AI 模型上下文交互协议，便于扩展和集成第三方工具
- 多智能体协作框架：支持构建 Agent Team，实现多 Agent 间的任务分解与协作
- 企业级知识库集成：内置 RAG 能力，支持文档检索和知识管理
- TypeScript 全栈架构：前后端均采用 TypeScript 开发，保证类型安全与代码可维护性

**适用场景**:
- 企业级智能助手团队：为中大型企业构建多业务领域的 AI Agent 团队，实现客户服务、文档处理、数据分析等场景的自动化
- AI 应用快速开发：开发者利用现成的 Agent 框架和 UI 组件，快速搭建聊天机器人、智能客服、知识问答系统
- 团队协作与知识管理：利用知识库功能构建企业文档库，结合多 Agent 实现智能检索和内容生成



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,341 |
| 语言 | TypeScript |
| Forks | 3,876 |
| Issues | 204 |
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
| Stars | 45,820 |
| 语言 | Java |
| Forks | 15,900 |
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
| Stars | 38,962 |
| 语言 | Python |
| Forks | 6,185 |
| Issues | 75 |
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
| Stars | 35,537 |
| 语言 | Python |
| Forks | 4,182 |
| Issues | 93 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,720 |
| 语言 | TypeScript |
| Forks | 3,649 |
| Issues | 292 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,718 |
| 语言 | TypeScript |
| Forks | 12,054 |
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
| Stars | 58,159 |
| 语言 | JavaScript |
| Forks | 6,284 |
| Issues | 320 |
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
| Stars | 75,428 |
| 语言 | Python |
| Forks | 10,230 |
| Issues | 241 |
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
| Stars | 51,825 |
| 语言 | TypeScript |
| Forks | 24,125 |
| Issues | 806 |
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
| Stars | 43,751 |
| 语言 | Go |
| Forks | 3,958 |
| Issues | 1,150 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### HKUDS/LightRAG

**描述**: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,018 |
| 语言 | Python |
| Forks | 4,699 |
| Issues | 204 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,033 |
| 语言 | Python |
| Forks | 2,131 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,459 |
| 语言 | Jupyter Notebook |
| Forks | 5,528 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,230 |
| 语言 | Python |
| Forks | 15,356 |
| Issues | 9 |
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
| Stars | 131,448 |
| 语言 | Python |
| Forks | 18,654 |
| Issues | 335 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 LLM 界面平台，支持 Ollama 和 OpenAI API 等多种后端，拥有超过 13 万 Stars，其最大的独特价值在于提供开箱即用的自托管解决方案，让用户完全掌控自己的 AI 数据和隐私，特别适合需要在本地部署企业级 AI 助手的场景。

**技术亮点**:
- 支持多种 LLM 后端集成：原生支持 Ollama 和 OpenAI API，同时兼容 OpenAPI 规范，便于扩展更多模型服务
- 内置 RAG（检索增强生成）系统，支持文档上传和向量检索，提升问答准确率
- 支持 MCP（Model Context Protocol）协议，可连接外部工具和数据源扩展能力
- 基于 Python 构建，提供完整的 Web UI 界面，开源可自部署，数据完全本地存储
- 功能丰富：支持对话管理、模型切换、多用户系统、图片上传等企业级特性

**适用场景**:
- 企业私有 AI 助手部署：需要保障数据隐私、不希望将敏感信息发送给第三方 API 的企业场景
- 个人开发者/研究者本地实验：需要便捷地测试和比较不同 LLM 模型效果，同时希望完全控制数据
- 构建内部知识库问答系统：利用 RAG 功能上传文档构建私有知识库，实现精准的知识检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,847 |
| 语言 | Python |
| Forks | 8,762 |
| Issues | 3,235 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，它将 RAG 与 Agent 能力深度融合，支持文档智能理解、多模态检索和 Deep Research，已在生产环境中验证，适合构建企业级知识问答系统和深度研究应用。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力增强检索-生成链路，支持复杂推理和工具调用
- 深度文档理解：内置 OCR、表格识别、版面分析等能力，支持 PDF、Word、Excel 等多格式文档处理
- GraphRAG 支持：基于知识图谱的检索增强，提升复杂关联查询效果
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型接入
- MCP 协议集成：支持 Model Context Protocol，便于扩展工具和外部系统集成

**适用场景**:
- 企业知识库问答：构建内部文档、FAQ、技术手册的智能问答系统
- 智能文档分析：自动解析合同、报告、技术文档，提取关键信息并回答相关问题
- Deep Research 助手：支持深度研究场景，通过 Agent 编排实现复杂问题的多步骤推理和跨文档综合分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,439 |
| 语言 | JavaScript |
| Forks | 23,642 |
| Issues | 78 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 代码助手的综合性能优化框架，通过 Skills、Instincts、Memory 等模块显著提升 Claude Code、Cursor 等工具的响应效率和任务完成质量，是当前 AI 编程辅助领域star数最高的项目之一（152k+），社区活跃度极高。

**技术亮点**:
- 多平台 AI 代理支持：统一兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手框架
- Skills & Instincts 系统：提供可扩展的技能库和本能反应机制，增强 AI 代理的决策能力
- Memory 记忆管理模块：实现上下文持久化和高效检索，减少重复交互开销
- Security 安全模块：内置安全策略和权限控制，保障代码操作安全性
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于扩展和第三方集成

**适用场景**:
- 个人开发者优化 AI 编程效率：通过 Skills 和 Instincts 系统，让 AI 代码助手更准确地理解开发者意图，减少无效交互
- 企业级 AI 开发辅助平台：基于该框架构建统一的 AI 代码审核、自动化测试和代码生成流水线
- 安全敏感型代码开发：利用内置 Security 模块，在金融、医疗等高安全要求场景下规范 AI 代码操作



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,087 |
| 语言 | TypeScript |
| Forks | 14,906 |
| Issues | 656 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 平台，拥有超过 75k Stars，集成多模型支持（MCP、OpenAI、Claude、Gemini、DeepSeek）和知识库能力，特别适合需要构建多智能体协作系统的企业和开发者。其"Agents as the unit of work"理念和低门槛的 Agent 团队设计，使复杂 AI 工作流搭建变得简单高效。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，通过统一接口实现模型切换
- MCP (Model Context Protocol) 原生支持：标准化 AI 模型上下文交互协议，便于扩展和集成第三方工具
- 多智能体协作框架：支持构建 Agent Team，实现多 Agent 间的任务分解与协作
- 企业级知识库集成：内置 RAG 能力，支持文档检索和知识管理
- TypeScript 全栈架构：前后端均采用 TypeScript 开发，保证类型安全与代码可维护性

**适用场景**:
- 企业级智能助手团队：为中大型企业构建多业务领域的 AI Agent 团队，实现客户服务、文档处理、数据分析等场景的自动化
- AI 应用快速开发：开发者利用现成的 Agent 框架和 UI 组件，快速搭建聊天机器人、智能客服、知识问答系统
- 团队协作与知识管理：利用知识库功能构建企业文档库，结合多 Agent 实现智能检索和内容生成



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,517 |
| 语言 | Python |
| Forks | 8,755 |
| Issues | 3,481 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名 AI 研究组织 NousResearch 打造的高星 AI Agent 框架，支持多种主流 LLM 提供商（OpenAI、Anthropic、Claude 等），具有成熟的 Agent 架构和工具调用能力，适合构建智能化的 AI 应用。

**技术亮点**:
- 多模型支持：集成 OpenAI GPT、Anthropic Claude 等多种主流大语言模型，提供统一的 Agent 接口
- 成熟的 Agent 框架：实现了规划、推理、工具调用等核心 Agent 能力，支持复杂任务分解
- 工具调用系统：内置 MCP（Model Context Protocol）支持，可扩展的工具生态
- 代码生成能力：通过 Claude Code 集成支持高质量代码生成和自动化编程
- 开源可定制：MIT 许可证，代码透明可审计，便于企业级定制和私有化部署

**适用场景**:
- 企业 AI 助手开发：构建企业内部智能助手，集成到现有工作流程提升效率
- 智能代码助手：基于 Claude Code 能力开发代码审查、自动化生成、调试辅助工具
- AI Agent 应用：开发自动化任务执行、多步骤推理、工具编排等复杂 Agent 应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,446 |
| 语言 | HTML |
| Forks | 20,898 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万 Stars，汇集了数千个经过验证的高质量 ChatGPT 提示词，支持自托管部署，是 AI 从业者必备的资源库和隐私保护方案。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持完整自托管部署，可完全控制数据和隐私
- 社区驱动的提示词收集与分享机制，包含精选分类
- 多平台支持：ChatGPT、Claude、Gemini、GPT-4 等主流 LLM
- 响应式设计，支持 Web 端直接使用或集成到其他应用

**适用场景**:
- AI 开发者和研究者：快速查找和复用经过社区验证的高质量提示词，提升开发效率
- 企业自托管：部署私有化实例，保护内部数据隐私，满足合规要求
- 个人用户：发现和收藏优质提示词，优化 ChatGPT 等 AI 工具的使用体验



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,592 |
| 语言 | Jupyter Notebook |
| Forks | 13,900 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,162 |
| 语言 | TypeScript |
| Forks | 8,524 |
| Issues | 78 |
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
| Stars | 49,341 |
| 语言 | TypeScript |
| Forks | 3,876 |
| Issues | 204 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,008 |
| 语言 | Python |
| Forks | 9,896 |
| Issues | 358 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,197 |
| 语言 | Python |
| Forks | 6,846 |
| Issues | 952 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,263 |
| 语言 | Python |
| Forks | 3,121 |
| Issues | 205 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,159 |
| 语言 | JavaScript |
| Forks | 6,284 |
| Issues | 320 |
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
| Stars | 71,071 |
| 语言 | Python |
| Forks | 8,926 |
| Issues | 395 |
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
| Stars | 50,883 |
| 语言 | TypeScript |
| Forks | 4,078 |
| Issues | 499 |
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
| Stars | 51,825 |
| 语言 | TypeScript |
| Forks | 24,125 |
| Issues | 806 |
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
| Stars | 76,272 |
| 语言 | Python |
| Forks | 15,488 |
| Issues | 4,198 |
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
| Stars | 39,409 |
| 语言 | TypeScript |
| Forks | 4,007 |
| Issues | 1,099 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### shanraisshan/claude-code-best-practice

**描述**: practice made claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,733 |
| 语言 | HTML |
| Forks | 3,654 |
| Issues | 10 |
| Topics | agentic-engineering, anthropic, best-practices, boris, boris-cherny, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, vibe-coding |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 146,857 |
| 语言 | Python |
| Forks | 8,756 |
| Issues | 950 |
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
| Stars | 168,708 |
| 语言 | Go |
| Forks | 15,548 |
| Issues | 2,925 |
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
| Stars | 47,717 |
| 语言 | Rust |
| Forks | 9,503 |
| Issues | 0 |
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
| Stars | 34,033 |
| 语言 | Python |
| Forks | 2,131 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 63,601 |
| 语言 | Python |
| Forks | 6,379 |
| Issues | 88 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
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
| Stars | 104,318 |
| 语言 | Python |
| Forks | 6,499 |
| Issues | 560 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (10 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,969 |
| 语言 | Python |
| Forks | 8,545 |
| Issues | 966 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的大模型微调框架之一，通过统一接口支持100+ LLMs和VLMs的高效微调，基于ACL 2024学术认可和7万Stars的社区验证，为研究者和开发者提供了从实验到部署的一站式解决方案，特别适合需要在有限算力下快速定制大模型的企业团队和学术机构。

**技术亮点**:
- 统一微调框架：支持100+预训练模型（LLaMA、LLaMA3、Qwen、DeepSeek、Gemma等）和视觉语言模型，提供标准化API降低学习成本
- 高效微调技术：集成LORA、QLORA、PEFT等轻量化微调方法，支持Int4/Int8量化，显著降低GPU显存占用
- 完整训练流程：覆盖预训练、指令微调、RLHF（基于人类反馈的强化学习）等全链路训练范式
- 多模态能力：同时支持语言模型和多模态视觉语言模型的微调，适应AI多模态发展趋势
- ACL 2024顶会论文验证：学术背书保证了方法的先进性和工程实现的可靠性

**适用场景**:
- 企业AI应用：企业可利用LlamaFactory快速将开源大模型微调至特定领域（如金融、医疗、法律），构建专属AI助手或垂直应用
- 学术研究与实验：研究人员能在统一框架下快速对比不同模型和微调方法的效果，加速NLP/ML领域的研究迭代
- 个人开发者定制：个人开发者借助量化技术，在消费级GPU（如RTX 3090/4090）上即可完成7B-70B模型的微调，实现低成本AI创新



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,765 |
| 语言 | Python |
| Forks | 6,532 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是一个功能全面的开源金融数据平台，拥有超过65k Stars的活跃社区，支持股票、加密货币、期权、固收等多种金融产品的数据获取与技术分析，并内置AI和机器学习能力，为量化分析师和开发者提供了一站式解决方案，是目前最成熟的Python金融分析开源项目之一。

**技术亮点**:
- 模块化架构设计：提供Python SDK、CLI和GUI三种交互方式，支持灵活集成到现有工作流
- AI代理集成：内置AI代理能力，支持自然语言查询金融数据，降低使用门槛
- 多数据源统一接口：聚合多个金融数据API，提供一致的数据访问体验
- 丰富的分析工具集：内置技术指标、基本面分析、图表可视化等完整工具链
- 覆盖多资产类别：支持股票、加密货币、期权、衍生品、固定收益等多元化金融产品

**适用场景**:
- 量化交易研究：quant和算法交易开发者可使用SDK快速获取市场数据，构建回测和交易策略
- 金融数据分析：分析师利用内置工具进行技术分析和基本面研究，提高工作效率
- AI金融应用开发：开发团队可基于平台的AI代理能力构建智能投顾、风险预测等应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,446 |
| 语言 | HTML |
| Forks | 20,898 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万 Stars，汇集了数千个经过验证的高质量 ChatGPT 提示词，支持自托管部署，是 AI 从业者必备的资源库和隐私保护方案。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持完整自托管部署，可完全控制数据和隐私
- 社区驱动的提示词收集与分享机制，包含精选分类
- 多平台支持：ChatGPT、Claude、Gemini、GPT-4 等主流 LLM
- 响应式设计，支持 Web 端直接使用或集成到其他应用

**适用场景**:
- AI 开发者和研究者：快速查找和复用经过社区验证的高质量提示词，提升开发效率
- 企业自托管：部署私有化实例，保护内部数据隐私，满足合规要求
- 个人用户：发现和收藏优质提示词，优化 ChatGPT 等 AI 工具的使用体验



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,592 |
| 语言 | Jupyter Notebook |
| Forks | 13,900 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,720 |
| 语言 | TypeScript |
| Forks | 3,649 |
| Issues | 292 |
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
| Stars | 159,250 |
| 语言 | Python |
| Forks | 32,845 |
| Issues | 2,368 |
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
| Stars | 76,272 |
| 语言 | Python |
| Forks | 15,488 |
| Issues | 4,198 |
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
| Stars | 108,533 |
| 语言 | Python |
| Forks | 12,595 |
| Issues | 3,965 |
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
| Stars | 99,068 |
| 语言 | Python |
| Forks | 27,472 |
| Issues | 18,467 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,459 |
| 语言 | Jupyter Notebook |
| Forks | 5,528 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 152,439 |
| 语言 | JavaScript |
| Forks | 23,642 |
| Issues | 78 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 代码助手的综合性能优化框架，通过 Skills、Instincts、Memory 等模块显著提升 Claude Code、Cursor 等工具的响应效率和任务完成质量，是当前 AI 编程辅助领域star数最高的项目之一（152k+），社区活跃度极高。

**技术亮点**:
- 多平台 AI 代理支持：统一兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手框架
- Skills & Instincts 系统：提供可扩展的技能库和本能反应机制，增强 AI 代理的决策能力
- Memory 记忆管理模块：实现上下文持久化和高效检索，减少重复交互开销
- Security 安全模块：内置安全策略和权限控制，保障代码操作安全性
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于扩展和第三方集成

**适用场景**:
- 个人开发者优化 AI 编程效率：通过 Skills 和 Instincts 系统，让 AI 代码助手更准确地理解开发者意图，减少无效交互
- 企业级 AI 开发辅助平台：基于该框架构建统一的 AI 代码审核、自动化测试和代码生成流水线
- 安全敏感型代码开发：利用内置 Security 模块，在金融、医疗等高安全要求场景下规范 AI 代码操作



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,311 |
| 语言 | Go |
| Forks | 3,931 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最全面的开源本地 AI 推理平台，一站式支持 LLM、图像、音频、视频等多种模型，配合去中心化架构设计，特别适合需要数据隐私保护或降低云服务依赖的企业和开发者，无需 GPU 即可运行复杂的 AI 工作负载。

**技术亮点**:
- 多模态统一推理引擎 - 同时支持 LLMs (Llama/Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、TTS、对象检测等十余种模型类型
- 去中心化分布式架构 - 基于 libp2p 构建，支持分布式部署和 P2P 通信，适合边缘计算和去中心化应用场景
- API 优先设计 - 提供 OpenAI 兼容的 REST API，可无缝替代云端 AI 服务，便于现有应用迁移
- 硬件无关运行 - 支持 CPU 推理，无强制 GPU 要求，降低部署门槛，同时兼容 GPU 加速
- MCP (Model Context Protocol) 支持 - 集成最新的模型上下文协议，支持 AI Agents 和工具调用能力

**适用场景**:
- 企业私有化 AI 部署 - 对数据隐私敏感的场景（如医疗、金融、法律），需要完全控制数据和模型
- 本地开发与测试 - 开发者本地构建 AI 原型应用，无需付费订阅云服务，支持快速迭代
- 边缘设备 AI 推理 - 在资源受限的边缘节点部署 AI 能力，支持离线工作和低延迟响应



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,071 |
| 语言 | Python |
| Forks | 8,926 |
| Issues | 395 |
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
| Stars | 50,883 |
| 语言 | TypeScript |
| Forks | 4,078 |
| Issues | 499 |
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
| Stars | 183,725 |
| 语言 | TypeScript |
| Forks | 56,724 |
| Issues | 1,469 |
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
| Stars | 156,397 |
| 语言 | Python |
| Forks | 12,863 |
| Issues | 2,462 |
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
| Stars | 97,112 |
| 语言 | Python |
| Forks | 9,059 |
| Issues | 172 |
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
| Stars | 80,847 |
| 语言 | Python |
| Forks | 9,390 |
| Issues | 253 |
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
| Stars | 183,749 |
| 语言 | TypeScript |
| Forks | 39,139 |
| Issues | 16,243 |
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
| Stars | 94,092 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 304 |
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
| Stars | 78,895 |
| 语言 | TypeScript |
| Forks | 5,792 |
| Issues | 757 |
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
| Stars | 77,078 |
| 语言 | TypeScript |
| Forks | 6,601 |
| Issues | 138 |
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
| Stars | 79,409 |
| 语言 | Go |
| Forks | 2,766 |
| Issues | 312 |
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
| Stars | 76,267 |
| 语言 | Go |
| Forks | 2,748 |
| Issues | 957 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### cli/cli

**描述**: GitHub’s official command line tool

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,772 |
| 语言 | Go |
| Forks | 8,243 |
| Issues | 958 |
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
| Stars | 41,509 |
| 语言 | Go |
| Forks | 1,182 |
| Issues | 173 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
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
| Stars | 421,094 |
| 语言 | Python |
| Forks | 45,840 |
| Issues | 1,237 |
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
| Stars | 75,577 |
| 语言 | JavaScript |
| Forks | 7,280 |
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
| Stars | 50,883 |
| 语言 | TypeScript |
| Forks | 4,078 |
| Issues | 499 |
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
| Stars | 183,725 |
| 语言 | TypeScript |
| Forks | 56,724 |
| Issues | 1,469 |
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
| Stars | 51,612 |
| 语言 | Go |
| Forks | 10,315 |
| Issues | 231 |
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
| Stars | 121,671 |
| 语言 | Go |
| Forks | 42,837 |
| Issues | 2,727 |
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
| Stars | 71,484 |
| 语言 | Go |
| Forks | 18,914 |
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
| Stars | 54,859 |
| 语言 | Go |
| Forks | 6,561 |
| Issues | 2,828 |
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
| Stars | 47,498 |
| 语言 | Go |
| Forks | 5,044 |
| Issues | 980 |
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
| Stars | 94,092 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 304 |
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
| Stars | 76,634 |
| 语言 | TypeScript |
| Forks | 6,616 |
| Issues | 404 |
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
| Stars | 85,163 |
| 语言 | JavaScript |
| Forks | 7,629 |
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
| Stars | 69,830 |
| 语言 | Go |
| Forks | 1,910 |
| Issues | 321 |
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
| Stars | 62,661 |
| 语言 | Go |
| Forks | 5,906 |
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
| Stars | 58,781 |
| 语言 | Go |
| Forks | 4,260 |
| Issues | 24 |
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
| Stars | 85,163 |
| 语言 | JavaScript |
| Forks | 7,629 |
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
| Stars | 63,548 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 759 |
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
| Stars | 45,311 |
| 语言 | Go |
| Forks | 3,931 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最全面的开源本地 AI 推理平台，一站式支持 LLM、图像、音频、视频等多种模型，配合去中心化架构设计，特别适合需要数据隐私保护或降低云服务依赖的企业和开发者，无需 GPU 即可运行复杂的 AI 工作负载。

**技术亮点**:
- 多模态统一推理引擎 - 同时支持 LLMs (Llama/Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、TTS、对象检测等十余种模型类型
- 去中心化分布式架构 - 基于 libp2p 构建，支持分布式部署和 P2P 通信，适合边缘计算和去中心化应用场景
- API 优先设计 - 提供 OpenAI 兼容的 REST API，可无缝替代云端 AI 服务，便于现有应用迁移
- 硬件无关运行 - 支持 CPU 推理，无强制 GPU 要求，降低部署门槛，同时兼容 GPU 加速
- MCP (Model Context Protocol) 支持 - 集成最新的模型上下文协议，支持 AI Agents 和工具调用能力

**适用场景**:
- 企业私有化 AI 部署 - 对数据隐私敏感的场景（如医疗、金融、法律），需要完全控制数据和模型
- 本地开发与测试 - 开发者本地构建 AI 原型应用，无需付费订阅云服务，支持快速迭代
- 边缘设备 AI 推理 - 在资源受限的边缘节点部署 AI 能力，支持离线工作和低延迟响应



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,112 |
| 语言 | Python |
| Forks | 9,059 |
| Issues | 172 |
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
| Stars | 87,260 |
| 语言 | Python |
| Forks | 33,814 |
| Issues | 432 |
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
| Stars | 100,036 |
| 语言 | TypeScript |
| Forks | 27,152 |
| Issues | 1,148 |
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
| Stars | 78,895 |
| 语言 | TypeScript |
| Forks | 5,792 |
| Issues | 757 |
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
| Stars | 68,925 |
| 语言 | JavaScript |
| Forks | 23,093 |
| Issues | 208 |
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
| Stars | 55,957 |
| 语言 | JavaScript |
| Forks | 10,215 |
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
| Stars | 51,786 |
| 语言 | JavaScript |
| Forks | 4,704 |
| Issues | 1,465 |
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
| Stars | 47,789 |
| 语言 | JavaScript |
| Forks | 1,582 |
| Issues | 657 |
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
| Stars | 88,292 |
| 语言 | Go |
| Forks | 8,576 |
| Issues | 674 |
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
| Stars | 71,475 |
| 语言 | Go |
| Forks | 4,694 |
| Issues | 253 |
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
| Stars | 57,565 |
| 语言 | Go |
| Forks | 3,281 |
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
| Stars | 41,509 |
| 语言 | Go |
| Forks | 1,182 |
| Issues | 173 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
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
| Stars | 421,094 |
| 语言 | Python |
| Forks | 45,840 |
| Issues | 1,237 |
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
| Stars | 75,577 |
| 语言 | JavaScript |
| Forks | 7,280 |
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
| Stars | 100,718 |
| 语言 | TypeScript |
| Forks | 12,054 |
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
| Stars | 58,159 |
| 语言 | JavaScript |
| Forks | 6,284 |
| Issues | 320 |
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
| Stars | 43,751 |
| 语言 | Go |
| Forks | 3,958 |
| Issues | 1,150 |
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
| Stars | 51,612 |
| 语言 | Go |
| Forks | 10,315 |
| Issues | 231 |
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
| Stars | 159,446 |
| 语言 | HTML |
| Forks | 20,898 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词社区之一，拥有近 16 万 Stars，汇集了数千个经过验证的高质量 ChatGPT 提示词，支持自托管部署，是 AI 从业者必备的资源库和隐私保护方案。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持完整自托管部署，可完全控制数据和隐私
- 社区驱动的提示词收集与分享机制，包含精选分类
- 多平台支持：ChatGPT、Claude、Gemini、GPT-4 等主流 LLM
- 响应式设计，支持 Web 端直接使用或集成到其他应用

**适用场景**:
- AI 开发者和研究者：快速查找和复用经过社区验证的高质量提示词，提升开发效率
- 企业自托管：部署私有化实例，保护内部数据隐私，满足合规要求
- 个人用户：发现和收藏优质提示词，优化 ChatGPT 等 AI 工具的使用体验



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,162 |
| 语言 | TypeScript |
| Forks | 8,524 |
| Issues | 78 |
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
| Stars | 38,263 |
| 语言 | Python |
| Forks | 3,121 |
| Issues | 205 |
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
| Stars | 35,537 |
| 语言 | Python |
| Forks | 4,182 |
| Issues | 93 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,687 |
| 语言 | TypeScript |
| Forks | 9,998 |
| Issues | 2,243 |
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
| Stars | 87,297 |
| 语言 | TypeScript |
| Forks | 8,856 |
| Issues | 1,646 |
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
| Stars | 127,440 |
| 语言 | JavaScript |
| Forks | 12,473 |
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
| Stars | 169,798 |
| 语言 | Go |
| Forks | 13,139 |
| Issues | 178 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,803 |
| 语言 | Shell |
| Forks | 12,546 |
| Issues | 79 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,856 |
| 语言 | Python |
| Forks | 6,547 |
| Issues | 67 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,929 |
| 语言 | Python |
| Forks | 13,078 |
| Issues | 118 |
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
| Stars | 87,307 |
| 语言 | Python |
| Forks | 7,513 |
| Issues | 631 |
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
| Stars | 135,013 |
| 语言 | Unknown |
| Forks | 33,946 |
| Issues | 145 |
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
| Stars | 385,404 |
| 语言 | Python |
| Forks | 66,103 |
| Issues | 81 |
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
| Stars | 114,530 |
| 语言 | TypeScript |
| Forks | 5,895 |
| Issues | 71 |
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
| Stars | 110,023 |
| 语言 | TypeScript |
| Forks | 7,994 |
| Issues | 253 |
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
| Stars | 51,229 |
| 语言 | JavaScript |
| Forks | 4,290 |
| Issues | 29 |
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
| Stars | 48,122 |
| 语言 | Go |
| Forks | 10,283 |
| Issues | 1,895 |
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
| Stars | 103,313 |
| 语言 | C++ |
| Forks | 16,754 |
| Issues | 1,477 |
| Topics | ggml |
| 许可证 | MIT License |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,520 |
| 语言 | TypeScript |
| Forks | 9,919 |
| Issues | 344 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,553 |
| 语言 | Python |
| Forks | 1,632 |
| Issues | 37 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 291,930 |
| 语言 | Python |
| Forks | 27,655 |
| Issues | 22 |
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
| Stars | 219,538 |
| 语言 | Python |
| Forks | 50,324 |
| Issues | 922 |
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
| Stars | 86,010 |
| 语言 | Python |
| Forks | 37,225 |
| Issues | 3,625 |
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
| Stars | 77,677 |
| 语言 | Python |
| Forks | 45,156 |
| Issues | 1,279 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,838 |
| 语言 | Python |
| Forks | 16,839 |
| Issues | 22 |
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
| Stars | 442,713 |
| 语言 | TypeScript |
| Forks | 44,261 |
| Issues | 206 |
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
| Stars | 352,761 |
| 语言 | TypeScript |
| Forks | 43,905 |
| Issues | 8 |
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
| Stars | 138,674 |
| 语言 | TypeScript |
| Forks | 16,493 |
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
| Stars | 120,874 |
| 语言 | TypeScript |
| Forks | 13,244 |
| Issues | 2,959 |
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
| Stars | 112,171 |
| 语言 | TypeScript |
| Forks | 8,506 |
| Issues | 1,810 |
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
| Stars | 108,519 |
| 语言 | TypeScript |
| Forks | 13,345 |
| Issues | 5,026 |
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
| Stars | 97,755 |
| 语言 | TypeScript |
| Forks | 54,594 |
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
| Stars | 97,710 |
| 语言 | TypeScript |
| Forks | 5,372 |
| Issues | 709 |
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
| Stars | 94,523 |
| 语言 | TypeScript |
| Forks | 5,188 |
| Issues | 109 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,865 |
| 语言 | TypeScript |
| Forks | 8,056 |
| Issues | 713 |
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
| Stars | 244,426 |
| 语言 | JavaScript |
| Forks | 50,903 |
| Issues | 1,223 |
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
| Stars | 116,689 |
| 语言 | JavaScript |
| Forks | 35,331 |
| Issues | 2,610 |
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
| Stars | 111,888 |
| 语言 | JavaScript |
| Forks | 36,331 |
| Issues | 562 |
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
| Stars | 108,992 |
| 语言 | JavaScript |
| Forks | 11,619 |
| Issues | 265 |
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
| Stars | 98,132 |
| 语言 | JavaScript |
| Forks | 32,692 |
| Issues | 1,679 |
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
| Stars | 95,572 |
| 语言 | JavaScript |
| Forks | 15,349 |
| Issues | 62 |
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
| Stars | 86,284 |
| 语言 | JavaScript |
| Forks | 4,886 |
| Issues | 979 |
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
| Stars | 70,977 |
| 语言 | JavaScript |
| Forks | 16,810 |
| Issues | 893 |
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
| Stars | 66,315 |
| 语言 | JavaScript |
| Forks | 9,188 |
| Issues | 0 |
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
| Stars | 65,841 |
| 语言 | JavaScript |
| Forks | 9,378 |
| Issues | 208 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,388 |
| 语言 | JavaScript |
| Forks | 5,649 |
| Issues | 72 |
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
| Stars | 59,844 |
| 语言 | JavaScript |
| Forks | 20,479 |
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
| Stars | 57,430 |
| 语言 | JavaScript |
| Forks | 12,305 |
| Issues | 26 |
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
| Stars | 53,110 |
| 语言 | JavaScript |
| Forks | 10,604 |
| Issues | 457 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,477 |
| 语言 | JavaScript |
| Forks | 11,464 |
| Issues | 238 |
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
| Stars | 48,624 |
| 语言 | JavaScript |
| Forks | 2,428 |
| Issues | 1,210 |
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
| Stars | 133,436 |
| 语言 | Go |
| Forks | 18,915 |
| Issues | 9,959 |
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
| Stars | 87,541 |
| 语言 | Go |
| Forks | 8,243 |
| Issues | 267 |
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
| Stars | 81,651 |
| 语言 | Go |
| Forks | 4,994 |
| Issues | 392 |
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
| Stars | 68,632 |
| 语言 | Go |
| Forks | 3,216 |
| Issues | 17 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,605 |
| 语言 | Go |
| Forks | 5,022 |
| Issues | 1,158 |
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
| Stars | 50,979 |
| 语言 | Go |
| Forks | 21,883 |
| Issues | 405 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,412 |
| 语言 | Python |
| Forks | 55,333 |
| Issues | 527 |
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
| Stars | 97,625 |
| 语言 | Python |
| Forks | 12,026 |
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
| Stars | 85,966 |
| 语言 | Python |
| Forks | 7,207 |
| Issues | 482 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,567 |
| 语言 | TypeScript |
| Forks | 10,351 |
| Issues | 746 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,084 |
| 语言 | TypeScript |
| Forks | 7,581 |
| Issues | 34 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,021 |
| 语言 | JavaScript |
| Forks | 32,452 |
| Issues | 280 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 62,697 |
| 语言 | JavaScript |
| Forks | 4,006 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,326 |
| 语言 | JavaScript |
| Forks | 7,129 |
| Issues | 141 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,819 |
| 语言 | Go |
| Forks | 14,985 |
| Issues | 44 |
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
| Stars | 50,622 |
| 语言 | Go |
| Forks | 1,594 |
| Issues | 267 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,297 |
| 语言 | Go |
| Forks | 7,957 |
| Issues | 564 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 150,626 |
| 语言 | Python |
| Forks | 11,461 |
| Issues | 322 |
| Topics | awesome, github, hellogithub, python |
