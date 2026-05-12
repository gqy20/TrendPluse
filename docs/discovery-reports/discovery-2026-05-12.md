# 项目发现报告 (2026-05-12)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
| 去重移除 | 35 |
| 已在监控 | 23 |


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


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 146,698 |
| 语言 | Python |
| Forks | 23,001 |
| Issues | 10,518 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-Agent 是由知名 AI 研究组织 NousResearch 开发的开源 AI Agent 框架，拥有超过 14.6 万 Stars 的庞大社区支持，支持 OpenAI、Anthropic Claude 等多种主流 LLM 提供商，采用 MIT 许可证开源，是构建企业级或个人 AI 应用的理想选择。

**技术亮点**:
- 支持多 LLM 提供商集成（OpenAI GPT、Anthropic Claude、Codex 等），便于灵活切换和对比不同模型效果
- MIT 许可证开源，社区活跃（146K+ Stars），持续迭代更新
- 基于 Python 开发，充分利用 Python 丰富的 AI 生态和工具链
- 专为 AI Agent 场景设计，支持多轮对话、工具调用和任务规划能力
- 支持 Anthropic Claude Code 和 OpenAI Codex 等代码生成能力，适用于自动化编程任务

**适用场景**:
- 企业级 AI 助手开发：构建客服机器人、智能文档助手、业务自动化流程等企业应用
- 个人开发者快速原型：利用现成框架快速验证 AI Agent 想法，降低开发成本
- 多模型对比与选型：同一代码库支持多种 LLM，方便企业根据场景和成本选择最优模型



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,784 |
| 语言 | Python |
| Forks | 19,482 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 协议支持，既能满足企业数据隐私需求，又能为个人开发者提供便捷的本地 LLM 使用体验，社区活跃度高（13万+ Stars）是其成熟度和可靠性的有力证明。

**技术亮点**:
- 多后端统一接入：同时支持 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 后端，可通过统一界面灵活切换和管理
- RAG 检索增强生成：内置知识库功能，支持文档上传和语义检索，提升 LLM 回答的准确性和上下文相关性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，完全私有化，数据留在本地，满足企业对数据安全和隐私的严格要求
- 丰富的 Web UI 功能：提供聊天管理、模型配置、提示词模板、历史记录等完整的前端功能，开箱即用

**适用场景**:
- 企业级 AI 助手部署：企业可在私有环境中部署统一的 AI 界面，整合内部知识库和文档，实现安全的智能问答和文档处理
- 个人开发者本地 LLM 使用：开发者可在本地运行 Ollama 等开源模型，通过友好的 Web 界面便捷地与本地 LLM 交互和测试
- AI 应用快速原型开发：开发团队可基于该项目快速构建 AI 应用原型，利用其 API 接口和插件机制进行二次开发



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,353 |
| 语言 | Python |
| Forks | 9,166 |
| Issues | 3,012 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源社区最活跃的 RAG 项目之一（80k+ stars），创新性地将 RAG 与 Agent 能力深度融合，实现了从简单检索到智能推理的跨越，提供端到端 RAG 流程支持，让开发者能快速构建高质量 LLM 应用

**技术亮点**:
- Agentic Retrieval（智能检索）：突破传统关键词/向量匹配，结合 Agent 能力实现意图理解、多步推理和动态检索策略
- RAG + Agent 融合架构：将检索增强生成与自主 Agent 有机结合，支持复杂任务的分解与执行
- 深度文档理解：支持多种文档格式的智能解析与结构化提取，提升知识库构建质量
- 灵活的 LLM 支持：兼容多种主流大语言模型，支持本地部署和云端 API 接入
- 可视化流程编排：提供友好的配置界面，降低 RAG 系统搭建门槛

**适用场景**:
- 企业知识库智能问答：构建私有化知识库问答系统，支持复杂文档的精准检索与回答生成
- 智能客服与助手：开发具备深度理解能力的 AI 客服，自动处理多轮对话和复杂查询
- 文档分析与挖掘：对合同、报告、手册等长文档进行智能解析、问答和知识提取



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 180,404 |
| 语言 | JavaScript |
| Forks | 27,807 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对 AI 编码助手生态的全面性能优化框架，通过 Skills、Memory、Security 等模块显著提升 Claude Code、Cursor 等工具的效能，180K+ Stars 验证了其极高的社区认可度和实用价值。

**技术亮点**:
- 多 AI 编码工具兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- MCP (Model Context Protocol) 集成：提供标准化的模型上下文协议支持
- Memory 系统：实现持久化记忆功能，让 AI 保持跨会话的上下文理解
- Security 模块：内置安全机制确保 AI 代理操作的代码安全合规
- Skills & Instincts 框架：通过预定义技能和本能机制优化 AI 决策路径

**适用场景**:
- 企业级 AI 开发助手部署：为企业团队配置统一的 AI 编程规范、安全策略和知识库
- 个人开发者效率提升：利用 Memory 功能构建个人代码知识库，AI 记住项目历史和偏好
- AI Agent 性能调优：研究并优化 AI 代理的决策流程、响应速度和输出质量



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,220 |
| 语言 | Go |
| Forks | 4,072 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面且成熟的开源本地AI推理引擎，支持LLM、视觉、语音、图像等多种模型类型，能够在普通硬件上运行而无需GPU，大大降低了AI应用部署的门槛，尤其适合对数据隐私有要求或需要控制成本的企业和个人开发者。

