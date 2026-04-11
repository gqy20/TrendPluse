# 项目发现报告 (2026-04-11)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
| 去重移除 | 30 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 29 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 15 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
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
| Stars | 131,288 |
| 语言 | Python |
| Forks | 18,626 |
| Issues | 352 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能强大的开源 LLM 交互界面，支持 Ollama、OpenAI API 等多种后端，131k+ Stars 证明了其成熟度和社区认可度。它让用户无需编程即可通过直观的 Web UI 与各种大语言模型交互，同时支持 RAG 和自托管部署，是个人开发者和企业构建私有 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 提供商，支持本地和云端部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 LLM 回答准确性
- 模型上下文协议(MCP)：支持 MCP 扩展，可连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，数据完全自主掌控，满足隐私合规需求
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时对话、代码高亮、Markdown 渲染

**适用场景**:
- 个人 AI 助手：本地部署私有 ChatGPT 替代品，支持自定义知识库和人格设定
- 企业级 AI 平台：构建内部 LLM 应用，支持文档问答、代码助手等场景
- 开发者集成：作为前端界面集成到现有产品中，支持 OpenAPI 扩展



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,783 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 3,231 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（77k+ stars），它创新性地将 RAG 与 AI Agent 深度融合，不仅提供精准的检索增强能力，还支持复杂的多跳推理和深度研究工作流，为构建企业级知识问答和智能文档分析系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 深度融合架构：支持将 RAG 检索结果无缝注入 Agent 推理链，实现检索→理解→执行的闭环能力
- 强大的文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式文档的智能解析和向量化，保留文档结构信息
- GraphRAG 支持：集成图知识图谱增强技术，能够发现实体间的复杂关系，提升知识关联性
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek 等主流 LLM，支持 MCP 协议和本地部署
- 可视化知识库管理：提供直观的 UI 界面用于知识库构建、配置管理和对话测试

**适用场景**:
- 企业级智能问答系统：构建支持复杂多轮对话的客服机器人，能够从海量企业文档中精准检索答案
- 智能文档分析与挖掘：自动处理和分析合同、报告、技术文档等，提取关键信息和关联知识
- 深度研究助手：支持复杂主题的多跳推理和信息综合，适用于学术研究、市场分析等需要深度探索的场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Power AI agents with clean web data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,462 |
| 语言 | TypeScript |
| Forks | 6,942 |
| Issues | 265 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一款专为 AI 应用设计的网页数据抓取工具，能够将任意网页转换为干净的 Markdown 格式，为 LLM 和 AI Agent 提供高质量、结构化的网络数据源，在 GitHub 拥有超过 10 万星标，是 AI 数据管道领域的明星项目。

**技术亮点**:
- HTML-to-Markdown 转换引擎：智能解析网页结构，将复杂 HTML 转换为 AI 可直接使用的干净 Markdown 格式
- AI 优先设计：专为 LLM 和 AI Agent 场景优化，输出的数据结构化程度高，大幅减少 token 消耗
- 智能内容提取：自动识别网页中的核心内容，过滤广告、导航栏等噪音元素
- 支持动态渲染：能够处理 JavaScript 渲染的 SPA 应用和需要登录认证的页面
- Scalable 架构设计：基于 TypeScript 构建，提供 RESTful API 接口，便于集成到现有 AI 应用流水线中

**适用场景**:
- AI Agent 数据获取：为 AI Agent 提供可靠的网络信息检索能力，让 Agent 能够实时抓取并理解网页内容
- LLM 训练与 RAG 数据准备：将大规模网页数据转换为结构化文本，用于检索增强生成（RAG）系统的知识库构建
- AI 搜索与问答系统：构建基于最新网络内容的智能搜索服务，实时抓取目标网站数据供 AI 分析处理



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,177 |
| 语言 | JavaScript |
| Forks | 23,420 |
| Issues | 63 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI Agent 性能优化系统，支持 Claude Code、Cursor、Codex 等主流 AI 编程工具，拥有超过 15 万 Stars，是提升开发团队 AI 编码效率的完整解决方案。

**技术亮点**:
- 多 AI 编程工具兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化接口
- Memory 系统：实现持久化上下文管理，让 AI Agent 能够跨会话保持记忆和状态
- Skills & Instincts 机制：可扩展的技能库和本能行为系统，快速适配新任务场景
- Security First：内置安全机制，确保 AI Agent 操作的安全性和可控性
- Research-First 开发模式：整合研究驱动的开发流程，优化 AI 推理和响应质量

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编程工具，优化团队协作效率，降低 AI 使用成本
- 个人开发者：快速构建高性能 AI 辅助编码环境，提升个人开发生产力和代码质量
- AI Agent 研究者：基于该框架研究多 Agent 协作、记忆系统和安全控制等前沿技术



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,258 |
| 语言 | Go |
| Forks | 3,919 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源本地AI推理引擎，支持在任意硬件上运行LLM、图像、语音、视频等多模态模型，无需GPU即可部署，是企业私有化AI和个人开发者本地AI开发的理想选择。

**技术亮点**:
- 多模态模型支持：覆盖LLM、图像生成、语音合成、目标检测等全场景AI能力
- Go语言高性能架构：利用Go的并发特性和跨平台能力实现高效模型推理
- libp2p去中心化网络：支持分布式部署和P2P通信，构建去中心化AI基础设施
- MCP (Model Context Protocol) 协议支持：实现标准化的模型上下文交互
- 无GPU依赖运行：支持CPU推理，降低硬件门槛，提升可访问性

