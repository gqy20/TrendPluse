# 项目发现报告 (2026-05-20)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 125 |
| 去重移除 | 40 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 19 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 19 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 58 |

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
| Stars | 159,438 |
| 语言 | Python |
| Forks | 25,859 |
| Issues | 12,470 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 来自知名AI研究组织NousResearch，拥有超过15万stars的高人气，是一个支持多模型（Claude、GPT等）的开源AI Agent框架，具备企业级应用潜力且代码完全开放可定制。

**技术亮点**:
- 多模型支持：原生集成Anthropic Claude、OpenAI GPT等多种主流大语言模型API
- 开源Agent架构：基于MIT许可证的完整Agent实现，支持任务规划与执行
- Python原生开发：充分利用Python生态系统，便于与现有项目集成
- NousResearch技术支持：源自知名开源AI研究组织，持续更新维护
- 支持Claude Code等高级功能：集成代码执行和多轮对话能力

**适用场景**:
- 企业AI助手开发：构建客服、文档处理、数据分析等企业级AI应用
- 开发者自动化工具：实现代码审查、测试生成、CI/CD流程自动化
- AI研究实验：为AI研究提供可定制的Agent实验平台



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,969 |
| 语言 | Python |
| Forks | 19,730 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完整的开源AI对话界面，支持多种大语言模型后端（Ollama、OpenAI API等），提供RAG检索增强、MCP协议支持等企业级功能，同时支持完全自托管，适合需要私有化部署AI能力的团队和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现灵活切换
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于扩展和集成第三方工具
- 现代化 Web 界面：基于 Python 构建，提供响应式、用户友好的交互体验
- 完全自托管：支持私有化部署，数据本地存储，满足企业安全和隐私需求

**适用场景**:
- 企业内部 AI 助手：利用 RAG 功能构建私有知识库问答系统，处理内部文档和专业知识
- 开发者本地调试：集成 Ollama 本地大模型，快速原型开发和测试 LLM 应用
- 个人 AI 工作站：支持多种模型切换，构建个人化的 AI 写作、编程、翻译等工具链



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,910 |
| 语言 | Python |
| Forks | 9,259 |
| Issues | 3,049 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 项目之一（80k+ stars），创新性地将 RAG 与 Agent 能力深度融合，能够处理复杂的多跳推理和任务编排，为企业构建知识库问答、智能文档分析等应用提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与智能代理能力结合，支持复杂任务的多步骤推理和工具调用
- 深度文档理解：支持 OCR、表格识别、版面分析等多模态内容解析，确保非结构化文档的精准处理
- 精确检索与重排序：采用混合检索策略结合语义重排序模型，提供高质量的上下文召回
- 可视化知识库管理：提供友好的 Web 界面，支持多种数据源接入和知识库配置
- 灵活的 LLM 支持：兼容主流大模型 API，可根据需求选择不同厂商的 LLM

**适用场景**:
- 企业知识库智能问答：构建内部文档检索、规章制度查询、技术文档问答等应用
- 智能客服与文档助手：基于产品手册、帮助文档实现自动化的客户咨询解答
- 专业领域知识管理：适用于法律、医疗、金融等需要精准检索和复杂推理的行业应用



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,726 |
| 语言 | Python |
| Forks | 15,140 |
| Issues | 356 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |

---

TradingAgents 是首个将多智能体架构与 LLM 深度融合的金融交易框架，77,726 Stars 证明了其在 AI 量化领域的标杆地位。该项目解决了传统量化系统缺乏自然语言理解和复杂推理能力的痛点，为金融交易智能化提供了完整的技术解决方案。

**技术亮点**:
- Multi-Agent 协作架构：多个专业智能体分工协作，分别负责数据分析、市场研究、风险评估和交易执行
- LLM 深度集成：利用大语言模型处理非结构化金融数据（新闻、财报、社交媒体），实现智能分析与决策
- 模块化框架设计：高度解耦的架构支持灵活替换 LLM 提供商、自定义交易策略和功能扩展
- 金融专用功能：集成实时行情获取、技术指标计算、风险管理和投资组合优化等交易必备功能
- 开源可定制：Apache 2.0 许可，代码完全开放，支持企业级私有化部署和深度定制

**适用场景**:
- 量化投资研究：策略研发、市场数据分析、因子挖掘和投资组合回测优化
- 自动化交易系统：构建智能交易机器人，实现从数据分析到下单执行的全流程自动化
- 金融机构智能化升级：帮助券商、基金、私募等机构快速构建 AI 驱动的投资研究平台



### firecrawl/firecrawl

**描述**: 🔥 Search, scrape, and clean the web for AI agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 122,300 |
| 语言 | TypeScript |
| Forks | 7,430 |
| Issues | 326 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 代理设计的网页爬取工具，能够将网页搜索、爬取和数据清洗一体化处理，并直接输出 AI 友好的 Markdown 格式，极大简化了大模型数据准备的流程。其 12 万+ Stars 表明它是 AI 数据采集领域的标杆项目。

**技术亮点**:
- 专为 AI 代理场景优化，支持 LLM 直接消费的结构化数据输出
- 内置 HTML 到 Markdown 的高质量转换，确保内容可读性
- 支持全站爬取和增量更新，适合构建大规模数据集
- 提供搜索和爬取双模式，覆盖多种数据采集需求
- TypeScript 实现，类型安全且易于集成到现代前端项目

**适用场景**:
- LLM 训练数据准备：从网页自动提取高质量文本内容
- AI 代理数据供给：为 AI 代理提供实时、准确的网页信息获取能力
- 竞品分析/市场调研：批量爬取和清洗目标网站内容



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,667 |
| 语言 | JavaScript |
| Forks | 29,046 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个全面的 AI Agent 性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Instincts、Memory 和 Security 等核心模块，显著提升 AI 辅助编程的效率和安全性，是现代 AI 开发者的必备工具链。

