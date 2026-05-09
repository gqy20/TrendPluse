# 项目发现报告 (2026-05-09)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 125 |
| 去重移除 | 33 |
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
| 🌐 Web 框架 | 12 |
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
| Stars | 140,770 |
| 语言 | Python |
| Forks | 21,837 |
| Issues | 9,563 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

hermes-agent 是由知名开源 AI 组织 NousResearch 打造的高质量 AI Agent 框架，凭借 14万+ Stars 成为开源 AI Agent 领域的标杆项目。其核心优势在于支持 OpenAI、Anthropic (Claude) 等多主流 AI 提供商的无缝切换，配合成熟的任务规划与工具调用能力，为开发者提供了"与项目共同成长"的灵活 AI 代理解决方案。

**技术亮点**:
- 多 AI 提供商统一接口：内置对 OpenAI、Anthropic/Claude、Codex 等主流 LLM 的适配器，实现一行代码切换不同 AI 引擎
- 结构化工具调用体系：基于 function calling 机制实现可靠的 Agent 工具调度，支持自定义工具扩展
- MIT 开源许可：完全开源且许可宽松，可免费商用，为企业级应用提供法律保障
- 模块化 Agent 架构：采用可扩展的 agent 设计模式，便于集成到现有系统或二次开发
- 成熟的生态集成：与 OpenClaw、Nous Research 工具链深度整合

**适用场景**:
- 企业智能助手开发：构建内部 AI 办公助手、客服机器人或业务流程自动化代理
- AI 应用原型快速搭建：开发者可快速验证 AI Agent 概念，缩短从 idea 到 demo 的周期



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,313 |
| 语言 | Python |
| Forks | 19,411 |
| Issues | 224 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持多后端（Ollama/OpenAI API）、RAG 和 MCP 协议，136K+ Stars 证明其成熟度和社区认可度，是部署私有化 LLM 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现统一接口访问不同 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库增强问答
- MCP 协议支持：支持 Model Context Protocol，可扩展连接外部工具和数据源
- 自托管部署：提供 Docker 一键部署，数据完全私有化，适合企业内网使用
- 现代化 Web 界面：响应式设计，支持多会话管理、代码高亮、图片生成等多模态能力

**适用场景**:
- 企业私有化 AI 助手：适合需要在防火墙内部署 AI 对话系统的企业，满足数据安全和合规要求
- 本地 LLM 开发测试：开发者可在本地运行 Ollama + WebUI 进行快速原型验证和模型调试
- 知识库问答系统：基于 RAG 功能构建私有知识库检索，增强 LLM 的领域知识回答准确性



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,100 |
| 语言 | Python |
| Forks | 9,131 |
| Issues | 3,001 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一（80k+ stars），创新性地将 RAG 与 Agent 能力融合，为 LLM 提供高质量的上下文增强层，特别适合构建企业级智能知识问答系统和 AI Agent 应用。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力实现智能检索规划与动态上下文组装，提升检索准确性和相关性
- 支持 Agentic Retrieval：采用智能体驱动的检索策略，能够理解用户意图并执行多步检索流程
- 完善的上下文管理机制：提供优质的上下文工程能力，确保为 LLM 提供清晰、相关的背景信息
- Apache 2.0 开源许可：完全开源且商业友好，降低企业采用门槛
- 模块化 Python 架构：基于 Python 开发，便于集成和扩展，支持主流 LLM 和向量数据库

**适用场景**:
- 企业智能知识库问答：构建内部知识库检索系统，为 LLM 提供准确的企业私有知识上下文，实现智能客服和员工助手
- AI Agent 应用开发：利用 Agentic RAG 能力开发智能代理应用，支持复杂任务拆解和多步推理
- 文档智能分析与问答：处理结构化/非结构化文档，实现精准的内容理解和问答能力



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 176,617 |
| 语言 | JavaScript |
| Forks | 27,308 |
| Issues | 174 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，拥有超过 17 万 Stars，涵盖 Skills、Instincts、Memory、Security 等完整体系，能显著提升 AI Agent 的开发效率和稳定性。

**技术亮点**:
- 多 Agent 平台支持：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- Skills & Instincts 系统：提供可扩展的技能库和本能机制，让 AI Agent 具备更智能的决策能力
- Memory 记忆管理：内置上下文记忆系统，帮助 AI 保持长程对话一致性和任务连续性
- Security 安全模块：针对 AI 代码生成提供安全防护和审计机制，适合企业级应用
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于生态扩展

**适用场景**:
- 个人开发者提升编码效率：通过 Skills 和 Instincts 优化个人工作流，让 AI 编程助手更懂你的习惯和偏好
- 企业级 AI Agent 部署：利用 Memory 和 Security 模块构建稳定可控的代码助手，处理内部代码库和敏感项目
- AI 编程工具性能调优：基于研究优先的开发方法，对 AI 模型进行性能基准测试和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,162 |
| 语言 | Go |
| Forks | 4,066 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，无需 GPU 即可运行，同时兼容 OpenAI API，极大降低了私有化 AI 部署的门槛，是构建隐私优先 AI 应用的理想选择。

**技术亮点**:
- 多模态模型支持：支持 LLM、图像生成、语音合成、视频处理、音乐生成等多种 AI 任务，覆盖 AI 应用主流场景
- Go 语言实现：采用高性能的 Go 语言开发，充分利用其并发优势和高效内存管理，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和对等网络通信，可构建去中心化 AI 服务网络
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有应用可零成本迁移，降低开发适配成本
- MCP 协议支持：支持 Model Context Protocol 协议，可实现高级 AI Agent 和工具调用能力