**技术亮点**:
- 基于Go语言开发，具备高性能和低内存占用的优势，适合生产环境部署
- 支持多种AI模型类型，包括Llama、Mamba等大语言模型，以及Stable Diffusion、MusicGen等多模态模型
- 去中心化架构设计，集成libp2p支持分布式和P2P网络部署能力
- 提供RESTful API接口，支持MCP协议，便于与现有系统快速集成
- 支持语音合成(TTS)、语音识别、图像生成、目标检测等多种任务，覆盖AI应用全场景

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI模型，数据不出本地，满足金融、医疗等敏感行业的隐私合规要求
- 边缘计算与物联网：部署在树莓派、工控机等资源受限设备上，实现本地化的AI推理能力
- 开发测试与原型验证：开发者可以在本地快速测试和迭代AI应用，无需依赖云服务或支付API费用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,932 |
| 语言 | TypeScript |
| Forks | 15,161 |
| Issues | 787 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI Agent协作平台，拥有76K+ Stars证明了其极高的社区认可度。它独特地将多Agent协作、Agent团队设计和知识库管理集成在一起，支持OpenAI/Claude/DeepSeek/Gemini等多模型，对于想要快速构建企业级AI Agent应用的团队来说，是一个值得信赖的开源选择。

**技术亮点**:
- 多模型支持：无缝集成OpenAI GPT、Claude、DeepSeek、Gemini等多个主流AI模型，支持灵活切换
- MCP协议支持：原生支持Model Context Protocol标准，便于扩展和生态对接
- 多Agent协作框架：提供完整的多智能体协作机制，支持Agent团队设计和任务分配
- 知识库集成：内置RAG能力，支持文档检索和知识增强的AI交互
- TypeScript全栈架构：从前端到后端采用TypeScript开发，提供完整的类型安全和开发体验

**适用场景**:
- 企业级AI Agent应用开发：适合需要快速构建多模型支持、智能对话、知识库问答等企业AI应用
- 多Agent协作系统搭建：适合需要构建多智能体协作、任务分工、自动化的复杂工作流场景
- AI助手/聊天机器人开发：适合开发者快速搭建支持多种AI模型的智能对话应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,197 |
| 语言 | TypeScript |
| Forks | 6,454 |
| Issues | 61 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

一款开源的跨会话 AI 记忆管理系统，通过 AI 压缩和 RAG 技术智能管理 Agent 上下文，能够让 AI Agent 跨越会话保持连贯记忆，大幅提升多轮对话和复杂任务的处理效率，特别适合需要长期上下文的企业级应用。

**技术亮点**:
- 采用 AI 驱动的记忆压缩算法，自动提炼关键信息并丢弃冗余内容
- 基于 RAG（检索增强生成）架构，支持 ChromaDB 等向量数据库实现语义检索
- 支持 SQLite 本地持久化存储，无需复杂基础设施即可部署
- 多 Agent 兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI Agent
- 提供 TypeScript SDK，现代化技术栈便于集成到现有项目

**适用场景**:
- AI Agent 开发：为自定义 AI 助手添加长期记忆能力，适用于客服机器人、个人助理等场景
- 企业知识管理：构建私有化的 AI 记忆库，帮助团队在多个会话中复用项目上下文和技术方案
- 个人生产力工具：作为 Super Memory 或 Mem0 的开源替代方案，打造个人 AI 知识管理系统



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,186 |
| 语言 | Python |
| Forks | 8,697 |
| Issues | 1,007 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持100+LLM和VLM的统一高效微调，集成 LoRA/QLoRA/RLHF 等多种技术，提供开箱即用的 WebUI，让研究者和开发者无需深入底层实现即可快速训练和微调大模型。

**技术亮点**:
- 支持100+主流大模型：Llama/Gemma/Qwen/DeepSeek/Mistral/MoE等，覆盖GPT/Gemma/LLaMA等生态
- 集成多种微调技术：LoRA、QLoRA、Prefix Tuning、Full-parameter Fine-tuning 及 RLHF (PPO/DPO/KTO)
- 支持视觉语言模型(VLM)微调：包括 LLaVA、Qwen-VL、InternVL 等多模态模型
- 提供 WebUI 和 CLI 双界面，支持分布式训练 (DeepSpeed ZeRO)，降低使用门槛
- 量化支持：4-bit/8-bit 量化配合 QLoRA 可在消费级 GPU 上微调大模型

**适用场景**:
- 企业级应用定制：企业可使用 LlamaFactory 微调私有模型，适配客服、文档分析、代码生成等垂直场景
- 个人开发者快速实验：利用 WebUI 和 QLoRA 技术，个人开发者可在 24GB 显存的消费级显卡上微调 7B-13B 参数模型
- 学术研究与模型对比：研究者可快速对比不同微调方法在各模型上的效果差异
- 多模态任务开发：支持视觉问答、图文理解等 VLM 微调，适合构建视觉智能应用



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,341 |
| 语言 | Python |
| Forks | 14,502 |
| Issues | 336 |
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
| Stars | 60,027 |
| 语言 | TypeScript |
| Forks | 9,839 |
| Issues | 119 |
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
| Stars | 52,642 |
| 语言 | HTML |
| Forks | 5,257 |
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
| Stars | 48,155 |
| 语言 | Python |
| Forks | 5,797 |
| Issues | 116 |
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
| Stars | 46,205 |
| 语言 | Java |
| Forks | 15,983 |
| Issues | 20 |
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
| Stars | 39,160 |
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
| Stars | 49,666 |
| 语言 | TypeScript |
| Forks | 5,512 |
| Issues | 536 |
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
| Stars | 118,879 |
| 语言 | TypeScript |
| Forks | 7,354 |
| Issues | 315 |
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
| Stars | 59,937 |
| 语言 | JavaScript |
| Forks | 6,474 |
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
| Stars | 73,280 |
| 语言 | Python |
| Forks | 9,267 |
| Issues | 424 |
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
| Stars | 57,431 |
| 语言 | TypeScript |
| Forks | 4,668 |
| Issues | 701 |
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
| Stars | 109,971 |
| 语言 | Python |
| Forks | 16,285 |
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
| Stars | 93,594 |
| 语言 | Python |
| Forks | 10,594 |
| Issues | 228 |
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
| Stars | 52,771 |
| 语言 | TypeScript |
| Forks | 24,325 |
| Issues | 835 |
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
| Stars | 187,595 |
| 语言 | TypeScript |
| Forks | 57,571 |
| Issues | 1,450 |
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
| Stars | 155,605 |
| 语言 | Java |
| Forks | 46,140 |
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
| Stars | 148,023 |
| 语言 | Python |
| Forks | 8,963 |
| Issues | 922 |
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
| Stars | 61,278 |
| 语言 | Jupyter Notebook |
| Forks | 20,753 |
| Issues | 9 |
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
| Stars | 68,580 |
| 语言 | Rust |
| Forks | 4,377 |
| Issues | 835 |
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
| Stars | 59,428 |
| 语言 | Python |
| Forks | 6,457 |
| Issues | 609 |
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
| Stars | 136,784 |
| 语言 | Python |
| Forks | 19,482 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 协议支持，既能满足企业数据隐私需求，又能为个人开发者提供便捷的本地 LLM 使用体验，社区活跃度高（13万+ Stars）是其成熟度和可靠性的有力证明。

