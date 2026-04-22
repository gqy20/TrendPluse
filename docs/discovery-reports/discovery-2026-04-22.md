# 项目发现报告 (2026-04-22)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
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
| Stars | 133,388 |
| 语言 | Python |
| Forks | 18,926 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 交互界面，支持 Ollama 和 OpenAI API 等多种后端，133k+ Stars 证明其成熟度和社区认可度，无需编写代码即可快速部署功能完整的 LLM 聊天界面，特别适合追求数据隐私和成本控制的用户自托管使用。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，灵活切换不同 LLM 提供商
- RAG 能力：内置检索增强生成功能，支持文档上传和知识库问答
- 开源自托管：提供完整的前后端代码，支持 Docker 一键部署，保障数据隐私
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时流式输出
- MCP 协议支持：支持 Model Context Protocol，扩展与其他工具和服务的集成能力

**适用场景**:
- 个人 AI 助手：个人用户在本地运行开源模型（如 Llama、Mistral）进行日常对话、代码编写、知识查询
- 企业内部知识库：企业使用 RAG 功能构建私有知识库系统，员工通过对话方式快速检索内部文档
- 开发测试环境：开发者测试不同 LLM API 的效果，对比模型性能，选择最适合业务场景的方案



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,461 |
| 语言 | Python |
| Forks | 16,012 |
| Issues | 6,287 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 由顶尖开源 AI 研究团队 NousResearch 开发，支持 Claude、ChatGPT、Codex 等多主流 AI 服务商，拥有 11 万+ Stars 的高人气社区验证，具备生产级可用性，是构建智能自动化工作流的可靠选择。

**技术亮点**:
- 多 AI 提供商支持：集成 Anthropic Claude、OpenAI ChatGPT、Codex 等主流大语言模型服务
- MIT 开源许可：完全开源可商用，社区驱动迭代活跃
- 模块化 Agent 架构：支持灵活的工具调用、任务规划和执行流程
- Python 原生实现：便于与现有 Python 生态集成（如 LangChain、FastAPI）
- 企业级稳定性：高 Stars 量验证的项目成熟度和稳定性

**适用场景**:
- 企业智能工作流自动化：通过 AI Agent 编排复杂业务流程，如客户服务、数据处理、报告生成
- 个人开发者 AI 助手：构建私人 AI 助手实现代码开发、文档撰写、邮件处理等日常任务
- 多模型对比与集成：利用多 AI 提供商支持进行模型能力对比或实现模型冗余备份



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,761 |
| 语言 | Python |
| Forks | 8,899 |
| Issues | 2,989 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ stars），将先进 RAG 技术与 Agent 能力深度融合，支持多模态文档理解、GraphRAG 和 MCP 协议，为企业级 LLM 应用提供强大的知识检索和上下文管理能力。

**技术亮点**:
- 深度融合 RAG 与 Agent 能力，支持复杂推理链路和工作流自动化编排
- 强大的多模态文档理解引擎，支持 PDF、Word、Excel 等多种格式的智能解析和结构化提取
- 支持 GraphRAG 知识图谱增强检索，提升关系型知识的召回效果
- 提供 MCP (Model Context Protocol) 协议支持，增强与外部工具和系统的互操作性
- 兼容多种 LLM 提供商（OpenAI、DeepSeek、Ollama 等），支持本地部署和云端调用

**适用场景**:
- 企业级智能知识库问答系统：基于私有知识库构建精准的 AI 问答助手
- 复杂文档分析场景：对合同、报告、手册等进行智能理解和信息抽取
- Agent 工作流自动化：构建多步骤推理和工具调用的智能代理应用
- RAG 应用快速开发：提供可视化配置界面，降低 RAG 系统开发门槛



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 164,132 |
| 语言 | JavaScript |
| Forks | 25,474 |
| Issues | 141 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Cursor、Codex、Opencode 等主流工具，拥有 16 万+ Stars，集成了 Skills、Memory、Security 等核心模块，能显著提升开发者使用 AI 辅助编程的效率和质量。

**技术亮点**:
- 多 Agent 框架兼容：统一支持 Claude Code、Cursor、Codex、Opencode 等主流 AI 编码工具，提供标准化的性能优化接口
- Advanced Memory System：实现智能记忆管理机制，让 AI Agent 能够跨会话保持上下文理解能力
- Security & Safety First：内置多层安全防护机制，确保 AI Agent 操作的企业级安全性
- Skills & Instincts 机制：通过预定义技能库和本能反应系统，提升 AI Agent 的任务执行能力
- MCP (Model Context Protocol) 支持：集成最新的模型上下文协议标准

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编程工具、优化团队协作效率的中大型开发组织
- 个人开发者效率提升：希望通过配置 Skills 和 Memory 系统，让 AI 编程助手更懂自己的代码风格和项目架构



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,704 |
| 语言 | Go |
| Forks | 3,997 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持 LLM、视觉、语音、图像生成等多模态模型，无需 GPU 即可运行，为开发者和企业提供了隐私友好、成本可控的私有化 AI 部署方案。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和良好的并发处理能力
- 支持多种模型架构：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS）、音乐生成（MusicGen）、目标检测等
- 支持 libp2p 去中心化分布式部署，可构建分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- 无需 GPU 即可在普通硬件上运行，降低了 AI 部署的硬件门槛

**适用场景**:
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），可完全在本地运行 AI 服务，数据不出本地
- 开发者快速原型开发：通过 API 快速集成 AI 能力，支持 Llama 等开源模型，无需依赖云服务
- 边缘计算与物联网：在资源受限的硬件上部署轻量级 AI 推理，实现本地化的智能处理



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,492 |
| 语言 | TypeScript |
| Forks | 14,957 |
| Issues | 707 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级别的 AI Agent 协作平台，拥有 75k+ Stars，通过 MCP 协议实现多 AI 模型集成，并支持多 Agent 团队协作设计，为构建智能 Agent 工作流提供了完整的开箱即用解决方案。

