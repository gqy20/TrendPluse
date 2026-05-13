# 项目发现报告 (2026-05-13)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
| 去重移除 | 35 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
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
| Stars | 148,488 |
| 语言 | Python |
| Forks | 23,376 |
| Issues | 10,917 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源 AI 组织 NousResearch 打造的高星项目（148K+ stars），支持多种主流 LLM 提供商（OpenAI、Anthropic等），是一个可扩展的 AI Agent 框架，MIT 许可证允许商业使用，非常适合构建智能自动化应用。

**技术亮点**:
- 支持多 LLM 提供商集成：无缝接入 OpenAI GPT、Anthropic Claude 等主流模型
- 模块化 Agent 架构：采用可扩展设计，方便自定义工具和插件
- 代码执行能力：内置 Claude Code/Codex 风格的代码生成与执行功能
- 开源可定制：基于 Hermes 系列模型，完全开源可修改
- Python 优先：充分利用 Python 生态，便于集成现有项目

**适用场景**:
- 企业智能自动化：构建客服机器人、流程自动化、RAG 问答系统等业务应用
- AI 辅助开发：集成到开发工作流，实现代码审查、自动化测试、智能IDE等功能
- 个人开发者快速原型：基于现有框架快速搭建 LLM 应用，降低开发门槛



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,925 |
| 语言 | Python |
| Forks | 19,511 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的 AI 界面平台，支持 Ollama 和 OpenAI API 双后端，提供了 RAG 检索增强、MCP 协议支持等企业级功能，同时支持完全自托管部署，能够满足从个人开发者到企业用户的多元化 AI 应用需求。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业数据安全合规要求
- RAG 检索增强生成：内置知识库检索功能，支持文档上传和语义搜索，提升模型回答质量
- MCP 协议支持：支持 Model Context Protocol 扩展，可与其他工具和服务深度集成
- 现代化 Web UI：提供直观的聊天界面，支持对话管理、多模态交互等丰富功能

**适用场景**:
- 企业 AI 助手：适合需要在内部部署 AI 对话系统，保护敏感数据的企业场景，如客服、知识库问答等
- 个人开发者本地开发：开发者可在本地运行完整的 AI 界面，支持 Ollama 管理本地大模型进行快速迭代测试
- 知识库智能问答：基于 RAG 功能，可构建私有知识库的智能问答系统，适用于文档检索、资料查询等场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,438 |
| 语言 | Python |
| Forks | 9,181 |
| Issues | 3,030 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（80k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，能够处理复杂的多跳推理任务，相比纯检索系统具有更强的语义理解和上下文管理能力，特别适合构建企业级知识问答和智能文档分析应用。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与 AI Agent 能力深度结合，支持复杂推理和多步工具调用
- 深度文档理解：基于深度学习的文档解析引擎，支持 PDF、Word、Excel、PPT 等多格式智能抽取
- Agentic Retrieval：超越传统关键词/向量检索，实现语义级代理检索和意图理解
- 优化的上下文管理：智能上下文压缩和分块策略，提升 LLM 对长文本的处理效率
- Apache 2.0 开源许可：完全开源可商用，社区活跃度高，文档完善易上手

**适用场景**:
- 企业知识库智能问答：构建私有化知识问答系统，支持复杂文档的语义理解和精准回答
- 智能客服与辅助决策：结合企业数据源，实现多轮对话式客户支持与决策建议
- 文档分析与挖掘：自动化解析合同、报告、手册等长文档，提取关键信息和知识图谱



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 181,292 |
| 语言 | JavaScript |
| Forks | 27,948 |
| Issues | 1 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专注于 AI 编程助手性能优化的框架，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，拥有 18 万+ Stars，提供了 Skills、Instincts、Memory 等高级功能，是提升 AI Agent 开发效率和企业级部署的首选方案。

**技术亮点**:
- 跨平台多 Agent 兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- 性能优化系统：专门针对 agent harness 的性能进行深度优化，提升响应速度和效率
- Memory 记忆系统：内置记忆机制，让 AI Agent 能够跨会话保持上下文和知识
- Security 安全机制：提供企业级安全保障，确保 AI Agent 交互的安全性
- Research-First 开发理念：采用研究驱动的开发方法，持续跟进 LLM 领域最新技术

**适用场景**:
- 企业级 AI 辅助编程：团队可以使用该框架统一管理多个 AI 编程工具，提升开发团队的整体效率
- LLM 工作流优化：开发者可以通过 Skills 和 Instincts 系统自定义 AI Agent 行为，打造个性化工作流
- AI Agent 研究与实验：研究人员可以使用该平台快速构建和测试新的 AI Agent 架构



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,242 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 152 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源本地 AI 引擎，支持运行 LLMs、图像、语音、视频等多种模型，且无需 GPU 即可在普通硬件上运行，为开发者和企业提供了经济高效的私有化 AI 部署方案。其 OpenAI 兼容 API 和丰富的多模态支持让用户可以轻松迁移现有应用，同时保障数据隐私安全。

