# 项目发现报告 (2026-05-18)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 125 |
| 去重移除 | 38 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 60 |

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
| Stars | 156,276 |
| 语言 | Python |
| Forks | 25,118 |
| Issues | 12,120 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由 Nous Research 开发的多功能 AI 代理框架，支持 Anthropic Claude、OpenAI GPT 等多种大语言模型集成，拥有超过 15 万星标的高人气，采用模块化架构设计，能够帮助开发者快速构建和部署智能代理应用，非常适合企业级 AI 自动化流程搭建。

**技术亮点**:
- 支持多模型集成：同时支持 Anthropic Claude、OpenAI GPT 等主流大语言模型 API，可灵活切换和对比不同模型效果
- 模块化 Agent 架构：采用可扩展的 agent 设计模式，便于定制和扩展代理功能
- MIT 开源许可：完全开源且采用宽松的 MIT 许可证，可自由用于商业项目
- 丰富的工具生态：内置代码执行、文件操作等多种工具支持，覆盖主流 AI 应用场景
- 活跃的社区生态：依托 Nous Research 研究团队和 15 万+星标社区，持续迭代更新

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理、数据分析等业务流程自动化代理
- 开发者 AI 助手：集成到开发工作流，实现代码审查、自动测试、智能文档生成等开发辅助功能
- 多模型对比研究：研究人员和开发者可使用该项目灵活对比不同 LLM 在相同任务上的表现



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,613 |
| 语言 | Python |
| Forks | 19,662 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的自托管 LLM 解决方案之一，将 RAG 检索增强生成、MCP 协议支持、多后端兼容（Ollama/OpenAI API）等功能集成到统一 Web 界面中，让用户无需编码即可轻松部署私有 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的用户。

**技术亮点**:
- 多后端灵活支持 — 同时兼容 Ollama 本地模型和 OpenAI API，支持无缝切换不同 LLM 提供商，降低厂商锁定风险
- RAG 检索增强生成 — 内置文档处理和向量检索能力，支持上传 PDF、TXT、Markdown 等文件，实现基于私有知识的问答
- MCP (Model Context Protocol) — 支持模型上下文协议，可扩展连接外部工具和数据源，构建更强大的 AI Agent
- 全栈 Python 实现 — 采用纯 Python 开发，便于二次开发和定制，生态系统成熟，依赖管理简单
- 现代化 Web 界面 — 提供直观的响应式 UI，支持对话管理、模型配置、聊天历史等企业级功能

**适用场景**:
- 企业私有化 AI 部署 — 需要在防火墙内运行 LLM、确保数据隐私不外泄的金融、医疗、法律等敏感行业
- 开发者本地调试与原型开发 — 希望快速测试不同 LLM 模型、调试 Prompt、评估 RAG 效果的个人开发者
- 团队协作与知识管理 — 需要构建内部知识库 AI 助手的团队，支持多人共享文档库和对话上下文
- 离线/内网环境使用 — 网络受限的科研机构、政府部门或大型企业的特殊业务场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,750 |
| 语言 | Python |
| Forks | 9,232 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的国产开源 RAG 引擎之一，通过将 RAG 与 Agent 能力深度融合，解决了传统 RAG 面临的文档理解不准确、检索召回率低等问题，为企业级 LLM 应用提供了开箱即用的生产级解决方案。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，实现智能化的上下文理解和任务规划
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel等）的结构化解析，提取多模态信息并构建知识图谱
- 可视化知识库管理：提供直观的 Web 界面，支持文档上传、分块策略配置、向量索引管理等一站式操作
- 多源检索能力：支持语义检索、关键词检索、混合检索等多种方式，通过 Agent 动态选择最优检索策略
- 灵活的 LLM 后端支持：兼容 OpenAI、Claude、通义千问、文心一言等主流大模型，支持本地部署的 embedding 模型

**适用场景**:
- 企业知识库问答系统：构建私有化知识库，支持员工快速检索内部文档、规章制度、技术文档等
- 智能客服与文档助手：基于企业自有文档构建 AI 助手，实现精准的 FAQ 问答和产品支持
- 复杂文档处理与分析：自动解析长文档、合同、报告等，提取关键信息并支持智能问答



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 121,412 |
| 语言 | TypeScript |
| Forks | 7,400 |
| Issues | 324 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 代理场景设计的高 Star 数开源爬虫工具，提供了 Search、爬取、清理一体化的工作流，特别擅长将网页内容转换为 AI 友好的 Markdown 格式，大幅简化 LLM 应用的数据准备工作。

**技术亮点**:
- 专为 AI 代理场景优化，支持 Search、爬取、清理的端到端工作流
- 强大的 HTML 到 Markdown 转换能力，输出 AI/LLM 友好的结构化数据
- 支持多种数据提取模式，包括全文提取、智能清理去噪等
- 基于 TypeScript/Node.js 开发，类型安全且易于集成到现有项目
- 活跃的开源社区，高达 12 万+ Stars，经过生产环境验证

**适用场景**:
- LLM/RAG 应用开发中需要从网页抓取结构化数据作为训练或检索材料
- AI 代理（AI Agent）开发中需要实时获取网页信息进行决策
- 构建 AI 搜索产品或垂直领域搜索引擎时需要大规模网页数据采集



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 186,476 |
| 语言 | JavaScript |
| Forks | 28,869 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的热门 AI 编码增强项目，通过 Skills、Instincts、Memory 等模块化系统为 Claude Code 等工具提供性能优化和能力扩展，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 架构设计，提供标准化的 AI 工具扩展能力
- Skills 系统：模块化的技能扩展机制，可定制化增强 AI 编码能力
- Memory 机制：实现跨会话的上下文保持和知识积累
- Security 模块：内置安全审计和保护机制，确保 AI 辅助开发的安全性
- Instincts 本能系统：模拟开发者编程直觉，优化 AI 响应质量