**技术亮点**:
- MCP (Model Context Protocol) 协议支持，实现多 AI 提供商（OpenAI GPT、Claude、DeepSeek、Gemini）的统一集成
- 多 Agent 协作框架，支持设计、构建和管理 Agent 团队，实现复杂任务的分工协作
- 内置知识库系统，支持 RAG（检索增强生成）能力，提升 Agent 知识问答准确性
- TypeScript/React 现代技术栈，提供完整的类型安全和高质量代码基础
- 生产级架构设计，支持扩展的 Agent 生态系统和模块化组件设计

**适用场景**:
- 企业级 AI 工作流自动化：通过多 Agent 协作处理复杂业务流程，如客户服务、数据分析、内容生成等需要多种 AI 能力协同的任务
- 个人开发者快速构建 AI 应用：利用现成的 Agent 组件和 MCP 集成，快速搭建支持多种大模型的智能应用
- AI Agent 团队协作平台：设计和管理专业化的 Agent 团队，让不同角色的 Agent 协同完成知识管理、编程辅助等专业任务



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,476 |
| 语言 | Python |
| Forks | 8,613 |
| Issues | 983 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个高度成熟的 LLM 微调框架，拥有 7 万+ stars 和 ACL 2024 学术认证，支持 100+ 主流大模型（Llama3/Qwen/Deepseek/Gemma 等）的统一微调，融合 LoRA/QLoRA/RLHF 等多种技术，一站式解决个人开发者和企业的模型定制需求。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 Llama、Qwen、Deepseek、Gemma、Mistral 等主流模型系列
- 集成多种微调方法：LoRA、QLoRA、Prefix-tuning、Prompt Tuning、RLHF (PPO/DPO/KTO) 等，支持全参数微调和高效参数微调
- 内置多种量化技术：AWQ、GPTQ、GGUF、bitsandbytes，支持从 4bit 到 8bit 的量化训练与推理
- 提供友好的 Web UI 和 CLI 工具，支持模型训练监控、预览和 API 服务部署，开箱即用
- 支持多模态大模型 (VLM) 微调，兼容视觉-语言模型，支持 agent 工具调用和函数识别能力

**适用场景**:
- 企业级 AI 应用开发：快速基于自有数据微调领域专属模型，应用于客服、知识库、文档分析等业务场景
- 学术研究与实验：便捷对比不同微调方法（LoRA vs QLoRA vs RLHF）和不同模型的效果差异，加速论文实验
- 个人开发者快速上手：零基础通过 WebUI 一键微调 Llama3/Qwen 等开源模型，定制私人 AI 助手或本地知识库
- 模型量化与部署：支持 GGUF 格式导出，在消费级 GPU 上部署运行 7B-70B 参数模型



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,712 |
| 语言 | TypeScript |
| Forks | 5,564 |
| Issues | 124 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过将 Claude Code 的每次编码会话转化为可检索的长期记忆，解决了 AI 编程助手缺乏上下文连续性的核心痛点，让开发者能够在多会话项目中保持连贯的 AI 辅助体验，显著提升开发效率。

**技术亮点**:
- 基于 Claude agent-sdk 的智能压缩引擎，自动提炼编码会话中的关键信息和决策
- 集成 ChromaDB 向量数据库，支持语义级别的上下文检索和相似度匹配
- 采用 SQLite 本地持久化存储，保障数据隐私的同时支持离线访问
- RAG（检索增强生成）架构设计，将历史记忆无缝注入未来对话上下文
- 插件化设计，无缝集成 Claude Code，无需改变现有工作流程

**适用场景**:
- 长时间多会话项目开发：开发者可在间隔数天的项目中快速恢复上下文，避免重复解释项目结构和需求
- 复杂代码库维护：AI 代理能够记住之前的技术决策、重构思路和代码规范，保持维护一致性
- 个人开发者效率提升：自动追踪编码过程中的重要洞察和解决方案，构建个人知识库供日后参考



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,388 |
| 语言 | HTML |
| Forks | 4,660 |
| Issues | 16 |
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
| Stars | 43,640 |
| 语言 | Python |
| Forks | 9,977 |
| Issues | 354 |
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
| Stars | 45,924 |
| 语言 | Java |
| Forks | 15,934 |
| Issues | 13 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 4,734 |
| Issues | 95 |
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
| Stars | 39,033 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 67 |
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
| Stars | 111,592 |
| 语言 | TypeScript |
| Forks | 7,116 |
| Issues | 288 |
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
| Stars | 58,777 |
| 语言 | JavaScript |
| Forks | 6,352 |
| Issues | 329 |
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
| Stars | 71,770 |
| 语言 | Python |
| Forks | 9,040 |
| Issues | 407 |
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
| Stars | 53,466 |
| 语言 | TypeScript |
| Forks | 4,314 |
| Issues | 604 |
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
| Stars | 106,916 |
| 语言 | Python |
| Forks | 15,693 |
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
| Stars | 89,502 |
| 语言 | Python |
| Forks | 10,226 |
| Issues | 225 |
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
| Stars | 52,165 |
| 语言 | TypeScript |
| Forks | 24,194 |
| Issues | 825 |
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
| Stars | 185,146 |
| 语言 | TypeScript |
| Forks | 57,038 |
| Issues | 1,556 |
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
| Stars | 155,149 |
| 语言 | Java |
| Forks | 46,148 |
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
| Stars | 147,262 |
| 语言 | Python |
| Forks | 8,829 |
| Issues | 954 |
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
| Stars | 58,338 |
| 语言 | Jupyter Notebook |
| Forks | 19,956 |
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
| Stars | 55,629 |
| 语言 | Python |
| Forks | 5,971 |
| Issues | 546 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,702 |
| 语言 | TypeScript |
| Forks | 9,169 |
| Issues | 103 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,196 |
| 语言 | Python |
| Forks | 2,164 |
| Issues | 98 |
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
| Stars | 33,997 |
| 语言 | Jupyter Notebook |
| Forks | 5,625 |
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
| Stars | 33,901 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 294 |
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
| Stars | 49,128 |
| 语言 | Rust |
| Forks | 3,140 |
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
| Stars | 133,388 |
| 语言 | Python |
| Forks | 18,926 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 交互界面，支持 Ollama 和 OpenAI API 等多种后端，133k+ Stars 证明其成熟度和社区认可度，无需编写代码即可快速部署功能完整的 LLM 聊天界面，特别适合追求数据隐私和成本控制的用户自托管使用。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，灵活切换不同 LLM 提供商
- RAG 能力：内置检索增强生成功能，支持文档上传和知识库问答
- 开源自托管：提供完整的前后端代码，支持 Docker 一键部署，保障数据隐私
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时流式输出
- MCP 协议支持：支持 Model Context Protocol，扩展与其他工具和服务的集成能力

