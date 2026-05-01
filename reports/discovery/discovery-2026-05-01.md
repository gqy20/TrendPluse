# 项目发现报告 (2026-05-01)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 124 |
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
| Stars | 135,109 |
| 语言 | Python |
| Forks | 19,207 |
| Issues | 341 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面项目，支持 Ollama、OpenAI API 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议支持，135k+ stars 证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人开发者构建私有化 AI 助手。

**技术亮点**:
- 多后端统一接口：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，提供统一的对话和管理体验
- RAG 检索增强生成：内置文档处理和向量检索能力，可基于私有知识库进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展与外部工具和数据的集成
- 自托管部署：可完全私有化部署，无需依赖第三方服务，保障数据安全与隐私
- 现代化 Web 界面：提供直观的用户界面，支持模型管理、会话历史、多模态交互等功能

**适用场景**:
- 企业私有 AI 助手：需要在内部部署 AI 对话系统，处理敏感业务数据，符合合规要求
- 开发者本地 LLM 开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 进行快速原型开发和测试
- RAG 应用构建：基于自有文档库构建知识问答系统，支持文档上传、向量化存储和智能检索



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 128,062 |
| 语言 | Python |
| Forks | 19,253 |
| Issues | 7,569 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是由顶级开源AI研究组织打造的成熟AI代理框架，拥有128K+ Stars的社区认可度，支持Claude、ChatGPT等多模型集成，具备强大的代码执行和多Agent协作能力，是构建企业级AI应用和个人智能助手的理想选择。

**技术亮点**:
- 多AI提供商集成：无缝支持Anthropic (Claude)、OpenAI (ChatGPT)等主流大语言模型，提供统一的接口抽象层
- 开源Hermes模型生态：基于Nous Research著名的Hermes系列开源模型开发，具备强大的推理和对话能力
- 代码执行能力：深度集成Claude Code和Codex等代码智能功能，支持自动化编程和代码生成任务
- 模块化Agent架构：采用可扩展的模块化设计，支持自定义工具、插件和工作流，便于二次开发
- 活跃的社区生态：拥有庞大的开源社区支持，持续迭代更新，文档和示例完善

**适用场景**:
- 企业级AI应用开发：构建智能客服、工作流自动化、知识库问答等商业应用系统
- 个人开发者智能助手：开发个人AI助手、代码审查工具、自动文档生成等开发效率提升工具
- AI研究实验：基于成熟的Agent框架进行LLM应用研究、多Agent系统实验和prompt工程测试



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,455 |
| 语言 | JavaScript |
| Forks | 26,584 |
| Issues | 149 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 Claude Code、Cursor 等主流 AI 编程助手设计的性能优化框架，通过 Skills、Memory、Security 等模块显著提升 AI Agent 的任务完成效率，是当前最受欢迎的 AI 代码助手增强工具之一。

**技术亮点**:
- Skills 系统：支持自定义技能扩展，让 AI 助手具备特定领域专业能力
- MCP (Model Context Protocol) 集成：标准化上下文管理协议，提升多工具协作能力
- Memory 记忆管理：持久化上下文记忆，解决长对话中的信息丢失问题
- Security 安全模块：内置代码审查与安全检查机制，保障 AI 生成代码的安全性
- Research-First 开发方法：基于研究的最佳实践优化 AI 输出质量

**适用场景**:
- 企业开发团队：统一管理多个 AI 编程助手，标准化代码质量与安全规范
- 个人开发者：优化 Claude Code/Cursor 等工具的响应效率和任务完成度
- AI Agent 开发：基于 MCP 协议构建多模型协作的智能开发环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,988 |
| 语言 | Go |
| Forks | 4,040 |
| Issues | 153 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持文本生成、图像生成、语音合成、目标检测等多模态任务，无需 GPU 即可在各类硬件上运行，非常适合需要本地化部署 AI 能力的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现在 CPU 上高效运行 AI 模型，无需依赖昂贵的 GPU 资源
- 丰富的 API 接口：提供 RESTful API，兼容 OpenAI API 规范，便于现有应用快速集成
- 分布式与去中心化架构：支持 libp2p 协议实现去中心化部署，支持分布式推理
- Go 语言实现：利用 Go 的并发优势和高效性能，确保系统稳定性和高吞吐量

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地环境运行 AI 服务，数据不出本地，满足隐私合规要求
- 边缘计算场景：在资源受限的边缘设备上部署 AI 能力，无需云计算支持，降低延迟和网络依赖
- 快速原型开发：开发者利用兼容 OpenAI 的 API 快速搭建 AI 应用原型，降低开发成本
- 去中心化 AI 应用：基于 libp2p 构建分布式 AI 网络，实现去中心化的模型推理和服务



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,922 |
| 语言 | TypeScript |
| Forks | 15,050 |
| Issues | 756 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备且社区活跃的多智能体协作平台，提供了开箱即用的 Agent 团队设计能力和 MCP 协议集成，让开发者能够快速构建企业级 AI 工作流，极大降低了多智能体系统的开发门槛。

**技术亮点**:
- 基于 TypeScript/Next.js 的现代化全栈架构，75K+ Stars 证明其代码质量和工程化水平业界领先
- 原生支持 MCP (Model Context Protocol) 协议，实现 Agent 与外部工具/数据的标准化交互
- 多模型统一接入层，同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型
- 内置知识库与 RAG 能力，支持 Agent 在特定领域知识上进行推理和问答
- 提供完整的 Agent 生命周期管理，包括设计、部署、监控和协作的全链路能力

