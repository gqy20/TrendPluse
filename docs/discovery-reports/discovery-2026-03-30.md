# 项目发现报告 (2026-03-30)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 28 |
| 已在监控 | 26 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
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
| Stars | 129,306 |
| 语言 | Python |
| Forks | 18,303 |
| Issues | 283 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面解决方案，通过统一接口支持 Ollama、OpenAI 等多款 LLM 后端，配合 RAG 和 MCP 扩展能力，既能满足企业级隐私合规需求，又为个人开发者提供了开箱即用的 AI 前端体验。

**技术亮点**:
- 多后端统一接入：支持 Ollama、OpenAI API、兼容 OpenAPI 标准的各类 LLM 服务，可灵活切换
- RAG 检索增强生成：内置文档解析和向量检索能力，支持知识库增强问答
- MCP (Model Context Protocol) 支持：实现与外部工具和服务的标准化集成
- 自托管部署：完整的前后端解决方案，支持 Docker 快速部署，保障数据隐私
- Web UI 界面：现代化响应式设计，提供对话管理、模型配置等完整功能

**适用场景**:
- 企业私有化 AI 助手：需要在内部部署 AI 对话系统以满足数据安全和合规要求的企业
- 多模型管理场景：团队或开发者需要统一管理多个 LLM 后端、对比不同模型效果的开发环境
- 知识库问答系统：基于 RAG 能力构建私有知识库的智能问答应用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,616 |
| 语言 | Python |
| Forks | 8,581 |
| Issues | 3,179 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档解析和多模态上下文构建，配合 Deep Research 和 GraphRAG 等前沿技术，为企业级知识问答和智能文档处理提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agentic Workflow 实现动态检索策略和自主决策，提升复杂查询的处理能力
- 深度文档理解：支持多种文档格式的智能解析，提取结构化信息构建高质量知识库
- GraphRAG 支持：基于知识图谱的检索增强，显著提升跨文档关联分析和复杂推理能力
- 多 LLM 统一接入：兼容 OpenAI、Ollama、DeepSeek 等多种模型，提供灵活的模型切换能力
- MCP 协议集成：支持 Model Context Protocol 标准，便于扩展和集成第三方工具生态

**适用场景**:
- 企业智能客服与知识库问答：构建支持复杂多轮对话和上下文理解的企业级问答系统，可处理技术文档、规章制度、产品手册等企业知识
- 智能文档分析与处理：自动解析合同、报告、论文等长文档，提取关键信息、生成摘要、回答专业问题，适用于法务、财务、学术研究场景
- 深度研究与分析助手：利用 Deep Research 和 GraphRAG 能力，辅助进行市场调研、竞品分析、学术文献综述等需要跨源综合分析的任务



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,202 |
| 语言 | TypeScript |
| Forks | 6,721 |
| Issues | 240 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的 Web 数据抓取工具，可将任意网站转换为 LLM 就绪的 Markdown 或结构化数据，拥有 10 万+ Stars，是 AI 数据管道建设的首选开源解决方案。

**技术亮点**:
- 多格式输出：支持 Markdown、HTML、JSON 等多种格式，满足不同 AI 框架需求
- LLM-Ready 处理：内置智能内容清洗，自动去除噪音保留核心语义
- 高级爬取能力：支持整站爬取、深度抓取，兼容 SPA/CSR 动态渲染页面
- 多语言 SDK：提供 Python、Node.js、Go 等多语言 SDK，一行代码集成
- 反爬对抗策略：内置代理轮换、自动限速等机制，提高抓取成功率

**适用场景**:
- AI/LLM 应用数据管道：为 RAG 系统、知识库 AI、LLM 微调提供高质量训练/推理数据
- 竞品分析 & 市场研究：快速抓取竞争对手网站进行结构化数据分析
- 内容聚合平台：构建行业资讯平台、垂直搜索引擎或知识库



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,904 |
| 语言 | JavaScript |
| Forks | 15,428 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 编码 Agent 的综合性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大核心模块显著提升 AI agent 的开发效率和能力上限，拥有 118k+ stars 的高人气，是研究 AI agent 架构和开发效率工具的绝佳参考。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 的标准化工具集成框架，支持多种 AI 编码工具生态
- 创新的 Memory 系统设计，实现长期上下文保持和跨会话信息复用
- 安全沙箱机制 (Security) 确保 AI agent 操作的安全性和可控性
- Skills & Instincts 双轨系统：Skills 提供可复用技能库，Instincts 实现本能级响应优化
- 支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的跨平台兼容

**适用场景**:
- 企业级 AI 辅助开发平台：构建内部 AI coding assistant，集成到 CI/CD 流程提升团队开发效率
- AI Agent 研究与开发：基于项目架构快速构建新的 AI agent 原型，验证 LLM 应用假设
- 个人开发者效率工具：利用现成的 Skills 和 Instincts 模块增强现有 AI 编码工具的能力
- 多 Agent 协作系统：借助 Memory 和 MCP 框架设计复杂的多 Agent 协作工作流



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,598 |
| 语言 | Go |
| Forks | 3,822 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型的本地运行，无需 GPU 即可部署，特别适合需要在本地环境或边缘设备上运行 AI 能力的开发者和企业。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和低内存占用优势，支持并发处理多模型请求
- 支持多种模型类型：LLM（Mamba、Llama）、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成（MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在多节点间协同运行
- 提供标准 API 接口，兼容 OpenAI API 格式，便于现有应用快速迁移集成
- 无 GPU 依赖设计，支持在 CPU 和各类硬件上运行，降低部署门槛和成本

