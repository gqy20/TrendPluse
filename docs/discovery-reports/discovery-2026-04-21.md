# 项目发现报告 (2026-04-21)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 34 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 15 |
| ⚙️ DevOps/基础设施 | 14 |
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
| Stars | 133,051 |
| 语言 | Python |
| Forks | 18,878 |
| Issues | 249 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一的 Web 界面整合了 Ollama、OpenAI API 等多种 LLM 后端，同时内置 RAG 和 MCP 支持，让用户无需编写代码即可快速部署私有化 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的企业和个人开发者。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 等主流 LLM 提供商，支持 OpenAPI 标准接口
- RAG 功能：内置检索增强生成能力，支持知识库问答和文档处理
- MCP 协议支持：支持 Model Context Protocol，实现更强大的上下文管理和工具调用
- 自托管部署：完全自主控制，数据不出本地，适合对数据隐私有严格要求的场景
- 现代化 Web UI：提供直观的用户界面，支持多用户管理和丰富的配置选项

**适用场景**:
- 企业级 AI 助手：在企业内部私有化部署，处理敏感业务数据，满足合规和隐私要求
- 个人开发者/研究者：快速搭建本地 LLM 实验环境，测试和对比不同模型效果
- 知识管理团队：利用 RAG 功能构建私有知识库问答系统，提升信息检索效率



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,884 |
| 语言 | Python |
| Forks | 15,512 |
| Issues | 6,001 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

 NousResearch 出品的 AI Agent 框架，拥有超过 10 万 Stars 的高人气，支持多 AI 提供商（Claude、ChatGPT 等）统一调用，提供了可扩展的 agent 架构设计，适合构建复杂的多步骤任务自动化系统。

**技术亮点**:
- 多 AI 提供商集成：支持 Anthropic Claude、OpenAI GPT、Nous Research 等主流 LLM 的统一接口调用
- 模块化 Agent 架构：提供可组合的工具系统和行为扩展机制，便于自定义工作流
- MIT 许可证开源：允许商业使用，社区活跃度高，经过大规模生产环境验证
- 支持 Code Agent 能力：集成 Claude Code 和 Codex 等代码生成与执行功能
- 丰富的插件生态：基于 Topics 可以看出支持 clawdbot、moltbot 等多种机器人集成

**适用场景**:
- 企业级 AI 自动化工作流：构建客服机器人、文档处理、数据分析等业务流程自动化
- 开发者 AI 助手：集成到 IDE 或 CLI 中，实现代码审查、bug 修复、代码生成等开发辅助功能
- 多模型对比与选择：利用多提供商支持，在同一框架内对比不同 LLM 的效果和成本



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,673 |
| 语言 | Python |
| Forks | 8,886 |
| Issues | 2,970 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎项目之一（78k+ Stars），它创新性地将 RAG 与 Agent 能力深度融合，为大语言模型提供了 superior context layer，特别适合构建企业级智能问答系统和知识库应用。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 Agent 智能体能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解：支持复杂文档的智能解析和处理，包括多格式文档的结构化提取
- 多 LLM 后端支持：原生支持 OpenAI、DeepSeek、Ollama 等多种主流大模型，可灵活切换
- GraphRAG 支持：集成图谱增强检索能力，提升关系型知识的检索效果
- MCP 协议集成：支持 Model Context Protocol，便于扩展和集成外部工具

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服和文档问答系统
- Deep Research 深度研究：用于学术研究、市场分析等需要深入推理的复杂查询场景
- Agentic Workflow 自动化：开发基于 RAG 的智能工作流，实现文档处理、信息抽取等自动化任务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 163,040 |
| 语言 | JavaScript |
| Forks | 25,315 |
| Issues | 159 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等 AI 编程助手提供全面性能优化的开源系统，通过 Skills、Instincts、Memory 和 Security 模块显著提升 AI Agent 的开发效率和安全性，适合追求极致开发工作流优化的团队和个人。

**技术亮点**:
- 模块化 Agent 架构：提供 Skills、Instincts、Memory 三大核心模块，支持灵活扩展和定制 AI 行为模式
- 安全优先设计：内置 Security 模块确保 AI 操作的安全边界，防止越权和危险操作
- MCP 协议支持：深度集成 Model Context Protocol，实现与多种 AI 平台的无缝对接
- 性能优化系统：专门针对 AI Agent 执行效率进行优化，减少响应延迟和资源消耗
- 研究驱动开发：采用 Research-first 开发理念，确保技术方案基于最新 AI 研究成果

**适用场景**:
- 企业级 AI 开发团队：构建标准化、可控的 AI 编程辅助工作流
- 个人开发者：快速搭建个人 AI 助手环境，提升编程效率
- AI 产品集成：将项目作为基础框架，为自研 AI 编程产品添加高级能力



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,669 |
| 语言 | Go |
| Forks | 3,988 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源 AI 推理引擎，支持在无需 GPU 的消费级硬件上运行 LLM、图像生成、语音合成等多种模型，提供 OpenAI 兼容 API，是构建私有 AI 应用的理想选择。

**技术亮点**:
- 多模态统一推理：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、TTS 等多种模型
- 硬件无依赖：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- Go 语言开发：高性能、跨平台编译，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和去中心化部署场景

**适用场景**:
- 私有 AI 部署：企业或个人在本地/私有云部署 AI 服务，确保数据隐私安全
- 边缘计算场景：在资源受限的边缘设备上运行 AI 推理任务
- 开发测试环境：开发者本地快速构建和测试 AI 应用原型



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,444 |
| 语言 | TypeScript |
| Forks | 14,951 |
| Issues | 705 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发与协作平台，拥有超过 7.5 万 Stars，支持多 AI 模型接入（OpenAI、Claude、DeepSeek、Gemini 等），提供开箱即用的 Chat 界面、知识库管理和 MCP 协议扩展能力，是构建企业级 AI 应用和探索多 Agent 协作的最佳起点。