**适用场景**:
- 个人 AI 助手：个人用户在本地运行开源模型（如 Llama、Mistral）进行日常对话、代码编写、知识查询
- 企业内部知识库：企业使用 RAG 功能构建私有知识库系统，员工通过对话方式快速检索内部文档
- 开发测试环境：开发者测试不同 LLM API 的效果，对比模型性能，选择最适合业务场景的方案



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,761 |
| 语言 | Python |
| Forks | 8,899 |
| Issues | 2,989 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ stars），将先进 RAG 技术与 Agent 能力深度融合，支持多模态文档理解、GraphRAG 和 MCP 协议，为企业级 LLM 应用提供强大的知识检索和上下文管理能力。

**技术亮点**:
- 深度融合 RAG 与 Agent 能力，支持复杂推理链路和工作流自动化编排
- 强大的多模态文档理解引擎，支持 PDF、Word、Excel 等多种格式的智能解析和结构化提取
- 支持 GraphRAG 知识图谱增强检索，提升关系型知识的召回效果
- 提供 MCP (Model Context Protocol) 协议支持，增强与外部工具和系统的互操作性
- 兼容多种 LLM 提供商（OpenAI、DeepSeek、Ollama 等），支持本地部署和云端调用

**适用场景**:
- 企业级智能知识库问答系统：基于私有知识库构建精准的 AI 问答助手
- 复杂文档分析场景：对合同、报告、手册等进行智能理解和信息抽取
- Agent 工作流自动化：构建多步骤推理和工具调用的智能代理应用
- RAG 应用快速开发：提供可视化配置界面，降低 RAG 系统开发门槛



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,492 |
| 语言 | TypeScript |
| Forks | 14,957 |
| Issues | 707 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级别的 AI Agent 协作平台，拥有 75k+ Stars，通过 MCP 协议实现多 AI 模型集成，并支持多 Agent 团队协作设计，为构建智能 Agent 工作流提供了完整的开箱即用解决方案。

**技术亮点**:
- MCP (Model Context Protocol) 协议支持，实现多 AI 提供商（OpenAI GPT、Claude、DeepSeek、Gemini）的统一集成
- 多 Agent 协作框架，支持设计、构建和管理 Agent 团队，实现复杂任务的分工协作
- 内置知识库系统，支持 RAG（检索增强生成）能力，提升 Agent 知识问答准确性
- TypeScript/React 现代技术栈，提供完整的类型安全和高质量代码基础
- 生产级架构设计，支持扩展的 Agent 生态系统和模块化组件设计

**适用场景**:
- 企业级 AI 工作流自动化：通过多 Agent 协作处理复杂业务流程，如客户服务、数据分析、内容生成等需要多种 AI 能力协同的任务
- 个人开发者快速构建 AI 应用：利用现成的 Agent 组件和 MCP 集成，快速搭建支持多种大模型的智能应用
- AI Agent 团队协作平台：设计和管理专业化的 Agent 团队，让不同角色的 Agent 协同完成知识管理、编程辅助等专业任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,712 |
| 语言 | TypeScript |
| Forks | 5,564 |
| Issues | 124 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过将 Claude Code 的每次编码会话转化为可检索的长期记忆，解决了 AI 编程助手缺乏上下文连续性的核心痛点，让开发者能够在多会话项目中保持连贯的 AI 辅助体验，显著提升开发效率。

**技术亮点**:
- 基于 Claude agent-sdk 的智能压缩引擎，自动提炼编码会话中的关键信息和决策
- 集成 ChromaDB 向量数据库，支持语义级别的上下文检索和相似度匹配
- 采用 SQLite 本地持久化存储，保障数据隐私的同时支持离线访问
- RAG（检索增强生成）架构设计，将历史记忆无缝注入未来对话上下文
- 插件化设计，无缝集成 Claude Code，无需改变现有工作流程

**适用场景**:
- 长时间多会话项目开发：开发者可在间隔数天的项目中快速恢复上下文，避免重复解释项目结构和需求
- 复杂代码库维护：AI 代理能够记住之前的技术决策、重构思路和代码规范，保持维护一致性
- 个人开发者效率提升：自动追踪编码过程中的重要洞察和解决方案，构建个人知识库供日后参考



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,924 |
| 语言 | Java |
| Forks | 15,934 |
| Issues | 13 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 4,734 |
| Issues | 95 |
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
| Stars | 39,033 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 67 |
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
| Stars | 101,258 |
| 语言 | TypeScript |
| Forks | 12,150 |
| Issues | 948 |
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
| Stars | 58,777 |
| 语言 | JavaScript |
| Forks | 6,352 |
| Issues | 329 |
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
| Stars | 106,916 |
| 语言 | Python |
| Forks | 15,693 |
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
| Stars | 76,211 |
| 语言 | Python |
| Forks | 10,280 |
| Issues | 233 |
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
| Stars | 52,165 |
| 语言 | TypeScript |
| Forks | 24,194 |
| Issues | 825 |
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
| Stars | 43,924 |
| 语言 | Go |
| Forks | 3,972 |
| Issues | 1,139 |
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
| Stars | 34,062 |
| 语言 | Python |
| Forks | 4,826 |
| Issues | 211 |
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
| Stars | 34,196 |
| 语言 | Python |
| Forks | 2,164 |
| Issues | 98 |
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
| Stars | 33,997 |
| 语言 | Jupyter Notebook |
| Forks | 5,625 |
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
| Stars | 33,901 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 294 |
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
| Stars | 133,388 |
| 语言 | Python |
| Forks | 18,926 |
| Issues | 287 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 提供了开箱即用的 AI 交互界面，支持 Ollama 和 OpenAI API 等多种后端，133k+ Stars 证明其成熟度和社区认可度，无需编写代码即可快速部署功能完整的 LLM 聊天界面，特别适合追求数据隐私和成本控制的用户自托管使用。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，灵活切换不同 LLM 提供商
- RAG 能力：内置检索增强生成功能，支持文档上传和知识库问答
- 开源自托管：提供完整的前后端代码，支持 Docker 一键部署，保障数据隐私
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时流式输出
- MCP 协议支持：支持 Model Context Protocol，扩展与其他工具和服务的集成能力

