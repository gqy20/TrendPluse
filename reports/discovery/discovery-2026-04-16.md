# 项目发现报告 (2026-04-16)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
| 去重移除 | 31 |
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
| 📁 其他 | 62 |

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
| Stars | 132,226 |
| 语言 | Python |
| Forks | 18,774 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI API 等多种后端，132k+ Stars 验证了其成熟度和社区认可度，提供了开箱即用的 Rag、管道、工作流等企业级功能，是私有化部署 LLM 界面的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI、Anthropic Claude 等主流 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库问答
- MCP (Model Context Protocol) 支持：可扩展的工具调用和外部系统集成框架
- 自托管部署：支持 Docker 一键部署，完全私有化，数据不出本地
- 丰富的管道和工作流：支持自定义 AI 助手、预设模板、多模态交互

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 个人开发者本地 LLM：适合开发者本地运行 Ollama 等开源模型，通过友好界面进行调试和交互
- 知识库问答系统：基于 RAG 功能构建私有文档问答，支持上传 PDF、Markdown 等格式



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,315 |
| 语言 | Python |
| Forks | 12,962 |
| Issues | 4,938 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名 AI 研究组织 NousResearch 开发的高星（93,315⭐）AI Agent 框架，支持 OpenAI、Anthropic Claude 等多模型集成，具备强大的工具调用和任务自动化能力，是构建智能代理应用的优秀基础框架。

**技术亮点**:
- 多模型统一支持：集成 OpenAI GPT、Anthropic Claude 等主流 LLM，提供统一的 Agent 接口
- 强大的工具调用系统：支持函数调用（Function Calling），可扩展工具生态
- NousResearch 背书：基于该组织在 LLM 领域积累的 Hermes 系列模型经验开发
- Python 原生设计：便于与现有 Python 生态集成，降低开发门槛
- MIT 开源许可：可自由用于商业项目，无使用限制

**适用场景**:
- 企业级 AI 自动化流程：构建客服机器人、文档处理、数据分析等自动化业务助手
- 智能开发辅助工具：基于 Claude Code 和 Codex 能力，实现代码生成、代码审查、自动化测试
- 个人开发者 AI 助手：打造个人 AI 工作流助手，集成到日常开发、设计、写作等场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,267 |
| 语言 | Python |
| Forks | 8,828 |
| Issues | 3,083 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，拥有 78k+ Stars，通过将 RAG 与 Agent 能力深度融合，能够构建高质量的 LLM 上下文层，特别适合需要精准文档理解和复杂推理的企业级应用。

**技术亮点**:
- RAG + Agent 双引擎架构：深度融合检索增强生成与智能代理能力，支持复杂多步骤推理和工作流自动化
- 强大的文档理解：内置 OCR、表格解析、布局识别等高级文档处理能力，支持 PDF、Word、Excel 等多格式文档智能解析
- GraphRAG 图谱增强：支持知识图谱与向量检索的混合检索模式，提升复杂关联查询的准确性
- 多模型灵活接入：兼容 OpenAI、DeepSeek、Ollama 等主流 LLM，支持 MCP 协议便于扩展
- Deep Research 能力：支持深度研究和复杂任务规划，适合构建企业级智能问答和决策辅助系统

**适用场景**:
- 企业级智能知识库：构建支持复杂文档理解的企业知识问答系统，支持合同分析、政策解读、技术文档检索等场景
- 智能文档处理平台：自动解析结构化/非结构化文档，提取关键信息，适用于法务、财报、合同审查等场景
- Agentic 自动化工作流：基于 RAG + Agent 架构实现复杂业务流程自动化，如智能客服、报告生成、数据分析助手



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,476 |
| 语言 | JavaScript |
| Forks | 24,642 |
| Issues | 110 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI 编码代理性能优化框架，通过 Skills、Instincts、Memory 等机制显著提升 Claude Code 等工具的效率，且支持多种主流 AI 编码工具生态。

**技术亮点**:
- 多代理兼容架构：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- Skills 与 Instincts 机制：通过可扩展的技能库和本能反应系统增强代理能力
- Memory 管理模块：实现持久化上下文记忆，提升长程任务处理能力
- 安全沙箱机制：提供企业级安全保障，确保 AI 代理操作安全可控
- 研究优先开发理念：采用实验驱动的迭代优化方法，持续改进系统性能

**适用场景**:
- 个人开发者效率提升：帮助开发者通过优化后的 AI 代理加速日常编码任务、代码审查和文档生成
- 团队协作与 CI/CD 集成：在团队开发流程中部署 AI 代理，实现自动化代码质量检查和重构建议
- 企业级 AI 安全部署：为企业提供可控的 AI 代理环境，满足安全合规要求



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,457 |
| 语言 | Go |
| Forks | 3,957 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源AI引擎，支持在任意硬件（包括无GPU环境）上运行LLM、图像生成、语音合成等多种AI模型，拥有活跃的开源社区（45k+ stars），是构建私有化AI能力和边缘AI部署的理想选择。

**技术亮点**:
- 基于Go语言开发，充分利用Go的高并发和轻量级特性，适合构建高性能AI推理服务
- 支持去中心化架构，基于libp2p实现分布式AI推理能力
- 提供统一的API接口，支持文本生成、图像生成、语音合成、目标检测等多种AI任务
- 支持主流开源模型如LLaMA、Mamba、Stable Diffusion、MusicGen等
- 无需GPU即可运行，降低了AI部署的硬件门槛，支持CPU推理

**适用场景**:
- 企业私有化AI部署：在本地数据中心运行AI服务，确保数据隐私和安全，适合金融、医疗等敏感数据场景
- 边缘计算与IoT：无需昂贵GPU，在树莓派或嵌入式设备上部署轻量级AI推理能力
- 开发者快速原型：提供统一REST API，开发者可快速集成AI功能到现有应用，无需关注底层模型实现
- 本地开发与实验：个人开发者可在本地机器上实验各种开源AI模型，降低学习和开发成本



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,274 |
| 语言 | TypeScript |
| Forks | 14,932 |
| Issues | 680 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个现代化的多智能体协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，并提供 MCP 协议集成，为开发者提供开箱即用的 Agent 开发框架，显著降低多 Agent 系统构建的复杂度