**适用场景**:
- 企业级 AI 工作流自动化：构建由多个专业化 Agent 组成的团队，处理复杂的业务流程如客服、工单处理、数据分析等
- 个人开发者快速原型开发：利用现成的 Agent 框架和 MCP 生态快速搭建 AI 应用，降低从零开发的时间成本
- 多模型对比与集成：在一个平台上同时测试和比较不同大语言模型的效果，选择最适合特定场景的模型组合



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,825 |
| 语言 | Python |
| Forks | 8,646 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 背书的统一大模型微调框架，支持 100+ LLM 和 VLM 的高效微调，通过 LoRA、QLoRA、MOE 等技术大幅降低训练成本，是目前最受欢迎的开源微调解决方案之一。

**技术亮点**:
- 支持 100+ 大语言模型（Llama、Qwen、DeepSeek、Gemma 等）和视觉语言模型的统一微调框架
- 集成多种高效微调技术：LoRA、QLoRA、AdaLoRA、DoRA、GaLore、QLoRA+ 等
- 支持 MOE（混合专家）架构的高效微调
- 集成量化技术（AWQ、GPTQ），显著降低 GPU 显存需求
- 支持 RLHF（DPO/CPO/KTO/ORPO）、Supervised Fine-tuning 等多种训练范式

**适用场景**:
- 企业场景：快速定制化企业专属大模型，降低 AI 应用开发成本，支持私有化部署
- 学术研究：模块化设计便于实验对比不同微调方法，支持多种训练策略
- 个人开发者：低门槛微调开源大模型，通过 WebUI 零代码实现模型定制



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,692 |
| 语言 | TypeScript |
| Forks | 6,045 |
| Issues | 50 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个让 Claude Code 拥有长期记忆的插件，通过自动捕获会话内容、AI 压缩和 RAG 检索，解决了 AI 助手中上下文窗口限制的核心痛点，70k+ stars 证明了其在开发者社区的极高认可度。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义记忆存储和检索，支持高效的相似度搜索
- 集成 RAG（检索增强生成）技术，将历史上下文智能注入未来会话
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，优化存储效率
- 支持 SQLite 本地存储和 Mem0/OpenMemory 等记忆引擎集成，灵活性强
- 基于 Embeddings 技术实现语义理解，支持跨会话的项目上下文保持

**适用场景**:
- 个人开发者：让 AI 记住项目架构、编码规范和决策历史，无需每次重复解释背景
- 复杂长期项目：维护跨月甚至跨年的项目上下文，特别适合大型代码库或多人协作项目
- AI 工作流优化：自动建立项目知识库，提升 AI 辅助编程的效率和准确性



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,100 |
| 语言 | HTML |
| Forks | 4,984 |
| Issues | 11 |
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
| Stars | 46,058 |
| 语言 | Java |
| Forks | 15,959 |
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
| Stars | 42,112 |
| 语言 | Python |
| Forks | 5,088 |
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
| Stars | 39,087 |
| 语言 | Python |
| Forks | 6,192 |
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
| Stars | 34,899 |
| 语言 | TypeScript |
| Forks | 3,961 |
| Issues | 480 |
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
| Stars | 113,819 |
| 语言 | TypeScript |
| Forks | 7,213 |
| Issues | 302 |
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
| Stars | 59,370 |
| 语言 | JavaScript |
| Forks | 6,414 |
| Issues | 342 |
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
| Stars | 72,475 |
| 语言 | Python |
| Forks | 9,160 |
| Issues | 404 |
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
| Stars | 55,347 |
| 语言 | TypeScript |
| Forks | 4,489 |
| Issues | 669 |
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
| Stars | 108,316 |
| 语言 | Python |
| Forks | 15,963 |
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
| Stars | 91,544 |
| 语言 | Python |
| Forks | 10,420 |
| Issues | 238 |
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
| Stars | 52,462 |
| 语言 | TypeScript |
| Forks | 24,250 |
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
| Stars | 186,389 |
| 语言 | TypeScript |
| Forks | 57,278 |
| Issues | 1,569 |
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
| Stars | 155,363 |
| 语言 | Java |
| Forks | 46,154 |
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
| Stars | 147,597 |
| 语言 | Python |
| Forks | 8,887 |
| Issues | 944 |
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
| Stars | 60,290 |
| 语言 | Jupyter Notebook |
| Forks | 20,407 |
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
| Stars | 57,394 |
| 语言 | Python |
| Forks | 6,204 |
| Issues | 564 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,723 |
| 语言 | TypeScript |
| Forks | 9,478 |
| Issues | 113 |
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
| Stars | 34,090 |
| 语言 | TypeScript |
| Forks | 3,712 |
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
| Stars | 57,140 |
| 语言 | Rust |
| Forks | 3,704 |
| Issues | 694 |
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
| Stars | 135,109 |
| 语言 | Python |
| Forks | 19,207 |
| Issues | 341 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面项目，支持 Ollama、OpenAI API 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议支持，135k+ stars 证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人开发者构建私有化 AI 助手。

**技术亮点**:
- 多后端统一接口：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，提供统一的对话和管理体验
- RAG 检索增强生成：内置文档处理和向量检索能力，可基于私有知识库进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展与外部工具和数据的集成
- 自托管部署：可完全私有化部署，无需依赖第三方服务，保障数据安全与隐私
- 现代化 Web 界面：提供直观的用户界面，支持模型管理、会话历史、多模态交互等功能

**适用场景**:
- 企业私有 AI 助手：需要在内部部署 AI 对话系统，处理敏感业务数据，符合合规要求
- 开发者本地 LLM 开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 进行快速原型开发和测试
- RAG 应用构建：基于自有文档库构建知识问答系统，支持文档上传、向量化存储和智能检索



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,922 |
| 语言 | TypeScript |
| Forks | 15,050 |
| Issues | 756 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备且社区活跃的多智能体协作平台，提供了开箱即用的 Agent 团队设计能力和 MCP 协议集成，让开发者能够快速构建企业级 AI 工作流，极大降低了多智能体系统的开发门槛。

