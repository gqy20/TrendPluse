# 项目发现报告 (2026-05-21)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
| 去重移除 | 42 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 18 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 19 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 57 |

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
| Stars | 161,337 |
| 语言 | Python |
| Forks | 26,251 |
| Issues | 12,842 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个高度成熟的多 LLM 集成 AI Agent 框架，拥有超过 16 万 Stars 的社区认可度，支持 Claude、GPT 等主流模型，能够帮助开发者快速构建智能代理应用，非常适合希望在不锁定单一 LLM 提供商的情况下构建 AI 应用的团队和个人开发者。

**技术亮点**:
- 多 LLM 提供商集成：原生支持 Anthropic Claude、OpenAI GPT 等多种大语言模型，提供统一的 Agent 接口
- 成熟的 Agent 架构：基于 NousResearch 在 LLM 领域的深厚积累，实现了可靠的 Agent 推理和任务分解能力
- 开源且商业友好：采用 MIT 许可证，无使用限制，可直接用于商业产品开发
- 活跃的社区生态：超过 16 万 Stars 和丰富的 Topics 标签，证明了其广泛的社区参与度
- Python 生态兼容：使用 Python 开发，可无缝集成到现有的 Python 数据科学和 AI 开发工作流中

**适用场景**:
- 企业级 AI 应用开发：适合企业构建内部智能助手、自动化工作流、客服机器人等应用
- AI 产品原型快速验证：个人开发者或创业团队可以快速基于该框架搭建 AI 产品原型
- 多模型对比研究：研究人员可以通过框架快速对比不同 LLM 在特定任务上的表现



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,116 |
| 语言 | Python |
| Forks | 19,756 |
| Issues | 272 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完善的开源AI界面解决方案，支持Ollama、OpenAI等多种后端，并内置RAG和MCP协议支持，让用户能够轻松搭建私有化的AI助手平台，兼顾功能性与隐私安全。

**技术亮点**:
- 多后端支持：同时兼容Ollama、OpenAI API、Azure OpenAI等多种LLM服务，提供统一的使用体验
- RAG检索增强生成：内置知识库功能，支持文档上传和向量检索，大幅提升问答准确性
- MCP协议支持：集成Model Context Protocol，可扩展连接多种外部工具和数据源
- 自托管部署：提供完整的Docker部署方案，支持私有化部署，数据完全留在本地
- 现代Web界面：响应式设计，支持实时流式输出、对话管理、多语言界面等功能

**适用场景**:
- 企业私有AI助手：适合需要在内部部署AI助手的企业，数据完全本地存储，满足合规和隐私要求
- 个人开发者实验：开发者可快速搭建本地LLM实验环境，支持多种模型切换测试
- 知识库问答系统：基于RAG功能，可构建文档问答、知识库检索等专业应用场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,993 |
| 语言 | Python |
| Forks | 9,274 |
| Issues | 3,047 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎之一（80K+ stars），创新性地将 RAG 与 Agent 能力融合，为 LLM 应用提供智能检索和上下文管理能力，特别适合构建企业级知识库问答系统和 AI Agent 应用。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，实现智能化的上下文理解和任务规划
- 深度文档理解：支持多格式文档的语义解析和结构化提取，包括 PDF、Word、PPT 等复杂文档
- Agentic Retrieval 能力：支持代理式检索，可自主判断检索策略和多次迭代优化查询
- 多模态上下文管理：统一处理文本、表格、图像等多种数据类型的上下文信息
- 模块化 RAG 管道：提供可配置的 RAG 流程组件，支持自定义嵌入模型和向量数据库

**适用场景**:
- 企业知识库问答系统：构建私有化知识库智能问答，支持多文档、多格式的企业资料检索和问答
- AI Agent 应用开发：作为 LLM 的智能上下文层，为 Agent 提供可靠的知识检索和上下文管理能力
- 智能客服与文档检索：集成到客服系统中，实现基于企业文档的精准自动问答



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,213 |
| 语言 | Python |
| Forks | 15,238 |
| Issues | 361 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |

---

TradingAgents 是一个高度成熟的多代理LLM金融交易框架，78k+ stars 证明了其在AI量化交易领域的领先地位，为开发者和金融机构提供了将大语言模型能力与金融决策结合的一站式解决方案。

**技术亮点**:
- Multi-Agent 多代理架构：通过多个专业化代理协同工作，实现复杂的交易决策流程
- LLM深度集成：利用大语言模型进行市场分析、情感识别和交易策略生成
- 模块化Python设计：采用Python实现，便于与现有交易系统、数据源和风控模块集成
- 完整的交易工作流：从数据分析、信号生成到执行建议，覆盖量化交易全链路
- Apache 2.0开源许可：允许商业使用和二次开发，降低企业应用门槛

**适用场景**:
- 个人量化交易者：利用AI代理自动化市场研究和交易决策，提升投研效率
- 金融机构：构建智能投研平台，实现大规模金融数据分析与策略发现
- AI研究者：探索多代理系统与大语言模型在金融领域的应用与优化
- 金融科技创新：作为基础框架快速开发智能投顾、量化策略等创新产品



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 122,683 |
| 语言 | TypeScript |
| Forks | 7,444 |
| Issues | 328 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 代理设计的网页搜索和抓取工具，支持将 HTML 高质量转换为 Markdown 格式，为 LLM 应用提供干净的网页数据，拥有超过 12 万 Stars 的成熟开源项目，特别适合需要大规模网页数据采集和处理的 AI 应用场景。

**技术亮点**:
- 专为 AI 代理优化的网页爬虫框架，支持智能网页抓取和清洗
- 高质量 HTML 到 Markdown 转换，保留关键内容便于 LLM 处理
- 支持多种数据提取模式，包括全文提取、结构化数据提取等
- 基于 TypeScript 开发，提供完整的类型安全和现代开发体验
- 支持批量抓取和增量更新，适合构建大规模数据管道

