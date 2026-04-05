# 项目发现报告 (2026-04-05)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 10 |
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


## 🤖 AI Agents (28 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 130,169 |
| 语言 | Python |
| Forks | 18,437 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，13万+ Stars 证明了其成熟度和社区认可度，是快速部署自托管 AI 助手的最佳选择之一。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现灵活部署
- RAG 支持：内置检索增强生成能力，提升问答质量
- MCP 协议集成：支持 Model Context Protocol，增强模型上下文处理能力
- OpenAPI 兼容：提供标准化 API 接口，便于二次开发和系统集成
- 自托管部署：支持完全私有化部署，保障数据安全和隐私

**适用场景**:
- 企业内部 AI 助手：部署私有化 LLM 界面供团队使用，处理文档问答、知识库检索等场景
- 个人开发者本地开发：配合 Ollama 本地运行，降低 AI 应用开发成本和延迟
- AI 应用快速原型：利用现有 UI 和 API 快速构建 AI 产品演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,177 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 3,207 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的国产开源 RAG 项目之一（77k+ Stars），将深度文档理解与 Agent 能力完美融合，为企业级知识库问答提供了端到端的解决方案，通过可视化流程编排和多种 Agent 模板大幅降低了构建智能问答系统的门槛。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式复杂文档的智能解析，能处理表格、图表、公式等富文本内容，实现精准的内容切片和语义理解
- GraphRAG + Agent 双轨架构：创新性地将知识图谱增强检索与多类型 Agent（DeepResearch、CodeInterpreter、ConstitutionalCritic 等）结合，支持复杂的推理和多跳问答场景
- 可视化 RAG 流程编排：提供直观的拖拽式工作流设计器，开发者可以灵活组合重排序、意图识别、意图分类、生成等模块
- 多模型灵活接入：原生支持 OpenAI、DeepSeek、通义千问、Ollama 等主流 LLM 接口，兼容 MCP 协议，具备良好的扩展性
- 企业级生产就绪：提供完整的权限管理、日志审计、多租户支持，配套 Web UI 和 API 服务，开箱即用

**适用场景**:
- 企业知识库智能问答：构建内部文档助手、政策查询系统、客服机器人，支持复杂表格和多文档关联查询
- 深度研究分析场景：利用 DeepResearch Agent 进行多源信息检索、对比分析和报告生成，适合投研、咨询、法务等领域
- 代码助手与数据分析：CodeInterpreter Agent 支持自然语言驱动的数据分析、代码生成与调试



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,490 |
| 语言 | TypeScript |
| Forks | 6,830 |
| Issues | 253 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 时代打造的网页数据抓取工具，能够将复杂 HTML 高效转换为干净的 Markdown 格式，特别适合为 LLM 和 AI agents 提供高质量的输入数据，在 10 万+ Stars 的社区验证下，已成为 AI 数据管道建设的首选方案。

**技术亮点**:
- AI-Ready 数据输出：核心能力是将网页内容转换为结构化 Markdown，天然适配 LLM 的训练和推理需求
- 全栈内容提取：支持提取正文、标题、元数据、图像描述等完整页面信息，输出格式统一规范
- 智能容错机制：内置错误处理和降级策略，即使部分内容解析失败也能返回可用数据
- TypeScript 原生开发：提供完整的类型定义和 IDE 支持，便于与现有 TypeScript/JavaScript 项目集成

**适用场景**:
- RAG/LLM 应用数据准备：为检索增强生成系统抓取和预处理网页内容，构建高质量知识库
- AI 产品数据管道：为 AI agents 和智能搜索应用搭建可靠的数据采集和格式化层



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 140,135 |
| 语言 | JavaScript |
| Forks | 21,049 |
| Issues | 115 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专为 AI 编程代理打造的性能优化系统框架，支持 Claude Code、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 架构显著提升 AI Agent 的任务执行效率和稳定性。

**技术亮点**:
- 模块化 Agent Harness 架构：提供可扩展的性能优化框架，支持多种 AI 编程工具的标准化集成
- 创新的 Skills 与 Instincts 双系统：Skills 定义可执行能力，Instincts 实现上下文感知响应机制
- Memory 记忆管理系统：实现长期上下文保持和跨会话知识复用，解决 LLM 上下文窗口限制
- Security-First 设计理念：内置安全审计机制，确保 AI Agent 操作的可控性和合规性
- Research-First 开发范式：融合研究导向的方法论，提供可观测性和调试能力

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该框架构建统一的 AI 编程规范和安全策略，提升开发效率
- AI Agent 性能优化：开发者可利用其 Skill/Instinct 机制快速提升 AI 编程工具的任务完成率
- 跨工具集成开发：为需要在多个 AI 编程工具间切换的开发者提供一致性体验



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,917 |
| 语言 | Go |
| Forks | 3,861 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，完全兼容 OpenAI API 格式，无需 GPU 即可部署，大大降低了 AI 应用的成本和门槛，特别适合隐私敏感或需要私有化部署的场景。