**适用场景**:
- 企业私有化AI部署：构建内部AI服务，保障数据隐私，降低API调用成本
- 本地开发与测试：开发者在本地环境快速验证AI功能，无需依赖云服务
- 边缘计算与离线场景：在边缘设备或网络受限环境中部署AI推理能力



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,055 |
| 语言 | TypeScript |
| Forks | 14,899 |
| Issues | 645 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的 AI Agent 协作平台，支持多 Agent 团队协作设计，拥有 75k+ Stars 的成熟社区生态，兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合企业快速搭建智能 Agent 工作流。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工与协作
- 多模型统一接入：整合 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型 API
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成
- 知识库集成：内置 RAG 能力，支持私有知识库检索增强
- TypeScript 全栈架构：从前端到后端完整 TypeScript 实现，类型安全且易于维护

**适用场景**:
- 企业智能助手平台：构建多 Agent 团队处理客户服务、数据分析、文档处理等企业级任务
- 开发者 AI 应用开发：快速原型验证基于多 Agent 架构的 AI 应用，支持本地部署
- 个人 AI 助手：整合多个 AI 模型能力，打造私人知识助手和任务自动化工具



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,932 |
| 语言 | Python |
| Forks | 8,531 |
| Issues | 967 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是最受欢迎的 LLM 微调框架之一，支持 100+ 大语言模型和视觉语言模型的统一高效微调，获得了 NLP 顶会 ACL 2024 的学术认可，集成 LoRA、QLoRA、RLHF 等多种微调技术，大幅降低了大模型定制化训练的门槛。

**技术亮点**:
- 多模型统一框架：支持 Llama、Qwen、Gemma、DeepSeek、GLM 等 100+ 主流 LLMs 和 VLMs，提供统一的训练接口
- 丰富的微调方法：集成 LoRA、QLoRA、RLHF、P-Tuning 等多种 PEFT 技术，满足不同场景的微调需求
- 高效量化支持：内置 4-bit/8-bit 量化训练，大幅降低显存占用，使消费级 GPU 也能微调大模型
- MoE 模型支持：原生支持混合专家（Mixture of Experts）架构模型的微调
- ACL 2024 学术验证：项目成果发表于国际顶会，技术方案经过学术同行评审认可

**适用场景**:
- 企业级 AI 应用定制：企业可基于 LlamaFactory 对开源大模型进行领域适配，构建专属的行业垂直应用
- 学术研究与实验：研究人员可以快速对比不同微调方法（LoRA vs RLHF 等）在各类模型上的效果差异
- 个人开发者低成本实践：借助量化技术，个人开发者仅需单卡即可对 7B-70B 参数模型进行微调实验



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,119 |
| 语言 | Python |
| Forks | 7,704 |
| Issues | 3,082 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个高人气的多模型AI代理框架（58k+ stars），支持Anthropic Claude、OpenAI GPT、Codex等多主流AI提供商，提供统一的代理接口和灵活的工具调用机制，适合需要快速构建智能自动化流程的企业和个人开发者。

**技术亮点**:
- 多AI模型支持：集成Anthropic Claude、OpenAI GPT、Codex等主流大语言模型，提供统一的API抽象层
- 模块化工具系统：支持自定义工具扩展，可灵活集成外部API、数据库、文件系统等资源
- MIT开源许可证：完全开源，可自由用于商业项目，降低使用门槛
- Python原生实现：基于Python生态，便于与现有AI/ML项目集成（如LangChain、Hugging Face等）
- 自动化代理框架：内置任务规划、记忆管理和多轮对话能力，支持复杂任务的自主分解与执行

**适用场景**:
- 企业级智能客服：构建支持多模型切换的客服代理，实现自动问答、工单处理和知识库检索
- 开发者效率工具：集成到IDE或CLI中，实现代码自动补全、代码审查和自动化测试生成（Codex集成）
- 个人AI助手：打造本地化或云端部署的个人助手，支持日程管理、信息聚合和跨平台任务自动化
- 研究与实验平台：用于AI Agent、LLM编排和多智能体系统的学术研究与原型开发



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,707 |
| 语言 | TypeScript |
| Forks | 8,440 |
| Issues | 75 |
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
| Stars | 48,048 |
| 语言 | TypeScript |
| Forks | 3,733 |
| Issues | 191 |
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
| Stars | 42,977 |
| 语言 | Python |
| Forks | 9,891 |
| Issues | 359 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,075 |
| 语言 | Python |
| Forks | 6,825 |
| Issues | 948 |
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
| Stars | 45,810 |
| 语言 | Java |
| Forks | 15,899 |
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
| Stars | 38,954 |
| 语言 | Python |
| Forks | 6,185 |
| Issues | 76 |
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
| Stars | 35,351 |
| 语言 | Python |
| Forks | 4,147 |
| Issues | 90 |
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
| Stars | 33,708 |
| 语言 | TypeScript |
| Forks | 3,645 |
| Issues | 290 |
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
| Stars | 58,086 |
| 语言 | JavaScript |
| Forks | 6,277 |
| Issues | 320 |
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
| Stars | 71,022 |
| 语言 | Python |
| Forks | 8,917 |
| Issues | 399 |
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
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 4,047 |
| Issues | 493 |
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
| Stars | 87,216 |
| 语言 | Python |
| Forks | 10,051 |
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
| Stars | 51,779 |
| 语言 | TypeScript |
| Forks | 24,117 |
| Issues | 805 |
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
| Stars | 183,587 |
| 语言 | TypeScript |
| Forks | 56,691 |
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
| Stars | 154,839 |
| 语言 | Java |
| Forks | 46,147 |
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
| Stars | 146,812 |
| 语言 | Python |
| Forks | 8,746 |
| Issues | 948 |
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
| Stars | 56,444 |
| 语言 | Jupyter Notebook |
| Forks | 19,518 |
| Issues | 28 |
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
| Stars | 34,016 |
| 语言 | Python |
| Forks | 2,129 |
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
| Stars | 33,410 |
| 语言 | Jupyter Notebook |
| Forks | 5,522 |
| Issues | 126 |
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
| Stars | 105,144 |
| 语言 | Python |
| Forks | 15,343 |
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
| Stars | 42,939 |
| 语言 | Rust |
| Forks | 2,703 |
| Issues | 454 |
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
| Stars | 131,288 |
| 语言 | Python |
| Forks | 18,626 |
| Issues | 352 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能强大的开源 LLM 交互界面，支持 Ollama、OpenAI API 等多种后端，131k+ Stars 证明了其成熟度和社区认可度。它让用户无需编程即可通过直观的 Web UI 与各种大语言模型交互，同时支持 RAG 和自托管部署，是个人开发者和企业构建私有 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 提供商，支持本地和云端部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 LLM 回答准确性
- 模型上下文协议(MCP)：支持 MCP 扩展，可连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，数据完全自主掌控，满足隐私合规需求
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时对话、代码高亮、Markdown 渲染

