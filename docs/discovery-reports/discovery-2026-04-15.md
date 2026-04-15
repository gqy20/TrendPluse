# 项目发现报告 (2026-04-15)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 23 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 19 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 7 |
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
| Stars | 132,037 |
| 语言 | Python |
| Forks | 18,738 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源AI界面项目，支持 Ollama、OpenAI API 等多种后端，拥有超过13万stars证明了其成熟度和社区认可度。作为自托管解决方案，它特别适合需要数据隐私保护和定制化需求的企业与个人用户，同时支持 RAG 和 MCP 等高级功能。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，实现统一接口管理
- 自托管部署：支持完全私有化部署，保障数据隐私安全，无需依赖云服务
- RAG 支持：内置检索增强生成功能，可结合本地知识库实现精准问答
- MCP 协议支持：支持 Model Context Protocol 协议，便于扩展和集成第三方工具
- 现代化 Web UI：提供直观的用户界面，支持实时对话、文件上传、多模态交互等功能

**适用场景**:
- 企业级 AI 助手：适用于企业内部知识管理、客服系统、文档问答等场景，支持私有化部署确保数据安全
- 个人开发者本地 AI 环境：为开发者提供便捷的本地 LLM 调试和测试平台，支持快速切换不同模型
- 隐私敏感型应用：医疗、金融、法律等行业需要在本地处理敏感数据，避免数据上传到第三方云服务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,120 |
| 语言 | Python |
| Forks | 12,172 |
| Issues | 4,655 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是来自知名开源 AI 组织 NousResearch 的 AI Agent 框架，拥有 89k+ Stars 的高热度，证明了其在社区中的广泛认可度。该项目支持 OpenAI、Anthropic Claude 等主流 LLM 提供商，提供灵活的多模型集成能力，是构建智能代理系统的可靠选择。

**技术亮点**:
- 支持多 LLM 提供商集成，包括 OpenAI (ChatGPT/Codex)、Anthropic (Claude)、Nous Research (Hermes) 等主流模型
- 基于 Python 开发，生态丰富，易于与现有 Python 项目和工具链集成
- 支持 Claude Code 和 OpenClaw 等相关生态，可与其他 AI Agent 协同工作
- 采用 MIT 许可证，开源透明，适合商业和个人项目使用
- Hermes 系列模型经过针对性优化，在 Agent 任务场景中表现优异

**适用场景**:
- 企业级 AI Agent 系统开发：需要集成多个 LLM 提供商，构建多功能的智能代理平台
- 代码助手与自动化编程：结合 Claude Code 等工具，实现智能代码生成、调试和重构能力
- 个人开发者快速原型验证：利用开源框架快速搭建 AI Agent 原型，验证业务场景可行性



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,166 |
| 语言 | Python |
| Forks | 8,813 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源社区最受欢迎的 RAG 引擎之一，通过将 RAG 与 Agent 能力深度融合，为 LLMs 提供高质量上下文层，支持复杂文档理解、多模型兼容和可视化工作流编排，是构建企业级智能知识库的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性融合检索增强生成与 AI Agent，支持复杂推理和多步骤任务执行
- 多模态文档理解：内置 OCR 和文档解析能力，支持 PDF、Word、Excel 等多种格式的智能提取
- 多 LLM 兼容性：无缝支持 OpenAI、DeepSeek、Ollama 等主流大模型，支持本地部署
- GraphRAG 与高级检索：集成知识图谱增强检索，结合向量检索与图检索，显著提升复杂查询准确性
- 可视化工作流编排：提供图形化界面设计 RAG Pipeline，降低使用门槛

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持政策手册、技术文档、合同分析的智能检索
- 复杂文档处理与分析：处理大量非结构化文档（合同、报告、手册），实现精准问答与信息抽取
- 智能 Agent 工作流：构建具备深度推理能力的 AI 助手，支持多轮对话与复杂任务自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,260 |
| 语言 | JavaScript |
| Forks | 24,410 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个经过15万+用户验证的AI代理性能优化框架，支持Claude Code、Codex、Cursor等主流AI编程工具，通过Skills、Memory和Security机制显著提升开发效率，是目前最全面的AI代码助手增强系统。

**技术亮点**:
- 多AI代理兼容：统一支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具框架
- 性能优化系统：专门针对agent harness的性能调优，提升响应速度和资源利用率
- Memory机制：实现智能记忆系统，让AI代理能够跨会话保持上下文连贯性
- 安全沙箱设计：内置Security模块，确保AI代码执行环境的安全性
- MCP协议支持：遵循Model Context Protocol标准，便于扩展和集成

**适用场景**:
- 企业级AI代码助手集成：帮助团队统一管理多种AI编程工具，提升整体开发效率
- 个人开发者效率提升：通过Skills和Instincts机制，让AI更懂你的编码习惯和项目需求
- AI代理系统开发：为开发者提供构建高性能AI代理的参考架构和最佳实践



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,427 |
| 语言 | Go |
| Forks | 3,953 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在无需 GPU 的情况下运行 LLM、图像生成、语音合成、目标检测等多种 AI 模型，提供统一的 API 接口让开发者轻松集成各种 AI 能力，特别适合需要数据隐私保护和私有化部署的企业场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）、目标检测等多种模型类型
- 无 GPU 依赖运行：通过优化的推理引擎，在 CPU 上也能高效运行各类 AI 模型，降低硬件门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络下的模型共享和协作推理
- 丰富的协议支持：支持 MCP（Model Context Protocol）、OpenAI 兼容 API、Rerank 等多种协议，便于现有应用迁移
- Go 语言实现：高性能、高并发、低内存占用的运行时环境，适合生产环境部署

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下，为企业内部系统提供文本生成、智能问答、文档分析等 AI 能力，确保数据隐私合规
- 本地开发与测试环境：开发者可以在本地快速原型开发和测试 AI 应用，无需申请云 API 密钥或支付调用费用
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 推理能力，实现本地化的图像识别、语音交互等功能



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,220 |
| 语言 | TypeScript |
| Forks | 14,923 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多智能体协作和 MCP 协议，兼容 OpenAI/Claude/Gemini 等主流模型，拥有 75k+ Stars 的成熟开源生态，是构建企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 Agent 之间协作与通信，实现复杂任务的分布式处理
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成第三方工具
- 多模型集成：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- TypeScript 全栈架构：类型安全的现代前端框架，确保代码质量和可维护性
- Agent Team 设计工具：可视化构建和管理 Agent 团队，降低多智能体系统开发门槛

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务系统，如客服自动化、工作流编排
- 个人开发者快速原型：用 LobeHub 的模块化组件快速搭建 AI 助手和知识库应用
- AI 工作流自动化：整合多种 AI 能力，实现文档处理、数据分析、内容生成等任务的自动化



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,143 |
| 语言 | Python |
| Forks | 8,580 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的大模型微调框架之一，统一支持 100+ LLM 和 VLM 的高效微调，提供从 LoRA、QLoRA 到 RLHF 的全链路解决方案，特别适合需要快速适配和部署开源大模型的企业和个人开发者。

