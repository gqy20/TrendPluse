# 项目发现报告 (2026-05-19)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 127 |
| 去重移除 | 39 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 19 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 59 |

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


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,862 |
| 语言 | Python |
| Forks | 25,509 |
| Issues | 12,168 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

hermes-agent 是由开源LLM领域知名团队 NousResearch 打造的通用型 AI Agent 框架，支持 OpenAI、Anthropic Claude、Codex 等多主流 LLM 提供商，以 15.7 万 Stars 的社区认可度证明了其技术成熟度和可靠性，特别适合构建企业级智能代理应用。

**技术亮点**:
- 多模型支持：原生集成 OpenAI GPT、Anthropic Claude、Codex 等主流大语言模型，提供统一的调用接口
- 模块化 Agent 架构：采用可扩展的 Agent 设计模式，支持工具调用、任务规划、记忆管理等核心能力
- MIT 开源许可：完全开源且采用宽松的 MIT 许可证，便于商业集成和二次开发
- 成熟的社区生态：依托 NousResearch 在开源 AI 领域的深厚积累，拥有活跃的社区支持和持续更新
- Python 原生实现：深度适配 Python 生态，可无缝对接 LangChain、LlamaIndex 等主流 AI 开发框架

**适用场景**:
- 企业级 AI 自动化：构建客服机器人、文档处理助手、业务流程自动化等企业智能应用
- 开发者 AI 工具链：集成到开发工作流，实现代码审查、自动化测试、智能文档生成等开发辅助功能
- 个人生产力助手：开发个人知识管理、日程规划、信息检索等提升个人效率的智能工具



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,802 |
| 语言 | Python |
| Forks | 19,698 |
| Issues | 259 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面项目，支持 Ollama、OpenAI API 等多种后端，并内置 RAG 和 MCP 支持，超过 13 万星标证明了其成熟度和社区认可度，是自托管 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 规范，可灵活切换不同 LLM 提供商
- 内置 RAG 系统：支持检索增强生成，可连接外部知识库提升回答质量
- Model Context Protocol (MCP) 支持：实现与外部工具和数据源的深度集成
- 开箱即用的 Web UI：响应式设计，支持中文界面，提供类 ChatGPT 的交互体验
- 完整的后端 API：提供 RESTful API 接口，便于二次开发和与企业系统集成

**适用场景**:
- 企业私有化部署：适合对数据隐私有要求的企业，在本地服务器部署 AI 助手，完全掌控数据
- 开发者快速原型开发：个人开发者可基于此项目快速搭建 AI 应用界面，节省 UI 开发时间
- 研究实验环境：研究人员和 AI 爱好者可方便地测试不同 LLM 模型和 RAG 效果
- 团队知识库问答系统：通过 RAG 功能构建基于内部文档的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,828 |
| 语言 | Python |
| Forks | 9,250 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，将前沿 RAG 技术与 Agent 能力深度融合，通过可视化界面简化知识库构建流程，特别适合需要构建企业级智能问答系统和文档理解应用的团队。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，支持复杂多跳推理和动态工具调用
- 深度文档理解：支持 PDF、Word、Excel、PPT 等多格式文档的智能解析和结构化提取
- 可视化知识库管理：提供直观的 Web 界面，支持文档上传、切片策略配置、检索参数调整
- 灵活的模型集成：支持 OpenAI、Claude、通义千问等多种 LLM 以及多向量数据库
- 语义切片技术：基于深度学习的文档智能分块，提升检索质量和生成准确性

**适用场景**:
- 企业知识库问答：构建私有化智能客服和内部知识检索系统，支持复杂文档的专业问答
- 文档智能分析处理：对合同、报告、手册等长文档进行结构化解析和信息提取
- AI 应用开发：为开发者提供 RAG 应用快速开发和部署能力，支持自定义工作流和插件扩展



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,321 |
| 语言 | Python |
| Forks | 15,081 |
| Issues | 353 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |

---

TradingAgents 是首个将多智能体架构与 LLM 结合的开源金融交易框架，拥有 7.7 万星的高人气，采用 Apache 2.0 许可证允许商业使用，适合需要构建智能化量化交易系统的企业和个人开发者快速上手。

**技术亮点**:
- 多智能体协作架构：多个专业代理协同工作，分工处理市场分析、策略制定、风险评估等任务
- LLM 驱动的决策引擎：利用大语言模型理解市场新闻、财务报告和非结构化数据
- 模块化设计：支持自定义代理、工具和交易策略，便于扩展和定制
- 丰富的金融工具集成：内置技术指标、基本面分析和情绪分析等工具
- 生产级代码质量：完整的日志记录、错误处理和监控告警机制

**适用场景**:
- 量化交易策略开发：利用 LLM 分析市场趋势和新闻情绪，自动生成和执行交易策略
- 投资研究自动化：自动抓取和分析上市公司财报、行业动态，辅助投资决策
- 金融教育和模拟交易：为金融专业学生和爱好者提供真实的 AI 交易环境进行学习和实验



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 121,868 |
| 语言 | TypeScript |
| Forks | 7,411 |
| Issues | 325 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前最完善的 AI 驱动网页抓取工具，专门解决 AI 代理和 LLM 应用的数据获取难题，支持端到端的搜索、抓取和清洗流程，能将混乱的网页内容转化为 LLM 友好的 Markdown 格式。

**技术亮点**:
- 专为 AI 代理设计的数据处理管道，支持智能网页清洗和内容提取
- 强大的 HTML 转 Markdown 转换能力，输出结构化、对 LLM 友好的数据格式
- 支持批量网站抓取和智能搜索，可获取整个网站的结构化数据
- TypeScript 原生实现，提供完整的 API 接口和 SDK 支持
- 支持多种数据提取模式，包括全文提取、链接发现和元数据解析