**技术亮点**:
- 多后端统一接入：同时支持 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 后端，可通过统一界面灵活切换和管理
- RAG 检索增强生成：内置知识库功能，支持文档上传和语义检索，提升 LLM 回答的准确性和上下文相关性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，完全私有化，数据留在本地，满足企业对数据安全和隐私的严格要求
- 丰富的 Web UI 功能：提供聊天管理、模型配置、提示词模板、历史记录等完整的前端功能，开箱即用

**适用场景**:
- 企业级 AI 助手部署：企业可在私有环境中部署统一的 AI 界面，整合内部知识库和文档，实现安全的智能问答和文档处理
- 个人开发者本地 LLM 使用：开发者可在本地运行 Ollama 等开源模型，通过友好的 Web 界面便捷地与本地 LLM 交互和测试
- AI 应用快速原型开发：开发团队可基于该项目快速构建 AI 应用原型，利用其 API 接口和插件机制进行二次开发



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,353 |
| 语言 | Python |
| Forks | 9,166 |
| Issues | 3,012 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是开源社区最活跃的 RAG 项目之一（80k+ stars），创新性地将 RAG 与 Agent 能力深度融合，实现了从简单检索到智能推理的跨越，提供端到端 RAG 流程支持，让开发者能快速构建高质量 LLM 应用

**技术亮点**:
- Agentic Retrieval（智能检索）：突破传统关键词/向量匹配，结合 Agent 能力实现意图理解、多步推理和动态检索策略
- RAG + Agent 融合架构：将检索增强生成与自主 Agent 有机结合，支持复杂任务的分解与执行
- 深度文档理解：支持多种文档格式的智能解析与结构化提取，提升知识库构建质量
- 灵活的 LLM 支持：兼容多种主流大语言模型，支持本地部署和云端 API 接入
- 可视化流程编排：提供友好的配置界面，降低 RAG 系统搭建门槛

**适用场景**:
- 企业知识库智能问答：构建私有化知识库问答系统，支持复杂文档的精准检索与回答生成
- 智能客服与助手：开发具备深度理解能力的 AI 客服，自动处理多轮对话和复杂查询
- 文档分析与挖掘：对合同、报告、手册等长文档进行智能解析、问答和知识提取



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,932 |
| 语言 | TypeScript |
| Forks | 15,161 |
| Issues | 787 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI Agent协作平台，拥有76K+ Stars证明了其极高的社区认可度。它独特地将多Agent协作、Agent团队设计和知识库管理集成在一起，支持OpenAI/Claude/DeepSeek/Gemini等多模型，对于想要快速构建企业级AI Agent应用的团队来说，是一个值得信赖的开源选择。

**技术亮点**:
- 多模型支持：无缝集成OpenAI GPT、Claude、DeepSeek、Gemini等多个主流AI模型，支持灵活切换
- MCP协议支持：原生支持Model Context Protocol标准，便于扩展和生态对接
- 多Agent协作框架：提供完整的多智能体协作机制，支持Agent团队设计和任务分配
- 知识库集成：内置RAG能力，支持文档检索和知识增强的AI交互
- TypeScript全栈架构：从前端到后端采用TypeScript开发，提供完整的类型安全和开发体验

**适用场景**:
- 企业级AI Agent应用开发：适合需要快速构建多模型支持、智能对话、知识库问答等企业AI应用
- 多Agent协作系统搭建：适合需要构建多智能体协作、任务分工、自动化的复杂工作流场景
- AI助手/聊天机器人开发：适合开发者快速搭建支持多种AI模型的智能对话应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,197 |
| 语言 | TypeScript |
| Forks | 6,454 |
| Issues | 61 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

一款开源的跨会话 AI 记忆管理系统，通过 AI 压缩和 RAG 技术智能管理 Agent 上下文，能够让 AI Agent 跨越会话保持连贯记忆，大幅提升多轮对话和复杂任务的处理效率，特别适合需要长期上下文的企业级应用。

**技术亮点**:
- 采用 AI 驱动的记忆压缩算法，自动提炼关键信息并丢弃冗余内容
- 基于 RAG（检索增强生成）架构，支持 ChromaDB 等向量数据库实现语义检索
- 支持 SQLite 本地持久化存储，无需复杂基础设施即可部署
- 多 Agent 兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI Agent
- 提供 TypeScript SDK，现代化技术栈便于集成到现有项目