**技术亮点**:
- 统一微调框架：支持 100+ 主流大语言模型（如 LLaMA、Qwen、DeepSeek、Gemma 等）和视觉语言模型的统一微调接口
- 多样化微调技术：集成 LoRA、QLoRA、Prefix-tuning、Ptuning 等多种参数高效微调方法，并支持 RLHF (PPO/DPO) 训练范式
- 量化训练支持：内置 4-bit/8-bit 量化训练能力，大幅降低显存占用，使单卡微调大模型成为可能
- ACL 2024 学术认可：经过顶级学术会议验证的技术方案，工程实现具备较高的可靠性和可扩展性
- 完善的监控与工具链：提供训练监控、早停、模型导出等完整工具链，支持从实验到生产的无缝衔接

**适用场景**:
- 企业级模型定制：企业需要基于自有业务数据快速微调开源大模型（如客服摘要、私域知识问答等垂直场景）
- 学术研究与模型实验：研究者需要对比不同微调方法、模型架构的效果，LlamaFactory 提供统一基准便于实验
- 低成本模型适配：个人开发者或资源有限的团队，利用 QLoRA 在消费级 GPU 上微调大模型，实现本地化部署



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,528 |
| 语言 | TypeScript |
| Forks | 4,647 |
| Issues | 240 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个革命性的Claude Code长期记忆插件，通过AI自动压缩编码会话历史并注入未来上下文，解决了AI助手无法跨会话保持连续性的核心痛点，让Claude能够真正"记住"之前的开发工作。

**技术亮点**:
- 基于ChromaDB向量数据库实现语义记忆检索，通过embeddings技术实现跨会话的上下文匹配
- 采用RAG（检索增强生成）架构，将历史编码上下文动态注入到新会话的prompt中
- 使用Claude自身的agent-sdk进行智能压缩，大幅减少记忆存储开销同时保留关键信息
- 支持SQLite本地持久化存储，无需复杂基础设施即可部署使用
- 作为Claude Code官方插件架构实现，无缝集成到现有开发工作流中

**适用场景**:
- 大型项目的长期开发维护：跨越数周甚至数月的项目中，Claude能自动回忆之前的架构决策、代码修改和调试过程，避免重复探索
- 多人协作场景：团队成员可以共享项目记忆，新成员加入时Claude能快速了解项目历史和上下文
- 复杂重构和迁移工作：Claude能记住之前的重构进度、遇到的问题和解决方案，确保重构工作的连续性



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,767 |
| 语言 | TypeScript |
| Forks | 8,828 |
| Issues | 87 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,263 |
| 语言 | Python |
| Forks | 9,923 |
| Issues | 354 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,656 |
| 语言 | Python |
| Forks | 6,951 |
| Issues | 937 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,858 |
| 语言 | Java |
| Forks | 15,910 |
| Issues | 19 |
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
| Stars | 38,987 |
| 语言 | Python |
| Forks | 6,188 |
| Issues | 70 |
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
| Stars | 37,079 |
| 语言 | Python |
| Forks | 4,387 |
| Issues | 95 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,747 |
| 语言 | TypeScript |
| Forks | 3,654 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,714 |
| 语言 | Python |
| Forks | 15,442 |
| Issues | 5 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,549 |
| 语言 | TypeScript |
| Forks | 7,010 |
| Issues | 280 |
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
| Stars | 58,377 |
| 语言 | JavaScript |
| Forks | 6,316 |
| Issues | 324 |
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
| Stars | 71,276 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 402 |
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
| Stars | 51,853 |
| 语言 | TypeScript |
| Forks | 4,161 |
| Issues | 532 |
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
| Stars | 87,969 |
| 语言 | Python |
| Forks | 10,112 |
| Issues | 235 |
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
| Stars | 51,936 |
| 语言 | TypeScript |
| Forks | 24,154 |
| Issues | 808 |
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
| Stars | 184,200 |
| 语言 | TypeScript |
| Forks | 56,830 |
| Issues | 1,468 |
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
| Stars | 154,981 |
| 语言 | Java |
| Forks | 46,155 |
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
| Stars | 146,982 |
| 语言 | Python |
| Forks | 8,775 |
| Issues | 935 |
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
| Stars | 56,746 |
| 语言 | Jupyter Notebook |
| Forks | 19,641 |
| Issues | 7 |
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
| Stars | 34,092 |
| 语言 | Python |
| Forks | 2,138 |
| Issues | 94 |
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
| Stars | 33,572 |
| 语言 | Jupyter Notebook |
| Forks | 5,546 |
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
| Stars | 45,323 |
| 语言 | Rust |
| Forks | 2,877 |
| Issues | 511 |
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
| Stars | 132,037 |
| 语言 | Python |
| Forks | 18,738 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源AI界面项目，支持 Ollama、OpenAI API 等多种后端，拥有超过13万stars证明了其成熟度和社区认可度。作为自托管解决方案，它特别适合需要数据隐私保护和定制化需求的企业与个人用户，同时支持 RAG 和 MCP 等高级功能。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，实现统一接口管理
- 自托管部署：支持完全私有化部署，保障数据隐私安全，无需依赖云服务
- RAG 支持：内置检索增强生成功能，可结合本地知识库实现精准问答
- MCP 协议支持：支持 Model Context Protocol 协议，便于扩展和集成第三方工具
- 现代化 Web UI：提供直观的用户界面，支持实时对话、文件上传、多模态交互等功能

