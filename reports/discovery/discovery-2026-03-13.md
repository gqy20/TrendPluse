# 项目发现报告 (2026-03-13)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
| 去重移除 | 32 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
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
| Stars | 127,048 |
| 语言 | Python |
| Forks | 17,964 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有 12.7 万 stars 的超人气自托管 AI 聊天界面，核心价值在于支持 Ollama、OpenAI API 等多种后端的统一接入，让用户能够快速部署私有化的 AI 对话平台，完美兼顾易用性与数据隐私控制。

**技术亮点**:
- 多后端统一支持：同时兼容 Ollama、OpenAI API 等主流 LLM 服务，灵活切换不同模型
- RAG（检索增强生成）内置支持：可在对话中结合私有知识库，提升回答准确性
- MCP（Model Context Protocol）协议支持：实现模型与外部工具/数据源的标准交互
- 完全自托管架构：用户可本地或私有云部署，数据完全自主可控
- 现代化 Web UI：Python 技术栈构建，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部 AI 助手：保护敏感数据不出内网，支持对接私有知识库
- 个人开发者学习与实验：低成本搭建本地 LLM 对话环境，支持 Ollama 本地模型
- 多模型对比测试：统一界面切换 OpenAI、本地模型等，便于效果评估



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,949 |
| 语言 | Python |
| Forks | 8,374 |
| Issues | 3,089 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（74K+ Stars），创新性地将检索增强生成与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层。支持 DeepSeek、OpenAI、Ollama 等多种模型，是企业级 RAG 应用的首选解决方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力，打造智能检索增强生成引擎，支持深度推理和自主决策
- 内置强大的文档解析与理解能力，支持复杂文档的结构化提取和知识图谱构建（GraphRAG）
- 支持 MCP 协议和多模型接入（DeepSeek-R1、OpenAI、Ollama），具备极强的生态兼容性
- 提供 Agentic Workflow 编排能力，支持复杂的多步骤推理和任务自动化流程
- 具备 AI Search 和 Deep Research 能力，适合构建企业级智能问答和知识库系统

**适用场景**:
- 企业知识库搭建：构建智能文档问答系统，支持复杂文档的解析、理解和检索
- AI Agent 开发：基于 RAG + Agent 能力开发智能助手，支持多轮对话和任务执行
- 智能搜索与深度研究：构建具备上下文理解能力的 AI 搜索引擎，支持 Deep Research 模式的深度信息挖掘



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,522 |
| 语言 | TypeScript |
| Forks | 6,409 |
| Issues | 207 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个拥有超过 9 万 star 的顶级开源项目，专门为 AI 应用设计，能够将任意网站内容转换为 LLM-ready 的 Markdown 或结构化数据，极大简化了 AI 应用开发中的数据准备流程，是构建 RAG、AI Agent 和知识库的必备工具。

**技术亮点**:
- 一键将复杂网页转换为 LLM 可直接使用的 Markdown 格式，支持 HTML-to-Markdown 智能转换
- 专为 AI 时代设计的 Web 爬虫和数据提取 API，支持 AI 搜索和 AI Agent 数据采集
- 支持将非结构化网页内容转化为结构化数据，便于后续 AI 模型处理和分析
- TypeScript 实现，易于集成和二次开发，活跃的开源社区支持
- AGPL v3.0 开源许可，代码完全透明，支持自托管部署

**适用场景**:
- 构建 RAG（检索增强生成）应用时需要从网站批量提取知识内容
- AI Agent 开发中需要实时抓取网页数据进行智能决策和分析
- 企业知识库建设，自动将官网、文档站等网页内容转换为 AI 可理解的格式
- 数据科学家和研究员从公开网站采集训练数据用于 LLM 微调
- 内容聚合平台和 AI 搜索引擎的网页数据预处理



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,632 |
| 语言 | JavaScript |
| Forks | 9,327 |
| Issues | 13 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个革命性的AI编程助手增强系统，为Claude Code、Cursor等主流AI开发工具提供了类似人类专家的"技能、直觉、记忆"能力，通过性能优化显著提升AI编程助手的开发效率和代码质量。74K+ Stars证明了其在AI辅助开发领域的巨大价值和社区认可度。

**技术亮点**:
- Agent Harness性能优化系统 - 提供技能、直觉、记忆三大核心能力模块，让AI助手具备专家级开发直觉
- Research-First开发方法论 - 优先研究最佳实践后再编码，提高代码质量和架构合理性
- 内置安全机制 - 针对AI生成代码的安全审查和防护体系
- 支持MCP协议集成 - 模型上下文协议，实现与多种AI开发工具的无缝对接
- 多平台兼容架构 - 同时支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具

**适用场景**:
- 企业开发团队：标准化AI辅助开发流程，提升团队整体编码效率和代码质量，降低技术债务
- 个人开发者：快速掌握AI编程工具的高级用法，将AI助手能力提升到专家级水平
- AI应用开发者：学习如何构建和优化AI Agent系统，理解性能调优和记忆机制的最佳实践



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,547 |
| 语言 | Go |
| Forks | 3,680 |
| Issues | 152 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全开源、免费且功能强大的本地 AI 解决方案，最大的亮点是**无需 GPU 即可在消费级硬件上运行**，同时提供与 OpenAI API 兼容的接口，让开发者能够以极低成本实现 AI 能力的私有化部署。它集成了文本生成、图像生成、语音克隆、视频生成等多种 AI 能力，并支持去中心化和 P2P 分布式推理，是目前最全面的本地 AI 替代方案之一。

**技术亮点**:
- 完全兼容 OpenAI API 标准，支持零代码迁移（Drop-in replacement）
- 无需 GPU，在消费级 CPU 硬件上即可运行，支持 GGUF、Transformers、Diffusers 等多种模型格式
- 多功能集成：文本生成、图像生成、语音克隆(TTS)、视频生成、音频生成、目标检测等一体化支持
- 支持分布式和 P2P 去中心化推理，基于 libp2p 实现节点间协作
- 原生支持 MCP（Model Context Protocol）和多种主流开源模型（Llama、Mistral、Gemma、RWKV、Mamba 等）

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保数据不出域，满足合规和隐私要求
- 个人开发者低成本 AI 应用：无需购买昂贵 GPU，在普通电脑上即可开发和测试 AI 功能
- 边缘计算与离线场景：在网络受限或无网络环境下使用 AI 能力，如 IoT 设备、移动端应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,586 |
| 语言 | TypeScript |
| Forks | 14,787 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI Agent 工作空间平台，73K+ Star 证明了其社区认可度。它突破了传统单一 AI 对话模式，创新性地引入多 Agent 协作和知识库管理，让用户能够像组建团队一样构建 AI 助手矩阵，显著提升复杂任务的解决效率。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工协作
- 统一多模型接入：支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型一站式集成
- 知识库管理 (Knowledge Base)：支持构建和管理私有知识库，增强 AI 上下文理解能力
- MCP 协议支持：兼容 Model Context Protocol，实现工具和数据的标准化调用
- 全栈 TypeScript 实现：现代化技术栈，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流：适合团队构建专属 AI 助手体系，处理客服、文档分析、数据分析等多场景任务
- AI Agent 开发平台：开发者可基于此快速搭建定制化 Agent 应用，降低多模型集成成本
- 个人知识管理与效率提升：个人用户可构建私有知识库，通过多 Agent 协作提升学习、写作、研究效率



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,543 |
| 语言 | MDX |
| Forks | 7,639 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程领域综合资源库，汇聚了来自顶尖学术机构和工业界的最佳实践，涵盖从基础Prompt Engineering到前沿AI Agents的完整知识体系。项目持续更新，整合了论文、实战笔记本、教程和工具资源，是AI开发者从入门到精通的必备参考指南。