**适用场景**:
- 为 LLM/AI 代理应用提供可靠的网络数据获取和清洗服务
- 构建企业级知识库和 RAG（检索增强生成）系统的数据源
- 自动化市场调研、竞品分析和内容聚合的数据采集



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,131 |
| 语言 | JavaScript |
| Forks | 28,975 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Memory、Security 等模块显著提升 AI 辅助编程的效率与安全性，特别适合追求高效 AI 编程工作流的开发者。

**技术亮点**:
- 支持多平台 AI 代理（Claude Code、Codex、Opencode、Cursor 等），提供统一优化接口
- 基于 MCP（Model Context Protocol）实现标准化的代理交互协议
- Memory 模块支持持久化上下文记忆，增强代理状态管理能力
- Security 模块提供安全沙箱机制，保障代码执行安全
- Skills & Instincts 系统实现可扩展的技能注入与本能行为优化

**适用场景**:
- 企业级 AI 辅助开发：团队可部署 ECC 统一管理多个 AI 编码工具，优化开发工作流
- 个人开发者效率提升：通过 Memory 和 Skills 模块定制个人化的 AI 编程助手
- AI 代理研究与实验：研究人员可基于 ECC 框架进行代理性能对比与优化研究
- 安全敏感场景开发：利用 Security 模块在沙箱环境中测试 AI 生成的代码



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,360 |
| 语言 | Go |
| Forks | 4,091 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型类型，无需 GPU 即可在各类硬件上部署，特别适合需要数据隐私保护和降低云服务成本的场景。

**技术亮点**:
- 多模态模型支持：同时支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成和目标检测等多种模型类型
- CPU 友好架构：无需 GPU 即可运行 AI 模型，降低硬件门槛，支持在各类硬件上部署
- Go 语言开发：利用 Go 的高性能和并发特性，提供高效的推理性能
- 去中心化架构：集成 libp2p 支持分布式部署，可构建去中心化 AI 网络
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，便于现有应用快速迁移和集成

**适用场景**:
- 数据隐私敏感场景：企业或个人需要本地处理敏感数据（如医疗记录、财务信息），避免数据上传到第三方云服务
- 资源受限环境：在没有强大 GPU 的服务器或个人电脑上运行 AI 模型，适合开发者学习和实验
- AI 服务本地化部署：构建私有化的 AI API 服务，为内部应用提供 LLM、图像生成等能力，支持定制化需求



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,350 |
| 语言 | TypeScript |
| Forks | 15,225 |
| Issues | 292 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的开源 AI Agent 管理平台，拥有 77K+ Stars 的社区验证，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，并提供 MCP 协议集成、知识库管理和 Agent 协作编排能力，是构建企业级 AI 团队工作流的最佳选择。

**技术亮点**:
- 多模型集成支持：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：实现 AI Agent 与外部工具和服务的标准化连接协议
- Agent 协作编排引擎：支持多个 AI Agent 之间的任务分配、调度和结果汇总
- 内置知识库系统：支持 RAG 增强检索和向量存储，增强 Agent 的领域知识
- TypeScript/React 现代技术栈：基于 React 18 + TypeScript 开发，支持插件化架构和主题定制

**适用场景**:
- 企业 AI 团队自动化运营：构建 7×24 小时运作的 AI Agent 团队，处理客户服务、数据分析、内容生成等任务
- AI 应用快速开发：使用现成的 Agent 框架和 MCP 生态快速构建 AI 应用，无需从零开发底层能力
- 个人 AI 工作流编排：个人开发者可以将多个 AI 助手串联成自动化工作流，提升个人生产力



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,819 |
| 语言 | TypeScript |
| Forks | 6,611 |
| Issues | 165 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现跨会话持久化上下文管理，解决了 AI Agent 无法保留历史记忆的核心痛点，支持 7+ 主流 AI 编程工具（Stars 76,819 验证了其极高的社区认可度和实用性）。

**技术亮点**:
- AI 驱动的语义压缩：自动分析会话内容并提取关键信息，有效降低存储成本
- 多 Agent 平台兼容：支持 Claude Code、Copilot、Codex、Gemini 等 7+ 主流 AI 编程工具
- RAG + Embeddings 技术栈：结合检索增强生成和向量嵌入实现精准上下文召回
- 本地化存储方案：支持 SQLite 和 ChromaDB，兼顾轻量与高性能
- Apache 2.0 开源许可：允许商业使用，降低企业采纳门槛

