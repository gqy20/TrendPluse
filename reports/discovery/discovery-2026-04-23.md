# 项目发现报告 (2026-04-23)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
| 去重移除 | 34 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 16 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 9 |
| 🛠️ 开发工具 | 15 |
| ⚙️ DevOps/基础设施 | 14 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
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


## 🤖 AI Agents (30 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,673 |
| 语言 | Python |
| Forks | 18,964 |
| Issues | 312 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI 等多种后端，提供了开箱即用的 RAG 能力和完全自托管部署选项，特别适合需要快速搭建私有 AI 界面的企业和个人开发者，无需复杂配置即可获得生产级别的用户体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，提供统一的交互接口
- RAG 能力：内置检索增强生成功能，支持文档导入和上下文增强，提升回答质量
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业对数据安全的要求
- 现代化 Web 界面：响应式设计，支持实时流式输出、多会话管理、代码高亮等专业功能
- 可扩展架构：支持 MCP (Model Context Protocol) 扩展，可自定义工具和集成第三方服务

**适用场景**:
- 企业私有 AI 助手：需要部署内部 AI 知识库问答系统，对接内部文档和业务流程，保证数据隐私
- 开发者快速原型：使用 Ollama 本地模型快速搭建 AI 应用原型，支持多模型切换对比测试
- 个人 AI 工作站：聚合多个 LLM 服务，通过统一界面管理日常编码、写作、分析等任务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,922 |
| 语言 | Python |
| Forks | 16,437 |
| Issues | 6,500 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是 NousResearch 团队打造的模块化 AI Agent 框架，支持 Claude Code、ChatGPT 等多模型接入，拥有超过 11 万 Stars 的活跃社区，适合构建企业级智能助手和自动化工作流。

**技术亮点**:
- 多模型统一抽象层，支持 Anthropic Claude、OpenAI GPT 等主流 LLM 的无缝切换
- 基于 ReAct/ReAct-LangChain 架构的自主推理与工具调用能力
- 模块化 Tool System，支持自定义工具扩展和第三方集成
- 支持 Code Execution 和文件操作，实现端到端的代码自动化
- MIT 许可证开源，商业友好且社区生态成熟

**适用场景**:
- 企业智能助手：构建客服、文档问答、数据分析等自动化业务流程
- 开发者工具链：集成到 IDE 实现代码审查、Bug 修复、测试生成等 Coding Agent 场景
- 个人生产力提升：邮件处理、日程管理、信息检索等日常任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,845 |
| 语言 | Python |
| Forks | 8,912 |
| Issues | 2,987 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（78k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档理解、多跳推理和 GraphRAG 等高级特性，为企业级 LLM 应用提供生产级的上下文检索能力。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态检索策略规划和多步推理，大幅提升复杂查询的准确性
- 深度文档理解：支持 PDF、Word、Excel 等多种格式的语义切片，保留文档结构和层级关系
- GraphRAG 原生支持：基于知识图谱的检索增强，能够捕捉实体间的复杂关系，提升摘要和问答质量
- 支持多种 LLM 后端：兼容 OpenAI、DeepSeek、Ollama 等主流模型，灵活适配不同场景需求
- MCP (Model Context Protocol) 集成：支持与外部工具和服务无缝连接，构建更强大的 AI 工作流

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，实现精准的文档检索和智能问答，适合法务、医疗、金融等专业知识密集型行业
- Agentic Workflow 自动化：利用 Agent 能力构建复杂的多步任务自动化流程，如研究助理、数据分析报告生成等场景
- Deep Research 深度研究：支持多源文档的跨文档推理和综合分析，适合学术研究、市场调研等需要深度上下文理解的场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 165,177 |
| 语言 | JavaScript |
| Forks | 25,640 |
| Issues | 156 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手设计的性能优化系统，通过 Skills、Instincts、Memory 等机制显著增强 Claude Code 等工具的智能化水平，特别适合追求高效、安全 AI 辅助开发的团队。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，支持与多种 AI agent 无缝协作
- 模块化 Skills 系统，允许自定义扩展 agent 能力
- Instincts 本能机制，实现自动化的最佳实践执行
- Memory 持久化记忆系统，保持跨会话的上下文连贯性
- Security 安全沙箱机制，保障代码执行环境隔离

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该系统构建统一的 AI 开发规范和安全策略
- 安全敏感项目开发：利用安全沙箱机制在可控环境中运行 AI 生成的代码
- 个人开发者效率提升：通过 Skills 和 Memory 定制个性化的 AI 编程助手工作流



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,744 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在消费级硬件上运行多种 AI 模型（LLM、图像生成、语音合成等），无需依赖云服务或 GPU，为开发者和企业提供了完全可控、私有化的 AI 部署解决方案，特别适合对数据隐私和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种任务，通过统一 API 调用
- 去中心化分布式架构：集成 libp2p 支持 P2P 网络通信，支持分布式部署和去中心化推理，可构建本地 AI 集群
- 无 GPU 依赖设计：针对 CPU 推理优化，可在普通消费级硬件上运行，降低 AI 应用部署门槛
- API 优先架构：提供 OpenAI 兼容的 REST API，支持 MCP 协议，便于集成到现有系统和应用
- Go 语言高性能实现：利用 Go 的并发优势实现高效的模型推理和资源调度

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地运行 AI 服务，处理敏感数据（如医疗、金融、法律文档），避免数据上传到第三方云服务
- 边缘计算与物联网：在边缘设备（如树莓派、工控机）上部署轻量级 AI 推理能力，支持智能监控、语音交互等场景
- 开发与测试环境：开发者在本地构建和测试 AI 应用原型，无需付费订阅云 API，降低开发成本并提高迭代效率



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,536 |
| 语言 | TypeScript |
| Forks | 14,969 |
| Issues | 717 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是下一代 AI Agent 开发平台，支持多智能体协作和 Agent 团队设计，拥有 75k+ Stars 的活跃社区。预置集成 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 提供商，并支持 MCP 协议，适合快速构建生产级 AI Agent 应用。

