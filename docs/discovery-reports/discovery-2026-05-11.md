# 项目发现报告 (2026-05-11)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
| 去重移除 | 34 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
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


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 144,543 |
| 语言 | Python |
| Forks | 22,596 |
| Issues | 10,143 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI组织 NousResearch 打造的高星AI代理框架（144K+ Stars），支持 OpenAI、Anthropic Claude 等多模型后端，"The agent that grows with you" 的理念意味着可扩展性强、适合构建从简单到复杂的各类AI应用，是快速落地企业级AI Agent 的优秀选择。

**技术亮点**:
- 多模型后端支持：集成 OpenAI GPT、Anthropic Claude 等主流 LLM，可灵活切换和扩展
- MIT 开源许可证：代码完全开源，商业友好，社区活跃度高（144K+ Stars）
- NousResearch 生态核心：与 Hermes 系列模型深度整合，可使用 NousResearch 自研模型
- Python 优先架构：充分利用 Python 丰富的 AI/ML 生态系统，便于集成 LangChain、LlamaIndex 等工具
- AI Agent 设计模式：提供结构化的 Agent 执行框架，支持工具调用、任务分解和长程规划

**适用场景**:
- 企业智能助手：构建客服机器人、知识库问答、业务流程自动化等企业级 AI 应用
- 开发者快速原型：利用现成的 Agent 框架快速验证 AI 应用想法，支持主流 LLM API
- 多模型对比研究：同时接入多个 LLM 提供商进行性能、成本、效果的对比分析



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,626 |
| 语言 | Python |
| Forks | 19,457 |
| Issues | 234 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 交互界面，拥有超过 13 万 Stars，支持多种 LLM 后端（Ollama、OpenAI API 等）以及 RAG 和 MCP 扩展，可轻松实现自托管部署，非常适合希望拥有私有 AI 能力的个人用户和企业。

**技术亮点**:
- 多后端支持：同时支持 Ollama、OpenAI API、兼容 OpenAPI 的各种 LLM 服务，以及 MCP 协议扩展
- RAG 检索增强生成：内置文档向量化检索功能，支持上传文档并基于知识库进行问答
- 现代 Web UI 界面：基于 Python 构建，提供直观的对话界面和用户管理功能
- 自托管部署：支持 Docker 一键部署，数据完全私有，适合对数据安全有要求的企业
- 丰富的可扩展性：通过 MCP 支持连接各种外部工具和服务，扩展能力强

**适用场景**:
- 个人开发者搭建本地 AI 助手或知识库系统，无需依赖云服务
- 企业内部分享 AI 能力：部署私有化 AI 对话平台，支持团队协作和权限管理
- 构建智能客服或文档问答系统：利用 RAG 功能实现基于企业知识库的智能问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,261 |
| 语言 | Python |
| Forks | 9,149 |
| Issues | 2,994 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款将 RAG 与 Agent 能力深度融合的开源引擎，提供了从文档解析到智能检索的完整 RAG 流程，能够显著提升 LLM 的上下文理解能力，尤其适合需要精准问答和企业知识库构建的场景。

**技术亮点**:
- 融合 RAG 与 Agent 架构：创新性地将检索增强生成与智能代理能力结合，支持复杂的多步推理和动态上下文更新
- 深度文档理解引擎：支持 PDF、Word、Excel 等多格式文档的智能解析和结构化提取，确保高质量的输入数据
- 可配置的 Agent 检索策略：提供灵活的 Agent 配置选项，支持自定义检索策略和工具调用，适应不同业务需求
- 优化的向量检索管道：实现高效的语义检索，支持混合检索和重排序，提升检索结果的准确性
- 完整的 RAG 流程覆盖：从文档上传、智能解析、检索召回到生成回答，提供端到端的解决方案

**适用场景**:
- 企业知识库智能问答：构建内部文档知识库，支持员工通过自然语言查询公司制度、技术文档等，提升信息获取效率
- 客服与支持系统：基于产品文档和常见问题构建智能客服，自动理解用户问题并从知识库中检索准确答案
- 研究与数据分析助手：帮助研究人员和数据分析师快速从大量文献和报告中提取关键信息，辅助决策分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 179,466 |
| 语言 | JavaScript |
| Forks | 27,676 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流AI编程代理工具的性能优化系统，支持Claude Code、Codex、Cursor等多个平台，通过技能系统、本能机制、记忆管理和安全增强等模块，显著提升开发效率

**技术亮点**:
- 多平台代理支持：兼容Claude Code、Codex、Opencode、Cursor等主流AI编码工具
- 模块化架构设计：将系统拆分为技能、本能、记忆、安全等独立模块
- 研究优先开发方法：强调research-first理念，确保AI决策基于充分的信息检索和分析
- MCP协议集成：遵循Model Context Protocol标准，便于扩展和第三方集成
- 企业级安全机制：内置多层安全防护，保障代码生成和执行过程的安全性

**适用场景**:
- 企业级开发团队：需要统一管理AI代理工具、优化团队开发流程、保障代码安全
- 个人开发者：希望提升AI编程辅助效率、个性化配置代理行为的独立开发者
- AI代理研究者：需要研究和实验不同AI代理优化策略的研究人员



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,197 |
| 语言 | Go |
| Forks | 4,071 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 推理引擎，支持 LLM、图像、音频、视频等多种模态模型在无 GPU 环境下运行，采用 Go 语言实现兼顾高性能与低资源占用，为企业和开发者提供了无需依赖云服务的去中心化 AI 部署方案，特别适合对数据隐私和成本敏感的场景

**技术亮点**:
- 多模态统一推理：一站式支持文本生成（Llama、Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、语音转文本（TTS）等多种 AI 能力，通过统一 API 简化集成
- 无 GPU 运行能力：可在 CPU 环境下运行各类模型，大幅降低硬件门槛，让个人开发者和中小企业也能部署 AI 应用
- 去中心化分布式架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理网络，提升系统弹性和可扩展性
- 丰富的模型生态：支持主流开源模型（Llama、Mamba、Stable Diffusion、MusicGen 等），兼容 MCP 协议和 Rerank 等高级功能
- 高性能 Go 实现：使用 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，资源利用率高