**技术亮点**:
- 多模态模型支持：支持文本生成 (Llama, Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、语音合成 (TTS) 和目标检测等多种 AI 任务
- 零硬件依赖：可在任何硬件上运行，无需昂贵的 GPU，通过优化的 CPU 推理实现高效部署
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，开发者无需修改代码即可无缝迁移现有应用
- 去中心化架构：基于 libp2p 实现分布式部署，支持构建去中心化的 AI 推理网络
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业（如医疗、金融）可本地运行 AI 模型，数据不出域
- 个人开发者/小团队：无需购买 GPU，通过普通服务器或个人电脑即可部署和实验各种 AI 模型



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,006 |
| 语言 | TypeScript |
| Forks | 15,163 |
| Issues | 792 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 Agent 协作平台，提供了开箱即用的多 Agent 协作框架和统一的多 AI 提供商集成方案（支持 OpenAI、Claude、DeepSeek、Gemini 等），同时具备 MCP 协议支持和知识库功能。凭借 77,006 Stars 的社区认可度，它为开发者提供了一个生产级的 Agent 开发起点，能够显著加速 AI 应用从原型到落地的过程。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 之间的协作与通信，提供 Agent 团队设计能力，让 Agent 成为工作交互的基本单位
- 统一的多 AI 提供商集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供一致的 API 接口抽象
- MCP (Model Context Protocol) 支持：遵循 AI 领域的标准上下文协议，便于扩展和集成第三方工具
- 知识库集成：内置知识管理功能，增强 Agent 的上下文理解和问答能力
- TypeScript 完整类型系统：全栈 TypeScript 开发，提供完善的类型安全保证和 IDE 支持

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 框架构建复杂的企业工作流自动化，如客户服务、知识问答、内容审核等场景
- AI 应用快速原型开发：开发者可以利用已有的 Agent 基础设施快速验证 AI 产品想法，减少从零搭建的时间成本
- 团队协作与工作流编排：构建由多个专业 Agent 组成的虚拟团队，分工处理不同任务，提升团队整体效率



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,466 |
| 语言 | TypeScript |
| Forks | 6,488 |
| Issues | 71 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是目前最实用的 AI Agent 记忆增强工具，通过 AI 压缩技术解决大模型上下文窗口限制问题，同时支持 10+ 种主流 AI Agent（Claude Code、Copilot、Gemini 等），让 Agent 能够真正"记住"跨会话的工作内容和偏好，极大提升长期任务的效率。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，配合 Embeddings 技术实现精准的上下文召回
- 使用 AI 压缩算法减少记忆体积，解决大模型 token 限制问题
- 集成 SQLite 本地持久化存储，数据安全可控且部署简单
- 支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot 等 10+ 种 AI Agent
- TypeScript 原生实现，完美适配现代 AI 开发技术栈

**适用场景**:
- 企业级 AI Agent 部署：在客服、数据分析等长期任务中保持上下文连贯性，避免重复解释项目背景
- 个人开发者效率提升：编程时让 AI 记住项目结构、代码规范和个人偏好，减少沟通成本
- 多 Agent 协作场景：多个 AI Agent 共享记忆库，实现任务接力与知识传递



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,223 |
| 语言 | Python |
| Forks | 8,701 |
| Issues | 1,006 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调工具箱，通过统一接口支持 100+ 主流 LLMs 和 VLMs，集成 LoRA、QLoRA、RLHF 等主流微调技术，让研究者和开发者能够以最低成本快速完成模型定制化训练，特别适合私有化部署和领域适配场景。

**技术亮点**:
- 多模型统一框架：支持 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及 VLMs，一键切换
- 高效微调技术栈：完整支持 LoRA、QLoRA、Prefix Tuning、Ptuning 等 PEFT 方法，大幅降低算力需求
- 先进训练范式：支持 SFT、DPO、ORPO、PPO 等 RLHF 相关训练方法，覆盖从基础微调到强化学习对齐全流程
- 推理优化集成：内置 4-bit/8-bit 量化（GPTQ、AWQ、GGUF），支持 MoE 架构，提供完整优化链路
- 工程化易用性：提供 Web UI 和 CLI 工具，支持分布式训练，配备详细文档和预置数据集

**适用场景**:
- 企业私有化部署：对开源基础模型进行领域适配和个性化训练，用于客服、知识库、文档分析等垂直场景
- 学术研究与实验：快速验证不同微调算法和模型架构效果，加速论文实验迭代
- AI 应用开发者：利用量化压缩功能将大模型部署到资源受限环境，快速构建端侧 AI 应用



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,891 |
| 语言 | Python |
| Forks | 14,601 |
| Issues | 339 |
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
| Stars | 60,232 |
| 语言 | TypeScript |
| Forks | 9,852 |
| Issues | 123 |
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
| Stars | 52,845 |
| 语言 | HTML |
| Forks | 5,289 |
| Issues | 13 |
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
| Stars | 48,994 |
| 语言 | Python |
| Forks | 5,896 |
| Issues | 119 |
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
| Stars | 46,225 |
| 语言 | Java |
| Forks | 15,986 |
| Issues | 19 |
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
| Stars | 39,162 |
| 语言 | Python |
| Forks | 6,202 |
| Issues | 83 |
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
| Stars | 50,254 |
| 语言 | TypeScript |
| Forks | 5,607 |
| Issues | 545 |
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
| Stars | 119,399 |
| 语言 | TypeScript |
| Forks | 7,364 |
| Issues | 318 |
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
| Stars | 59,994 |
| 语言 | JavaScript |
| Forks | 6,485 |
| Issues | 361 |
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
| Stars | 73,398 |
| 语言 | Python |
| Forks | 9,274 |
| Issues | 428 |
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
| Stars | 57,612 |
| 语言 | TypeScript |
| Forks | 4,673 |
| Issues | 620 |
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
| Stars | 110,145 |
| 语言 | Python |
| Forks | 16,313 |
| Issues | 10 |
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
| Stars | 93,761 |
| 语言 | Python |
| Forks | 10,604 |
| Issues | 227 |
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
| Stars | 52,794 |
| 语言 | TypeScript |
| Forks | 24,331 |
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
| Stars | 187,714 |
| 语言 | TypeScript |
| Forks | 57,603 |
| Issues | 1,457 |
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
| Stars | 155,636 |
| 语言 | Java |
| Forks | 46,138 |
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
| Stars | 148,069 |
| 语言 | Python |
| Forks | 8,971 |
| Issues | 928 |
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
| Stars | 61,373 |
| 语言 | Jupyter Notebook |
| Forks | 20,786 |
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
| Stars | 69,739 |
| 语言 | Rust |
| Forks | 4,471 |
| Issues | 849 |
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
| Stars | 59,629 |
| 语言 | Python |
| Forks | 6,470 |
| Issues | 614 |
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
| Stars | 136,925 |
| 语言 | Python |
| Forks | 19,511 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的 AI 界面平台，支持 Ollama 和 OpenAI API 双后端，提供了 RAG 检索增强、MCP 协议支持等企业级功能，同时支持完全自托管部署，能够满足从个人开发者到企业用户的多元化 AI 应用需求。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业数据安全合规要求
- RAG 检索增强生成：内置知识库检索功能，支持文档上传和语义搜索，提升模型回答质量
- MCP 协议支持：支持 Model Context Protocol 扩展，可与其他工具和服务深度集成
- 现代化 Web UI：提供直观的聊天界面，支持对话管理、多模态交互等丰富功能

**适用场景**:
- 企业 AI 助手：适合需要在内部部署 AI 对话系统，保护敏感数据的企业场景，如客服、知识库问答等
- 个人开发者本地开发：开发者可在本地运行完整的 AI 界面，支持 Ollama 管理本地大模型进行快速迭代测试
- 知识库智能问答：基于 RAG 功能，可构建私有知识库的智能问答系统，适用于文档检索、资料查询等场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,438 |
| 语言 | Python |
| Forks | 9,181 |
| Issues | 3,030 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（80k+ Stars），创新性地将 RAG 与 Agent 能力深度融合，能够处理复杂的多跳推理任务，相比纯检索系统具有更强的语义理解和上下文管理能力，特别适合构建企业级知识问答和智能文档分析应用。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与 AI Agent 能力深度结合，支持复杂推理和多步工具调用
- 深度文档理解：基于深度学习的文档解析引擎，支持 PDF、Word、Excel、PPT 等多格式智能抽取
- Agentic Retrieval：超越传统关键词/向量检索，实现语义级代理检索和意图理解
- 优化的上下文管理：智能上下文压缩和分块策略，提升 LLM 对长文本的处理效率
- Apache 2.0 开源许可：完全开源可商用，社区活跃度高，文档完善易上手

**适用场景**:
- 企业知识库智能问答：构建私有化知识问答系统，支持复杂文档的语义理解和精准回答
- 智能客服与辅助决策：结合企业数据源，实现多轮对话式客户支持与决策建议
- 文档分析与挖掘：自动化解析合同、报告、手册等长文档，提取关键信息和知识图谱



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,006 |
| 语言 | TypeScript |
| Forks | 15,163 |
| Issues | 792 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 Agent 协作平台，提供了开箱即用的多 Agent 协作框架和统一的多 AI 提供商集成方案（支持 OpenAI、Claude、DeepSeek、Gemini 等），同时具备 MCP 协议支持和知识库功能。凭借 77,006 Stars 的社区认可度，它为开发者提供了一个生产级的 Agent 开发起点，能够显著加速 AI 应用从原型到落地的过程。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 之间的协作与通信，提供 Agent 团队设计能力，让 Agent 成为工作交互的基本单位
- 统一的多 AI 提供商集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供一致的 API 接口抽象
- MCP (Model Context Protocol) 支持：遵循 AI 领域的标准上下文协议，便于扩展和集成第三方工具
- 知识库集成：内置知识管理功能，增强 Agent 的上下文理解和问答能力
- TypeScript 完整类型系统：全栈 TypeScript 开发，提供完善的类型安全保证和 IDE 支持

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 框架构建复杂的企业工作流自动化，如客户服务、知识问答、内容审核等场景
- AI 应用快速原型开发：开发者可以利用已有的 Agent 基础设施快速验证 AI 产品想法，减少从零搭建的时间成本
- 团队协作与工作流编排：构建由多个专业 Agent 组成的虚拟团队，分工处理不同任务，提升团队整体效率



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,466 |
| 语言 | TypeScript |
| Forks | 6,488 |
| Issues | 71 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是目前最实用的 AI Agent 记忆增强工具，通过 AI 压缩技术解决大模型上下文窗口限制问题，同时支持 10+ 种主流 AI Agent（Claude Code、Copilot、Gemini 等），让 Agent 能够真正"记住"跨会话的工作内容和偏好，极大提升长期任务的效率。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，配合 Embeddings 技术实现精准的上下文召回
- 使用 AI 压缩算法减少记忆体积，解决大模型 token 限制问题
- 集成 SQLite 本地持久化存储，数据安全可控且部署简单
- 支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot 等 10+ 种 AI Agent
- TypeScript 原生实现，完美适配现代 AI 开发技术栈

**适用场景**:
- 企业级 AI Agent 部署：在客服、数据分析等长期任务中保持上下文连贯性，避免重复解释项目背景
- 个人开发者效率提升：编程时让 AI 记住项目结构、代码规范和个人偏好，减少沟通成本
- 多 Agent 协作场景：多个 AI Agent 共享记忆库，实现任务接力与知识传递



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,994 |
| 语言 | Python |
| Forks | 5,896 |
| Issues | 119 |
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
| Stars | 46,225 |
| 语言 | Java |
| Forks | 15,986 |
| Issues | 19 |
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
| Stars | 39,162 |
| 语言 | Python |
| Forks | 6,202 |
| Issues | 83 |
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
| Stars | 102,285 |
| 语言 | TypeScript |
| Forks | 12,374 |
| Issues | 1,015 |
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
| Stars | 59,994 |
| 语言 | JavaScript |
| Forks | 6,485 |
| Issues | 361 |
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
| Stars | 110,145 |
| 语言 | Python |
| Forks | 16,313 |
| Issues | 10 |
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
| Stars | 77,756 |
| 语言 | Python |
| Forks | 10,426 |
| Issues | 202 |
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
| Stars | 52,794 |
| 语言 | TypeScript |
| Forks | 24,331 |
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
| Stars | 47,600 |
| 语言 | Python |
| Forks | 5,169 |
| Issues | 265 |
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
| Stars | 44,274 |
| 语言 | Go |
| Forks | 3,999 |
| Issues | 893 |
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
| Stars | 35,149 |
| 语言 | Python |
| Forks | 4,985 |
| Issues | 235 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


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
| Stars | 148,488 |
| 语言 | Python |
| Forks | 23,376 |
| Issues | 10,917 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源 AI 组织 NousResearch 打造的高星项目（148K+ stars），支持多种主流 LLM 提供商（OpenAI、Anthropic等），是一个可扩展的 AI Agent 框架，MIT 许可证允许商业使用，非常适合构建智能自动化应用。

**技术亮点**:
- 支持多 LLM 提供商集成：无缝接入 OpenAI GPT、Anthropic Claude 等主流模型
- 模块化 Agent 架构：采用可扩展设计，方便自定义工具和插件
- 代码执行能力：内置 Claude Code/Codex 风格的代码生成与执行功能
- 开源可定制：基于 Hermes 系列模型，完全开源可修改
- Python 优先：充分利用 Python 生态，便于集成现有项目

**适用场景**:
- 企业智能自动化：构建客服机器人、流程自动化、RAG 问答系统等业务应用
- AI 辅助开发：集成到开发工作流，实现代码审查、自动化测试、智能IDE等功能
- 个人开发者快速原型：基于现有框架快速搭建 LLM 应用，降低开发门槛



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,925 |
| 语言 | Python |
| Forks | 19,511 |
| Issues | 250 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的 AI 界面平台，支持 Ollama 和 OpenAI API 双后端，提供了 RAG 检索增强、MCP 协议支持等企业级功能，同时支持完全自托管部署，能够满足从个人开发者到企业用户的多元化 AI 应用需求。

**技术亮点**:
- 多后端兼容：同时支持 Ollama 本地模型和 OpenAI API，可灵活切换不同 LLM 提供商
- 自托管部署：支持完全私有化部署，数据不出本地，满足企业数据安全合规要求
- RAG 检索增强生成：内置知识库检索功能，支持文档上传和语义搜索，提升模型回答质量
- MCP 协议支持：支持 Model Context Protocol 扩展，可与其他工具和服务深度集成
- 现代化 Web UI：提供直观的聊天界面，支持对话管理、多模态交互等丰富功能

**适用场景**:
- 企业 AI 助手：适合需要在内部部署 AI 对话系统，保护敏感数据的企业场景，如客服、知识库问答等
- 个人开发者本地开发：开发者可在本地运行完整的 AI 界面，支持 Ollama 管理本地大模型进行快速迭代测试
- 知识库智能问答：基于 RAG 功能，可构建私有知识库的智能问答系统，适用于文档检索、资料查询等场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 181,292 |
| 语言 | JavaScript |
| Forks | 27,948 |
| Issues | 1 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专注于 AI 编程助手性能优化的框架，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，拥有 18 万+ Stars，提供了 Skills、Instincts、Memory 等高级功能，是提升 AI Agent 开发效率和企业级部署的首选方案。

**技术亮点**:
- 跨平台多 Agent 兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- 性能优化系统：专门针对 agent harness 的性能进行深度优化，提升响应速度和效率
- Memory 记忆系统：内置记忆机制，让 AI Agent 能够跨会话保持上下文和知识
- Security 安全机制：提供企业级安全保障，确保 AI Agent 交互的安全性
- Research-First 开发理念：采用研究驱动的开发方法，持续跟进 LLM 领域最新技术

**适用场景**:
- 企业级 AI 辅助编程：团队可以使用该框架统一管理多个 AI 编程工具，提升开发团队的整体效率
- LLM 工作流优化：开发者可以通过 Skills 和 Instincts 系统自定义 AI Agent 行为，打造个性化工作流
- AI Agent 研究与实验：研究人员可以使用该平台快速构建和测试新的 AI Agent 架构



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,584 |
| 语言 | JavaScript |
| Forks | 3,295 |
| Issues | 194 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

一个将" caveman 说话风格"工程化为实用 token 优化工具的项目，通过幽默的 prompt 设计实现了 65% 的 token 消耗削减，对于需要在成本敏感场景下使用 Claude 的开发者具有极高的实用价值。

**技术亮点**:
- 基于 Anthropic Claude Code 的 Skill 插件架构，便于集成到 AI 辅助开发工作流中
- 通过独特的 caveman 语言风格 prompt 设计显著压缩 token 使用量
- 采用 JavaScript 实现，兼容 Node.js 生态，便于二次开发和扩展
- 项目包含完整的 prompt 工程最佳实践，可作为学习示例
- 支持自定义 caveman 说话风格参数，可灵活调整压缩效果

**适用场景**:
- AI 开发成本优化：在 API 调用费用敏感的项目中，使用 caveman 风格降低 token 消耗
- 学习 prompt 工程：通过该项目学习如何通过创意 prompt 设计实现高效 AI 交互
- Claude Code 工作流增强：为 Claude Code 添加 token 优化能力，提升开发效率



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,006 |
| 语言 | TypeScript |
| Forks | 15,163 |
| Issues | 792 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的 Agent 协作平台，提供了开箱即用的多 Agent 协作框架和统一的多 AI 提供商集成方案（支持 OpenAI、Claude、DeepSeek、Gemini 等），同时具备 MCP 协议支持和知识库功能。凭借 77,006 Stars 的社区认可度，它为开发者提供了一个生产级的 Agent 开发起点，能够显著加速 AI 应用从原型到落地的过程。

**技术亮点**:
- 多 Agent 协作框架：支持多 Agent 之间的协作与通信，提供 Agent 团队设计能力，让 Agent 成为工作交互的基本单位
- 统一的多 AI 提供商集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供一致的 API 接口抽象
- MCP (Model Context Protocol) 支持：遵循 AI 领域的标准上下文协议，便于扩展和集成第三方工具
- 知识库集成：内置知识管理功能，增强 Agent 的上下文理解和问答能力
- TypeScript 完整类型系统：全栈 TypeScript 开发，提供完善的类型安全保证和 IDE 支持

**适用场景**:
- 企业级 AI 应用开发：使用多 Agent 框架构建复杂的企业工作流自动化，如客户服务、知识问答、内容审核等场景
- AI 应用快速原型开发：开发者可以利用已有的 Agent 基础设施快速验证 AI 产品想法，减少从零搭建的时间成本
- 团队协作与工作流编排：构建由多个专业 Agent 组成的虚拟团队，分工处理不同任务，提升团队整体效率



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,466 |
| 语言 | TypeScript |
| Forks | 6,488 |
| Issues | 71 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是目前最实用的 AI Agent 记忆增强工具，通过 AI 压缩技术解决大模型上下文窗口限制问题，同时支持 10+ 种主流 AI Agent（Claude Code、Copilot、Gemini 等），让 Agent 能够真正"记住"跨会话的工作内容和偏好，极大提升长期任务的效率。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义检索，配合 Embeddings 技术实现精准的上下文召回
- 使用 AI 压缩算法减少记忆体积，解决大模型 token 限制问题
- 集成 SQLite 本地持久化存储，数据安全可控且部署简单
- 支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot 等 10+ 种 AI Agent
- TypeScript 原生实现，完美适配现代 AI 开发技术栈

**适用场景**:
- 企业级 AI Agent 部署：在客服、数据分析等长期任务中保持上下文连贯性，避免重复解释项目背景
- 个人开发者效率提升：编程时让 AI 记住项目结构、代码规范和个人偏好，减少沟通成本
- 多 Agent 协作场景：多个 AI Agent 共享记忆库，实现任务接力与知识传递



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,184 |
| 语言 | HTML |
| Forks | 21,112 |
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
| Stars | 94,389 |
| 语言 | Jupyter Notebook |
| Forks | 14,474 |
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
| Stars | 60,232 |
| 语言 | TypeScript |
| Forks | 9,852 |
| Issues | 123 |
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
| Stars | 52,845 |
| 语言 | HTML |
| Forks | 5,289 |
| Issues | 13 |
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
| Stars | 59,994 |
| 语言 | JavaScript |
| Forks | 6,485 |
| Issues | 361 |
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
| Stars | 73,398 |
| 语言 | Python |
| Forks | 9,274 |
| Issues | 428 |
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
| Stars | 57,612 |
| 语言 | TypeScript |
| Forks | 4,673 |
| Issues | 620 |
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
| Stars | 52,794 |
| 语言 | TypeScript |
| Forks | 24,331 |
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
| Stars | 79,912 |
| 语言 | Python |
| Forks | 16,756 |
| Issues | 4,961 |
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
| Stars | 148,069 |
| 语言 | Python |
| Forks | 8,971 |
| Issues | 928 |
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
| Stars | 59,629 |
| 语言 | Python |
| Forks | 6,470 |
| Issues | 614 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,339 |
| 语言 | Go |
| Forks | 16,099 |
| Issues | 3,243 |
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
| Stars | 48,688 |
| 语言 | Rust |
| Forks | 9,800 |
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
| Stars | 123,037 |
| 语言 | Python |
| Forks | 8,313 |
| Issues | 640 |
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
| Stars | 71,223 |
| 语言 | Python |
| Forks | 8,701 |
| Issues | 1,006 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调工具箱，通过统一接口支持 100+ 主流 LLMs 和 VLMs，集成 LoRA、QLoRA、RLHF 等主流微调技术，让研究者和开发者能够以最低成本快速完成模型定制化训练，特别适合私有化部署和领域适配场景。

**技术亮点**:
- 多模型统一框架：支持 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等 100+ 主流 LLMs 及 VLMs，一键切换
- 高效微调技术栈：完整支持 LoRA、QLoRA、Prefix Tuning、Ptuning 等 PEFT 方法，大幅降低算力需求
- 先进训练范式：支持 SFT、DPO、ORPO、PPO 等 RLHF 相关训练方法，覆盖从基础微调到强化学习对齐全流程
- 推理优化集成：内置 4-bit/8-bit 量化（GPTQ、AWQ、GGUF），支持 MoE 架构，提供完整优化链路
- 工程化易用性：提供 Web UI 和 CLI 工具，支持分布式训练，配备详细文档和预置数据集

**适用场景**:
- 企业私有化部署：对开源基础模型进行领域适配和个性化训练，用于客服、知识库、文档分析等垂直场景
- 学术研究与实验：快速验证不同微调算法和模型架构效果，加速论文实验迭代
- AI 应用开发者：利用量化压缩功能将大模型部署到资源受限环境，快速构建端侧 AI 应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,530 |
| 语言 | Python |
| Forks | 6,782 |
| Issues | 79 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个拥有 67k+ Stars 的成熟开源金融数据平台，为分析师、量化交易员和 AI 代理提供统一的金融数据获取框架，支持股票、加密货币、期权、衍生品等多品类数据，并内置 AI 和机器学习集成能力，大幅降低金融数据分析的开发门槛。

**技术亮点**:
- 支持多品类金融数据：覆盖股票、加密货币、期权、衍生品、固定收益、经济指标等，实现一站式数据获取
- 内置 AI/ML 集成能力：提供与大语言模型和机器学习框架的原生集成，便于构建智能投研和量化策略
- Python 生态深度整合：基于 Python 开发，提供简洁易用的 API，支持 pandas DataFrame 输出，便于数据分析和可视化
- 模块化架构设计：数据源、终端和扩展模块解耦，支持自定义数据源和功能扩展
- 活跃的开源社区：67k+ Stars，数千次提交，持续迭代更新，社区资源丰富

**适用场景**:
- 个人投资者和散户：使用 OpenBB 获取市场数据、进行技术分析和量化回测，快速搭建个人交易决策系统
- 量化交易团队：集成到量化投研流程，获取标准化金融数据，构建因子模型和算法交易策略
- AI 应用开发者：利用 OpenBB 的金融数据能力，为 AI 代理和智能投顾应用提供实时市场信息支持
- 金融机构：作为内部金融数据中台，统一管理数据源，降低数据采购成本，加速投研和产品开发



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,184 |
| 语言 | HTML |
| Forks | 21,112 |
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
| Stars | 94,389 |
| 语言 | Jupyter Notebook |
| Forks | 14,474 |
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
| Stars | 160,577 |
| 语言 | Python |
| Forks | 33,196 |
| Issues | 2,353 |
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
| Stars | 79,912 |
| 语言 | Python |
| Forks | 16,756 |
| Issues | 4,961 |
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
| Stars | 112,777 |
| 语言 | Python |
| Forks | 13,193 |
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
| Stars | 99,883 |
| 语言 | Python |
| Forks | 27,771 |
| Issues | 18,431 |
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
| Stars | 181,292 |
| 语言 | JavaScript |
| Forks | 27,948 |
| Issues | 1 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个专注于 AI 编程助手性能优化的框架，支持 Claude Code、Codex、Cursor 等主流 AI 编码工具，拥有 18 万+ Stars，提供了 Skills、Instincts、Memory 等高级功能，是提升 AI Agent 开发效率和企业级部署的首选方案。

**技术亮点**:
- 跨平台多 Agent 兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的统一优化框架
- 性能优化系统：专门针对 agent harness 的性能进行深度优化，提升响应速度和效率
- Memory 记忆系统：内置记忆机制，让 AI Agent 能够跨会话保持上下文和知识
- Security 安全机制：提供企业级安全保障，确保 AI Agent 交互的安全性
- Research-First 开发理念：采用研究驱动的开发方法，持续跟进 LLM 领域最新技术

**适用场景**:
- 企业级 AI 辅助编程：团队可以使用该框架统一管理多个 AI 编程工具，提升开发团队的整体效率
- LLM 工作流优化：开发者可以通过 Skills 和 Instincts 系统自定义 AI Agent 行为，打造个性化工作流
- AI Agent 研究与实验：研究人员可以使用该平台快速构建和测试新的 AI Agent 架构



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,242 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 152 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源本地 AI 引擎，支持运行 LLMs、图像、语音、视频等多种模型，且无需 GPU 即可在普通硬件上运行，为开发者和企业提供了经济高效的私有化 AI 部署方案。其 OpenAI 兼容 API 和丰富的多模态支持让用户可以轻松迁移现有应用，同时保障数据隐私安全。

**技术亮点**:
- 多模态模型支持：支持文本生成 (Llama, Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、语音合成 (TTS) 和目标检测等多种 AI 任务
- 零硬件依赖：可在任何硬件上运行，无需昂贵的 GPU，通过优化的 CPU 推理实现高效部署
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，开发者无需修改代码即可无缝迁移现有应用
- 去中心化架构：基于 libp2p 实现分布式部署，支持构建去中心化的 AI 推理网络
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业（如医疗、金融）可本地运行 AI 模型，数据不出域
- 个人开发者/小团队：无需购买 GPU，通过普通服务器或个人电脑即可部署和实验各种 AI 模型



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,225 |
| 语言 | Java |
| Forks | 15,986 |
| Issues | 19 |
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
| Stars | 73,398 |
| 语言 | Python |
| Forks | 9,274 |
| Issues | 428 |
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
| Stars | 57,612 |
| 语言 | TypeScript |
| Forks | 4,673 |
| Issues | 620 |
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
| Stars | 187,714 |
| 语言 | TypeScript |
| Forks | 57,603 |
| Issues | 1,457 |
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
| Stars | 59,629 |
| 语言 | Python |
| Forks | 6,470 |
| Issues | 614 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,038 |
| 语言 | JavaScript |
| Forks | 4,191 |
| Issues | 1,318 |
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
| Stars | 434,834 |
| 语言 | Python |
| Forks | 47,639 |
| Issues | 1,322 |
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
| Stars | 162,104 |
| 语言 | Python |
| Forks | 13,555 |
| Issues | 2,491 |
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
| Stars | 98,167 |
| 语言 | Python |
| Forks | 9,280 |
| Issues | 197 |
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
| Stars | 83,279 |
| 语言 | Python |
| Forks | 9,718 |
| Issues | 265 |
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
| Stars | 184,885 |
| 语言 | TypeScript |
| Forks | 39,809 |
| Issues | 17,542 |
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
| Stars | 94,313 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 256 |
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
| Stars | 79,175 |
| 语言 | TypeScript |
| Forks | 5,869 |
| Issues | 719 |
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
| Stars | 77,522 |
| 语言 | TypeScript |
| Forks | 6,667 |
| Issues | 152 |
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
| Stars | 80,224 |
| 语言 | Go |
| Forks | 2,805 |
| Issues | 317 |
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
| Stars | 77,886 |
| 语言 | Go |
| Forks | 2,832 |
| Issues | 961 |
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
| Stars | 57,612 |
| 语言 | TypeScript |
| Forks | 4,673 |
| Issues | 620 |
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
| Stars | 187,714 |
| 语言 | TypeScript |
| Forks | 57,603 |
| Issues | 1,457 |
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
| Stars | 59,629 |
| 语言 | Python |
| Forks | 6,470 |
| Issues | 614 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,699 |
| 语言 | Go |
| Forks | 10,350 |
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
| Stars | 122,237 |
| 语言 | Go |
| Forks | 43,048 |
| Issues | 2,696 |
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
| Stars | 71,548 |
| 语言 | Go |
| Forks | 18,949 |
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
| Stars | 55,649 |
| 语言 | Go |
| Forks | 6,692 |
| Issues | 2,792 |
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
| Stars | 94,313 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 256 |
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
| Stars | 78,700 |
| 语言 | TypeScript |
| Forks | 6,891 |
| Issues | 396 |
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
| Stars | 86,671 |
| 语言 | JavaScript |
| Forks | 7,831 |
| Issues | 742 |
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
| Stars | 70,268 |
| 语言 | Go |
| Forks | 1,920 |
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
| Stars | 63,144 |
| 语言 | Go |
| Forks | 5,985 |
| Issues | 814 |
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
| Stars | 59,540 |
| 语言 | Go |
| Forks | 4,341 |
| Issues | 21 |
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
| Stars | 47,511 |
| 语言 | Go |
| Forks | 5,058 |
| Issues | 990 |
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
| Stars | 60,929 |
| 语言 | Go |
| Forks | 7,489 |
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
| Stars | 86,671 |
| 语言 | JavaScript |
| Forks | 7,831 |
| Issues | 742 |
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
| Stars | 64,022 |
| 语言 | Go |
| Forks | 10,402 |
| Issues | 767 |
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
| Stars | 46,242 |
| 语言 | Go |
| Forks | 4,074 |
| Issues | 152 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一款功能强大的开源本地 AI 引擎，支持运行 LLMs、图像、语音、视频等多种模型，且无需 GPU 即可在普通硬件上运行，为开发者和企业提供了经济高效的私有化 AI 部署方案。其 OpenAI 兼容 API 和丰富的多模态支持让用户可以轻松迁移现有应用，同时保障数据隐私安全。

**技术亮点**:
- 多模态模型支持：支持文本生成 (Llama, Mamba)、图像生成 (Stable Diffusion)、音频/音乐生成 (MusicGen)、语音合成 (TTS) 和目标检测等多种 AI 任务
- 零硬件依赖：可在任何硬件上运行，无需昂贵的 GPU，通过优化的 CPU 推理实现高效部署
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，开发者无需修改代码即可无缝迁移现有应用
- 去中心化架构：基于 libp2p 实现分布式部署，支持构建去中心化的 AI 推理网络
- Go 语言高性能：采用 Go 编写，具备优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业（如医疗、金融）可本地运行 AI 模型，数据不出域
- 个人开发者/小团队：无需购买 GPU，通过普通服务器或个人电脑即可部署和实验各种 AI 模型



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 434,834 |
| 语言 | Python |
| Forks | 47,639 |
| Issues | 1,322 |
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
| Stars | 98,167 |
| 语言 | Python |
| Forks | 9,280 |
| Issues | 197 |
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
| Stars | 87,469 |
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
| Stars | 100,096 |
| 语言 | TypeScript |
| Forks | 27,210 |
| Issues | 1,136 |
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
| Stars | 79,175 |
| 语言 | TypeScript |
| Forks | 5,869 |
| Issues | 719 |
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
| Stars | 69,017 |
| 语言 | JavaScript |
| Forks | 23,307 |
| Issues | 212 |
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
| Stars | 55,951 |
| 语言 | JavaScript |
| Forks | 10,199 |
| Issues | 372 |
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
| Stars | 88,495 |
| 语言 | Go |
| Forks | 8,608 |
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
| Stars | 72,401 |
| 语言 | Go |
| Forks | 4,732 |
| Issues | 243 |
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
| Stars | 58,308 |
| 语言 | Go |
| Forks | 3,372 |
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
| Stars | 102,285 |
| 语言 | TypeScript |
| Forks | 12,374 |
| Issues | 1,015 |
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
| Stars | 59,994 |
| 语言 | JavaScript |
| Forks | 6,485 |
| Issues | 361 |
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
| Stars | 44,274 |
| 语言 | Go |
| Forks | 3,999 |
| Issues | 893 |
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
| Stars | 51,699 |
| 语言 | Go |
| Forks | 10,350 |
| Issues | 238 |
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
| Stars | 59,584 |
| 语言 | JavaScript |
| Forks | 3,295 |
| Issues | 194 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

一个将" caveman 说话风格"工程化为实用 token 优化工具的项目，通过幽默的 prompt 设计实现了 65% 的 token 消耗削减，对于需要在成本敏感场景下使用 Claude 的开发者具有极高的实用价值。

**技术亮点**:
- 基于 Anthropic Claude Code 的 Skill 插件架构，便于集成到 AI 辅助开发工作流中
- 通过独特的 caveman 语言风格 prompt 设计显著压缩 token 使用量
- 采用 JavaScript 实现，兼容 Node.js 生态，便于二次开发和扩展
- 项目包含完整的 prompt 工程最佳实践，可作为学习示例
- 支持自定义 caveman 说话风格参数，可灵活调整压缩效果

**适用场景**:
- AI 开发成本优化：在 API 调用费用敏感的项目中，使用 caveman 风格降低 token 消耗
- 学习 prompt 工程：通过该项目学习如何通过创意 prompt 设计实现高效 AI 交互
- Claude Code 工作流增强：为 Claude Code 添加 token 优化能力，提升开发效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,184 |
| 语言 | HTML |
| Forks | 21,112 |
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
| Stars | 60,232 |
| 语言 | TypeScript |
| Forks | 9,852 |
| Issues | 123 |
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
| Stars | 48,994 |
| 语言 | Python |
| Forks | 5,896 |
| Issues | 119 |
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
| Stars | 89,902 |
| 语言 | TypeScript |
| Forks | 10,055 |
| Issues | 2,264 |
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
| Stars | 88,020 |
| 语言 | TypeScript |
| Forks | 8,970 |
| Issues | 1,663 |
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
| Stars | 127,789 |
| 语言 | JavaScript |
| Forks | 12,485 |
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
| Stars | 172,560 |
| 语言 | Go |
| Forks | 13,207 |
| Issues | 184 |
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
| Stars | 137,322 |
| 语言 | Unknown |
| Forks | 34,219 |
| Issues | 141 |
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
| Stars | 78,719 |
| 语言 | Shell |
| Forks | 6,779 |
| Issues | 26 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,224 |
| 语言 | Python |
| Forks | 8,555 |
| Issues | 406 |
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
| Stars | 92,965 |
| 语言 | Python |
| Forks | 13,541 |
| Issues | 130 |
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
| Stars | 388,216 |
| 语言 | Python |
| Forks | 66,296 |
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
| Stars | 117,873 |
| 语言 | TypeScript |
| Forks | 8,591 |
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
| Stars | 116,192 |
| 语言 | TypeScript |
| Forks | 6,128 |
| Issues | 17 |
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
| Stars | 95,634 |
| 语言 | TypeScript |
| Forks | 14,211 |
| Issues | 480 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,961 |
| 语言 | JavaScript |
| Forks | 5,256 |
| Issues | 53 |
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
| Stars | 48,392 |
| 语言 | Go |
| Forks | 10,347 |
| Issues | 1,896 |
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
| Stars | 109,944 |
| 语言 | C++ |
| Forks | 18,155 |
| Issues | 1,608 |
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
| Stars | 63,306 |
| 语言 | Python |
| Forks | 1,662 |
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
| Stars | 38,165 |
| 语言 | TypeScript |
| Forks | 4,364 |
| Issues | 282 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 297,466 |
| 语言 | Python |
| Forks | 27,891 |
| Issues | 16 |
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
| Stars | 87,043 |
| 语言 | Python |
| Forks | 37,472 |
| Issues | 3,915 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,635 |
| 语言 | TypeScript |
| Forks | 44,547 |
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
| Stars | 354,721 |
| 语言 | TypeScript |
| Forks | 44,067 |
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
| Stars | 123,131 |
| 语言 | TypeScript |
| Forks | 13,627 |
| Issues | 3,044 |
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
| Stars | 114,261 |
| 语言 | TypeScript |
| Forks | 8,793 |
| Issues | 1,880 |
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
| Stars | 108,838 |
| 语言 | TypeScript |
| Forks | 13,394 |
| Issues | 5,034 |
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
| Stars | 100,472 |
| 语言 | TypeScript |
| Forks | 5,585 |
| Issues | 664 |
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
| Stars | 98,021 |
| 语言 | TypeScript |
| Forks | 54,613 |
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
| Stars | 94,987 |
| 语言 | TypeScript |
| Forks | 5,237 |
| Issues | 89 |
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
| Stars | 85,591 |
| 语言 | TypeScript |
| Forks | 10,674 |
| Issues | 442 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,433 |
| 语言 | TypeScript |
| Forks | 7,609 |
| Issues | 36 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,580 |
| 语言 | TypeScript |
| Forks | 8,170 |
| Issues | 745 |
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
| Stars | 244,991 |
| 语言 | JavaScript |
| Forks | 51,030 |
| Issues | 1,298 |
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
| Stars | 117,182 |
| 语言 | JavaScript |
| Forks | 35,526 |
| Issues | 2,675 |
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
| Stars | 112,462 |
| 语言 | JavaScript |
| Forks | 36,373 |
| Issues | 481 |
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
| Stars | 109,056 |
| 语言 | JavaScript |
| Forks | 11,686 |
| Issues | 149 |
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
| Stars | 98,327 |
| 语言 | JavaScript |
| Forks | 32,645 |
| Issues | 1,542 |
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
| Stars | 95,749 |
| 语言 | JavaScript |
| Forks | 15,478 |
| Issues | 60 |
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
| Stars | 86,553 |
| 语言 | JavaScript |
| Forks | 4,912 |
| Issues | 1,004 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,406 |
| 语言 | JavaScript |
| Forks | 9,189 |
| Issues | 4 |
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
| Stars | 65,767 |
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
| Stars | 64,650 |
| 语言 | JavaScript |
| Forks | 4,102 |
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
| Stars | 61,229 |
| 语言 | JavaScript |
| Forks | 7,165 |
| Issues | 142 |
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
| Stars | 61,076 |
| 语言 | JavaScript |
| Forks | 5,673 |
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
| Stars | 59,843 |
| 语言 | JavaScript |
| Forks | 20,438 |
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
| Stars | 53,308 |
| 语言 | JavaScript |
| Forks | 10,616 |
| Issues | 448 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,792 |
| 语言 | JavaScript |
| Forks | 11,547 |
| Issues | 271 |
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
| Stars | 133,871 |
| 语言 | Go |
| Forks | 19,002 |
| Issues | 10,129 |
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
| Stars | 106,508 |
| 语言 | Go |
| Forks | 15,047 |
| Issues | 42 |
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
| Stars | 88,037 |
| 语言 | Go |
| Forks | 8,267 |
| Issues | 230 |
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
| Stars | 83,975 |
| 语言 | Go |
| Forks | 5,178 |
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
| Stars | 68,574 |
| 语言 | Go |
| Forks | 3,234 |
| Issues | 44 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,169 |
| 语言 | Go |
| Forks | 5,086 |
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
| Stars | 51,038 |
| 语言 | Go |
| Forks | 21,911 |
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
| Stars | 49,462 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 575 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### multica-ai/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 128,255 |
| 语言 | Unknown |
| Forks | 13,009 |
| Issues | 89 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 221,014 |
| 语言 | Python |
| Forks | 50,625 |
| Issues | 972 |
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
| Stars | 99,435 |
| 语言 | Python |
| Forks | 12,183 |
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
| Stars | 86,801 |
| 语言 | Python |
| Forks | 7,286 |
| Issues | 492 |
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
| Stars | 77,683 |
| 语言 | Python |
| Forks | 16,955 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,125 |
| 语言 | JavaScript |
| Forks | 26,684 |
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
| Stars | 71,203 |
| 语言 | JavaScript |
| Forks | 16,803 |
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
| Stars | 68,088 |
| 语言 | JavaScript |
| Forks | 4,574 |
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
| Stars | 67,413 |
| 语言 | JavaScript |
| Forks | 11,952 |
| Issues | 563 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,434 |
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
| Stars | 51,026 |
| 语言 | Go |
| Forks | 1,612 |
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
| Stars | 46,852 |
| 语言 | Go |
| Forks | 8,856 |
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
| Stars | 46,345 |
| 语言 | Go |
| Forks | 3,820 |
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
| Stars | 156,636 |
| 语言 | Python |
| Forks | 11,946 |
| Issues | 364 |
| Topics | awesome, github, hellogithub, python |
