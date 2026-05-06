# 项目发现报告 (2026-05-06)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 122 |
| 去重移除 | 34 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 66 |

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
| Stars | 135,785 |
| 语言 | Python |
| Forks | 19,334 |
| Issues | 355 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最流行的开源 LLM 界面项目，提供类似 ChatGPT 的现代化体验，同时支持 Ollama、OpenAI API 等多种后端，可完全自托管部署，特别适合注重数据隐私和希望灵活切换大模型服务的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，支持无缝切换
- RAG 检索增强生成：内置文档向量化和语义搜索能力，支持知识库问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展功能和集成外部工具
- 现代化 Web 界面：基于 React 构建的响应式 UI，支持实时流式响应和 Markdown 渲染
- 自托管部署：支持 Docker 一键部署，数据完全本地存储，保障隐私安全

**适用场景**:
- 企业私有化 AI 助手：需要本地部署、数据不出网的场景，部署内部知识库问答系统
- 个人开发者本地开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 获得更好的交互体验
- 多模型统一管理：同时使用多个 LLM 服务，通过统一界面进行管理和对比测试



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,732 |
| 语言 | Python |
| Forks | 20,785 |
| Issues | 8,586 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由 NousResearch 打造的高人气开源 AI Agent 框架（135K+ Stars），支持 Anthropic Claude、OpenAI 等多 LLM 后端统一抽象，其"随你成长"的理念和模块化架构设计让开发者能快速构建和迭代智能代理系统，是当前 AI Agent 领域最具影响力的开源项目之一。

**技术亮点**:
- 多 LLM 后端统一抽象：支持 Anthropic Claude、OpenAI GPT 等主流大模型，通过标准化接口实现无缝切换
- 模块化 Agent 架构：采用可组合组件设计，便于扩展工具链、记忆系统和执行策略
- 丰富的工具生态集成：开箱即用支持代码执行、API 调用、数据库查询，深度集成 Claude Code、OpenClaw 等能力
- 企业级部署友好：MIT 许可证允许商业使用，Python 原生实现便于与现有 ML 基础设施集成
- 活跃的开源社区：135K+ Stars 表明项目维护积极、文档完善、问题响应迅速

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理自动化、数据分析助手等企业级 AI 应用
- 开发者效率工具：集成到 IDE/CLI 实现智能代码补全、Bug 修复、代码审查等开发辅助
- AI 原生应用开发：快速原型验证和构建新一代 AI-first 产品，如个人助手、工作流自动化工具



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,821 |
| 语言 | Python |
| Forks | 9,086 |
| Issues | 3,003 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源 RAG 领域的标杆项目，将 RAG 与 Agent 深度融合，为 LLM 提供精准的上下文增强能力，近 8 万 star 证明了其技术实力和社区认可度，是构建企业级 LLM 应用的首选技术栈。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与智能代理能力结合，实现更智能的上下文理解和任务执行
- 深度文档理解：支持 PDF、Word、Excel 等多格式复杂文档的智能解析和向量化
- Agentic Retrieval 能力：具备自主规划、拆解任务、迭代检索的智能代理特性，而非简单关键词匹配
- 灵活的 LLM 集成：支持 OpenAI、Claude、本地部署等多种大模型，可根据场景选择最优方案
- 可视化知识库管理：提供直观的界面用于文档上传、切片策略配置、检索测试等全流程操作

**适用场景**:
- 企业智能知识库：构建支持自然语言查询的内部知识检索系统，如 HR 政策文档、技术文档、合同管理等场景的智能问答
- 文档智能分析平台：自动化处理和分析大量业务文档，实现智能摘要、关键信息提取、合规检查等
- 智能客服增强：为现有客服系统提供 RAG 增强的对话能力，提升问题回答的准确性和上下文连贯性



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 174,595 |
| 语言 | JavaScript |
| Forks | 27,016 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Memory、Security 等机制显著提升开发效率，特别适合希望深度定制和优化 AI 编码体验的开发者。

**技术亮点**:
- 跨平台 AI 代理支持：统一支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具，提供一致的性能优化体验
- MCP (Model Context Protocol) 集成：基于标准化的模型上下文协议，实现与各类 AI 代理的无缝连接和扩展
- Memory 记忆系统：实现持久化上下文记忆，让 AI 代理能够跨会话保持状态和关键信息
- Skills & Instincts 机制：通过预定义的技能和本能模式，提升 AI 代理的响应质量和准确性
- Security First 设计：在 AI 代理系统中内置安全防护机制，确保代码生成和执行的安全性

**适用场景**:
- 企业级 AI 辅助开发：为开发团队提供统一的 AI 编程工具管理和性能优化，提升整体开发效率
- 个人开发者效率提升：定制化配置 AI 代理的行为模式和记忆系统，打造个人专属的开发助手
- AI 研究与实验：作为 research-first 开发框架，用于探索和实验新的 AI 代理优化策略
- 跨工具迁移：帮助开发者在不同 AI 编程工具之间迁移配置和经验，保持工作流的连续性



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,092 |
| 语言 | Go |
| Forks | 4,061 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源的本地 AI 推理引擎，可在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，大幅降低部署成本并保护数据隐私，46k+ Stars 证明其成熟度和社区活跃度

**技术亮点**:
- 多模态支持：一站式支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测、重新排序等多种 AI 任务
- Go 语言高性能架构：优秀的并发处理能力和跨平台兼容性，部署简单
- 去中心化分布式设计：基于 libp2p 实现分布式部署，适合构建私有化 AI 服务网络
- 零 GPU 依赖：可在 CPU 上运行主流模型，大幅降低硬件投入门槛
- 丰富的协议支持：内置 MCP（Model Context Protocol）支持和标准 REST API，便于系统集成

