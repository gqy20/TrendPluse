# 项目发现报告 (2026-04-18)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 137 |
| 去重移除 | 31 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 23 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 7 |
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
| Stars | 132,548 |
| 语言 | Python |
| Forks | 18,813 |
| Issues | 231 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 界面项目，支持 Ollama 和 OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，132k+ Stars 证明了其极高的社区认可度和稳定性，是企业和个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的交互界面
- 内置 RAG（检索增强生成）功能，支持知识库管理和文档问答
- 支持 MCP（Model Control Protocol）协议，便于扩展和集成第三方工具
- 提供完整的 Web UI 界面，支持实时对话、对话管理和模型切换
- 支持自托管部署，保障数据隐私安全，适合企业内网使用

**适用场景**:
- 企业内部 AI 助手：企业可自托管部署，建立私有化的 AI 对话系统，用于客服、文档检索、知识管理等场景
- 个人开发者本地 LLM 体验：通过 Ollama 本地运行开源大模型，配合友好的 Web UI 获得更好的交互体验
- 多模型统一管理平台：同时接入多个 LLM 提供商，通过统一界面进行模型对比、切换和优化



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,111 |
| 语言 | Python |
| Forks | 14,004 |
| Issues | 5,492 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名 AI 研究团队 NousResearch 打造的多功能 AI Agent 框架，支持 OpenAI、Anthropic、Claude 等主流 LLM 提供商，拥有超过 99k stars 的社区认可度，采用 MIT 许可证，非常适合企业快速构建智能代理应用。

**技术亮点**:
- 支持多 LLM 提供商集成（OpenAI GPT、Anthropic Claude 等），可灵活切换不同模型
- 基于 Python 的现代化架构，便于扩展和自定义 Agent 行为
- 专注于 AI Agent 能力，支持复杂任务分解和自动化执行
- 活跃的开源社区维护，99k+ stars 证明其成熟度和稳定性
- MIT 许可证许可，商业使用无限制，易于集成到商业产品

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、工作流自动化、业务流程机器人
- 开发者效率工具：代码助手、自动化脚本、测试生成等开发工作流
- 个人生产力助手：日程管理、信息检索、文档处理等个人任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,437 |
| 语言 | Python |
| Forks | 8,852 |
| Issues | 3,009 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将 RAG 检索能力与 Agent 智能体深度融合，配合深度文档理解和 GraphRAG 支持，为企业级 LLM 应用提供了生产级的上下文增强方案，是构建智能问答和深度研究系统的理想选择。

**技术亮点**:
- RAG + Agent 深度融合：通过 Agent 能力实现智能检索规划、多步推理和动态知识更新，相比传统 RAG 具有更强的复杂问题处理能力
- 深度文档理解：支持多种文档格式的语义解析，能够提取结构化信息并理解文档层级关系，提升检索质量
- GraphRAG 支持：集成知识图谱增强检索能力，通过图关系发现隐式关联，提升跨文档推理能力
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型，支持本地部署，满足不同隐私和性能需求
- MCP (Model Context Protocol) 支持：遵循标准协议便于扩展集成，可快速接入现有 AI 生态

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服、产品文档问答、法规政策查询等需要精准溯源的场景
- 深度研究分析：利用 Agent 规划能力和 GraphRAG 实现多文档关联分析，适合学术研究、市场调研、竞品分析等需要综合推理的场景
- 智能文档处理：处理合同审查、报告生成、技术文档管理等需要理解复杂文档结构的业务场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,317 |
| 语言 | JavaScript |
| Forks | 24,944 |
| Issues | 120 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有超过16万Stars的大规模社区验证项目，为Claude Code、Codex、Cursor等主流AI编程工具提供Skills、Instincts、Memory等创新机制的性能优化框架，特别适合希望深度定制AI编程工作流的开发团队。

**技术亮点**:
- 多Agent引擎支持 - 统一兼容Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- Skills & Instincts系统 - 创新的行为模式库，通过预定义技能集让AI代理具备专业领域知识
- Memory管理架构 - 内置长期记忆系统，支持跨会话上下文保持和高效检索
- 安全沙箱机制 - 专为AI代理设计的安全防护层，支持细粒度权限控制
- Research-first开发方法论 - 强调实验驱动优化，提供性能基准测试工具

**适用场景**:
- 企业级AI编程平台集成 - 在组织内部署定制化AI编程助手，统一管理合规性和安全策略
- AI Agent开发研究 - 用于构建和测试新型AI代理架构，特别是MCP相关应用
- 个人开发者效率提升 - 优化本地AI编程工具的响应速度和任务完成质量



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,529 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，特别适合隐私敏感或需要离线部署的场景。其 Go 语言实现保证了高性能和易部署性，45k+ stars 的社区认可度证明了其成熟度和可靠性。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、视觉、语音、图像、视频等多种模型类型，包括 llama、mamba、stable-diffusion、musicgen 等主流模型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低部署门槛和成本
- Go 语言实现：提供高性能和轻量级部署，支持分布式和去中心化架构（基于 libp2p）
- 丰富的 API 接口：提供 OpenAI 兼容的 API，支持 agent、rerank 等高级功能，降低迁移成本
- MCP 协议支持：支持 Model Context Protocol，便于构建 AI agents 和自动化工作流

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等需要本地处理敏感数据的企业，可在不依赖云服务的情况下运行 AI 助手
- 边缘设备部署：在没有强大 GPU 的边缘服务器或工作站上部署 AI 应用，适用于工业物联网和远程办公场景
- 离线 AI 应用：为网络受限或需要完全离线运行的场景（如偏远地区、军事应用）提供完整的 AI 能力
- AI 开发原型验证：开发者可在本地快速测试和迭代 AI 应用，无需云服务订阅或 API 配额限制



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,327 |
| 语言 | TypeScript |
| Forks | 14,939 |
| Issues | 694 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有超过 75K Stars 的顶级开源 AI Agent 协作平台，其独特价值在于提供了开箱即用的多 Agent 协作框架和多模型统一接入能力（支持 GPT、Claude、Gemini、DeepSeek 等），让开发者能够快速构建、部署和管理企业级 AI Agent 团队，无需从零搭建基础设施。