**技术亮点**:
- 多模型支持：涵盖文本生成（llama/mamba）、图像生成（stable-diffusion）、音频处理（musicgen/tts）、目标检测等多种模型类型
- Go 语言实现：高性能、低内存占用的架构设计，支持在资源受限环境下高效运行
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有的 AI 应用可以零成本迁移到本地部署
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化推理网络
- 零 GPU 依赖：可在 CPU 环境下运行多种模型，大幅降低部署成本

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下部署内部 AI 助手、客服机器人或文档分析系统，数据完全留在本地
- 隐私敏感场景：医疗、金融、法律等领域需要在本地处理敏感数据，避免数据外传
- 边缘计算与物联网：将 AI 能力部署到边缘设备，实现实时推理如智能监控、语音交互、异常检测等



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,768 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的现代化 AI Agent 协作平台，提供多 Agent 协作、Agent 团队编排和 MCP 协议支持，同时支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，74k+ Stars 验证了其极高的社区认可度和成熟度，是构建智能工作流的优秀选择。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一接口层便于切换和对比不同模型效果
- MCP (Model Context Protocol) 协议支持：遵循 Anthropic 提出的 MCP 标准，实现标准化的 Agent 与外部工具/数据源连接
- 多 Agent 协作系统：支持构建 Agent 团队，实现 Agent 间的任务分解、协作和状态共享，提供 Agent as the unit of work 的设计理念
- TypeScript + 现代化架构：全栈 TypeScript 开发，提供完整的类型安全和 IDE 支持，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库管理功能，支持基于私有数据的 Agent 问答和检索增强生成

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 团队处理复杂业务场景，如客户服务、数据分析、文档处理等需要多步骤协作的任务
- 个人 AI 助手与知识管理：搭建个人专属的 AI 助手，整合私有知识库实现智能问答、内容生成和信息检索
- AI 应用快速原型开发：利用现成的 Agent 框架和 MCP 生态快速验证 AI 产品想法，无需从零构建基础设施



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,555 |
| 语言 | Python |
| Forks | 8,467 |
| Issues | 947 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 认证的统一高效微调框架，支持 100+ 主流大语言模型和视觉语言模型，通过集成 LoRA、QLoRA、RLHF 等前沿技术大幅降低 LLM 微调门槛，是 LLM 微调领域最受欢迎的开源项目之一。

**技术亮点**:
- 🏆 ACL 2024 认证：顶级学术会议官方认可的技术方案，具有权威性和前沿性
- 🔧 统一微调框架：支持 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等 100+ 主流模型
- ⚡ 高效微调技术：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低显存占用
- 🎯 多训练范式：支持监督微调(SFT)、RLHF、DPO、ORPO 等多种训练范式
- 🔄 模型压缩支持：内置量化技术，支持 INT4/INT8 量化推理，适配边缘部署场景

**适用场景**:
- 🏢 企业级 AI 应用：企业定制私有化大模型，如客服机器人、知识库问答、业务数据分析等场景
- 🔬 学术研究：研究人员快速验证新模型架构和训练方法，降低实验成本
- 💡 个人开发者：开发者基于开源模型构建 AI 原生应用，如智能助手、内容生成工具等



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,583 |
| 语言 | TypeScript |
| Forks | 7,840 |
| Issues | 46 |
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
| Stars | 45,505 |
| 语言 | TypeScript |
| Forks | 3,456 |
| Issues | 250 |
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
| Stars | 42,779 |
| 语言 | Python |
| Forks | 9,867 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,735 |
| 语言 | Java |
| Forks | 15,878 |
| Issues | 35 |
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
| Stars | 38,909 |
| 语言 | Python |
| Forks | 6,178 |
| Issues | 99 |
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
| Stars | 33,752 |
| 语言 | Python |
| Forks | 3,884 |
| Issues | 81 |
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
| Stars | 104,540 |
| 语言 | Python |
| Forks | 15,260 |
| Issues | 14 |
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
| Stars | 57,705 |
| 语言 | JavaScript |
| Forks | 6,235 |
| Issues | 303 |
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
| Stars | 70,626 |
| 语言 | Python |
| Forks | 8,850 |
| Issues | 368 |
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
| Stars | 48,522 |
| 语言 | TypeScript |
| Forks | 3,808 |
| Issues | 421 |
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
| Stars | 86,118 |
| 语言 | Python |
| Forks | 9,958 |
| Issues | 231 |
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
| Stars | 51,574 |
| 语言 | TypeScript |
| Forks | 24,071 |
| Issues | 822 |
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
| Stars | 182,575 |
| 语言 | TypeScript |
| Forks | 56,504 |
| Issues | 1,481 |
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
| Stars | 154,663 |
| 语言 | Java |
| Forks | 46,136 |
| Issues | 70 |
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
| Stars | 146,593 |
| 语言 | Python |
| Forks | 8,700 |
| Issues | 956 |
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
| Stars | 72,857 |
| 语言 | MDX |
| Forks | 7,824 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,889 |
| 语言 | Python |
| Forks | 2,114 |
| Issues | 94 |
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
| Stars | 33,638 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 285 |
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
| Stars | 33,193 |
| 语言 | Jupyter Notebook |
| Forks | 5,488 |
| Issues | 125 |
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
| Stars | 39,273 |
| 语言 | Rust |
| Forks | 2,458 |
| Issues | 448 |
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
| Stars | 55,968 |
| 语言 | Jupyter Notebook |
| Forks | 19,349 |
| Issues | 23 |
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
| Stars | 130,169 |
| 语言 | Python |
| Forks | 18,437 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，13万+ Stars 证明了其成熟度和社区认可度，是快速部署自托管 AI 助手的最佳选择之一。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现灵活部署
- RAG 支持：内置检索增强生成能力，提升问答质量
- MCP 协议集成：支持 Model Context Protocol，增强模型上下文处理能力
- OpenAPI 兼容：提供标准化 API 接口，便于二次开发和系统集成
- 自托管部署：支持完全私有化部署，保障数据安全和隐私

**适用场景**:
- 企业内部 AI 助手：部署私有化 LLM 界面供团队使用，处理文档问答、知识库检索等场景
- 个人开发者本地开发：配合 Ollama 本地运行，降低 AI 应用开发成本和延迟
- AI 应用快速原型：利用现有 UI 和 API 快速构建 AI 产品演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,177 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 3,207 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的国产开源 RAG 项目之一（77k+ Stars），将深度文档理解与 Agent 能力完美融合，为企业级知识库问答提供了端到端的解决方案，通过可视化流程编排和多种 Agent 模板大幅降低了构建智能问答系统的门槛。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式复杂文档的智能解析，能处理表格、图表、公式等富文本内容，实现精准的内容切片和语义理解
- GraphRAG + Agent 双轨架构：创新性地将知识图谱增强检索与多类型 Agent（DeepResearch、CodeInterpreter、ConstitutionalCritic 等）结合，支持复杂的推理和多跳问答场景
- 可视化 RAG 流程编排：提供直观的拖拽式工作流设计器，开发者可以灵活组合重排序、意图识别、意图分类、生成等模块
- 多模型灵活接入：原生支持 OpenAI、DeepSeek、通义千问、Ollama 等主流 LLM 接口，兼容 MCP 协议，具备良好的扩展性
- 企业级生产就绪：提供完整的权限管理、日志审计、多租户支持，配套 Web UI 和 API 服务，开箱即用