**技术亮点**:
- 多模型统一接入：支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，通过统一接口进行模型切换和对比实验
- MCP 协议原生支持：内置 Model Context Protocol 实现，可扩展连接各类数据源和工具
- 多 Agent 协作编排：支持多 Agent 间的任务分解、协作与通信，实现复杂工作流程自动化
- TypeScript 全栈架构：基于类型安全设计，前后端一致性高，便于二次开发
- 知识库集成：内置知识库管理，支持 RAG 检索增强生成场景

**适用场景**:
- 企业级 AI 助手开发：构建内部知识问答、客服机器人、文档处理等多 Agent 系统
- AI 应用快速原型开发：快速搭建多模型对比实验环境，验证不同模型表现
- 多 Agent 协作工作流：研究分析、内容创作、代码审查等分工协作场景



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,191 |
| 语言 | Python |
| Forks | 8,592 |
| Issues | 972 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的 LLM 微调框架之一，70K+ Stars 证明了其工业级成熟度。它提供了统一的微调平台，支持 100+ 主流 LLMs 和 VLMs，集成了 LoRA/QLoRA/RLHF 等主流技术，让研究者和开发者无需从零搭建复杂的基础设施，即可高效完成模型定制化训练。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，包括 LLaMA、Qwen、DeepSeek、Gemma 等主流模型系列
- 集成多种 PEFT 高效微调方法：LoRA、QLoRA、DoRA、GaLore 等，大幅降低显存占用
- 支持完整的 RLHF 训练流程，包括 SFT、RM、RLHF 以及 DPO/KTO 等新型对齐算法
- 支持 MoE 混合专家架构、4-bit/8-bit 量化训练、DeepSeek-V2 等前沿技术
- 提供 Web UI 和 CLI 两种交互方式，支持多卡分布式训练和梯度累积

**适用场景**:
- 企业场景：使用 LoRA/QLoRA 快速微调私有化部署的 Llama/Qwen 等模型，降低推理成本
- 学术研究：低成本复现 RLHF、DPO 等对齐实验，支持前沿算法验证和 ablation study
- 垂直领域定制：针对金融、医疗、法律等专业领域快速构建专属的指令遵循模型
- 多模态应用：微调视觉-语言模型（VLM），实现 OCR、文档理解等特定任务优化



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,398 |
| 语言 | TypeScript |
| Forks | 4,868 |
| Issues | 141 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现长期记忆管理，解决了 AI 编码助手中"每次会话都从零开始"的痛点，让 Claude 能够真正记住项目的历史决策和技术债务，极大提升开发效率。

**技术亮点**:
- AI 驱动的智能压缩：集成 Claude Agent SDK，使用 AI 自动分析和压缩编码会话中的关键信息，过滤噪音，保留高价值上下文
- RAG + 向量检索架构：采用 ChromaDB 向量数据库存储语义嵌入，结合 RAG（检索增强生成）技术，在新会话中精准检索并注入相关历史记忆
- SQLite 本地持久化：轻量级 SQLite 数据库存储记忆数据，无需复杂的基础设施部署，本地即可运行，保护代码隐私
- 多维记忆管理：支持项目级别的长期记忆、会话级别的短期记忆和语义级别的检索
- 无缝插件集成：作为 Claude Code 官方插件，开箱即用，无需修改现有工作流，自动在后台运行

**适用场景**:
- 长期项目开发：适用于周期超过数周的复杂项目，Claude 能够记住早期的架构决策、放弃的方案和设计权衡，避免重复讨论
- 团队知识传承：开发团队成员可以借助共享的项目记忆上下文，新加入的开发者通过 Claude 快速了解项目的技术演进历程
- 个人开发者效率提升：个人开发者可以借助记忆系统，在多任务切换时快速恢复上下文，减少重新理解代码库的时间成本



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,085 |
| 语言 | TypeScript |
| Forks | 8,900 |
| Issues | 91 |
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
| Stars | 43,349 |
| 语言 | Python |
| Forks | 9,936 |
| Issues | 353 |
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
| Stars | 39,795 |
| 语言 | Python |
| Forks | 6,983 |
| Issues | 943 |
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
| Stars | 45,868 |
| 语言 | Java |
| Forks | 15,913 |
| Issues | 11 |
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
| Stars | 38,988 |
| 语言 | Python |
| Forks | 6,190 |
| Issues | 71 |
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
| Stars | 37,540 |
| 语言 | Python |
| Forks | 4,449 |
| Issues | 98 |
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
| Stars | 33,767 |
| 语言 | TypeScript |
| Forks | 3,656 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,005 |
| 语言 | TypeScript |
| Forks | 7,029 |
| Issues | 275 |
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
| Stars | 58,444 |
| 语言 | JavaScript |
| Forks | 6,324 |
| Issues | 332 |
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
| Stars | 71,327 |
| 语言 | Python |
| Forks | 8,969 |
| Issues | 422 |
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
| Stars | 52,108 |
| 语言 | TypeScript |
| Forks | 4,191 |
| Issues | 534 |
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
| Stars | 105,881 |
| 语言 | Python |
| Forks | 15,483 |
| Issues | 1 |
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
| Stars | 88,128 |
| 语言 | Python |
| Forks | 10,124 |
| Issues | 215 |
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
| Stars | 51,981 |
| 语言 | TypeScript |
| Forks | 24,159 |
| Issues | 812 |
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
| Stars | 184,344 |
| 语言 | TypeScript |
| Forks | 56,861 |
| Issues | 1,502 |
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
| Stars | 155,014 |
| 语言 | Java |
| Forks | 46,154 |
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
| Stars | 147,015 |
| 语言 | Python |
| Forks | 8,784 |
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
| Stars | 56,810 |
| 语言 | Jupyter Notebook |
| Forks | 19,664 |
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
| Stars | 34,111 |
| 语言 | Python |
| Forks | 2,141 |
| Issues | 95 |
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
| Stars | 33,603 |
| 语言 | Jupyter Notebook |
| Forks | 5,553 |
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
| Stars | 45,921 |
| 语言 | Rust |
| Forks | 2,922 |
| Issues | 522 |
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
| Stars | 132,226 |
| 语言 | Python |
| Forks | 18,774 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI API 等多种后端，132k+ Stars 验证了其成熟度和社区认可度，提供了开箱即用的 Rag、管道、工作流等企业级功能，是私有化部署 LLM 界面的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI、Anthropic Claude 等主流 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库问答
- MCP (Model Context Protocol) 支持：可扩展的工具调用和外部系统集成框架
- 自托管部署：支持 Docker 一键部署，完全私有化，数据不出本地
- 丰富的管道和工作流：支持自定义 AI 助手、预设模板、多模态交互

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 个人开发者本地 LLM：适合开发者本地运行 Ollama 等开源模型，通过友好界面进行调试和交互
- 知识库问答系统：基于 RAG 功能构建私有文档问答，支持上传 PDF、Markdown 等格式



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,267 |
| 语言 | Python |
| Forks | 8,828 |
| Issues | 3,083 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，拥有 78k+ Stars，通过将 RAG 与 Agent 能力深度融合，能够构建高质量的 LLM 上下文层，特别适合需要精准文档理解和复杂推理的企业级应用。