**技术亮点**:
- 多 AI 模型统一接入：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：内置 MCP 协议实现，标准化 Agent 与外部工具/数据的交互方式
- 多 Agent 协作框架：支持多个 Agent 组成团队协同工作，实现复杂的任务分解与协作流程
- 内置知识库系统：提供完整的知识检索增强生成（RAG）能力，支持 Agent 访问私有知识库
- TypeScript 全栈架构：从前端界面到后端逻辑保持类型安全，代码质量高且易于维护

**适用场景**:
- 企业智能办公助手平台：构建支持多 Agent 协作的智能办公系统，如数据分析、文档处理、日程管理 Agent 协同工作
- AI 应用快速原型开发：利用成熟的 Agent 框架和模型集成能力快速构建 AI 应用
- 智能客服与支持系统：实现问题分类、专业问答、情绪识别等不同 Agent 的分工协作



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,268 |
| 语言 | Python |
| Forks | 8,600 |
| Issues | 977 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个功能强大的统一微调框架，支持100+主流大语言模型和视觉语言模型，提供LoRA、QLoRA、RLHF等多种高效微调方法，通过WebUI和CLI实现零代码微调，是目前最受欢迎的LLM微调开源项目。

**技术亮点**:
- 支持100+ LLMs & VLMs统一微调，包括LLaMA、LLaMA3、Qwen、DeepSeek、Gemma、ChatGLM等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、Peft、RLHF、DPO、KTO、ORPO等
- 支持多级量化（AWQ、GPTQ、GGUF），大幅降低显存占用和推理成本
- 提供WebUI可视化界面和CLI命令行两种使用方式，支持数据管理和训练监控
- 基于Transformers和PEFT库实现，模块化架构便于扩展新模型和训练方法

**适用场景**:
- 企业场景：快速基于自有数据微调领域专属大模型，应用于客服、知识库问答、内容生成等业务
- 学术研究：便捷进行指令微调、RLHF等实验，支持多种训练方法和评估指标
- 个人开发者：零代码微调开源模型，低成本定制个性化AI助手或特定任务模型



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,318 |
| 语言 | TypeScript |
| Forks | 5,193 |
| Issues | 145 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的革命性记忆插件，通过 AI 自动压缩编码会话上下文并跨会话注入，让 AI 助手真正拥有"记忆能力"，避免重复解释项目背景，大幅提升开发效率。Stars 高达 62,318 证明了其在 AI 编程工具领域的极高认可度。

**技术亮点**:
- 基于 Claude agent-sdk 实现智能上下文压缩，使用 AI 本身来压缩和提炼记忆内容
- 支持 ChromaDB、SQLite 等多种向量数据库，实现高效的语义检索和相似度匹配
- 集成 RAG（检索增强生成）技术和 Embeddings 向量化，精准召回相关历史上下文
- 采用 TypeScript 开发，提供完整的 Claude Code 插件架构，易于集成和扩展
- 实现长期记忆引擎，支持跨会话持久化存储，保持项目理解的连续性

**适用场景**:
- 大型项目开发：AI 能够在多周甚至数月的开发周期中记住架构决策、设计模式和之前解决的问题，避免重复踩坑
- 个人开发者效率提升：新会话自动理解项目结构、编码风格和技术栈，无需每次从头解释项目背景
- 复杂代码库维护：在处理遗留系统时，AI 能调用历史会话中的上下文信息，提供更准确的分析和修改建议



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,625 |
| 语言 | TypeScript |
| Forks | 8,982 |
| Issues | 94 |
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
| Stars | 43,467 |
| 语言 | Python |
| Forks | 9,949 |
| Issues | 352 |
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
| Stars | 39,996 |
| 语言 | Python |
| Forks | 7,040 |
| Issues | 960 |
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
| Stars | 45,880 |
| 语言 | Java |
| Forks | 15,920 |
| Issues | 8 |
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
| Stars | 39,004 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
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
| Stars | 38,235 |
| 语言 | Python |
| Forks | 4,540 |
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
| Stars | 33,829 |
| 语言 | TypeScript |
| Forks | 3,670 |
| Issues | 293 |
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
| Stars | 110,573 |
| 语言 | TypeScript |
| Forks | 7,052 |
| Issues | 280 |
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
| Stars | 58,552 |
| 语言 | JavaScript |
| Forks | 6,335 |
| Issues | 337 |
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
| Stars | 71,445 |
| 语言 | Python |
| Forks | 8,987 |
| Issues | 419 |
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
| Stars | 52,559 |
| 语言 | TypeScript |
| Forks | 4,234 |
| Issues | 556 |
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
| Stars | 106,273 |
| 语言 | Python |
| Forks | 15,567 |
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
| Stars | 88,418 |
| 语言 | Python |
| Forks | 10,141 |
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
| Stars | 52,042 |
| 语言 | TypeScript |
| Forks | 24,171 |
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
| Stars | 184,578 |
| 语言 | TypeScript |
| Forks | 56,920 |
| Issues | 1,514 |
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
| Stars | 155,046 |
| 语言 | Java |
| Forks | 46,152 |
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
| Stars | 147,084 |
| 语言 | Python |
| Forks | 8,801 |
| Issues | 929 |
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
| Stars | 56,918 |
| 语言 | Jupyter Notebook |
| Forks | 19,722 |
| Issues | 10 |
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
| Stars | 34,144 |
| 语言 | Python |
| Forks | 2,151 |
| Issues | 96 |
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
| Stars | 33,699 |
| 语言 | Jupyter Notebook |
| Forks | 5,578 |
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
| Stars | 46,849 |
| 语言 | Rust |
| Forks | 2,992 |
| Issues | 536 |
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
| Stars | 132,548 |
| 语言 | Python |
| Forks | 18,813 |
| Issues | 231 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 界面项目，支持 Ollama 和 OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，132k+ Stars 证明了其极高的社区认可度和稳定性，是企业和个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的交互界面
- 内置 RAG（检索增强生成）功能，支持知识库管理和文档问答
- 支持 MCP（Model Control Protocol）协议，便于扩展和集成第三方工具
- 提供完整的 Web UI 界面，支持实时对话、对话管理和模型切换
- 支持自托管部署，保障数据隐私安全，适合企业内网使用

