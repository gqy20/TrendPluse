# 项目发现报告 (2026-03-16)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
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
| ⚙️ DevOps/基础设施 | 16 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
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
| Stars | 127,444 |
| 语言 | Python |
| Forks | 18,019 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个极具价值的开源AI交互平台，拥有超过12万Star的强大社区支持。它提供了统一的Web界面来连接多种LLM后端（Ollama、OpenAI API等），让用户能够轻松部署和自托管私有AI服务，兼具功能丰富性与易用性。

**技术亮点**:
- 支持多种LLM后端：无缝集成Ollama、OpenAI API等多种大语言模型服务
- RAG（检索增强生成）支持：集成知识库检索能力，提升AI回答准确性
- MCP协议支持：支持Model Context Protocol，实现更灵活的工具调用和上下文管理
- 完全自托管：支持私有化部署，数据安全可控，满足企业隐私合规需求
- 现代化Web界面：基于Python构建的友好UI，支持多用户、对话管理、模型切换等功能

**适用场景**:
- 企业内部AI助手：私有化部署LLM服务，保护敏感数据，为员工提供安全的AI交互平台
- 个人开发者学习和实验：快速搭建本地AI环境，测试不同模型（如通过Ollama运行本地模型）
- AI应用原型开发：作为LLM应用的前端界面，快速验证RAG、多模型切换等功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,141 |
| 语言 | Python |
| Forks | 8,409 |
| Issues | 3,102 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，拥有超过 7.5 万 Star，其独特之处在于将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的优选框架。

**技术亮点**:
- 融合 RAG + Agent 双引擎架构，支持 Agentic Workflow 智能工作流编排
- 强大的文档解析与理解能力（Document Parser & Understanding），支持复杂文档处理
- 原生支持 GraphRAG 图检索增强生成，提升知识关联与推理能力
- 广泛兼容主流 LLM 后端：OpenAI、DeepSeek、Ollama 等，支持 MCP 协议
- 集成 Deep Research 与 AI Search 能力，适合构建深度知识问答系统

**适用场景**:
- 企业知识库构建：快速搭建内部文档检索与智能问答系统，提升知识管理效率
- 智能客服与助手开发：基于企业专属文档构建高准确度的对话式 AI 服务
- 研究与文献分析：利用 Deep Research 和 GraphRAG 能力进行学术文献深度挖掘与知识图谱构建



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,897 |
| 语言 | TypeScript |
| Forks | 6,460 |
| Issues | 215 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前最成熟的开源 Web 数据提取工具之一，拥有近 10 万 Stars，它解决了 AI 开发中最头疼的数据准备问题——将杂乱的网页内容转换为 LLM 可直接使用的结构化 Markdown 或 JSON 数据，大幅降低了构建 AI 应用的门槛。

**技术亮点**:
- 支持将整个网站转换为 LLM-ready 的 Markdown 格式，自动处理 HTML 标签、脚本、样式等干扰元素
- 提供 Web Data API，支持爬取、搜索、提取等多种 Web 数据获取方式
- 内置 JavaScript 渲染能力，可处理动态网页和 SPA 应用
- 支持结构化数据提取，可自定义 Schema 输出 JSON 格式
- 专为 AI 场景优化，与主流 LLM 框架无缝集成

**适用场景**:
- 企业构建 RAG 知识库，从官网、文档站、帮助中心批量提取内容用于 AI 问答系统
- AI Agent 开发者需要实时获取网页数据作为上下文输入
- 研究人员和数据分析师进行大规模网页内容采集与结构化处理



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,045 |
| 语言 | JavaScript |
| Forks | 10,266 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有8万+星标的高人气AI Agent性能优化系统，为Claude Code、Cursor等主流AI编程工具提供了统一的增强框架，通过技能系统、记忆机制和安全控制大幅提升AI辅助开发效率，是当前AI编程工具生态中最全面的性能优化解决方案。

**技术亮点**:
- 多平台统一集成框架 - 支持Claude Code、Codex、Opencode、Cursor等多个AI编程平台，提供跨平台的一致性增强体验
- Agent五维能力系统 - 包含Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）、Research（研究）五大核心模块，全方位优化AI Agent性能
- MCP协议支持 - 集成Model Context Protocol，实现与外部工具和数据的标准化交互，扩展AI能力边界
- 研究优先开发模式 - 采用Research-first理念，AI在编写代码前先进行充分的上下文分析和信息收集，提高代码质量和准确性
- MIT开源许可 - 采用宽松的开源协议，支持商业和私人使用，便于企业集成和二次开发

**适用场景**:
- 企业开发团队集成 - 为使用Claude Code、Cursor等AI编程工具的开发团队提供统一的性能增强层，提升整体开发效率和代码质量
- AI Agent定制化开发 - 开发者可基于此框架为特定业务场景训练和配置专属的AI编程助手，包括自定义技能、记忆持久化和安全策略
- 多AI工具协同场景 - 需要同时使用多个AI编程工具的项目，可通过此系统实现统一的配置管理和能力增强



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,713 |
| 语言 | Go |
| Forks | 3,708 |
| Issues | 147 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费、开源的本地化 AI 解决方案，最大亮点是无需 GPU 就能在消费级硬件上运行，并且提供与 OpenAI API 兼容的接口，让开发者可以零成本、隐私安全地在本地部署大语言模型和多模态生成能力。

**技术亮点**:
- 无需 GPU 的本地推理：专为消费级硬件优化，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：提供 drop-in replacement，现有 OpenAI 应用可无缝迁移
- 多模态全能支持：涵盖文本生成、图像生成、音频/视频生成、语音克隆、目标检测等全栈能力
- 分布式与 P2P 架构：基于 libp2p 实现去中心化推理，支持分布式部署
- 原生 MCP 支持：集成模型上下文协议，便于与 AI 代理和工具链集成