**适用场景**:
- 企业级 AI 辅助开发：团队可通过 Skills 定制统一的代码规范和质量标准，提升整体开发效率
- 个人开发者效率提升：利用 Memory 机制让 AI 记住项目背景，减少重复解释；通过 Instincts 获得更符合编程习惯的智能建议
- 代码安全审计：使用内置 Security 模块对 AI 生成的代码进行安全检查，降低潜在风险



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,339 |
| 语言 | Go |
| Forks | 4,085 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 且支持分布式部署，特别适合需要在本地或边缘环境中部署 AI 能力的开发者，有效降低 AI 应用门槛和成本。

**技术亮点**:
- 支持多种模型架构：包括 LLaMA、Mamba 等大语言模型，以及 Stable Diffusion、MusicGen、Whisper 等视觉、音频、多模态模型
- 基于 Go 语言开发，充分利用 Go 的并发优势和高性能特性，支持高并发请求处理
- 去中心化架构：集成 libp2p 实现分布式和对等网络，支持分布式推理和边缘计算部署
- 支持 MCP (Model Context Protocol) 协议，提供标准化的模型管理和交互接口
- 提供统一 REST API，支持文本生成、图像生成、语音合成、目标检测等多种任务，简化 AI 应用集成

**适用场景**:
- 本地 AI 开发与测试：开发者可以在本地硬件上快速验证和测试各种 AI 模型，无需云端 API 或昂贵的 GPU 资源
- 隐私敏感型应用：金融、医疗、企业内部等需要数据本地化处理的场景，支持完全私有化部署
- 边缘计算与分布式推理：在边缘设备或分布式环境中部署 AI 能力，降低带宽成本，减少推理延迟



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,269 |
| 语言 | TypeScript |
| Forks | 15,209 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，支持多模型（GPT/Claude/DeepSeek/Gemini）统一管理和 MCP 协议集成，拥有 77k+ Stars 的活跃社区，是构建企业级 AI 团队协作系统的优秀选择。

**技术亮点**:
- 多模型支持：统一集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供灵活的模型切换能力
- MCP 协议支持：基于 Model Context Protocol 实现标准化的模型上下文管理和工具调用
- Agent 编排引擎：提供完整的 Agent 雇佣、调度和协作机制，支持 7×24 自动化运营
- 知识库集成：内置知识库功能，支持 RAG 增强检索和上下文管理
- TypeScript/现代前端：基于 React + TypeScript 构建，提供完善的类型安全和开发体验

**适用场景**:
- 企业 AI 团队管理：使用 LobeHub 统一管理和调度多个 AI Agent，实现 7×24 自动化业务流程
- 多模型应用开发：开发者可基于该项目快速构建需要灵活切换和对比不同大模型能力的 AI 应用
- Agent 应用市场：利用其模块化架构构建自己的 Agent 市场或垂直领域 AI 助手平台



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,575 |
| 语言 | TypeScript |
| Forks | 6,583 |
| Issues | 127 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 的"记忆丧失"痛点，通过 AI 压缩技术将会话上下文持久化存储，使 Agent 能在后续会话中自动召回历史信息，大幅提升复杂任务的连贯性和效率。项目拥有 76k+ Stars 的高人气验证了其技术价值和社区认可度。

**技术亮点**:
- 采用 ChromaDB 向量数据库实现语义检索，通过 Embeddings 技术将记忆内容转化为可搜索的向量表示
- 集成 RAG（检索增强生成）架构，将历史上下文智能注入新会话的提示中
- 支持 SQLite 本地持久化存储，无需额外基础设施即可快速部署
- 兼容 Claude Code、Copilot、Codex、Gemini 等 10+ 主流 AI Agent 框架
- AI 驱动的会话压缩算法，自动提炼关键信息并过滤冗余内容

**适用场景**:
- 长期 AI 辅助开发项目：团队使用 AI 编码助手处理多阶段重构或大型功能开发时，自动保持上下文连贯性
- 个人开发者工作流优化：让 AI 记住项目架构决策、代码规范和历史问题，避免重复解释
- 企业级 AI Agent 部署：构建具有持久记忆能力的智能助手，应用于客服、数据分析等场景



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,369 |
| 语言 | Python |
| Forks | 8,717 |
| Issues | 1,018 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效大模型微调框架，支持 100+ 开源模型（包括 LLaMA、Gemma、Qwen、DeepSeek 等），集成 LoRA/QLoRA/RLHF 等主流 PEFT 技术，兼具学术认可度（ACL 2024）和工业级实用性，适合需要快速定制专属 LLM 的开发者和企业。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs，涵盖 LLaMA、LLaMA3、Gemma、Qwen、DeepSeek、Mistral 等主流开源模型
- 集成 LoRA、QLoRA、Adapter、Prefix Tuning 等多种 PEFT 方法，支持 RLHF（PPO/DPO）训练
- 支持 MoE（专家混合）架构和 INT4/INT8/FP8 量化，大幅降低显存占用
- 提供统一的训练框架，支持预训练、指令微调、对齐微调全流程
- 模块化设计，支持 Agent 微调和多模态模型（VLM）微调