**适用场景**:
- 企业内部 AI 助手：企业可自托管部署，建立私有化的 AI 对话系统，用于客服、文档检索、知识管理等场景
- 个人开发者本地 LLM 体验：通过 Ollama 本地运行开源大模型，配合友好的 Web UI 获得更好的交互体验
- 多模型统一管理平台：同时接入多个 LLM 提供商，通过统一界面进行模型对比、切换和优化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,437 |
| 语言 | Python |
| Forks | 8,852 |
| Issues | 3,009 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将 RAG 检索能力与 Agent 智能体深度融合，配合深度文档理解和 GraphRAG 支持，为企业级 LLM 应用提供了生产级的上下文增强方案，是构建智能问答和深度研究系统的理想选择。

**技术亮点**:
- RAG + Agent 深度融合：通过 Agent 能力实现智能检索规划、多步推理和动态知识更新，相比传统 RAG 具有更强的复杂问题处理能力
- 深度文档理解：支持多种文档格式的语义解析，能够提取结构化信息并理解文档层级关系，提升检索质量
- GraphRAG 支持：集成知识图谱增强检索能力，通过图关系发现隐式关联，提升跨文档推理能力
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型，支持本地部署，满足不同隐私和性能需求
- MCP (Model Context Protocol) 支持：遵循标准协议便于扩展集成，可快速接入现有 AI 生态

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服、产品文档问答、法规政策查询等需要精准溯源的场景
- 深度研究分析：利用 Agent 规划能力和 GraphRAG 实现多文档关联分析，适合学术研究、市场调研、竞品分析等需要综合推理的场景
- 智能文档处理：处理合同审查、报告生成、技术文档管理等需要理解复杂文档结构的业务场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,327 |
| 语言 | TypeScript |
| Forks | 14,939 |
| Issues | 694 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有超过 75K Stars 的顶级开源 AI Agent 协作平台，其独特价值在于提供了开箱即用的多 Agent 协作框架和多模型统一接入能力（支持 GPT、Claude、Gemini、DeepSeek 等），让开发者能够快速构建、部署和管理企业级 AI Agent 团队，无需从零搭建基础设施。

**技术亮点**:
- 多 AI 模型统一接入：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：内置 MCP 协议实现，标准化 Agent 与外部工具/数据的交互方式
- 多 Agent 协作框架：支持多个 Agent 组成团队协同工作，实现复杂的任务分解与协作流程
- 内置知识库系统：提供完整的知识检索增强生成（RAG）能力，支持 Agent 访问私有知识库
- TypeScript 全栈架构：从前端界面到后端逻辑保持类型安全，代码质量高且易于维护

**适用场景**:
- 企业智能办公助手平台：构建支持多 Agent 协作的智能办公系统，如数据分析、文档处理、日程管理 Agent 协同工作
- AI 应用快速原型开发：利用成熟的 Agent 框架和模型集成能力快速构建 AI 应用
- 智能客服与支持系统：实现问题分类、专业问答、情绪识别等不同 Agent 的分工协作



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,318 |
| 语言 | TypeScript |
| Forks | 5,193 |
| Issues | 145 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的革命性记忆插件，通过 AI 自动压缩编码会话上下文并跨会话注入，让 AI 助手真正拥有"记忆能力"，避免重复解释项目背景，大幅提升开发效率。Stars 高达 62,318 证明了其在 AI 编程工具领域的极高认可度。

**技术亮点**:
- 基于 Claude agent-sdk 实现智能上下文压缩，使用 AI 本身来压缩和提炼记忆内容
- 支持 ChromaDB、SQLite 等多种向量数据库，实现高效的语义检索和相似度匹配
- 集成 RAG（检索增强生成）技术和 Embeddings 向量化，精准召回相关历史上下文
- 采用 TypeScript 开发，提供完整的 Claude Code 插件架构，易于集成和扩展
- 实现长期记忆引擎，支持跨会话持久化存储，保持项目理解的连续性

**适用场景**:
- 大型项目开发：AI 能够在多周甚至数月的开发周期中记住架构决策、设计模式和之前解决的问题，避免重复踩坑
- 个人开发者效率提升：新会话自动理解项目结构、编码风格和技术栈，无需每次从头解释项目背景
- 复杂代码库维护：在处理遗留系统时，AI 能调用历史会话中的上下文信息，提供更准确的分析和修改建议



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,880 |
| 语言 | Java |
| Forks | 15,920 |
| Issues | 8 |
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
| Stars | 39,004 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
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
| Stars | 38,235 |
| 语言 | Python |
| Forks | 4,540 |
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
| Stars | 33,829 |
| 语言 | TypeScript |
| Forks | 3,670 |
| Issues | 293 |
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
| Stars | 101,074 |
| 语言 | TypeScript |
| Forks | 12,112 |
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
| Stars | 58,552 |
| 语言 | JavaScript |
| Forks | 6,335 |
| Issues | 337 |
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
| Stars | 106,273 |
| 语言 | Python |
| Forks | 15,567 |
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
| Stars | 75,888 |
| 语言 | Python |
| Forks | 10,254 |
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
| Stars | 52,042 |
| 语言 | TypeScript |
| Forks | 24,171 |
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
| Stars | 43,852 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,127 |
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
| Stars | 33,764 |
| 语言 | Python |
| Forks | 4,786 |
| Issues | 212 |
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
| Stars | 34,144 |
| 语言 | Python |
| Forks | 2,151 |
| Issues | 96 |
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
| Stars | 33,699 |
| 语言 | Jupyter Notebook |
| Forks | 5,578 |
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
| Stars | 132,548 |
| 语言 | Python |
| Forks | 18,813 |
| Issues | 231 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完善的开源 AI 界面项目，支持 Ollama 和 OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，132k+ Stars 证明了其极高的社区认可度和稳定性，是企业和个人快速搭建私有 AI 助手的理想选择。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的交互界面
- 内置 RAG（检索增强生成）功能，支持知识库管理和文档问答
- 支持 MCP（Model Control Protocol）协议，便于扩展和集成第三方工具
- 提供完整的 Web UI 界面，支持实时对话、对话管理和模型切换
- 支持自托管部署，保障数据隐私安全，适合企业内网使用

