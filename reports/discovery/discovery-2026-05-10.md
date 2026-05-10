# 项目发现报告 (2026-05-10)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 123 |
| 去重移除 | 34 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 20 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
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
| Stars | 142,240 |
| 语言 | Python |
| Forks | 22,159 |
| Issues | 9,815 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个功能全面的开源 AI Agent 框架，拥有超过 14 万颗 Stars，支持 OpenAI、Anthropic Claude 等多种主流 LLM，提供 MCP 协议集成和结构化工具调用能力，适合构建生产级智能助手和自动化工作流。

**技术亮点**:
- 多 LLM 提供商支持：同时集成 OpenAI GPT 系列、Anthropic Claude 等多个大语言模型 API，灵活切换和对比不同模型能力
- MCP (Model Context Protocol) 协议支持：遵循 Anthropic 提出的 MCP 标准协议，实现标准化的 Agent 与外部工具/数据源连接
- 结构化工具调用 (Structured Tool Calling)：支持定义复杂工具 schema，实现 Agent 对外部工具的可靠调用和参数验证
- 会话状态管理：内置多轮对话上下文管理能力，支持 Agent 在长对话中保持状态和记忆
- MIT 许可证开源：完全开源可商用，社区活跃度高，提供完善的文档和示例

**适用场景**:
- 企业智能助手：构建客服机器人、知识问答系统、文档处理自动化等企业级 AI 应用
- 开发者工作流自动化：集成到开发流程中，实现代码审查、自动化测试、CI/CD 流程辅助等开发效率提升场景
- 个人生产力工具：作为个人 AI 助理，处理日程管理、邮件撰写、信息检索等日常任务



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,462 |
| 语言 | Python |
| Forks | 19,433 |
| Issues | 214 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 提供商，提供 RAG 和 MCP 支持，允许用户完全自托管，适合需要私有化部署 AI 能力的个人开发者和企业。

**技术亮点**:
- 支持多种 LLM 提供商：Ollama、OpenAI API、兼容 OpenAPI 的接口
- 内置 RAG（检索增强生成）功能，支持知识库增强问答
- 支持 MCP（Model Context Protocol），可扩展工具和能力
- 采用 Python 开发，支持 Docker 部署，自托管友好
- 开源可定制，许可证灵活（Other），适合企业二次开发

**适用场景**:
- 企业内部 AI 助手：需要私有化部署、保护数据隐私的企业场景
- 个人开发者本地开发：利用 Ollama 本地运行 LLM，配合 WebUI 提升开发体验
- RAG 应用构建：基于自有文档构建知识库问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,176 |
| 语言 | Python |
| Forks | 9,134 |
| Issues | 3,008 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，拥有 8 万+ Stars，将深度文档理解与 Agent 能力深度融合，为 LLM 提供精准的上下文检索，特别适合构建企业级知识库问答和智能文档处理应用。

**技术亮点**:
- 深度文档理解：支持 PDF、Word、PPT 等多格式智能解析，提取结构化信息
- Agent 驱动检索：融合 Agent 能力实现语义理解、意图识别和动态检索策略
- 可配置工作流：提供可视化 Agent 配置，支持复杂对话场景定制
- 多向量数据库支持：兼容多种向量存储后端，支持混合检索
- 完整的 RAG Pipeline：从文档解析、embedding、检索到生成的端到端解决方案

**适用场景**:
- 企业级知识库问答系统：构建智能客服、技术文档问答、内部知识检索等场景
- 智能文档处理与分析：实现合同审查、报告摘要、简历筛选等自动化文档处理
- LLM 应用开发框架：为个人开发者提供快速构建 RAG 应用的 Python SDK 和完整 API



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 177,926 |
| 语言 | JavaScript |
| Forks | 27,485 |
| Issues | 176 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是针对 Claude Code、Codex、Cursor 等主流 AI 编程助手的性能优化系统，通过 Skills/Instincts/Memory 等创新机制提升 AI 代理效率，17 万+ stars 证明其极高的人气和技术价值

**技术亮点**:
- 多 AI 代理兼容框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- Skills 与 Instincts 机制：创新的技能系统和本能响应模式，增强 AI 任务处理能力
- Memory 持久化系统：支持跨会话上下文保持和知识积累
- MCP 协议支持：遵循 Model Context Protocol 实现标准化交互
- Security 安全防护体系：确保 AI 代码生成的安全性和可靠性

**适用场景**:
- 企业级 AI 开发平台：为开发团队提供标准化的 AI 辅助编码优化方案，支持知识沉淀和团队协作
- 个人开发者提效：帮助独立开发者通过 Skills 配置和 Memory 功能构建个性化的 AI 开发工作流
- AI 代理开发研究：作为 research-first 框架，用于研究和实验新型 AI 编程助手的优化策略



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,177 |
| 语言 | Go |
| Forks | 4,070 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 降低了 AI 部署门槛，无需 GPU 即可在普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，为隐私敏感场景和边缘计算提供了灵活的本地化解决方案。

**技术亮点**:
- 多模态模型支持：统一支持文本生成(LLM/Mamba)、图像生成(Stable Diffusion)、音频合成(MusicGen)、语音识别(TTS)等多种 AI 任务
- 无 GPU 依赖架构：采用 CPU 友好设计，支持在普通硬件上运行，大幅降低 AI 部署硬件门槛
- Go 语言高性能：利用 Go 语言的并发特性和高效性能，确保 API 响应延迟低
- 分布式与去中心化：集成 libp2p 支持分布式部署，可构建去中心化的 AI 推理网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用无缝迁移

**适用场景**:
- 隐私敏感型应用：数据无法上云的医疗、法律、金融等领域，需要在本地处理敏感信息
- 边缘计算与物联网：在边缘设备上部署 AI 能力，如智能摄像头、机器人、工业控制器等
- 中小企业 AI 快速落地：预算有限但需要 AI 能力的团队，可快速搭建本地化 AI 服务原型



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,801 |
| 语言 | TypeScript |
| Forks | 15,143 |
| Issues | 783 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，通过 MCP 协议实现标准化的多 agent 编排，为开发者和企业提供了开箱即用的 agent 团队构建方案，降低了多 agent 系统开发门槛。