**适用场景**:
- 企业级 AI 助手：适用于企业内部知识管理、客服系统、文档问答等场景，支持私有化部署确保数据安全
- 个人开发者本地 AI 环境：为开发者提供便捷的本地 LLM 调试和测试平台，支持快速切换不同模型
- 隐私敏感型应用：医疗、金融、法律等行业需要在本地处理敏感数据，避免数据上传到第三方云服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,166 |
| 语言 | Python |
| Forks | 8,813 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源社区最受欢迎的 RAG 引擎之一，通过将 RAG 与 Agent 能力深度融合，为 LLMs 提供高质量上下文层，支持复杂文档理解、多模型兼容和可视化工作流编排，是构建企业级智能知识库的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性融合检索增强生成与 AI Agent，支持复杂推理和多步骤任务执行
- 多模态文档理解：内置 OCR 和文档解析能力，支持 PDF、Word、Excel 等多种格式的智能提取
- 多 LLM 兼容性：无缝支持 OpenAI、DeepSeek、Ollama 等主流大模型，支持本地部署
- GraphRAG 与高级检索：集成知识图谱增强检索，结合向量检索与图检索，显著提升复杂查询准确性
- 可视化工作流编排：提供图形化界面设计 RAG Pipeline，降低使用门槛

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持政策手册、技术文档、合同分析的智能检索
- 复杂文档处理与分析：处理大量非结构化文档（合同、报告、手册），实现精准问答与信息抽取
- 智能 Agent 工作流：构建具备深度推理能力的 AI 助手，支持多轮对话与复杂任务自动化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,220 |
| 语言 | TypeScript |
| Forks | 14,923 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多智能体协作和 MCP 协议，兼容 OpenAI/Claude/Gemini 等主流模型，拥有 75k+ Stars 的成熟开源生态，是构建企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 Agent 之间协作与通信，实现复杂任务的分布式处理
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成第三方工具
- 多模型集成：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- TypeScript 全栈架构：类型安全的现代前端框架，确保代码质量和可维护性
- Agent Team 设计工具：可视化构建和管理 Agent 团队，降低多智能体系统开发门槛

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务系统，如客服自动化、工作流编排
- 个人开发者快速原型：用 LobeHub 的模块化组件快速搭建 AI 助手和知识库应用
- AI 工作流自动化：整合多种 AI 能力，实现文档处理、数据分析、内容生成等任务的自动化



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,528 |
| 语言 | TypeScript |
| Forks | 4,647 |
| Issues | 240 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个革命性的Claude Code长期记忆插件，通过AI自动压缩编码会话历史并注入未来上下文，解决了AI助手无法跨会话保持连续性的核心痛点，让Claude能够真正"记住"之前的开发工作。

**技术亮点**:
- 基于ChromaDB向量数据库实现语义记忆检索，通过embeddings技术实现跨会话的上下文匹配
- 采用RAG（检索增强生成）架构，将历史编码上下文动态注入到新会话的prompt中
- 使用Claude自身的agent-sdk进行智能压缩，大幅减少记忆存储开销同时保留关键信息
- 支持SQLite本地持久化存储，无需复杂基础设施即可部署使用
- 作为Claude Code官方插件架构实现，无缝集成到现有开发工作流中

**适用场景**:
- 大型项目的长期开发维护：跨越数周甚至数月的项目中，Claude能自动回忆之前的架构决策、代码修改和调试过程，避免重复探索
- 多人协作场景：团队成员可以共享项目记忆，新成员加入时Claude能快速了解项目历史和上下文
- 复杂重构和迁移工作：Claude能记住之前的重构进度、遇到的问题和解决方案，确保重构工作的连续性



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,858 |
| 语言 | Java |
| Forks | 15,910 |
| Issues | 19 |
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
| Stars | 38,987 |
| 语言 | Python |
| Forks | 6,188 |
| Issues | 70 |
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
| Stars | 37,079 |
| 语言 | Python |
| Forks | 4,387 |
| Issues | 95 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,747 |
| 语言 | TypeScript |
| Forks | 3,654 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,714 |
| 语言 | Python |
| Forks | 15,442 |
| Issues | 5 |
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
| Stars | 100,894 |
| 语言 | TypeScript |
| Forks | 12,088 |
| Issues | 969 |
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
| Stars | 58,377 |
| 语言 | JavaScript |
| Forks | 6,316 |
| Issues | 324 |
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
| Stars | 75,660 |
| 语言 | Python |
| Forks | 10,239 |
| Issues | 236 |
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
| Stars | 51,936 |
| 语言 | TypeScript |
| Forks | 24,154 |
| Issues | 808 |
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
| Stars | 43,817 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,180 |
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
| Stars | 33,339 |
| 语言 | Python |
| Forks | 4,742 |
| Issues | 205 |
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
| Stars | 34,092 |
| 语言 | Python |
| Forks | 2,138 |
| Issues | 94 |
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
| Stars | 33,572 |
| 语言 | Jupyter Notebook |
| Forks | 5,546 |
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
| Stars | 132,037 |
| 语言 | Python |
| Forks | 18,738 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源AI界面项目，支持 Ollama、OpenAI API 等多种后端，拥有超过13万stars证明了其成熟度和社区认可度。作为自托管解决方案，它特别适合需要数据隐私保护和定制化需求的企业与个人用户，同时支持 RAG 和 MCP 等高级功能。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API 等多种 LLM 提供商，实现统一接口管理
- 自托管部署：支持完全私有化部署，保障数据隐私安全，无需依赖云服务
- RAG 支持：内置检索增强生成功能，可结合本地知识库实现精准问答
- MCP 协议支持：支持 Model Context Protocol 协议，便于扩展和集成第三方工具
- 现代化 Web UI：提供直观的用户界面，支持实时对话、文件上传、多模态交互等功能