**适用场景**:
- 企业内部 AI 助手：企业可自托管部署，建立私有化的 AI 对话系统，用于客服、文档检索、知识管理等场景
- 个人开发者本地 LLM 体验：通过 Ollama 本地运行开源大模型，配合友好的 Web UI 获得更好的交互体验
- 多模型统一管理平台：同时接入多个 LLM 提供商，通过统一界面进行模型对比、切换和优化



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,111 |
| 语言 | Python |
| Forks | 14,004 |
| Issues | 5,492 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名 AI 研究团队 NousResearch 打造的多功能 AI Agent 框架，支持 OpenAI、Anthropic、Claude 等主流 LLM 提供商，拥有超过 99k stars 的社区认可度，采用 MIT 许可证，非常适合企业快速构建智能代理应用。

**技术亮点**:
- 支持多 LLM 提供商集成（OpenAI GPT、Anthropic Claude 等），可灵活切换不同模型
- 基于 Python 的现代化架构，便于扩展和自定义 Agent 行为
- 专注于 AI Agent 能力，支持复杂任务分解和自动化执行
- 活跃的开源社区维护，99k+ stars 证明其成熟度和稳定性
- MIT 许可证许可，商业使用无限制，易于集成到商业产品

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、工作流自动化、业务流程机器人
- 开发者效率工具：代码助手、自动化脚本、测试生成等开发工作流
- 个人生产力助手：日程管理、信息检索、文档处理等个人任务自动化



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,437 |
| 语言 | Python |
| Forks | 8,852 |
| Issues | 3,009 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将 RAG 检索能力与 Agent 智能体深度融合，配合深度文档理解和 GraphRAG 支持，为企业级 LLM 应用提供了生产级的上下文增强方案，是构建智能问答和深度研究系统的理想选择。

**技术亮点**:
- RAG + Agent 深度融合：通过 Agent 能力实现智能检索规划、多步推理和动态知识更新，相比传统 RAG 具有更强的复杂问题处理能力
- 深度文档理解：支持多种文档格式的语义解析，能够提取结构化信息并理解文档层级关系，提升检索质量
- GraphRAG 支持：集成知识图谱增强检索能力，通过图关系发现隐式关联，提升跨文档推理能力
- 多 LLM 后端兼容：同时支持 OpenAI、DeepSeek、Ollama 等多种模型，支持本地部署，满足不同隐私和性能需求
- MCP (Model Context Protocol) 支持：遵循标准协议便于扩展集成，可快速接入现有 AI 生态

**适用场景**:
- 企业知识库问答系统：构建私有化部署的智能客服、产品文档问答、法规政策查询等需要精准溯源的场景
- 深度研究分析：利用 Agent 规划能力和 GraphRAG 实现多文档关联分析，适合学术研究、市场调研、竞品分析等需要综合推理的场景
- 智能文档处理：处理合同审查、报告生成、技术文档管理等需要理解复杂文档结构的业务场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,317 |
| 语言 | JavaScript |
| Forks | 24,944 |
| Issues | 120 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有超过16万Stars的大规模社区验证项目，为Claude Code、Codex、Cursor等主流AI编程工具提供Skills、Instincts、Memory等创新机制的性能优化框架，特别适合希望深度定制AI编程工作流的开发团队。

**技术亮点**:
- 多Agent引擎支持 - 统一兼容Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- Skills & Instincts系统 - 创新的行为模式库，通过预定义技能集让AI代理具备专业领域知识
- Memory管理架构 - 内置长期记忆系统，支持跨会话上下文保持和高效检索
- 安全沙箱机制 - 专为AI代理设计的安全防护层，支持细粒度权限控制
- Research-first开发方法论 - 强调实验驱动优化，提供性能基准测试工具

**适用场景**:
- 企业级AI编程平台集成 - 在组织内部署定制化AI编程助手，统一管理合规性和安全策略
- AI Agent开发研究 - 用于构建和测试新型AI代理架构，特别是MCP相关应用
- 个人开发者效率提升 - 优化本地AI编程工具的响应速度和任务完成质量



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,327 |
| 语言 | TypeScript |
| Forks | 14,939 |
| Issues | 694 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有超过 75K Stars 的顶级开源 AI Agent 协作平台，其独特价值在于提供了开箱即用的多 Agent 协作框架和多模型统一接入能力（支持 GPT、Claude、Gemini、DeepSeek 等），让开发者能够快速构建、部署和管理企业级 AI Agent 团队，无需从零搭建基础设施。

**技术亮点**:
- 多 AI 模型统一接入：无缝集成 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：内置 MCP 协议实现，标准化 Agent 与外部工具/数据的交互方式
- 多 Agent 协作框架：支持多个 Agent 组成团队协同工作，实现复杂的任务分解与协作流程
- 内置知识库系统：提供完整的知识检索增强生成（RAG）能力，支持 Agent 访问私有知识库
- TypeScript 全栈架构：从前端界面到后端逻辑保持类型安全，代码质量高且易于维护

**适用场景**:
- 企业智能办公助手平台：构建支持多 Agent 协作的智能办公系统，如数据分析、文档处理、日程管理 Agent 协同工作
- AI 应用快速原型开发：利用成熟的 Agent 框架和模型集成能力快速构建 AI 应用
- 智能客服与支持系统：实现问题分类、专业问答、情绪识别等不同 Agent 的分工协作



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,318 |
| 语言 | TypeScript |
| Forks | 5,193 |
| Issues | 145 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的革命性记忆插件，通过 AI 自动压缩编码会话上下文并跨会话注入，让 AI 助手真正拥有"记忆能力"，避免重复解释项目背景，大幅提升开发效率。Stars 高达 62,318 证明了其在 AI 编程工具领域的极高认可度。

**技术亮点**:
- 基于 Claude agent-sdk 实现智能上下文压缩，使用 AI 本身来压缩和提炼记忆内容
- 支持 ChromaDB、SQLite 等多种向量数据库，实现高效的语义检索和相似度匹配
- 集成 RAG（检索增强生成）技术和 Embeddings 向量化，精准召回相关历史上下文
- 采用 TypeScript 开发，提供完整的 Claude Code 插件架构，易于集成和扩展
- 实现长期记忆引擎，支持跨会话持久化存储，保持项目理解的连续性