**技术亮点**:
- 基于 TypeScript/Next.js 的现代化全栈架构，75K+ Stars 证明其代码质量和工程化水平业界领先
- 原生支持 MCP (Model Context Protocol) 协议，实现 Agent 与外部工具/数据的标准化交互
- 多模型统一接入层，同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型
- 内置知识库与 RAG 能力，支持 Agent 在特定领域知识上进行推理和问答
- 提供完整的 Agent 生命周期管理，包括设计、部署、监控和协作的全链路能力

**适用场景**:
- 企业级 AI 工作流自动化：构建由多个专业化 Agent 组成的团队，处理复杂的业务流程如客服、工单处理、数据分析等
- 个人开发者快速原型开发：利用现成的 Agent 框架和 MCP 生态快速搭建 AI 应用，降低从零开发的时间成本
- 多模型对比与集成：在一个平台上同时测试和比较不同大语言模型的效果，选择最适合特定场景的模型组合



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,692 |
| 语言 | TypeScript |
| Forks | 6,045 |
| Issues | 50 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个让 Claude Code 拥有长期记忆的插件，通过自动捕获会话内容、AI 压缩和 RAG 检索，解决了 AI 助手中上下文窗口限制的核心痛点，70k+ stars 证明了其在开发者社区的极高认可度。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义记忆存储和检索，支持高效的相似度搜索
- 集成 RAG（检索增强生成）技术，将历史上下文智能注入未来会话
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，优化存储效率
- 支持 SQLite 本地存储和 Mem0/OpenMemory 等记忆引擎集成，灵活性强
- 基于 Embeddings 技术实现语义理解，支持跨会话的项目上下文保持

**适用场景**:
- 个人开发者：让 AI 记住项目架构、编码规范和决策历史，无需每次重复解释背景
- 复杂长期项目：维护跨月甚至跨年的项目上下文，特别适合大型代码库或多人协作项目
- AI 工作流优化：自动建立项目知识库，提升 AI 辅助编程的效率和准确性



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,058 |
| 语言 | Java |
| Forks | 15,959 |
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
| Stars | 42,112 |
| 语言 | Python |
| Forks | 5,088 |
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
| Stars | 39,087 |
| 语言 | Python |
| Forks | 6,192 |
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
| Stars | 101,702 |
| 语言 | TypeScript |
| Forks | 12,245 |
| Issues | 979 |
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
| Stars | 59,370 |
| 语言 | JavaScript |
| Forks | 6,414 |
| Issues | 342 |
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
| Stars | 108,316 |
| 语言 | Python |
| Forks | 15,963 |
| Issues | 8 |
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
| Stars | 76,927 |
| 语言 | Python |
| Forks | 10,351 |
| Issues | 208 |
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
| Stars | 52,462 |
| 语言 | TypeScript |
| Forks | 24,250 |
| Issues | 825 |
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
| Stars | 44,075 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,080 |
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
| Stars | 34,647 |
| 语言 | Python |
| Forks | 4,897 |
| Issues | 225 |
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
| Stars | 34,090 |
| 语言 | TypeScript |
| Forks | 3,712 |
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
| Stars | 135,109 |
| 语言 | Python |
| Forks | 19,207 |
| Issues | 341 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面项目，支持 Ollama、OpenAI API 等多种 LLM 后端，具备 RAG 检索增强和 MCP 协议支持，135k+ stars 证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人开发者构建私有化 AI 助手。

**技术亮点**:
- 多后端统一接口：同时支持 Ollama 本地模型和 OpenAI API 等云端服务，提供统一的对话和管理体验
- RAG 检索增强生成：内置文档处理和向量检索能力，可基于私有知识库进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展与外部工具和数据的集成
- 自托管部署：可完全私有化部署，无需依赖第三方服务，保障数据安全与隐私
- 现代化 Web 界面：提供直观的用户界面，支持模型管理、会话历史、多模态交互等功能

**适用场景**:
- 企业私有 AI 助手：需要在内部部署 AI 对话系统，处理敏感业务数据，符合合规要求
- 开发者本地 LLM 开发：使用 Ollama 在本地运行开源大模型，搭配 WebUI 进行快速原型开发和测试
- RAG 应用构建：基于自有文档库构建知识问答系统，支持文档上传、向量化存储和智能检索



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 128,062 |
| 语言 | Python |
| Forks | 19,253 |
| Issues | 7,569 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是由顶级开源AI研究组织打造的成熟AI代理框架，拥有128K+ Stars的社区认可度，支持Claude、ChatGPT等多模型集成，具备强大的代码执行和多Agent协作能力，是构建企业级AI应用和个人智能助手的理想选择。

**技术亮点**:
- 多AI提供商集成：无缝支持Anthropic (Claude)、OpenAI (ChatGPT)等主流大语言模型，提供统一的接口抽象层
- 开源Hermes模型生态：基于Nous Research著名的Hermes系列开源模型开发，具备强大的推理和对话能力
- 代码执行能力：深度集成Claude Code和Codex等代码智能功能，支持自动化编程和代码生成任务
- 模块化Agent架构：采用可扩展的模块化设计，支持自定义工具、插件和工作流，便于二次开发
- 活跃的社区生态：拥有庞大的开源社区支持，持续迭代更新，文档和示例完善

**适用场景**:
- 企业级AI应用开发：构建智能客服、工作流自动化、知识库问答等商业应用系统
- 个人开发者智能助手：开发个人AI助手、代码审查工具、自动文档生成等开发效率提升工具
- AI研究实验：基于成熟的Agent框架进行LLM应用研究、多Agent系统实验和prompt工程测试



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,455 |
| 语言 | JavaScript |
| Forks | 26,584 |
| Issues | 149 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 Claude Code、Cursor 等主流 AI 编程助手设计的性能优化框架，通过 Skills、Memory、Security 等模块显著提升 AI Agent 的任务完成效率，是当前最受欢迎的 AI 代码助手增强工具之一。