**适用场景**:
- AI Agent 开发：为自定义 AI 助手添加长期记忆能力，适用于客服机器人、个人助理等场景
- 企业知识管理：构建私有化的 AI 记忆库，帮助团队在多个会话中复用项目上下文和技术方案
- 个人生产力工具：作为 Super Memory 或 Mem0 的开源替代方案，打造个人 AI 知识管理系统



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,155 |
| 语言 | Python |
| Forks | 5,797 |
| Issues | 116 |
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
| Stars | 46,205 |
| 语言 | Java |
| Forks | 15,983 |
| Issues | 20 |
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
| Stars | 39,160 |
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
| Stars | 102,237 |
| 语言 | TypeScript |
| Forks | 12,368 |
| Issues | 1,017 |
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
| Stars | 59,937 |
| 语言 | JavaScript |
| Forks | 6,474 |
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
| Stars | 109,971 |
| 语言 | Python |
| Forks | 16,285 |
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
| Stars | 77,693 |
| 语言 | Python |
| Forks | 10,418 |
| Issues | 199 |
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
| Stars | 52,771 |
| 语言 | TypeScript |
| Forks | 24,325 |
| Issues | 835 |
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
| Stars | 47,175 |
| 语言 | Python |
| Forks | 5,113 |
| Issues | 255 |
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
| Stars | 44,256 |
| 语言 | Go |
| Forks | 3,999 |
| Issues | 891 |
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
| Stars | 35,096 |
| 语言 | Python |
| Forks | 4,979 |
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
| Stars | 146,698 |
| 语言 | Python |
| Forks | 23,001 |
| Issues | 10,518 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-Agent 是由知名 AI 研究组织 NousResearch 开发的开源 AI Agent 框架，拥有超过 14.6 万 Stars 的庞大社区支持，支持 OpenAI、Anthropic Claude 等多种主流 LLM 提供商，采用 MIT 许可证开源，是构建企业级或个人 AI 应用的理想选择。

**技术亮点**:
- 支持多 LLM 提供商集成（OpenAI GPT、Anthropic Claude、Codex 等），便于灵活切换和对比不同模型效果
- MIT 许可证开源，社区活跃（146K+ Stars），持续迭代更新
- 基于 Python 开发，充分利用 Python 丰富的 AI 生态和工具链
- 专为 AI Agent 场景设计，支持多轮对话、工具调用和任务规划能力
- 支持 Anthropic Claude Code 和 OpenAI Codex 等代码生成能力，适用于自动化编程任务

**适用场景**:
- 企业级 AI 助手开发：构建客服机器人、智能文档助手、业务自动化流程等企业应用
- 个人开发者快速原型：利用现成框架快速验证 AI Agent 想法，降低开发成本
- 多模型对比与选型：同一代码库支持多种 LLM，方便企业根据场景和成本选择最优模型



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,784 |
| 语言 | Python |
| Forks | 19,482 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的自托管 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 协议支持，既能满足企业数据隐私需求，又能为个人开发者提供便捷的本地 LLM 使用体验，社区活跃度高（13万+ Stars）是其成熟度和可靠性的有力证明。

**技术亮点**:
- 多后端统一接入：同时支持 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 后端，可通过统一界面灵活切换和管理
- RAG 检索增强生成：内置知识库功能，支持文档上传和语义检索，提升 LLM 回答的准确性和上下文相关性
- MCP 协议支持：支持 Model Context Protocol 协议，可扩展连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，完全私有化，数据留在本地，满足企业对数据安全和隐私的严格要求
- 丰富的 Web UI 功能：提供聊天管理、模型配置、提示词模板、历史记录等完整的前端功能，开箱即用

**适用场景**:
- 企业级 AI 助手部署：企业可在私有环境中部署统一的 AI 界面，整合内部知识库和文档，实现安全的智能问答和文档处理
- 个人开发者本地 LLM 使用：开发者可在本地运行 Ollama 等开源模型，通过友好的 Web 界面便捷地与本地 LLM 交互和测试
- AI 应用快速原型开发：开发团队可基于该项目快速构建 AI 应用原型，利用其 API 接口和插件机制进行二次开发



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 180,404 |
| 语言 | JavaScript |
| Forks | 27,807 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对 AI 编码助手生态的全面性能优化框架，通过 Skills、Memory、Security 等模块显著提升 Claude Code、Cursor 等工具的效能，180K+ Stars 验证了其极高的社区认可度和实用价值。

**技术亮点**:
- 多 AI 编码工具兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- MCP (Model Context Protocol) 集成：提供标准化的模型上下文协议支持
- Memory 系统：实现持久化记忆功能，让 AI 保持跨会话的上下文理解
- Security 模块：内置安全机制确保 AI 代理操作的代码安全合规
- Skills & Instincts 框架：通过预定义技能和本能机制优化 AI 决策路径

**适用场景**:
- 企业级 AI 开发助手部署：为企业团队配置统一的 AI 编程规范、安全策略和知识库
- 个人开发者效率提升：利用 Memory 功能构建个人代码知识库，AI 记住项目历史和偏好
- AI Agent 性能调优：研究并优化 AI 代理的决策流程、响应速度和输出质量



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,950 |
| 语言 | JavaScript |
| Forks | 3,251 |
| Issues | 186 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 项目通过穴居人风格的极简表达实现 65% token 削减，在高性价比方面极具吸引力。58,950 stars 证明了其在大规模 AI 编程辅助场景中的实用价值，是追求 API 成本优化的开发者的必备工具。

**技术亮点**:
- Token 极致压缩技术：将复杂自然语言压缩为穴居人式短句，实现 65% token 削减
- Claude Code 原生 Skill 集成：直接作为 Claude Code 扩展使用，无缝对接开发工作流
- 零依赖轻量设计：无需额外模型或库，直接利用 LLM 本身的理解能力
- Prompt Engineering 创新实践：探索极简指令边界，验证 LLM 对压缩语言的理解力
- MIT 开源许可：支持自由使用、商业集成和二次开发

**适用场景**:
- 成本敏感型 AI 开发：个人开发者和初创团队降低 Claude API 调用费用
- 高频代码辅助场景：日常编程中减少 token 消耗以提升响应速度
- 企业级 LLM 成本优化：大规模部署时通过精简 prompt 降低整体支出



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,932 |
| 语言 | TypeScript |
| Forks | 15,161 |
| Issues | 787 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完整的AI Agent协作平台，拥有76K+ Stars证明了其极高的社区认可度。它独特地将多Agent协作、Agent团队设计和知识库管理集成在一起，支持OpenAI/Claude/DeepSeek/Gemini等多模型，对于想要快速构建企业级AI Agent应用的团队来说，是一个值得信赖的开源选择。