**适用场景**:
- 隐私敏感型应用：医疗、金融、法律等领域需要本地处理敏感数据，避免数据上传到第三方云服务，满足合规要求
- 边缘计算与物联网：在边缘设备上部署 AI 推理能力，实现低延迟的本地智能响应，适用于智能摄像头、工业检测等场景
- 开发与研究实验：研究人员和学生可在消费级硬件上实验各种开源模型，降低 AI 学习与研究的成本和门槛



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,863 |
| 语言 | TypeScript |
| Forks | 15,145 |
| Issues | 801 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，拥有 7.6 万+ Stars 的社区影响力，适合需要快速构建和管理 AI Agent 团队的企业和个人开发者。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供统一的 API 接口和切换能力
- MCP (Model Context Protocol) 支持：实现了标准化的模型上下文协议，便于扩展和集成第三方工具
- 多 Agent 协作框架：支持多个 Agent 之间的协同工作，以 Agent 为单位进行任务交互和分工
- 企业级知识库集成：内置知识库管理功能，支持 RAG（检索增强生成）模式
- TypeScript 全栈实现：基于 TypeScript 的现代化架构，提供完整的类型安全和开发体验

**适用场景**:
- 企业智能工作流：构建多 Agent 团队处理复杂业务流程，如客服自动化、数据分析、文档处理等
- AI 应用快速开发：开发者可基于平台快速搭建 AI 应用，支持插件扩展和自定义 Agent 设计
- 个人 AI 助手定制：个人用户可创建专属的 Agent 团队，辅助日常办公、学习和创作任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,832 |
| 语言 | TypeScript |
| Forks | 6,418 |
| Issues | 48 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 缺乏长期记忆的核心痛点，通过 AI 压缩技术实现跨会话上下文持久化，配合 74,832 的高星标验证了其成熟度和社区认可度，支持 Claude Code、Copilot、Gemini 等主流 Agent 平台，适合构建真正具有连续记忆能力的智能助手。

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等多种主流 AI Agent，实现统一的记忆管理
- AI 驱动的上下文压缩：智能分析会话内容并进行压缩，保留关键信息同时优化存储空间
- 双存储引擎架构：结合 SQLite 本地持久化和 ChromaDB 向量数据库，支持高效的语义检索
- RAG + Embeddings 技术：基于检索增强生成和向量嵌入，实现精准的上下文召回
- TypeScript 实现：类型安全的现代开发，良好的 IDE 支持和维护性

**适用场景**:
- 企业级 AI 助手：构建具有长期记忆的客户服务或业务分析 Agent，保持跨会话的上下文连续性
- 智能开发环境：为编程 Agent 提供项目历史、技术债务和开发进度的持久记忆，提升代码理解能力
- 个人知识管理：基于 AI 记忆引擎构建个人 supermemory 系统，自动组织和检索重要信息



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,146 |
| 语言 | Python |
| Forks | 8,693 |
| Issues | 1,005 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效微调框架，支持100+大语言模型和多模态模型的微调，提供从数据处理到模型训练的一站式解决方案，特别适合需要在有限算力下快速适配和部署大模型的企业和研究者。

**技术亮点**:
- 统一的多模型支持架构：支持100+ LLMs（包括LLaMA、Qwen、DeepSeek、Gemma等）和VLMs，提供统一的训练接口，支持LLaMA3、GPT、MoE等主流架构
- 高效微调技术栈：完整支持LoRA、QLORA等PEFT方法，支持MoE架构微调，支持INT4/INT8量化，大幅降低硬件门槛
- 完整的后训练流程：支持RLHF和DPO，支持SFT和Instruction Tuning，内置Agent训练能力
- 工程化成熟度高：Apache License 2.0开源许可，71K+ Stars验证项目可靠性，与Hugging Face Transformers深度集成

**适用场景**:
- 企业级AI应用定制：快速基于自有数据微调专属大模型，应用于客服、内容生成、知识库问答等业务场景
- 学术研究与算法验证：快速实验各种微调方法、RLHF算法，降低复现成本
- 个人开发者与创业团队：在消费级GPU上微调大模型，用于AI应用开发或创业项目原型验证



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,785 |
| 语言 | Python |
| Forks | 14,387 |
| Issues | 328 |
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
| Stars | 59,786 |
| 语言 | TypeScript |
| Forks | 9,805 |
| Issues | 119 |
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
| Stars | 52,380 |
| 语言 | HTML |
| Forks | 5,224 |
| Issues | 12 |
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
| Stars | 47,546 |
| 语言 | Python |
| Forks | 5,724 |
| Issues | 113 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,184 |
| 语言 | Java |
| Forks | 15,977 |
| Issues | 20 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,146 |
| 语言 | Python |
| Forks | 6,198 |
| Issues | 82 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ZhuLinsen/daily_stock_analysis

**描述**: LLM驱动的 A/H/美股智能分析：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,318 |
| 语言 | Python |
| Forks | 34,847 |
| Issues | 48 |
| Topics | agent, ai, aigc, gemini, llm, quant, quantitative-trading, rag, stock |
| 许可证 | MIT License |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,036 |
| 语言 | TypeScript |
| Forks | 5,442 |
| Issues | 537 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,381 |
| 语言 | TypeScript |
| Forks | 7,345 |
| Issues | 312 |
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
| Stars | 59,881 |
| 语言 | JavaScript |
| Forks | 6,469 |
| Issues | 356 |
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
| Stars | 73,188 |
| 语言 | Python |
| Forks | 9,257 |
| Issues | 420 |
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
| Stars | 57,243 |
| 语言 | TypeScript |
| Forks | 4,655 |
| Issues | 688 |
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
| Stars | 109,817 |
| 语言 | Python |
| Forks | 16,251 |
| Issues | 11 |
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
| Stars | 93,423 |
| 语言 | Python |
| Forks | 10,569 |
| Issues | 228 |
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
| Stars | 52,739 |
| 语言 | TypeScript |
| Forks | 24,316 |
| Issues | 839 |
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
| Stars | 187,465 |
| 语言 | TypeScript |
| Forks | 57,544 |
| Issues | 1,463 |
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
| Stars | 155,578 |
| 语言 | Java |
| Forks | 46,142 |
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
| Stars | 147,984 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 918 |
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
| Stars | 61,202 |
| 语言 | Jupyter Notebook |
| Forks | 20,719 |
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
| Stars | 67,231 |
| 语言 | Rust |
| Forks | 4,311 |
| Issues | 811 |
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
| Stars | 59,261 |
| 语言 | Python |
| Forks | 6,430 |
| Issues | 601 |
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
| Stars | 136,626 |
| 语言 | Python |
| Forks | 19,457 |
| Issues | 234 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 交互界面，拥有超过 13 万 Stars，支持多种 LLM 后端（Ollama、OpenAI API 等）以及 RAG 和 MCP 扩展，可轻松实现自托管部署，非常适合希望拥有私有 AI 能力的个人用户和企业。