**适用场景**:
- 企业场景：基于开源基座模型快速构建垂直领域定制模型（如金融、医疗、法律问答系统）
- 个人开发者/研究者：低成本实验大模型微调，使用 QLoRA 在消费级 GPU 上训练百亿参数模型
- 学术研究：复现论文实验、探索新的微调方法和 RLHF 算法



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,885 |
| 语言 | Python |
| Forks | 14,981 |
| Issues | 345 |
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
| Stars | 61,169 |
| 语言 | TypeScript |
| Forks | 10,004 |
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
| Stars | 53,571 |
| 语言 | HTML |
| Forks | 5,368 |
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
| Stars | 50,847 |
| 语言 | Python |
| Forks | 6,154 |
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
| Stars | 46,310 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 22 |
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
| Stars | 52,758 |
| 语言 | TypeScript |
| Forks | 5,974 |
| Issues | 548 |
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
| Stars | 60,242 |
| 语言 | JavaScript |
| Forks | 6,516 |
| Issues | 367 |
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
| Stars | 73,990 |
| 语言 | Python |
| Forks | 9,385 |
| Issues | 410 |
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
| Stars | 58,404 |
| 语言 | TypeScript |
| Forks | 4,736 |
| Issues | 574 |
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
| Stars | 39,185 |
| 语言 | Python |
| Forks | 6,210 |
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
| Stars | 94,501 |
| 语言 | Python |
| Forks | 10,667 |
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
| Stars | 52,915 |
| 语言 | TypeScript |
| Forks | 24,355 |
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
| Stars | 188,562 |
| 语言 | TypeScript |
| Forks | 57,788 |
| Issues | 1,473 |
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
| Stars | 155,750 |
| 语言 | JavaScript |
| Forks | 46,132 |
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
| Stars | 148,453 |
| 语言 | Python |
| Forks | 9,035 |
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
| Stars | 63,352 |
| 语言 | Jupyter Notebook |
| Forks | 21,161 |
| Issues | 6 |
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
| Stars | 74,498 |
| 语言 | Rust |
| Forks | 4,833 |
| Issues | 906 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 110,970 |
| 语言 | Python |
| Forks | 16,459 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,473 |
| 语言 | Python |
| Forks | 6,582 |
| Issues | 639 |
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
| Stars | 137,613 |
| 语言 | Python |
| Forks | 19,662 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的自托管 LLM 解决方案之一，将 RAG 检索增强生成、MCP 协议支持、多后端兼容（Ollama/OpenAI API）等功能集成到统一 Web 界面中，让用户无需编码即可轻松部署私有 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的用户。

**技术亮点**:
- 多后端灵活支持 — 同时兼容 Ollama 本地模型和 OpenAI API，支持无缝切换不同 LLM 提供商，降低厂商锁定风险
- RAG 检索增强生成 — 内置文档处理和向量检索能力，支持上传 PDF、TXT、Markdown 等文件，实现基于私有知识的问答
- MCP (Model Context Protocol) — 支持模型上下文协议，可扩展连接外部工具和数据源，构建更强大的 AI Agent
- 全栈 Python 实现 — 采用纯 Python 开发，便于二次开发和定制，生态系统成熟，依赖管理简单
- 现代化 Web 界面 — 提供直观的响应式 UI，支持对话管理、模型配置、聊天历史等企业级功能

**适用场景**:
- 企业私有化 AI 部署 — 需要在防火墙内运行 LLM、确保数据隐私不外泄的金融、医疗、法律等敏感行业
- 开发者本地调试与原型开发 — 希望快速测试不同 LLM 模型、调试 Prompt、评估 RAG 效果的个人开发者
- 团队协作与知识管理 — 需要构建内部知识库 AI 助手的团队，支持多人共享文档库和对话上下文
- 离线/内网环境使用 — 网络受限的科研机构、政府部门或大型企业的特殊业务场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,750 |
| 语言 | Python |
| Forks | 9,232 |
| Issues | 3,018 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的国产开源 RAG 引擎之一，通过将 RAG 与 Agent 能力深度融合，解决了传统 RAG 面临的文档理解不准确、检索召回率低等问题，为企业级 LLM 应用提供了开箱即用的生产级解决方案。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，实现智能化的上下文理解和任务规划
- 深度文档理解引擎：支持复杂文档（PDF、Word、Excel等）的结构化解析，提取多模态信息并构建知识图谱
- 可视化知识库管理：提供直观的 Web 界面，支持文档上传、分块策略配置、向量索引管理等一站式操作
- 多源检索能力：支持语义检索、关键词检索、混合检索等多种方式，通过 Agent 动态选择最优检索策略
- 灵活的 LLM 后端支持：兼容 OpenAI、Claude、通义千问、文心一言等主流大模型，支持本地部署的 embedding 模型

**适用场景**:
- 企业知识库问答系统：构建私有化知识库，支持员工快速检索内部文档、规章制度、技术文档等
- 智能客服与文档助手：基于企业自有文档构建 AI 助手，实现精准的 FAQ 问答和产品支持
- 复杂文档处理与分析：自动解析长文档、合同、报告等，提取关键信息并支持智能问答



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,269 |
| 语言 | TypeScript |
| Forks | 15,209 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，支持多模型（GPT/Claude/DeepSeek/Gemini）统一管理和 MCP 协议集成，拥有 77k+ Stars 的活跃社区，是构建企业级 AI 团队协作系统的优秀选择。

**技术亮点**:
- 多模型支持：统一集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供灵活的模型切换能力
- MCP 协议支持：基于 Model Context Protocol 实现标准化的模型上下文管理和工具调用
- Agent 编排引擎：提供完整的 Agent 雇佣、调度和协作机制，支持 7×24 自动化运营
- 知识库集成：内置知识库功能，支持 RAG 增强检索和上下文管理
- TypeScript/现代前端：基于 React + TypeScript 构建，提供完善的类型安全和开发体验

**适用场景**:
- 企业 AI 团队管理：使用 LobeHub 统一管理和调度多个 AI Agent，实现 7×24 自动化业务流程
- 多模型应用开发：开发者可基于该项目快速构建需要灵活切换和对比不同大模型能力的 AI 应用
- Agent 应用市场：利用其模块化架构构建自己的 Agent 市场或垂直领域 AI 助手平台



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,575 |
| 语言 | TypeScript |
| Forks | 6,583 |
| Issues | 127 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 的"记忆丧失"痛点，通过 AI 压缩技术将会话上下文持久化存储，使 Agent 能在后续会话中自动召回历史信息，大幅提升复杂任务的连贯性和效率。项目拥有 76k+ Stars 的高人气验证了其技术价值和社区认可度。