**适用场景**:
- 企业级 AI 助手：适用于企业内部知识管理、客服系统、文档问答等场景，支持私有化部署确保数据安全
- 个人开发者本地 AI 环境：为开发者提供便捷的本地 LLM 调试和测试平台，支持快速切换不同模型
- 隐私敏感型应用：医疗、金融、法律等行业需要在本地处理敏感数据，避免数据上传到第三方云服务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,120 |
| 语言 | Python |
| Forks | 12,172 |
| Issues | 4,655 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是来自知名开源 AI 组织 NousResearch 的 AI Agent 框架，拥有 89k+ Stars 的高热度，证明了其在社区中的广泛认可度。该项目支持 OpenAI、Anthropic Claude 等主流 LLM 提供商，提供灵活的多模型集成能力，是构建智能代理系统的可靠选择。

**技术亮点**:
- 支持多 LLM 提供商集成，包括 OpenAI (ChatGPT/Codex)、Anthropic (Claude)、Nous Research (Hermes) 等主流模型
- 基于 Python 开发，生态丰富，易于与现有 Python 项目和工具链集成
- 支持 Claude Code 和 OpenClaw 等相关生态，可与其他 AI Agent 协同工作
- 采用 MIT 许可证，开源透明，适合商业和个人项目使用
- Hermes 系列模型经过针对性优化，在 Agent 任务场景中表现优异

**适用场景**:
- 企业级 AI Agent 系统开发：需要集成多个 LLM 提供商，构建多功能的智能代理平台
- 代码助手与自动化编程：结合 Claude Code 等工具，实现智能代码生成、调试和重构能力
- 个人开发者快速原型验证：利用开源框架快速搭建 AI Agent 原型，验证业务场景可行性



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,166 |
| 语言 | Python |
| Forks | 8,813 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源社区最受欢迎的 RAG 引擎之一，通过将 RAG 与 Agent 能力深度融合，为 LLMs 提供高质量上下文层，支持复杂文档理解、多模型兼容和可视化工作流编排，是构建企业级智能知识库的首选方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性融合检索增强生成与 AI Agent，支持复杂推理和多步骤任务执行
- 多模态文档理解：内置 OCR 和文档解析能力，支持 PDF、Word、Excel 等多种格式的智能提取
- 多 LLM 兼容性：无缝支持 OpenAI、DeepSeek、Ollama 等主流大模型，支持本地部署
- GraphRAG 与高级检索：集成知识图谱增强检索，结合向量检索与图检索，显著提升复杂查询准确性
- 可视化工作流编排：提供图形化界面设计 RAG Pipeline，降低使用门槛

**适用场景**:
- 企业智能知识库：构建内部文档问答系统，支持政策手册、技术文档、合同分析的智能检索
- 复杂文档处理与分析：处理大量非结构化文档（合同、报告、手册），实现精准问答与信息抽取
- 智能 Agent 工作流：构建具备深度推理能力的 AI 助手，支持多轮对话与复杂任务自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,260 |
| 语言 | JavaScript |
| Forks | 24,410 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个经过15万+用户验证的AI代理性能优化框架，支持Claude Code、Codex、Cursor等主流AI编程工具，通过Skills、Memory和Security机制显著提升开发效率，是目前最全面的AI代码助手增强系统。

**技术亮点**:
- 多AI代理兼容：统一支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具框架
- 性能优化系统：专门针对agent harness的性能调优，提升响应速度和资源利用率
- Memory机制：实现智能记忆系统，让AI代理能够跨会话保持上下文连贯性
- 安全沙箱设计：内置Security模块，确保AI代码执行环境的安全性
- MCP协议支持：遵循Model Context Protocol标准，便于扩展和集成

**适用场景**:
- 企业级AI代码助手集成：帮助团队统一管理多种AI编程工具，提升整体开发效率
- 个人开发者效率提升：通过Skills和Instincts机制，让AI更懂你的编码习惯和项目需求
- AI代理系统开发：为开发者提供构建高性能AI代理的参考架构和最佳实践



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,220 |
| 语言 | TypeScript |
| Forks | 14,923 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 AI Agent 协作平台，支持多智能体协作和 MCP 协议，兼容 OpenAI/Claude/Gemini 等主流模型，拥有 75k+ Stars 的成熟开源生态，是构建企业级 AI Agent 应用的理想选择。

**技术亮点**:
- 多智能体协作框架：支持多个 Agent 之间协作与通信，实现复杂任务的分布式处理
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成第三方工具
- 多模型集成：同时支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，可灵活切换
- TypeScript 全栈架构：类型安全的现代前端框架，确保代码质量和可维护性
- Agent Team 设计工具：可视化构建和管理 Agent 团队，降低多智能体系统开发门槛

**适用场景**:
- 企业级 AI 应用开发：构建需要多 Agent 协作的复杂业务系统，如客服自动化、工作流编排
- 个人开发者快速原型：用 LobeHub 的模块化组件快速搭建 AI 助手和知识库应用
- AI 工作流自动化：整合多种 AI 能力，实现文档处理、数据分析、内容生成等任务的自动化



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,528 |
| 语言 | TypeScript |
| Forks | 4,647 |
| Issues | 240 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个革命性的Claude Code长期记忆插件，通过AI自动压缩编码会话历史并注入未来上下文，解决了AI助手无法跨会话保持连续性的核心痛点，让Claude能够真正"记住"之前的开发工作。

**技术亮点**:
- 基于ChromaDB向量数据库实现语义记忆检索，通过embeddings技术实现跨会话的上下文匹配
- 采用RAG（检索增强生成）架构，将历史编码上下文动态注入到新会话的prompt中
- 使用Claude自身的agent-sdk进行智能压缩，大幅减少记忆存储开销同时保留关键信息
- 支持SQLite本地持久化存储，无需复杂基础设施即可部署使用
- 作为Claude Code官方插件架构实现，无缝集成到现有开发工作流中