**技术亮点**:
- 多后端支持：同时支持 Ollama、OpenAI API、兼容 OpenAPI 的各种 LLM 服务，以及 MCP 协议扩展
- RAG 检索增强生成：内置文档向量化检索功能，支持上传文档并基于知识库进行问答
- 现代 Web UI 界面：基于 Python 构建，提供直观的对话界面和用户管理功能
- 自托管部署：支持 Docker 一键部署，数据完全私有，适合对数据安全有要求的企业
- 丰富的可扩展性：通过 MCP 支持连接各种外部工具和服务，扩展能力强

**适用场景**:
- 个人开发者搭建本地 AI 助手或知识库系统，无需依赖云服务
- 企业内部分享 AI 能力：部署私有化 AI 对话平台，支持团队协作和权限管理
- 构建智能客服或文档问答系统：利用 RAG 功能实现基于企业知识库的智能问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,261 |
| 语言 | Python |
| Forks | 9,149 |
| Issues | 2,994 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款将 RAG 与 Agent 能力深度融合的开源引擎，提供了从文档解析到智能检索的完整 RAG 流程，能够显著提升 LLM 的上下文理解能力，尤其适合需要精准问答和企业知识库构建的场景。

**技术亮点**:
- 融合 RAG 与 Agent 架构：创新性地将检索增强生成与智能代理能力结合，支持复杂的多步推理和动态上下文更新
- 深度文档理解引擎：支持 PDF、Word、Excel 等多格式文档的智能解析和结构化提取，确保高质量的输入数据
- 可配置的 Agent 检索策略：提供灵活的 Agent 配置选项，支持自定义检索策略和工具调用，适应不同业务需求
- 优化的向量检索管道：实现高效的语义检索，支持混合检索和重排序，提升检索结果的准确性
- 完整的 RAG 流程覆盖：从文档上传、智能解析、检索召回到生成回答，提供端到端的解决方案

**适用场景**:
- 企业知识库智能问答：构建内部文档知识库，支持员工通过自然语言查询公司制度、技术文档等，提升信息获取效率
- 客服与支持系统：基于产品文档和常见问题构建智能客服，自动理解用户问题并从知识库中检索准确答案
- 研究与数据分析助手：帮助研究人员和数据分析师快速从大量文献和报告中提取关键信息，辅助决策分析



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,863 |
| 语言 | TypeScript |
| Forks | 15,145 |
| Issues | 801 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，拥有 7.6 万+ Stars 的社区影响力，适合需要快速构建和管理 AI Agent 团队的企业和个人开发者。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供统一的 API 接口和切换能力
- MCP (Model Context Protocol) 支持：实现了标准化的模型上下文协议，便于扩展和集成第三方工具
- 多 Agent 协作框架：支持多个 Agent 之间的协同工作，以 Agent 为单位进行任务交互和分工
- 企业级知识库集成：内置知识库管理功能，支持 RAG（检索增强生成）模式
- TypeScript 全栈实现：基于 TypeScript 的现代化架构，提供完整的类型安全和开发体验

**适用场景**:
- 企业智能工作流：构建多 Agent 团队处理复杂业务流程，如客服自动化、数据分析、文档处理等
- AI 应用快速开发：开发者可基于平台快速搭建 AI 应用，支持插件扩展和自定义 Agent 设计
- 个人 AI 助手定制：个人用户可创建专属的 Agent 团队，辅助日常办公、学习和创作任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,832 |
| 语言 | TypeScript |
| Forks | 6,418 |
| Issues | 48 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 缺乏长期记忆的核心痛点，通过 AI 压缩技术实现跨会话上下文持久化，配合 74,832 的高星标验证了其成熟度和社区认可度，支持 Claude Code、Copilot、Gemini 等主流 Agent 平台，适合构建真正具有连续记忆能力的智能助手。

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等多种主流 AI Agent，实现统一的记忆管理
- AI 驱动的上下文压缩：智能分析会话内容并进行压缩，保留关键信息同时优化存储空间
- 双存储引擎架构：结合 SQLite 本地持久化和 ChromaDB 向量数据库，支持高效的语义检索
- RAG + Embeddings 技术：基于检索增强生成和向量嵌入，实现精准的上下文召回
- TypeScript 实现：类型安全的现代开发，良好的 IDE 支持和维护性

**适用场景**:
- 企业级 AI 助手：构建具有长期记忆的客户服务或业务分析 Agent，保持跨会话的上下文连续性
- 智能开发环境：为编程 Agent 提供项目历史、技术债务和开发进度的持久记忆，提升代码理解能力
- 个人知识管理：基于 AI 记忆引擎构建个人 supermemory 系统，自动组织和检索重要信息



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,546 |
| 语言 | Python |
| Forks | 5,724 |
| Issues | 113 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,184 |
| 语言 | Java |
| Forks | 15,977 |
| Issues | 20 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,146 |
| 语言 | Python |
| Forks | 6,198 |
| Issues | 82 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ZhuLinsen/daily_stock_analysis