**适用场景**:
- AI 代理应用的数据获取：为 AI 代理和机器人提供可靠的网页信息采集能力
- LLM 训练数据准备：将网页内容转换为 AI 模型易于处理的 Markdown 格式
- 竞品分析和市场调研：自动化采集和分析公开网页数据



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 188,122 |
| 语言 | JavaScript |
| Forks | 29,121 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个面向多 AI 编码代理的性能优化框架，通过 Skills/Instincts/Memory 三层架构显著提升 Claude Code、Cursor 等工具的开发效率，同时内置安全机制，是 AI 原生开发团队不可或缺的效率基础设施。

**技术亮点**:
- 多代理框架兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具
- 三层记忆系统：Skills（技能库）+ Instincts（本能优化）+ Memory（持久记忆）
- MCP 协议集成：支持 Model Context Protocol 实现标准化上下文管理
- 研究优先开发模式：采用 R&D-first 方法论确保技术领先性
- MIT 许可开源：可自由商用，降低企业采用门槛

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编码代理的能力边界和安全策略
- 个人开发者：构建个人 AI 助手工作流，实现代码审查、调试、文档生成的自动化
- AI 原生应用开发：基于 ECC 框架二次开发定制化 AI 代理系统



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,390 |
| 语言 | Go |
| Forks | 4,093 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，配合 OpenAI 兼容 API，可轻松实现私有化 AI 部署，特别适合隐私敏感场景和资源有限的环境。

**技术亮点**:
- 多模态模型支持：支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理
- 硬件兼容性：支持 CPU 运行，无需昂贵 GPU，降低部署门槛
- 丰富的模型支持：兼容 Llama、Mamba 等主流开源模型，支持 rerank 等高级功能
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用迁移

**适用场景**:
- 私有化 AI 部署：企业可在本地环境部署 AI 服务，数据不出本地，满足合规和隐私要求
- 边缘计算场景：在没有 GPU 的边缘设备上运行 AI 推理，适合 IoT 和嵌入式场景
- 开发者快速原型：开发者可以通过兼容 API 快速搭建 AI 应用原型，降低开发成本



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,494 |
| 语言 | TypeScript |
| Forks | 15,245 |
| Issues | 317 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，通过"首席 Agent 运营官"理念实现了多 Agent 的统一管理和 7×24 自动化运营，支持 OpenAI、Claude、DeepSeek 等多模型集成，为开发者和企业提供了开箱即用的智能体协作解决方案。

**技术亮点**:
- 多模型支持：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，支持灵活切换和对比
- MCP 协议支持：实现 Model Context Protocol 标准化接入，扩展生态兼容性
- Agent 协作编排：支持多个 Agent 之间的任务分配、调度和协同工作，实现复杂业务流程自动化
- 知识库集成：内置 RAG 知识库系统，支持向量检索和语义理解，提升 Agent 回答准确性
- 7×24 运营能力：提供完整的 Agent 生命周期管理，包括雇佣、调度、监控和报告机制

**适用场景**:
- 企业级 AI 运营中心：构建企业内部的 AI Agent 团队，实现客户支持、数据分析、内容生成等业务的自动化运营
- 个人开发者快速原型：开发者可快速搭建多模型 Agent 系统，验证 AI 应用想法，降低开发成本
- 智能工作流自动化：通过 Agent 协作编排，将重复性工作流程（如市场调研、报告生成）交给 AI 团队自动完成



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,259 |
| 语言 | TypeScript |
| Forks | 6,657 |
| Issues | 195 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是一个 Star 数高达 77K 的开源 AI Agent 长期记忆系统，能够跨会话持久化上下文并智能注入相关记忆，兼容 8+ 主流 AI Agent（Claude Code、Copilot、Codex 等），是提升 AI 编程助手效率和连贯性的最佳开源选择。

**技术亮点**:
- 基于 RAG 架构实现智能记忆检索，使用向量嵌入（Embeddings）进行语义相似度匹配
- 支持 ChromaDB 作为向量数据库，结合 SQLite 本地持久化存储
- AI 驱动的记忆压缩技术，自动提炼和总结会话内容
- 多 Agent 统一适配层：Claude Code、OpenClaw、Codex、Copilot、Codex、Gemini、OpenCode 等
- 采用 Apache License 2.0 开源，TypeScript 实现便于二次开发和集成