**适用场景**:
- 个人 AI 助手：个人用户在本地运行开源模型（如 Llama、Mistral）进行日常对话、代码编写、知识查询
- 企业内部知识库：企业使用 RAG 功能构建私有知识库系统，员工通过对话方式快速检索内部文档
- 开发测试环境：开发者测试不同 LLM API 的效果，对比模型性能，选择最适合业务场景的方案



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,461 |
| 语言 | Python |
| Forks | 16,012 |
| Issues | 6,287 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 由顶尖开源 AI 研究团队 NousResearch 开发，支持 Claude、ChatGPT、Codex 等多主流 AI 服务商，拥有 11 万+ Stars 的高人气社区验证，具备生产级可用性，是构建智能自动化工作流的可靠选择。

**技术亮点**:
- 多 AI 提供商支持：集成 Anthropic Claude、OpenAI ChatGPT、Codex 等主流大语言模型服务
- MIT 开源许可：完全开源可商用，社区驱动迭代活跃
- 模块化 Agent 架构：支持灵活的工具调用、任务规划和执行流程
- Python 原生实现：便于与现有 Python 生态集成（如 LangChain、FastAPI）
- 企业级稳定性：高 Stars 量验证的项目成熟度和稳定性

**适用场景**:
- 企业智能工作流自动化：通过 AI Agent 编排复杂业务流程，如客户服务、数据处理、报告生成
- 个人开发者 AI 助手：构建私人 AI 助手实现代码开发、文档撰写、邮件处理等日常任务
- 多模型对比与集成：利用多 AI 提供商支持进行模型能力对比或实现模型冗余备份



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,761 |
| 语言 | Python |
| Forks | 8,899 |
| Issues | 2,989 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（78k+ stars），将先进 RAG 技术与 Agent 能力深度融合，支持多模态文档理解、GraphRAG 和 MCP 协议，为企业级 LLM 应用提供强大的知识检索和上下文管理能力。

**技术亮点**:
- 深度融合 RAG 与 Agent 能力，支持复杂推理链路和工作流自动化编排
- 强大的多模态文档理解引擎，支持 PDF、Word、Excel 等多种格式的智能解析和结构化提取
- 支持 GraphRAG 知识图谱增强检索，提升关系型知识的召回效果
- 提供 MCP (Model Context Protocol) 协议支持，增强与外部工具和系统的互操作性
- 兼容多种 LLM 提供商（OpenAI、DeepSeek、Ollama 等），支持本地部署和云端调用

**适用场景**:
- 企业级智能知识库问答系统：基于私有知识库构建精准的 AI 问答助手
- 复杂文档分析场景：对合同、报告、手册等进行智能理解和信息抽取
- Agent 工作流自动化：构建多步骤推理和工具调用的智能代理应用
- RAG 应用快速开发：提供可视化配置界面，降低 RAG 系统开发门槛



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 164,132 |
| 语言 | JavaScript |
| Forks | 25,474 |
| Issues | 141 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Cursor、Codex、Opencode 等主流工具，拥有 16 万+ Stars，集成了 Skills、Memory、Security 等核心模块，能显著提升开发者使用 AI 辅助编程的效率和质量。

**技术亮点**:
- 多 Agent 框架兼容：统一支持 Claude Code、Cursor、Codex、Opencode 等主流 AI 编码工具，提供标准化的性能优化接口
- Advanced Memory System：实现智能记忆管理机制，让 AI Agent 能够跨会话保持上下文理解能力
- Security & Safety First：内置多层安全防护机制，确保 AI Agent 操作的企业级安全性
- Skills & Instincts 机制：通过预定义技能库和本能反应系统，提升 AI Agent 的任务执行能力
- MCP (Model Context Protocol) 支持：集成最新的模型上下文协议标准

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编程工具、优化团队协作效率的中大型开发组织
- 个人开发者效率提升：希望通过配置 Skills 和 Memory 系统，让 AI 编程助手更懂自己的代码风格和项目架构



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,492 |
| 语言 | TypeScript |
| Forks | 14,957 |
| Issues | 707 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级别的 AI Agent 协作平台，拥有 75k+ Stars，通过 MCP 协议实现多 AI 模型集成，并支持多 Agent 团队协作设计，为构建智能 Agent 工作流提供了完整的开箱即用解决方案。

**技术亮点**:
- MCP (Model Context Protocol) 协议支持，实现多 AI 提供商（OpenAI GPT、Claude、DeepSeek、Gemini）的统一集成
- 多 Agent 协作框架，支持设计、构建和管理 Agent 团队，实现复杂任务的分工协作
- 内置知识库系统，支持 RAG（检索增强生成）能力，提升 Agent 知识问答准确性
- TypeScript/React 现代技术栈，提供完整的类型安全和高质量代码基础
- 生产级架构设计，支持扩展的 Agent 生态系统和模块化组件设计

**适用场景**:
- 企业级 AI 工作流自动化：通过多 Agent 协作处理复杂业务流程，如客户服务、数据分析、内容生成等需要多种 AI 能力协同的任务
- 个人开发者快速构建 AI 应用：利用现成的 Agent 组件和 MCP 集成，快速搭建支持多种大模型的智能应用
- AI Agent 团队协作平台：设计和管理专业化的 Agent 团队，让不同角色的 Agent 协同完成知识管理、编程辅助等专业任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,712 |
| 语言 | TypeScript |
| Forks | 5,564 |
| Issues | 124 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过将 Claude Code 的每次编码会话转化为可检索的长期记忆，解决了 AI 编程助手缺乏上下文连续性的核心痛点，让开发者能够在多会话项目中保持连贯的 AI 辅助体验，显著提升开发效率。