**适用场景**:
- 企业内部 AI 服务：在私有环境中部署文本生成、知识问答和内容创作，保护敏感数据不外泄
- 个人开发者学习与实验：低成本在本地运行 LLaMA、Stable Diffusion 等模型，无需云服务费用
- 边缘设备与离线场景：在没有网络或 GPU 的环境下（如嵌入式设备、老旧服务器）运行 AI 推理



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,764 |
| 语言 | TypeScript |
| Forks | 14,790 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3万+ Stars 的顶级 AI Agent 开发平台，它将 Agent 协作能力提升到了全新高度。作为一个集成了 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型的开源平台，它不仅支持多 Agent 协作和知识库管理，还引入了 MCP 协议，让开发者能够轻松构建、设计和管理智能 Agent 团队，是实现 AI 驱动工作流的理想选择。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的自动化处理和智能分工
- 全栈 AI 模型集成：原生支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流大语言模型，提供统一的接口层
- MCP 协议支持：集成 Model Context Protocol，实现模型上下文标准化和跨平台互操作
- 知识库管理系统：内置知识库功能，支持 Agent 长期记忆和上下文增强，提升 AI 决策质量
- 现代化 TypeScript 技术栈：采用类型安全的架构设计，提供良好的开发体验和代码可维护性

**适用场景**:
- 企业级 AI 工作流自动化：构建客服机器人、智能助手团队、自动化办公流程等需要多 Agent 协作的业务场景
- AI 应用快速原型开发：个人开发者快速搭建基于大模型的对话应用、知识问答系统和智能工具
- 团队协作与知识管理：为团队提供统一的 AI Agent 平台，实现知识沉淀、智能搜索和协同工作



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,731 |
| 语言 | MDX |
| Forks | 7,661 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前 GitHub 上最全面、最受认可的提示工程学习资源库，涵盖了从基础提示工程到高级 RAG 和 AI Agent 开发的完整知识体系，是掌握现代 AI 应用开发技能的必读指南。

**技术亮点**:
- 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG 检索增强生成、AI Agents 智能体开发
- 提供多形式学习资源：包含理论指南、学术论文、实战课程和 Jupyter Notebook 代码示例
- 紧跟前沿技术趋势：涵盖 LLMs、ChatGPT、OpenAI API 等主流大语言模型工具的最佳实践
- MDX 格式编写，支持 Markdown 与 React 组件混合，便于构建交互式文档
- MIT 开源许可，7万+ Star 社区验证，内容质量高且持续更新

**适用场景**:
- 企业 AI 团队培训：系统学习提示工程和 RAG 技术，提升内部 AI 应用开发能力
- 个人开发者学习路径：从零开始掌握大语言模型应用开发，包括 ChatBot、智能助手等场景
- 产品经理和技术决策者：了解 AI Agent 和 RAG 技术能力边界，规划产品技术方案



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,537 |
| 语言 | Python |
| Forks | 8,359 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的 LLM 微调框架之一，支持 100+ 大语言模型和视觉语言模型的统一高效微调，在 GitHub 上获得 68K+ Stars 的广泛认可，并被 ACL 2024 收录，是企业和研究团队快速定制化大模型的首选工具。

**技术亮点**:
- 统一框架支持 100+ LLMs 和 VLMs（包括 Llama3、Qwen、DeepSeek、Gemma 等主流模型），一套代码适配多种模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化训练，显著降低显存需求和训练成本
- 支持全栈训练流程：指令微调、RLHF（人类反馈强化学习）、MoE（混合专家）模型训练
- 兼容 Transformers 生态，支持 Agent 和 NLP 多种应用场景
- Apache 2.0 开源许可，提供 WebUI 和命令行两种使用方式，易用性强

**适用场景**:
- 企业私有化部署：快速微调开源大模型以适应特定业务场景（如客服、知识库问答、垂直领域应用）
- 学术研究与实验：研究人员可快速对比不同微调方法（LoRA/QLoRA/RLHF）在多种模型上的效果
- 个人开发者学习与实践：低成本上手大模型微调技术，支持消费级 GPU 进行模型训练



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,415 |
| 语言 | Java |
| Forks | 15,841 |
| Issues | 56 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是目前国内最受欢迎的 AI 驱动低代码平台之一（45K+ Stars），其独特价值在于融合了"零代码"快速搭建与"代码生成"灵活定制双模式，并深度集成 AI 大模型能力，让开发者既能通过自然语言一句话生成完整系统，又能获得可二次开发的源码，在效率与灵活性之间实现了绝佳平衡。

**技术亮点**:
- AI 深度集成：内置 AI 聊天助手、知识库(RAG)、AI 流程编排、MCP 协议与插件体系，兼容 DeepSeek、LangChain4j、Spring AI 等主流大模型生态
- 双模式开发架构：零代码模式支持自然语言一句话生成系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行
- 现代化技术栈：基于 Spring Boot 3 + Vue3 + MyBatis-Plus + Ant Design，支持 Spring Cloud 微服务架构
- 流程引擎支持：集成 Flowable/Activiti 工作流引擎，支持一句话生成流程图和表单设计
- 企业级特性：支持聊天式业务操作，解决 Java 项目 80% 重复工作，兼具高效性与灵活性

**适用场景**:
- 企业快速开发：适合需要快速搭建后台管理系统、CRM、ERP 等业务系统的企业开发团队，大幅缩短开发周期
- AI 应用落地：适合需要快速集成 AI 能力（智能客服、知识问答、AI 流程编排）的项目，降低 AI 应用开发门槛
- 个人/创业项目：适合独立开发者或创业团队快速验证想法、搭建 MVP 产品原型



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,241 |
| 语言 | Python |
| Forks | 9,827 |
| Issues | 354 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,596 |
| 语言 | TypeScript |
| Forks | 2,624 |
| Issues | 119 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,687 |
| 语言 | TypeScript |
| Forks | 7,014 |
| Issues | 454 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,762 |
| 语言 | Python |
| Forks | 6,144 |
| Issues | 186 |
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
| Stars | 33,045 |
| 语言 | TypeScript |
| Forks | 3,555 |
| Issues | 279 |
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
| Stars | 32,167 |
| 语言 | Jupyter Notebook |
| Forks | 5,302 |
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
| Stars | 102,372 |
| 语言 | Python |
| Forks | 14,916 |
| Issues | 10 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,315 |
| 语言 | JavaScript |
| Forks | 6,086 |
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
| Stars | 69,221 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 347 |
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
| Stars | 40,503 |
| 语言 | TypeScript |
| Forks | 3,055 |
| Issues | 389 |
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
| Stars | 80,967 |
| 语言 | Python |
| Forks | 9,565 |
| Issues | 257 |
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
| Stars | 50,802 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 808 |
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
| Stars | 179,441 |
| 语言 | TypeScript |
| Forks | 55,834 |
| Issues | 1,414 |
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
| Stars | 145,732 |
| 语言 | Python |
| Forks | 8,593 |
| Issues | 894 |
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
| Stars | 54,164 |
| 语言 | Jupyter Notebook |
| Forks | 18,772 |
| Issues | 6 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,433 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,417 |
| 语言 | Python |
| Forks | 3,440 |
| Issues | 8 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 44,719 |
| 语言 | Python |
| Forks | 4,523 |
| Issues | 321 |
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
| Stars | 127,444 |
| 语言 | Python |
| Forks | 18,019 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个极具价值的开源AI交互平台，拥有超过12万Star的强大社区支持。它提供了统一的Web界面来连接多种LLM后端（Ollama、OpenAI API等），让用户能够轻松部署和自托管私有AI服务，兼具功能丰富性与易用性。

