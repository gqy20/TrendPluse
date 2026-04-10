# 项目发现报告 (2026-04-10)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 129 |
| 去重移除 | 30 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 10 |
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
| Stars | 131,136 |
| 语言 | Python |
| Forks | 18,592 |
| Issues | 340 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面解决方案，支持 Ollama、OpenAI API 等多种后端，Stars 超 13 万证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现统一的 AI 接口管理
- RAG 检索增强生成：内置文档检索和知识库功能，支持基于私有数据的问答
- MCP (Model Context Protocol) 支持：支持模型上下文协议，便于扩展和集成
- 自托管部署：可完全私有化部署，数据不出本地，满足企业安全和隐私合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、多语言等功能

**适用场景**:
- 企业 AI 私有化部署：企业可在自有服务器上部署 AI 助手，保护敏感数据，满足合规要求
- 研究人员与开发者：统一管理多个 LLM 模型，方便进行实验对比和 API 集成开发
- 个人知识助手：利用 RAG 功能构建基于个人文档库的专业知识问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,688 |
| 语言 | Python |
| Forks | 8,739 |
| Issues | 3,226 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，Stars 数高达 77k+，它将深度文档理解与 Agent 能力完美融合，为 LLM 应用提供了高质量的上下文检索层，是企业构建知识库问答、智能文档分析和 AI 工作流的理想选择。

**技术亮点**:
- 深度文档理解引擎：支持 OCR、表格识别、复杂布局分析，能从 PDF、Word、图片等多模态文档中精准提取结构化信息
- GraphRAG 知识图谱检索：结合知识图谱技术实现更智能的语义检索，提升复杂问答场景的准确性
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于与各类 AI 工具和平台集成
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和对比
- Agent 工作流编排：内置 deep-research 等高级 Agent 能力，支持复杂的多步骤推理和研究任务

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档检索等业务场景
- 智能文档处理与分析：自动处理大量非结构化文档，提取关键信息并生成摘要或答案
- Deep Research 深度研究：支持复杂问题的多步骤研究工作流，用于市场调研、竞品分析等场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 106,985 |
| 语言 | TypeScript |
| Forks | 6,915 |
| Issues | 263 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的网页数据抓取工具，支持将复杂网页转换为 LLM 友好的 Markdown 格式，拥有超过 10 万星的高人气，是构建 AI agents 和数据管道的首选解决方案。

**技术亮点**:
- 专为 AI/LLM 应用优化：直接输出 Markdown、HTML 等 AI 模型友好的数据格式，减少数据处理环节
- 智能网页解析：支持动态渲染页面、JavaScript 渲染内容和复杂网站结构抓取
- 多格式数据提取：提供网页内容、链接、元数据、结构化数据等多种提取模式
- 开发者友好的 API 设计：TypeScript 开发，简洁易用的 SDK，支持快速集成到现有系统
- 批量处理能力：支持网站地图爬取、批量 URL 处理，适合大规模数据采集场景

**适用场景**:
- AI Agent 数据获取：为 AI agents 提供实时、准确的网页数据，作为决策和问答的知识来源
- LLM 训练数据准备：批量抓取并转换为 Markdown 格式，用于构建训练数据集或 RAG 应用
- 竞品分析系统：自动化采集多个网站的产品信息、价格、评论等数据
- 内容聚合平台：新闻聚合、知识库构建、内容监控等需要大规模网页采集的场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,929 |
| 语言 | JavaScript |
| Forks | 23,198 |
| Issues | 58 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有 149,929 Stars 的热门项目，为多种主流 AI 编码助手提供统一的能力扩展框架，涵盖 Skills 技能、Instincts 本能、Memory 记忆和 Security 安全机制，能显著提升 AI 代理的响应速度和任务完成质量。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供一致的扩展接口
- MCP 协议深度集成：实现标准化的上下文管理和工具调用，提升 AI 代理的互操作性
- 分层能力架构：通过 Skills、Instincts、Memory 三层设计灵活扩展 AI 代理能力
- 安全优先设计：内置 Security 机制确保 AI 代理操作的合规性和数据安全
- 研究驱动开发：采用 Research-first 方法论持续优化 AI 代理推理效率

**适用场景**:
- 企业级 AI 开发平台：团队需要统一管理多个 AI 编码助手的能力扩展和安全策略
- AI 代理开发者：构建、测试和优化自定义 AI 代理系统，研究代理性能瓶颈
- 个人开发者效率提升：通过自定义 Skills 和 Memory 扩展打造个人专属的 AI 编程助手



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,207 |
| 语言 | Go |
| Forks | 3,906 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型类型，无需 GPU 即可在普通硬件上运行，为企业提供了一种经济高效的私有化 AI 部署方案，同时让个人开发者零成本构建 AI 应用。

**技术亮点**:
- 多模态模型支持：统一支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频处理（TTS/MusicGen）、目标检测等多种任务
- 零硬件门槛：采用 Go 语言优化，可在 CPU 环境下运行，无需昂贵 GPU，降低 AI 部署成本
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零改动迁移至本地部署
- 分布式架构：支持 libp2p 去中心化组网，便于构建分布式 AI 推理网络
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的本地工具引擎使用

**适用场景**:
- 企业私有化 AI 部署：金融、医疗、政务等对数据隐私要求严格的行业，需本地化处理敏感数据
- 离线/边缘计算场景：物联网设备、远程工作站等无网络或网络受限环境下的 AI 推理
- 开发者快速原型验证：个人开发者或团队在没有云服务预算的情况下，快速搭建 AI 功能演示或 MVP 产品



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,013 |
| 语言 | TypeScript |
| Forks | 14,891 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 协作平台，支持多 Agent 团队协作和编排，拥有 75K+ Stars 的成熟社区，集成 OpenAI/Claude/DeepSeek/Gemini 等主流大模型，并提供 MCP 协议支持，是构建企业级 AI Agent 应用的优秀选择。