**技术亮点**:
- 采用 ChromaDB 向量数据库实现语义检索，通过 Embeddings 技术将记忆内容转化为可搜索的向量表示
- 集成 RAG（检索增强生成）架构，将历史上下文智能注入新会话的提示中
- 支持 SQLite 本地持久化存储，无需额外基础设施即可快速部署
- 兼容 Claude Code、Copilot、Codex、Gemini 等 10+ 主流 AI Agent 框架
- AI 驱动的会话压缩算法，自动提炼关键信息并过滤冗余内容

**适用场景**:
- 长期 AI 辅助开发项目：团队使用 AI 编码助手处理多阶段重构或大型功能开发时，自动保持上下文连贯性
- 个人开发者工作流优化：让 AI 记住项目架构决策、代码规范和历史问题，避免重复解释
- 企业级 AI Agent 部署：构建具有持久记忆能力的智能助手，应用于客服、数据分析等场景



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,847 |
| 语言 | Python |
| Forks | 6,154 |
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
| Stars | 46,310 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 22 |
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
| Stars | 102,633 |
| 语言 | TypeScript |
| Forks | 12,460 |
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
| Stars | 60,242 |
| 语言 | JavaScript |
| Forks | 6,516 |
| Issues | 367 |
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
| Stars | 39,185 |
| 语言 | Python |
| Forks | 6,210 |
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
| Stars | 78,074 |
| 语言 | Python |
| Forks | 10,450 |
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
| Stars | 52,915 |
| 语言 | TypeScript |
| Forks | 24,355 |
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
| Stars | 49,095 |
| 语言 | Python |
| Forks | 5,332 |
| Issues | 250 |
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
| Stars | 44,342 |
| 语言 | Go |
| Forks | 4,004 |
| Issues | 877 |
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
| Stars | 35,344 |
| 语言 | Python |
| Forks | 5,004 |
| Issues | 230 |
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
| Stars | 110,970 |
| 语言 | Python |
| Forks | 16,459 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


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
| Stars | 156,276 |
| 语言 | Python |
| Forks | 25,118 |
| Issues | 12,120 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由 Nous Research 开发的多功能 AI 代理框架，支持 Anthropic Claude、OpenAI GPT 等多种大语言模型集成，拥有超过 15 万星标的高人气，采用模块化架构设计，能够帮助开发者快速构建和部署智能代理应用，非常适合企业级 AI 自动化流程搭建。

**技术亮点**:
- 支持多模型集成：同时支持 Anthropic Claude、OpenAI GPT 等主流大语言模型 API，可灵活切换和对比不同模型效果
- 模块化 Agent 架构：采用可扩展的 agent 设计模式，便于定制和扩展代理功能
- MIT 开源许可：完全开源且采用宽松的 MIT 许可证，可自由用于商业项目
- 丰富的工具生态：内置代码执行、文件操作等多种工具支持，覆盖主流 AI 应用场景
- 活跃的社区生态：依托 Nous Research 研究团队和 15 万+星标社区，持续迭代更新

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理、数据分析等业务流程自动化代理
- 开发者 AI 助手：集成到开发工作流，实现代码审查、自动测试、智能文档生成等开发辅助功能
- 多模型对比研究：研究人员和开发者可使用该项目灵活对比不同 LLM 在相同任务上的表现



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,613 |
| 语言 | Python |
| Forks | 19,662 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的自托管 LLM 解决方案之一，将 RAG 检索增强生成、MCP 协议支持、多后端兼容（Ollama/OpenAI API）等功能集成到统一 Web 界面中，让用户无需编码即可轻松部署私有 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的用户。

**技术亮点**:
- 多后端灵活支持 — 同时兼容 Ollama 本地模型和 OpenAI API，支持无缝切换不同 LLM 提供商，降低厂商锁定风险
- RAG 检索增强生成 — 内置文档处理和向量检索能力，支持上传 PDF、TXT、Markdown 等文件，实现基于私有知识的问答
- MCP (Model Context Protocol) — 支持模型上下文协议，可扩展连接外部工具和数据源，构建更强大的 AI Agent
- 全栈 Python 实现 — 采用纯 Python 开发，便于二次开发和定制，生态系统成熟，依赖管理简单
- 现代化 Web 界面 — 提供直观的响应式 UI，支持对话管理、模型配置、聊天历史等企业级功能

**适用场景**:
- 企业私有化 AI 部署 — 需要在防火墙内运行 LLM、确保数据隐私不外泄的金融、医疗、法律等敏感行业
- 开发者本地调试与原型开发 — 希望快速测试不同 LLM 模型、调试 Prompt、评估 RAG 效果的个人开发者
- 团队协作与知识管理 — 需要构建内部知识库 AI 助手的团队，支持多人共享文档库和对话上下文
- 离线/内网环境使用 — 网络受限的科研机构、政府部门或大型企业的特殊业务场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 186,476 |
| 语言 | JavaScript |
| Forks | 28,869 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的热门 AI 编码增强项目，通过 Skills、Instincts、Memory 等模块化系统为 Claude Code 等工具提供性能优化和能力扩展，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 架构设计，提供标准化的 AI 工具扩展能力
- Skills 系统：模块化的技能扩展机制，可定制化增强 AI 编码能力
- Memory 机制：实现跨会话的上下文保持和知识积累
- Security 模块：内置安全审计和保护机制，确保 AI 辅助开发的安全性
- Instincts 本能系统：模拟开发者编程直觉，优化 AI 响应质量

**适用场景**:
- 企业级 AI 辅助开发：团队可通过 Skills 定制统一的代码规范和质量标准，提升整体开发效率
- 个人开发者效率提升：利用 Memory 机制让 AI 记住项目背景，减少重复解释；通过 Instincts 获得更符合编程习惯的智能建议
- 代码安全审计：使用内置 Security 模块对 AI 生成的代码进行安全检查，降低潜在风险



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,791 |
| 语言 | JavaScript |
| Forks | 3,443 |
| Issues | 205 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"穴居人语言"风格与 Claude 交互，成功将 token 消耗削减 65%，既显著降低了 API 成本，又保持了表达清晰度。Stars 超过 6 万证明了其在开发者社区的巨大实用价值和受欢迎程度。