**技术亮点**:
- 基于 Claude agent-sdk 的智能压缩引擎，自动提炼编码会话中的关键信息和决策
- 集成 ChromaDB 向量数据库，支持语义级别的上下文检索和相似度匹配
- 采用 SQLite 本地持久化存储，保障数据隐私的同时支持离线访问
- RAG（检索增强生成）架构设计，将历史记忆无缝注入未来对话上下文
- 插件化设计，无缝集成 Claude Code，无需改变现有工作流程

**适用场景**:
- 长时间多会话项目开发：开发者可在间隔数天的项目中快速恢复上下文，避免重复解释项目结构和需求
- 复杂代码库维护：AI 代理能够记住之前的技术决策、重构思路和代码规范，保持维护一致性
- 个人开发者效率提升：自动追踪编码过程中的重要洞察和解决方案，构建个人知识库供日后参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,415 |
| 语言 | HTML |
| Forks | 20,983 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万stars的开源提示词社区平台，提供了数千个经过验证的高质量ChatGPT提示词模板，支持多模态AI模型（GPT-4、Claude、Gemini等），并且可以完全私有化部署，非常适合企业级应用。

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用，提供完整的类型安全保证
- 支持私有化部署，企业可完全掌控数据，确保隐私合规
- 收录超过5000+经过社区验证的优质提示词模板
- 多模型支持：OpenAI GPT-4、Claude、Gemini 等主流 LLM
- 完整的社区功能：分享、发现、收藏、分类检索

**适用场景**:
- 个人用户快速获取高质量提示词，提升 AI 交互效率
- 企业团队私有化部署，构建内部提示词知识库
- 开发者参考项目架构，学习 AI 应用的开发模式



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,243 |
| 语言 | Jupyter Notebook |
| Forks | 14,044 |
| Issues | 6 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,388 |
| 语言 | HTML |
| Forks | 4,660 |
| Issues | 16 |
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
| Stars | 43,640 |
| 语言 | Python |
| Forks | 9,977 |
| Issues | 354 |
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
| Stars | 43,468 |
| 语言 | Python |
| Forks | 2,256 |
| Issues | 141 |
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
| Stars | 58,777 |
| 语言 | JavaScript |
| Forks | 6,352 |
| Issues | 329 |
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
| Stars | 71,770 |
| 语言 | Python |
| Forks | 9,040 |
| Issues | 407 |
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
| Stars | 53,466 |
| 语言 | TypeScript |
| Forks | 4,314 |
| Issues | 604 |
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
| Stars | 52,165 |
| 语言 | TypeScript |
| Forks | 24,194 |
| Issues | 825 |
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
| Stars | 77,729 |
| 语言 | Python |
| Forks | 15,952 |
| Issues | 4,401 |
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
| Stars | 147,262 |
| 语言 | Python |
| Forks | 8,829 |
| Issues | 954 |
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
| Stars | 55,629 |
| 语言 | Python |
| Forks | 5,971 |
| Issues | 546 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,714 |
| 语言 | Go |
| Forks | 15,734 |
| Issues | 3,025 |
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
| Stars | 55,702 |
| 语言 | TypeScript |
| Forks | 9,169 |
| Issues | 103 |
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
| Stars | 48,050 |
| 语言 | Rust |
| Forks | 9,597 |
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
| Stars | 34,196 |
| 语言 | Python |
| Forks | 2,164 |
| Issues | 98 |
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
| Stars | 114,906 |
| 语言 | Python |
| Forks | 7,493 |
| Issues | 626 |
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
| Stars | 69,215 |
| 语言 | Python |
| Forks | 7,082 |
| Issues | 118 |
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
| Stars | 70,476 |
| 语言 | Python |
| Forks | 8,613 |
| Issues | 983 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个高度成熟的 LLM 微调框架，拥有 7 万+ stars 和 ACL 2024 学术认证，支持 100+ 主流大模型（Llama3/Qwen/Deepseek/Gemma 等）的统一微调，融合 LoRA/QLoRA/RLHF 等多种技术，一站式解决个人开发者和企业的模型定制需求。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，涵盖 Llama、Qwen、Deepseek、Gemma、Mistral 等主流模型系列
- 集成多种微调方法：LoRA、QLoRA、Prefix-tuning、Prompt Tuning、RLHF (PPO/DPO/KTO) 等，支持全参数微调和高效参数微调
- 内置多种量化技术：AWQ、GPTQ、GGUF、bitsandbytes，支持从 4bit 到 8bit 的量化训练与推理
- 提供友好的 Web UI 和 CLI 工具，支持模型训练监控、预览和 API 服务部署，开箱即用
- 支持多模态大模型 (VLM) 微调，兼容视觉-语言模型，支持 agent 工具调用和函数识别能力

**适用场景**:
- 企业级 AI 应用开发：快速基于自有数据微调领域专属模型，应用于客服、知识库、文档分析等业务场景
- 学术研究与实验：便捷对比不同微调方法（LoRA vs QLoRA vs RLHF）和不同模型的效果差异，加速论文实验
- 个人开发者快速上手：零基础通过 WebUI 一键微调 Llama3/Qwen 等开源模型，定制私人 AI 助手或本地知识库
- 模型量化与部署：支持 GGUF 格式导出，在消费级 GPU 上部署运行 7B-70B 参数模型



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,340 |
| 语言 | Python |
| Forks | 6,620 |
| Issues | 73 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，集成 AI 和机器学习能力，支持股票、加密货币、期权、衍生品等多类资产分析，为量化交易员和金融分析师提供一站式数据获取和可视化解决方案。

**技术亮点**:
- 支持多资产类别数据（股票、加密货币、期权、期货、固定收益等），提供统一的数据访问接口
- 深度集成 AI/ML 能力，支持机器学习驱动的金融分析和预测模型
- 模块化架构设计，支持自定义扩展和数据源集成
- 提供丰富的可视化组件和交互式图表，便于金融数据探索
- 基于 Python 生态系统，支持 Jupyter Notebook 集成和脚本自动化

