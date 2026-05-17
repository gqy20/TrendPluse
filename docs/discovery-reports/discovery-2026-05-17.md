# 项目发现报告 (2026-05-17)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 123 |
| 去重移除 | 38 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 61 |

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
| Stars | 154,581 |
| 语言 | Python |
| Forks | 24,755 |
| Issues | 11,853 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个由知名开源 LLM 研究团队打造的 AI Agent 框架，支持 OpenAI、Anthropic Claude 等多平台 LLM 集成，拥有超过 15 万星标的高人气，MIT 许可证友好，适合构建企业级智能代理应用。

**技术亮点**:
- 多 LLM 平台支持：无缝集成 OpenAI GPT 系列和 Anthropic Claude 系列等主流大语言模型
- 模块化 Agent 架构：采用可扩展的 agent 设计，支持自定义工具和插件
-  NousResearch 团队背书：由知名开源 LLM 研究团队开发，代码质量和维护有保障
- Python 原生实现：便于与现有 Python 生态（如 LangChain、PyTorch）集成
- 丰富的 Topic 生态：覆盖代码生成、对话系统、多 Agent 协作等多个领域

**适用场景**:
- 企业级智能客服与对话系统：基于多 LLM 支持构建稳定的企业级 AI 助手
- 开发者工具链集成：结合 Claude Code 和 Codex 实现代码审查、自动化测试等开发效率提升
- AI Agent 应用开发：构建自主执行复杂任务的多模态 AI 代理解决方案



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,488 |
| 语言 | Python |
| Forks | 19,633 |
| Issues | 284 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，支持 Ollama、OpenAI 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议扩展能力，13.7 万 Stars 验证了其成熟度和社区认可度，是企业或个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，实现零成本迁移和混合部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：可扩展的工具调用框架，方便集成外部工具和服务
- 自托管部署：支持 Docker 一键部署，数据完全私有化，满足安全合规需求
- 丰富的 UI 功能：支持多用户管理、会话历史、代码高亮、图片生成等完整功能

**适用场景**:
- 企业私有 AI 助手：部署在内网环境，处理敏感业务数据（如客服、内部知识问答）
- 个人开发者本地 LLM 调试：配合 Ollama 本地运行，零成本测试和调优大语言模型
- AI 应用快速原型开发：基于现有界面二次开发，快速交付 AI 产品 Demo



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,667 |
| 语言 | Python |
| Forks | 9,228 |
| Issues | 3,023 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 项目之一（80k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，为 LLM 提供高质量的上下文理解和精准检索，特别适合构建企业级知识问答和智能助手系统。

**技术亮点**:
- 采用 Graph-based RAG 架构，通过知识图谱增强检索的语义关联性和准确性
- 支持多模态文档理解，能够处理 PDF、Word、Excel、图片等多种格式的复杂文档
- 内置 Agent Framework，支持 Tool Calling 和多轮对话推理能力
- 提供可视化知识库管理界面，支持自定义分块策略和向量化配置
- 兼容主流 LLM API（OpenAI、Claude、本地模型），部署灵活度高

**适用场景**:
- 企业级智能客服：构建基于私有知识库的自然语言问答系统，支持复杂多轮对话
- 文档智能分析：自动处理和理解大量技术文档、合同、报告等非结构化数据
- RAG 应用快速开发：为开发者提供完整的 RAG  pipeline，降低 LLM 应用开发门槛



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,998 |
| 语言 | TypeScript |
| Forks | 7,391 |
| Issues | 322 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 时代设计的网页数据提取工具，能将任意网页智能转换为 LLM 可直接使用的 Markdown 格式，是构建 RAG 系统、AI Agents 和数据管道的利器，在 GitHub 拥有超过 12 万星标，社区活跃度极高。

**技术亮点**:
- 专为 AI Agents 设计的数据提取管道，支持网页搜索、爬取和清洗的一站式解决方案
- HTML 转 Markdown 高质量转换，保留关键语义信息的同时去除噪音，输出格式对 LLM 友好
- 智能内容提取技术，自动识别网页主体内容并过滤广告、导航栏等干扰元素
- 支持批量爬取和增量更新，提供完整的错误处理和重试机制
- TypeScript/Node.js 原生实现，支持 Python SDK，易于集成到现有 AI 应用架构

**适用场景**:
- 构建 RAG（检索增强生成）系统：为 LLM 提供实时、可靠的网络数据作为知识库上下文
- AI Agents 开发：让智能体能够自主搜索和获取最新网络信息，扩展其能力边界
- AI 数据管道搭建：批量抓取和清洗网页数据，用于模型训练或数据分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 185,523 |
| 语言 | JavaScript |
| Forks | 28,701 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理打造的性能优化系统框架，Stars 高达 18.5 万，证明了其在开发者社区的巨大影响力。它为 Claude Code、Codex、Cursor 等主流 AI 编码工具提供了统一的能力扩展接口，是目前最完整的 AI Agent 性能优化解决方案之一。

**技术亮点**:
- 创新的 Skills 和 Instincts 机制：允许开发者为 AI 代理添加自定义技能和本能反应，提升代理的任务执行能力
- Memory 记忆系统：实现持久化上下文管理，让 AI 代理能够跨会话保持状态和记忆
- Security 安全模块：内置多层安全防护机制，确保 AI 代理操作的可靠性和数据安全
- 多代理兼容性：同时支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- MCP (Model Context Protocol) 支持：遵循标准化协议，实现与其他工具和服务的无缝集成