**技术亮点**:
- 支持多种主流 AI 模型集成：OpenAI GPT、Claude、Gemini、DeepSeek 等，提供统一的多模型调用接口
- 完整实现 MCP (Model Context Protocol) 协议，支持标准化的 AI 模型上下文交互和工具调用
- 多 agent 协作框架：支持 agent 团队设计、任务编排和协作执行，实现复杂的 AI 工作流
- TypeScript 全栈架构：类型安全的开发体验，前后端一致的代码规范
- 内置知识库管理功能，支持 RAG（检索增强生成）场景

**适用场景**:
- 企业 AI 应用开发：构建智能客服、工作流自动化、知识管理系统等多 agent 应用
- 开发者快速原型验证：利用现成的 agent 框架和模型集成快速搭建 AI 原型
- 个人效率工具：构建个人 AI 助手团队，处理复杂的多步骤任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,430 |
| 语言 | TypeScript |
| Forks | 6,387 |
| Issues | 38 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

这是一个具有 74k+ Stars 的热门 AI 记忆系统项目，能够为各种 AI 代理（如 Claude Code、Copilot、Gemini 等）提供跨会话的持久化上下文，大幅提升代理在复杂任务中的连贯性和效率。采用 AI 压缩技术智能管理记忆，既解决了上下文窗口限制，又保留了关键信息。

**技术亮点**:
- 采用 AI 驱动的智能压缩技术，自动提炼和总结会话内容，有效降低上下文窗口负担
- 基于 ChromaDB 和嵌入技术实现语义搜索，能精准检索历史相关上下文
- 使用 SQLite 作为轻量级本地存储，无需复杂基础设施部署即可使用
- 支持 RAG（检索增强生成）架构，将历史记忆无缝注入到新的推理过程中
- 广泛的代理兼容性：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI 代理平台

**适用场景**:
- 复杂的多步骤开发任务：如需要跨多个会话完成的大型代码重构或功能开发项目，代理可以记住之前的进度和决策
- 个人开发者的代码助手：作为长期使用的编程助手，能记住开发者的代码风格、项目架构和偏好设置，提供更个性化的辅助
- 企业级 AI 工作流：团队成员可以共享 AI 代理的工作记忆，确保任务交接的连续性和上下文一致性
- 自动化测试和调试场景：AI 代理能够记住之前发现的 bug 模式和相关代码历史，提高调试效率



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,111 |
| 语言 | Python |
| Forks | 8,691 |
| Issues | 1,002 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个高度集成化的 LLM 微调框架，支持 100+ 主流大语言模型和视觉语言模型，通过统一的接口封装了 LoRA、QLoRA、RLHF 等多种高效微调技术，显著降低了微调大模型的门槛和成本，适合企业级模型定制和个人开发者快速实验。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，包括 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等主流模型
- 高效微调技术：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低 GPU 显存占用
- 多种训练范式：支持监督微调 (SFT)、人类反馈强化学习 (RLHF)、直接偏好优化 (DPO) 等
- 量化与压缩：支持多种量化方法，便于将大模型部署到资源受限环境
- 分布式训练支持：支持多卡并行训练，提升大规模模型训练效率

**适用场景**:
- 企业 AI 定制化：企业利用私有数据微调开源大模型，打造专属领域应用（如客服、文档分析、代码生成等）
- 学术研究与实验：研究人员快速验证不同微调策略、模型架构和训练方法的效果，加速论文实验
- 个人开发者/小团队：低门槛微调开源模型，降低 AI 应用开发成本，适合创业项目或原型验证
- 边缘部署场景：通过量化技术将大模型压缩后部署到边缘设备或低配服务器



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,085 |
| 语言 | Python |
| Forks | 14,225 |
| Issues | 401 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,134 |
| 语言 | HTML |
| Forks | 5,195 |
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
| Stars | 46,390 |
| 语言 | Python |
| Forks | 5,590 |
| Issues | 112 |
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
| Stars | 46,159 |
| 语言 | Java |
| Forks | 15,975 |
| Issues | 21 |
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
| Stars | 39,142 |
| 语言 | Python |
| Forks | 6,199 |
| Issues | 82 |
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
| Stars | 48,398 |
| 语言 | TypeScript |
| Forks | 5,362 |
| Issues | 527 |
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
| Stars | 117,865 |
| 语言 | TypeScript |
| Forks | 7,333 |
| Issues | 312 |
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
| Stars | 59,819 |
| 语言 | JavaScript |
| Forks | 6,465 |
| Issues | 355 |
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
| Stars | 73,062 |
| 语言 | Python |
| Forks | 9,249 |
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
| Stars | 56,973 |
| 语言 | TypeScript |
| Forks | 4,640 |
| Issues | 711 |
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
| Stars | 109,589 |
| 语言 | Python |
| Forks | 16,213 |
| Issues | 8 |
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
| Stars | 93,233 |
| 语言 | Python |
| Forks | 10,555 |
| Issues | 232 |
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
| Stars | 52,702 |
| 语言 | TypeScript |
| Forks | 24,308 |
| Issues | 838 |
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
| Stars | 187,345 |
| 语言 | TypeScript |
| Forks | 57,517 |
| Issues | 1,485 |
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
| Stars | 155,539 |
| 语言 | Java |
| Forks | 46,140 |
| Issues | 64 |
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
| Stars | 147,926 |
| 语言 | Python |
| Forks | 8,944 |
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
| Stars | 61,108 |
| 语言 | Jupyter Notebook |
| Forks | 20,681 |
| Issues | 6 |
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
| Stars | 59,065 |
| 语言 | Python |
| Forks | 6,402 |
| Issues | 593 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 59,529 |
| 语言 | TypeScript |
| Forks | 9,769 |
| Issues | 118 |
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
| Stars | 65,895 |
| 语言 | Rust |
| Forks | 4,242 |
| Issues | 802 |
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
| Stars | 136,462 |
| 语言 | Python |
| Forks | 19,433 |
| Issues | 214 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 提供商，提供 RAG 和 MCP 支持，允许用户完全自托管，适合需要私有化部署 AI 能力的个人开发者和企业。