**适用场景**:
- 企业私有 AI 部署：企业可在本地服务器部署 AI 服务，满足数据隐私合规要求，避免敏感数据上传到第三方云服务
- 个人开发者隐私应用：开发者可在个人设备上运行 AI 模型，构建隐私优先的应用，如本地知识助手、个人 AI 助手等
- 资源受限环境：在没有 GPU 或网络条件有限的边缘设备、嵌入式系统中运行 AI 推理任务
- 快速原型开发：开发者可利用 OpenAI API 兼容性快速开发 AI 应用原型，完成后轻松切换到本地模型



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,752 |
| 语言 | TypeScript |
| Forks | 15,129 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个企业级多 Agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，提供完整的多 Agent 团队设计和编排能力，是当前最成熟的开源 Agent 开发框架之一

**技术亮点**:
- 多 Agent 协作框架：支持多个 Agent 无缝协作，将 Agent 作为工作交互的基本单位
- 多模型集成：原生支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- MCP 协议支持：遵循 Model Context Protocol 标准，确保 Agent 互操作性
- 知识库集成：内置知识库功能，支持 RAG 检索增强生成架构
- TypeScript 现代技术栈：提供完整类型安全和良好的开发体验

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 协作的自动化流程
- AI 应用快速开发：快速搭建和部署 AI Agent 应用
- 团队协作与知识管理：构建团队共享的 AI 助手



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,078 |
| 语言 | TypeScript |
| Forks | 6,360 |
| Issues | 28 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI 编程助手的"记忆缺失"痛点，通过自动捕获、压缩和检索编码上下文，让 Claude 在每个新会话都能继承历史积累，显著提升长期项目的开发效率，特别适合需要跨会话维护复杂上下文的开发者。

**技术亮点**:
- 基于 Claude Agent SDK 实现端侧 AI 压缩，采用本地 embedding 模型确保数据隐私不外泄
- 结合 ChromaDB 向量数据库与 SQLite 关系存储，实现语义检索 + 结构化数据双重查询能力
- 采用 RAG (检索增强生成) 架构，将历史编码上下文动态注入 LLM 上下文窗口
- 支持 OpenMemory/Mem0 等多 memory 引擎生态，可扩展性强
- TypeScript 原生开发，无缝集成 Claude Code 插件体系

**适用场景**:
- 长期大型项目的开发维护：自动记忆 API 设计决策、业务逻辑变更，避免重复上下文说明
- 多任务并行处理：跨项目复用编码模式和最佳实践，建立个人代码知识库
- 团队知识传承：新成员快速了解项目历史上下文和技术债务背景



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,092 |
| 语言 | Python |
| Forks | 8,690 |
| Issues | 1,001 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是当前最成熟的大模型微调框架之一，基于 ACL 2024 学术论文，支持 100+ 主流 LLMs 和 VLMs 的统一高效微调，通过 LoRA/QLoRA 等技术大幅降低训练门槛和资源消耗。

**技术亮点**:
- 统一微调框架：支持 LLaMA、Qwen、DeepSeek、Gemma 等 100+ 主流 LLMs 及视觉语言模型 VLMs，一套代码支持多种架构
- 高效微调技术栈：集成 LoRA、QLoRA、PEFT 等先进微调方法，显著降低 GPU 显存占用和训练成本
- 完整训练流程支持：涵盖 SFT、DPO、PPO、GRPO 等监督微调和强化学习微调方案
- 多模态能力：支持视觉语言模型微调，可处理图文多模态任务
- 量化与 MoE 支持：内置 INT4/INT8 量化及混合专家模型支持，进一步优化资源利用

**适用场景**:
- 企业 AI 定制：企业可基于 LlamaFactory 使用内部数据快速微调专属大模型，应用于客服、内容生成、业务分析等场景
- 学术研究与实验：研究者可便捷对比不同模型、不同微调方法的效果，加速 NLP/AI 领域研究论文产出
- 个人开发者学习：小体量显存需求让个人开发者也能学习大模型微调技术，降低 LLM 应用开发门槛



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,994 |
| 语言 | HTML |
| Forks | 5,180 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,144 |
| 语言 | Java |
| Forks | 15,970 |
| Issues | 21 |
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
| Stars | 45,617 |
| 语言 | Python |
| Forks | 5,522 |
| Issues | 109 |
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
| Stars | 39,141 |
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
| Stars | 47,690 |
| 语言 | TypeScript |
| Forks | 5,283 |
| Issues | 520 |
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
| Stars | 117,430 |
| 语言 | TypeScript |
| Forks | 7,324 |
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
| Stars | 59,778 |
| 语言 | JavaScript |
| Forks | 6,460 |
| Issues | 366 |
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
| Stars | 72,990 |
| 语言 | Python |
| Forks | 9,243 |
| Issues | 422 |
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
| Stars | 56,831 |
| 语言 | TypeScript |
| Forks | 4,628 |
| Issues | 696 |
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
| Stars | 109,445 |
| 语言 | Python |
| Forks | 16,185 |
| Issues | 5 |
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
| Stars | 93,104 |
| 语言 | Python |
| Forks | 10,540 |
| Issues | 234 |
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
| Stars | 52,681 |
| 语言 | TypeScript |
| Forks | 24,301 |
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
| Stars | 187,229 |
| 语言 | TypeScript |
| Forks | 57,496 |
| Issues | 1,479 |
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
| Stars | 155,520 |
| 语言 | Java |
| Forks | 46,139 |
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
| Stars | 147,893 |
| 语言 | Python |
| Forks | 8,937 |
| Issues | 924 |
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
| Stars | 61,029 |
| 语言 | Jupyter Notebook |
| Forks | 20,657 |
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
| Stars | 58,935 |
| 语言 | Python |
| Forks | 6,380 |
| Issues | 586 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,417 |
| 语言 | Python |
| Forks | 14,068 |
| Issues | 404 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 59,380 |
| 语言 | TypeScript |
| Forks | 9,743 |
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
| Stars | 64,922 |
| 语言 | Rust |
| Forks | 4,181 |
| Issues | 783 |
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
| Stars | 136,313 |
| 语言 | Python |
| Forks | 19,411 |
| Issues | 224 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持多后端（Ollama/OpenAI API）、RAG 和 MCP 协议，136K+ Stars 证明其成熟度和社区认可度，是部署私有化 LLM 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现统一接口访问不同 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库增强问答
- MCP 协议支持：支持 Model Context Protocol，可扩展连接外部工具和数据源
- 自托管部署：提供 Docker 一键部署，数据完全私有化，适合企业内网使用
- 现代化 Web 界面：响应式设计，支持多会话管理、代码高亮、图片生成等多模态能力