**适用场景**:
- 个人开发者提升编程效率：通过自定义 Skills 扩展 AI 编码助手的能力，实现更高效的代码编写和调试
- 企业级 AI 开发平台建设：利用该框架构建统一的 AI 代理管理平台，实现代码审查、自动测试、文档生成等流程自动化
- AI Agent 研究与实验：作为实验平台，快速测试和验证新的 AI Agent 优化策略和技巧



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,311 |
| 语言 | Go |
| Forks | 4,086 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个开源的本地 AI 引擎，支持在普通硬件（无需 GPU）上运行 LLM、视觉、语音、图像等多种模型，Stars 高达 46k+，社区活跃。相较于 OpenAI API 等云端方案，它提供了完全本地化、数据隐私保护、低成本的替代方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- **多模型支持**：兼容 llama、mamba、stable-diffusion、musicgen 等多种开源模型，覆盖文本、图像、音频、视频生成及对象检测等场景
- **无 GPU 运行**：可在 CPU 和普通硬件上运行 AI 模型，降低了部署门槛和成本
- **Go 语言开发**：高性能、跨平台（Linux/macOS/Windows），易于集成到现有系统
- **去中心化架构**：基于 libp2p 实现分布式计算，支持 P2P 网络部署
- **API 优先设计**：通过 RESTful API 提供模型调用，支持 MCP 协议，可快速替换 OpenAI API 兼容应用

**适用场景**:
- **企业私有化部署**：需要数据隐私合规（如医疗、金融、法律文档处理），或内网隔离环境的 AI 应用开发
- **离线/边缘计算**：无网络连接或网络受限的场景（如工厂设备、偏远地区终端），需要本地运行 AI 推理
- **成本优化场景**：中小团队或个人开发者希望以极低成本使用 AI 能力，避免云端 API 的持续计费



### lobehub/lobehub

**描述**: LobeHub organizes your agents into 7×24 operation. It hires, schedules, reports on your entire AI team. You stay in charge — without staying online.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,205 |
| 语言 | TypeScript |
| Forks | 15,197 |
| Issues | 805 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 管理平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多模型集成，并通过 MCP 协议实现 Agent 编排与自动化运营，适合需要管理多个 AI 智能体团队的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的管理接口
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具/数据的标准化集成
- 7×24 自动运营系统：自动化调度、排班和报告生成，减少人工干预
- 知识库集成：内置知识库管理功能，支持 RAG 增强检索
- TypeScript + React 现代技术栈：采用 TypeScript 开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业级 AI 团队管理：集中管理多个 AI Agent，实现 7×24 自动化运营和监控
- 多模型应用开发：统一集成多种大语言模型，简化多模型切换和对比测试
- 智能运维自动化：AI Agent 协作完成报告生成、数据分析等周期性任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,365 |
| 语言 | TypeScript |
| Forks | 6,550 |
| Issues | 116 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现了 AI Agent 的长期记忆能力，解决了大模型上下文窗口限制与长期任务需求之间的矛盾，同时支持 8+ 种主流 AI Agent，通用性极强。凭借 7.6 万 Stars 的社区认可，是构建智能 Agent 系统的关键基础设施。

**技术亮点**:
- **多后端存储架构**：支持 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储引擎，可根据隐私需求和数据规模灵活选择
- **AI 驱动的上下文压缩**：利用 AI 算法对会话历史进行智能压缩，在保持关键信息的同时最大化利用有限的上下文窗口
- **RAG + Embeddings 技术栈**：采用检索增强生成和向量嵌入技术，确保注入的上下文高度相关且精准
- **广泛的 Agent 兼容性**：原生支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI Agent，覆盖个人开发者到企业用户的各类工具链
- **TypeScript 原生实现**：与现代开发工作流深度集成，提供良好的类型安全和开发体验

**适用场景**:
- **个人开发者的 AI 编程助手**：让 Claude Code/Copilot 等工具记住项目架构、代码风格偏好和未完成的任务，实现真正的连续性编程体验
- **企业级 Agent 系统**：构建具备长期记忆能力的客服机器人或业务流程自动化 Agent，通过私有化部署确保数据安全
- **复杂多会话任务处理**：如代码审查、技术文档编写、架构设计等需要跨多天、多轮迭代的长周期任务



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,339 |
| 语言 | Python |
| Forks | 8,714 |
| Issues | 1,017 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是最受欢迎的大模型微调框架，支持100+ LLMs和VLMs的统一高效微调，已被ACL 2024录用，为企业和研究者提供了从模型选择到部署的完整微调解决方案，极大降低了LLM微调的技术门槛。

**技术亮点**:
- 统一微调框架：支持100+主流大语言模型和视觉语言模型，包括LLaMA、Qwen、DeepSeek、Gemma等
- 多样化高效微调技术：集成LoRA、QLoRA、PEFT等参数高效微调方法，大幅降低显存占用
- 完整训练范式支持：涵盖SFT、RLHF、DPO等多种训练策略
- 模型量化与MoE支持：内置量化技术降低推理成本，同时支持混合专家模型微调
- ACL 2024学术认可：研究成果获得顶级学术会议认证，技术方案经过严格同行评审