**适用场景**:
- 量化交易研究：获取多市场数据、构建交易策略和回测分析
- 金融分析与报告：快速生成市场洞察、资产比较和投资组合分析报告
- AI 金融应用开发：构建智能投顾、风险预测和市场情绪分析等应用
- 投研团队协作：共享数据管道和分析模板，提升研究效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,415 |
| 语言 | HTML |
| Forks | 20,983 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万stars的开源提示词社区平台，提供了数千个经过验证的高质量ChatGPT提示词模板，支持多模态AI模型（GPT-4、Claude、Gemini等），并且可以完全私有化部署，非常适合企业级应用。

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用，提供完整的类型安全保证
- 支持私有化部署，企业可完全掌控数据，确保隐私合规
- 收录超过5000+经过社区验证的优质提示词模板
- 多模型支持：OpenAI GPT-4、Claude、Gemini 等主流 LLM
- 完整的社区功能：分享、发现、收藏、分类检索

**适用场景**:
- 个人用户快速获取高质量提示词，提升 AI 交互效率
- 企业团队私有化部署，构建内部提示词知识库
- 开发者参考项目架构，学习 AI 应用的开发模式



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,243 |
| 语言 | Jupyter Notebook |
| Forks | 14,044 |
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
| Stars | 159,759 |
| 语言 | Python |
| Forks | 32,977 |
| Issues | 2,342 |
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
| Stars | 77,729 |
| 语言 | Python |
| Forks | 15,952 |
| Issues | 4,401 |
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
| Stars | 109,656 |
| 语言 | Python |
| Forks | 12,767 |
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
| Stars | 99,352 |
| 语言 | Python |
| Forks | 27,566 |
| Issues | 18,569 |
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
| Stars | 33,997 |
| 语言 | Jupyter Notebook |
| Forks | 5,625 |
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
| Stars | 33,901 |
| 语言 | TypeScript |
| Forks | 3,674 |
| Issues | 294 |
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
| Stars | 164,132 |
| 语言 | JavaScript |
| Forks | 25,474 |
| Issues | 141 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 AI 编码代理的性能优化系统，支持 Claude Code、Cursor、Codex、Opencode 等主流工具，拥有 16 万+ Stars，集成了 Skills、Memory、Security 等核心模块，能显著提升开发者使用 AI 辅助编程的效率和质量。

**技术亮点**:
- 多 Agent 框架兼容：统一支持 Claude Code、Cursor、Codex、Opencode 等主流 AI 编码工具，提供标准化的性能优化接口
- Advanced Memory System：实现智能记忆管理机制，让 AI Agent 能够跨会话保持上下文理解能力
- Security & Safety First：内置多层安全防护机制，确保 AI Agent 操作的企业级安全性
- Skills & Instincts 机制：通过预定义技能库和本能反应系统，提升 AI Agent 的任务执行能力
- MCP (Model Context Protocol) 支持：集成最新的模型上下文协议标准

**适用场景**:
- 企业级 AI 开发团队：需要统一管理多个 AI 编程工具、优化团队协作效率的中大型开发组织
- 个人开发者效率提升：希望通过配置 Skills 和 Memory 系统，让 AI 编程助手更懂自己的代码风格和项目架构



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,704 |
| 语言 | Go |
| Forks | 3,997 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持 LLM、视觉、语音、图像生成等多模态模型，无需 GPU 即可运行，为开发者和企业提供了隐私友好、成本可控的私有化 AI 部署方案。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和良好的并发处理能力
- 支持多种模型架构：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS）、音乐生成（MusicGen）、目标检测等
- 支持 libp2p 去中心化分布式部署，可构建分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- 无需 GPU 即可在普通硬件上运行，降低了 AI 部署的硬件门槛

**适用场景**:
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），可完全在本地运行 AI 服务，数据不出本地
- 开发者快速原型开发：通过 API 快速集成 AI 能力，支持 Llama 等开源模型，无需依赖云服务
- 边缘计算与物联网：在资源受限的硬件上部署轻量级 AI 推理，实现本地化的智能处理



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,770 |
| 语言 | Python |
| Forks | 9,040 |
| Issues | 407 |
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
| Stars | 53,466 |
| 语言 | TypeScript |
| Forks | 4,314 |
| Issues | 604 |
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
| Stars | 185,146 |
| 语言 | TypeScript |
| Forks | 57,038 |
| Issues | 1,556 |
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
| Stars | 158,146 |
| 语言 | Python |
| Forks | 13,068 |
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
| Stars | 97,528 |
| 语言 | Python |
| Forks | 9,125 |
| Issues | 169 |
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
| Stars | 81,748 |
| 语言 | Python |
| Forks | 9,518 |
| Issues | 256 |
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
| Stars | 184,149 |
| 语言 | TypeScript |
| Forks | 39,345 |
| Issues | 16,581 |
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
| Stars | 94,167 |
| 语言 | TypeScript |
| Forks | 9,411 |
| Issues | 303 |
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
| Stars | 79,008 |
| 语言 | TypeScript |
| Forks | 5,820 |
| Issues | 774 |
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
| Stars | 79,706 |
| 语言 | Go |
| Forks | 2,789 |
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
| Stars | 76,867 |
| 语言 | Go |
| Forks | 2,778 |
| Issues | 956 |
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
| Stars | 43,984 |
| 语言 | Go |
| Forks | 8,308 |
| Issues | 981 |
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
| Stars | 75,557 |
| 语言 | JavaScript |
| Forks | 7,286 |
| Issues | 714 |
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
| Stars | 53,466 |
| 语言 | TypeScript |
| Forks | 4,314 |
| Issues | 604 |
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
| Stars | 185,146 |
| 语言 | TypeScript |
| Forks | 57,038 |
| Issues | 1,556 |
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
| Stars | 55,629 |
| 语言 | Python |
| Forks | 5,971 |
| Issues | 546 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,615 |
| 语言 | Go |
| Forks | 10,320 |
| Issues | 227 |
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
| Stars | 121,853 |
| 语言 | Go |
| Forks | 42,900 |
| Issues | 2,810 |
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
| Stars | 71,482 |
| 语言 | Go |
| Forks | 18,919 |
| Issues | 3,797 |
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
| Stars | 55,039 |
| 语言 | Go |
| Forks | 6,605 |
| Issues | 2,839 |
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
| Stars | 47,484 |
| 语言 | Go |
| Forks | 5,047 |
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
| Stars | 94,167 |
| 语言 | TypeScript |
| Forks | 9,411 |
| Issues | 303 |
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
| Stars | 77,584 |
| 语言 | TypeScript |
| Forks | 6,760 |
| Issues | 416 |
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
| Stars | 85,608 |
| 语言 | JavaScript |
| Forks | 7,667 |
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
| Stars | 69,989 |
| 语言 | Go |
| Forks | 1,920 |
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
| Stars | 62,827 |
| 语言 | Go |
| Forks | 5,933 |
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
| Stars | 59,092 |
| 语言 | Go |
| Forks | 4,292 |
| Issues | 30 |
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
| Stars | 85,608 |
| 语言 | JavaScript |
| Forks | 7,667 |
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
| Stars | 63,710 |
| 语言 | Go |
| Forks | 10,348 |
| Issues | 750 |
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
| Stars | 45,704 |
| 语言 | Go |
| Forks | 3,997 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 推理引擎，支持 LLM、视觉、语音、图像生成等多模态模型，无需 GPU 即可运行，为开发者和企业提供了隐私友好、成本可控的私有化 AI 部署方案。