**适用场景**:
- 企业知识库智能问答：构建内部文档助手、政策查询系统、客服机器人，支持复杂表格和多文档关联查询
- 深度研究分析场景：利用 DeepResearch Agent 进行多源信息检索、对比分析和报告生成，适合投研、咨询、法务等领域
- 代码助手与数据分析：CodeInterpreter Agent 支持自然语言驱动的数据分析、代码生成与调试



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,768 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的现代化 AI Agent 协作平台，提供多 Agent 协作、Agent 团队编排和 MCP 协议支持，同时支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，74k+ Stars 验证了其极高的社区认可度和成熟度，是构建智能工作流的优秀选择。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一接口层便于切换和对比不同模型效果
- MCP (Model Context Protocol) 协议支持：遵循 Anthropic 提出的 MCP 标准，实现标准化的 Agent 与外部工具/数据源连接
- 多 Agent 协作系统：支持构建 Agent 团队，实现 Agent 间的任务分解、协作和状态共享，提供 Agent as the unit of work 的设计理念
- TypeScript + 现代化架构：全栈 TypeScript 开发，提供完整的类型安全和 IDE 支持，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库管理功能，支持基于私有数据的 Agent 问答和检索增强生成

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 团队处理复杂业务场景，如客户服务、数据分析、文档处理等需要多步骤协作的任务
- 个人 AI 助手与知识管理：搭建个人专属的 AI 助手，整合私有知识库实现智能问答、内容生成和信息检索
- AI 应用快速原型开发：利用现成的 Agent 框架和 MCP 生态快速验证 AI 产品想法，无需从零构建基础设施



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,505 |
| 语言 | TypeScript |
| Forks | 3,456 |
| Issues | 250 |
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
| Stars | 45,735 |
| 语言 | Java |
| Forks | 15,878 |
| Issues | 35 |
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
| Stars | 38,909 |
| 语言 | Python |
| Forks | 6,178 |
| Issues | 99 |
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
| Stars | 33,752 |
| 语言 | Python |
| Forks | 3,884 |
| Issues | 81 |
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
| Stars | 104,540 |
| 语言 | Python |
| Forks | 15,260 |
| Issues | 14 |
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
| Stars | 100,290 |
| 语言 | TypeScript |
| Forks | 11,986 |
| Issues | 970 |
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
| Stars | 57,705 |
| 语言 | JavaScript |
| Forks | 6,235 |
| Issues | 303 |
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
| Stars | 74,932 |
| 语言 | Python |
| Forks | 10,181 |
| Issues | 256 |
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
| Stars | 51,574 |
| 语言 | TypeScript |
| Forks | 24,071 |
| Issues | 822 |
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
| Stars | 43,609 |
| 语言 | Go |
| Forks | 3,934 |
| Issues | 1,102 |
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
| Stars | 72,857 |
| 语言 | MDX |
| Forks | 7,824 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,889 |
| 语言 | Python |
| Forks | 2,114 |
| Issues | 94 |
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
| Stars | 33,638 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 285 |
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
| Stars | 33,193 |
| 语言 | Jupyter Notebook |
| Forks | 5,488 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
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
| Stars | 130,169 |
| 语言 | Python |
| Forks | 18,437 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，13万+ Stars 证明了其成熟度和社区认可度，是快速部署自托管 AI 助手的最佳选择之一。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现灵活部署
- RAG 支持：内置检索增强生成能力，提升问答质量
- MCP 协议集成：支持 Model Context Protocol，增强模型上下文处理能力
- OpenAPI 兼容：提供标准化 API 接口，便于二次开发和系统集成
- 自托管部署：支持完全私有化部署，保障数据安全和隐私

**适用场景**:
- 企业内部 AI 助手：部署私有化 LLM 界面供团队使用，处理文档问答、知识库检索等场景
- 个人开发者本地开发：配合 Ollama 本地运行，降低 AI 应用开发成本和延迟
- AI 应用快速原型：利用现有 UI 和 API 快速构建 AI 产品演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,177 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 3,207 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的国产开源 RAG 项目之一（77k+ Stars），将深度文档理解与 Agent 能力完美融合，为企业级知识库问答提供了端到端的解决方案，通过可视化流程编排和多种 Agent 模板大幅降低了构建智能问答系统的门槛。

**技术亮点**:
- 深度文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式复杂文档的智能解析，能处理表格、图表、公式等富文本内容，实现精准的内容切片和语义理解
- GraphRAG + Agent 双轨架构：创新性地将知识图谱增强检索与多类型 Agent（DeepResearch、CodeInterpreter、ConstitutionalCritic 等）结合，支持复杂的推理和多跳问答场景
- 可视化 RAG 流程编排：提供直观的拖拽式工作流设计器，开发者可以灵活组合重排序、意图识别、意图分类、生成等模块
- 多模型灵活接入：原生支持 OpenAI、DeepSeek、通义千问、Ollama 等主流 LLM 接口，兼容 MCP 协议，具备良好的扩展性
- 企业级生产就绪：提供完整的权限管理、日志审计、多租户支持，配套 Web UI 和 API 服务，开箱即用

**适用场景**:
- 企业知识库智能问答：构建内部文档助手、政策查询系统、客服机器人，支持复杂表格和多文档关联查询
- 深度研究分析场景：利用 DeepResearch Agent 进行多源信息检索、对比分析和报告生成，适合投研、咨询、法务等领域
- 代码助手与数据分析：CodeInterpreter Agent 支持自然语言驱动的数据分析、代码生成与调试



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 140,135 |
| 语言 | JavaScript |
| Forks | 21,049 |
| Issues | 115 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专为 AI 编程代理打造的性能优化系统框架，支持 Claude Code、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 架构显著提升 AI Agent 的任务执行效率和稳定性。