**适用场景**:
- 本地/私有化 AI 部署：对数据隐私有严格要求的企业，可在本地服务器运行 AI 模型，避免数据外传
- 边缘计算场景：在没有强大 GPU 支持的边缘设备上部署 AI 能力，如 IoT 设备、嵌入式系统
- 开发测试环境：开发者可在本地机器上快速测试 AI 应用，无需依赖云服务 API



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,510 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 687 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 协作平台，拥有 74k+ stars 的高人气，支持多 Agent 协作、团队设计以及 OpenAI/Claude/DeepSeek/Gemini 等多种主流 AI 模型集成，特别适合需要构建智能 Agent 工作流的团队和个人开发者。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 协同工作，引入 Agent 作为工作交互单元的理念，实现复杂的 AI 任务分工与协作
- 多模型统一集成：一站式支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供灵活的模型切换能力
- MCP 协议支持：遵循 Model Context Protocol 标准，实现与外部工具和服务的标准化集成
- 知识库管理：内置知识库功能，支持 RAG（检索增强生成）场景，便于构建私域知识问答系统
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保证类型安全，便于维护和扩展

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部 AI 助手平台，实现客服、文档处理、数据分析等业务流程自动化
- AI Agent 团队协作：团队可以设计多个专业 Agent 组成协作团队，模拟真实工作中的分工协作场景
- 个人开发者 AI 应用开发：开发者可利用其模块化设计和多模型支持，快速构建和部署 AI 应用原型



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,270 |
| 语言 | Python |
| Forks | 8,438 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持100+开源模型的一站式微调，融合LoRA、QLoRA、RLHF等主流技术，让研究者和开发者无需从零搭建训练流水线即可快速定制专属模型，极大降低了LLM微调的工程门槛。

**技术亮点**:
- 【统一微调框架】支持100+LLMs和VLMs，包括Llama3、Qwen、Gemma、DeepSeek、ChatGLM等主流开源模型，一套代码库覆盖所有模型
- 【多范式微调支持】集成LoRA、QLoRA、Prefix-Tuning、Ptuning等多种参数高效微调方法，显著降低GPU显存占用
- 【RLHF完整实现】内置PPO、DPO、KTO等强化学习人类反馈训练算法，支持构建更高质量的对齐模型
- 【多模态融合】同时支持视觉-语言模型的微调，可用于图文理解和多模态Agent开发
- 【工程优化完善】提供分布式训练、混合精度、梯度累积等优化，支持DeepSpeed加速，开箱即用的训练监控和断点续训功能

**适用场景**:
- 【企业私有化部署】企业可基于LlamaFactory对开源基座模型进行领域适配微调（如金融、医疗、法律），构建私有化AI助手，在保证数据安全的同时实现业务定制
- 【学术研究快速验证】研究人员可快速实验不同模型架构和微调策略组合，支持新算法对比评估，已有多篇顶会论文采用
- 【个人开发者定制AI】个人开发者可低成本微调小模型实现特定任务（如聊天机器人、代码助手、文案生成），无需昂贵的云端API调用费用



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,809 |
| 语言 | TypeScript |
| Forks | 6,704 |
| Issues | 28 |
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
| Stars | 43,482 |
| 语言 | TypeScript |
| Forks | 3,230 |
| Issues | 194 |
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
| Stars | 42,658 |
| 语言 | Python |
| Forks | 9,862 |
| Issues | 349 |
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
| Stars | 35,058 |
| 语言 | TypeScript |
| Forks | 7,124 |
| Issues | 465 |
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
| Stars | 45,630 |
| 语言 | Java |
| Forks | 15,860 |
| Issues | 78 |
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
| Stars | 38,875 |
| 语言 | Python |
| Forks | 6,172 |
| Issues | 106 |
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
| Stars | 33,717 |
| 语言 | Python |
| Forks | 2,092 |
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
| Stars | 33,500 |
| 语言 | TypeScript |
| Forks | 3,633 |
| Issues | 279 |
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
| Stars | 32,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,453 |
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
| Stars | 32,194 |
| 语言 | Python |
| Forks | 3,635 |
| Issues | 72 |
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
| Stars | 104,028 |
| 语言 | Python |
| Forks | 15,174 |
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
| Stars | 57,168 |
| 语言 | JavaScript |
| Forks | 6,188 |
| Issues | 310 |
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
| Stars | 70,218 |
| 语言 | Python |
| Forks | 8,792 |
| Issues | 343 |
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
| Stars | 44,962 |
| 语言 | TypeScript |
| Forks | 3,353 |
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
| Stars | 85,096 |
| 语言 | Python |
| Forks | 9,859 |
| Issues | 213 |
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
| Stars | 51,255 |
| 语言 | TypeScript |
| Forks | 24,001 |
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
| Stars | 181,749 |
| 语言 | TypeScript |
| Forks | 56,322 |
| Issues | 1,428 |
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
| Stars | 154,541 |
| 语言 | Java |
| Forks | 46,140 |
| Issues | 67 |
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
| Stars | 146,417 |
| 语言 | Python |
| Forks | 8,672 |
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
| Stars | 72,487 |
| 语言 | MDX |
| Forks | 7,763 |
| Issues | 254 |
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
| Stars | 35,685 |
| 语言 | Rust |
| Forks | 2,122 |
| Issues | 472 |
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
| Stars | 55,468 |
| 语言 | Jupyter Notebook |
| Forks | 19,157 |
| Issues | 15 |
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
| Stars | 129,306 |
| 语言 | Python |
| Forks | 18,303 |
| Issues | 283 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面解决方案，通过统一接口支持 Ollama、OpenAI 等多款 LLM 后端，配合 RAG 和 MCP 扩展能力，既能满足企业级隐私合规需求，又为个人开发者提供了开箱即用的 AI 前端体验。

**技术亮点**:
- 多后端统一接入：支持 Ollama、OpenAI API、兼容 OpenAPI 标准的各类 LLM 服务，可灵活切换
- RAG 检索增强生成：内置文档解析和向量检索能力，支持知识库增强问答
- MCP (Model Context Protocol) 支持：实现与外部工具和服务的标准化集成
- 自托管部署：完整的前后端解决方案，支持 Docker 快速部署，保障数据隐私
- Web UI 界面：现代化响应式设计，提供对话管理、模型配置等完整功能