**技术亮点**:
- 多智能体协作框架：支持 Agent 间的高效通信与任务协调，实现复杂工作流的自动化
- 多 AI 提供商集成：开箱即用支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流模型
- MCP (Model Context Protocol) 支持：标准化的 AI 模型上下文管理协议，便于扩展和集成
- TypeScript 完整类型支持：提供完整的类型定义和 IDE 智能提示，提升开发体验和代码质量
- 知识库与 RAG 功能：内置向量存储和检索增强生成能力，支持构建知识型 Agent

**适用场景**:
- 企业级 AI Agent 应用开发：构建智能客服、数据分析、内容生成等多业务场景的 AI 助手
- 多智能体协作系统：设计和部署多个 Agent 协同工作的复杂工作流，如项目管理、代码审查等
- 个人 AI 助手搭建：基于知识库功能构建个人知识管理、任务规划、日程管理等私人 AI 助理



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,524 |
| 语言 | Python |
| Forks | 8,616 |
| Issues | 987 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 顶会认证的统一微调框架，支持 100+ 主流 LLM 和 VLM 模型，集成 LoRA/QLoRA/RLHF 等多种微调技术，70k+ Stars 证明其成熟度和社区认可度，是企业和研究者进行大模型定制的高效解决方案。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流架构
- 集成 PEFT 库支持 LoRA、QLoRA 等高效参数微调技术，大幅降低显存占用
- 支持量化技术（INT4/INT8）和 MoE 混合专家模型架构
- 支持 RLHF（人类反馈强化学习）训练范式，包括 DPO/KTO 等对齐算法
- 提供 WebUI、CLI、Python API 三种交互方式，开箱即用

**适用场景**:
- 企业场景：使用私有数据快速微调垂直领域大模型（如金融、医疗、法律），打造专属 AI 应用
- 个人开发者/研究者：低成本实验多种微调技术，比较不同模型在特定任务上的表现
- 多模态应用开发：利用 VLM 微调能力开发视觉问答、图像理解等应用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,381 |
| 语言 | TypeScript |
| Forks | 5,621 |
| Issues | 143 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个解决 AI 编程助手长期记忆缺失痛点的插件，通过自动捕获、压缩和检索编码上下文，让 Claude Code 能够跨越会话记住之前的操作和决策，实现真正的长期 AI 辅助编程体验。该项目拥有 66k+ Stars 的社区认可度，证明其在实际开发中的巨大价值。

**技术亮点**:
- Claude Agent SDK 深度集成：利用官方 Claude SDK 实现与 Claude 的无缝对接，确保记忆捕获和注入的准确性和可靠性
- RAG + 向量检索架构：采用 ChromaDB 等向量数据库和嵌入模型进行语义检索，支持基于语义相似度召回历史上下文
- AI 驱动的记忆压缩：使用 Claude 本身对捕获的编码活动进行智能压缩，在保留关键信息的同时最小化记忆体积
- SQLite 本地持久化存储：使用 SQLite 作为本地数据库，确保记忆数据的安全性和隐私性，所有数据存储在本地
- 多层次记忆系统：结合 mem0/openmemory 等成熟记忆引擎理念，支持长期记忆和短期会话记忆的分层管理