**技术亮点**:
- RAG + Agent 双引擎架构：深度融合检索增强生成与智能代理能力，支持复杂多步骤推理和工作流自动化
- 强大的文档理解：内置 OCR、表格解析、布局识别等高级文档处理能力，支持 PDF、Word、Excel 等多格式文档智能解析
- GraphRAG 图谱增强：支持知识图谱与向量检索的混合检索模式，提升复杂关联查询的准确性
- 多模型灵活接入：兼容 OpenAI、DeepSeek、Ollama 等主流 LLM，支持 MCP 协议便于扩展
- Deep Research 能力：支持深度研究和复杂任务规划，适合构建企业级智能问答和决策辅助系统

**适用场景**:
- 企业级智能知识库：构建支持复杂文档理解的企业知识问答系统，支持合同分析、政策解读、技术文档检索等场景
- 智能文档处理平台：自动解析结构化/非结构化文档，提取关键信息，适用于法务、财报、合同审查等场景
- Agentic 自动化工作流：基于 RAG + Agent 架构实现复杂业务流程自动化，如智能客服、报告生成、数据分析助手



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,274 |
| 语言 | TypeScript |
| Forks | 14,932 |
| Issues | 680 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个现代化的多智能体协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，并提供 MCP 协议集成，为开发者提供开箱即用的 Agent 开发框架，显著降低多 Agent 系统构建的复杂度

**技术亮点**:
- 多模型统一接入：支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，通过统一接口进行模型切换和对比实验
- MCP 协议原生支持：内置 Model Context Protocol 实现，可扩展连接各类数据源和工具
- 多 Agent 协作编排：支持多 Agent 间的任务分解、协作与通信，实现复杂工作流程自动化
- TypeScript 全栈架构：基于类型安全设计，前后端一致性高，便于二次开发
- 知识库集成：内置知识库管理，支持 RAG 检索增强生成场景

**适用场景**:
- 企业级 AI 助手开发：构建内部知识问答、客服机器人、文档处理等多 Agent 系统
- AI 应用快速原型开发：快速搭建多模型对比实验环境，验证不同模型表现
- 多 Agent 协作工作流：研究分析、内容创作、代码审查等分工协作场景



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,398 |
| 语言 | TypeScript |
| Forks | 4,868 |
| Issues | 141 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现长期记忆管理，解决了 AI 编码助手中"每次会话都从零开始"的痛点，让 Claude 能够真正记住项目的历史决策和技术债务，极大提升开发效率。

**技术亮点**:
- AI 驱动的智能压缩：集成 Claude Agent SDK，使用 AI 自动分析和压缩编码会话中的关键信息，过滤噪音，保留高价值上下文
- RAG + 向量检索架构：采用 ChromaDB 向量数据库存储语义嵌入，结合 RAG（检索增强生成）技术，在新会话中精准检索并注入相关历史记忆
- SQLite 本地持久化：轻量级 SQLite 数据库存储记忆数据，无需复杂的基础设施部署，本地即可运行，保护代码隐私
- 多维记忆管理：支持项目级别的长期记忆、会话级别的短期记忆和语义级别的检索
- 无缝插件集成：作为 Claude Code 官方插件，开箱即用，无需修改现有工作流，自动在后台运行

**适用场景**:
- 长期项目开发：适用于周期超过数周的复杂项目，Claude 能够记住早期的架构决策、放弃的方案和设计权衡，避免重复讨论
- 团队知识传承：开发团队成员可以借助共享的项目记忆上下文，新加入的开发者通过 Claude 快速了解项目的技术演进历程
- 个人开发者效率提升：个人开发者可以借助记忆系统，在多任务切换时快速恢复上下文，减少重新理解代码库的时间成本



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,868 |
| 语言 | Java |
| Forks | 15,913 |
| Issues | 11 |
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
| Stars | 38,988 |
| 语言 | Python |
| Forks | 6,190 |
| Issues | 71 |
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
| Stars | 37,540 |
| 语言 | Python |
| Forks | 4,449 |
| Issues | 98 |
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
| Stars | 33,767 |
| 语言 | TypeScript |
| Forks | 3,656 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,962 |
| 语言 | TypeScript |
| Forks | 12,094 |
| Issues | 957 |
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
| Stars | 58,444 |
| 语言 | JavaScript |
| Forks | 6,324 |
| Issues | 332 |
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
| Stars | 105,881 |
| 语言 | Python |
| Forks | 15,483 |
| Issues | 1 |
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
| Stars | 75,741 |
| 语言 | Python |
| Forks | 10,243 |
| Issues | 232 |
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
| Stars | 51,981 |
| 语言 | TypeScript |
| Forks | 24,159 |
| Issues | 812 |
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
| Stars | 43,835 |
| 语言 | Go |
| Forks | 3,962 |
| Issues | 1,186 |
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
| Stars | 33,500 |
| 语言 | Python |
| Forks | 4,757 |
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
| Stars | 34,111 |
| 语言 | Python |
| Forks | 2,141 |
| Issues | 95 |
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
| Stars | 33,603 |
| 语言 | Jupyter Notebook |
| Forks | 5,553 |
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
| Stars | 132,226 |
| 语言 | Python |
| Forks | 18,774 |
| Issues | 273 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是当前最受欢迎的开源 LLM Web 界面项目，支持 Ollama、OpenAI API 等多种后端，132k+ Stars 验证了其成熟度和社区认可度，提供了开箱即用的 Rag、管道、工作流等企业级功能，是私有化部署 LLM 界面的最佳选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI、Anthropic Claude 等主流 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库问答
- MCP (Model Context Protocol) 支持：可扩展的工具调用和外部系统集成框架
- 自托管部署：支持 Docker 一键部署，完全私有化，数据不出本地
- 丰富的管道和工作流：支持自定义 AI 助手、预设模板、多模态交互

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 个人开发者本地 LLM：适合开发者本地运行 Ollama 等开源模型，通过友好界面进行调试和交互
- 知识库问答系统：基于 RAG 功能构建私有文档问答，支持上传 PDF、Markdown 等格式



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,315 |
| 语言 | Python |
| Forks | 12,962 |
| Issues | 4,938 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名 AI 研究组织 NousResearch 开发的高星（93,315⭐）AI Agent 框架，支持 OpenAI、Anthropic Claude 等多模型集成，具备强大的工具调用和任务自动化能力，是构建智能代理应用的优秀基础框架。