**技术亮点**:
- 全面覆盖LLM开发三大核心技术：提示工程(Prompt Engineering)、检索增强生成(RAG)、AI智能体(Agents)
- 提供可执行的MDX Notebook，将理论学习与代码实践深度结合
- 系统整理了ChatGPT、OpenAI等主流模型的提示词最佳实践和设计模式
- 包含Generative AI领域的最新研究论文和技术进展追踪
- MIT开源许可，支持社区协作共建，资源质量有保障

**适用场景**:
- 企业AI应用开发：帮助团队快速掌握LLM应用开发技能，构建RAG系统、智能客服、AI Agent等生产级应用
- 个人学习进阶：适合AI工程师、开发者系统学习提示工程和LLM技术栈，从零基础到实战应用
- 学术研究参考：为研究人员提供Prompt Engineering和AI Agents领域的论文合集和技术综述



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,372 |
| 语言 | Python |
| Forks | 8,349 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一高效的大模型微调框架，支持100多种LLM和VLM模型，被ACL 2024收录。项目获得了68K+ Stars，是当前最流行的开源微调工具之一，通过集成LoRA、QLoRA、量化、RLHF等前沿技术，大幅降低了大模型训练的技术门槛和硬件成本。

**技术亮点**:
- 支持100+主流大模型统一微调，包括LLaMA、Qwen、DeepSeek、Gemma、GPT系列等，提供一站式训练体验
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、全量微调，以及4/8bit量化训练，显著降低显存需求
- 支持全流程训练方法：指令微调(Instruction Tuning)、预训练、RLHF强化学习人类反馈对齐
- 兼容MoE混合专家模型架构，适配最新的大模型技术趋势
- 提供Agent开发能力和多模态VLM支持，满足复杂AI应用需求

**适用场景**:
- 企业级场景：快速微调和部署行业专属大模型，如客服机器人、知识库问答、业务流程自动化等
- 研究开发场景：学术研究人员和算法工程师进行大模型实验、性能对比和新技术验证
- 个人开发者场景：在消费级GPU上微调个性化AI助手，如角色扮演、专业领域助手等



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,394 |
| 语言 | Java |
| Forks | 15,838 |
| Issues | 34 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个成熟的企业级 AI 低代码开发平台，凭借"低代码+零代码"双模驱动架构和强大的代码生成器，让开发者无需手写代码即可快速构建企业级应用。该项目融合了最新的 AI 技术（如 LangChain4j、DeepSeek、MCP 等）和传统低代码优势，45k+ stars 证明了其在开源社区的广泛认可度和实用价值。

**技术亮点**:
- 基于 SpringBoot3 + Vue3 + Ant Design Vue 的现代化全栈架构，支持微服务（SpringCloud）和分布式场景
- 集成 LangChain4j、Spring AI 等主流 AI 框架，支持 RAG 知识库、AI 聊天助手、AI 流程编排（AIFlow）等 AI 能力
- 强大的一键代码生成器，支持前后端代码自动生成，显著降低开发成本
- 内置 Flowable/Activiti 工作流引擎，支持复杂业务流程自动化
- 支持 MCP（Model Context Protocol）和插件化架构，便于 AI 能力扩展和集成

**适用场景**:
- 企业内部管理系统快速开发：ERP、CRM、OA、HR 等业务系统，无需从零搭建
- AI 应用快速构建：企业知识库、智能客服、AI 助手、业务流程智能化等场景
- 初创团队/个人开发者快速验证产品原型，大幅缩短从想法到上线的周期



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,187 |
| 语言 | Python |
| Forks | 9,822 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,613 |
| 语言 | TypeScript |
| Forks | 6,999 |
| Issues | 452 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,609 |
| 语言 | TypeScript |
| Forks | 2,433 |
| Issues | 103 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,374 |
| 语言 | Python |
| Forks | 2,059 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,712 |
| 语言 | Python |
| Forks | 6,135 |
| Issues | 182 |
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
| Stars | 32,897 |
| 语言 | TypeScript |
| Forks | 3,535 |
| Issues | 275 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,920 |
| 语言 | Jupyter Notebook |
| Forks | 5,219 |
| Issues | 123 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,953 |
| 语言 | Python |
| Forks | 14,829 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,179 |
| 语言 | JavaScript |
| Forks | 6,074 |
| Issues | 302 |
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
| Stars | 69,062 |
| 语言 | Python |
| Forks | 8,652 |
| Issues | 344 |
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
| Stars | 39,741 |
| 语言 | TypeScript |
| Forks | 2,999 |
| Issues | 364 |
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
| Stars | 80,668 |
| 语言 | Python |
| Forks | 9,532 |
| Issues | 230 |
| Topics | ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,696 |
| 语言 | TypeScript |
| Forks | 23,946 |
| Issues | 804 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,164 |
| 语言 | Python |
| Forks | 3,414 |
| Issues | 4 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,977 |
| 语言 | TypeScript |
| Forks | 55,749 |
| Issues | 1,422 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,614 |
| 语言 | Python |
| Forks | 8,582 |
| Issues | 893 |
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
| Stars | 53,894 |
| 语言 | Jupyter Notebook |
| Forks | 18,702 |
| Issues | 5 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 43,737 |
| 语言 | Python |
| Forks | 4,396 |
| Issues | 294 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


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
| Stars | 127,048 |
| 语言 | Python |
| Forks | 17,964 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有 12.7 万 stars 的超人气自托管 AI 聊天界面，核心价值在于支持 Ollama、OpenAI API 等多种后端的统一接入，让用户能够快速部署私有化的 AI 对话平台，完美兼顾易用性与数据隐私控制。