**技术亮点**:
- 多模型统一接入层：无缝支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具、数据源的标准化连接，扩展性强
- 多 Agent 协作框架：支持设计和管理 Agent 团队，Agent 可作为工作交互的基本单元协同完成任务
- 完整的知识库系统：内置 RAG 能力，支持文档管理和向量检索，为 Agent 提供持久化记忆
- TypeScript 全栈架构：基于 React + Node.js 构建，提供完整的类型安全和现代化的开发体验

**适用场景**:
- 企业 AI 应用开发：快速构建智能客服、知识问答、业务助手等企业级 AI 解决方案
- 多 Agent 协作场景：构建复杂的工作流自动化，如研究分析、内容创作、数据处理等需要多个 AI 角色配合的任务
- 个人 AI 助手：作为个人工作空间，集成的 Chat、知识管理和 Agent 协作能力可以显著提升个人生产力



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,429 |
| 语言 | Python |
| Forks | 8,613 |
| Issues | 977 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个获得 ACL 2024 认可的大模型微调框架，提供统一的接口支持 100+ 大语言模型和多模态模型的高效微调，尤其适合资源有限的场景下快速定制化部署企业级 LLM 应用。

**技术亮点**:
- 统一微调框架：支持 Llama、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 和 VLMs，一套代码支持多种模型族
- 集成多种高效微调技术：LoRA、QLoRA、AdaLoRA、Prefix Tuning、Ptuning 等 PEFT 方法，支持 RLHF、DPO、ORPO 等对齐训练
- 深度优化训练效率：支持 FlashAttention-2、混合精度训练、DeepSpeed 加速，显著降低 GPU 显存占用
- 完善的数据处理流程：支持多格式数据集加载、自动模板构建、数据混合比例控制
- 便捷的训练监控与导出：集成 TensorBoard 监控、模型量化和导出为 Oaffinium 格式，部署流程简化

**适用场景**:
- 企业场景：企业可基于 LlamaFactory 快速将开源大模型微调至垂直领域（如金融、医疗、法律），实现私有化部署和成本控制
- 学术研究：研究人员可灵活实验各种 PEFT 方法、RLHF 流程和数据配比，快速验证假设并复现实验
- 个人开发者：个人开发者可利用 QLoRA 在消费级 GPU 上微调大模型，创建定制化聊天机器人或个人 AI 助手



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,068 |
| 语言 | TypeScript |
| Forks | 5,481 |
| Issues | 123 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是 Claude Code 的革命性记忆插件，通过 AI 自动压缩编码会话历史并向未来会话注入相关上下文，解决了大模型无法跨会话保持记忆的核心痛点，配合 RAG 和 ChromaDB 向量检索实现智能上下文复用，大幅提升 AI 辅助编程的连续性和效率。

**技术亮点**:
- 基于 ChromaDB 的向量数据库实现语义相似性检索，支持精确回溯历史编码决策
- 集成 Claude Agent SDK 进行 AI 驱动的会话压缩，智能提取关键上下文信息
- 采用 RAG（检索增强生成）架构，将长期记忆无缝注入 AI 响应流程
- 使用 SQLite 本地存储元数据，轻量级且便于隐私保护
- 支持 embeddings 向量化表示，实现跨会话的语义级记忆关联

**适用场景**:
- 长期大型项目开发：跨多日/多周维护复杂的代码库，AI 可自动回忆之前的架构决策和技术选型
- 团队知识传承：开发者离开后，接手者可借助 AI 记忆快速理解历史上下文和编码规范
- 复杂调试场景：AI 可关联历史相似的 bug 修复经验，提供更精准的问题诊断建议
- 个人开发者效率提升：构建个人编码记忆库，让 AI 助手越用越懂你的编码风格和偏好



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,424 |
| 语言 | TypeScript |
| Forks | 9,130 |
| Issues | 102 |
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
| Stars | 47,142 |
| 语言 | HTML |
| Forks | 4,634 |
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
| Stars | 43,596 |
| 语言 | Python |
| Forks | 9,962 |
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
| Stars | 45,911 |
| 语言 | Java |
| Forks | 15,928 |
| Issues | 10 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,278 |
| 语言 | Python |
| Forks | 4,676 |
| Issues | 93 |
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
| Stars | 39,026 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 63 |
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
| Stars | 111,333 |
| 语言 | TypeScript |
| Forks | 7,108 |
| Issues | 287 |
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
| Stars | 58,703 |
| 语言 | JavaScript |
| Forks | 6,349 |
| Issues | 336 |
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
| Stars | 71,649 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 411 |
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
| Stars | 53,235 |
| 语言 | TypeScript |
| Forks | 4,289 |
| Issues | 592 |
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
| Stars | 106,753 |
| 语言 | Python |
| Forks | 15,667 |
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
| Stars | 89,227 |
| 语言 | Python |
| Forks | 10,202 |
| Issues | 223 |
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
| Stars | 52,128 |
| 语言 | TypeScript |
| Forks | 24,184 |
| Issues | 816 |
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
| Stars | 185,010 |
| 语言 | TypeScript |
| Forks | 57,008 |
| Issues | 1,543 |
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
| Stars | 155,124 |
| 语言 | Java |
| Forks | 46,144 |
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
| Stars | 147,220 |
| 语言 | Python |
| Forks | 8,816 |
| Issues | 959 |
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
| Stars | 57,527 |
| 语言 | Jupyter Notebook |
| Forks | 19,856 |
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
| Stars | 55,402 |
| 语言 | Python |
| Forks | 5,945 |
| Issues | 542 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,180 |
| 语言 | Python |
| Forks | 2,162 |
| Issues | 100 |
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
| Stars | 33,921 |
| 语言 | Jupyter Notebook |
| Forks | 5,611 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,886 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 293 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,456 |
| 语言 | Rust |
| Forks | 3,100 |
| Issues | 558 |
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
| Stars | 133,051 |
| 语言 | Python |
| Forks | 18,878 |
| Issues | 249 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一的 Web 界面整合了 Ollama、OpenAI API 等多种 LLM 后端，同时内置 RAG 和 MCP 支持，让用户无需编写代码即可快速部署私有化 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的企业和个人开发者。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 等主流 LLM 提供商，支持 OpenAPI 标准接口
- RAG 功能：内置检索增强生成能力，支持知识库问答和文档处理
- MCP 协议支持：支持 Model Context Protocol，实现更强大的上下文管理和工具调用
- 自托管部署：完全自主控制，数据不出本地，适合对数据隐私有严格要求的场景
- 现代化 Web UI：提供直观的用户界面，支持多用户管理和丰富的配置选项