**技术亮点**:
- 多模型统一支持：集成 OpenAI GPT、Anthropic Claude 等主流 LLM，提供统一的 Agent 接口
- 强大的工具调用系统：支持函数调用（Function Calling），可扩展工具生态
- NousResearch 背书：基于该组织在 LLM 领域积累的 Hermes 系列模型经验开发
- Python 原生设计：便于与现有 Python 生态集成，降低开发门槛
- MIT 开源许可：可自由用于商业项目，无使用限制

**适用场景**:
- 企业级 AI 自动化流程：构建客服机器人、文档处理、数据分析等自动化业务助手
- 智能开发辅助工具：基于 Claude Code 和 Codex 能力，实现代码生成、代码审查、自动化测试
- 个人开发者 AI 助手：打造个人 AI 工作流助手，集成到日常开发、设计、写作等场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,267 |
| 语言 | Python |
| Forks | 8,828 |
| Issues | 3,083 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，拥有 78k+ Stars，通过将 RAG 与 Agent 能力深度融合，能够构建高质量的 LLM 上下文层，特别适合需要精准文档理解和复杂推理的企业级应用。

**技术亮点**:
- RAG + Agent 双引擎架构：深度融合检索增强生成与智能代理能力，支持复杂多步骤推理和工作流自动化
- 强大的文档理解：内置 OCR、表格解析、布局识别等高级文档处理能力，支持 PDF、Word、Excel 等多格式文档智能解析
- GraphRAG 图谱增强：支持知识图谱与向量检索的混合检索模式，提升复杂关联查询的准确性
- 多模型灵活接入：兼容 OpenAI、DeepSeek、Ollama 等主流 LLM，支持 MCP 协议便于扩展
- Deep Research 能力：支持深度研究和复杂任务规划，适合构建企业级智能问答和决策辅助系统

**适用场景**:
- 企业级智能知识库：构建支持复杂文档理解的企业知识问答系统，支持合同分析、政策解读、技术文档检索等场景
- 智能文档处理平台：自动解析结构化/非结构化文档，提取关键信息，适用于法务、财报、合同审查等场景
- Agentic 自动化工作流：基于 RAG + Agent 架构实现复杂业务流程自动化，如智能客服、报告生成、数据分析助手



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,476 |
| 语言 | JavaScript |
| Forks | 24,642 |
| Issues | 110 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI 编码代理性能优化框架，通过 Skills、Instincts、Memory 等机制显著提升 Claude Code 等工具的效率，且支持多种主流 AI 编码工具生态。

**技术亮点**:
- 多代理兼容架构：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- Skills 与 Instincts 机制：通过可扩展的技能库和本能反应系统增强代理能力
- Memory 管理模块：实现持久化上下文记忆，提升长程任务处理能力
- 安全沙箱机制：提供企业级安全保障，确保 AI 代理操作安全可控
- 研究优先开发理念：采用实验驱动的迭代优化方法，持续改进系统性能

**适用场景**:
- 个人开发者效率提升：帮助开发者通过优化后的 AI 代理加速日常编码任务、代码审查和文档生成
- 团队协作与 CI/CD 集成：在团队开发流程中部署 AI 代理，实现自动化代码质量检查和重构建议
- 企业级 AI 安全部署：为企业提供可控的 AI 代理环境，满足安全合规要求



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,274 |
| 语言 | TypeScript |
| Forks | 14,932 |
| Issues | 680 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个现代化的多智能体协作平台，支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，并提供 MCP 协议集成，为开发者提供开箱即用的 Agent 开发框架，显著降低多 Agent 系统构建的复杂度

**技术亮点**:
- 多模型统一接入：支持 OpenAI、Claude、DeepSeek、Gemini 等多种大模型，通过统一接口进行模型切换和对比实验
- MCP 协议原生支持：内置 Model Context Protocol 实现，可扩展连接各类数据源和工具
- 多 Agent 协作编排：支持多 Agent 间的任务分解、协作与通信，实现复杂工作流程自动化
- TypeScript 全栈架构：基于类型安全设计，前后端一致性高，便于二次开发
- 知识库集成：内置知识库管理，支持 RAG 检索增强生成场景

**适用场景**:
- 企业级 AI 助手开发：构建内部知识问答、客服机器人、文档处理等多 Agent 系统
- AI 应用快速原型开发：快速搭建多模型对比实验环境，验证不同模型表现
- 多 Agent 协作工作流：研究分析、内容创作、代码审查等分工协作场景



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,398 |
| 语言 | TypeScript |
| Forks | 4,868 |
| Issues | 141 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 是目前最实用的 Claude Code 记忆增强插件之一，通过自动捕获编码会话上下文并利用 AI 压缩技术实现长期记忆管理，解决了 AI 编码助手中"每次会话都从零开始"的痛点，让 Claude 能够真正记住项目的历史决策和技术债务，极大提升开发效率。