**适用场景**:
- 大型项目开发：AI 能够在多周甚至数月的开发周期中记住架构决策、设计模式和之前解决的问题，避免重复踩坑
- 个人开发者效率提升：新会话自动理解项目结构、编码风格和技术栈，无需每次从头解释项目背景
- 复杂代码库维护：在处理遗留系统时，AI 能调用历史会话中的上下文信息，提供更准确的分析和修改建议



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,033 |
| 语言 | HTML |
| Forks | 20,953 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词聚合平台，前身是著名的Awesome ChatGPT Prompts项目，支持自托管部署，可帮助个人开发者和企业安全地管理内部提示词库，同时支持ChatGPT、Claude、Gemini等多款主流AI模型。

**技术亮点**:
- 基于Next.js + TypeScript现代技术栈构建，提供良好的开发体验和类型安全
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini等主流LLM
- 提供自托管部署选项，支持企业私有化部署保障数据隐私
- 采用开源架构设计，便于社区贡献和二次开发
- 汇集超过5000+高质量提示词模板，覆盖写作、编程、创意等多个领域

**适用场景**:
- 个人开发者：快速查找和学习高质量的AI提示词，提升与AI交互的效率
- 企业团队：自托管部署私有提示词库，保护商业机密和敏感数据
- AI爱好者/学习者：参考优秀提示词设计，理解prompt engineering最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,035 |
| 语言 | Jupyter Notebook |
| Forks | 13,990 |
| Issues | 3 |
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
| Stars | 54,625 |
| 语言 | TypeScript |
| Forks | 8,982 |
| Issues | 94 |
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
| Stars | 43,467 |
| 语言 | Python |
| Forks | 9,949 |
| Issues | 352 |
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
| Stars | 39,996 |
| 语言 | Python |
| Forks | 7,040 |
| Issues | 960 |
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
| Stars | 58,552 |
| 语言 | JavaScript |
| Forks | 6,335 |
| Issues | 337 |
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
| Stars | 71,445 |
| 语言 | Python |
| Forks | 8,987 |
| Issues | 419 |
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
| Stars | 52,559 |
| 语言 | TypeScript |
| Forks | 4,234 |
| Issues | 556 |
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
| Stars | 46,199 |
| 语言 | HTML |
| Forks | 4,511 |
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
| Stars | 52,042 |
| 语言 | TypeScript |
| Forks | 24,171 |
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
| Stars | 77,215 |
| 语言 | Python |
| Forks | 15,789 |
| Issues | 4,408 |
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
| Stars | 147,084 |
| 语言 | Python |
| Forks | 8,801 |
| Issues | 929 |
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
| Stars | 169,352 |
| 语言 | Go |
| Forks | 15,664 |
| Issues | 2,982 |
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
| Stars | 47,877 |
| 语言 | Rust |
| Forks | 9,549 |
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
| Stars | 34,144 |
| 语言 | Python |
| Forks | 2,151 |
| Issues | 96 |
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
| Stars | 111,909 |
| 语言 | Python |
| Forks | 7,203 |
| Issues | 610 |
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
| Stars | 67,402 |
| 语言 | Python |
| Forks | 6,870 |
| Issues | 117 |
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
| Stars | 70,268 |
| 语言 | Python |
| Forks | 8,600 |
| Issues | 977 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个功能强大的统一微调框架，支持100+主流大语言模型和视觉语言模型，提供LoRA、QLoRA、RLHF等多种高效微调方法，通过WebUI和CLI实现零代码微调，是目前最受欢迎的LLM微调开源项目。

**技术亮点**:
- 支持100+ LLMs & VLMs统一微调，包括LLaMA、LLaMA3、Qwen、DeepSeek、Gemma、ChatGLM等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、Peft、RLHF、DPO、KTO、ORPO等
- 支持多级量化（AWQ、GPTQ、GGUF），大幅降低显存占用和推理成本
- 提供WebUI可视化界面和CLI命令行两种使用方式，支持数据管理和训练监控
- 基于Transformers和PEFT库实现，模块化架构便于扩展新模型和训练方法

**适用场景**:
- 企业场景：快速基于自有数据微调领域专属大模型，应用于客服、知识库问答、内容生成等业务
- 学术研究：便捷进行指令微调、RLHF等实验，支持多种训练方法和评估指标
- 个人开发者：零代码微调开源模型，低成本定制个性化AI助手或特定任务模型



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,054 |
| 语言 | Python |
| Forks | 6,579 |
| Issues | 77 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是金融领域最成熟的开源数据平台之一，拥有 66K+ Stars，提供了覆盖股票、加密、期权、固定收益等多资产类别的统一数据接口，特别适合需要快速构建 AI 驱动金融应用的开发者。

**技术亮点**:
- 统一数据层：聚合多个数据源（Yahoo Finance、CoinGecko、FRED等），提供一致的 Python API 接口
- 全资产类别覆盖：支持股票、加密货币、期权、期货、固定收益、外汇和宏观经济数据
- 内置分析工具：提供技术指标、蜡烛图分析、财务报表分析、期权定价等金融分析功能
- AI/ML 原生支持：专为 AI agents 和机器学习工作流设计，支持 Pandas、NumPy 原生集成
- 可扩展架构：模块化设计，支持自定义数据源和分析函数，易于扩展新功能

**适用场景**:
- 量化交易研究：获取实时市场数据、计算技术指标、进行策略回测和因子分析
- 投资组合分析：多资产配置分析、风险评估、收益归因和报表生成
- AI 金融助手：构建基于 LLM 的智能投顾、自动化研报生成、实时市场问答系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,033 |
| 语言 | HTML |
| Forks | 20,953 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词聚合平台，前身是著名的Awesome ChatGPT Prompts项目，支持自托管部署，可帮助个人开发者和企业安全地管理内部提示词库，同时支持ChatGPT、Claude、Gemini等多款主流AI模型。

**技术亮点**:
- 基于Next.js + TypeScript现代技术栈构建，提供良好的开发体验和类型安全
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini等主流LLM
- 提供自托管部署选项，支持企业私有化部署保障数据隐私
- 采用开源架构设计，便于社区贡献和二次开发
- 汇集超过5000+高质量提示词模板，覆盖写作、编程、创意等多个领域