**适用场景**:
- 企业级AI应用开发：针对业务场景定制专属大模型（如客服机器人、文档分析、内容生成等）的企业团队
- 学术研究与模型实验：NLP/AI研究者快速验证新模型架构或训练方法，降低实验迭代成本
- 个人开发者与AI爱好者：具备技术背景的开发者想要微调开源模型构建个性化AI助手或垂直领域应用
- 低成本模型定制：资源有限但需要进行大模型微调的个人或组织，通过QLoRA等技术实现消费级GPU训练



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,480 |
| 语言 | Python |
| Forks | 14,897 |
| Issues | 344 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,960 |
| 语言 | TypeScript |
| Forks | 9,971 |
| Issues | 128 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,416 |
| 语言 | HTML |
| Forks | 5,351 |
| Issues | 15 |
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
| Stars | 50,394 |
| 语言 | Python |
| Forks | 6,090 |
| Issues | 111 |
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
| Stars | 46,298 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 21 |
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
| Stars | 52,301 |
| 语言 | TypeScript |
| Forks | 5,909 |
| Issues | 552 |
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
| Stars | 60,174 |
| 语言 | JavaScript |
| Forks | 6,513 |
| Issues | 364 |
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
| Stars | 73,874 |
| 语言 | Python |
| Forks | 9,355 |
| Issues | 416 |
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
| Stars | 58,251 |
| 语言 | TypeScript |
| Forks | 4,724 |
| Issues | 568 |
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
| Stars | 39,182 |
| 语言 | Python |
| Forks | 6,209 |
| Issues | 83 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,835 |
| 语言 | Python |
| Forks | 16,433 |
| Issues | 5 |
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
| Stars | 94,315 |
| 语言 | Python |
| Forks | 10,650 |
| Issues | 230 |
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
| Stars | 52,884 |
| 语言 | TypeScript |
| Forks | 24,352 |
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
| Stars | 188,352 |
| 语言 | TypeScript |
| Forks | 57,734 |
| Issues | 1,484 |
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
| Stars | 155,730 |
| 语言 | JavaScript |
| Forks | 46,134 |
| Issues | 61 |
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
| Stars | 148,372 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 920 |
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
| Stars | 62,407 |
| 语言 | Jupyter Notebook |
| Forks | 21,011 |
| Issues | 8 |
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
| Stars | 73,432 |
| 语言 | Rust |
| Forks | 4,768 |
| Issues | 885 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,295 |
| 语言 | Python |
| Forks | 6,561 |
| Issues | 641 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


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
| Stars | 137,488 |
| 语言 | Python |
| Forks | 19,633 |
| Issues | 284 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，支持 Ollama、OpenAI 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议扩展能力，13.7 万 Stars 验证了其成熟度和社区认可度，是企业或个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，实现零成本迁移和混合部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：可扩展的工具调用框架，方便集成外部工具和服务
- 自托管部署：支持 Docker 一键部署，数据完全私有化，满足安全合规需求
- 丰富的 UI 功能：支持多用户管理、会话历史、代码高亮、图片生成等完整功能

**适用场景**:
- 企业私有 AI 助手：部署在内网环境，处理敏感业务数据（如客服、内部知识问答）
- 个人开发者本地 LLM 调试：配合 Ollama 本地运行，零成本测试和调优大语言模型
- AI 应用快速原型开发：基于现有界面二次开发，快速交付 AI 产品 Demo



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,667 |
| 语言 | Python |
| Forks | 9,228 |
| Issues | 3,023 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 项目之一（80k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，为 LLM 提供高质量的上下文理解和精准检索，特别适合构建企业级知识问答和智能助手系统。

**技术亮点**:
- 采用 Graph-based RAG 架构，通过知识图谱增强检索的语义关联性和准确性
- 支持多模态文档理解，能够处理 PDF、Word、Excel、图片等多种格式的复杂文档
- 内置 Agent Framework，支持 Tool Calling 和多轮对话推理能力
- 提供可视化知识库管理界面，支持自定义分块策略和向量化配置
- 兼容主流 LLM API（OpenAI、Claude、本地模型），部署灵活度高

**适用场景**:
- 企业级智能客服：构建基于私有知识库的自然语言问答系统，支持复杂多轮对话
- 文档智能分析：自动处理和理解大量技术文档、合同、报告等非结构化数据
- RAG 应用快速开发：为开发者提供完整的 RAG  pipeline，降低 LLM 应用开发门槛



### lobehub/lobehub

**描述**: LobeHub organizes your agents into 7×24 operation. It hires, schedules, reports on your entire AI team. You stay in charge — without staying online.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,205 |
| 语言 | TypeScript |
| Forks | 15,197 |
| Issues | 805 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 管理平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多模型集成，并通过 MCP 协议实现 Agent 编排与自动化运营，适合需要管理多个 AI 智能体团队的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的管理接口
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具/数据的标准化集成
- 7×24 自动运营系统：自动化调度、排班和报告生成，减少人工干预
- 知识库集成：内置知识库管理功能，支持 RAG 增强检索
- TypeScript + React 现代技术栈：采用 TypeScript 开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业级 AI 团队管理：集中管理多个 AI Agent，实现 7×24 自动化运营和监控
- 多模型应用开发：统一集成多种大语言模型，简化多模型切换和对比测试
- 智能运维自动化：AI Agent 协作完成报告生成、数据分析等周期性任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,365 |
| 语言 | TypeScript |
| Forks | 6,550 |
| Issues | 116 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现了 AI Agent 的长期记忆能力，解决了大模型上下文窗口限制与长期任务需求之间的矛盾，同时支持 8+ 种主流 AI Agent，通用性极强。凭借 7.6 万 Stars 的社区认可，是构建智能 Agent 系统的关键基础设施。

**技术亮点**:
- **多后端存储架构**：支持 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储引擎，可根据隐私需求和数据规模灵活选择
- **AI 驱动的上下文压缩**：利用 AI 算法对会话历史进行智能压缩，在保持关键信息的同时最大化利用有限的上下文窗口
- **RAG + Embeddings 技术栈**：采用检索增强生成和向量嵌入技术，确保注入的上下文高度相关且精准
- **广泛的 Agent 兼容性**：原生支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI Agent，覆盖个人开发者到企业用户的各类工具链
- **TypeScript 原生实现**：与现代开发工作流深度集成，提供良好的类型安全和开发体验