**适用场景**:
- 企业级 AI 助手：在企业内部私有化部署，处理敏感业务数据，满足合规和隐私要求
- 个人开发者/研究者：快速搭建本地 LLM 实验环境，测试和对比不同模型效果
- 知识管理团队：利用 RAG 功能构建私有知识库问答系统，提升信息检索效率



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,673 |
| 语言 | Python |
| Forks | 8,886 |
| Issues | 2,970 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎项目之一（78k+ Stars），它创新性地将 RAG 与 Agent 能力深度融合，为大语言模型提供了 superior context layer，特别适合构建企业级智能问答系统和知识库应用。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 Agent 智能体能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解：支持复杂文档的智能解析和处理，包括多格式文档的结构化提取
- 多 LLM 后端支持：原生支持 OpenAI、DeepSeek、Ollama 等多种主流大模型，可灵活切换
- GraphRAG 支持：集成图谱增强检索能力，提升关系型知识的检索效果
- MCP 协议集成：支持 Model Context Protocol，便于扩展和集成外部工具

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服和文档问答系统
- Deep Research 深度研究：用于学术研究、市场分析等需要深入推理的复杂查询场景
- Agentic Workflow 自动化：开发基于 RAG 的智能工作流，实现文档处理、信息抽取等自动化任务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,444 |
| 语言 | TypeScript |
| Forks | 14,951 |
| Issues | 705 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发与协作平台，拥有超过 7.5 万 Stars，支持多 AI 模型接入（OpenAI、Claude、DeepSeek、Gemini 等），提供开箱即用的 Chat 界面、知识库管理和 MCP 协议扩展能力，是构建企业级 AI 应用和探索多 Agent 协作的最佳起点。

**技术亮点**:
- 多模型统一接入层：无缝支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具、数据源的标准化连接，扩展性强
- 多 Agent 协作框架：支持设计和管理 Agent 团队，Agent 可作为工作交互的基本单元协同完成任务
- 完整的知识库系统：内置 RAG 能力，支持文档管理和向量检索，为 Agent 提供持久化记忆
- TypeScript 全栈架构：基于 React + Node.js 构建，提供完整的类型安全和现代化的开发体验

**适用场景**:
- 企业 AI 应用开发：快速构建智能客服、知识问答、业务助手等企业级 AI 解决方案
- 多 Agent 协作场景：构建复杂的工作流自动化，如研究分析、内容创作、数据处理等需要多个 AI 角色配合的任务
- 个人 AI 助手：作为个人工作空间，集成的 Chat、知识管理和 Agent 协作能力可以显著提升个人生产力



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,068 |
| 语言 | TypeScript |
| Forks | 5,481 |
| Issues | 123 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是 Claude Code 的革命性记忆插件，通过 AI 自动压缩编码会话历史并向未来会话注入相关上下文，解决了大模型无法跨会话保持记忆的核心痛点，配合 RAG 和 ChromaDB 向量检索实现智能上下文复用，大幅提升 AI 辅助编程的连续性和效率。

**技术亮点**:
- 基于 ChromaDB 的向量数据库实现语义相似性检索，支持精确回溯历史编码决策
- 集成 Claude Agent SDK 进行 AI 驱动的会话压缩，智能提取关键上下文信息
- 采用 RAG（检索增强生成）架构，将长期记忆无缝注入 AI 响应流程
- 使用 SQLite 本地存储元数据，轻量级且便于隐私保护
- 支持 embeddings 向量化表示，实现跨会话的语义级记忆关联

**适用场景**:
- 长期大型项目开发：跨多日/多周维护复杂的代码库，AI 可自动回忆之前的架构决策和技术选型
- 团队知识传承：开发者离开后，接手者可借助 AI 记忆快速理解历史上下文和编码规范
- 复杂调试场景：AI 可关联历史相似的 bug 修复经验，提供更精准的问题诊断建议
- 个人开发者效率提升：构建个人编码记忆库，让 AI 助手越用越懂你的编码风格和偏好



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,911 |
| 语言 | Java |
| Forks | 15,928 |
| Issues | 10 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,278 |
| 语言 | Python |
| Forks | 4,676 |
| Issues | 93 |
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
| Stars | 39,026 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 63 |
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
| Stars | 101,218 |
| 语言 | TypeScript |
| Forks | 12,143 |
| Issues | 952 |
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
| Stars | 58,703 |
| 语言 | JavaScript |
| Forks | 6,349 |
| Issues | 336 |
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
| Stars | 106,753 |
| 语言 | Python |
| Forks | 15,667 |
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
| Stars | 76,099 |
| 语言 | Python |
| Forks | 10,267 |
| Issues | 231 |
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
| Stars | 52,128 |
| 语言 | TypeScript |
| Forks | 24,184 |
| Issues | 816 |
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
| Stars | 43,897 |
| 语言 | Go |
| Forks | 3,969 |
| Issues | 1,131 |
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
| Stars | 33,991 |
| 语言 | Python |
| Forks | 4,821 |
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
| Stars | 34,180 |
| 语言 | Python |
| Forks | 2,162 |
| Issues | 100 |
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
| Stars | 33,921 |
| 语言 | Jupyter Notebook |
| Forks | 5,611 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,886 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 293 |
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
| Stars | 133,051 |
| 语言 | Python |
| Forks | 18,878 |
| Issues | 249 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的自托管 AI 界面解决方案，通过统一的 Web 界面整合了 Ollama、OpenAI API 等多种 LLM 后端，同时内置 RAG 和 MCP 支持，让用户无需编写代码即可快速部署私有化 AI 助手，特别适合注重数据隐私和希望掌控 AI 基础设施的企业和个人开发者。