**描述**: LLM驱动的 A/H/美股智能分析：多数据源行情 + 实时新闻 + LLM决策仪表盘 + 多渠道推送，零成本定时运行，纯白嫖. LLM-powered stock analysis system for A/H/US markets.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,318 |
| 语言 | Python |
| Forks | 34,847 |
| Issues | 48 |
| Topics | agent, ai, aigc, gemini, llm, quant, quantitative-trading, rag, stock |
| 许可证 | MIT License |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 102,181 |
| 语言 | TypeScript |
| Forks | 12,354 |
| Issues | 999 |
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
| Stars | 59,881 |
| 语言 | JavaScript |
| Forks | 6,469 |
| Issues | 356 |
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
| Stars | 109,817 |
| 语言 | Python |
| Forks | 16,251 |
| Issues | 11 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,617 |
| 语言 | Python |
| Forks | 10,412 |
| Issues | 195 |
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
| Stars | 52,739 |
| 语言 | TypeScript |
| Forks | 24,316 |
| Issues | 839 |
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
| Stars | 46,639 |
| 语言 | Python |
| Forks | 5,061 |
| Issues | 244 |
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
| Stars | 44,241 |
| 语言 | Go |
| Forks | 3,996 |
| Issues | 877 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
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
| Stars | 144,543 |
| 语言 | Python |
| Forks | 22,596 |
| Issues | 10,143 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI组织 NousResearch 打造的高星AI代理框架（144K+ Stars），支持 OpenAI、Anthropic Claude 等多模型后端，"The agent that grows with you" 的理念意味着可扩展性强、适合构建从简单到复杂的各类AI应用，是快速落地企业级AI Agent 的优秀选择。

**技术亮点**:
- 多模型后端支持：集成 OpenAI GPT、Anthropic Claude 等主流 LLM，可灵活切换和扩展
- MIT 开源许可证：代码完全开源，商业友好，社区活跃度高（144K+ Stars）
- NousResearch 生态核心：与 Hermes 系列模型深度整合，可使用 NousResearch 自研模型
- Python 优先架构：充分利用 Python 丰富的 AI/ML 生态系统，便于集成 LangChain、LlamaIndex 等工具
- AI Agent 设计模式：提供结构化的 Agent 执行框架，支持工具调用、任务分解和长程规划

**适用场景**:
- 企业智能助手：构建客服机器人、知识库问答、业务流程自动化等企业级 AI 应用
- 开发者快速原型：利用现成的 Agent 框架快速验证 AI 应用想法，支持主流 LLM API
- 多模型对比研究：同时接入多个 LLM 提供商进行性能、成本、效果的对比分析



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,626 |
| 语言 | Python |
| Forks | 19,457 |
| Issues | 234 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 交互界面，拥有超过 13 万 Stars，支持多种 LLM 后端（Ollama、OpenAI API 等）以及 RAG 和 MCP 扩展，可轻松实现自托管部署，非常适合希望拥有私有 AI 能力的个人用户和企业。

**技术亮点**:
- 多后端支持：同时支持 Ollama、OpenAI API、兼容 OpenAPI 的各种 LLM 服务，以及 MCP 协议扩展
- RAG 检索增强生成：内置文档向量化检索功能，支持上传文档并基于知识库进行问答
- 现代 Web UI 界面：基于 Python 构建，提供直观的对话界面和用户管理功能
- 自托管部署：支持 Docker 一键部署，数据完全私有，适合对数据安全有要求的企业
- 丰富的可扩展性：通过 MCP 支持连接各种外部工具和服务，扩展能力强

**适用场景**:
- 个人开发者搭建本地 AI 助手或知识库系统，无需依赖云服务
- 企业内部分享 AI 能力：部署私有化 AI 对话平台，支持团队协作和权限管理
- 构建智能客服或文档问答系统：利用 RAG 功能实现基于企业知识库的智能问答



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 179,466 |
| 语言 | JavaScript |
| Forks | 27,676 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流AI编程代理工具的性能优化系统，支持Claude Code、Codex、Cursor等多个平台，通过技能系统、本能机制、记忆管理和安全增强等模块，显著提升开发效率

**技术亮点**:
- 多平台代理支持：兼容Claude Code、Codex、Opencode、Cursor等主流AI编码工具
- 模块化架构设计：将系统拆分为技能、本能、记忆、安全等独立模块
- 研究优先开发方法：强调research-first理念，确保AI决策基于充分的信息检索和分析
- MCP协议集成：遵循Model Context Protocol标准，便于扩展和第三方集成
- 企业级安全机制：内置多层安全防护，保障代码生成和执行过程的安全性

**适用场景**:
- 企业级开发团队：需要统一管理AI代理工具、优化团队开发流程、保障代码安全
- 个人开发者：希望提升AI编程辅助效率、个性化配置代理行为的独立开发者
- AI代理研究者：需要研究和实验不同AI代理优化策略的研究人员



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,254 |
| 语言 | JavaScript |
| Forks | 3,213 |
| Issues | 203 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过将提示词压缩成穴居人式的简短语言风格，在实际测试中实现了高达 65% 的 token 削减效果，将成本优化与幽默创意完美结合。

**技术亮点**:
- 革命性的 Token 压缩方案：通过独特的语言风格转换，将复杂的提示词压缩至原始长度的约三分之一
- 深度集成 Claude Code 生态：作为官方支持的 skill，无缝融入 Claude Code 工作流程，开箱即用
- 基于 LLM 理解能力的巧妙设计：利用现代大语言模型对简洁、压缩语言仍保持强大理解力的特性
- 零门槛使用体验：安装简单，使用时仅需极少的配置即可显著降低 API 调用成本
- 开源可验证的实现：MIT 许可证下完整开源，代码透明可审计

**适用场景**:
- 企业级 AI 应用成本优化：对于日均 API 调用量大的企业应用，65% 的 token 削减意味着等比例的成本节省，在大规模部署时效果尤为显著
- 个人开发者日常使用：减少每个对话的 token 消耗，延长免费额度的使用时间或降低订阅费用
- 高并发 AI 服务场景：在需要处理大量并发请求的 SaaS 平台或 API 服务中，token 优化直接转化为基础设施成本下降



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,863 |
| 语言 | TypeScript |
| Forks | 15,145 |
| Issues | 801 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，拥有 7.6 万+ Stars 的社区影响力，适合需要快速构建和管理 AI Agent 团队的企业和个人开发者。

**技术亮点**:
- 多模型统一集成：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种大语言模型，提供统一的 API 接口和切换能力
- MCP (Model Context Protocol) 支持：实现了标准化的模型上下文协议，便于扩展和集成第三方工具
- 多 Agent 协作框架：支持多个 Agent 之间的协同工作，以 Agent 为单位进行任务交互和分工
- 企业级知识库集成：内置知识库管理功能，支持 RAG（检索增强生成）模式
- TypeScript 全栈实现：基于 TypeScript 的现代化架构，提供完整的类型安全和开发体验