**技术亮点**:
- Token 优化算法：通过简化的语言表达模式显著减少 LLM 输出的 token 数量，实现 65% 的节省
- Prompt Engineering 技巧：展示如何通过巧妙的 system prompt 设计引导 AI 采用特定语言风格
- Claude Code 集成：作为 Claude Code 技能直接集成到开发工作流中，无缝融入日常编码体验
- 轻量级 JavaScript 实现：无需复杂依赖即可快速部署和使用
- Meme 文化应用：将互联网 meme 融入技术实践，降低 AI 使用门槛

**适用场景**:
- 成本敏感型项目：企业或个人开发者在大量使用 Claude API 时，需要严格控制 token 消耗和费用支出
- CI/CD 自动化流程：在持续集成/部署环境中，AI 辅助脚本需要高效处理大量重复性任务时
- 大规模代码分析：需要对整个代码库进行批量处理、重构或审查的场景



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,269 |
| 语言 | TypeScript |
| Forks | 15,209 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，支持多模型（GPT/Claude/DeepSeek/Gemini）统一管理和 MCP 协议集成，拥有 77k+ Stars 的活跃社区，是构建企业级 AI 团队协作系统的优秀选择。

**技术亮点**:
- 多模型支持：统一集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供灵活的模型切换能力
- MCP 协议支持：基于 Model Context Protocol 实现标准化的模型上下文管理和工具调用
- Agent 编排引擎：提供完整的 Agent 雇佣、调度和协作机制，支持 7×24 自动化运营
- 知识库集成：内置知识库功能，支持 RAG 增强检索和上下文管理
- TypeScript/现代前端：基于 React + TypeScript 构建，提供完善的类型安全和开发体验

**适用场景**:
- 企业 AI 团队管理：使用 LobeHub 统一管理和调度多个 AI Agent，实现 7×24 自动化业务流程
- 多模型应用开发：开发者可基于该项目快速构建需要灵活切换和对比不同大模型能力的 AI 应用
- Agent 应用市场：利用其模块化架构构建自己的 Agent 市场或垂直领域 AI 助手平台



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,575 |
| 语言 | TypeScript |
| Forks | 6,583 |
| Issues | 127 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 的"记忆丧失"痛点，通过 AI 压缩技术将会话上下文持久化存储，使 Agent 能在后续会话中自动召回历史信息，大幅提升复杂任务的连贯性和效率。项目拥有 76k+ Stars 的高人气验证了其技术价值和社区认可度。

**技术亮点**:
- 采用 ChromaDB 向量数据库实现语义检索，通过 Embeddings 技术将记忆内容转化为可搜索的向量表示
- 集成 RAG（检索增强生成）架构，将历史上下文智能注入新会话的提示中
- 支持 SQLite 本地持久化存储，无需额外基础设施即可快速部署
- 兼容 Claude Code、Copilot、Codex、Gemini 等 10+ 主流 AI Agent 框架
- AI 驱动的会话压缩算法，自动提炼关键信息并过滤冗余内容

**适用场景**:
- 长期 AI 辅助开发项目：团队使用 AI 编码助手处理多阶段重构或大型功能开发时，自动保持上下文连贯性
- 个人开发者工作流优化：让 AI 记住项目架构决策、代码规范和历史问题，避免重复解释
- 企业级 AI Agent 部署：构建具有持久记忆能力的智能助手，应用于客服、数据分析等场景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,475 |
| 语言 | HTML |
| Forks | 21,151 |
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
| Stars | 95,098 |
| 语言 | Jupyter Notebook |
| Forks | 14,560 |
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
| Stars | 61,169 |
| 语言 | TypeScript |
| Forks | 10,004 |
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
| Stars | 53,571 |
| 语言 | HTML |
| Forks | 5,368 |
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
| Stars | 60,242 |
| 语言 | JavaScript |
| Forks | 6,516 |
| Issues | 367 |
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
| Stars | 73,990 |
| 语言 | Python |
| Forks | 9,385 |
| Issues | 410 |
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
| Stars | 58,404 |
| 语言 | TypeScript |
| Forks | 4,736 |
| Issues | 574 |
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
| Stars | 52,915 |
| 语言 | TypeScript |
| Forks | 24,355 |
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
| Stars | 80,375 |
| 语言 | Python |
| Forks | 16,929 |
| Issues | 5,011 |
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
| Stars | 88,038 |
| 语言 | TypeScript |
| Forks | 59,716 |
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
| Stars | 148,453 |
| 语言 | Python |
| Forks | 9,035 |
| Issues | 927 |
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
| Stars | 171,699 |
| 语言 | Go |
| Forks | 16,182 |
| Issues | 3,262 |
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
| Stars | 60,473 |
| 语言 | Python |
| Forks | 6,582 |
| Issues | 639 |
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
| Stars | 123,698 |
| 语言 | Python |
| Forks | 8,379 |
| Issues | 659 |
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
| Stars | 71,369 |
| 语言 | Python |
| Forks | 8,717 |
| Issues | 1,018 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效大模型微调框架，支持 100+ 开源模型（包括 LLaMA、Gemma、Qwen、DeepSeek 等），集成 LoRA/QLoRA/RLHF 等主流 PEFT 技术，兼具学术认可度（ACL 2024）和工业级实用性，适合需要快速定制专属 LLM 的开发者和企业。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs，涵盖 LLaMA、LLaMA3、Gemma、Qwen、DeepSeek、Mistral 等主流开源模型
- 集成 LoRA、QLoRA、Adapter、Prefix Tuning 等多种 PEFT 方法，支持 RLHF（PPO/DPO）训练
- 支持 MoE（专家混合）架构和 INT4/INT8/FP8 量化，大幅降低显存占用
- 提供统一的训练框架，支持预训练、指令微调、对齐微调全流程
- 模块化设计，支持 Agent 微调和多模态模型（VLM）微调