**技术亮点**:
- AI 驱动的智能压缩：集成 Claude Agent SDK，使用 AI 自动分析和压缩编码会话中的关键信息，过滤噪音，保留高价值上下文
- RAG + 向量检索架构：采用 ChromaDB 向量数据库存储语义嵌入，结合 RAG（检索增强生成）技术，在新会话中精准检索并注入相关历史记忆
- SQLite 本地持久化：轻量级 SQLite 数据库存储记忆数据，无需复杂的基础设施部署，本地即可运行，保护代码隐私
- 多维记忆管理：支持项目级别的长期记忆、会话级别的短期记忆和语义级别的检索
- 无缝插件集成：作为 Claude Code 官方插件，开箱即用，无需修改现有工作流，自动在后台运行

**适用场景**:
- 长期项目开发：适用于周期超过数周的复杂项目，Claude 能够记住早期的架构决策、放弃的方案和设计权衡，避免重复讨论
- 团队知识传承：开发团队成员可以借助共享的项目记忆上下文，新加入的开发者通过 Claude 快速了解项目的技术演进历程
- 个人开发者效率提升：个人开发者可以借助记忆系统，在多任务切换时快速恢复上下文，减少重新理解代码库的时间成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,875 |
| 语言 | HTML |
| Forks | 20,936 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最受欢迎的 AI 提示词聚合平台，拥有近 16 万星标，支持 ChatGPT、Claude、Gemini 等多平台，开源可自托管且完全隐私保护，是个人开发者和企业团队提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，具备现代化的全栈开发架构和优秀的类型安全保障
- 支持多 AI 平台集成（ChatGPT、Claude、Gemini、GPT-4 等），提供统一的 prompt 管理体验
- 开源项目支持自托管部署，企业可完全控制数据，满足隐私合规要求
- 社区驱动的 prompt 分享机制，持续积累优质提示词资源
- 采用现代化的 Web 技术栈，支持响应式设计和多端访问

**适用场景**:
- 个人用户探索和收藏优质 AI prompts，提升日常工作和创作效率
- 企业和团队搭建私有 prompt 知识库，统一管理团队共享的 AI 交互模板
- 开发者基于开源代码二次开发，定制化部署企业级 AI 提示词管理平台



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,892 |
| 语言 | Jupyter Notebook |
| Forks | 13,965 |
| Issues | 2 |
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
| Stars | 54,085 |
| 语言 | TypeScript |
| Forks | 8,900 |
| Issues | 91 |
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
| Stars | 43,349 |
| 语言 | Python |
| Forks | 9,936 |
| Issues | 353 |
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
| Stars | 39,795 |
| 语言 | Python |
| Forks | 6,983 |
| Issues | 943 |
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
| Stars | 58,444 |
| 语言 | JavaScript |
| Forks | 6,324 |
| Issues | 332 |
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
| Stars | 71,327 |
| 语言 | Python |
| Forks | 8,969 |
| Issues | 422 |
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
| Stars | 52,108 |
| 语言 | TypeScript |
| Forks | 4,191 |
| Issues | 534 |
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
| Stars | 45,510 |
| 语言 | HTML |
| Forks | 4,399 |
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
| Stars | 51,981 |
| 语言 | TypeScript |
| Forks | 24,159 |
| Issues | 812 |
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
| Stars | 76,953 |
| 语言 | Python |
| Forks | 15,703 |
| Issues | 4,318 |
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
| Stars | 147,015 |
| 语言 | Python |
| Forks | 8,784 |
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
| Stars | 169,180 |
| 语言 | Go |
| Forks | 15,624 |
| Issues | 2,953 |
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
| Stars | 47,809 |
| 语言 | Rust |
| Forks | 9,532 |
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
| Stars | 34,111 |
| 语言 | Python |
| Forks | 2,141 |
| Issues | 95 |
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
| Stars | 110,281 |
| 语言 | Python |
| Forks | 7,046 |
| Issues | 602 |
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
| Stars | 66,411 |
| 语言 | Python |
| Forks | 6,753 |
| Issues | 107 |
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
| Stars | 70,191 |
| 语言 | Python |
| Forks | 8,592 |
| Issues | 972 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最流行的 LLM 微调框架之一，70K+ Stars 证明了其工业级成熟度。它提供了统一的微调平台，支持 100+ 主流 LLMs 和 VLMs，集成了 LoRA/QLoRA/RLHF 等主流技术，让研究者和开发者无需从零搭建复杂的基础设施，即可高效完成模型定制化训练。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 的统一微调框架，包括 LLaMA、Qwen、DeepSeek、Gemma 等主流模型系列
- 集成多种 PEFT 高效微调方法：LoRA、QLoRA、DoRA、GaLore 等，大幅降低显存占用
- 支持完整的 RLHF 训练流程，包括 SFT、RM、RLHF 以及 DPO/KTO 等新型对齐算法
- 支持 MoE 混合专家架构、4-bit/8-bit 量化训练、DeepSeek-V2 等前沿技术
- 提供 Web UI 和 CLI 两种交互方式，支持多卡分布式训练和梯度累积

**适用场景**:
- 企业场景：使用 LoRA/QLoRA 快速微调私有化部署的 Llama/Qwen 等模型，降低推理成本
- 学术研究：低成本复现 RLHF、DPO 等对齐实验，支持前沿算法验证和 ablation study
- 垂直领域定制：针对金融、医疗、法律等专业领域快速构建专属的指令遵循模型
- 多模态应用：微调视觉-语言模型（VLM），实现 OCR、文档理解等特定任务优化



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,968 |
| 语言 | Python |
| Forks | 6,569 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，支持股票、加密货币、期权、固定收益等多品类数据接入，并原生支持 AI 代理集成，65K+ Stars 验证了其成熟度和社区活跃度，是量化研究和 AI 金融应用开发的优秀基础框架。

**技术亮点**:
- 统一的数据 API 层，支持多个数据源接入（股票、加密货币、衍生品等），简化数据获取流程
- 模块化架构设计，便于扩展自定义数据源和分析功能
- 原生支持 AI Agent 集成，提供标准化的工具调用接口，方便构建 AI 金融助手
- 丰富的金融分析工具集，涵盖技术分析、固收分析、衍生品定价等模块
- 基于 Python，提供交互式终端界面和 SDK，满足不同使用习惯