**技术亮点**:
- 支持多种 LLM 提供商：Ollama、OpenAI API、兼容 OpenAPI 的接口
- 内置 RAG（检索增强生成）功能，支持知识库增强问答
- 支持 MCP（Model Context Protocol），可扩展工具和能力
- 采用 Python 开发，支持 Docker 部署，自托管友好
- 开源可定制，许可证灵活（Other），适合企业二次开发

**适用场景**:
- 企业内部 AI 助手：需要私有化部署、保护数据隐私的企业场景
- 个人开发者本地开发：利用 Ollama 本地运行 LLM，配合 WebUI 提升开发体验
- RAG 应用构建：基于自有文档构建知识库问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,176 |
| 语言 | Python |
| Forks | 9,134 |
| Issues | 3,008 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一，拥有 8 万+ Stars，将深度文档理解与 Agent 能力深度融合，为 LLM 提供精准的上下文检索，特别适合构建企业级知识库问答和智能文档处理应用。

**技术亮点**:
- 深度文档理解：支持 PDF、Word、PPT 等多格式智能解析，提取结构化信息
- Agent 驱动检索：融合 Agent 能力实现语义理解、意图识别和动态检索策略
- 可配置工作流：提供可视化 Agent 配置，支持复杂对话场景定制
- 多向量数据库支持：兼容多种向量存储后端，支持混合检索
- 完整的 RAG Pipeline：从文档解析、embedding、检索到生成的端到端解决方案

**适用场景**:
- 企业级知识库问答系统：构建智能客服、技术文档问答、内部知识检索等场景
- 智能文档处理与分析：实现合同审查、报告摘要、简历筛选等自动化文档处理
- LLM 应用开发框架：为个人开发者提供快速构建 RAG 应用的 Python SDK 和完整 API



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,801 |
| 语言 | TypeScript |
| Forks | 15,143 |
| Issues | 783 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，通过 MCP 协议实现标准化的多 agent 编排，为开发者和企业提供了开箱即用的 agent 团队构建方案，降低了多 agent 系统开发门槛。

**技术亮点**:
- 支持多种主流 AI 模型集成：OpenAI GPT、Claude、Gemini、DeepSeek 等，提供统一的多模型调用接口
- 完整实现 MCP (Model Context Protocol) 协议，支持标准化的 AI 模型上下文交互和工具调用
- 多 agent 协作框架：支持 agent 团队设计、任务编排和协作执行，实现复杂的 AI 工作流
- TypeScript 全栈架构：类型安全的开发体验，前后端一致的代码规范
- 内置知识库管理功能，支持 RAG（检索增强生成）场景

**适用场景**:
- 企业 AI 应用开发：构建智能客服、工作流自动化、知识管理系统等多 agent 应用
- 开发者快速原型验证：利用现成的 agent 框架和模型集成快速搭建 AI 原型
- 个人效率工具：构建个人 AI 助手团队，处理复杂的多步骤任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,430 |
| 语言 | TypeScript |
| Forks | 6,387 |
| Issues | 38 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

这是一个具有 74k+ Stars 的热门 AI 记忆系统项目，能够为各种 AI 代理（如 Claude Code、Copilot、Gemini 等）提供跨会话的持久化上下文，大幅提升代理在复杂任务中的连贯性和效率。采用 AI 压缩技术智能管理记忆，既解决了上下文窗口限制，又保留了关键信息。

**技术亮点**:
- 采用 AI 驱动的智能压缩技术，自动提炼和总结会话内容，有效降低上下文窗口负担
- 基于 ChromaDB 和嵌入技术实现语义搜索，能精准检索历史相关上下文
- 使用 SQLite 作为轻量级本地存储，无需复杂基础设施部署即可使用
- 支持 RAG（检索增强生成）架构，将历史记忆无缝注入到新的推理过程中
- 广泛的代理兼容性：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI 代理平台

**适用场景**:
- 复杂的多步骤开发任务：如需要跨多个会话完成的大型代码重构或功能开发项目，代理可以记住之前的进度和决策
- 个人开发者的代码助手：作为长期使用的编程助手，能记住开发者的代码风格、项目架构和偏好设置，提供更个性化的辅助
- 企业级 AI 工作流：团队成员可以共享 AI 代理的工作记忆，确保任务交接的连续性和上下文一致性
- 自动化测试和调试场景：AI 代理能够记住之前发现的 bug 模式和相关代码历史，提高调试效率



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,390 |
| 语言 | Python |
| Forks | 5,590 |
| Issues | 112 |
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
| Stars | 46,159 |
| 语言 | Java |
| Forks | 15,975 |
| Issues | 21 |
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
| Stars | 39,142 |
| 语言 | Python |
| Forks | 6,199 |
| Issues | 82 |
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
| Stars | 102,124 |
| 语言 | TypeScript |
| Forks | 12,348 |
| Issues | 1,010 |
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
| Stars | 59,819 |
| 语言 | JavaScript |
| Forks | 6,465 |
| Issues | 355 |
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
| Stars | 109,589 |
| 语言 | Python |
| Forks | 16,213 |
| Issues | 8 |
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
| Stars | 77,550 |
| 语言 | Python |
| Forks | 10,404 |
| Issues | 192 |
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
| Stars | 52,702 |
| 语言 | TypeScript |
| Forks | 24,308 |
| Issues | 838 |
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
| Stars | 46,022 |
| 语言 | Python |
| Forks | 4,995 |
| Issues | 241 |
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
| Stars | 44,218 |
| 语言 | Go |
| Forks | 3,995 |
| Issues | 875 |
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
| Stars | 35,000 |
| 语言 | Python |
| Forks | 4,960 |
| Issues | 233 |
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
| Stars | 142,240 |
| 语言 | Python |
| Forks | 22,159 |
| Issues | 9,815 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个功能全面的开源 AI Agent 框架，拥有超过 14 万颗 Stars，支持 OpenAI、Anthropic Claude 等多种主流 LLM，提供 MCP 协议集成和结构化工具调用能力，适合构建生产级智能助手和自动化工作流。