**适用场景**:
- 企业场景：基于开源基座模型快速构建垂直领域定制模型（如金融、医疗、法律问答系统）
- 个人开发者/研究者：低成本实验大模型微调，使用 QLoRA 在消费级 GPU 上训练百亿参数模型
- 学术研究：复现论文实验、探索新的微调方法和 RLHF 算法



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,749 |
| 语言 | Python |
| Forks | 6,820 |
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
| Stars | 162,475 |
| 语言 | HTML |
| Forks | 21,151 |
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
| Stars | 95,098 |
| 语言 | Jupyter Notebook |
| Forks | 14,560 |
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
| Stars | 160,735 |
| 语言 | Python |
| Forks | 33,250 |
| Issues | 2,345 |
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
| Stars | 80,375 |
| 语言 | Python |
| Forks | 16,929 |
| Issues | 5,011 |
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
| Stars | 113,451 |
| 语言 | Python |
| Forks | 13,287 |
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
| Stars | 99,995 |
| 语言 | Python |
| Forks | 27,809 |
| Issues | 18,540 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


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
| Stars | 186,476 |
| 语言 | JavaScript |
| Forks | 28,869 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数超过 18 万的热门 AI 编码增强项目，通过 Skills、Instincts、Memory 等模块化系统为 Claude Code 等工具提供性能优化和能力扩展，是提升 AI 辅助编程效率的必备工具箱。

**技术亮点**:
- 基于 Model Context Protocol (MCP) 架构设计，提供标准化的 AI 工具扩展能力
- Skills 系统：模块化的技能扩展机制，可定制化增强 AI 编码能力
- Memory 机制：实现跨会话的上下文保持和知识积累
- Security 模块：内置安全审计和保护机制，确保 AI 辅助开发的安全性
- Instincts 本能系统：模拟开发者编程直觉，优化 AI 响应质量

**适用场景**:
- 企业级 AI 辅助开发：团队可通过 Skills 定制统一的代码规范和质量标准，提升整体开发效率
- 个人开发者效率提升：利用 Memory 机制让 AI 记住项目背景，减少重复解释；通过 Instincts 获得更符合编程习惯的智能建议
- 代码安全审计：使用内置 Security 模块对 AI 生成的代码进行安全检查，降低潜在风险



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,339 |
| 语言 | Go |
| Forks | 4,085 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 且支持分布式部署，特别适合需要在本地或边缘环境中部署 AI 能力的开发者，有效降低 AI 应用门槛和成本。

**技术亮点**:
- 支持多种模型架构：包括 LLaMA、Mamba 等大语言模型，以及 Stable Diffusion、MusicGen、Whisper 等视觉、音频、多模态模型
- 基于 Go 语言开发，充分利用 Go 的并发优势和高性能特性，支持高并发请求处理
- 去中心化架构：集成 libp2p 实现分布式和对等网络，支持分布式推理和边缘计算部署
- 支持 MCP (Model Context Protocol) 协议，提供标准化的模型管理和交互接口
- 提供统一 REST API，支持文本生成、图像生成、语音合成、目标检测等多种任务，简化 AI 应用集成

**适用场景**:
- 本地 AI 开发与测试：开发者可以在本地硬件上快速验证和测试各种 AI 模型，无需云端 API 或昂贵的 GPU 资源
- 隐私敏感型应用：金融、医疗、企业内部等需要数据本地化处理的场景，支持完全私有化部署
- 边缘计算与分布式推理：在边缘设备或分布式环境中部署 AI 能力，降低带宽成本，减少推理延迟



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,310 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 22 |
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
| Stars | 73,990 |
| 语言 | Python |
| Forks | 9,385 |
| Issues | 410 |
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
| Stars | 58,404 |
| 语言 | TypeScript |
| Forks | 4,736 |
| Issues | 574 |
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
| Stars | 188,562 |
| 语言 | TypeScript |
| Forks | 57,788 |
| Issues | 1,473 |
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
| Stars | 56,203 |
| 语言 | JavaScript |
| Forks | 4,214 |
| Issues | 1,179 |
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
| Stars | 435,695 |
| 语言 | Python |
| Forks | 47,758 |
| Issues | 1,343 |
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
| Stars | 162,987 |
| 语言 | Python |
| Forks | 13,678 |
| Issues | 2,506 |
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
| Stars | 98,307 |
| 语言 | Python |
| Forks | 9,313 |
| Issues | 181 |
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
| Stars | 83,473 |
| 语言 | Python |
| Forks | 9,744 |
| Issues | 271 |
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
| Stars | 185,065 |
| 语言 | TypeScript |
| Forks | 39,945 |
| Issues | 17,741 |
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
| Stars | 94,339 |
| 语言 | TypeScript |
| Forks | 9,420 |
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
| Stars | 79,205 |
| 语言 | TypeScript |
| Forks | 5,880 |
| Issues | 729 |
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
| Stars | 80,325 |
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
| Stars | 78,092 |
| 语言 | Go |
| Forks | 2,838 |
| Issues | 963 |
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
| Stars | 44,454 |
| 语言 | Go |
| Forks | 8,451 |
| Issues | 1,010 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,473 |
| 语言 | Python |
| Forks | 6,582 |
| Issues | 639 |
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
| Stars | 58,404 |
| 语言 | TypeScript |
| Forks | 4,736 |
| Issues | 574 |
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
| Stars | 188,562 |
| 语言 | TypeScript |
| Forks | 57,788 |
| Issues | 1,473 |
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
| Stars | 51,705 |
| 语言 | Go |
| Forks | 10,359 |
| Issues | 242 |
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
| Stars | 122,336 |
| 语言 | Go |
| Forks | 43,095 |
| Issues | 2,699 |
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
| Stars | 71,568 |
| 语言 | Go |
| Forks | 18,955 |
| Issues | 3,768 |
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
| Stars | 55,755 |
| 语言 | Go |
| Forks | 6,708 |
| Issues | 2,793 |
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
| Stars | 47,520 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 996 |
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
| Stars | 94,339 |
| 语言 | TypeScript |
| Forks | 9,420 |
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
| Stars | 78,906 |
| 语言 | TypeScript |
| Forks | 6,907 |
| Issues | 407 |
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
| Stars | 86,950 |
| 语言 | JavaScript |
| Forks | 7,867 |
| Issues | 748 |
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
| Stars | 70,353 |
| 语言 | Go |
| Forks | 1,923 |
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
| Stars | 63,211 |
| 语言 | Go |
| Forks | 6,001 |
| Issues | 825 |
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
| Stars | 59,753 |
| 语言 | Go |
| Forks | 4,376 |
| Issues | 24 |
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
| Stars | 60,473 |
| 语言 | Python |
| Forks | 6,582 |
| Issues | 639 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,949 |
| 语言 | Go |
| Forks | 7,509 |
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
| Stars | 86,950 |
| 语言 | JavaScript |
| Forks | 7,867 |
| Issues | 748 |
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
| Stars | 64,087 |
| 语言 | Go |
| Forks | 10,416 |
| Issues | 774 |
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
| Stars | 46,339 |
| 语言 | Go |
| Forks | 4,085 |
| Issues | 157 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持在任意硬件上运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 且支持分布式部署，特别适合需要在本地或边缘环境中部署 AI 能力的开发者，有效降低 AI 应用门槛和成本。

