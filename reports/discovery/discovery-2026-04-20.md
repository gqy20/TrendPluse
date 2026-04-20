# 项目发现报告 (2026-04-20)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 34 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 23 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 16 |
| ⚙️ DevOps/基础设施 | 12 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 63 |

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
| Stars | 132,838 |
| 语言 | Python |
| Forks | 18,858 |
| Issues | 227 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的 LLM Web 界面开源项目（星标 132,838），提供了开箱即用的 AI 交互界面，支持 Ollama、OpenAI API 等多种后端，让用户能够快速在本地搭建私有化的 AI 助手平台，同时内置 RAG 检索增强生成能力，真正实现了零门槛的 AI 界面部署体验。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，用户可以在同一界面中灵活切换不同的 LLM 提供商
- 内置 RAG 能力：集成检索增强生成功能，支持文档向量化处理，提升 AI 回答的准确性和上下文相关性
- 自托管部署方案：支持完全私有化部署，数据无需上传云端，满足企业级数据安全和隐私合规要求
- 现代化 Web 界面：提供响应式设计的用户界面，支持实时对话、对话历史管理、多用户协作等功能
- 开放协议集成：支持 MCP (Model Control Protocol) 和 OpenAPI 标准，便于与现有系统集成和功能扩展

**适用场景**:
- 企业私有 AI 平台：适合对数据隐私有高要求的企业部署内部 AI 助手，所有交互数据完全保留在本地网络内
- 个人开发者/AI 爱好者：希望快速在本地运行开源大语言模型（如 Llama、Qwen 等），通过友好界面进行交互和测试
- 多模型统一管理：需要同时使用多个 LLM 服务（本地+云端）的开发团队，可通过统一界面管理不同模型



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,055 |
| 语言 | Python |
| Forks | 15,001 |
| Issues | 5,787 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源 AI 研究组织 NousResearch 开发的高星 AI Agent 框架，拥有超过 10 万 Stars 的社区认可，支持 Claude、ChatGPT 等多主流 LLM 提供商，可扩展性强，适合构建企业级智能代理应用。

**技术亮点**:
- 多 LLM 提供商支持：原生集成 Anthropic Claude、OpenAI GPT 等主流大语言模型
- MIT 开源许可证：代码完全开放，可自由商用和二次开发
- 模块化 Agent 架构：支持工具调用、任务规划、多步骤推理等复杂能力
- 活跃的社区生态：依托 NousResearch 组织，拥有丰富的预训练模型和工具链支持
- Python 优先实现：便于与现有 Python 项目和 ML 生态集成

**适用场景**:
- 构建企业级 AI 助手：开发内部客服、数据分析、文档处理等自动化代理
- 代码智能助手开发：基于 Claude Code 能力构建代码审查、bug 修复等开发工具
- 个人效率工具：创建日程管理、信息检索、任务自动化等个人助理应用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,590 |
| 语言 | Python |
| Forks | 8,875 |
| Issues | 2,983 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 解决方案之一，将深度文档理解、多跳推理 Agent 与 GraphRAG 能力完美融合，为企业级知识问答和深度研究场景提供端到端的完整管道，尤其适合需要处理复杂 PDF、Word 等结构化文档的团队。

**技术亮点**:
- **深度文档理解引擎**：支持复杂 PDF、Word、Excel 等多格式文档的智能解析与结构化提取，自动识别标题、表格、图表等元素，显著提升检索质量
- **融合式检索架构**：结合向量检索、关键词搜索与 GraphRAG 知识图谱能力，支持多跳推理和语义关联发现，有效解决复杂问答场景
- **Agent 驱动的多步推理**：内置 Agent 工作流引擎，支持 Chain-of-Thought、Tool Use 等高级推理模式，可处理需要多步检索和验证的深度研究任务
- **多 LLM 灵活接入**：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并集成 MCP 协议实现标准化工具扩展
- **可视化配置与监控**：提供 Web UI 进行知识库管理、检索策略调优和 Agent 流程编排，降低企业级部署和运维门槛

**适用场景**:
- **企业级知识库问答**：构建内部知识库智能问答系统，支持复杂文档（如财报、技术文档、法律合同）的深度理解和精准回答
- **深度研究与分析助手**：基于 GraphRAG 和 Agent 能力，实现多源文档的综合分析、关联推理和结构化报告生成
- **智能客服与文档助手**：为产品文档、API 文档等提供语义级检索和上下文增强的对话服务，提升用户自助服务效率



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,035 |
| 语言 | JavaScript |
| Forks | 25,185 |
| Issues | 132 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，162K+ Stars 证明了其在 AI 辅助开发领域的广泛认可。

**技术亮点**:
- 多 AI 编码工具统一框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化体验
- 模块化 AI Agent 架构：包含 Skills（技能）、Instincts（本能）、Memory（记忆）等核心组件，实现复杂任务分解与执行
- Memory 记忆系统：持久化上下文和会话状态，解决长对话场景下的上下文丢失问题
- Security 安全模块：内置代码安全审查和敏感信息保护机制，确保 AI 生成代码的安全性
- MCP (Model Context Protocol) 深度集成：标准化模型上下文交互协议，提升 AI 理解代码的能力

**适用场景**:
- 企业级 AI 开发助手集成：团队可将框架部署到内部开发环境，统一管理 AI 编码规范和安全策略
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 助手能力，实现自动化代码重构和测试生成
- AI Agent 应用开发：基于框架构建定制化的 AI 编程助手，支持特定领域知识的注入



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,623 |
| 语言 | Go |
| Forks | 3,977 |
| Issues | 171 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的开源本地 AI 部署方案，支持 LLM、图像、语音、视频等多种模型，无需 GPU 即可运行，特别适合隐私敏感或需要完全控制 AI 能力的场景，在 GitHub 上获得 45k+ Stars 证明其社区认可度极高。

**技术亮点**:
- 多模型支持：支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 无需 GPU 即可运行：支持 CPU 推理，大幅降低部署门槛，可在普通硬件上运行 AI 模型
- Go 语言开发：高性能、高并发，原生支持分布式部署和 libp2p 去中心化网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- 丰富的模型支持：支持 Mamba 架构、ReRank 模型、多模态模型等前沿技术，涵盖 text-generation、image-generation、audio-generation 等全场景