**技术亮点**:
- 多后端支持：无缝集成 Ollama、OpenAI API 等主流 LLM 提供商，支持 OpenAPI 标准接口
- RAG 功能：内置检索增强生成能力，支持知识库问答和文档处理
- MCP 协议支持：支持 Model Context Protocol，实现更强大的上下文管理和工具调用
- 自托管部署：完全自主控制，数据不出本地，适合对数据隐私有严格要求的场景
- 现代化 Web UI：提供直观的用户界面，支持多用户管理和丰富的配置选项

**适用场景**:
- 企业级 AI 助手：在企业内部私有化部署，处理敏感业务数据，满足合规和隐私要求
- 个人开发者/研究者：快速搭建本地 LLM 实验环境，测试和对比不同模型效果
- 知识管理团队：利用 RAG 功能构建私有知识库问答系统，提升信息检索效率



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,884 |
| 语言 | Python |
| Forks | 15,512 |
| Issues | 6,001 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

 NousResearch 出品的 AI Agent 框架，拥有超过 10 万 Stars 的高人气，支持多 AI 提供商（Claude、ChatGPT 等）统一调用，提供了可扩展的 agent 架构设计，适合构建复杂的多步骤任务自动化系统。

**技术亮点**:
- 多 AI 提供商集成：支持 Anthropic Claude、OpenAI GPT、Nous Research 等主流 LLM 的统一接口调用
- 模块化 Agent 架构：提供可组合的工具系统和行为扩展机制，便于自定义工作流
- MIT 许可证开源：允许商业使用，社区活跃度高，经过大规模生产环境验证
- 支持 Code Agent 能力：集成 Claude Code 和 Codex 等代码生成与执行功能
- 丰富的插件生态：基于 Topics 可以看出支持 clawdbot、moltbot 等多种机器人集成

**适用场景**:
- 企业级 AI 自动化工作流：构建客服机器人、文档处理、数据分析等业务流程自动化
- 开发者 AI 助手：集成到 IDE 或 CLI 中，实现代码审查、bug 修复、代码生成等开发辅助功能
- 多模型对比与选择：利用多提供商支持，在同一框架内对比不同 LLM 的效果和成本



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,673 |
| 语言 | Python |
| Forks | 8,886 |
| Issues | 2,970 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的开源 RAG 引擎项目之一（78k+ Stars），它创新性地将 RAG 与 Agent 能力深度融合，为大语言模型提供了 superior context layer，特别适合构建企业级智能问答系统和知识库应用。

**技术亮点**:
- RAG + Agent 双引擎架构：将检索增强生成与 Agent 智能体能力完美结合，实现更智能的上下文理解和任务执行
- 深度文档理解：支持复杂文档的智能解析和处理，包括多格式文档的结构化提取
- 多 LLM 后端支持：原生支持 OpenAI、DeepSeek、Ollama 等多种主流大模型，可灵活切换
- GraphRAG 支持：集成图谱增强检索能力，提升关系型知识的检索效果
- MCP 协议集成：支持 Model Context Protocol，便于扩展和集成外部工具

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服和文档问答系统
- Deep Research 深度研究：用于学术研究、市场分析等需要深入推理的复杂查询场景
- Agentic Workflow 自动化：开发基于 RAG 的智能工作流，实现文档处理、信息抽取等自动化任务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 163,040 |
| 语言 | JavaScript |
| Forks | 25,315 |
| Issues | 159 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等 AI 编程助手提供全面性能优化的开源系统，通过 Skills、Instincts、Memory 和 Security 模块显著提升 AI Agent 的开发效率和安全性，适合追求极致开发工作流优化的团队和个人。

**技术亮点**:
- 模块化 Agent 架构：提供 Skills、Instincts、Memory 三大核心模块，支持灵活扩展和定制 AI 行为模式
- 安全优先设计：内置 Security 模块确保 AI 操作的安全边界，防止越权和危险操作
- MCP 协议支持：深度集成 Model Context Protocol，实现与多种 AI 平台的无缝对接
- 性能优化系统：专门针对 AI Agent 执行效率进行优化，减少响应延迟和资源消耗
- 研究驱动开发：采用 Research-first 开发理念，确保技术方案基于最新 AI 研究成果

**适用场景**:
- 企业级 AI 开发团队：构建标准化、可控的 AI 编程辅助工作流
- 个人开发者：快速搭建个人 AI 助手环境，提升编程效率
- AI 产品集成：将项目作为基础框架，为自研 AI 编程产品添加高级能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,444 |
| 语言 | TypeScript |
| Forks | 14,951 |
| Issues | 705 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 开发与协作平台，拥有超过 7.5 万 Stars，支持多 AI 模型接入（OpenAI、Claude、DeepSeek、Gemini 等），提供开箱即用的 Chat 界面、知识库管理和 MCP 协议扩展能力，是构建企业级 AI 应用和探索多 Agent 协作的最佳起点。

**技术亮点**:
- 多模型统一接入层：无缝支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现 Agent 与外部工具、数据源的标准化连接，扩展性强
- 多 Agent 协作框架：支持设计和管理 Agent 团队，Agent 可作为工作交互的基本单元协同完成任务
- 完整的知识库系统：内置 RAG 能力，支持文档管理和向量检索，为 Agent 提供持久化记忆
- TypeScript 全栈架构：基于 React + Node.js 构建，提供完整的类型安全和现代化的开发体验

**适用场景**:
- 企业 AI 应用开发：快速构建智能客服、知识问答、业务助手等企业级 AI 解决方案
- 多 Agent 协作场景：构建复杂的工作流自动化，如研究分析、内容创作、数据处理等需要多个 AI 角色配合的任务
- 个人 AI 助手：作为个人工作空间，集成的 Chat、知识管理和 Agent 协作能力可以显著提升个人生产力



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,068 |
| 语言 | TypeScript |
| Forks | 5,481 |
| Issues | 123 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是 Claude Code 的革命性记忆插件，通过 AI 自动压缩编码会话历史并向未来会话注入相关上下文，解决了大模型无法跨会话保持记忆的核心痛点，配合 RAG 和 ChromaDB 向量检索实现智能上下文复用，大幅提升 AI 辅助编程的连续性和效率。