**技术亮点**:
- 多模型支持：无缝集成OpenAI GPT、Claude、DeepSeek、Gemini等多个主流AI模型，支持灵活切换
- MCP协议支持：原生支持Model Context Protocol标准，便于扩展和生态对接
- 多Agent协作框架：提供完整的多智能体协作机制，支持Agent团队设计和任务分配
- 知识库集成：内置RAG能力，支持文档检索和知识增强的AI交互
- TypeScript全栈架构：从前端到后端采用TypeScript开发，提供完整的类型安全和开发体验

**适用场景**:
- 企业级AI Agent应用开发：适合需要快速构建多模型支持、智能对话、知识库问答等企业AI应用
- 多Agent协作系统搭建：适合需要构建多智能体协作、任务分工、自动化的复杂工作流场景
- AI助手/聊天机器人开发：适合开发者快速搭建支持多种AI模型的智能对话应用



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,197 |
| 语言 | TypeScript |
| Forks | 6,454 |
| Issues | 61 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

一款开源的跨会话 AI 记忆管理系统，通过 AI 压缩和 RAG 技术智能管理 Agent 上下文，能够让 AI Agent 跨越会话保持连贯记忆，大幅提升多轮对话和复杂任务的处理效率，特别适合需要长期上下文的企业级应用。

**技术亮点**:
- 采用 AI 驱动的记忆压缩算法，自动提炼关键信息并丢弃冗余内容
- 基于 RAG（检索增强生成）架构，支持 ChromaDB 等向量数据库实现语义检索
- 支持 SQLite 本地持久化存储，无需复杂基础设施即可部署
- 多 Agent 兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI Agent
- 提供 TypeScript SDK，现代化技术栈便于集成到现有项目

**适用场景**:
- AI Agent 开发：为自定义 AI 助手添加长期记忆能力，适用于客服机器人、个人助理等场景
- 企业知识管理：构建私有化的 AI 记忆库，帮助团队在多个会话中复用项目上下文和技术方案
- 个人生产力工具：作为 Super Memory 或 Mem0 的开源替代方案，打造个人 AI 知识管理系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,114 |
| 语言 | HTML |
| Forks | 21,109 |
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
| Stars | 93,657 |
| 语言 | Jupyter Notebook |
| Forks | 14,409 |
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
| Stars | 60,027 |
| 语言 | TypeScript |
| Forks | 9,839 |
| Issues | 119 |
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
| Stars | 52,642 |
| 语言 | HTML |
| Forks | 5,257 |
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
| Stars | 59,937 |
| 语言 | JavaScript |
| Forks | 6,474 |
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
| Stars | 73,280 |
| 语言 | Python |
| Forks | 9,267 |
| Issues | 424 |
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
| Stars | 57,431 |
| 语言 | TypeScript |
| Forks | 4,668 |
| Issues | 701 |
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
| Stars | 52,771 |
| 语言 | TypeScript |
| Forks | 24,325 |
| Issues | 835 |
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
| Stars | 79,798 |
| 语言 | Python |
| Forks | 16,710 |
| Issues | 4,920 |
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
| Stars | 148,023 |
| 语言 | Python |
| Forks | 8,963 |
| Issues | 922 |
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
| Stars | 59,428 |
| 语言 | Python |
| Forks | 6,457 |
| Issues | 609 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,277 |
| 语言 | Go |
| Forks | 16,091 |
| Issues | 3,233 |
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
| Stars | 48,662 |
| 语言 | Rust |
| Forks | 9,785 |
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
| Stars | 122,855 |
| 语言 | Python |
| Forks | 8,296 |
| Issues | 639 |
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
| Stars | 71,186 |
| 语言 | Python |
| Forks | 8,697 |
| Issues | 1,007 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的大模型微调框架，支持100+LLM和VLM的统一高效微调，集成 LoRA/QLoRA/RLHF 等多种技术，提供开箱即用的 WebUI，让研究者和开发者无需深入底层实现即可快速训练和微调大模型。

**技术亮点**:
- 支持100+主流大模型：Llama/Gemma/Qwen/DeepSeek/Mistral/MoE等，覆盖GPT/Gemma/LLaMA等生态
- 集成多种微调技术：LoRA、QLoRA、Prefix Tuning、Full-parameter Fine-tuning 及 RLHF (PPO/DPO/KTO)
- 支持视觉语言模型(VLM)微调：包括 LLaVA、Qwen-VL、InternVL 等多模态模型
- 提供 WebUI 和 CLI 双界面，支持分布式训练 (DeepSpeed ZeRO)，降低使用门槛
- 量化支持：4-bit/8-bit 量化配合 QLoRA 可在消费级 GPU 上微调大模型

**适用场景**:
- 企业级应用定制：企业可使用 LlamaFactory 微调私有模型，适配客服、文档分析、代码生成等垂直场景
- 个人开发者快速实验：利用 WebUI 和 QLoRA 技术，个人开发者可在 24GB 显存的消费级显卡上微调 7B-13B 参数模型
- 学术研究与模型对比：研究者可快速对比不同微调方法在各模型上的效果差异
- 多模态任务开发：支持视觉问答、图文理解等 VLM 微调，适合构建视觉智能应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,469 |
| 语言 | Python |
| Forks | 6,778 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个拥有超过 67k Stars 的开源金融数据平台，覆盖股票、加密货币、期权、固定收益等多类资产，提供 AI 和机器学习集成能力，适合分析师、量化交易员和 AI 代理使用，一站式满足金融数据获取、分析和建模需求。

**技术亮点**:
- 统一的数据 API：整合多个数据源，提供标准化的金融数据接口，支持股票、加密货币、期权、固收等资产类别
- AI/ML 原生支持：内置机器学习模块，支持金融预测、情绪分析和量化策略开发
- Python 生态深度集成：利用 pandas、numpy、matplotlib 等库，支持 Jupyter Notebook 交互式分析
- 模块化架构设计：数据获取、清洗、分析、可视化模块解耦，便于扩展和自定义
- 丰富的可视化能力：内置专业金融图表（K线、期权链、收益率曲线等），支持交互式图表生成