**适用场景**:
- 企业私有化 AI 助手：需要在内部部署 AI 对话系统以满足数据安全和合规要求的企业
- 多模型管理场景：团队或开发者需要统一管理多个 LLM 后端、对比不同模型效果的开发环境
- 知识库问答系统：基于 RAG 能力构建私有知识库的智能问答应用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,616 |
| 语言 | Python |
| Forks | 8,581 |
| Issues | 3,179 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档解析和多模态上下文构建，配合 Deep Research 和 GraphRAG 等前沿技术，为企业级知识问答和智能文档处理提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agentic Workflow 实现动态检索策略和自主决策，提升复杂查询的处理能力
- 深度文档理解：支持多种文档格式的智能解析，提取结构化信息构建高质量知识库
- GraphRAG 支持：基于知识图谱的检索增强，显著提升跨文档关联分析和复杂推理能力
- 多 LLM 统一接入：兼容 OpenAI、Ollama、DeepSeek 等多种模型，提供灵活的模型切换能力
- MCP 协议集成：支持 Model Context Protocol 标准，便于扩展和集成第三方工具生态

**适用场景**:
- 企业智能客服与知识库问答：构建支持复杂多轮对话和上下文理解的企业级问答系统，可处理技术文档、规章制度、产品手册等企业知识
- 智能文档分析与处理：自动解析合同、报告、论文等长文档，提取关键信息、生成摘要、回答专业问题，适用于法务、财务、学术研究场景
- 深度研究与分析助手：利用 Deep Research 和 GraphRAG 能力，辅助进行市场调研、竞品分析、学术文献综述等需要跨源综合分析的任务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,510 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 687 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 协作平台，拥有 74k+ stars 的高人气，支持多 Agent 协作、团队设计以及 OpenAI/Claude/DeepSeek/Gemini 等多种主流 AI 模型集成，特别适合需要构建智能 Agent 工作流的团队和个人开发者。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 协同工作，引入 Agent 作为工作交互单元的理念，实现复杂的 AI 任务分工与协作
- 多模型统一集成：一站式支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供灵活的模型切换能力
- MCP 协议支持：遵循 Model Context Protocol 标准，实现与外部工具和服务的标准化集成
- 知识库管理：内置知识库功能，支持 RAG（检索增强生成）场景，便于构建私域知识问答系统
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保证类型安全，便于维护和扩展

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部 AI 助手平台，实现客服、文档处理、数据分析等业务流程自动化
- AI Agent 团队协作：团队可以设计多个专业 Agent 组成协作团队，模拟真实工作中的分工协作场景
- 个人开发者 AI 应用开发：开发者可利用其模块化设计和多模型支持，快速构建和部署 AI 应用原型



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,482 |
| 语言 | TypeScript |
| Forks | 3,230 |
| Issues | 194 |
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
| Stars | 45,630 |
| 语言 | Java |
| Forks | 15,860 |
| Issues | 78 |
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
| Stars | 38,875 |
| 语言 | Python |
| Forks | 6,172 |
| Issues | 106 |
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
| Stars | 33,717 |
| 语言 | Python |
| Forks | 2,092 |
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
| Stars | 33,500 |
| 语言 | TypeScript |
| Forks | 3,633 |
| Issues | 279 |
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
| Stars | 32,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,453 |
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
| Stars | 32,194 |
| 语言 | Python |
| Forks | 3,635 |
| Issues | 72 |
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
| Stars | 104,028 |
| 语言 | Python |
| Forks | 15,174 |
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
| Stars | 99,852 |
| 语言 | TypeScript |
| Forks | 11,927 |
| Issues | 978 |
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
| Stars | 57,168 |
| 语言 | JavaScript |
| Forks | 6,188 |
| Issues | 310 |
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
| Stars | 73,568 |
| 语言 | Python |
| Forks | 10,067 |
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
| Stars | 51,255 |
| 语言 | TypeScript |
| Forks | 24,001 |
| Issues | 829 |
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
| Stars | 43,512 |
| 语言 | Go |
| Forks | 3,922 |
| Issues | 1,094 |
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
| Stars | 72,487 |
| 语言 | MDX |
| Forks | 7,763 |
| Issues | 254 |
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
| Stars | 129,306 |
| 语言 | Python |
| Forks | 18,303 |
| Issues | 283 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面解决方案，通过统一接口支持 Ollama、OpenAI 等多款 LLM 后端，配合 RAG 和 MCP 扩展能力，既能满足企业级隐私合规需求，又为个人开发者提供了开箱即用的 AI 前端体验。

**技术亮点**:
- 多后端统一接入：支持 Ollama、OpenAI API、兼容 OpenAPI 标准的各类 LLM 服务，可灵活切换
- RAG 检索增强生成：内置文档解析和向量检索能力，支持知识库增强问答
- MCP (Model Context Protocol) 支持：实现与外部工具和服务的标准化集成
- 自托管部署：完整的前后端解决方案，支持 Docker 快速部署，保障数据隐私
- Web UI 界面：现代化响应式设计，提供对话管理、模型配置等完整功能

**适用场景**:
- 企业私有化 AI 助手：需要在内部部署 AI 对话系统以满足数据安全和合规要求的企业
- 多模型管理场景：团队或开发者需要统一管理多个 LLM 后端、对比不同模型效果的开发环境
- 知识库问答系统：基于 RAG 能力构建私有知识库的智能问答应用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,616 |
| 语言 | Python |
| Forks | 8,581 |
| Issues | 3,179 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎之一（76k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档解析和多模态上下文构建，配合 Deep Research 和 GraphRAG 等前沿技术，为企业级知识问答和智能文档处理提供了端到端的解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agentic Workflow 实现动态检索策略和自主决策，提升复杂查询的处理能力
- 深度文档理解：支持多种文档格式的智能解析，提取结构化信息构建高质量知识库
- GraphRAG 支持：基于知识图谱的检索增强，显著提升跨文档关联分析和复杂推理能力
- 多 LLM 统一接入：兼容 OpenAI、Ollama、DeepSeek 等多种模型，提供灵活的模型切换能力
- MCP 协议集成：支持 Model Context Protocol 标准，便于扩展和集成第三方工具生态