**适用场景**:
- 企业私有化 AI 部署：数据合规和隐私保护需求的企业可将 AI 能力完全部署在本地
- 开发者快速原型验证：个人开发者或团队低成本快速搭建 AI 应用原型，无需云服务和 GPU 资源
- 边缘计算与离线场景：在边缘设备、无网络环境或低延迟需求场景中提供本地 AI 推理能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,127 |
| 语言 | TypeScript |
| Forks | 15,083 |
| Issues | 758 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，拥有超过 76k Stars 的庞大社区支持，集成了 OpenAI、Claude、DeepSeek、Gemini 等主流 AI 模型，支持 MCP 协议和知识库管理，为开发者和企业提供了从 Agent 设计到团队协作的完整解决方案，是构建智能 Agent 应用的优秀起点。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工与配合，突破单一 Agent 的能力边界
- 全模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：遵循 MCP 协议标准，实现 Agent 与外部工具和服务的标准化连接
- 知识库管理：内置 RAG 能力，支持向量存储和检索，增强 Agent 的领域知识和上下文理解
- TypeScript/React 技术栈：基于现代前端技术构建，提供类型安全的开发和优秀的可维护性

**适用场景**:
- 企业级 Agent 应用开发：构建客服、销售、运营等业务场景的 AI Agent 团队，实现自动化工作流
- AI Agent 研究与实验：利用平台提供的多 Agent 协作框架，探索 Agent 自主决策和协作的新范式
- 个人 AI 助手搭建：集成多种 AI 模型的能力，构建个性化的 AI 工作站，支持知识管理和任务协作



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,884 |
| 语言 | TypeScript |
| Forks | 6,260 |
| Issues | 86 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 嵌入向量技术为 Claude Code 赋予了长期记忆能力，解决了 AI 编程助手的"会话失忆"痛点，让 Claude 能够跨会话理解项目上下文和开发者偏好，大幅提升长期编码效率。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义相似度检索
- 使用 Claude 自身的 agent-sdk 进行 AI 压缩，在本地完成信息提炼
- 混合存储方案：ChromaDB 存储语义嵌入 + SQLite 存储结构化元数据
- 支持向量嵌入生成，自动将代码片段、命令执行结果转为可检索的语义向量
- 作为 Claude Code 原生插件集成，开箱即用的非侵入式架构

**适用场景**:
- 复杂项目的长期开发维护：Claude 能记住项目架构决策、已解决的 bug 和代码规范，跨月甚至跨年保持上下文连贯
- 团队协作场景：同一项目多个开发者可共享 Claude 的项目记忆，避免重复解释背景
- 个性化 AI 编程助手：Claude 学习并记住开发者的编码风格、常用工具和偏好设置



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,975 |
| 语言 | Python |
| Forks | 8,671 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的大模型微调框架，支持 100+ 主流 LLMs 和 VLMs 的统一高效微调，提供 LoRA/QLoRA/RLHF 等多种技术，一站式解决大模型定制化难题，大幅降低微调门槛。

**技术亮点**:
- 支持 100+ 开源大模型（Llama/Qwen/Gemma/DeepSeek/Mistral 等）和视觉语言模型，统一接口设计
- 集成 PEFT 技术生态，支持 LoRA、QLoRA、Prefix Tuning、Ptuning 等多种轻量化微调方法
- 内置 RLHF 完整流程（PPO/DPO/KTO），支持人类反馈强化学习训练
- 支持 4-bit/8-bit 量化训练，结合 Flash Attention 2 和 gradient checkpointing 优化显存
- 提供 WebUI、CLI、Python API 三种使用方式，支持多卡分布式训练和混合精度计算

**适用场景**:
- 企业级 LLM 定制：企业可基于 LlamaFactory 快速将通用大模型微调为领域专用模型（如客服、医疗、金融），结合量化技术实现低成本的本地化部署
- 学术研究与实验：研究人员可便捷对比不同微调方法（LoRA vs PPO vs DPO）在各模型上的效果，加速 NLP 论文实验迭代
- 个人开发者微调：个人开发者无需深入理解底层原理，通过简单配置即可对自己的数据集训练专属 AI 助手



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,370 |
| 语言 | HTML |
| Forks | 5,112 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,089 |
| 语言 | Java |
| Forks | 15,967 |
| Issues | 16 |
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
| Stars | 42,968 |
| 语言 | Python |
| Forks | 5,206 |
| Issues | 106 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,121 |
| 语言 | Python |
| Forks | 6,199 |
| Issues | 77 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,065 |
| 语言 | TypeScript |
| Forks | 4,994 |
| Issues | 546 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,967 |
| 语言 | TypeScript |
| Forks | 7,281 |
| Issues | 306 |
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
| Stars | 59,612 |
| 语言 | JavaScript |
| Forks | 6,442 |
| Issues | 347 |
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
| Stars | 72,753 |
| 语言 | Python |
| Forks | 9,215 |
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
| Stars | 56,181 |
| 语言 | TypeScript |
| Forks | 4,575 |
| Issues | 650 |
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
| Stars | 109,045 |
| 语言 | Python |
| Forks | 16,131 |
| Issues | 7 |
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
| Stars | 92,495 |
| 语言 | Python |
| Forks | 10,487 |
| Issues | 234 |
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
| Stars | 52,603 |
| 语言 | TypeScript |
| Forks | 24,278 |
| Issues | 834 |
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
| Stars | 186,888 |
| 语言 | TypeScript |
| Forks | 57,405 |
| Issues | 1,442 |
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
| Stars | 155,440 |
| 语言 | Java |
| Forks | 46,146 |
| Issues | 63 |
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
| Stars | 147,775 |
| 语言 | Python |
| Forks | 8,915 |
| Issues | 931 |
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
| Stars | 60,673 |
| 语言 | Jupyter Notebook |
| Forks | 20,538 |
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
| Stars | 58,323 |
| 语言 | Python |
| Forks | 6,308 |
| Issues | 575 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,506 |
| 语言 | TypeScript |
| Forks | 9,600 |
| Issues | 116 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,108 |
| 语言 | Rust |
| Forks | 3,955 |
| Issues | 751 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


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
| Stars | 135,785 |
| 语言 | Python |
| Forks | 19,334 |
| Issues | 355 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最流行的开源 LLM 界面项目，提供类似 ChatGPT 的现代化体验，同时支持 Ollama、OpenAI API 等多种后端，可完全自托管部署，特别适合注重数据隐私和希望灵活切换大模型服务的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，支持无缝切换
- RAG 检索增强生成：内置文档向量化和语义搜索能力，支持知识库问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展功能和集成外部工具
- 现代化 Web 界面：基于 React 构建的响应式 UI，支持实时流式响应和 Markdown 渲染
- 自托管部署：支持 Docker 一键部署，数据完全本地存储，保障隐私安全