**适用场景**:
- 量化交易研究：获取实时市场数据，构建和回测量化交易策略
- 投资组合分析与风险管理：多维度分析资产配置，计算风险指标
- AI 金融代理：作为 AI Agent 的金融数据后端，支持自动化投资决策和报告生成



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,114 |
| 语言 | HTML |
| Forks | 21,109 |
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
| Stars | 93,657 |
| 语言 | Jupyter Notebook |
| Forks | 14,409 |
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
| Stars | 160,532 |
| 语言 | Python |
| Forks | 33,182 |
| Issues | 2,350 |
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
| Stars | 79,798 |
| 语言 | Python |
| Forks | 16,710 |
| Issues | 4,920 |
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
| Stars | 112,628 |
| 语言 | Python |
| Forks | 13,169 |
| Issues | 3,988 |
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
| Stars | 99,857 |
| 语言 | Python |
| Forks | 27,765 |
| Issues | 18,416 |
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
| Stars | 180,404 |
| 语言 | JavaScript |
| Forks | 27,807 |
| Issues | 0 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个针对 AI 编码助手生态的全面性能优化框架，通过 Skills、Memory、Security 等模块显著提升 Claude Code、Cursor 等工具的效能，180K+ Stars 验证了其极高的社区认可度和实用价值。

**技术亮点**:
- 多 AI 编码工具兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手
- MCP (Model Context Protocol) 集成：提供标准化的模型上下文协议支持
- Memory 系统：实现持久化记忆功能，让 AI 保持跨会话的上下文理解
- Security 模块：内置安全机制确保 AI 代理操作的代码安全合规
- Skills & Instincts 框架：通过预定义技能和本能机制优化 AI 决策路径

**适用场景**:
- 企业级 AI 开发助手部署：为企业团队配置统一的 AI 编程规范、安全策略和知识库
- 个人开发者效率提升：利用 Memory 功能构建个人代码知识库，AI 记住项目历史和偏好
- AI Agent 性能调优：研究并优化 AI 代理的决策流程、响应速度和输出质量



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,220 |
| 语言 | Go |
| Forks | 4,072 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面且成熟的开源本地AI推理引擎，支持LLM、视觉、语音、图像等多种模型类型，能够在普通硬件上运行而无需GPU，大大降低了AI应用部署的门槛，尤其适合对数据隐私有要求或需要控制成本的企业和个人开发者。

**技术亮点**:
- 基于Go语言开发，具备高性能和低内存占用的优势，适合生产环境部署
- 支持多种AI模型类型，包括Llama、Mamba等大语言模型，以及Stable Diffusion、MusicGen等多模态模型
- 去中心化架构设计，集成libp2p支持分布式和P2P网络部署能力
- 提供RESTful API接口，支持MCP协议，便于与现有系统快速集成
- 支持语音合成(TTS)、语音识别、图像生成、目标检测等多种任务，覆盖AI应用全场景

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI模型，数据不出本地，满足金融、医疗等敏感行业的隐私合规要求
- 边缘计算与物联网：部署在树莓派、工控机等资源受限设备上，实现本地化的AI推理能力
- 开发测试与原型验证：开发者可以在本地快速测试和迭代AI应用，无需依赖云服务或支付API费用



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,205 |
| 语言 | Java |
| Forks | 15,983 |
| Issues | 20 |
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
| Stars | 73,280 |
| 语言 | Python |
| Forks | 9,267 |
| Issues | 424 |
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
| Stars | 57,431 |
| 语言 | TypeScript |
| Forks | 4,668 |
| Issues | 701 |
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
| Stars | 187,595 |
| 语言 | TypeScript |
| Forks | 57,571 |
| Issues | 1,450 |
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
| Stars | 59,428 |
| 语言 | Python |
| Forks | 6,457 |
| Issues | 609 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,018 |
| 语言 | JavaScript |
| Forks | 4,187 |
| Issues | 1,316 |
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
| Stars | 434,478 |
| 语言 | Python |
| Forks | 47,568 |
| Issues | 1,317 |
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
| Stars | 161,930 |
| 语言 | Python |
| Forks | 13,532 |
| Issues | 2,500 |
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
| Stars | 98,127 |
| 语言 | Python |
| Forks | 9,252 |
| Issues | 195 |
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
| Stars | 83,253 |
| 语言 | Python |
| Forks | 9,716 |
| Issues | 264 |
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
| Stars | 184,836 |
| 语言 | TypeScript |
| Forks | 39,785 |
| Issues | 17,538 |
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
| Stars | 94,303 |
| 语言 | TypeScript |
| Forks | 9,417 |
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
| Stars | 79,164 |
| 语言 | TypeScript |
| Forks | 5,868 |
| Issues | 720 |
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
| Stars | 77,513 |
| 语言 | TypeScript |
| Forks | 6,666 |
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
| Stars | 80,191 |
| 语言 | Go |
| Forks | 2,804 |
| Issues | 316 |
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
| Stars | 77,842 |
| 语言 | Go |
| Forks | 2,828 |
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
| Stars | 57,431 |
| 语言 | TypeScript |
| Forks | 4,668 |
| Issues | 701 |
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
| Stars | 187,595 |
| 语言 | TypeScript |
| Forks | 57,571 |
| Issues | 1,450 |
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
| Stars | 59,428 |
| 语言 | Python |
| Forks | 6,457 |
| Issues | 609 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,692 |
| 语言 | Go |
| Forks | 10,349 |
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
| Stars | 122,211 |
| 语言 | Go |
| Forks | 43,035 |
| Issues | 2,681 |
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
| Issues | 3,810 |
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
| Stars | 55,614 |
| 语言 | Go |
| Forks | 6,685 |
| Issues | 2,793 |
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
| Stars | 94,303 |
| 语言 | TypeScript |
| Forks | 9,417 |
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
| Stars | 78,649 |
| 语言 | TypeScript |
| Forks | 6,888 |
| Issues | 395 |
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
| Stars | 86,613 |
| 语言 | JavaScript |
| Forks | 7,826 |
| Issues | 744 |
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
| Stars | 70,263 |
| 语言 | Go |
| Forks | 1,918 |
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
| Stars | 63,138 |
| 语言 | Go |
| Forks | 5,983 |
| Issues | 807 |
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
| Stars | 59,519 |
| 语言 | Go |
| Forks | 4,337 |
| Issues | 22 |
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
| Stars | 47,509 |
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
| Stars | 60,914 |
| 语言 | Go |
| Forks | 7,487 |
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
| Stars | 86,613 |
| 语言 | JavaScript |
| Forks | 7,826 |
| Issues | 744 |
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
| Stars | 64,002 |
| 语言 | Go |
| Forks | 10,401 |
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
| Stars | 46,220 |
| 语言 | Go |
| Forks | 4,072 |
| Issues | 160 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面且成熟的开源本地AI推理引擎，支持LLM、视觉、语音、图像等多种模型类型，能够在普通硬件上运行而无需GPU，大大降低了AI应用部署的门槛，尤其适合对数据隐私有要求或需要控制成本的企业和个人开发者。

