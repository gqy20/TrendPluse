# 项目发现报告 (2026-03-19)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 133 |
| 去重移除 | 31 |
| 已在监控 | 23 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 27 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 14 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
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


## 🤖 AI Agents (28 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,893 |
| 语言 | Python |
| Forks | 18,073 |
| Issues | 317 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个功能全面、开箱即用的自托管AI交互平台，支持Ollama和OpenAI API等多种后端，让用户无需依赖第三方服务即可部署属于自己的ChatGPT风格界面。项目拥有12.7万+ Stars，是目前最成熟的LLM WebUI解决方案之一，兼具易用性和强大的扩展能力。

**技术亮点**:
- 支持多种LLM后端接入（Ollama、OpenAI API、OpenAPI兼容接口），灵活切换不同模型
- 内置RAG（检索增强生成）能力，支持知识库上传与文档对话
- 支持MCP（Model Context Protocol）协议，便于模型上下文扩展
- 完全自托管部署，数据隐私可控，支持私有化环境运行
- 现代化的Python技术栈，社区活跃，功能迭代快速

**适用场景**:
- 企业内部私有化部署AI助手，保护敏感数据不外泄
- 个人开发者搭建本地LLM服务前端，配合Ollama实现离线AI对话
- 构建基于知识库的智能问答系统，支持上传企业文档进行RAG检索



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,517 |
| 语言 | Python |
| Forks | 8,460 |
| Issues | 3,130 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，拥有 7.5万+ Stars，其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅是检索增强，还支持 Agentic Workflow 和 Agentic AI，实现智能化的文档理解和交互
- 强大的文档处理能力：内置 Document Parser 和 Deep Research 功能，支持复杂文档的深度理解与解析
- 全面的生态兼容：支持 OpenAI、Ollama、DeepSeek-R1 等主流 LLM，以及 MCP（Model Context Protocol）协议
- 先进的检索技术：整合 GraphRAG 图检索技术，提供更精准的上下文检索和 Context Engineering
- AI 搜索与深度理解：结合 AI Search 和 Document Understanding，打造智能化的知识检索引擎

**适用场景**:
- 企业知识库构建：为企业搭建智能文档检索和问答系统，快速从海量文档中提取关键信息
- 智能客服与助手开发：基于企业私有数据构建 AI 客服、智能助手，提供精准的业务知识回答
- 研究与文档分析：学术研究、法律文档、技术文档的深度分析和知识提取，辅助专业决策



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,274 |
| 语言 | TypeScript |
| Forks | 6,516 |
| Issues | 221 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个专为 AI 应用设计的网页数据采集工具，能够将任意网站转换为 LLM-ready 的 Markdown 或结构化数据，极大简化了 AI 应用开发中的数据准备流程。作为拥有近 10 万 Star 的明星项目，它解决了 AI 开发中最耗时的数据采集和清洗环节，是目前最成熟的 AI 数据采集解决方案之一。

**技术亮点**:
- 支持将 HTML 网页自动转换为 LLM 友好的 Markdown 格式，保留文档结构和语义信息
- 提供强大的数据提取能力，支持从复杂网页中抽取结构化数据
- 内置 AI 代理和 AI 搜索功能，智能识别和处理网页内容
- 基于 TypeScript 构建，提供 Web Data API，易于集成到各类 AI 应用中
- 支持 Web Crawler 和 Scraper 功能，可处理动态内容和复杂网站结构

**适用场景**:
- 构建 RAG（检索增强生成）应用时，用于从企业官网、文档站点抓取知识库内容
- AI Agent 开发中，需要从网页实时获取数据进行分析和决策的场景
- 数据科学家和研究人员需要从多个网站批量采集数据进行分析和训练模型



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,655 |
| 语言 | JavaScript |
| Forks | 11,486 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的AI智能体优化系统，整合了技能、本能、记忆、安全和研究驱动开发等核心能力，为Claude Code、Cursor等主流AI编程工具提供统一的能力增强框架，极大提升AI辅助开发的效率和质量。87K+的Star数证明了其在AI开发者社区中的重要地位和实用价值。

**技术亮点**:
- 智能体能力增强框架：整合技能系统、本能反应、持久记忆等多维度能力，实现AI智能体的全面优化
- 跨平台兼容架构：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一接口
- 安全与性能并重：内置安全机制的同时专注于性能优化，确保AI代理的可靠性和高效性
- MCP协议集成：支持Model Context Protocol，实现与AI模型的标准化交互
- 研究驱动开发模式：采用Research-First方法论，基于实际研究和测试数据优化系统性能

**适用场景**:
- 企业AI开发团队：为使用Claude Code、Cursor等AI编程助手的开发团队提供性能优化和能力扩展方案
- 个人开发者：希望提升AI编程工具效率，获得更智能代码生成和开发辅助的独立开发者
- AI智能体应用开发：构建复杂AI应用系统，需要记忆、安全、技能管理等高级功能的开发者



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,037 |
| 语言 | Go |
| Forks | 3,757 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费开源的本地化 AI 解决方案，作为 OpenAI 等商业服务的直接替代品，它无需 GPU 就能在消费级硬件上运行，支持文本、图像、音频、视频等多模态生成，特别适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers）和架构（LLaMA、Mamba等），兼容性极强
- 无需GPU即可在消费级硬件上运行，大幅降低部署门槛和硬件成本
- 完整的OpenAI API兼容性，实现drop-in replacement无缝迁移
- 支持分布式和P2P去中心化推理（基于libp2p），具备横向扩展能力
- 多模态能力全覆盖：文本生成、图像生成、音频生成、视频、语音克隆、TTS等

**适用场景**:
- 企业内部私有化部署AI服务，确保敏感数据不出本地，满足合规和隐私要求
- 个人开发者或创业团队在预算有限情况下，构建AI应用而无需承担高昂的API调用费用
- 边缘设备和离线场景下的AI应用部署，如IoT设备、移动应用或网络受限环境



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,979 |
| 语言 | TypeScript |
| Forks | 14,809 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的热门开源 AI Agent 平台，它不仅是聊天界面，更是一个完整的多智能体协作生态系统。支持 GPT、Claude、Gemini、DeepSeek 等多种主流大模型，通过 MCP 协议和知识库功能，让用户能够轻松构建、部署和管理个性化的 AI 智能体团队，是个人和企业 AI 应用开发的理想选择。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 协同工作，将 Agent 作为工作交互的基本单元
- 多模型统一接入：兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，灵活切换
- MCP 协议支持：通过 Model Context Protocol 实现与外部工具和知识库的无缝集成
- 知识库管理：内置知识库功能，支持文档上传、向量检索和 RAG 增强生成
- 现代化 TypeScript 技术栈：采用 TypeScript 开发，提供良好的类型安全和开发体验