**技术亮点**:
- 模块化 Agent Harness 架构：提供可扩展的性能优化框架，支持多种 AI 编程工具的标准化集成
- 创新的 Skills 与 Instincts 双系统：Skills 定义可执行能力，Instincts 实现上下文感知响应机制
- Memory 记忆管理系统：实现长期上下文保持和跨会话知识复用，解决 LLM 上下文窗口限制
- Security-First 设计理念：内置安全审计机制，确保 AI Agent 操作的可控性和合规性
- Research-First 开发范式：融合研究导向的方法论，提供可观测性和调试能力

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该框架构建统一的 AI 编程规范和安全策略，提升开发效率
- AI Agent 性能优化：开发者可利用其 Skill/Instinct 机制快速提升 AI 编程工具的任务完成率
- 跨工具集成开发：为需要在多个 AI 编程工具间切换的开发者提供一致性体验



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,768 |
| 语言 | TypeScript |
| Forks | 14,863 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的现代化 AI Agent 协作平台，提供多 Agent 协作、Agent 团队编排和 MCP 协议支持，同时支持 OpenAI、Claude、DeepSeek、Gemini 等主流大模型，74k+ Stars 验证了其极高的社区认可度和成熟度，是构建智能工作流的优秀选择。

**技术亮点**:
- 多模型统一集成框架：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一接口层便于切换和对比不同模型效果
- MCP (Model Context Protocol) 协议支持：遵循 Anthropic 提出的 MCP 标准，实现标准化的 Agent 与外部工具/数据源连接
- 多 Agent 协作系统：支持构建 Agent 团队，实现 Agent 间的任务分解、协作和状态共享，提供 Agent as the unit of work 的设计理念
- TypeScript + 现代化架构：全栈 TypeScript 开发，提供完整的类型安全和 IDE 支持，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库管理功能，支持基于私有数据的 Agent 问答和检索增强生成

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 团队处理复杂业务场景，如客户服务、数据分析、文档处理等需要多步骤协作的任务
- 个人 AI 助手与知识管理：搭建个人专属的 AI 助手，整合私有知识库实现智能问答、内容生成和信息检索
- AI 应用快速原型开发：利用现成的 Agent 框架和 MCP 生态快速验证 AI 产品想法，无需从零构建基础设施



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,541 |
| 语言 | HTML |
| Forks | 20,631 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是全球最大的开源提示词社区之一，前身是著名的 Awesome ChatGPT Prompts 项目，拥有超过 15 万星标，支持自托管部署，既能享受社区共享的丰富提示词资源，又能满足企业级隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持多种主流 LLM 模型（ChatGPT、Claude、Gemini、GPT-4）
- 完全开源且支持自托管部署，确保数据隐私安全
- Creative Commons Zero v1.0 Universal 许可证，商业使用零限制
- 活跃的社区贡献机制，持续更新高质量提示词资源

**适用场景**:
- 个人用户寻找和收藏高质量 AI 提示词，提升与 AI 助手的交互效率
- 企业自建提示词管理系统，保护内部数据隐私的同时共享团队知识
- 开发者学习提示词工程技巧，参考开源项目的最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,038 |
| 语言 | Jupyter Notebook |
| Forks | 13,781 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是学习大语言模型内部工作原理的最佳实践项目，通过 Jupyter Notebook 逐步演示如何从零实现 ChatGPT 级别的 LLM，无需依赖 Hugging Face 等高层封装库，帮助开发者真正理解 GPT/Transformer 的底层机制，而非仅仅学会调用 API。

**技术亮点**:
- 纯 PyTorch 从零实现：手写注意力机制、前馈网络、位置编码等核心组件，不依赖任何高级封装库
- 完整的 GPT 架构实现：涵盖 Tokenizer、Embedding、Multi-Head Self-Attention、LayerNorm、Dropout 等完整流程
- 预训练与微调全流程：包含语言建模任务训练、指令微调、RLHF 等关键阶段
- 渐进式教学设计：每个 Notebook 聚焦单一概念，从基础到复杂逐步构建完整 LLM
- 详细的数学原理与代码对照：每个实现都配合直观的数学公式解释和可视化分析

**适用场景**:
- AI/ML 教育与培训：企业或院校用于培训工程师/学生理解 LLM 内部原理，是系统性学习生成式 AI 的最佳教材
- 个人深度学习研究者：用于实验新架构变体、微调策略或研究 LLM 可解释性
- 全栈 AI 开发者：理解底层机制后，能更有效地使用 LangChain、HuggingFace 等工具进行应用开发



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,583 |
| 语言 | TypeScript |
| Forks | 7,840 |
| Issues | 46 |
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
| Stars | 45,505 |
| 语言 | TypeScript |
| Forks | 3,456 |
| Issues | 250 |
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
| Stars | 42,779 |
| 语言 | Python |
| Forks | 9,867 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,692 |
| 语言 | Python |
| Forks | 2,900 |
| Issues | 167 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,705 |
| 语言 | JavaScript |
| Forks | 6,235 |
| Issues | 303 |
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
| Stars | 70,626 |
| 语言 | Python |
| Forks | 8,850 |
| Issues | 368 |
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
| Stars | 48,522 |
| 语言 | TypeScript |
| Forks | 3,808 |
| Issues | 421 |
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
| Stars | 51,574 |
| 语言 | TypeScript |
| Forks | 24,071 |
| Issues | 822 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,421 |
| 语言 | Unknown |
| Forks | 6,174 |
| Issues | 19 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,355 |
| 语言 | Python |
| Forks | 15,195 |
| Issues | 4,112 |
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
| Stars | 58,843 |
| 语言 | Python |
| Forks | 5,817 |
| Issues | 75 |
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
| Stars | 39,280 |
| 语言 | TypeScript |
| Forks | 4,006 |
| Issues | 1,094 |
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
| Stars | 146,593 |
| 语言 | Python |
| Forks | 8,700 |
| Issues | 956 |
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
| Stars | 167,284 |
| 语言 | Go |
| Forks | 15,347 |
| Issues | 2,864 |
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
| Stars | 72,857 |
| 语言 | MDX |
| Forks | 7,824 |
| Issues | 256 |
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
| Stars | 47,567 |
| 语言 | Rust |
| Forks | 9,460 |
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
| Stars | 33,889 |
| 语言 | Python |
| Forks | 2,114 |
| Issues | 94 |
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
| Stars | 93,338 |
| 语言 | Python |
| Forks | 5,630 |
| Issues | 507 |
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
| Stars | 37,105 |
| 语言 | Python |
| Forks | 2,584 |
| Issues | 65 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