**技术亮点**:
- 多 Agent 协作架构 - 支持多个 Agent 协同工作，实现复杂任务的分工与协作
- 多模型集成 - 支持 OpenAI GPT、Claude、DeepSeek、GitHub Copilot 等多种 AI 模型
- MCP 协议支持 - 深度集成 Model Context Protocol，实现标准化的 Agent 上下文管理
- Agent Harness 框架 - 提供完整的 Agent 生命周期管理和编排能力
- TypeScript/React 技术栈 - 类型安全的现代前端架构，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流自动化 - 构建多 Agent 协作的业务流程，如客服自动化、文档处理、数据分析等
- AI 应用快速开发 - 使用 Agent Harness 框架快速构建和部署 AI 应用，减少从零开发的时间成本
- 个人 AI 助手搭建 - 集成多种 AI 模型打造统一的个人 AI 工作站，支持知识库管理和智能对话



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,877 |
| 语言 | Python |
| Forks | 8,524 |
| Issues | 964 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的开源 LLM 微调框架，支持 100+ 主流大模型的高效微调，提供 LoRA、QLoRA、RLHF 等多种低成本训练方案，并获得 ACL 2024 学术认可，特别适合需要快速适配垂类场景的企业和研究者。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 统一微调，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型系列
- 集成 LoRA、QLoRA、Adapter、Prefix-tuning 等多种 PEFT 高效微调方法，大幅降低显存占用
- 支持 INT4/INT8 量化训练，可在消费级 GPU 上微调百亿参数模型
- 内置 SFT、DPO、PPO 等多种训练范式，覆盖从监督学习到强化学习的完整流程
- 提供 Web UI 和 CLI 工具，训练过程可视化监控，开箱即用

**适用场景**:
- 企业私有化部署：快速将开源大模型微调适配到金融、医疗、法律等垂直领域，打造专属 AI 助手
- 学术研究与实验：研究人员可便捷对比不同微调方法、模型架构的效果，加速论文实验迭代
- 个人开发者定制：利用 QLoRA 在单卡消费级显卡上微调小模型，降低 LLM 应用开发门槛



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,360 |
| 语言 | Python |
| Forks | 6,645 |
| Issues | 2,781 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,326 |
| 语言 | TypeScript |
| Forks | 8,373 |
| Issues | 72 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,427 |
| 语言 | TypeScript |
| Forks | 3,662 |
| Issues | 167 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,953 |
| 语言 | Python |
| Forks | 9,886 |
| Issues | 358 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,803 |
| 语言 | Java |
| Forks | 15,892 |
| Issues | 43 |
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
| Stars | 38,944 |
| 语言 | Python |
| Forks | 6,181 |
| Issues | 79 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,696 |
| 语言 | TypeScript |
| Forks | 3,643 |
| Issues | 289 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,037 |
| 语言 | JavaScript |
| Forks | 6,273 |
| Issues | 318 |
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
| Stars | 70,979 |
| 语言 | Python |
| Forks | 8,903 |
| Issues | 394 |
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
| Stars | 50,316 |
| 语言 | TypeScript |
| Forks | 4,013 |
| Issues | 482 |
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
| Stars | 87,018 |
| 语言 | Python |
| Forks | 10,035 |
| Issues | 237 |
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
| Stars | 51,751 |
| 语言 | TypeScript |
| Forks | 24,101 |
| Issues | 803 |
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
| Stars | 183,446 |
| 语言 | TypeScript |
| Forks | 56,656 |
| Issues | 1,462 |
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
| Stars | 154,816 |
| 语言 | Java |
| Forks | 46,151 |
| Issues | 66 |
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
| Stars | 146,784 |
| 语言 | Python |
| Forks | 8,745 |
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
| Stars | 56,361 |
| 语言 | Jupyter Notebook |
| Forks | 19,494 |
| Issues | 28 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,108 |
| 语言 | MDX |
| Forks | 7,880 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 35,161 |
| 语言 | Python |
| Forks | 4,120 |
| Issues | 91 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,985 |
| 语言 | Python |
| Forks | 2,125 |
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
| Stars | 33,376 |
| 语言 | Jupyter Notebook |
| Forks | 5,519 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,014 |
| 语言 | Python |
| Forks | 15,316 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,407 |
| 语言 | Rust |
| Forks | 2,676 |
| Issues | 490 |
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
| Stars | 131,136 |
| 语言 | Python |
| Forks | 18,592 |
| Issues | 340 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面解决方案，支持 Ollama、OpenAI API 等多种后端，Stars 超 13 万证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现统一的 AI 接口管理
- RAG 检索增强生成：内置文档检索和知识库功能，支持基于私有数据的问答
- MCP (Model Context Protocol) 支持：支持模型上下文协议，便于扩展和集成
- 自托管部署：可完全私有化部署，数据不出本地，满足企业安全和隐私合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、多语言等功能

**适用场景**:
- 企业 AI 私有化部署：企业可在自有服务器上部署 AI 助手，保护敏感数据，满足合规要求
- 研究人员与开发者：统一管理多个 LLM 模型，方便进行实验对比和 API 集成开发
- 个人知识助手：利用 RAG 功能构建基于个人文档库的专业知识问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,688 |
| 语言 | Python |
| Forks | 8,739 |
| Issues | 3,226 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，Stars 数高达 77k+，它将深度文档理解与 Agent 能力完美融合，为 LLM 应用提供了高质量的上下文检索层，是企业构建知识库问答、智能文档分析和 AI 工作流的理想选择。

**技术亮点**:
- 深度文档理解引擎：支持 OCR、表格识别、复杂布局分析，能从 PDF、Word、图片等多模态文档中精准提取结构化信息
- GraphRAG 知识图谱检索：结合知识图谱技术实现更智能的语义检索，提升复杂问答场景的准确性
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于与各类 AI 工具和平台集成
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和对比
- Agent 工作流编排：内置 deep-research 等高级 Agent 能力，支持复杂的多步骤推理和研究任务

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档检索等业务场景
- 智能文档处理与分析：自动处理大量非结构化文档，提取关键信息并生成摘要或答案
- Deep Research 深度研究：支持复杂问题的多步骤研究工作流，用于市场调研、竞品分析等场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,013 |
| 语言 | TypeScript |
| Forks | 14,891 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 协作平台，支持多 Agent 团队协作和编排，拥有 75K+ Stars 的成熟社区，集成 OpenAI/Claude/DeepSeek/Gemini 等主流大模型，并提供 MCP 协议支持，是构建企业级 AI Agent 应用的优秀选择。