**适用场景**:
- 个人开发者：让 AI 编程助手记住项目上下文、代码风格和历史决策，避免重复解释
- AI Agent 平台集成：构建具备长期记忆能力的智能助手，支持复杂多步骤任务
- 团队协作知识库：自动积累和复用团队的技术决策、代码规范和最佳实践



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,480 |
| 语言 | Python |
| Forks | 8,718 |
| Issues | 1,014 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,798 |
| 语言 | Python |
| Forks | 10,099 |
| Issues | 131 |
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
| Stars | 54,183 |
| 语言 | HTML |
| Forks | 5,431 |
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
| Stars | 52,165 |
| 语言 | Python |
| Forks | 6,337 |
| Issues | 116 |
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
| Stars | 46,347 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 23 |
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
| Stars | 53,882 |
| 语言 | TypeScript |
| Forks | 6,103 |
| Issues | 563 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,420 |
| 语言 | Python |
| Forks | 9,433 |
| Issues | 402 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,810 |
| 语言 | JavaScript |
| Forks | 46,137 |
| Issues | 61 |
| Topics | agent, ai, context-engineering, deepseek, interview, java, mcp, mysql, redis, redisson, skills, springai, system-design |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,421 |
| 语言 | JavaScript |
| Forks | 6,536 |
| Issues | 339 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,894 |
| 语言 | TypeScript |
| Forks | 4,792 |
| Issues | 499 |
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
| Stars | 39,194 |
| 语言 | Python |
| Forks | 6,210 |
| Issues | 85 |
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
| Stars | 95,000 |
| 语言 | Python |
| Forks | 10,707 |
| Issues | 226 |
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
| Stars | 52,988 |
| 语言 | TypeScript |
| Forks | 24,370 |
| Issues | 867 |
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
| Stars | 189,063 |
| 语言 | TypeScript |
| Forks | 57,882 |
| Issues | 1,465 |
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
| Stars | 148,614 |
| 语言 | Python |
| Forks | 9,080 |
| Issues | 932 |
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
| Stars | 65,060 |
| 语言 | Jupyter Notebook |
| Forks | 21,456 |
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
| Stars | 77,274 |
| 语言 | Rust |
| Forks | 5,028 |
| Issues | 996 |
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
| Stars | 61,082 |
| 语言 | Python |
| Forks | 6,661 |
| Issues | 665 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,358 |
| 语言 | Python |
| Forks | 16,535 |
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
| Stars | 138,116 |
| 语言 | Python |
| Forks | 19,756 |
| Issues | 272 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完善的开源AI界面解决方案，支持Ollama、OpenAI等多种后端，并内置RAG和MCP协议支持，让用户能够轻松搭建私有化的AI助手平台，兼顾功能性与隐私安全。

**技术亮点**:
- 多后端支持：同时兼容Ollama、OpenAI API、Azure OpenAI等多种LLM服务，提供统一的使用体验
- RAG检索增强生成：内置知识库功能，支持文档上传和向量检索，大幅提升问答准确性
- MCP协议支持：集成Model Context Protocol，可扩展连接多种外部工具和数据源
- 自托管部署：提供完整的Docker部署方案，支持私有化部署，数据完全留在本地
- 现代Web界面：响应式设计，支持实时流式输出、对话管理、多语言界面等功能

**适用场景**:
- 企业私有AI助手：适合需要在内部部署AI助手的企业，数据完全本地存储，满足合规和隐私要求
- 个人开发者实验：开发者可快速搭建本地LLM实验环境，支持多种模型切换测试
- 知识库问答系统：基于RAG功能，可构建文档问答、知识库检索等专业应用场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,993 |
| 语言 | Python |
| Forks | 9,274 |
| Issues | 3,047 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎之一（80K+ stars），创新性地将 RAG 与 Agent 能力融合，为 LLM 应用提供智能检索和上下文管理能力，特别适合构建企业级知识库问答系统和 AI Agent 应用。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，实现智能化的上下文理解和任务规划
- 深度文档理解：支持多格式文档的语义解析和结构化提取，包括 PDF、Word、PPT 等复杂文档
- Agentic Retrieval 能力：支持代理式检索，可自主判断检索策略和多次迭代优化查询
- 多模态上下文管理：统一处理文本、表格、图像等多种数据类型的上下文信息
- 模块化 RAG 管道：提供可配置的 RAG 流程组件，支持自定义嵌入模型和向量数据库

**适用场景**:
- 企业知识库问答系统：构建私有化知识库智能问答，支持多文档、多格式的企业资料检索和问答
- AI Agent 应用开发：作为 LLM 的智能上下文层，为 Agent 提供可靠的知识检索和上下文管理能力
- 智能客服与文档检索：集成到客服系统中，实现基于企业文档的精准自动问答



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,494 |
| 语言 | TypeScript |
| Forks | 15,245 |
| Issues | 317 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，通过"首席 Agent 运营官"理念实现了多 Agent 的统一管理和 7×24 自动化运营，支持 OpenAI、Claude、DeepSeek 等多模型集成，为开发者和企业提供了开箱即用的智能体协作解决方案。

**技术亮点**:
- 多模型支持：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，支持灵活切换和对比
- MCP 协议支持：实现 Model Context Protocol 标准化接入，扩展生态兼容性
- Agent 协作编排：支持多个 Agent 之间的任务分配、调度和协同工作，实现复杂业务流程自动化
- 知识库集成：内置 RAG 知识库系统，支持向量检索和语义理解，提升 Agent 回答准确性
- 7×24 运营能力：提供完整的 Agent 生命周期管理，包括雇佣、调度、监控和报告机制

**适用场景**:
- 企业级 AI 运营中心：构建企业内部的 AI Agent 团队，实现客户支持、数据分析、内容生成等业务的自动化运营
- 个人开发者快速原型：开发者可快速搭建多模型 Agent 系统，验证 AI 应用想法，降低开发成本
- 智能工作流自动化：通过 Agent 协作编排，将重复性工作流程（如市场调研、报告生成）交给 AI 团队自动完成



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,259 |
| 语言 | TypeScript |
| Forks | 6,657 |
| Issues | 195 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是一个 Star 数高达 77K 的开源 AI Agent 长期记忆系统，能够跨会话持久化上下文并智能注入相关记忆，兼容 8+ 主流 AI Agent（Claude Code、Copilot、Codex 等），是提升 AI 编程助手效率和连贯性的最佳开源选择。

**技术亮点**:
- 基于 RAG 架构实现智能记忆检索，使用向量嵌入（Embeddings）进行语义相似度匹配
- 支持 ChromaDB 作为向量数据库，结合 SQLite 本地持久化存储
- AI 驱动的记忆压缩技术，自动提炼和总结会话内容
- 多 Agent 统一适配层：Claude Code、OpenClaw、Codex、Copilot、Codex、Gemini、OpenCode 等
- 采用 Apache License 2.0 开源，TypeScript 实现便于二次开发和集成