## 🧠 机器学习框架 (11 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,555 |
| 语言 | Python |
| Forks | 8,467 |
| Issues | 947 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 认证的统一高效微调框架，支持 100+ 主流大语言模型和视觉语言模型，通过集成 LoRA、QLoRA、RLHF 等前沿技术大幅降低 LLM 微调门槛，是 LLM 微调领域最受欢迎的开源项目之一。

**技术亮点**:
- 🏆 ACL 2024 认证：顶级学术会议官方认可的技术方案，具有权威性和前沿性
- 🔧 统一微调框架：支持 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等 100+ 主流模型
- ⚡ 高效微调技术：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低显存占用
- 🎯 多训练范式：支持监督微调(SFT)、RLHF、DPO、ORPO 等多种训练范式
- 🔄 模型压缩支持：内置量化技术，支持 INT4/INT8 量化推理，适配边缘部署场景

**适用场景**:
- 🏢 企业级 AI 应用：企业定制私有化大模型，如客服机器人、知识库问答、业务数据分析等场景
- 🔬 学术研究：研究人员快速验证新模型架构和训练方法，降低实验成本
- 💡 个人开发者：开发者基于开源模型构建 AI 原生应用，如智能助手、内容生成工具等



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,411 |
| 语言 | Python |
| Forks | 6,477 |
| Issues | 73 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有 65k+ Stars，为分析师、量化交易员和 AI 代理提供统一的数据访问接口，大幅降低了金融数据分析的技术门槛，是构建智能投研系统和量化交易平台的理想基础。

**技术亮点**:
- 多数据源统一 API：聚合多个金融数据提供商，提供标准化数据访问接口，支持股票、期权、加密货币、债券、外汇等多资产类别
- AI/ML 原生集成：专门设计了 AI Agent 接口，支持与大语言模型集成，可构建智能投研助手和对话式数据分析系统
- 完整的量化分析工具链：内置技术指标、因子分析、回测框架等量化交易常用功能，开箱即用
- 模块化架构设计：采用插件化架构，用户可灵活扩展自定义数据源和分析模块
- 丰富的可视化能力：集成交互式图表和仪表盘功能，支持专业级金融数据可视化展示

**适用场景**:
- 量化研究与策略开发：quant 研究员可利用平台进行数据获取、因子构建、策略回测的完整工作流
- 智能投研与 AI 助手：开发团队可基于 OpenBB 构建金融对话机器人或智能投研助手
- 企业级金融分析平台：投资机构可基于此开源项目快速搭建内部研究分析系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,541 |
| 语言 | HTML |
| Forks | 20,631 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是全球最大的开源提示词社区之一，前身是著名的 Awesome ChatGPT Prompts 项目，拥有超过 15 万星标，支持自托管部署，既能享受社区共享的丰富提示词资源，又能满足企业级隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持多种主流 LLM 模型（ChatGPT、Claude、Gemini、GPT-4）
- 完全开源且支持自托管部署，确保数据隐私安全
- Creative Commons Zero v1.0 Universal 许可证，商业使用零限制
- 活跃的社区贡献机制，持续更新高质量提示词资源

**适用场景**:
- 个人用户寻找和收藏高质量 AI 提示词，提升与 AI 助手的交互效率
- 企业自建提示词管理系统，保护内部数据隐私的同时共享团队知识
- 开发者学习提示词工程技巧，参考开源项目的最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,038 |
| 语言 | Jupyter Notebook |
| Forks | 13,781 |
| Issues | 2 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是学习大语言模型内部工作原理的最佳实践项目，通过 Jupyter Notebook 逐步演示如何从零实现 ChatGPT 级别的 LLM，无需依赖 Hugging Face 等高层封装库，帮助开发者真正理解 GPT/Transformer 的底层机制，而非仅仅学会调用 API。

**技术亮点**:
- 纯 PyTorch 从零实现：手写注意力机制、前馈网络、位置编码等核心组件，不依赖任何高级封装库
- 完整的 GPT 架构实现：涵盖 Tokenizer、Embedding、Multi-Head Self-Attention、LayerNorm、Dropout 等完整流程
- 预训练与微调全流程：包含语言建模任务训练、指令微调、RLHF 等关键阶段
- 渐进式教学设计：每个 Notebook 聚焦单一概念，从基础到复杂逐步构建完整 LLM
- 详细的数学原理与代码对照：每个实现都配合直观的数学公式解释和可视化分析

**适用场景**:
- AI/ML 教育与培训：企业或院校用于培训工程师/学生理解 LLM 内部原理，是系统性学习生成式 AI 的最佳教材
- 个人深度学习研究者：用于实验新架构变体、微调策略或研究 LLM 可解释性
- 全栈 AI 开发者：理解底层机制后，能更有效地使用 LangChain、HuggingFace 等工具进行应用开发



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,840 |
| 语言 | Python |
| Forks | 32,740 |
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
| Stars | 75,355 |
| 语言 | Python |
| Forks | 15,195 |
| Issues | 4,112 |
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
| Stars | 107,848 |
| 语言 | Python |
| Forks | 12,476 |
| Issues | 3,931 |
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
| Stars | 98,813 |
| 语言 | Python |
| Forks | 27,404 |
| Issues | 18,236 |
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
| Stars | 72,857 |
| 语言 | MDX |
| Forks | 7,824 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,638 |
| 语言 | TypeScript |
| Forks | 3,634 |
| Issues | 285 |
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
| Stars | 33,193 |
| 语言 | Jupyter Notebook |
| Forks | 5,488 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 140,135 |
| 语言 | JavaScript |
| Forks | 21,049 |
| Issues | 115 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专为 AI 编程代理打造的性能优化系统框架，支持 Claude Code、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 架构显著提升 AI Agent 的任务执行效率和稳定性。