**技术亮点**:
- 支持多种LLM后端：无缝集成Ollama、OpenAI API等多种大语言模型服务
- RAG（检索增强生成）支持：集成知识库检索能力，提升AI回答准确性
- MCP协议支持：支持Model Context Protocol，实现更灵活的工具调用和上下文管理
- 完全自托管：支持私有化部署，数据安全可控，满足企业隐私合规需求
- 现代化Web界面：基于Python构建的友好UI，支持多用户、对话管理、模型切换等功能

**适用场景**:
- 企业内部AI助手：私有化部署LLM服务，保护敏感数据，为员工提供安全的AI交互平台
- 个人开发者学习和实验：快速搭建本地AI环境，测试不同模型（如通过Ollama运行本地模型）
- AI应用原型开发：作为LLM应用的前端界面，快速验证RAG、多模型切换等功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,141 |
| 语言 | Python |
| Forks | 8,409 |
| Issues | 3,102 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，拥有超过 7.5 万 Star，其独特之处在于将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的优选框架。

**技术亮点**:
- 融合 RAG + Agent 双引擎架构，支持 Agentic Workflow 智能工作流编排
- 强大的文档解析与理解能力（Document Parser & Understanding），支持复杂文档处理
- 原生支持 GraphRAG 图检索增强生成，提升知识关联与推理能力
- 广泛兼容主流 LLM 后端：OpenAI、DeepSeek、Ollama 等，支持 MCP 协议
- 集成 Deep Research 与 AI Search 能力，适合构建深度知识问答系统

**适用场景**:
- 企业知识库构建：快速搭建内部文档检索与智能问答系统，提升知识管理效率
- 智能客服与助手开发：基于企业专属文档构建高准确度的对话式 AI 服务
- 研究与文献分析：利用 Deep Research 和 GraphRAG 能力进行学术文献深度挖掘与知识图谱构建



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,764 |
| 语言 | TypeScript |
| Forks | 14,790 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3万+ Stars 的顶级 AI Agent 开发平台，它将 Agent 协作能力提升到了全新高度。作为一个集成了 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型的开源平台，它不仅支持多 Agent 协作和知识库管理，还引入了 MCP 协议，让开发者能够轻松构建、设计和管理智能 Agent 团队，是实现 AI 驱动工作流的理想选择。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的自动化处理和智能分工
- 全栈 AI 模型集成：原生支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流大语言模型，提供统一的接口层
- MCP 协议支持：集成 Model Context Protocol，实现模型上下文标准化和跨平台互操作
- 知识库管理系统：内置知识库功能，支持 Agent 长期记忆和上下文增强，提升 AI 决策质量
- 现代化 TypeScript 技术栈：采用类型安全的架构设计，提供良好的开发体验和代码可维护性

**适用场景**:
- 企业级 AI 工作流自动化：构建客服机器人、智能助手团队、自动化办公流程等需要多 Agent 协作的业务场景
- AI 应用快速原型开发：个人开发者快速搭建基于大模型的对话应用、知识问答系统和智能工具
- 团队协作与知识管理：为团队提供统一的 AI Agent 平台，实现知识沉淀、智能搜索和协同工作



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,731 |
| 语言 | MDX |
| Forks | 7,661 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前 GitHub 上最全面、最受认可的提示工程学习资源库，涵盖了从基础提示工程到高级 RAG 和 AI Agent 开发的完整知识体系，是掌握现代 AI 应用开发技能的必读指南。

**技术亮点**:
- 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG 检索增强生成、AI Agents 智能体开发
- 提供多形式学习资源：包含理论指南、学术论文、实战课程和 Jupyter Notebook 代码示例
- 紧跟前沿技术趋势：涵盖 LLMs、ChatGPT、OpenAI API 等主流大语言模型工具的最佳实践
- MDX 格式编写，支持 Markdown 与 React 组件混合，便于构建交互式文档
- MIT 开源许可，7万+ Star 社区验证，内容质量高且持续更新

**适用场景**:
- 企业 AI 团队培训：系统学习提示工程和 RAG 技术，提升内部 AI 应用开发能力
- 个人开发者学习路径：从零开始掌握大语言模型应用开发，包括 ChatBot、智能助手等场景
- 产品经理和技术决策者：了解 AI Agent 和 RAG 技术能力边界，规划产品技术方案



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,415 |
| 语言 | Java |
| Forks | 15,841 |
| Issues | 56 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是目前国内最受欢迎的 AI 驱动低代码平台之一（45K+ Stars），其独特价值在于融合了"零代码"快速搭建与"代码生成"灵活定制双模式，并深度集成 AI 大模型能力，让开发者既能通过自然语言一句话生成完整系统，又能获得可二次开发的源码，在效率与灵活性之间实现了绝佳平衡。

**技术亮点**:
- AI 深度集成：内置 AI 聊天助手、知识库(RAG)、AI 流程编排、MCP 协议与插件体系，兼容 DeepSeek、LangChain4j、Spring AI 等主流大模型生态
- 双模式开发架构：零代码模式支持自然语言一句话生成系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行
- 现代化技术栈：基于 Spring Boot 3 + Vue3 + MyBatis-Plus + Ant Design，支持 Spring Cloud 微服务架构
- 流程引擎支持：集成 Flowable/Activiti 工作流引擎，支持一句话生成流程图和表单设计
- 企业级特性：支持聊天式业务操作，解决 Java 项目 80% 重复工作，兼具高效性与灵活性