**技术亮点**:
- Skills 系统：支持自定义技能扩展，让 AI 助手具备特定领域专业能力
- MCP (Model Context Protocol) 集成：标准化上下文管理协议，提升多工具协作能力
- Memory 记忆管理：持久化上下文记忆，解决长对话中的信息丢失问题
- Security 安全模块：内置代码审查与安全检查机制，保障 AI 生成代码的安全性
- Research-First 开发方法：基于研究的最佳实践优化 AI 输出质量

**适用场景**:
- 企业开发团队：统一管理多个 AI 编程助手，标准化代码质量与安全规范
- 个人开发者：优化 Claude Code/Cursor 等工具的响应效率和任务完成度
- AI Agent 开发：基于 MCP 协议构建多模型协作的智能开发环境



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,922 |
| 语言 | TypeScript |
| Forks | 15,050 |
| Issues | 756 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备且社区活跃的多智能体协作平台，提供了开箱即用的 Agent 团队设计能力和 MCP 协议集成，让开发者能够快速构建企业级 AI 工作流，极大降低了多智能体系统的开发门槛。

**技术亮点**:
- 基于 TypeScript/Next.js 的现代化全栈架构，75K+ Stars 证明其代码质量和工程化水平业界领先
- 原生支持 MCP (Model Context Protocol) 协议，实现 Agent 与外部工具/数据的标准化交互
- 多模型统一接入层，同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大语言模型
- 内置知识库与 RAG 能力，支持 Agent 在特定领域知识上进行推理和问答
- 提供完整的 Agent 生命周期管理，包括设计、部署、监控和协作的全链路能力

**适用场景**:
- 企业级 AI 工作流自动化：构建由多个专业化 Agent 组成的团队，处理复杂的业务流程如客服、工单处理、数据分析等
- 个人开发者快速原型开发：利用现成的 Agent 框架和 MCP 生态快速搭建 AI 应用，降低从零开发的时间成本
- 多模型对比与集成：在一个平台上同时测试和比较不同大语言模型的效果，选择最适合特定场景的模型组合



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,692 |
| 语言 | TypeScript |
| Forks | 6,045 |
| Issues | 50 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个让 Claude Code 拥有长期记忆的插件，通过自动捕获会话内容、AI 压缩和 RAG 检索，解决了 AI 助手中上下文窗口限制的核心痛点，70k+ stars 证明了其在开发者社区的极高认可度。

**技术亮点**:
- 基于 ChromaDB 向量数据库实现语义记忆存储和检索，支持高效的相似度搜索
- 集成 RAG（检索增强生成）技术，将历史上下文智能注入未来会话
- 使用 Claude Agent SDK 进行 AI 驱动的记忆压缩，优化存储效率
- 支持 SQLite 本地存储和 Mem0/OpenMemory 等记忆引擎集成，灵活性强
- 基于 Embeddings 技术实现语义理解，支持跨会话的项目上下文保持

**适用场景**:
- 个人开发者：让 AI 记住项目架构、编码规范和决策历史，无需每次重复解释背景
- 复杂长期项目：维护跨月甚至跨年的项目上下文，特别适合大型代码库或多人协作项目
- AI 工作流优化：自动建立项目知识库，提升 AI 辅助编程的效率和准确性



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,327 |
| 语言 | HTML |
| Forks | 21,056 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有16万+ Stars的顶级开源提示词聚合平台，提供海量精选AI提示词库，支持企业私有化自托管部署保障数据隐私，是个人开发者和企业拥抱AI时代的绝佳工具。

**技术亮点**:
- Next.js + TypeScript全栈架构，提供良好的开发体验和类型安全
- 支持完全自托管部署，企业数据不出本地，完整隐私保护机制
- 多模型支持涵盖ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 社区驱动的提示词贡献机制，持续丰富提示词库
- 现代化响应式前端界面，基于HTML/TypeScript技术栈

**适用场景**:
- AI应用开发：快速获取高质量提示词，加速AI应用开发
- 企业私有化部署：自部署提示词平台确保内部数据安全
- 个人效率提升：收藏整理个性化提示词，提升与AI交互效率



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,925 |
| 语言 | Python |
| Forks | 2,772 |
| Issues | 175 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过"穴居人语言"风格将 token 消耗降低 65%，在保持功能有效性的同时显著节省 LLM 调用成本，51k Stars 证明了其极高的实用价值和社区认可度。

**技术亮点**:
- 采用极简语言压缩策略，将复杂自然语言压缩为穴居人风格的简短表达，显著降低 token 计数
- 专门针对 Claude Code 平台优化，无缝集成作为 Claude Code Skill 使用
- 基于提示工程（Prompt Engineering）技术，通过语言风格转换而非修改模型参数实现成本优化
- 开源实现清晰简单，便于学习和二次开发
- MIT 许可证允许商业使用，降低企业采用门槛