**适用场景**:
- 个人 AI 助手：本地部署私有 ChatGPT 替代品，支持自定义知识库和人格设定
- 企业级 AI 平台：构建内部 LLM 应用，支持文档问答、代码助手等场景
- 开发者集成：作为前端界面集成到现有产品中，支持 OpenAPI 扩展



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,783 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 3,231 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（77k+ stars），它创新性地将 RAG 与 AI Agent 深度融合，不仅提供精准的检索增强能力，还支持复杂的多跳推理和深度研究工作流，为构建企业级知识问答和智能文档分析系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 深度融合架构：支持将 RAG 检索结果无缝注入 Agent 推理链，实现检索→理解→执行的闭环能力
- 强大的文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式文档的智能解析和向量化，保留文档结构信息
- GraphRAG 支持：集成图知识图谱增强技术，能够发现实体间的复杂关系，提升知识关联性
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek 等主流 LLM，支持 MCP 协议和本地部署
- 可视化知识库管理：提供直观的 UI 界面用于知识库构建、配置管理和对话测试

**适用场景**:
- 企业级智能问答系统：构建支持复杂多轮对话的客服机器人，能够从海量企业文档中精准检索答案
- 智能文档分析与挖掘：自动处理和分析合同、报告、技术文档等，提取关键信息和关联知识
- 深度研究助手：支持复杂主题的多跳推理和信息综合，适用于学术研究、市场分析等需要深度探索的场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,055 |
| 语言 | TypeScript |
| Forks | 14,899 |
| Issues | 645 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的 AI Agent 协作平台，支持多 Agent 团队协作设计，拥有 75k+ Stars 的成熟社区生态，兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合企业快速搭建智能 Agent 工作流。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工与协作
- 多模型统一接入：整合 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型 API
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成
- 知识库集成：内置 RAG 能力，支持私有知识库检索增强
- TypeScript 全栈架构：从前端到后端完整 TypeScript 实现，类型安全且易于维护

**适用场景**:
- 企业智能助手平台：构建多 Agent 团队处理客户服务、数据分析、文档处理等企业级任务
- 开发者 AI 应用开发：快速原型验证基于多 Agent 架构的 AI 应用，支持本地部署
- 个人 AI 助手：整合多个 AI 模型能力，打造私人知识助手和任务自动化工具



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,048 |
| 语言 | TypeScript |
| Forks | 3,733 |
| Issues | 191 |
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
| Stars | 45,810 |
| 语言 | Java |
| Forks | 15,899 |
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
| Stars | 38,954 |
| 语言 | Python |
| Forks | 6,185 |
| Issues | 76 |
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
| Stars | 35,351 |
| 语言 | Python |
| Forks | 4,147 |
| Issues | 90 |
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
| Stars | 33,708 |
| 语言 | TypeScript |
| Forks | 3,645 |
| Issues | 290 |
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
| Stars | 100,677 |
| 语言 | TypeScript |
| Forks | 12,045 |
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
| Stars | 58,086 |
| 语言 | JavaScript |
| Forks | 6,277 |
| Issues | 320 |
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
| Stars | 75,383 |
| 语言 | Python |
| Forks | 10,228 |
| Issues | 242 |
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
| Stars | 51,779 |
| 语言 | TypeScript |
| Forks | 24,117 |
| Issues | 805 |
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
| Stars | 43,735 |
| 语言 | Go |
| Forks | 3,950 |
| Issues | 1,144 |
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
| Stars | 32,933 |
| 语言 | Python |
| Forks | 4,691 |
| Issues | 205 |
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
| Stars | 34,016 |
| 语言 | Python |
| Forks | 2,129 |
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
| Stars | 33,410 |
| 语言 | Jupyter Notebook |
| Forks | 5,522 |
| Issues | 126 |
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
| Stars | 105,144 |
| 语言 | Python |
| Forks | 15,343 |
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
| Stars | 131,288 |
| 语言 | Python |
| Forks | 18,626 |
| Issues | 352 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能强大的开源 LLM 交互界面，支持 Ollama、OpenAI API 等多种后端，131k+ Stars 证明了其成熟度和社区认可度。它让用户无需编程即可通过直观的 Web UI 与各种大语言模型交互，同时支持 RAG 和自托管部署，是个人开发者和企业构建私有 AI 应用的理想选择。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、Azure OpenAI 等多种 LLM 提供商，支持本地和云端部署
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 LLM 回答准确性
- 模型上下文协议(MCP)：支持 MCP 扩展，可连接外部工具和数据源
- 自托管部署：支持 Docker 一键部署，数据完全自主掌控，满足隐私合规需求
- 现代 Web 架构：基于 Python 构建，提供响应式 UI，支持实时对话、代码高亮、Markdown 渲染