**适用场景**:
- 企业快速开发：适合需要快速搭建后台管理系统、CRM、ERP 等业务系统的企业开发团队，大幅缩短开发周期
- AI 应用落地：适合需要快速集成 AI 能力（智能客服、知识问答、AI 流程编排）的项目，降低 AI 应用开发门槛
- 个人/创业项目：适合独立开发者或创业团队快速验证想法、搭建 MVP 产品原型



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,596 |
| 语言 | TypeScript |
| Forks | 2,624 |
| Issues | 119 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,762 |
| 语言 | Python |
| Forks | 6,144 |
| Issues | 186 |
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
| Stars | 33,045 |
| 语言 | TypeScript |
| Forks | 3,555 |
| Issues | 279 |
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
| Stars | 32,167 |
| 语言 | Jupyter Notebook |
| Forks | 5,302 |
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
| Stars | 102,372 |
| 语言 | Python |
| Forks | 14,916 |
| Issues | 10 |
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
| Stars | 99,103 |
| 语言 | TypeScript |
| Forks | 11,807 |
| Issues | 938 |
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
| Stars | 56,315 |
| 语言 | JavaScript |
| Forks | 6,086 |
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
| Stars | 50,802 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 808 |
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
| Stars | 72,407 |
| 语言 | Python |
| Forks | 9,973 |
| Issues | 251 |
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
| Stars | 43,366 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,063 |
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
| Stars | 31,523 |
| 语言 | Python |
| Forks | 3,323 |
| Issues | 80 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,433 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


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
| Stars | 127,444 |
| 语言 | Python |
| Forks | 18,019 |
| Issues | 279 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个极具价值的开源AI交互平台，拥有超过12万Star的强大社区支持。它提供了统一的Web界面来连接多种LLM后端（Ollama、OpenAI API等），让用户能够轻松部署和自托管私有AI服务，兼具功能丰富性与易用性。

**技术亮点**:
- 支持多种LLM后端：无缝集成Ollama、OpenAI API等多种大语言模型服务
- RAG（检索增强生成）支持：集成知识库检索能力，提升AI回答准确性
- MCP协议支持：支持Model Context Protocol，实现更灵活的工具调用和上下文管理
- 完全自托管：支持私有化部署，数据安全可控，满足企业隐私合规需求
- 现代化Web界面：基于Python构建的友好UI，支持多用户、对话管理、模型切换等功能

**适用场景**:
- 企业内部AI助手：私有化部署LLM服务，保护敏感数据，为员工提供安全的AI交互平台
- 个人开发者学习和实验：快速搭建本地AI环境，测试不同模型（如通过Ollama运行本地模型）
- AI应用原型开发：作为LLM应用的前端界面，快速验证RAG、多模型切换等功能



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,141 |
| 语言 | Python |
| Forks | 8,409 |
| Issues | 3,102 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，拥有超过 7.5 万 Star，其独特之处在于将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的优选框架。

**技术亮点**:
- 融合 RAG + Agent 双引擎架构，支持 Agentic Workflow 智能工作流编排
- 强大的文档解析与理解能力（Document Parser & Understanding），支持复杂文档处理
- 原生支持 GraphRAG 图检索增强生成，提升知识关联与推理能力
- 广泛兼容主流 LLM 后端：OpenAI、DeepSeek、Ollama 等，支持 MCP 协议
- 集成 Deep Research 与 AI Search 能力，适合构建深度知识问答系统

**适用场景**:
- 企业知识库构建：快速搭建内部文档检索与智能问答系统，提升知识管理效率
- 智能客服与助手开发：基于企业专属文档构建高准确度的对话式 AI 服务
- 研究与文献分析：利用 Deep Research 和 GraphRAG 能力进行学术文献深度挖掘与知识图谱构建



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,045 |
| 语言 | JavaScript |
| Forks | 10,266 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有8万+星标的高人气AI Agent性能优化系统，为Claude Code、Cursor等主流AI编程工具提供了统一的增强框架，通过技能系统、记忆机制和安全控制大幅提升AI辅助开发效率，是当前AI编程工具生态中最全面的性能优化解决方案。

**技术亮点**:
- 多平台统一集成框架 - 支持Claude Code、Codex、Opencode、Cursor等多个AI编程平台，提供跨平台的一致性增强体验
- Agent五维能力系统 - 包含Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）、Research（研究）五大核心模块，全方位优化AI Agent性能
- MCP协议支持 - 集成Model Context Protocol，实现与外部工具和数据的标准化交互，扩展AI能力边界
- 研究优先开发模式 - 采用Research-first理念，AI在编写代码前先进行充分的上下文分析和信息收集，提高代码质量和准确性
- MIT开源许可 - 采用宽松的开源协议，支持商业和私人使用，便于企业集成和二次开发

**适用场景**:
- 企业开发团队集成 - 为使用Claude Code、Cursor等AI编程工具的开发团队提供统一的性能增强层，提升整体开发效率和代码质量
- AI Agent定制化开发 - 开发者可基于此框架为特定业务场景训练和配置专属的AI编程助手，包括自定义技能、记忆持久化和安全策略
- 多AI工具协同场景 - 需要同时使用多个AI编程工具的项目，可通过此系统实现统一的配置管理和能力增强



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,764 |
| 语言 | TypeScript |
| Forks | 14,790 |
| Issues | 648 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3万+ Stars 的顶级 AI Agent 开发平台，它将 Agent 协作能力提升到了全新高度。作为一个集成了 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型的开源平台，它不仅支持多 Agent 协作和知识库管理，还引入了 MCP 协议，让开发者能够轻松构建、设计和管理智能 Agent 团队，是实现 AI 驱动工作流的理想选择。

**技术亮点**:
- 多 Agent 协作架构：支持多个 AI Agent 协同工作，实现复杂任务的自动化处理和智能分工
- 全栈 AI 模型集成：原生支持 ChatGPT、Claude、Gemini、DeepSeek、GPT 等主流大语言模型，提供统一的接口层
- MCP 协议支持：集成 Model Context Protocol，实现模型上下文标准化和跨平台互操作
- 知识库管理系统：内置知识库功能，支持 Agent 长期记忆和上下文增强，提升 AI 决策质量
- 现代化 TypeScript 技术栈：采用类型安全的架构设计，提供良好的开发体验和代码可维护性

**适用场景**:
- 企业级 AI 工作流自动化：构建客服机器人、智能助手团队、自动化办公流程等需要多 Agent 协作的业务场景
- AI 应用快速原型开发：个人开发者快速搭建基于大模型的对话应用、知识问答系统和智能工具
- 团队协作与知识管理：为团队提供统一的 AI Agent 平台，实现知识沉淀、智能搜索和协同工作



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,731 |
| 语言 | MDX |
| Forks | 7,661 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前 GitHub 上最全面、最受认可的提示工程学习资源库，涵盖了从基础提示工程到高级 RAG 和 AI Agent 开发的完整知识体系，是掌握现代 AI 应用开发技能的必读指南。