**技术亮点**:
- 基于 ChromaDB 的向量数据库实现语义相似性检索，支持精确回溯历史编码决策
- 集成 Claude Agent SDK 进行 AI 驱动的会话压缩，智能提取关键上下文信息
- 采用 RAG（检索增强生成）架构，将长期记忆无缝注入 AI 响应流程
- 使用 SQLite 本地存储元数据，轻量级且便于隐私保护
- 支持 embeddings 向量化表示，实现跨会话的语义级记忆关联

**适用场景**:
- 长期大型项目开发：跨多日/多周维护复杂的代码库，AI 可自动回忆之前的架构决策和技术选型
- 团队知识传承：开发者离开后，接手者可借助 AI 记忆快速理解历史上下文和编码规范
- 复杂调试场景：AI 可关联历史相似的 bug 修复经验，提供更精准的问题诊断建议
- 个人开发者效率提升：构建个人编码记忆库，让 AI 助手越用越懂你的编码风格和偏好



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,306 |
| 语言 | HTML |
| Forks | 20,976 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是 GitHub 上最受欢迎的提示词聚合项目之一，拥有 16 万+ Stars，支持 ChatGPT、Claude、Gemini 等多平台 LLM，既可开箱即用也可自托管满足企业隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，代码质量高且易于维护
- 支持多种主流 LLM 平台（ChatGPT、Claude-3、Gemini 等），统一提示词格式
- 完全开源支持自托管，企业可完全控制数据，满足隐私合规要求
- 社区驱动的提示词收集机制，持续更新高质量 prompt 资源
- 提示词分类清晰，支持搜索和收藏功能用户体验优秀

**适用场景**:
- 个人用户：发现、收藏和复用社区精选的高质量 AI 提示词，提升工作效率
- 企业场景：自托管部署私有提示词库，保护商业机密和用户隐私数据
- 开发者集成：将提示词 API 集成到自建 AI 应用中，快速具备 prompt 工程能力



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,187 |
| 语言 | Jupyter Notebook |
| Forks | 14,031 |
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
| Stars | 55,424 |
| 语言 | TypeScript |
| Forks | 9,130 |
| Issues | 102 |
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
| Stars | 47,142 |
| 语言 | HTML |
| Forks | 4,634 |
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
| Stars | 43,596 |
| 语言 | Python |
| Forks | 9,962 |
| Issues | 353 |
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
| Stars | 42,108 |
| 语言 | Python |
| Forks | 2,152 |
| Issues | 126 |
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
| Stars | 58,703 |
| 语言 | JavaScript |
| Forks | 6,349 |
| Issues | 336 |
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
| Stars | 71,649 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 411 |
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
| Stars | 53,235 |
| 语言 | TypeScript |
| Forks | 4,289 |
| Issues | 592 |
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
| Stars | 52,128 |
| 语言 | TypeScript |
| Forks | 24,184 |
| Issues | 816 |
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
| Stars | 77,582 |
| 语言 | Python |
| Forks | 15,904 |
| Issues | 4,371 |
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
| Stars | 147,220 |
| 语言 | Python |
| Forks | 8,816 |
| Issues | 959 |
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
| Stars | 55,402 |
| 语言 | Python |
| Forks | 5,945 |
| Issues | 542 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,629 |
| 语言 | Go |
| Forks | 15,721 |
| Issues | 3,018 |
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
| Stars | 47,987 |
| 语言 | Rust |
| Forks | 9,583 |
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
| Stars | 34,180 |
| 语言 | Python |
| Forks | 2,162 |
| Issues | 100 |
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
| Stars | 113,959 |
| 语言 | Python |
| Forks | 7,405 |
| Issues | 618 |
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
| Stars | 68,721 |
| 语言 | Python |
| Forks | 7,033 |
| Issues | 116 |
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
| Stars | 70,429 |
| 语言 | Python |
| Forks | 8,613 |
| Issues | 977 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个获得 ACL 2024 认可的大模型微调框架，提供统一的接口支持 100+ 大语言模型和多模态模型的高效微调，尤其适合资源有限的场景下快速定制化部署企业级 LLM 应用。

**技术亮点**:
- 统一微调框架：支持 Llama、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 和 VLMs，一套代码支持多种模型族
- 集成多种高效微调技术：LoRA、QLoRA、AdaLoRA、Prefix Tuning、Ptuning 等 PEFT 方法，支持 RLHF、DPO、ORPO 等对齐训练
- 深度优化训练效率：支持 FlashAttention-2、混合精度训练、DeepSpeed 加速，显著降低 GPU 显存占用
- 完善的数据处理流程：支持多格式数据集加载、自动模板构建、数据混合比例控制
- 便捷的训练监控与导出：集成 TensorBoard 监控、模型量化和导出为 Oaffinium 格式，部署流程简化

**适用场景**:
- 企业场景：企业可基于 LlamaFactory 快速将开源大模型微调至垂直领域（如金融、医疗、法律），实现私有化部署和成本控制
- 学术研究：研究人员可灵活实验各种 PEFT 方法、RLHF 流程和数据配比，快速验证假设并复现实验
- 个人开发者：个人开发者可利用 QLoRA 在消费级 GPU 上微调大模型，创建定制化聊天机器人或个人 AI 助手



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,266 |
| 语言 | Python |
| Forks | 6,607 |
| Issues | 73 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是当前最完整的开源金融数据平台之一，提供从股票、加密货币到期权、固收资产的统一数据接口，配合 AI Agent 支持，是金融分析师、量化交易员和数据科学家的首选工具。