**适用场景**:
- 企业私有化 AI 助手：需要本地部署、数据不出网的场景，部署内部知识库问答系统
- 个人开发者本地开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 获得更好的交互体验
- 多模型统一管理：同时使用多个 LLM 服务，通过统一界面进行管理和对比测试



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,821 |
| 语言 | Python |
| Forks | 9,086 |
| Issues | 3,003 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源 RAG 领域的标杆项目，将 RAG 与 Agent 深度融合，为 LLM 提供精准的上下文增强能力，近 8 万 star 证明了其技术实力和社区认可度，是构建企业级 LLM 应用的首选技术栈。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与智能代理能力结合，实现更智能的上下文理解和任务执行
- 深度文档理解：支持 PDF、Word、Excel 等多格式复杂文档的智能解析和向量化
- Agentic Retrieval 能力：具备自主规划、拆解任务、迭代检索的智能代理特性，而非简单关键词匹配
- 灵活的 LLM 集成：支持 OpenAI、Claude、本地部署等多种大模型，可根据场景选择最优方案
- 可视化知识库管理：提供直观的界面用于文档上传、切片策略配置、检索测试等全流程操作

**适用场景**:
- 企业智能知识库：构建支持自然语言查询的内部知识检索系统，如 HR 政策文档、技术文档、合同管理等场景的智能问答
- 文档智能分析平台：自动化处理和分析大量业务文档，实现智能摘要、关键信息提取、合规检查等
- 智能客服增强：为现有客服系统提供 RAG 增强的对话能力，提升问题回答的准确性和上下文连贯性



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,127 |
| 语言 | TypeScript |
| Forks | 15,083 |
| Issues | 758 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，拥有超过 76k Stars 的庞大社区支持，集成了 OpenAI、Claude、DeepSeek、Gemini 等主流 AI 模型，支持 MCP 协议和知识库管理，为开发者和企业提供了从 Agent 设计到团队协作的完整解决方案，是构建智能 Agent 应用的优秀起点。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工与配合，突破单一 Agent 的能力边界
- 全模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：遵循 MCP 协议标准，实现 Agent 与外部工具和服务的标准化连接
- 知识库管理：内置 RAG 能力，支持向量存储和检索，增强 Agent 的领域知识和上下文理解
- TypeScript/React 技术栈：基于现代前端技术构建，提供类型安全的开发和优秀的可维护性

**适用场景**:
- 企业级 Agent 应用开发：构建客服、销售、运营等业务场景的 AI Agent 团队，实现自动化工作流
- AI Agent 研究与实验：利用平台提供的多 Agent 协作框架，探索 Agent 自主决策和协作的新范式
- 个人 AI 助手搭建：集成多种 AI 模型的能力，构建个性化的 AI 工作站，支持知识管理和任务协作



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,884 |
| 语言 | TypeScript |
| Forks | 6,260 |
| Issues | 86 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 嵌入向量技术为 Claude Code 赋予了长期记忆能力，解决了 AI 编程助手的"会话失忆"痛点，让 Claude 能够跨会话理解项目上下文和开发者偏好，大幅提升长期编码效率。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义相似度检索
- 使用 Claude 自身的 agent-sdk 进行 AI 压缩，在本地完成信息提炼
- 混合存储方案：ChromaDB 存储语义嵌入 + SQLite 存储结构化元数据
- 支持向量嵌入生成，自动将代码片段、命令执行结果转为可检索的语义向量
- 作为 Claude Code 原生插件集成，开箱即用的非侵入式架构