**适用场景**:
- 个人开发者：让 AI 编程助手记住项目上下文、代码风格和历史决策，避免重复解释
- AI Agent 平台集成：构建具备长期记忆能力的智能助手，支持复杂多步骤任务
- 团队协作知识库：自动积累和复用团队的技术决策、代码规范和最佳实践



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,165 |
| 语言 | Python |
| Forks | 6,337 |
| Issues | 116 |
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
| Stars | 46,347 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 23 |
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
| Stars | 102,806 |
| 语言 | TypeScript |
| Forks | 12,502 |
| Issues | 1,039 |
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
| Stars | 60,421 |
| 语言 | JavaScript |
| Forks | 6,536 |
| Issues | 339 |
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
| Stars | 39,194 |
| 语言 | Python |
| Forks | 6,210 |
| Issues | 85 |
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
| Stars | 78,296 |
| 语言 | Python |
| Forks | 10,464 |
| Issues | 209 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### safishamsi/graphify

**描述**: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,691 |
| 语言 | Python |
| Forks | 5,480 |
| Issues | 273 |
| Topics | antigravity, claude-code, codex, gemini, graphrag, knowledge-graph, leiden, openclaw, rag, skills, tree-sitter |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,988 |
| 语言 | TypeScript |
| Forks | 24,370 |
| Issues | 867 |
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
| Stars | 44,391 |
| 语言 | Go |
| Forks | 4,012 |
| Issues | 911 |
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
| Stars | 35,489 |
| 语言 | Python |
| Forks | 5,016 |
| Issues | 238 |
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
| Stars | 111,358 |
| 语言 | Python |
| Forks | 16,535 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 💬 LLM 界面 (18 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,337 |
| 语言 | Python |
| Forks | 26,251 |
| Issues | 12,842 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个高度成熟的多 LLM 集成 AI Agent 框架，拥有超过 16 万 Stars 的社区认可度，支持 Claude、GPT 等主流模型，能够帮助开发者快速构建智能代理应用，非常适合希望在不锁定单一 LLM 提供商的情况下构建 AI 应用的团队和个人开发者。

**技术亮点**:
- 多 LLM 提供商集成：原生支持 Anthropic Claude、OpenAI GPT 等多种大语言模型，提供统一的 Agent 接口
- 成熟的 Agent 架构：基于 NousResearch 在 LLM 领域的深厚积累，实现了可靠的 Agent 推理和任务分解能力
- 开源且商业友好：采用 MIT 许可证，无使用限制，可直接用于商业产品开发
- 活跃的社区生态：超过 16 万 Stars 和丰富的 Topics 标签，证明了其广泛的社区参与度
- Python 生态兼容：使用 Python 开发，可无缝集成到现有的 Python 数据科学和 AI 开发工作流中

**适用场景**:
- 企业级 AI 应用开发：适合企业构建内部智能助手、自动化工作流、客服机器人等应用
- AI 产品原型快速验证：个人开发者或创业团队可以快速基于该框架搭建 AI 产品原型
- 多模型对比研究：研究人员可以通过框架快速对比不同 LLM 在特定任务上的表现



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,116 |
| 语言 | Python |
| Forks | 19,756 |
| Issues | 272 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完善的开源AI界面解决方案，支持Ollama、OpenAI等多种后端，并内置RAG和MCP协议支持，让用户能够轻松搭建私有化的AI助手平台，兼顾功能性与隐私安全。

**技术亮点**:
- 多后端支持：同时兼容Ollama、OpenAI API、Azure OpenAI等多种LLM服务，提供统一的使用体验
- RAG检索增强生成：内置知识库功能，支持文档上传和向量检索，大幅提升问答准确性
- MCP协议支持：集成Model Context Protocol，可扩展连接多种外部工具和数据源
- 自托管部署：提供完整的Docker部署方案，支持私有化部署，数据完全留在本地
- 现代Web界面：响应式设计，支持实时流式输出、对话管理、多语言界面等功能

**适用场景**:
- 企业私有AI助手：适合需要在内部部署AI助手的企业，数据完全本地存储，满足合规和隐私要求
- 个人开发者实验：开发者可快速搭建本地LLM实验环境，支持多种模型切换测试
- 知识库问答系统：基于RAG功能，可构建文档问答、知识库检索等专业应用场景



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 188,122 |
| 语言 | JavaScript |
| Forks | 29,121 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个面向多 AI 编码代理的性能优化框架，通过 Skills/Instincts/Memory 三层架构显著提升 Claude Code、Cursor 等工具的开发效率，同时内置安全机制，是 AI 原生开发团队不可或缺的效率基础设施。

**技术亮点**:
- 多代理框架兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具
- 三层记忆系统：Skills（技能库）+ Instincts（本能优化）+ Memory（持久记忆）
- MCP 协议集成：支持 Model Context Protocol 实现标准化上下文管理
- 研究优先开发模式：采用 R&D-first 方法论确保技术领先性
- MIT 许可开源：可自由商用，降低企业采用门槛

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编码代理的能力边界和安全策略
- 个人开发者：构建个人 AI 助手工作流，实现代码审查、调试、文档生成的自动化
- AI 原生应用开发：基于 ECC 框架二次开发定制化 AI 代理系统



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,229 |
| 语言 | JavaScript |
| Forks | 3,547 |
| Issues | 219 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 以其独特的穴居人语言风格幽默地解决了 LLM 开发中的核心痛点——token 消耗成本，在保持功能完整性的同时实现了 65% 的 token 削减，非常适合大规模 AI 应用场景。

**技术亮点**:
- 创新性 Token 压缩算法：通过独特的语言简化策略实现 65% token 削减
- 专为 Anthropic Claude Code 平台优化的官方集成技能
- 基于 Prompt Engineering 的轻量级解决方案，无需额外模型或基础设施
- 开源 MIT 许可证，代码可自由使用和修改
- 社区反响强烈，63,000+ Stars 验证了其实际价值

**适用场景**:
- 大规模 API 调用场景：对于高频调用 LLM API 的应用（如聊天机器人、内容生成平台），显著降低运营成本
- Claude Code 用户：直接在 Claude Code 环境中使用，优化开发工作流中的 AI 交互效率
- 个人开发者和初创公司：预算有限但需要大量使用 LLM 能力的项目，通过 token 优化最大化资源利用率
- 企业级 AI 应用：需要精细化成本控制的 Production 环境 AI 集成



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,494 |
| 语言 | TypeScript |
| Forks | 15,245 |
| Issues | 317 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是一个开源的 AI Agent 编排平台，通过"首席 Agent 运营官"理念实现了多 Agent 的统一管理和 7×24 自动化运营，支持 OpenAI、Claude、DeepSeek 等多模型集成，为开发者和企业提供了开箱即用的智能体协作解决方案。

**技术亮点**:
- 多模型支持：无缝集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，支持灵活切换和对比
- MCP 协议支持：实现 Model Context Protocol 标准化接入，扩展生态兼容性
- Agent 协作编排：支持多个 Agent 之间的任务分配、调度和协同工作，实现复杂业务流程自动化
- 知识库集成：内置 RAG 知识库系统，支持向量检索和语义理解，提升 Agent 回答准确性
- 7×24 运营能力：提供完整的 Agent 生命周期管理，包括雇佣、调度、监控和报告机制

**适用场景**:
- 企业级 AI 运营中心：构建企业内部的 AI Agent 团队，实现客户支持、数据分析、内容生成等业务的自动化运营
- 个人开发者快速原型：开发者可快速搭建多模型 Agent 系统，验证 AI 应用想法，降低开发成本
- 智能工作流自动化：通过 Agent 协作编排，将重复性工作流程（如市场调研、报告生成）交给 AI 团队自动完成



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,259 |
| 语言 | TypeScript |
| Forks | 6,657 |
| Issues | 195 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是一个 Star 数高达 77K 的开源 AI Agent 长期记忆系统，能够跨会话持久化上下文并智能注入相关记忆，兼容 8+ 主流 AI Agent（Claude Code、Copilot、Codex 等），是提升 AI 编程助手效率和连贯性的最佳开源选择。

**技术亮点**:
- 基于 RAG 架构实现智能记忆检索，使用向量嵌入（Embeddings）进行语义相似度匹配
- 支持 ChromaDB 作为向量数据库，结合 SQLite 本地持久化存储
- AI 驱动的记忆压缩技术，自动提炼和总结会话内容
- 多 Agent 统一适配层：Claude Code、OpenClaw、Codex、Copilot、Codex、Gemini、OpenCode 等
- 采用 Apache License 2.0 开源，TypeScript 实现便于二次开发和集成

**适用场景**:
- 个人开发者：让 AI 编程助手记住项目上下文、代码风格和历史决策，避免重复解释
- AI Agent 平台集成：构建具备长期记忆能力的智能助手，支持复杂多步骤任务
- 团队协作知识库：自动积累和复用团队的技术决策、代码规范和最佳实践



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,626 |
| 语言 | HTML |
| Forks | 21,160 |
| Issues | 48 |
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
| Stars | 61,798 |
| 语言 | Python |
| Forks | 10,099 |
| Issues | 131 |
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
| Stars | 54,183 |
| 语言 | HTML |
| Forks | 5,431 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,420 |
| 语言 | Python |
| Forks | 9,433 |
| Issues | 402 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,421 |
| 语言 | JavaScript |
| Forks | 6,536 |
| Issues | 339 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,894 |
| 语言 | TypeScript |
| Forks | 4,792 |
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
| Stars | 52,988 |
| 语言 | TypeScript |
| Forks | 24,370 |
| Issues | 867 |
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
| Stars | 80,665 |
| 语言 | Python |
| Forks | 17,069 |
| Issues | 5,020 |
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
| Stars | 88,063 |
| 语言 | TypeScript |
| Forks | 59,703 |
| Issues | 827 |
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
| Stars | 148,614 |
| 语言 | Python |
| Forks | 9,080 |
| Issues | 932 |
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
| Stars | 61,082 |
| 语言 | Python |
| Forks | 6,661 |
| Issues | 665 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,925 |
| 语言 | Go |
| Forks | 16,230 |
| Issues | 3,264 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
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
| Stars | 71,480 |
| 语言 | Python |
| Forks | 8,718 |
| Issues | 1,014 |
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
| Stars | 67,897 |
| 语言 | Python |
| Forks | 6,831 |
| Issues | 84 |
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
| Stars | 162,626 |
| 语言 | HTML |
| Forks | 21,160 |
| Issues | 48 |
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
| Stars | 95,352 |
| 语言 | Jupyter Notebook |
| Forks | 14,604 |
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
| Stars | 160,848 |
| 语言 | Python |
| Forks | 33,291 |
| Issues | 2,376 |
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
| Stars | 80,665 |
| 语言 | Python |
| Forks | 17,069 |
| Issues | 5,020 |
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
| Stars | 113,875 |
| 语言 | Python |
| Forks | 13,332 |
| Issues | 4,025 |
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
| Stars | 100,064 |
| 语言 | Python |
| Forks | 27,846 |
| Issues | 18,514 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (19 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 188,122 |
| 语言 | JavaScript |
| Forks | 29,121 |
| Issues | 11 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个面向多 AI 编码代理的性能优化框架，通过 Skills/Instincts/Memory 三层架构显著提升 Claude Code、Cursor 等工具的开发效率，同时内置安全机制，是 AI 原生开发团队不可或缺的效率基础设施。

**技术亮点**:
- 多代理框架兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具
- 三层记忆系统：Skills（技能库）+ Instincts（本能优化）+ Memory（持久记忆）
- MCP 协议集成：支持 Model Context Protocol 实现标准化上下文管理
- 研究优先开发模式：采用 R&D-first 方法论确保技术领先性
- MIT 许可开源：可自由商用，降低企业采用门槛

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编码代理的能力边界和安全策略
- 个人开发者：构建个人 AI 助手工作流，实现代码审查、调试、文档生成的自动化
- AI 原生应用开发：基于 ECC 框架二次开发定制化 AI 代理系统



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,390 |
| 语言 | Go |
| Forks | 4,093 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，配合 OpenAI 兼容 API，可轻松实现私有化 AI 部署，特别适合隐私敏感场景和资源有限的环境。

**技术亮点**:
- 多模态模型支持：支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理
- 硬件兼容性：支持 CPU 运行，无需昂贵 GPU，降低部署门槛
- 丰富的模型支持：兼容 Llama、Mamba 等主流开源模型，支持 rerank 等高级功能
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用迁移

**适用场景**:
- 私有化 AI 部署：企业可在本地环境部署 AI 服务，数据不出本地，满足合规和隐私要求
- 边缘计算场景：在没有 GPU 的边缘设备上运行 AI 推理，适合 IoT 和嵌入式场景
- 开发者快速原型：开发者可以通过兼容 API 快速搭建 AI 应用原型，降低开发成本



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,347 |
| 语言 | Java |
| Forks | 15,998 |
| Issues | 23 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,420 |
| 语言 | Python |
| Forks | 9,433 |
| Issues | 402 |
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
| Stars | 58,894 |
| 语言 | TypeScript |
| Forks | 4,792 |
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
| Stars | 189,063 |
| 语言 | TypeScript |
| Forks | 57,882 |
| Issues | 1,465 |
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
| Stars | 61,082 |
| 语言 | Python |
| Forks | 6,661 |
| Issues | 665 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,292 |
| 语言 | JavaScript |
| Forks | 4,221 |
| Issues | 1,155 |
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
| Stars | 436,371 |
| 语言 | Python |
| Forks | 47,840 |
| Issues | 1,363 |
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
| Stars | 163,701 |
| 语言 | Python |
| Forks | 13,764 |
| Issues | 2,513 |
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
| Stars | 98,410 |
| 语言 | Python |
| Forks | 9,325 |
| Issues | 185 |
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
| Stars | 83,562 |
| 语言 | Python |
| Forks | 9,755 |
| Issues | 269 |
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
| Stars | 185,183 |
| 语言 | TypeScript |
| Forks | 40,039 |
| Issues | 17,906 |
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
| Stars | 94,351 |
| 语言 | TypeScript |
| Forks | 9,424 |
| Issues | 268 |
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
| Stars | 79,247 |
| 语言 | TypeScript |
| Forks | 5,885 |
| Issues | 731 |
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
| Stars | 80,408 |
| 语言 | Go |
| Forks | 2,803 |
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
| Stars | 78,270 |
| 语言 | Go |
| Forks | 2,841 |
| Issues | 967 |
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
| Stars | 44,501 |
| 语言 | Go |
| Forks | 8,463 |
| Issues | 1,019 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ⭐ 中优先级


### spf13/cobra

**描述**: A Commander for modern Go CLI interactions

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 43,971 |
| 语言 | Go |
| Forks | 3,145 |
| Issues | 369 |
| Topics | cli, cli-app, cobra, cobra-generator, cobra-library, command, command-cobra, command-line, commandline, go, golang, golang-application, golang-library, posix, posix-compliant-flags, subcommands |
| 许可证 | Apache License 2.0 |


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
| Stars | 58,894 |
| 语言 | TypeScript |
| Forks | 4,792 |
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
| Stars | 189,063 |
| 语言 | TypeScript |
| Forks | 57,882 |
| Issues | 1,465 |
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
| Stars | 61,082 |
| 语言 | Python |
| Forks | 6,661 |
| Issues | 665 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,720 |
| 语言 | Go |
| Forks | 10,362 |
| Issues | 251 |
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
| Stars | 122,386 |
| 语言 | Go |
| Forks | 43,130 |
| Issues | 2,724 |
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
| Stars | 71,584 |
| 语言 | Go |
| Forks | 18,952 |
| Issues | 3,773 |
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
| Stars | 55,830 |
| 语言 | Go |
| Forks | 6,708 |
| Issues | 2,788 |
| Topics | bitbucket, cicd, devops, docker-registry-v2, git, git-gui, git-lfs, git-server, gitea, github, github-actions, gitlab, go, golang, hacktoberfest, maven-server, npm-registry, self-hosted, typescript, vue |
| 许可证 | MIT License |


### gogs/gogs

**描述**: The painless way to host your own Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,545 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 988 |
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
| Stars | 94,351 |
| 语言 | TypeScript |
| Forks | 9,424 |
| Issues | 268 |
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
| Stars | 79,075 |
| 语言 | TypeScript |
| Forks | 6,923 |
| Issues | 401 |
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
| Stars | 87,068 |
| 语言 | JavaScript |
| Forks | 7,880 |
| Issues | 751 |
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
| Stars | 70,442 |
| 语言 | Go |
| Forks | 1,930 |
| Issues | 330 |
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
| Stars | 63,255 |
| 语言 | Go |
| Forks | 6,006 |
| Issues | 835 |
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
| Stars | 59,886 |
| 语言 | Go |
| Forks | 4,383 |
| Issues | 27 |
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
| Stars | 60,979 |
| 语言 | Go |
| Forks | 7,514 |
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
| Stars | 87,068 |
| 语言 | JavaScript |
| Forks | 7,880 |
| Issues | 751 |
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
| Stars | 64,119 |
| 语言 | Go |
| Forks | 10,421 |
| Issues | 787 |
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
| Stars | 46,390 |
| 语言 | Go |
| Forks | 4,093 |
| Issues | 162 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLM、视觉、语音、图像、视频等多种模型，无需 GPU 即可运行，配合 OpenAI 兼容 API，可轻松实现私有化 AI 部署，特别适合隐私敏感场景和资源有限的环境。

**技术亮点**:
- 多模态模型支持：支持 LLMs、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化 AI 推理
- 硬件兼容性：支持 CPU 运行，无需昂贵 GPU，降低部署门槛
- 丰富的模型支持：兼容 Llama、Mamba 等主流开源模型，支持 rerank 等高级功能
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用迁移

**适用场景**:
- 私有化 AI 部署：企业可在本地环境部署 AI 服务，数据不出本地，满足合规和隐私要求
- 边缘计算场景：在没有 GPU 的边缘设备上运行 AI 推理，适合 IoT 和嵌入式场景
- 开发者快速原型：开发者可以通过兼容 API 快速搭建 AI 应用原型，降低开发成本



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 436,371 |
| 语言 | Python |
| Forks | 47,840 |
| Issues | 1,363 |
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
| Stars | 98,410 |
| 语言 | Python |
| Forks | 9,325 |
| Issues | 185 |
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
| Stars | 87,513 |
| 语言 | Python |
| Forks | 33,927 |
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
| Stars | 100,131 |
| 语言 | TypeScript |
| Forks | 27,240 |
| Issues | 1,166 |
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
| Stars | 79,247 |
| 语言 | TypeScript |
| Forks | 5,885 |
| Issues | 731 |
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
| Stars | 69,050 |
| 语言 | JavaScript |
| Forks | 23,405 |
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
| Stars | 55,948 |
| 语言 | JavaScript |
| Forks | 10,188 |
| Issues | 375 |
| Topics | blog, compiler, gatsby, graphql, react, static-site-generator, web-app |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,631 |
| 语言 | Go |
| Forks | 4,751 |
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
| Stars | 58,467 |
| 语言 | Go |
| Forks | 3,388 |
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
| Stars | 88,553 |
| 语言 | Go |
| Forks | 8,608 |
| Issues | 690 |
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
| Stars | 102,806 |
| 语言 | TypeScript |
| Forks | 12,502 |
| Issues | 1,039 |
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
| Stars | 60,421 |
| 语言 | JavaScript |
| Forks | 6,536 |
| Issues | 339 |
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
| Stars | 44,391 |
| 语言 | Go |
| Forks | 4,012 |
| Issues | 911 |
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
| Stars | 51,720 |
| 语言 | Go |
| Forks | 10,362 |
| Issues | 251 |
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
| Stars | 63,229 |
| 语言 | JavaScript |
| Forks | 3,547 |
| Issues | 219 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 以其独特的穴居人语言风格幽默地解决了 LLM 开发中的核心痛点——token 消耗成本，在保持功能完整性的同时实现了 65% 的 token 削减，非常适合大规模 AI 应用场景。

**技术亮点**:
- 创新性 Token 压缩算法：通过独特的语言简化策略实现 65% token 削减
- 专为 Anthropic Claude Code 平台优化的官方集成技能
- 基于 Prompt Engineering 的轻量级解决方案，无需额外模型或基础设施
- 开源 MIT 许可证，代码可自由使用和修改
- 社区反响强烈，63,000+ Stars 验证了其实际价值

**适用场景**:
- 大规模 API 调用场景：对于高频调用 LLM API 的应用（如聊天机器人、内容生成平台），显著降低运营成本
- Claude Code 用户：直接在 Claude Code 环境中使用，优化开发工作流中的 AI 交互效率
- 个人开发者和初创公司：预算有限但需要大量使用 LLM 能力的项目，通过 token 优化最大化资源利用率
- 企业级 AI 应用：需要精细化成本控制的 Production 环境 AI 集成



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,626 |
| 语言 | HTML |
| Forks | 21,160 |
| Issues | 48 |
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
| Stars | 61,798 |
| 语言 | Python |
| Forks | 10,099 |
| Issues | 131 |
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
| Stars | 52,165 |
| 语言 | Python |
| Forks | 6,337 |
| Issues | 116 |
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
| Stars | 90,032 |
| 语言 | TypeScript |
| Forks | 10,075 |
| Issues | 2,053 |
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
| Stars | 88,203 |
| 语言 | TypeScript |
| Forks | 9,002 |
| Issues | 1,667 |
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
| Stars | 173,269 |
| 语言 | Go |
| Forks | 13,240 |
| Issues | 185 |
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
| Stars | 127,885 |
| 语言 | JavaScript |
| Forks | 12,485 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (57 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,016 |
| 语言 | Unknown |
| Forks | 34,398 |
| Issues | 148 |
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
| Stars | 98,876 |
| 语言 | Shell |
| Forks | 8,749 |
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
| Stars | 104,511 |
| 语言 | Python |
| Forks | 9,212 |
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
| Stars | 93,262 |
| 语言 | Python |
| Forks | 13,577 |
| Issues | 119 |
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
| Stars | 388,683 |
| 语言 | Python |
| Forks | 66,335 |
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
| Stars | 119,913 |
| 语言 | TypeScript |
| Forks | 8,734 |
| Issues | 344 |
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
| Stars | 116,397 |
| 语言 | TypeScript |
| Forks | 6,158 |
| Issues | 8 |
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
| Stars | 100,436 |
| 语言 | TypeScript |
| Forks | 14,952 |
| Issues | 556 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,513 |
| 语言 | JavaScript |
| Forks | 5,390 |
| Issues | 78 |
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
| Stars | 48,445 |
| 语言 | Go |
| Forks | 10,350 |
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
| Stars | 112,120 |
| 语言 | C++ |
| Forks | 18,564 |
| Issues | 1,714 |
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
| Stars | 63,248 |
| 语言 | Python |
| Forks | 1,672 |
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
| Stars | 39,574 |
| 语言 | TypeScript |
| Forks | 4,516 |
| Issues | 316 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 298,867 |
| 语言 | Python |
| Forks | 27,940 |
| Issues | 18 |
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
| Stars | 221,284 |
| 语言 | Python |
| Forks | 50,663 |
| Issues | 919 |
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
| Stars | 87,174 |
| 语言 | Python |
| Forks | 37,544 |
| Issues | 4,237 |
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
| Stars | 77,661 |
| 语言 | Python |
| Forks | 45,084 |
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
| Stars | 445,248 |
| 语言 | TypeScript |
| Forks | 44,662 |
| Issues | 182 |
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
| Stars | 355,191 |
| 语言 | TypeScript |
| Forks | 44,093 |
| Issues | 19 |
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
| Stars | 123,781 |
| 语言 | TypeScript |
| Forks | 13,732 |
| Issues | 3,082 |
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
| Stars | 114,811 |
| 语言 | TypeScript |
| Forks | 8,872 |
| Issues | 1,940 |
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
| Stars | 108,920 |
| 语言 | TypeScript |
| Forks | 13,406 |
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
| Stars | 101,246 |
| 语言 | TypeScript |
| Forks | 5,656 |
| Issues | 659 |
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
| Stars | 98,103 |
| 语言 | TypeScript |
| Forks | 54,604 |
| Issues | 1,368 |
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
| Stars | 95,083 |
| 语言 | TypeScript |
| Forks | 5,258 |
| Issues | 87 |
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
| Stars | 86,055 |
| 语言 | TypeScript |
| Forks | 10,780 |
| Issues | 502 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,462 |
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
| Stars | 80,750 |
| 语言 | TypeScript |
| Forks | 8,203 |
| Issues | 724 |
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
| Stars | 245,166 |
| 语言 | JavaScript |
| Forks | 51,089 |
| Issues | 1,310 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 195,980 |
| 语言 | JavaScript |
| Forks | 31,065 |
| Issues | 402 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,320 |
| 语言 | JavaScript |
| Forks | 35,588 |
| Issues | 2,578 |
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
| Stars | 112,601 |
| 语言 | JavaScript |
| Forks | 36,376 |
| Issues | 448 |
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
| Stars | 109,069 |
| 语言 | JavaScript |
| Forks | 11,712 |
| Issues | 163 |
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
| Stars | 98,360 |
| 语言 | JavaScript |
| Forks | 32,629 |
| Issues | 1,526 |
| Topics | design-system, material-design, material-ui, react, react-components |
| 许可证 | MIT License |


### sveltejs/svelte

**描述**: web development for the rest of us

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,611 |
| 语言 | JavaScript |
| Forks | 4,920 |
| Issues | 1,001 |
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
| Stars | 71,252 |
| 语言 | JavaScript |
| Forks | 16,806 |
| Issues | 898 |
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
| Stars | 65,767 |
| 语言 | JavaScript |
| Forks | 9,354 |
| Issues | 190 |
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
| Stars | 64,840 |
| 语言 | JavaScript |
| Forks | 4,118 |
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
| Stars | 61,221 |
| 语言 | JavaScript |
| Forks | 5,676 |
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
| Forks | 20,427 |
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
| Stars | 57,456 |
| 语言 | JavaScript |
| Forks | 12,302 |
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
| Stars | 53,595 |
| 语言 | JavaScript |
| Forks | 11,647 |
| Issues | 274 |
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
| Stars | 53,354 |
| 语言 | JavaScript |
| Forks | 10,621 |
| Issues | 449 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,003 |
| 语言 | Go |
| Forks | 19,037 |
| Issues | 10,114 |
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
| Stars | 106,724 |
| 语言 | Go |
| Forks | 15,047 |
| Issues | 47 |
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
| Stars | 88,198 |
| 语言 | Go |
| Forks | 8,266 |
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
| Stars | 84,278 |
| 语言 | Go |
| Forks | 5,199 |
| Issues | 388 |
| Topics | go, p2p, peer-to-peer, synchronization |
| 许可证 | Mozilla Public License 2.0 |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,315 |
| 语言 | Go |
| Forks | 5,103 |
| Issues | 1,180 |
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
| Stars | 51,054 |
| 语言 | Go |
| Forks | 21,926 |
| Issues | 396 |
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
| Stars | 49,512 |
| 语言 | Go |
| Forks | 7,943 |
| Issues | 564 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,850 |
| 语言 | Python |
| Forks | 16,980 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 95,778 |
| 语言 | JavaScript |
| Forks | 15,502 |
| Issues | 63 |
| Topics | css, curriculum, education, html, javascript, learning, microsoft-for-beginners, tutorials |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,762 |
| 语言 | JavaScript |
| Forks | 4,631 |
| Issues | 106 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,451 |
| 语言 | JavaScript |
| Forks | 9,189 |
| Issues | 4 |
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
| Stars | 61,237 |
| 语言 | JavaScript |
| Forks | 7,158 |
| Issues | 143 |
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
| Stars | 46,849 |
| 语言 | Go |
| Forks | 8,848 |
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
| Stars | 157,999 |
| 语言 | Python |
| Forks | 12,028 |
| Issues | 386 |
| Topics | awesome, github, hellogithub, python |