**适用场景**:
- 企业智能工作流：构建多 Agent 团队处理复杂业务流程，如客服自动化、数据分析、文档处理等
- AI 应用快速开发：开发者可基于平台快速搭建 AI 应用，支持插件扩展和自定义 Agent 设计
- 个人 AI 助手定制：个人用户可创建专属的 Agent 团队，辅助日常办公、学习和创作任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,832 |
| 语言 | TypeScript |
| Forks | 6,418 |
| Issues | 48 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI Agent 缺乏长期记忆的核心痛点，通过 AI 压缩技术实现跨会话上下文持久化，配合 74,832 的高星标验证了其成熟度和社区认可度，支持 Claude Code、Copilot、Gemini 等主流 Agent 平台，适合构建真正具有连续记忆能力的智能助手。

**技术亮点**:
- 多 Agent 平台兼容：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等多种主流 AI Agent，实现统一的记忆管理
- AI 驱动的上下文压缩：智能分析会话内容并进行压缩，保留关键信息同时优化存储空间
- 双存储引擎架构：结合 SQLite 本地持久化和 ChromaDB 向量数据库，支持高效的语义检索
- RAG + Embeddings 技术：基于检索增强生成和向量嵌入，实现精准的上下文召回
- TypeScript 实现：类型安全的现代开发，良好的 IDE 支持和维护性

**适用场景**:
- 企业级 AI 助手：构建具有长期记忆的客户服务或业务分析 Agent，保持跨会话的上下文连续性
- 智能开发环境：为编程 Agent 提供项目历史、技术债务和开发进度的持久记忆，提升代码理解能力
- 个人知识管理：基于 AI 记忆引擎构建个人 supermemory 系统，自动组织和检索重要信息



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,040 |
| 语言 | HTML |
| Forks | 21,105 |
| Issues | 43 |
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
| Stars | 92,888 |
| 语言 | Jupyter Notebook |
| Forks | 14,329 |
| Issues | 6 |
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
| Stars | 59,786 |
| 语言 | TypeScript |
| Forks | 9,805 |
| Issues | 119 |
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
| Stars | 52,380 |
| 语言 | HTML |
| Forks | 5,224 |
| Issues | 12 |
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
| Stars | 59,881 |
| 语言 | JavaScript |
| Forks | 6,469 |
| Issues | 356 |
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
| Stars | 73,188 |
| 语言 | Python |
| Forks | 9,257 |
| Issues | 420 |
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
| Stars | 57,243 |
| 语言 | TypeScript |
| Forks | 4,655 |
| Issues | 688 |
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
| Stars | 52,739 |
| 语言 | TypeScript |
| Forks | 24,316 |
| Issues | 839 |
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
| Stars | 79,683 |
| 语言 | Python |
| Forks | 16,663 |
| Issues | 4,887 |
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
| Stars | 147,984 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 918 |
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
| Stars | 59,261 |
| 语言 | Python |
| Forks | 6,430 |
| Issues | 601 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,212 |
| 语言 | Go |
| Forks | 16,070 |
| Issues | 3,231 |
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
| Stars | 48,639 |
| 语言 | Rust |
| Forks | 9,777 |
| Issues | 1 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
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
| Stars | 122,645 |
| 语言 | Python |
| Forks | 8,265 |
| Issues | 636 |
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
| Stars | 71,146 |
| 语言 | Python |
| Forks | 8,693 |
| Issues | 1,005 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效微调框架，支持100+大语言模型和多模态模型的微调，提供从数据处理到模型训练的一站式解决方案，特别适合需要在有限算力下快速适配和部署大模型的企业和研究者。

**技术亮点**:
- 统一的多模型支持架构：支持100+ LLMs（包括LLaMA、Qwen、DeepSeek、Gemma等）和VLMs，提供统一的训练接口，支持LLaMA3、GPT、MoE等主流架构
- 高效微调技术栈：完整支持LoRA、QLORA等PEFT方法，支持MoE架构微调，支持INT4/INT8量化，大幅降低硬件门槛
- 完整的后训练流程：支持RLHF和DPO，支持SFT和Instruction Tuning，内置Agent训练能力
- 工程化成熟度高：Apache License 2.0开源许可，71K+ Stars验证项目可靠性，与Hugging Face Transformers深度集成

**适用场景**:
- 企业级AI应用定制：快速基于自有数据微调专属大模型，应用于客服、内容生成、知识库问答等业务场景
- 学术研究与算法验证：快速实验各种微调方法、RLHF算法，降低复现成本
- 个人开发者与创业团队：在消费级GPU上微调大模型，用于AI应用开发或创业项目原型验证



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,407 |
| 语言 | Python |
| Forks | 6,757 |
| Issues | 79 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个社区驱动的开源金融数据平台，拥有超过 67k Stars 的高人气，提供了统一的 API 接口来访问多种金融数据源（股票、加密货币、期权、固定收益等），特别适合需要快速构建量化分析系统和 AI 金融应用的开发者。

**技术亮点**:
- 统一的数据 API 层：抽象多个数据源，提供标准化的接口访问股票、加密货币、期权、债券等金融数据
- 模块化架构设计：支持插件式扩展，用户可以轻松添加自定义数据源和分析模块
- AI/ML 原生支持：内置机器学习模型集成，便于构建智能投研和预测分析系统
- 丰富的量化工具：提供技术指标、回测框架、风险管理等量化金融必备组件
- 支持 CLI/Terminal/SDK 多种使用方式：满足不同用户的使用偏好和集成需求

**适用场景**:
- 量化交易系统开发：量化研究员可以使用该平台快速获取市场数据、进行因子挖掘和策略回测
- 金融数据分析平台：分析师通过统一接口获取多资产类别数据，进行投资研究和市场分析
- AI 金融代理应用：开发者可将 OpenBB 作为后台数据服务，为 AI 代理提供实时金融数据支撑
- 投研报告自动化：自动采集和整合金融数据，生成结构化的投资研究报告



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,040 |
| 语言 | HTML |
| Forks | 21,105 |
| Issues | 43 |
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
| Stars | 92,888 |
| 语言 | Jupyter Notebook |
| Forks | 14,329 |
| Issues | 6 |
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
| Stars | 160,488 |
| 语言 | Python |
| Forks | 33,172 |
| Issues | 2,357 |
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
| Stars | 79,683 |
| 语言 | Python |
| Forks | 16,663 |
| Issues | 4,887 |
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
| Stars | 112,462 |
| 语言 | Python |
| Forks | 13,138 |
| Issues | 3,993 |
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
| Stars | 99,825 |
| 语言 | Python |
| Forks | 27,746 |
| Issues | 18,445 |
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
| Stars | 179,466 |
| 语言 | JavaScript |
| Forks | 27,676 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对主流AI编程代理工具的性能优化系统，支持Claude Code、Codex、Cursor等多个平台，通过技能系统、本能机制、记忆管理和安全增强等模块，显著提升开发效率