**技术亮点**:
- 基于Go语言开发，具备高性能和低内存占用的优势，适合生产环境部署
- 支持多种AI模型类型，包括Llama、Mamba等大语言模型，以及Stable Diffusion、MusicGen等多模态模型
- 去中心化架构设计，集成libp2p支持分布式和P2P网络部署能力
- 提供RESTful API接口，支持MCP协议，便于与现有系统快速集成
- 支持语音合成(TTS)、语音识别、图像生成、目标检测等多种任务，覆盖AI应用全场景

**适用场景**:
- 企业私有化AI部署：在本地服务器运行AI模型，数据不出本地，满足金融、医疗等敏感行业的隐私合规要求
- 边缘计算与物联网：部署在树莓派、工控机等资源受限设备上，实现本地化的AI推理能力
- 开发测试与原型验证：开发者可以在本地快速测试和迭代AI应用，无需依赖云服务或支付API费用



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 434,478 |
| 语言 | Python |
| Forks | 47,568 |
| Issues | 1,317 |
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
| Stars | 98,127 |
| 语言 | Python |
| Forks | 9,252 |
| Issues | 195 |
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
| Stars | 87,466 |
| 语言 | Python |
| Forks | 33,868 |
| Issues | 428 |
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
| Stars | 100,085 |
| 语言 | TypeScript |
| Forks | 27,204 |
| Issues | 1,138 |
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
| Stars | 79,164 |
| 语言 | TypeScript |
| Forks | 5,868 |
| Issues | 720 |
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
| Stars | 69,015 |
| 语言 | JavaScript |
| Forks | 23,306 |
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
| Stars | 55,954 |
| 语言 | JavaScript |
| Forks | 10,200 |
| Issues | 370 |
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
| Stars | 88,487 |
| 语言 | Go |
| Forks | 8,606 |
| Issues | 684 |
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
| Stars | 72,375 |
| 语言 | Go |
| Forks | 4,732 |
| Issues | 239 |
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
| Stars | 58,289 |
| 语言 | Go |
| Forks | 3,370 |
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
| Stars | 102,237 |
| 语言 | TypeScript |
| Forks | 12,368 |
| Issues | 1,017 |
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
| Stars | 59,937 |
| 语言 | JavaScript |
| Forks | 6,474 |
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
| Stars | 44,256 |
| 语言 | Go |
| Forks | 3,999 |
| Issues | 891 |
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
| Stars | 51,692 |
| 语言 | Go |
| Forks | 10,349 |
| Issues | 242 |
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
| Stars | 58,950 |
| 语言 | JavaScript |
| Forks | 3,251 |
| Issues | 186 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

caveman 项目通过穴居人风格的极简表达实现 65% token 削减，在高性价比方面极具吸引力。58,950 stars 证明了其在大规模 AI 编程辅助场景中的实用价值，是追求 API 成本优化的开发者的必备工具。

**技术亮点**:
- Token 极致压缩技术：将复杂自然语言压缩为穴居人式短句，实现 65% token 削减
- Claude Code 原生 Skill 集成：直接作为 Claude Code 扩展使用，无缝对接开发工作流
- 零依赖轻量设计：无需额外模型或库，直接利用 LLM 本身的理解能力
- Prompt Engineering 创新实践：探索极简指令边界，验证 LLM 对压缩语言的理解力
- MIT 开源许可：支持自由使用、商业集成和二次开发