**适用场景**:
- 个人知识管理与智能助手：搭建个人 AI 工作空间，整合多个 AI 模型处理日常任务、知识整理和学习辅助
- 企业 AI 中台建设：作为企业级 AI 应用基础平台，统一管理多个 AI 模型，构建业务专属的智能体团队
- AI 应用快速原型开发：开发者可基于 LobeHub 快速搭建和测试多智能体协作应用，降低 AI 应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,954 |
| 语言 | MDX |
| Forks | 7,683 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71k+ stars的提示工程领域顶级开源资源库，系统性地整合了从基础Prompt Engineering到高级AI Agent开发的完整知识体系，涵盖理论指南、学术论文、实践教程和可运行代码，是AI开发者和大模型应用工程师必学的核心参考资料。

**技术亮点**:
- 📖 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG检索增强生成、AI Agent开发
- 🎯 融合理论与实践：包含学术论文、教程指南、Jupyter Notebook可执行示例，实现从理论到落地的完整闭环
- 🤖 紧跟AI前沿技术：涵盖ChatGPT、OpenAI API、大语言模型(LLMs)、生成式AI等最新技术应用
- 📑 采用MDX格式：支持在Markdown中嵌入交互式组件，提供更丰富的学习体验
- 🔬 开源社区驱动：MIT许可证，持续更新，汇集全球AI社区的最佳实践经验

**适用场景**:
- 🏢 企业AI应用开发：帮助团队快速掌握大模型应用开发技能，构建智能客服、知识库问答、自动化工作流等企业级AI解决方案
- 👨‍💻 个人开发者学习：作为系统学习Prompt Engineering和大模型应用开发的完整教程，从入门到进阶的技能提升路径
- 🎓 AI研究与教育：为研究人员和教育者提供丰富的学术论文资源和教学材料，支持课程设计和前沿技术探索



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,742 |
| 语言 | Python |
| Forks | 8,377 |
| Issues | 933 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个功能强大且生产就绪的大模型微调框架，支持100+主流LLM和VLM的统一高效微调，拥有68K+ Stars证明了其社区活跃度和实用性。作为ACL 2024论文项目，它将前沿研究成果转化为易用的工具，降低了企业落地大模型的门槛。

**技术亮点**:
- 支持100+主流大语言模型和多模态模型的统一微调框架，涵盖Llama3、Qwen、DeepSeek、Gemma等最新模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化技术，大幅降低显存需求和训练成本
- 支持全栈训练流程：指令微调、RLHF人类反馈强化学习、MoE混合专家模型训练
- 提供Agent能力支持，可构建具备工具调用和推理能力的智能体应用
- 与Transformers生态深度集成，提供开箱即用的训练和推理Pipeline

**适用场景**:
- 企业级大模型私有化部署：基于开源模型快速微调领域专用模型，保护数据隐私并降低API成本
- 学术研究与实验：快速验证不同微调策略（LoRA/QLoRA/RLHF）在各类模型上的效果对比
- AI应用开发与产品化：将通用大模型适配到垂直场景（客服、医疗、法律、教育等），提升专业领域能力



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,456 |
| 语言 | Java |
| Forks | 15,843 |
| Issues | 59 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 能力的企业级低代码平台，以"零代码"+"代码生成"双模式帮助开发者快速搭建系统，结合 AI 聊天助手、流程编排和知识库等智能化功能，大幅提升 Java 项目开发效率，是追求高效交付与灵活定制团队的理想选择。

**技术亮点**:
- AI 深度集成：内置 AI 聊天助手、兼容主流大模型（DeepSeek、Spring AI、LangChain4j），支持 RAG 知识库与 MCP 插件体系
- 双模式开发：零代码一句话生成系统 + 代码生成模式自动输出前后端代码与建表 SQL，兼顾效率与可控性
- 流程编排能力：支持 AI 流程编排（AIFlow）、Flowable/Activiti 工作流，一句话生成流程图
- 现代技术栈：基于 Spring Boot 3、Spring Cloud、Vue3、Ant Design、MyBatis-Plus，面向企业级架构设计
- 智能表单与业务：支持一句话设计表单、聊天式业务操作，降低开发门槛

**适用场景**:
- 企业内部管理系统（OA、ERP、CRM 等）快速搭建与定制开发
- Java 团队希望减少重复编码工作、加速项目交付的场景
- 需要快速验证业务想法或搭建 MVP 的创业团队/个人开发者



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,313 |
| 语言 | Python |
| Forks | 9,840 |
| Issues | 348 |
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
| Stars | 38,395 |
| 语言 | JavaScript |
| Forks | 2,773 |
| Issues | 126 |
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
| Stars | 34,784 |
| 语言 | TypeScript |
| Forks | 7,038 |
| Issues | 464 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,496 |
| 语言 | Python |
| Forks | 2,072 |
| Issues | 93 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,494 |
| 语言 | TypeScript |
| Forks | 5,464 |
| Issues | 55 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,789 |
| 语言 | Python |
| Forks | 6,149 |
| Issues | 171 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,304 |
| 语言 | Jupyter Notebook |
| Forks | 5,331 |
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
| Stars | 102,865 |
| 语言 | Python |
| Forks | 14,993 |
| Issues | 13 |
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
| Stars | 56,466 |
| 语言 | JavaScript |
| Forks | 6,100 |
| Issues | 304 |
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
| Stars | 69,418 |
| 语言 | Python |
| Forks | 8,702 |
| Issues | 326 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### unslothai/unsloth

**描述**: Unified web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,587 |
| 语言 | Python |
| Forks | 4,746 |
| Issues | 993 |
| Topics | agent, deepseek, deepseek-r1, fine-tuning, gemma, gemma3, gpt-oss, llama, llama3, llm, llms, mistral, openai, qwen, qwen3, reinforcement-learning, text-to-speech, tts, unsloth, voice-cloning |
| 许可证 | Apache License 2.0 |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,555 |
| 语言 | TypeScript |
| Forks | 3,105 |
| Issues | 425 |
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
| Stars | 81,319 |
| 语言 | Python |
| Forks | 9,605 |
| Issues | 223 |
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
| Stars | 50,911 |
| 语言 | TypeScript |
| Forks | 23,980 |
| Issues | 809 |
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
| Stars | 180,022 |
| 语言 | TypeScript |
| Forks | 55,970 |
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
| Stars | 145,902 |
| 语言 | Python |
| Forks | 8,614 |
| Issues | 896 |
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
| Stars | 54,479 |
| 语言 | Jupyter Notebook |
| Forks | 18,857 |
| Issues | 2 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,142 |
| 语言 | TypeScript |
| Forks | 3,569 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,075 |
| 语言 | Python |
| Forks | 4,683 |
| Issues | 335 |
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
| Stars | 127,893 |
| 语言 | Python |
| Forks | 18,073 |
| Issues | 317 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个功能全面、开箱即用的自托管AI交互平台，支持Ollama和OpenAI API等多种后端，让用户无需依赖第三方服务即可部署属于自己的ChatGPT风格界面。项目拥有12.7万+ Stars，是目前最成熟的LLM WebUI解决方案之一，兼具易用性和强大的扩展能力。