**适用场景**:
- **个人开发者的 AI 编程助手**：让 Claude Code/Copilot 等工具记住项目架构、代码风格偏好和未完成的任务，实现真正的连续性编程体验
- **企业级 Agent 系统**：构建具备长期记忆能力的客服机器人或业务流程自动化 Agent，通过私有化部署确保数据安全
- **复杂多会话任务处理**：如代码审查、技术文档编写、架构设计等需要跨多天、多轮迭代的长周期任务



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,394 |
| 语言 | Python |
| Forks | 6,090 |
| Issues | 111 |
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
| Stars | 46,298 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 21 |
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
| Stars | 102,556 |
| 语言 | TypeScript |
| Forks | 12,443 |
| Issues | 1,017 |
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
| Stars | 60,174 |
| 语言 | JavaScript |
| Forks | 6,513 |
| Issues | 364 |
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
| Stars | 39,182 |
| 语言 | Python |
| Forks | 6,209 |
| Issues | 83 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,835 |
| 语言 | Python |
| Forks | 16,433 |
| Issues | 5 |
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
| Stars | 78,001 |
| 语言 | Python |
| Forks | 10,442 |
| Issues | 207 |
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
| Stars | 52,884 |
| 语言 | TypeScript |
| Forks | 24,352 |
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
| Stars | 48,753 |
| 语言 | Python |
| Forks | 5,302 |
| Issues | 259 |
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
| Stars | 44,332 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 878 |
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
| Stars | 35,304 |
| 语言 | Python |
| Forks | 4,992 |
| Issues | 232 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (20 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,581 |
| 语言 | Python |
| Forks | 24,755 |
| Issues | 11,853 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个由知名开源 LLM 研究团队打造的 AI Agent 框架，支持 OpenAI、Anthropic Claude 等多平台 LLM 集成，拥有超过 15 万星标的高人气，MIT 许可证友好，适合构建企业级智能代理应用。

**技术亮点**:
- 多 LLM 平台支持：无缝集成 OpenAI GPT 系列和 Anthropic Claude 系列等主流大语言模型
- 模块化 Agent 架构：采用可扩展的 agent 设计，支持自定义工具和插件
-  NousResearch 团队背书：由知名开源 LLM 研究团队开发，代码质量和维护有保障
- Python 原生实现：便于与现有 Python 生态（如 LangChain、PyTorch）集成
- 丰富的 Topic 生态：覆盖代码生成、对话系统、多 Agent 协作等多个领域

**适用场景**:
- 企业级智能客服与对话系统：基于多 LLM 支持构建稳定的企业级 AI 助手
- 开发者工具链集成：结合 Claude Code 和 Codex 实现代码审查、自动化测试等开发效率提升
- AI Agent 应用开发：构建自主执行复杂任务的多模态 AI 代理解决方案



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,488 |
| 语言 | Python |
| Forks | 19,633 |
| Issues | 284 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完备的开源 AI 界面，支持 Ollama、OpenAI 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议扩展能力，13.7 万 Stars 验证了其成熟度和社区认可度，是企业或个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，实现零成本迁移和混合部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：可扩展的工具调用框架，方便集成外部工具和服务
- 自托管部署：支持 Docker 一键部署，数据完全私有化，满足安全合规需求
- 丰富的 UI 功能：支持多用户管理、会话历史、代码高亮、图片生成等完整功能

**适用场景**:
- 企业私有 AI 助手：部署在内网环境，处理敏感业务数据（如客服、内部知识问答）
- 个人开发者本地 LLM 调试：配合 Ollama 本地运行，零成本测试和调优大语言模型
- AI 应用快速原型开发：基于现有界面二次开发，快速交付 AI 产品 Demo



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 185,523 |
| 语言 | JavaScript |
| Forks | 28,701 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理打造的性能优化系统框架，Stars 高达 18.5 万，证明了其在开发者社区的巨大影响力。它为 Claude Code、Codex、Cursor 等主流 AI 编码工具提供了统一的能力扩展接口，是目前最完整的 AI Agent 性能优化解决方案之一。

**技术亮点**:
- 创新的 Skills 和 Instincts 机制：允许开发者为 AI 代理添加自定义技能和本能反应，提升代理的任务执行能力
- Memory 记忆系统：实现持久化上下文管理，让 AI 代理能够跨会话保持状态和记忆
- Security 安全模块：内置多层安全防护机制，确保 AI 代理操作的可靠性和数据安全
- 多代理兼容性：同时支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- MCP (Model Context Protocol) 支持：遵循标准化协议，实现与其他工具和服务的无缝集成

**适用场景**:
- 个人开发者提升编程效率：通过自定义 Skills 扩展 AI 编码助手的能力，实现更高效的代码编写和调试
- 企业级 AI 开发平台建设：利用该框架构建统一的 AI 代理管理平台，实现代码审查、自动测试、文档生成等流程自动化
- AI Agent 研究与实验：作为实验平台，快速测试和验证新的 AI Agent 优化策略和技巧



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,291 |
| 语言 | JavaScript |
| Forks | 3,410 |
| Issues | 205 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Prompt 工程实践，通过"穴居人语言"风格实现 65% 的 token 压缩，直接降低 LLM API 调用成本，同时保持输出质量不受影响，非常适合高频使用 AI 助手的开发者。

**技术亮点**:
- 革命性的 Prompt 压缩算法：通过简化的语言表达方式，将复杂的自然语言指令压缩至原来的 35%，大幅降低 token 消耗
- 专门针对 Claude 模型优化的提示词工程技术，利用模型对简洁指令的理解能力
- 零依赖的轻量级 JavaScript 实现，易于集成到现有 Claude Code 工作流中
- 保留原始 Prompt 的语义完整性，在压缩体积的同时不牺牲任务执行效果
- 基于 MIT 许可证开源，代码可自由使用、修改和商业化部署

**适用场景**:
- 企业级 AI 应用成本优化：大规模部署 Claude 等 LLM 服务的企业，通过 token 压缩显著降低 API 调用成本和延迟
- 个人开发者日常使用：频繁使用 Claude Code 的开发者可减少约 65% 的 token 消耗，降低个人使用成本
- 快速原型开发：在进行 AI 功能验证和原型迭代时，使用压缩后的 Prompt 可加快测试循环并节省资源
- 资源受限环境部署：在对 token 使用量有严格限制的边缘计算或移动端场景下特别有价值



### lobehub/lobehub

**描述**: LobeHub organizes your agents into 7×24 operation. It hires, schedules, reports on your entire AI team. You stay in charge — without staying online.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,205 |
| 语言 | TypeScript |
| Forks | 15,197 |
| Issues | 805 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的企业级 AI Agent 管理平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多模型集成，并通过 MCP 协议实现 Agent 编排与自动化运营，适合需要管理多个 AI 智能体团队的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的管理接口
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具/数据的标准化集成
- 7×24 自动运营系统：自动化调度、排班和报告生成，减少人工干预
- 知识库集成：内置知识库管理功能，支持 RAG 增强检索
- TypeScript + React 现代技术栈：采用 TypeScript 开发，具备良好的类型安全和可维护性

**适用场景**:
- 企业级 AI 团队管理：集中管理多个 AI Agent，实现 7×24 自动化运营和监控
- 多模型应用开发：统一集成多种大语言模型，简化多模型切换和对比测试
- 智能运维自动化：AI Agent 协作完成报告生成、数据分析等周期性任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,365 |
| 语言 | TypeScript |
| Forks | 6,550 |
| Issues | 116 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过 AI 压缩技术实现了 AI Agent 的长期记忆能力，解决了大模型上下文窗口限制与长期任务需求之间的矛盾，同时支持 8+ 种主流 AI Agent，通用性极强。凭借 7.6 万 Stars 的社区认可，是构建智能 Agent 系统的关键基础设施。

**技术亮点**:
- **多后端存储架构**：支持 ChromaDB、SQLite、Mem0、OpenMemory 等多种向量数据库和存储引擎，可根据隐私需求和数据规模灵活选择
- **AI 驱动的上下文压缩**：利用 AI 算法对会话历史进行智能压缩，在保持关键信息的同时最大化利用有限的上下文窗口
- **RAG + Embeddings 技术栈**：采用检索增强生成和向量嵌入技术，确保注入的上下文高度相关且精准
- **广泛的 Agent 兼容性**：原生支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI Agent，覆盖个人开发者到企业用户的各类工具链
- **TypeScript 原生实现**：与现代开发工作流深度集成，提供良好的类型安全和开发体验

**适用场景**:
- **个人开发者的 AI 编程助手**：让 Claude Code/Copilot 等工具记住项目架构、代码风格偏好和未完成的任务，实现真正的连续性编程体验
- **企业级 Agent 系统**：构建具备长期记忆能力的客服机器人或业务流程自动化 Agent，通过私有化部署确保数据安全
- **复杂多会话任务处理**：如代码审查、技术文档编写、架构设计等需要跨多天、多轮迭代的长周期任务



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,416 |
| 语言 | HTML |
| Forks | 21,142 |
| Issues | 45 |
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
| Stars | 94,994 |
| 语言 | Jupyter Notebook |
| Forks | 14,552 |
| Issues | 4 |
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
| Stars | 60,960 |
| 语言 | TypeScript |
| Forks | 9,971 |
| Issues | 128 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,416 |
| 语言 | HTML |
| Forks | 5,351 |
| Issues | 15 |
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
| Stars | 60,174 |
| 语言 | JavaScript |
| Forks | 6,513 |
| Issues | 364 |
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
| Stars | 73,874 |
| 语言 | Python |
| Forks | 9,355 |
| Issues | 416 |
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
| Stars | 58,251 |
| 语言 | TypeScript |
| Forks | 4,724 |
| Issues | 568 |
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
| Stars | 52,884 |
| 语言 | TypeScript |
| Forks | 24,352 |
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
| Stars | 80,268 |
| 语言 | Python |
| Forks | 16,875 |
| Issues | 4,983 |
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
| Stars | 88,026 |
| 语言 | TypeScript |
| Forks | 59,711 |
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
| Stars | 148,372 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 920 |
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
| Stars | 171,619 |
| 语言 | Go |
| Forks | 16,163 |
| Issues | 3,258 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,295 |
| 语言 | Python |
| Forks | 6,561 |
| Issues | 641 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 123,519 |
| 语言 | Python |
| Forks | 8,359 |
| Issues | 654 |
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
| Stars | 71,339 |
| 语言 | Python |
| Forks | 8,714 |
| Issues | 1,017 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是最受欢迎的大模型微调框架，支持100+ LLMs和VLMs的统一高效微调，已被ACL 2024录用，为企业和研究者提供了从模型选择到部署的完整微调解决方案，极大降低了LLM微调的技术门槛。

**技术亮点**:
- 统一微调框架：支持100+主流大语言模型和视觉语言模型，包括LLaMA、Qwen、DeepSeek、Gemma等
- 多样化高效微调技术：集成LoRA、QLoRA、PEFT等参数高效微调方法，大幅降低显存占用
- 完整训练范式支持：涵盖SFT、RLHF、DPO等多种训练策略
- 模型量化与MoE支持：内置量化技术降低推理成本，同时支持混合专家模型微调
- ACL 2024学术认可：研究成果获得顶级学术会议认证，技术方案经过严格同行评审

**适用场景**:
- 企业级AI应用开发：针对业务场景定制专属大模型（如客服机器人、文档分析、内容生成等）的企业团队
- 学术研究与模型实验：NLP/AI研究者快速验证新模型架构或训练方法，降低实验迭代成本
- 个人开发者与AI爱好者：具备技术背景的开发者想要微调开源模型构建个性化AI助手或垂直领域应用
- 低成本模型定制：资源有限但需要进行大模型微调的个人或组织，通过QLoRA等技术实现消费级GPU训练



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,706 |
| 语言 | Python |
| Forks | 6,813 |
| Issues | 81 |
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
| Stars | 162,416 |
| 语言 | HTML |
| Forks | 21,142 |
| Issues | 45 |
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
| Stars | 94,994 |
| 语言 | Jupyter Notebook |
| Forks | 14,552 |
| Issues | 4 |
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
| Stars | 160,695 |
| 语言 | Python |
| Forks | 33,238 |
| Issues | 2,356 |
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
| Stars | 80,268 |
| 语言 | Python |
| Forks | 16,875 |
| Issues | 4,983 |
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
| Stars | 113,305 |
| 语言 | Python |
| Forks | 13,271 |
| Issues | 4,019 |
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
| Stars | 99,962 |
| 语言 | Python |
| Forks | 27,810 |
| Issues | 18,516 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


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
| Stars | 185,523 |
| 语言 | JavaScript |
| Forks | 28,701 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理打造的性能优化系统框架，Stars 高达 18.5 万，证明了其在开发者社区的巨大影响力。它为 Claude Code、Codex、Cursor 等主流 AI 编码工具提供了统一的能力扩展接口，是目前最完整的 AI Agent 性能优化解决方案之一。

**技术亮点**:
- 创新的 Skills 和 Instincts 机制：允许开发者为 AI 代理添加自定义技能和本能反应，提升代理的任务执行能力
- Memory 记忆系统：实现持久化上下文管理，让 AI 代理能够跨会话保持状态和记忆
- Security 安全模块：内置多层安全防护机制，确保 AI 代理操作的可靠性和数据安全
- 多代理兼容性：同时支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- MCP (Model Context Protocol) 支持：遵循标准化协议，实现与其他工具和服务的无缝集成

**适用场景**:
- 个人开发者提升编程效率：通过自定义 Skills 扩展 AI 编码助手的能力，实现更高效的代码编写和调试
- 企业级 AI 开发平台建设：利用该框架构建统一的 AI 代理管理平台，实现代码审查、自动测试、文档生成等流程自动化
- AI Agent 研究与实验：作为实验平台，快速测试和验证新的 AI Agent 优化策略和技巧



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,311 |
| 语言 | Go |
| Forks | 4,086 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个开源的本地 AI 引擎，支持在普通硬件（无需 GPU）上运行 LLM、视觉、语音、图像等多种模型，Stars 高达 46k+，社区活跃。相较于 OpenAI API 等云端方案，它提供了完全本地化、数据隐私保护、低成本的替代方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- **多模型支持**：兼容 llama、mamba、stable-diffusion、musicgen 等多种开源模型，覆盖文本、图像、音频、视频生成及对象检测等场景
- **无 GPU 运行**：可在 CPU 和普通硬件上运行 AI 模型，降低了部署门槛和成本
- **Go 语言开发**：高性能、跨平台（Linux/macOS/Windows），易于集成到现有系统
- **去中心化架构**：基于 libp2p 实现分布式计算，支持 P2P 网络部署
- **API 优先设计**：通过 RESTful API 提供模型调用，支持 MCP 协议，可快速替换 OpenAI API 兼容应用

**适用场景**:
- **企业私有化部署**：需要数据隐私合规（如医疗、金融、法律文档处理），或内网隔离环境的 AI 应用开发
- **离线/边缘计算**：无网络连接或网络受限的场景（如工厂设备、偏远地区终端），需要本地运行 AI 推理
- **成本优化场景**：中小团队或个人开发者希望以极低成本使用 AI 能力，避免云端 API 的持续计费



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,298 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 21 |
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
| Stars | 73,874 |
| 语言 | Python |
| Forks | 9,355 |
| Issues | 416 |
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
| Stars | 58,251 |
| 语言 | TypeScript |
| Forks | 4,724 |
| Issues | 568 |
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
| Stars | 188,352 |
| 语言 | TypeScript |
| Forks | 57,734 |
| Issues | 1,484 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,168 |
| 语言 | JavaScript |
| Forks | 4,211 |
| Issues | 1,308 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,507 |
| 语言 | Python |
| Forks | 47,740 |
| Issues | 1,341 |
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
| Stars | 162,795 |
| 语言 | Python |
| Forks | 13,660 |
| Issues | 2,511 |
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
| Stars | 98,286 |
| 语言 | Python |
| Forks | 9,306 |
| Issues | 207 |
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
| Stars | 83,432 |
| 语言 | Python |
| Forks | 9,730 |
| Issues | 273 |
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
| Stars | 185,020 |
| 语言 | TypeScript |
| Forks | 39,916 |
| Issues | 17,614 |
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
| Stars | 94,336 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 258 |
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
| Stars | 79,200 |
| 语言 | TypeScript |
| Forks | 5,877 |
| Issues | 726 |
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
| Stars | 80,302 |
| 语言 | Go |
| Forks | 2,805 |
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
| Stars | 78,051 |
| 语言 | Go |
| Forks | 2,837 |
| Issues | 963 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,295 |
| 语言 | Python |
| Forks | 6,561 |
| Issues | 641 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


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
| Stars | 58,251 |
| 语言 | TypeScript |
| Forks | 4,724 |
| Issues | 568 |
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
| Stars | 188,352 |
| 语言 | TypeScript |
| Forks | 57,734 |
| Issues | 1,484 |
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
| Stars | 51,709 |
| 语言 | Go |
| Forks | 10,355 |
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
| Stars | 122,318 |
| 语言 | Go |
| Forks | 43,088 |
| Issues | 2,698 |
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
| Stars | 71,564 |
| 语言 | Go |
| Forks | 18,952 |
| Issues | 3,783 |
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
| Stars | 55,739 |
| 语言 | Go |
| Forks | 6,706 |
| Issues | 2,794 |
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
| Stars | 94,336 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 258 |
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
| Stars | 78,863 |
| 语言 | TypeScript |
| Forks | 6,906 |
| Issues | 402 |
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
| Stars | 86,905 |
| 语言 | JavaScript |
| Forks | 7,862 |
| Issues | 747 |
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
| Stars | 70,304 |
| 语言 | Go |
| Forks | 1,921 |
| Issues | 325 |
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
| Stars | 63,193 |
| 语言 | Go |
| Forks | 5,996 |
| Issues | 829 |
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
| Stars | 59,716 |
| 语言 | Go |
| Forks | 4,372 |
| Issues | 28 |
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
| Stars | 60,295 |
| 语言 | Python |
| Forks | 6,561 |
| Issues | 641 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,520 |
| 语言 | Go |
| Forks | 5,064 |
| Issues | 994 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,944 |
| 语言 | Go |
| Forks | 7,502 |
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
| Stars | 86,905 |
| 语言 | JavaScript |
| Forks | 7,862 |
| Issues | 747 |
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
| Stars | 64,085 |
| 语言 | Go |
| Forks | 10,412 |
| Issues | 775 |
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
| Stars | 46,311 |
| 语言 | Go |
| Forks | 4,086 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个开源的本地 AI 引擎，支持在普通硬件（无需 GPU）上运行 LLM、视觉、语音、图像等多种模型，Stars 高达 46k+，社区活跃。相较于 OpenAI API 等云端方案，它提供了完全本地化、数据隐私保护、低成本的替代方案，特别适合对数据安全和成本敏感的场景。

**技术亮点**:
- **多模型支持**：兼容 llama、mamba、stable-diffusion、musicgen 等多种开源模型，覆盖文本、图像、音频、视频生成及对象检测等场景
- **无 GPU 运行**：可在 CPU 和普通硬件上运行 AI 模型，降低了部署门槛和成本
- **Go 语言开发**：高性能、跨平台（Linux/macOS/Windows），易于集成到现有系统
- **去中心化架构**：基于 libp2p 实现分布式计算，支持 P2P 网络部署
- **API 优先设计**：通过 RESTful API 提供模型调用，支持 MCP 协议，可快速替换 OpenAI API 兼容应用

**适用场景**:
- **企业私有化部署**：需要数据隐私合规（如医疗、金融、法律文档处理），或内网隔离环境的 AI 应用开发
- **离线/边缘计算**：无网络连接或网络受限的场景（如工厂设备、偏远地区终端），需要本地运行 AI 推理
- **成本优化场景**：中小团队或个人开发者希望以极低成本使用 AI 能力，避免云端 API 的持续计费



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,507 |
| 语言 | Python |
| Forks | 47,740 |
| Issues | 1,341 |
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
| Stars | 98,286 |
| 语言 | Python |
| Forks | 9,306 |
| Issues | 207 |
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
| Stars | 87,495 |
| 语言 | Python |
| Forks | 33,888 |
| Issues | 428 |
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
| Stars | 100,114 |
| 语言 | TypeScript |
| Forks | 27,223 |
| Issues | 1,154 |
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
| Stars | 79,200 |
| 语言 | TypeScript |
| Forks | 5,877 |
| Issues | 726 |
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
| Stars | 69,033 |
| 语言 | JavaScript |
| Forks | 23,355 |
| Issues | 207 |
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
| Forks | 10,196 |
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
| Stars | 51,878 |
| 语言 | JavaScript |
| Forks | 4,721 |
| Issues | 1,487 |
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
| Stars | 72,528 |
| 语言 | Go |
| Forks | 4,740 |
| Issues | 251 |
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
| Stars | 58,389 |
| 语言 | Go |
| Forks | 3,375 |
| Issues | 17 |
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
| Stars | 88,518 |
| 语言 | Go |
| Forks | 8,608 |
| Issues | 687 |
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
| Stars | 102,556 |
| 语言 | TypeScript |
| Forks | 12,443 |
| Issues | 1,017 |
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
| Stars | 60,174 |
| 语言 | JavaScript |
| Forks | 6,513 |
| Issues | 364 |
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
| Stars | 44,332 |
| 语言 | Go |
| Forks | 4,002 |
| Issues | 878 |
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
| Stars | 51,709 |
| 语言 | Go |
| Forks | 10,355 |
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
| Stars | 61,291 |
| 语言 | JavaScript |
| Forks | 3,410 |
| Issues | 205 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Prompt 工程实践，通过"穴居人语言"风格实现 65% 的 token 压缩，直接降低 LLM API 调用成本，同时保持输出质量不受影响，非常适合高频使用 AI 助手的开发者。

**技术亮点**:
- 革命性的 Prompt 压缩算法：通过简化的语言表达方式，将复杂的自然语言指令压缩至原来的 35%，大幅降低 token 消耗
- 专门针对 Claude 模型优化的提示词工程技术，利用模型对简洁指令的理解能力
- 零依赖的轻量级 JavaScript 实现，易于集成到现有 Claude Code 工作流中
- 保留原始 Prompt 的语义完整性，在压缩体积的同时不牺牲任务执行效果
- 基于 MIT 许可证开源，代码可自由使用、修改和商业化部署

**适用场景**:
- 企业级 AI 应用成本优化：大规模部署 Claude 等 LLM 服务的企业，通过 token 压缩显著降低 API 调用成本和延迟
- 个人开发者日常使用：频繁使用 Claude Code 的开发者可减少约 65% 的 token 消耗，降低个人使用成本
- 快速原型开发：在进行 AI 功能验证和原型迭代时，使用压缩后的 Prompt 可加快测试循环并节省资源
- 资源受限环境部署：在对 token 使用量有严格限制的边缘计算或移动端场景下特别有价值



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,416 |
| 语言 | HTML |
| Forks | 21,142 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,960 |
| 语言 | TypeScript |
| Forks | 9,971 |
| Issues | 128 |
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
| Stars | 50,394 |
| 语言 | Python |
| Forks | 6,090 |
| Issues | 111 |
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
| Stars | 89,921 |
| 语言 | TypeScript |
| Forks | 10,061 |
| Issues | 2,210 |
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
| Stars | 88,101 |
| 语言 | TypeScript |
| Forks | 8,980 |
| Issues | 1,670 |
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
| Stars | 127,844 |
| 语言 | JavaScript |
| Forks | 12,489 |
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
| Stars | 172,904 |
| 语言 | Go |
| Forks | 13,217 |
| Issues | 184 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (61 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,574 |
| 语言 | Unknown |
| Forks | 34,283 |
| Issues | 143 |
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
| Stars | 88,662 |
| 语言 | Shell |
| Forks | 7,740 |
| Issues | 37 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,433 |
| 语言 | Python |
| Forks | 8,897 |
| Issues | 425 |
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
| Stars | 93,082 |
| 语言 | Python |
| Forks | 13,546 |
| Issues | 112 |
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
| Stars | 388,464 |
| 语言 | Python |
| Forks | 66,306 |
| Issues | 83 |
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
| Stars | 118,742 |
| 语言 | TypeScript |
| Forks | 8,648 |
| Issues | 324 |
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
| Stars | 116,281 |
| 语言 | TypeScript |
| Forks | 6,141 |
| Issues | 22 |
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
| Stars | 98,474 |
| 语言 | TypeScript |
| Forks | 14,657 |
| Issues | 518 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,720 |
| 语言 | JavaScript |
| Forks | 5,329 |
| Issues | 58 |
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
| Stars | 48,413 |
| 语言 | Go |
| Forks | 10,351 |
| Issues | 1,897 |
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
| Stars | 110,624 |
| 语言 | C++ |
| Forks | 18,324 |
| Issues | 1,655 |
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
| Stars | 63,291 |
| 语言 | Python |
| Forks | 1,673 |
| Issues | 38 |
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
| Stars | 38,727 |
| 语言 | TypeScript |
| Forks | 4,439 |
| Issues | 303 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 298,189 |
| 语言 | Python |
| Forks | 27,924 |
| Issues | 18 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,089 |
| 语言 | Python |
| Forks | 37,507 |
| Issues | 4,145 |
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
| Stars | 77,662 |
| 语言 | Python |
| Forks | 45,091 |
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
| Stars | 445,010 |
| 语言 | TypeScript |
| Forks | 44,618 |
| Issues | 187 |
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
| Stars | 354,962 |
| 语言 | TypeScript |
| Forks | 44,079 |
| Issues | 15 |
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
| Stars | 123,420 |
| 语言 | TypeScript |
| Forks | 13,678 |
| Issues | 3,063 |
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
| Stars | 114,546 |
| 语言 | TypeScript |
| Forks | 8,837 |
| Issues | 1,920 |
| Topics | base-ui, components, laravel, nextjs, radix-ui, react, shadcn, tailwindcss, tanstack, ui, vite |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,858 |
| 语言 | TypeScript |
| Forks | 5,629 |
| Issues | 661 |
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
| Stars | 98,055 |
| 语言 | TypeScript |
| Forks | 54,613 |
| Issues | 1,371 |
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
| Stars | 95,041 |
| 语言 | TypeScript |
| Forks | 5,242 |
| Issues | 93 |
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
| Stars | 85,797 |
| 语言 | TypeScript |
| Forks | 10,729 |
| Issues | 472 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,445 |
| 语言 | TypeScript |
| Forks | 7,607 |
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
| Stars | 80,658 |
| 语言 | TypeScript |
| Forks | 8,184 |
| Issues | 733 |
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
| Stars | 245,088 |
| 语言 | JavaScript |
| Forks | 51,059 |
| Issues | 1,303 |
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
| Stars | 117,267 |
| 语言 | JavaScript |
| Forks | 35,549 |
| Issues | 2,685 |
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
| Stars | 112,536 |
| 语言 | JavaScript |
| Forks | 36,376 |
| Issues | 467 |
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
| Stars | 109,065 |
| 语言 | JavaScript |
| Forks | 11,702 |
| Issues | 160 |
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
| Stars | 98,352 |
| 语言 | JavaScript |
| Forks | 32,639 |
| Issues | 1,536 |
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
| Stars | 95,775 |
| 语言 | JavaScript |
| Forks | 15,488 |
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
| Stars | 86,581 |
| 语言 | JavaScript |
| Forks | 4,913 |
| Issues | 1,009 |
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
| Stars | 66,437 |
| 语言 | JavaScript |
| Forks | 9,189 |
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
| Stars | 65,769 |
| 语言 | JavaScript |
| Forks | 9,357 |
| Issues | 204 |
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
| Stars | 64,752 |
| 语言 | JavaScript |
| Forks | 4,114 |
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
| Stars | 61,143 |
| 语言 | JavaScript |
| Forks | 5,672 |
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
| Stars | 59,844 |
| 语言 | JavaScript |
| Forks | 20,436 |
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
| Stars | 57,439 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 27 |
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
| Stars | 53,323 |
| 语言 | JavaScript |
| Forks | 10,617 |
| Issues | 447 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,212 |
| 语言 | JavaScript |
| Forks | 11,604 |
| Issues | 281 |
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
| Stars | 133,936 |
| 语言 | Go |
| Forks | 19,024 |
| Issues | 10,147 |
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
| Stars | 106,604 |
| 语言 | Go |
| Forks | 15,042 |
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
| Stars | 88,105 |
| 语言 | Go |
| Forks | 8,265 |
| Issues | 231 |
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
| Stars | 84,113 |
| 语言 | Go |
| Forks | 5,189 |
| Issues | 387 |
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
| Stars | 68,567 |
| 语言 | Go |
| Forks | 3,233 |
| Issues | 49 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,235 |
| 语言 | Go |
| Forks | 5,094 |
| Issues | 1,181 |
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
| Stars | 51,046 |
| 语言 | Go |
| Forks | 21,916 |
| Issues | 402 |
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
| Stars | 49,483 |
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
| Stars | 133,800 |
| 语言 | Unknown |
| Forks | 13,671 |
| Issues | 90 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 221,144 |
| 语言 | Python |
| Forks | 50,651 |
| Issues | 978 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,891 |
| 语言 | Python |
| Forks | 7,290 |
| Issues | 492 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,756 |
| 语言 | Python |
| Forks | 16,968 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 108,889 |
| 语言 | TypeScript |
| Forks | 13,399 |
| Issues | 5,039 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,224 |
| 语言 | JavaScript |
| Forks | 16,802 |
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
| Stars | 68,506 |
| 语言 | JavaScript |
| Forks | 4,615 |
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
| Stars | 61,231 |
| 语言 | JavaScript |
| Forks | 7,164 |
| Issues | 141 |
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
| Stars | 51,058 |
| 语言 | Go |
| Forks | 1,614 |
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
| Stars | 46,849 |
| 语言 | Go |
| Forks | 8,852 |
| Issues | 17 |
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
| Stars | 46,408 |
| 语言 | Go |
| Forks | 3,825 |
| Issues | 85 |
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
| Stars | 157,359 |
| 语言 | Python |
| Forks | 11,997 |
| Issues | 378 |
| Topics | awesome, github, hellogithub, python |