**适用场景**:
- 隐私敏感的本地 AI 部署：企业或个人不想将数据发送到第三方服务，需要完全控制的数据处理场景
- 资源受限环境：在没有 GPU 的服务器、开发机或边缘设备上运行 AI 推理任务
- 快速集成 AI 能力的应用开发：通过 OpenAI 兼容的 API 为现有应用快速添加 AI 功能，支持文本生成、图像生成、语音合成等多种能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,399 |
| 语言 | TypeScript |
| Forks | 14,947 |
| Issues | 699 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的 AI Agent 平台，支持多 Agent 协作和团队设计，整合了 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，拥有 75k+ Stars 的活跃社区，是构建和部署智能代理应用的优秀选择。

**技术亮点**:
- 基于 TypeScript/React 的现代化全栈架构，提供流畅的 Type-Safe 开发体验
- Multi-Agent 协作框架支持多个 Agent 协同工作，实现复杂任务的分工处理
- 支持 MCP (Model Context Protocol) 协议，便于扩展和集成第三方工具
- 多模型统一接入能力，同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型 API
- 内置知识库系统，支持 RAG 增强检索和向量存储能力

**适用场景**:
- 企业级 AI 工作流自动化：构建多 Agent 协作团队处理复杂业务流程，如客服、销售、数据分析等场景
- 个人开发者快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 Demo
- 团队知识管理和协作平台：通过知识库功能构建企业专属的 AI 助手，支持文档检索和智能问答



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,375 |
| 语言 | Python |
| Forks | 8,606 |
| Issues | 978 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个支持 100+ 大模型统一微调的工业级框架，提供了从数据处理到模型部署的完整闭环，相比 Colab 方案能节省 80% 以上微调成本，且在 ACL 2024 获得顶会认可，是企业落地 LLM 和 VLM 的首选工具。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 Llama3、Qwen、DeepSeek、Gemma 等主流模型家族
- 集成 LoRA、QLoRA、Peft 等参数高效微调技术，显存占用降低 60-80%，单卡即可训练 7B 模型
- 支持 RLHF（DPO/PPO）、SFT、Supervisor Tuning 等多种训练范式，覆盖从基础微调到强化学习对齐全链路
- 内置 4-bit/8-bit 量化、Flash Attention、Gradient Checkpoint 等优化，支持 MoE 架构高效训练
- 提供 Web UI 和 CLI 双入口，支持分布式多节点训练，适配 DeepSpeed、 Accelerate 等主流训练框架

**适用场景**:
- 企业定制化场景：金融机构和医疗企业可基于 LlamaFactory 快速微调领域专属模型，满足数据安全和合规要求
- 学术研究场景：研究人员可便捷对比不同微调方法（LoRA vs QLoRA vs RLHF）在各类任务上的效果差异
- 多模态应用场景：支持视觉语言模型微调，适合构建垂类图文理解和生成系统，如文档分析、图表理解等业务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,181 |
| 语言 | TypeScript |
| Forks | 5,391 |
| Issues | 122 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现智能记忆注入，能显著提升 AI 助手的个性化程度和任务连续性，特别适合需要长时间迭代开发或处理复杂项目的开发者。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义级别的上下文检索
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，智能提取关键信息并过滤噪音
- 集成 SQLite 本地存储，数据完全可控且易于迁移
- 支持 embeddings 向量化表示，实现跨会话的语义关联记忆
- 作为 Claude Code 原生插件，无缝集成到现有开发工作流中

**适用场景**:
- 长时间复杂项目开发：维护跨会话的项目上下文，避免每次从头解释项目结构和需求
- 个人知识管理：自动记录代码决策过程和设计思路，构建个人编程知识库
- 团队知识共享（进阶）：基于记忆库实现代码片段、设计模式的智能推荐和复用



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,124 |
| 语言 | TypeScript |
| Forks | 9,076 |
| Issues | 101 |
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
| Stars | 46,880 |
| 语言 | HTML |
| Forks | 4,606 |
| Issues | 10 |
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
| Stars | 43,554 |
| 语言 | Python |
| Forks | 9,961 |
| Issues | 352 |
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
| Stars | 45,896 |
| 语言 | Java |
| Forks | 15,923 |
| Issues | 12 |
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
| Stars | 39,020 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
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
| Stars | 38,907 |
| 语言 | Python |
| Forks | 4,627 |
| Issues | 93 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 111,093 |
| 语言 | TypeScript |
| Forks | 7,091 |
| Issues | 282 |
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
| Stars | 58,659 |
| 语言 | JavaScript |
| Forks | 6,344 |
| Issues | 338 |
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
| Stars | 71,573 |
| 语言 | Python |
| Forks | 9,010 |
| Issues | 418 |
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
| Stars | 53,014 |
| 语言 | TypeScript |
| Forks | 4,274 |
| Issues | 579 |
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
| Stars | 106,599 |
| 语言 | Python |
| Forks | 15,648 |
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
| Stars | 88,907 |
| 语言 | Python |
| Forks | 10,176 |
| Issues | 216 |
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
| Stars | 52,091 |
| 语言 | TypeScript |
| Forks | 24,175 |
| Issues | 813 |
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
| Stars | 184,872 |
| 语言 | TypeScript |
| Forks | 56,982 |
| Issues | 1,550 |
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
| Stars | 155,090 |
| 语言 | Java |
| Forks | 46,143 |
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
| Stars | 147,162 |
| 语言 | Python |
| Forks | 8,807 |
| Issues | 947 |
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
| Stars | 57,084 |
| 语言 | Jupyter Notebook |
| Forks | 19,793 |
| Issues | 5 |
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
| Stars | 34,168 |
| 语言 | Python |
| Forks | 2,156 |
| Issues | 97 |
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
| Stars | 33,870 |
| 语言 | TypeScript |
| Forks | 3,671 |
| Issues | 291 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,849 |
| 语言 | Jupyter Notebook |
| Forks | 5,601 |
| Issues | 126 |
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
| Stars | 47,811 |
| 语言 | Rust |
| Forks | 3,057 |
| Issues | 550 |
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
| Stars | 132,838 |
| 语言 | Python |
| Forks | 18,858 |
| Issues | 227 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的 LLM Web 界面开源项目（星标 132,838），提供了开箱即用的 AI 交互界面，支持 Ollama、OpenAI API 等多种后端，让用户能够快速在本地搭建私有化的 AI 助手平台，同时内置 RAG 检索增强生成能力，真正实现了零门槛的 AI 界面部署体验。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，用户可以在同一界面中灵活切换不同的 LLM 提供商
- 内置 RAG 能力：集成检索增强生成功能，支持文档向量化处理，提升 AI 回答的准确性和上下文相关性
- 自托管部署方案：支持完全私有化部署，数据无需上传云端，满足企业级数据安全和隐私合规要求
- 现代化 Web 界面：提供响应式设计的用户界面，支持实时对话、对话历史管理、多用户协作等功能
- 开放协议集成：支持 MCP (Model Control Protocol) 和 OpenAPI 标准，便于与现有系统集成和功能扩展