**技术亮点**:
- 统一的数据抽象层，支持股票、加密货币、期权、固收、衍生品等多资产类别
- 内置 AI Agent 框架，支持自然语言查询金融数据，降低使用门槛
- 完整的量化金融工具链，包括技术分析、因子分析、风险管理等
- 模块化架构设计，支持扩展自定义数据源和分析模块
- 支持 Jupyter Notebook 集成，提供交互式金融分析体验

**适用场景**:
- 量化交易研究：获取多资产市场数据、进行因子分析、回测交易策略
- 金融数据分析：构建投资组合分析、固定收益定价、衍生品定价模型
- AI 金融应用开发：基于平台数据接口开发智能投顾、风险预测等 AI 应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,306 |
| 语言 | HTML |
| Forks | 20,976 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是 GitHub 上最受欢迎的提示词聚合项目之一，拥有 16 万+ Stars，支持 ChatGPT、Claude、Gemini 等多平台 LLM，既可开箱即用也可自托管满足企业隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，代码质量高且易于维护
- 支持多种主流 LLM 平台（ChatGPT、Claude-3、Gemini 等），统一提示词格式
- 完全开源支持自托管，企业可完全控制数据，满足隐私合规要求
- 社区驱动的提示词收集机制，持续更新高质量 prompt 资源
- 提示词分类清晰，支持搜索和收藏功能用户体验优秀

**适用场景**:
- 个人用户：发现、收藏和复用社区精选的高质量 AI 提示词，提升工作效率
- 企业场景：自托管部署私有提示词库，保护商业机密和用户隐私数据
- 开发者集成：将提示词 API 集成到自建 AI 应用中，快速具备 prompt 工程能力



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,187 |
| 语言 | Jupyter Notebook |
| Forks | 14,031 |
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
| Stars | 159,705 |
| 语言 | Python |
| Forks | 32,960 |
| Issues | 2,354 |
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
| Stars | 77,582 |
| 语言 | Python |
| Forks | 15,904 |
| Issues | 4,371 |
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
| Stars | 109,521 |
| 语言 | Python |
| Forks | 12,740 |
| Issues | 3,983 |
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
| Stars | 99,316 |
| 语言 | Python |
| Forks | 27,547 |
| Issues | 18,527 |
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
| Stars | 33,921 |
| 语言 | Jupyter Notebook |
| Forks | 5,611 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,886 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 293 |
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
| Stars | 163,040 |
| 语言 | JavaScript |
| Forks | 25,315 |
| Issues | 159 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等 AI 编程助手提供全面性能优化的开源系统，通过 Skills、Instincts、Memory 和 Security 模块显著提升 AI Agent 的开发效率和安全性，适合追求极致开发工作流优化的团队和个人。

**技术亮点**:
- 模块化 Agent 架构：提供 Skills、Instincts、Memory 三大核心模块，支持灵活扩展和定制 AI 行为模式
- 安全优先设计：内置 Security 模块确保 AI 操作的安全边界，防止越权和危险操作
- MCP 协议支持：深度集成 Model Context Protocol，实现与多种 AI 平台的无缝对接
- 性能优化系统：专门针对 AI Agent 执行效率进行优化，减少响应延迟和资源消耗
- 研究驱动开发：采用 Research-first 开发理念，确保技术方案基于最新 AI 研究成果

**适用场景**:
- 企业级 AI 开发团队：构建标准化、可控的 AI 编程辅助工作流
- 个人开发者：快速搭建个人 AI 助手环境，提升编程效率
- AI 产品集成：将项目作为基础框架，为自研 AI 编程产品添加高级能力



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,669 |
| 语言 | Go |
| Forks | 3,988 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源 AI 推理引擎，支持在无需 GPU 的消费级硬件上运行 LLM、图像生成、语音合成等多种模型，提供 OpenAI 兼容 API，是构建私有 AI 应用的理想选择。

**技术亮点**:
- 多模态统一推理：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、TTS 等多种模型
- 硬件无依赖：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- Go 语言开发：高性能、跨平台编译，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和去中心化部署场景

**适用场景**:
- 私有 AI 部署：企业或个人在本地/私有云部署 AI 服务，确保数据隐私安全
- 边缘计算场景：在资源受限的边缘设备上运行 AI 推理任务
- 开发测试环境：开发者本地快速构建和测试 AI 应用原型



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,649 |
| 语言 | Python |
| Forks | 9,020 |
| Issues | 411 |
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
| Stars | 53,235 |
| 语言 | TypeScript |
| Forks | 4,289 |
| Issues | 592 |
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
| Stars | 185,010 |
| 语言 | TypeScript |
| Forks | 57,008 |
| Issues | 1,543 |
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
| Stars | 157,996 |
| 语言 | Python |
| Forks | 13,046 |
| Issues | 2,467 |
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
| Stars | 97,487 |
| 语言 | Python |
| Forks | 9,111 |
| Issues | 168 |
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
| Stars | 81,680 |
| 语言 | Python |
| Forks | 9,499 |
| Issues | 258 |
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
| Stars | 184,096 |
| 语言 | TypeScript |
| Forks | 39,310 |
| Issues | 16,530 |
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
| Stars | 94,165 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 302 |
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
| Stars | 78,998 |
| 语言 | TypeScript |
| Forks | 5,821 |
| Issues | 769 |
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
| Stars | 79,690 |
| 语言 | Go |
| Forks | 2,787 |
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
| Stars | 76,808 |
| 语言 | Go |
| Forks | 2,775 |
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
| Stars | 43,962 |
| 语言 | Go |
| Forks | 8,300 |
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
| Stars | 75,581 |
| 语言 | JavaScript |
| Forks | 7,286 |
| Issues | 715 |
| Topics | api, fake, frontend, json, mock, rest, test |
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
| Stars | 53,235 |
| 语言 | TypeScript |
| Forks | 4,289 |
| Issues | 592 |
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
| Stars | 185,010 |
| 语言 | TypeScript |
| Forks | 57,008 |
| Issues | 1,543 |
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
| Stars | 55,402 |
| 语言 | Python |
| Forks | 5,945 |
| Issues | 542 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,656 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 228 |
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
| Stars | 121,828 |
| 语言 | Go |
| Forks | 42,891 |
| Issues | 2,797 |
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
| Stars | 71,504 |
| 语言 | Go |
| Forks | 18,919 |
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
| Stars | 55,017 |
| 语言 | Go |
| Forks | 6,602 |
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
| Stars | 47,523 |
| 语言 | Go |
| Forks | 5,048 |
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
| Stars | 94,165 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 302 |
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
| Stars | 77,342 |
| 语言 | TypeScript |
| Forks | 6,728 |
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
| Stars | 85,563 |
| 语言 | JavaScript |
| Forks | 7,669 |
| Issues | 725 |
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
| Stars | 69,970 |
| 语言 | Go |
| Forks | 1,921 |
| Issues | 323 |
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
| Stars | 62,805 |
| 语言 | Go |
| Forks | 5,931 |
| Issues | 767 |
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
| Stars | 59,053 |
| 语言 | Go |
| Forks | 4,290 |
| Issues | 27 |
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
| Stars | 85,563 |
| 语言 | JavaScript |
| Forks | 7,669 |
| Issues | 725 |
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
| Stars | 63,683 |
| 语言 | Go |
| Forks | 10,343 |
| Issues | 747 |
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
| Stars | 45,669 |
| 语言 | Go |
| Forks | 3,988 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源 AI 推理引擎，支持在无需 GPU 的消费级硬件上运行 LLM、图像生成、语音合成等多种模型，提供 OpenAI 兼容 API，是构建私有 AI 应用的理想选择。