**技术亮点**:
- 支持多种模型架构：包括 LLaMA、Mamba 等大语言模型，以及 Stable Diffusion、MusicGen、Whisper 等视觉、音频、多模态模型
- 基于 Go 语言开发，充分利用 Go 的并发优势和高性能特性，支持高并发请求处理
- 去中心化架构：集成 libp2p 实现分布式和对等网络，支持分布式推理和边缘计算部署
- 支持 MCP (Model Context Protocol) 协议，提供标准化的模型管理和交互接口
- 提供统一 REST API，支持文本生成、图像生成、语音合成、目标检测等多种任务，简化 AI 应用集成

**适用场景**:
- 本地 AI 开发与测试：开发者可以在本地硬件上快速验证和测试各种 AI 模型，无需云端 API 或昂贵的 GPU 资源
- 隐私敏感型应用：金融、医疗、企业内部等需要数据本地化处理的场景，支持完全私有化部署
- 边缘计算与分布式推理：在边缘设备或分布式环境中部署 AI 能力，降低带宽成本，减少推理延迟



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 435,695 |
| 语言 | Python |
| Forks | 47,758 |
| Issues | 1,343 |
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
| Stars | 98,307 |
| 语言 | Python |
| Forks | 9,313 |
| Issues | 181 |
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
| Stars | 87,501 |
| 语言 | Python |
| Forks | 33,918 |
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
| Stars | 100,111 |
| 语言 | TypeScript |
| Forks | 27,227 |
| Issues | 1,157 |
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
| Stars | 79,205 |
| 语言 | TypeScript |
| Forks | 5,880 |
| Issues | 729 |
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
| Stars | 69,035 |
| 语言 | JavaScript |
| Forks | 23,365 |
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
| Forks | 10,195 |
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
| Stars | 51,876 |
| 语言 | JavaScript |
| Forks | 4,723 |
| Issues | 1,490 |
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
| Stars | 72,559 |
| 语言 | Go |
| Forks | 4,746 |
| Issues | 254 |
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
| Stars | 58,410 |
| 语言 | Go |
| Forks | 3,381 |
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
| Stars | 88,529 |
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
| Stars | 102,633 |
| 语言 | TypeScript |
| Forks | 12,460 |
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
| Stars | 60,242 |
| 语言 | JavaScript |
| Forks | 6,516 |
| Issues | 367 |
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
| Stars | 44,342 |
| 语言 | Go |
| Forks | 4,004 |
| Issues | 877 |
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
| Stars | 51,705 |
| 语言 | Go |
| Forks | 10,359 |
| Issues | 242 |
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
| Stars | 61,791 |
| 语言 | JavaScript |
| Forks | 3,443 |
| Issues | 205 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"穴居人语言"风格与 Claude 交互，成功将 token 消耗削减 65%，既显著降低了 API 成本，又保持了表达清晰度。Stars 超过 6 万证明了其在开发者社区的巨大实用价值和受欢迎程度。

**技术亮点**:
- Token 优化算法：通过简化的语言表达模式显著减少 LLM 输出的 token 数量，实现 65% 的节省
- Prompt Engineering 技巧：展示如何通过巧妙的 system prompt 设计引导 AI 采用特定语言风格
- Claude Code 集成：作为 Claude Code 技能直接集成到开发工作流中，无缝融入日常编码体验
- 轻量级 JavaScript 实现：无需复杂依赖即可快速部署和使用
- Meme 文化应用：将互联网 meme 融入技术实践，降低 AI 使用门槛