**适用场景**:
- 企业私有化 AI 助手：适合需要在防火墙内部署 AI 对话系统的企业，满足数据安全和合规要求
- 本地 LLM 开发测试：开发者可在本地运行 Ollama + WebUI 进行快速原型验证和模型调试
- 知识库问答系统：基于 RAG 功能构建私有知识库检索，增强 LLM 的领域知识回答准确性



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,100 |
| 语言 | Python |
| Forks | 9,131 |
| Issues | 3,001 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一（80k+ stars），创新性地将 RAG 与 Agent 能力融合，为 LLM 提供高质量的上下文增强层，特别适合构建企业级智能知识问答系统和 AI Agent 应用。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力实现智能检索规划与动态上下文组装，提升检索准确性和相关性
- 支持 Agentic Retrieval：采用智能体驱动的检索策略，能够理解用户意图并执行多步检索流程
- 完善的上下文管理机制：提供优质的上下文工程能力，确保为 LLM 提供清晰、相关的背景信息
- Apache 2.0 开源许可：完全开源且商业友好，降低企业采用门槛
- 模块化 Python 架构：基于 Python 开发，便于集成和扩展，支持主流 LLM 和向量数据库

**适用场景**:
- 企业智能知识库问答：构建内部知识库检索系统，为 LLM 提供准确的企业私有知识上下文，实现智能客服和员工助手
- AI Agent 应用开发：利用 Agentic RAG 能力开发智能代理应用，支持复杂任务拆解和多步推理
- 文档智能分析与问答：处理结构化/非结构化文档，实现精准的内容理解和问答能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,752 |
| 语言 | TypeScript |
| Forks | 15,129 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个企业级多 Agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，提供完整的多 Agent 团队设计和编排能力，是当前最成熟的开源 Agent 开发框架之一

**技术亮点**:
- 多 Agent 协作框架：支持多个 Agent 无缝协作，将 Agent 作为工作交互的基本单位
- 多模型集成：原生支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- MCP 协议支持：遵循 Model Context Protocol 标准，确保 Agent 互操作性
- 知识库集成：内置知识库功能，支持 RAG 检索增强生成架构
- TypeScript 现代技术栈：提供完整类型安全和良好的开发体验

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 协作的自动化流程
- AI 应用快速开发：快速搭建和部署 AI Agent 应用
- 团队协作与知识管理：构建团队共享的 AI 助手



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,078 |
| 语言 | TypeScript |
| Forks | 6,360 |
| Issues | 28 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI 编程助手的"记忆缺失"痛点，通过自动捕获、压缩和检索编码上下文，让 Claude 在每个新会话都能继承历史积累，显著提升长期项目的开发效率，特别适合需要跨会话维护复杂上下文的开发者。

**技术亮点**:
- 基于 Claude Agent SDK 实现端侧 AI 压缩，采用本地 embedding 模型确保数据隐私不外泄
- 结合 ChromaDB 向量数据库与 SQLite 关系存储，实现语义检索 + 结构化数据双重查询能力
- 采用 RAG (检索增强生成) 架构，将历史编码上下文动态注入 LLM 上下文窗口
- 支持 OpenMemory/Mem0 等多 memory 引擎生态，可扩展性强
- TypeScript 原生开发，无缝集成 Claude Code 插件体系

**适用场景**:
- 长期大型项目的开发维护：自动记忆 API 设计决策、业务逻辑变更，避免重复上下文说明
- 多任务并行处理：跨项目复用编码模式和最佳实践，建立个人代码知识库
- 团队知识传承：新成员快速了解项目历史上下文和技术债务背景



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,144 |
| 语言 | Java |
| Forks | 15,970 |
| Issues | 21 |
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
| Stars | 45,617 |
| 语言 | Python |
| Forks | 5,522 |
| Issues | 109 |
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
| Stars | 39,141 |
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
| Stars | 102,101 |
| 语言 | TypeScript |
| Forks | 12,345 |
| Issues | 997 |
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
| Stars | 59,778 |
| 语言 | JavaScript |
| Forks | 6,460 |
| Issues | 366 |
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
| Stars | 109,445 |
| 语言 | Python |
| Forks | 16,185 |
| Issues | 5 |
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
| Stars | 77,496 |
| 语言 | Python |
| Forks | 10,397 |
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
| Stars | 52,681 |
| 语言 | TypeScript |
| Forks | 24,301 |
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
| Stars | 45,528 |
| 语言 | Python |
| Forks | 4,931 |
| Issues | 239 |
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
| Stars | 44,199 |
| 语言 | Go |
| Forks | 3,993 |
| Issues | 902 |
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
| Stars | 34,961 |
| 语言 | Python |
| Forks | 4,957 |
| Issues | 231 |
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
| Stars | 140,770 |
| 语言 | Python |
| Forks | 21,837 |
| Issues | 9,563 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

hermes-agent 是由知名开源 AI 组织 NousResearch 打造的高质量 AI Agent 框架，凭借 14万+ Stars 成为开源 AI Agent 领域的标杆项目。其核心优势在于支持 OpenAI、Anthropic (Claude) 等多主流 AI 提供商的无缝切换，配合成熟的任务规划与工具调用能力，为开发者提供了"与项目共同成长"的灵活 AI 代理解决方案。