**适用场景**:
- 企业私有 AI 平台：适合对数据隐私有高要求的企业部署内部 AI 助手，所有交互数据完全保留在本地网络内
- 个人开发者/AI 爱好者：希望快速在本地运行开源大语言模型（如 Llama、Qwen 等），通过友好界面进行交互和测试
- 多模型统一管理：需要同时使用多个 LLM 服务（本地+云端）的开发团队，可通过统一界面管理不同模型



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,590 |
| 语言 | Python |
| Forks | 8,875 |
| Issues | 2,983 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 解决方案之一，将深度文档理解、多跳推理 Agent 与 GraphRAG 能力完美融合，为企业级知识问答和深度研究场景提供端到端的完整管道，尤其适合需要处理复杂 PDF、Word 等结构化文档的团队。

**技术亮点**:
- **深度文档理解引擎**：支持复杂 PDF、Word、Excel 等多格式文档的智能解析与结构化提取，自动识别标题、表格、图表等元素，显著提升检索质量
- **融合式检索架构**：结合向量检索、关键词搜索与 GraphRAG 知识图谱能力，支持多跳推理和语义关联发现，有效解决复杂问答场景
- **Agent 驱动的多步推理**：内置 Agent 工作流引擎，支持 Chain-of-Thought、Tool Use 等高级推理模式，可处理需要多步检索和验证的深度研究任务
- **多 LLM 灵活接入**：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并集成 MCP 协议实现标准化工具扩展
- **可视化配置与监控**：提供 Web UI 进行知识库管理、检索策略调优和 Agent 流程编排，降低企业级部署和运维门槛

**适用场景**:
- **企业级知识库问答**：构建内部知识库智能问答系统，支持复杂文档（如财报、技术文档、法律合同）的深度理解和精准回答
- **深度研究与分析助手**：基于 GraphRAG 和 Agent 能力，实现多源文档的综合分析、关联推理和结构化报告生成
- **智能客服与文档助手**：为产品文档、API 文档等提供语义级检索和上下文增强的对话服务，提升用户自助服务效率



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,399 |
| 语言 | TypeScript |
| Forks | 14,947 |
| Issues | 699 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的 AI Agent 平台，支持多 Agent 协作和团队设计，整合了 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，拥有 75k+ Stars 的活跃社区，是构建和部署智能代理应用的优秀选择。

**技术亮点**:
- 基于 TypeScript/React 的现代化全栈架构，提供流畅的 Type-Safe 开发体验
- Multi-Agent 协作框架支持多个 Agent 协同工作，实现复杂任务的分工处理
- 支持 MCP (Model Context Protocol) 协议，便于扩展和集成第三方工具
- 多模型统一接入能力，同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型 API
- 内置知识库系统，支持 RAG 增强检索和向量存储能力

**适用场景**:
- 企业级 AI 工作流自动化：构建多 Agent 协作团队处理复杂业务流程，如客服、销售、数据分析等场景
- 个人开发者快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 Demo
- 团队知识管理和协作平台：通过知识库功能构建企业专属的 AI 助手，支持文档检索和智能问答



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,181 |
| 语言 | TypeScript |
| Forks | 5,391 |
| Issues | 122 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现智能记忆注入，能显著提升 AI 助手的个性化程度和任务连续性，特别适合需要长时间迭代开发或处理复杂项目的开发者。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义级别的上下文检索
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，智能提取关键信息并过滤噪音
- 集成 SQLite 本地存储，数据完全可控且易于迁移
- 支持 embeddings 向量化表示，实现跨会话的语义关联记忆
- 作为 Claude Code 原生插件，无缝集成到现有开发工作流中