**技术亮点**:
- 多 LLM 提供商支持：同时集成 OpenAI GPT 系列、Anthropic Claude 等多个大语言模型 API，灵活切换和对比不同模型能力
- MCP (Model Context Protocol) 协议支持：遵循 Anthropic 提出的 MCP 标准协议，实现标准化的 Agent 与外部工具/数据源连接
- 结构化工具调用 (Structured Tool Calling)：支持定义复杂工具 schema，实现 Agent 对外部工具的可靠调用和参数验证
- 会话状态管理：内置多轮对话上下文管理能力，支持 Agent 在长对话中保持状态和记忆
- MIT 许可证开源：完全开源可商用，社区活跃度高，提供完善的文档和示例

**适用场景**:
- 企业智能助手：构建客服机器人、知识问答系统、文档处理自动化等企业级 AI 应用
- 开发者工作流自动化：集成到开发流程中，实现代码审查、自动化测试、CI/CD 流程辅助等开发效率提升场景
- 个人生产力工具：作为个人 AI 助理，处理日程管理、邮件撰写、信息检索等日常任务



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,462 |
| 语言 | Python |
| Forks | 19,433 |
| Issues | 214 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 提供商，提供 RAG 和 MCP 支持，允许用户完全自托管，适合需要私有化部署 AI 能力的个人开发者和企业。

**技术亮点**:
- 支持多种 LLM 提供商：Ollama、OpenAI API、兼容 OpenAPI 的接口
- 内置 RAG（检索增强生成）功能，支持知识库增强问答
- 支持 MCP（Model Context Protocol），可扩展工具和能力
- 采用 Python 开发，支持 Docker 部署，自托管友好
- 开源可定制，许可证灵活（Other），适合企业二次开发

**适用场景**:
- 企业内部 AI 助手：需要私有化部署、保护数据隐私的企业场景
- 个人开发者本地开发：利用 Ollama 本地运行 LLM，配合 WebUI 提升开发体验
- RAG 应用构建：基于自有文档构建知识库问答系统



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 177,926 |
| 语言 | JavaScript |
| Forks | 27,485 |
| Issues | 176 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是针对 Claude Code、Codex、Cursor 等主流 AI 编程助手的性能优化系统，通过 Skills/Instincts/Memory 等创新机制提升 AI 代理效率，17 万+ stars 证明其极高的人气和技术价值

**技术亮点**:
- 多 AI 代理兼容框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- Skills 与 Instincts 机制：创新的技能系统和本能响应模式，增强 AI 任务处理能力
- Memory 持久化系统：支持跨会话上下文保持和知识积累
- MCP 协议支持：遵循 Model Context Protocol 实现标准化交互
- Security 安全防护体系：确保 AI 代码生成的安全性和可靠性

**适用场景**:
- 企业级 AI 开发平台：为开发团队提供标准化的 AI 辅助编码优化方案，支持知识沉淀和团队协作
- 个人开发者提效：帮助独立开发者通过 Skills 配置和 Memory 功能构建个性化的 AI 开发工作流
- AI 代理开发研究：作为 research-first 框架，用于研究和实验新型 AI 编程助手的优化策略



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,421 |
| 语言 | JavaScript |
| Forks | 3,152 |
| Issues | 202 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个将幽默创意与实用价值完美结合的项目，通过"穴居人语言"风格将复杂提示词压缩 65%，在节省 Token 成本的同时保持输出质量，非常适合高频调用 LLM API 的开发者和企业。

**技术亮点**:
- 通过极度精简的 prompt 风格实现 Token 用量大幅削减，官方宣称可节省 65% 的 Token 消耗
- 基于 Claude Code 生态的官方 Skill 扩展，集成方式简单，零门槛使用
- 巧妙利用 LLM 对简洁指令的理解能力，用幽默的 caveman speak 风格降低 Prompt 复杂度
- MIT 开源许可，项目代码可自由使用、修改和商业集成
- 项目热度极高（57k+ Stars），经过大规模社区验证和实战检验

**适用场景**:
- 需要频繁调用 Claude API 进行代码生成、代码审查或重构的个人开发者或小型团队
- 对 API 调用成本敏感、需要在预算有限的情况下维持高质量 LLM 服务的企业级应用
- Prompt 工程学习者希望通过实际案例理解如何撰写高效、精简的指令以优化 LLM 输出



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,801 |
| 语言 | TypeScript |
| Forks | 15,143 |
| Issues | 783 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个开源的多 agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流 AI 模型，通过 MCP 协议实现标准化的多 agent 编排，为开发者和企业提供了开箱即用的 agent 团队构建方案，降低了多 agent 系统开发门槛。

**技术亮点**:
- 支持多种主流 AI 模型集成：OpenAI GPT、Claude、Gemini、DeepSeek 等，提供统一的多模型调用接口
- 完整实现 MCP (Model Context Protocol) 协议，支持标准化的 AI 模型上下文交互和工具调用
- 多 agent 协作框架：支持 agent 团队设计、任务编排和协作执行，实现复杂的 AI 工作流
- TypeScript 全栈架构：类型安全的开发体验，前后端一致的代码规范
- 内置知识库管理功能，支持 RAG（检索增强生成）场景