**适用场景**:
- 个人开发者：快速查找和学习高质量的AI提示词，提升与AI交互的效率
- 企业团队：自托管部署私有提示词库，保护商业机密和敏感数据
- AI爱好者/学习者：参考优秀提示词设计，理解prompt engineering最佳实践



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,035 |
| 语言 | Jupyter Notebook |
| Forks | 13,990 |
| Issues | 3 |
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
| Stars | 33,829 |
| 语言 | TypeScript |
| Forks | 3,670 |
| Issues | 293 |
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
| Stars | 159,574 |
| 语言 | Python |
| Forks | 32,910 |
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
| Stars | 77,215 |
| 语言 | Python |
| Forks | 15,789 |
| Issues | 4,408 |
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
| Stars | 109,195 |
| 语言 | Python |
| Forks | 12,686 |
| Issues | 4,002 |
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
| Stars | 99,247 |
| 语言 | Python |
| Forks | 27,525 |
| Issues | 18,472 |
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
| Stars | 33,699 |
| 语言 | Jupyter Notebook |
| Forks | 5,578 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 160,317 |
| 语言 | JavaScript |
| Forks | 24,944 |
| Issues | 120 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有超过16万Stars的大规模社区验证项目，为Claude Code、Codex、Cursor等主流AI编程工具提供Skills、Instincts、Memory等创新机制的性能优化框架，特别适合希望深度定制AI编程工作流的开发团队。

**技术亮点**:
- 多Agent引擎支持 - 统一兼容Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- Skills & Instincts系统 - 创新的行为模式库，通过预定义技能集让AI代理具备专业领域知识
- Memory管理架构 - 内置长期记忆系统，支持跨会话上下文保持和高效检索
- 安全沙箱机制 - 专为AI代理设计的安全防护层，支持细粒度权限控制
- Research-first开发方法论 - 强调实验驱动优化，提供性能基准测试工具

**适用场景**:
- 企业级AI编程平台集成 - 在组织内部署定制化AI编程助手，统一管理合规性和安全策略
- AI Agent开发研究 - 用于构建和测试新型AI代理架构，特别是MCP相关应用
- 个人开发者效率提升 - 优化本地AI编程工具的响应速度和任务完成质量



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,529 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，特别适合隐私敏感或需要离线部署的场景。其 Go 语言实现保证了高性能和易部署性，45k+ stars 的社区认可度证明了其成熟度和可靠性。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、视觉、语音、图像、视频等多种模型类型，包括 llama、mamba、stable-diffusion、musicgen 等主流模型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低部署门槛和成本
- Go 语言实现：提供高性能和轻量级部署，支持分布式和去中心化架构（基于 libp2p）
- 丰富的 API 接口：提供 OpenAI 兼容的 API，支持 agent、rerank 等高级功能，降低迁移成本
- MCP 协议支持：支持 Model Context Protocol，便于构建 AI agents 和自动化工作流

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等需要本地处理敏感数据的企业，可在不依赖云服务的情况下运行 AI 助手
- 边缘设备部署：在没有强大 GPU 的边缘服务器或工作站上部署 AI 应用，适用于工业物联网和远程办公场景
- 离线 AI 应用：为网络受限或需要完全离线运行的场景（如偏远地区、军事应用）提供完整的 AI 能力
- AI 开发原型验证：开发者可在本地快速测试和迭代 AI 应用，无需云服务订阅或 API 配额限制



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,445 |
| 语言 | Python |
| Forks | 8,987 |
| Issues | 419 |
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
| Stars | 52,559 |
| 语言 | TypeScript |
| Forks | 4,234 |
| Issues | 556 |
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
| Stars | 184,578 |
| 语言 | TypeScript |
| Forks | 56,920 |
| Issues | 1,514 |
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
| Stars | 157,509 |
| 语言 | Python |
| Forks | 12,998 |
| Issues | 2,479 |
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
| Stars | 97,372 |
| 语言 | Python |
| Forks | 9,092 |
| Issues | 177 |
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
| Stars | 81,301 |
| 语言 | Python |
| Forks | 9,453 |
| Issues | 259 |
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
| Stars | 184,004 |
| 语言 | TypeScript |
| Forks | 39,268 |
| Issues | 16,420 |
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
| Stars | 94,159 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 294 |
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
| Stars | 78,961 |
| 语言 | TypeScript |
| Forks | 5,811 |
| Issues | 763 |
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
| Stars | 77,176 |
| 语言 | TypeScript |
| Forks | 6,620 |
| Issues | 138 |
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
| Stars | 79,583 |
| 语言 | Go |
| Forks | 2,781 |
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
| Stars | 76,637 |
| 语言 | Go |
| Forks | 2,759 |
| Issues | 961 |
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
| Stars | 43,900 |
| 语言 | Go |
| Forks | 8,282 |
| Issues | 969 |
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
| Stars | 43,713 |
| 语言 | Go |
| Forks | 3,122 |
| Issues | 365 |
| Topics | cli, cli-app, cobra, cobra-generator, cobra-library, command, command-cobra, command-line, commandline, go, golang, golang-application, golang-library, posix, posix-compliant-flags, subcommands |
| 许可证 | Apache License 2.0 |