**适用场景**:
- 企业智能客服与知识库问答：构建支持复杂多轮对话和上下文理解的企业级问答系统，可处理技术文档、规章制度、产品手册等企业知识
- 智能文档分析与处理：自动解析合同、报告、论文等长文档，提取关键信息、生成摘要、回答专业问题，适用于法务、财务、学术研究场景
- 深度研究与分析助手：利用 Deep Research 和 GraphRAG 能力，辅助进行市场调研、竞品分析、学术文献综述等需要跨源综合分析的任务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,904 |
| 语言 | JavaScript |
| Forks | 15,428 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 编码 Agent 的综合性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大核心模块显著提升 AI agent 的开发效率和能力上限，拥有 118k+ stars 的高人气，是研究 AI agent 架构和开发效率工具的绝佳参考。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 的标准化工具集成框架，支持多种 AI 编码工具生态
- 创新的 Memory 系统设计，实现长期上下文保持和跨会话信息复用
- 安全沙箱机制 (Security) 确保 AI agent 操作的安全性和可控性
- Skills & Instincts 双轨系统：Skills 提供可复用技能库，Instincts 实现本能级响应优化
- 支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的跨平台兼容

**适用场景**:
- 企业级 AI 辅助开发平台：构建内部 AI coding assistant，集成到 CI/CD 流程提升团队开发效率
- AI Agent 研究与开发：基于项目架构快速构建新的 AI agent 原型，验证 LLM 应用假设
- 个人开发者效率工具：利用现成的 Skills 和 Instincts 模块增强现有 AI 编码工具的能力
- 多 Agent 协作系统：借助 Memory 和 MCP 框架设计复杂的多 Agent 协作工作流



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,510 |
| 语言 | TypeScript |
| Forks | 14,839 |
| Issues | 687 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 协作平台，拥有 74k+ stars 的高人气，支持多 Agent 协作、团队设计以及 OpenAI/Claude/DeepSeek/Gemini 等多种主流 AI 模型集成，特别适合需要构建智能 Agent 工作流的团队和个人开发者。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 协同工作，引入 Agent 作为工作交互单元的理念，实现复杂的 AI 任务分工与协作
- 多模型统一集成：一站式支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供灵活的模型切换能力
- MCP 协议支持：遵循 Model Context Protocol 标准，实现与外部工具和服务的标准化集成
- 知识库管理：内置知识库功能，支持 RAG（检索增强生成）场景，便于构建私域知识问答系统
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保证类型安全，便于维护和扩展

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部 AI 助手平台，实现客服、文档处理、数据分析等业务流程自动化
- AI Agent 团队协作：团队可以设计多个专业 Agent 组成协作团队，模拟真实工作中的分工协作场景
- 个人开发者 AI 应用开发：开发者可利用其模块化设计和多模型支持，快速构建和部署 AI 应用原型



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,903 |
| 语言 | HTML |
| Forks | 20,332 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最大、最活跃的开源提示词社区项目，拥有超过 15 万 Stars，为 AI 爱好者和开发者提供了超过 5000+ 经过社区验证的高质量提示词模板，并支持完全私有化部署，是个人学习和企业构建 AI 应用的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，具有优秀的性能和类型安全
- 支持多 LLM 模型集成（ChatGPT、Claude、Gemini、GPT-4 等），适配性强
- 开源可自托管，支持企业私有化部署，保证数据隐私和安全
- 社区驱动的提示词收集与评分机制，确保提示词质量和实用性
- Creative Commons Zero (CC0) 完全公共领域许可证，商用无忧

**适用场景**:
- 个人开发者/AI爱好者：快速查找、学习和复用经过验证的高质量提示词，提升 AI 使用效率
- 企业应用：私有化部署提示词库，为内部团队提供统一的 AI 交互规范，保护商业隐私
- AI 应用开发者：将开源提示词库集成到自己的产品中，快速构建 AI 功能



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,553 |
| 语言 | Jupyter Notebook |
| Forks | 13,674 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是目前GitHub上最受欢迎的LLM从零实现项目（89,553 ⭐），作者Sebastian Raschka以其深厚的机器学习教学经验，将ChatGPT背后复杂的transformer架构、注意力机制、GPT训练流程拆解成清晰易懂的代码，是理论学习与工程实践结合的绝佳资源。

**技术亮点**:
- 从零实现完整LLM pipeline：包括数据预处理、tokenization、模型架构、训练循环、推理生成的端到端流程
- 深入剖析Transformer和Self-Attention机制的数学原理与代码实现，而非仅调用高层API
- 涵盖GPT的预训练（Next Token Prediction）和指令微调（Instruction Tuning）两个关键阶段
- 提供分步骤的Jupyter Notebook，代码配有详细注释，便于理解每个组件的输入输出和内部逻辑
- 完整实现Causal Attention Mask、Positional Embeddings、Layer Normalization等核心组件