**技术亮点**:
- 多 Agent 协作架构 - 支持多个 Agent 协同工作，实现复杂任务的分工与协作
- 多模型集成 - 支持 OpenAI GPT、Claude、DeepSeek、GitHub Copilot 等多种 AI 模型
- MCP 协议支持 - 深度集成 Model Context Protocol，实现标准化的 Agent 上下文管理
- Agent Harness 框架 - 提供完整的 Agent 生命周期管理和编排能力
- TypeScript/React 技术栈 - 类型安全的现代前端架构，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流自动化 - 构建多 Agent 协作的业务流程，如客服自动化、文档处理、数据分析等
- AI 应用快速开发 - 使用 Agent Harness 框架快速构建和部署 AI 应用，减少从零开发的时间成本
- 个人 AI 助手搭建 - 集成多种 AI 模型打造统一的个人 AI 工作站，支持知识库管理和智能对话



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,427 |
| 语言 | TypeScript |
| Forks | 3,662 |
| Issues | 167 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,803 |
| 语言 | Java |
| Forks | 15,892 |
| Issues | 43 |
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
| Stars | 38,944 |
| 语言 | Python |
| Forks | 6,181 |
| Issues | 79 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,696 |
| 语言 | TypeScript |
| Forks | 3,643 |
| Issues | 289 |
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
| Stars | 100,609 |
| 语言 | TypeScript |
| Forks | 12,033 |
| Issues | 982 |
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
| Stars | 58,037 |
| 语言 | JavaScript |
| Forks | 6,273 |
| Issues | 318 |
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
| Stars | 75,329 |
| 语言 | Python |
| Forks | 10,229 |
| Issues | 244 |
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
| Stars | 51,751 |
| 语言 | TypeScript |
| Forks | 24,101 |
| Issues | 803 |
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
| Stars | 43,718 |
| 语言 | Go |
| Forks | 3,947 |
| Issues | 1,156 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,108 |
| 语言 | MDX |
| Forks | 7,880 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 35,161 |
| 语言 | Python |
| Forks | 4,120 |
| Issues | 91 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,985 |
| 语言 | Python |
| Forks | 2,125 |
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
| Stars | 33,376 |
| 语言 | Jupyter Notebook |
| Forks | 5,519 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,014 |
| 语言 | Python |
| Forks | 15,316 |
| Issues | 9 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


## 💬 LLM 界面 (25 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 131,136 |
| 语言 | Python |
| Forks | 18,592 |
| Issues | 340 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 LLM 界面解决方案，支持 Ollama、OpenAI API 等多种后端，Stars 超 13 万证明了其成熟度和社区认可度，特别适合需要自托管、保护数据隐私的企业和个人用户。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API 等云端服务，实现统一的 AI 接口管理
- RAG 检索增强生成：内置文档检索和知识库功能，支持基于私有数据的问答
- MCP (Model Context Protocol) 支持：支持模型上下文协议，便于扩展和集成
- 自托管部署：可完全私有化部署，数据不出本地，满足企业安全和隐私合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、多语言等功能

**适用场景**:
- 企业 AI 私有化部署：企业可在自有服务器上部署 AI 助手，保护敏感数据，满足合规要求
- 研究人员与开发者：统一管理多个 LLM 模型，方便进行实验对比和 API 集成开发
- 个人知识助手：利用 RAG 功能构建基于个人文档库的专业知识问答系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,688 |
| 语言 | Python |
| Forks | 8,739 |
| Issues | 3,226 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 引擎之一，Stars 数高达 77k+，它将深度文档理解与 Agent 能力完美融合，为 LLM 应用提供了高质量的上下文检索层，是企业构建知识库问答、智能文档分析和 AI 工作流的理想选择。

**技术亮点**:
- 深度文档理解引擎：支持 OCR、表格识别、复杂布局分析，能从 PDF、Word、图片等多模态文档中精准提取结构化信息
- GraphRAG 知识图谱检索：结合知识图谱技术实现更智能的语义检索，提升复杂问答场景的准确性
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于与各类 AI 工具和平台集成
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种大模型，可灵活切换和对比
- Agent 工作流编排：内置 deep-research 等高级 Agent 能力，支持复杂的多步骤推理和研究任务

**适用场景**:
- 企业级知识库问答系统：构建私有化知识库，支持合同分析、政策查询、技术文档检索等业务场景
- 智能文档处理与分析：自动处理大量非结构化文档，提取关键信息并生成摘要或答案
- Deep Research 深度研究：支持复杂问题的多步骤研究工作流，用于市场调研、竞品分析等场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,929 |
| 语言 | JavaScript |
| Forks | 23,198 |
| Issues | 58 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有 149,929 Stars 的热门项目，为多种主流 AI 编码助手提供统一的能力扩展框架，涵盖 Skills 技能、Instincts 本能、Memory 记忆和 Security 安全机制，能显著提升 AI 代理的响应速度和任务完成质量。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供一致的扩展接口
- MCP 协议深度集成：实现标准化的上下文管理和工具调用，提升 AI 代理的互操作性
- 分层能力架构：通过 Skills、Instincts、Memory 三层设计灵活扩展 AI 代理能力
- 安全优先设计：内置 Security 机制确保 AI 代理操作的合规性和数据安全
- 研究驱动开发：采用 Research-first 方法论持续优化 AI 代理推理效率

