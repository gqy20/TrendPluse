# 项目发现报告 (2026-04-30)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 121 |
| 去重移除 | 33 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 14 |
| 💬 LLM 界面 | 21 |
| 🧠 机器学习框架 | 9 |
| 🛠️ 开发工具 | 14 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 68 |

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
| Stars | 134,971 |
| 语言 | Python |
| Forks | 19,186 |
| Issues | 318 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

OpenWebUI 是一个功能全面的开源 AI 界面平台，支持 Ollama、OpenAI API 等多种 LLM 后端，内置 RAG 和 MCP 协议支持，Stars 数超过 13 万，是构建私有化 AI 应用的理想选择，特别适合需要数据隐私控制和自托管部署的企业与开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API 云端服务，灵活切换不同 LLM 提供商
- RAG 检索增强：内置检索增强生成功能，可连接外部知识库提升问答质量
- MCP 协议支持：支持 Model Context Protocol，实现与各种 AI 工具和插件的无缝集成
- 自托管部署：提供完整的自部署方案，支持 Docker 一键部署，数据完全自主控制
- 现代化 Web UI：响应式 Web 界面，支持实时对话、模型管理、对话历史等功能

**适用场景**:
- 企业私有化 AI 部署：需要处理敏感数据、希望 AI 数据留存的金融机构、医疗健康、企业知识管理等领域
- 个人开发者与 AI 爱好者：希望本地运行开源大模型（如 Llama、Gemma 等）、构建个人 AI 助手的技术爱好者
- 研究机构与教育场景：需要实验不同 LLM 模型、进行 AI 对话研究和教学演示的学术环境



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 126,576 |
| 语言 | Python |
| Forks | 18,941 |
| Issues | 7,352 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI研究组织 Nous Research 开发的通用AI Agent框架，支持多种主流大语言模型（OpenAI GPT、Claude等）接入，具备高度可扩展性和模块化设计，适合构建复杂的AI自动化工作流程。凭借12.6万Stars的高人气和MIT开源许可证，是企业及个人开发者快速构建AI Agent应用的优秀选择。

**技术亮点**:
- 多模型支持：无缝集成 Anthropic Claude、OpenAI GPT、ChatGPT 等主流大语言模型，支持灵活切换和混合使用
- 模块化架构：采用松耦合设计，工具调用、记忆管理、任务规划等核心模块可独立扩展和定制
- Agent能力框架：内置 Tool Use、Chain-of-Thought、ReAct 等先进Agent设计模式，支持复杂任务分解与执行
- 开源可扩展：MIT许可证允许商业使用，代码完全开源便于深度定制和安全审计
- 生态丰富：支持 Claude Code、Codex 等代码执行能力，覆盖编程、自动化、对话等多种应用场景

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理、报表分析等业务流程自动化，提升运营效率
- 开发者AI助手：集成到开发工作流，实现代码审查、Bug修复、文档生成等开发辅助功能
- 个人效率工具：作为个人AI助理处理邮件整理、会议纪要、日程管理等日常事务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,862 |
| 语言 | JavaScript |
| Forks | 26,479 |
| Issues | 145 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 代理开发框架，通过 Skills（技能系统）、Instincts（本能机制）、Memory（记忆管理）和 Security（安全防护）四大核心模块，为开发者提供了从代码生成到生产环境部署的全链路优化方案，特别适合追求高效和安全并重的团队。

**技术亮点**:
- 多代理框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，实现跨平台统一优化
- Memory 记忆管理系统：提供持久化上下文记忆能力，让 AI 代理在长会话中保持状态连贯性
- Security 安全防护体系：内置代码安全审查机制，防止恶意指令注入和数据泄露风险
- Skills 技能扩展系统：模块化的技能注册与调用机制，支持自定义工作流编排
- MCP 协议集成：深度整合 Model Context Protocol，实现标准化的工具生态互联

**适用场景**:
- 企业级 AI 编程助手部署：为大型开发团队构建统一、安全、可审计的 AI 编码辅助平台
- AI Agent 性能调优：通过研究优先的方法论，优化 AI 代理的响应速度和准确率
- 开发者个人效率提升：利用 Memory 和 Skills 系统打造个性化的 AI 编程搭档



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,947 |
| 语言 | Go |
| Forks | 4,036 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 推理引擎，提供统一的 API 接口支持 LLM、图像、音频、视频等多种模型类型，核心优势是无需 GPU 即可在消费级硬件上运行大模型，特别适合隐私敏感或成本受限的场景。

**技术亮点**:
- 基于 Go 语言开发，性能高效，支持并发处理，适合生产环境部署
- 提供 OpenAI API 兼容接口，可无缝替换云端 AI 服务，降低迁移成本
- 支持多种模型架构：llama、mamba、qwen、whisper、stable-diffusion、musicgen 等
- 去中心化设计，支持 libp2p 分布式部署，可构建本地 AI 网络
- 支持 CPU 和 GPU 推理，适配从树莓派到高端服务器的多种硬件

**适用场景**:
- 私有化 AI 部署：企业或个人希望在本地运行 AI 模型，避免数据上传到第三方云服务，满足数据隐私合规要求
- 边缘计算场景：在没有稳定网络或 GPU 资源的边缘设备（如物联网网关、嵌入式设备）上运行 AI 推理任务
- 开发测试环境：开发者使用兼容 OpenAI 的 API 在本地进行 AI 应用开发和调试，降低 API 调用成本
- 离线 AI 应用：为无法访问互联网的环境（如企业内部网络、偏远地区）提供 AI 能力
- 多模型统一管理：通过单一接口管理多种类型的 AI 模型（文本生成、图像生成、语音识别等），简化系统架构



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,896 |
| 语言 | TypeScript |
| Forks | 15,041 |
| Issues | 747 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 协作平台之一，拥有 75,000+ Stars 的社区认可度。它创新性地支持多 Agent 协作设计，并原生集成 MCP 协议连接多种大模型，为开发者和企业提供了从原型到生产的完整 Agent 开发框架。