**适用场景**:
- 企业 AI 应用开发：构建智能客服、工作流自动化、知识管理系统等多 agent 应用
- 开发者快速原型验证：利用现成的 agent 框架和模型集成快速搭建 AI 原型
- 个人效率工具：构建个人 AI 助手团队，处理复杂的多步骤任务



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,430 |
| 语言 | TypeScript |
| Forks | 6,387 |
| Issues | 38 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

这是一个具有 74k+ Stars 的热门 AI 记忆系统项目，能够为各种 AI 代理（如 Claude Code、Copilot、Gemini 等）提供跨会话的持久化上下文，大幅提升代理在复杂任务中的连贯性和效率。采用 AI 压缩技术智能管理记忆，既解决了上下文窗口限制，又保留了关键信息。

**技术亮点**:
- 采用 AI 驱动的智能压缩技术，自动提炼和总结会话内容，有效降低上下文窗口负担
- 基于 ChromaDB 和嵌入技术实现语义搜索，能精准检索历史相关上下文
- 使用 SQLite 作为轻量级本地存储，无需复杂基础设施部署即可使用
- 支持 RAG（检索增强生成）架构，将历史记忆无缝注入到新的推理过程中
- 广泛的代理兼容性：支持 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流 AI 代理平台

**适用场景**:
- 复杂的多步骤开发任务：如需要跨多个会话完成的大型代码重构或功能开发项目，代理可以记住之前的进度和决策
- 个人开发者的代码助手：作为长期使用的编程助手，能记住开发者的代码风格、项目架构和偏好设置，提供更个性化的辅助
- 企业级 AI 工作流：团队成员可以共享 AI 代理的工作记忆，确保任务交接的连续性和上下文一致性
- 自动化测试和调试场景：AI 代理能够记住之前发现的 bug 模式和相关代码历史，提高调试效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,962 |
| 语言 | HTML |
| Forks | 21,098 |
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
| Stars | 92,441 |
| 语言 | Jupyter Notebook |
| Forks | 14,277 |
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
| Stars | 52,134 |
| 语言 | HTML |
| Forks | 5,195 |
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
| Stars | 59,819 |
| 语言 | JavaScript |
| Forks | 6,465 |
| Issues | 355 |
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
| Stars | 73,062 |
| 语言 | Python |
| Forks | 9,249 |
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
| Stars | 56,973 |
| 语言 | TypeScript |
| Forks | 4,640 |
| Issues | 711 |
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
| Stars | 52,702 |
| 语言 | TypeScript |
| Forks | 24,308 |
| Issues | 838 |
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
| Stars | 79,564 |
| 语言 | Python |
| Forks | 16,627 |
| Issues | 4,882 |
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
| Stars | 147,926 |
| 语言 | Python |
| Forks | 8,944 |
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
| Stars | 59,065 |
| 语言 | Python |
| Forks | 6,402 |
| Issues | 593 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,140 |
| 语言 | Go |
| Forks | 16,056 |
| Issues | 3,227 |
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
| Stars | 59,529 |
| 语言 | TypeScript |
| Forks | 9,769 |
| Issues | 118 |
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
| Stars | 48,611 |
| 语言 | Rust |
| Forks | 9,763 |
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
| Stars | 122,401 |
| 语言 | Python |
| Forks | 8,248 |
| Issues | 635 |
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
| Stars | 71,111 |
| 语言 | Python |
| Forks | 8,691 |
| Issues | 1,002 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个高度集成化的 LLM 微调框架，支持 100+ 主流大语言模型和视觉语言模型，通过统一的接口封装了 LoRA、QLoRA、RLHF 等多种高效微调技术，显著降低了微调大模型的门槛和成本，适合企业级模型定制和个人开发者快速实验。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，包括 LLaMA、LLaMA3、Qwen、DeepSeek、Gemma 等主流模型
- 高效微调技术：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低 GPU 显存占用
- 多种训练范式：支持监督微调 (SFT)、人类反馈强化学习 (RLHF)、直接偏好优化 (DPO) 等
- 量化与压缩：支持多种量化方法，便于将大模型部署到资源受限环境
- 分布式训练支持：支持多卡并行训练，提升大规模模型训练效率

**适用场景**:
- 企业 AI 定制化：企业利用私有数据微调开源大模型，打造专属领域应用（如客服、文档分析、代码生成等）
- 学术研究与实验：研究人员快速验证不同微调策略、模型架构和训练方法的效果，加速论文实验
- 个人开发者/小团队：低门槛微调开源模型，降低 AI 应用开发成本，适合创业项目或原型验证
- 边缘部署场景：通过量化技术将大模型压缩后部署到边缘设备或低配服务器



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,344 |
| 语言 | Python |
| Forks | 6,755 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，拥有超过67K Stars的成熟社区支持，为分析师、量化交易员和AI代理提供了一站式的数据获取、分析和可视化解决方案，融合了机器学习技术，显著降低了金融数据分析的门槛。

**技术亮点**:
- 统一的数据API网关：整合多个数据源（股票、加密货币、期权等），提供标准化的数据访问接口
- AI/ML深度集成：内置机器学习模型支持金融预测、情绪分析和模式识别
- 模块化架构设计：采用插件式架构，便于扩展新数据源和分析功能
- 企业级数据管道：支持数据清洗、标准化和实时流处理
- 丰富的技术指标库：内置100+技术分析指标和量化交易工具

**适用场景**:
- 量化交易策略开发：用于策略回测、因子分析和算法交易研究
- 投资研究分析：支持基本面分析、技术分析和投资组合优化
- AI金融代理：作为AI Agent的数据层，提供实时金融信息查询和分析能力



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,962 |
| 语言 | HTML |
| Forks | 21,098 |
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
| Stars | 92,441 |
| 语言 | Jupyter Notebook |
| Forks | 14,277 |
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
| Stars | 160,440 |
| 语言 | Python |
| Forks | 33,155 |
| Issues | 2,364 |
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
| Stars | 79,564 |
| 语言 | Python |
| Forks | 16,627 |
| Issues | 4,882 |
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
| Stars | 112,268 |
| 语言 | Python |
| Forks | 13,115 |
| Issues | 3,990 |
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
| Stars | 99,793 |
| 语言 | Python |
| Forks | 27,739 |
| Issues | 18,500 |
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
| Stars | 177,926 |
| 语言 | JavaScript |
| Forks | 27,485 |
| Issues | 176 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是针对 Claude Code、Codex、Cursor 等主流 AI 编程助手的性能优化系统，通过 Skills/Instincts/Memory 等创新机制提升 AI 代理效率，17 万+ stars 证明其极高的人气和技术价值