**技术亮点**:
- 多 Agent 框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- Skills & Instincts 机制：通过预定义技能和本能反应增强 Agent 任务执行能力
- Memory 系统：实现上下文持久化和长期记忆，提升 Agent 状态管理
- Security 模块：内置代码安全检查机制，保障 AI 生成代码的安全性
- MCP 协议集成：支持 Model Context Protocol，实现标准化 Agent 通信

**适用场景**:
- 企业级 AI 开发团队：利用多 Agent 协作和 Memory 系统实现团队知识沉淀和代码审查流程自动化
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 编程能力，自动处理重复性编码任务
- 安全敏感型项目：集成 Security 模块进行实时代码安全扫描，适合金融、医疗等高安全要求的开发场景



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,371 |
| 语言 | Go |
| Forks | 4,089 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 推理解决方案，支持文本、图像、音频、视频等多模态模型运行，46K+ Stars 验证了其成熟度和社区活跃度，特别适合在没有高端 GPU 的情况下实现 AI 能力私有化部署。

**技术亮点**:
- 多模态统一推理引擎：支持 LLMs（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 硬件无关架构：基于 Go 语言优化，无需 NVIDIA GPU 即可运行，支持 CPU 推理和多种硬件加速
- 原生兼容 OpenAI API：提供与 OpenAI API 完全兼容的接口，现有应用无需修改即可迁移
- 去中心化分布式部署：支持 libp2p 协议实现去中心化组网和分布式推理
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的工具调用后端

**适用场景**:
- 个人开发者/小型团队 AI 应用：缺乏 GPU 资源但需要集成 LLM、图像生成等 AI 能力，通过 OpenAI 兼容 API 快速接入
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律文档处理），本地运行模型确保数据不外泄
- 边缘计算/嵌入式 AI：资源受限的物联网设备或边缘服务器，通过轻量化部署实现本地智能推理



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,420 |
| 语言 | TypeScript |
| Forks | 15,234 |
| Issues | 305 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是企业级 AI Agent 编排平台，支持多模型统一接入（MCP/GPT/Claude/DeepSeek/Gemini），提供 7×24 小时 AI 团队自动化运营能力，帮助企业快速构建智能化的多 Agent 协作工作流，适合需要大规模 AI 运营的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供标准化的模型调用接口
- MCP 协议支持：实现 Model Context Protocol 标准，便于扩展工具和集成第三方服务
- 多 Agent 编排调度：支持 Agent 的招聘、排程、汇报机制，实现 7×24 全天候 AI 团队运营
- 知识库管理：内置知识库系统，支持 RAG 增强检索和上下文管理
- TypeScript 全栈架构：类型安全的前后端分离设计，便于二次开发和维护

**适用场景**:
- 企业级 AI 运营中心：构建多 Agent 协作团队，实现客服、审批、分析等业务流程的自动化
- 智能助手平台：集成多种 AI 能力，为用户提供统一入口的智能服务
- 开发者 AI 工作流：利用 MCP 扩展和 Agent 调度能力，构建定制化的 AI 开发辅助工具



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,045 |
| 语言 | TypeScript |
| Forks | 6,644 |
| Issues | 180 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过向量数据库和 RAG 技术实现 AI 代理的长期记忆能力，解决了大模型上下文窗口限制和会话断连后记忆丢失的痛点，拥有 77k+ Stars 验证了其成熟度和社区认可度。

**技术亮点**:
- 基于 ChromaDB 的向量存储实现高效的语义检索，支持 Embeddings 相似度匹配
- 采用 RAG (检索增强生成) 架构，将历史上下文压缩后注入到新会话中
- 支持 SQLite 本地持久化存储，数据完全可控且跨设备同步
- 多代理兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI 代理工具
- 智能压缩算法：使用 AI 自动压缩会话内容，降低存储成本的同时保留关键信息

**适用场景**:
- AI 助手/代理开发：为 AI 代理添加长期记忆能力，提升连续对话体验
- 个人知识管理：打造具备上下文的个人 AI 助手，记住用户偏好、历史任务和项目进展
- 企业级应用：为客户服务机器人或自动化流程添加会话记忆能力，避免重复询问已知信息



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,447 |
| 语言 | Python |
| Forks | 8,718 |
| Issues | 1,016 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,563 |
| 语言 | Python |
| Forks | 10,063 |
| Issues | 129 |
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
| Stars | 54,014 |
| 语言 | HTML |
| Forks | 5,412 |
| Issues | 16 |
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
| Stars | 51,798 |
| 语言 | Python |
| Forks | 6,282 |
| Issues | 114 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,337 |
| 语言 | Java |
| Forks | 16,002 |
| Issues | 23 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,562 |
| 语言 | TypeScript |
| Forks | 6,061 |
| Issues | 558 |
| Topics | agentic-ai, agentic-framework, agentic-rag, agentic-workflow, agents, ai-agent, ai-assistant, ai-coding, ai-skills, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,372 |
| 语言 | JavaScript |
| Forks | 6,526 |
| Issues | 346 |
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
| Stars | 74,270 |
| 语言 | Python |
| Forks | 9,415 |
| Issues | 414 |
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
| Stars | 58,728 |
| 语言 | TypeScript |
| Forks | 4,776 |
| Issues | 537 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,193 |
| 语言 | Python |
| Forks | 6,210 |
| Issues | 85 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,837 |
| 语言 | Python |
| Forks | 10,692 |
| Issues | 229 |
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
| Stars | 52,962 |
| 语言 | TypeScript |
| Forks | 24,363 |
| Issues | 864 |
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
| Stars | 188,884 |
| 语言 | TypeScript |
| Forks | 57,851 |
| Issues | 1,485 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,788 |
| 语言 | JavaScript |
| Forks | 46,133 |
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
| Stars | 148,565 |
| 语言 | Python |
| Forks | 9,067 |
| Issues | 932 |
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
| Stars | 64,883 |
| 语言 | Jupyter Notebook |
| Forks | 21,409 |
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
| Stars | 76,423 |
| 语言 | Rust |
| Forks | 4,966 |
| Issues | 960 |
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
| Stars | 60,892 |
| 语言 | Python |
| Forks | 6,633 |
| Issues | 657 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,248 |
| 语言 | Python |
| Forks | 16,521 |
| Issues | 12 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


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
| Stars | 137,969 |
| 语言 | Python |
| Forks | 19,730 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完整的开源AI对话界面，支持多种大语言模型后端（Ollama、OpenAI API等），提供RAG检索增强、MCP协议支持等企业级功能，同时支持完全自托管，适合需要私有化部署AI能力的团队和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现灵活切换
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于扩展和集成第三方工具
- 现代化 Web 界面：基于 Python 构建，提供响应式、用户友好的交互体验
- 完全自托管：支持私有化部署，数据本地存储，满足企业安全和隐私需求