**技术亮点**:
- 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG 检索增强生成、AI Agents 智能体开发
- 提供多形式学习资源：包含理论指南、学术论文、实战课程和 Jupyter Notebook 代码示例
- 紧跟前沿技术趋势：涵盖 LLMs、ChatGPT、OpenAI API 等主流大语言模型工具的最佳实践
- MDX 格式编写，支持 Markdown 与 React 组件混合，便于构建交互式文档
- MIT 开源许可，7万+ Star 社区验证，内容质量高且持续更新

**适用场景**:
- 企业 AI 团队培训：系统学习提示工程和 RAG 技术，提升内部 AI 应用开发能力
- 个人开发者学习路径：从零开始掌握大语言模型应用开发，包括 ChatBot、智能助手等场景
- 产品经理和技术决策者：了解 AI Agent 和 RAG 技术能力边界，规划产品技术方案



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,864 |
| 语言 | HTML |
| Forks | 20,108 |
| Issues | 33 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,241 |
| 语言 | Python |
| Forks | 9,827 |
| Issues | 354 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,596 |
| 语言 | TypeScript |
| Forks | 2,624 |
| Issues | 119 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,687 |
| 语言 | TypeScript |
| Forks | 7,014 |
| Issues | 454 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,315 |
| 语言 | JavaScript |
| Forks | 6,086 |
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
| Stars | 69,221 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 347 |
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
| Stars | 40,503 |
| 语言 | TypeScript |
| Forks | 3,055 |
| Issues | 389 |
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
| Stars | 50,802 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 808 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,422 |
| 语言 | HTML |
| Forks | 5,537 |
| Issues | 17 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,317 |
| 语言 | Python |
| Forks | 14,420 |
| Issues | 3,713 |
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
| Stars | 42,761 |
| 语言 | Python |
| Forks | 4,134 |
| Issues | 72 |
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
| Stars | 38,986 |
| 语言 | TypeScript |
| Forks | 3,943 |
| Issues | 1,074 |
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
| Stars | 145,732 |
| 语言 | Python |
| Forks | 8,593 |
| Issues | 894 |
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
| Stars | 165,286 |
| 语言 | Go |
| Forks | 15,003 |
| Issues | 2,653 |
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
| Stars | 88,326 |
| 语言 | Jupyter Notebook |
| Forks | 13,476 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,674 |
| 语言 | Rust |
| Forks | 9,131 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,433 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,417 |
| 语言 | Python |
| Forks | 3,440 |
| Issues | 8 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,828 |
| 语言 | Python |
| Forks | 5,362 |
| Issues | 470 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,694 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 63 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 44,719 |
| 语言 | Python |
| Forks | 4,523 |
| Issues | 321 |
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
| Stars | 71,731 |
| 语言 | MDX |
| Forks | 7,661 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前 GitHub 上最全面、最受认可的提示工程学习资源库，涵盖了从基础提示工程到高级 RAG 和 AI Agent 开发的完整知识体系，是掌握现代 AI 应用开发技能的必读指南。

**技术亮点**:
- 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG 检索增强生成、AI Agents 智能体开发
- 提供多形式学习资源：包含理论指南、学术论文、实战课程和 Jupyter Notebook 代码示例
- 紧跟前沿技术趋势：涵盖 LLMs、ChatGPT、OpenAI API 等主流大语言模型工具的最佳实践
- MDX 格式编写，支持 Markdown 与 React 组件混合，便于构建交互式文档
- MIT 开源许可，7万+ Star 社区验证，内容质量高且持续更新

**适用场景**:
- 企业 AI 团队培训：系统学习提示工程和 RAG 技术，提升内部 AI 应用开发能力
- 个人开发者学习路径：从零开始掌握大语言模型应用开发，包括 ChatBot、智能助手等场景
- 产品经理和技术决策者：了解 AI Agent 和 RAG 技术能力边界，规划产品技术方案



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,537 |
| 语言 | Python |
| Forks | 8,359 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的 LLM 微调框架之一，支持 100+ 大语言模型和视觉语言模型的统一高效微调，在 GitHub 上获得 68K+ Stars 的广泛认可，并被 ACL 2024 收录，是企业和研究团队快速定制化大模型的首选工具。

**技术亮点**:
- 统一框架支持 100+ LLMs 和 VLMs（包括 Llama3、Qwen、DeepSeek、Gemma 等主流模型），一套代码适配多种模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化训练，显著降低显存需求和训练成本
- 支持全栈训练流程：指令微调、RLHF（人类反馈强化学习）、MoE（混合专家）模型训练
- 兼容 Transformers 生态，支持 Agent 和 NLP 多种应用场景
- Apache 2.0 开源许可，提供 WebUI 和命令行两种使用方式，易用性强

**适用场景**:
- 企业私有化部署：快速微调开源大模型以适应特定业务场景（如客服、知识库问答、垂直领域应用）
- 学术研究与实验：研究人员可快速对比不同微调方法（LoRA/QLoRA/RLHF）在多种模型上的效果
- 个人开发者学习与实践：低成本上手大模型微调技术，支持消费级 GPU 进行模型训练



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,182 |
| 语言 | Python |
| Forks | 6,205 |
| Issues | 66 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是一个开源的金融数据聚合平台，拥有超过6万Star，为分析师、量化交易员和AI智能体提供统一的数据访问接口，打破了传统金融数据孤岛，让专业级金融数据分析变得开放且易于获取。

**技术亮点**:
- Python原生开发，提供统一的API接口聚合多源金融数据（股票、加密货币、期权、衍生品、宏观经济等）
- 专为AI代理设计的数据平台架构，支持LLM和机器学习模型直接调用结构化金融数据
- 模块化扩展系统，支持自定义数据源接入和功能插件开发
- 支持多资产类别分析：权益、固定收益、衍生品、加密货币全品类覆盖
- 活跃的社区生态，持续更新并整合最新的金融数据源和量化工具