**适用场景**:
- 企业级 LLM 应用成本优化：对于需要频繁调用 Claude API 的企业应用，使用 caveman 风格可大幅降低 token 消耗和 API 成本
- 个人开发者节省预算：个人开发者在使用 Claude Code 时，通过此技能减少 token 使用量，延长免费/付费额度的使用时间
- AI 交互效率提升：在资源受限或网络延迟较高的场景下，减少 token 意味着更快的响应速度和更低的带宽消耗



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,100 |
| 语言 | HTML |
| Forks | 4,984 |
| Issues | 11 |
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
| Stars | 59,370 |
| 语言 | JavaScript |
| Forks | 6,414 |
| Issues | 342 |
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
| Stars | 72,475 |
| 语言 | Python |
| Forks | 9,160 |
| Issues | 404 |
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
| Stars | 55,347 |
| 语言 | TypeScript |
| Forks | 4,489 |
| Issues | 669 |
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
| Stars | 52,462 |
| 语言 | TypeScript |
| Forks | 24,250 |
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
| Stars | 78,793 |
| 语言 | Python |
| Forks | 16,333 |
| Issues | 4,704 |
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
| Stars | 147,597 |
| 语言 | Python |
| Forks | 8,887 |
| Issues | 944 |
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
| Stars | 57,394 |
| 语言 | Python |
| Forks | 6,204 |
| Issues | 564 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,491 |
| 语言 | Go |
| Forks | 15,922 |
| Issues | 3,133 |
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
| Stars | 91,794 |
| 语言 | Jupyter Notebook |
| Forks | 14,149 |
| Issues | 6 |
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
| Stars | 57,723 |
| 语言 | TypeScript |
| Forks | 9,478 |
| Issues | 113 |
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
| Stars | 48,288 |
| 语言 | Rust |
| Forks | 9,666 |
| Issues | 3 |
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
| Stars | 72,958 |
| 语言 | Python |
| Forks | 7,526 |
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
| Stars | 119,213 |
| 语言 | Python |
| Forks | 7,897 |
| Issues | 650 |
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
| Stars | 70,825 |
| 语言 | Python |
| Forks | 8,646 |
| Issues | 996 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 背书的统一大模型微调框架，支持 100+ LLM 和 VLM 的高效微调，通过 LoRA、QLoRA、MOE 等技术大幅降低训练成本，是目前最受欢迎的开源微调解决方案之一。

**技术亮点**:
- 支持 100+ 大语言模型（Llama、Qwen、DeepSeek、Gemma 等）和视觉语言模型的统一微调框架
- 集成多种高效微调技术：LoRA、QLoRA、AdaLoRA、DoRA、GaLore、QLoRA+ 等
- 支持 MOE（混合专家）架构的高效微调
- 集成量化技术（AWQ、GPTQ），显著降低 GPU 显存需求
- 支持 RLHF（DPO/CPO/KTO/ORPO）、Supervised Fine-tuning 等多种训练范式

**适用场景**:
- 企业场景：快速定制化企业专属大模型，降低 AI 应用开发成本，支持私有化部署
- 学术研究：模块化设计便于实验对比不同微调方法，支持多种训练策略
- 个人开发者：低门槛微调开源大模型，通过 WebUI 零代码实现模型定制



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,848 |
| 语言 | Python |
| Forks | 6,684 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是当前最成熟的开源金融数据分析平台，提供统一API接入全球30+金融数据源，支持从股票、加密货币到期权、固定收益的全品类数据覆盖，特别适合需要快速构建量化策略或AI金融应用的开发者，可大幅降低数据获取和处理的技术门槛。

**技术亮点**:
- 统一数据管道：标准化接口整合多个数据源（Yahoo Finance、CoinGecko、FRED等），提供一致的API调用体验
- 全面的金融分析工具集：内置技术指标、蜡烛图分析、期权定价、收益率分析等专业金融计算功能
- AI/ML就绪架构：提供LangChain集成和LLM代理支持，可构建对话式金融分析助手
- 多语言SDK支持：除Python外还提供Terminal、R、Excel等客户端，降低集成成本
- 模块化设计：数据层、分析层、UI层解耦，支持按需扩展和自定义数据源

**适用场景**:
- 量化研究与回测：获取历史市场数据，使用内置分析工具快速验证交易策略，进行因子分析和回测
- 金融数据分析和报告：自动抓取多资产类别数据，生成标准化的市场分析报告和仪表盘
- AI驱动的投资助手：基于LangChain构建对话式金融问答系统，实现自然语言查询市场数据和投资建议



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,327 |
| 语言 | HTML |
| Forks | 21,056 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有16万+ Stars的顶级开源提示词聚合平台，提供海量精选AI提示词库，支持企业私有化自托管部署保障数据隐私，是个人开发者和企业拥抱AI时代的绝佳工具。

**技术亮点**:
- Next.js + TypeScript全栈架构，提供良好的开发体验和类型安全
- 支持完全自托管部署，企业数据不出本地，完整隐私保护机制
- 多模型支持涵盖ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 社区驱动的提示词贡献机制，持续丰富提示词库
- 现代化响应式前端界面，基于HTML/TypeScript技术栈

**适用场景**:
- AI应用开发：快速获取高质量提示词，加速AI应用开发
- 企业私有化部署：自部署提示词平台确保内部数据安全
- 个人效率提升：收藏整理个性化提示词，提升与AI交互效率



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,149 |
| 语言 | Python |
| Forks | 33,076 |
| Issues | 2,338 |
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
| Stars | 78,793 |
| 语言 | Python |
| Forks | 16,333 |
| Issues | 4,704 |
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
| Stars | 110,942 |
| 语言 | Python |
| Forks | 12,941 |
| Issues | 4,012 |
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
| Stars | 99,579 |
| 语言 | Python |
| Forks | 27,636 |
| Issues | 18,556 |
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
| Stars | 91,794 |
| 语言 | Jupyter Notebook |
| Forks | 14,149 |
| Issues | 6 |
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
| Stars | 34,090 |
| 语言 | TypeScript |
| Forks | 3,712 |
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
| Stars | 171,455 |
| 语言 | JavaScript |
| Forks | 26,584 |
| Issues | 149 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 Claude Code、Cursor 等主流 AI 编程助手设计的性能优化框架，通过 Skills、Memory、Security 等模块显著提升 AI Agent 的任务完成效率，是当前最受欢迎的 AI 代码助手增强工具之一。