**技术亮点**:
- 多 AI 提供商统一接口：内置对 OpenAI、Anthropic/Claude、Codex 等主流 LLM 的适配器，实现一行代码切换不同 AI 引擎
- 结构化工具调用体系：基于 function calling 机制实现可靠的 Agent 工具调度，支持自定义工具扩展
- MIT 开源许可：完全开源且许可宽松，可免费商用，为企业级应用提供法律保障
- 模块化 Agent 架构：采用可扩展的 agent 设计模式，便于集成到现有系统或二次开发
- 成熟的生态集成：与 OpenClaw、Nous Research 工具链深度整合

**适用场景**:
- 企业智能助手开发：构建内部 AI 办公助手、客服机器人或业务流程自动化代理
- AI 应用原型快速搭建：开发者可快速验证 AI Agent 概念，缩短从 idea 到 demo 的周期



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,313 |
| 语言 | Python |
| Forks | 19,411 |
| Issues | 224 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面解决方案，支持多后端（Ollama/OpenAI API）、RAG 和 MCP 协议，136K+ Stars 证明其成熟度和社区认可度，是部署私有化 LLM 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，实现统一接口访问不同 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持知识库增强问答
- MCP 协议支持：支持 Model Context Protocol，可扩展连接外部工具和数据源
- 自托管部署：提供 Docker 一键部署，数据完全私有化，适合企业内网使用
- 现代化 Web 界面：响应式设计，支持多会话管理、代码高亮、图片生成等多模态能力

**适用场景**:
- 企业私有化 AI 助手：适合需要在防火墙内部署 AI 对话系统的企业，满足数据安全和合规要求
- 本地 LLM 开发测试：开发者可在本地运行 Ollama + WebUI 进行快速原型验证和模型调试
- 知识库问答系统：基于 RAG 功能构建私有知识库检索，增强 LLM 的领域知识回答准确性



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 176,617 |
| 语言 | JavaScript |
| Forks | 27,308 |
| Issues | 174 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，拥有超过 17 万 Stars，涵盖 Skills、Instincts、Memory、Security 等完整体系，能显著提升 AI Agent 的开发效率和稳定性。

**技术亮点**:
- 多 Agent 平台支持：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- Skills & Instincts 系统：提供可扩展的技能库和本能机制，让 AI Agent 具备更智能的决策能力
- Memory 记忆管理：内置上下文记忆系统，帮助 AI 保持长程对话一致性和任务连续性
- Security 安全模块：针对 AI 代码生成提供安全防护和审计机制，适合企业级应用
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于生态扩展

**适用场景**:
- 个人开发者提升编码效率：通过 Skills 和 Instincts 优化个人工作流，让 AI 编程助手更懂你的习惯和偏好
- 企业级 AI Agent 部署：利用 Memory 和 Security 模块构建稳定可控的代码助手，处理内部代码库和敏感项目
- AI 编程工具性能调优：基于研究优先的开发方法，对 AI 模型进行性能基准测试和优化



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,752 |
| 语言 | TypeScript |
| Forks | 15,129 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个企业级多 Agent 协作平台，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，提供完整的多 Agent 团队设计和编排能力，是当前最成熟的开源 Agent 开发框架之一

**技术亮点**:
- 多 Agent 协作框架：支持多个 Agent 无缝协作，将 Agent 作为工作交互的基本单位
- 多模型集成：原生支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型
- MCP 协议支持：遵循 Model Context Protocol 标准，确保 Agent 互操作性
- 知识库集成：内置知识库功能，支持 RAG 检索增强生成架构
- TypeScript 现代技术栈：提供完整类型安全和良好的开发体验

**适用场景**:
- 企业智能工作流自动化：构建多 Agent 协作的自动化流程
- AI 应用快速开发：快速搭建和部署 AI Agent 应用
- 团队协作与知识管理：构建团队共享的 AI 助手



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,078 |
| 语言 | TypeScript |
| Forks | 6,360 |
| Issues | 28 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 解决了 AI 编程助手的"记忆缺失"痛点，通过自动捕获、压缩和检索编码上下文，让 Claude 在每个新会话都能继承历史积累，显著提升长期项目的开发效率，特别适合需要跨会话维护复杂上下文的开发者。

**技术亮点**:
- 基于 Claude Agent SDK 实现端侧 AI 压缩，采用本地 embedding 模型确保数据隐私不外泄
- 结合 ChromaDB 向量数据库与 SQLite 关系存储，实现语义检索 + 结构化数据双重查询能力
- 采用 RAG (检索增强生成) 架构，将历史编码上下文动态注入 LLM 上下文窗口
- 支持 OpenMemory/Mem0 等多 memory 引擎生态，可扩展性强
- TypeScript 原生开发，无缝集成 Claude Code 插件体系

**适用场景**:
- 长期大型项目的开发维护：自动记忆 API 设计决策、业务逻辑变更，避免重复上下文说明
- 多任务并行处理：跨项目复用编码模式和最佳实践，建立个人代码知识库
- 团队知识传承：新成员快速了解项目历史上下文和技术债务背景



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,907 |
| 语言 | HTML |
| Forks | 21,100 |
| Issues | 47 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万 Star，支持 ChatGPT、Claude、Gemini 等多模型，可自托管实现完全隐私保护，非常适合希望优化 AI 交互的个人开发者和企业团队。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，支持服务端渲染和良好的 SEO
- 支持多 AI 模型集成（ChatGPT、Claude-3、Gemini Pro、GPT-4），提供统一的提示词管理
- 提供自托管部署方案，支持 Docker 和 Vercel 一键部署，保护企业数据隐私
- 活跃的开源社区维护，持续更新高质量提示词，覆盖写作、编程、分析等 50+ 场景
- 支持提示词版本管理和社区评分机制，便于筛选优质内容