**技术亮点**:
- 多 AI 代理兼容框架：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- Skills 与 Instincts 机制：创新的技能系统和本能响应模式，增强 AI 任务处理能力
- Memory 持久化系统：支持跨会话上下文保持和知识积累
- MCP 协议支持：遵循 Model Context Protocol 实现标准化交互
- Security 安全防护体系：确保 AI 代码生成的安全性和可靠性

**适用场景**:
- 企业级 AI 开发平台：为开发团队提供标准化的 AI 辅助编码优化方案，支持知识沉淀和团队协作
- 个人开发者提效：帮助独立开发者通过 Skills 配置和 Memory 功能构建个性化的 AI 开发工作流
- AI 代理开发研究：作为 research-first 框架，用于研究和实验新型 AI 编程助手的优化策略



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,177 |
| 语言 | Go |
| Forks | 4,070 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 降低了 AI 部署门槛，无需 GPU 即可在普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，为隐私敏感场景和边缘计算提供了灵活的本地化解决方案。

**技术亮点**:
- 多模态模型支持：统一支持文本生成(LLM/Mamba)、图像生成(Stable Diffusion)、音频合成(MusicGen)、语音识别(TTS)等多种 AI 任务
- 无 GPU 依赖架构：采用 CPU 友好设计，支持在普通硬件上运行，大幅降低 AI 部署硬件门槛
- Go 语言高性能：利用 Go 语言的并发特性和高效性能，确保 API 响应延迟低
- 分布式与去中心化：集成 libp2p 支持分布式部署，可构建去中心化的 AI 推理网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用无缝迁移

**适用场景**:
- 隐私敏感型应用：数据无法上云的医疗、法律、金融等领域，需要在本地处理敏感信息
- 边缘计算与物联网：在边缘设备上部署 AI 能力，如智能摄像头、机器人、工业控制器等
- 中小企业 AI 快速落地：预算有限但需要 AI 能力的团队，可快速搭建本地化 AI 服务原型



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,159 |
| 语言 | Java |
| Forks | 15,975 |
| Issues | 21 |
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
| Stars | 73,062 |
| 语言 | Python |
| Forks | 9,249 |
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
| Stars | 56,973 |
| 语言 | TypeScript |
| Forks | 4,640 |
| Issues | 711 |
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
| Stars | 187,345 |
| 语言 | TypeScript |
| Forks | 57,517 |
| Issues | 1,485 |
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
| Stars | 59,065 |
| 语言 | Python |
| Forks | 6,402 |
| Issues | 593 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 433,810 |
| 语言 | Python |
| Forks | 47,492 |
| Issues | 1,313 |
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
| Stars | 161,503 |
| 语言 | Python |
| Forks | 13,424 |
| Issues | 2,488 |
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
| Stars | 98,070 |
| 语言 | Python |
| Forks | 9,223 |
| Issues | 191 |
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
| Stars | 83,178 |
| 语言 | Python |
| Forks | 9,697 |
| Issues | 262 |
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
| Stars | 184,759 |
| 语言 | TypeScript |
| Forks | 39,739 |
| Issues | 17,415 |
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
| Stars | 94,290 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 305 |
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
| Stars | 79,146 |
| 语言 | TypeScript |
| Forks | 5,864 |
| Issues | 715 |
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
| Stars | 77,469 |
| 语言 | TypeScript |
| Forks | 6,658 |
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
| Stars | 80,123 |
| 语言 | Go |
| Forks | 2,804 |
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
| Stars | 77,722 |
| 语言 | Go |
| Forks | 2,822 |
| Issues | 957 |
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
| Stars | 56,973 |
| 语言 | TypeScript |
| Forks | 4,640 |
| Issues | 711 |
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
| Stars | 187,345 |
| 语言 | TypeScript |
| Forks | 57,517 |
| Issues | 1,485 |
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
| Stars | 59,065 |
| 语言 | Python |
| Forks | 6,402 |
| Issues | 593 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,678 |
| 语言 | Go |
| Forks | 10,341 |
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
| Stars | 122,171 |
| 语言 | Go |
| Forks | 43,017 |
| Issues | 2,667 |
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
| Stars | 71,537 |
| 语言 | Go |
| Forks | 18,933 |
| Issues | 3,815 |
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
| Stars | 55,543 |
| 语言 | Go |
| Forks | 6,678 |
| Issues | 2,776 |
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
| Stars | 94,290 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 305 |
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
| Stars | 78,500 |
| 语言 | TypeScript |
| Forks | 6,871 |
| Issues | 404 |
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
| Stars | 86,495 |
| 语言 | JavaScript |
| Forks | 7,810 |
| Issues | 736 |
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
| Stars | 63,095 |
| 语言 | Go |
| Forks | 5,973 |
| Issues | 803 |
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
| Stars | 59,473 |
| 语言 | Go |
| Forks | 4,333 |
| Issues | 26 |
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
| Stars | 47,504 |
| 语言 | Go |
| Forks | 5,056 |
| Issues | 989 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
| 许可证 | MIT License |


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,238 |
| 语言 | Go |
| Forks | 1,918 |
| Issues | 325 |
| Topics | ci, devops, github-actions, golang |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,901 |
| 语言 | Go |
| Forks | 7,482 |
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
| Stars | 86,495 |
| 语言 | JavaScript |
| Forks | 7,810 |
| Issues | 736 |
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
| Stars | 63,979 |
| 语言 | Go |
| Forks | 10,393 |
| Issues | 779 |
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
| Stars | 46,177 |
| 语言 | Go |
| Forks | 4,070 |
| Issues | 164 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 降低了 AI 部署门槛，无需 GPU 即可在普通硬件上运行 LLM、图像生成、语音合成等多模态 AI 模型，为隐私敏感场景和边缘计算提供了灵活的本地化解决方案。