**适用场景**:
- 长时间复杂项目开发：维护跨会话的项目上下文，避免每次从头解释项目结构和需求
- 个人知识管理：自动记录代码决策过程和设计思路，构建个人编程知识库
- 团队知识共享（进阶）：基于记忆库实现代码片段、设计模式的智能推荐和复用



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,896 |
| 语言 | Java |
| Forks | 15,923 |
| Issues | 12 |
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
| Stars | 39,020 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
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
| Stars | 38,907 |
| 语言 | Python |
| Forks | 4,627 |
| Issues | 93 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,169 |
| 语言 | TypeScript |
| Forks | 12,140 |
| Issues | 963 |
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
| Stars | 58,659 |
| 语言 | JavaScript |
| Forks | 6,344 |
| Issues | 338 |
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
| Stars | 106,599 |
| 语言 | Python |
| Forks | 15,648 |
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
| Stars | 76,013 |
| 语言 | Python |
| Forks | 10,263 |
| Issues | 228 |
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
| Stars | 52,091 |
| 语言 | TypeScript |
| Forks | 24,175 |
| Issues | 813 |
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
| Stars | 43,880 |
| 语言 | Go |
| Forks | 3,967 |
| Issues | 1,132 |
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
| Stars | 33,911 |
| 语言 | Python |
| Forks | 4,809 |
| Issues | 210 |
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
| Stars | 34,168 |
| 语言 | Python |
| Forks | 2,156 |
| Issues | 97 |
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
| Stars | 33,870 |
| 语言 | TypeScript |
| Forks | 3,671 |
| Issues | 291 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,849 |
| 语言 | Jupyter Notebook |
| Forks | 5,601 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (23 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,838 |
| 语言 | Python |
| Forks | 18,858 |
| Issues | 227 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的 LLM Web 界面开源项目（星标 132,838），提供了开箱即用的 AI 交互界面，支持 Ollama、OpenAI API 等多种后端，让用户能够快速在本地搭建私有化的 AI 助手平台，同时内置 RAG 检索增强生成能力，真正实现了零门槛的 AI 界面部署体验。

**技术亮点**:
- 多后端兼容架构：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，用户可以在同一界面中灵活切换不同的 LLM 提供商
- 内置 RAG 能力：集成检索增强生成功能，支持文档向量化处理，提升 AI 回答的准确性和上下文相关性
- 自托管部署方案：支持完全私有化部署，数据无需上传云端，满足企业级数据安全和隐私合规要求
- 现代化 Web 界面：提供响应式设计的用户界面，支持实时对话、对话历史管理、多用户协作等功能
- 开放协议集成：支持 MCP (Model Control Protocol) 和 OpenAPI 标准，便于与现有系统集成和功能扩展

**适用场景**:
- 企业私有 AI 平台：适合对数据隐私有高要求的企业部署内部 AI 助手，所有交互数据完全保留在本地网络内
- 个人开发者/AI 爱好者：希望快速在本地运行开源大语言模型（如 Llama、Qwen 等），通过友好界面进行交互和测试
- 多模型统一管理：需要同时使用多个 LLM 服务（本地+云端）的开发团队，可通过统一界面管理不同模型



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,055 |
| 语言 | Python |
| Forks | 15,001 |
| Issues | 5,787 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源 AI 研究组织 NousResearch 开发的高星 AI Agent 框架，拥有超过 10 万 Stars 的社区认可，支持 Claude、ChatGPT 等多主流 LLM 提供商，可扩展性强，适合构建企业级智能代理应用。

**技术亮点**:
- 多 LLM 提供商支持：原生集成 Anthropic Claude、OpenAI GPT 等主流大语言模型
- MIT 开源许可证：代码完全开放，可自由商用和二次开发
- 模块化 Agent 架构：支持工具调用、任务规划、多步骤推理等复杂能力
- 活跃的社区生态：依托 NousResearch 组织，拥有丰富的预训练模型和工具链支持
- Python 优先实现：便于与现有 Python 项目和 ML 生态集成

**适用场景**:
- 构建企业级 AI 助手：开发内部客服、数据分析、文档处理等自动化代理
- 代码智能助手开发：基于 Claude Code 能力构建代码审查、bug 修复等开发工具
- 个人效率工具：创建日程管理、信息检索、任务自动化等个人助理应用



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,590 |
| 语言 | Python |
| Forks | 8,875 |
| Issues | 2,983 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 解决方案之一，将深度文档理解、多跳推理 Agent 与 GraphRAG 能力完美融合，为企业级知识问答和深度研究场景提供端到端的完整管道，尤其适合需要处理复杂 PDF、Word 等结构化文档的团队。

**技术亮点**:
- **深度文档理解引擎**：支持复杂 PDF、Word、Excel 等多格式文档的智能解析与结构化提取，自动识别标题、表格、图表等元素，显著提升检索质量
- **融合式检索架构**：结合向量检索、关键词搜索与 GraphRAG 知识图谱能力，支持多跳推理和语义关联发现，有效解决复杂问答场景
- **Agent 驱动的多步推理**：内置 Agent 工作流引擎，支持 Chain-of-Thought、Tool Use 等高级推理模式，可处理需要多步检索和验证的深度研究任务
- **多 LLM 灵活接入**：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并集成 MCP 协议实现标准化工具扩展
- **可视化配置与监控**：提供 Web UI 进行知识库管理、检索策略调优和 Agent 流程编排，降低企业级部署和运维门槛

**适用场景**:
- **企业级知识库问答**：构建内部知识库智能问答系统，支持复杂文档（如财报、技术文档、法律合同）的深度理解和精准回答
- **深度研究与分析助手**：基于 GraphRAG 和 Agent 能力，实现多源文档的综合分析、关联推理和结构化报告生成
- **智能客服与文档助手**：为产品文档、API 文档等提供语义级检索和上下文增强的对话服务，提升用户自助服务效率



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,035 |
| 语言 | JavaScript |
| Forks | 25,185 |
| Issues | 132 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，162K+ Stars 证明了其在 AI 辅助开发领域的广泛认可。

**技术亮点**:
- 多 AI 编码工具统一框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化体验
- 模块化 AI Agent 架构：包含 Skills（技能）、Instincts（本能）、Memory（记忆）等核心组件，实现复杂任务分解与执行
- Memory 记忆系统：持久化上下文和会话状态，解决长对话场景下的上下文丢失问题
- Security 安全模块：内置代码安全审查和敏感信息保护机制，确保 AI 生成代码的安全性
- MCP (Model Context Protocol) 深度集成：标准化模型上下文交互协议，提升 AI 理解代码的能力

**适用场景**:
- 企业级 AI 开发助手集成：团队可将框架部署到内部开发环境，统一管理 AI 编码规范和安全策略
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 助手能力，实现自动化代码重构和测试生成
- AI Agent 应用开发：基于框架构建定制化的 AI 编程助手，支持特定领域知识的注入



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,399 |
| 语言 | TypeScript |
| Forks | 14,947 |
| Issues | 699 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完善的 AI Agent 平台，支持多 Agent 协作和团队设计，整合了 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，拥有 75k+ Stars 的活跃社区，是构建和部署智能代理应用的优秀选择。

**技术亮点**:
- 基于 TypeScript/React 的现代化全栈架构，提供流畅的 Type-Safe 开发体验
- Multi-Agent 协作框架支持多个 Agent 协同工作，实现复杂任务的分工处理
- 支持 MCP (Model Context Protocol) 协议，便于扩展和集成第三方工具
- 多模型统一接入能力，同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型 API
- 内置知识库系统，支持 RAG 增强检索和向量存储能力

**适用场景**:
- 企业级 AI 工作流自动化：构建多 Agent 协作团队处理复杂业务流程，如客服、销售、数据分析等场景
- 个人开发者快速原型开发：利用现成的 Agent 框架和 UI 组件快速搭建 AI 应用 Demo
- 团队知识管理和协作平台：通过知识库功能构建企业专属的 AI 助手，支持文档检索和智能问答



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,181 |
| 语言 | TypeScript |
| Forks | 5,391 |
| Issues | 122 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现智能记忆注入，能显著提升 AI 助手的个性化程度和任务连续性，特别适合需要长时间迭代开发或处理复杂项目的开发者。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义级别的上下文检索
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，智能提取关键信息并过滤噪音
- 集成 SQLite 本地存储，数据完全可控且易于迁移
- 支持 embeddings 向量化表示，实现跨会话的语义关联记忆
- 作为 Claude Code 原生插件，无缝集成到现有开发工作流中

**适用场景**:
- 长时间复杂项目开发：维护跨会话的项目上下文，避免每次从头解释项目结构和需求
- 个人知识管理：自动记录代码决策过程和设计思路，构建个人编程知识库
- 团队知识共享（进阶）：基于记忆库实现代码片段、设计模式的智能推荐和复用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,206 |
| 语言 | HTML |
| Forks | 20,963 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万星标和 5000+ 精选提示词，支持多种主流 AI 模型，企业可自托管实现数据完全私有化，是个人和团队提升 AI 效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的响应式 Web 应用架构
- 支持 ChatGPT、Claude、Gemini、GPT-4 等多种主流 LLM 模型
- 开源可自托管， 企业可部署私有版本保障数据隐私
- 社区驱动的提示词贡献机制，持续更新高质量 prompt 模板
- 采用现代化的前端技术栈，支持静态生成和增量渲染优化性能

**适用场景**:
- 个人用户：发现和学习优质 AI 提示词，提升 ChatGPT 等工具的使用效率
- 企业团队：自托管部署，在保护商业机密和用户数据隐私的前提下使用提示词库
- AI 开发者：参考开源架构搭建自己的提示词管理平台，或贡献优质提示词到社区



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,145 |
| 语言 | Jupyter Notebook |
| Forks | 14,012 |
| Issues | 5 |
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
| Stars | 55,124 |
| 语言 | TypeScript |
| Forks | 9,076 |
| Issues | 101 |
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
| Stars | 46,880 |
| 语言 | HTML |
| Forks | 4,606 |
| Issues | 10 |
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
| Stars | 43,554 |
| 语言 | Python |
| Forks | 9,961 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,451 |
| 语言 | Python |
| Forks | 2,036 |
| Issues | 118 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,659 |
| 语言 | JavaScript |
| Forks | 6,344 |
| Issues | 338 |
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
| Stars | 71,573 |
| 语言 | Python |
| Forks | 9,010 |
| Issues | 418 |
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
| Stars | 53,014 |
| 语言 | TypeScript |
| Forks | 4,274 |
| Issues | 579 |
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
| Stars | 52,091 |
| 语言 | TypeScript |
| Forks | 24,175 |
| Issues | 813 |
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
| Stars | 77,443 |
| 语言 | Python |
| Forks | 15,866 |
| Issues | 4,407 |
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
| Stars | 147,162 |
| 语言 | Python |
| Forks | 8,807 |
| Issues | 947 |
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
| Stars | 169,529 |
| 语言 | Go |
| Forks | 15,705 |
| Issues | 3,016 |
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
| Stars | 47,952 |
| 语言 | Rust |
| Forks | 9,578 |
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
| Stars | 34,168 |
| 语言 | Python |
| Forks | 2,156 |
| Issues | 97 |
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
| Stars | 113,297 |
| 语言 | Python |
| Forks | 7,345 |
| Issues | 615 |
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
| Stars | 68,252 |
| 语言 | Python |
| Forks | 6,979 |
| Issues | 115 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
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
| Stars | 70,375 |
| 语言 | Python |
| Forks | 8,606 |
| Issues | 978 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个支持 100+ 大模型统一微调的工业级框架，提供了从数据处理到模型部署的完整闭环，相比 Colab 方案能节省 80% 以上微调成本，且在 ACL 2024 获得顶会认可，是企业落地 LLM 和 VLM 的首选工具。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 Llama3、Qwen、DeepSeek、Gemma 等主流模型家族
- 集成 LoRA、QLoRA、Peft 等参数高效微调技术，显存占用降低 60-80%，单卡即可训练 7B 模型
- 支持 RLHF（DPO/PPO）、SFT、Supervisor Tuning 等多种训练范式，覆盖从基础微调到强化学习对齐全链路
- 内置 4-bit/8-bit 量化、Flash Attention、Gradient Checkpoint 等优化，支持 MoE 架构高效训练
- 提供 Web UI 和 CLI 双入口，支持分布式多节点训练，适配 DeepSpeed、 Accelerate 等主流训练框架

**适用场景**:
- 企业定制化场景：金融机构和医疗企业可基于 LlamaFactory 快速微调领域专属模型，满足数据安全和合规要求
- 学术研究场景：研究人员可便捷对比不同微调方法（LoRA vs QLoRA vs RLHF）在各类任务上的效果差异
- 多模态应用场景：支持视觉语言模型微调，适合构建垂类图文理解和生成系统，如文档分析、图表理解等业务



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,170 |
| 语言 | Python |
| Forks | 6,595 |
| Issues | 75 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过 66,000 颗星，集成了股票、加密货币、衍生品、固定收益等多类资产数据，并原生支持 AI Agent 开发，特别适合需要快速获取和分析金融数据的量化分析师和 AI 应用开发者。

**技术亮点**:
- 统一数据接口：聚合多个数据源，提供标准化的 API 和 CLI 工具，支持快速查询市场数据、财报、宏观经济指标等
- AI Agent 原生支持：专为 AI 代理设计，提供结构化数据输出和工具调用接口，便于构建金融领域的 AI 应用
- 全面的资产覆盖：涵盖股票、加密货币、期权、债券、外汇、宏观经济等 40+ 数据类别
- 模块化可扩展架构：支持自定义数据源和功能扩展，开放标准化接口供第三方集成
- 机器学习集成：内置数据预处理和特征工程工具，支持量化策略回测和因子分析

**适用场景**:
- 量化交易研究：用于获取市场数据、构建因子模型、执行回测和策略分析
- AI 金融应用开发：作为数据后端，为金融类 AI Agent 或聊天机器人提供实时市场数据和查询能力
- 投资研究与分析：个人投资者或机构分析师快速获取多资产类别数据、生成可视化报告和财务分析
- 金融数据聚合平台：企业可基于 OpenBB 构建定制化的金融数据仪表盘或内部研究系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,206 |
| 语言 | HTML |
| Forks | 20,963 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万星标和 5000+ 精选提示词，支持多种主流 AI 模型，企业可自托管实现数据完全私有化，是个人和团队提升 AI 效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的响应式 Web 应用架构
- 支持 ChatGPT、Claude、Gemini、GPT-4 等多种主流 LLM 模型
- 开源可自托管， 企业可部署私有版本保障数据隐私
- 社区驱动的提示词贡献机制，持续更新高质量 prompt 模板
- 采用现代化的前端技术栈，支持静态生成和增量渲染优化性能

**适用场景**:
- 个人用户：发现和学习优质 AI 提示词，提升 ChatGPT 等工具的使用效率
- 企业团队：自托管部署，在保护商业机密和用户数据隐私的前提下使用提示词库
- AI 开发者：参考开源架构搭建自己的提示词管理平台，或贡献优质提示词到社区



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,145 |
| 语言 | Jupyter Notebook |
| Forks | 14,012 |
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
| Stars | 159,656 |
| 语言 | Python |
| Forks | 32,944 |
| Issues | 2,349 |
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
| Stars | 77,443 |
| 语言 | Python |
| Forks | 15,866 |
| Issues | 4,407 |
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
| Stars | 109,390 |
| 语言 | Python |
| Forks | 12,718 |
| Issues | 4,000 |
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
| Stars | 99,289 |
| 语言 | Python |
| Forks | 27,534 |
| Issues | 18,509 |
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
| Stars | 33,870 |
| 语言 | TypeScript |
| Forks | 3,671 |
| Issues | 291 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,849 |
| 语言 | Jupyter Notebook |
| Forks | 5,601 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 🛠️ 开发工具 (16 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,035 |
| 语言 | JavaScript |
| Forks | 25,185 |
| Issues | 132 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向 AI 代码助手的性能优化框架，通过 Skills、Instincts、Memory 和 Security 等模块显著提升 Claude Code、Cursor 等工具的开发效率，162K+ Stars 证明了其在 AI 辅助开发领域的广泛认可。

**技术亮点**:
- 多 AI 编码工具统一框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化体验
- 模块化 AI Agent 架构：包含 Skills（技能）、Instincts（本能）、Memory（记忆）等核心组件，实现复杂任务分解与执行
- Memory 记忆系统：持久化上下文和会话状态，解决长对话场景下的上下文丢失问题
- Security 安全模块：内置代码安全审查和敏感信息保护机制，确保 AI 生成代码的安全性
- MCP (Model Context Protocol) 深度集成：标准化模型上下文交互协议，提升 AI 理解代码的能力

**适用场景**:
- 企业级 AI 开发助手集成：团队可将框架部署到内部开发环境，统一管理 AI 编码规范和安全策略
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 助手能力，实现自动化代码重构和测试生成
- AI Agent 应用开发：基于框架构建定制化的 AI 编程助手，支持特定领域知识的注入



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,623 |
| 语言 | Go |
| Forks | 3,977 |
| Issues | 171 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的开源本地 AI 部署方案，支持 LLM、图像、语音、视频等多种模型，无需 GPU 即可运行，特别适合隐私敏感或需要完全控制 AI 能力的场景，在 GitHub 上获得 45k+ Stars 证明其社区认可度极高。

**技术亮点**:
- 多模型支持：支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 无需 GPU 即可运行：支持 CPU 推理，大幅降低部署门槛，可在普通硬件上运行 AI 模型
- Go 语言开发：高性能、高并发，原生支持分布式部署和 libp2p 去中心化网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- 丰富的模型支持：支持 Mamba 架构、ReRank 模型、多模态模型等前沿技术，涵盖 text-generation、image-generation、audio-generation 等全场景

**适用场景**:
- 隐私敏感的本地 AI 部署：企业或个人不想将数据发送到第三方服务，需要完全控制的数据处理场景
- 资源受限环境：在没有 GPU 的服务器、开发机或边缘设备上运行 AI 推理任务
- 快速集成 AI 能力的应用开发：通过 OpenAI 兼容的 API 为现有应用快速添加 AI 功能，支持文本生成、图像生成、语音合成等多种能力



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,573 |
| 语言 | Python |
| Forks | 9,010 |
| Issues | 418 |
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
| Stars | 53,014 |
| 语言 | TypeScript |
| Forks | 4,274 |
| Issues | 579 |
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
| Stars | 184,872 |
| 语言 | TypeScript |
| Forks | 56,982 |
| Issues | 1,550 |
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
| Stars | 157,850 |
| 语言 | Python |
| Forks | 13,029 |
| Issues | 2,460 |
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
| Stars | 97,441 |
| 语言 | Python |
| Forks | 9,106 |
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
| Stars | 81,596 |
| 语言 | Python |
| Forks | 9,489 |
| Issues | 259 |
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
| Stars | 184,050 |
| 语言 | TypeScript |
| Forks | 39,290 |
| Issues | 16,503 |
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
| Stars | 94,159 |
| 语言 | TypeScript |
| Forks | 9,412 |
| Issues | 296 |
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
| Stars | 78,984 |
| 语言 | TypeScript |
| Forks | 5,817 |
| Issues | 767 |
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
| Stars | 77,198 |
| 语言 | TypeScript |
| Forks | 6,620 |
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
| Stars | 79,658 |
| 语言 | Go |
| Forks | 2,786 |
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
| Stars | 76,748 |
| 语言 | Go |
| Forks | 2,774 |
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
| Stars | 43,942 |
| 语言 | Go |
| Forks | 8,298 |
| Issues | 977 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ⭐ 中优先级


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,584 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 715 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (12 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,014 |
| 语言 | TypeScript |
| Forks | 4,274 |
| Issues | 579 |
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
| Stars | 184,872 |
| 语言 | TypeScript |
| Forks | 56,982 |
| Issues | 1,550 |
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
| Stars | 51,647 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 233 |
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
| Stars | 121,801 |
| 语言 | Go |
| Forks | 42,880 |
| Issues | 2,784 |
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
| Stars | 71,500 |
| 语言 | Go |
| Forks | 18,918 |
| Issues | 3,792 |
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
| Stars | 54,998 |
| 语言 | Go |
| Forks | 6,598 |
| Issues | 2,835 |
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
| Stars | 47,512 |
| 语言 | Go |
| Forks | 5,045 |
| Issues | 981 |
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
| Stars | 94,159 |
| 语言 | TypeScript |
| Forks | 9,412 |
| Issues | 296 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,514 |
| 语言 | JavaScript |
| Forks | 7,663 |
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
| Stars | 69,951 |
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
| Stars | 62,787 |
| 语言 | Go |
| Forks | 5,928 |
| Issues | 763 |
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
| Stars | 59,018 |
| 语言 | Go |
| Forks | 4,288 |
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
| Stars | 85,514 |
| 语言 | JavaScript |
| Forks | 7,663 |
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
| Stars | 63,662 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 751 |
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
| Stars | 45,623 |
| 语言 | Go |
| Forks | 3,977 |
| Issues | 171 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的开源本地 AI 部署方案，支持 LLM、图像、语音、视频等多种模型，无需 GPU 即可运行，特别适合隐私敏感或需要完全控制 AI 能力的场景，在 GitHub 上获得 45k+ Stars 证明其社区认可度极高。

**技术亮点**:
- 多模型支持：支持 LLMs（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 无需 GPU 即可运行：支持 CPU 推理，大幅降低部署门槛，可在普通硬件上运行 AI 模型
- Go 语言开发：高性能、高并发，原生支持分布式部署和 libp2p 去中心化网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- 丰富的模型支持：支持 Mamba 架构、ReRank 模型、多模态模型等前沿技术，涵盖 text-generation、image-generation、audio-generation 等全场景

**适用场景**:
- 隐私敏感的本地 AI 部署：企业或个人不想将数据发送到第三方服务，需要完全控制的数据处理场景
- 资源受限环境：在没有 GPU 的服务器、开发机或边缘设备上运行 AI 推理任务
- 快速集成 AI 能力的应用开发：通过 OpenAI 兼容的 API 为现有应用快速添加 AI 功能，支持文本生成、图像生成、语音合成等多种能力



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,441 |
| 语言 | Python |
| Forks | 9,106 |
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
| Stars | 87,290 |
| 语言 | Python |
| Forks | 33,815 |
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
| Stars | 100,065 |
| 语言 | TypeScript |
| Forks | 27,179 |
| Issues | 1,125 |
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
| Stars | 78,984 |
| 语言 | TypeScript |
| Forks | 5,817 |
| Issues | 767 |
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
| Stars | 68,951 |
| 语言 | JavaScript |
| Forks | 23,155 |
| Issues | 211 |
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
| Stars | 55,958 |
| 语言 | JavaScript |
| Forks | 10,209 |
| Issues | 367 |
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
| Stars | 51,809 |
| 语言 | JavaScript |
| Forks | 4,706 |
| Issues | 1,463 |
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
| Stars | 71,698 |
| 语言 | Go |
| Forks | 4,699 |
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
| Stars | 57,747 |
| 语言 | Go |
| Forks | 3,304 |
| Issues | 16 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,584 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 715 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,355 |
| 语言 | Go |
| Forks | 8,574 |
| Issues | 675 |
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
| Stars | 101,169 |
| 语言 | TypeScript |
| Forks | 12,140 |
| Issues | 963 |
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
| Stars | 58,659 |
| 语言 | JavaScript |
| Forks | 6,344 |
| Issues | 338 |
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
| Stars | 43,880 |
| 语言 | Go |
| Forks | 3,967 |
| Issues | 1,132 |
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
| Stars | 51,647 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 233 |
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
| Stars | 160,206 |
| 语言 | HTML |
| Forks | 20,963 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万星标和 5000+ 精选提示词，支持多种主流 AI 模型，企业可自托管实现数据完全私有化，是个人和团队提升 AI 效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供完整的响应式 Web 应用架构
- 支持 ChatGPT、Claude、Gemini、GPT-4 等多种主流 LLM 模型
- 开源可自托管， 企业可部署私有版本保障数据隐私
- 社区驱动的提示词贡献机制，持续更新高质量 prompt 模板
- 采用现代化的前端技术栈，支持静态生成和增量渲染优化性能

**适用场景**:
- 个人用户：发现和学习优质 AI 提示词，提升 ChatGPT 等工具的使用效率
- 企业团队：自托管部署，在保护商业机密和用户数据隐私的前提下使用提示词库
- AI 开发者：参考开源架构搭建自己的提示词管理平台，或贡献优质提示词到社区



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,124 |
| 语言 | TypeScript |
| Forks | 9,076 |
| Issues | 101 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,451 |
| 语言 | Python |
| Forks | 2,036 |
| Issues | 118 |
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
| Stars | 38,907 |
| 语言 | Python |
| Forks | 4,627 |
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
| Stars | 89,752 |
| 语言 | TypeScript |
| Forks | 10,022 |
| Issues | 2,248 |
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
| Stars | 87,505 |
| 语言 | TypeScript |
| Forks | 8,887 |
| Issues | 1,651 |
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
| Stars | 127,517 |
| 语言 | JavaScript |
| Forks | 12,473 |
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
| Stars | 170,513 |
| 语言 | Go |
| Forks | 13,165 |
| Issues | 182 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,634 |
| 语言 | Unknown |
| Forks | 34,012 |
| Issues | 146 |
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
| Stars | 91,319 |
| 语言 | Python |
| Forks | 13,296 |
| Issues | 104 |
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
| Stars | 89,617 |
| 语言 | Python |
| Forks | 7,711 |
| Issues | 627 |
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
| Stars | 385,767 |
| 语言 | Python |
| Forks | 66,112 |
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
| Stars | 114,971 |
| 语言 | TypeScript |
| Forks | 5,972 |
| Issues | 208 |
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
| Stars | 112,091 |
| 语言 | TypeScript |
| Forks | 8,176 |
| Issues | 279 |
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
| Stars | 78,516 |
| 语言 | TypeScript |
| Forks | 11,282 |
| Issues | 365 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,353 |
| 语言 | JavaScript |
| Forks | 4,669 |
| Issues | 34 |
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
| Stars | 48,174 |
| 语言 | Go |
| Forks | 10,293 |
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
| Stars | 105,275 |
| 语言 | C++ |
| Forks | 17,119 |
| Issues | 1,543 |
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
| Stars | 63,454 |
| 语言 | Python |
| Forks | 1,624 |
| Issues | 36 |
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
| Stars | 65,851 |
| 语言 | Unknown |
| Forks | 5,804 |
| Issues | 61 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 293,433 |
| 语言 | Python |
| Forks | 27,725 |
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
| Stars | 219,942 |
| 语言 | Python |
| Forks | 50,371 |
| Issues | 932 |
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
| Stars | 98,088 |
| 语言 | Python |
| Forks | 12,069 |
| Issues | 121 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,158 |
| 语言 | Python |
| Forks | 7,221 |
| Issues | 485 |
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
| Stars | 86,119 |
| 语言 | Python |
| Forks | 37,281 |
| Issues | 3,634 |
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
| Forks | 45,134 |
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
| Stars | 77,036 |
| 语言 | Python |
| Forks | 16,863 |
| Issues | 23 |
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
| Stars | 443,259 |
| 语言 | TypeScript |
| Forks | 44,348 |
| Issues | 203 |
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
| Stars | 353,260 |
| 语言 | TypeScript |
| Forks | 43,952 |
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
| Stars | 121,543 |
| 语言 | TypeScript |
| Forks | 13,358 |
| Issues | 2,994 |
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
| Stars | 112,681 |
| 语言 | TypeScript |
| Forks | 8,597 |
| Issues | 1,827 |
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
| Stars | 108,599 |
| 语言 | TypeScript |
| Forks | 13,355 |
| Issues | 5,021 |
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
| Stars | 98,253 |
| 语言 | TypeScript |
| Forks | 5,434 |
| Issues | 691 |
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
| Stars | 97,820 |
| 语言 | TypeScript |
| Forks | 54,594 |
| Issues | 1,366 |
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
| Stars | 94,655 |
| 语言 | TypeScript |
| Forks | 5,204 |
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
| Stars | 84,153 |
| 语言 | TypeScript |
| Forks | 10,453 |
| Issues | 345 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,206 |
| 语言 | TypeScript |
| Forks | 7,592 |
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
| Stars | 80,028 |
| 语言 | TypeScript |
| Forks | 8,073 |
| Issues | 704 |
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
| Stars | 244,589 |
| 语言 | JavaScript |
| Forks | 50,962 |
| Issues | 1,234 |
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
| Stars | 148,124 |
| 语言 | JavaScript |
| Forks | 26,715 |
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
| Stars | 116,833 |
| 语言 | JavaScript |
| Forks | 35,400 |
| Issues | 2,636 |
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
| Stars | 112,089 |
| 语言 | JavaScript |
| Forks | 36,327 |
| Issues | 533 |
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
| Stars | 109,030 |
| 语言 | JavaScript |
| Forks | 11,644 |
| Issues | 276 |
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
| Stars | 98,188 |
| 语言 | JavaScript |
| Forks | 32,669 |
| Issues | 1,571 |
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
| Stars | 95,635 |
| 语言 | JavaScript |
| Forks | 15,383 |
| Issues | 49 |
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
| Stars | 86,367 |
| 语言 | JavaScript |
| Forks | 4,892 |
| Issues | 989 |
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
| Stars | 71,038 |
| 语言 | JavaScript |
| Forks | 16,806 |
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
| Stars | 67,368 |
| 语言 | JavaScript |
| Forks | 11,956 |
| Issues | 551 |
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
| Stars | 65,813 |
| 语言 | JavaScript |
| Forks | 9,362 |
| Issues | 203 |
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
| Stars | 62,881 |
| 语言 | JavaScript |
| Forks | 4,018 |
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
| Stars | 60,569 |
| 语言 | JavaScript |
| Forks | 5,654 |
| Issues | 63 |
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
| Stars | 59,829 |
| 语言 | JavaScript |
| Forks | 20,468 |
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
| Stars | 57,425 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 24 |
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
| Stars | 53,160 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 452 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,575 |
| 语言 | JavaScript |
| Forks | 11,478 |
| Issues | 247 |
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
| Stars | 133,557 |
| 语言 | Go |
| Forks | 18,940 |
| Issues | 9,982 |
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
| Stars | 106,035 |
| 语言 | Go |
| Forks | 15,004 |
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
| Stars | 87,696 |
| 语言 | Go |
| Forks | 8,235 |
| Issues | 246 |
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
| Stars | 82,308 |
| 语言 | Go |
| Forks | 5,044 |
| Issues | 394 |
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
| Stars | 68,618 |
| 语言 | Go |
| Forks | 3,218 |
| Issues | 20 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,756 |
| 语言 | Go |
| Forks | 5,045 |
| Issues | 1,173 |
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
| Stars | 50,989 |
| 语言 | Go |
| Forks | 21,887 |
| Issues | 401 |
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
| Stars | 50,724 |
| 语言 | Go |
| Forks | 1,605 |
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
| Stars | 49,322 |
| 语言 | Go |
| Forks | 7,949 |
| Issues | 556 |
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
| Stars | 46,024 |
| 语言 | Go |
| Forks | 3,796 |
| Issues | 83 |
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
| Stars | 84,046 |
| 语言 | Shell |
| Forks | 13,389 |
| Issues | 100 |
| 许可证 | MIT License |


### ⭐ 中优先级


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,933 |
| 语言 | TypeScript |
| Forks | 16,514 |
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
| Stars | 79,098 |
| 语言 | JavaScript |
| Forks | 32,592 |
| Issues | 278 |
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
| Stars | 66,331 |
| 语言 | JavaScript |
| Forks | 9,191 |
| Issues | 1 |
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
| Stars | 61,303 |
| 语言 | JavaScript |
| Forks | 7,140 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 152,124 |
| 语言 | Python |
| Forks | 11,581 |
| Issues | 331 |
| Topics | awesome, github, hellogithub, python |