**适用场景**:
- 个人开发者/研究者：系统学习LLM底层原理，理解GPT/BERT等模型的工作机制，为后续研究或应用开发打牢基础
- 企业内训/教学：作为内部培训或高校课程的实战教材，让团队/学生快速掌握大模型核心技术
- 快速原型验证：研究人员可基于此项目快速修改模型架构、实验不同训练策略，验证创新想法



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,809 |
| 语言 | TypeScript |
| Forks | 6,704 |
| Issues | 28 |
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
| Stars | 43,482 |
| 语言 | TypeScript |
| Forks | 3,230 |
| Issues | 194 |
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
| Stars | 42,658 |
| 语言 | Python |
| Forks | 9,862 |
| Issues | 349 |
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
| Stars | 35,058 |
| 语言 | TypeScript |
| Forks | 7,124 |
| Issues | 465 |
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
| Stars | 33,717 |
| 语言 | Python |
| Forks | 2,092 |
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
| Stars | 57,168 |
| 语言 | JavaScript |
| Forks | 6,188 |
| Issues | 310 |
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
| Stars | 70,218 |
| 语言 | Python |
| Forks | 8,792 |
| Issues | 343 |
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
| Stars | 44,962 |
| 语言 | TypeScript |
| Forks | 3,353 |
| Issues | 359 |
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
| Stars | 51,255 |
| 语言 | TypeScript |
| Forks | 24,001 |
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
| Stars | 35,232 |
| 语言 | HTML |
| Forks | 5,661 |
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
| Stars | 74,739 |
| 语言 | Python |
| Forks | 14,965 |
| Issues | 3,997 |
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
| Stars | 55,023 |
| 语言 | Python |
| Forks | 5,334 |
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
| Stars | 39,202 |
| 语言 | TypeScript |
| Forks | 3,983 |
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
| Stars | 146,417 |
| 语言 | Python |
| Forks | 8,672 |
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
| Stars | 166,494 |
| 语言 | Go |
| Forks | 15,233 |
| Issues | 2,755 |
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
| Stars | 72,487 |
| 语言 | MDX |
| Forks | 7,763 |
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
| Stars | 47,385 |
| 语言 | Rust |
| Forks | 9,391 |
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
| Stars | 92,888 |
| 语言 | Python |
| Forks | 5,593 |
| Issues | 497 |
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
| Stars | 36,990 |
| 语言 | Python |
| Forks | 2,585 |
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
| Stars | 69,270 |
| 语言 | Python |
| Forks | 8,438 |
| Issues | 935 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持100+开源模型的一站式微调，融合LoRA、QLoRA、RLHF等主流技术，让研究者和开发者无需从零搭建训练流水线即可快速定制专属模型，极大降低了LLM微调的工程门槛。

**技术亮点**:
- 【统一微调框架】支持100+LLMs和VLMs，包括Llama3、Qwen、Gemma、DeepSeek、ChatGLM等主流开源模型，一套代码库覆盖所有模型
- 【多范式微调支持】集成LoRA、QLoRA、Prefix-Tuning、Ptuning等多种参数高效微调方法，显著降低GPU显存占用
- 【RLHF完整实现】内置PPO、DPO、KTO等强化学习人类反馈训练算法，支持构建更高质量的对齐模型
- 【多模态融合】同时支持视觉-语言模型的微调，可用于图文理解和多模态Agent开发
- 【工程优化完善】提供分布式训练、混合精度、梯度累积等优化，支持DeepSpeed加速，开箱即用的训练监控和断点续训功能

**适用场景**:
- 【企业私有化部署】企业可基于LlamaFactory对开源基座模型进行领域适配微调（如金融、医疗、法律），构建私有化AI助手，在保证数据安全的同时实现业务定制
- 【学术研究快速验证】研究人员可快速实验不同模型架构和微调策略组合，支持新算法对比评估，已有多篇顶会论文采用
- 【个人开发者定制AI】个人开发者可低成本微调小模型实现特定任务（如聊天机器人、代码助手、文案生成），无需昂贵的云端API调用费用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,452 |
| 语言 | Python |
| Forks | 6,344 |
| Issues | 79 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，整合了股票、加密货币、期权、固定收益等多类资产的数据接口，并内置 AI 和机器学习分析能力，超过 6.4 万星标表明其在金融科技领域的领先地位和活跃的社区生态。

**技术亮点**:
- 模块化架构设计：采用高度解耦的模块化结构，支持独立安装和使用各个功能模块（如股票、加密货币、期权等），便于按需扩展和维护
- 多数据源集成：统一封装了多个主流金融数据 API，提供标准化的数据获取接口，降低了数据采集的复杂性
- AI/ML 原生支持：内置机器学习模型和 AI 代理功能，支持自然语言处理和智能投研分析
- 丰富的量化工具：提供技术指标计算、衍生品分析、固定收益分析等专业量化金融功能
- 标准化数据模型：统一的 DataFrame 格式输出，与 Python 数据科学生态（Pandas、NumPy 等）无缝衔接

**适用场景**:
- 量化交易策略开发：分析师和量化交易员可快速获取多资产市场数据，使用内置指标库进行策略回测和优化
- 智能投研与数据分析：利用 AI 功能进行财报解读、市场趋势分析和投资机会挖掘，提升研究效率
- 金融应用开发：企业和开发者可基于 OpenBB 构建投资组合管理系统、交易终端或财务分析工具



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,903 |
| 语言 | HTML |
| Forks | 20,332 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最大、最活跃的开源提示词社区项目，拥有超过 15 万 Stars，为 AI 爱好者和开发者提供了超过 5000+ 经过社区验证的高质量提示词模板，并支持完全私有化部署，是个人学习和企业构建 AI 应用的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，具有优秀的性能和类型安全
- 支持多 LLM 模型集成（ChatGPT、Claude、Gemini、GPT-4 等），适配性强
- 开源可自托管，支持企业私有化部署，保证数据隐私和安全
- 社区驱动的提示词收集与评分机制，确保提示词质量和实用性
- Creative Commons Zero (CC0) 完全公共领域许可证，商用无忧

**适用场景**:
- 个人开发者/AI爱好者：快速查找、学习和复用经过验证的高质量提示词，提升 AI 使用效率
- 企业应用：私有化部署提示词库，为内部团队提供统一的 AI 交互规范，保护商业隐私
- AI 应用开发者：将开源提示词库集成到自己的产品中，快速构建 AI 功能



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,553 |
| 语言 | Jupyter Notebook |
| Forks | 13,674 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是目前GitHub上最受欢迎的LLM从零实现项目（89,553 ⭐），作者Sebastian Raschka以其深厚的机器学习教学经验，将ChatGPT背后复杂的transformer架构、注意力机制、GPT训练流程拆解成清晰易懂的代码，是理论学习与工程实践结合的绝佳资源。

**技术亮点**:
- 从零实现完整LLM pipeline：包括数据预处理、tokenization、模型架构、训练循环、推理生成的端到端流程
- 深入剖析Transformer和Self-Attention机制的数学原理与代码实现，而非仅调用高层API
- 涵盖GPT的预训练（Next Token Prediction）和指令微调（Instruction Tuning）两个关键阶段
- 提供分步骤的Jupyter Notebook，代码配有详细注释，便于理解每个组件的输入输出和内部逻辑
- 完整实现Causal Attention Mask、Positional Embeddings、Layer Normalization等核心组件