**技术亮点**:
- 多后端统一支持：同时兼容 Ollama、OpenAI API 等主流 LLM 服务，灵活切换不同模型
- RAG（检索增强生成）内置支持：可在对话中结合私有知识库，提升回答准确性
- MCP（Model Context Protocol）协议支持：实现模型与外部工具/数据源的标准交互
- 完全自托管架构：用户可本地或私有云部署，数据完全自主可控
- 现代化 Web UI：Python 技术栈构建，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部 AI 助手：保护敏感数据不出内网，支持对接私有知识库
- 个人开发者学习与实验：低成本搭建本地 LLM 对话环境，支持 Ollama 本地模型
- 多模型对比测试：统一界面切换 OpenAI、本地模型等，便于效果评估



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,949 |
| 语言 | Python |
| Forks | 8,374 |
| Issues | 3,089 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（74K+ Stars），创新性地将检索增强生成与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层。支持 DeepSeek、OpenAI、Ollama 等多种模型，是企业级 RAG 应用的首选解决方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力，打造智能检索增强生成引擎，支持深度推理和自主决策
- 内置强大的文档解析与理解能力，支持复杂文档的结构化提取和知识图谱构建（GraphRAG）
- 支持 MCP 协议和多模型接入（DeepSeek-R1、OpenAI、Ollama），具备极强的生态兼容性
- 提供 Agentic Workflow 编排能力，支持复杂的多步骤推理和任务自动化流程
- 具备 AI Search 和 Deep Research 能力，适合构建企业级智能问答和知识库系统

**适用场景**:
- 企业知识库搭建：构建智能文档问答系统，支持复杂文档的解析、理解和检索
- AI Agent 开发：基于 RAG + Agent 能力开发智能助手，支持多轮对话和任务执行
- 智能搜索与深度研究：构建具备上下文理解能力的 AI 搜索引擎，支持 Deep Research 模式的深度信息挖掘



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,586 |
| 语言 | TypeScript |
| Forks | 14,787 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI Agent 工作空间平台，73K+ Star 证明了其社区认可度。它突破了传统单一 AI 对话模式，创新性地引入多 Agent 协作和知识库管理，让用户能够像组建团队一样构建 AI 助手矩阵，显著提升复杂任务的解决效率。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工协作
- 统一多模型接入：支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型一站式集成
- 知识库管理 (Knowledge Base)：支持构建和管理私有知识库，增强 AI 上下文理解能力
- MCP 协议支持：兼容 Model Context Protocol，实现工具和数据的标准化调用
- 全栈 TypeScript 实现：现代化技术栈，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流：适合团队构建专属 AI 助手体系，处理客服、文档分析、数据分析等多场景任务
- AI Agent 开发平台：开发者可基于此快速搭建定制化 Agent 应用，降低多模型集成成本
- 个人知识管理与效率提升：个人用户可构建私有知识库，通过多 Agent 协作提升学习、写作、研究效率



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,543 |
| 语言 | MDX |
| Forks | 7,639 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程领域综合资源库，汇聚了来自顶尖学术机构和工业界的最佳实践，涵盖从基础Prompt Engineering到前沿AI Agents的完整知识体系。项目持续更新，整合了论文、实战笔记本、教程和工具资源，是AI开发者从入门到精通的必备参考指南。

**技术亮点**:
- 全面覆盖LLM开发三大核心技术：提示工程(Prompt Engineering)、检索增强生成(RAG)、AI智能体(Agents)
- 提供可执行的MDX Notebook，将理论学习与代码实践深度结合
- 系统整理了ChatGPT、OpenAI等主流模型的提示词最佳实践和设计模式
- 包含Generative AI领域的最新研究论文和技术进展追踪
- MIT开源许可，支持社区协作共建，资源质量有保障

**适用场景**:
- 企业AI应用开发：帮助团队快速掌握LLM应用开发技能，构建RAG系统、智能客服、AI Agent等生产级应用
- 个人学习进阶：适合AI工程师、开发者系统学习提示工程和LLM技术栈，从零基础到实战应用
- 学术研究参考：为研究人员提供Prompt Engineering和AI Agents领域的论文合集和技术综述



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,394 |
| 语言 | Java |
| Forks | 15,838 |
| Issues | 34 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个成熟的企业级 AI 低代码开发平台，凭借"低代码+零代码"双模驱动架构和强大的代码生成器，让开发者无需手写代码即可快速构建企业级应用。该项目融合了最新的 AI 技术（如 LangChain4j、DeepSeek、MCP 等）和传统低代码优势，45k+ stars 证明了其在开源社区的广泛认可度和实用价值。

**技术亮点**:
- 基于 SpringBoot3 + Vue3 + Ant Design Vue 的现代化全栈架构，支持微服务（SpringCloud）和分布式场景
- 集成 LangChain4j、Spring AI 等主流 AI 框架，支持 RAG 知识库、AI 聊天助手、AI 流程编排（AIFlow）等 AI 能力
- 强大的一键代码生成器，支持前后端代码自动生成，显著降低开发成本
- 内置 Flowable/Activiti 工作流引擎，支持复杂业务流程自动化
- 支持 MCP（Model Context Protocol）和插件化架构，便于 AI 能力扩展和集成

**适用场景**:
- 企业内部管理系统快速开发：ERP、CRM、OA、HR 等业务系统，无需从零搭建
- AI 应用快速构建：企业知识库、智能客服、AI 助手、业务流程智能化等场景
- 初创团队/个人开发者快速验证产品原型，大幅缩短从想法到上线的周期



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,609 |
| 语言 | TypeScript |
| Forks | 2,433 |
| Issues | 103 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,374 |
| 语言 | Python |
| Forks | 2,059 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,712 |
| 语言 | Python |
| Forks | 6,135 |
| Issues | 182 |
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
| Stars | 32,897 |
| 语言 | TypeScript |
| Forks | 3,535 |
| Issues | 275 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,920 |
| 语言 | Jupyter Notebook |
| Forks | 5,219 |
| Issues | 123 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,953 |
| 语言 | Python |
| Forks | 14,829 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,921 |
| 语言 | TypeScript |
| Forks | 11,789 |
| Issues | 935 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,179 |
| 语言 | JavaScript |
| Forks | 6,074 |
| Issues | 302 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,696 |
| 语言 | TypeScript |
| Forks | 23,946 |
| Issues | 804 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,199 |
| 语言 | Python |
| Forks | 9,955 |
| Issues | 246 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,279 |
| 语言 | Go |
| Forks | 3,897 |
| Issues | 1,070 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### microsoft/graphrag