**适用场景**:
- 个人用户：发现和收藏优质 AI 提示词，提升 ChatGPT/Claude 等工具的使用效率
- 企业团队：自托管部署专属提示词库，避免敏感数据外泄，适合金融、医疗等高隐私行业
- AI 开发者：参考开源提示词设计模式，学习 prompt engineering 最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,258 |
| 语言 | Jupyter Notebook |
| Forks | 14,256 |
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
| Stars | 51,994 |
| 语言 | HTML |
| Forks | 5,180 |
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
| Stars | 59,778 |
| 语言 | JavaScript |
| Forks | 6,460 |
| Issues | 366 |
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
| Stars | 72,990 |
| 语言 | Python |
| Forks | 9,243 |
| Issues | 422 |
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
| Stars | 56,831 |
| 语言 | TypeScript |
| Forks | 4,628 |
| Issues | 696 |
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
| Stars | 52,681 |
| 语言 | TypeScript |
| Forks | 24,301 |
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
| Stars | 79,501 |
| 语言 | Python |
| Forks | 16,595 |
| Issues | 4,875 |
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
| Stars | 147,893 |
| 语言 | Python |
| Forks | 8,937 |
| Issues | 924 |
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
| Stars | 58,935 |
| 语言 | Python |
| Forks | 6,380 |
| Issues | 586 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,067 |
| 语言 | Go |
| Forks | 16,047 |
| Issues | 3,211 |
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
| Stars | 59,380 |
| 语言 | TypeScript |
| Forks | 9,743 |
| Issues | 118 |
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
| Stars | 57,047 |
| 语言 | Python |
| Forks | 3,131 |
| Issues | 192 |
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
| Stars | 48,585 |
| 语言 | Rust |
| Forks | 9,751 |
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
| Stars | 122,209 |
| 语言 | Python |
| Forks | 8,233 |
| Issues | 634 |
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
| Stars | 71,092 |
| 语言 | Python |
| Forks | 8,690 |
| Issues | 1,001 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是当前最成熟的大模型微调框架之一，基于 ACL 2024 学术论文，支持 100+ 主流 LLMs 和 VLMs 的统一高效微调，通过 LoRA/QLoRA 等技术大幅降低训练门槛和资源消耗。

**技术亮点**:
- 统一微调框架：支持 LLaMA、Qwen、DeepSeek、Gemma 等 100+ 主流 LLMs 及视觉语言模型 VLMs，一套代码支持多种架构
- 高效微调技术栈：集成 LoRA、QLoRA、PEFT 等先进微调方法，显著降低 GPU 显存占用和训练成本
- 完整训练流程支持：涵盖 SFT、DPO、PPO、GRPO 等监督微调和强化学习微调方案
- 多模态能力：支持视觉语言模型微调，可处理图文多模态任务
- 量化与 MoE 支持：内置 INT4/INT8 量化及混合专家模型支持，进一步优化资源利用

**适用场景**:
- 企业 AI 定制：企业可基于 LlamaFactory 使用内部数据快速微调专属大模型，应用于客服、内容生成、业务分析等场景
- 学术研究与实验：研究者可便捷对比不同模型、不同微调方法的效果，加速 NLP/AI 领域研究论文产出
- 个人开发者学习：小体量显存需求让个人开发者也能学习大模型微调技术，降低 LLM 应用开发门槛



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,285 |
| 语言 | Python |
| Forks | 6,748 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面、社区活跃（67k+ stars）的开源金融数据平台，支持股票、加密货币、期权、固收等多品类数据分析，并内置 AI 和机器学习能力，为分析师、量化交易员和 AI 代理提供一站式解决方案。

**技术亮点**:
- 统一的数据 API 层，聚合多个数据源（Yahoo Finance、CoinGecko、FRED 等），提供标准化数据接口
- 内置丰富的金融分析工具库，涵盖技术分析、因子分析、衍生品定价等量化计算模块
- 深度集成 AI/LLM 能力，支持自然语言查询金融数据并生成分析报告
- 模块化架构设计，支持自定义扩展和数据源接入，便于构建个性化金融分析工作流
- 提供 CLI、SDK（Python/TypeScript）和 Web UI 多种交互方式，适配不同技术栈的开发者

**适用场景**:
- 量化投资研究：利用内置的金融指标和量化模型进行策略回测与因子分析
- AI 驱动金融分析：集成大语言模型，实现自然语言驱动的数据查询与报告生成
- 企业级金融数据平台：基于模块化架构构建定制化的市场监控系统或投研系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,907 |
| 语言 | HTML |
| Forks | 21,100 |
| Issues | 47 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万 Star，支持 ChatGPT、Claude、Gemini 等多模型，可自托管实现完全隐私保护，非常适合希望优化 AI 交互的个人开发者和企业团队。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，支持服务端渲染和良好的 SEO
- 支持多 AI 模型集成（ChatGPT、Claude-3、Gemini Pro、GPT-4），提供统一的提示词管理
- 提供自托管部署方案，支持 Docker 和 Vercel 一键部署，保护企业数据隐私
- 活跃的开源社区维护，持续更新高质量提示词，覆盖写作、编程、分析等 50+ 场景
- 支持提示词版本管理和社区评分机制，便于筛选优质内容

**适用场景**:
- 个人用户：发现和收藏优质 AI 提示词，提升 ChatGPT/Claude 等工具的使用效率
- 企业团队：自托管部署专属提示词库，避免敏感数据外泄，适合金融、医疗等高隐私行业
- AI 开发者：参考开源提示词设计模式，学习 prompt engineering 最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,258 |
| 语言 | Jupyter Notebook |
| Forks | 14,256 |
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
| Stars | 160,421 |
| 语言 | Python |
| Forks | 33,148 |
| Issues | 2,357 |
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
| Stars | 79,501 |
| 语言 | Python |
| Forks | 16,595 |
| Issues | 4,875 |
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
| Stars | 112,146 |
| 语言 | Python |
| Forks | 13,101 |
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
| Stars | 99,782 |
| 语言 | Python |
| Forks | 27,731 |
| Issues | 18,504 |
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
| Stars | 176,617 |
| 语言 | JavaScript |
| Forks | 27,308 |
| Issues | 174 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，拥有超过 17 万 Stars，涵盖 Skills、Instincts、Memory、Security 等完整体系，能显著提升 AI Agent 的开发效率和稳定性。