**适用场景**:
- 成本敏感型 AI 开发：个人开发者和初创团队降低 Claude API 调用费用
- 高频代码辅助场景：日常编程中减少 token 消耗以提升响应速度
- 企业级 LLM 成本优化：大规模部署时通过精简 prompt 降低整体支出



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,114 |
| 语言 | HTML |
| Forks | 21,109 |
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
| Stars | 60,027 |
| 语言 | TypeScript |
| Forks | 9,839 |
| Issues | 119 |
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
| Stars | 48,155 |
| 语言 | Python |
| Forks | 5,797 |
| Issues | 116 |
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
| Stars | 89,893 |
| 语言 | TypeScript |
| Forks | 10,052 |
| Issues | 2,272 |
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
| Stars | 88,007 |
| 语言 | TypeScript |
| Forks | 8,965 |
| Issues | 1,662 |
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
| Stars | 172,485 |
| 语言 | Go |
| Forks | 13,208 |
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
| Stars | 127,778 |
| 语言 | JavaScript |
| Forks | 12,484 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (64 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,243 |
| 语言 | Unknown |
| Forks | 34,205 |
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
| Stars | 75,684 |
| 语言 | Shell |
| Forks | 6,522 |
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
| Stars | 97,136 |
| 语言 | Python |
| Forks | 8,434 |
| Issues | 404 |
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
| Stars | 92,941 |
| 语言 | Python |
| Forks | 13,533 |
| Issues | 129 |
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
| Stars | 388,142 |
| 语言 | Python |
| Forks | 66,289 |
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
| Stars | 117,642 |
| 语言 | TypeScript |
| Forks | 8,578 |
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
| Stars | 116,165 |
| 语言 | TypeScript |
| Forks | 6,124 |
| Issues | 30 |
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
| Stars | 94,608 |
| 语言 | TypeScript |
| Forks | 14,018 |
| Issues | 459 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,751 |
| 语言 | JavaScript |
| Forks | 5,233 |
| Issues | 63 |
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
| Stars | 48,387 |
| 语言 | Go |
| Forks | 10,348 |
| Issues | 1,906 |
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
| Stars | 109,767 |
| 语言 | C++ |
| Forks | 18,118 |
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
| Stars | 63,296 |
| 语言 | Python |
| Forks | 1,655 |
| Issues | 38 |
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
| Stars | 37,963 |
| 语言 | TypeScript |
| Forks | 4,338 |
| Issues | 276 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 297,292 |
| 语言 | Python |
| Forks | 27,879 |
| Issues | 17 |
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
| Stars | 87,026 |
| 语言 | Python |
| Forks | 37,465 |
| Issues | 3,945 |
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
| Stars | 444,572 |
| 语言 | TypeScript |
| Forks | 44,533 |
| Issues | 186 |
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
| Stars | 354,657 |
| 语言 | TypeScript |
| Forks | 44,062 |
| Issues | 9 |
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
| Stars | 123,019 |
| 语言 | TypeScript |
| Forks | 13,617 |
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
| Stars | 114,156 |
| 语言 | TypeScript |
| Forks | 8,782 |
| Issues | 1,875 |
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
| Stars | 108,827 |
| 语言 | TypeScript |
| Forks | 13,391 |
| Issues | 5,037 |
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
| Stars | 100,395 |
| 语言 | TypeScript |
| Forks | 5,586 |
| Issues | 668 |
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
| Stars | 98,003 |
| 语言 | TypeScript |
| Forks | 54,615 |
| Issues | 1,373 |
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
| Stars | 94,968 |
| 语言 | TypeScript |
| Forks | 5,234 |
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
| Stars | 85,527 |
| 语言 | TypeScript |
| Forks | 10,669 |
| Issues | 438 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,430 |
| 语言 | TypeScript |
| Forks | 7,610 |
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
| Stars | 80,561 |
| 语言 | TypeScript |
| Forks | 8,164 |
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
| Stars | 244,982 |
| 语言 | JavaScript |
| Forks | 51,025 |
| Issues | 1,291 |
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
| Stars | 117,168 |
| 语言 | JavaScript |
| Forks | 35,526 |
| Issues | 2,664 |
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
| Stars | 112,427 |
| 语言 | JavaScript |
| Forks | 36,370 |
| Issues | 484 |
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
| Stars | 109,049 |
| 语言 | JavaScript |
| Forks | 11,684 |
| Issues | 153 |
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
| Stars | 98,320 |
| 语言 | JavaScript |
| Forks | 32,645 |
| Issues | 1,536 |
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
| Stars | 95,751 |
| 语言 | JavaScript |
| Forks | 15,472 |
| Issues | 59 |
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
| Stars | 86,549 |
| 语言 | JavaScript |
| Forks | 4,912 |
| Issues | 1,001 |
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
| Stars | 66,393 |
| 语言 | JavaScript |
| Forks | 9,188 |
| Issues | 3 |
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
| Stars | 65,766 |
| 语言 | JavaScript |
| Forks | 9,358 |
| Issues | 199 |
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
| Stars | 64,626 |
| 语言 | JavaScript |
| Forks | 4,101 |
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
| Stars | 61,224 |
| 语言 | JavaScript |
| Forks | 7,164 |
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
| Stars | 61,054 |
| 语言 | JavaScript |
| Forks | 5,668 |
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
| Stars | 59,842 |
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
| Stars | 53,302 |
| 语言 | JavaScript |
| Forks | 10,616 |
| Issues | 451 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,793 |
| 语言 | JavaScript |
| Forks | 11,542 |
| Issues | 276 |
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
| Stars | 133,849 |
| 语言 | Go |
| Forks | 19,001 |
| Issues | 10,125 |
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
| Stars | 106,464 |
| 语言 | Go |
| Forks | 15,045 |
| Issues | 41 |
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
| Stars | 88,034 |
| 语言 | Go |
| Forks | 8,267 |
| Issues | 244 |
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
| Stars | 83,937 |
| 语言 | Go |
| Forks | 5,177 |
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
| Stars | 68,575 |
| 语言 | Go |
| Forks | 3,232 |
| Issues | 43 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,148 |
| 语言 | Go |
| Forks | 5,085 |
| Issues | 1,179 |
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
| Stars | 51,031 |
| 语言 | Go |
| Forks | 21,909 |
| Issues | 388 |
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
| Stars | 49,460 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 575 |
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
| Stars | 96,446 |
| 语言 | Shell |
| Forks | 15,991 |
| Issues | 134 |
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
| Stars | 126,817 |
| 语言 | Unknown |
| Forks | 12,887 |
| Issues | 88 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,973 |
| 语言 | Python |
| Forks | 50,613 |
| Issues | 970 |
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
| Stars | 99,374 |
| 语言 | Python |
| Forks | 12,179 |
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
| Stars | 86,770 |
| 语言 | Python |
| Forks | 7,286 |
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
| Stars | 77,663 |
| 语言 | Python |
| Forks | 16,948 |
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
| Stars | 148,114 |
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
| Stars | 71,192 |
| 语言 | JavaScript |
| Forks | 16,800 |
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
| Stars | 68,046 |
| 语言 | JavaScript |
| Forks | 4,571 |
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
| Stars | 67,408 |
| 语言 | JavaScript |
| Forks | 11,951 |
| Issues | 562 |
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
| Stars | 51,011 |
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
| Stars | 46,854 |
| 语言 | Go |
| Forks | 8,858 |
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
| Stars | 46,318 |
| 语言 | Go |
| Forks | 3,817 |
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
| Stars | 156,442 |
| 语言 | Python |
| Forks | 11,936 |
| Issues | 362 |
| Topics | awesome, github, hellogithub, python |