### ⭐ 中优先级


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,593 |
| 语言 | JavaScript |
| Forks | 7,287 |
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
| Stars | 52,559 |
| 语言 | TypeScript |
| Forks | 4,234 |
| Issues | 556 |
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
| Stars | 184,578 |
| 语言 | TypeScript |
| Forks | 56,920 |
| Issues | 1,514 |
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
| Stars | 51,645 |
| 语言 | Go |
| Forks | 10,324 |
| Issues | 228 |
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
| Stars | 121,768 |
| 语言 | Go |
| Forks | 42,882 |
| Issues | 2,767 |
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
| Stars | 71,506 |
| 语言 | Go |
| Forks | 18,921 |
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
| Stars | 54,977 |
| 语言 | Go |
| Forks | 6,589 |
| Issues | 2,826 |
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
| Stars | 47,511 |
| 语言 | Go |
| Forks | 5,043 |
| Issues | 981 |
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
| Stars | 94,159 |
| 语言 | TypeScript |
| Forks | 9,418 |
| Issues | 294 |
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
| Stars | 76,961 |
| 语言 | TypeScript |
| Forks | 6,676 |
| Issues | 405 |
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
| Stars | 85,441 |
| 语言 | JavaScript |
| Forks | 7,654 |
| Issues | 722 |
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
| Stars | 69,918 |
| 语言 | Go |
| Forks | 1,916 |
| Issues | 321 |
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
| Stars | 62,761 |
| 语言 | Go |
| Forks | 5,923 |
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
| Stars | 58,969 |
| 语言 | Go |
| Forks | 4,280 |
| Issues | 18 |
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
| Stars | 85,441 |
| 语言 | JavaScript |
| Forks | 7,654 |
| Issues | 722 |
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
| Stars | 63,642 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 751 |
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
| Stars | 45,529 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能全面的开源本地 AI 引擎，支持在无需 GPU 的普通硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，特别适合隐私敏感或需要离线部署的场景。其 Go 语言实现保证了高性能和易部署性，45k+ stars 的社区认可度证明了其成熟度和可靠性。

**技术亮点**:
- 多模态模型支持：统一接口支持 LLMs、视觉、语音、图像、视频等多种模型类型，包括 llama、mamba、stable-diffusion、musicgen 等主流模型
- 无 GPU 依赖：可在 CPU 硬件上运行 AI 推理，大幅降低部署门槛和成本
- Go 语言实现：提供高性能和轻量级部署，支持分布式和去中心化架构（基于 libp2p）
- 丰富的 API 接口：提供 OpenAI 兼容的 API，支持 agent、rerank 等高级功能，降低迁移成本
- MCP 协议支持：支持 Model Context Protocol，便于构建 AI agents 和自动化工作流

**适用场景**:
- 隐私敏感场景：医疗、金融、法律等需要本地处理敏感数据的企业，可在不依赖云服务的情况下运行 AI 助手
- 边缘设备部署：在没有强大 GPU 的边缘服务器或工作站上部署 AI 应用，适用于工业物联网和远程办公场景
- 离线 AI 应用：为网络受限或需要完全离线运行的场景（如偏远地区、军事应用）提供完整的 AI 能力
- AI 开发原型验证：开发者可在本地快速测试和迭代 AI 应用，无需云服务订阅或 API 配额限制



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,372 |
| 语言 | Python |
| Forks | 9,092 |
| Issues | 177 |
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
| Stars | 87,282 |
| 语言 | Python |
| Forks | 33,822 |
| Issues | 435 |
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
| Stars | 100,073 |
| 语言 | TypeScript |
| Forks | 27,174 |
| Issues | 1,111 |
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
| Stars | 78,961 |
| 语言 | TypeScript |
| Forks | 5,811 |
| Issues | 763 |
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
| Stars | 68,948 |
| 语言 | JavaScript |
| Forks | 23,146 |
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
| Stars | 55,969 |
| 语言 | JavaScript |
| Forks | 10,214 |
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
| Stars | 51,802 |
| 语言 | JavaScript |
| Forks | 4,702 |
| Issues | 1,461 |
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
| Stars | 71,656 |
| 语言 | Go |
| Forks | 4,693 |
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
| Stars | 57,692 |
| 语言 | Go |
| Forks | 3,296 |
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
| Stars | 75,593 |
| 语言 | JavaScript |
| Forks | 7,287 |
| Issues | 715 |
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
| Stars | 88,341 |
| 语言 | Go |
| Forks | 8,573 |
| Issues | 674 |
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
| Stars | 101,074 |
| 语言 | TypeScript |
| Forks | 12,112 |
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
| Stars | 58,552 |
| 语言 | JavaScript |
| Forks | 6,335 |
| Issues | 337 |
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
| Stars | 43,852 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,127 |
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
| Stars | 51,645 |
| 语言 | Go |
| Forks | 10,324 |
| Issues | 228 |
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
| Stars | 160,033 |
| 语言 | HTML |
| Forks | 20,953 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词聚合平台，前身是著名的Awesome ChatGPT Prompts项目，支持自托管部署，可帮助个人开发者和企业安全地管理内部提示词库，同时支持ChatGPT、Claude、Gemini等多款主流AI模型。

**技术亮点**:
- 基于Next.js + TypeScript现代技术栈构建，提供良好的开发体验和类型安全
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini等主流LLM
- 提供自托管部署选项，支持企业私有化部署保障数据隐私
- 采用开源架构设计，便于社区贡献和二次开发
- 汇集超过5000+高质量提示词模板，覆盖写作、编程、创意等多个领域