**适用场景**:
- 大型项目的长期开发维护：跨越数周甚至数月的项目中，Claude能自动回忆之前的架构决策、代码修改和调试过程，避免重复探索
- 多人协作场景：团队成员可以共享项目记忆，新成员加入时Claude能快速了解项目历史和上下文
- 复杂重构和迁移工作：Claude能记住之前的重构进度、遇到的问题和解决方案，确保重构工作的连续性



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,806 |
| 语言 | HTML |
| Forks | 20,930 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有近16万星标的社区驱动型AI提示词平台，支持ChatGPT、Claude、Gemini等多模型，提供了自托管部署选项，适合企业和个人用户免费使用、分享和收藏提示词，是学习提示工程和构建团队提示词库的绝佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构和良好的开发体验
- 支持多种大语言模型（ChatGPT、Claude、Gemini、GPT-4），实现跨平台的提示词兼容
- 开源且支持自托管部署，满足企业级隐私合规需求
- 采用社区驱动的模式，拥有丰富的提示词资源库和持续更新的内容
- 基于静态站点生成（HTML），加载速度快，SEO 友好，便于内容分发

**适用场景**:
- 个人开发者学习AI提示工程，通过参考社区优秀提示词提升LLM交互效果
- 企业团队自建提示词库，保护内部知识和数据隐私，避免使用第三方服务
- AI爱好者收集整理不同场景的提示词模板，提升日常工作和创作效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,838 |
| 语言 | Jupyter Notebook |
| Forks | 13,950 |
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
| Stars | 53,767 |
| 语言 | TypeScript |
| Forks | 8,828 |
| Issues | 87 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,263 |
| 语言 | Python |
| Forks | 9,923 |
| Issues | 354 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,656 |
| 语言 | Python |
| Forks | 6,951 |
| Issues | 937 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,377 |
| 语言 | JavaScript |
| Forks | 6,316 |
| Issues | 324 |
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
| Stars | 71,276 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 402 |
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
| Stars | 51,853 |
| 语言 | TypeScript |
| Forks | 4,161 |
| Issues | 532 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,861 |
| 语言 | HTML |
| Forks | 4,312 |
| Issues | 10 |
| Topics | agentic-engineering, anthropic, best-practices, boris, boris-cherny, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, vibe-coding |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,936 |
| 语言 | TypeScript |
| Forks | 24,154 |
| Issues | 808 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,741 |
| 语言 | Python |
| Forks | 15,636 |
| Issues | 4,293 |
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
| Stars | 146,982 |
| 语言 | Python |
| Forks | 8,775 |
| Issues | 935 |
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
| Stars | 169,104 |
| 语言 | Go |
| Forks | 15,610 |
| Issues | 2,943 |
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
| Stars | 47,791 |
| 语言 | Rust |
| Forks | 9,522 |
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
| Stars | 34,092 |
| 语言 | Python |
| Forks | 2,138 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 65,603 |
| 语言 | Python |
| Forks | 6,662 |
| Issues | 105 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
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
| Stars | 109,384 |
| 语言 | Python |
| Forks | 6,953 |
| Issues | 601 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
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
| Stars | 70,143 |
| 语言 | Python |
| Forks | 8,580 |
| Issues | 969 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的大模型微调框架之一，统一支持 100+ LLM 和 VLM 的高效微调，提供从 LoRA、QLoRA 到 RLHF 的全链路解决方案，特别适合需要快速适配和部署开源大模型的企业和个人开发者。

**技术亮点**:
- 统一微调框架：支持 100+ 主流大语言模型（如 LLaMA、Qwen、DeepSeek、Gemma 等）和视觉语言模型的统一微调接口
- 多样化微调技术：集成 LoRA、QLoRA、Prefix-tuning、Ptuning 等多种参数高效微调方法，并支持 RLHF (PPO/DPO) 训练范式
- 量化训练支持：内置 4-bit/8-bit 量化训练能力，大幅降低显存占用，使单卡微调大模型成为可能
- ACL 2024 学术认可：经过顶级学术会议验证的技术方案，工程实现具备较高的可靠性和可扩展性
- 完善的监控与工具链：提供训练监控、早停、模型导出等完整工具链，支持从实验到生产的无缝衔接

**适用场景**:
- 企业级模型定制：企业需要基于自有业务数据快速微调开源大模型（如客服摘要、私域知识问答等垂直场景）
- 学术研究与模型实验：研究者需要对比不同微调方法、模型架构的效果，LlamaFactory 提供统一基准便于实验
- 低成本模型适配：个人开发者或资源有限的团队，利用 QLoRA 在消费级 GPU 上微调大模型，实现本地化部署



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,926 |
| 语言 | Python |
| Forks | 6,564 |
| Issues | 77 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有 65k+ Stars 的活跃社区，支持股票、加密货币、期权、固定收益等多种资产类别，并原生集成 AI/ML 能力，为量化分析师和 AI 交易代理提供一站式数据解决方案。

**技术亮点**:
- 模块化架构设计，支持数据源插拔式扩展，可轻松集成多个金融数据提供商
- 原生支持 AI 和机器学习集成，提供 LangChain 等主流 AI 框架的对接能力
- 覆盖股票、加密货币、期权、固收、经济数据等全品类金融数据
- 提供标准化的 API 接口，支持 Python SDK 和 CLI 工具，方便开发者快速接入
- 活跃的开源社区维护，持续迭代更新，具备企业级稳定性

**适用场景**:
- 量化交易研究：获取实时市场数据，进行策略回测和因子分析
- 金融分析与投研：自动化采集和整理多资产类别的财务数据，生成分析报告
- AI 交易代理开发：基于平台数据构建智能投顾或自动化交易系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,806 |
| 语言 | HTML |
| Forks | 20,930 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有近16万星标的社区驱动型AI提示词平台，支持ChatGPT、Claude、Gemini等多模型，提供了自托管部署选项，适合企业和个人用户免费使用、分享和收藏提示词，是学习提示工程和构建团队提示词库的绝佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构和良好的开发体验
- 支持多种大语言模型（ChatGPT、Claude、Gemini、GPT-4），实现跨平台的提示词兼容
- 开源且支持自托管部署，满足企业级隐私合规需求
- 采用社区驱动的模式，拥有丰富的提示词资源库和持续更新的内容
- 基于静态站点生成（HTML），加载速度快，SEO 友好，便于内容分发