**适用场景**:
- 个人 AI 助手：本地部署私有 ChatGPT 替代品，支持自定义知识库和人格设定
- 企业级 AI 平台：构建内部 LLM 应用，支持文档问答、代码助手等场景
- 开发者集成：作为前端界面集成到现有产品中，支持 OpenAPI 扩展



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,783 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 3,231 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最活跃的 RAG 开源项目之一（77k+ stars），它创新性地将 RAG 与 AI Agent 深度融合，不仅提供精准的检索增强能力，还支持复杂的多跳推理和深度研究工作流，为构建企业级知识问答和智能文档分析系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 深度融合架构：支持将 RAG 检索结果无缝注入 Agent 推理链，实现检索→理解→执行的闭环能力
- 强大的文档理解引擎：支持 PDF、Word、Excel、PPT 等多格式文档的智能解析和向量化，保留文档结构信息
- GraphRAG 支持：集成图知识图谱增强技术，能够发现实体间的复杂关系，提升知识关联性
- 多模型灵活接入：兼容 OpenAI、Ollama、DeepSeek 等主流 LLM，支持 MCP 协议和本地部署
- 可视化知识库管理：提供直观的 UI 界面用于知识库构建、配置管理和对话测试

**适用场景**:
- 企业级智能问答系统：构建支持复杂多轮对话的客服机器人，能够从海量企业文档中精准检索答案
- 智能文档分析与挖掘：自动处理和分析合同、报告、技术文档等，提取关键信息和关联知识
- 深度研究助手：支持复杂主题的多跳推理和信息综合，适用于学术研究、市场分析等需要深度探索的场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,177 |
| 语言 | JavaScript |
| Forks | 23,420 |
| Issues | 63 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI Agent 性能优化系统，支持 Claude Code、Cursor、Codex 等主流 AI 编程工具，拥有超过 15 万 Stars，是提升开发团队 AI 编码效率的完整解决方案。

**技术亮点**:
- 多 AI 编程工具兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化接口
- Memory 系统：实现持久化上下文管理，让 AI Agent 能够跨会话保持记忆和状态
- Skills & Instincts 机制：可扩展的技能库和本能行为系统，快速适配新任务场景
- Security First：内置安全机制，确保 AI Agent 操作的安全性和可控性
- Research-First 开发模式：整合研究驱动的开发流程，优化 AI 推理和响应质量

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编程工具，优化团队协作效率，降低 AI 使用成本
- 个人开发者：快速构建高性能 AI 辅助编码环境，提升个人开发生产力和代码质量
- AI Agent 研究者：基于该框架研究多 Agent 协作、记忆系统和安全控制等前沿技术



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,055 |
| 语言 | TypeScript |
| Forks | 14,899 |
| Issues | 645 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是目前最完整的 AI Agent 协作平台，支持多 Agent 团队协作设计，拥有 75k+ Stars 的成熟社区生态，兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合企业快速搭建智能 Agent 工作流。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，实现复杂任务的分工与协作
- 多模型统一接入：整合 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型 API
- MCP (Model Context Protocol) 支持：标准化的模型上下文协议，便于扩展和集成
- 知识库集成：内置 RAG 能力，支持私有知识库检索增强
- TypeScript 全栈架构：从前端到后端完整 TypeScript 实现，类型安全且易于维护

**适用场景**:
- 企业智能助手平台：构建多 Agent 团队处理客户服务、数据分析、文档处理等企业级任务
- 开发者 AI 应用开发：快速原型验证基于多 Agent 架构的 AI 应用，支持本地部署
- 个人 AI 助手：整合多个 AI 模型能力，打造私人知识助手和任务自动化工具



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,119 |
| 语言 | Python |
| Forks | 7,704 |
| Issues | 3,082 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

NousResearch/hermes-agent 是一个高人气的多模型AI代理框架（58k+ stars），支持Anthropic Claude、OpenAI GPT、Codex等多主流AI提供商，提供统一的代理接口和灵活的工具调用机制，适合需要快速构建智能自动化流程的企业和个人开发者。

**技术亮点**:
- 多AI模型支持：集成Anthropic Claude、OpenAI GPT、Codex等主流大语言模型，提供统一的API抽象层
- 模块化工具系统：支持自定义工具扩展，可灵活集成外部API、数据库、文件系统等资源
- MIT开源许可证：完全开源，可自由用于商业项目，降低使用门槛
- Python原生实现：基于Python生态，便于与现有AI/ML项目集成（如LangChain、Hugging Face等）
- 自动化代理框架：内置任务规划、记忆管理和多轮对话能力，支持复杂任务的自主分解与执行

**适用场景**:
- 企业级智能客服：构建支持多模型切换的客服代理，实现自动问答、工单处理和知识库检索
- 开发者效率工具：集成到IDE或CLI中，实现代码自动补全、代码审查和自动化测试生成（Codex集成）
- 个人AI助手：打造本地化或云端部署的个人助手，支持日程管理、信息聚合和跨平台任务自动化
- 研究与实验平台：用于AI Agent、LLM编排和多智能体系统的学术研究与原型开发



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,303 |
| 语言 | HTML |
| Forks | 20,860 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是最受欢迎的 AI 提示词集合项目（超 15 万星），支持 ChatGPT/Claude/Gemini 等多模型，社区驱动的开源平台允许完全自托管部署，在保障隐私的同时汇聚集体智慧。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈
- 多模型支持：兼容 ChatGPT、Claude、Gemini 等主流 LLM
- 支持自托管部署，数据完全私有化，适合企业级应用
- 社区驱动的提示词贡献模式，经过真实使用验证
- 项目开源（Other 许可证），便于二次开发和集成

**适用场景**:
- AI 爱好者和学习者：快速获取高质量提示词，提升 AI 对话效率
- 企业团队：自托管部署，在完全私有环境中使用社区优质提示词
- AI 应用开发者：参考项目架构，将提示词管理功能集成到自有产品



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,524 |
| 语言 | Jupyter Notebook |
| Forks | 13,879 |
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
| Stars | 51,707 |
| 语言 | TypeScript |
| Forks | 8,440 |
| Issues | 75 |
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
| Stars | 48,048 |
| 语言 | TypeScript |
| Forks | 3,733 |
| Issues | 191 |
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
| Stars | 42,977 |
| 语言 | Python |
| Forks | 9,891 |
| Issues | 359 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,075 |
| 语言 | Python |
| Forks | 6,825 |
| Issues | 948 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### hesreallyhim/awesome-claude-code