**技术亮点**:
- Skills 系统：支持自定义技能扩展，让 AI 助手具备特定领域专业能力
- MCP (Model Context Protocol) 集成：标准化上下文管理协议，提升多工具协作能力
- Memory 记忆管理：持久化上下文记忆，解决长对话中的信息丢失问题
- Security 安全模块：内置代码审查与安全检查机制，保障 AI 生成代码的安全性
- Research-First 开发方法：基于研究的最佳实践优化 AI 输出质量

**适用场景**:
- 企业开发团队：统一管理多个 AI 编程助手，标准化代码质量与安全规范
- 个人开发者：优化 Claude Code/Cursor 等工具的响应效率和任务完成度
- AI Agent 开发：基于 MCP 协议构建多模型协作的智能开发环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,988 |
| 语言 | Go |
| Forks | 4,040 |
| Issues | 153 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持文本生成、图像生成、语音合成、目标检测等多模态任务，无需 GPU 即可在各类硬件上运行，非常适合需要本地化部署 AI 能力的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现在 CPU 上高效运行 AI 模型，无需依赖昂贵的 GPU 资源
- 丰富的 API 接口：提供 RESTful API，兼容 OpenAI API 规范，便于现有应用快速集成
- 分布式与去中心化架构：支持 libp2p 协议实现去中心化部署，支持分布式推理
- Go 语言实现：利用 Go 的并发优势和高效性能，确保系统稳定性和高吞吐量

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地环境运行 AI 服务，数据不出本地，满足隐私合规要求
- 边缘计算场景：在资源受限的边缘设备上部署 AI 能力，无需云计算支持，降低延迟和网络依赖
- 快速原型开发：开发者利用兼容 OpenAI 的 API 快速搭建 AI 应用原型，降低开发成本
- 去中心化 AI 应用：基于 libp2p 构建分布式 AI 网络，实现去中心化的模型推理和服务



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,058 |
| 语言 | Java |
| Forks | 15,959 |
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
| Stars | 72,475 |
| 语言 | Python |
| Forks | 9,160 |
| Issues | 404 |
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
| Stars | 55,347 |
| 语言 | TypeScript |
| Forks | 4,489 |
| Issues | 669 |
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
| Stars | 186,389 |
| 语言 | TypeScript |
| Forks | 57,278 |
| Issues | 1,569 |
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
| Stars | 160,060 |
| 语言 | Python |
| Forks | 13,270 |
| Issues | 2,501 |
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
| Stars | 97,818 |
| 语言 | Python |
| Forks | 9,180 |
| Issues | 185 |
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
| Stars | 82,771 |
| 语言 | Python |
| Forks | 9,653 |
| Issues | 277 |
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
| Stars | 184,452 |
| 语言 | TypeScript |
| Forks | 39,606 |
| Issues | 16,936 |
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
| Stars | 94,229 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Forks | 5,843 |
| Issues | 773 |
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
| Stars | 79,931 |
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
| Stars | 77,305 |
| 语言 | Go |
| Forks | 2,804 |
| Issues | 955 |
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
| Stars | 55,347 |
| 语言 | TypeScript |
| Forks | 4,489 |
| Issues | 669 |
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
| Stars | 186,389 |
| 语言 | TypeScript |
| Forks | 57,278 |
| Issues | 1,569 |
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
| Stars | 57,394 |
| 语言 | Python |
| Forks | 6,204 |
| Issues | 564 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,666 |
| 语言 | Go |
| Forks | 10,327 |
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
| Stars | 122,018 |
| 语言 | Go |
| Forks | 42,991 |
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
| Stars | 71,522 |
| 语言 | Go |
| Forks | 18,926 |
| Issues | 3,812 |
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
| Stars | 55,275 |
| 语言 | Go |
| Forks | 6,645 |
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
| Stars | 47,504 |
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
| Stars | 94,229 |
| 语言 | TypeScript |
| Forks | 9,408 |
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
| Stars | 78,067 |
| 语言 | TypeScript |
| Forks | 6,827 |
| Issues | 425 |
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
| Stars | 86,106 |
| 语言 | JavaScript |
| Forks | 7,754 |
| Issues | 730 |
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
| Stars | 70,113 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 324 |
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
| Stars | 62,950 |
| 语言 | Go |
| Forks | 5,953 |
| Issues | 785 |
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
| Stars | 60,839 |
| 语言 | Go |
| Forks | 7,458 |
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
| Stars | 59,321 |
| 语言 | Go |
| Forks | 4,319 |
| Issues | 23 |
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
| Stars | 86,106 |
| 语言 | JavaScript |
| Forks | 7,754 |
| Issues | 730 |
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
| Stars | 63,859 |
| 语言 | Go |
| Forks | 10,370 |
| Issues | 764 |
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
| Stars | 45,988 |
| 语言 | Go |
| Forks | 4,040 |
| Issues | 153 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 引擎，支持文本生成、图像生成、语音合成、目标检测等多模态任务，无需 GPU 即可在各类硬件上运行，非常适合需要本地化部署 AI 能力的企业和个人开发者。

**技术亮点**:
- 多模态模型支持：统一支持 LLM（Llama、Mamba）、图像生成（Stable Diffusion）、语音合成（TTS、MusicGen）、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现在 CPU 上高效运行 AI 模型，无需依赖昂贵的 GPU 资源
- 丰富的 API 接口：提供 RESTful API，兼容 OpenAI API 规范，便于现有应用快速集成
- 分布式与去中心化架构：支持 libp2p 协议实现去中心化部署，支持分布式推理
- Go 语言实现：利用 Go 的并发优势和高效性能，确保系统稳定性和高吞吐量