**技术亮点**:
- 多模态统一推理：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频合成（MusicGen）、TTS 等多种模型
- 硬件无依赖：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零成本迁移
- Go 语言开发：高性能、跨平台编译，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和去中心化部署场景

**适用场景**:
- 私有 AI 部署：企业或个人在本地/私有云部署 AI 服务，确保数据隐私安全
- 边缘计算场景：在资源受限的边缘设备上运行 AI 推理任务
- 开发测试环境：开发者本地快速构建和测试 AI 应用原型



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,487 |
| 语言 | Python |
| Forks | 9,111 |
| Issues | 168 |
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
| Stars | 87,302 |
| 语言 | Python |
| Forks | 33,812 |
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
| Stars | 100,074 |
| 语言 | TypeScript |
| Forks | 27,177 |
| Issues | 1,116 |
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
| Stars | 78,998 |
| 语言 | TypeScript |
| Forks | 5,821 |
| Issues | 769 |
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
| Stars | 68,954 |
| 语言 | JavaScript |
| Forks | 23,158 |
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
| Stars | 55,956 |
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
| Stars | 51,812 |
| 语言 | JavaScript |
| Forks | 4,704 |
| Issues | 1,460 |
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
| Stars | 71,728 |
| 语言 | Go |
| Forks | 4,700 |
| Issues | 242 |
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
| Stars | 57,797 |
| 语言 | Go |
| Forks | 3,313 |
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
| Stars | 75,581 |
| 语言 | JavaScript |
| Forks | 7,286 |
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
| Stars | 88,364 |
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
| Stars | 101,218 |
| 语言 | TypeScript |
| Forks | 12,143 |
| Issues | 952 |
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
| Stars | 58,703 |
| 语言 | JavaScript |
| Forks | 6,349 |
| Issues | 336 |
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
| Stars | 43,897 |
| 语言 | Go |
| Forks | 3,969 |
| Issues | 1,131 |
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
| Stars | 51,656 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 228 |
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
| Stars | 160,306 |
| 语言 | HTML |
| Forks | 20,976 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是 GitHub 上最受欢迎的提示词聚合项目之一，拥有 16 万+ Stars，支持 ChatGPT、Claude、Gemini 等多平台 LLM，既可开箱即用也可自托管满足企业隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，代码质量高且易于维护
- 支持多种主流 LLM 平台（ChatGPT、Claude-3、Gemini 等），统一提示词格式
- 完全开源支持自托管，企业可完全控制数据，满足隐私合规要求
- 社区驱动的提示词收集机制，持续更新高质量 prompt 资源
- 提示词分类清晰，支持搜索和收藏功能用户体验优秀