**适用场景**:
- 量化交易研究：获取多品类金融数据、进行因子分析、回测策略
- 投资研究与分析：快速获取市场数据、生成研究报告、追踪投资组合
- AI 金融代理开发：利用标准化的函数工具，构建能够执行金融任务的 AI Agent
- 金融教学与演示：提供真实市场数据，支持金融课程实践



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,875 |
| 语言 | HTML |
| Forks | 20,936 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最受欢迎的 AI 提示词聚合平台，拥有近 16 万星标，支持 ChatGPT、Claude、Gemini 等多平台，开源可自托管且完全隐私保护，是个人开发者和企业团队提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，具备现代化的全栈开发架构和优秀的类型安全保障
- 支持多 AI 平台集成（ChatGPT、Claude、Gemini、GPT-4 等），提供统一的 prompt 管理体验
- 开源项目支持自托管部署，企业可完全控制数据，满足隐私合规要求
- 社区驱动的 prompt 分享机制，持续积累优质提示词资源
- 采用现代化的 Web 技术栈，支持响应式设计和多端访问

**适用场景**:
- 个人用户探索和收藏优质 AI prompts，提升日常工作和创作效率
- 企业和团队搭建私有 prompt 知识库，统一管理团队共享的 AI 交互模板
- 开发者基于开源代码二次开发，定制化部署企业级 AI 提示词管理平台



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,892 |
| 语言 | Jupyter Notebook |
| Forks | 13,965 |
| Issues | 2 |
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
| Stars | 33,767 |
| 语言 | TypeScript |
| Forks | 3,656 |
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
| Stars | 159,481 |
| 语言 | Python |
| Forks | 32,893 |
| Issues | 2,352 |
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
| Stars | 76,953 |
| 语言 | Python |
| Forks | 15,703 |
| Issues | 4,318 |
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
| Stars | 109,011 |
| 语言 | Python |
| Forks | 12,662 |
| Issues | 3,987 |
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
| Stars | 99,198 |
| 语言 | Python |
| Forks | 27,513 |
| Issues | 18,507 |
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
| Stars | 33,603 |
| 语言 | Jupyter Notebook |
| Forks | 5,553 |
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
| Stars | 158,476 |
| 语言 | JavaScript |
| Forks | 24,642 |
| Issues | 110 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI 编码代理性能优化框架，通过 Skills、Instincts、Memory 等机制显著提升 Claude Code 等工具的效率，且支持多种主流 AI 编码工具生态。

**技术亮点**:
- 多代理兼容架构：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- Skills 与 Instincts 机制：通过可扩展的技能库和本能反应系统增强代理能力
- Memory 管理模块：实现持久化上下文记忆，提升长程任务处理能力
- 安全沙箱机制：提供企业级安全保障，确保 AI 代理操作安全可控
- 研究优先开发理念：采用实验驱动的迭代优化方法，持续改进系统性能

**适用场景**:
- 个人开发者效率提升：帮助开发者通过优化后的 AI 代理加速日常编码任务、代码审查和文档生成
- 团队协作与 CI/CD 集成：在团队开发流程中部署 AI 代理，实现自动化代码质量检查和重构建议
- 企业级 AI 安全部署：为企业提供可控的 AI 代理环境，满足安全合规要求



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,457 |
| 语言 | Go |
| Forks | 3,957 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源AI引擎，支持在任意硬件（包括无GPU环境）上运行LLM、图像生成、语音合成等多种AI模型，拥有活跃的开源社区（45k+ stars），是构建私有化AI能力和边缘AI部署的理想选择。

**技术亮点**:
- 基于Go语言开发，充分利用Go的高并发和轻量级特性，适合构建高性能AI推理服务
- 支持去中心化架构，基于libp2p实现分布式AI推理能力
- 提供统一的API接口，支持文本生成、图像生成、语音合成、目标检测等多种AI任务
- 支持主流开源模型如LLaMA、Mamba、Stable Diffusion、MusicGen等
- 无需GPU即可运行，降低了AI部署的硬件门槛，支持CPU推理

**适用场景**:
- 企业私有化AI部署：在本地数据中心运行AI服务，确保数据隐私和安全，适合金融、医疗等敏感数据场景
- 边缘计算与IoT：无需昂贵GPU，在树莓派或嵌入式设备上部署轻量级AI推理能力
- 开发者快速原型：提供统一REST API，开发者可快速集成AI功能到现有应用，无需关注底层模型实现
- 本地开发与实验：个人开发者可在本地机器上实验各种开源AI模型，降低学习和开发成本



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,327 |
| 语言 | Python |
| Forks | 8,969 |
| Issues | 422 |
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
| Stars | 52,108 |
| 语言 | TypeScript |
| Forks | 4,191 |
| Issues | 534 |
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
| Stars | 184,344 |
| 语言 | TypeScript |
| Forks | 56,861 |
| Issues | 1,502 |
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
| Stars | 157,193 |
| 语言 | Python |
| Forks | 12,954 |
| Issues | 2,474 |
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
| Stars | 97,293 |
| 语言 | Python |
| Forks | 9,089 |
| Issues | 174 |
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
| Stars | 81,228 |
| 语言 | Python |
| Forks | 9,435 |
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
| Stars | 183,934 |
| 语言 | TypeScript |
| Forks | 39,235 |
| Issues | 16,385 |
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
| Stars | 94,135 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 295 |
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
| Stars | 78,941 |
| 语言 | TypeScript |
| Forks | 5,802 |
| Issues | 764 |
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
| Stars | 77,148 |
| 语言 | TypeScript |
| Forks | 6,612 |
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
| Stars | 79,525 |
| 语言 | Go |
| Forks | 2,776 |
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
| Stars | 76,522 |
| 语言 | Go |
| Forks | 2,756 |
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
| Stars | 43,859 |
| 语言 | Go |
| Forks | 8,269 |
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
| Stars | 43,691 |
| 语言 | Go |
| Forks | 3,117 |
| Issues | 364 |
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
| Stars | 41,625 |
| 语言 | Go |
| Forks | 1,191 |
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
| Stars | 424,134 |
| 语言 | Python |
| Forks | 46,172 |
| Issues | 1,259 |
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
| Stars | 75,591 |
| 语言 | JavaScript |
| Forks | 7,286 |
| Issues | 715 |
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
| Stars | 52,108 |
| 语言 | TypeScript |
| Forks | 4,191 |
| Issues | 534 |
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
| Stars | 184,344 |
| 语言 | TypeScript |
| Forks | 56,861 |
| Issues | 1,502 |
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
| Stars | 51,638 |
| 语言 | Go |
| Forks | 10,324 |
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
| Stars | 121,744 |
| 语言 | Go |
| Forks | 42,873 |
| Issues | 2,761 |
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
| Stars | 71,503 |
| 语言 | Go |
| Forks | 18,918 |
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
| Stars | 54,946 |
| 语言 | Go |
| Forks | 6,585 |
| Issues | 2,821 |
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
| Stars | 94,135 |
| 语言 | TypeScript |
| Forks | 9,419 |
| Issues | 295 |
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
| Stars | 76,832 |
| 语言 | TypeScript |
| Forks | 6,657 |
| Issues | 406 |
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
| Stars | 85,350 |
| 语言 | JavaScript |
| Forks | 7,646 |
| Issues | 718 |
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
| Stars | 69,889 |
| 语言 | Go |
| Forks | 1,912 |
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
| Stars | 62,727 |
| 语言 | Go |
| Forks | 5,921 |
| Issues | 760 |
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
| Stars | 58,928 |
| 语言 | Go |
| Forks | 4,276 |
| Issues | 28 |
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
| Stars | 47,501 |
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
| Stars | 85,350 |
| 语言 | JavaScript |
| Forks | 7,646 |
| Issues | 718 |
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
| Stars | 63,623 |
| 语言 | Go |
| Forks | 10,332 |
| Issues | 747 |
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
| Stars | 45,457 |
| 语言 | Go |
| Forks | 3,957 |
| Issues | 168 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源AI引擎，支持在任意硬件（包括无GPU环境）上运行LLM、图像生成、语音合成等多种AI模型，拥有活跃的开源社区（45k+ stars），是构建私有化AI能力和边缘AI部署的理想选择。