**技术亮点**:
- MCP（Model Context Protocol）协议支持：原生集成 MCP 协议，无缝连接 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- 多 Agent 协作框架：支持设计和管理多个 Agent 组成的协作团队，Agent 之间可分工协作、共享上下文，适合复杂任务分解处理
- 知识库与 RAG 集成：内置知识库功能，支持检索增强生成模式，让 Agent 能够基于私有知识进行问答和推理
- TypeScript 全栈架构：从前端到后端保持类型安全，便于二次开发和定制，降低维护成本
- 现代化 UI/UX 设计：提供直观的可视化界面，支持 Agent 的快速创建、配置和监控，降低使用门槛

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部智能助手，整合知识库实现客服、HR、行政等部门的自动化服务
- 多 Agent 工作流编排：需要多个 AI Agent 协同处理复杂业务流程的场景，如数据分析、报告生成、多步骤决策等
- 知识密集型应用：适用于需要结合私有知识库进行问答、检索和内容生成的场景，如教育、法律、医疗等垂直领域



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,800 |
| 语言 | Python |
| Forks | 8,643 |
| Issues | 997 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持 100+ 开源模型（ Llama、Qwen、DeepSeek、Gemma 等）的统一高效微调，集成 LoRA、QLoRA、RLHF、DPO 等多种前沿技术，显著降低 LLM 微调的工程门槛，在 ACL 2024 发表并拥有超过 7 万 Stars，是研究和企业落地 LLM 微调的首选工具。

**技术亮点**:
- 统一的微调框架：支持 100+ LLMs 和 VLMs（视觉-语言模型），包括 Llama3、Qwen、DeepSeek、Gemma、Mistral 等主流开源模型
- 多 PEFT 方法集成：内置 LoRA、QLoRA、AdaLoRA、DoRA、GaLore 等多种参数高效微调算法
- 支持强化学习微调：集成 RLHF（PPO）、DPO、ORPO 等对齐技术，便于构建更安全的 AI 助手
- 量化训练支持：支持 4-bit / 8-bit 量化，大幅降低 GPU 显存需求，使消费级 GPU 也能微调大模型
- MoE 与 Agent 支持：支持混合专家（MoE）模型微调，并提供 Agent 训练能力，适配复杂多步推理任务

**适用场景**:
- 企业定制化 AI：企业可基于 LlamaFactory 使用自有业务数据微调专属大模型（如客服机器人、行业知识助手），结合 RLHF 提升模型安全性和实用性
- 学术研究与论文复现：研究人员可快速复现 LoRA、QLoRA、RLHF 等论文中的微调实验，降低科研实验的工程成本
- 个人开发者与爱好者：个人开发者可在消费级 GPU（如 RTX 3090）上微调 7B-70B 参数模型，学习 LLM 训练流程或构建本地 AI 应用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,255 |
| 语言 | TypeScript |
| Forks | 6,002 |
| Issues | 33 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和向量检索实现了 Claude Code 的长期记忆能力，让 AI 能够跨会话学习和复用上下文，极大提升了开发效率和代码连贯性，是 AI 辅助编程领域的标杆项目。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，支持高维 embeddings 的高效存储和相似度搜索
- 集成 Claude Agent SDK 进行 AI 驱动的记忆压缩，自动提取关键信息并减少上下文噪音
- RAG（检索增强生成）架构设计，实现记忆存储-检索-注入的完整闭环
- SQLite + ChromaDB 混合存储方案，兼顾结构化数据管理和向量语义检索
- 支持多维度记忆关联，上下文感知的智能检索和会话恢复能力

**适用场景**:
- 个人开发者：跨项目维护代码上下文，让 AI 在新会话中快速理解历史决策和代码风格
- 企业团队：建立项目知识库，沉淀编码规范和解决方案，新成员可快速融入项目上下文
- AI Agent 开发：构建具备长期记忆能力的智能助手，适用于复杂多轮对话场景



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,863 |
| 语言 | HTML |
| Forks | 4,966 |
| Issues | 14 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个专注于 Claude Code 使用的实践指南仓库，近 5 万星的高人气证明了其在 AI 辅助编程领域的实用价值。项目从 vibe coding 基础延伸到 agentic engineering 高级实践，为开发者提供了完整的 AI 编程能力提升路径。

**技术亮点**:
- 系统化的 Claude Code 最佳实践指南，涵盖命令使用、技能开发和代理工作流设计
- 提供 Agentic Engineering 实践方法论，将 AI 编程从简单辅助提升到工程化水平
- 包含丰富的 Context Engineering 技术，帮助优化 AI 代码生成的上下文理解
- 覆盖多个实用场景的代码模板和命令示例，可直接应用于实际开发
- MIT 许可证允许商业使用，社区活跃且持续更新