**适用场景**:
- 企业级 AI 开发团队：需要 AI 编程助手记住项目上下文、编码规范和历史决策的大型项目开发
- 复杂多阶段任务处理：需要 AI Agent 跨天/跨周持续工作的研究、数据分析或自动化流程
- 个人开发者效率提升：让 AI 编程助手记住个人偏好、项目架构和技术栈，避免重复解释



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,413 |
| 语言 | Python |
| Forks | 8,719 |
| Issues | 1,018 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,844 |
| 语言 | HTML |
| Forks | 5,389 |
| Issues | 16 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,379 |
| 语言 | Python |
| Forks | 6,214 |
| Issues | 113 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,327 |
| 语言 | Java |
| Forks | 16,000 |
| Issues | 24 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,157 |
| 语言 | TypeScript |
| Forks | 6,019 |
| Issues | 556 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,305 |
| 语言 | JavaScript |
| Forks | 6,518 |
| Issues | 355 |
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
| Stars | 74,161 |
| 语言 | Python |
| Forks | 9,401 |
| Issues | 409 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,574 |
| 语言 | TypeScript |
| Forks | 4,754 |
| Issues | 590 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,191 |
| 语言 | Python |
| Forks | 6,212 |
| Issues | 83 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,661 |
| 语言 | Python |
| Forks | 10,678 |
| Issues | 229 |
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
| Stars | 52,934 |
| 语言 | TypeScript |
| Forks | 24,360 |
| Issues | 861 |
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
| Stars | 188,730 |
| 语言 | TypeScript |
| Forks | 57,828 |
| Issues | 1,495 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,771 |
| 语言 | JavaScript |
| Forks | 46,133 |
| Issues | 62 |
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
| Stars | 148,522 |
| 语言 | Python |
| Forks | 9,048 |
| Issues | 927 |
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
| Stars | 64,215 |
| 语言 | Jupyter Notebook |
| Forks | 21,278 |
| Issues | 9 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Gemini CLI & Hermes Agent. Only official website: ccswitch.io

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,524 |
| 语言 | Rust |
| Forks | 4,903 |
| Issues | 941 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,674 |
| 语言 | Python |
| Forks | 6,604 |
| Issues | 648 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,359 |
| 语言 | TypeScript |
| Forks | 10,033 |
| Issues | 131 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,114 |
| 语言 | Python |
| Forks | 16,495 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 🔍 RAG/检索 (15 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,802 |
| 语言 | Python |
| Forks | 19,698 |
| Issues | 259 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面项目，支持 Ollama、OpenAI API 等多种后端，并内置 RAG 和 MCP 支持，超过 13 万星标证明了其成熟度和社区认可度，是自托管 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 规范，可灵活切换不同 LLM 提供商
- 内置 RAG 系统：支持检索增强生成，可连接外部知识库提升回答质量
- Model Context Protocol (MCP) 支持：实现与外部工具和数据源的深度集成
- 开箱即用的 Web UI：响应式设计，支持中文界面，提供类 ChatGPT 的交互体验
- 完整的后端 API：提供 RESTful API 接口，便于二次开发和与企业系统集成

**适用场景**:
- 企业私有化部署：适合对数据隐私有要求的企业，在本地服务器部署 AI 助手，完全掌控数据
- 开发者快速原型开发：个人开发者可基于此项目快速搭建 AI 应用界面，节省 UI 开发时间
- 研究实验环境：研究人员和 AI 爱好者可方便地测试不同 LLM 模型和 RAG 效果
- 团队知识库问答系统：通过 RAG 功能构建基于内部文档的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,828 |
| 语言 | Python |
| Forks | 9,250 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，将前沿 RAG 技术与 Agent 能力深度融合，通过可视化界面简化知识库构建流程，特别适合需要构建企业级智能问答系统和文档理解应用的团队。

**技术亮点**:
- RAG + Agent 双引擎架构：融合检索增强生成与智能代理能力，支持复杂多跳推理和动态工具调用
- 深度文档理解：支持 PDF、Word、Excel、PPT 等多格式文档的智能解析和结构化提取
- 可视化知识库管理：提供直观的 Web 界面，支持文档上传、切片策略配置、检索参数调整
- 灵活的模型集成：支持 OpenAI、Claude、通义千问等多种 LLM 以及多向量数据库
- 语义切片技术：基于深度学习的文档智能分块，提升检索质量和生成准确性

**适用场景**:
- 企业知识库问答：构建私有化智能客服和内部知识检索系统，支持复杂文档的专业问答
- 文档智能分析处理：对合同、报告、手册等长文档进行结构化解析和信息提取
- AI 应用开发：为开发者提供 RAG 应用快速开发和部署能力，支持自定义工作流和插件扩展



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,350 |
| 语言 | TypeScript |
| Forks | 15,225 |
| Issues | 292 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的开源 AI Agent 管理平台，拥有 77K+ Stars 的社区验证，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，并提供 MCP 协议集成、知识库管理和 Agent 协作编排能力，是构建企业级 AI 团队工作流的最佳选择。

**技术亮点**:
- 多模型集成支持：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：实现 AI Agent 与外部工具和服务的标准化连接协议
- Agent 协作编排引擎：支持多个 AI Agent 之间的任务分配、调度和结果汇总
- 内置知识库系统：支持 RAG 增强检索和向量存储，增强 Agent 的领域知识
- TypeScript/React 现代技术栈：基于 React 18 + TypeScript 开发，支持插件化架构和主题定制

**适用场景**:
- 企业 AI 团队自动化运营：构建 7×24 小时运作的 AI Agent 团队，处理客户服务、数据分析、内容生成等任务
- AI 应用快速开发：使用现成的 Agent 框架和 MCP 生态快速构建 AI 应用，无需从零开发底层能力
- 个人 AI 工作流编排：个人开发者可以将多个 AI 助手串联成自动化工作流，提升个人生产力



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,819 |
| 语言 | TypeScript |
| Forks | 6,611 |
| Issues | 165 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现跨会话持久化上下文管理，解决了 AI Agent 无法保留历史记忆的核心痛点，支持 7+ 主流 AI 编程工具（Stars 76,819 验证了其极高的社区认可度和实用性）。

**技术亮点**:
- AI 驱动的语义压缩：自动分析会话内容并提取关键信息，有效降低存储成本
- 多 Agent 平台兼容：支持 Claude Code、Copilot、Codex、Gemini 等 7+ 主流 AI 编程工具
- RAG + Embeddings 技术栈：结合检索增强生成和向量嵌入实现精准上下文召回
- 本地化存储方案：支持 SQLite 和 ChromaDB，兼顾轻量与高性能
- Apache 2.0 开源许可：允许商业使用，降低企业采纳门槛

**适用场景**:
- 企业级 AI 开发团队：需要 AI 编程助手记住项目上下文、编码规范和历史决策的大型项目开发
- 复杂多阶段任务处理：需要 AI Agent 跨天/跨周持续工作的研究、数据分析或自动化流程
- 个人开发者效率提升：让 AI 编程助手记住个人偏好、项目架构和技术栈，避免重复解释



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,379 |
| 语言 | Python |
| Forks | 6,214 |
| Issues | 113 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,327 |
| 语言 | Java |
| Forks | 16,000 |
| Issues | 24 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 102,696 |
| 语言 | TypeScript |
| Forks | 12,472 |
| Issues | 1,013 |
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
| Stars | 60,305 |
| 语言 | JavaScript |
| Forks | 6,518 |
| Issues | 355 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,191 |
| 语言 | Python |
| Forks | 6,212 |
| Issues | 83 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,158 |
| 语言 | Python |
| Forks | 10,455 |
| Issues | 210 |
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
| Stars | 52,934 |
| 语言 | TypeScript |
| Forks | 24,360 |
| Issues | 861 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### safishamsi/graphify

**描述**: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,592 |
| 语言 | Python |
| Forks | 5,387 |
| Issues | 256 |
| Topics | antigravity, claude-code, codex, gemini, graphrag, knowledge-graph, leiden, openclaw, rag, skills, tree-sitter |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,362 |
| 语言 | Go |
| Forks | 4,007 |
| Issues | 903 |
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
| Stars | 35,385 |
| 语言 | Python |
| Forks | 5,004 |
| Issues | 233 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,114 |
| 语言 | Python |
| Forks | 16,495 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 💬 LLM 界面 (19 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,862 |
| 语言 | Python |
| Forks | 25,509 |
| Issues | 12,168 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

hermes-agent 是由开源LLM领域知名团队 NousResearch 打造的通用型 AI Agent 框架，支持 OpenAI、Anthropic Claude、Codex 等多主流 LLM 提供商，以 15.7 万 Stars 的社区认可度证明了其技术成熟度和可靠性，特别适合构建企业级智能代理应用。

**技术亮点**:
- 多模型支持：原生集成 OpenAI GPT、Anthropic Claude、Codex 等主流大语言模型，提供统一的调用接口
- 模块化 Agent 架构：采用可扩展的 Agent 设计模式，支持工具调用、任务规划、记忆管理等核心能力
- MIT 开源许可：完全开源且采用宽松的 MIT 许可证，便于商业集成和二次开发
- 成熟的社区生态：依托 NousResearch 在开源 AI 领域的深厚积累，拥有活跃的社区支持和持续更新
- Python 原生实现：深度适配 Python 生态，可无缝对接 LangChain、LlamaIndex 等主流 AI 开发框架

**适用场景**:
- 企业级 AI 自动化：构建客服机器人、文档处理助手、业务流程自动化等企业智能应用
- 开发者 AI 工具链：集成到开发工作流，实现代码审查、自动化测试、智能文档生成等开发辅助功能
- 个人生产力助手：开发个人知识管理、日程规划、信息检索等提升个人效率的智能工具



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,802 |
| 语言 | Python |
| Forks | 19,698 |
| Issues | 259 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面项目，支持 Ollama、OpenAI API 等多种后端，并内置 RAG 和 MCP 支持，超过 13 万星标证明了其成熟度和社区认可度，是自托管 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAPI 规范，可灵活切换不同 LLM 提供商
- 内置 RAG 系统：支持检索增强生成，可连接外部知识库提升回答质量
- Model Context Protocol (MCP) 支持：实现与外部工具和数据源的深度集成
- 开箱即用的 Web UI：响应式设计，支持中文界面，提供类 ChatGPT 的交互体验
- 完整的后端 API：提供 RESTful API 接口，便于二次开发和与企业系统集成

**适用场景**:
- 企业私有化部署：适合对数据隐私有要求的企业，在本地服务器部署 AI 助手，完全掌控数据
- 开发者快速原型开发：个人开发者可基于此项目快速搭建 AI 应用界面，节省 UI 开发时间
- 研究实验环境：研究人员和 AI 爱好者可方便地测试不同 LLM 模型和 RAG 效果
- 团队知识库问答系统：通过 RAG 功能构建基于内部文档的智能问答服务



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,131 |
| 语言 | JavaScript |
| Forks | 28,975 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Memory、Security 等模块显著提升 AI 辅助编程的效率与安全性，特别适合追求高效 AI 编程工作流的开发者。

**技术亮点**:
- 支持多平台 AI 代理（Claude Code、Codex、Opencode、Cursor 等），提供统一优化接口
- 基于 MCP（Model Context Protocol）实现标准化的代理交互协议
- Memory 模块支持持久化上下文记忆，增强代理状态管理能力
- Security 模块提供安全沙箱机制，保障代码执行安全
- Skills & Instincts 系统实现可扩展的技能注入与本能行为优化

**适用场景**:
- 企业级 AI 辅助开发：团队可部署 ECC 统一管理多个 AI 编码工具，优化开发工作流
- 个人开发者效率提升：通过 Memory 和 Skills 模块定制个人化的 AI 编程助手
- AI 代理研究与实验：研究人员可基于 ECC 框架进行代理性能对比与优化研究
- 安全敏感场景开发：利用 Security 模块在沙箱环境中测试 AI 生成的代码



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,271 |
| 语言 | JavaScript |
| Forks | 3,481 |
| Issues | 211 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 是一个通过「穴居人语言风格」实现 Token 消耗降低 65% 的 Claude Code 技能，项目已获得 62,271 Stars 的社区认可，是将 meme 文化与实际工程价值完美结合的 Prompt 工程创新方案。

**技术亮点**:
- 语言压缩技术：通过简化词汇和语法结构，将复杂表达压缩为简洁的穴居人风格，有效减少 token 计数
- Claude Code 技能集成：作为 Claude Code 的官方 skill 扩展，无缝接入 AI 辅助编程工作流
- 65% Token 节省：实测可显著降低 API 调用成本，适用于大规模 LLM 应用场景
- 零依赖实现：纯 JavaScript 实现，代码轻量且易于理解和修改
- Prompt 工程典范：展示了如何通过语言风格优化而非模型调参来提升效率

**适用场景**:
- 成本敏感型应用：需要频繁调用 LLM API 的项目，通过减少 token 消耗显著降低运营成本
- 开发测试环境：在不影响核心功能的前提下，使用简化的交互方式加速开发迭代
- 批量任务处理：适用于需要大规模 LLM 调用的自动化脚本和数据处理流程
- 个人开发者/小团队：资源有限但需要高效利用 AI 能力的场景



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,350 |
| 语言 | TypeScript |
| Forks | 15,225 |
| Issues | 292 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个成熟的开源 AI Agent 管理平台，拥有 77K+ Stars 的社区验证，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，并提供 MCP 协议集成、知识库管理和 Agent 协作编排能力，是构建企业级 AI 团队工作流的最佳选择。

**技术亮点**:
- 多模型集成支持：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流 AI 模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：实现 AI Agent 与外部工具和服务的标准化连接协议
- Agent 协作编排引擎：支持多个 AI Agent 之间的任务分配、调度和结果汇总
- 内置知识库系统：支持 RAG 增强检索和向量存储，增强 Agent 的领域知识
- TypeScript/React 现代技术栈：基于 React 18 + TypeScript 开发，支持插件化架构和主题定制

**适用场景**:
- 企业 AI 团队自动化运营：构建 7×24 小时运作的 AI Agent 团队，处理客户服务、数据分析、内容生成等任务
- AI 应用快速开发：使用现成的 Agent 框架和 MCP 生态快速构建 AI 应用，无需从零开发底层能力
- 个人 AI 工作流编排：个人开发者可以将多个 AI 助手串联成自动化工作流，提升个人生产力



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,819 |
| 语言 | TypeScript |
| Forks | 6,611 |
| Issues | 165 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现跨会话持久化上下文管理，解决了 AI Agent 无法保留历史记忆的核心痛点，支持 7+ 主流 AI 编程工具（Stars 76,819 验证了其极高的社区认可度和实用性）。

**技术亮点**:
- AI 驱动的语义压缩：自动分析会话内容并提取关键信息，有效降低存储成本
- 多 Agent 平台兼容：支持 Claude Code、Copilot、Codex、Gemini 等 7+ 主流 AI 编程工具
- RAG + Embeddings 技术栈：结合检索增强生成和向量嵌入实现精准上下文召回
- 本地化存储方案：支持 SQLite 和 ChromaDB，兼顾轻量与高性能
- Apache 2.0 开源许可：允许商业使用，降低企业采纳门槛

**适用场景**:
- 企业级 AI 开发团队：需要 AI 编程助手记住项目上下文、编码规范和历史决策的大型项目开发
- 复杂多阶段任务处理：需要 AI Agent 跨天/跨周持续工作的研究、数据分析或自动化流程
- 个人开发者效率提升：让 AI 编程助手记住个人偏好、项目架构和技术栈，避免重复解释



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,535 |
| 语言 | HTML |
| Forks | 21,154 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,844 |
| 语言 | HTML |
| Forks | 5,389 |
| Issues | 16 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,305 |
| 语言 | JavaScript |
| Forks | 6,518 |
| Issues | 355 |
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
| Stars | 74,161 |
| 语言 | Python |
| Forks | 9,401 |
| Issues | 409 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,574 |
| 语言 | TypeScript |
| Forks | 4,754 |
| Issues | 590 |
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
| Stars | 52,934 |
| 语言 | TypeScript |
| Forks | 24,360 |
| Issues | 861 |
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
| Stars | 80,491 |
| 语言 | Python |
| Forks | 16,972 |
| Issues | 5,039 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### ChatGPTNextWeb/NextChat

**描述**: ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android |  Linux | Windows

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,052 |
| 语言 | TypeScript |
| Forks | 59,704 |
| Issues | 824 |
| Topics | calclaude, chatgpt, claude, cross-platform, desktop, fe, gemini, gemini-pro, gemini-server, gemini-ultra, gpt-4o, groq, nextjs, ollama, react, tauri, tauri-app, vercel, webui |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,522 |
| 语言 | Python |
| Forks | 9,048 |
| Issues | 927 |
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
| Stars | 60,674 |
| 语言 | Python |
| Forks | 6,604 |
| Issues | 648 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,753 |
| 语言 | Go |
| Forks | 16,188 |
| Issues | 3,264 |
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
| Stars | 61,359 |
| 语言 | TypeScript |
| Forks | 10,033 |
| Issues | 131 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
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
| Stars | 123,833 |
| 语言 | Python |
| Forks | 8,396 |
| Issues | 658 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (8 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,413 |
| 语言 | Python |
| Forks | 8,719 |
| Issues | 1,018 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |


### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,794 |
| 语言 | Python |
| Forks | 6,830 |
| Issues | 82 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,535 |
| 语言 | HTML |
| Forks | 21,154 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,177 |
| 语言 | Jupyter Notebook |
| Forks | 14,575 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, attention-mechanism, deep-learning, finetuning, from-scratch, generative-ai, gpt, instruction-tuning, language-model, large-language-models, llm, machine-learning, natural-language-processing, pretraining, python, pytorch, tokenizer, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,784 |
| 语言 | Python |
| Forks | 33,272 |
| Issues | 2,348 |
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
| Stars | 80,491 |
| 语言 | Python |
| Forks | 16,972 |
| Issues | 5,039 |
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
| Stars | 113,582 |
| 语言 | Python |
| Forks | 13,300 |
| Issues | 4,032 |
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
| Stars | 100,017 |
| 语言 | Python |
| Forks | 27,818 |
| Issues | 18,474 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (18 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,131 |
| 语言 | JavaScript |
| Forks | 28,975 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Codex、Cursor 等主流工具，通过 Skills、Memory、Security 等模块显著提升 AI 辅助编程的效率与安全性，特别适合追求高效 AI 编程工作流的开发者。

**技术亮点**:
- 支持多平台 AI 代理（Claude Code、Codex、Opencode、Cursor 等），提供统一优化接口
- 基于 MCP（Model Context Protocol）实现标准化的代理交互协议
- Memory 模块支持持久化上下文记忆，增强代理状态管理能力
- Security 模块提供安全沙箱机制，保障代码执行安全
- Skills & Instincts 系统实现可扩展的技能注入与本能行为优化

**适用场景**:
- 企业级 AI 辅助开发：团队可部署 ECC 统一管理多个 AI 编码工具，优化开发工作流
- 个人开发者效率提升：通过 Memory 和 Skills 模块定制个人化的 AI 编程助手
- AI 代理研究与实验：研究人员可基于 ECC 框架进行代理性能对比与优化研究
- 安全敏感场景开发：利用 Security 模块在沙箱环境中测试 AI 生成的代码



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,360 |
| 语言 | Go |
| Forks | 4,091 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型类型，无需 GPU 即可在各类硬件上部署，特别适合需要数据隐私保护和降低云服务成本的场景。

**技术亮点**:
- 多模态模型支持：同时支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成和目标检测等多种模型类型
- CPU 友好架构：无需 GPU 即可运行 AI 模型，降低硬件门槛，支持在各类硬件上部署
- Go 语言开发：利用 Go 的高性能和并发特性，提供高效的推理性能
- 去中心化架构：集成 libp2p 支持分布式部署，可构建去中心化 AI 网络
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，便于现有应用快速迁移和集成

**适用场景**:
- 数据隐私敏感场景：企业或个人需要本地处理敏感数据（如医疗记录、财务信息），避免数据上传到第三方云服务
- 资源受限环境：在没有强大 GPU 的服务器或个人电脑上运行 AI 模型，适合开发者学习和实验
- AI 服务本地化部署：构建私有化的 AI API 服务，为内部应用提供 LLM、图像生成等能力，支持定制化需求



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,327 |
| 语言 | Java |
| Forks | 16,000 |
| Issues | 24 |
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
| Stars | 74,161 |
| 语言 | Python |
| Forks | 9,401 |
| Issues | 409 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,574 |
| 语言 | TypeScript |
| Forks | 4,754 |
| Issues | 590 |
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
| Stars | 188,730 |
| 语言 | TypeScript |
| Forks | 57,828 |
| Issues | 1,495 |
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
| Stars | 60,674 |
| 语言 | Python |
| Forks | 6,604 |
| Issues | 648 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,234 |
| 语言 | JavaScript |
| Forks | 4,216 |
| Issues | 1,178 |
| Topics | dark-mode, editor, electron, focus-mode, latex, linux, mac, macos, markdown, marktext, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,897 |
| 语言 | Python |
| Forks | 47,784 |
| Issues | 1,344 |
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
| Stars | 163,190 |
| 语言 | Python |
| Forks | 13,698 |
| Issues | 2,509 |
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
| Stars | 98,350 |
| 语言 | Python |
| Forks | 9,320 |
| Issues | 186 |
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
| Stars | 83,504 |
| 语言 | Python |
| Forks | 9,751 |
| Issues | 270 |
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
| Stars | 185,102 |
| 语言 | TypeScript |
| Forks | 39,973 |
| Issues | 17,766 |
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
| Stars | 94,343 |
| 语言 | TypeScript |
| Forks | 9,421 |
| Issues | 257 |
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
| Stars | 79,226 |
| 语言 | TypeScript |
| Forks | 5,882 |
| Issues | 733 |
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
| Stars | 80,363 |
| 语言 | Go |
| Forks | 2,807 |
| Issues | 318 |
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
| Stars | 78,152 |
| 语言 | Go |
| Forks | 2,842 |
| Issues | 964 |
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
| Stars | 44,476 |
| 语言 | Go |
| Forks | 8,453 |
| Issues | 1,012 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,574 |
| 语言 | TypeScript |
| Forks | 4,754 |
| Issues | 590 |
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
| Stars | 188,730 |
| 语言 | TypeScript |
| Forks | 57,828 |
| Issues | 1,495 |
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
| Stars | 60,674 |
| 语言 | Python |
| Forks | 6,604 |
| Issues | 648 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,706 |
| 语言 | Go |
| Forks | 10,363 |
| Issues | 240 |
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
| Stars | 122,354 |
| 语言 | Go |
| Forks | 43,104 |
| Issues | 2,707 |
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
| Stars | 71,574 |
| 语言 | Go |
| Forks | 18,953 |
| Issues | 3,765 |
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
| Stars | 55,785 |
| 语言 | Go |
| Forks | 6,709 |
| Issues | 2,792 |
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
| Stars | 47,526 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 986 |
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
| Stars | 94,343 |
| 语言 | TypeScript |
| Forks | 9,421 |
| Issues | 257 |
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
| Stars | 78,970 |
| 语言 | TypeScript |
| Forks | 6,916 |
| Issues | 410 |
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
| Stars | 86,992 |
| 语言 | JavaScript |
| Forks | 7,875 |
| Issues | 749 |
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
| Stars | 70,397 |
| 语言 | Go |
| Forks | 1,927 |
| Issues | 327 |
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
| Stars | 63,224 |
| 语言 | Go |
| Forks | 6,003 |
| Issues | 830 |
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
| Stars | 59,788 |
| 语言 | Go |
| Forks | 4,380 |
| Issues | 25 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,960 |
| 语言 | Go |
| Forks | 7,512 |
| Issues | 81 |
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
| Stars | 86,992 |
| 语言 | JavaScript |
| Forks | 7,875 |
| Issues | 749 |
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
| Stars | 64,091 |
| 语言 | Go |
| Forks | 10,417 |
| Issues | 771 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (12 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,360 |
| 语言 | Go |
| Forks | 4,091 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像和视频等多种模型类型，无需 GPU 即可在各类硬件上部署，特别适合需要数据隐私保护和降低云服务成本的场景。

**技术亮点**:
- 多模态模型支持：同时支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS）、音频生成和目标检测等多种模型类型
- CPU 友好架构：无需 GPU 即可运行 AI 模型，降低硬件门槛，支持在各类硬件上部署
- Go 语言开发：利用 Go 的高性能和并发特性，提供高效的推理性能
- 去中心化架构：集成 libp2p 支持分布式部署，可构建去中心化 AI 网络
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，便于现有应用快速迁移和集成

**适用场景**:
- 数据隐私敏感场景：企业或个人需要本地处理敏感数据（如医疗记录、财务信息），避免数据上传到第三方云服务
- 资源受限环境：在没有强大 GPU 的服务器或个人电脑上运行 AI 模型，适合开发者学习和实验
- AI 服务本地化部署：构建私有化的 AI API 服务，为内部应用提供 LLM、图像生成等能力，支持定制化需求



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,897 |
| 语言 | Python |
| Forks | 47,784 |
| Issues | 1,344 |
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
| Stars | 98,350 |
| 语言 | Python |
| Forks | 9,320 |
| Issues | 186 |
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
| Stars | 87,510 |
| 语言 | Python |
| Forks | 33,934 |
| Issues | 443 |
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
| Stars | 100,122 |
| 语言 | TypeScript |
| Forks | 27,231 |
| Issues | 1,152 |
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
| Stars | 79,226 |
| 语言 | TypeScript |
| Forks | 5,882 |
| Issues | 733 |
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
| Stars | 69,046 |
| 语言 | JavaScript |
| Forks | 23,382 |
| Issues | 209 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,194 |
| Issues | 375 |
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
| Stars | 51,877 |
| 语言 | JavaScript |
| Forks | 4,725 |
| Issues | 1,480 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,585 |
| 语言 | Go |
| Forks | 4,749 |
| Issues | 256 |
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
| Stars | 58,432 |
| 语言 | Go |
| Forks | 3,384 |
| Issues | 18 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,537 |
| 语言 | Go |
| Forks | 8,609 |
| Issues | 688 |
| Topics | framework, gin, go, middleware, performance, router, server |
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
| Stars | 102,696 |
| 语言 | TypeScript |
| Forks | 12,472 |
| Issues | 1,013 |
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
| Stars | 60,305 |
| 语言 | JavaScript |
| Forks | 6,518 |
| Issues | 355 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,362 |
| 语言 | Go |
| Forks | 4,007 |
| Issues | 903 |
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
| Stars | 51,706 |
| 语言 | Go |
| Forks | 10,363 |
| Issues | 240 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,271 |
| 语言 | JavaScript |
| Forks | 3,481 |
| Issues | 211 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 是一个通过「穴居人语言风格」实现 Token 消耗降低 65% 的 Claude Code 技能，项目已获得 62,271 Stars 的社区认可，是将 meme 文化与实际工程价值完美结合的 Prompt 工程创新方案。

**技术亮点**:
- 语言压缩技术：通过简化词汇和语法结构，将复杂表达压缩为简洁的穴居人风格，有效减少 token 计数
- Claude Code 技能集成：作为 Claude Code 的官方 skill 扩展，无缝接入 AI 辅助编程工作流
- 65% Token 节省：实测可显著降低 API 调用成本，适用于大规模 LLM 应用场景
- 零依赖实现：纯 JavaScript 实现，代码轻量且易于理解和修改
- Prompt 工程典范：展示了如何通过语言风格优化而非模型调参来提升效率

**适用场景**:
- 成本敏感型应用：需要频繁调用 LLM API 的项目，通过减少 token 消耗显著降低运营成本
- 开发测试环境：在不影响核心功能的前提下，使用简化的交互方式加速开发迭代
- 批量任务处理：适用于需要大规模 LLM 调用的自动化脚本和数据处理流程
- 个人开发者/小团队：资源有限但需要高效利用 AI 能力的场景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,535 |
| 语言 | HTML |
| Forks | 21,154 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,379 |
| 语言 | Python |
| Forks | 6,214 |
| Issues | 113 |
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
| Stars | 61,359 |
| 语言 | TypeScript |
| Forks | 10,033 |
| Issues | 131 |
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
| Stars | 89,952 |
| 语言 | TypeScript |
| Forks | 10,062 |
| Issues | 2,105 |
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
| Stars | 88,161 |
| 语言 | TypeScript |
| Forks | 8,994 |
| Issues | 1,667 |
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
| Stars | 127,865 |
| 语言 | JavaScript |
| Forks | 12,487 |
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
| Stars | 173,077 |
| 语言 | Go |
| Forks | 13,230 |
| Issues | 184 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (59 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,853 |
| 语言 | Unknown |
| Forks | 34,381 |
| Issues | 145 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### mattpocock/skills

**描述**: Skills for Real Engineers. Straight from my .claude directory.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,185 |
| 语言 | Shell |
| Forks | 8,285 |
| Issues | 30 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 103,118 |
| 语言 | Python |
| Forks | 9,066 |
| Issues | 428 |
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
| Stars | 93,151 |
| 语言 | Python |
| Forks | 13,560 |
| Issues | 118 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
| 许可证 | GNU Affero General Public License v3.0 |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 388,585 |
| 语言 | Python |
| Forks | 66,310 |
| Issues | 79 |
| Topics | books, education, hacktoberfest, list, resource |
| 许可证 | Creative Commons Attribution 4.0 International |


### clash-verge-rev/clash-verge-rev

**描述**: A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 119,309 |
| 语言 | TypeScript |
| Forks | 8,685 |
| Issues | 338 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### iptv-org/iptv

**描述**: Collection of publicly available IPTV channels from all over the world

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,339 |
| 语言 | TypeScript |
| Forks | 6,144 |
| Issues | 12 |
| Topics | iptv, m3u, playlist, streams, tv |
| 许可证 | The Unlicense |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,512 |
| 语言 | TypeScript |
| Forks | 14,836 |
| Issues | 552 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,132 |
| 语言 | JavaScript |
| Forks | 5,366 |
| Issues | 70 |
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
| Stars | 48,428 |
| 语言 | Go |
| Forks | 10,353 |
| Issues | 1,903 |
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
| Stars | 111,421 |
| 语言 | C++ |
| Forks | 18,440 |
| Issues | 1,681 |
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
| Stars | 63,272 |
| 语言 | Python |
| Forks | 1,673 |
| Issues | 36 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### abhigyanpatwari/GitNexus

**描述**: GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,059 |
| 语言 | TypeScript |
| Forks | 4,473 |
| Issues | 323 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 298,555 |
| 语言 | Python |
| Forks | 27,940 |
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
| Stars | 221,204 |
| 语言 | Python |
| Forks | 50,663 |
| Issues | 920 |
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
| Stars | 87,126 |
| 语言 | Python |
| Forks | 37,525 |
| Issues | 4,177 |
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
| Stars | 77,665 |
| 语言 | Python |
| Forks | 45,089 |
| Issues | 1,287 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 445,154 |
| 语言 | TypeScript |
| Forks | 44,628 |
| Issues | 181 |
| Topics | careers, certification, community, curriculum, d3, education, freecodecamp, javascript, learn-to-code, math, nodejs, nonprofits, programming, react, teachers |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### nilbuild/developer-roadmap

**描述**: Interactive roadmaps, guides and other educational content to help developers grow in their careers.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 355,085 |
| 语言 | TypeScript |
| Forks | 44,089 |
| Issues | 6 |
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
| Stars | 123,620 |
| 语言 | TypeScript |
| Forks | 13,704 |
| Issues | 3,069 |
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
| Stars | 114,691 |
| 语言 | TypeScript |
| Forks | 8,853 |
| Issues | 1,926 |
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
| Stars | 108,916 |
| 语言 | TypeScript |
| Forks | 13,405 |
| Issues | 5,036 |
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
| Stars | 101,095 |
| 语言 | TypeScript |
| Forks | 5,647 |
| Issues | 658 |
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
| Stars | 98,080 |
| 语言 | TypeScript |
| Forks | 54,607 |
| Issues | 1,372 |
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
| Stars | 95,061 |
| 语言 | TypeScript |
| Forks | 5,243 |
| Issues | 89 |
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
| Stars | 85,932 |
| 语言 | TypeScript |
| Forks | 10,759 |
| Issues | 489 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,457 |
| 语言 | TypeScript |
| Forks | 7,609 |
| Issues | 35 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,706 |
| 语言 | TypeScript |
| Forks | 8,192 |
| Issues | 731 |
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
| Stars | 245,139 |
| 语言 | JavaScript |
| Forks | 51,081 |
| Issues | 1,300 |
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
| Stars | 117,298 |
| 语言 | JavaScript |
| Forks | 35,567 |
| Issues | 2,649 |
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
| Stars | 112,565 |
| 语言 | JavaScript |
| Forks | 36,378 |
| Issues | 462 |
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
| Stars | 109,072 |
| 语言 | JavaScript |
| Forks | 11,715 |
| Issues | 164 |
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
| Stars | 98,366 |
| 语言 | JavaScript |
| Forks | 32,635 |
| Issues | 1,533 |
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
| Stars | 95,784 |
| 语言 | JavaScript |
| Forks | 15,502 |
| Issues | 61 |
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
| Stars | 86,599 |
| 语言 | JavaScript |
| Forks | 4,917 |
| Issues | 994 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,455 |
| 语言 | JavaScript |
| Forks | 9,191 |
| Issues | 4 |
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
| Stars | 65,768 |
| 语言 | JavaScript |
| Forks | 9,354 |
| Issues | 195 |
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
| Stars | 64,794 |
| 语言 | JavaScript |
| Forks | 4,117 |
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
| Stars | 61,182 |
| 语言 | JavaScript |
| Forks | 5,676 |
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
| Stars | 59,844 |
| 语言 | JavaScript |
| Forks | 20,432 |
| Issues | 92 |
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
| Stars | 57,447 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 29 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,544 |
| 语言 | JavaScript |
| Forks | 11,639 |
| Issues | 261 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,342 |
| 语言 | JavaScript |
| Forks | 10,619 |
| Issues | 446 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,974 |
| 语言 | Go |
| Forks | 19,032 |
| Issues | 10,076 |
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
| Stars | 106,665 |
| 语言 | Go |
| Forks | 15,048 |
| Issues | 46 |
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
| Stars | 88,160 |
| 语言 | Go |
| Forks | 8,266 |
| Issues | 232 |
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
| Stars | 84,200 |
| 语言 | Go |
| Forks | 5,195 |
| Issues | 388 |
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
| Stars | 68,565 |
| 语言 | Go |
| Forks | 3,233 |
| Issues | 48 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,268 |
| 语言 | Go |
| Forks | 5,100 |
| Issues | 1,182 |
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
| Stars | 51,051 |
| 语言 | Go |
| Forks | 21,916 |
| Issues | 398 |
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
| Stars | 49,503 |
| 语言 | Go |
| Forks | 7,941 |
| Issues | 564 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### multica-ai/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 137,772 |
| 语言 | Unknown |
| Forks | 14,121 |
| Issues | 94 |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,808 |
| 语言 | Python |
| Forks | 16,977 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,235 |
| 语言 | JavaScript |
| Forks | 16,805 |
| Issues | 897 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,677 |
| 语言 | JavaScript |
| Forks | 4,623 |
| Issues | 104 |
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
| Stars | 61,235 |
| 语言 | JavaScript |
| Forks | 7,163 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,090 |
| 语言 | Go |
| Forks | 1,615 |
| Issues | 274 |
| 许可证 | MIT License |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,850 |
| 语言 | Go |
| Forks | 8,850 |
| Issues | 17 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 157,715 |
| 语言 | Python |
| Forks | 12,011 |
| Issues | 384 |
| Topics | awesome, github, hellogithub, python |