**适用场景**:
- 个人开发者/研究者：系统学习LLM底层原理，理解GPT/BERT等模型的工作机制，为后续研究或应用开发打牢基础
- 企业内训/教学：作为内部培训或高校课程的实战教材，让团队/学生快速掌握大模型核心技术
- 快速原型验证：研究人员可基于此项目快速修改模型架构、实验不同训练策略，验证创新想法



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,500 |
| 语言 | TypeScript |
| Forks | 3,633 |
| Issues | 279 |
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
| Stars | 32,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,453 |
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
| Stars | 158,560 |
| 语言 | Python |
| Forks | 32,685 |
| Issues | 2,320 |
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
| Stars | 74,739 |
| 语言 | Python |
| Forks | 14,965 |
| Issues | 3,997 |
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
| Stars | 107,331 |
| 语言 | Python |
| Forks | 12,399 |
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
| Stars | 98,653 |
| 语言 | Python |
| Forks | 27,349 |
| Issues | 18,145 |
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
| Stars | 72,487 |
| 语言 | MDX |
| Forks | 7,763 |
| Issues | 254 |
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
| Stars | 162,036 |
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
| Stars | 118,904 |
| 语言 | JavaScript |
| Forks | 15,428 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 编码 Agent 的综合性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大核心模块显著提升 AI agent 的开发效率和能力上限，拥有 118k+ stars 的高人气，是研究 AI agent 架构和开发效率工具的绝佳参考。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 的标准化工具集成框架，支持多种 AI 编码工具生态
- 创新的 Memory 系统设计，实现长期上下文保持和跨会话信息复用
- 安全沙箱机制 (Security) 确保 AI agent 操作的安全性和可控性
- Skills & Instincts 双轨系统：Skills 提供可复用技能库，Instincts 实现本能级响应优化
- 支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的跨平台兼容

**适用场景**:
- 企业级 AI 辅助开发平台：构建内部 AI coding assistant，集成到 CI/CD 流程提升团队开发效率
- AI Agent 研究与开发：基于项目架构快速构建新的 AI agent 原型，验证 LLM 应用假设
- 个人开发者效率工具：利用现成的 Skills 和 Instincts 模块增强现有 AI 编码工具的能力
- 多 Agent 协作系统：借助 Memory 和 MCP 框架设计复杂的多 Agent 协作工作流



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,598 |
| 语言 | Go |
| Forks | 3,822 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型的本地运行，无需 GPU 即可部署，特别适合需要在本地环境或边缘设备上运行 AI 能力的开发者和企业。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和低内存占用优势，支持并发处理多模型请求
- 支持多种模型类型：LLM（Mamba、Llama）、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成（MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在多节点间协同运行
- 提供标准 API 接口，兼容 OpenAI API 格式，便于现有应用快速迁移集成
- 无 GPU 依赖设计，支持在 CPU 和各类硬件上运行，降低部署门槛和成本

**适用场景**:
- 本地/私有化 AI 部署：对数据隐私有严格要求的企业，可在本地服务器运行 AI 模型，避免数据外传
- 边缘计算场景：在没有强大 GPU 支持的边缘设备上部署 AI 能力，如 IoT 设备、嵌入式系统
- 开发测试环境：开发者可在本地机器上快速测试 AI 应用，无需依赖云服务 API



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,218 |
| 语言 | Python |
| Forks | 8,792 |
| Issues | 343 |
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
| Stars | 44,962 |
| 语言 | TypeScript |
| Forks | 3,353 |
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
| Stars | 181,749 |
| 语言 | TypeScript |
| Forks | 56,322 |
| Issues | 1,428 |
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
| Stars | 153,994 |
| 语言 | Python |
| Forks | 12,507 |
| Issues | 2,426 |
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
| Stars | 96,687 |
| 语言 | Python |
| Forks | 8,964 |
| Issues | 171 |
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
| Stars | 183,197 |
| 语言 | TypeScript |
| Forks | 38,845 |
| Issues | 15,718 |
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
| Stars | 93,973 |
| 语言 | TypeScript |
| Forks | 9,407 |
| Issues | 297 |
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
| Stars | 78,706 |
| 语言 | TypeScript |
| Forks | 5,745 |
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
| Stars | 76,902 |
| 语言 | TypeScript |
| Forks | 6,571 |
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
| Stars | 75,668 |
| 语言 | JavaScript |
| Forks | 7,276 |
| Issues | 711 |
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
| Stars | 79,100 |
| 语言 | Go |
| Forks | 2,743 |
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
| Stars | 75,278 |
| 语言 | Go |
| Forks | 2,655 |
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
| Stars | 36,990 |
| 语言 | Python |
| Forks | 2,585 |
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
| Stars | 54,773 |
| 语言 | JavaScript |
| Forks | 4,069 |
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
| Stars | 417,526 |
| 语言 | Python |
| Forks | 45,344 |
| Issues | 1,165 |
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
| Stars | 44,962 |
| 语言 | TypeScript |
| Forks | 3,353 |
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
| Stars | 181,749 |
| 语言 | TypeScript |
| Forks | 56,322 |
| Issues | 1,428 |
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
| Stars | 51,669 |
| 语言 | Go |
| Forks | 10,339 |
| Issues | 214 |
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
| Stars | 121,401 |
| 语言 | Go |
| Forks | 42,756 |
| Issues | 2,658 |
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
| Stars | 71,554 |
| 语言 | Go |
| Forks | 18,912 |
| Issues | 3,797 |
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
| Stars | 54,605 |
| 语言 | Go |
| Forks | 6,512 |
| Issues | 2,863 |
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
| Stars | 47,578 |
| 语言 | Go |
| Forks | 5,062 |
| Issues | 971 |
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
| Stars | 93,973 |
| 语言 | TypeScript |
| Forks | 9,407 |
| Issues | 297 |
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
| Stars | 75,953 |
| 语言 | TypeScript |
| Forks | 6,470 |
| Issues | 445 |
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
| Stars | 84,654 |
| 语言 | JavaScript |
| Forks | 7,580 |
| Issues | 713 |
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
| Stars | 69,631 |
| 语言 | Go |
| Forks | 1,895 |
| Issues | 311 |
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
| Stars | 62,406 |
| 语言 | Go |
| Forks | 5,895 |
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
| Stars | 58,393 |
| 语言 | Go |
| Forks | 4,228 |
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
| Stars | 84,654 |
| 语言 | JavaScript |
| Forks | 7,580 |
| Issues | 713 |
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
| Stars | 63,314 |
| 语言 | Go |
| Forks | 10,288 |
| Issues | 772 |
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
| Stars | 44,598 |
| 语言 | Go |
| Forks | 3,822 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型的本地运行，无需 GPU 即可部署，特别适合需要在本地环境或边缘设备上运行 AI 能力的开发者和企业。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和低内存占用优势，支持并发处理多模型请求
- 支持多种模型类型：LLM（Mamba、Llama）、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成（MusicGen）、目标检测等
- 去中心化架构设计，支持 libp2p 分布式网络，可在多节点间协同运行
- 提供标准 API 接口，兼容 OpenAI API 格式，便于现有应用快速迁移集成
- 无 GPU 依赖设计，支持在 CPU 和各类硬件上运行，降低部署门槛和成本