**描述**: A modular graph-based Retrieval-Augmented Generation (RAG) system

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,439 |
| 语言 | Python |
| Forks | 3,319 |
| Issues | 75 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (26 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,048 |
| 语言 | Python |
| Forks | 17,964 |
| Issues | 289 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有 12.7 万 stars 的超人气自托管 AI 聊天界面，核心价值在于支持 Ollama、OpenAI API 等多种后端的统一接入，让用户能够快速部署私有化的 AI 对话平台，完美兼顾易用性与数据隐私控制。

**技术亮点**:
- 多后端统一支持：同时兼容 Ollama、OpenAI API 等主流 LLM 服务，灵活切换不同模型
- RAG（检索增强生成）内置支持：可在对话中结合私有知识库，提升回答准确性
- MCP（Model Context Protocol）协议支持：实现模型与外部工具/数据源的标准交互
- 完全自托管架构：用户可本地或私有云部署，数据完全自主可控
- 现代化 Web UI：Python 技术栈构建，提供类似 ChatGPT 的流畅交互体验

**适用场景**:
- 企业内部 AI 助手：保护敏感数据不出内网，支持对接私有知识库
- 个人开发者学习与实验：低成本搭建本地 LLM 对话环境，支持 Ollama 本地模型
- 多模型对比测试：统一界面切换 OpenAI、本地模型等，便于效果评估



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,949 |
| 语言 | Python |
| Forks | 8,374 |
| Issues | 3,089 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（74K+ Stars），创新性地将检索增强生成与 Agent 能力深度融合，为 LLM 提供卓越的上下文理解层。支持 DeepSeek、OpenAI、Ollama 等多种模型，是企业级 RAG 应用的首选解决方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力，打造智能检索增强生成引擎，支持深度推理和自主决策
- 内置强大的文档解析与理解能力，支持复杂文档的结构化提取和知识图谱构建（GraphRAG）
- 支持 MCP 协议和多模型接入（DeepSeek-R1、OpenAI、Ollama），具备极强的生态兼容性
- 提供 Agentic Workflow 编排能力，支持复杂的多步骤推理和任务自动化流程
- 具备 AI Search 和 Deep Research 能力，适合构建企业级智能问答和知识库系统

**适用场景**:
- 企业知识库搭建：构建智能文档问答系统，支持复杂文档的解析、理解和检索
- AI Agent 开发：基于 RAG + Agent 能力开发智能助手，支持多轮对话和任务执行
- 智能搜索与深度研究：构建具备上下文理解能力的 AI 搜索引擎，支持 Deep Research 模式的深度信息挖掘



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,632 |
| 语言 | JavaScript |
| Forks | 9,327 |
| Issues | 13 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个革命性的AI编程助手增强系统，为Claude Code、Cursor等主流AI开发工具提供了类似人类专家的"技能、直觉、记忆"能力，通过性能优化显著提升AI编程助手的开发效率和代码质量。74K+ Stars证明了其在AI辅助开发领域的巨大价值和社区认可度。

**技术亮点**:
- Agent Harness性能优化系统 - 提供技能、直觉、记忆三大核心能力模块，让AI助手具备专家级开发直觉
- Research-First开发方法论 - 优先研究最佳实践后再编码，提高代码质量和架构合理性
- 内置安全机制 - 针对AI生成代码的安全审查和防护体系
- 支持MCP协议集成 - 模型上下文协议，实现与多种AI开发工具的无缝对接
- 多平台兼容架构 - 同时支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具

**适用场景**:
- 企业开发团队：标准化AI辅助开发流程，提升团队整体编码效率和代码质量，降低技术债务
- 个人开发者：快速掌握AI编程工具的高级用法，将AI助手能力提升到专家级水平
- AI应用开发者：学习如何构建和优化AI Agent系统，理解性能调优和记忆机制的最佳实践



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,586 |
| 语言 | TypeScript |
| Forks | 14,787 |
| Issues | 634 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的 AI Agent 工作空间平台，73K+ Star 证明了其社区认可度。它突破了传统单一 AI 对话模式，创新性地引入多 Agent 协作和知识库管理，让用户能够像组建团队一样构建 AI 助手矩阵，显著提升复杂任务的解决效率。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的分工协作
- 统一多模型接入：支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型一站式集成
- 知识库管理 (Knowledge Base)：支持构建和管理私有知识库，增强 AI 上下文理解能力
- MCP 协议支持：兼容 Model Context Protocol，实现工具和数据的标准化调用
- 全栈 TypeScript 实现：现代化技术栈，便于二次开发和定制

**适用场景**:
- 企业级 AI 工作流：适合团队构建专属 AI 助手体系，处理客服、文档分析、数据分析等多场景任务
- AI Agent 开发平台：开发者可基于此快速搭建定制化 Agent 应用，降低多模型集成成本
- 个人知识管理与效率提升：个人用户可构建私有知识库，通过多 Agent 协作提升学习、写作、研究效率



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,543 |
| 语言 | MDX |
| Forks | 7,639 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程领域综合资源库，汇聚了来自顶尖学术机构和工业界的最佳实践，涵盖从基础Prompt Engineering到前沿AI Agents的完整知识体系。项目持续更新，整合了论文、实战笔记本、教程和工具资源，是AI开发者从入门到精通的必备参考指南。

**技术亮点**:
- 全面覆盖LLM开发三大核心技术：提示工程(Prompt Engineering)、检索增强生成(RAG)、AI智能体(Agents)
- 提供可执行的MDX Notebook，将理论学习与代码实践深度结合
- 系统整理了ChatGPT、OpenAI等主流模型的提示词最佳实践和设计模式
- 包含Generative AI领域的最新研究论文和技术进展追踪
- MIT开源许可，支持社区协作共建，资源质量有保障

**适用场景**:
- 企业AI应用开发：帮助团队快速掌握LLM应用开发技能，构建RAG系统、智能客服、AI Agent等生产级应用
- 个人学习进阶：适合AI工程师、开发者系统学习提示工程和LLM技术栈，从零基础到实战应用
- 学术研究参考：为研究人员提供Prompt Engineering和AI Agents领域的论文合集和技术综述



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,077 |
| 语言 | HTML |
| Forks | 19,985 |
| Issues | 27 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,932 |
| 语言 | Jupyter Notebook |
| Forks | 13,418 |
| Issues | 1 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,187 |
| 语言 | Python |
| Forks | 9,822 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,613 |
| 语言 | TypeScript |
| Forks | 6,999 |
| Issues | 452 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,609 |
| 语言 | TypeScript |
| Forks | 2,433 |
| Issues | 103 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,374 |
| 语言 | Python |
| Forks | 2,059 |
| Issues | 95 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,179 |
| 语言 | JavaScript |
| Forks | 6,074 |
| Issues | 302 |
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
| Stars | 69,062 |
| 语言 | Python |
| Forks | 8,652 |
| Issues | 344 |
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
| Stars | 39,741 |
| 语言 | TypeScript |
| Forks | 2,999 |
| Issues | 364 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,696 |
| 语言 | TypeScript |
| Forks | 23,946 |
| Issues | 804 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,164 |
| 语言 | Python |
| Forks | 3,414 |
| Issues | 4 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,273 |
| 语言 | HTML |
| Forks | 5,503 |
| Issues | 27 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,006 |
| 语言 | Python |
| Forks | 14,328 |
| Issues | 3,672 |
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
| Stars | 40,967 |
| 语言 | Python |
| Forks | 3,967 |
| Issues | 70 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,606 |
| 语言 | Python |
| Forks | 2,560 |
| Issues | 62 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,614 |
| 语言 | Python |
| Forks | 8,582 |
| Issues | 893 |
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
| Stars | 164,967 |
| 语言 | Go |
| Forks | 14,957 |
| Issues | 2,627 |
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
| Stars | 46,626 |
| 语言 | Rust |
| Forks | 9,116 |
| Issues | 5 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,695 |
| 语言 | Python |
| Forks | 5,357 |
| Issues | 471 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 38,926 |
| 语言 | TypeScript |
| Forks | 3,938 |
| Issues | 1,072 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 43,737 |
| 语言 | Python |
| Forks | 4,396 |
| Issues | 294 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


## 🧠 机器学习框架 (12 个项目) { #机器学习框架 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,543 |
| 语言 | MDX |
| Forks | 7,639 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程领域综合资源库，汇聚了来自顶尖学术机构和工业界的最佳实践，涵盖从基础Prompt Engineering到前沿AI Agents的完整知识体系。项目持续更新，整合了论文、实战笔记本、教程和工具资源，是AI开发者从入门到精通的必备参考指南。

**技术亮点**:
- 全面覆盖LLM开发三大核心技术：提示工程(Prompt Engineering)、检索增强生成(RAG)、AI智能体(Agents)
- 提供可执行的MDX Notebook，将理论学习与代码实践深度结合
- 系统整理了ChatGPT、OpenAI等主流模型的提示词最佳实践和设计模式
- 包含Generative AI领域的最新研究论文和技术进展追踪
- MIT开源许可，支持社区协作共建，资源质量有保障

**适用场景**:
- 企业AI应用开发：帮助团队快速掌握LLM应用开发技能，构建RAG系统、智能客服、AI Agent等生产级应用
- 个人学习进阶：适合AI工程师、开发者系统学习提示工程和LLM技术栈，从零基础到实战应用
- 学术研究参考：为研究人员提供Prompt Engineering和AI Agents领域的论文合集和技术综述



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,372 |
| 语言 | Python |
| Forks | 8,349 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一高效的大模型微调框架，支持100多种LLM和VLM模型，被ACL 2024收录。项目获得了68K+ Stars，是当前最流行的开源微调工具之一，通过集成LoRA、QLoRA、量化、RLHF等前沿技术，大幅降低了大模型训练的技术门槛和硬件成本。

**技术亮点**:
- 支持100+主流大模型统一微调，包括LLaMA、Qwen、DeepSeek、Gemma、GPT系列等，提供一站式训练体验
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、全量微调，以及4/8bit量化训练，显著降低显存需求
- 支持全流程训练方法：指令微调(Instruction Tuning)、预训练、RLHF强化学习人类反馈对齐
- 兼容MoE混合专家模型架构，适配最新的大模型技术趋势
- 提供Agent开发能力和多模态VLM支持，满足复杂AI应用需求

**适用场景**:
- 企业级场景：快速微调和部署行业专属大模型，如客服机器人、知识库问答、业务流程自动化等
- 研究开发场景：学术研究人员和算法工程师进行大模型实验、性能对比和新技术验证
- 个人开发者场景：在消费级GPU上微调个性化AI助手，如角色扮演、专业领域助手等



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,978 |
| 语言 | Python |
| Forks | 6,179 |
| Issues | 64 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是目前GitHub上最热门的开源金融数据平台，拥有超过6.2万Stars，为分析师、量化交易者和AI Agent提供统一的数据访问接口，将多个金融数据源整合到一个平台中，大幅降低了金融数据分析的门槛。

**技术亮点**:
- 支持多数据源整合：覆盖股票、加密货币、期权、衍生品、经济指标、固定收益等多个金融领域的数据
- Python原生开发，提供完善的API接口，方便量化分析师和数据科学家快速集成
- 内置机器学习和AI功能，支持构建智能金融分析Agent
- 完全开源且模块化设计，用户可自定义扩展数据源和功能
- 支持量化金融全栈开发，从数据获取到策略回测的一站式解决方案

**适用场景**:
- 量化交易研究与策略开发：适合量化分析师获取多维度市场数据并进行回测分析
- 金融科技产品开发：企业可基于OpenBB快速构建金融数据分析平台或投研工具
- AI金融应用构建：开发者可利用其AI Agent能力构建智能投顾或自动化分析系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,077 |
| 语言 | HTML |
| Forks | 19,985 |
| Issues | 27 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,932 |
| 语言 | Jupyter Notebook |
| Forks | 13,418 |
| Issues | 1 |
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
| Stars | 32,897 |
| 语言 | TypeScript |
| Forks | 3,535 |
| Issues | 275 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,920 |
| 语言 | Jupyter Notebook |
| Forks | 5,219 |
| Issues | 123 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 157,769 |
| 语言 | Python |
| Forks | 32,459 |
| Issues | 2,278 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,006 |
| 语言 | Python |
| Forks | 14,328 |
| Issues | 3,672 |
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
| Stars | 105,756 |
| 语言 | Python |
| Forks | 12,146 |
| Issues | 3,812 |
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
| Stars | 98,209 |
| 语言 | Python |
| Forks | 27,191 |
| Issues | 18,057 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,670 |
| 语言 | Python |
| Forks | 30,156 |
| Issues | 2,470 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


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
| Stars | 74,632 |
| 语言 | JavaScript |
| Forks | 9,327 |
| Issues | 13 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个革命性的AI编程助手增强系统，为Claude Code、Cursor等主流AI开发工具提供了类似人类专家的"技能、直觉、记忆"能力，通过性能优化显著提升AI编程助手的开发效率和代码质量。74K+ Stars证明了其在AI辅助开发领域的巨大价值和社区认可度。

**技术亮点**:
- Agent Harness性能优化系统 - 提供技能、直觉、记忆三大核心能力模块，让AI助手具备专家级开发直觉
- Research-First开发方法论 - 优先研究最佳实践后再编码，提高代码质量和架构合理性
- 内置安全机制 - 针对AI生成代码的安全审查和防护体系
- 支持MCP协议集成 - 模型上下文协议，实现与多种AI开发工具的无缝对接
- 多平台兼容架构 - 同时支持Claude Code、Codex、Opencode、Cursor等主流AI编程工具

**适用场景**:
- 企业开发团队：标准化AI辅助开发流程，提升团队整体编码效率和代码质量，降低技术债务
- 个人开发者：快速掌握AI编程工具的高级用法，将AI助手能力提升到专家级水平
- AI应用开发者：学习如何构建和优化AI Agent系统，理解性能调优和记忆机制的最佳实践



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,547 |
| 语言 | Go |
| Forks | 3,680 |
| Issues | 152 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全开源、免费且功能强大的本地 AI 解决方案，最大的亮点是**无需 GPU 即可在消费级硬件上运行**，同时提供与 OpenAI API 兼容的接口，让开发者能够以极低成本实现 AI 能力的私有化部署。它集成了文本生成、图像生成、语音克隆、视频生成等多种 AI 能力，并支持去中心化和 P2P 分布式推理，是目前最全面的本地 AI 替代方案之一。

**技术亮点**:
- 完全兼容 OpenAI API 标准，支持零代码迁移（Drop-in replacement）
- 无需 GPU，在消费级 CPU 硬件上即可运行，支持 GGUF、Transformers、Diffusers 等多种模型格式
- 多功能集成：文本生成、图像生成、语音克隆(TTS)、视频生成、音频生成、目标检测等一体化支持
- 支持分布式和 P2P 去中心化推理，基于 libp2p 实现节点间协作
- 原生支持 MCP（Model Context Protocol）和多种主流开源模型（Llama、Mistral、Gemma、RWKV、Mamba 等）

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保数据不出域，满足合规和隐私要求
- 个人开发者低成本 AI 应用：无需购买昂贵 GPU，在普通电脑上即可开发和测试 AI 功能
- 边缘计算与离线场景：在网络受限或无网络环境下使用 AI 能力，如 IoT 设备、移动端应用



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,062 |
| 语言 | Python |
| Forks | 8,652 |
| Issues | 344 |
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
| Stars | 39,741 |
| 语言 | TypeScript |
| Forks | 2,999 |
| Issues | 364 |
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
| Stars | 178,977 |
| 语言 | TypeScript |
| Forks | 55,749 |
| Issues | 1,422 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,606 |
| 语言 | Python |
| Forks | 2,560 |
| Issues | 62 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,011 |
| 语言 | Python |
| Forks | 12,244 |
| Issues | 2,362 |
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
| Stars | 96,178 |
| 语言 | Python |
| Forks | 8,850 |
| Issues | 157 |
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
| Stars | 73,661 |
| 语言 | Python |
| Forks | 8,744 |
| Issues | 201 |
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
| Stars | 182,604 |
| 语言 | TypeScript |
| Forks | 38,484 |
| Issues | 15,163 |
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
| Stars | 93,805 |
| 语言 | TypeScript |
| Forks | 9,397 |
| Issues | 292 |
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
| Stars | 78,423 |
| 语言 | TypeScript |
| Forks | 5,680 |
| Issues | 706 |
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
| Stars | 76,631 |
| 语言 | TypeScript |
| Forks | 6,547 |
| Issues | 172 |
| Topics | browser-ide, dev-tools, development-environment, ide, remote-work, vscode, vscode-remote |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,650 |
| 语言 | JavaScript |
| Forks | 7,270 |
| Issues | 709 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,568 |
| 语言 | Go |
| Forks | 2,721 |
| Issues | 319 |
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
| Stars | 74,118 |
| 语言 | Go |
| Forks | 2,591 |
| Issues | 926 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### ⭐ 中优先级


### marktext/marktext

**描述**: 📝A simple and elegant markdown editor, available for Linux, macOS and Windows.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 54,423 |
| 语言 | JavaScript |
| Forks | 4,024 |
| Issues | 1,402 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 409,248 |
| 语言 | Python |
| Forks | 44,214 |
| Issues | 974 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,741 |
| 语言 | TypeScript |
| Forks | 2,999 |
| Issues | 364 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,164 |
| 语言 | Python |
| Forks | 3,414 |
| Issues | 4 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 178,977 |
| 语言 | TypeScript |
| Forks | 55,749 |
| Issues | 1,422 |
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
| Stars | 51,603 |
| 语言 | Go |
| Forks | 10,347 |
| Issues | 227 |
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
| Stars | 121,104 |
| 语言 | Go |
| Forks | 42,670 |
| Issues | 2,637 |
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
| Forks | 18,921 |
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
| Stars | 54,273 |
| 语言 | Go |
| Forks | 6,471 |
| Issues | 2,854 |
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
| Stars | 93,805 |
| 语言 | TypeScript |
| Forks | 9,397 |
| Issues | 292 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### microsoft/playwright

**描述**: Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 84,170 |
| 语言 | TypeScript |
| Forks | 5,287 |
| Issues | 608 |
| Topics | automation, chrome, chromium, e2e-testing, electron, end-to-end-testing, firefox, javascript, playwright, test, test-automation, testing, testing-tools, web, webkit |
| 许可证 | Apache License 2.0 |


### Stirling-Tools/Stirling-PDF

**描述**: #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,264 |
| 语言 | TypeScript |
| Forks | 6,391 |
| Issues | 442 |
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
| Stars | 84,025 |
| 语言 | JavaScript |
| Forks | 7,519 |
| Issues | 705 |
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
| Stars | 62,154 |
| 语言 | Go |
| Forks | 5,880 |
| Issues | 780 |
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
| Stars | 57,835 |
| 语言 | Go |
| Forks | 4,191 |
| Issues | 21 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 43,737 |
| 语言 | Python |
| Forks | 4,396 |
| Issues | 294 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,579 |
| 语言 | Go |
| Forks | 5,071 |
| Issues | 965 |
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
| Stars | 69,328 |
| 语言 | Go |
| Forks | 1,877 |
| Issues | 293 |
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
| Stars | 60,476 |
| 语言 | Go |
| Forks | 7,240 |
| Issues | 80 |
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
| Stars | 84,025 |
| 语言 | JavaScript |
| Forks | 7,519 |
| Issues | 705 |
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
| Stars | 63,162 |
| 语言 | Go |
| Forks | 10,241 |
| Issues | 755 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (14 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,547 |
| 语言 | Go |
| Forks | 3,680 |
| Issues | 152 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全开源、免费且功能强大的本地 AI 解决方案，最大的亮点是**无需 GPU 即可在消费级硬件上运行**，同时提供与 OpenAI API 兼容的接口，让开发者能够以极低成本实现 AI 能力的私有化部署。它集成了文本生成、图像生成、语音克隆、视频生成等多种 AI 能力，并支持去中心化和 P2P 分布式推理，是目前最全面的本地 AI 替代方案之一。

**技术亮点**:
- 完全兼容 OpenAI API 标准，支持零代码迁移（Drop-in replacement）
- 无需 GPU，在消费级 CPU 硬件上即可运行，支持 GGUF、Transformers、Diffusers 等多种模型格式
- 多功能集成：文本生成、图像生成、语音克隆(TTS)、视频生成、音频生成、目标检测等一体化支持
- 支持分布式和 P2P 去中心化推理，基于 libp2p 实现节点间协作
- 原生支持 MCP（Model Context Protocol）和多种主流开源模型（Llama、Mistral、Gemma、RWKV、Mamba 等）

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保数据不出域，满足合规和隐私要求
- 个人开发者低成本 AI 应用：无需购买昂贵 GPU，在普通电脑上即可开发和测试 AI 功能
- 边缘计算与离线场景：在网络受限或无网络环境下使用 AI 能力，如 IoT 设备、移动端应用



### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,606 |
| 语言 | Python |
| Forks | 2,560 |
| Issues | 62 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,178 |
| 语言 | Python |
| Forks | 8,850 |
| Issues | 157 |
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
| Stars | 87,029 |
| 语言 | Python |
| Forks | 33,748 |
| Issues | 423 |
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
| Stars | 100,080 |
| 语言 | TypeScript |
| Forks | 27,118 |
| Issues | 1,128 |
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
| Stars | 78,423 |
| 语言 | TypeScript |
| Forks | 5,680 |
| Issues | 706 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### nestjs/nest

**描述**: A progressive Node.js framework for building efficient, scalable, and enterprise-grade server-side applications with TypeScript/JavaScript 🚀

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,905 |
| 语言 | TypeScript |
| Forks | 8,254 |
| Issues | 36 |
| Topics | framework, hacktoberfest, javascript, javascript-framework, microservices, nest, nestjs, node, nodejs, nodejs-framework, typescript, typescript-framework, websockets |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,650 |
| 语言 | JavaScript |
| Forks | 7,270 |
| Issues | 709 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### gatsbyjs/gatsby

**描述**: React-based framework with performance, scalability, and security built in.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,944 |
| 语言 | JavaScript |
| Forks | 10,229 |
| Issues | 354 |
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
| Stars | 88,225 |
| 语言 | Go |
| Forks | 8,575 |
| Issues | 648 |
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
| Stars | 70,766 |
| 语言 | Go |
| Forks | 4,673 |
| Issues | 241 |
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
| Stars | 56,719 |
| 语言 | Go |
| Forks | 3,178 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
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
| Stars | 409,248 |
| 语言 | Python |
| Forks | 44,214 |
| Issues | 974 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,874 |
| 语言 | JavaScript |
| Forks | 22,818 |
| Issues | 189 |
| Topics | express, javascript, nodejs, server |
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
| Stars | 98,921 |
| 语言 | TypeScript |
| Forks | 11,789 |
| Issues | 935 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,179 |
| 语言 | JavaScript |
| Forks | 6,074 |
| Issues | 302 |
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
| Stars | 43,279 |
| 语言 | Go |
| Forks | 3,897 |
| Issues | 1,070 |
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
| Stars | 51,603 |
| 语言 | Go |
| Forks | 10,347 |
| Issues | 227 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,543 |
| 语言 | MDX |
| Forks | 7,639 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程领域综合资源库，汇聚了来自顶尖学术机构和工业界的最佳实践，涵盖从基础Prompt Engineering到前沿AI Agents的完整知识体系。项目持续更新，整合了论文、实战笔记本、教程和工具资源，是AI开发者从入门到精通的必备参考指南。

**技术亮点**:
- 全面覆盖LLM开发三大核心技术：提示工程(Prompt Engineering)、检索增强生成(RAG)、AI智能体(Agents)
- 提供可执行的MDX Notebook，将理论学习与代码实践深度结合
- 系统整理了ChatGPT、OpenAI等主流模型的提示词最佳实践和设计模式
- 包含Generative AI领域的最新研究论文和技术进展追踪
- MIT开源许可，支持社区协作共建，资源质量有保障

**适用场景**:
- 企业AI应用开发：帮助团队快速掌握LLM应用开发技能，构建RAG系统、智能客服、AI Agent等生产级应用
- 个人学习进阶：适合AI工程师、开发者系统学习提示工程和LLM技术栈，从零基础到实战应用
- 学术研究参考：为研究人员提供Prompt Engineering和AI Agents领域的论文合集和技术综述



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,077 |
| 语言 | HTML |
| Forks | 19,985 |
| Issues | 27 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,273 |
| 语言 | HTML |
| Forks | 5,503 |
| Issues | 27 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,444 |
| 语言 | TypeScript |
| Forks | 9,919 |
| Issues | 2,188 |
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
| Stars | 86,629 |
| 语言 | TypeScript |
| Forks | 8,728 |
| Issues | 1,616 |
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
| Stars | 127,070 |
| 语言 | JavaScript |
| Forks | 12,453 |
| Issues | 4 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### jaywcjlove/awesome-mac

**描述**:  Now we have become very big, Different from the original idea. Collect premium software in various categories.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,115 |
| 语言 | JavaScript |
| Forks | 7,489 |
| Issues | 219 |
| Topics | app, apple, application, apps, awesome, awesome-list, awesome-lists, awesome-mac, desktop-app, desktop-application, desktop-apps, list, mac, mac-osx, macos, macos-app, macos-apps, macosx, software |
| 许可证 | Creative Commons Zero v1.0 Universal |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 167,271 |
| 语言 | Go |
| Forks | 13,047 |
| Issues | 172 |
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
| Stars | 130,732 |
| 语言 | Unknown |
| Forks | 33,214 |
| Issues | 128 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### CherryHQ/cherry-studio

**描述**: AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,432 |
| 语言 | TypeScript |
| Forks | 3,830 |
| Issues | 653 |
| Topics | ai-agent, claude-code, code-agent, codex, openclaw, opencode, shannon, skills, superpowers, superpowers-core-skills, vibe-coding |
| 许可证 | GNU Affero General Public License v3.0 |


### openclaw/openclaw

**描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 310,478 |
| 语言 | TypeScript |
| Forks | 59,004 |
| Issues | 13,078 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,902 |
| 语言 | Python |
| Forks | 6,317 |
| Issues | 26 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,997 |
| 语言 | Python |
| Forks | 11,667 |
| Issues | 105 |
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
| Stars | 76,524 |
| 语言 | Python |
| Forks | 6,520 |
| Issues | 625 |
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
| Stars | 383,950 |
| 语言 | Python |
| Forks | 66,008 |
| Issues | 69 |
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
| Stars | 112,846 |
| 语言 | TypeScript |
| Forks | 5,715 |
| Issues | 304 |
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
| Stars | 102,531 |
| 语言 | TypeScript |
| Forks | 7,462 |
| Issues | 178 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,913 |
| 语言 | Go |
| Forks | 10,244 |
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
| Stars | 97,824 |
| 语言 | C++ |
| Forks | 15,470 |
| Issues | 1,273 |
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
| Stars | 59,404 |
| 语言 | Python |
| Forks | 1,608 |
| Issues | 38 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 338,726 |
| 语言 | Python |
| Forks | 54,871 |
| Issues | 517 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 286,964 |
| 语言 | Python |
| Forks | 27,380 |
| Issues | 20 |
| Topics | awesome, collections, python, python-framework, python-library, python-resources |
| 许可证 | Other |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 218,575 |
| 语言 | Python |
| Forks | 50,166 |
| Issues | 880 |
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
| Stars | 85,314 |
| 语言 | Python |
| Forks | 36,981 |
| Issues | 3,586 |
| Topics | asyncio, hacktoberfest, home-automation, internet-of-things, iot, mqtt, python, raspberry-pi |
| 许可证 | Apache License 2.0 |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,218 |
| 语言 | Python |
| Forks | 7,164 |
| Issues | 475 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### tensorflow/models

**描述**: Models and examples built with TensorFlow

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,688 |
| 语言 | Python |
| Forks | 45,245 |
| Issues | 1,283 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,026 |
| 语言 | Python |
| Forks | 16,750 |
| Issues | 15 |
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
| Stars | 438,082 |
| 语言 | TypeScript |
| Forks | 43,595 |
| Issues | 258 |
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
| Stars | 350,836 |
| 语言 | TypeScript |
| Forks | 43,778 |
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
| Stars | 118,665 |
| 语言 | TypeScript |
| Forks | 12,860 |
| Issues | 2,831 |
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
| Stars | 109,432 |
| 语言 | TypeScript |
| Forks | 8,167 |
| Issues | 1,790 |
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
| Stars | 108,140 |
| 语言 | TypeScript |
| Forks | 13,292 |
| Issues | 5,489 |
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
| Stars | 97,691 |
| 语言 | TypeScript |
| Forks | 54,557 |
| Issues | 1,363 |
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
| Stars | 94,651 |
| 语言 | TypeScript |
| Forks | 5,092 |
| Issues | 643 |
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
| Stars | 94,016 |
| 语言 | TypeScript |
| Forks | 5,111 |
| Issues | 91 |
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
| Stars | 82,988 |
| 语言 | TypeScript |
| Forks | 7,580 |
| Issues | 37 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,013 |
| 语言 | TypeScript |
| Forks | 9,888 |
| Issues | 481 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,879 |
| 语言 | TypeScript |
| Forks | 7,903 |
| Issues | 636 |
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
| Stars | 243,902 |
| 语言 | JavaScript |
| Forks | 50,773 |
| Issues | 1,170 |
| Topics | declarative, frontend, javascript, library, react, ui |
| 许可证 | MIT License |


### vercel/next.js

**描述**: The React Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,281 |
| 语言 | JavaScript |
| Forks | 30,642 |
| Issues | 3,455 |
| Topics | blog, browser, compiler, components, hybrid, nextjs, node, react, server-rendering, ssg, static, static-site-generator, universal, vercel |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,227 |
| 语言 | JavaScript |
| Forks | 35,039 |
| Issues | 2,526 |
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
| Stars | 111,338 |
| 语言 | JavaScript |
| Forks | 36,300 |
| Issues | 585 |
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
| Stars | 108,646 |
| 语言 | JavaScript |
| Forks | 11,550 |
| Issues | 344 |
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
| Stars | 98,004 |
| 语言 | JavaScript |
| Forks | 32,712 |
| Issues | 1,720 |
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
| Stars | 95,416 |
| 语言 | JavaScript |
| Forks | 15,236 |
| Issues | 43 |
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
| Stars | 86,044 |
| 语言 | JavaScript |
| Forks | 4,803 |
| Issues | 976 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,712 |
| 语言 | JavaScript |
| Forks | 31,516 |
| Issues | 271 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,722 |
| 语言 | JavaScript |
| Forks | 16,802 |
| Issues | 884 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,015 |
| 语言 | JavaScript |
| Forks | 9,323 |
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
| Stars | 62,071 |
| 语言 | JavaScript |
| Forks | 3,974 |
| Issues | 17 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,870 |
| 语言 | JavaScript |
| Forks | 20,473 |
| Issues | 97 |
| Topics | jquery |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,805 |
| 语言 | JavaScript |
| Forks | 5,604 |
| Issues | 66 |
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
| Stars | 57,401 |
| 语言 | JavaScript |
| Forks | 12,306 |
| Issues | 23 |
| Topics | best-practices, css, html, html5, html5-boilerplate, javascript, robust |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,023 |
| 语言 | Go |
| Forks | 18,856 |
| Issues | 9,868 |
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
| Stars | 105,176 |
| 语言 | Go |
| Forks | 14,945 |
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
| Stars | 87,064 |
| 语言 | Go |
| Forks | 8,205 |
| Issues | 267 |
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
| Stars | 80,786 |
| 语言 | Go |
| Forks | 4,958 |
| Issues | 408 |
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
| Stars | 68,694 |
| 语言 | Go |
| Forks | 3,219 |
| Issues | 9 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,005 |
| 语言 | Go |
| Forks | 4,972 |
| Issues | 1,140 |
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
| Stars | 50,911 |
| 语言 | Go |
| Forks | 21,845 |
| Issues | 375 |
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
| Stars | 49,164 |
| 语言 | Go |
| Forks | 7,980 |
| Issues | 572 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,948 |
| 语言 | Go |
| Forks | 8,883 |
| Issues | 8 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,427 |
| 语言 | Go |
| Forks | 3,762 |
| Issues | 91 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,860 |
| 语言 | Python |
| Forks | 10,603 |
| Issues | 4,118 |
| 许可证 | The Unlicense |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,750 |
| 语言 | JavaScript |
| Forks | 31,115 |
| Issues | 393 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
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
| Forks | 26,775 |
| Issues | 189 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,258 |
| 语言 | JavaScript |
| Forks | 11,984 |
| Issues | 538 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,840 |
| 语言 | JavaScript |
| Forks | 4,470 |
| Issues | 94 |
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
| Stars | 66,277 |
| 语言 | JavaScript |
| Forks | 9,188 |
| Issues | 1 |
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
| Stars | 61,575 |
| 语言 | JavaScript |
| Forks | 7,128 |
| Issues | 129 |
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
| Stars | 145,987 |
| 语言 | Python |
| Forks | 11,213 |
| Issues | 293 |
| Topics | awesome, github, hellogithub, python |