**技术亮点**:
- 多模态模型支持：统一支持文本生成(LLM/Mamba)、图像生成(Stable Diffusion)、音频合成(MusicGen)、语音识别(TTS)等多种 AI 任务
- 无 GPU 依赖架构：采用 CPU 友好设计，支持在普通硬件上运行，大幅降低 AI 部署硬件门槛
- Go 语言高性能：利用 Go 语言的并发特性和高效性能，确保 API 响应延迟低
- 分布式与去中心化：集成 libp2p 支持分布式部署，可构建去中心化的 AI 推理网络
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，方便现有应用无缝迁移

**适用场景**:
- 隐私敏感型应用：数据无法上云的医疗、法律、金融等领域，需要在本地处理敏感信息
- 边缘计算与物联网：在边缘设备上部署 AI 能力，如智能摄像头、机器人、工业控制器等
- 中小企业 AI 快速落地：预算有限但需要 AI 能力的团队，可快速搭建本地化 AI 服务原型



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 433,810 |
| 语言 | Python |
| Forks | 47,492 |
| Issues | 1,313 |
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
| Stars | 98,070 |
| 语言 | Python |
| Forks | 9,223 |
| Issues | 191 |
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
| Stars | 87,456 |
| 语言 | Python |
| Forks | 33,849 |
| Issues | 432 |
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
| Stars | 100,069 |
| 语言 | TypeScript |
| Forks | 27,209 |
| Issues | 1,140 |
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
| Stars | 79,146 |
| 语言 | TypeScript |
| Forks | 5,864 |
| Issues | 715 |
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
| Stars | 69,008 |
| 语言 | JavaScript |
| Forks | 23,280 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,199 |
| Issues | 375 |
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
| Stars | 88,463 |
| 语言 | Go |
| Forks | 8,603 |
| Issues | 683 |
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
| Stars | 72,306 |
| 语言 | Go |
| Forks | 4,723 |
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
| Stars | 58,254 |
| 语言 | Go |
| Forks | 3,363 |
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
| Stars | 102,124 |
| 语言 | TypeScript |
| Forks | 12,348 |
| Issues | 1,010 |
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
| Stars | 59,819 |
| 语言 | JavaScript |
| Forks | 6,465 |
| Issues | 355 |
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
| Stars | 44,218 |
| 语言 | Go |
| Forks | 3,995 |
| Issues | 875 |
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
| Stars | 51,678 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 241 |
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
| Stars | 57,421 |
| 语言 | JavaScript |
| Forks | 3,152 |
| Issues | 202 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个将幽默创意与实用价值完美结合的项目，通过"穴居人语言"风格将复杂提示词压缩 65%，在节省 Token 成本的同时保持输出质量，非常适合高频调用 LLM API 的开发者和企业。

**技术亮点**:
- 通过极度精简的 prompt 风格实现 Token 用量大幅削减，官方宣称可节省 65% 的 Token 消耗
- 基于 Claude Code 生态的官方 Skill 扩展，集成方式简单，零门槛使用
- 巧妙利用 LLM 对简洁指令的理解能力，用幽默的 caveman speak 风格降低 Prompt 复杂度
- MIT 开源许可，项目代码可自由使用、修改和商业集成
- 项目热度极高（57k+ Stars），经过大规模社区验证和实战检验