**技术亮点**:
- 模块化 Agent Harness 架构：提供可扩展的性能优化框架，支持多种 AI 编程工具的标准化集成
- 创新的 Skills 与 Instincts 双系统：Skills 定义可执行能力，Instincts 实现上下文感知响应机制
- Memory 记忆管理系统：实现长期上下文保持和跨会话知识复用，解决 LLM 上下文窗口限制
- Security-First 设计理念：内置安全审计机制，确保 AI Agent 操作的可控性和合规性
- Research-First 开发范式：融合研究导向的方法论，提供可观测性和调试能力

**适用场景**:
- 企业级 AI 辅助开发：团队可基于该框架构建统一的 AI 编程规范和安全策略，提升开发效率
- AI Agent 性能优化：开发者可利用其 Skill/Instinct 机制快速提升 AI 编程工具的任务完成率
- 跨工具集成开发：为需要在多个 AI 编程工具间切换的开发者提供一致性体验



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,917 |
| 语言 | Go |
| Forks | 3,861 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，完全兼容 OpenAI API 格式，无需 GPU 即可部署，大大降低了 AI 应用的成本和门槛，特别适合隐私敏感或需要私有化部署的场景。

**技术亮点**:
- 多模型支持：涵盖文本生成（llama/mamba）、图像生成（stable-diffusion）、音频处理（musicgen/tts）、目标检测等多种模型类型
- Go 语言实现：高性能、低内存占用的架构设计，支持在资源受限环境下高效运行
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有的 AI 应用可以零成本迁移到本地部署
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化推理网络
- 零 GPU 依赖：可在 CPU 环境下运行多种模型，大幅降低部署成本

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下部署内部 AI 助手、客服机器人或文档分析系统，数据完全留在本地
- 隐私敏感场景：医疗、金融、法律等领域需要在本地处理敏感数据，避免数据外传
- 边缘计算与物联网：将 AI 能力部署到边缘设备，实现实时推理如智能监控、语音交互、异常检测等



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,626 |
| 语言 | Python |
| Forks | 8,850 |
| Issues | 368 |
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
| Stars | 48,522 |
| 语言 | TypeScript |
| Forks | 3,808 |
| Issues | 421 |
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
| Stars | 182,575 |
| 语言 | TypeScript |
| Forks | 56,504 |
| Issues | 1,481 |
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
| Stars | 154,987 |
| 语言 | Python |
| Forks | 12,677 |
| Issues | 2,440 |
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
| Stars | 96,867 |
| 语言 | Python |
| Forks | 9,009 |
| Issues | 165 |
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
| Stars | 79,818 |
| 语言 | Python |
| Forks | 9,286 |
| Issues | 242 |
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
| Stars | 183,450 |
| 语言 | TypeScript |
| Forks | 39,039 |
| Issues | 16,066 |
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
| Stars | 94,018 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 304 |
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
| Stars | 78,813 |
| 语言 | TypeScript |
| Forks | 5,763 |
| Issues | 733 |
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
| Stars | 76,963 |
| 语言 | TypeScript |
| Forks | 6,591 |
| Issues | 181 |
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
| Stars | 79,283 |
| 语言 | Go |
| Forks | 2,751 |
| Issues | 314 |
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
| Stars | 75,611 |
| 语言 | Go |
| Forks | 2,673 |
| Issues | 941 |
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
| Stars | 37,105 |
| 语言 | Python |
| Forks | 2,584 |
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
| Stars | 419,373 |
| 语言 | Python |
| Forks | 45,616 |
| Issues | 1,192 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,671 |
| 语言 | JavaScript |
| Forks | 7,277 |
| Issues | 713 |
| Topics | api, fake, frontend, json, mock, rest, test |
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
| Stars | 48,522 |
| 语言 | TypeScript |
| Forks | 3,808 |
| Issues | 421 |
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
| Stars | 182,575 |
| 语言 | TypeScript |
| Forks | 56,504 |
| Issues | 1,481 |
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
| Stars | 51,680 |
| 语言 | Go |
| Forks | 10,342 |
| Issues | 217 |
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
| Stars | 121,500 |
| 语言 | Go |
| Forks | 42,795 |
| Issues | 2,701 |
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
| Stars | 71,563 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,777 |
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
| Stars | 54,742 |
| 语言 | Go |
| Forks | 6,535 |
| Issues | 2,831 |
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
| Stars | 47,592 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 979 |
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
| Stars | 94,018 |
| 语言 | TypeScript |
| Forks | 9,414 |
| Issues | 304 |
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
| Stars | 76,276 |
| 语言 | TypeScript |
| Forks | 6,540 |
| Issues | 404 |
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
| Stars | 84,877 |
| 语言 | JavaScript |
| Forks | 7,602 |
| Issues | 715 |
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
| Stars | 69,719 |
| 语言 | Go |
| Forks | 1,901 |
| Issues | 318 |
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
| Stars | 62,472 |
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
| Stars | 58,562 |
| 语言 | Go |
| Forks | 4,248 |
| Issues | 28 |
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
| Stars | 84,877 |
| 语言 | JavaScript |
| Forks | 7,602 |
| Issues | 715 |
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
| Stars | 63,392 |
| 语言 | Go |
| Forks | 10,306 |
| Issues | 765 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (15 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,917 |
| 语言 | Go |
| Forks | 3,861 |
| Issues | 158 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，完全兼容 OpenAI API 格式，无需 GPU 即可部署，大大降低了 AI 应用的成本和门槛，特别适合隐私敏感或需要私有化部署的场景。

**技术亮点**:
- 多模型支持：涵盖文本生成（llama/mamba）、图像生成（stable-diffusion）、音频处理（musicgen/tts）、目标检测等多种模型类型
- Go 语言实现：高性能、低内存占用的架构设计，支持在资源受限环境下高效运行
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有的 AI 应用可以零成本迁移到本地部署
- 去中心化架构：基于 libp2p 实现分布式部署，支持去中心化推理网络
- 零 GPU 依赖：可在 CPU 环境下运行多种模型，大幅降低部署成本

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下部署内部 AI 助手、客服机器人或文档分析系统，数据完全留在本地
- 隐私敏感场景：医疗、金融、法律等领域需要在本地处理敏感数据，避免数据外传
- 边缘计算与物联网：将 AI 能力部署到边缘设备，实现实时推理如智能监控、语音交互、异常检测等



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,867 |
| 语言 | Python |
| Forks | 9,009 |
| Issues | 165 |
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
| Stars | 87,174 |
| 语言 | Python |
| Forks | 33,802 |
| Issues | 424 |
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
| Stars | 100,104 |
| 语言 | TypeScript |
| Forks | 27,144 |
| Issues | 1,132 |
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
| Stars | 78,813 |
| 语言 | TypeScript |
| Forks | 5,763 |
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
| Stars | 68,887 |
| 语言 | JavaScript |
| Forks | 23,041 |
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
| Forks | 10,212 |
| Issues | 361 |
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
| Stars | 51,724 |
| 语言 | JavaScript |
| Forks | 4,695 |
| Issues | 1,476 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### bigskysoftware/htmx

**描述**: </> htmx - high power tools for HTML

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,739 |
| 语言 | JavaScript |
| Forks | 1,582 |
| Issues | 662 |
| Topics | hateoas, html, htmx, hyperscript, javascript, rest |
| 许可证 | Other |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,335 |
| 语言 | Go |
| Forks | 8,568 |
| Issues | 665 |
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
| Stars | 71,295 |
| 语言 | Go |
| Forks | 4,691 |
| Issues | 260 |
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
| Stars | 57,387 |
| 语言 | Go |
| Forks | 3,256 |
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
| Stars | 37,105 |
| 语言 | Python |
| Forks | 2,584 |
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
| Stars | 419,373 |
| 语言 | Python |
| Forks | 45,616 |
| Issues | 1,192 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,671 |
| 语言 | JavaScript |
| Forks | 7,277 |
| Issues | 713 |
| Topics | api, fake, frontend, json, mock, rest, test |
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
| Stars | 100,290 |
| 语言 | TypeScript |
| Forks | 11,986 |
| Issues | 970 |
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
| Stars | 57,705 |
| 语言 | JavaScript |
| Forks | 6,235 |
| Issues | 303 |
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
| Stars | 43,609 |
| 语言 | Go |
| Forks | 3,934 |
| Issues | 1,102 |
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
| Stars | 51,680 |
| 语言 | Go |
| Forks | 10,342 |
| Issues | 217 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (10 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,541 |
| 语言 | HTML |
| Forks | 20,631 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

prompts.chat 是全球最大的开源提示词社区之一，前身是著名的 Awesome ChatGPT Prompts 项目，拥有超过 15 万星标，支持自托管部署，既能享受社区共享的丰富提示词资源，又能满足企业级隐私需求。

**技术亮点**:
- 基于 Next.js + TypeScript 构建的现代化 Web 应用架构
- 支持多种主流 LLM 模型（ChatGPT、Claude、Gemini、GPT-4）
- 完全开源且支持自托管部署，确保数据隐私安全
- Creative Commons Zero v1.0 Universal 许可证，商业使用零限制
- 活跃的社区贡献机制，持续更新高质量提示词资源

**适用场景**:
- 个人用户寻找和收藏高质量 AI 提示词，提升与 AI 助手的交互效率
- 企业自建提示词管理系统，保护内部数据隐私的同时共享团队知识
- 开发者学习提示词工程技巧，参考开源项目的最佳实践



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,583 |
| 语言 | TypeScript |
| Forks | 7,840 |
| Issues | 46 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,692 |
| 语言 | Python |
| Forks | 2,900 |
| Issues | 167 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,752 |
| 语言 | Python |
| Forks | 3,884 |
| Issues | 81 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,421 |
| 语言 | Unknown |
| Forks | 6,174 |
| Issues | 19 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,857 |
| 语言 | MDX |
| Forks | 7,824 |
| Issues | 256 |
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
| Stars | 89,627 |
| 语言 | TypeScript |
| Forks | 9,979 |
| Issues | 2,224 |
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
| Stars | 87,128 |
| 语言 | TypeScript |
| Forks | 8,820 |
| Issues | 1,637 |
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
| Stars | 127,331 |
| 语言 | JavaScript |
| Forks | 12,468 |
| Issues | 2 |
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
| Stars | 169,147 |
| 语言 | Go |
| Forks | 13,111 |
| Issues | 171 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (64 个项目) { #其他 }


### 🌟 高优先级


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,421 |
| 语言 | Python |
| Forks | 6,481 |
| Issues | 56 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,858 |
| 语言 | Python |
| Forks | 12,893 |
| Issues | 109 |
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
| Stars | 85,429 |
| 语言 | Python |
| Forks | 7,348 |
| Issues | 631 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 134,454 |
| 语言 | Unknown |
| Forks | 33,866 |
| Issues | 143 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 385,046 |
| 语言 | Python |
| Forks | 66,087 |
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
| Stars | 114,246 |
| 语言 | TypeScript |
| Forks | 5,866 |
| Issues | 319 |
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
| Stars | 107,919 |
| 语言 | TypeScript |
| Forks | 7,847 |
| Issues | 230 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,000 |
| 语言 | JavaScript |
| Forks | 3,947 |
| Issues | 75 |
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
| Stars | 48,031 |
| 语言 | Go |
| Forks | 10,264 |
| Issues | 1,891 |
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
| Stars | 101,581 |
| 语言 | C++ |
| Forks | 16,395 |
| Issues | 1,389 |
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
| Stars | 63,410 |
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
| Stars | 64,519 |
| 语言 | TypeScript |
| Forks | 8,790 |
| Issues | 308 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 290,829 |
| 语言 | Python |
| Forks | 27,584 |
| Issues | 21 |
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
| Stars | 219,302 |
| 语言 | Python |
| Forks | 50,305 |
| Issues | 915 |
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
| Stars | 85,999 |
| 语言 | Python |
| Forks | 37,162 |
| Issues | 3,586 |
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
| Stars | 77,679 |
| 语言 | Python |
| Forks | 45,174 |
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
| Stars | 441,405 |
| 语言 | TypeScript |
| Forks | 44,096 |
| Issues | 216 |
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
| Stars | 352,263 |
| 语言 | TypeScript |
| Forks | 43,871 |
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
| Stars | 120,300 |
| 语言 | TypeScript |
| Forks | 13,141 |
| Issues | 2,924 |
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
| Stars | 111,558 |
| 语言 | TypeScript |
| Forks | 8,419 |
| Issues | 1,805 |
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
| Stars | 108,417 |
| 语言 | TypeScript |
| Forks | 13,322 |
| Issues | 5,011 |
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
| Stars | 97,765 |
| 语言 | TypeScript |
| Forks | 54,575 |
| Issues | 1,361 |
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
| Stars | 96,451 |
| 语言 | TypeScript |
| Forks | 5,268 |
| Issues | 668 |
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
| Stars | 94,344 |
| 语言 | TypeScript |
| Forks | 5,156 |
| Issues | 106 |
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
| Stars | 83,054 |
| 语言 | TypeScript |
| Forks | 7,578 |
| Issues | 33 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,017 |
| 语言 | TypeScript |
| Forks | 10,207 |
| Issues | 672 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,577 |
| 语言 | TypeScript |
| Forks | 7,989 |
| Issues | 713 |
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
| Stars | 244,419 |
| 语言 | JavaScript |
| Forks | 50,977 |
| Issues | 1,216 |
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
| Stars | 116,559 |
| 语言 | JavaScript |
| Forks | 35,253 |
| Issues | 2,600 |
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
| Stars | 111,777 |
| 语言 | JavaScript |
| Forks | 36,319 |
| Issues | 563 |
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
| Stars | 109,041 |
| 语言 | JavaScript |
| Forks | 11,598 |
| Issues | 327 |
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
| Stars | 98,015 |
| 语言 | JavaScript |
| Forks | 32,688 |
| Issues | 1,674 |
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
| Stars | 95,529 |
| 语言 | JavaScript |
| Forks | 15,318 |
| Issues | 55 |
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
| Stars | 86,166 |
| 语言 | JavaScript |
| Forks | 4,844 |
| Issues | 982 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,966 |
| 语言 | JavaScript |
| Forks | 32,158 |
| Issues | 271 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,932 |
| 语言 | JavaScript |
| Forks | 16,812 |
| Issues | 892 |
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
| Stars | 65,933 |
| 语言 | JavaScript |
| Forks | 9,381 |
| Issues | 207 |
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
| Stars | 62,537 |
| 语言 | JavaScript |
| Forks | 3,995 |
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
| Stars | 61,517 |
| 语言 | JavaScript |
| Forks | 7,126 |
| Issues | 135 |
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
| Stars | 60,236 |
| 语言 | JavaScript |
| Forks | 5,645 |
| Issues | 67 |
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
| Stars | 59,850 |
| 语言 | JavaScript |
| Forks | 20,461 |
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
| Stars | 57,423 |
| 语言 | JavaScript |
| Forks | 12,298 |
| Issues | 25 |
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
| Stars | 53,078 |
| 语言 | JavaScript |
| Forks | 10,606 |
| Issues | 458 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,384 |
| 语言 | JavaScript |
| Forks | 11,429 |
| Issues | 232 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,630 |
| 语言 | JavaScript |
| Forks | 2,427 |
| Issues | 1,208 |
| Topics | date, date-formatting, datetime, dayjs, moment, time |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,293 |
| 语言 | Go |
| Forks | 18,963 |
| Issues | 9,929 |
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
| Stars | 105,818 |
| 语言 | Go |
| Forks | 14,976 |
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
| Stars | 87,430 |
| 语言 | Go |
| Forks | 8,233 |
| Issues | 264 |
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
| Stars | 81,430 |
| 语言 | Go |
| Forks | 4,984 |
| Issues | 392 |
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
| Stars | 68,640 |
| 语言 | Go |
| Forks | 3,212 |
| Issues | 7 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,476 |
| 语言 | Go |
| Forks | 5,008 |
| Issues | 1,162 |
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
| Stars | 50,967 |
| 语言 | Go |
| Forks | 21,880 |
| Issues | 397 |
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
| Stars | 49,255 |
| 语言 | Go |
| Forks | 7,957 |
| Issues | 560 |
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
| Stars | 71,911 |
| 语言 | Shell |
| Forks | 11,143 |
| Issues | 112 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,983 |
| 语言 | Python |
| Forks | 11,307 |
| Issues | 323 |
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
| Stars | 341,480 |
| 语言 | Python |
| Forks | 55,216 |
| Issues | 527 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 97,202 |
| 语言 | Python |
| Forks | 11,980 |
| Issues | 118 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,787 |
| 语言 | Python |
| Forks | 7,199 |
| Issues | 481 |
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
| Stars | 76,639 |
| 语言 | Python |
| Forks | 16,827 |
| Issues | 20 |
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
| Stars | 138,563 |
| 语言 | TypeScript |
| Forks | 16,492 |
| Issues | 45 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,300 |
| 语言 | JavaScript |
| Forks | 9,186 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,532 |
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
| Stars | 46,964 |
| 语言 | Go |
| Forks | 8,866 |
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
| Stars | 45,816 |
| 语言 | Go |
| Forks | 3,779 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