**适用场景**:
- 复杂项目的长期开发维护：Claude 能记住项目架构决策、已解决的 bug 和代码规范，跨月甚至跨年保持上下文连贯
- 团队协作场景：同一项目多个开发者可共享 Claude 的项目记忆，避免重复解释背景
- 个性化 AI 编程助手：Claude 学习并记住开发者的编码风格、常用工具和偏好设置



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,089 |
| 语言 | Java |
| Forks | 15,967 |
| Issues | 16 |
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
| Stars | 42,968 |
| 语言 | Python |
| Forks | 5,206 |
| Issues | 106 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,121 |
| 语言 | Python |
| Forks | 6,199 |
| Issues | 77 |
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
| Stars | 101,956 |
| 语言 | TypeScript |
| Forks | 12,319 |
| Issues | 990 |
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
| Stars | 59,612 |
| 语言 | JavaScript |
| Forks | 6,442 |
| Issues | 347 |
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
| Stars | 109,045 |
| 语言 | Python |
| Forks | 16,131 |
| Issues | 7 |
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
| Stars | 77,180 |
| 语言 | Python |
| Forks | 10,372 |
| Issues | 205 |
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
| Stars | 52,603 |
| 语言 | TypeScript |
| Forks | 24,278 |
| Issues | 834 |
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
| Stars | 43,829 |
| 语言 | Python |
| Forks | 4,781 |
| Issues | 231 |
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
| Stars | 44,144 |
| 语言 | Go |
| Forks | 3,987 |
| Issues | 1,031 |
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
| Stars | 34,814 |
| 语言 | Python |
| Forks | 4,930 |
| Issues | 230 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (20 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,785 |
| 语言 | Python |
| Forks | 19,334 |
| Issues | 355 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是当前最流行的开源 LLM 界面项目，提供类似 ChatGPT 的现代化体验，同时支持 Ollama、OpenAI API 等多种后端，可完全自托管部署，特别适合注重数据隐私和希望灵活切换大模型服务的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，支持无缝切换
- RAG 检索增强生成：内置文档向量化和语义搜索能力，支持知识库问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展功能和集成外部工具
- 现代化 Web 界面：基于 React 构建的响应式 UI，支持实时流式响应和 Markdown 渲染
- 自托管部署：支持 Docker 一键部署，数据完全本地存储，保障隐私安全

**适用场景**:
- 企业私有化 AI 助手：需要本地部署、数据不出网的场景，部署内部知识库问答系统
- 个人开发者本地开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 获得更好的交互体验
- 多模型统一管理：同时使用多个 LLM 服务，通过统一界面进行管理和对比测试



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,732 |
| 语言 | Python |
| Forks | 20,785 |
| Issues | 8,586 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由 NousResearch 打造的高人气开源 AI Agent 框架（135K+ Stars），支持 Anthropic Claude、OpenAI 等多 LLM 后端统一抽象，其"随你成长"的理念和模块化架构设计让开发者能快速构建和迭代智能代理系统，是当前 AI Agent 领域最具影响力的开源项目之一。

**技术亮点**:
- 多 LLM 后端统一抽象：支持 Anthropic Claude、OpenAI GPT 等主流大模型，通过标准化接口实现无缝切换
- 模块化 Agent 架构：采用可组合组件设计，便于扩展工具链、记忆系统和执行策略
- 丰富的工具生态集成：开箱即用支持代码执行、API 调用、数据库查询，深度集成 Claude Code、OpenClaw 等能力
- 企业级部署友好：MIT 许可证允许商业使用，Python 原生实现便于与现有 ML 基础设施集成
- 活跃的开源社区：135K+ Stars 表明项目维护积极、文档完善、问题响应迅速

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理自动化、数据分析助手等企业级 AI 应用
- 开发者效率工具：集成到 IDE/CLI 实现智能代码补全、Bug 修复、代码审查等开发辅助
- AI 原生应用开发：快速原型验证和构建新一代 AI-first 产品，如个人助手、工作流自动化工具



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 174,595 |
| 语言 | JavaScript |
| Forks | 27,016 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Memory、Security 等机制显著提升开发效率，特别适合希望深度定制和优化 AI 编码体验的开发者。

**技术亮点**:
- 跨平台 AI 代理支持：统一支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具，提供一致的性能优化体验
- MCP (Model Context Protocol) 集成：基于标准化的模型上下文协议，实现与各类 AI 代理的无缝连接和扩展
- Memory 记忆系统：实现持久化上下文记忆，让 AI 代理能够跨会话保持状态和关键信息
- Skills & Instincts 机制：通过预定义的技能和本能模式，提升 AI 代理的响应质量和准确性
- Security First 设计：在 AI 代理系统中内置安全防护机制，确保代码生成和执行的安全性

**适用场景**:
- 企业级 AI 辅助开发：为开发团队提供统一的 AI 编程工具管理和性能优化，提升整体开发效率
- 个人开发者效率提升：定制化配置 AI 代理的行为模式和记忆系统，打造个人专属的开发助手
- AI 研究与实验：作为 research-first 开发框架，用于探索和实验新的 AI 代理优化策略
- 跨工具迁移：帮助开发者在不同 AI 编程工具之间迁移配置和经验，保持工作流的连续性



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,127 |
| 语言 | TypeScript |
| Forks | 15,083 |
| Issues | 758 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的多 Agent 协作平台，拥有超过 76k Stars 的庞大社区支持，集成了 OpenAI、Claude、DeepSeek、Gemini 等主流 AI 模型，支持 MCP 协议和知识库管理，为开发者和企业提供了从 Agent 设计到团队协作的完整解决方案，是构建智能 Agent 应用的优秀起点。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工与配合，突破单一 Agent 的能力边界
- 全模型支持：集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供统一的 API 抽象层
- MCP (Model Context Protocol) 支持：遵循 MCP 协议标准，实现 Agent 与外部工具和服务的标准化连接
- 知识库管理：内置 RAG 能力，支持向量存储和检索，增强 Agent 的领域知识和上下文理解
- TypeScript/React 技术栈：基于现代前端技术构建，提供类型安全的开发和优秀的可维护性

**适用场景**:
- 企业级 Agent 应用开发：构建客服、销售、运营等业务场景的 AI Agent 团队，实现自动化工作流
- AI Agent 研究与实验：利用平台提供的多 Agent 协作框架，探索 Agent 自主决策和协作的新范式
- 个人 AI 助手搭建：集成多种 AI 模型的能力，构建个性化的 AI 工作站，支持知识管理和任务协作



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,884 |
| 语言 | TypeScript |
| Forks | 6,260 |
| Issues | 86 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 嵌入向量技术为 Claude Code 赋予了长期记忆能力，解决了 AI 编程助手的"会话失忆"痛点，让 Claude 能够跨会话理解项目上下文和开发者偏好，大幅提升长期编码效率。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义相似度检索
- 使用 Claude 自身的 agent-sdk 进行 AI 压缩，在本地完成信息提炼
- 混合存储方案：ChromaDB 存储语义嵌入 + SQLite 存储结构化元数据
- 支持向量嵌入生成，自动将代码片段、命令执行结果转为可检索的语义向量
- 作为 Claude Code 原生插件集成，开箱即用的非侵入式架构

**适用场景**:
- 复杂项目的长期开发维护：Claude 能记住项目架构决策、已解决的 bug 和代码规范，跨月甚至跨年保持上下文连贯
- 团队协作场景：同一项目多个开发者可共享 Claude 的项目记忆，避免重复解释背景
- 个性化 AI 编程助手：Claude 学习并记住开发者的编码风格、常用工具和偏好设置



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,707 |
| 语言 | HTML |
| Forks | 21,089 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是 Awesome ChatGPT Prompts 的继任者，拥有超过 16 万 Stars，是目前最受欢迎的 AI 提示词社区项目。其最大亮点是支持完全自托管部署，企业可实现数据完全私有化，同时支持 ChatGPT、Claude、Gemini 等多平台。

**技术亮点**:
- 基于 Next.js + TypeScript 构建高性能 Web 应用
- 支持多平台 LLM（ChatGPT、Claude、Gemini 等）集成
- 开源可自托管，支持企业私有化部署保障数据隐私
- 活跃的开源社区维护，持续更新高质量提示词
- 现代化全栈架构，易于扩展和定制

**适用场景**:
- 个人用户：发现、收藏和分享优质 AI 提示词，提升工作效率
- 企业用户：自托管部署，内部团队共享私有提示词库，保护商业敏感信息
- 开发者：学习提示词工程最佳实践，参考开源实现进行二次开发



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,051 |
| 语言 | Jupyter Notebook |
| Forks | 14,222 |
| Issues | 6 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,235 |
| 语言 | Python |
| Forks | 3,021 |
| Issues | 185 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,370 |
| 语言 | HTML |
| Forks | 5,112 |
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
| Stars | 59,612 |
| 语言 | JavaScript |
| Forks | 6,442 |
| Issues | 347 |
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
| Stars | 72,753 |
| 语言 | Python |
| Forks | 9,215 |
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
| Stars | 56,181 |
| 语言 | TypeScript |
| Forks | 4,575 |
| Issues | 650 |
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
| Stars | 52,603 |
| 语言 | TypeScript |
| Forks | 24,278 |
| Issues | 834 |
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
| Stars | 79,194 |
| 语言 | Python |
| Forks | 16,483 |
| Issues | 4,808 |
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
| Stars | 147,775 |
| 语言 | Python |
| Forks | 8,915 |
| Issues | 931 |
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
| Stars | 58,323 |
| 语言 | Python |
| Forks | 6,308 |
| Issues | 575 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,852 |
| 语言 | Go |
| Forks | 16,014 |
| Issues | 3,200 |
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
| Stars | 58,506 |
| 语言 | TypeScript |
| Forks | 9,600 |
| Issues | 116 |
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
| Stars | 48,493 |
| 语言 | Rust |
| Forks | 9,720 |
| Issues | 0 |
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
| Stars | 121,100 |
| 语言 | Python |
| Forks | 8,113 |
| Issues | 630 |
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
| Stars | 70,975 |
| 语言 | Python |
| Forks | 8,671 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 收录的大模型微调框架，支持 100+ 主流 LLMs 和 VLMs 的统一高效微调，提供 LoRA/QLoRA/RLHF 等多种技术，一站式解决大模型定制化难题，大幅降低微调门槛。

**技术亮点**:
- 支持 100+ 开源大模型（Llama/Qwen/Gemma/DeepSeek/Mistral 等）和视觉语言模型，统一接口设计
- 集成 PEFT 技术生态，支持 LoRA、QLoRA、Prefix Tuning、Ptuning 等多种轻量化微调方法
- 内置 RLHF 完整流程（PPO/DPO/KTO），支持人类反馈强化学习训练
- 支持 4-bit/8-bit 量化训练，结合 Flash Attention 2 和 gradient checkpointing 优化显存
- 提供 WebUI、CLI、Python API 三种使用方式，支持多卡分布式训练和混合精度计算

**适用场景**:
- 企业级 LLM 定制：企业可基于 LlamaFactory 快速将通用大模型微调为领域专用模型（如客服、医疗、金融），结合量化技术实现低成本的本地化部署
- 学术研究与实验：研究人员可便捷对比不同微调方法（LoRA vs PPO vs DPO）在各模型上的效果，加速 NLP 论文实验迭代
- 个人开发者微调：个人开发者无需深入理解底层原理，通过简单配置即可对自己的数据集训练专属 AI 助手



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,105 |
| 语言 | Python |
| Forks | 6,723 |
| Issues | 75 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过 67K Stars 的庞大社区支持，集成了 AI/ML 能力，能够为分析师、量化交易员和 AI 代理提供一站式的金融数据分析解决方案，特别适合需要快速获取多品类金融数据并构建智能投资研究系统的场景。

**技术亮点**:
- 多数据源聚合：整合股票、加密货币、期权、衍生品、固定收益等多品类金融数据，提供统一的数据访问接口
- AI/ML 深度集成：内置机器学习模型和 AI 代理支持，可用于市场预测、情感分析、风险评估等智能分析任务
- 模块化架构设计：采用 Python 模块化架构，支持按需扩展和自定义开发，便于集成到现有 Quant 工作流
- 丰富的可视化能力：内置专业级金融图表和可视化组件，支持技术分析、蜡烛图、K线等常用金融可视化
- 完善的量化工具链：提供回测框架、技术指标计算、因子分析等量化研究必需的工具集

**适用场景**:
- 量化研究与回测：量化交易员可使用该项目快速获取市场数据、进行策略回测和因子分析
- AI 金融应用开发：开发者可基于其 AI 代理框架构建智能投顾、情感分析机器人等 AI 金融产品
- 投资研究与分析：分析师可借助统一的数据平台进行多资产类别的投资研究和市场分析
- 企业级金融数据中台：金融机构可基于开源版本构建自主可控的内部金融数据服务平台



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,707 |
| 语言 | HTML |
| Forks | 21,089 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是 Awesome ChatGPT Prompts 的继任者，拥有超过 16 万 Stars，是目前最受欢迎的 AI 提示词社区项目。其最大亮点是支持完全自托管部署，企业可实现数据完全私有化，同时支持 ChatGPT、Claude、Gemini 等多平台。

**技术亮点**:
- 基于 Next.js + TypeScript 构建高性能 Web 应用
- 支持多平台 LLM（ChatGPT、Claude、Gemini 等）集成
- 开源可自托管，支持企业私有化部署保障数据隐私
- 活跃的开源社区维护，持续更新高质量提示词
- 现代化全栈架构，易于扩展和定制

**适用场景**:
- 个人用户：发现、收藏和分享优质 AI 提示词，提升工作效率
- 企业用户：自托管部署，内部团队共享私有提示词库，保护商业敏感信息
- 开发者：学习提示词工程最佳实践，参考开源实现进行二次开发



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,051 |
| 语言 | Jupyter Notebook |
| Forks | 14,222 |
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
| Stars | 160,309 |
| 语言 | Python |
| Forks | 33,125 |
| Issues | 2,347 |
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
| Stars | 79,194 |
| 语言 | Python |
| Forks | 16,483 |
| Issues | 4,808 |
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
| Stars | 111,641 |
| 语言 | Python |
| Forks | 13,035 |
| Issues | 3,986 |
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
| Stars | 99,692 |
| 语言 | Python |
| Forks | 27,689 |
| Issues | 18,537 |
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
| Stars | 174,595 |
| 语言 | JavaScript |
| Forks | 27,016 |
| Issues | 162 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个全面的 AI 代理性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Memory、Security 等机制显著提升开发效率，特别适合希望深度定制和优化 AI 编码体验的开发者。

**技术亮点**:
- 跨平台 AI 代理支持：统一支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具，提供一致的性能优化体验
- MCP (Model Context Protocol) 集成：基于标准化的模型上下文协议，实现与各类 AI 代理的无缝连接和扩展
- Memory 记忆系统：实现持久化上下文记忆，让 AI 代理能够跨会话保持状态和关键信息
- Skills & Instincts 机制：通过预定义的技能和本能模式，提升 AI 代理的响应质量和准确性
- Security First 设计：在 AI 代理系统中内置安全防护机制，确保代码生成和执行的安全性

**适用场景**:
- 企业级 AI 辅助开发：为开发团队提供统一的 AI 编程工具管理和性能优化，提升整体开发效率
- 个人开发者效率提升：定制化配置 AI 代理的行为模式和记忆系统，打造个人专属的开发助手
- AI 研究与实验：作为 research-first 开发框架，用于探索和实验新的 AI 代理优化策略
- 跨工具迁移：帮助开发者在不同 AI 编程工具之间迁移配置和经验，保持工作流的连续性



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,092 |
| 语言 | Go |
| Forks | 4,061 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源的本地 AI 推理引擎，可在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，大幅降低部署成本并保护数据隐私，46k+ Stars 证明其成熟度和社区活跃度

**技术亮点**:
- 多模态支持：一站式支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测、重新排序等多种 AI 任务
- Go 语言高性能架构：优秀的并发处理能力和跨平台兼容性，部署简单
- 去中心化分布式设计：基于 libp2p 实现分布式部署，适合构建私有化 AI 服务网络
- 零 GPU 依赖：可在 CPU 上运行主流模型，大幅降低硬件投入门槛
- 丰富的协议支持：内置 MCP（Model Context Protocol）支持和标准 REST API，便于系统集成

**适用场景**:
- 企业私有化 AI 部署：数据合规和隐私保护需求的企业可将 AI 能力完全部署在本地
- 开发者快速原型验证：个人开发者或团队低成本快速搭建 AI 应用原型，无需云服务和 GPU 资源
- 边缘计算与离线场景：在边缘设备、无网络环境或低延迟需求场景中提供本地 AI 推理能力



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,089 |
| 语言 | Java |
| Forks | 15,967 |
| Issues | 16 |
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
| Stars | 72,753 |
| 语言 | Python |
| Forks | 9,215 |
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
| Stars | 56,181 |
| 语言 | TypeScript |
| Forks | 4,575 |
| Issues | 650 |
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
| Stars | 186,888 |
| 语言 | TypeScript |
| Forks | 57,405 |
| Issues | 1,442 |
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
| Stars | 58,323 |
| 语言 | Python |
| Forks | 6,308 |
| Issues | 575 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 432,674 |
| 语言 | Python |
| Forks | 47,316 |
| Issues | 1,332 |
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
| Stars | 160,824 |
| 语言 | Python |
| Forks | 13,348 |
| Issues | 2,510 |
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
| Stars | 97,946 |
| 语言 | Python |
| Forks | 9,209 |
| Issues | 187 |
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
| Stars | 82,998 |
| 语言 | Python |
| Forks | 9,681 |
| Issues | 260 |
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
| Stars | 184,616 |
| 语言 | TypeScript |
| Forks | 39,669 |
| Issues | 17,281 |
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
| Stars | 94,259 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 299 |
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
| Stars | 79,120 |
| 语言 | TypeScript |
| Forks | 5,860 |
| Issues | 705 |
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
| Stars | 77,423 |
| 语言 | TypeScript |
| Forks | 6,647 |
| Issues | 151 |
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
| Stars | 80,018 |
| 语言 | Go |
| Forks | 2,802 |
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
| Stars | 77,522 |
| 语言 | Go |
| Forks | 2,814 |
| Issues | 956 |
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
| Stars | 56,181 |
| 语言 | TypeScript |
| Forks | 4,575 |
| Issues | 650 |
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
| Stars | 186,888 |
| 语言 | TypeScript |
| Forks | 57,405 |
| Issues | 1,442 |
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
| Stars | 58,323 |
| 语言 | Python |
| Forks | 6,308 |
| Issues | 575 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,672 |
| 语言 | Go |
| Forks | 10,336 |
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
| Stars | 122,088 |
| 语言 | Go |
| Forks | 42,981 |
| Issues | 2,669 |
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
| Stars | 71,521 |
| 语言 | Go |
| Forks | 18,926 |
| Issues | 3,817 |
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
| Stars | 55,401 |
| 语言 | Go |
| Forks | 6,667 |
| Issues | 2,777 |
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
| Stars | 47,491 |
| 语言 | Go |
| Forks | 5,056 |
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
| Stars | 94,259 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 299 |
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
| Stars | 78,290 |
| 语言 | TypeScript |
| Forks | 6,856 |
| Issues | 381 |
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
| Stars | 86,301 |
| 语言 | JavaScript |
| Forks | 7,790 |
| Issues | 734 |
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
| Stars | 70,180 |
| 语言 | Go |
| Forks | 1,917 |
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
| Stars | 63,016 |
| 语言 | Go |
| Forks | 5,964 |
| Issues | 787 |
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
| Stars | 59,403 |
| 语言 | Go |
| Forks | 4,330 |
| Issues | 28 |
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
| Stars | 60,871 |
| 语言 | Go |
| Forks | 7,474 |
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
| Stars | 86,301 |
| 语言 | JavaScript |
| Forks | 7,790 |
| Issues | 734 |
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
| Stars | 63,928 |
| 语言 | Go |
| Forks | 10,376 |
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
| Stars | 46,092 |
| 语言 | Go |
| Forks | 4,061 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源的本地 AI 推理引擎，可在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，大幅降低部署成本并保护数据隐私，46k+ Stars 证明其成熟度和社区活跃度

**技术亮点**:
- 多模态支持：一站式支持 LLM（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测、重新排序等多种 AI 任务
- Go 语言高性能架构：优秀的并发处理能力和跨平台兼容性，部署简单
- 去中心化分布式设计：基于 libp2p 实现分布式部署，适合构建私有化 AI 服务网络
- 零 GPU 依赖：可在 CPU 上运行主流模型，大幅降低硬件投入门槛
- 丰富的协议支持：内置 MCP（Model Context Protocol）支持和标准 REST API，便于系统集成

**适用场景**:
- 企业私有化 AI 部署：数据合规和隐私保护需求的企业可将 AI 能力完全部署在本地
- 开发者快速原型验证：个人开发者或团队低成本快速搭建 AI 应用原型，无需云服务和 GPU 资源
- 边缘计算与离线场景：在边缘设备、无网络环境或低延迟需求场景中提供本地 AI 推理能力



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 432,674 |
| 语言 | Python |
| Forks | 47,316 |
| Issues | 1,332 |
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
| Stars | 97,946 |
| 语言 | Python |
| Forks | 9,209 |
| Issues | 187 |
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
| Stars | 87,421 |
| 语言 | Python |
| Forks | 33,845 |
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
| Stars | 100,060 |
| 语言 | TypeScript |
| Forks | 27,199 |
| Issues | 1,150 |
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
| Stars | 79,120 |
| 语言 | TypeScript |
| Forks | 5,860 |
| Issues | 705 |
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
| Stars | 68,993 |
| 语言 | JavaScript |
| Forks | 23,251 |
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
| Stars | 55,948 |
| 语言 | JavaScript |
| Forks | 10,202 |
| Issues | 369 |
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
| Stars | 51,847 |
| 语言 | JavaScript |
| Forks | 4,715 |
| Issues | 1,475 |
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
| Stars | 72,131 |
| 语言 | Go |
| Forks | 4,714 |
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
| Stars | 58,166 |
| 语言 | Go |
| Forks | 3,353 |
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
| Stars | 88,430 |
| 语言 | Go |
| Forks | 8,596 |
| Issues | 683 |
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
| Stars | 101,956 |
| 语言 | TypeScript |
| Forks | 12,319 |
| Issues | 990 |
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
| Stars | 59,612 |
| 语言 | JavaScript |
| Forks | 6,442 |
| Issues | 347 |
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
| Stars | 44,144 |
| 语言 | Go |
| Forks | 3,987 |
| Issues | 1,031 |
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
| Stars | 51,672 |
| 语言 | Go |
| Forks | 10,336 |
| Issues | 242 |
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
| Stars | 161,707 |
| 语言 | HTML |
| Forks | 21,089 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是 Awesome ChatGPT Prompts 的继任者，拥有超过 16 万 Stars，是目前最受欢迎的 AI 提示词社区项目。其最大亮点是支持完全自托管部署，企业可实现数据完全私有化，同时支持 ChatGPT、Claude、Gemini 等多平台。

**技术亮点**:
- 基于 Next.js + TypeScript 构建高性能 Web 应用
- 支持多平台 LLM（ChatGPT、Claude、Gemini 等）集成
- 开源可自托管，支持企业私有化部署保障数据隐私
- 活跃的开源社区维护，持续更新高质量提示词
- 现代化全栈架构，易于扩展和定制

**适用场景**:
- 个人用户：发现、收藏和分享优质 AI 提示词，提升工作效率
- 企业用户：自托管部署，内部团队共享私有提示词库，保护商业敏感信息
- 开发者：学习提示词工程最佳实践，参考开源实现进行二次开发



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,235 |
| 语言 | Python |
| Forks | 3,021 |
| Issues | 185 |
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
| Stars | 42,968 |
| 语言 | Python |
| Forks | 5,206 |
| Issues | 106 |
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
| Stars | 58,506 |
| 语言 | TypeScript |
| Forks | 9,600 |
| Issues | 116 |
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
| Stars | 89,858 |
| 语言 | TypeScript |
| Forks | 10,040 |
| Issues | 2,266 |
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
| Stars | 87,844 |
| 语言 | TypeScript |
| Forks | 8,944 |
| Issues | 1,666 |
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
| Stars | 171,977 |
| 语言 | Go |
| Forks | 13,192 |
| Issues | 180 |
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
| Stars | 127,716 |
| 语言 | JavaScript |
| Forks | 12,483 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (66 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,818 |
| 语言 | Unknown |
| Forks | 34,148 |
| Issues | 138 |
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
| Stars | 62,802 |
| 语言 | Shell |
| Forks | 5,429 |
| Issues | 20 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,896 |
| 语言 | Python |
| Forks | 8,051 |
| Issues | 493 |
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
| Stars | 92,686 |
| 语言 | Python |
| Forks | 13,477 |
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
| Stars | 387,809 |
| 语言 | Python |
| Forks | 66,239 |
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
| Stars | 116,118 |
| 语言 | TypeScript |
| Forks | 8,475 |
| Issues | 310 |
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
| Stars | 115,972 |
| 语言 | TypeScript |
| Forks | 6,094 |
| Issues | 27 |
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
| Stars | 90,405 |
| 语言 | TypeScript |
| Forks | 13,348 |
| Issues | 524 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,459 |
| 语言 | JavaScript |
| Forks | 5,140 |
| Issues | 42 |
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
| Stars | 48,337 |
| 语言 | Go |
| Forks | 10,340 |
| Issues | 1,894 |
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
| Stars | 108,659 |
| 语言 | C++ |
| Forks | 17,843 |
| Issues | 1,598 |
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
| Stars | 63,339 |
| 语言 | Python |
| Forks | 1,636 |
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
| Stars | 36,368 |
| 语言 | TypeScript |
| Forks | 4,139 |
| Issues | 383 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 296,233 |
| 语言 | Python |
| Forks | 27,830 |
| Issues | 20 |
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
| Stars | 220,810 |
| 语言 | Python |
| Forks | 50,550 |
| Issues | 954 |
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
| Stars | 86,939 |
| 语言 | Python |
| Forks | 37,423 |
| Issues | 3,832 |
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
| Forks | 45,102 |
| Issues | 1,286 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,258 |
| 语言 | TypeScript |
| Forks | 44,479 |
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
| Stars | 354,313 |
| 语言 | TypeScript |
| Forks | 44,039 |
| Issues | 3 |
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
| Stars | 122,626 |
| 语言 | TypeScript |
| Forks | 13,547 |
| Issues | 3,031 |
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
| Stars | 113,667 |
| 语言 | TypeScript |
| Forks | 8,739 |
| Issues | 1,848 |
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
| Stars | 108,766 |
| 语言 | TypeScript |
| Forks | 13,385 |
| Issues | 5,031 |
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
| Stars | 99,829 |
| 语言 | TypeScript |
| Forks | 5,541 |
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
| Stars | 97,930 |
| 语言 | TypeScript |
| Forks | 54,601 |
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
| Stars | 94,854 |
| 语言 | TypeScript |
| Forks | 5,219 |
| Issues | 89 |
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
| Stars | 83,383 |
| 语言 | TypeScript |
| Forks | 7,610 |
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
| Stars | 80,421 |
| 语言 | TypeScript |
| Forks | 8,135 |
| Issues | 754 |
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
| Stars | 244,834 |
| 语言 | JavaScript |
| Forks | 51,004 |
| Issues | 1,279 |
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
| Stars | 117,058 |
| 语言 | JavaScript |
| Forks | 35,492 |
| Issues | 2,658 |
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
| Stars | 112,340 |
| 语言 | JavaScript |
| Forks | 36,363 |
| Issues | 502 |
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
| Stars | 109,027 |
| 语言 | JavaScript |
| Forks | 11,671 |
| Issues | 151 |
| Topics | hacktoberfest, http-client, javascript, nodejs, promise |
| 许可证 | MIT License |


### Anduin2017/HowToCook

**描述**: 程序员在家做饭方法指南。Programmer's guide about how to cook at home (Simplified Chinese only).

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,778 |
| 语言 | JavaScript |
| Forks | 10,930 |
| Issues | 474 |
| Topics | chinese, cookbook, cooking, dishes, recipes |
| 许可证 | The Unlicense |


### mui/material-ui

**描述**: Material UI: Comprehensive React component library that implements Google's Material Design. Free forever.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,285 |
| 语言 | JavaScript |
| Forks | 32,649 |
| Issues | 1,540 |
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
| Stars | 86,483 |
| 语言 | JavaScript |
| Forks | 4,903 |
| Issues | 998 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,851 |
| 语言 | JavaScript |
| Forks | 4,556 |
| Issues | 101 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,759 |
| 语言 | JavaScript |
| Forks | 9,356 |
| Issues | 197 |
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
| Stars | 64,442 |
| 语言 | JavaScript |
| Forks | 4,093 |
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
| Stars | 60,904 |
| 语言 | JavaScript |
| Forks | 5,661 |
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
| Stars | 59,838 |
| 语言 | JavaScript |
| Forks | 20,453 |
| Issues | 92 |
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
| Stars | 53,263 |
| 语言 | JavaScript |
| Forks | 10,608 |
| Issues | 446 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,742 |
| 语言 | JavaScript |
| Forks | 11,529 |
| Issues | 243 |
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
| Stars | 133,757 |
| 语言 | Go |
| Forks | 18,975 |
| Issues | 10,100 |
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
| Stars | 106,277 |
| 语言 | Go |
| Forks | 15,029 |
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
| Stars | 87,935 |
| 语言 | Go |
| Forks | 8,253 |
| Issues | 241 |
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
| Stars | 83,623 |
| 语言 | Go |
| Forks | 5,156 |
| Issues | 386 |
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
| Stars | 68,582 |
| 语言 | Go |
| Forks | 3,228 |
| Issues | 12 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,038 |
| 语言 | Go |
| Forks | 5,075 |
| Issues | 1,163 |
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
| Stars | 51,020 |
| 语言 | Go |
| Forks | 21,898 |
| Issues | 403 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 94,317 |
| 语言 | Shell |
| Forks | 15,521 |
| Issues | 123 |
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
| Stars | 116,292 |
| 语言 | Unknown |
| Forks | 11,661 |
| Issues | 87 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,007 |
| 语言 | Python |
| Forks | 12,149 |
| Issues | 122 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,619 |
| 语言 | Python |
| Forks | 7,262 |
| Issues | 488 |
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
| Stars | 77,510 |
| 语言 | Python |
| Forks | 16,930 |
| Issues | 28 |
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
| Stars | 85,152 |
| 语言 | TypeScript |
| Forks | 10,609 |
| Issues | 419 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,113 |
| 语言 | JavaScript |
| Forks | 26,693 |
| Issues | 159 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 95,715 |
| 语言 | JavaScript |
| Forks | 15,463 |
| Issues | 53 |
| Topics | css, curriculum, education, html, javascript, learning, microsoft-for-beginners, tutorials |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,136 |
| 语言 | JavaScript |
| Forks | 16,796 |
| Issues | 897 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,392 |
| 语言 | JavaScript |
| Forks | 11,955 |
| Issues | 560 |
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
| Stars | 66,369 |
| 语言 | JavaScript |
| Forks | 9,185 |
| Issues | 3 |
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
| Stars | 61,220 |
| 语言 | JavaScript |
| Forks | 7,155 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,436 |
| 语言 | JavaScript |
| Forks | 12,306 |
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
| Stars | 50,932 |
| 语言 | Go |
| Forks | 1,609 |
| Issues | 274 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,434 |
| 语言 | Go |
| Forks | 7,946 |
| Issues | 569 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,846 |
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
| Stars | 46,235 |
| 语言 | Go |
| Forks | 3,815 |
| Issues | 82 |
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
| Stars | 155,082 |
| 语言 | Python |
| Forks | 11,828 |
| Issues | 354 |
| Topics | awesome, github, hellogithub, python |