**适用场景**:
- 成本敏感型项目：企业或个人开发者在大量使用 Claude API 时，需要严格控制 token 消耗和费用支出
- CI/CD 自动化流程：在持续集成/部署环境中，AI 辅助脚本需要高效处理大量重复性任务时
- 大规模代码分析：需要对整个代码库进行批量处理、重构或审查的场景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,475 |
| 语言 | HTML |
| Forks | 21,151 |
| Issues | 46 |
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
| Stars | 61,169 |
| 语言 | TypeScript |
| Forks | 10,004 |
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
| Stars | 50,847 |
| 语言 | Python |
| Forks | 6,154 |
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
| Stars | 89,934 |
| 语言 | TypeScript |
| Forks | 10,062 |
| Issues | 2,185 |
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
| Stars | 88,133 |
| 语言 | TypeScript |
| Forks | 8,987 |
| Issues | 1,671 |
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
| Stars | 127,854 |
| 语言 | JavaScript |
| Forks | 12,490 |
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
| Stars | 172,998 |
| 语言 | Go |
| Forks | 13,223 |
| Issues | 184 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (60 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,730 |
| 语言 | Unknown |
| Forks | 34,347 |
| Issues | 144 |
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
| Stars | 91,598 |
| 语言 | Shell |
| Forks | 8,034 |
| Issues | 40 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 102,050 |
| 语言 | Python |
| Forks | 8,963 |
| Issues | 420 |
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
| Stars | 93,115 |
| 语言 | Python |
| Forks | 13,551 |
| Issues | 113 |
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
| Stars | 388,502 |
| 语言 | Python |
| Forks | 66,310 |
| Issues | 84 |
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
| Stars | 118,998 |
| 语言 | TypeScript |
| Forks | 8,667 |
| Issues | 325 |
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
| Stars | 116,309 |
| 语言 | TypeScript |
| Forks | 6,143 |
| Issues | 4 |
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
| Stars | 99,049 |
| 语言 | TypeScript |
| Forks | 14,751 |
| Issues | 535 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,909 |
| 语言 | JavaScript |
| Forks | 5,346 |
| Issues | 57 |
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
| Stars | 48,418 |
| 语言 | Go |
| Forks | 10,351 |
| Issues | 1,901 |
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
| Stars | 110,951 |
| 语言 | C++ |
| Forks | 18,364 |
| Issues | 1,679 |
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
| Stars | 63,279 |
| 语言 | Python |
| Forks | 1,674 |
| Issues | 37 |
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
| Stars | 38,889 |
| 语言 | TypeScript |
| Forks | 4,448 |
| Issues | 319 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 298,374 |
| 语言 | Python |
| Forks | 27,936 |
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
| Stars | 87,102 |
| 语言 | Python |
| Forks | 37,517 |
| Issues | 4,070 |
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
| Stars | 445,090 |
| 语言 | TypeScript |
| Forks | 44,625 |
| Issues | 184 |
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
| Stars | 355,023 |
| 语言 | TypeScript |
| Forks | 44,078 |
| Issues | 7 |
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
| Stars | 123,519 |
| 语言 | TypeScript |
| Forks | 13,690 |
| Issues | 3,066 |
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
| Stars | 114,621 |
| 语言 | TypeScript |
| Forks | 8,847 |
| Issues | 1,926 |
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
| Stars | 100,986 |
| 语言 | TypeScript |
| Forks | 5,637 |
| Issues | 648 |
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
| Stars | 98,058 |
| 语言 | TypeScript |
| Forks | 54,612 |
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
| Stars | 95,051 |
| 语言 | TypeScript |
| Forks | 5,243 |
| Issues | 94 |
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
| Stars | 85,878 |
| 语言 | TypeScript |
| Forks | 10,743 |
| Issues | 475 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,449 |
| 语言 | TypeScript |
| Forks | 7,608 |
| Issues | 36 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,681 |
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
| Stars | 245,109 |
| 语言 | JavaScript |
| Forks | 51,062 |
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
| Stars | 117,279 |
| 语言 | JavaScript |
| Forks | 35,556 |
| Issues | 2,698 |
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
| Stars | 112,544 |
| 语言 | JavaScript |
| Forks | 36,377 |
| Issues | 461 |
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
| Stars | 109,071 |
| 语言 | JavaScript |
| Forks | 11,709 |
| Issues | 162 |
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
| Stars | 98,353 |
| 语言 | JavaScript |
| Forks | 32,638 |
| Issues | 1,537 |
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
| Stars | 95,777 |
| 语言 | JavaScript |
| Forks | 15,497 |
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
| Stars | 86,588 |
| 语言 | JavaScript |
| Forks | 4,913 |
| Issues | 998 |
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
| Stars | 66,445 |
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
| Stars | 65,767 |
| 语言 | JavaScript |
| Forks | 9,354 |
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
| Stars | 64,782 |
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
| Stars | 61,161 |
| 语言 | JavaScript |
| Forks | 5,675 |
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
| Stars | 59,841 |
| 语言 | JavaScript |
| Forks | 20,435 |
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
| Stars | 57,440 |
| 语言 | JavaScript |
| Forks | 12,303 |
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
| Stars | 53,503 |
| 语言 | JavaScript |
| Forks | 11,631 |
| Issues | 279 |
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
| Stars | 53,333 |
| 语言 | JavaScript |
| Forks | 10,619 |
| Issues | 445 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,952 |
| 语言 | Go |
| Forks | 19,023 |
| Issues | 10,097 |
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
| Stars | 106,631 |
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
| Stars | 88,133 |
| 语言 | Go |
| Forks | 8,265 |
| Issues | 237 |
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
| Stars | 84,157 |
| 语言 | Go |
| Forks | 5,195 |
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
| Stars | 68,566 |
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
| Stars | 57,250 |
| 语言 | Go |
| Forks | 5,096 |
| Issues | 1,183 |
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
| Stars | 51,048 |
| 语言 | Go |
| Forks | 21,915 |
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
| Stars | 49,494 |
| 语言 | Go |
| Forks | 7,943 |
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
| Stars | 135,782 |
| 语言 | Unknown |
| Forks | 13,923 |
| Issues | 91 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 221,172 |
| 语言 | Python |
| Forks | 50,657 |
| Issues | 979 |
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
| Stars | 86,926 |
| 语言 | Python |
| Forks | 7,291 |
| Issues | 493 |
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
| Stars | 77,780 |
| 语言 | Python |
| Forks | 16,971 |
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
| Stars | 108,895 |
| 语言 | TypeScript |
| Forks | 13,402 |
| Issues | 5,037 |
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
| Stars | 71,228 |
| 语言 | JavaScript |
| Forks | 16,804 |
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
| Stars | 68,601 |
| 语言 | JavaScript |
| Forks | 4,619 |
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
| Forks | 7,165 |
| Issues | 143 |
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
| Stars | 51,076 |
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
| Forks | 8,851 |
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
| Stars | 157,552 |
| 语言 | Python |
| Forks | 12,001 |
| Issues | 382 |
| Topics | awesome, github, hellogithub, python |