**适用场景**:
- 本地/私有化 AI 部署：对数据隐私有严格要求的企业，可在本地服务器运行 AI 模型，避免数据外传
- 边缘计算场景：在没有强大 GPU 支持的边缘设备上部署 AI 能力，如 IoT 设备、嵌入式系统
- 开发测试环境：开发者可在本地机器上快速测试 AI 应用，无需依赖云服务 API



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,687 |
| 语言 | Python |
| Forks | 8,964 |
| Issues | 171 |
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
| Stars | 87,123 |
| 语言 | Python |
| Forks | 33,810 |
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
| Stars | 100,100 |
| 语言 | TypeScript |
| Forks | 27,151 |
| Issues | 1,117 |
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
| Stars | 78,706 |
| 语言 | TypeScript |
| Forks | 5,745 |
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
| Stars | 75,668 |
| 语言 | JavaScript |
| Forks | 7,276 |
| Issues | 711 |
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
| Stars | 55,953 |
| 语言 | JavaScript |
| Forks | 10,212 |
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
| Stars | 51,739 |
| 语言 | JavaScript |
| Forks | 4,695 |
| Issues | 1,468 |
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
| Stars | 88,302 |
| 语言 | Go |
| Forks | 8,573 |
| Issues | 661 |
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
| Stars | 71,180 |
| 语言 | Go |
| Forks | 4,691 |
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
| Stars | 57,242 |
| 语言 | Go |
| Forks | 3,235 |
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
| Stars | 36,990 |
| 语言 | Python |
| Forks | 2,585 |
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
| Stars | 417,526 |
| 语言 | Python |
| Forks | 45,344 |
| Issues | 1,165 |
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
| Stars | 68,884 |
| 语言 | JavaScript |
| Forks | 22,964 |
| Issues | 200 |
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
| Stars | 99,852 |
| 语言 | TypeScript |
| Forks | 11,927 |
| Issues | 978 |
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
| Stars | 57,168 |
| 语言 | JavaScript |
| Forks | 6,188 |
| Issues | 310 |
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
| Stars | 43,512 |
| 语言 | Go |
| Forks | 3,922 |
| Issues | 1,094 |
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
| Stars | 51,669 |
| 语言 | Go |
| Forks | 10,339 |
| Issues | 214 |
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
| Stars | 154,903 |
| 语言 | HTML |
| Forks | 20,332 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是目前最大、最活跃的开源提示词社区项目，拥有超过 15 万 Stars，为 AI 爱好者和开发者提供了超过 5000+ 经过社区验证的高质量提示词模板，并支持完全私有化部署，是个人学习和企业构建 AI 应用的最佳资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，具有优秀的性能和类型安全
- 支持多 LLM 模型集成（ChatGPT、Claude、Gemini、GPT-4 等），适配性强
- 开源可自托管，支持企业私有化部署，保证数据隐私和安全
- 社区驱动的提示词收集与评分机制，确保提示词质量和实用性
- Creative Commons Zero (CC0) 完全公共领域许可证，商用无忧