**适用场景**:
- 长期复杂项目开发：如大型代码库维护、企业级应用开发，需要 AI 记住数周甚至数月前的架构决策和技术债务
- 个人开发者知识积累：构建个人专属的 AI 编程知识库，让 AI 逐渐学习开发者的编码风格、偏好和项目规范
- 跨会话问题追溯：当代码出现 regression 或需要理解历史变更时，AI 可快速检索相关上下文进行问题定位



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,636 |
| 语言 | HTML |
| Forks | 4,691 |
| Issues | 8 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,663 |
| 语言 | Python |
| Forks | 9,981 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,954 |
| 语言 | Java |
| Forks | 15,942 |
| Issues | 14 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,063 |
| 语言 | Python |
| Forks | 4,797 |
| Issues | 97 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,040 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 65 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 111,804 |
| 语言 | TypeScript |
| Forks | 7,125 |
| Issues | 291 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,848 |
| 语言 | JavaScript |
| Forks | 6,357 |
| Issues | 330 |
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
| Stars | 71,926 |
| 语言 | Python |
| Forks | 9,061 |
| Issues | 412 |
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
| Stars | 53,706 |
| 语言 | TypeScript |
| Forks | 4,346 |
| Issues | 617 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,168 |
| 语言 | Python |
| Forks | 15,750 |
| Issues | 3 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,751 |
| 语言 | Python |
| Forks | 10,255 |
| Issues | 232 |
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
| Stars | 52,207 |
| 语言 | TypeScript |
| Forks | 24,208 |
| Issues | 821 |
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
| Stars | 185,315 |
| 语言 | TypeScript |
| Forks | 57,066 |
| Issues | 1,556 |
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
| Stars | 155,180 |
| 语言 | Java |
| Forks | 46,148 |
| Issues | 64 |
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
| Stars | 147,303 |
| 语言 | Python |
| Forks | 8,841 |
| Issues | 954 |
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
| Stars | 58,703 |
| 语言 | Jupyter Notebook |
| Forks | 20,025 |
| Issues | 5 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,881 |
| 语言 | Python |
| Forks | 5,995 |
| Issues | 548 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,965 |
| 语言 | TypeScript |
| Forks | 9,214 |
| Issues | 106 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,218 |
| 语言 | Python |
| Forks | 2,167 |
| Issues | 99 |
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
| Stars | 33,928 |
| 语言 | TypeScript |
| Forks | 3,678 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,929 |
| 语言 | TypeScript |
| Forks | 3,718 |
| Issues | 482 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,820 |
| 语言 | Rust |
| Forks | 3,194 |
| Issues | 540 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (16 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,673 |
| 语言 | Python |
| Forks | 18,964 |
| Issues | 312 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI 等多种后端，提供了开箱即用的 RAG 能力和完全自托管部署选项，特别适合需要快速搭建私有 AI 界面的企业和个人开发者，无需复杂配置即可获得生产级别的用户体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，提供统一的交互接口
- RAG 能力：内置检索增强生成功能，支持文档导入和上下文增强，提升回答质量
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业对数据安全的要求
- 现代化 Web 界面：响应式设计，支持实时流式输出、多会话管理、代码高亮等专业功能
- 可扩展架构：支持 MCP (Model Context Protocol) 扩展，可自定义工具和集成第三方服务

**适用场景**:
- 企业私有 AI 助手：需要部署内部 AI 知识库问答系统，对接内部文档和业务流程，保证数据隐私
- 开发者快速原型：使用 Ollama 本地模型快速搭建 AI 应用原型，支持多模型切换对比测试
- 个人 AI 工作站：聚合多个 LLM 服务，通过统一界面管理日常编码、写作、分析等任务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,845 |
| 语言 | Python |
| Forks | 8,912 |
| Issues | 2,987 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（78k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档理解、多跳推理和 GraphRAG 等高级特性，为企业级 LLM 应用提供生产级的上下文检索能力。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态检索策略规划和多步推理，大幅提升复杂查询的准确性
- 深度文档理解：支持 PDF、Word、Excel 等多种格式的语义切片，保留文档结构和层级关系
- GraphRAG 原生支持：基于知识图谱的检索增强，能够捕捉实体间的复杂关系，提升摘要和问答质量
- 支持多种 LLM 后端：兼容 OpenAI、DeepSeek、Ollama 等主流模型，灵活适配不同场景需求
- MCP (Model Context Protocol) 集成：支持与外部工具和服务无缝连接，构建更强大的 AI 工作流

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，实现精准的文档检索和智能问答，适合法务、医疗、金融等专业知识密集型行业
- Agentic Workflow 自动化：利用 Agent 能力构建复杂的多步任务自动化流程，如研究助理、数据分析报告生成等场景
- Deep Research 深度研究：支持多源文档的跨文档推理和综合分析，适合学术研究、市场调研等需要深度上下文理解的场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,536 |
| 语言 | TypeScript |
| Forks | 14,969 |
| Issues | 717 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是下一代 AI Agent 开发平台，支持多智能体协作和 Agent 团队设计，拥有 75k+ Stars 的活跃社区。预置集成 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 提供商，并支持 MCP 协议，适合快速构建生产级 AI Agent 应用。

**技术亮点**:
- 多智能体协作框架：支持 Agent 间的高效通信与任务协调，实现复杂工作流的自动化
- 多 AI 提供商集成：开箱即用支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流模型
- MCP (Model Context Protocol) 支持：标准化的 AI 模型上下文管理协议，便于扩展和集成
- TypeScript 完整类型支持：提供完整的类型定义和 IDE 智能提示，提升开发体验和代码质量
- 知识库与 RAG 功能：内置向量存储和检索增强生成能力，支持构建知识型 Agent

**适用场景**:
- 企业级 AI Agent 应用开发：构建智能客服、数据分析、内容生成等多业务场景的 AI 助手
- 多智能体协作系统：设计和部署多个 Agent 协同工作的复杂工作流，如项目管理、代码审查等
- 个人 AI 助手搭建：基于知识库功能构建个人知识管理、任务规划、日程管理等私人 AI 助理



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,381 |
| 语言 | TypeScript |
| Forks | 5,621 |
| Issues | 143 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个解决 AI 编程助手长期记忆缺失痛点的插件，通过自动捕获、压缩和检索编码上下文，让 Claude Code 能够跨越会话记住之前的操作和决策，实现真正的长期 AI 辅助编程体验。该项目拥有 66k+ Stars 的社区认可度，证明其在实际开发中的巨大价值。

**技术亮点**:
- Claude Agent SDK 深度集成：利用官方 Claude SDK 实现与 Claude 的无缝对接，确保记忆捕获和注入的准确性和可靠性
- RAG + 向量检索架构：采用 ChromaDB 等向量数据库和嵌入模型进行语义检索，支持基于语义相似度召回历史上下文
- AI 驱动的记忆压缩：使用 Claude 本身对捕获的编码活动进行智能压缩，在保留关键信息的同时最小化记忆体积
- SQLite 本地持久化存储：使用 SQLite 作为本地数据库，确保记忆数据的安全性和隐私性，所有数据存储在本地
- 多层次记忆系统：结合 mem0/openmemory 等成熟记忆引擎理念，支持长期记忆和短期会话记忆的分层管理

**适用场景**:
- 长期复杂项目开发：如大型代码库维护、企业级应用开发，需要 AI 记住数周甚至数月前的架构决策和技术债务
- 个人开发者知识积累：构建个人专属的 AI 编程知识库，让 AI 逐渐学习开发者的编码风格、偏好和项目规范
- 跨会话问题追溯：当代码出现 regression 或需要理解历史变更时，AI 可快速检索相关上下文进行问题定位



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,954 |
| 语言 | Java |
| Forks | 15,942 |
| Issues | 14 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,063 |
| 语言 | Python |
| Forks | 4,797 |
| Issues | 97 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,040 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 65 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,315 |
| 语言 | TypeScript |
| Forks | 12,159 |
| Issues | 956 |
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
| Stars | 58,848 |
| 语言 | JavaScript |
| Forks | 6,357 |
| Issues | 330 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,168 |
| 语言 | Python |
| Forks | 15,750 |
| Issues | 3 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,357 |
| 语言 | Python |
| Forks | 10,298 |
| Issues | 237 |
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
| Stars | 52,207 |
| 语言 | TypeScript |
| Forks | 24,208 |
| Issues | 821 |
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
| Stars | 43,936 |
| 语言 | Go |
| Forks | 3,972 |
| Issues | 1,135 |
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
| Stars | 34,145 |
| 语言 | Python |
| Forks | 4,829 |
| Issues | 217 |
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
| Stars | 34,218 |
| 语言 | Python |
| Forks | 2,167 |
| Issues | 99 |
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
| Stars | 33,928 |
| 语言 | TypeScript |
| Forks | 3,678 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
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
| Stars | 133,673 |
| 语言 | Python |
| Forks | 18,964 |
| Issues | 312 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI 等多种后端，提供了开箱即用的 RAG 能力和完全自托管部署选项，特别适合需要快速搭建私有 AI 界面的企业和个人开发者，无需复杂配置即可获得生产级别的用户体验。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 等多种 LLM 服务，提供统一的交互接口
- RAG 能力：内置检索增强生成功能，支持文档导入和上下文增强，提升回答质量
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业对数据安全的要求
- 现代化 Web 界面：响应式设计，支持实时流式输出、多会话管理、代码高亮等专业功能
- 可扩展架构：支持 MCP (Model Context Protocol) 扩展，可自定义工具和集成第三方服务

**适用场景**:
- 企业私有 AI 助手：需要部署内部 AI 知识库问答系统，对接内部文档和业务流程，保证数据隐私
- 开发者快速原型：使用 Ollama 本地模型快速搭建 AI 应用原型，支持多模型切换对比测试
- 个人 AI 工作站：聚合多个 LLM 服务，通过统一界面管理日常编码、写作、分析等任务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,922 |
| 语言 | Python |
| Forks | 16,437 |
| Issues | 6,500 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是 NousResearch 团队打造的模块化 AI Agent 框架，支持 Claude Code、ChatGPT 等多模型接入，拥有超过 11 万 Stars 的活跃社区，适合构建企业级智能助手和自动化工作流。

**技术亮点**:
- 多模型统一抽象层，支持 Anthropic Claude、OpenAI GPT 等主流 LLM 的无缝切换
- 基于 ReAct/ReAct-LangChain 架构的自主推理与工具调用能力
- 模块化 Tool System，支持自定义工具扩展和第三方集成
- 支持 Code Execution 和文件操作，实现端到端的代码自动化
- MIT 许可证开源，商业友好且社区生态成熟

**适用场景**:
- 企业智能助手：构建客服、文档问答、数据分析等自动化业务流程
- 开发者工具链：集成到 IDE 实现代码审查、Bug 修复、测试生成等 Coding Agent 场景
- 个人生产力提升：邮件处理、日程管理、信息检索等日常任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,845 |
| 语言 | Python |
| Forks | 8,912 |
| Issues | 2,987 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（78k+ stars），它创新性地将 RAG 与 Agent 能力深度融合，支持复杂文档理解、多跳推理和 GraphRAG 等高级特性，为企业级 LLM 应用提供生产级的上下文检索能力。

**技术亮点**:
- RAG + Agent 双引擎架构：通过 Agent 能力实现动态检索策略规划和多步推理，大幅提升复杂查询的准确性
- 深度文档理解：支持 PDF、Word、Excel 等多种格式的语义切片，保留文档结构和层级关系
- GraphRAG 原生支持：基于知识图谱的检索增强，能够捕捉实体间的复杂关系，提升摘要和问答质量
- 支持多种 LLM 后端：兼容 OpenAI、DeepSeek、Ollama 等主流模型，灵活适配不同场景需求
- MCP (Model Context Protocol) 集成：支持与外部工具和服务无缝连接，构建更强大的 AI 工作流

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，实现精准的文档检索和智能问答，适合法务、医疗、金融等专业知识密集型行业
- Agentic Workflow 自动化：利用 Agent 能力构建复杂的多步任务自动化流程，如研究助理、数据分析报告生成等场景
- Deep Research 深度研究：支持多源文档的跨文档推理和综合分析，适合学术研究、市场调研等需要深度上下文理解的场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 165,177 |
| 语言 | JavaScript |
| Forks | 25,640 |
| Issues | 156 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手设计的性能优化系统，通过 Skills、Instincts、Memory 等机制显著增强 Claude Code 等工具的智能化水平，特别适合追求高效、安全 AI 辅助开发的团队。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，支持与多种 AI agent 无缝协作
- 模块化 Skills 系统，允许自定义扩展 agent 能力
- Instincts 本能机制，实现自动化的最佳实践执行
- Memory 持久化记忆系统，保持跨会话的上下文连贯性
- Security 安全沙箱机制，保障代码执行环境隔离

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该系统构建统一的 AI 开发规范和安全策略
- 安全敏感项目开发：利用安全沙箱机制在可控环境中运行 AI 生成的代码
- 个人开发者效率提升：通过 Skills 和 Memory 定制个性化的 AI 编程助手工作流



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,536 |
| 语言 | TypeScript |
| Forks | 14,969 |
| Issues | 717 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是下一代 AI Agent 开发平台，支持多智能体协作和 Agent 团队设计，拥有 75k+ Stars 的活跃社区。预置集成 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 提供商，并支持 MCP 协议，适合快速构建生产级 AI Agent 应用。

**技术亮点**:
- 多智能体协作框架：支持 Agent 间的高效通信与任务协调，实现复杂工作流的自动化
- 多 AI 提供商集成：开箱即用支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流模型
- MCP (Model Context Protocol) 支持：标准化的 AI 模型上下文管理协议，便于扩展和集成
- TypeScript 完整类型支持：提供完整的类型定义和 IDE 智能提示，提升开发体验和代码质量
- 知识库与 RAG 功能：内置向量存储和检索增强生成能力，支持构建知识型 Agent

**适用场景**:
- 企业级 AI Agent 应用开发：构建智能客服、数据分析、内容生成等多业务场景的 AI 助手
- 多智能体协作系统：设计和部署多个 Agent 协同工作的复杂工作流，如项目管理、代码审查等
- 个人 AI 助手搭建：基于知识库功能构建个人知识管理、任务规划、日程管理等私人 AI 助理



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,381 |
| 语言 | TypeScript |
| Forks | 5,621 |
| Issues | 143 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个解决 AI 编程助手长期记忆缺失痛点的插件，通过自动捕获、压缩和检索编码上下文，让 Claude Code 能够跨越会话记住之前的操作和决策，实现真正的长期 AI 辅助编程体验。该项目拥有 66k+ Stars 的社区认可度，证明其在实际开发中的巨大价值。

**技术亮点**:
- Claude Agent SDK 深度集成：利用官方 Claude SDK 实现与 Claude 的无缝对接，确保记忆捕获和注入的准确性和可靠性
- RAG + 向量检索架构：采用 ChromaDB 等向量数据库和嵌入模型进行语义检索，支持基于语义相似度召回历史上下文
- AI 驱动的记忆压缩：使用 Claude 本身对捕获的编码活动进行智能压缩，在保留关键信息的同时最小化记忆体积
- SQLite 本地持久化存储：使用 SQLite 作为本地数据库，确保记忆数据的安全性和隐私性，所有数据存储在本地
- 多层次记忆系统：结合 mem0/openmemory 等成熟记忆引擎理念，支持长期记忆和短期会话记忆的分层管理

**适用场景**:
- 长期复杂项目开发：如大型代码库维护、企业级应用开发，需要 AI 记住数周甚至数月前的架构决策和技术债务
- 个人开发者知识积累：构建个人专属的 AI 编程知识库，让 AI 逐渐学习开发者的编码风格、偏好和项目规范
- 跨会话问题追溯：当代码出现 regression 或需要理解历史变更时，AI 可快速检索相关上下文进行问题定位



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,475 |
| 语言 | HTML |
| Forks | 20,993 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万星标的热门 AI 提示词库，前身是著名的 Awesome ChatGPT Prompts 项目，支持 ChatGPT、Claude、Gemini 等多款主流 LLM，提供了超过 5000+ 精选提示词，且完全开源可自托管，是学习和提升 prompt engineering 能力的最佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持多平台 LLM 集成（ChatGPT、Claude、Gemini、GPT-4），统一管理不同模型的提示词
- 开源可自托管部署，支持企业级私有化部署保障数据隐私
- 社区驱动的提示词共享机制，持续收录高质量 user prompts
- 采用响应式设计，提供良好的跨设备用户体验

**适用场景**:
- 个人开发者学习 prompt engineering 技巧，提升与 AI 交互的效率和质量
- 企业团队自托管部署，在保证数据隐私的前提下使用社区优质提示词
- AI 爱好者探索和收藏各类场景的提示词，包括写作、编程、内容创作等



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,286 |
| 语言 | Jupyter Notebook |
| Forks | 14,052 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,636 |
| 语言 | HTML |
| Forks | 4,691 |
| Issues | 8 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,637 |
| 语言 | Python |
| Forks | 2,328 |
| Issues | 146 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,663 |
| 语言 | Python |
| Forks | 9,981 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,848 |
| 语言 | JavaScript |
| Forks | 6,357 |
| Issues | 330 |
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
| Stars | 71,926 |
| 语言 | Python |
| Forks | 9,061 |
| Issues | 412 |
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
| Stars | 53,706 |
| 语言 | TypeScript |
| Forks | 4,346 |
| Issues | 617 |
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
| Stars | 52,207 |
| 语言 | TypeScript |
| Forks | 24,208 |
| Issues | 821 |
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
| Stars | 77,881 |
| 语言 | Python |
| Forks | 15,991 |
| Issues | 4,431 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,303 |
| 语言 | Python |
| Forks | 8,841 |
| Issues | 954 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,881 |
| 语言 | Python |
| Forks | 5,995 |
| Issues | 548 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,798 |
| 语言 | Go |
| Forks | 15,757 |
| Issues | 3,041 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,965 |
| 语言 | TypeScript |
| Forks | 9,214 |
| Issues | 106 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,089 |
| 语言 | Rust |
| Forks | 9,607 |
| Issues | 1 |
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
| Stars | 34,218 |
| 语言 | Python |
| Forks | 2,167 |
| Issues | 99 |
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
| Stars | 115,874 |
| 语言 | Python |
| Forks | 7,574 |
| Issues | 639 |
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
| Stars | 69,643 |
| 语言 | Python |
| Forks | 7,124 |
| Issues | 120 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


## 🧠 机器学习框架 (9 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,524 |
| 语言 | Python |
| Forks | 8,616 |
| Issues | 987 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 顶会认证的统一微调框架，支持 100+ 主流 LLM 和 VLM 模型，集成 LoRA/QLoRA/RLHF 等多种微调技术，70k+ Stars 证明其成熟度和社区认可度，是企业和研究者进行大模型定制的高效解决方案。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流架构
- 集成 PEFT 库支持 LoRA、QLoRA 等高效参数微调技术，大幅降低显存占用
- 支持量化技术（INT4/INT8）和 MoE 混合专家模型架构
- 支持 RLHF（人类反馈强化学习）训练范式，包括 DPO/KTO 等对齐算法
- 提供 WebUI、CLI、Python API 三种交互方式，开箱即用

**适用场景**:
- 企业场景：使用私有数据快速微调垂直领域大模型（如金融、医疗、法律），打造专属 AI 应用
- 个人开发者/研究者：低成本实验多种微调技术，比较不同模型在特定任务上的表现
- 多模态应用开发：利用 VLM 微调能力开发视觉问答、图像理解等应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,393 |
| 语言 | Python |
| Forks | 6,626 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过66k Stars的活跃社区支持，提供从股票、加密货币到期权、衍生品的统一数据接口，并原生支持AI Agent集成，是现代量化分析师和金融科技开发者的一站式解决方案。

**技术亮点**:
- 统一的金融数据API：整合多个数据源，提供股票、加密货币、期权、固收等资产的标准化数据接口
- AI Agent原生支持：内置AI代理集成能力，可与大语言模型无缝对接构建智能投研助手
- 模块化架构设计：采用插件式设计，支持自定义数据源和分析模块扩展
- 丰富的分析工具集：涵盖技术分析、量化因子、风险管理等金融分析功能
- 完整的生态工具链：提供CLI终端、Python SDK、API服务等多种接入方式

**适用场景**:
- 量化交易策略开发：用于获取市场数据、构建因子模型、执行回测和风险管理
- 投研分析与报告生成：辅助分析师快速获取多资产类别数据，生成投研报告
- AI金融应用开发：集成LLM构建智能投顾、量化投研助手等AI驱动金融产品



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,475 |
| 语言 | HTML |
| Forks | 20,993 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万星标的热门 AI 提示词库，前身是著名的 Awesome ChatGPT Prompts 项目，支持 ChatGPT、Claude、Gemini 等多款主流 LLM，提供了超过 5000+ 精选提示词，且完全开源可自托管，是学习和提升 prompt engineering 能力的最佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持多平台 LLM 集成（ChatGPT、Claude、Gemini、GPT-4），统一管理不同模型的提示词
- 开源可自托管部署，支持企业级私有化部署保障数据隐私
- 社区驱动的提示词共享机制，持续收录高质量 user prompts
- 采用响应式设计，提供良好的跨设备用户体验

**适用场景**:
- 个人开发者学习 prompt engineering 技巧，提升与 AI 交互的效率和质量
- 企业团队自托管部署，在保证数据隐私的前提下使用社区优质提示词
- AI 爱好者探索和收藏各类场景的提示词，包括写作、编程、内容创作等



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,286 |
| 语言 | Jupyter Notebook |
| Forks | 14,052 |
| Issues | 5 |
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
| Stars | 159,824 |
| 语言 | Python |
| Forks | 32,992 |
| Issues | 2,342 |
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
| Stars | 77,881 |
| 语言 | Python |
| Forks | 15,991 |
| Issues | 4,431 |
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
| Stars | 109,813 |
| 语言 | Python |
| Forks | 12,790 |
| Issues | 3,977 |
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
| Stars | 99,386 |
| 语言 | Python |
| Forks | 27,573 |
| Issues | 18,522 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,928 |
| 语言 | TypeScript |
| Forks | 3,678 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 🛠️ 开发工具 (15 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 165,177 |
| 语言 | JavaScript |
| Forks | 25,640 |
| Issues | 156 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程助手设计的性能优化系统，通过 Skills、Instincts、Memory 等机制显著增强 Claude Code 等工具的智能化水平，特别适合追求高效、安全 AI 辅助开发的团队。

**技术亮点**:
- MCP (Model Context Protocol) 深度集成，支持与多种 AI agent 无缝协作
- 模块化 Skills 系统，允许自定义扩展 agent 能力
- Instincts 本能机制，实现自动化的最佳实践执行
- Memory 持久化记忆系统，保持跨会话的上下文连贯性
- Security 安全沙箱机制，保障代码执行环境隔离

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该系统构建统一的 AI 开发规范和安全策略
- 安全敏感项目开发：利用安全沙箱机制在可控环境中运行 AI 生成的代码
- 个人开发者效率提升：通过 Skills 和 Memory 定制个性化的 AI 编程助手工作流



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,744 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在消费级硬件上运行多种 AI 模型（LLM、图像生成、语音合成等），无需依赖云服务或 GPU，为开发者和企业提供了完全可控、私有化的 AI 部署解决方案，特别适合对数据隐私和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种任务，通过统一 API 调用
- 去中心化分布式架构：集成 libp2p 支持 P2P 网络通信，支持分布式部署和去中心化推理，可构建本地 AI 集群
- 无 GPU 依赖设计：针对 CPU 推理优化，可在普通消费级硬件上运行，降低 AI 应用部署门槛
- API 优先架构：提供 OpenAI 兼容的 REST API，支持 MCP 协议，便于集成到现有系统和应用
- Go 语言高性能实现：利用 Go 的并发优势实现高效的模型推理和资源调度

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地运行 AI 服务，处理敏感数据（如医疗、金融、法律文档），避免数据上传到第三方云服务
- 边缘计算与物联网：在边缘设备（如树莓派、工控机）上部署轻量级 AI 推理能力，支持智能监控、语音交互等场景
- 开发与测试环境：开发者在本地构建和测试 AI 应用原型，无需付费订阅云 API，降低开发成本并提高迭代效率



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,954 |
| 语言 | Java |
| Forks | 15,942 |
| Issues | 14 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,926 |
| 语言 | Python |
| Forks | 9,061 |
| Issues | 412 |
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
| Stars | 53,706 |
| 语言 | TypeScript |
| Forks | 4,346 |
| Issues | 617 |
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
| Stars | 185,315 |
| 语言 | TypeScript |
| Forks | 57,066 |
| Issues | 1,556 |
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
| Stars | 158,291 |
| 语言 | Python |
| Forks | 13,093 |
| Issues | 2,482 |
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
| Stars | 97,571 |
| 语言 | Python |
| Forks | 9,139 |
| Issues | 173 |
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
| Stars | 81,793 |
| 语言 | Python |
| Forks | 9,524 |
| Issues | 256 |
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
| Stars | 184,182 |
| 语言 | TypeScript |
| Forks | 39,373 |
| Issues | 16,594 |
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
| Stars | 94,175 |
| 语言 | TypeScript |
| Forks | 9,409 |
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
| Stars | 79,011 |
| 语言 | TypeScript |
| Forks | 5,826 |
| Issues | 775 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,735 |
| 语言 | Go |
| Forks | 2,790 |
| Issues | 311 |
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
| Stars | 76,931 |
| 语言 | Go |
| Forks | 2,781 |
| Issues | 959 |
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
| Stars | 44,002 |
| 语言 | Go |
| Forks | 8,316 |
| Issues | 983 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (14 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,706 |
| 语言 | TypeScript |
| Forks | 4,346 |
| Issues | 617 |
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
| Stars | 185,315 |
| 语言 | TypeScript |
| Forks | 57,066 |
| Issues | 1,556 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,881 |
| 语言 | Python |
| Forks | 5,995 |
| Issues | 548 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,619 |
| 语言 | Go |
| Forks | 10,320 |
| Issues | 232 |
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
| Stars | 121,876 |
| 语言 | Go |
| Forks | 42,904 |
| Issues | 2,706 |
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
| Stars | 71,488 |
| 语言 | Go |
| Forks | 18,918 |
| Issues | 3,799 |
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
| Stars | 55,070 |
| 语言 | Go |
| Forks | 6,607 |
| Issues | 2,776 |
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
| Stars | 47,487 |
| 语言 | Go |
| Forks | 5,049 |
| Issues | 982 |
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
| Stars | 94,175 |
| 语言 | TypeScript |
| Forks | 9,409 |
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
| Stars | 77,698 |
| 语言 | TypeScript |
| Forks | 6,771 |
| Issues | 415 |
| Topics | docker, hacktoberfest, java, pdf, pdf-converter, pdf-editor, pdf-manipulation, pdf-merger, pdf-ocr, pdf-tools, pdf-web-apps, pdfmerger, self-hosted |
| 许可证 | Other |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,721 |
| 语言 | JavaScript |
| Forks | 7,698 |
| Issues | 726 |
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
| Stars | 70,004 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 322 |
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
| Stars | 62,843 |
| 语言 | Go |
| Forks | 5,935 |
| Issues | 766 |
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
| Stars | 59,119 |
| 语言 | Go |
| Forks | 4,296 |
| Issues | 29 |
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
| Stars | 85,721 |
| 语言 | JavaScript |
| Forks | 7,698 |
| Issues | 726 |
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
| Stars | 63,731 |
| 语言 | Go |
| Forks | 10,352 |
| Issues | 748 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (11 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,744 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在消费级硬件上运行多种 AI 模型（LLM、图像生成、语音合成等），无需依赖云服务或 GPU，为开发者和企业提供了完全可控、私有化的 AI 部署解决方案，特别适合对数据隐私和成本敏感的场景。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种任务，通过统一 API 调用
- 去中心化分布式架构：集成 libp2p 支持 P2P 网络通信，支持分布式部署和去中心化推理，可构建本地 AI 集群
- 无 GPU 依赖设计：针对 CPU 推理优化，可在普通消费级硬件上运行，降低 AI 应用部署门槛
- API 优先架构：提供 OpenAI 兼容的 REST API，支持 MCP 协议，便于集成到现有系统和应用
- Go 语言高性能实现：利用 Go 的并发优势实现高效的模型推理和资源调度

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地运行 AI 服务，处理敏感数据（如医疗、金融、法律文档），避免数据上传到第三方云服务
- 边缘计算与物联网：在边缘设备（如树莓派、工控机）上部署轻量级 AI 推理能力，支持智能监控、语音交互等场景
- 开发与测试环境：开发者在本地构建和测试 AI 应用原型，无需付费订阅云 API，降低开发成本并提高迭代效率



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,571 |
| 语言 | Python |
| Forks | 9,139 |
| Issues | 173 |
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
| Stars | 87,318 |
| 语言 | Python |
| Forks | 33,824 |
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
| Stars | 100,043 |
| 语言 | TypeScript |
| Forks | 27,184 |
| Issues | 1,126 |
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
| Stars | 79,011 |
| 语言 | TypeScript |
| Forks | 5,826 |
| Issues | 775 |
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
| Stars | 68,965 |
| 语言 | JavaScript |
| Forks | 23,162 |
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
| Stars | 55,954 |
| 语言 | JavaScript |
| Forks | 10,207 |
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
| Stars | 51,817 |
| 语言 | JavaScript |
| Forks | 4,705 |
| Issues | 1,464 |
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
| Stars | 88,360 |
| 语言 | Go |
| Forks | 8,576 |
| Issues | 679 |
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
| Stars | 71,779 |
| 语言 | Go |
| Forks | 4,701 |
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
| Stars | 57,862 |
| 语言 | Go |
| Forks | 3,322 |
| Issues | 19 |
| Topics | authentication, backend, golang, realtime |
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
| Stars | 101,315 |
| 语言 | TypeScript |
| Forks | 12,159 |
| Issues | 956 |
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
| Stars | 58,848 |
| 语言 | JavaScript |
| Forks | 6,357 |
| Issues | 330 |
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
| Stars | 43,936 |
| 语言 | Go |
| Forks | 3,972 |
| Issues | 1,135 |
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
| Stars | 51,619 |
| 语言 | Go |
| Forks | 10,320 |
| Issues | 232 |
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
| Stars | 160,475 |
| 语言 | HTML |
| Forks | 20,993 |
| Issues | 40 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过 16 万星标的热门 AI 提示词库，前身是著名的 Awesome ChatGPT Prompts 项目，支持 ChatGPT、Claude、Gemini 等多款主流 LLM，提供了超过 5000+ 精选提示词，且完全开源可自托管，是学习和提升 prompt engineering 能力的最佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构
- 支持多平台 LLM 集成（ChatGPT、Claude、Gemini、GPT-4），统一管理不同模型的提示词
- 开源可自托管部署，支持企业级私有化部署保障数据隐私
- 社区驱动的提示词共享机制，持续收录高质量 user prompts
- 采用响应式设计，提供良好的跨设备用户体验

**适用场景**:
- 个人开发者学习 prompt engineering 技巧，提升与 AI 交互的效率和质量
- 企业团队自托管部署，在保证数据隐私的前提下使用社区优质提示词
- AI 爱好者探索和收藏各类场景的提示词，包括写作、编程、内容创作等



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,637 |
| 语言 | Python |
| Forks | 2,328 |
| Issues | 146 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,063 |
| 语言 | Python |
| Forks | 4,797 |
| Issues | 97 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,965 |
| 语言 | TypeScript |
| Forks | 9,214 |
| Issues | 106 |
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
| Stars | 89,778 |
| 语言 | TypeScript |
| Forks | 10,028 |
| Issues | 2,255 |
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
| Stars | 87,600 |
| 语言 | TypeScript |
| Forks | 8,901 |
| Issues | 1,629 |
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
| Stars | 127,550 |
| 语言 | JavaScript |
| Forks | 12,480 |
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
| Stars | 170,814 |
| 语言 | Go |
| Forks | 13,176 |
| Issues | 179 |
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
| Stars | 135,875 |
| 语言 | Unknown |
| Forks | 34,038 |
| Issues | 138 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,056 |
| 语言 | Python |
| Forks | 13,375 |
| Issues | 108 |
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
| Stars | 90,462 |
| 语言 | Python |
| Forks | 7,790 |
| Issues | 628 |
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
| Stars | 385,920 |
| 语言 | Python |
| Forks | 66,117 |
| Issues | 77 |
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
| Stars | 115,089 |
| 语言 | TypeScript |
| Forks | 5,993 |
| Issues | 59 |
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
| Stars | 112,867 |
| 语言 | TypeScript |
| Forks | 8,245 |
| Issues | 295 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,358 |
| 语言 | TypeScript |
| Forks | 11,771 |
| Issues | 417 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,648 |
| 语言 | JavaScript |
| Forks | 4,793 |
| Issues | 23 |
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
| Stars | 48,225 |
| 语言 | Go |
| Forks | 10,301 |
| Issues | 1,893 |
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
| Stars | 105,991 |
| 语言 | C++ |
| Forks | 17,272 |
| Issues | 1,538 |
| Topics | ggml |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,421 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 30 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,048 |
| 语言 | Unknown |
| Forks | 7,544 |
| Issues | 70 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 294,021 |
| 语言 | Python |
| Forks | 27,751 |
| Issues | 20 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,242 |
| 语言 | Python |
| Forks | 7,237 |
| Issues | 487 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,147 |
| 语言 | Python |
| Forks | 37,315 |
| Issues | 3,744 |
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
| Stars | 77,668 |
| 语言 | Python |
| Forks | 45,121 |
| Issues | 1,280 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,119 |
| 语言 | Python |
| Forks | 16,877 |
| Issues | 26 |
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
| Stars | 443,435 |
| 语言 | TypeScript |
| Forks | 44,365 |
| Issues | 190 |
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
| Stars | 353,471 |
| 语言 | TypeScript |
| Forks | 43,958 |
| Issues | 10 |
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
| Stars | 121,792 |
| 语言 | TypeScript |
| Forks | 13,410 |
| Issues | 3,009 |
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
| Stars | 112,878 |
| 语言 | TypeScript |
| Forks | 8,631 |
| Issues | 1,833 |
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
| Stars | 108,642 |
| 语言 | TypeScript |
| Forks | 13,358 |
| Issues | 5,029 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,459 |
| 语言 | TypeScript |
| Forks | 5,459 |
| Issues | 682 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,826 |
| 语言 | TypeScript |
| Forks | 54,597 |
| Issues | 1,363 |
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
| Stars | 94,715 |
| 语言 | TypeScript |
| Forks | 5,209 |
| Issues | 110 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 84,404 |
| 语言 | TypeScript |
| Forks | 10,477 |
| Issues | 385 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,171 |
| 语言 | TypeScript |
| Forks | 8,087 |
| Issues | 709 |
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
| Stars | 244,625 |
| 语言 | JavaScript |
| Forks | 50,971 |
| Issues | 1,241 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,135 |
| 语言 | JavaScript |
| Forks | 26,712 |
| Issues | 160 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,879 |
| 语言 | JavaScript |
| Forks | 35,416 |
| Issues | 2,635 |
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
| Stars | 112,141 |
| 语言 | JavaScript |
| Forks | 36,336 |
| Issues | 523 |
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
| Stars | 109,018 |
| 语言 | JavaScript |
| Forks | 11,650 |
| Issues | 272 |
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
| Stars | 98,217 |
| 语言 | JavaScript |
| Forks | 32,669 |
| Issues | 1,534 |
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
| Stars | 95,656 |
| 语言 | JavaScript |
| Forks | 15,392 |
| Issues | 50 |
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
| Stars | 86,406 |
| 语言 | JavaScript |
| Forks | 4,896 |
| Issues | 994 |
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
| Stars | 71,059 |
| 语言 | JavaScript |
| Forks | 16,809 |
| Issues | 894 |
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
| Stars | 67,379 |
| 语言 | JavaScript |
| Forks | 11,956 |
| Issues | 554 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,783 |
| 语言 | JavaScript |
| Forks | 9,362 |
| Issues | 205 |
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
| Stars | 62,940 |
| 语言 | JavaScript |
| Forks | 4,020 |
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
| Stars | 61,254 |
| 语言 | JavaScript |
| Forks | 7,147 |
| Issues | 140 |
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
| Stars | 60,653 |
| 语言 | JavaScript |
| Forks | 5,657 |
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
| Stars | 59,831 |
| 语言 | JavaScript |
| Forks | 20,459 |
| Issues | 89 |
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
| Stars | 57,425 |
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
| Stars | 53,181 |
| 语言 | JavaScript |
| Forks | 10,604 |
| Issues | 454 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,630 |
| 语言 | JavaScript |
| Forks | 11,503 |
| Issues | 242 |
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
| Stars | 133,604 |
| 语言 | Go |
| Forks | 18,941 |
| Issues | 9,978 |
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
| Stars | 87,735 |
| 语言 | Go |
| Forks | 8,247 |
| Issues | 238 |
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
| Stars | 82,989 |
| 语言 | Go |
| Forks | 5,105 |
| Issues | 389 |
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
| Stars | 68,613 |
| 语言 | Go |
| Forks | 3,220 |
| Issues | 21 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,813 |
| 语言 | Go |
| Forks | 5,054 |
| Issues | 1,175 |
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
| Stars | 50,996 |
| 语言 | Go |
| Forks | 21,900 |
| Issues | 409 |
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
| Stars | 50,764 |
| 语言 | Go |
| Forks | 1,606 |
| Issues | 271 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,351 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 562 |
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
| Stars | 46,071 |
| 语言 | Go |
| Forks | 3,796 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,901 |
| 语言 | Shell |
| Forks | 13,782 |
| Issues | 110 |
| 许可证 | MIT License |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,093 |
| 语言 | Python |
| Forks | 50,398 |
| Issues | 927 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 98,264 |
| 语言 | Python |
| Forks | 12,080 |
| Issues | 121 |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,990 |
| 语言 | TypeScript |
| Forks | 16,521 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,235 |
| 语言 | TypeScript |
| Forks | 7,597 |
| Issues | 35 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,134 |
| 语言 | JavaScript |
| Forks | 32,615 |
| Issues | 279 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,337 |
| 语言 | JavaScript |
| Forks | 9,191 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,304 |
| 语言 | JavaScript |
| Forks | 10,352 |
| Issues | 134 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 106,050 |
| 语言 | Go |
| Forks | 15,017 |
| Issues | 38 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 152,703 |
| 语言 | Python |
| Forks | 11,634 |
| Issues | 336 |
| Topics | awesome, github, hellogithub, python |