**技术亮点**:
- 多 Agent 平台支持：兼容 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具的统一优化框架
- Skills & Instincts 系统：提供可扩展的技能库和本能机制，让 AI Agent 具备更智能的决策能力
- Memory 记忆管理：内置上下文记忆系统，帮助 AI 保持长程对话一致性和任务连续性
- Security 安全模块：针对 AI 代码生成提供安全防护和审计机制，适合企业级应用
- MCP (Model Context Protocol) 集成：支持标准化的模型上下文协议，便于生态扩展

**适用场景**:
- 个人开发者提升编码效率：通过 Skills 和 Instincts 优化个人工作流，让 AI 编程助手更懂你的习惯和偏好
- 企业级 AI Agent 部署：利用 Memory 和 Security 模块构建稳定可控的代码助手，处理内部代码库和敏感项目
- AI 编程工具性能调优：基于研究优先的开发方法，对 AI 模型进行性能基准测试和优化



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,162 |
| 语言 | Go |
| Forks | 4,066 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，无需 GPU 即可运行，同时兼容 OpenAI API，极大降低了私有化 AI 部署的门槛，是构建隐私优先 AI 应用的理想选择。

**技术亮点**:
- 多模态模型支持：支持 LLM、图像生成、语音合成、视频处理、音乐生成等多种 AI 任务，覆盖 AI 应用主流场景
- Go 语言实现：采用高性能的 Go 语言开发，充分利用其并发优势和高效内存管理，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和对等网络通信，可构建去中心化 AI 服务网络
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有应用可零成本迁移，降低开发适配成本
- MCP 协议支持：支持 Model Context Protocol 协议，可实现高级 AI Agent 和工具调用能力

**适用场景**:
- 企业私有 AI 部署：企业可在本地服务器部署 AI 服务，满足数据隐私合规要求，避免敏感数据上传到第三方云服务
- 个人开发者隐私应用：开发者可在个人设备上运行 AI 模型，构建隐私优先的应用，如本地知识助手、个人 AI 助手等
- 资源受限环境：在没有 GPU 或网络条件有限的边缘设备、嵌入式系统中运行 AI 推理任务
- 快速原型开发：开发者可利用 OpenAI API 兼容性快速开发 AI 应用原型，完成后轻松切换到本地模型



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,144 |
| 语言 | Java |
| Forks | 15,970 |
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
| Stars | 72,990 |
| 语言 | Python |
| Forks | 9,243 |
| Issues | 422 |
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
| Stars | 56,831 |
| 语言 | TypeScript |
| Forks | 4,628 |
| Issues | 696 |
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
| Stars | 187,229 |
| 语言 | TypeScript |
| Forks | 57,496 |
| Issues | 1,479 |
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
| Stars | 58,935 |
| 语言 | Python |
| Forks | 6,380 |
| Issues | 586 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 433,544 |
| 语言 | Python |
| Forks | 47,450 |
| Issues | 1,323 |
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
| Stars | 161,311 |
| 语言 | Python |
| Forks | 13,406 |
| Issues | 2,475 |
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
| Stars | 98,052 |
| 语言 | Python |
| Forks | 9,224 |
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
| Stars | 83,146 |
| 语言 | Python |
| Forks | 9,692 |
| Issues | 261 |
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
| Stars | 184,733 |
| 语言 | TypeScript |
| Forks | 39,734 |
| Issues | 17,398 |
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
| Stars | 94,282 |
| 语言 | TypeScript |
| Forks | 9,416 |
| Issues | 300 |
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
| Stars | 79,145 |
| 语言 | TypeScript |
| Forks | 5,863 |
| Issues | 714 |
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
| Stars | 77,457 |
| 语言 | TypeScript |
| Forks | 6,653 |
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
| Stars | 80,103 |
| 语言 | Go |
| Forks | 2,802 |
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
| Stars | 77,688 |
| 语言 | Go |
| Forks | 2,822 |
| Issues | 959 |
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
| Stars | 56,831 |
| 语言 | TypeScript |
| Forks | 4,628 |
| Issues | 696 |
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
| Stars | 187,229 |
| 语言 | TypeScript |
| Forks | 57,496 |
| Issues | 1,479 |
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
| Stars | 58,935 |
| 语言 | Python |
| Forks | 6,380 |
| Issues | 586 |
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
| Forks | 10,339 |
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
| Stars | 122,159 |
| 语言 | Go |
| Forks | 43,014 |
| Issues | 2,670 |
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
| Stars | 71,535 |
| 语言 | Go |
| Forks | 18,932 |
| Issues | 3,813 |
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
| Stars | 55,520 |
| 语言 | Go |
| Forks | 6,675 |
| Issues | 2,775 |
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
| Stars | 47,501 |
| 语言 | Go |
| Forks | 5,058 |
| Issues | 989 |
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
| Stars | 94,282 |
| 语言 | TypeScript |
| Forks | 9,416 |
| Issues | 300 |
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
| Stars | 78,459 |
| 语言 | TypeScript |
| Forks | 6,867 |
| Issues | 391 |
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
| Stars | 86,448 |
| 语言 | JavaScript |
| Forks | 7,803 |
| Issues | 737 |
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
| Stars | 63,073 |
| 语言 | Go |
| Forks | 5,972 |
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
| Stars | 59,468 |
| 语言 | Go |
| Forks | 4,333 |
| Issues | 27 |
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
| Stars | 70,229 |
| 语言 | Go |
| Forks | 1,917 |
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
| Forks | 7,483 |
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
| Stars | 86,448 |
| 语言 | JavaScript |
| Forks | 7,803 |
| Issues | 737 |
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
| Stars | 63,974 |
| 语言 | Go |
| Forks | 10,388 |
| Issues | 778 |
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
| Stars | 46,162 |
| 语言 | Go |
| Forks | 4,066 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的本地 AI 引擎，支持 LLM、视觉、语音、图像、视频等多种模型类型，无需 GPU 即可运行，同时兼容 OpenAI API，极大降低了私有化 AI 部署的门槛，是构建隐私优先 AI 应用的理想选择。