**适用场景**:
- 量化交易团队构建多资产数据分析和回测系统
- AI/ML开发者训练金融预测模型或构建金融智能助手
- 个人投资者和分析师进行深度市场研究和投资决策支持
- 金融科技初创公司快速搭建数据分析原型，降低数据获取成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,864 |
| 语言 | HTML |
| Forks | 20,108 |
| Issues | 33 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,045 |
| 语言 | TypeScript |
| Forks | 3,555 |
| Issues | 279 |
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
| Stars | 32,167 |
| 语言 | Jupyter Notebook |
| Forks | 5,302 |
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
| Stars | 157,932 |
| 语言 | Python |
| Forks | 32,498 |
| Issues | 2,330 |
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
| Stars | 73,317 |
| 语言 | Python |
| Forks | 14,420 |
| Issues | 3,713 |
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
| Stars | 106,051 |
| 语言 | Python |
| Forks | 12,184 |
| Issues | 3,843 |
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
| Stars | 98,330 |
| 语言 | Python |
| Forks | 27,224 |
| Issues | 18,072 |
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
| Stars | 88,326 |
| 语言 | Jupyter Notebook |
| Forks | 13,476 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,812 |
| 语言 | Python |
| Forks | 30,186 |
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
| Stars | 80,045 |
| 语言 | JavaScript |
| Forks | 10,266 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有8万+星标的高人气AI Agent性能优化系统，为Claude Code、Cursor等主流AI编程工具提供了统一的增强框架，通过技能系统、记忆机制和安全控制大幅提升AI辅助开发效率，是当前AI编程工具生态中最全面的性能优化解决方案。

**技术亮点**:
- 多平台统一集成框架 - 支持Claude Code、Codex、Opencode、Cursor等多个AI编程平台，提供跨平台的一致性增强体验
- Agent五维能力系统 - 包含Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）、Research（研究）五大核心模块，全方位优化AI Agent性能
- MCP协议支持 - 集成Model Context Protocol，实现与外部工具和数据的标准化交互，扩展AI能力边界
- 研究优先开发模式 - 采用Research-first理念，AI在编写代码前先进行充分的上下文分析和信息收集，提高代码质量和准确性
- MIT开源许可 - 采用宽松的开源协议，支持商业和私人使用，便于企业集成和二次开发

**适用场景**:
- 企业开发团队集成 - 为使用Claude Code、Cursor等AI编程工具的开发团队提供统一的性能增强层，提升整体开发效率和代码质量
- AI Agent定制化开发 - 开发者可基于此框架为特定业务场景训练和配置专属的AI编程助手，包括自定义技能、记忆持久化和安全策略
- 多AI工具协同场景 - 需要同时使用多个AI编程工具的项目，可通过此系统实现统一的配置管理和能力增强



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,713 |
| 语言 | Go |
| Forks | 3,708 |
| Issues | 147 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费、开源的本地化 AI 解决方案，最大亮点是无需 GPU 就能在消费级硬件上运行，并且提供与 OpenAI API 兼容的接口，让开发者可以零成本、隐私安全地在本地部署大语言模型和多模态生成能力。

**技术亮点**:
- 无需 GPU 的本地推理：专为消费级硬件优化，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：提供 drop-in replacement，现有 OpenAI 应用可无缝迁移
- 多模态全能支持：涵盖文本生成、图像生成、音频/视频生成、语音克隆、目标检测等全栈能力
- 分布式与 P2P 架构：基于 libp2p 实现去中心化推理，支持分布式部署
- 原生 MCP 支持：集成模型上下文协议，便于与 AI 代理和工具链集成