**技术亮点**:
- 支持多种LLM后端接入（Ollama、OpenAI API、OpenAPI兼容接口），灵活切换不同模型
- 内置RAG（检索增强生成）能力，支持知识库上传与文档对话
- 支持MCP（Model Context Protocol）协议，便于模型上下文扩展
- 完全自托管部署，数据隐私可控，支持私有化环境运行
- 现代化的Python技术栈，社区活跃，功能迭代快速

**适用场景**:
- 企业内部私有化部署AI助手，保护敏感数据不外泄
- 个人开发者搭建本地LLM服务前端，配合Ollama实现离线AI对话
- 构建基于知识库的智能问答系统，支持上传企业文档进行RAG检索



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,517 |
| 语言 | Python |
| Forks | 8,460 |
| Issues | 3,130 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，拥有 7.5万+ Stars，其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅是检索增强，还支持 Agentic Workflow 和 Agentic AI，实现智能化的文档理解和交互
- 强大的文档处理能力：内置 Document Parser 和 Deep Research 功能，支持复杂文档的深度理解与解析
- 全面的生态兼容：支持 OpenAI、Ollama、DeepSeek-R1 等主流 LLM，以及 MCP（Model Context Protocol）协议
- 先进的检索技术：整合 GraphRAG 图检索技术，提供更精准的上下文检索和 Context Engineering
- AI 搜索与深度理解：结合 AI Search 和 Document Understanding，打造智能化的知识检索引擎

**适用场景**:
- 企业知识库构建：为企业搭建智能文档检索和问答系统，快速从海量文档中提取关键信息
- 智能客服与助手开发：基于企业私有数据构建 AI 客服、智能助手，提供精准的业务知识回答
- 研究与文档分析：学术研究、法律文档、技术文档的深度分析和知识提取，辅助专业决策



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,979 |
| 语言 | TypeScript |
| Forks | 14,809 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的热门开源 AI Agent 平台，它不仅是聊天界面，更是一个完整的多智能体协作生态系统。支持 GPT、Claude、Gemini、DeepSeek 等多种主流大模型，通过 MCP 协议和知识库功能，让用户能够轻松构建、部署和管理个性化的 AI 智能体团队，是个人和企业 AI 应用开发的理想选择。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 协同工作，将 Agent 作为工作交互的基本单元
- 多模型统一接入：兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，灵活切换
- MCP 协议支持：通过 Model Context Protocol 实现与外部工具和知识库的无缝集成
- 知识库管理：内置知识库功能，支持文档上传、向量检索和 RAG 增强生成
- 现代化 TypeScript 技术栈：采用 TypeScript 开发，提供良好的类型安全和开发体验

**适用场景**:
- 个人知识管理与智能助手：搭建个人 AI 工作空间，整合多个 AI 模型处理日常任务、知识整理和学习辅助
- 企业 AI 中台建设：作为企业级 AI 应用基础平台，统一管理多个 AI 模型，构建业务专属的智能体团队
- AI 应用快速原型开发：开发者可基于 LobeHub 快速搭建和测试多智能体协作应用，降低 AI 应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,954 |
| 语言 | MDX |
| Forks | 7,683 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71k+ stars的提示工程领域顶级开源资源库，系统性地整合了从基础Prompt Engineering到高级AI Agent开发的完整知识体系，涵盖理论指南、学术论文、实践教程和可运行代码，是AI开发者和大模型应用工程师必学的核心参考资料。

**技术亮点**:
- 📖 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG检索增强生成、AI Agent开发
- 🎯 融合理论与实践：包含学术论文、教程指南、Jupyter Notebook可执行示例，实现从理论到落地的完整闭环
- 🤖 紧跟AI前沿技术：涵盖ChatGPT、OpenAI API、大语言模型(LLMs)、生成式AI等最新技术应用
- 📑 采用MDX格式：支持在Markdown中嵌入交互式组件，提供更丰富的学习体验
- 🔬 开源社区驱动：MIT许可证，持续更新，汇集全球AI社区的最佳实践经验

**适用场景**:
- 🏢 企业AI应用开发：帮助团队快速掌握大模型应用开发技能，构建智能客服、知识库问答、自动化工作流等企业级AI解决方案
- 👨‍💻 个人开发者学习：作为系统学习Prompt Engineering和大模型应用开发的完整教程，从入门到进阶的技能提升路径
- 🎓 AI研究与教育：为研究人员和教育者提供丰富的学术论文资源和教学材料，支持课程设计和前沿技术探索



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,456 |
| 语言 | Java |
| Forks | 15,843 |
| Issues | 59 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 能力的企业级低代码平台，以"零代码"+"代码生成"双模式帮助开发者快速搭建系统，结合 AI 聊天助手、流程编排和知识库等智能化功能，大幅提升 Java 项目开发效率，是追求高效交付与灵活定制团队的理想选择。

**技术亮点**:
- AI 深度集成：内置 AI 聊天助手、兼容主流大模型（DeepSeek、Spring AI、LangChain4j），支持 RAG 知识库与 MCP 插件体系
- 双模式开发：零代码一句话生成系统 + 代码生成模式自动输出前后端代码与建表 SQL，兼顾效率与可控性
- 流程编排能力：支持 AI 流程编排（AIFlow）、Flowable/Activiti 工作流，一句话生成流程图
- 现代技术栈：基于 Spring Boot 3、Spring Cloud、Vue3、Ant Design、MyBatis-Plus，面向企业级架构设计
- 智能表单与业务：支持一句话设计表单、聊天式业务操作，降低开发门槛