**描述**: A curated list of awesome skills, hooks, slash-commands, agent orchestrators, applications, and plugins for Claude Code by Anthropic

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,037 |
| 语言 | Python |
| Forks | 3,085 |
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
| Stars | 58,086 |
| 语言 | JavaScript |
| Forks | 6,277 |
| Issues | 320 |
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
| Stars | 71,022 |
| 语言 | Python |
| Forks | 8,917 |
| Issues | 399 |
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
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 4,047 |
| Issues | 493 |
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
| Stars | 51,779 |
| 语言 | TypeScript |
| Forks | 24,117 |
| Issues | 805 |
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
| Stars | 38,126 |
| 语言 | Unknown |
| Forks | 6,278 |
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
| Stars | 76,157 |
| 语言 | Python |
| Forks | 15,451 |
| Issues | 4,174 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,390 |
| 语言 | TypeScript |
| Forks | 4,010 |
| Issues | 1,097 |
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
| Stars | 146,812 |
| 语言 | Python |
| Forks | 8,746 |
| Issues | 948 |
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
| Stars | 168,602 |
| 语言 | Go |
| Forks | 15,528 |
| Issues | 2,910 |
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
| Stars | 47,699 |
| 语言 | Rust |
| Forks | 9,504 |
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
| Stars | 34,016 |
| 语言 | Python |
| Forks | 2,129 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 62,924 |
| 语言 | Python |
| Forks | 6,300 |
| Issues | 87 |
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
| Stars | 101,825 |
| 语言 | Python |
| Forks | 6,286 |
| Issues | 546 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
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
| Stars | 69,932 |
| 语言 | Python |
| Forks | 8,531 |
| Issues | 967 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是最受欢迎的 LLM 微调框架之一，支持 100+ 大语言模型和视觉语言模型的统一高效微调，获得了 NLP 顶会 ACL 2024 的学术认可，集成 LoRA、QLoRA、RLHF 等多种微调技术，大幅降低了大模型定制化训练的门槛。

**技术亮点**:
- 多模型统一框架：支持 Llama、Qwen、Gemma、DeepSeek、GLM 等 100+ 主流 LLMs 和 VLMs，提供统一的训练接口
- 丰富的微调方法：集成 LoRA、QLoRA、RLHF、P-Tuning 等多种 PEFT 技术，满足不同场景的微调需求
- 高效量化支持：内置 4-bit/8-bit 量化训练，大幅降低显存占用，使消费级 GPU 也能微调大模型
- MoE 模型支持：原生支持混合专家（Mixture of Experts）架构模型的微调
- ACL 2024 学术验证：项目成果发表于国际顶会，技术方案经过学术同行评审认可

**适用场景**:
- 企业级 AI 应用定制：企业可基于 LlamaFactory 对开源大模型进行领域适配，构建专属的行业垂直应用
- 学术研究与实验：研究人员可以快速对比不同微调方法（LoRA vs RLHF 等）在各类模型上的效果差异
- 个人开发者低成本实践：借助量化技术，个人开发者仅需单卡即可对 7B-70B 参数模型进行微调实验



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,715 |
| 语言 | Python |
| Forks | 6,526 |
| Issues | 76 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是最流行的开源金融分析平台之一，拥有 65K+ Stars，支持股票、加密货币、期权、固定收益等多品类金融数据分析，并深度集成 AI 和机器学习能力，为分析师、量化交易员和 AI 代理提供一站式金融数据解决方案。

**技术亮点**:
- 多品类金融数据覆盖：支持股票、加密货币、期权、衍生品、固定收益等全品类金融产品分析
- AI 与机器学习集成：内置 AI 代理支持和机器学习模型，便于智能投研和自动化分析
- 量化金融功能：提供专业的量化分析工具，支持策略回测和技术指标计算
- 模块化 Python 架构：基于 Python 构建，支持 SDK、API 和终端界面，生态完善易于扩展
- 全面的数据源集成：整合多个数据提供商，支持实时和历史数据访问

**适用场景**:
- 投资研究分析：金融分析师使用 OpenBB 进行股票筛选、行业研究、财务报表分析和市场趋势预测
- 量化策略开发：量化交易员利用平台进行策略回测、因子分析、风险管理和衍生品定价
- AI 金融代理：为 AI 代理和自动化交易系统提供金融数据接口和智能分析能力支持



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,303 |
| 语言 | HTML |
| Forks | 20,860 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是最受欢迎的 AI 提示词集合项目（超 15 万星），支持 ChatGPT/Claude/Gemini 等多模型，社区驱动的开源平台允许完全自托管部署，在保障隐私的同时汇聚集体智慧。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈
- 多模型支持：兼容 ChatGPT、Claude、Gemini 等主流 LLM
- 支持自托管部署，数据完全私有化，适合企业级应用
- 社区驱动的提示词贡献模式，经过真实使用验证
- 项目开源（Other 许可证），便于二次开发和集成