**技术亮点**:
- 多平台代理支持：兼容Claude Code、Codex、Opencode、Cursor等主流AI编码工具
- 模块化架构设计：将系统拆分为技能、本能、记忆、安全等独立模块
- 研究优先开发方法：强调research-first理念，确保AI决策基于充分的信息检索和分析
- MCP协议集成：遵循Model Context Protocol标准，便于扩展和第三方集成
- 企业级安全机制：内置多层安全防护，保障代码生成和执行过程的安全性

**适用场景**:
- 企业级开发团队：需要统一管理AI代理工具、优化团队开发流程、保障代码安全
- 个人开发者：希望提升AI编程辅助效率、个性化配置代理行为的独立开发者
- AI代理研究者：需要研究和实验不同AI代理优化策略的研究人员



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,197 |
| 语言 | Go |
| Forks | 4,071 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 推理引擎，支持 LLM、图像、音频、视频等多种模态模型在无 GPU 环境下运行，采用 Go 语言实现兼顾高性能与低资源占用，为企业和开发者提供了无需依赖云服务的去中心化 AI 部署方案，特别适合对数据隐私和成本敏感的场景

**技术亮点**:
- 多模态统一推理：一站式支持文本生成（Llama、Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、语音转文本（TTS）等多种 AI 能力，通过统一 API 简化集成
- 无 GPU 运行能力：可在 CPU 环境下运行各类模型，大幅降低硬件门槛，让个人开发者和中小企业也能部署 AI 应用
- 去中心化分布式架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理网络，提升系统弹性和可扩展性
- 丰富的模型生态：支持主流开源模型（Llama、Mamba、Stable Diffusion、MusicGen 等），兼容 MCP 协议和 Rerank 等高级功能
- 高性能 Go 实现：使用 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，资源利用率高

**适用场景**:
- 隐私敏感型应用：医疗、金融、法律等领域需要本地处理敏感数据，避免数据上传到第三方云服务，满足合规要求
- 边缘计算与物联网：在边缘设备上部署 AI 推理能力，实现低延迟的本地智能响应，适用于智能摄像头、工业检测等场景
- 开发与研究实验：研究人员和学生可在消费级硬件上实验各种开源模型，降低 AI 学习与研究的成本和门槛



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,184 |
| 语言 | Java |
| Forks | 15,977 |
| Issues | 20 |
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
| Stars | 73,188 |
| 语言 | Python |
| Forks | 9,257 |
| Issues | 420 |
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
| Stars | 57,243 |
| 语言 | TypeScript |
| Forks | 4,655 |
| Issues | 688 |
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
| Stars | 187,465 |
| 语言 | TypeScript |
| Forks | 57,544 |
| Issues | 1,463 |
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
| Stars | 59,261 |
| 语言 | Python |
| Forks | 6,430 |
| Issues | 601 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,983 |
| 语言 | JavaScript |
| Forks | 4,185 |
| Issues | 1,319 |
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
| Stars | 434,150 |
| 语言 | Python |
| Forks | 47,542 |
| Issues | 1,312 |
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
| Stars | 161,742 |
| 语言 | Python |
| Forks | 13,471 |
| Issues | 2,496 |
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
| Stars | 98,104 |
| 语言 | Python |
| Forks | 9,226 |
| Issues | 188 |
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
| Stars | 83,221 |
| 语言 | Python |
| Forks | 9,701 |
| Issues | 263 |
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
| Stars | 184,801 |
| 语言 | TypeScript |
| Forks | 39,763 |
| Issues | 17,526 |
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
| Stars | 94,298 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 263 |
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
| Stars | 79,154 |
| 语言 | TypeScript |
| Forks | 5,864 |
| Issues | 718 |
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
| Stars | 77,496 |
| 语言 | TypeScript |
| Forks | 6,660 |
| Issues | 153 |
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
| Stars | 80,153 |
| 语言 | Go |
| Forks | 2,803 |
| Issues | 315 |
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
| Stars | 77,785 |
| 语言 | Go |
| Forks | 2,826 |
| Issues | 957 |
| Topics | cli, git, terminal |
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
| Stars | 57,243 |
| 语言 | TypeScript |
| Forks | 4,655 |
| Issues | 688 |
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
| Stars | 187,465 |
| 语言 | TypeScript |
| Forks | 57,544 |
| Issues | 1,463 |
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
| Stars | 59,261 |
| 语言 | Python |
| Forks | 6,430 |
| Issues | 601 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,687 |
| 语言 | Go |
| Forks | 10,343 |
| Issues | 241 |
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
| Stars | 122,198 |
| 语言 | Go |
| Forks | 43,028 |
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
| Stars | 71,542 |
| 语言 | Go |
| Forks | 18,945 |
| Issues | 3,811 |
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
| Stars | 55,572 |
| 语言 | Go |
| Forks | 6,681 |
| Issues | 2,783 |
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
| Stars | 94,298 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 263 |
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
| Stars | 78,580 |
| 语言 | TypeScript |
| Forks | 6,878 |
| Issues | 393 |
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
| Stars | 86,559 |
| 语言 | JavaScript |
| Forks | 7,815 |
| Issues | 740 |
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
| Stars | 70,246 |
| 语言 | Go |
| Forks | 1,918 |
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
| Stars | 63,119 |
| 语言 | Go |
| Forks | 5,979 |
| Issues | 804 |
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
| Stars | 59,494 |
| 语言 | Go |
| Forks | 4,335 |
| Issues | 27 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,509 |
| 语言 | Go |
| Forks | 5,057 |
| Issues | 989 |
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
| Stars | 60,914 |
| 语言 | Go |
| Forks | 7,487 |
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
| Stars | 86,559 |
| 语言 | JavaScript |
| Forks | 7,815 |
| Issues | 740 |
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
| Stars | 63,991 |
| 语言 | Go |
| Forks | 10,398 |
| Issues | 775 |
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
| Stars | 46,197 |
| 语言 | Go |
| Forks | 4,071 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 推理引擎，支持 LLM、图像、音频、视频等多种模态模型在无 GPU 环境下运行，采用 Go 语言实现兼顾高性能与低资源占用，为企业和开发者提供了无需依赖云服务的去中心化 AI 部署方案，特别适合对数据隐私和成本敏感的场景