**适用场景**:
- 企业级 AI 开发平台：团队需要统一管理多个 AI 编码助手的能力扩展和安全策略
- AI 代理开发者：构建、测试和优化自定义 AI 代理系统，研究代理性能瓶颈
- 个人开发者效率提升：通过自定义 Skills 和 Memory 扩展打造个人专属的 AI 编程助手



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,013 |
| 语言 | TypeScript |
| Forks | 14,891 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个生产级的 AI Agent 协作平台，支持多 Agent 团队协作和编排，拥有 75K+ Stars 的成熟社区，集成 OpenAI/Claude/DeepSeek/Gemini 等主流大模型，并提供 MCP 协议支持，是构建企业级 AI Agent 应用的优秀选择。

**技术亮点**:
- 多 Agent 协作架构 - 支持多个 Agent 协同工作，实现复杂任务的分工与协作
- 多模型集成 - 支持 OpenAI GPT、Claude、DeepSeek、GitHub Copilot 等多种 AI 模型
- MCP 协议支持 - 深度集成 Model Context Protocol，实现标准化的 Agent 上下文管理
- Agent Harness 框架 - 提供完整的 Agent 生命周期管理和编排能力
- TypeScript/React 技术栈 - 类型安全的现代前端架构，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流自动化 - 构建多 Agent 协作的业务流程，如客服自动化、文档处理、数据分析等
- AI 应用快速开发 - 使用 Agent Harness 框架快速构建和部署 AI 应用，减少从零开发的时间成本
- 个人 AI 助手搭建 - 集成多种 AI 模型打造统一的个人 AI 工作站，支持知识库管理和智能对话



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,139 |
| 语言 | HTML |
| Forks | 20,843 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最大的开源提示词社区项目，拥有超过15万星标，支持多平台LLM集成，提供自托管能力，是个人开发者和企业构建私有提示词管理系统的最佳参考和直接使用方案。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态导出
- 多 LLM 平台支持（ChatGPT/Claude/Gemini/GPT-4），统一提示词格式转换
- 开源可自托管，完整隐私保护，适合企业内网部署
- 社区驱动的提示词贡献机制，包含提示词验证和分类系统
- 提供提示词导入/导出功能，支持 Chrome 扩展集成

**适用场景**:
- 个人用户：发现和收藏高质量 AI 提示词，提升 GPT/Claude 等工具的使用效率
- 企业团队：自托管部署私有提示词库，保护内部知识资产，避免数据外泄
- AI 开发者：参考提示词工程最佳实践，构建自己的提示词管理应用或服务



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,456 |
| 语言 | Jupyter Notebook |
| Forks | 13,861 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是目前最受欢迎的 LLM 从零实现项目，通过 Jupyter Notebook 逐步构建的方式，让开发者真正理解 GPT 架构的每个细节，而非仅依赖黑盒 API，是系统学习大语言模型原理的绝佳实践资源。

**技术亮点**:
- 完全从零实现，不依赖 transformers 等高级库，深入理解 LLM 底层机制
- 使用 Jupyter Notebook 格式，每个步骤都有详细代码和解释，便于循序渐进学习
- 完整实现 GPT 架构核心组件：Transformer 块、自注意力机制、RoPE 位置编码等
- 包含完整的预训练流程演示，使用小型 GPT-2 模型进行训练实践
- 涵盖推理优化技术如 KV cache 和 INT8 量化，兼顾理论与实践