**适用场景**:
- 企业内部管理系统（OA、ERP、CRM 等）快速搭建与定制开发
- Java 团队希望减少重复编码工作、加速项目交付的场景
- 需要快速验证业务想法或搭建 MVP 的创业团队/个人开发者



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,395 |
| 语言 | JavaScript |
| Forks | 2,773 |
| Issues | 126 |
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
| Stars | 33,496 |
| 语言 | Python |
| Forks | 2,072 |
| Issues | 93 |
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
| Stars | 38,789 |
| 语言 | Python |
| Forks | 6,149 |
| Issues | 171 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,304 |
| 语言 | Jupyter Notebook |
| Forks | 5,331 |
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
| Stars | 102,865 |
| 语言 | Python |
| Forks | 14,993 |
| Issues | 13 |
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
| Stars | 99,265 |
| 语言 | TypeScript |
| Forks | 11,839 |
| Issues | 954 |
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
| Stars | 56,466 |
| 语言 | JavaScript |
| Forks | 6,100 |
| Issues | 304 |
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
| Stars | 50,911 |
| 语言 | TypeScript |
| Forks | 23,980 |
| Issues | 809 |
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
| Stars | 72,630 |
| 语言 | Python |
| Forks | 9,999 |
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
| Stars | 43,385 |
| 语言 | Go |
| Forks | 3,903 |
| Issues | 1,092 |
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
| Stars | 31,625 |
| 语言 | Python |
| Forks | 3,334 |
| Issues | 79 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,142 |
| 语言 | TypeScript |
| Forks | 3,569 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (27 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,893 |
| 语言 | Python |
| Forks | 18,073 |
| Issues | 317 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

这是一个功能全面、开箱即用的自托管AI交互平台，支持Ollama和OpenAI API等多种后端，让用户无需依赖第三方服务即可部署属于自己的ChatGPT风格界面。项目拥有12.7万+ Stars，是目前最成熟的LLM WebUI解决方案之一，兼具易用性和强大的扩展能力。

**技术亮点**:
- 支持多种LLM后端接入（Ollama、OpenAI API、OpenAPI兼容接口），灵活切换不同模型
- 内置RAG（检索增强生成）能力，支持知识库上传与文档对话
- 支持MCP（Model Context Protocol）协议，便于模型上下文扩展
- 完全自托管部署，数据隐私可控，支持私有化环境运行
- 现代化的Python技术栈，社区活跃，功能迭代快速

**适用场景**:
- 企业内部私有化部署AI助手，保护敏感数据不外泄
- 个人开发者搭建本地LLM服务前端，配合Ollama实现离线AI对话
- 构建基于知识库的智能问答系统，支持上传企业文档进行RAG检索



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,517 |
| 语言 | Python |
| Forks | 8,460 |
| Issues | 3,130 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，拥有 7.5万+ Stars，其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为大语言模型构建了卓越的上下文理解层，是企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅是检索增强，还支持 Agentic Workflow 和 Agentic AI，实现智能化的文档理解和交互
- 强大的文档处理能力：内置 Document Parser 和 Deep Research 功能，支持复杂文档的深度理解与解析
- 全面的生态兼容：支持 OpenAI、Ollama、DeepSeek-R1 等主流 LLM，以及 MCP（Model Context Protocol）协议
- 先进的检索技术：整合 GraphRAG 图检索技术，提供更精准的上下文检索和 Context Engineering
- AI 搜索与深度理解：结合 AI Search 和 Document Understanding，打造智能化的知识检索引擎

**适用场景**:
- 企业知识库构建：为企业搭建智能文档检索和问答系统，快速从海量文档中提取关键信息
- 智能客服与助手开发：基于企业私有数据构建 AI 客服、智能助手，提供精准的业务知识回答
- 研究与文档分析：学术研究、法律文档、技术文档的深度分析和知识提取，辅助专业决策



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,655 |
| 语言 | JavaScript |
| Forks | 11,486 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的AI智能体优化系统，整合了技能、本能、记忆、安全和研究驱动开发等核心能力，为Claude Code、Cursor等主流AI编程工具提供统一的能力增强框架，极大提升AI辅助开发的效率和质量。87K+的Star数证明了其在AI开发者社区中的重要地位和实用价值。

**技术亮点**:
- 智能体能力增强框架：整合技能系统、本能反应、持久记忆等多维度能力，实现AI智能体的全面优化
- 跨平台兼容架构：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一接口
- 安全与性能并重：内置安全机制的同时专注于性能优化，确保AI代理的可靠性和高效性
- MCP协议集成：支持Model Context Protocol，实现与AI模型的标准化交互
- 研究驱动开发模式：采用Research-First方法论，基于实际研究和测试数据优化系统性能

**适用场景**:
- 企业AI开发团队：为使用Claude Code、Cursor等AI编程助手的开发团队提供性能优化和能力扩展方案
- 个人开发者：希望提升AI编程工具效率，获得更智能代码生成和开发辅助的独立开发者
- AI智能体应用开发：构建复杂AI应用系统，需要记忆、安全、技能管理等高级功能的开发者



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,979 |
| 语言 | TypeScript |
| Forks | 14,809 |
| Issues | 672 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 7.3 万+ Stars 的热门开源 AI Agent 平台，它不仅是聊天界面，更是一个完整的多智能体协作生态系统。支持 GPT、Claude、Gemini、DeepSeek 等多种主流大模型，通过 MCP 协议和知识库功能，让用户能够轻松构建、部署和管理个性化的 AI 智能体团队，是个人和企业 AI 应用开发的理想选择。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 协同工作，将 Agent 作为工作交互的基本单元
- 多模型统一接入：兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，灵活切换
- MCP 协议支持：通过 Model Context Protocol 实现与外部工具和知识库的无缝集成
- 知识库管理：内置知识库功能，支持文档上传、向量检索和 RAG 增强生成
- 现代化 TypeScript 技术栈：采用 TypeScript 开发，提供良好的类型安全和开发体验

**适用场景**:
- 个人知识管理与智能助手：搭建个人 AI 工作空间，整合多个 AI 模型处理日常任务、知识整理和学习辅助
- 企业 AI 中台建设：作为企业级 AI 应用基础平台，统一管理多个 AI 模型，构建业务专属的智能体团队
- AI 应用快速原型开发：开发者可基于 LobeHub 快速搭建和测试多智能体协作应用，降低 AI 应用开发门槛



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,954 |
| 语言 | MDX |
| Forks | 7,683 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71k+ stars的提示工程领域顶级开源资源库，系统性地整合了从基础Prompt Engineering到高级AI Agent开发的完整知识体系，涵盖理论指南、学术论文、实践教程和可运行代码，是AI开发者和大模型应用工程师必学的核心参考资料。

**技术亮点**:
- 📖 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG检索增强生成、AI Agent开发
- 🎯 融合理论与实践：包含学术论文、教程指南、Jupyter Notebook可执行示例，实现从理论到落地的完整闭环
- 🤖 紧跟AI前沿技术：涵盖ChatGPT、OpenAI API、大语言模型(LLMs)、生成式AI等最新技术应用
- 📑 采用MDX格式：支持在Markdown中嵌入交互式组件，提供更丰富的学习体验
- 🔬 开源社区驱动：MIT许可证，持续更新，汇集全球AI社区的最佳实践经验

**适用场景**:
- 🏢 企业AI应用开发：帮助团队快速掌握大模型应用开发技能，构建智能客服、知识库问答、自动化工作流等企业级AI解决方案
- 👨‍💻 个人开发者学习：作为系统学习Prompt Engineering和大模型应用开发的完整教程，从入门到进阶的技能提升路径
- 🎓 AI研究与教育：为研究人员和教育者提供丰富的学术论文资源和教学材料，支持课程设计和前沿技术探索



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,338 |
| 语言 | HTML |
| Forks | 20,179 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,313 |
| 语言 | Python |
| Forks | 9,840 |
| Issues | 348 |
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
| Stars | 38,395 |
| 语言 | JavaScript |
| Forks | 2,773 |
| Issues | 126 |
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
| Stars | 34,784 |
| 语言 | TypeScript |
| Forks | 7,038 |
| Issues | 464 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,496 |
| 语言 | Python |
| Forks | 2,072 |
| Issues | 93 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,494 |
| 语言 | TypeScript |
| Forks | 5,464 |
| Issues | 55 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,466 |
| 语言 | JavaScript |
| Forks | 6,100 |
| Issues | 304 |
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
| Stars | 69,418 |
| 语言 | Python |
| Forks | 8,702 |
| Issues | 326 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### unslothai/unsloth

**描述**: Unified web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,587 |
| 语言 | Python |
| Forks | 4,746 |
| Issues | 993 |
| Topics | agent, deepseek, deepseek-r1, fine-tuning, gemma, gemma3, gpt-oss, llama, llama3, llm, llms, mistral, openai, qwen, qwen3, reinforcement-learning, text-to-speech, tts, unsloth, voice-cloning |
| 许可证 | Apache License 2.0 |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,555 |
| 语言 | TypeScript |
| Forks | 3,105 |
| Issues | 425 |
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
| Stars | 50,911 |
| 语言 | TypeScript |
| Forks | 23,980 |
| Issues | 809 |
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
| Stars | 34,669 |
| 语言 | HTML |
| Forks | 5,574 |
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
| Stars | 73,699 |
| 语言 | Python |
| Forks | 14,554 |
| Issues | 3,798 |
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
| Stars | 39,034 |
| 语言 | TypeScript |
| Forks | 3,951 |
| Issues | 1,078 |
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
| Stars | 145,902 |
| 语言 | Python |
| Forks | 8,614 |
| Issues | 896 |
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
| Stars | 165,589 |
| 语言 | Go |
| Forks | 15,058 |
| Issues | 2,683 |
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
| Stars | 88,748 |
| 语言 | Jupyter Notebook |
| Forks | 13,553 |
| Issues | 6 |
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
| Stars | 46,740 |
| 语言 | Rust |
| Forks | 9,147 |
| Issues | 0 |
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
| Stars | 90,983 |
| 语言 | Python |
| Forks | 5,381 |
| Issues | 473 |
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
| Stars | 46,037 |
| 语言 | Python |
| Forks | 4,451 |
| Issues | 79 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,781 |
| 语言 | Python |
| Forks | 2,572 |
| Issues | 64 |
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
| Stars | 46,075 |
| 语言 | Python |
| Forks | 4,683 |
| Issues | 335 |
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
| Stars | 71,954 |
| 语言 | MDX |
| Forks | 7,683 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71k+ stars的提示工程领域顶级开源资源库，系统性地整合了从基础Prompt Engineering到高级AI Agent开发的完整知识体系，涵盖理论指南、学术论文、实践教程和可运行代码，是AI开发者和大模型应用工程师必学的核心参考资料。

**技术亮点**:
- 📖 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG检索增强生成、AI Agent开发
- 🎯 融合理论与实践：包含学术论文、教程指南、Jupyter Notebook可执行示例，实现从理论到落地的完整闭环
- 🤖 紧跟AI前沿技术：涵盖ChatGPT、OpenAI API、大语言模型(LLMs)、生成式AI等最新技术应用
- 📑 采用MDX格式：支持在Markdown中嵌入交互式组件，提供更丰富的学习体验
- 🔬 开源社区驱动：MIT许可证，持续更新，汇集全球AI社区的最佳实践经验

**适用场景**:
- 🏢 企业AI应用开发：帮助团队快速掌握大模型应用开发技能，构建智能客服、知识库问答、自动化工作流等企业级AI解决方案
- 👨‍💻 个人开发者学习：作为系统学习Prompt Engineering和大模型应用开发的完整教程，从入门到进阶的技能提升路径
- 🎓 AI研究与教育：为研究人员和教育者提供丰富的学术论文资源和教学材料，支持课程设计和前沿技术探索



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,742 |
| 语言 | Python |
| Forks | 8,377 |
| Issues | 933 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个功能强大且生产就绪的大模型微调框架，支持100+主流LLM和VLM的统一高效微调，拥有68K+ Stars证明了其社区活跃度和实用性。作为ACL 2024论文项目，它将前沿研究成果转化为易用的工具，降低了企业落地大模型的门槛。

**技术亮点**:
- 支持100+主流大语言模型和多模态模型的统一微调框架，涵盖Llama3、Qwen、DeepSeek、Gemma等最新模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、量化技术，大幅降低显存需求和训练成本
- 支持全栈训练流程：指令微调、RLHF人类反馈强化学习、MoE混合专家模型训练
- 提供Agent能力支持，可构建具备工具调用和推理能力的智能体应用
- 与Transformers生态深度集成，提供开箱即用的训练和推理Pipeline

**适用场景**:
- 企业级大模型私有化部署：基于开源模型快速微调领域专用模型，保护数据隐私并降低API成本
- 学术研究与实验：快速验证不同微调策略（LoRA/QLoRA/RLHF）在各类模型上的效果对比
- AI应用开发与产品化：将通用大模型适配到垂直场景（客服、医疗、法律、教育等），提升专业领域能力



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,327 |
| 语言 | Python |
| Forks | 6,232 |
| Issues | 65 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是一个领先的开源金融数据平台，拥有超过6.3万Stars的庞大社区支持，为分析师、量化交易者和AI代理提供统一的数据访问接口，打破了传统金融数据被商业垄断的局面，让专业级金融分析工具真正实现民主化。

**技术亮点**:
- 支持多资产类别数据整合：涵盖股票、加密货币、衍生品、期权、固定收益、宏观经济等多维度金融数据
- 深度集成AI与机器学习能力：专为AI代理和量化模型设计，支持智能化数据分析和预测
- Python原生开发：提供完整的Python SDK和API，便于与现有量化工作流无缝集成
- 开放式架构设计：支持自定义数据源扩展和插件化开发，高度可定制化
- 专为量化金融优化：提供专业级的金融数据处理和分析工具链

**适用场景**:
- 量化分析师构建多资产类别投资策略和回测系统
- 个人开发者打造个性化投资组合监控和分析工具
- AI/ML工程师训练金融预测模型，获取高质量训练数据
- 金融科技公司快速搭建金融数据平台，降低数据获取成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,338 |
| 语言 | HTML |
| Forks | 20,179 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,304 |
| 语言 | Jupyter Notebook |
| Forks | 5,331 |
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
| Stars | 158,102 |
| 语言 | Python |
| Forks | 32,550 |
| Issues | 2,279 |
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
| Stars | 73,699 |
| 语言 | Python |
| Forks | 14,554 |
| Issues | 3,798 |
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
| Stars | 106,358 |
| 语言 | Python |
| Forks | 12,244 |
| Issues | 3,854 |
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
| Stars | 98,403 |
| 语言 | Python |
| Forks | 27,256 |
| Issues | 18,048 |
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
| Stars | 88,748 |
| 语言 | Jupyter Notebook |
| Forks | 13,553 |
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
| Stars | 33,142 |
| 语言 | TypeScript |
| Forks | 3,569 |
| Issues | 282 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,871 |
| 语言 | Python |
| Forks | 30,189 |
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
| Stars | 87,655 |
| 语言 | JavaScript |
| Forks | 11,486 |
| Issues | 71 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的AI智能体优化系统，整合了技能、本能、记忆、安全和研究驱动开发等核心能力，为Claude Code、Cursor等主流AI编程工具提供统一的能力增强框架，极大提升AI辅助开发的效率和质量。87K+的Star数证明了其在AI开发者社区中的重要地位和实用价值。

**技术亮点**:
- 智能体能力增强框架：整合技能系统、本能反应、持久记忆等多维度能力，实现AI智能体的全面优化
- 跨平台兼容架构：支持Claude Code、Codex、Opencode、Cursor等多种AI编程工具的统一接口
- 安全与性能并重：内置安全机制的同时专注于性能优化，确保AI代理的可靠性和高效性
- MCP协议集成：支持Model Context Protocol，实现与AI模型的标准化交互
- 研究驱动开发模式：采用Research-First方法论，基于实际研究和测试数据优化系统性能

**适用场景**:
- 企业AI开发团队：为使用Claude Code、Cursor等AI编程助手的开发团队提供性能优化和能力扩展方案
- 个人开发者：希望提升AI编程工具效率，获得更智能代码生成和开发辅助的独立开发者
- AI智能体应用开发：构建复杂AI应用系统，需要记忆、安全、技能管理等高级功能的开发者



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,037 |
| 语言 | Go |
| Forks | 3,757 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费开源的本地化 AI 解决方案，作为 OpenAI 等商业服务的直接替代品，它无需 GPU 就能在消费级硬件上运行，支持文本、图像、音频、视频等多模态生成，特别适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers）和架构（LLaMA、Mamba等），兼容性极强
- 无需GPU即可在消费级硬件上运行，大幅降低部署门槛和硬件成本
- 完整的OpenAI API兼容性，实现drop-in replacement无缝迁移
- 支持分布式和P2P去中心化推理（基于libp2p），具备横向扩展能力
- 多模态能力全覆盖：文本生成、图像生成、音频生成、视频、语音克隆、TTS等

**适用场景**:
- 企业内部私有化部署AI服务，确保敏感数据不出本地，满足合规和隐私要求
- 个人开发者或创业团队在预算有限情况下，构建AI应用而无需承担高昂的API调用费用
- 边缘设备和离线场景下的AI应用部署，如IoT设备、移动应用或网络受限环境



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,418 |
| 语言 | Python |
| Forks | 8,702 |
| Issues | 326 |
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
| Stars | 41,555 |
| 语言 | TypeScript |
| Forks | 3,105 |
| Issues | 425 |
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
| Stars | 180,022 |
| 语言 | TypeScript |
| Forks | 55,970 |
| Issues | 1,422 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 412,305 |
| 语言 | Python |
| Forks | 44,600 |
| Issues | 1,025 |
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
| Stars | 152,097 |
| 语言 | Python |
| Forks | 12,345 |
| Issues | 2,378 |
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
| Stars | 96,354 |
| 语言 | Python |
| Forks | 8,891 |
| Issues | 164 |
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
| Stars | 73,863 |
| 语言 | Python |
| Forks | 8,772 |
| Issues | 199 |
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
| Stars | 182,840 |
| 语言 | TypeScript |
| Forks | 38,622 |
| Issues | 15,478 |
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
| Stars | 93,875 |
| 语言 | TypeScript |
| Forks | 9,399 |
| Issues | 293 |
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
| Stars | 78,536 |
| 语言 | TypeScript |
| Forks | 5,715 |
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
| Stars | 76,729 |
| 语言 | TypeScript |
| Forks | 6,565 |
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
| Stars | 75,673 |
| 语言 | JavaScript |
| Forks | 7,279 |
| Issues | 710 |
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
| Stars | 78,747 |
| 语言 | Go |
| Forks | 2,740 |
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
| Stars | 74,652 |
| 语言 | Go |
| Forks | 2,626 |
| Issues | 941 |
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
| Stars | 36,781 |
| 语言 | Python |
| Forks | 2,572 |
| Issues | 64 |
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
| Stars | 54,549 |
| 语言 | JavaScript |
| Forks | 4,038 |
| Issues | 1,406 |
| Topics | dark-mode, editor, electron, element-ui, emoji, focus-mode, latex, linux, mac, macos, markdown, marktext, next-generation, source-code, typewriter-mode, vue, windows |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (14 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,555 |
| 语言 | TypeScript |
| Forks | 3,105 |
| Issues | 425 |
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
| Stars | 180,022 |
| 语言 | TypeScript |
| Forks | 55,970 |
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
| Stars | 51,661 |
| 语言 | Go |
| Forks | 10,339 |
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
| Stars | 121,226 |
| 语言 | Go |
| Forks | 42,705 |
| Issues | 2,611 |
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
| Stars | 71,547 |
| 语言 | Go |
| Forks | 18,919 |
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
| Stars | 54,378 |
| 语言 | Go |
| Forks | 6,488 |
| Issues | 2,857 |
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
| Stars | 47,583 |
| 语言 | Go |
| Forks | 5,071 |
| Issues | 964 |
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
| Stars | 93,875 |
| 语言 | TypeScript |
| Forks | 9,399 |
| Issues | 293 |
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
| Stars | 75,561 |
| 语言 | TypeScript |
| Forks | 6,434 |
| Issues | 436 |
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
| Stars | 84,257 |
| 语言 | JavaScript |
| Forks | 7,545 |
| Issues | 702 |
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
| Stars | 62,255 |
| 语言 | Go |
| Forks | 5,884 |
| Issues | 772 |
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
| Stars | 58,047 |
| 语言 | Go |
| Forks | 4,209 |
| Issues | 26 |
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
| Stars | 46,075 |
| 语言 | Python |
| Forks | 4,683 |
| Issues | 335 |
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
| Stars | 69,435 |
| 语言 | Go |
| Forks | 1,884 |
| Issues | 299 |
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
| Stars | 84,257 |
| 语言 | JavaScript |
| Forks | 7,545 |
| Issues | 702 |
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
| Stars | 63,218 |
| 语言 | Go |
| Forks | 10,251 |
| Issues | 754 |
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
| Stars | 44,037 |
| 语言 | Go |
| Forks | 3,757 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个完全免费开源的本地化 AI 解决方案，作为 OpenAI 等商业服务的直接替代品，它无需 GPU 就能在消费级硬件上运行，支持文本、图像、音频、视频等多模态生成，特别适合注重数据隐私和成本控制的场景。

**技术亮点**:
- 支持多种模型格式（GGUF、Transformers、Diffusers）和架构（LLaMA、Mamba等），兼容性极强
- 无需GPU即可在消费级硬件上运行，大幅降低部署门槛和硬件成本
- 完整的OpenAI API兼容性，实现drop-in replacement无缝迁移
- 支持分布式和P2P去中心化推理（基于libp2p），具备横向扩展能力
- 多模态能力全覆盖：文本生成、图像生成、音频生成、视频、语音克隆、TTS等

**适用场景**:
- 企业内部私有化部署AI服务，确保敏感数据不出本地，满足合规和隐私要求
- 个人开发者或创业团队在预算有限情况下，构建AI应用而无需承担高昂的API调用费用
- 边缘设备和离线场景下的AI应用部署，如IoT设备、移动应用或网络受限环境



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 412,305 |
| 语言 | Python |
| Forks | 44,600 |
| Issues | 1,025 |
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
| Stars | 96,354 |
| 语言 | Python |
| Forks | 8,891 |
| Issues | 164 |
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
| Forks | 33,779 |
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
| Stars | 100,119 |
| 语言 | TypeScript |
| Forks | 27,141 |
| Issues | 1,126 |
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
| Stars | 78,536 |
| 语言 | TypeScript |
| Forks | 5,715 |
| Issues | 720 |
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
| Stars | 74,965 |
| 语言 | TypeScript |
| Forks | 8,262 |
| Issues | 38 |
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
| Stars | 75,673 |
| 语言 | JavaScript |
| Forks | 7,279 |
| Issues | 710 |
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
| Stars | 55,950 |
| 语言 | JavaScript |
| Forks | 10,223 |
| Issues | 353 |
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
| Stars | 88,270 |
| 语言 | Go |
| Forks | 8,575 |
| Issues | 646 |
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
| Stars | 70,929 |
| 语言 | Go |
| Forks | 4,683 |
| Issues | 248 |
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
| Stars | 56,822 |
| 语言 | Go |
| Forks | 3,182 |
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
| Stars | 36,781 |
| 语言 | Python |
| Forks | 2,572 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
| 许可证 | MIT License |


### ⭐ 中优先级


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 68,889 |
| 语言 | JavaScript |
| Forks | 22,859 |
| Issues | 193 |
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
| Stars | 99,265 |
| 语言 | TypeScript |
| Forks | 11,839 |
| Issues | 954 |
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
| Stars | 56,466 |
| 语言 | JavaScript |
| Forks | 6,100 |
| Issues | 304 |
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
| Stars | 43,385 |
| 语言 | Go |
| Forks | 3,903 |
| Issues | 1,092 |
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
| Stars | 51,661 |
| 语言 | Go |
| Forks | 10,339 |
| Issues | 227 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (9 个项目) { #学习资源 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,954 |
| 语言 | MDX |
| Forks | 7,683 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71k+ stars的提示工程领域顶级开源资源库，系统性地整合了从基础Prompt Engineering到高级AI Agent开发的完整知识体系，涵盖理论指南、学术论文、实践教程和可运行代码，是AI开发者和大模型应用工程师必学的核心参考资料。

**技术亮点**:
- 📖 全面覆盖提示工程核心技术栈：Prompt Engineering、Context Engineering、RAG检索增强生成、AI Agent开发
- 🎯 融合理论与实践：包含学术论文、教程指南、Jupyter Notebook可执行示例，实现从理论到落地的完整闭环
- 🤖 紧跟AI前沿技术：涵盖ChatGPT、OpenAI API、大语言模型(LLMs)、生成式AI等最新技术应用
- 📑 采用MDX格式：支持在Markdown中嵌入交互式组件，提供更丰富的学习体验
- 🔬 开源社区驱动：MIT许可证，持续更新，汇集全球AI社区的最佳实践经验

**适用场景**:
- 🏢 企业AI应用开发：帮助团队快速掌握大模型应用开发技能，构建智能客服、知识库问答、自动化工作流等企业级AI解决方案
- 👨‍💻 个人开发者学习：作为系统学习Prompt Engineering和大模型应用开发的完整教程，从入门到进阶的技能提升路径
- 🎓 AI研究与教育：为研究人员和教育者提供丰富的学术论文资源和教学材料，支持课程设计和前沿技术探索



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,338 |
| 语言 | HTML |
| Forks | 20,179 |
| Issues | 35 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,494 |
| 语言 | TypeScript |
| Forks | 5,464 |
| Issues | 55 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,669 |
| 语言 | HTML |
| Forks | 5,574 |
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
| Stars | 89,491 |
| 语言 | TypeScript |
| Forks | 9,940 |
| Issues | 2,200 |
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
| Stars | 86,772 |
| 语言 | TypeScript |
| Forks | 8,751 |
| Issues | 1,607 |
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
| Stars | 127,145 |
| 语言 | JavaScript |
| Forks | 12,460 |
| Issues | 5 |
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
| Stars | 100,488 |
| 语言 | JavaScript |
| Forks | 7,503 |
| Issues | 223 |
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
| Stars | 167,738 |
| 语言 | Go |
| Forks | 13,069 |
| Issues | 172 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,287 |
| 语言 | Shell |
| Forks | 8,277 |
| Issues | 75 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,248 |
| 语言 | Python |
| Forks | 6,353 |
| Issues | 32 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,190 |
| 语言 | Python |
| Forks | 11,704 |
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
| Stars | 78,574 |
| 语言 | Python |
| Forks | 6,667 |
| Issues | 617 |
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
| Stars | 132,173 |
| 语言 | Unknown |
| Forks | 33,479 |
| Issues | 133 |
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
| Stars | 384,208 |
| 语言 | Python |
| Forks | 66,028 |
| Issues | 72 |
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
| Stars | 113,055 |
| 语言 | TypeScript |
| Forks | 5,738 |
| Issues | 321 |
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
| Stars | 103,931 |
| 语言 | TypeScript |
| Forks | 7,564 |
| Issues | 190 |
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
| Stars | 47,959 |
| 语言 | Go |
| Forks | 10,253 |
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
| Stars | 98,602 |
| 语言 | C++ |
| Forks | 15,629 |
| Issues | 1,275 |
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
| Stars | 61,080 |
| 语言 | Python |
| Forks | 1,610 |
| Issues | 37 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,855 |
| 语言 | JavaScript |
| Forks | 2,939 |
| Issues | 13 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 339,433 |
| 语言 | Python |
| Forks | 54,948 |
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
| Stars | 287,971 |
| 语言 | Python |
| Forks | 27,434 |
| Issues | 18 |
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
| Stars | 218,843 |
| 语言 | Python |
| Forks | 50,233 |
| Issues | 888 |
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
| Stars | 85,455 |
| 语言 | Python |
| Forks | 37,009 |
| Issues | 3,556 |
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
| Stars | 85,380 |
| 语言 | Python |
| Forks | 7,171 |
| Issues | 476 |
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
| Stars | 77,691 |
| 语言 | Python |
| Forks | 45,227 |
| Issues | 1,281 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,195 |
| 语言 | Python |
| Forks | 16,769 |
| Issues | 19 |
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
| Stars | 438,474 |
| 语言 | TypeScript |
| Forks | 43,705 |
| Issues | 228 |
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
| Stars | 351,170 |
| 语言 | TypeScript |
| Forks | 43,810 |
| Issues | 26 |
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
| Stars | 119,111 |
| 语言 | TypeScript |
| Forks | 12,928 |
| Issues | 2,848 |
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
| Stars | 110,114 |
| 语言 | TypeScript |
| Forks | 8,264 |
| Issues | 1,805 |
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
| Stars | 108,211 |
| 语言 | TypeScript |
| Forks | 13,313 |
| Issues | 5,494 |
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
| Stars | 97,742 |
| 语言 | TypeScript |
| Forks | 54,580 |
| Issues | 1,368 |
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
| Stars | 95,160 |
| 语言 | TypeScript |
| Forks | 5,153 |
| Issues | 653 |
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
| Stars | 94,115 |
| 语言 | TypeScript |
| Forks | 5,124 |
| Issues | 98 |
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
| Stars | 83,014 |
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
| Stars | 81,540 |
| 语言 | TypeScript |
| Forks | 9,975 |
| Issues | 534 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,190 |
| 语言 | TypeScript |
| Forks | 7,942 |
| Issues | 673 |
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
| Stars | 244,073 |
| 语言 | JavaScript |
| Forks | 50,841 |
| Issues | 1,188 |
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
| Stars | 116,329 |
| 语言 | JavaScript |
| Forks | 35,110 |
| Issues | 2,535 |
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
| Stars | 111,468 |
| 语言 | JavaScript |
| Forks | 36,307 |
| Issues | 587 |
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
| Forks | 11,562 |
| Issues | 335 |
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
| Stars | 98,025 |
| 语言 | JavaScript |
| Forks | 32,704 |
| Issues | 1,718 |
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
| Stars | 95,440 |
| 语言 | JavaScript |
| Forks | 15,267 |
| Issues | 46 |
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
| Stars | 86,092 |
| 语言 | JavaScript |
| Forks | 4,814 |
| Issues | 970 |
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
| Stars | 70,798 |
| 语言 | JavaScript |
| Forks | 16,806 |
| Issues | 889 |
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
| Stars | 66,008 |
| 语言 | JavaScript |
| Forks | 9,331 |
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
| Stars | 62,183 |
| 语言 | JavaScript |
| Forks | 3,982 |
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
| Stars | 59,920 |
| 语言 | JavaScript |
| Forks | 5,616 |
| Issues | 66 |
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
| Stars | 59,872 |
| 语言 | JavaScript |
| Forks | 20,472 |
| Issues | 97 |
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
| Stars | 57,400 |
| 语言 | JavaScript |
| Forks | 12,302 |
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
| Stars | 52,999 |
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
| Forks | 18,869 |
| Issues | 9,878 |
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
| Stars | 105,408 |
| 语言 | Go |
| Forks | 14,957 |
| Issues | 49 |
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
| Stars | 87,156 |
| 语言 | Go |
| Forks | 8,217 |
| Issues | 260 |
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
| Stars | 80,952 |
| 语言 | Go |
| Forks | 4,969 |
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
| Stars | 68,676 |
| 语言 | Go |
| Forks | 3,221 |
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
| Stars | 56,123 |
| 语言 | Go |
| Forks | 4,984 |
| Issues | 1,147 |
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
| Stars | 50,932 |
| 语言 | Go |
| Forks | 21,865 |
| Issues | 371 |
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
| Stars | 50,226 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 259 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,184 |
| 语言 | Go |
| Forks | 7,975 |
| Issues | 566 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,911 |
| 语言 | Python |
| Forks | 10,604 |
| Issues | 4,120 |
| 许可证 | The Unlicense |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,764 |
| 语言 | JavaScript |
| Forks | 31,114 |
| Issues | 397 |
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
| Stars | 148,129 |
| 语言 | JavaScript |
| Forks | 26,775 |
| Issues | 189 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 78,804 |
| 语言 | JavaScript |
| Forks | 31,569 |
| Issues | 266 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,285 |
| 语言 | JavaScript |
| Forks | 11,980 |
| Issues | 536 |
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
| Stars | 66,298 |
| 语言 | JavaScript |
| Forks | 9,197 |
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
| Stars | 61,579 |
| 语言 | JavaScript |
| Forks | 7,125 |
| Issues | 131 |
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
| Stars | 46,966 |
| 语言 | Go |
| Forks | 8,877 |
| Issues | 8 |
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
| Stars | 45,540 |
| 语言 | Go |
| Forks | 3,775 |
| Issues | 95 |
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
| Stars | 146,733 |
| 语言 | Python |
| Forks | 11,253 |
| Issues | 302 |
| Topics | awesome, github, hellogithub, python |