**技术亮点**:
- 多模态模型支持：支持 LLM、图像生成、语音合成、视频处理、音乐生成等多种 AI 任务，覆盖 AI 应用主流场景
- Go 语言实现：采用高性能的 Go 语言开发，充分利用其并发优势和高效内存管理，适合生产环境部署
- 去中心化架构：集成 libp2p 支持分布式和对等网络通信，可构建去中心化 AI 服务网络
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有应用可零成本迁移，降低开发适配成本
- MCP 协议支持：支持 Model Context Protocol 协议，可实现高级 AI Agent 和工具调用能力

**适用场景**:
- 企业私有 AI 部署：企业可在本地服务器部署 AI 服务，满足数据隐私合规要求，避免敏感数据上传到第三方云服务
- 个人开发者隐私应用：开发者可在个人设备上运行 AI 模型，构建隐私优先的应用，如本地知识助手、个人 AI 助手等
- 资源受限环境：在没有 GPU 或网络条件有限的边缘设备、嵌入式系统中运行 AI 推理任务
- 快速原型开发：开发者可利用 OpenAI API 兼容性快速开发 AI 应用原型，完成后轻松切换到本地模型



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 433,544 |
| 语言 | Python |
| Forks | 47,450 |
| Issues | 1,323 |
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
| Stars | 98,052 |
| 语言 | Python |
| Forks | 9,224 |
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
| Stars | 87,451 |
| 语言 | Python |
| Forks | 33,853 |
| Issues | 429 |
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
| Forks | 27,211 |
| Issues | 1,133 |
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
| Stars | 79,145 |
| 语言 | TypeScript |
| Forks | 5,863 |
| Issues | 714 |
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
| Stars | 69,006 |
| 语言 | JavaScript |
| Forks | 23,272 |
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
| Stars | 55,947 |
| 语言 | JavaScript |
| Forks | 10,201 |
| Issues | 375 |
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
| Stars | 51,855 |
| 语言 | JavaScript |
| Forks | 4,714 |
| Issues | 1,475 |
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
| Stars | 88,464 |
| 语言 | Go |
| Forks | 8,608 |
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
| Stars | 72,271 |
| 语言 | Go |
| Forks | 4,720 |
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
| Stars | 58,229 |
| 语言 | Go |
| Forks | 3,359 |
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
| Stars | 102,101 |
| 语言 | TypeScript |
| Forks | 12,345 |
| Issues | 997 |
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
| Stars | 59,778 |
| 语言 | JavaScript |
| Forks | 6,460 |
| Issues | 366 |
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
| Stars | 44,199 |
| 语言 | Go |
| Forks | 3,993 |
| Issues | 902 |
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
| Forks | 10,339 |
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
| Stars | 161,907 |
| 语言 | HTML |
| Forks | 21,100 |
| Issues | 47 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是目前最大的开源提示词库之一，拥有超过 16 万 Star，支持 ChatGPT、Claude、Gemini 等多模型，可自托管实现完全隐私保护，非常适合希望优化 AI 交互的个人开发者和企业团队。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈，支持服务端渲染和良好的 SEO
- 支持多 AI 模型集成（ChatGPT、Claude-3、Gemini Pro、GPT-4），提供统一的提示词管理
- 提供自托管部署方案，支持 Docker 和 Vercel 一键部署，保护企业数据隐私
- 活跃的开源社区维护，持续更新高质量提示词，覆盖写作、编程、分析等 50+ 场景
- 支持提示词版本管理和社区评分机制，便于筛选优质内容