**适用场景**:
- AI 爱好者和学习者：快速获取高质量提示词，提升 AI 对话效率
- 企业团队：自托管部署，在完全私有环境中使用社区优质提示词
- AI 应用开发者：参考项目架构，将提示词管理功能集成到自有产品



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,524 |
| 语言 | Jupyter Notebook |
| Forks | 13,879 |
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
| Stars | 33,708 |
| 语言 | TypeScript |
| Forks | 3,645 |
| Issues | 290 |
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
| Stars | 159,203 |
| 语言 | Python |
| Forks | 32,835 |
| Issues | 2,362 |
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
| Stars | 76,157 |
| 语言 | Python |
| Forks | 15,451 |
| Issues | 4,174 |
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
| Stars | 108,437 |
| 语言 | Python |
| Forks | 12,571 |
| Issues | 3,958 |
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
| Stars | 99,034 |
| 语言 | Python |
| Forks | 27,462 |
| Issues | 18,446 |
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
| Stars | 33,410 |
| 语言 | Jupyter Notebook |
| Forks | 5,522 |
| Issues | 126 |
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
| Stars | 151,177 |
| 语言 | JavaScript |
| Forks | 23,420 |
| Issues | 63 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高度实用的 AI Agent 性能优化系统，支持 Claude Code、Cursor、Codex 等主流 AI 编程工具，拥有超过 15 万 Stars，是提升开发团队 AI 编码效率的完整解决方案。

**技术亮点**:
- 多 AI 编程工具兼容框架：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程助手，提供一致的优化接口
- Memory 系统：实现持久化上下文管理，让 AI Agent 能够跨会话保持记忆和状态
- Skills & Instincts 机制：可扩展的技能库和本能行为系统，快速适配新任务场景
- Security First：内置安全机制，确保 AI Agent 操作的安全性和可控性
- Research-First 开发模式：整合研究驱动的开发流程，优化 AI 推理和响应质量

**适用场景**:
- 企业级 AI 开发团队：统一管理多个 AI 编程工具，优化团队协作效率，降低 AI 使用成本
- 个人开发者：快速构建高性能 AI 辅助编码环境，提升个人开发生产力和代码质量
- AI Agent 研究者：基于该框架研究多 Agent 协作、记忆系统和安全控制等前沿技术



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,258 |
| 语言 | Go |
| Forks | 3,919 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源本地AI推理引擎，支持在任意硬件上运行LLM、图像、语音、视频等多模态模型，无需GPU即可部署，是企业私有化AI和个人开发者本地AI开发的理想选择。

**技术亮点**:
- 多模态模型支持：覆盖LLM、图像生成、语音合成、目标检测等全场景AI能力
- Go语言高性能架构：利用Go的并发特性和跨平台能力实现高效模型推理
- libp2p去中心化网络：支持分布式部署和P2P通信，构建去中心化AI基础设施
- MCP (Model Context Protocol) 协议支持：实现标准化的模型上下文交互
- 无GPU依赖运行：支持CPU推理，降低硬件门槛，提升可访问性

**适用场景**:
- 企业私有化AI部署：构建内部AI服务，保障数据隐私，降低API调用成本
- 本地开发与测试：开发者在本地环境快速验证AI功能，无需依赖云服务
- 边缘计算与离线场景：在边缘设备或网络受限环境中部署AI推理能力



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,022 |
| 语言 | Python |
| Forks | 8,917 |
| Issues | 399 |
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
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 4,047 |
| Issues | 493 |
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
| Stars | 183,587 |
| 语言 | TypeScript |
| Forks | 56,691 |
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
| Stars | 156,184 |
| 语言 | Python |
| Forks | 12,830 |
| Issues | 2,457 |
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
| Stars | 97,077 |
| 语言 | Python |
| Forks | 9,049 |
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
| Stars | 80,811 |
| 语言 | Python |
| Forks | 9,377 |
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
| Stars | 183,719 |
| 语言 | TypeScript |
| Forks | 39,127 |
| Issues | 16,200 |
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
| Stars | 94,084 |
| 语言 | TypeScript |
| Forks | 9,419 |
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
| Stars | 78,887 |
| 语言 | TypeScript |
| Forks | 5,790 |
| Issues | 754 |
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
| Stars | 77,053 |
| 语言 | TypeScript |
| Forks | 6,599 |
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
| Stars | 79,388 |
| 语言 | Go |
| Forks | 2,764 |
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
| Stars | 76,227 |
| 语言 | Go |
| Forks | 2,745 |
| Issues | 952 |
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
| Stars | 43,743 |
| 语言 | Go |
| Forks | 8,237 |
| Issues | 957 |
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
| Stars | 41,476 |
| 语言 | Go |
| Forks | 1,180 |
| Issues | 173 |
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
| Stars | 420,892 |
| 语言 | Python |
| Forks | 45,808 |
| Issues | 1,230 |
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
| Stars | 50,566 |
| 语言 | TypeScript |
| Forks | 4,047 |
| Issues | 493 |
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
| Stars | 183,587 |
| 语言 | TypeScript |
| Forks | 56,691 |
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
| Stars | 51,606 |
| 语言 | Go |
| Forks | 10,316 |
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
| Stars | 121,660 |
| 语言 | Go |
| Forks | 42,833 |
| Issues | 2,729 |
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
| Stars | 71,479 |
| 语言 | Go |
| Forks | 18,916 |
| Issues | 3,796 |
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
| Stars | 54,848 |
| 语言 | Go |
| Forks | 6,558 |
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
| Stars | 47,493 |
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
| Stars | 94,084 |
| 语言 | TypeScript |
| Forks | 9,419 |
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
| Stars | 76,571 |
| 语言 | TypeScript |
| Forks | 6,606 |
| Issues | 404 |
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
| Stars | 85,131 |
| 语言 | JavaScript |
| Forks | 7,628 |
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
| Stars | 69,820 |
| 语言 | Go |
| Forks | 1,909 |
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
| Stars | 62,651 |
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
| Stars | 58,745 |
| 语言 | Go |
| Forks | 4,256 |
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
| Stars | 85,131 |
| 语言 | JavaScript |
| Forks | 7,628 |
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
| Forks | 10,323 |
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
| Stars | 45,258 |
| 语言 | Go |
| Forks | 3,919 |
| Issues | 174 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源本地AI推理引擎，支持在任意硬件上运行LLM、图像、语音、视频等多模态模型，无需GPU即可部署，是企业私有化AI和个人开发者本地AI开发的理想选择。