**技术亮点**:
- 多模态统一推理：一站式支持文本生成（Llama、Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、语音转文本（TTS）等多种 AI 能力，通过统一 API 简化集成
- 无 GPU 运行能力：可在 CPU 环境下运行各类模型，大幅降低硬件门槛，让个人开发者和中小企业也能部署 AI 应用
- 去中心化分布式架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理网络，提升系统弹性和可扩展性
- 丰富的模型生态：支持主流开源模型（Llama、Mamba、Stable Diffusion、MusicGen 等），兼容 MCP 协议和 Rerank 等高级功能
- 高性能 Go 实现：使用 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，资源利用率高

**适用场景**:
- 隐私敏感型应用：医疗、金融、法律等领域需要本地处理敏感数据，避免数据上传到第三方云服务，满足合规要求
- 边缘计算与物联网：在边缘设备上部署 AI 推理能力，实现低延迟的本地智能响应，适用于智能摄像头、工业检测等场景
- 开发与研究实验：研究人员和学生可在消费级硬件上实验各种开源模型，降低 AI 学习与研究的成本和门槛



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 434,150 |
| 语言 | Python |
| Forks | 47,542 |
| Issues | 1,312 |
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
| Stars | 98,104 |
| 语言 | Python |
| Forks | 9,226 |
| Issues | 188 |
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
| Stars | 87,465 |
| 语言 | Python |
| Forks | 33,856 |
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
| Stars | 100,081 |
| 语言 | TypeScript |
| Forks | 27,207 |
| Issues | 1,138 |
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
| Stars | 79,154 |
| 语言 | TypeScript |
| Forks | 5,864 |
| Issues | 718 |
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
| Stars | 69,014 |
| 语言 | JavaScript |
| Forks | 23,294 |
| Issues | 210 |
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
| Forks | 10,199 |
| Issues | 370 |
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
| Stars | 88,475 |
| 语言 | Go |
| Forks | 8,606 |
| Issues | 685 |
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
| Stars | 72,339 |
| 语言 | Go |
| Forks | 4,728 |
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
| Stars | 58,277 |
| 语言 | Go |
| Forks | 3,368 |
| Issues | 17 |
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
| Stars | 102,181 |
| 语言 | TypeScript |
| Forks | 12,354 |
| Issues | 999 |
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
| Stars | 59,881 |
| 语言 | JavaScript |
| Forks | 6,469 |
| Issues | 356 |
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
| Stars | 44,241 |
| 语言 | Go |
| Forks | 3,996 |
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
| Stars | 51,687 |
| 语言 | Go |
| Forks | 10,343 |
| Issues | 241 |
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
| Stars | 58,254 |
| 语言 | JavaScript |
| Forks | 3,213 |
| Issues | 203 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过将提示词压缩成穴居人式的简短语言风格，在实际测试中实现了高达 65% 的 token 削减效果，将成本优化与幽默创意完美结合。

**技术亮点**:
- 革命性的 Token 压缩方案：通过独特的语言风格转换，将复杂的提示词压缩至原始长度的约三分之一
- 深度集成 Claude Code 生态：作为官方支持的 skill，无缝融入 Claude Code 工作流程，开箱即用
- 基于 LLM 理解能力的巧妙设计：利用现代大语言模型对简洁、压缩语言仍保持强大理解力的特性
- 零门槛使用体验：安装简单，使用时仅需极少的配置即可显著降低 API 调用成本
- 开源可验证的实现：MIT 许可证下完整开源，代码透明可审计

**适用场景**:
- 企业级 AI 应用成本优化：对于日均 API 调用量大的企业应用，65% 的 token 削减意味着等比例的成本节省，在大规模部署时效果尤为显著
- 个人开发者日常使用：减少每个对话的 token 消耗，延长免费额度的使用时间或降低订阅费用
- 高并发 AI 服务场景：在需要处理大量并发请求的 SaaS 平台或 API 服务中，token 优化直接转化为基础设施成本下降



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,040 |
| 语言 | HTML |
| Forks | 21,105 |
| Issues | 43 |
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
| Stars | 59,786 |
| 语言 | TypeScript |
| Forks | 9,805 |
| Issues | 119 |
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
| Stars | 47,546 |
| 语言 | Python |
| Forks | 5,724 |
| Issues | 113 |
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
| Stars | 89,886 |
| 语言 | TypeScript |
| Forks | 10,049 |
| Issues | 2,270 |
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
| Stars | 87,976 |
| 语言 | TypeScript |
| Forks | 8,962 |
| Issues | 1,663 |
| Topics | diagrams, diagrams-as-code, documentation, flowchart, javascript, mindmap, typescript, uml-diagrams |
| 许可证 | MIT License |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 172,400 |
| 语言 | Go |
| Forks | 13,206 |
| Issues | 182 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


### ⭐ 中优先级


### Chalarangelo/30-seconds-of-code