**技术亮点**:
- 基于Go语言开发，充分利用Go的高并发和轻量级特性，适合构建高性能AI推理服务
- 支持去中心化架构，基于libp2p实现分布式AI推理能力
- 提供统一的API接口，支持文本生成、图像生成、语音合成、目标检测等多种AI任务
- 支持主流开源模型如LLaMA、Mamba、Stable Diffusion、MusicGen等
- 无需GPU即可运行，降低了AI部署的硬件门槛，支持CPU推理

**适用场景**:
- 企业私有化AI部署：在本地数据中心运行AI服务，确保数据隐私和安全，适合金融、医疗等敏感数据场景
- 边缘计算与IoT：无需昂贵GPU，在树莓派或嵌入式设备上部署轻量级AI推理能力
- 开发者快速原型：提供统一REST API，开发者可快速集成AI功能到现有应用，无需关注底层模型实现
- 本地开发与实验：个人开发者可在本地机器上实验各种开源AI模型，降低学习和开发成本



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,293 |
| 语言 | Python |
| Forks | 9,089 |
| Issues | 174 |
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
| Stars | 87,280 |
| 语言 | Python |
| Forks | 33,817 |
| Issues | 430 |
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
| Stars | 100,071 |
| 语言 | TypeScript |
| Forks | 27,171 |
| Issues | 1,134 |
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
| Stars | 78,941 |
| 语言 | TypeScript |
| Forks | 5,802 |
| Issues | 764 |
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
| Stars | 68,953 |
| 语言 | JavaScript |
| Forks | 23,139 |
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
| Stars | 55,966 |
| 语言 | JavaScript |
| Forks | 10,216 |
| Issues | 364 |
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
| Stars | 51,795 |
| 语言 | JavaScript |
| Forks | 4,701 |
| Issues | 1,459 |
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
| Stars | 88,328 |
| 语言 | Go |
| Forks | 8,572 |
| Issues | 673 |
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
| Stars | 71,594 |
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
| Stars | 57,652 |
| 语言 | Go |
| Forks | 3,290 |
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
| Stars | 41,625 |
| 语言 | Go |
| Forks | 1,191 |
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
| Stars | 424,134 |
| 语言 | Python |
| Forks | 46,172 |
| Issues | 1,259 |
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
| Stars | 75,591 |
| 语言 | JavaScript |
| Forks | 7,286 |
| Issues | 715 |
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
| Stars | 100,962 |
| 语言 | TypeScript |
| Forks | 12,094 |
| Issues | 957 |
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
| Stars | 58,444 |
| 语言 | JavaScript |
| Forks | 6,324 |
| Issues | 332 |
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
| Stars | 43,835 |
| 语言 | Go |
| Forks | 3,962 |
| Issues | 1,186 |
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
| Stars | 51,638 |
| 语言 | Go |
| Forks | 10,324 |
| Issues | 242 |
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
| Stars | 159,875 |
| 语言 | HTML |
| Forks | 20,936 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最受欢迎的 AI 提示词聚合平台，拥有近 16 万星标，支持 ChatGPT、Claude、Gemini 等多平台，开源可自托管且完全隐私保护，是个人开发者和企业团队提升 AI 使用效率的必备资源。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，具备现代化的全栈开发架构和优秀的类型安全保障
- 支持多 AI 平台集成（ChatGPT、Claude、Gemini、GPT-4 等），提供统一的 prompt 管理体验
- 开源项目支持自托管部署，企业可完全控制数据，满足隐私合规要求
- 社区驱动的 prompt 分享机制，持续积累优质提示词资源
- 采用现代化的 Web 技术栈，支持响应式设计和多端访问