**适用场景**:
- 个人用户：发现和收藏优质 AI 提示词，提升 ChatGPT/Claude 等工具的使用效率
- 企业团队：自托管部署专属提示词库，避免敏感数据外泄，适合金融、医疗等高隐私行业
- AI 开发者：参考开源提示词设计模式，学习 prompt engineering 最佳实践



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,617 |
| 语言 | Python |
| Forks | 5,522 |
| Issues | 109 |
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
| Stars | 59,380 |
| 语言 | TypeScript |
| Forks | 9,743 |
| Issues | 118 |
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
| Stars | 57,047 |
| 语言 | Python |
| Forks | 3,131 |
| Issues | 192 |
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
| Stars | 89,872 |
| 语言 | TypeScript |
| Forks | 10,044 |
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
| Stars | 87,928 |
| 语言 | TypeScript |
| Forks | 8,954 |
| Issues | 1,670 |
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
| Stars | 172,199 |
| 语言 | Go |
| Forks | 13,198 |
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
| Stars | 127,749 |
| 语言 | JavaScript |
| Forks | 12,485 |
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
| Stars | 136,976 |
| 语言 | Unknown |
| Forks | 34,175 |
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
| Stars | 67,896 |
| 语言 | Shell |
| Forks | 5,849 |
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
| Stars | 94,240 |
| 语言 | Python |
| Forks | 8,190 |
| Issues | 417 |
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
| Stars | 92,805 |
| 语言 | Python |
| Forks | 13,505 |
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
| Stars | 387,953 |
| 语言 | Python |
| Forks | 66,277 |
| Issues | 82 |
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
| Stars | 116,884 |
| 语言 | TypeScript |
| Forks | 8,530 |
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
| Stars | 116,073 |
| 语言 | TypeScript |
| Forks | 6,108 |
| Issues | 52 |
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
| Stars | 92,281 |
| 语言 | TypeScript |
| Forks | 13,648 |
| Issues | 541 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,121 |
| 语言 | JavaScript |
| Forks | 5,187 |
| Issues | 32 |
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
| Stars | 48,364 |
| 语言 | Go |
| Forks | 10,345 |
| Issues | 1,899 |
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
| Stars | 109,229 |
| 语言 | C++ |
| Forks | 18,002 |
| Issues | 1,598 |
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
| Stars | 63,287 |
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
| Stars | 37,257 |
| 语言 | TypeScript |
| Forks | 4,239 |
| Issues | 386 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 296,751 |
| 语言 | Python |
| Forks | 27,850 |
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
| Stars | 220,895 |
| 语言 | Python |
| Forks | 50,582 |
| Issues | 963 |
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
| Stars | 86,980 |
| 语言 | Python |
| Forks | 37,429 |
| Issues | 3,903 |
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
| Stars | 77,661 |
| 语言 | Python |
| Forks | 45,097 |
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
| Stars | 444,404 |
| 语言 | TypeScript |
| Forks | 44,501 |
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
| Stars | 354,471 |
| 语言 | TypeScript |
| Forks | 44,045 |
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
| Stars | 122,834 |
| 语言 | TypeScript |
| Forks | 13,584 |
| Issues | 3,037 |
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
| Stars | 113,917 |
| 语言 | TypeScript |
| Forks | 8,752 |
| Issues | 1,855 |
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
| Stars | 108,800 |
| 语言 | TypeScript |
| Forks | 13,387 |
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
| Stars | 100,116 |
| 语言 | TypeScript |
| Forks | 5,564 |
| Issues | 665 |
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
| Stars | 97,978 |
| 语言 | TypeScript |
| Forks | 54,608 |
| Issues | 1,364 |
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
| Stars | 94,903 |
| 语言 | TypeScript |
| Forks | 5,223 |
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
| Stars | 83,402 |
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
| Stars | 80,486 |
| 语言 | TypeScript |
| Forks | 8,153 |
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
| Stars | 244,900 |
| 语言 | JavaScript |
| Forks | 51,008 |
| Issues | 1,288 |
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
| Stars | 117,120 |
| 语言 | JavaScript |
| Forks | 35,510 |
| Issues | 2,672 |
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
| Stars | 112,381 |
| 语言 | JavaScript |
| Forks | 36,367 |
| Issues | 491 |
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
| Stars | 109,039 |
| 语言 | JavaScript |
| Forks | 11,676 |
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
| Stars | 99,817 |
| 语言 | JavaScript |
| Forks | 10,931 |
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
| Stars | 98,295 |
| 语言 | JavaScript |
| Forks | 32,638 |
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
| Stars | 95,742 |
| 语言 | JavaScript |
| Forks | 15,468 |
| Issues | 57 |
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
| Stars | 86,512 |
| 语言 | JavaScript |
| Forks | 4,907 |
| Issues | 998 |
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
| Stars | 65,766 |
| 语言 | JavaScript |
| Forks | 9,356 |
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
| Stars | 64,529 |
| 语言 | JavaScript |
| Forks | 4,095 |
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
| Forks | 7,157 |
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
| Stars | 60,972 |
| 语言 | JavaScript |
| Forks | 5,664 |
| Issues | 60 |
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
| Stars | 59,839 |
| 语言 | JavaScript |
| Forks | 20,446 |
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
| Stars | 53,280 |
| 语言 | JavaScript |
| Forks | 10,613 |
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
| Stars | 52,769 |
| 语言 | JavaScript |
| Forks | 11,538 |
| Issues | 265 |
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
| Stars | 133,817 |
| 语言 | Go |
| Forks | 18,998 |
| Issues | 10,111 |
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
| Stars | 106,368 |
| 语言 | Go |
| Forks | 15,035 |
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
| Stars | 87,991 |
| 语言 | Go |
| Forks | 8,256 |
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
| Stars | 83,755 |
| 语言 | Go |
| Forks | 5,164 |
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
| Stars | 68,579 |
| 语言 | Go |
| Forks | 3,228 |
| Issues | 13 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,095 |
| 语言 | Go |
| Forks | 5,080 |
| Issues | 1,169 |
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
| Stars | 51,024 |
| 语言 | Go |
| Forks | 21,906 |
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
| Stars | 49,450 |
| 语言 | Go |
| Forks | 7,948 |
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
| Stars | 95,326 |
| 语言 | Shell |
| Forks | 15,744 |
| Issues | 131 |
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
| Stars | 122,141 |
| 语言 | Unknown |
| Forks | 12,359 |
| Issues | 88 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,202 |
| 语言 | Python |
| Forks | 12,170 |
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
| Stars | 86,698 |
| 语言 | Python |
| Forks | 7,269 |
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
| Stars | 77,587 |
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
| Stars | 85,338 |
| 语言 | TypeScript |
| Forks | 10,644 |
| Issues | 425 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,117 |
| 语言 | JavaScript |
| Forks | 26,687 |
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
| Stars | 71,152 |
| 语言 | JavaScript |
| Forks | 16,796 |
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
| Stars | 67,921 |
| 语言 | JavaScript |
| Forks | 4,558 |
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
| Stars | 67,402 |
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
| Stars | 66,376 |
| 语言 | JavaScript |
| Forks | 9,188 |
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
| Stars | 57,432 |
| 语言 | JavaScript |
| Forks | 12,306 |
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
| Stars | 50,971 |
| 语言 | Go |
| Forks | 1,611 |
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
| Stars | 46,851 |
| 语言 | Go |
| Forks | 8,853 |
| Issues | 18 |
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
| Stars | 46,274 |
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
| Stars | 155,754 |
| 语言 | Python |
| Forks | 11,876 |
| Issues | 359 |
| Topics | awesome, github, hellogithub, python |