**描述**: Coding articles to level up your development skills

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 127,765 |
| 语言 | JavaScript |
| Forks | 12,487 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


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
| Stars | 137,161 |
| 语言 | Unknown |
| Forks | 34,199 |
| Issues | 140 |
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
| Stars | 71,976 |
| 语言 | Shell |
| Forks | 6,215 |
| Issues | 22 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,770 |
| 语言 | Python |
| Forks | 8,318 |
| Issues | 412 |
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
| Stars | 92,904 |
| 语言 | Python |
| Forks | 13,527 |
| Issues | 128 |
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
| Stars | 388,094 |
| 语言 | Python |
| Forks | 66,280 |
| Issues | 80 |
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
| Stars | 117,367 |
| 语言 | TypeScript |
| Forks | 8,555 |
| Issues | 316 |
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
| Stars | 116,152 |
| 语言 | TypeScript |
| Forks | 6,121 |
| Issues | 16 |
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
| Stars | 93,806 |
| 语言 | TypeScript |
| Forks | 13,864 |
| Issues | 448 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,544 |
| 语言 | JavaScript |
| Forks | 5,215 |
| Issues | 48 |
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
| Stars | 48,377 |
| 语言 | Go |
| Forks | 10,347 |
| Issues | 1,902 |
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
| Stars | 109,574 |
| 语言 | C++ |
| Forks | 18,082 |
| Issues | 1,613 |
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
| Stars | 63,307 |
| 语言 | Python |
| Forks | 1,640 |
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
| Stars | 37,720 |
| 语言 | TypeScript |
| Forks | 4,312 |
| Issues | 271 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 297,124 |
| 语言 | Python |
| Forks | 27,863 |
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
| Stars | 220,948 |
| 语言 | Python |
| Forks | 50,592 |
| Issues | 966 |
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
| Stars | 87,015 |
| 语言 | Python |
| Forks | 37,440 |
| Issues | 3,912 |
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
| Stars | 77,660 |
| 语言 | Python |
| Forks | 45,095 |
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
| Stars | 444,512 |
| 语言 | TypeScript |
| Forks | 44,523 |
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
| Stars | 354,605 |
| 语言 | TypeScript |
| Forks | 44,059 |
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
| Stars | 122,958 |
| 语言 | TypeScript |
| Forks | 13,600 |
| Issues | 3,041 |
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
| Stars | 114,072 |
| 语言 | TypeScript |
| Forks | 8,773 |
| Issues | 1,866 |
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
| Stars | 108,812 |
| 语言 | TypeScript |
| Forks | 13,390 |
| Issues | 5,035 |
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
| Stars | 100,326 |
| 语言 | TypeScript |
| Forks | 5,578 |
| Issues | 675 |
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
| Stars | 97,999 |
| 语言 | TypeScript |
| Forks | 54,613 |
| Issues | 1,361 |
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
| Stars | 94,947 |
| 语言 | TypeScript |
| Forks | 5,232 |
| Issues | 91 |
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
| Stars | 83,422 |
| 语言 | TypeScript |
| Forks | 7,610 |
| Issues | 37 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,545 |
| 语言 | TypeScript |
| Forks | 8,160 |
| Issues | 741 |
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
| Stars | 244,958 |
| 语言 | JavaScript |
| Forks | 51,010 |
| Issues | 1,288 |
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
| Stars | 117,155 |
| 语言 | JavaScript |
| Forks | 35,523 |
| Issues | 2,672 |
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
| Stars | 112,410 |
| 语言 | JavaScript |
| Forks | 36,370 |
| Issues | 487 |
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
| Stars | 109,046 |
| 语言 | JavaScript |
| Forks | 11,676 |
| Issues | 150 |
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
| Stars | 98,316 |
| 语言 | JavaScript |
| Forks | 32,643 |
| Issues | 1,547 |
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
| Stars | 95,748 |
| 语言 | JavaScript |
| Forks | 15,470 |
| Issues | 59 |
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
| Stars | 86,541 |
| 语言 | JavaScript |
| Forks | 4,911 |
| Issues | 1,001 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,766 |
| 语言 | JavaScript |
| Forks | 9,357 |
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
| Stars | 64,584 |
| 语言 | JavaScript |
| Forks | 4,099 |
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
| Stars | 61,223 |
| 语言 | JavaScript |
| Forks | 7,162 |
| Issues | 141 |
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
| Stars | 61,022 |
| 语言 | JavaScript |
| Forks | 5,669 |
| Issues | 61 |
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
| Forks | 20,442 |
| Issues | 95 |
| Topics | jquery |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,294 |
| 语言 | JavaScript |
| Forks | 10,615 |
| Issues | 451 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,786 |
| 语言 | JavaScript |
| Forks | 11,541 |
| Issues | 266 |
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
| Stars | 133,842 |
| 语言 | Go |
| Forks | 18,999 |
| Issues | 10,119 |
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
| Stars | 106,415 |
| 语言 | Go |
| Forks | 15,040 |
| Issues | 39 |
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
| Stars | 88,019 |
| 语言 | Go |
| Forks | 8,262 |
| Issues | 245 |
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
| Stars | 83,849 |
| 语言 | Go |
| Forks | 5,170 |
| Issues | 383 |
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
| Stars | 68,577 |
| 语言 | Go |
| Forks | 3,230 |
| Issues | 39 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,125 |
| 语言 | Go |
| Forks | 5,082 |
| Issues | 1,174 |
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
| Stars | 51,031 |
| 语言 | Go |
| Forks | 21,907 |
| Issues | 392 |
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
| Stars | 49,461 |
| 语言 | Go |
| Forks | 7,944 |
| Issues | 572 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 96,134 |
| 语言 | Shell |
| Forks | 15,935 |
| Issues | 133 |
| 许可证 | MIT License |


### ⭐ 中优先级


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 125,168 |
| 语言 | Unknown |
| Forks | 12,730 |
| Issues | 88 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,309 |
| 语言 | Python |
| Forks | 12,175 |
| Issues | 123 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,749 |
| 语言 | Python |
| Forks | 7,272 |
| Issues | 489 |
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
| Stars | 77,634 |
| 语言 | Python |
| Forks | 16,938 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,460 |
| 语言 | TypeScript |
| Forks | 10,660 |
| Issues | 433 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,118 |
| 语言 | JavaScript |
| Forks | 26,686 |
| Issues | 159 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,173 |
| 语言 | JavaScript |
| Forks | 16,800 |
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
| Stars | 67,976 |
| 语言 | JavaScript |
| Forks | 4,561 |
| Issues | 102 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,403 |
| 语言 | JavaScript |
| Forks | 11,952 |
| Issues | 561 |
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
| Stars | 66,386 |
| 语言 | JavaScript |
| Forks | 9,187 |
| Issues | 3 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,432 |
| 语言 | JavaScript |
| Forks | 12,307 |
| Issues | 28 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,993 |
| 语言 | Go |
| Forks | 1,611 |
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
| Stars | 46,854 |
| 语言 | Go |
| Forks | 8,857 |
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
| Stars | 46,295 |
| 语言 | Go |
| Forks | 3,818 |
| Issues | 84 |
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
| Stars | 156,230 |
| 语言 | Python |
| Forks | 11,914 |
| Issues | 362 |
| Topics | awesome, github, hellogithub, python |