**适用场景**:
- 私有化 AI 部署：企业或个人需要在本地环境运行 AI 服务，数据不出本地，满足隐私合规要求
- 边缘计算场景：在资源受限的边缘设备上部署 AI 能力，无需云计算支持，降低延迟和网络依赖
- 快速原型开发：开发者利用兼容 OpenAI 的 API 快速搭建 AI 应用原型，降低开发成本
- 去中心化 AI 应用：基于 libp2p 构建分布式 AI 网络，实现去中心化的模型推理和服务



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,818 |
| 语言 | Python |
| Forks | 9,180 |
| Issues | 185 |
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
| Stars | 87,377 |
| 语言 | Python |
| Forks | 33,876 |
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
| Stars | 100,059 |
| 语言 | TypeScript |
| Forks | 27,236 |
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
| Stars | 79,068 |
| 语言 | TypeScript |
| Forks | 5,843 |
| Issues | 773 |
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
| Stars | 68,978 |
| 语言 | JavaScript |
| Forks | 23,216 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,205 |
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
| Stars | 51,835 |
| 语言 | JavaScript |
| Forks | 4,711 |
| Issues | 1,470 |
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
| Stars | 71,999 |
| 语言 | Go |
| Forks | 4,708 |
| Issues | 238 |
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
| Stars | 58,071 |
| 语言 | Go |
| Forks | 3,341 |
| Issues | 18 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,419 |
| 语言 | Go |
| Forks | 8,591 |
| Issues | 681 |
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
| Stars | 101,702 |
| 语言 | TypeScript |
| Forks | 12,245 |
| Issues | 979 |
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
| Stars | 59,370 |
| 语言 | JavaScript |
| Forks | 6,414 |
| Issues | 342 |
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
| Stars | 44,075 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,080 |
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
| Stars | 51,666 |
| 语言 | Go |
| Forks | 10,327 |
| Issues | 242 |
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
| Stars | 161,327 |
| 语言 | HTML |
| Forks | 21,056 |
| Issues | 46 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有16万+ Stars的顶级开源提示词聚合平台，提供海量精选AI提示词库，支持企业私有化自托管部署保障数据隐私，是个人开发者和企业拥抱AI时代的绝佳工具。

**技术亮点**:
- Next.js + TypeScript全栈架构，提供良好的开发体验和类型安全
- 支持完全自托管部署，企业数据不出本地，完整隐私保护机制
- 多模型支持涵盖ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 社区驱动的提示词贡献机制，持续丰富提示词库
- 现代化响应式前端界面，基于HTML/TypeScript技术栈

**适用场景**:
- AI应用开发：快速获取高质量提示词，加速AI应用开发
- 企业私有化部署：自部署提示词平台确保内部数据安全
- 个人效率提升：收藏整理个性化提示词，提升与AI交互效率



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,925 |
| 语言 | Python |
| Forks | 2,772 |
| Issues | 175 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个极具创意的 Claude Code 技能，通过"穴居人语言"风格将 token 消耗降低 65%，在保持功能有效性的同时显著节省 LLM 调用成本，51k Stars 证明了其极高的实用价值和社区认可度。

**技术亮点**:
- 采用极简语言压缩策略，将复杂自然语言压缩为穴居人风格的简短表达，显著降低 token 计数
- 专门针对 Claude Code 平台优化，无缝集成作为 Claude Code Skill 使用
- 基于提示工程（Prompt Engineering）技术，通过语言风格转换而非修改模型参数实现成本优化
- 开源实现清晰简单，便于学习和二次开发
- MIT 许可证允许商业使用，降低企业采用门槛