**技术亮点**:
- 基于 Go 语言开发，具备高性能和良好的并发处理能力
- 支持多种模型架构：LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS）、音乐生成（MusicGen）、目标检测等
- 支持 libp2p 去中心化分布式部署，可构建分布式 AI 推理网络
- 提供 RESTful API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- 无需 GPU 即可在普通硬件上运行，降低了 AI 部署的硬件门槛

**适用场景**:
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律），可完全在本地运行 AI 服务，数据不出本地
- 开发者快速原型开发：通过 API 快速集成 AI 能力，支持 Llama 等开源模型，无需依赖云服务
- 边缘计算与物联网：在资源受限的硬件上部署轻量级 AI 推理，实现本地化的智能处理



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,528 |
| 语言 | Python |
| Forks | 9,125 |
| Issues | 169 |
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
| Stars | 87,307 |
| 语言 | Python |
| Forks | 33,826 |
| Issues | 434 |
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
| Stars | 100,049 |
| 语言 | TypeScript |
| Forks | 27,181 |
| Issues | 1,124 |
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
| Stars | 79,008 |
| 语言 | TypeScript |
| Forks | 5,820 |
| Issues | 774 |
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
| Stars | 68,963 |
| 语言 | JavaScript |
| Forks | 23,160 |
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
| Stars | 55,952 |
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
| Forks | 4,705 |
| Issues | 1,462 |
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
| Stars | 71,762 |
| 语言 | Go |
| Forks | 4,699 |
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
| Stars | 57,829 |
| 语言 | Go |
| Forks | 3,321 |
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
| Stars | 75,557 |
| 语言 | JavaScript |
| Forks | 7,286 |
| Issues | 714 |
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
| Stars | 88,354 |
| 语言 | Go |
| Forks | 8,575 |
| Issues | 678 |
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
| Stars | 101,258 |
| 语言 | TypeScript |
| Forks | 12,150 |
| Issues | 948 |
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
| Stars | 58,777 |
| 语言 | JavaScript |
| Forks | 6,352 |
| Issues | 329 |
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
| Stars | 43,924 |
| 语言 | Go |
| Forks | 3,972 |
| Issues | 1,139 |
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
| Stars | 51,615 |
| 语言 | Go |
| Forks | 10,320 |
| Issues | 227 |
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
| Stars | 160,415 |
| 语言 | HTML |
| Forks | 20,983 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万stars的开源提示词社区平台，提供了数千个经过验证的高质量ChatGPT提示词模板，支持多模态AI模型（GPT-4、Claude、Gemini等），并且可以完全私有化部署，非常适合企业级应用。

**技术亮点**:
- 基于 Next.js + TypeScript 构建现代化 Web 应用，提供完整的类型安全保证
- 支持私有化部署，企业可完全掌控数据，确保隐私合规
- 收录超过5000+经过社区验证的优质提示词模板
- 多模型支持：OpenAI GPT-4、Claude、Gemini 等主流 LLM
- 完整的社区功能：分享、发现、收藏、分类检索