**适用场景**:
- 个人用户探索和收藏优质 AI prompts，提升日常工作和创作效率
- 企业和团队搭建私有 prompt 知识库，统一管理团队共享的 AI 交互模板
- 开发者基于开源代码二次开发，定制化部署企业级 AI 提示词管理平台



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,085 |
| 语言 | TypeScript |
| Forks | 8,900 |
| Issues | 91 |
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
| Stars | 37,540 |
| 语言 | Python |
| Forks | 4,449 |
| Issues | 98 |
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
| Stars | 89,727 |
| 语言 | TypeScript |
| Forks | 10,016 |
| Issues | 2,240 |
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
| Stars | 87,423 |
| 语言 | TypeScript |
| Forks | 8,875 |
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
| Stars | 127,489 |
| 语言 | JavaScript |
| Forks | 12,479 |
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
| Stars | 170,144 |
| 语言 | Go |
| Forks | 13,148 |
| Issues | 178 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,006 |
| 语言 | Shell |
| Forks | 12,963 |
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
| Stars | 64,124 |
| 语言 | Python |
| Forks | 6,569 |
| Issues | 70 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,785 |
| 语言 | Python |
| Forks | 13,206 |
| Issues | 127 |
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
| Stars | 88,580 |
| 语言 | Python |
| Forks | 7,617 |
| Issues | 625 |
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
| Stars | 135,320 |
| 语言 | Unknown |
| Forks | 33,992 |
| Issues | 147 |
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
| Stars | 385,604 |
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
| Stars | 114,671 |
| 语言 | TypeScript |
| Forks | 5,917 |
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
| Stars | 111,164 |
| 语言 | TypeScript |
| Forks | 8,081 |
| Issues | 266 |
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
| Stars | 54,024 |
| 语言 | JavaScript |
| Forks | 4,532 |
| Issues | 28 |
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
| Stars | 48,155 |
| 语言 | Go |
| Forks | 10,288 |
| Issues | 1,888 |
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
| Stars | 104,073 |
| 语言 | C++ |
| Forks | 16,917 |
| Issues | 1,503 |
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
| Stars | 73,894 |
| 语言 | TypeScript |
| Forks | 10,451 |
| Issues | 312 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,505 |
| 语言 | Python |
| Forks | 1,630 |
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
| Stars | 49,044 |
| 语言 | Unknown |
| Forks | 4,028 |
| Issues | 63 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 292,710 |
| 语言 | Python |
| Forks | 27,698 |
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
| Stars | 219,666 |
| 语言 | Python |
| Forks | 50,334 |
| Issues | 927 |
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
| Stars | 97,868 |
| 语言 | Python |
| Forks | 12,047 |
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
| Stars | 86,056 |
| 语言 | Python |
| Forks | 37,255 |
| Issues | 3,612 |
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
| Stars | 77,676 |
| 语言 | Python |
| Forks | 45,149 |
| Issues | 1,279 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 443,022 |
| 语言 | TypeScript |
| Forks | 44,314 |
| Issues | 207 |
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
| Stars | 353,058 |
| 语言 | TypeScript |
| Forks | 43,941 |
| Issues | 11 |
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
| Stars | 121,223 |
| 语言 | TypeScript |
| Forks | 13,299 |
| Issues | 2,973 |
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
| Stars | 112,473 |
| 语言 | TypeScript |
| Forks | 8,549 |
| Issues | 1,822 |
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
| Stars | 108,570 |
| 语言 | TypeScript |
| Forks | 13,358 |
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
| Stars | 97,974 |
| 语言 | TypeScript |
| Forks | 5,405 |
| Issues | 687 |
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
| Stars | 97,798 |
| 语言 | TypeScript |
| Forks | 54,591 |
| Issues | 1,359 |
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
| Stars | 94,604 |
| 语言 | TypeScript |
| Forks | 5,196 |
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
| Stars | 83,893 |
| 语言 | TypeScript |
| Forks | 10,408 |
| Issues | 404 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,137 |
| 语言 | TypeScript |
| Forks | 7,589 |
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
| Stars | 79,956 |
| 语言 | TypeScript |
| Forks | 8,061 |
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
| Stars | 244,571 |
| 语言 | JavaScript |
| Forks | 50,954 |
| Issues | 1,228 |
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
| Stars | 148,118 |
| 语言 | JavaScript |
| Forks | 26,725 |
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
| Stars | 116,773 |
| 语言 | JavaScript |
| Forks | 35,364 |
| Issues | 2,626 |
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
| Stars | 111,976 |
| 语言 | JavaScript |
| Forks | 36,325 |
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
| Stars | 109,034 |
| 语言 | JavaScript |
| Forks | 11,643 |
| Issues | 268 |
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
| Stars | 98,183 |
| 语言 | JavaScript |
| Forks | 32,685 |
| Issues | 1,582 |
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
| Stars | 95,616 |
| 语言 | JavaScript |
| Forks | 15,365 |
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
| Stars | 86,327 |
| 语言 | JavaScript |
| Forks | 4,888 |
| Issues | 988 |
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
| Stars | 71,014 |
| 语言 | JavaScript |
| Forks | 16,809 |
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
| Stars | 67,363 |
| 语言 | JavaScript |
| Forks | 11,967 |
| Issues | 550 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,326 |
| 语言 | JavaScript |
| Forks | 9,192 |
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
| Stars | 65,833 |
| 语言 | JavaScript |
| Forks | 9,374 |
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
| Stars | 62,797 |
| 语言 | JavaScript |
| Forks | 4,011 |
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
| Stars | 60,477 |
| 语言 | JavaScript |
| Forks | 5,650 |
| Issues | 68 |
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
| Stars | 59,843 |
| 语言 | JavaScript |
| Forks | 20,480 |
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
| Stars | 57,423 |
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
| Stars | 53,145 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 450 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,534 |
| 语言 | JavaScript |
| Forks | 11,476 |
| Issues | 238 |
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
| Stars | 133,495 |
| 语言 | Go |
| Forks | 18,923 |
| Issues | 9,971 |
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
| Stars | 105,955 |
| 语言 | Go |
| Forks | 15,003 |
| Issues | 44 |
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
| Stars | 87,630 |
| 语言 | Go |
| Forks | 8,240 |
| Issues | 260 |
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
| Stars | 81,785 |
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
| Stars | 68,622 |
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
| Stars | 56,674 |
| 语言 | Go |
| Forks | 5,035 |
| Issues | 1,168 |
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
| Forks | 21,889 |
| Issues | 400 |
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
| Stars | 49,321 |
| 语言 | Go |
| Forks | 7,953 |
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
| Stars | 343,023 |
| 语言 | Python |
| Forks | 55,417 |
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
| Stars | 86,071 |
| 语言 | Python |
| Forks | 7,216 |
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
| Stars | 138,780 |
| 语言 | TypeScript |
| Forks | 16,498 |
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
| Stars | 79,057 |
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
| Stars | 61,318 |
| 语言 | JavaScript |
| Forks | 7,135 |
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
| Stars | 151,495 |
| 语言 | Python |
| Forks | 11,534 |
| Issues | 327 |
| Topics | awesome, github, hellogithub, python |