**适用场景**:
- 企业开发团队引入 AI 辅助编程时的培训教材和实践参考
- 个人开发者学习 Claude Code 高效使用技巧，提升编程生产力
- 团队建立 AI 代码审查和 agentic workflow 的规范指南



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,046 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 11 |
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
| Stars | 42,001 |
| 语言 | Python |
| Forks | 5,077 |
| Issues | 112 |
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
| Stars | 39,084 |
| 语言 | Python |
| Forks | 6,193 |
| Issues | 74 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,139 |
| 语言 | TypeScript |
| Forks | 3,868 |
| Issues | 477 |
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
| Stars | 113,372 |
| 语言 | TypeScript |
| Forks | 7,207 |
| Issues | 301 |
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
| Stars | 59,306 |
| 语言 | JavaScript |
| Forks | 6,405 |
| Issues | 345 |
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
| Stars | 72,421 |
| 语言 | Python |
| Forks | 9,151 |
| Issues | 400 |
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
| Stars | 55,207 |
| 语言 | TypeScript |
| Forks | 4,468 |
| Issues | 672 |
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
| Stars | 108,201 |
| 语言 | Python |
| Forks | 15,948 |
| Issues | 9 |
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
| Stars | 91,402 |
| 语言 | Python |
| Forks | 10,405 |
| Issues | 239 |
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
| Stars | 52,428 |
| 语言 | TypeScript |
| Forks | 24,242 |
| Issues | 829 |
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
| Stars | 186,260 |
| 语言 | TypeScript |
| Forks | 57,266 |
| Issues | 1,560 |
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
| Stars | 155,351 |
| 语言 | Java |
| Forks | 46,153 |
| Issues | 65 |
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
| Stars | 147,563 |
| 语言 | Python |
| Forks | 8,883 |
| Issues | 946 |
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
| Stars | 60,208 |
| 语言 | Jupyter Notebook |
| Forks | 20,388 |
| Issues | 3 |
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
| Stars | 57,250 |
| 语言 | Python |
| Forks | 6,186 |
| Issues | 563 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,618 |
| 语言 | TypeScript |
| Forks | 9,460 |
| Issues | 111 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,079 |
| 语言 | TypeScript |
| Forks | 3,711 |
| Issues | 302 |
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
| Stars | 56,476 |
| 语言 | Rust |
| Forks | 3,668 |
| Issues | 691 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (14 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,971 |
| 语言 | Python |
| Forks | 19,186 |
| Issues | 318 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

OpenWebUI 是一个功能全面的开源 AI 界面平台，支持 Ollama、OpenAI API 等多种 LLM 后端，内置 RAG 和 MCP 协议支持，Stars 数超过 13 万，是构建私有化 AI 应用的理想选择，特别适合需要数据隐私控制和自托管部署的企业与开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API 云端服务，灵活切换不同 LLM 提供商
- RAG 检索增强：内置检索增强生成功能，可连接外部知识库提升问答质量
- MCP 协议支持：支持 Model Context Protocol，实现与各种 AI 工具和插件的无缝集成
- 自托管部署：提供完整的自部署方案，支持 Docker 一键部署，数据完全自主控制
- 现代化 Web UI：响应式 Web 界面，支持实时对话、模型管理、对话历史等功能

**适用场景**:
- 企业私有化 AI 部署：需要处理敏感数据、希望 AI 数据留存的金融机构、医疗健康、企业知识管理等领域
- 个人开发者与 AI 爱好者：希望本地运行开源大模型（如 Llama、Gemma 等）、构建个人 AI 助手的技术爱好者
- 研究机构与教育场景：需要实验不同 LLM 模型、进行 AI 对话研究和教学演示的学术环境



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,896 |
| 语言 | TypeScript |
| Forks | 15,041 |
| Issues | 747 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 协作平台之一，拥有 75,000+ Stars 的社区认可度。它创新性地支持多 Agent 协作设计，并原生集成 MCP 协议连接多种大模型，为开发者和企业提供了从原型到生产的完整 Agent 开发框架。

**技术亮点**:
- MCP（Model Context Protocol）协议支持：原生集成 MCP 协议，无缝连接 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- 多 Agent 协作框架：支持设计和管理多个 Agent 组成的协作团队，Agent 之间可分工协作、共享上下文，适合复杂任务分解处理
- 知识库与 RAG 集成：内置知识库功能，支持检索增强生成模式，让 Agent 能够基于私有知识进行问答和推理
- TypeScript 全栈架构：从前端到后端保持类型安全，便于二次开发和定制，降低维护成本
- 现代化 UI/UX 设计：提供直观的可视化界面，支持 Agent 的快速创建、配置和监控，降低使用门槛

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部智能助手，整合知识库实现客服、HR、行政等部门的自动化服务
- 多 Agent 工作流编排：需要多个 AI Agent 协同处理复杂业务流程的场景，如数据分析、报告生成、多步骤决策等
- 知识密集型应用：适用于需要结合私有知识库进行问答、检索和内容生成的场景，如教育、法律、医疗等垂直领域



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,255 |
| 语言 | TypeScript |
| Forks | 6,002 |
| Issues | 33 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和向量检索实现了 Claude Code 的长期记忆能力，让 AI 能够跨会话学习和复用上下文，极大提升了开发效率和代码连贯性，是 AI 辅助编程领域的标杆项目。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，支持高维 embeddings 的高效存储和相似度搜索
- 集成 Claude Agent SDK 进行 AI 驱动的记忆压缩，自动提取关键信息并减少上下文噪音
- RAG（检索增强生成）架构设计，实现记忆存储-检索-注入的完整闭环
- SQLite + ChromaDB 混合存储方案，兼顾结构化数据管理和向量语义检索
- 支持多维度记忆关联，上下文感知的智能检索和会话恢复能力

**适用场景**:
- 个人开发者：跨项目维护代码上下文，让 AI 在新会话中快速理解历史决策和代码风格
- 企业团队：建立项目知识库，沉淀编码规范和解决方案，新成员可快速融入项目上下文
- AI Agent 开发：构建具备长期记忆能力的智能助手，适用于复杂多轮对话场景



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,046 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 11 |
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
| Stars | 42,001 |
| 语言 | Python |
| Forks | 5,077 |
| Issues | 112 |
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
| Stars | 39,084 |
| 语言 | Python |
| Forks | 6,193 |
| Issues | 74 |
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
| Stars | 101,662 |
| 语言 | TypeScript |
| Forks | 12,237 |
| Issues | 975 |
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
| Stars | 59,306 |
| 语言 | JavaScript |
| Forks | 6,405 |
| Issues | 345 |
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
| Stars | 108,201 |
| 语言 | Python |
| Forks | 15,948 |
| Issues | 9 |
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
| Stars | 76,886 |
| 语言 | Python |
| Forks | 10,345 |
| Issues | 209 |
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
| Stars | 52,428 |
| 语言 | TypeScript |
| Forks | 24,242 |
| Issues | 829 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,072 |
| 语言 | Go |
| Forks | 3,986 |
| Issues | 1,074 |
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
| Stars | 34,618 |
| 语言 | Python |
| Forks | 4,894 |
| Issues | 222 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,079 |
| 语言 | TypeScript |
| Forks | 3,711 |
| Issues | 302 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (21 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,971 |
| 语言 | Python |
| Forks | 19,186 |
| Issues | 318 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

OpenWebUI 是一个功能全面的开源 AI 界面平台，支持 Ollama、OpenAI API 等多种 LLM 后端，内置 RAG 和 MCP 协议支持，Stars 数超过 13 万，是构建私有化 AI 应用的理想选择，特别适合需要数据隐私控制和自托管部署的企业与开发者。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API 云端服务，灵活切换不同 LLM 提供商
- RAG 检索增强：内置检索增强生成功能，可连接外部知识库提升问答质量
- MCP 协议支持：支持 Model Context Protocol，实现与各种 AI 工具和插件的无缝集成
- 自托管部署：提供完整的自部署方案，支持 Docker 一键部署，数据完全自主控制
- 现代化 Web UI：响应式 Web 界面，支持实时对话、模型管理、对话历史等功能

**适用场景**:
- 企业私有化 AI 部署：需要处理敏感数据、希望 AI 数据留存的金融机构、医疗健康、企业知识管理等领域
- 个人开发者与 AI 爱好者：希望本地运行开源大模型（如 Llama、Gemma 等）、构建个人 AI 助手的技术爱好者
- 研究机构与教育场景：需要实验不同 LLM 模型、进行 AI 对话研究和教学演示的学术环境



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 126,576 |
| 语言 | Python |
| Forks | 18,941 |
| Issues | 7,352 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名开源AI研究组织 Nous Research 开发的通用AI Agent框架，支持多种主流大语言模型（OpenAI GPT、Claude等）接入，具备高度可扩展性和模块化设计，适合构建复杂的AI自动化工作流程。凭借12.6万Stars的高人气和MIT开源许可证，是企业及个人开发者快速构建AI Agent应用的优秀选择。

**技术亮点**:
- 多模型支持：无缝集成 Anthropic Claude、OpenAI GPT、ChatGPT 等主流大语言模型，支持灵活切换和混合使用
- 模块化架构：采用松耦合设计，工具调用、记忆管理、任务规划等核心模块可独立扩展和定制
- Agent能力框架：内置 Tool Use、Chain-of-Thought、ReAct 等先进Agent设计模式，支持复杂任务分解与执行
- 开源可扩展：MIT许可证允许商业使用，代码完全开源便于深度定制和安全审计
- 生态丰富：支持 Claude Code、Codex 等代码执行能力，覆盖编程、自动化、对话等多种应用场景

**适用场景**:
- 企业智能自动化：构建客服机器人、文档处理、报表分析等业务流程自动化，提升运营效率
- 开发者AI助手：集成到开发工作流，实现代码审查、Bug修复、文档生成等开发辅助功能
- 个人效率工具：作为个人AI助理处理邮件整理、会议纪要、日程管理等日常事务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,862 |
| 语言 | JavaScript |
| Forks | 26,479 |
| Issues | 145 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 代理开发框架，通过 Skills（技能系统）、Instincts（本能机制）、Memory（记忆管理）和 Security（安全防护）四大核心模块，为开发者提供了从代码生成到生产环境部署的全链路优化方案，特别适合追求高效和安全并重的团队。

**技术亮点**:
- 多代理框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，实现跨平台统一优化
- Memory 记忆管理系统：提供持久化上下文记忆能力，让 AI 代理在长会话中保持状态连贯性
- Security 安全防护体系：内置代码安全审查机制，防止恶意指令注入和数据泄露风险
- Skills 技能扩展系统：模块化的技能注册与调用机制，支持自定义工作流编排
- MCP 协议集成：深度整合 Model Context Protocol，实现标准化的工具生态互联

**适用场景**:
- 企业级 AI 编程助手部署：为大型开发团队构建统一、安全、可审计的 AI 编码辅助平台
- AI Agent 性能调优：通过研究优先的方法论，优化 AI 代理的响应速度和准确率
- 开发者个人效率提升：利用 Memory 和 Skills 系统打造个性化的 AI 编程搭档



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,896 |
| 语言 | TypeScript |
| Forks | 15,041 |
| Issues | 747 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的开源 AI Agent 协作平台之一，拥有 75,000+ Stars 的社区认可度。它创新性地支持多 Agent 协作设计，并原生集成 MCP 协议连接多种大模型，为开发者和企业提供了从原型到生产的完整 Agent 开发框架。

**技术亮点**:
- MCP（Model Context Protocol）协议支持：原生集成 MCP 协议，无缝连接 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- 多 Agent 协作框架：支持设计和管理多个 Agent 组成的协作团队，Agent 之间可分工协作、共享上下文，适合复杂任务分解处理
- 知识库与 RAG 集成：内置知识库功能，支持检索增强生成模式，让 Agent 能够基于私有知识进行问答和推理
- TypeScript 全栈架构：从前端到后端保持类型安全，便于二次开发和定制，降低维护成本
- 现代化 UI/UX 设计：提供直观的可视化界面，支持 Agent 的快速创建、配置和监控，降低使用门槛

**适用场景**:
- 企业智能助手搭建：企业可基于 LobeHub 构建内部智能助手，整合知识库实现客服、HR、行政等部门的自动化服务
- 多 Agent 工作流编排：需要多个 AI Agent 协同处理复杂业务流程的场景，如数据分析、报告生成、多步骤决策等
- 知识密集型应用：适用于需要结合私有知识库进行问答、检索和内容生成的场景，如教育、法律、医疗等垂直领域



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,255 |
| 语言 | TypeScript |
| Forks | 6,002 |
| Issues | 33 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 架构和向量检索实现了 Claude Code 的长期记忆能力，让 AI 能够跨会话学习和复用上下文，极大提升了开发效率和代码连贯性，是 AI 辅助编程领域的标杆项目。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，支持高维 embeddings 的高效存储和相似度搜索
- 集成 Claude Agent SDK 进行 AI 驱动的记忆压缩，自动提取关键信息并减少上下文噪音
- RAG（检索增强生成）架构设计，实现记忆存储-检索-注入的完整闭环
- SQLite + ChromaDB 混合存储方案，兼顾结构化数据管理和向量语义检索
- 支持多维度记忆关联，上下文感知的智能检索和会话恢复能力

**适用场景**:
- 个人开发者：跨项目维护代码上下文，让 AI 在新会话中快速理解历史决策和代码风格
- 企业团队：建立项目知识库，沉淀编码规范和解决方案，新成员可快速融入项目上下文
- AI Agent 开发：构建具备长期记忆能力的智能助手，适用于复杂多轮对话场景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,247 |
| 语言 | HTML |
| Forks | 21,050 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是全球最大且最活跃的开源提示词库之一（16万+ Stars），汇集了600+经过社区验证的优质提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，一键复制即可使用，同时提供完整私有化部署方案，是个人开发者和企业团队提升 AI 生产力的首选资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术架构，支持服务端渲染（SSR）和静态站点生成（SSG）
- 提供完整的 API 接口和 Webhook 集成能力，便于与现有工作流和自动化工具对接
- 支持多种 AI 模型平台（OpenAI GPT-4、Claude、Gemini），提示词模板兼容性强
- 可完全私有化部署，无需任何外部依赖运行，确保企业数据安全和隐私合规
- 采用开源许可证，提供透明可审计的代码库，支持社区持续贡献和版本迭代

**适用场景**:
- 个人开发者快速获取经过验证的高质量提示词，提升与 AI 助手的交互效率和输出质量
- 企业团队私有化部署专属提示词库，保护内部知识资产和数据隐私，满足合规要求
- AI 应用开发者参考社区最佳实践，学习提示词工程（Prompt Engineering）设计模式
- 内容创作者和知识工作者构建个人提示词工作流，实现高效的 AI 辅助创作



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,863 |
| 语言 | HTML |
| Forks | 4,966 |
| Issues | 14 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个专注于 Claude Code 使用的实践指南仓库，近 5 万星的高人气证明了其在 AI 辅助编程领域的实用价值。项目从 vibe coding 基础延伸到 agentic engineering 高级实践，为开发者提供了完整的 AI 编程能力提升路径。

**技术亮点**:
- 系统化的 Claude Code 最佳实践指南，涵盖命令使用、技能开发和代理工作流设计
- 提供 Agentic Engineering 实践方法论，将 AI 编程从简单辅助提升到工程化水平
- 包含丰富的 Context Engineering 技术，帮助优化 AI 代码生成的上下文理解
- 覆盖多个实用场景的代码模板和命令示例，可直接应用于实际开发
- MIT 许可证允许商业使用，社区活跃且持续更新

**适用场景**:
- 企业开发团队引入 AI 辅助编程时的培训教材和实践参考
- 个人开发者学习 Claude Code 高效使用技巧，提升编程生产力
- 团队建立 AI 代码审查和 agentic workflow 的规范指南



### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,306 |
| 语言 | JavaScript |
| Forks | 6,405 |
| Issues | 345 |
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
| Stars | 72,421 |
| 语言 | Python |
| Forks | 9,151 |
| Issues | 400 |
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
| Stars | 55,207 |
| 语言 | TypeScript |
| Forks | 4,468 |
| Issues | 672 |
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
| Stars | 52,428 |
| 语言 | TypeScript |
| Forks | 24,242 |
| Issues | 829 |
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
| Stars | 78,693 |
| 语言 | Python |
| Forks | 16,298 |
| Issues | 4,694 |
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
| Stars | 147,563 |
| 语言 | Python |
| Forks | 8,883 |
| Issues | 946 |
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
| Stars | 57,250 |
| 语言 | Python |
| Forks | 6,186 |
| Issues | 563 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,408 |
| 语言 | Go |
| Forks | 15,904 |
| Issues | 3,125 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 91,760 |
| 语言 | Jupyter Notebook |
| Forks | 14,140 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,618 |
| 语言 | TypeScript |
| Forks | 9,460 |
| Issues | 111 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,240 |
| 语言 | Python |
| Forks | 2,720 |
| Issues | 172 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,250 |
| 语言 | Rust |
| Forks | 9,659 |
| Issues | 2 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,673 |
| 语言 | Python |
| Forks | 7,485 |
| Issues | 136 |
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
| Stars | 118,970 |
| 语言 | Python |
| Forks | 7,864 |
| Issues | 649 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (9 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,800 |
| 语言 | Python |
| Forks | 8,643 |
| Issues | 997 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持 100+ 开源模型（ Llama、Qwen、DeepSeek、Gemma 等）的统一高效微调，集成 LoRA、QLoRA、RLHF、DPO 等多种前沿技术，显著降低 LLM 微调的工程门槛，在 ACL 2024 发表并拥有超过 7 万 Stars，是研究和企业落地 LLM 微调的首选工具。

**技术亮点**:
- 统一的微调框架：支持 100+ LLMs 和 VLMs（视觉-语言模型），包括 Llama3、Qwen、DeepSeek、Gemma、Mistral 等主流开源模型
- 多 PEFT 方法集成：内置 LoRA、QLoRA、AdaLoRA、DoRA、GaLore 等多种参数高效微调算法
- 支持强化学习微调：集成 RLHF（PPO）、DPO、ORPO 等对齐技术，便于构建更安全的 AI 助手
- 量化训练支持：支持 4-bit / 8-bit 量化，大幅降低 GPU 显存需求，使消费级 GPU 也能微调大模型
- MoE 与 Agent 支持：支持混合专家（MoE）模型微调，并提供 Agent 训练能力，适配复杂多步推理任务

**适用场景**:
- 企业定制化 AI：企业可基于 LlamaFactory 使用自有业务数据微调专属大模型（如客服机器人、行业知识助手），结合 RLHF 提升模型安全性和实用性
- 学术研究与论文复现：研究人员可快速复现 LoRA、QLoRA、RLHF 等论文中的微调实验，降低科研实验的工程成本
- 个人开发者与爱好者：个人开发者可在消费级 GPU（如 RTX 3090）上微调 7B-70B 参数模型，学习 LLM 训练流程或构建本地 AI 应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,792 |
| 语言 | Python |
| Forks | 6,677 |
| Issues | 77 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是金融科技领域的明星开源项目，拥有超过66,000颗Stars，为分析师和量化交易员提供了统一的数据访问接口，同时支持AI代理集成，是构建智能投研系统的理想基础设施。

**技术亮点**:
- 统一的数据抽象层：提供标准化的API接口，整合多个数据源（股票、加密货币、宏观经济数据等），简化数据获取流程
- 模块化架构设计：采用插件化设计，支持数据源、终端、分析工具的灵活扩展和自定义开发
- AI/ML集成能力：原生支持机器学习模型集成，可用于金融预测、情感分析、量化策略开发等场景
- 丰富的可视化组件：内置专业的金融图表和仪表盘，支持交互式数据探索和分析报告生成
- 全面的金融产品覆盖：支持股票、期权、加密货币、固定收益、衍生品等多类资产的数据和分析

**适用场景**:
- 量化投资研究：用于获取市场数据、构建量化策略、回测交易模型、开发因子分析系统
- 金融数据分析：为投资机构、投研团队提供数据聚合、快速分析、报告生成的工作流支持
- AI金融应用开发：作为AI代理的数据后端，为智能投顾、自动化交易、风险管理等AI应用提供实时金融数据支撑



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,247 |
| 语言 | HTML |
| Forks | 21,050 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是全球最大且最活跃的开源提示词库之一（16万+ Stars），汇集了600+经过社区验证的优质提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，一键复制即可使用，同时提供完整私有化部署方案，是个人开发者和企业团队提升 AI 生产力的首选资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术架构，支持服务端渲染（SSR）和静态站点生成（SSG）
- 提供完整的 API 接口和 Webhook 集成能力，便于与现有工作流和自动化工具对接
- 支持多种 AI 模型平台（OpenAI GPT-4、Claude、Gemini），提示词模板兼容性强
- 可完全私有化部署，无需任何外部依赖运行，确保企业数据安全和隐私合规
- 采用开源许可证，提供透明可审计的代码库，支持社区持续贡献和版本迭代

**适用场景**:
- 个人开发者快速获取经过验证的高质量提示词，提升与 AI 助手的交互效率和输出质量
- 企业团队私有化部署专属提示词库，保护内部知识资产和数据隐私，满足合规要求
- AI 应用开发者参考社区最佳实践，学习提示词工程（Prompt Engineering）设计模式
- 内容创作者和知识工作者构建个人提示词工作流，实现高效的 AI 辅助创作



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,123 |
| 语言 | Python |
| Forks | 33,066 |
| Issues | 2,341 |
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
| Stars | 78,693 |
| 语言 | Python |
| Forks | 16,298 |
| Issues | 4,694 |
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
| Stars | 110,802 |
| 语言 | Python |
| Forks | 12,921 |
| Issues | 4,009 |
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
| Stars | 99,560 |
| 语言 | Python |
| Forks | 27,630 |
| Issues | 18,538 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 91,760 |
| 语言 | Jupyter Notebook |
| Forks | 14,140 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,079 |
| 语言 | TypeScript |
| Forks | 3,711 |
| Issues | 302 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 🛠️ 开发工具 (14 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,862 |
| 语言 | JavaScript |
| Forks | 26,479 |
| Issues | 145 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是目前最全面的 AI 代理开发框架，通过 Skills（技能系统）、Instincts（本能机制）、Memory（记忆管理）和 Security（安全防护）四大核心模块，为开发者提供了从代码生成到生产环境部署的全链路优化方案，特别适合追求高效和安全并重的团队。

**技术亮点**:
- 多代理框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，实现跨平台统一优化
- Memory 记忆管理系统：提供持久化上下文记忆能力，让 AI 代理在长会话中保持状态连贯性
- Security 安全防护体系：内置代码安全审查机制，防止恶意指令注入和数据泄露风险
- Skills 技能扩展系统：模块化的技能注册与调用机制，支持自定义工作流编排
- MCP 协议集成：深度整合 Model Context Protocol，实现标准化的工具生态互联

**适用场景**:
- 企业级 AI 编程助手部署：为大型开发团队构建统一、安全、可审计的 AI 编码辅助平台
- AI Agent 性能调优：通过研究优先的方法论，优化 AI 代理的响应速度和准确率
- 开发者个人效率提升：利用 Memory 和 Skills 系统打造个性化的 AI 编程搭档



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,947 |
| 语言 | Go |
| Forks | 4,036 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 推理引擎，提供统一的 API 接口支持 LLM、图像、音频、视频等多种模型类型，核心优势是无需 GPU 即可在消费级硬件上运行大模型，特别适合隐私敏感或成本受限的场景。

**技术亮点**:
- 基于 Go 语言开发，性能高效，支持并发处理，适合生产环境部署
- 提供 OpenAI API 兼容接口，可无缝替换云端 AI 服务，降低迁移成本
- 支持多种模型架构：llama、mamba、qwen、whisper、stable-diffusion、musicgen 等
- 去中心化设计，支持 libp2p 分布式部署，可构建本地 AI 网络
- 支持 CPU 和 GPU 推理，适配从树莓派到高端服务器的多种硬件

**适用场景**:
- 私有化 AI 部署：企业或个人希望在本地运行 AI 模型，避免数据上传到第三方云服务，满足数据隐私合规要求
- 边缘计算场景：在没有稳定网络或 GPU 资源的边缘设备（如物联网网关、嵌入式设备）上运行 AI 推理任务
- 开发测试环境：开发者使用兼容 OpenAI 的 API 在本地进行 AI 应用开发和调试，降低 API 调用成本
- 离线 AI 应用：为无法访问互联网的环境（如企业内部网络、偏远地区）提供 AI 能力
- 多模型统一管理：通过单一接口管理多种类型的 AI 模型（文本生成、图像生成、语音识别等），简化系统架构



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,046 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 11 |
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
| Stars | 72,421 |
| 语言 | Python |
| Forks | 9,151 |
| Issues | 400 |
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
| Stars | 55,207 |
| 语言 | TypeScript |
| Forks | 4,468 |
| Issues | 672 |
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
| Stars | 186,260 |
| 语言 | TypeScript |
| Forks | 57,266 |
| Issues | 1,560 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,788 |
| 语言 | Python |
| Forks | 9,176 |
| Issues | 180 |
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
| Stars | 82,741 |
| 语言 | Python |
| Forks | 9,647 |
| Issues | 276 |
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
| Stars | 184,421 |
| 语言 | TypeScript |
| Forks | 39,579 |
| Issues | 16,899 |
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
| Stars | 94,220 |
| 语言 | TypeScript |
| Forks | 9,409 |
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
| Stars | 79,068 |
| 语言 | TypeScript |
| Forks | 5,840 |
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
| Stars | 79,905 |
| 语言 | Go |
| Forks | 2,796 |
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
| Stars | 77,258 |
| 语言 | Go |
| Forks | 2,802 |
| Issues | 957 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### ⭐ 中优先级


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 159,840 |
| 语言 | Python |
| Forks | 13,255 |
| Issues | 2,504 |
| Topics | cli, downloader, python, sponsorblock, youtube-dl, youtube-downloader, yt-dlp |
| 许可证 | The Unlicense |


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
| Stars | 55,207 |
| 语言 | TypeScript |
| Forks | 4,468 |
| Issues | 672 |
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
| Stars | 186,260 |
| 语言 | TypeScript |
| Forks | 57,266 |
| Issues | 1,560 |
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
| Stars | 57,250 |
| 语言 | Python |
| Forks | 6,186 |
| Issues | 563 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,665 |
| 语言 | Go |
| Forks | 10,327 |
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
| Stars | 122,008 |
| 语言 | Go |
| Forks | 42,975 |
| Issues | 2,706 |
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
| Stars | 71,517 |
| 语言 | Go |
| Forks | 18,925 |
| Issues | 3,809 |
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
| Stars | 55,251 |
| 语言 | Go |
| Forks | 6,639 |
| Issues | 2,774 |
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
| Stars | 47,503 |
| 语言 | Go |
| Forks | 5,056 |
| Issues | 987 |
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
| Stars | 94,220 |
| 语言 | TypeScript |
| Forks | 9,409 |
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
| Stars | 78,024 |
| 语言 | TypeScript |
| Forks | 6,823 |
| Issues | 421 |
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
| Stars | 86,072 |
| 语言 | JavaScript |
| Forks | 7,748 |
| Issues | 729 |
| Topics | docker, monitor, monitoring, responsive, self-hosted, selfhosted, single-page-app, socket-io, uptime, uptime-monitoring, webapp, websocket |
| 许可证 | MIT License |


### traefik/traefik

**描述**: The Cloud Native Application Proxy

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,936 |
| 语言 | Go |
| Forks | 5,952 |
| Issues | 784 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,838 |
| 语言 | Go |
| Forks | 7,451 |
| Issues | 81 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


### usememos/memos

**描述**: Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,303 |
| 语言 | Go |
| Forks | 4,316 |
| Issues | 24 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,098 |
| 语言 | Go |
| Forks | 1,919 |
| Issues | 322 |
| Topics | ci, devops, github-actions, golang |
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
| Stars | 86,072 |
| 语言 | JavaScript |
| Forks | 7,748 |
| Issues | 729 |
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
| Stars | 63,852 |
| 语言 | Go |
| Forks | 10,370 |
| Issues | 762 |
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
| Stars | 45,947 |
| 语言 | Go |
| Forks | 4,036 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地化 AI 推理引擎，提供统一的 API 接口支持 LLM、图像、音频、视频等多种模型类型，核心优势是无需 GPU 即可在消费级硬件上运行大模型，特别适合隐私敏感或成本受限的场景。

**技术亮点**:
- 基于 Go 语言开发，性能高效，支持并发处理，适合生产环境部署
- 提供 OpenAI API 兼容接口，可无缝替换云端 AI 服务，降低迁移成本
- 支持多种模型架构：llama、mamba、qwen、whisper、stable-diffusion、musicgen 等
- 去中心化设计，支持 libp2p 分布式部署，可构建本地 AI 网络
- 支持 CPU 和 GPU 推理，适配从树莓派到高端服务器的多种硬件

**适用场景**:
- 私有化 AI 部署：企业或个人希望在本地运行 AI 模型，避免数据上传到第三方云服务，满足数据隐私合规要求
- 边缘计算场景：在没有稳定网络或 GPU 资源的边缘设备（如物联网网关、嵌入式设备）上运行 AI 推理任务
- 开发测试环境：开发者使用兼容 OpenAI 的 API 在本地进行 AI 应用开发和调试，降低 API 调用成本
- 离线 AI 应用：为无法访问互联网的环境（如企业内部网络、偏远地区）提供 AI 能力
- 多模型统一管理：通过单一接口管理多种类型的 AI 模型（文本生成、图像生成、语音识别等），简化系统架构



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,788 |
| 语言 | Python |
| Forks | 9,176 |
| Issues | 180 |
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
| Stars | 87,364 |
| 语言 | Python |
| Forks | 33,865 |
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
| Stars | 100,054 |
| 语言 | TypeScript |
| Forks | 27,214 |
| Issues | 1,143 |
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
| Stars | 79,068 |
| 语言 | TypeScript |
| Forks | 5,840 |
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
| Stars | 68,979 |
| 语言 | JavaScript |
| Forks | 23,208 |
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
| Forks | 10,206 |
| Issues | 368 |
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
| Stars | 51,834 |
| 语言 | JavaScript |
| Forks | 4,710 |
| Issues | 1,470 |
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
| Stars | 88,416 |
| 语言 | Go |
| Forks | 8,590 |
| Issues | 681 |
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
| Stars | 71,965 |
| 语言 | Go |
| Forks | 4,709 |
| Issues | 237 |
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
| Stars | 58,045 |
| 语言 | Go |
| Forks | 3,338 |
| Issues | 18 |
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
| Stars | 101,662 |
| 语言 | TypeScript |
| Forks | 12,237 |
| Issues | 975 |
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
| Stars | 59,306 |
| 语言 | JavaScript |
| Forks | 6,405 |
| Issues | 345 |
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
| Stars | 44,072 |
| 语言 | Go |
| Forks | 3,986 |
| Issues | 1,074 |
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
| Stars | 51,665 |
| 语言 | Go |
| Forks | 10,327 |
| Issues | 241 |
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
| Stars | 161,247 |
| 语言 | HTML |
| Forks | 21,050 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是全球最大且最活跃的开源提示词库之一（16万+ Stars），汇集了600+经过社区验证的优质提示词模板，支持 ChatGPT、Claude、Gemini 等多平台，一键复制即可使用，同时提供完整私有化部署方案，是个人开发者和企业团队提升 AI 生产力的首选资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术架构，支持服务端渲染（SSR）和静态站点生成（SSG）
- 提供完整的 API 接口和 Webhook 集成能力，便于与现有工作流和自动化工具对接
- 支持多种 AI 模型平台（OpenAI GPT-4、Claude、Gemini），提示词模板兼容性强
- 可完全私有化部署，无需任何外部依赖运行，确保企业数据安全和隐私合规
- 采用开源许可证，提供透明可审计的代码库，支持社区持续贡献和版本迭代

**适用场景**:
- 个人开发者快速获取经过验证的高质量提示词，提升与 AI 助手的交互效率和输出质量
- 企业团队私有化部署专属提示词库，保护内部知识资产和数据隐私，满足合规要求
- AI 应用开发者参考社区最佳实践，学习提示词工程（Prompt Engineering）设计模式
- 内容创作者和知识工作者构建个人提示词工作流，实现高效的 AI 辅助创作



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,001 |
| 语言 | Python |
| Forks | 5,077 |
| Issues | 112 |
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
| Stars | 57,618 |
| 语言 | TypeScript |
| Forks | 9,460 |
| Issues | 111 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,240 |
| 语言 | Python |
| Forks | 2,720 |
| Issues | 172 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,836 |
| 语言 | TypeScript |
| Forks | 10,041 |
| Issues | 2,269 |
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
| Stars | 87,745 |
| 语言 | TypeScript |
| Forks | 8,923 |
| Issues | 1,657 |
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
| Stars | 171,430 |
| 语言 | Go |
| Forks | 13,178 |
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
| Stars | 127,635 |
| 语言 | JavaScript |
| Forks | 12,481 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (68 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,452 |
| 语言 | Unknown |
| Forks | 34,099 |
| Issues | 137 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,313 |
| 语言 | Python |
| Forks | 9,000 |
| Issues | 2,991 |
| Topics | llm-app |
| 许可证 | Apache License 2.0 |


### mattpocock/skills

**描述**: Skills for Real Engineers. Straight from my .claude directory.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,912 |
| 语言 | Shell |
| Forks | 3,996 |
| Issues | 6 |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,503 |
| 语言 | Python |
| Forks | 13,435 |
| Issues | 114 |
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
| Stars | 91,967 |
| 语言 | Python |
| Forks | 7,959 |
| Issues | 652 |
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
| Stars | 387,428 |
| 语言 | Python |
| Forks | 66,204 |
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
| Stars | 115,639 |
| 语言 | TypeScript |
| Forks | 6,062 |
| Issues | 20 |
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
| Stars | 114,948 |
| 语言 | TypeScript |
| Forks | 8,401 |
| Issues | 300 |
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
| Stars | 87,316 |
| 语言 | TypeScript |
| Forks | 12,819 |
| Issues | 492 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,996 |
| 语言 | JavaScript |
| Forks | 4,994 |
| Issues | 29 |
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
| Stars | 48,293 |
| 语言 | Go |
| Forks | 10,328 |
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
| Stars | 107,606 |
| 语言 | C++ |
| Forks | 17,622 |
| Issues | 1,561 |
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
| Stars | 63,373 |
| 语言 | Python |
| Forks | 1,632 |
| Issues | 34 |
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
| Stars | 33,731 |
| 语言 | TypeScript |
| Forks | 3,835 |
| Issues | 364 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 295,252 |
| 语言 | Python |
| Forks | 27,797 |
| Issues | 21 |
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
| Stars | 86,876 |
| 语言 | Python |
| Forks | 37,394 |
| Issues | 3,708 |
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
| Stars | 77,667 |
| 语言 | Python |
| Forks | 45,112 |
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
| Stars | 443,940 |
| 语言 | TypeScript |
| Forks | 44,432 |
| Issues | 181 |
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
| Stars | 353,934 |
| 语言 | TypeScript |
| Forks | 43,983 |
| Issues | 12 |
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
| Stars | 122,281 |
| 语言 | TypeScript |
| Forks | 13,476 |
| Issues | 3,029 |
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
| Stars | 113,289 |
| 语言 | TypeScript |
| Forks | 8,688 |
| Issues | 1,853 |
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
| Stars | 108,706 |
| 语言 | TypeScript |
| Forks | 13,374 |
| Issues | 5,032 |
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
| Stars | 99,368 |
| 语言 | TypeScript |
| Forks | 5,520 |
| Issues | 696 |
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
| Stars | 97,902 |
| 语言 | TypeScript |
| Forks | 54,595 |
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
| Stars | 94,810 |
| 语言 | TypeScript |
| Forks | 5,214 |
| Issues | 94 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,315 |
| 语言 | TypeScript |
| Forks | 8,115 |
| Issues | 735 |
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
| Stars | 244,771 |
| 语言 | JavaScript |
| Forks | 51,018 |
| Issues | 1,256 |
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
| Stars | 116,991 |
| 语言 | JavaScript |
| Forks | 35,487 |
| Issues | 2,648 |
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
| Stars | 112,263 |
| 语言 | JavaScript |
| Forks | 36,353 |
| Issues | 516 |
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
| Forks | 11,659 |
| Issues | 167 |
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
| Stars | 98,256 |
| 语言 | JavaScript |
| Forks | 32,653 |
| Issues | 1,534 |
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
| Stars | 95,696 |
| 语言 | JavaScript |
| Forks | 15,431 |
| Issues | 48 |
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
| Stars | 86,447 |
| 语言 | JavaScript |
| Forks | 4,898 |
| Issues | 994 |
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
| Stars | 67,633 |
| 语言 | JavaScript |
| Forks | 4,540 |
| Issues | 100 |
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
| Stars | 65,779 |
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
| Stars | 64,189 |
| 语言 | JavaScript |
| Forks | 4,080 |
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
| Stars | 60,797 |
| 语言 | JavaScript |
| Forks | 5,660 |
| Issues | 69 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,437 |
| 语言 | JavaScript |
| Forks | 12,312 |
| Issues | 28 |
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
| Stars | 53,217 |
| 语言 | JavaScript |
| Forks | 10,601 |
| Issues | 443 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,721 |
| 语言 | JavaScript |
| Forks | 11,521 |
| Issues | 240 |
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
| Stars | 133,695 |
| 语言 | Go |
| Forks | 18,989 |
| Issues | 9,987 |
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
| Stars | 106,196 |
| 语言 | Go |
| Forks | 15,034 |
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
| Stars | 87,840 |
| 语言 | Go |
| Forks | 8,254 |
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
| Stars | 83,336 |
| 语言 | Go |
| Forks | 5,137 |
| Issues | 384 |
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
| Stars | 68,594 |
| 语言 | Go |
| Forks | 3,229 |
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
| Stars | 56,945 |
| 语言 | Go |
| Forks | 5,064 |
| Issues | 1,177 |
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
| Stars | 51,009 |
| 语言 | Go |
| Forks | 21,892 |
| Issues | 413 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,856 |
| 语言 | Go |
| Forks | 8,856 |
| Issues | 18 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 89,541 |
| 语言 | Shell |
| Forks | 14,523 |
| Issues | 118 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,114 |
| 语言 | Python |
| Forks | 11,754 |
| Issues | 352 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 102,346 |
| 语言 | Unknown |
| Forks | 10,050 |
| Issues | 77 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,515 |
| 语言 | Python |
| Forks | 50,488 |
| Issues | 940 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 98,690 |
| 语言 | Python |
| Forks | 12,127 |
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
| Stars | 86,421 |
| 语言 | Python |
| Forks | 7,248 |
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
| Stars | 77,374 |
| 语言 | Python |
| Forks | 16,910 |
| Issues | 27 |
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
| Stars | 139,190 |
| 语言 | TypeScript |
| Forks | 16,544 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 84,833 |
| 语言 | TypeScript |
| Forks | 10,546 |
| Issues | 420 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,332 |
| 语言 | TypeScript |
| Forks | 7,602 |
| Issues | 35 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,119 |
| 语言 | JavaScript |
| Forks | 26,705 |
| Issues | 159 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,203 |
| 语言 | JavaScript |
| Forks | 32,684 |
| Issues | 279 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,099 |
| 语言 | JavaScript |
| Forks | 16,802 |
| Issues | 895 |
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
| Stars | 67,395 |
| 语言 | JavaScript |
| Forks | 11,953 |
| Issues | 556 |
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
| Stars | 66,358 |
| 语言 | JavaScript |
| Forks | 9,192 |
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
| Stars | 61,262 |
| 语言 | JavaScript |
| Forks | 7,154 |
| Issues | 141 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 59,837 |
| 语言 | JavaScript |
| Forks | 20,453 |
| Issues | 89 |
| Topics | jquery |
| 许可证 | MIT License |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,865 |
| 语言 | Go |
| Forks | 1,608 |
| Issues | 273 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,391 |
| 语言 | Go |
| Forks | 7,947 |
| Issues | 567 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,183 |
| 语言 | Go |
| Forks | 3,805 |
| Issues | 81 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