**适用场景**:
- 个人用户：发现、收藏和复用社区精选的高质量 AI 提示词，提升工作效率
- 企业场景：自托管部署私有提示词库，保护商业机密和用户隐私数据
- 开发者集成：将提示词 API 集成到自建 AI 应用中，快速具备 prompt 工程能力



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,424 |
| 语言 | TypeScript |
| Forks | 9,130 |
| Issues | 102 |
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
| Stars | 42,108 |
| 语言 | Python |
| Forks | 2,152 |
| Issues | 126 |
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
| Stars | 39,278 |
| 语言 | Python |
| Forks | 4,676 |
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
| Stars | 89,765 |
| 语言 | TypeScript |
| Forks | 10,022 |
| Issues | 2,249 |
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
| Stars | 87,538 |
| 语言 | TypeScript |
| Forks | 8,890 |
| Issues | 1,622 |
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
| Stars | 127,523 |
| 语言 | JavaScript |
| Forks | 12,476 |
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
| Stars | 170,603 |
| 语言 | Go |
| Forks | 13,170 |
| Issues | 180 |
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
| Stars | 135,714 |
| 语言 | Unknown |
| Forks | 34,018 |
| Issues | 137 |
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
| Stars | 91,520 |
| 语言 | Python |
| Forks | 13,307 |
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
| Stars | 89,897 |
| 语言 | Python |
| Forks | 7,736 |
| Issues | 626 |
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
| Stars | 385,819 |
| 语言 | Python |
| Forks | 66,113 |
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
| Stars | 114,996 |
| 语言 | TypeScript |
| Forks | 5,973 |
| Issues | 66 |
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
| Stars | 112,353 |
| 语言 | TypeScript |
| Forks | 8,204 |
| Issues | 286 |
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
| Stars | 79,440 |
| 语言 | TypeScript |
| Forks | 11,441 |
| Issues | 384 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,754 |
| 语言 | JavaScript |
| Forks | 4,714 |
| Issues | 27 |
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
| Stars | 48,186 |
| 语言 | Go |
| Forks | 10,293 |
| Issues | 1,889 |
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
| Stars | 105,529 |
| 语言 | C++ |
| Forks | 17,177 |
| Issues | 1,548 |
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
| Stars | 63,440 |
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
| Stars | 71,547 |
| 语言 | Unknown |
| Forks | 6,519 |
| Issues | 65 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 293,645 |
| 语言 | Python |
| Forks | 27,727 |
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
| Stars | 219,999 |
| 语言 | Python |
| Forks | 50,376 |
| Issues | 930 |
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
| Stars | 98,153 |
| 语言 | Python |
| Forks | 12,072 |
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
| Stars | 86,186 |
| 语言 | Python |
| Forks | 7,225 |
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
| Stars | 86,144 |
| 语言 | Python |
| Forks | 37,292 |
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
| Stars | 77,669 |
| 语言 | Python |
| Forks | 45,131 |
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
| Stars | 77,074 |
| 语言 | Python |
| Forks | 16,864 |
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
| Stars | 443,317 |
| 语言 | TypeScript |
| Forks | 44,357 |
| Issues | 188 |
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
| Stars | 353,329 |
| 语言 | TypeScript |
| Forks | 43,953 |
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
| Stars | 121,645 |
| 语言 | TypeScript |
| Forks | 13,376 |
| Issues | 3,006 |
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
| Stars | 112,748 |
| 语言 | TypeScript |
| Forks | 8,605 |
| Issues | 1,828 |
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
| Stars | 108,613 |
| 语言 | TypeScript |
| Forks | 13,358 |
| Issues | 5,022 |
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
| Stars | 98,318 |
| 语言 | TypeScript |
| Forks | 5,438 |
| Issues | 689 |
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
| Stars | 97,834 |
| 语言 | TypeScript |
| Forks | 54,597 |
| Issues | 1,365 |
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
| Stars | 94,673 |
| 语言 | TypeScript |
| Forks | 5,206 |
| Issues | 112 |
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
| Stars | 84,238 |
| 语言 | TypeScript |
| Forks | 10,459 |
| Issues | 355 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,216 |
| 语言 | TypeScript |
| Forks | 7,595 |
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
| Stars | 80,069 |
| 语言 | TypeScript |
| Forks | 8,078 |
| Issues | 714 |
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
| Stars | 244,635 |
| 语言 | JavaScript |
| Forks | 50,966 |
| Issues | 1,236 |
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
| Stars | 148,133 |
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
| Stars | 116,858 |
| 语言 | JavaScript |
| Forks | 35,409 |
| Issues | 2,639 |
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
| Stars | 112,107 |
| 语言 | JavaScript |
| Forks | 36,331 |
| Issues | 532 |
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
| Stars | 109,037 |
| 语言 | JavaScript |
| Forks | 11,645 |
| Issues | 273 |
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
| Stars | 98,198 |
| 语言 | JavaScript |
| Forks | 32,671 |
| Issues | 1,541 |
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
| Stars | 95,641 |
| 语言 | JavaScript |
| Forks | 15,380 |
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
| Stars | 86,379 |
| 语言 | JavaScript |
| Forks | 4,895 |
| Issues | 990 |
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
| Stars | 71,047 |
| 语言 | JavaScript |
| Forks | 16,808 |
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
| Stars | 67,372 |
| 语言 | JavaScript |
| Forks | 11,955 |
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
| Stars | 65,812 |
| 语言 | JavaScript |
| Forks | 9,363 |
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
| Stars | 62,906 |
| 语言 | JavaScript |
| Forks | 4,019 |
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
| Stars | 60,595 |
| 语言 | JavaScript |
| Forks | 5,654 |
| Issues | 64 |
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
| Stars | 59,832 |
| 语言 | JavaScript |
| Forks | 20,464 |
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
| Stars | 57,426 |
| 语言 | JavaScript |
| Forks | 12,302 |
| Issues | 23 |
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
| Stars | 53,161 |
| 语言 | JavaScript |
| Forks | 10,604 |
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
| Stars | 52,596 |
| 语言 | JavaScript |
| Forks | 11,485 |
| Issues | 244 |
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
| Stars | 133,570 |
| 语言 | Go |
| Forks | 18,942 |
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
| Stars | 87,711 |
| 语言 | Go |
| Forks | 8,238 |
| Issues | 249 |
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
| Stars | 82,620 |
| 语言 | Go |
| Forks | 5,068 |
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
| Stars | 68,613 |
| 语言 | Go |
| Forks | 3,219 |
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
| Stars | 56,776 |
| 语言 | Go |
| Forks | 5,050 |
| Issues | 1,172 |
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
| Stars | 50,994 |
| 语言 | Go |
| Forks | 21,890 |
| Issues | 406 |
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
| Stars | 50,739 |
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
| Stars | 49,331 |
| 语言 | Go |
| Forks | 7,949 |
| Issues | 561 |
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
| Stars | 46,037 |
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
| Stars | 84,705 |
| 语言 | Shell |
| Forks | 13,516 |
| Issues | 105 |
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
| Stars | 138,951 |
| 语言 | TypeScript |
| Forks | 16,515 |
| Issues | 47 |
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
| Stars | 79,118 |
| 语言 | JavaScript |
| Forks | 32,604 |
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
| Stars | 66,333 |
| 语言 | JavaScript |
| Forks | 9,191 |
| Issues | 2 |
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
| Stars | 61,304 |
| 语言 | JavaScript |
| Forks | 7,142 |
| Issues | 143 |
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
| Stars | 106,065 |
| 语言 | Go |
| Forks | 15,006 |
| Issues | 39 |
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
| Stars | 152,314 |
| 语言 | Python |
| Forks | 11,595 |
| Issues | 333 |
| Topics | awesome, github, hellogithub, python |