**适用场景**:
- 个人开发者：快速查找和学习高质量的AI提示词，提升与AI交互的效率
- 企业团队：自托管部署私有提示词库，保护商业机密和敏感数据
- AI爱好者/学习者：参考优秀提示词设计，理解prompt engineering最佳实践



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,625 |
| 语言 | TypeScript |
| Forks | 8,982 |
| Issues | 94 |
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
| Stars | 38,235 |
| 语言 | Python |
| Forks | 4,540 |
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
| Stars | 89,737 |
| 语言 | TypeScript |
| Forks | 10,019 |
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
| Stars | 87,462 |
| 语言 | TypeScript |
| Forks | 8,877 |
| Issues | 1,649 |
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
| Stars | 127,503 |
| 语言 | JavaScript |
| Forks | 12,474 |
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
| Stars | 170,324 |
| 语言 | Go |
| Forks | 13,159 |
| Issues | 178 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


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
| Stars | 135,479 |
| 语言 | Unknown |
| Forks | 34,011 |
| Issues | 147 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,525 |
| 语言 | Shell |
| Forks | 13,185 |
| Issues | 99 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,240 |
| 语言 | Python |
| Forks | 6,578 |
| Issues | 71 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,038 |
| 语言 | Python |
| Forks | 13,259 |
| Issues | 129 |
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
| Stars | 89,130 |
| 语言 | Python |
| Forks | 7,673 |
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
| Stars | 385,678 |
| 语言 | Python |
| Forks | 66,111 |
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
| Stars | 114,901 |
| 语言 | TypeScript |
| Forks | 5,960 |
| Issues | 26 |
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
| Stars | 111,644 |
| 语言 | TypeScript |
| Forks | 8,134 |
| Issues | 270 |
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
| Stars | 54,651 |
| 语言 | JavaScript |
| Forks | 4,586 |
| Issues | 43 |
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
| Stars | 48,161 |
| 语言 | Go |
| Forks | 10,289 |
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
| Stars | 104,658 |
| 语言 | C++ |
| Forks | 17,009 |
| Issues | 1,521 |
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
| Stars | 76,163 |
| 语言 | TypeScript |
| Forks | 10,808 |
| Issues | 336 |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,479 |
| 语言 | Python |
| Forks | 1,628 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### multica-ai/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,535 |
| 语言 | Unknown |
| Forks | 4,926 |
| Issues | 62 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 293,056 |
| 语言 | Python |
| Forks | 27,710 |
| Issues | 17 |
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
| Stars | 219,784 |
| 语言 | Python |
| Forks | 50,356 |
| Issues | 928 |
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
| Stars | 97,984 |
| 语言 | Python |
| Forks | 12,060 |
| Issues | 119 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,111 |
| 语言 | Python |
| Forks | 7,220 |
| Issues | 485 |
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
| Stars | 86,087 |
| 语言 | Python |
| Forks | 37,269 |
| Issues | 3,647 |
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
| Stars | 77,673 |
| 语言 | Python |
| Forks | 45,145 |
| Issues | 1,279 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,977 |
| 语言 | Python |
| Forks | 16,860 |
| Issues | 23 |
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
| Stars | 443,142 |
| 语言 | TypeScript |
| Forks | 44,334 |
| Issues | 205 |
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
| Stars | 353,163 |
| 语言 | TypeScript |
| Forks | 43,949 |
| Issues | 14 |
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
| Stars | 121,352 |
| 语言 | TypeScript |
| Forks | 13,320 |
| Issues | 2,985 |
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
| Stars | 112,575 |
| 语言 | TypeScript |
| Forks | 8,576 |
| Issues | 1,827 |
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
| Stars | 108,580 |
| 语言 | TypeScript |
| Forks | 13,359 |
| Issues | 5,021 |
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
| Stars | 98,110 |
| 语言 | TypeScript |
| Forks | 5,419 |
| Issues | 681 |
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
| Stars | 97,815 |
| 语言 | TypeScript |
| Forks | 54,590 |
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
| Stars | 94,617 |
| 语言 | TypeScript |
| Forks | 5,199 |
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
| Stars | 84,042 |
| 语言 | TypeScript |
| Forks | 10,433 |
| Issues | 398 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,184 |
| 语言 | TypeScript |
| Forks | 7,591 |
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
| Stars | 79,987 |
| 语言 | TypeScript |
| Forks | 8,068 |
| Issues | 712 |
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
| Stars | 244,574 |
| 语言 | JavaScript |
| Forks | 50,969 |
| Issues | 1,236 |
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
| Forks | 26,717 |
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
| Stars | 116,798 |
| 语言 | JavaScript |
| Forks | 35,379 |
| Issues | 2,624 |
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
| Stars | 112,040 |
| 语言 | JavaScript |
| Forks | 36,323 |
| Issues | 531 |
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
| Stars | 109,040 |
| 语言 | JavaScript |
| Forks | 11,647 |
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
| Stars | 98,193 |
| 语言 | JavaScript |
| Forks | 32,680 |
| Issues | 1,571 |
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
| Stars | 95,619 |
| 语言 | JavaScript |
| Forks | 15,371 |
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
| Stars | 86,340 |
| 语言 | JavaScript |
| Forks | 4,887 |
| Issues | 992 |
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
| Stars | 71,034 |
| 语言 | JavaScript |
| Forks | 16,808 |
| Issues | 893 |
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
| Stars | 67,369 |
| 语言 | JavaScript |
| Forks | 11,965 |
| Issues | 551 |
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
| Stars | 66,332 |
| 语言 | JavaScript |
| Forks | 9,192 |
| Issues | 1 |
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
| Stars | 65,832 |
| 语言 | JavaScript |
| Forks | 9,373 |
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
| Stars | 62,842 |
| 语言 | JavaScript |
| Forks | 4,017 |
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
| Stars | 60,523 |
| 语言 | JavaScript |
| Forks | 5,652 |
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
| Stars | 59,837 |
| 语言 | JavaScript |
| Forks | 20,479 |
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
| Stars | 57,422 |
| 语言 | JavaScript |
| Forks | 12,303 |
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
| Stars | 53,152 |
| 语言 | JavaScript |
| Forks | 10,601 |
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
| Stars | 52,555 |
| 语言 | JavaScript |
| Forks | 11,476 |
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
| Stars | 133,519 |
| 语言 | Go |
| Forks | 18,934 |
| Issues | 9,975 |
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
| Stars | 106,007 |
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
| Stars | 87,664 |
| 语言 | Go |
| Forks | 8,237 |
| Issues | 249 |
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
| Stars | 81,855 |
| 语言 | Go |
| Forks | 4,998 |
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
| Stars | 68,623 |
| 语言 | Go |
| Forks | 3,218 |
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
| Stars | 56,710 |
| 语言 | Go |
| Forks | 5,042 |
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
| Stars | 50,988 |
| 语言 | Go |
| Forks | 21,888 |
| Issues | 398 |
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
| Forks | 7,950 |
| Issues | 559 |
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
| Stars | 46,000 |
| 语言 | Go |
| Forks | 3,794 |
| Issues | 83 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
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
| Stars | 343,220 |
| 语言 | Python |
| Forks | 55,450 |
| Issues | 529 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,846 |
| 语言 | TypeScript |
| Forks | 16,501 |
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
| Stars | 79,075 |
| 语言 | JavaScript |
| Forks | 32,581 |
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
| Stars | 61,315 |
| 语言 | JavaScript |
| Forks | 7,138 |
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
| Stars | 151,773 |
| 语言 | Python |
| Forks | 11,549 |
| Issues | 328 |
| Topics | awesome, github, hellogithub, python |