**技术亮点**:
- 多模态模型支持：覆盖LLM、图像生成、语音合成、目标检测等全场景AI能力
- Go语言高性能架构：利用Go的并发特性和跨平台能力实现高效模型推理
- libp2p去中心化网络：支持分布式部署和P2P通信，构建去中心化AI基础设施
- MCP (Model Context Protocol) 协议支持：实现标准化的模型上下文交互
- 无GPU依赖运行：支持CPU推理，降低硬件门槛，提升可访问性

**适用场景**:
- 企业私有化AI部署：构建内部AI服务，保障数据隐私，降低API调用成本
- 本地开发与测试：开发者在本地环境快速验证AI功能，无需依赖云服务
- 边缘计算与离线场景：在边缘设备或网络受限环境中部署AI推理能力



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,077 |
| 语言 | Python |
| Forks | 9,049 |
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
| Stars | 87,253 |
| 语言 | Python |
| Forks | 33,814 |
| Issues | 436 |
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
| Stars | 100,035 |
| 语言 | TypeScript |
| Forks | 27,155 |
| Issues | 1,137 |
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
| Stars | 78,887 |
| 语言 | TypeScript |
| Forks | 5,790 |
| Issues | 754 |
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
| Stars | 68,924 |
| 语言 | JavaScript |
| Forks | 23,074 |
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
| Stars | 55,952 |
| 语言 | JavaScript |
| Forks | 10,215 |
| Issues | 363 |
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
| Stars | 51,780 |
| 语言 | JavaScript |
| Forks | 4,702 |
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
| Stars | 47,784 |
| 语言 | JavaScript |
| Forks | 1,582 |
| Issues | 659 |
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
| Stars | 88,281 |
| 语言 | Go |
| Forks | 8,576 |
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
| Stars | 71,447 |
| 语言 | Go |
| Forks | 4,694 |
| Issues | 252 |
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
| Stars | 57,540 |
| 语言 | Go |
| Forks | 3,278 |
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
| Stars | 41,476 |
| 语言 | Go |
| Forks | 1,180 |
| Issues | 173 |
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
| Stars | 420,892 |
| 语言 | Python |
| Forks | 45,808 |
| Issues | 1,230 |
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
| Stars | 100,677 |
| 语言 | TypeScript |
| Forks | 12,045 |
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
| Stars | 58,086 |
| 语言 | JavaScript |
| Forks | 6,277 |
| Issues | 320 |
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
| Stars | 43,735 |
| 语言 | Go |
| Forks | 3,950 |
| Issues | 1,144 |
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
| Stars | 51,606 |
| 语言 | Go |
| Forks | 10,316 |
| Issues | 231 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (9 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,303 |
| 语言 | HTML |
| Forks | 20,860 |
| Issues | 41 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

prompts.chat 是最受欢迎的 AI 提示词集合项目（超 15 万星），支持 ChatGPT/Claude/Gemini 等多模型，社区驱动的开源平台允许完全自托管部署，在保障隐私的同时汇聚集体智慧。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化技术栈
- 多模型支持：兼容 ChatGPT、Claude、Gemini 等主流 LLM
- 支持自托管部署，数据完全私有化，适合企业级应用
- 社区驱动的提示词贡献模式，经过真实使用验证
- 项目开源（Other 许可证），便于二次开发和集成

**适用场景**:
- AI 爱好者和学习者：快速获取高质量提示词，提升 AI 对话效率
- 企业团队：自托管部署，在完全私有环境中使用社区优质提示词
- AI 应用开发者：参考项目架构，将提示词管理功能集成到自有产品



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,707 |
| 语言 | TypeScript |
| Forks | 8,440 |
| Issues | 75 |
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
| Stars | 38,037 |
| 语言 | Python |
| Forks | 3,085 |
| Issues | 201 |
| Topics | agent-skills, agentic-code, agentic-coding, ai-workflow-optimization, ai-workflows, anthropic, anthropic-claude, awesome, awesome-claude-code, awesome-list, awesome-lists, awesome-resources, claude, claude-code, coding-agent, coding-agents, coding-assistant, coding-assistants, llm |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,351 |
| 语言 | Python |
| Forks | 4,147 |
| Issues | 90 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from ChatGPT (GPT-5.4, GPT-5.3, Codex), Claude (Opus 4.6, Sonnet 4.6, Claude Code), Gemini (3.1 Pro, 3 Flash, CLI), Grok (4.2, 4), Perplexity, and more. Updated regularly.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,126 |
| 语言 | Unknown |
| Forks | 6,278 |
| Issues | 18 |
| Topics | ai, ai-transparency, anthropic, chatgpt, claude, claude-code, gemini, generative-ai, gpt-5, grok, large-language-models, llm, openai, perplexity, prompt-engineering, system-prompt, system-prompts, xai |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,681 |
| 语言 | TypeScript |
| Forks | 9,997 |
| Issues | 2,242 |
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
| Stars | 87,280 |
| 语言 | TypeScript |
| Forks | 8,852 |
| Issues | 1,639 |
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
| Stars | 127,424 |
| 语言 | JavaScript |
| Forks | 12,473 |
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
| Stars | 169,703 |
| 语言 | Go |
| Forks | 13,137 |
| Issues | 177 |
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
| Stars | 78,334 |
| 语言 | Shell |
| Forks | 12,436 |
| Issues | 82 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,792 |
| 语言 | Python |
| Forks | 6,537 |
| Issues | 67 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,593 |
| 语言 | Python |
| Forks | 13,025 |
| Issues | 117 |
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
| Stars | 87,095 |
| 语言 | Python |
| Forks | 7,482 |
| Issues | 619 |
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
| Stars | 134,946 |
| 语言 | Unknown |
| Forks | 33,927 |
| Issues | 145 |
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
| Stars | 385,354 |
| 语言 | Python |
| Forks | 66,098 |
| Issues | 81 |
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
| Stars | 114,490 |
| 语言 | TypeScript |
| Forks | 5,891 |
| Issues | 365 |
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
| Stars | 109,783 |
| 语言 | TypeScript |
| Forks | 7,976 |
| Issues | 252 |
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
| Stars | 50,619 |
| 语言 | JavaScript |
| Forks | 4,223 |
| Issues | 26 |
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
| Stars | 48,122 |
| 语言 | Go |
| Forks | 10,282 |
| Issues | 1,895 |
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
| Stars | 103,123 |
| 语言 | C++ |
| Forks | 16,694 |
| Issues | 1,451 |
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
| Stars | 63,505 |
| 语言 | Python |
| Forks | 1,633 |
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
| Stars | 69,796 |
| 语言 | TypeScript |
| Forks | 9,785 |
| Issues | 336 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 291,753 |
| 语言 | Python |
| Forks | 27,643 |
| Issues | 20 |
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
| Stars | 219,510 |
| 语言 | Python |
| Forks | 50,320 |
| Issues | 920 |
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
| Stars | 85,999 |
| 语言 | Python |
| Forks | 37,214 |
| Issues | 3,586 |
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
| Stars | 77,674 |
| 语言 | Python |
| Forks | 45,155 |
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
| Stars | 76,808 |
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
| Stars | 442,629 |
| 语言 | TypeScript |
| Forks | 44,253 |
| Issues | 202 |
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
| Stars | 352,702 |
| 语言 | TypeScript |
| Forks | 43,904 |
| Issues | 7 |
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
| Stars | 138,655 |
| 语言 | TypeScript |
| Forks | 16,495 |
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
| Stars | 120,813 |
| 语言 | TypeScript |
| Forks | 13,235 |
| Issues | 2,953 |
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
| Stars | 112,115 |
| 语言 | TypeScript |
| Forks | 8,500 |
| Issues | 1,809 |
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
| Stars | 108,506 |
| 语言 | TypeScript |
| Forks | 13,339 |
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
| Stars | 97,747 |
| 语言 | TypeScript |
| Forks | 54,589 |
| Issues | 1,354 |
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
| Stars | 97,617 |
| 语言 | TypeScript |
| Forks | 5,360 |
| Issues | 700 |
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
| Stars | 94,503 |
| 语言 | TypeScript |
| Forks | 5,190 |
| Issues | 109 |
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
| Stars | 79,847 |
| 语言 | TypeScript |
| Forks | 8,050 |
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
| Stars | 244,422 |
| 语言 | JavaScript |
| Forks | 50,902 |
| Issues | 1,225 |
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
| Stars | 116,677 |
| 语言 | JavaScript |
| Forks | 35,315 |
| Issues | 2,600 |
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
| Stars | 111,870 |
| 语言 | JavaScript |
| Forks | 36,329 |
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
| Stars | 108,984 |
| 语言 | JavaScript |
| Forks | 11,616 |
| Issues | 267 |
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
| Stars | 98,124 |
| 语言 | JavaScript |
| Forks | 32,690 |
| Issues | 1,675 |
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
| Stars | 95,561 |
| 语言 | JavaScript |
| Forks | 15,345 |
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
| Stars | 86,279 |
| 语言 | JavaScript |
| Forks | 4,886 |
| Issues | 979 |
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
| Stars | 70,968 |
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
| Stars | 66,316 |
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
| Stars | 65,839 |
| 语言 | JavaScript |
| Forks | 9,380 |
| Issues | 209 |
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
| Stars | 60,366 |
| 语言 | JavaScript |
| Forks | 5,650 |
| Issues | 71 |
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
| Stars | 59,846 |
| 语言 | JavaScript |
| Forks | 20,480 |
| Issues | 96 |
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
| Stars | 57,429 |
| 语言 | JavaScript |
| Forks | 12,306 |
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
| Forks | 10,604 |
| Issues | 462 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,470 |
| 语言 | JavaScript |
| Forks | 11,456 |
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
| Stars | 48,623 |
| 语言 | JavaScript |
| Forks | 2,428 |
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
| Stars | 133,413 |
| 语言 | Go |
| Forks | 18,913 |
| Issues | 9,941 |
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
| Stars | 87,525 |
| 语言 | Go |
| Forks | 8,242 |
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
| Stars | 81,615 |
| 语言 | Go |
| Forks | 4,992 |
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
| Stars | 68,633 |
| 语言 | Go |
| Forks | 3,214 |
| Issues | 10 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,583 |
| 语言 | Go |
| Forks | 5,017 |
| Issues | 1,157 |
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
| Stars | 50,973 |
| 语言 | Go |
| Forks | 21,884 |
| Issues | 400 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 342,285 |
| 语言 | Python |
| Forks | 55,299 |
| Issues | 527 |
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
| Stars | 97,577 |
| 语言 | Python |
| Forks | 12,023 |
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
| Stars | 85,949 |
| 语言 | Python |
| Forks | 7,205 |
| Issues | 482 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,493 |
| 语言 | TypeScript |
| Forks | 10,333 |
| Issues | 738 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,075 |
| 语言 | TypeScript |
| Forks | 7,579 |
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
| Stars | 79,014 |
| 语言 | JavaScript |
| Forks | 32,411 |
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
| Stars | 62,676 |
| 语言 | JavaScript |
| Forks | 4,004 |
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
| Stars | 61,326 |
| 语言 | JavaScript |
| Forks | 7,130 |
| Issues | 140 |
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
| Stars | 105,801 |
| 语言 | Go |
| Forks | 14,986 |
| Issues | 46 |
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
| Stars | 50,606 |
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
| Stars | 49,294 |
| 语言 | Go |
| Forks | 7,957 |
| Issues | 563 |
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
| Stars | 150,380 |
| 语言 | Python |
| Forks | 11,439 |
| Issues | 322 |
| Topics | awesome, github, hellogithub, python |