**适用场景**:
- 企业内部 AI 助手：利用 RAG 功能构建私有知识库问答系统，处理内部文档和专业知识
- 开发者本地调试：集成 Ollama 本地大模型，快速原型开发和测试 LLM 应用
- 个人 AI 工作站：支持多种模型切换，构建个人化的 AI 写作、编程、翻译等工具链



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,910 |
| 语言 | Python |
| Forks | 9,259 |
| Issues | 3,049 |
| Topics | agentic-ai, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-management, llm-apps, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 项目之一（80k+ stars），创新性地将 RAG 与 Agent 能力深度融合，能够处理复杂的多跳推理和任务编排，为企业构建知识库问答、智能文档分析等应用提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 双引擎架构：创新性地将检索增强生成与智能代理能力结合，支持复杂任务的多步骤推理和工具调用
- 深度文档理解：支持 OCR、表格识别、版面分析等多模态内容解析，确保非结构化文档的精准处理
- 精确检索与重排序：采用混合检索策略结合语义重排序模型，提供高质量的上下文召回
- 可视化知识库管理：提供友好的 Web 界面，支持多种数据源接入和知识库配置
- 灵活的 LLM 支持：兼容主流大模型 API，可根据需求选择不同厂商的 LLM

**适用场景**:
- 企业知识库智能问答：构建内部文档检索、规章制度查询、技术文档问答等应用
- 智能客服与文档助手：基于产品手册、帮助文档实现自动化的客户咨询解答
- 专业领域知识管理：适用于法律、医疗、金融等需要精准检索和复杂推理的行业应用



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,420 |
| 语言 | TypeScript |
| Forks | 15,234 |
| Issues | 305 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是企业级 AI Agent 编排平台，支持多模型统一接入（MCP/GPT/Claude/DeepSeek/Gemini），提供 7×24 小时 AI 团队自动化运营能力，帮助企业快速构建智能化的多 Agent 协作工作流，适合需要大规模 AI 运营的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供标准化的模型调用接口
- MCP 协议支持：实现 Model Context Protocol 标准，便于扩展工具和集成第三方服务
- 多 Agent 编排调度：支持 Agent 的招聘、排程、汇报机制，实现 7×24 全天候 AI 团队运营
- 知识库管理：内置知识库系统，支持 RAG 增强检索和上下文管理
- TypeScript 全栈架构：类型安全的前后端分离设计，便于二次开发和维护

**适用场景**:
- 企业级 AI 运营中心：构建多 Agent 协作团队，实现客服、审批、分析等业务流程的自动化
- 智能助手平台：集成多种 AI 能力，为用户提供统一入口的智能服务
- 开发者 AI 工作流：利用 MCP 扩展和 Agent 调度能力，构建定制化的 AI 开发辅助工具



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,045 |
| 语言 | TypeScript |
| Forks | 6,644 |
| Issues | 180 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过向量数据库和 RAG 技术实现 AI 代理的长期记忆能力，解决了大模型上下文窗口限制和会话断连后记忆丢失的痛点，拥有 77k+ Stars 验证了其成熟度和社区认可度。

**技术亮点**:
- 基于 ChromaDB 的向量存储实现高效的语义检索，支持 Embeddings 相似度匹配
- 采用 RAG (检索增强生成) 架构，将历史上下文压缩后注入到新会话中
- 支持 SQLite 本地持久化存储，数据完全可控且跨设备同步
- 多代理兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI 代理工具
- 智能压缩算法：使用 AI 自动压缩会话内容，降低存储成本的同时保留关键信息

**适用场景**:
- AI 助手/代理开发：为 AI 代理添加长期记忆能力，提升连续对话体验
- 个人知识管理：打造具备上下文的个人 AI 助手，记住用户偏好、历史任务和项目进展
- 企业级应用：为客户服务机器人或自动化流程添加会话记忆能力，避免重复询问已知信息



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,798 |
| 语言 | Python |
| Forks | 6,282 |
| Issues | 114 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,337 |
| 语言 | Java |
| Forks | 16,002 |
| Issues | 23 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 102,745 |
| 语言 | TypeScript |
| Forks | 12,489 |
| Issues | 1,029 |
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
| Stars | 60,372 |
| 语言 | JavaScript |
| Forks | 6,526 |
| Issues | 346 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### mindsdb/minds-platform