**适用场景**:
- 企业级 LLM 应用成本优化：对于需要频繁调用 Claude API 的企业应用，使用 caveman 风格可大幅降低 token 消耗和 API 成本
- 个人开发者节省预算：个人开发者在使用 Claude Code 时，通过此技能减少 token 使用量，延长免费/付费额度的使用时间
- AI 交互效率提升：在资源受限或网络延迟较高的场景下，减少 token 意味着更快的响应速度和更低的带宽消耗



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,112 |
| 语言 | Python |
| Forks | 5,088 |
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
| Stars | 57,723 |
| 语言 | TypeScript |
| Forks | 9,478 |
| Issues | 113 |
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
| Stars | 89,837 |
| 语言 | TypeScript |
| Forks | 10,040 |
| Issues | 2,266 |
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
| Stars | 87,759 |
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
| Stars | 171,526 |
| 语言 | Go |
| Forks | 13,179 |
| Issues | 183 |
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
| Stars | 127,647 |
| 语言 | JavaScript |
| Forks | 12,479 |
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
| Stars | 136,509 |
| 语言 | Unknown |
| Forks | 34,102 |
| Issues | 136 |
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
| Stars | 79,365 |
| 语言 | Python |
| Forks | 9,002 |
| Issues | 2,997 |
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
| Stars | 52,184 |
| 语言 | Shell |
| Forks | 4,357 |
| Issues | 7 |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,533 |
| 语言 | Python |
| Forks | 13,438 |
| Issues | 115 |
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
| Stars | 92,093 |
| 语言 | Python |
| Forks | 7,973 |
| Issues | 643 |
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
| Stars | 387,471 |
| 语言 | Python |
| Forks | 66,210 |
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
| Stars | 115,662 |
| 语言 | TypeScript |
| Forks | 6,061 |
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
| Stars | 115,143 |
| 语言 | TypeScript |
| Forks | 8,407 |
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
| Stars | 87,731 |
| 语言 | TypeScript |
| Forks | 12,897 |
| Issues | 488 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,220 |
| 语言 | JavaScript |
| Forks | 5,027 |
| Issues | 21 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。 欢迎参加飞书AI先锋诗活动  https://bytedance.aiforce.cloud/app/app_4jvnd48x7khm1

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,373 |
| 语言 | JavaScript |
| Forks | 10,364 |
| Issues | 135 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,303 |
| 语言 | Go |
| Forks | 10,331 |
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
| Stars | 107,794 |
| 语言 | C++ |
| Forks | 17,660 |
| Issues | 1,557 |
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
| Stars | 63,363 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 35 |
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
| Stars | 34,019 |
| 语言 | TypeScript |
| Forks | 3,864 |
| Issues | 357 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 295,433 |
| 语言 | Python |
| Forks | 27,797 |
| Issues | 18 |
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
| Stars | 86,892 |
| 语言 | Python |
| Forks | 37,402 |
| Issues | 3,731 |
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
| Stars | 443,991 |
| 语言 | TypeScript |
| Forks | 44,437 |
| Issues | 185 |
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
| Stars | 353,996 |
| 语言 | TypeScript |
| Forks | 43,988 |
| Issues | 13 |
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
| Stars | 122,331 |
| 语言 | TypeScript |
| Forks | 13,490 |
| Issues | 3,030 |
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
| Stars | 113,337 |
| 语言 | TypeScript |
| Forks | 8,701 |
| Issues | 1,854 |
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
| Stars | 108,711 |
| 语言 | TypeScript |
| Forks | 13,375 |
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
| Stars | 99,441 |
| 语言 | TypeScript |
| Forks | 5,522 |
| Issues | 694 |
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
| Stars | 97,905 |
| 语言 | TypeScript |
| Forks | 54,590 |
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
| Stars | 94,823 |
| 语言 | TypeScript |
| Forks | 5,213 |
| Issues | 93 |
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
| Stars | 80,336 |
| 语言 | TypeScript |
| Forks | 8,118 |
| Issues | 742 |
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
| Stars | 244,788 |
| 语言 | JavaScript |
| Forks | 51,036 |
| Issues | 1,257 |
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
| Stars | 117,010 |
| 语言 | JavaScript |
| Forks | 35,507 |
| Issues | 2,647 |
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
| Stars | 112,272 |
| 语言 | JavaScript |
| Forks | 36,352 |
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
| Stars | 109,043 |
| 语言 | JavaScript |
| Forks | 11,661 |
| Issues | 166 |
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
| Stars | 98,260 |
| 语言 | JavaScript |
| Forks | 32,655 |
| Issues | 1,537 |
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
| Stars | 95,702 |
| 语言 | JavaScript |
| Forks | 15,439 |
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
| Stars | 86,453 |
| 语言 | JavaScript |
| Forks | 4,897 |
| Issues | 999 |
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
| Stars | 67,682 |
| 语言 | JavaScript |
| Forks | 4,542 |
| Issues | 101 |
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
| Stars | 65,777 |
| 语言 | JavaScript |
| Forks | 9,356 |
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
| Stars | 64,255 |
| 语言 | JavaScript |
| Forks | 4,086 |
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
| Stars | 60,820 |
| 语言 | JavaScript |
| Forks | 5,660 |
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
| Stars | 59,837 |
| 语言 | JavaScript |
| Forks | 20,454 |
| Issues | 91 |
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
| Stars | 57,439 |
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
| Stars | 53,223 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 441 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,724 |
| 语言 | JavaScript |
| Forks | 11,522 |
| Issues | 237 |
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
| Stars | 133,699 |
| 语言 | Go |
| Forks | 19,009 |
| Issues | 10,071 |
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
| Stars | 106,219 |
| 语言 | Go |
| Forks | 15,032 |
| Issues | 40 |
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
| Stars | 87,850 |
| 语言 | Go |
| Forks | 8,251 |
| Issues | 240 |
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
| Stars | 83,366 |
| 语言 | Go |
| Forks | 5,138 |
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
| Stars | 68,592 |
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
| Stars | 56,965 |
| 语言 | Go |
| Forks | 5,067 |
| Issues | 1,175 |
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
| Stars | 51,014 |
| 语言 | Go |
| Forks | 21,891 |
| Issues | 407 |
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
| Stars | 46,861 |
| 语言 | Go |
| Forks | 8,855 |
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
| Stars | 90,046 |
| 语言 | Shell |
| Forks | 14,649 |
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
| Stars | 154,256 |
| 语言 | Python |
| Forks | 11,763 |
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
| Stars | 104,519 |
| 语言 | Unknown |
| Forks | 10,317 |
| Issues | 79 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,590 |
| 语言 | Python |
| Forks | 50,504 |
| Issues | 941 |
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
| Stars | 98,724 |
| 语言 | Python |
| Forks | 12,130 |
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
| Stars | 86,459 |
| 语言 | Python |
| Forks | 7,253 |
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
| Stars | 77,392 |
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
| Stars | 139,256 |
| 语言 | TypeScript |
| Forks | 16,546 |
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
| Stars | 84,883 |
| 语言 | TypeScript |
| Forks | 10,555 |
| Issues | 422 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,343 |
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
| Stars | 148,124 |
| 语言 | JavaScript |
| Forks | 26,701 |
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
| Stars | 71,106 |
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
| Stars | 67,393 |
| 语言 | JavaScript |
| Forks | 11,953 |
| Issues | 558 |
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
| Forks | 9,191 |
| Issues | 3 |
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
| Stars | 61,264 |
| 语言 | JavaScript |
| Forks | 7,153 |
| Issues | 141 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,871 |
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
| Stars | 49,395 |
| 语言 | Go |
| Forks | 7,945 |
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
| Stars | 46,192 |
| 语言 | Go |
| Forks | 3,806 |
| Issues | 81 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