**适用场景**:
- 个人开发者学习AI提示工程，通过参考社区优秀提示词提升LLM交互效果
- 企业团队自建提示词库，保护内部知识和数据隐私，避免使用第三方服务
- AI爱好者收集整理不同场景的提示词模板，提升日常工作和创作效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,838 |
| 语言 | Jupyter Notebook |
| Forks | 13,950 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,747 |
| 语言 | TypeScript |
| Forks | 3,654 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,433 |
| 语言 | Python |
| Forks | 32,879 |
| Issues | 2,345 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,741 |
| 语言 | Python |
| Forks | 15,636 |
| Issues | 4,293 |
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
| Stars | 108,896 |
| 语言 | Python |
| Forks | 12,640 |
| Issues | 3,979 |
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
| Stars | 99,158 |
| 语言 | Python |
| Forks | 27,499 |
| Issues | 18,525 |
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
| Stars | 33,572 |
| 语言 | Jupyter Notebook |
| Forks | 5,546 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 🛠️ 开发工具 (19 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,260 |
| 语言 | JavaScript |
| Forks | 24,410 |
| Issues | 99 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个经过15万+用户验证的AI代理性能优化框架，支持Claude Code、Codex、Cursor等主流AI编程工具，通过Skills、Memory和Security机制显著提升开发效率，是目前最全面的AI代码助手增强系统。

**技术亮点**:
- 多AI代理兼容：统一支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具框架
- 性能优化系统：专门针对agent harness的性能调优，提升响应速度和资源利用率
- Memory机制：实现智能记忆系统，让AI代理能够跨会话保持上下文连贯性
- 安全沙箱设计：内置Security模块，确保AI代码执行环境的安全性
- MCP协议支持：遵循Model Context Protocol标准，便于扩展和集成

**适用场景**:
- 企业级AI代码助手集成：帮助团队统一管理多种AI编程工具，提升整体开发效率
- 个人开发者效率提升：通过Skills和Instincts机制，让AI更懂你的编码习惯和项目需求
- AI代理系统开发：为开发者提供构建高性能AI代理的参考架构和最佳实践



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,427 |
| 语言 | Go |
| Forks | 3,953 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在无需 GPU 的情况下运行 LLM、图像生成、语音合成、目标检测等多种 AI 模型，提供统一的 API 接口让开发者轻松集成各种 AI 能力，特别适合需要数据隐私保护和私有化部署的企业场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）、目标检测等多种模型类型
- 无 GPU 依赖运行：通过优化的推理引擎，在 CPU 上也能高效运行各类 AI 模型，降低硬件门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络下的模型共享和协作推理
- 丰富的协议支持：支持 MCP（Model Context Protocol）、OpenAI 兼容 API、Rerank 等多种协议，便于现有应用迁移
- Go 语言实现：高性能、高并发、低内存占用的运行时环境，适合生产环境部署

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下，为企业内部系统提供文本生成、智能问答、文档分析等 AI 能力，确保数据隐私合规
- 本地开发与测试环境：开发者可以在本地快速原型开发和测试 AI 应用，无需申请云 API 密钥或支付调用费用
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 推理能力，实现本地化的图像识别、语音交互等功能



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,276 |
| 语言 | Python |
| Forks | 8,956 |
| Issues | 402 |
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
| Stars | 51,853 |
| 语言 | TypeScript |
| Forks | 4,161 |
| Issues | 532 |
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
| Stars | 184,200 |
| 语言 | TypeScript |
| Forks | 56,830 |
| Issues | 1,468 |
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
| Stars | 157,038 |
| 语言 | Python |
| Forks | 12,939 |
| Issues | 2,471 |
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
| Stars | 97,249 |
| 语言 | Python |
| Forks | 9,085 |
| Issues | 182 |
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
| Stars | 81,161 |
| 语言 | Python |
| Forks | 9,434 |
| Issues | 255 |
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
| Stars | 183,897 |
| 语言 | TypeScript |
| Forks | 39,218 |
| Issues | 16,342 |
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
| Stars | 94,126 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 294 |
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
| Stars | 78,925 |
| 语言 | TypeScript |
| Forks | 5,800 |
| Issues | 766 |
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
| Stars | 77,128 |
| 语言 | TypeScript |
| Forks | 6,610 |
| Issues | 142 |
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
| Stars | 79,497 |
| 语言 | Go |
| Forks | 2,774 |
| Issues | 313 |
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
| Stars | 76,477 |
| 语言 | Go |
| Forks | 2,758 |
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
| Stars | 43,843 |
| 语言 | Go |
| Forks | 8,267 |
| Issues | 956 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### spf13/cobra

**描述**: A Commander for modern Go CLI interactions

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,683 |
| 语言 | Go |
| Forks | 3,117 |
| Issues | 363 |
| Topics | cli, cli-app, cobra, cobra-generator, cobra-library, command, command-cobra, command-line, commandline, go, golang, golang-application, golang-library, posix, posix-compliant-flags, subcommands |
| 许可证 | Apache License 2.0 |


### charmbracelet/bubbletea

**描述**: A powerful little TUI framework 🏗

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,594 |
| 语言 | Go |
| Forks | 1,194 |
| Issues | 166 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
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
| Stars | 423,100 |
| 语言 | Python |
| Forks | 46,069 |
| Issues | 1,250 |
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
| Stars | 75,581 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 714 |
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
| Stars | 51,853 |
| 语言 | TypeScript |
| Forks | 4,161 |
| Issues | 532 |
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
| Stars | 184,200 |
| 语言 | TypeScript |
| Forks | 56,830 |
| Issues | 1,468 |
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
| Stars | 51,625 |
| 语言 | Go |
| Forks | 10,322 |
| Issues | 238 |
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
| Stars | 121,727 |
| 语言 | Go |
| Forks | 42,861 |
| Issues | 2,750 |
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
| Stars | 71,497 |
| 语言 | Go |
| Forks | 18,914 |
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
| Stars | 54,918 |
| 语言 | Go |
| Forks | 6,580 |
| Issues | 2,830 |
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
| Stars | 94,126 |
| 语言 | TypeScript |
| Forks | 9,420 |
| Issues | 294 |
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
| Stars | 76,789 |
| 语言 | TypeScript |
| Forks | 6,653 |
| Issues | 405 |
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
| Stars | 85,293 |
| 语言 | JavaScript |
| Forks | 7,645 |
| Issues | 720 |
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
| Stars | 69,873 |
| 语言 | Go |
| Forks | 1,911 |
| Issues | 319 |
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
| Stars | 62,708 |
| 语言 | Go |
| Forks | 5,916 |
| Issues | 788 |
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
| Stars | 58,893 |
| 语言 | Go |
| Forks | 4,273 |
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
| Stars | 47,503 |
| 语言 | Go |
| Forks | 5,043 |
| Issues | 981 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
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
| Stars | 85,293 |
| 语言 | JavaScript |
| Forks | 7,645 |
| Issues | 720 |
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
| Stars | 63,604 |
| 语言 | Go |
| Forks | 10,331 |
| Issues | 741 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (14 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,427 |
| 语言 | Go |
| Forks | 3,953 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在无需 GPU 的情况下运行 LLM、图像生成、语音合成、目标检测等多种 AI 模型，提供统一的 API 接口让开发者轻松集成各种 AI 能力，特别适合需要数据隐私保护和私有化部署的企业场景。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、音频生成（MusicGen）、语音合成（TTS）、目标检测等多种模型类型
- 无 GPU 依赖运行：通过优化的推理引擎，在 CPU 上也能高效运行各类 AI 模型，降低硬件门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络下的模型共享和协作推理
- 丰富的协议支持：支持 MCP（Model Context Protocol）、OpenAI 兼容 API、Rerank 等多种协议，便于现有应用迁移
- Go 语言实现：高性能、高并发、低内存占用的运行时环境，适合生产环境部署

**适用场景**:
- 企业私有化 AI 部署：在不依赖云服务的情况下，为企业内部系统提供文本生成、智能问答、文档分析等 AI 能力，确保数据隐私合规
- 本地开发与测试环境：开发者可以在本地快速原型开发和测试 AI 应用，无需申请云 API 密钥或支付调用费用
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 推理能力，实现本地化的图像识别、语音交互等功能



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,249 |
| 语言 | Python |
| Forks | 9,085 |
| Issues | 182 |
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
| Stars | 87,276 |
| 语言 | Python |
| Forks | 33,810 |
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
| Stars | 100,066 |
| 语言 | TypeScript |
| Forks | 27,162 |
| Issues | 1,112 |
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
| Stars | 78,925 |
| 语言 | TypeScript |
| Forks | 5,800 |
| Issues | 766 |
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
| Stars | 68,943 |
| 语言 | JavaScript |
| Forks | 23,133 |
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
| Stars | 55,963 |
| 语言 | JavaScript |
| Forks | 10,218 |
| Issues | 362 |
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
| Stars | 51,796 |
| 语言 | JavaScript |
| Forks | 4,704 |
| Issues | 1,461 |
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
| Stars | 88,321 |
| 语言 | Go |
| Forks | 8,570 |
| Issues | 674 |
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
| Stars | 71,573 |
| 语言 | Go |
| Forks | 4,694 |
| Issues | 247 |
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
| Stars | 57,629 |
| 语言 | Go |
| Forks | 3,288 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### charmbracelet/bubbletea

**描述**: A powerful little TUI framework 🏗

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,594 |
| 语言 | Go |
| Forks | 1,194 |
| Issues | 166 |
| Topics | cli, elm-architecture, framework, functional, go, golang, hacktoberfest, tui |
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
| Stars | 423,100 |
| 语言 | Python |
| Forks | 46,069 |
| Issues | 1,250 |
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
| Stars | 75,581 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 714 |
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
| Stars | 100,894 |
| 语言 | TypeScript |
| Forks | 12,088 |
| Issues | 969 |
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
| Stars | 58,377 |
| 语言 | JavaScript |
| Forks | 6,316 |
| Issues | 324 |
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
| Stars | 43,817 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,180 |
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
| Stars | 51,625 |
| 语言 | Go |
| Forks | 10,322 |
| Issues | 238 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (7 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,806 |
| 语言 | HTML |
| Forks | 20,930 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有近16万星标的社区驱动型AI提示词平台，支持ChatGPT、Claude、Gemini等多模型，提供了自托管部署选项，适合企业和个人用户免费使用、分享和收藏提示词，是学习提示工程和构建团队提示词库的绝佳资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的 Web 应用架构和良好的开发体验
- 支持多种大语言模型（ChatGPT、Claude、Gemini、GPT-4），实现跨平台的提示词兼容
- 开源且支持自托管部署，满足企业级隐私合规需求
- 采用社区驱动的模式，拥有丰富的提示词资源库和持续更新的内容
- 基于静态站点生成（HTML），加载速度快，SEO 友好，便于内容分发

**适用场景**:
- 个人开发者学习AI提示工程，通过参考社区优秀提示词提升LLM交互效果
- 企业团队自建提示词库，保护内部知识和数据隐私，避免使用第三方服务
- AI爱好者收集整理不同场景的提示词模板，提升日常工作和创作效率



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,767 |
| 语言 | TypeScript |
| Forks | 8,828 |
| Issues | 87 |
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
| Stars | 37,079 |
| 语言 | Python |
| Forks | 4,387 |
| Issues | 95 |
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
| Stars | 89,719 |
| 语言 | TypeScript |
| Forks | 10,008 |
| Issues | 2,234 |
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
| Stars | 87,393 |
| 语言 | TypeScript |
| Forks | 8,873 |
| Issues | 1,647 |
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
| Stars | 127,478 |
| 语言 | JavaScript |
| Forks | 12,482 |
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
| Stars | 170,054 |
| 语言 | Go |
| Forks | 13,142 |
| Issues | 177 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,328 |
| 语言 | Shell |
| Forks | 12,841 |
| Issues | 91 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,051 |
| 语言 | Python |
| Forks | 6,566 |
| Issues | 69 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,682 |
| 语言 | Python |
| Forks | 13,187 |
| Issues | 119 |
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
| Stars | 88,277 |
| 语言 | Python |
| Forks | 7,586 |
| Issues | 630 |
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
| Stars | 135,244 |
| 语言 | Unknown |
| Forks | 33,985 |
| Issues | 146 |
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
| Stars | 385,571 |
| 语言 | Python |
| Forks | 66,105 |
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
| Stars | 114,619 |
| 语言 | TypeScript |
| Forks | 5,911 |
| Issues | 23 |
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
| Stars | 110,879 |
| 语言 | TypeScript |
| Forks | 8,057 |
| Issues | 260 |
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
| Stars | 53,470 |
| 语言 | JavaScript |
| Forks | 4,488 |
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
| Stars | 48,152 |
| 语言 | Go |
| Forks | 10,288 |
| Issues | 1,886 |
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
| Stars | 103,826 |
| 语言 | C++ |
| Forks | 16,877 |
| Issues | 1,504 |
| Topics | ggml |
| 许可证 | MIT License |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,151 |
| 语言 | TypeScript |
| Forks | 10,315 |
| Issues | 350 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,509 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,024 |
| 语言 | Unknown |
| Forks | 3,417 |
| Issues | 59 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 292,511 |
| 语言 | Python |
| Forks | 27,685 |
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
| Stars | 219,640 |
| 语言 | Python |
| Forks | 50,333 |
| Issues | 926 |
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
| Stars | 97,815 |
| 语言 | Python |
| Forks | 12,042 |
| Issues | 119 |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,039 |
| 语言 | Python |
| Forks | 37,244 |
| Issues | 3,608 |
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
| Stars | 77,677 |
| 语言 | Python |
| Forks | 45,150 |
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
| Stars | 76,911 |
| 语言 | Python |
| Forks | 16,848 |
| Issues | 22 |
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
| Stars | 442,973 |
| 语言 | TypeScript |
| Forks | 44,298 |
| Issues | 199 |
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
| Stars | 353,003 |
| 语言 | TypeScript |
| Forks | 43,928 |
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
| Stars | 121,123 |
| 语言 | TypeScript |
| Forks | 13,284 |
| Issues | 2,969 |
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
| Stars | 112,411 |
| 语言 | TypeScript |
| Forks | 8,542 |
| Issues | 1,823 |
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
| Stars | 108,559 |
| 语言 | TypeScript |
| Forks | 13,352 |
| Issues | 5,024 |
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
| Stars | 97,913 |
| 语言 | TypeScript |
| Forks | 5,396 |
| Issues | 699 |
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
| Stars | 97,782 |
| 语言 | TypeScript |
| Forks | 54,588 |
| Issues | 1,354 |
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
| Stars | 94,587 |
| 语言 | TypeScript |
| Forks | 5,192 |
| Issues | 111 |
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
| Stars | 83,808 |
| 语言 | TypeScript |
| Forks | 10,388 |
| Issues | 401 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,113 |
| 语言 | TypeScript |
| Forks | 7,587 |
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
| Stars | 79,939 |
| 语言 | TypeScript |
| Forks | 8,057 |
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
| Stars | 244,545 |
| 语言 | JavaScript |
| Forks | 50,940 |
| Issues | 1,223 |
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
| Stars | 116,756 |
| 语言 | JavaScript |
| Forks | 35,351 |
| Issues | 2,617 |
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
| Stars | 111,953 |
| 语言 | JavaScript |
| Forks | 36,325 |
| Issues | 541 |
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
| Stars | 109,024 |
| 语言 | JavaScript |
| Forks | 11,637 |
| Issues | 264 |
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
| Stars | 98,169 |
| 语言 | JavaScript |
| Forks | 32,682 |
| Issues | 1,596 |
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
| Stars | 95,610 |
| 语言 | JavaScript |
| Forks | 15,361 |
| Issues | 64 |
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
| Stars | 86,314 |
| 语言 | JavaScript |
| Forks | 4,889 |
| Issues | 987 |
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
| Stars | 71,001 |
| 语言 | JavaScript |
| Forks | 16,810 |
| Issues | 894 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,322 |
| 语言 | JavaScript |
| Forks | 9,190 |
| Issues | 0 |
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
| Stars | 65,835 |
| 语言 | JavaScript |
| Forks | 9,374 |
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
| Stars | 62,774 |
| 语言 | JavaScript |
| Forks | 4,008 |
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
| Stars | 60,455 |
| 语言 | JavaScript |
| Forks | 5,648 |
| Issues | 69 |
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
| Forks | 20,477 |
| Issues | 95 |
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
| Stars | 57,427 |
| 语言 | JavaScript |
| Forks | 12,306 |
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
| Stars | 53,133 |
| 语言 | JavaScript |
| Forks | 10,604 |
| Issues | 457 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,516 |
| 语言 | JavaScript |
| Forks | 11,475 |
| Issues | 235 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,263 |
| 语言 | JavaScript |
| Forks | 10,343 |
| Issues | 132 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,625 |
| 语言 | JavaScript |
| Forks | 2,428 |
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
| Stars | 133,487 |
| 语言 | Go |
| Forks | 18,917 |
| Issues | 9,947 |
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
| Stars | 105,934 |
| 语言 | Go |
| Forks | 15,001 |
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
| Stars | 87,610 |
| 语言 | Go |
| Forks | 8,238 |
| Issues | 263 |
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
| Stars | 81,750 |
| 语言 | Go |
| Forks | 4,994 |
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
| Stars | 68,625 |
| 语言 | Go |
| Forks | 3,217 |
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
| Stars | 56,662 |
| 语言 | Go |
| Forks | 5,033 |
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
| Stars | 50,984 |
| 语言 | Go |
| Forks | 21,884 |
| Issues | 393 |
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
| Stars | 49,314 |
| 语言 | Go |
| Forks | 7,955 |
| Issues | 558 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,908 |
| 语言 | Python |
| Forks | 55,409 |
| Issues | 527 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,045 |
| 语言 | Python |
| Forks | 7,211 |
| Issues | 484 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,763 |
| 语言 | TypeScript |
| Forks | 16,499 |
| Issues | 44 |
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
| Stars | 79,047 |
| 语言 | JavaScript |
| Forks | 32,570 |
| Issues | 278 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,320 |
| 语言 | JavaScript |
| Forks | 7,134 |
| Issues | 141 |
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
| Stars | 151,304 |
| 语言 | Python |
| Forks | 11,522 |
| Issues | 327 |
| Topics | awesome, github, hellogithub, python |