**描述**: Platform dedicated to building an open foundation for applied Artificial Intelligence, designed for people seeking production-ready AI systems they can truly control, extend and deploy anywhere.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,193 |
| 语言 | Python |
| Forks | 6,210 |
| Issues | 85 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,234 |
| 语言 | Python |
| Forks | 10,461 |
| Issues | 210 |
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
| Stars | 52,962 |
| 语言 | TypeScript |
| Forks | 24,363 |
| Issues | 864 |
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
| Stars | 50,178 |
| 语言 | Python |
| Forks | 5,432 |
| Issues | 260 |
| Topics | antigravity, claude-code, codex, gemini, graphrag, knowledge-graph, leiden, openclaw, rag, skills, tree-sitter |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,382 |
| 语言 | Go |
| Forks | 4,011 |
| Issues | 924 |
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
| Stars | 35,432 |
| 语言 | Python |
| Forks | 5,011 |
| Issues | 233 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,248 |
| 语言 | Python |
| Forks | 16,521 |
| Issues | 12 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 💬 LLM 界面 (19 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,438 |
| 语言 | Python |
| Forks | 25,859 |
| Issues | 12,470 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 来自知名AI研究组织NousResearch，拥有超过15万stars的高人气，是一个支持多模型（Claude、GPT等）的开源AI Agent框架，具备企业级应用潜力且代码完全开放可定制。

**技术亮点**:
- 多模型支持：原生集成Anthropic Claude、OpenAI GPT等多种主流大语言模型API
- 开源Agent架构：基于MIT许可证的完整Agent实现，支持任务规划与执行
- Python原生开发：充分利用Python生态系统，便于与现有项目集成
- NousResearch技术支持：源自知名开源AI研究组织，持续更新维护
- 支持Claude Code等高级功能：集成代码执行和多轮对话能力

**适用场景**:
- 企业AI助手开发：构建客服、文档处理、数据分析等企业级AI应用
- 开发者自动化工具：实现代码审查、测试生成、CI/CD流程自动化
- AI研究实验：为AI研究提供可定制的Agent实验平台



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,969 |
| 语言 | Python |
| Forks | 19,730 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完整的开源AI对话界面，支持多种大语言模型后端（Ollama、OpenAI API等），提供RAG检索增强、MCP协议支持等企业级功能，同时支持完全自托管，适合需要私有化部署AI能力的团队和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现灵活切换
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升回答准确性
- MCP 协议支持：支持 Model Context Protocol，便于扩展和集成第三方工具
- 现代化 Web 界面：基于 Python 构建，提供响应式、用户友好的交互体验
- 完全自托管：支持私有化部署，数据本地存储，满足企业安全和隐私需求

**适用场景**:
- 企业内部 AI 助手：利用 RAG 功能构建私有知识库问答系统，处理内部文档和专业知识
- 开发者本地调试：集成 Ollama 本地大模型，快速原型开发和测试 LLM 应用
- 个人 AI 工作站：支持多种模型切换，构建个人化的 AI 写作、编程、翻译等工具链



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,667 |
| 语言 | JavaScript |
| Forks | 29,046 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个全面的 AI Agent 性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Instincts、Memory 和 Security 等核心模块，显著提升 AI 辅助编程的效率和安全性，是现代 AI 开发者的必备工具链。

**技术亮点**:
- 多 Agent 框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- Skills & Instincts 机制：通过预定义技能和本能反应增强 Agent 任务执行能力
- Memory 系统：实现上下文持久化和长期记忆，提升 Agent 状态管理
- Security 模块：内置代码安全检查机制，保障 AI 生成代码的安全性
- MCP 协议集成：支持 Model Context Protocol，实现标准化 Agent 通信

**适用场景**:
- 企业级 AI 开发团队：利用多 Agent 协作和 Memory 系统实现团队知识沉淀和代码审查流程自动化
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 编程能力，自动处理重复性编码任务
- 安全敏感型项目：集成 Security 模块进行实时代码安全扫描，适合金融、医疗等高安全要求的开发场景



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,749 |
| 语言 | JavaScript |
| Forks | 3,517 |
| Issues | 217 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"穴居人语言风格"这一创意方案，将 LLM 对话的 token 消耗削减 65%，是一个非常实用的 AI 成本优化工具。它证明了通过语言压缩技术可以在保持功能有效性的同时显著降低 API 调用成本，为大规模 LLM 应用提供了经济高效的解决方案。

**技术亮点**:
- 基于简洁语言的 prompt 压缩技术，将复杂表达转化为简化的 caveman 风格语法
- token 优化率达 65%，通过减少冗余词汇实现显著的 API 成本降低
- 集成 Claude Code skill 机制，可作为 AI 编程助手的增强技能使用
- 利用 LLM 对简化指令的理解能力，在语义等效前提下实现语言压缩
- MIT 开源许可，可自由集成到商业项目和个人工具链中

**适用场景**:
- 大规模 LLM 应用场景：需要频繁调用 AI API 的产品和服务，通过 token 压缩显著降低运营成本
- 个人开发者/独立项目：预算有限但需要高效使用 AI 能力的场景，优化资源利用
- 企业级 AI 集成：需要控制 API 支出的团队，可将此作为成本优化策略的一部分
- prompt 工程研究：探索语言压缩与语义保真度的平衡，为更高效的 AI 交互提供参考



### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,420 |
| 语言 | TypeScript |
| Forks | 15,234 |
| Issues | 305 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai, skills |
| 许可证 | Other |

---

LobeHub 是企业级 AI Agent 编排平台，支持多模型统一接入（MCP/GPT/Claude/DeepSeek/Gemini），提供 7×24 小时 AI 团队自动化运营能力，帮助企业快速构建智能化的多 Agent 协作工作流，适合需要大规模 AI 运营的企业和开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供标准化的模型调用接口
- MCP 协议支持：实现 Model Context Protocol 标准，便于扩展工具和集成第三方服务
- 多 Agent 编排调度：支持 Agent 的招聘、排程、汇报机制，实现 7×24 全天候 AI 团队运营
- 知识库管理：内置知识库系统，支持 RAG 增强检索和上下文管理
- TypeScript 全栈架构：类型安全的前后端分离设计，便于二次开发和维护

**适用场景**:
- 企业级 AI 运营中心：构建多 Agent 协作团队，实现客服、审批、分析等业务流程的自动化
- 智能助手平台：集成多种 AI 能力，为用户提供统一入口的智能服务
- 开发者 AI 工作流：利用 MCP 扩展和 Agent 调度能力，构建定制化的 AI 开发辅助工具



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,045 |
| 语言 | TypeScript |
| Forks | 6,644 |
| Issues | 180 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 通过向量数据库和 RAG 技术实现 AI 代理的长期记忆能力，解决了大模型上下文窗口限制和会话断连后记忆丢失的痛点，拥有 77k+ Stars 验证了其成熟度和社区认可度。

**技术亮点**:
- 基于 ChromaDB 的向量存储实现高效的语义检索，支持 Embeddings 相似度匹配
- 采用 RAG (检索增强生成) 架构，将历史上下文压缩后注入到新会话中
- 支持 SQLite 本地持久化存储，数据完全可控且跨设备同步
- 多代理兼容：支持 Claude Code、OpenAI Codex、Gemini、Copilot 等主流 AI 代理工具
- 智能压缩算法：使用 AI 自动压缩会话内容，降低存储成本的同时保留关键信息

**适用场景**:
- AI 助手/代理开发：为 AI 代理添加长期记忆能力，提升连续对话体验
- 个人知识管理：打造具备上下文的个人 AI 助手，记住用户偏好、历史任务和项目进展
- 企业级应用：为客户服务机器人或自动化流程添加会话记忆能力，避免重复询问已知信息



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,588 |
| 语言 | HTML |
| Forks | 21,155 |
| Issues | 48 |
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
| Stars | 61,563 |
| 语言 | Python |
| Forks | 10,063 |
| Issues | 129 |
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
| Stars | 54,014 |
| 语言 | HTML |
| Forks | 5,412 |
| Issues | 16 |
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
| Stars | 60,372 |
| 语言 | JavaScript |
| Forks | 6,526 |
| Issues | 346 |
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
| Stars | 74,270 |
| 语言 | Python |
| Forks | 9,415 |
| Issues | 414 |
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
| Stars | 58,728 |
| 语言 | TypeScript |
| Forks | 4,776 |
| Issues | 537 |
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
| Stars | 52,962 |
| 语言 | TypeScript |
| Forks | 24,363 |
| Issues | 864 |
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
| Stars | 80,574 |
| 语言 | Python |
| Forks | 17,013 |
| Issues | 5,026 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### ChatGPTNextWeb/NextChat

**描述**: ✨ Light and Fast AI Assistant. Support: Web | iOS | MacOS | Android |  Linux | Windows

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,055 |
| 语言 | TypeScript |
| Forks | 59,702 |
| Issues | 825 |
| Topics | calclaude, chatgpt, claude, cross-platform, desktop, fe, gemini, gemini-pro, gemini-server, gemini-ultra, gpt-4o, groq, nextjs, ollama, react, tauri, tauri-app, vercel, webui |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 148,565 |
| 语言 | Python |
| Forks | 9,067 |
| Issues | 932 |
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
| Stars | 60,892 |
| 语言 | Python |
| Forks | 6,633 |
| Issues | 657 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,827 |
| 语言 | Go |
| Forks | 16,197 |
| Issues | 3,257 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
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
| Stars | 124,103 |
| 语言 | Python |
| Forks | 8,418 |
| Issues | 660 |
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
| Stars | 71,447 |
| 语言 | Python |
| Forks | 8,718 |
| Issues | 1,016 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |


### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,844 |
| 语言 | Python |
| Forks | 6,826 |
| Issues | 83 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,588 |
| 语言 | HTML |
| Forks | 21,155 |
| Issues | 48 |
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
| Stars | 95,268 |
| 语言 | Jupyter Notebook |
| Forks | 14,589 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, attention-mechanism, deep-learning, finetuning, from-scratch, generative-ai, gpt, instruction-tuning, language-model, large-language-models, llm, machine-learning, natural-language-processing, pretraining, python, pytorch, tokenizer, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,812 |
| 语言 | Python |
| Forks | 33,279 |
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
| Stars | 80,574 |
| 语言 | Python |
| Forks | 17,013 |
| Issues | 5,026 |
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
| Stars | 113,714 |
| 语言 | Python |
| Forks | 13,313 |
| Issues | 4,035 |
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
| Stars | 100,038 |
| 语言 | Python |
| Forks | 27,830 |
| Issues | 18,486 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (19 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 187,667 |
| 语言 | JavaScript |
| Forks | 29,046 |
| Issues | 2 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

ECC 是一个全面的 AI Agent 性能优化系统，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills、Instincts、Memory 和 Security 等核心模块，显著提升 AI 辅助编程的效率和安全性，是现代 AI 开发者的必备工具链。

**技术亮点**:
- 多 Agent 框架兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具
- Skills & Instincts 机制：通过预定义技能和本能反应增强 Agent 任务执行能力
- Memory 系统：实现上下文持久化和长期记忆，提升 Agent 状态管理
- Security 模块：内置代码安全检查机制，保障 AI 生成代码的安全性
- MCP 协议集成：支持 Model Context Protocol，实现标准化 Agent 通信

**适用场景**:
- 企业级 AI 开发团队：利用多 Agent 协作和 Memory 系统实现团队知识沉淀和代码审查流程自动化
- 个人开发者效率提升：通过 Skills 库快速扩展 AI 编程能力，自动处理重复性编码任务
- 安全敏感型项目：集成 Security 模块进行实时代码安全扫描，适合金融、医疗等高安全要求的开发场景



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,371 |
| 语言 | Go |
| Forks | 4,089 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 推理解决方案，支持文本、图像、音频、视频等多模态模型运行，46K+ Stars 验证了其成熟度和社区活跃度，特别适合在没有高端 GPU 的情况下实现 AI 能力私有化部署。

**技术亮点**:
- 多模态统一推理引擎：支持 LLMs（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 硬件无关架构：基于 Go 语言优化，无需 NVIDIA GPU 即可运行，支持 CPU 推理和多种硬件加速
- 原生兼容 OpenAI API：提供与 OpenAI API 完全兼容的接口，现有应用无需修改即可迁移
- 去中心化分布式部署：支持 libp2p 协议实现去中心化组网和分布式推理
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的工具调用后端

**适用场景**:
- 个人开发者/小型团队 AI 应用：缺乏 GPU 资源但需要集成 LLM、图像生成等 AI 能力，通过 OpenAI 兼容 API 快速接入
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律文档处理），本地运行模型确保数据不外泄
- 边缘计算/嵌入式 AI：资源受限的物联网设备或边缘服务器，通过轻量化部署实现本地智能推理



### jeecgboot/JeecgBoot

**描述**: AI 低代码平台，「低代码 + 零代码」双模式驱动：低代码一键生成前后端代码，零代码 5 分钟搭建系统，AI Skills 一句话画流程、设计表单、生成整套系统。内置 AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领「AI 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，消除 Java 项目 80% 的重复工作，提效而不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,337 |
| 语言 | Java |
| Forks | 16,002 |
| Issues | 23 |
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
| Stars | 74,270 |
| 语言 | Python |
| Forks | 9,415 |
| Issues | 414 |
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
| Stars | 58,728 |
| 语言 | TypeScript |
| Forks | 4,776 |
| Issues | 537 |
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
| Stars | 188,884 |
| 语言 | TypeScript |
| Forks | 57,851 |
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
| Stars | 60,892 |
| 语言 | Python |
| Forks | 6,633 |
| Issues | 657 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,260 |
| 语言 | JavaScript |
| Forks | 4,218 |
| Issues | 1,179 |
| Topics | dark-mode, editor, electron, focus-mode, latex, linux, mac, macos, markdown, marktext, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 436,136 |
| 语言 | Python |
| Forks | 47,805 |
| Issues | 1,357 |
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
| Stars | 163,369 |
| 语言 | Python |
| Forks | 13,713 |
| Issues | 2,509 |
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
| Stars | 98,373 |
| 语言 | Python |
| Forks | 9,323 |
| Issues | 188 |
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
| Stars | 83,533 |
| 语言 | Python |
| Forks | 9,749 |
| Issues | 270 |
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
| Stars | 185,149 |
| 语言 | TypeScript |
| Forks | 40,006 |
| Issues | 17,837 |
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
| Stars | 94,347 |
| 语言 | TypeScript |
| Forks | 9,425 |
| Issues | 262 |
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
| Stars | 79,235 |
| 语言 | TypeScript |
| Forks | 5,883 |
| Issues | 730 |
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
| Stars | 80,380 |
| 语言 | Go |
| Forks | 2,802 |
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
| Stars | 78,207 |
| 语言 | Go |
| Forks | 2,838 |
| Issues | 965 |
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
| Stars | 44,483 |
| 语言 | Go |
| Forks | 8,455 |
| Issues | 1,018 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ⭐ 中优先级


### spf13/cobra

**描述**: A Commander for modern Go CLI interactions

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 43,967 |
| 语言 | Go |
| Forks | 3,146 |
| Issues | 369 |
| Topics | cli, cli-app, cobra, cobra-generator, cobra-library, command, command-cobra, command-line, commandline, go, golang, golang-application, golang-library, posix, posix-compliant-flags, subcommands |
| 许可证 | Apache License 2.0 |


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
| Stars | 58,728 |
| 语言 | TypeScript |
| Forks | 4,776 |
| Issues | 537 |
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
| Stars | 188,884 |
| 语言 | TypeScript |
| Forks | 57,851 |
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
| Stars | 60,892 |
| 语言 | Python |
| Forks | 6,633 |
| Issues | 657 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,718 |
| 语言 | Go |
| Forks | 10,362 |
| Issues | 246 |
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
| Stars | 122,374 |
| 语言 | Go |
| Forks | 43,119 |
| Issues | 2,711 |
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
| Stars | 71,575 |
| 语言 | Go |
| Forks | 18,951 |
| Issues | 3,770 |
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
| Stars | 55,804 |
| 语言 | Go |
| Forks | 6,708 |
| Issues | 2,793 |
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
| Stars | 47,536 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 988 |
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
| Stars | 94,347 |
| 语言 | TypeScript |
| Forks | 9,425 |
| Issues | 262 |
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
| Stars | 79,025 |
| 语言 | TypeScript |
| Forks | 6,920 |
| Issues | 400 |
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
| Stars | 87,031 |
| 语言 | JavaScript |
| Forks | 7,873 |
| Issues | 750 |
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
| Stars | 70,425 |
| 语言 | Go |
| Forks | 1,929 |
| Issues | 330 |
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
| Stars | 63,242 |
| 语言 | Go |
| Forks | 6,003 |
| Issues | 834 |
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
| Stars | 59,820 |
| 语言 | Go |
| Forks | 4,376 |
| Issues | 27 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,968 |
| 语言 | Go |
| Forks | 7,514 |
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
| Stars | 87,031 |
| 语言 | JavaScript |
| Forks | 7,873 |
| Issues | 750 |
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
| Stars | 64,104 |
| 语言 | Go |
| Forks | 10,422 |
| Issues | 773 |
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
| Stars | 46,371 |
| 语言 | Go |
| Forks | 4,089 |
| Issues | 159 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最完整的开源本地 AI 推理解决方案，支持文本、图像、音频、视频等多模态模型运行，46K+ Stars 验证了其成熟度和社区活跃度，特别适合在没有高端 GPU 的情况下实现 AI 能力私有化部署。

**技术亮点**:
- 多模态统一推理引擎：支持 LLMs（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型类型
- 硬件无关架构：基于 Go 语言优化，无需 NVIDIA GPU 即可运行，支持 CPU 推理和多种硬件加速
- 原生兼容 OpenAI API：提供与 OpenAI API 完全兼容的接口，现有应用无需修改即可迁移
- 去中心化分布式部署：支持 libp2p 协议实现去中心化组网和分布式推理
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的工具调用后端

**适用场景**:
- 个人开发者/小型团队 AI 应用：缺乏 GPU 资源但需要集成 LLM、图像生成等 AI 能力，通过 OpenAI 兼容 API 快速接入
- 企业私有化 AI 部署：对数据隐私敏感的场景（如医疗、金融、法律文档处理），本地运行模型确保数据不外泄
- 边缘计算/嵌入式 AI：资源受限的物联网设备或边缘服务器，通过轻量化部署实现本地智能推理



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 436,136 |
| 语言 | Python |
| Forks | 47,805 |
| Issues | 1,357 |
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
| Stars | 98,373 |
| 语言 | Python |
| Forks | 9,323 |
| Issues | 188 |
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
| Stars | 87,512 |
| 语言 | Python |
| Forks | 33,931 |
| Issues | 441 |
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
| Stars | 100,126 |
| 语言 | TypeScript |
| Forks | 27,232 |
| Issues | 1,144 |
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
| Stars | 79,235 |
| 语言 | TypeScript |
| Forks | 5,883 |
| Issues | 730 |
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
| Stars | 69,046 |
| 语言 | JavaScript |
| Forks | 23,392 |
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
| Stars | 55,945 |
| 语言 | JavaScript |
| Forks | 10,188 |
| Issues | 375 |
| Topics | blog, compiler, gatsby, graphql, react, static-site-generator, web-app |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,606 |
| 语言 | Go |
| Forks | 4,750 |
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
| Stars | 58,445 |
| 语言 | Go |
| Forks | 3,385 |
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
| Stars | 88,551 |
| 语言 | Go |
| Forks | 8,609 |
| Issues | 690 |
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
| Stars | 102,745 |
| 语言 | TypeScript |
| Forks | 12,489 |
| Issues | 1,029 |
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
| Stars | 60,372 |
| 语言 | JavaScript |
| Forks | 6,526 |
| Issues | 346 |
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
| Stars | 44,382 |
| 语言 | Go |
| Forks | 4,011 |
| Issues | 924 |
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
| Stars | 51,718 |
| 语言 | Go |
| Forks | 10,362 |
| Issues | 246 |
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
| Stars | 62,749 |
| 语言 | JavaScript |
| Forks | 3,517 |
| Issues | 217 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这个项目通过"穴居人语言风格"这一创意方案，将 LLM 对话的 token 消耗削减 65%，是一个非常实用的 AI 成本优化工具。它证明了通过语言压缩技术可以在保持功能有效性的同时显著降低 API 调用成本，为大规模 LLM 应用提供了经济高效的解决方案。

**技术亮点**:
- 基于简洁语言的 prompt 压缩技术，将复杂表达转化为简化的 caveman 风格语法
- token 优化率达 65%，通过减少冗余词汇实现显著的 API 成本降低
- 集成 Claude Code skill 机制，可作为 AI 编程助手的增强技能使用
- 利用 LLM 对简化指令的理解能力，在语义等效前提下实现语言压缩
- MIT 开源许可，可自由集成到商业项目和个人工具链中

**适用场景**:
- 大规模 LLM 应用场景：需要频繁调用 AI API 的产品和服务，通过 token 压缩显著降低运营成本
- 个人开发者/独立项目：预算有限但需要高效使用 AI 能力的场景，优化资源利用
- 企业级 AI 集成：需要控制 API 支出的团队，可将此作为成本优化策略的一部分
- prompt 工程研究：探索语言压缩与语义保真度的平衡，为更高效的 AI 交互提供参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 162,588 |
| 语言 | HTML |
| Forks | 21,155 |
| Issues | 48 |
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
| Stars | 61,563 |
| 语言 | Python |
| Forks | 10,063 |
| Issues | 129 |
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
| Stars | 51,798 |
| 语言 | Python |
| Forks | 6,282 |
| Issues | 114 |
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
| Stars | 90,005 |
| 语言 | TypeScript |
| Forks | 10,070 |
| Issues | 2,115 |
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
| Stars | 88,174 |
| 语言 | TypeScript |
| Forks | 8,995 |
| Issues | 1,666 |
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
| Stars | 127,873 |
| 语言 | JavaScript |
| Forks | 12,486 |
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
| Stars | 173,163 |
| 语言 | Go |
| Forks | 13,236 |
| Issues | 186 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (58 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,936 |
| 语言 | Unknown |
| Forks | 34,386 |
| Issues | 145 |
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
| Stars | 96,776 |
| 语言 | Shell |
| Forks | 8,535 |
| Issues | 31 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,042 |
| 语言 | Python |
| Forks | 9,161 |
| Issues | 428 |
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
| Stars | 93,203 |
| 语言 | Python |
| Forks | 13,568 |
| Issues | 119 |
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
| Stars | 388,636 |
| 语言 | Python |
| Forks | 66,318 |
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
| Stars | 119,623 |
| 语言 | TypeScript |
| Forks | 8,712 |
| Issues | 340 |
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
| Stars | 116,371 |
| 语言 | TypeScript |
| Forks | 6,152 |
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
| Stars | 99,984 |
| 语言 | TypeScript |
| Forks | 14,888 |
| Issues | 553 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,318 |
| 语言 | JavaScript |
| Forks | 5,377 |
| Issues | 100 |
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
| Stars | 48,438 |
| 语言 | Go |
| Forks | 10,351 |
| Issues | 1,904 |
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
| Stars | 111,795 |
| 语言 | C++ |
| Forks | 18,500 |
| Issues | 1,710 |
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
| Stars | 63,255 |
| 语言 | Python |
| Forks | 1,672 |
| Issues | 36 |
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
| Stars | 39,313 |
| 语言 | TypeScript |
| Forks | 4,494 |
| Issues | 315 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 298,709 |
| 语言 | Python |
| Forks | 27,941 |
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
| Stars | 221,255 |
| 语言 | Python |
| Forks | 50,661 |
| Issues | 918 |
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
| Stars | 87,153 |
| 语言 | Python |
| Forks | 37,539 |
| Issues | 4,229 |
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
| Stars | 77,664 |
| 语言 | Python |
| Forks | 45,086 |
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
| Stars | 445,188 |
| 语言 | TypeScript |
| Forks | 44,642 |
| Issues | 180 |
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
| Stars | 355,137 |
| 语言 | TypeScript |
| Forks | 44,090 |
| Issues | 18 |
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
| Stars | 123,705 |
| 语言 | TypeScript |
| Forks | 13,720 |
| Issues | 3,075 |
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
| Stars | 114,755 |
| 语言 | TypeScript |
| Forks | 8,854 |
| Issues | 1,933 |
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
| Stars | 108,919 |
| 语言 | TypeScript |
| Forks | 13,405 |
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
| Stars | 101,180 |
| 语言 | TypeScript |
| Forks | 5,652 |
| Issues | 660 |
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
| Stars | 98,091 |
| 语言 | TypeScript |
| Forks | 54,601 |
| Issues | 1,375 |
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
| Stars | 95,074 |
| 语言 | TypeScript |
| Forks | 5,256 |
| Issues | 92 |
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
| Stars | 85,995 |
| 语言 | TypeScript |
| Forks | 10,769 |
| Issues | 496 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,457 |
| 语言 | TypeScript |
| Forks | 7,608 |
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
| Stars | 80,738 |
| 语言 | TypeScript |
| Forks | 8,198 |
| Issues | 739 |
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
| Stars | 245,144 |
| 语言 | JavaScript |
| Forks | 51,089 |
| Issues | 1,303 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 195,976 |
| 语言 | JavaScript |
| Forks | 31,065 |
| Issues | 402 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,309 |
| 语言 | JavaScript |
| Forks | 35,575 |
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
| Stars | 112,579 |
| 语言 | JavaScript |
| Forks | 36,377 |
| Issues | 457 |
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
| Stars | 109,069 |
| 语言 | JavaScript |
| Forks | 11,709 |
| Issues | 158 |
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
| Stars | 98,361 |
| 语言 | JavaScript |
| Forks | 32,627 |
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
| Stars | 95,780 |
| 语言 | JavaScript |
| Forks | 15,500 |
| Issues | 63 |
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
| Stars | 86,607 |
| 语言 | JavaScript |
| Forks | 4,917 |
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
| Forks | 9,354 |
| Issues | 193 |
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
| Stars | 64,818 |
| 语言 | JavaScript |
| Forks | 4,117 |
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
| Stars | 61,202 |
| 语言 | JavaScript |
| Forks | 5,676 |
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
| Stars | 59,843 |
| 语言 | JavaScript |
| Forks | 20,428 |
| Issues | 92 |
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
| Stars | 57,451 |
| 语言 | JavaScript |
| Forks | 12,303 |
| Issues | 29 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,562 |
| 语言 | JavaScript |
| Forks | 11,639 |
| Issues | 258 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### mozilla/pdf.js

**描述**: PDF Reader in JavaScript

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,350 |
| 语言 | JavaScript |
| Forks | 10,618 |
| Issues | 454 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,988 |
| 语言 | Go |
| Forks | 19,034 |
| Issues | 10,089 |
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
| Stars | 106,690 |
| 语言 | Go |
| Forks | 15,048 |
| Issues | 47 |
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
| Stars | 88,173 |
| 语言 | Go |
| Forks | 8,264 |
| Issues | 231 |
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
| Stars | 84,238 |
| 语言 | Go |
| Forks | 5,198 |
| Issues | 388 |
| Topics | go, p2p, peer-to-peer, synchronization |
| 许可证 | Mozilla Public License 2.0 |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,284 |
| 语言 | Go |
| Forks | 5,103 |
| Issues | 1,183 |
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
| Stars | 51,054 |
| 语言 | Go |
| Forks | 21,916 |
| Issues | 395 |
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
| Stars | 49,505 |
| 语言 | Go |
| Forks | 7,939 |
| Issues | 564 |
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
| Stars | 140,548 |
| 语言 | Unknown |
| Forks | 14,426 |
| Issues | 96 |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,826 |
| 语言 | Python |
| Forks | 16,977 |
| Issues | 27 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,246 |
| 语言 | JavaScript |
| Forks | 16,805 |
| Issues | 898 |
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
| Stars | 68,728 |
| 语言 | JavaScript |
| Forks | 4,627 |
| Issues | 106 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,449 |
| 语言 | JavaScript |
| Forks | 9,188 |
| Issues | 4 |
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
| Stars | 61,236 |
| 语言 | JavaScript |
| Forks | 7,160 |
| Issues | 143 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


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
| Forks | 8,848 |
| Issues | 17 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 157,861 |
| 语言 | Python |
| Forks | 12,015 |
| Issues | 382 |
| Topics | awesome, github, hellogithub, python |