**适用场景**:
- 企业内部 AI 服务：在私有环境中部署文本生成、知识问答和内容创作，保护敏感数据不外泄
- 个人开发者学习与实验：低成本在本地运行 LLaMA、Stable Diffusion 等模型，无需云服务费用
- 边缘设备与离线场景：在没有网络或 GPU 的环境下（如嵌入式设备、老旧服务器）运行 AI 推理



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,221 |
| 语言 | Python |
| Forks | 8,674 |
| Issues | 347 |
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
| Stars | 40,503 |
| 语言 | TypeScript |
| Forks | 3,055 |
| Issues | 389 |
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
| Stars | 179,441 |
| 语言 | TypeScript |
| Forks | 55,834 |
| Issues | 1,414 |
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
| Stars | 151,570 |
| 语言 | Python |
| Forks | 12,279 |
| Issues | 2,370 |
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
| Stars | 96,281 |
| 语言 | Python |
| Forks | 8,865 |
| Issues | 158 |
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
| Stars | 73,774 |
| 语言 | Python |
| Forks | 8,757 |
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
| Stars | 182,738 |
| 语言 | TypeScript |
| Forks | 38,532 |
| Issues | 15,389 |
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
| Stars | 93,840 |
| 语言 | TypeScript |
| Forks | 9,400 |
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
| Stars | 78,474 |
| 语言 | TypeScript |
| Forks | 5,692 |
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
| Stars | 76,682 |
| 语言 | TypeScript |
| Forks | 6,548 |
| Issues | 174 |
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
| Stars | 75,659 |
| 语言 | JavaScript |
| Forks | 7,273 |
| Issues | 706 |
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
| Stars | 78,666 |
| 语言 | Go |
| Forks | 2,732 |
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
| Stars | 74,416 |
| 语言 | Go |
| Forks | 2,613 |
| Issues | 931 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,694 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 63 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 54,493 |
| 语言 | JavaScript |
| Forks | 4,032 |
| Issues | 1,404 |
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
| Stars | 411,023 |
| 语言 | Python |
| Forks | 44,419 |
| Issues | 1,007 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (16 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,503 |
| 语言 | TypeScript |
| Forks | 3,055 |
| Issues | 389 |
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
| Stars | 179,441 |
| 语言 | TypeScript |
| Forks | 55,834 |
| Issues | 1,414 |
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
| Stars | 51,677 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 225 |
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
| Stars | 121,198 |
| 语言 | Go |
| Forks | 42,686 |
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
| Stars | 71,530 |
| 语言 | Go |
| Forks | 18,919 |
| Issues | 3,798 |
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
| Stars | 54,312 |
| 语言 | Go |
| Forks | 6,480 |
| Issues | 2,856 |
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
| Stars | 47,586 |
| 语言 | Go |
| Forks | 5,070 |
| Issues | 963 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
| 许可证 | MIT License |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,417 |
| 语言 | Python |
| Forks | 3,440 |
| Issues | 8 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### puppeteer/puppeteer

**描述**: JavaScript API for Chrome and Firefox

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,840 |
| 语言 | TypeScript |
| Forks | 9,400 |
| Issues | 294 |
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
| Stars | 84,374 |
| 语言 | TypeScript |
| Forks | 5,301 |
| Issues | 621 |
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
| Stars | 75,369 |
| 语言 | TypeScript |
| Forks | 6,402 |
| Issues | 439 |
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
| Stars | 84,149 |
| 语言 | JavaScript |
| Forks | 7,538 |
| Issues | 710 |
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
| Stars | 62,219 |
| 语言 | Go |
| Forks | 5,884 |
| Issues | 778 |
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
| Stars | 57,948 |
| 语言 | Go |
| Forks | 4,203 |
| Issues | 25 |
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
| Stars | 44,719 |
| 语言 | Python |
| Forks | 4,523 |
| Issues | 321 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 69,383 |
| 语言 | Go |
| Forks | 1,879 |
| Issues | 294 |
| Topics | ci, devops, github-actions, golang |
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
| Stars | 84,149 |
| 语言 | JavaScript |
| Forks | 7,538 |
| Issues | 710 |
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
| Stars | 63,219 |
| 语言 | Go |
| Forks | 10,246 |
| Issues | 769 |
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
| Stars | 43,713 |
| 语言 | Go |
| Forks | 3,708 |
| Issues | 147 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费、开源的本地化 AI 解决方案，最大亮点是无需 GPU 就能在消费级硬件上运行，并且提供与 OpenAI API 兼容的接口，让开发者可以零成本、隐私安全地在本地部署大语言模型和多模态生成能力。

**技术亮点**:
- 无需 GPU 的本地推理：专为消费级硬件优化，支持 gguf、transformers、diffusers 等多种模型格式
- OpenAI API 兼容：提供 drop-in replacement，现有 OpenAI 应用可无缝迁移
- 多模态全能支持：涵盖文本生成、图像生成、音频/视频生成、语音克隆、目标检测等全栈能力
- 分布式与 P2P 架构：基于 libp2p 实现去中心化推理，支持分布式部署
- 原生 MCP 支持：集成模型上下文协议，便于与 AI 代理和工具链集成

**适用场景**:
- 企业内部 AI 服务：在私有环境中部署文本生成、知识问答和内容创作，保护敏感数据不外泄
- 个人开发者学习与实验：低成本在本地运行 LLaMA、Stable Diffusion 等模型，无需云服务费用
- 边缘设备与离线场景：在没有网络或 GPU 的环境下（如嵌入式设备、老旧服务器）运行 AI 推理



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,281 |
| 语言 | Python |
| Forks | 8,865 |
| Issues | 158 |
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
| Stars | 87,078 |
| 语言 | Python |
| Forks | 33,752 |
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
| Stars | 100,116 |
| 语言 | TypeScript |
| Forks | 27,129 |
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
| Stars | 78,474 |
| 语言 | TypeScript |
| Forks | 5,692 |
| Issues | 714 |
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
| Stars | 74,950 |
| 语言 | TypeScript |
| Forks | 8,256 |
| Issues | 39 |
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
| Stars | 75,659 |
| 语言 | JavaScript |
| Forks | 7,273 |
| Issues | 706 |
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
| Stars | 55,946 |
| 语言 | JavaScript |
| Forks | 10,228 |
| Issues | 355 |
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
| Stars | 88,279 |
| 语言 | Go |
| Forks | 8,576 |
| Issues | 643 |
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
| Stars | 70,874 |
| 语言 | Go |
| Forks | 4,676 |
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
| Stars | 56,776 |
| 语言 | Go |
| Forks | 3,178 |
| Issues | 24 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,694 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 63 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 411,023 |
| 语言 | Python |
| Forks | 44,419 |
| Issues | 1,007 |
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
| Stars | 68,908 |
| 语言 | JavaScript |
| Forks | 22,844 |
| Issues | 190 |
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
| Stars | 99,103 |
| 语言 | TypeScript |
| Forks | 11,807 |
| Issues | 938 |
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
| Stars | 56,315 |
| 语言 | JavaScript |
| Forks | 6,086 |
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
| Stars | 43,366 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,063 |
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
| Stars | 51,677 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 225 |
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
| Stars | 71,731 |
| 语言 | MDX |
| Forks | 7,661 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前 GitHub 上最全面、最受认可的提示工程学习资源库，涵盖了从基础提示工程到高级 RAG 和 AI Agent 开发的完整知识体系，是掌握现代 AI 应用开发技能的必读指南。

**技术亮点**:
- 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG 检索增强生成、AI Agents 智能体开发
- 提供多形式学习资源：包含理论指南、学术论文、实战课程和 Jupyter Notebook 代码示例
- 紧跟前沿技术趋势：涵盖 LLMs、ChatGPT、OpenAI API 等主流大语言模型工具的最佳实践
- MDX 格式编写，支持 Markdown 与 React 组件混合，便于构建交互式文档
- MIT 开源许可，7万+ Star 社区验证，内容质量高且持续更新

**适用场景**:
- 企业 AI 团队培训：系统学习提示工程和 RAG 技术，提升内部 AI 应用开发能力
- 个人开发者学习路径：从零开始掌握大语言模型应用开发，包括 ChatBot、智能助手等场景
- 产品经理和技术决策者：了解 AI Agent 和 RAG 技术能力边界，规划产品技术方案



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,864 |
| 语言 | HTML |
| Forks | 20,108 |
| Issues | 33 |
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
| Stars | 34,422 |
| 语言 | HTML |
| Forks | 5,537 |
| Issues | 17 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,460 |
| 语言 | TypeScript |
| Forks | 9,926 |
| Issues | 2,197 |
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
| Stars | 86,718 |
| 语言 | TypeScript |
| Forks | 8,736 |
| Issues | 1,612 |
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
| Stars | 127,103 |
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
| Stars | 100,297 |
| 语言 | JavaScript |
| Forks | 7,501 |
| Issues | 222 |
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
| Stars | 167,507 |
| 语言 | Go |
| Forks | 13,061 |
| Issues | 172 |
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
| Stars | 131,517 |
| 语言 | Unknown |
| Forks | 33,368 |
| Issues | 128 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### openclaw/openclaw

**描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 317,130 |
| 语言 | TypeScript |
| Forks | 60,780 |
| Issues | 14,459 |
| Topics | ai, assistant, crustacean, molty, openclaw, own-your-data, personal |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,913 |
| 语言 | Shell |
| Forks | 7,283 |
| Issues | 51 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,041 |
| 语言 | Python |
| Forks | 6,334 |
| Issues | 30 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,059 |
| 语言 | Python |
| Forks | 11,679 |
| Issues | 101 |
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
| Stars | 77,451 |
| 语言 | Python |
| Forks | 6,582 |
| Issues | 637 |
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
| Stars | 384,122 |
| 语言 | Python |
| Forks | 66,031 |
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
| Stars | 112,964 |
| 语言 | TypeScript |
| Forks | 5,729 |
| Issues | 305 |
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
| Stars | 103,222 |
| 语言 | TypeScript |
| Forks | 7,514 |
| Issues | 187 |
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
| Stars | 47,955 |
| 语言 | Go |
| Forks | 10,250 |
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
| Stars | 98,199 |
| 语言 | C++ |
| Forks | 15,543 |
| Issues | 1,281 |
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
| Stars | 59,417 |
| 语言 | Python |
| Forks | 1,607 |
| Issues | 37 |
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
| Stars | 339,108 |
| 语言 | Python |
| Forks | 54,912 |
| Issues | 518 |
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
| Stars | 287,492 |
| 语言 | Python |
| Forks | 27,411 |
| Issues | 21 |
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
| Stars | 218,759 |
| 语言 | Python |
| Forks | 50,212 |
| Issues | 886 |
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
| Stars | 85,378 |
| 语言 | Python |
| Forks | 37,003 |
| Issues | 3,601 |
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
| Stars | 85,307 |
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
| Forks | 45,236 |
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
| Stars | 76,090 |
| 语言 | Python |
| Forks | 16,760 |
| Issues | 16 |
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
| Stars | 438,332 |
| 语言 | TypeScript |
| Forks | 43,652 |
| Issues | 250 |
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
| Stars | 351,033 |
| 语言 | TypeScript |
| Forks | 43,788 |
| Issues | 19 |
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
| Stars | 118,905 |
| 语言 | TypeScript |
| Forks | 12,889 |
| Issues | 2,839 |
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
| Stars | 109,736 |
| 语言 | TypeScript |
| Forks | 8,206 |
| Issues | 1,785 |
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
| Stars | 108,171 |
| 语言 | TypeScript |
| Forks | 13,300 |
| Issues | 5,487 |
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
| Stars | 97,738 |
| 语言 | TypeScript |
| Forks | 54,560 |
| Issues | 1,359 |
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
| Stars | 94,909 |
| 语言 | TypeScript |
| Forks | 5,112 |
| Issues | 651 |
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
| Stars | 94,094 |
| 语言 | TypeScript |
| Forks | 5,120 |
| Issues | 95 |
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
| Stars | 83,003 |
| 语言 | TypeScript |
| Forks | 7,579 |
| Issues | 34 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,239 |
| 语言 | TypeScript |
| Forks | 9,927 |
| Issues | 511 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,077 |
| 语言 | TypeScript |
| Forks | 7,921 |
| Issues | 650 |
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
| Stars | 243,983 |
| 语言 | JavaScript |
| Forks | 50,798 |
| Issues | 1,173 |
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
| Stars | 138,357 |
| 语言 | JavaScript |
| Forks | 30,650 |
| Issues | 3,470 |
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
| Stars | 116,297 |
| 语言 | JavaScript |
| Forks | 35,075 |
| Issues | 2,544 |
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
| Stars | 111,393 |
| 语言 | JavaScript |
| Forks | 36,305 |
| Issues | 588 |
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
| Stars | 108,654 |
| 语言 | JavaScript |
| Forks | 11,557 |
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
| Stars | 98,048 |
| 语言 | JavaScript |
| Forks | 32,712 |
| Issues | 1,723 |
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
| Stars | 95,427 |
| 语言 | JavaScript |
| Forks | 15,255 |
| Issues | 44 |
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
| Stars | 86,085 |
| 语言 | JavaScript |
| Forks | 4,806 |
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
| Stars | 78,752 |
| 语言 | JavaScript |
| Forks | 31,544 |
| Issues | 272 |
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
| Stars | 70,746 |
| 语言 | JavaScript |
| Forks | 16,803 |
| Issues | 886 |
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
| Stars | 66,044 |
| 语言 | JavaScript |
| Forks | 9,328 |
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
| Stars | 62,131 |
| 语言 | JavaScript |
| Forks | 3,977 |
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
| Stars | 59,872 |
| 语言 | JavaScript |
| Forks | 20,468 |
| Issues | 96 |
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
| Stars | 59,860 |
| 语言 | JavaScript |
| Forks | 5,610 |
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
| Stars | 57,400 |
| 语言 | JavaScript |
| Forks | 12,304 |
| Issues | 24 |
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
| Stars | 52,985 |
| 语言 | JavaScript |
| Forks | 10,597 |
| Issues | 481 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,093 |
| 语言 | Go |
| Forks | 18,859 |
| Issues | 9,867 |
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
| Stars | 105,276 |
| 语言 | Go |
| Forks | 14,953 |
| Issues | 46 |
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
| Stars | 87,107 |
| 语言 | Go |
| Forks | 8,205 |
| Issues | 256 |
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
| Stars | 80,868 |
| 语言 | Go |
| Forks | 4,965 |
| Issues | 410 |
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
| Stars | 68,685 |
| 语言 | Go |
| Forks | 3,219 |
| Issues | 8 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,070 |
| 语言 | Go |
| Forks | 4,972 |
| Issues | 1,141 |
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
| Stars | 50,921 |
| 语言 | Go |
| Forks | 21,856 |
| Issues | 374 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,152 |
| 语言 | Go |
| Forks | 1,589 |
| Issues | 258 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,171 |
| 语言 | Go |
| Forks | 7,979 |
| Issues | 565 |
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
| Stars | 46,955 |
| 语言 | Go |
| Forks | 8,880 |
| Issues | 8 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
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
| Stars | 139,881 |
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
| Stars | 195,793 |
| 语言 | JavaScript |
| Forks | 31,116 |
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
| Stars | 148,125 |
| 语言 | JavaScript |
| Forks | 26,772 |
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
| Stars | 67,265 |
| 语言 | JavaScript |
| Forks | 11,981 |
| Issues | 538 |
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
| Stars | 66,283 |
| 语言 | JavaScript |
| Forks | 9,189 |
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
| Stars | 61,580 |
| 语言 | JavaScript |
| Forks | 7,128 |
| Issues | 132 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 45,482 |
| 语言 | Go |
| Forks | 3,769 |
| Issues | 91 |
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
| Stars | 146,360 |
| 语言 | Python |
| Forks | 11,228 |
| Issues | 296 |
| Topics | awesome, github, hellogithub, python |