**适用场景**:
- 个人开发者/AI爱好者：快速查找、学习和复用经过验证的高质量提示词，提升 AI 使用效率
- 企业应用：私有化部署提示词库，为内部团队提供统一的 AI 交互规范，保护商业隐私
- AI 应用开发者：将开源提示词库集成到自己的产品中，快速构建 AI 功能



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,809 |
| 语言 | TypeScript |
| Forks | 6,704 |
| Issues | 28 |
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
| Stars | 32,194 |
| 语言 | Python |
| Forks | 3,635 |
| Issues | 72 |
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
| Stars | 35,232 |
| 语言 | HTML |
| Forks | 5,661 |
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
| Stars | 72,487 |
| 语言 | MDX |
| Forks | 7,763 |
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
| Stars | 89,574 |
| 语言 | TypeScript |
| Forks | 9,967 |
| Issues | 2,212 |
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
| Stars | 86,990 |
| 语言 | TypeScript |
| Forks | 8,795 |
| Issues | 1,638 |
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
| Stars | 127,281 |
| 语言 | JavaScript |
| Forks | 12,468 |
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
| Stars | 168,658 |
| 语言 | Go |
| Forks | 13,093 |
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
| Stars | 133,733 |
| 语言 | Unknown |
| Forks | 33,697 |
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
| Stars | 66,449 |
| 语言 | Shell |
| Forks | 10,036 |
| Issues | 91 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,925 |
| 语言 | Python |
| Forks | 6,419 |
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
| Stars | 86,210 |
| 语言 | Python |
| Forks | 12,526 |
| Issues | 111 |
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
| Stars | 83,765 |
| 语言 | Python |
| Forks | 7,164 |
| Issues | 643 |
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
| Stars | 384,719 |
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
| Stars | 114,037 |
| 语言 | TypeScript |
| Forks | 5,835 |
| Issues | 313 |
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
| Stars | 106,438 |
| 语言 | TypeScript |
| Forks | 7,720 |
| Issues | 211 |
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
| Stars | 48,006 |
| 语言 | Go |
| Forks | 10,256 |
| Issues | 1,892 |
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
| Stars | 100,093 |
| 语言 | C++ |
| Forks | 16,040 |
| Issues | 1,305 |
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
| Stars | 63,139 |
| 语言 | Python |
| Forks | 1,628 |
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
| Stars | 57,442 |
| 语言 | TypeScript |
| Forks | 7,501 |
| Issues | 297 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,277 |
| 语言 | JavaScript |
| Forks | 3,645 |
| Issues | 92 |
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
| Stars | 289,769 |
| 语言 | Python |
| Forks | 27,525 |
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
| Stars | 219,137 |
| 语言 | Python |
| Forks | 50,278 |
| Issues | 909 |
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
| Stars | 96,895 |
| 语言 | Python |
| Forks | 11,945 |
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
| Stars | 85,891 |
| 语言 | Python |
| Forks | 37,117 |
| Issues | 3,487 |
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
| Stars | 85,644 |
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
| Stars | 77,680 |
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
| Stars | 439,615 |
| 语言 | TypeScript |
| Forks | 43,883 |
| Issues | 221 |
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
| Stars | 351,875 |
| 语言 | TypeScript |
| Forks | 43,867 |
| Issues | 4 |
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
| Stars | 119,856 |
| 语言 | TypeScript |
| Forks | 13,049 |
| Issues | 2,914 |
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
| Stars | 111,068 |
| 语言 | TypeScript |
| Forks | 8,361 |
| Issues | 1,791 |
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
| Stars | 108,356 |
| 语言 | TypeScript |
| Forks | 13,313 |
| Issues | 5,002 |
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
| Stars | 97,749 |
| 语言 | TypeScript |
| Forks | 54,574 |
| Issues | 1,357 |
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
| Stars | 95,986 |
| 语言 | TypeScript |
| Forks | 5,217 |
| Issues | 679 |
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
| Stars | 94,222 |
| 语言 | TypeScript |
| Forks | 5,144 |
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
| Stars | 83,041 |
| 语言 | TypeScript |
| Forks | 7,576 |
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
| Stars | 82,528 |
| 语言 | TypeScript |
| Forks | 10,130 |
| Issues | 622 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,442 |
| 语言 | TypeScript |
| Forks | 7,968 |
| Issues | 685 |
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
| Stars | 244,256 |
| 语言 | JavaScript |
| Forks | 50,864 |
| Issues | 1,190 |
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
| Stars | 116,467 |
| 语言 | JavaScript |
| Forks | 35,217 |
| Issues | 2,593 |
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
| Stars | 111,666 |
| 语言 | JavaScript |
| Forks | 36,320 |
| Issues | 572 |
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
| Stars | 108,633 |
| 语言 | JavaScript |
| Forks | 11,572 |
| Issues | 354 |
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
| Forks | 32,697 |
| Issues | 1,706 |
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
| Stars | 95,482 |
| 语言 | JavaScript |
| Forks | 15,317 |
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
| Stars | 86,138 |
| 语言 | JavaScript |
| Forks | 4,837 |
| Issues | 975 |
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
| Stars | 70,890 |
| 语言 | JavaScript |
| Forks | 16,812 |
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
| Stars | 66,299 |
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
| Stars | 65,957 |
| 语言 | JavaScript |
| Forks | 9,372 |
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
| Stars | 62,411 |
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
| Stars | 61,529 |
| 语言 | JavaScript |
| Forks | 7,124 |
| Issues | 137 |
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
| Stars | 60,109 |
| 语言 | JavaScript |
| Forks | 5,635 |
| Issues | 65 |
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
| Stars | 59,860 |
| 语言 | JavaScript |
| Forks | 20,466 |
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
| Stars | 57,414 |
| 语言 | JavaScript |
| Forks | 12,300 |
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
| Stars | 53,055 |
| 语言 | JavaScript |
| Forks | 10,601 |
| Issues | 467 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,245 |
| 语言 | JavaScript |
| Forks | 11,407 |
| Issues | 362 |
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
| Stars | 133,204 |
| 语言 | Go |
| Forks | 18,886 |
| Issues | 9,920 |
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
| Stars | 105,656 |
| 语言 | Go |
| Forks | 14,971 |
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
| Stars | 87,348 |
| 语言 | Go |
| Forks | 8,230 |
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
| Stars | 81,263 |
| 语言 | Go |
| Forks | 4,978 |
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
| Stars | 68,661 |
| 语言 | Go |
| Forks | 3,229 |
| Issues | 5 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,372 |
| 语言 | Go |
| Forks | 5,003 |
| Issues | 1,165 |
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
| Stars | 50,963 |
| 语言 | Go |
| Forks | 21,885 |
| Issues | 386 |
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
| Forks | 7,964 |
| Issues | 559 |
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
| Stars | 148,037 |
| 语言 | Python |
| Forks | 11,268 |
| Issues | 314 |
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
| Stars | 340,698 |
| 语言 | Python |
| Forks | 55,117 |
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
| Stars | 76,462 |
| 语言 | Python |
| Forks | 16,802 |
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
| Stars | 138,448 |
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
| Forks | 31,867 |
| Issues | 266 |
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
| Stars | 67,318 |
| 语言 | JavaScript |
| Forks | 11,974 |
| Issues | 542 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
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
| Forks | 2,425 |
| Issues | 1,199 |
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
| Stars | 50,452 |
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
| Stars | 46,959 |
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
| Stars | 45,723 |
| 语言 | Go |
| Forks | 3,776 |
| Issues | 83 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