**适用场景**:
- 需要频繁调用 Claude API 进行代码生成、代码审查或重构的个人开发者或小型团队
- 对 API 调用成本敏感、需要在预算有限的情况下维持高质量 LLM 服务的企业级应用
- Prompt 工程学习者希望通过实际案例理解如何撰写高效、精简的指令以优化 LLM 输出



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,962 |
| 语言 | HTML |
| Forks | 21,098 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,390 |
| 语言 | Python |
| Forks | 5,590 |
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
| Stars | 59,529 |
| 语言 | TypeScript |
| Forks | 9,769 |
| Issues | 118 |
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
| Stars | 89,877 |
| 语言 | TypeScript |
| Forks | 10,046 |
| Issues | 2,275 |
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
| Stars | 87,952 |
| 语言 | TypeScript |
| Forks | 8,956 |
| Issues | 1,671 |
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
| Stars | 172,281 |
| 语言 | Go |
| Forks | 13,200 |
| Issues | 181 |
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
| Stars | 127,750 |
| 语言 | JavaScript |
| Forks | 12,486 |
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
| Stars | 137,040 |
| 语言 | Unknown |
| Forks | 34,181 |
| Issues | 139 |
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
| Stars | 68,923 |
| 语言 | Shell |
| Forks | 5,947 |
| Issues | 23 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,112 |
| 语言 | Python |
| Forks | 8,266 |
| Issues | 414 |
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
| Stars | 92,859 |
| 语言 | Python |
| Forks | 13,517 |
| Issues | 126 |
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
| Stars | 388,000 |
| 语言 | Python |
| Forks | 66,278 |
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
| Stars | 117,089 |
| 语言 | TypeScript |
| Forks | 8,536 |
| Issues | 315 |
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
| Stars | 116,104 |
| 语言 | TypeScript |
| Forks | 6,112 |
| Issues | 21 |
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
| Stars | 92,895 |
| 语言 | TypeScript |
| Forks | 13,737 |
| Issues | 442 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,303 |
| 语言 | JavaScript |
| Forks | 5,207 |
| Issues | 62 |
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
| Stars | 48,368 |
| 语言 | Go |
| Forks | 10,346 |
| Issues | 1,902 |
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
| Stars | 109,389 |
| 语言 | C++ |
| Forks | 18,041 |
| Issues | 1,609 |
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
| Stars | 63,264 |
| 语言 | Python |
| Forks | 1,635 |
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
| Stars | 37,429 |
| 语言 | TypeScript |
| Forks | 4,271 |
| Issues | 353 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 296,933 |
| 语言 | Python |
| Forks | 27,855 |
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
| Stars | 220,913 |
| 语言 | Python |
| Forks | 50,584 |
| Issues | 962 |
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
| Stars | 86,993 |
| 语言 | Python |
| Forks | 37,436 |
| Issues | 3,931 |
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
| Stars | 77,660 |
| 语言 | Python |
| Forks | 45,095 |
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
| Stars | 444,448 |
| 语言 | TypeScript |
| Forks | 44,501 |
| Issues | 183 |
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
| Stars | 354,522 |
| 语言 | TypeScript |
| Forks | 44,049 |
| Issues | 8 |
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
| Stars | 122,882 |
| 语言 | TypeScript |
| Forks | 13,592 |
| Issues | 3,038 |
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
| Stars | 113,969 |
| 语言 | TypeScript |
| Forks | 8,757 |
| Issues | 1,859 |
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
| Stars | 108,802 |
| 语言 | TypeScript |
| Forks | 13,390 |
| Issues | 5,033 |
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
| Stars | 100,229 |
| 语言 | TypeScript |
| Forks | 5,571 |
| Issues | 670 |
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
| Stars | 97,985 |
| 语言 | TypeScript |
| Forks | 54,607 |
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
| Stars | 94,913 |
| 语言 | TypeScript |
| Forks | 5,226 |
| Issues | 90 |
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
| Stars | 83,413 |
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
| Stars | 80,506 |
| 语言 | TypeScript |
| Forks | 8,154 |
| Issues | 748 |
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
| Stars | 244,929 |
| 语言 | JavaScript |
| Forks | 51,015 |
| Issues | 1,293 |
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
| Stars | 117,133 |
| 语言 | JavaScript |
| Forks | 35,513 |
| Issues | 2,671 |
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
| Stars | 112,388 |
| 语言 | JavaScript |
| Forks | 36,367 |
| Issues | 487 |
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
| Forks | 11,675 |
| Issues | 149 |
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
| Stars | 99,834 |
| 语言 | JavaScript |
| Forks | 10,932 |
| Issues | 475 |
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
| Stars | 98,303 |
| 语言 | JavaScript |
| Forks | 32,642 |
| Issues | 1,557 |
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
| Stars | 95,744 |
| 语言 | JavaScript |
| Forks | 15,470 |
| Issues | 58 |
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
| Stars | 86,520 |
| 语言 | JavaScript |
| Forks | 4,906 |
| Issues | 999 |
| Topics | compiler, template, ui |
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
| Issues | 202 |
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
| Stars | 64,555 |
| 语言 | JavaScript |
| Forks | 4,096 |
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
| Stars | 61,222 |
| 语言 | JavaScript |
| Forks | 7,159 |
| Issues | 141 |
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
| Stars | 60,991 |
| 语言 | JavaScript |
| Forks | 5,663 |
| Issues | 61 |
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
| Stars | 59,841 |
| 语言 | JavaScript |
| Forks | 20,443 |
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
| Stars | 53,285 |
| 语言 | JavaScript |
| Forks | 10,614 |
| Issues | 449 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,777 |
| 语言 | JavaScript |
| Forks | 11,539 |
| Issues | 266 |
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
| Stars | 133,824 |
| 语言 | Go |
| Forks | 18,999 |
| Issues | 10,118 |
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
| Stars | 106,380 |
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
| Stars | 88,000 |
| 语言 | Go |
| Forks | 8,257 |
| Issues | 238 |
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
| Stars | 83,795 |
| 语言 | Go |
| Forks | 5,165 |
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
| Stars | 68,577 |
| 语言 | Go |
| Forks | 3,228 |
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
| Stars | 57,103 |
| 语言 | Go |
| Forks | 5,080 |
| Issues | 1,171 |
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
| Stars | 51,026 |
| 语言 | Go |
| Forks | 21,905 |
| Issues | 402 |
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
| Stars | 49,452 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 572 |
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
| Stars | 95,775 |
| 语言 | Shell |
| Forks | 15,850 |
| Issues | 133 |
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
| Stars | 123,444 |
| 语言 | Unknown |
| Forks | 12,516 |
| Issues | 88 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,250 |
| 语言 | Python |
| Forks | 12,175 |
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
| Stars | 86,718 |
| 语言 | Python |
| Forks | 7,270 |
| Issues | 489 |
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
| Stars | 77,607 |
| 语言 | Python |
| Forks | 16,935 |
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
| Stars | 85,385 |
| 语言 | TypeScript |
| Forks | 10,653 |
| Issues | 429 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,118 |
| 语言 | JavaScript |
| Forks | 26,685 |
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
| Stars | 71,158 |
| 语言 | JavaScript |
| Forks | 16,795 |
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
| Stars | 67,948 |
| 语言 | JavaScript |
| Forks | 4,560 |
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
| Stars | 67,400 |
| 语言 | JavaScript |
| Forks | 11,952 |
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
| Stars | 66,380 |
| 语言 | JavaScript |
| Forks | 9,186 |
| Issues | 3 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### h5bp/html5-boilerplate

**描述**: A professional front-end template for building fast, robust, and adaptable web apps or sites.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,430 |
| 语言 | JavaScript |
| Forks | 12,308 |
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
| Stars | 50,975 |
| 语言 | Go |
| Forks | 1,610 |
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
| Stars | 46,850 |
| 语言 | Go |
| Forks | 8,854 |
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
| Stars | 46,278 |
| 语言 | Go |
| Forks | 3,817 |
| Issues | 83 |
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
| Stars | 155,984 |
| 语言 | Python |
| Forks | 11,898 |
| Issues | 360 |
| Topics | awesome, github, hellogithub, python |