**适用场景**:
- 系统学习 LLM 架构：适合想深入理解 ChatGPT/GPT-4 等大语言模型工作原理的开发者，从零构建比单纯看论文更能加深理解
- PyTorch 深度学习进阶：作为 PyTorch 高级应用案例，学习如何实现复杂的神经网络架构和训练流程
- AI 教育与课程设计：作为深度学习/NLP 课程的教学项目，通过代码实践帮助学生掌握 LLM 核心概念



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,360 |
| 语言 | Python |
| Forks | 6,645 |
| Issues | 2,781 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,326 |
| 语言 | TypeScript |
| Forks | 8,373 |
| Issues | 72 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,427 |
| 语言 | TypeScript |
| Forks | 3,662 |
| Issues | 167 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,953 |
| 语言 | Python |
| Forks | 9,886 |
| Issues | 358 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,896 |
| 语言 | Python |
| Forks | 3,063 |
| Issues | 201 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,037 |
| 语言 | JavaScript |
| Forks | 6,273 |
| Issues | 318 |
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
| Stars | 70,979 |
| 语言 | Python |
| Forks | 8,903 |
| Issues | 394 |
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
| Stars | 50,316 |
| 语言 | TypeScript |
| Forks | 4,013 |
| Issues | 482 |
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
| Stars | 51,751 |
| 语言 | TypeScript |
| Forks | 24,101 |
| Issues | 803 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,083 |
| 语言 | Unknown |
| Forks | 6,270 |
| Issues | 18 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,032 |
| 语言 | Python |
| Forks | 15,427 |
| Issues | 4,167 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,464 |
| 语言 | Python |
| Forks | 6,250 |
| Issues | 86 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,380 |
| 语言 | TypeScript |
| Forks | 4,010 |
| Issues | 1,096 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 146,784 |
| 语言 | Python |
| Forks | 8,745 |
| Issues | 946 |
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
| Stars | 168,471 |
| 语言 | Go |
| Forks | 15,504 |
| Issues | 2,908 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,108 |
| 语言 | MDX |
| Forks | 7,880 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,681 |
| 语言 | Rust |
| Forks | 9,496 |
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
| Stars | 33,985 |
| 语言 | Python |
| Forks | 2,125 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 99,185 |
| 语言 | Python |
| Forks | 6,076 |
| Issues | 530 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (11 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,877 |
| 语言 | Python |
| Forks | 8,524 |
| Issues | 964 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最成熟的开源 LLM 微调框架，支持 100+ 主流大模型的高效微调，提供 LoRA、QLoRA、RLHF 等多种低成本训练方案，并获得 ACL 2024 学术认可，特别适合需要快速适配垂类场景的企业和研究者。

**技术亮点**:
- 支持 100+ LLMs 和 VLMs 统一微调，涵盖 LLaMA、Qwen、DeepSeek、Gemma 等主流模型系列
- 集成 LoRA、QLoRA、Adapter、Prefix-tuning 等多种 PEFT 高效微调方法，大幅降低显存占用
- 支持 INT4/INT8 量化训练，可在消费级 GPU 上微调百亿参数模型
- 内置 SFT、DPO、PPO 等多种训练范式，覆盖从监督学习到强化学习的完整流程
- 提供 Web UI 和 CLI 工具，训练过程可视化监控，开箱即用

**适用场景**:
- 企业私有化部署：快速将开源大模型微调适配到金融、医疗、法律等垂直领域，打造专属 AI 助手
- 学术研究与实验：研究人员可便捷对比不同微调方法、模型架构的效果，加速论文实验迭代
- 个人开发者定制：利用 QLoRA 在单卡消费级显卡上微调小模型，降低 LLM 应用开发门槛



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,667 |
| 语言 | Python |
| Forks | 6,522 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是最受欢迎的 Python 金融数据开源平台之一，拥有 65,000+ Stars，提供统一 API 整合多数据源，支持股票、加密货币、期权等多资产类别，并内置机器学习和 AI Agent 支持，适合量化分析师、金融开发者和数据科学家快速构建投资分析工具。

**技术亮点**:
- 统一的 Python API 接口，整合多个金融数据源（Yahoo Finance、CoinGecko 等），简化数据获取流程
- 支持多资产类别分析：股票、加密货币、期权、固收、衍生品等
- 内置机器学习模块，提供预测模型和量化分析功能
- 支持 AI Agent 集成，可扩展性强，适合构建智能金融应用
- 模块化架构设计，支持自定义扩展和第三方集成

**适用场景**:
- 量化交易研究：使用历史数据进行策略回测、技术分析和因子挖掘
- 投资组合管理与风险分析：多资产配置、风险评估和收益归因
- 金融数据应用开发：为金融机构或金融科技产品构建数据分析和可视化功能



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,139 |
| 语言 | HTML |
| Forks | 20,843 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最大的开源提示词社区项目，拥有超过15万星标，支持多平台LLM集成，提供自托管能力，是个人开发者和企业构建私有提示词管理系统的最佳参考和直接使用方案。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态导出
- 多 LLM 平台支持（ChatGPT/Claude/Gemini/GPT-4），统一提示词格式转换
- 开源可自托管，完整隐私保护，适合企业内网部署
- 社区驱动的提示词贡献机制，包含提示词验证和分类系统
- 提供提示词导入/导出功能，支持 Chrome 扩展集成

**适用场景**:
- 个人用户：发现和收藏高质量 AI 提示词，提升 GPT/Claude 等工具的使用效率
- 企业团队：自托管部署私有提示词库，保护内部知识资产，避免数据外泄
- AI 开发者：参考提示词工程最佳实践，构建自己的提示词管理应用或服务



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,456 |
| 语言 | Jupyter Notebook |
| Forks | 13,861 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是目前最受欢迎的 LLM 从零实现项目，通过 Jupyter Notebook 逐步构建的方式，让开发者真正理解 GPT 架构的每个细节，而非仅依赖黑盒 API，是系统学习大语言模型原理的绝佳实践资源。

**技术亮点**:
- 完全从零实现，不依赖 transformers 等高级库，深入理解 LLM 底层机制
- 使用 Jupyter Notebook 格式，每个步骤都有详细代码和解释，便于循序渐进学习
- 完整实现 GPT 架构核心组件：Transformer 块、自注意力机制、RoPE 位置编码等
- 包含完整的预训练流程演示，使用小型 GPT-2 模型进行训练实践
- 涵盖推理优化技术如 KV cache 和 INT8 量化，兼顾理论与实践

**适用场景**:
- 系统学习 LLM 架构：适合想深入理解 ChatGPT/GPT-4 等大语言模型工作原理的开发者，从零构建比单纯看论文更能加深理解
- PyTorch 深度学习进阶：作为 PyTorch 高级应用案例，学习如何实现复杂的神经网络架构和训练流程
- AI 教育与课程设计：作为深度学习/NLP 课程的教学项目，通过代码实践帮助学生掌握 LLM 核心概念



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,696 |
| 语言 | TypeScript |
| Forks | 3,643 |
| Issues | 289 |
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
| Stars | 159,164 |
| 语言 | Python |
| Forks | 32,819 |
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
| Stars | 76,032 |
| 语言 | Python |
| Forks | 15,427 |
| Issues | 4,167 |
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
| Stars | 108,364 |
| 语言 | Python |
| Forks | 12,552 |
| Issues | 3,955 |
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
| Stars | 98,998 |
| 语言 | Python |
| Forks | 27,458 |
| Issues | 18,351 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,108 |
| 语言 | MDX |
| Forks | 7,880 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,376 |
| 语言 | Jupyter Notebook |
| Forks | 5,519 |
| Issues | 125 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 149,929 |
| 语言 | JavaScript |
| Forks | 23,198 |
| Issues | 58 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有 149,929 Stars 的热门项目，为多种主流 AI 编码助手提供统一的能力扩展框架，涵盖 Skills 技能、Instincts 本能、Memory 记忆和 Security 安全机制，能显著提升 AI 代理的响应速度和任务完成质量。

**技术亮点**:
- 多 Agent 平台兼容：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具，提供一致的扩展接口
- MCP 协议深度集成：实现标准化的上下文管理和工具调用，提升 AI 代理的互操作性
- 分层能力架构：通过 Skills、Instincts、Memory 三层设计灵活扩展 AI 代理能力
- 安全优先设计：内置 Security 机制确保 AI 代理操作的合规性和数据安全
- 研究驱动开发：采用 Research-first 方法论持续优化 AI 代理推理效率

**适用场景**:
- 企业级 AI 开发平台：团队需要统一管理多个 AI 编码助手的能力扩展和安全策略
- AI 代理开发者：构建、测试和优化自定义 AI 代理系统，研究代理性能瓶颈
- 个人开发者效率提升：通过自定义 Skills 和 Memory 扩展打造个人专属的 AI 编程助手



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,207 |
| 语言 | Go |
| Forks | 3,906 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型类型，无需 GPU 即可在普通硬件上运行，为企业提供了一种经济高效的私有化 AI 部署方案，同时让个人开发者零成本构建 AI 应用。

**技术亮点**:
- 多模态模型支持：统一支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频处理（TTS/MusicGen）、目标检测等多种任务
- 零硬件门槛：采用 Go 语言优化，可在 CPU 环境下运行，无需昂贵 GPU，降低 AI 部署成本
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零改动迁移至本地部署
- 分布式架构：支持 libp2p 去中心化组网，便于构建分布式 AI 推理网络
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的本地工具引擎使用

**适用场景**:
- 企业私有化 AI 部署：金融、医疗、政务等对数据隐私要求严格的行业，需本地化处理敏感数据
- 离线/边缘计算场景：物联网设备、远程工作站等无网络或网络受限环境下的 AI 推理
- 开发者快速原型验证：个人开发者或团队在没有云服务预算的情况下，快速搭建 AI 功能演示或 MVP 产品



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,979 |
| 语言 | Python |
| Forks | 8,903 |
| Issues | 394 |
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
| Stars | 50,316 |
| 语言 | TypeScript |
| Forks | 4,013 |
| Issues | 482 |
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
| Stars | 183,446 |
| 语言 | TypeScript |
| Forks | 56,656 |
| Issues | 1,462 |
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
| Stars | 155,990 |
| 语言 | Python |
| Forks | 12,804 |
| Issues | 2,452 |
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
| Stars | 97,055 |
| 语言 | Python |
| Forks | 9,047 |
| Issues | 171 |
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
| Stars | 80,753 |
| 语言 | Python |
| Forks | 9,370 |
| Issues | 253 |
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
| Stars | 183,687 |
| 语言 | TypeScript |
| Forks | 39,108 |
| Issues | 16,133 |
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
| Stars | 94,074 |
| 语言 | TypeScript |
| Forks | 9,417 |
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
| Stars | 78,881 |
| 语言 | TypeScript |
| Forks | 5,785 |
| Issues | 752 |
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
| Stars | 77,045 |
| 语言 | TypeScript |
| Forks | 6,598 |
| Issues | 139 |
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
| Stars | 79,355 |
| 语言 | Go |
| Forks | 2,760 |
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
| Stars | 76,152 |
| 语言 | Go |
| Forks | 2,744 |
| Issues | 950 |
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
| Stars | 43,720 |
| 语言 | Go |
| Forks | 8,230 |
| Issues | 961 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### charmbracelet/bubbletea

**描述**: A powerful little TUI framework 🏗

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,447 |
| 语言 | Go |
| Forks | 1,178 |
| Issues | 172 |
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
| Stars | 420,700 |
| 语言 | Python |
| Forks | 45,781 |
| Issues | 1,229 |
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
| Stars | 75,573 |
| 语言 | JavaScript |
| Forks | 7,278 |
| Issues | 712 |
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
| Stars | 50,316 |
| 语言 | TypeScript |
| Forks | 4,013 |
| Issues | 482 |
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
| Stars | 183,446 |
| 语言 | TypeScript |
| Forks | 56,656 |
| Issues | 1,462 |
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
| Stars | 51,605 |
| 语言 | Go |
| Forks | 10,313 |
| Issues | 231 |
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
| Stars | 121,662 |
| 语言 | Go |
| Forks | 42,831 |
| Issues | 2,731 |
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
| Stars | 71,476 |
| 语言 | Go |
| Forks | 18,916 |
| Issues | 3,788 |
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
| Stars | 54,832 |
| 语言 | Go |
| Forks | 6,557 |
| Issues | 2,824 |
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
| Stars | 47,487 |
| 语言 | Go |
| Forks | 5,044 |
| Issues | 980 |
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
| Stars | 94,074 |
| 语言 | TypeScript |
| Forks | 9,417 |
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
| Stars | 76,531 |
| 语言 | TypeScript |
| Forks | 6,596 |
| Issues | 401 |
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
| Stars | 85,081 |
| 语言 | JavaScript |
| Forks | 7,624 |
| Issues | 716 |
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
| Stars | 69,804 |
| 语言 | Go |
| Forks | 1,907 |
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
| Stars | 62,636 |
| 语言 | Go |
| Forks | 5,906 |
| Issues | 773 |
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
| Stars | 58,721 |
| 语言 | Go |
| Forks | 4,252 |
| Issues | 29 |
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
| Stars | 85,081 |
| 语言 | JavaScript |
| Forks | 7,624 |
| Issues | 716 |
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
| Stars | 63,534 |
| 语言 | Go |
| Forks | 10,319 |
| Issues | 759 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (15 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,207 |
| 语言 | Go |
| Forks | 3,906 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持 LLM、图像、音频、视频等多种模型类型，无需 GPU 即可在普通硬件上运行，为企业提供了一种经济高效的私有化 AI 部署方案，同时让个人开发者零成本构建 AI 应用。

**技术亮点**:
- 多模态模型支持：统一支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、音频处理（TTS/MusicGen）、目标检测等多种任务
- 零硬件门槛：采用 Go 语言优化，可在 CPU 环境下运行，无需昂贵 GPU，降低 AI 部署成本
- OpenAI 兼容 API：提供与 OpenAI API 兼容的接口，现有应用可零改动迁移至本地部署
- 分布式架构：支持 libp2p 去中心化组网，便于构建分布式 AI 推理网络
- MCP 协议支持：集成 Model Context Protocol，可作为 AI Agent 的本地工具引擎使用

**适用场景**:
- 企业私有化 AI 部署：金融、医疗、政务等对数据隐私要求严格的行业，需本地化处理敏感数据
- 离线/边缘计算场景：物联网设备、远程工作站等无网络或网络受限环境下的 AI 推理
- 开发者快速原型验证：个人开发者或团队在没有云服务预算的情况下，快速搭建 AI 功能演示或 MVP 产品



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,055 |
| 语言 | Python |
| Forks | 9,047 |
| Issues | 171 |
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
| Stars | 87,255 |
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
| Stars | 100,037 |
| 语言 | TypeScript |
| Forks | 27,150 |
| Issues | 1,127 |
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
| Stars | 78,881 |
| 语言 | TypeScript |
| Forks | 5,785 |
| Issues | 752 |
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
| Stars | 68,929 |
| 语言 | JavaScript |
| Forks | 23,073 |
| Issues | 209 |
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
| Stars | 55,950 |
| 语言 | JavaScript |
| Forks | 10,213 |
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
| Stars | 51,781 |
| 语言 | JavaScript |
| Forks | 4,697 |
| Issues | 1,470 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### bigskysoftware/htmx

**描述**: </> htmx - high power tools for HTML

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,782 |
| 语言 | JavaScript |
| Forks | 1,582 |
| Issues | 655 |
| Topics | hateoas, html, htmx, hyperscript, javascript, rest |
| 许可证 | Other |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,279 |
| 语言 | Go |
| Forks | 8,575 |
| Issues | 672 |
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
| Stars | 71,440 |
| 语言 | Go |
| Forks | 4,696 |
| Issues | 263 |
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
| Stars | 57,517 |
| 语言 | Go |
| Forks | 3,276 |
| Issues | 23 |
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
| Stars | 41,447 |
| 语言 | Go |
| Forks | 1,178 |
| Issues | 172 |
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
| Stars | 420,700 |
| 语言 | Python |
| Forks | 45,781 |
| Issues | 1,229 |
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
| Stars | 75,573 |
| 语言 | JavaScript |
| Forks | 7,278 |
| Issues | 712 |
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
| Stars | 100,609 |
| 语言 | TypeScript |
| Forks | 12,033 |
| Issues | 982 |
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
| Stars | 58,037 |
| 语言 | JavaScript |
| Forks | 6,273 |
| Issues | 318 |
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
| Stars | 43,718 |
| 语言 | Go |
| Forks | 3,947 |
| Issues | 1,156 |
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
| Stars | 51,605 |
| 语言 | Go |
| Forks | 10,313 |
| Issues | 231 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (10 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,139 |
| 语言 | HTML |
| Forks | 20,843 |
| Issues | 43 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最大的开源提示词社区项目，拥有超过15万星标，支持多平台LLM集成，提供自托管能力，是个人开发者和企业构建私有提示词管理系统的最佳参考和直接使用方案。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，支持服务端渲染和静态导出
- 多 LLM 平台支持（ChatGPT/Claude/Gemini/GPT-4），统一提示词格式转换
- 开源可自托管，完整隐私保护，适合企业内网部署
- 社区驱动的提示词贡献机制，包含提示词验证和分类系统
- 提供提示词导入/导出功能，支持 Chrome 扩展集成

**适用场景**:
- 个人用户：发现和收藏高质量 AI 提示词，提升 GPT/Claude 等工具的使用效率
- 企业团队：自托管部署私有提示词库，保护内部知识资产，避免数据外泄
- AI 开发者：参考提示词工程最佳实践，构建自己的提示词管理应用或服务



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,326 |
| 语言 | TypeScript |
| Forks | 8,373 |
| Issues | 72 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,896 |
| 语言 | Python |
| Forks | 3,063 |
| Issues | 201 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,083 |
| 语言 | Unknown |
| Forks | 6,270 |
| Issues | 18 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,108 |
| 语言 | MDX |
| Forks | 7,880 |
| Issues | 256 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 35,161 |
| 语言 | Python |
| Forks | 4,120 |
| Issues | 91 |
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
| Stars | 89,675 |
| 语言 | TypeScript |
| Forks | 9,993 |
| Issues | 2,238 |
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
| Stars | 87,252 |
| 语言 | TypeScript |
| Forks | 8,845 |
| Issues | 1,634 |
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
| Stars | 127,405 |
| 语言 | JavaScript |
| Forks | 12,472 |
| Issues | 2 |
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
| Stars | 169,618 |
| 语言 | Go |
| Forks | 13,131 |
| Issues | 177 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,736 |
| 语言 | Python |
| Forks | 6,529 |
| Issues | 66 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,522 |
| 语言 | Python |
| Forks | 13,008 |
| Issues | 116 |
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
| Stars | 86,896 |
| 语言 | Python |
| Forks | 7,468 |
| Issues | 606 |
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
| Stars | 134,885 |
| 语言 | Unknown |
| Forks | 33,915 |
| Issues | 143 |
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
| Stars | 385,300 |
| 语言 | Python |
| Forks | 66,100 |
| Issues | 80 |
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
| Stars | 114,409 |
| 语言 | TypeScript |
| Forks | 5,887 |
| Issues | 316 |
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
| Stars | 109,516 |
| 语言 | TypeScript |
| Forks | 7,956 |
| Issues | 246 |
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
| Stars | 50,286 |
| 语言 | JavaScript |
| Forks | 4,189 |
| Issues | 57 |
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
| Stars | 48,125 |
| 语言 | Go |
| Forks | 10,277 |
| Issues | 1,892 |
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
| Stars | 102,965 |
| 语言 | C++ |
| Forks | 16,651 |
| Issues | 1,449 |
| Topics | ggml |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,485 |
| 语言 | Python |
| Forks | 1,632 |
| Issues | 38 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,168 |
| 语言 | TypeScript |
| Forks | 9,648 |
| Issues | 324 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 291,590 |
| 语言 | Python |
| Forks | 27,635 |
| Issues | 19 |
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
| Stars | 219,486 |
| 语言 | Python |
| Forks | 50,319 |
| Issues | 919 |
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
| Stars | 85,989 |
| 语言 | Python |
| Forks | 37,204 |
| Issues | 3,571 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,787 |
| 语言 | Python |
| Forks | 16,837 |
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
| Stars | 442,521 |
| 语言 | TypeScript |
| Forks | 44,229 |
| Issues | 198 |
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
| Stars | 352,654 |
| 语言 | TypeScript |
| Forks | 43,906 |
| Issues | 8 |
| Topics | angular-roadmap, backend-roadmap, blockchain-roadmap, computer-science, dba-roadmap, developer-roadmap, devops-roadmap, frontend-roadmap, go-roadmap, java-roadmap, javascript-roadmap, nodejs-roadmap, python-roadmap, qa-roadmap, react-roadmap, roadmap, software-architect-roadmap, vue-roadmap |
| 许可证 | Other |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,637 |
| 语言 | TypeScript |
| Forks | 16,496 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### excalidraw/excalidraw

**描述**: Virtual whiteboard for sketching hand-drawn like diagrams

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 120,743 |
| 语言 | TypeScript |
| Forks | 13,216 |
| Issues | 2,941 |
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
| Stars | 112,021 |
| 语言 | TypeScript |
| Forks | 8,494 |
| Issues | 1,807 |
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
| Stars | 108,492 |
| 语言 | TypeScript |
| Forks | 13,335 |
| Issues | 5,023 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,741 |
| 语言 | TypeScript |
| Forks | 54,590 |
| Issues | 1,355 |
| Topics | ant-design, antd, design-systems, react, typescript, ui-kit, ui-library |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,519 |
| 语言 | TypeScript |
| Forks | 5,352 |
| Issues | 693 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### tailwindlabs/tailwindcss

**描述**: A utility-first CSS framework for rapid UI development.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,481 |
| 语言 | TypeScript |
| Forks | 5,190 |
| Issues | 110 |
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
| Stars | 79,802 |
| 语言 | TypeScript |
| Forks | 8,041 |
| Issues | 710 |
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
| Stars | 244,415 |
| 语言 | JavaScript |
| Forks | 50,897 |
| Issues | 1,228 |
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
| Stars | 116,664 |
| 语言 | JavaScript |
| Forks | 35,311 |
| Issues | 2,602 |
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
| Stars | 111,853 |
| 语言 | JavaScript |
| Forks | 36,328 |
| Issues | 560 |
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
| Stars | 108,979 |
| 语言 | JavaScript |
| Forks | 11,610 |
| Issues | 266 |
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
| Stars | 98,104 |
| 语言 | JavaScript |
| Forks | 32,691 |
| Issues | 1,674 |
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
| Stars | 95,552 |
| 语言 | JavaScript |
| Forks | 15,341 |
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
| Stars | 86,271 |
| 语言 | JavaScript |
| Forks | 4,885 |
| Issues | 973 |
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
| Stars | 70,967 |
| 语言 | JavaScript |
| Forks | 16,812 |
| Issues | 893 |
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
| Stars | 66,310 |
| 语言 | JavaScript |
| Forks | 9,190 |
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
| Stars | 65,846 |
| 语言 | JavaScript |
| Forks | 9,383 |
| Issues | 204 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,350 |
| 语言 | JavaScript |
| Forks | 5,649 |
| Issues | 70 |
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
| Forks | 20,481 |
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
| Stars | 57,423 |
| 语言 | JavaScript |
| Forks | 12,304 |
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
| Stars | 53,104 |
| 语言 | JavaScript |
| Forks | 10,602 |
| Issues | 459 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,458 |
| 语言 | JavaScript |
| Forks | 11,452 |
| Issues | 234 |
| Topics | blogging, cms, ghost, javascript, journalism, nodejs, publishing, web-application |
| 许可证 | MIT License |


### iamkun/dayjs

**描述**: ⏰ Day.js 2kB immutable date-time library alternative to Moment.js with the same modern API

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,624 |
| 语言 | JavaScript |
| Forks | 2,429 |
| Issues | 1,210 |
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
| Stars | 133,399 |
| 语言 | Go |
| Forks | 18,906 |
| Issues | 9,931 |
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
| Stars | 87,501 |
| 语言 | Go |
| Forks | 8,243 |
| Issues | 265 |
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
| Stars | 81,595 |
| 语言 | Go |
| Forks | 4,992 |
| Issues | 394 |
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
| Stars | 68,635 |
| 语言 | Go |
| Forks | 3,213 |
| Issues | 6 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,569 |
| 语言 | Go |
| Forks | 5,013 |
| Issues | 1,156 |
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
| Stars | 50,974 |
| 语言 | Go |
| Forks | 21,882 |
| Issues | 395 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,731 |
| 语言 | Shell |
| Forks | 12,310 |
| Issues | 120 |
| 许可证 | MIT License |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,140 |
| 语言 | Python |
| Forks | 55,278 |
| Issues | 528 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 97,514 |
| 语言 | Python |
| Forks | 12,017 |
| Issues | 119 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,927 |
| 语言 | Python |
| Forks | 7,204 |
| Issues | 482 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### tensorflow/models

**描述**: Models and examples built with TensorFlow

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 77,674 |
| 语言 | Python |
| Forks | 45,160 |
| Issues | 1,279 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,416 |
| 语言 | TypeScript |
| Forks | 10,314 |
| Issues | 731 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,074 |
| 语言 | TypeScript |
| Forks | 7,580 |
| Issues | 34 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,004 |
| 语言 | JavaScript |
| Forks | 32,381 |
| Issues | 280 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 62,647 |
| 语言 | JavaScript |
| Forks | 4,002 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,325 |
| 语言 | JavaScript |
| Forks | 7,129 |
| Issues | 139 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,776 |
| 语言 | Go |
| Forks | 14,985 |
| Issues | 45 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,596 |
| 语言 | Go |
| Forks | 1,593 |
| Issues | 267 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,288 |
| 语言 | Go |
| Forks | 7,959 |
| Issues | 564 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 150,136 |
| 语言 | Python |
| Forks | 11,414 |
| Issues | 320 |
| Topics | awesome, github, hellogithub, python |