**适用场景**:
- 个人用户快速获取高质量提示词，提升 AI 交互效率
- 企业团队私有化部署，构建内部提示词知识库
- 开发者参考项目架构，学习 AI 应用的开发模式



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,468 |
| 语言 | Python |
| Forks | 2,256 |
| Issues | 141 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 4,734 |
| Issues | 95 |
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
| Stars | 55,702 |
| 语言 | TypeScript |
| Forks | 9,169 |
| Issues | 103 |
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
| Stars | 89,769 |
| 语言 | TypeScript |
| Forks | 10,025 |
| Issues | 2,255 |
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
| Stars | 87,567 |
| 语言 | TypeScript |
| Forks | 8,895 |
| Issues | 1,630 |
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
| Stars | 127,540 |
| 语言 | JavaScript |
| Forks | 12,477 |
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
| Stars | 170,705 |
| 语言 | Go |
| Forks | 13,170 |
| Issues | 179 |
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
| Stars | 135,788 |
| 语言 | Unknown |
| Forks | 34,027 |
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
| Stars | 91,746 |
| 语言 | Python |
| Forks | 13,326 |
| Issues | 105 |
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
| Stars | 90,194 |
| 语言 | Python |
| Forks | 7,773 |
| Issues | 624 |
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
| Stars | 385,876 |
| 语言 | Python |
| Forks | 66,119 |
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
| Stars | 115,056 |
| 语言 | TypeScript |
| Forks | 5,992 |
| Issues | 25 |
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
| Stars | 112,605 |
| 语言 | TypeScript |
| Forks | 8,219 |
| Issues | 288 |
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
| Stars | 80,369 |
| 语言 | TypeScript |
| Forks | 11,617 |
| Issues | 401 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,177 |
| 语言 | JavaScript |
| Forks | 4,754 |
| Issues | 22 |
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
| Stars | 48,212 |
| 语言 | Go |
| Forks | 10,297 |
| Issues | 1,890 |
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
| Stars | 105,751 |
| 语言 | C++ |
| Forks | 17,225 |
| Issues | 1,533 |
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
| Stars | 63,435 |
| 语言 | Python |
| Forks | 1,631 |
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
| Stars | 75,730 |
| 语言 | Unknown |
| Forks | 7,043 |
| Issues | 67 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 293,811 |
| 语言 | Python |
| Forks | 27,740 |
| Issues | 17 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,214 |
| 语言 | Python |
| Forks | 12,079 |
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
| Stars | 86,217 |
| 语言 | Python |
| Forks | 7,235 |
| Issues | 486 |
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
| Stars | 86,131 |
| 语言 | Python |
| Forks | 37,309 |
| Issues | 3,660 |
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
| Forks | 45,125 |
| Issues | 1,281 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,091 |
| 语言 | Python |
| Forks | 16,870 |
| Issues | 25 |
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
| Stars | 443,375 |
| 语言 | TypeScript |
| Forks | 44,358 |
| Issues | 192 |
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
| Stars | 353,391 |
| 语言 | TypeScript |
| Forks | 43,951 |
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
| Stars | 121,723 |
| 语言 | TypeScript |
| Forks | 13,391 |
| Issues | 3,005 |
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
| Stars | 112,816 |
| 语言 | TypeScript |
| Forks | 8,616 |
| Issues | 1,830 |
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
| Stars | 108,629 |
| 语言 | TypeScript |
| Forks | 13,361 |
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
| Stars | 98,391 |
| 语言 | TypeScript |
| Forks | 5,446 |
| Issues | 684 |
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
| Stars | 97,819 |
| 语言 | TypeScript |
| Forks | 54,591 |
| Issues | 1,360 |
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
| Stars | 94,692 |
| 语言 | TypeScript |
| Forks | 5,206 |
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
| Stars | 84,321 |
| 语言 | TypeScript |
| Forks | 10,472 |
| Issues | 370 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,129 |
| 语言 | TypeScript |
| Forks | 8,085 |
| Issues | 716 |
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
| Stars | 244,605 |
| 语言 | JavaScript |
| Forks | 50,967 |
| Issues | 1,237 |
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
| Stars | 148,134 |
| 语言 | JavaScript |
| Forks | 26,710 |
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
| Stars | 116,869 |
| 语言 | JavaScript |
| Forks | 35,416 |
| Issues | 2,634 |
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
| Stars | 112,124 |
| 语言 | JavaScript |
| Forks | 36,333 |
| Issues | 525 |
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
| Stars | 109,010 |
| 语言 | JavaScript |
| Forks | 11,650 |
| Issues | 272 |
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
| Stars | 98,208 |
| 语言 | JavaScript |
| Forks | 32,670 |
| Issues | 1,540 |
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
| Stars | 95,653 |
| 语言 | JavaScript |
| Forks | 15,384 |
| Issues | 50 |
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
| Stars | 86,402 |
| 语言 | JavaScript |
| Forks | 4,896 |
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
| Stars | 71,056 |
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
| Forks | 11,956 |
| Issues | 554 |
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
| Stars | 65,782 |
| 语言 | JavaScript |
| Forks | 9,362 |
| Issues | 206 |
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
| Stars | 62,927 |
| 语言 | JavaScript |
| Forks | 4,018 |
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
| Stars | 61,254 |
| 语言 | JavaScript |
| Forks | 7,141 |
| Issues | 139 |
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
| Stars | 60,628 |
| 语言 | JavaScript |
| Forks | 5,655 |
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
| Stars | 59,831 |
| 语言 | JavaScript |
| Forks | 20,463 |
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
| Stars | 57,424 |
| 语言 | JavaScript |
| Forks | 12,303 |
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
| Stars | 53,169 |
| 语言 | JavaScript |
| Forks | 10,604 |
| Issues | 456 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,620 |
| 语言 | JavaScript |
| Forks | 11,498 |
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
| Stars | 133,594 |
| 语言 | Go |
| Forks | 18,939 |
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
| Stars | 87,724 |
| 语言 | Go |
| Forks | 8,240 |
| Issues | 242 |
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
| Stars | 82,893 |
| 语言 | Go |
| Forks | 5,096 |
| Issues | 391 |
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
| Stars | 68,614 |
| 语言 | Go |
| Forks | 3,221 |
| Issues | 21 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,796 |
| 语言 | Go |
| Forks | 5,055 |
| Issues | 1,176 |
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
| Stars | 50,996 |
| 语言 | Go |
| Forks | 21,895 |
| Issues | 407 |
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
| Stars | 50,747 |
| 语言 | Go |
| Forks | 1,606 |
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
| Stars | 49,339 |
| 语言 | Go |
| Forks | 7,947 |
| Issues | 562 |
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
| Stars | 46,047 |
| 语言 | Go |
| Forks | 3,796 |
| Issues | 84 |
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
| Stars | 85,353 |
| 语言 | Shell |
| Forks | 13,651 |
| Issues | 107 |
| 许可证 | MIT License |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,043 |
| 语言 | Python |
| Forks | 50,387 |
| Issues | 929 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,969 |
| 语言 | TypeScript |
| Forks | 16,520 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,229 |
| 语言 | TypeScript |
| Forks | 7,597 |
| Issues | 35 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,125 |
| 语言 | JavaScript |
| Forks | 32,607 |
| Issues | 279 |
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
| Stars | 66,336 |
| 语言 | JavaScript |
| Forks | 9,190 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 106,029 |
| 语言 | Go |
| Forks | 15,014 |
| Issues | 40 |
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
| Stars | 152,501 |
| 语言 | Python |
| Forks | 11,614 |
| Issues | 336 |
| Topics | awesome, github, hellogithub, python |
