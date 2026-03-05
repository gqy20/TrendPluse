# 项目发现报告 (2026-03-05)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
| 去重移除 | 33 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 13 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 62 |

## 📑 快速导航

### 按技术分类
- [🤖 AI Agents](#ai agents)
- [🔍 RAG/检索](#rag-检索)
- [💬 LLM 界面](#llm 界面)
- [🧠 机器学习框架](#机器学习框架)
- [🛠️ 开发工具](#开发工具)
- [⚙️ DevOps/基础设施](#devops-基础设施)
- [📈 监控/观测](#监控-观测)
- [🌐 Web 框架](#web 框架)
- [📊 数据/基础设施](#数据-基础设施)
- [📚 学习资源](#学习资源)
- [📁 其他](#其他)


## 🤖 AI Agents (27 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,861 |
| 语言 | Python |
| Forks | 17,808 |
| Issues | 306 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 AI 对话界面之一，拥有 12.5 万+ stars，提供类似 ChatGPT 的现代化用户体验。它的独特价值在于完全自托管、支持多种 AI 后端（Ollama、OpenAI API 等），并且功能丰富度极高，包括 RAG、MCP 协议支持等，是个人和企业快速搭建私有 AI 服务的最佳选择。

**技术亮点**:
- 多后端兼容性：同时支持 Ollama、OpenAI API 等多种 LLM 后端，灵活切换不同 AI 模型
- RAG（检索增强生成）集成：内置文档上传和知识库功能，支持基于私有数据的智能问答
- MCP 协议支持：集成 Model Context Protocol，实现更强大的工具调用和上下文管理能力
- 完全自托管部署：所有数据本地存储，保障隐私安全，适合企业和个人私有化部署
- 现代化 Web UI：提供类似 ChatGPT 的用户界面，支持多用户、模型管理、API key 管理等企业级功能

**适用场景**:
- 企业内部 AI 助手部署：为企业搭建私有的 AI 对话平台，接入内部知识库，保护数据隐私
- 个人开发者本地 LLM 实验环境：配合 Ollama 在本地运行开源大模型，进行 AI 应用开发和测试
- 多模型统一管理平台：整合多个 AI 服务商的 API，提供统一的对话界面和管理后台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,240 |
| 语言 | Python |
| Forks | 8,258 |
| Issues | 3,042 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的检索增强生成（RAG）开源引擎，完美融合了尖端 RAG 技术与 Agent 智能体能力，为大语言模型构建卓越的上下文理解层。该项目拥有超过 74k 的 GitHub Stars，采用 Apache 2.0 许可证，是企业级 AI 应用和智能搜索系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供深度上下文理解和智能工作流
- 强大的文档解析与理解引擎，支持多种格式文档的智能处理
- 集成 GraphRAG 和深度研究能力，提供知识图谱增强的检索体验
- 支持多种 LLM 后端（OpenAI、DeepSeek、Ollama 等），灵活性强
- 内置 MCP (Model Context Protocol) 和 AI 搜索功能，提供企业级上下文工程能力

**适用场景**:
- 企业知识库与智能问答系统：构建企业内部文档检索、智能客服和知识管理平台
- AI 智能搜索与深度研究：开发专业领域的深度搜索引擎和智能研究助手
- Agent 工作流自动化：创建具备文档理解和复杂推理能力的 AI 智能体应用



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,541 |
| 语言 | TypeScript |
| Forks | 6,227 |
| Issues | 198 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前 GitHub 上最受欢迎的 AI 数据获取工具之一，拥有超过 8.8 万颗星。它解决了大语言模型（LLM）应用中最关键的"最后一公里"问题——将非结构化的网页数据高效转化为 AI 可直接消费的 Markdown 或结构化数据，极大地降低了 AI 应用开发的数据处理门槛。

**技术亮点**:
- 🔥 一键爬取整个网站，自动处理分页和爬取深度，无需手动编写爬虫逻辑
- 智能 HTML 转 Markdown 引擎，专门针对 LLM 优化，输出干净、结构化的文本
- 🤖 内置 LLM 友好的数据提取 API，支持自定义 schema 结构化数据提取
- 🚀 提供完整的 API 和 SDK（TypeScript/Python），轻松集成到 AI Agent 和自动化工作流
- 🛡️ 内置反爬虫处理机制，支持代理池、速率限制和错误重试，保证数据采集稳定性

**适用场景**:
- 🤖 AI Agent 知识库构建：快速爬取目标网站内容，为 RAG 应用、智能客服、知识问答系统构建实时更新的数据源
- 📊 企业数据采集与分析：自动化采集竞品信息、市场数据、新闻资讯，转化为结构化数据用于商业分析和决策
- 🔍 AI 搜索增强：为 AI 搜索引擎提供实时网页数据索引，支持垂直领域的深度搜索和内容聚合



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,515 |
| 语言 | JavaScript |
| Forks | 7,614 |
| Issues | 32 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向Claude Code生态的智能体性能优化系统，集成了技能、记忆、安全性和研究优先开发能力，帮助开发者大幅提升AI编程助手的工作效率和代码质量。该项目获得了超6万星标，是当前最热门的Claude工具链优化方案之一。

**技术亮点**:
- 集成MCP（Model Context Protocol）实现可扩展的插件架构，支持与Claude Code、Codex、Cowork等多种工具无缝协作
- 提供内存管理（Memory）和技能系统（Skills），让AI助手能够学习开发习惯并积累专业知识
- 内置安全防护机制（Security），确保AI生成的代码符合安全最佳实践
- 研究优先（Research-first）的开发模式，持续优化AI代理的性能和准确性
- 基于JavaScript/TypeScript技术栈，易于集成到现有的开发工作流中

**适用场景**:
- 个人开发者：通过Claude Code提升编程效率，自动化代码生成、重构和调试工作
- 企业开发团队：统一团队AI辅助编程标准，利用MCP集成内部工具和知识库，提升协作效率
- AI工具开发者：基于该项目扩展Claude生态，构建定制化的AI编码助手和企业级解决方案



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,650 |
| 语言 | JavaScript |
| Forks | 6,019 |
| Issues | 310 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，它将 RAG、AI 智能体、No-code 构建器和 MCP 兼容性集成在一个开箱即用的桌面和 Docker 应用中。作为 55k+ stars 的开源项目，它不仅支持本地 LLM（如 Ollama、LM Studio）和云端模型，还提供了完整的多模态 AI 解决方案，降低了企业构建私有化 AI 助手的门槛。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量数据库和网页抓取，实现知识库增强的智能对话
- MCP（Model Context Protocol）兼容性，可无缝连接各种 MCP 服务器扩展功能
- No-code 智能体构建器，让非开发者也能快速创建和定制 AI Agent
- 多模型支持：集成 DeepSeek、Kimi、Llama3、Qwen3、Moonshot 等主流开源和商业模型
- 灵活部署方式：支持桌面应用和 Docker 容器化部署，适配本地 LLM（Ollama、LocalAI）和云端 API

**适用场景**:
- 企业私有化 AI 知识助手：结合 RAG 技术构建基于企业内部文档的智能问答系统，无需数据外泄
- 开发者快速构建 AI Agent：利用 No-code 构建器和 MCP 生态快速开发定制化 AI 智能体应用
- 个人本地 AI 工作台：在本地运行 LLM（通过 Ollama 等）搭建隐私安全的个人 AI 助手，支持多模态交互



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,280 |
| 语言 | Go |
| Forks | 3,634 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源 AI 基础设施项目，它提供了与 OpenAI、Claude 等商业服务完全兼容的 API 接口，但完全本地化运行，无需 GPU 和云服务。这解决了数据隐私、成本控制和离线部署三大痛点，让个人开发者和小企业也能在普通硬件上运行最前沿的 AI 模型，是实现 AI 自主化和去中心化推理的理想选择。

**技术亮点**:
- 🤖 多模态支持：集成 gguf、transformers、diffusers 等多种模型后端，支持文本、音频、图像、视频生成，以及语音克隆、目标检测等丰富功能
- 🔄 完全兼容 OpenAI API：Drop-in replacement 设计，无需修改代码即可无缝切换，支持 MCP 协议和 Rerank 功能
- 💻 零 GPU 部署：优化推理性能，可在消费级硬件（CPU）上运行，大幅降低部署门槛和硬件成本
- 🌐 去中心化架构：基于 libp2p 实现 P2P 分布式推理，支持联邦学习和跨节点协同计算
- 🎯 模型生态丰富：内置支持 LLaMA、Mistral、Gemma、RWKV、Mamba、Stable Diffusion、MusicGen 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求严格的行业，可本地部署 LLM 和多模态 AI 服务，确保敏感数据不出内网
- 👨‍💻 个人开发者 AI 应用：在普通电脑上搭建完整的 AI 开发环境，测试和部署聊天机器人、图像生成、语音合成等应用，无需承担 API 调用成本
- 🌍 离线/边缘计算场景：在无网络或弱网环境（如野外作业、船舶、军事设施）中提供 AI 能力，结合 P2P 分布式实现节点间资源共享



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,121 |
| 语言 | TypeScript |
| Forks | 14,727 |
| Issues | 704 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个革命性的多智能体协作平台，通过创新的 Agent 作为工作交互单元的理念，让用户能够轻松设计、构建和协作多个 AI 智能体团队。该项目已获得 7.3 万+ Stars，凭借其对 OpenAI、Claude、DeepSeek、Gemini 等主流 LLM 的全面支持以及 MCP 协议集成，成为当前最成熟的企业级智能体协作解决方案之一。

**技术亮点**:
- 基于 TypeScript 构建的企业级架构，提供高性能的类型安全开发体验
- 原生支持多智能体协作模式（Multi-Agent Collaboration），实现智能体间的无缝配合
- 集成 MCP（Model Context Protocol）协议，提供标准化的模型上下文交互能力
- 支持 GPT、Claude、Gemini、DeepSeek 等多种大语言模型，提供灵活的模型切换能力
- 内置知识库系统（Knowledge Base），支持智能体的知识积累与持续学习成长

**适用场景**:
- 企业团队协作：构建企业级 AI 智能体团队，实现自动化工作流程和跨部门协作，提升团队工作效率
- 个人开发者工具：个人开发者可快速搭建专属 AI 助手团队，用于代码生成、调试、文档编写等开发任务
- 知识管理与问答：建立基于企业内部知识库的智能问答系统，支持员工快速获取信息和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,145 |
| 语言 | MDX |
| Forks | 7,581 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示词工程指南项目（71k+ stars），由AI研究社区DAIR AI维护，涵盖了从基础的Prompt Engineering到前沿的AI Agents、RAG等完整技术栈，是AI开发者必备的系统性学习资源和实践指南。

**技术亮点**:
- 全方位覆盖提示词工程生态系统，包括基础Prompt Engineering、上下文工程、RAG检索增强生成和AI智能体等核心技术
- 提供多元化学习资源形式：实践指南、学术论文、交互式笔记本、课程教程，满足不同学习偏好的开发者需求
- 紧跟AI前沿技术趋势，涵盖ChatGPT、LLMs、生成式AI、深度学习等热门技术栈，内容持续更新迭代
- 开源友好（MIT许可），社区活跃，汇集了业界最佳实践和研究成果，适合系统学习和快速查阅

**适用场景**:
- AI应用开发者学习提示词设计模式和最佳实践，提升与大语言模型交互的效果和效率
- 企业技术团队构建RAG系统或AI Agents时，参考权威指南和论文，加速产品研发落地
- AI研究者快速了解提示词工程领域的前沿进展和技术方案，为学术研究提供理论基础



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,930 |
| 语言 | Python |
| Forks | 8,284 |
| Issues | 917 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个统一高效的100+大模型微调框架（ACL 2024论文成果），支持LoRA、QLoRA、全量微调等多种方式，覆盖LLaMA、Qwen、DeepSeek、Gemma等主流模型。该项目在GitHub获得超过6.7万星标，是企业级AI应用部署和个人开发者快速定制大模型的最佳开源工具。

**技术亮点**:
- 统一支持100+个大语言模型与视觉语言模型，包括LLaMA 3、Qwen、DeepSeek、Gemma、Mistral等主流开源模型
- 提供完整微调技术栈：LoRA、QLoRA、全量微调、MoE（混合专家模型）及量化技术，大幅降低显存需求
- 集成RLHF（人类反馈强化学习）与Agent指令调优功能，可直接训练对话助手和智能体
- 内置Web UI可视化界面与命令行工具，零代码/低代码即可完成模型微调流程
- 基于Transformers生态，兼容Hugging Face模型库，支持多模态(VLM)训练与推理

**适用场景**:
- 企业快速定制垂直领域大模型：企业可在有限GPU资源下，通过QLoRA等技术快速微调专属模型（如金融、医疗、法律等领域的专用模型）
- 个人开发者训练专属AI助手：基于LLaMA、Qwen等开源模型进行指令微调，打造个人AI伴侣或特定任务助手
- 学术研究与算法验证：研究人员可快速复现ACL 2024论文成果，对比不同微调方法（如LoRA vs QLoRA vs 全量微调）的效果
- 构建智能Agent系统：结合Agent训练功能，开发具备工具调用、规划推理能力的AI智能体应用



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,338 |
| 语言 | Java |
| Forks | 15,831 |
| Issues | 50 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,910 |
| 语言 | Python |
| Forks | 9,792 |
| Issues | 351 |
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
| Stars | 34,368 |
| 语言 | TypeScript |
| Forks | 6,936 |
| Issues | 428 |
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
| Stars | 33,134 |
| 语言 | Python |
| Forks | 2,036 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,033 |
| 语言 | TypeScript |
| Forks | 2,250 |
| Issues | 78 |
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
| Stars | 38,634 |
| 语言 | Python |
| Forks | 6,118 |
| Issues | 195 |
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
| Stars | 31,176 |
| 语言 | Jupyter Notebook |
| Forks | 5,074 |
| Issues | 124 |
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
| Stars | 99,814 |
| 语言 | Python |
| Forks | 14,509 |
| Issues | 8 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,612 |
| 语言 | Python |
| Forks | 8,565 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,212 |
| 语言 | TypeScript |
| Forks | 2,797 |
| Issues | 330 |
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
| Stars | 79,678 |
| 语言 | Python |
| Forks | 9,421 |
| Issues | 231 |
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
| Stars | 50,393 |
| 语言 | TypeScript |
| Forks | 23,876 |
| Issues | 792 |
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
| Stars | 177,730 |
| 语言 | TypeScript |
| Forks | 55,462 |
| Issues | 1,423 |
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
| Stars | 145,277 |
| 语言 | Python |
| Forks | 8,515 |
| Issues | 898 |
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
| Stars | 53,083 |
| 语言 | Jupyter Notebook |
| Forks | 18,441 |
| Issues | 2 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,244 |
| 语言 | TypeScript |
| Forks | 3,312 |
| Issues | 245 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 30,319 |
| 语言 | Python |
| Forks | 3,318 |
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
| Stars | 41,060 |
| 语言 | Python |
| Forks | 4,077 |
| Issues | 251 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


## 🔍 RAG/检索 (17 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,861 |
| 语言 | Python |
| Forks | 17,808 |
| Issues | 306 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 AI 对话界面之一，拥有 12.5 万+ stars，提供类似 ChatGPT 的现代化用户体验。它的独特价值在于完全自托管、支持多种 AI 后端（Ollama、OpenAI API 等），并且功能丰富度极高，包括 RAG、MCP 协议支持等，是个人和企业快速搭建私有 AI 服务的最佳选择。

**技术亮点**:
- 多后端兼容性：同时支持 Ollama、OpenAI API 等多种 LLM 后端，灵活切换不同 AI 模型
- RAG（检索增强生成）集成：内置文档上传和知识库功能，支持基于私有数据的智能问答
- MCP 协议支持：集成 Model Context Protocol，实现更强大的工具调用和上下文管理能力
- 完全自托管部署：所有数据本地存储，保障隐私安全，适合企业和个人私有化部署
- 现代化 Web UI：提供类似 ChatGPT 的用户界面，支持多用户、模型管理、API key 管理等企业级功能

**适用场景**:
- 企业内部 AI 助手部署：为企业搭建私有的 AI 对话平台，接入内部知识库，保护数据隐私
- 个人开发者本地 LLM 实验环境：配合 Ollama 在本地运行开源大模型，进行 AI 应用开发和测试
- 多模型统一管理平台：整合多个 AI 服务商的 API，提供统一的对话界面和管理后台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,240 |
| 语言 | Python |
| Forks | 8,258 |
| Issues | 3,042 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的检索增强生成（RAG）开源引擎，完美融合了尖端 RAG 技术与 Agent 智能体能力，为大语言模型构建卓越的上下文理解层。该项目拥有超过 74k 的 GitHub Stars，采用 Apache 2.0 许可证，是企业级 AI 应用和智能搜索系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供深度上下文理解和智能工作流
- 强大的文档解析与理解引擎，支持多种格式文档的智能处理
- 集成 GraphRAG 和深度研究能力，提供知识图谱增强的检索体验
- 支持多种 LLM 后端（OpenAI、DeepSeek、Ollama 等），灵活性强
- 内置 MCP (Model Context Protocol) 和 AI 搜索功能，提供企业级上下文工程能力

**适用场景**:
- 企业知识库与智能问答系统：构建企业内部文档检索、智能客服和知识管理平台
- AI 智能搜索与深度研究：开发专业领域的深度搜索引擎和智能研究助手
- Agent 工作流自动化：创建具备文档理解和复杂推理能力的 AI 智能体应用



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,650 |
| 语言 | JavaScript |
| Forks | 6,019 |
| Issues | 310 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，它将 RAG、AI 智能体、No-code 构建器和 MCP 兼容性集成在一个开箱即用的桌面和 Docker 应用中。作为 55k+ stars 的开源项目，它不仅支持本地 LLM（如 Ollama、LM Studio）和云端模型，还提供了完整的多模态 AI 解决方案，降低了企业构建私有化 AI 助手的门槛。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量数据库和网页抓取，实现知识库增强的智能对话
- MCP（Model Context Protocol）兼容性，可无缝连接各种 MCP 服务器扩展功能
- No-code 智能体构建器，让非开发者也能快速创建和定制 AI Agent
- 多模型支持：集成 DeepSeek、Kimi、Llama3、Qwen3、Moonshot 等主流开源和商业模型
- 灵活部署方式：支持桌面应用和 Docker 容器化部署，适配本地 LLM（Ollama、LocalAI）和云端 API

**适用场景**:
- 企业私有化 AI 知识助手：结合 RAG 技术构建基于企业内部文档的智能问答系统，无需数据外泄
- 开发者快速构建 AI Agent：利用 No-code 构建器和 MCP 生态快速开发定制化 AI 智能体应用
- 个人本地 AI 工作台：在本地运行 LLM（通过 Ollama 等）搭建隐私安全的个人 AI 助手，支持多模态交互



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,121 |
| 语言 | TypeScript |
| Forks | 14,727 |
| Issues | 704 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个革命性的多智能体协作平台，通过创新的 Agent 作为工作交互单元的理念，让用户能够轻松设计、构建和协作多个 AI 智能体团队。该项目已获得 7.3 万+ Stars，凭借其对 OpenAI、Claude、DeepSeek、Gemini 等主流 LLM 的全面支持以及 MCP 协议集成，成为当前最成熟的企业级智能体协作解决方案之一。

**技术亮点**:
- 基于 TypeScript 构建的企业级架构，提供高性能的类型安全开发体验
- 原生支持多智能体协作模式（Multi-Agent Collaboration），实现智能体间的无缝配合
- 集成 MCP（Model Context Protocol）协议，提供标准化的模型上下文交互能力
- 支持 GPT、Claude、Gemini、DeepSeek 等多种大语言模型，提供灵活的模型切换能力
- 内置知识库系统（Knowledge Base），支持智能体的知识积累与持续学习成长

**适用场景**:
- 企业团队协作：构建企业级 AI 智能体团队，实现自动化工作流程和跨部门协作，提升团队工作效率
- 个人开发者工具：个人开发者可快速搭建专属 AI 助手团队，用于代码生成、调试、文档编写等开发任务
- 知识管理与问答：建立基于企业内部知识库的智能问答系统，支持员工快速获取信息和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,145 |
| 语言 | MDX |
| Forks | 7,581 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示词工程指南项目（71k+ stars），由AI研究社区DAIR AI维护，涵盖了从基础的Prompt Engineering到前沿的AI Agents、RAG等完整技术栈，是AI开发者必备的系统性学习资源和实践指南。

**技术亮点**:
- 全方位覆盖提示词工程生态系统，包括基础Prompt Engineering、上下文工程、RAG检索增强生成和AI智能体等核心技术
- 提供多元化学习资源形式：实践指南、学术论文、交互式笔记本、课程教程，满足不同学习偏好的开发者需求
- 紧跟AI前沿技术趋势，涵盖ChatGPT、LLMs、生成式AI、深度学习等热门技术栈，内容持续更新迭代
- 开源友好（MIT许可），社区活跃，汇集了业界最佳实践和研究成果，适合系统学习和快速查阅

**适用场景**:
- AI应用开发者学习提示词设计模式和最佳实践，提升与大语言模型交互的效果和效率
- 企业技术团队构建RAG系统或AI Agents时，参考权威指南和论文，加速产品研发落地
- AI研究者快速了解提示词工程领域的前沿进展和技术方案，为学术研究提供理论基础



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,338 |
| 语言 | Java |
| Forks | 15,831 |
| Issues | 50 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,134 |
| 语言 | Python |
| Forks | 2,036 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,033 |
| 语言 | TypeScript |
| Forks | 2,250 |
| Issues | 78 |
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
| Stars | 38,634 |
| 语言 | Python |
| Forks | 6,118 |
| Issues | 195 |
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
| Stars | 31,176 |
| 语言 | Jupyter Notebook |
| Forks | 5,074 |
| Issues | 124 |
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
| Stars | 99,814 |
| 语言 | Python |
| Forks | 14,509 |
| Issues | 8 |
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
| Stars | 98,574 |
| 语言 | TypeScript |
| Forks | 11,716 |
| Issues | 970 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,393 |
| 语言 | TypeScript |
| Forks | 23,876 |
| Issues | 792 |
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
| Stars | 71,630 |
| 语言 | Python |
| Forks | 9,899 |
| Issues | 265 |
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
| Stars | 43,150 |
| 语言 | Go |
| Forks | 3,868 |
| Issues | 1,043 |
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
| Stars | 31,248 |
| 语言 | Python |
| Forks | 3,296 |
| Issues | 70 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,244 |
| 语言 | TypeScript |
| Forks | 3,312 |
| Issues | 245 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


## 💬 LLM 界面 (25 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,861 |
| 语言 | Python |
| Forks | 17,808 |
| Issues | 306 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最受欢迎的开源 AI 对话界面之一，拥有 12.5 万+ stars，提供类似 ChatGPT 的现代化用户体验。它的独特价值在于完全自托管、支持多种 AI 后端（Ollama、OpenAI API 等），并且功能丰富度极高，包括 RAG、MCP 协议支持等，是个人和企业快速搭建私有 AI 服务的最佳选择。

**技术亮点**:
- 多后端兼容性：同时支持 Ollama、OpenAI API 等多种 LLM 后端，灵活切换不同 AI 模型
- RAG（检索增强生成）集成：内置文档上传和知识库功能，支持基于私有数据的智能问答
- MCP 协议支持：集成 Model Context Protocol，实现更强大的工具调用和上下文管理能力
- 完全自托管部署：所有数据本地存储，保障隐私安全，适合企业和个人私有化部署
- 现代化 Web UI：提供类似 ChatGPT 的用户界面，支持多用户、模型管理、API key 管理等企业级功能

**适用场景**:
- 企业内部 AI 助手部署：为企业搭建私有的 AI 对话平台，接入内部知识库，保护数据隐私
- 个人开发者本地 LLM 实验环境：配合 Ollama 在本地运行开源大模型，进行 AI 应用开发和测试
- 多模型统一管理平台：整合多个 AI 服务商的 API，提供统一的对话界面和管理后台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,240 |
| 语言 | Python |
| Forks | 8,258 |
| Issues | 3,042 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的检索增强生成（RAG）开源引擎，完美融合了尖端 RAG 技术与 Agent 智能体能力，为大语言模型构建卓越的上下文理解层。该项目拥有超过 74k 的 GitHub Stars，采用 Apache 2.0 许可证，是企业级 AI 应用和智能搜索系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供深度上下文理解和智能工作流
- 强大的文档解析与理解引擎，支持多种格式文档的智能处理
- 集成 GraphRAG 和深度研究能力，提供知识图谱增强的检索体验
- 支持多种 LLM 后端（OpenAI、DeepSeek、Ollama 等），灵活性强
- 内置 MCP (Model Context Protocol) 和 AI 搜索功能，提供企业级上下文工程能力

**适用场景**:
- 企业知识库与智能问答系统：构建企业内部文档检索、智能客服和知识管理平台
- AI 智能搜索与深度研究：开发专业领域的深度搜索引擎和智能研究助手
- Agent 工作流自动化：创建具备文档理解和复杂推理能力的 AI 智能体应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,515 |
| 语言 | JavaScript |
| Forks | 7,614 |
| Issues | 32 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向Claude Code生态的智能体性能优化系统，集成了技能、记忆、安全性和研究优先开发能力，帮助开发者大幅提升AI编程助手的工作效率和代码质量。该项目获得了超6万星标，是当前最热门的Claude工具链优化方案之一。

**技术亮点**:
- 集成MCP（Model Context Protocol）实现可扩展的插件架构，支持与Claude Code、Codex、Cowork等多种工具无缝协作
- 提供内存管理（Memory）和技能系统（Skills），让AI助手能够学习开发习惯并积累专业知识
- 内置安全防护机制（Security），确保AI生成的代码符合安全最佳实践
- 研究优先（Research-first）的开发模式，持续优化AI代理的性能和准确性
- 基于JavaScript/TypeScript技术栈，易于集成到现有的开发工作流中

**适用场景**:
- 个人开发者：通过Claude Code提升编程效率，自动化代码生成、重构和调试工作
- 企业开发团队：统一团队AI辅助编程标准，利用MCP集成内部工具和知识库，提升协作效率
- AI工具开发者：基于该项目扩展Claude生态，构建定制化的AI编码助手和企业级解决方案



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,650 |
| 语言 | JavaScript |
| Forks | 6,019 |
| Issues | 310 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，它将 RAG、AI 智能体、No-code 构建器和 MCP 兼容性集成在一个开箱即用的桌面和 Docker 应用中。作为 55k+ stars 的开源项目，它不仅支持本地 LLM（如 Ollama、LM Studio）和云端模型，还提供了完整的多模态 AI 解决方案，降低了企业构建私有化 AI 助手的门槛。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量数据库和网页抓取，实现知识库增强的智能对话
- MCP（Model Context Protocol）兼容性，可无缝连接各种 MCP 服务器扩展功能
- No-code 智能体构建器，让非开发者也能快速创建和定制 AI Agent
- 多模型支持：集成 DeepSeek、Kimi、Llama3、Qwen3、Moonshot 等主流开源和商业模型
- 灵活部署方式：支持桌面应用和 Docker 容器化部署，适配本地 LLM（Ollama、LocalAI）和云端 API

**适用场景**:
- 企业私有化 AI 知识助手：结合 RAG 技术构建基于企业内部文档的智能问答系统，无需数据外泄
- 开发者快速构建 AI Agent：利用 No-code 构建器和 MCP 生态快速开发定制化 AI 智能体应用
- 个人本地 AI 工作台：在本地运行 LLM（通过 Ollama 等）搭建隐私安全的个人 AI 助手，支持多模态交互



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,121 |
| 语言 | TypeScript |
| Forks | 14,727 |
| Issues | 704 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个革命性的多智能体协作平台，通过创新的 Agent 作为工作交互单元的理念，让用户能够轻松设计、构建和协作多个 AI 智能体团队。该项目已获得 7.3 万+ Stars，凭借其对 OpenAI、Claude、DeepSeek、Gemini 等主流 LLM 的全面支持以及 MCP 协议集成，成为当前最成熟的企业级智能体协作解决方案之一。

**技术亮点**:
- 基于 TypeScript 构建的企业级架构，提供高性能的类型安全开发体验
- 原生支持多智能体协作模式（Multi-Agent Collaboration），实现智能体间的无缝配合
- 集成 MCP（Model Context Protocol）协议，提供标准化的模型上下文交互能力
- 支持 GPT、Claude、Gemini、DeepSeek 等多种大语言模型，提供灵活的模型切换能力
- 内置知识库系统（Knowledge Base），支持智能体的知识积累与持续学习成长

**适用场景**:
- 企业团队协作：构建企业级 AI 智能体团队，实现自动化工作流程和跨部门协作，提升团队工作效率
- 个人开发者工具：个人开发者可快速搭建专属 AI 助手团队，用于代码生成、调试、文档编写等开发任务
- 知识管理与问答：建立基于企业内部知识库的智能问答系统，支持员工快速获取信息和知识沉淀



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,145 |
| 语言 | MDX |
| Forks | 7,581 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示词工程指南项目（71k+ stars），由AI研究社区DAIR AI维护，涵盖了从基础的Prompt Engineering到前沿的AI Agents、RAG等完整技术栈，是AI开发者必备的系统性学习资源和实践指南。

**技术亮点**:
- 全方位覆盖提示词工程生态系统，包括基础Prompt Engineering、上下文工程、RAG检索增强生成和AI智能体等核心技术
- 提供多元化学习资源形式：实践指南、学术论文、交互式笔记本、课程教程，满足不同学习偏好的开发者需求
- 紧跟AI前沿技术趋势，涵盖ChatGPT、LLMs、生成式AI、深度学习等热门技术栈，内容持续更新迭代
- 开源友好（MIT许可），社区活跃，汇集了业界最佳实践和研究成果，适合系统学习和快速查阅

**适用场景**:
- AI应用开发者学习提示词设计模式和最佳实践，提升与大语言模型交互的效果和效率
- 企业技术团队构建RAG系统或AI Agents时，参考权威指南和论文，加速产品研发落地
- AI研究者快速了解提示词工程领域的前沿进展和技术方案，为学术研究提供理论基础



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,147 |
| 语言 | HTML |
| Forks | 19,734 |
| Issues | 12 |
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
| Stars | 87,201 |
| 语言 | Jupyter Notebook |
| Forks | 13,249 |
| Issues | 0 |
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
| Stars | 41,910 |
| 语言 | Python |
| Forks | 9,792 |
| Issues | 351 |
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
| Stars | 34,368 |
| 语言 | TypeScript |
| Forks | 6,936 |
| Issues | 428 |
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
| Stars | 33,134 |
| 语言 | Python |
| Forks | 2,036 |
| Issues | 90 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,033 |
| 语言 | TypeScript |
| Forks | 2,250 |
| Issues | 78 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,612 |
| 语言 | Python |
| Forks | 8,565 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,212 |
| 语言 | TypeScript |
| Forks | 2,797 |
| Issues | 330 |
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
| Stars | 50,393 |
| 语言 | TypeScript |
| Forks | 23,876 |
| Issues | 792 |
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
| Stars | 33,792 |
| 语言 | HTML |
| Forks | 5,401 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,123 |
| 语言 | Python |
| Forks | 13,990 |
| Issues | 3,524 |
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
| Stars | 37,449 |
| 语言 | Python |
| Forks | 3,644 |
| Issues | 61 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 145,277 |
| 语言 | Python |
| Forks | 8,515 |
| Issues | 898 |
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
| Stars | 164,188 |
| 语言 | Go |
| Forks | 14,780 |
| Issues | 2,570 |
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
| Stars | 46,444 |
| 语言 | Rust |
| Forks | 9,086 |
| Issues | 2 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 30,319 |
| 语言 | Python |
| Forks | 3,318 |
| Issues | 8 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 38,781 |
| 语言 | TypeScript |
| Forks | 3,925 |
| Issues | 1,058 |
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
| Stars | 41,060 |
| 语言 | Python |
| Forks | 4,077 |
| Issues | 251 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 90,152 |
| 语言 | Python |
| Forks | 5,289 |
| Issues | 445 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (13 个项目)


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,145 |
| 语言 | MDX |
| Forks | 7,581 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示词工程指南项目（71k+ stars），由AI研究社区DAIR AI维护，涵盖了从基础的Prompt Engineering到前沿的AI Agents、RAG等完整技术栈，是AI开发者必备的系统性学习资源和实践指南。

**技术亮点**:
- 全方位覆盖提示词工程生态系统，包括基础Prompt Engineering、上下文工程、RAG检索增强生成和AI智能体等核心技术
- 提供多元化学习资源形式：实践指南、学术论文、交互式笔记本、课程教程，满足不同学习偏好的开发者需求
- 紧跟AI前沿技术趋势，涵盖ChatGPT、LLMs、生成式AI、深度学习等热门技术栈，内容持续更新迭代
- 开源友好（MIT许可），社区活跃，汇集了业界最佳实践和研究成果，适合系统学习和快速查阅

**适用场景**:
- AI应用开发者学习提示词设计模式和最佳实践，提升与大语言模型交互的效果和效率
- 企业技术团队构建RAG系统或AI Agents时，参考权威指南和论文，加速产品研发落地
- AI研究者快速了解提示词工程领域的前沿进展和技术方案，为学术研究提供理论基础



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,930 |
| 语言 | Python |
| Forks | 8,284 |
| Issues | 917 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个统一高效的100+大模型微调框架（ACL 2024论文成果），支持LoRA、QLoRA、全量微调等多种方式，覆盖LLaMA、Qwen、DeepSeek、Gemma等主流模型。该项目在GitHub获得超过6.7万星标，是企业级AI应用部署和个人开发者快速定制大模型的最佳开源工具。

**技术亮点**:
- 统一支持100+个大语言模型与视觉语言模型，包括LLaMA 3、Qwen、DeepSeek、Gemma、Mistral等主流开源模型
- 提供完整微调技术栈：LoRA、QLoRA、全量微调、MoE（混合专家模型）及量化技术，大幅降低显存需求
- 集成RLHF（人类反馈强化学习）与Agent指令调优功能，可直接训练对话助手和智能体
- 内置Web UI可视化界面与命令行工具，零代码/低代码即可完成模型微调流程
- 基于Transformers生态，兼容Hugging Face模型库，支持多模态(VLM)训练与推理

**适用场景**:
- 企业快速定制垂直领域大模型：企业可在有限GPU资源下，通过QLoRA等技术快速微调专属模型（如金融、医疗、法律等领域的专用模型）
- 个人开发者训练专属AI助手：基于LLaMA、Qwen等开源模型进行指令微调，打造个人AI伴侣或特定任务助手
- 学术研究与算法验证：研究人员可快速复现ACL 2024论文成果，对比不同微调方法（如LoRA vs QLoRA vs 全量微调）的效果
- 构建智能Agent系统：结合Agent训练功能，开发具备工具调用、规划推理能力的AI智能体应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,596 |
| 语言 | Python |
| Forks | 6,123 |
| Issues | 60 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是金融数据领域的开源标杆项目，拥有超过 6.2 万颗星，为分析师、量化工程师和 AI 代理提供统一的金融数据平台。其独特价值在于打破了彭博终端等昂贵商业工具的垄断，以开源方式提供覆盖股票、期权、加密货币、固定收益、宏观经济等多资产类别的数据获取和分析能力，大幅降低了金融数据分析的门槛和成本。

**技术亮点**:
- 统一的数据访问接口：支持超过 400+ 数据提供商，覆盖股票、期权、衍生品、加密货币、固定收益、宏观经济等多资产类别
- Python 优先架构：基于 Python 构建，无缝集成 pandas、numpy、scipy 等科学计算栈，支持 Jupyter Notebook 交互式分析
- AI/ML 友好设计：专为 AI 代理和机器学习模型优化，提供结构化数据输出，便于构建量化交易策略和金融 AI 应用
- 模块化插件系统：支持自定义数据源和分析工具的扩展，采用 MIT 等宽松许可证，适合二次开发和商业集成
- 多终端支持：提供命令行工具 (CLI)、Python SDK 和 Web 界面，满足不同用户群体的使用习惯

**适用场景**:
- 量化投资研究：个人量化交易者或小型对冲基金使用该平台获取多资产类别数据，构建回测策略和风险模型，替代昂贵的彭博终端等商业数据服务
- 金融 AI 应用开发：开发者为 AI 代理和 LLM（大语言模型）构建金融数据工具链，实现自动化的财务分析、新闻摘要和投资建议生成
- 企业级金融数据集成：金融科技公司和传统机构将 OpenBB 集成到内部系统中，为客户提供市场数据可视化和分析工具，降低数据采购成本



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,147 |
| 语言 | HTML |
| Forks | 19,734 |
| Issues | 12 |
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
| Stars | 87,201 |
| 语言 | Jupyter Notebook |
| Forks | 13,249 |
| Issues | 0 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 31,176 |
| 语言 | Jupyter Notebook |
| Forks | 5,074 |
| Issues | 124 |
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
| Stars | 157,441 |
| 语言 | Python |
| Forks | 32,299 |
| Issues | 2,273 |
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
| Stars | 72,123 |
| 语言 | Python |
| Forks | 13,990 |
| Issues | 3,524 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,504 |
| 语言 | Python |
| Forks | 30,119 |
| Issues | 2,465 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


### Comfy-Org/ComfyUI

**描述**: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,948 |
| 语言 | Python |
| Forks | 12,033 |
| Issues | 3,790 |
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
| Stars | 97,983 |
| 语言 | Python |
| Forks | 27,079 |
| Issues | 18,085 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### ItzCrazyKns/Perplexica

**描述**: Perplexica is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,244 |
| 语言 | TypeScript |
| Forks | 3,312 |
| Issues | 245 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


### mlabonne/llm-course

**描述**: Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 88/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,099 |
| 语言 | Unknown |
| Forks | 8,783 |
| Issues | 77 |
| Topics | course, large-language-models, llm, machine-learning, roadmap |
| 许可证 | Apache License 2.0 |


## 🛠️ 开发工具 (17 个项目)


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,515 |
| 语言 | JavaScript |
| Forks | 7,614 |
| Issues | 32 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个面向Claude Code生态的智能体性能优化系统，集成了技能、记忆、安全性和研究优先开发能力，帮助开发者大幅提升AI编程助手的工作效率和代码质量。该项目获得了超6万星标，是当前最热门的Claude工具链优化方案之一。

**技术亮点**:
- 集成MCP（Model Context Protocol）实现可扩展的插件架构，支持与Claude Code、Codex、Cowork等多种工具无缝协作
- 提供内存管理（Memory）和技能系统（Skills），让AI助手能够学习开发习惯并积累专业知识
- 内置安全防护机制（Security），确保AI生成的代码符合安全最佳实践
- 研究优先（Research-first）的开发模式，持续优化AI代理的性能和准确性
- 基于JavaScript/TypeScript技术栈，易于集成到现有的开发工作流中

**适用场景**:
- 个人开发者：通过Claude Code提升编程效率，自动化代码生成、重构和调试工作
- 企业开发团队：统一团队AI辅助编程标准，利用MCP集成内部工具和知识库，提升协作效率
- AI工具开发者：基于该项目扩展Claude生态，构建定制化的AI编码助手和企业级解决方案



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,280 |
| 语言 | Go |
| Forks | 3,634 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源 AI 基础设施项目，它提供了与 OpenAI、Claude 等商业服务完全兼容的 API 接口，但完全本地化运行，无需 GPU 和云服务。这解决了数据隐私、成本控制和离线部署三大痛点，让个人开发者和小企业也能在普通硬件上运行最前沿的 AI 模型，是实现 AI 自主化和去中心化推理的理想选择。

**技术亮点**:
- 🤖 多模态支持：集成 gguf、transformers、diffusers 等多种模型后端，支持文本、音频、图像、视频生成，以及语音克隆、目标检测等丰富功能
- 🔄 完全兼容 OpenAI API：Drop-in replacement 设计，无需修改代码即可无缝切换，支持 MCP 协议和 Rerank 功能
- 💻 零 GPU 部署：优化推理性能，可在消费级硬件（CPU）上运行，大幅降低部署门槛和硬件成本
- 🌐 去中心化架构：基于 libp2p 实现 P2P 分布式推理，支持联邦学习和跨节点协同计算
- 🎯 模型生态丰富：内置支持 LLaMA、Mistral、Gemma、RWKV、Mamba、Stable Diffusion、MusicGen 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求严格的行业，可本地部署 LLM 和多模态 AI 服务，确保敏感数据不出内网
- 👨‍💻 个人开发者 AI 应用：在普通电脑上搭建完整的 AI 开发环境，测试和部署聊天机器人、图像生成、语音合成等应用，无需承担 API 调用成本
- 🌍 离线/边缘计算场景：在无网络或弱网环境（如野外作业、船舶、军事设施）中提供 AI 能力，结合 P2P 分布式实现节点间资源共享



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,612 |
| 语言 | Python |
| Forks | 8,565 |
| Issues | 356 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,212 |
| 语言 | TypeScript |
| Forks | 2,797 |
| Issues | 330 |
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
| Stars | 177,730 |
| 语言 | TypeScript |
| Forks | 55,462 |
| Issues | 1,423 |
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
| Stars | 149,739 |
| 语言 | Python |
| Forks | 12,122 |
| Issues | 2,357 |
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
| Stars | 95,911 |
| 语言 | Python |
| Forks | 8,789 |
| Issues | 144 |
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
| Stars | 73,393 |
| 语言 | Python |
| Forks | 8,707 |
| Issues | 202 |
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
| Stars | 182,323 |
| 语言 | TypeScript |
| Forks | 38,301 |
| Issues | 14,622 |
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
| Stars | 93,713 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 284 |
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
| Stars | 78,155 |
| 语言 | TypeScript |
| Forks | 5,616 |
| Issues | 676 |
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
| Stars | 76,489 |
| 语言 | TypeScript |
| Forks | 6,537 |
| Issues | 170 |
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
| Stars | 75,641 |
| 语言 | JavaScript |
| Forks | 7,267 |
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
| Stars | 78,324 |
| 语言 | Go |
| Forks | 2,701 |
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
| Stars | 73,563 |
| 语言 | Go |
| Forks | 2,559 |
| Issues | 914 |
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
| Stars | 42,927 |
| 语言 | Go |
| Forks | 8,021 |
| Issues | 926 |
| Topics | cli, git, github-api-v4, golang |
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
| Stars | 404,488 |
| 语言 | Python |
| Forks | 43,649 |
| Issues | 932 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目)


### 🌟 高优先级


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,212 |
| 语言 | TypeScript |
| Forks | 2,797 |
| Issues | 330 |
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
| Stars | 177,730 |
| 语言 | TypeScript |
| Forks | 55,462 |
| Issues | 1,423 |
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
| Stars | 51,611 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 216 |
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
| Stars | 120,940 |
| 语言 | Go |
| Forks | 42,595 |
| Issues | 2,676 |
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
| Forks | 18,913 |
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
| Stars | 54,103 |
| 语言 | Go |
| Forks | 6,425 |
| Issues | 2,846 |
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
| Stars | 47,545 |
| 语言 | Go |
| Forks | 5,065 |
| Issues | 962 |
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
| Stars | 30,319 |
| 语言 | Python |
| Forks | 3,318 |
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
| Stars | 93,713 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 284 |
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
| Stars | 83,533 |
| 语言 | TypeScript |
| Forks | 5,233 |
| Issues | 612 |
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
| Stars | 74,975 |
| 语言 | TypeScript |
| Forks | 6,355 |
| Issues | 420 |
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
| Stars | 83,630 |
| 语言 | JavaScript |
| Forks | 7,477 |
| Issues | 701 |
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
| Stars | 69,158 |
| 语言 | Go |
| Forks | 1,870 |
| Issues | 290 |
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
| Stars | 62,050 |
| 语言 | Go |
| Forks | 5,857 |
| Issues | 765 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### usememos/memos

**描述**: An open-source, self-hosted note-taking service. Your thoughts, your data, your control — no tracking, no ads, no subscription fees.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,496 |
| 语言 | Go |
| Forks | 4,153 |
| Issues | 19 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,060 |
| 语言 | Python |
| Forks | 4,077 |
| Issues | 251 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,430 |
| 语言 | Go |
| Forks | 7,181 |
| Issues | 80 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


## 📈 监控/观测 (2 个项目)


### 🌟 高优先级


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,630 |
| 语言 | JavaScript |
| Forks | 7,477 |
| Issues | 701 |
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
| Stars | 63,055 |
| 语言 | Go |
| Forks | 10,212 |
| Issues | 749 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (13 个项目)


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,280 |
| 语言 | Go |
| Forks | 3,634 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源 AI 基础设施项目，它提供了与 OpenAI、Claude 等商业服务完全兼容的 API 接口，但完全本地化运行，无需 GPU 和云服务。这解决了数据隐私、成本控制和离线部署三大痛点，让个人开发者和小企业也能在普通硬件上运行最前沿的 AI 模型，是实现 AI 自主化和去中心化推理的理想选择。

**技术亮点**:
- 🤖 多模态支持：集成 gguf、transformers、diffusers 等多种模型后端，支持文本、音频、图像、视频生成，以及语音克隆、目标检测等丰富功能
- 🔄 完全兼容 OpenAI API：Drop-in replacement 设计，无需修改代码即可无缝切换，支持 MCP 协议和 Rerank 功能
- 💻 零 GPU 部署：优化推理性能，可在消费级硬件（CPU）上运行，大幅降低部署门槛和硬件成本
- 🌐 去中心化架构：基于 libp2p 实现 P2P 分布式推理，支持联邦学习和跨节点协同计算
- 🎯 模型生态丰富：内置支持 LLaMA、Mistral、Gemma、RWKV、Mamba、Stable Diffusion、MusicGen 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求严格的行业，可本地部署 LLM 和多模态 AI 服务，确保敏感数据不出内网
- 👨‍💻 个人开发者 AI 应用：在普通电脑上搭建完整的 AI 开发环境，测试和部署聊天机器人、图像生成、语音合成等应用，无需承担 API 调用成本
- 🌍 离线/边缘计算场景：在无网络或弱网环境（如野外作业、船舶、军事设施）中提供 AI 能力，结合 P2P 分布式实现节点间资源共享



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,911 |
| 语言 | Python |
| Forks | 8,789 |
| Issues | 144 |
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
| Stars | 86,973 |
| 语言 | Python |
| Forks | 33,715 |
| Issues | 422 |
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
| Stars | 100,072 |
| 语言 | TypeScript |
| Forks | 27,099 |
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
| Stars | 78,155 |
| 语言 | TypeScript |
| Forks | 5,616 |
| Issues | 676 |
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
| Stars | 74,864 |
| 语言 | TypeScript |
| Forks | 8,232 |
| Issues | 42 |
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
| Stars | 75,641 |
| 语言 | JavaScript |
| Forks | 7,267 |
| Issues | 706 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,866 |
| 语言 | JavaScript |
| Forks | 22,734 |
| Issues | 189 |
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
| Forks | 10,221 |
| Issues | 345 |
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
| Stars | 88,196 |
| 语言 | Go |
| Forks | 8,568 |
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
| Stars | 70,596 |
| 语言 | Go |
| Forks | 4,658 |
| Issues | 229 |
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
| Stars | 56,557 |
| 语言 | Go |
| Forks | 3,162 |
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
| Stars | 404,488 |
| 语言 | Python |
| Forks | 43,649 |
| Issues | 932 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## 📊 数据/基础设施 (4 个项目)


### 🌟 高优先级


### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,650 |
| 语言 | JavaScript |
| Forks | 6,019 |
| Issues | 310 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，它将 RAG、AI 智能体、No-code 构建器和 MCP 兼容性集成在一个开箱即用的桌面和 Docker 应用中。作为 55k+ stars 的开源项目，它不仅支持本地 LLM（如 Ollama、LM Studio）和云端模型，还提供了完整的多模态 AI 解决方案，降低了企业构建私有化 AI 助手的门槛。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量数据库和网页抓取，实现知识库增强的智能对话
- MCP（Model Context Protocol）兼容性，可无缝连接各种 MCP 服务器扩展功能
- No-code 智能体构建器，让非开发者也能快速创建和定制 AI Agent
- 多模型支持：集成 DeepSeek、Kimi、Llama3、Qwen3、Moonshot 等主流开源和商业模型
- 灵活部署方式：支持桌面应用和 Docker 容器化部署，适配本地 LLM（Ollama、LocalAI）和云端 API

**适用场景**:
- 企业私有化 AI 知识助手：结合 RAG 技术构建基于企业内部文档的智能问答系统，无需数据外泄
- 开发者快速构建 AI Agent：利用 No-code 构建器和 MCP 生态快速开发定制化 AI 智能体应用
- 个人本地 AI 工作台：在本地运行 LLM（通过 Ollama 等）搭建隐私安全的个人 AI 助手，支持多模态交互



### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,574 |
| 语言 | TypeScript |
| Forks | 11,716 |
| Issues | 970 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,150 |
| 语言 | Go |
| Forks | 3,868 |
| Issues | 1,043 |
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
| Stars | 51,611 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 216 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目)


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,145 |
| 语言 | MDX |
| Forks | 7,581 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示词工程指南项目（71k+ stars），由AI研究社区DAIR AI维护，涵盖了从基础的Prompt Engineering到前沿的AI Agents、RAG等完整技术栈，是AI开发者必备的系统性学习资源和实践指南。

**技术亮点**:
- 全方位覆盖提示词工程生态系统，包括基础Prompt Engineering、上下文工程、RAG检索增强生成和AI智能体等核心技术
- 提供多元化学习资源形式：实践指南、学术论文、交互式笔记本、课程教程，满足不同学习偏好的开发者需求
- 紧跟AI前沿技术趋势，涵盖ChatGPT、LLMs、生成式AI、深度学习等热门技术栈，内容持续更新迭代
- 开源友好（MIT许可），社区活跃，汇集了业界最佳实践和研究成果，适合系统学习和快速查阅

**适用场景**:
- AI应用开发者学习提示词设计模式和最佳实践，提升与大语言模型交互的效果和效率
- 企业技术团队构建RAG系统或AI Agents时，参考权威指南和论文，加速产品研发落地
- AI研究者快速了解提示词工程领域的前沿进展和技术方案，为学术研究提供理论基础



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,147 |
| 语言 | HTML |
| Forks | 19,734 |
| Issues | 12 |
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
| Stars | 33,792 |
| 语言 | HTML |
| Forks | 5,401 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,367 |
| 语言 | TypeScript |
| Forks | 9,882 |
| Issues | 2,244 |
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
| Stars | 86,500 |
| 语言 | TypeScript |
| Forks | 8,694 |
| Issues | 1,623 |
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
| Stars | 126,956 |
| 语言 | JavaScript |
| Forks | 12,442 |
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
| Stars | 99,551 |
| 语言 | JavaScript |
| Forks | 7,448 |
| Issues | 202 |
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
| Stars | 166,629 |
| 语言 | Go |
| Forks | 13,012 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目)


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 128,310 |
| 语言 | Unknown |
| Forks | 32,725 |
| Issues | 126 |
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
| Stars | 265,107 |
| 语言 | TypeScript |
| Forks | 50,738 |
| Issues | 12,201 |
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
| Stars | 61,414 |
| 语言 | Python |
| Forks | 6,271 |
| Issues | 271 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,850 |
| 语言 | Python |
| Forks | 11,636 |
| Issues | 128 |
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
| Stars | 74,330 |
| 语言 | Python |
| Forks | 6,340 |
| Issues | 628 |
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
| Stars | 383,630 |
| 语言 | Python |
| Forks | 66,009 |
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
| Stars | 112,421 |
| 语言 | TypeScript |
| Forks | 5,672 |
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
| Stars | 100,604 |
| 语言 | TypeScript |
| Forks | 7,321 |
| Issues | 172 |
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
| Stars | 47,878 |
| 语言 | Go |
| Forks | 10,234 |
| Issues | 1,912 |
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
| Stars | 96,791 |
| 语言 | C++ |
| Forks | 15,250 |
| Issues | 1,198 |
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
| Stars | 59,513 |
| 语言 | Python |
| Forks | 1,610 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### musistudio/claude-code-router

**描述**: Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 29,028 |
| 语言 | TypeScript |
| Forks | 2,222 |
| Issues | 810 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 285,724 |
| 语言 | Python |
| Forks | 27,298 |
| Issues | 16 |
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
| Stars | 218,362 |
| 语言 | Python |
| Forks | 50,126 |
| Issues | 925 |
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
| Stars | 85,155 |
| 语言 | Python |
| Forks | 36,914 |
| Issues | 3,492 |
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
| Stars | 77,686 |
| 语言 | Python |
| Forks | 45,255 |
| Issues | 1,282 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,743 |
| 语言 | Python |
| Forks | 16,708 |
| Issues | 13 |
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
| Stars | 437,807 |
| 语言 | TypeScript |
| Forks | 43,522 |
| Issues | 278 |
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
| Stars | 350,234 |
| 语言 | TypeScript |
| Forks | 43,740 |
| Issues | 41 |
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
| Stars | 118,087 |
| 语言 | TypeScript |
| Forks | 12,745 |
| Issues | 2,842 |
| Topics | canvas, collaboration, diagrams, drawing, hacktoberfest, productivity, whiteboard |
| 许可证 | MIT License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,024 |
| 语言 | TypeScript |
| Forks | 13,255 |
| Issues | 5,473 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### shadcn-ui/ui

**描述**: A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Open Code.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 107,763 |
| 语言 | TypeScript |
| Forks | 8,009 |
| Issues | 1,765 |
| Topics | base-ui, components, nextjs, radix-ui, react, shadcn, tailwindcss, ui |
| 许可证 | MIT License |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,672 |
| 语言 | TypeScript |
| Forks | 54,544 |
| Issues | 1,376 |
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
| Stars | 94,085 |
| 语言 | TypeScript |
| Forks | 5,012 |
| Issues | 646 |
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
| Stars | 93,918 |
| 语言 | TypeScript |
| Forks | 5,096 |
| Issues | 84 |
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
| Stars | 82,917 |
| 语言 | TypeScript |
| Forks | 7,572 |
| Issues | 39 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,241 |
| 语言 | TypeScript |
| Forks | 9,774 |
| Issues | 422 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,612 |
| 语言 | TypeScript |
| Forks | 7,879 |
| Issues | 634 |
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
| Stars | 243,639 |
| 语言 | JavaScript |
| Forks | 50,649 |
| Issues | 1,142 |
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
| Stars | 138,166 |
| 语言 | JavaScript |
| Forks | 30,555 |
| Issues | 3,416 |
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
| Stars | 116,084 |
| 语言 | JavaScript |
| Forks | 34,937 |
| Issues | 2,500 |
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
| Stars | 111,192 |
| 语言 | JavaScript |
| Forks | 36,280 |
| Issues | 597 |
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
| Stars | 108,581 |
| 语言 | JavaScript |
| Forks | 11,534 |
| Issues | 349 |
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
| Forks | 32,719 |
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
| Stars | 95,384 |
| 语言 | JavaScript |
| Forks | 15,198 |
| Issues | 70 |
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
| Stars | 86,001 |
| 语言 | JavaScript |
| Forks | 4,792 |
| Issues | 977 |
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
| Stars | 78,622 |
| 语言 | JavaScript |
| Forks | 31,286 |
| Issues | 270 |
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
| Stars | 70,665 |
| 语言 | JavaScript |
| Forks | 16,803 |
| Issues | 889 |
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
| Stars | 67,216 |
| 语言 | JavaScript |
| Forks | 11,991 |
| Issues | 536 |
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
| Stars | 66,261 |
| 语言 | JavaScript |
| Forks | 9,184 |
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
| Stars | 66,021 |
| 语言 | JavaScript |
| Forks | 9,305 |
| Issues | 204 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jquery/jquery

**描述**: jQuery JavaScript Library

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,853 |
| 语言 | JavaScript |
| Forks | 20,474 |
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
| Stars | 59,675 |
| 语言 | JavaScript |
| Forks | 5,595 |
| Issues | 63 |
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
| Stars | 57,396 |
| 语言 | JavaScript |
| Forks | 12,309 |
| Issues | 24 |
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
| Stars | 132,895 |
| 语言 | Go |
| Forks | 18,841 |
| Issues | 9,829 |
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
| Stars | 104,905 |
| 语言 | Go |
| Forks | 14,918 |
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
| Stars | 86,915 |
| 语言 | Go |
| Forks | 8,196 |
| Issues | 268 |
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
| Stars | 80,532 |
| 语言 | Go |
| Forks | 4,947 |
| Issues | 402 |
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
| Stars | 68,708 |
| 语言 | Go |
| Forks | 3,214 |
| Issues | 16 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,859 |
| 语言 | Go |
| Forks | 4,944 |
| Issues | 1,129 |
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
| Stars | 50,892 |
| 语言 | Go |
| Forks | 21,828 |
| Issues | 387 |
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
| Stars | 49,110 |
| 语言 | Go |
| Forks | 7,984 |
| Issues | 583 |
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
| Stars | 45,233 |
| 语言 | Go |
| Forks | 3,743 |
| Issues | 96 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 144,887 |
| 语言 | Python |
| Forks | 11,170 |
| Issues | 285 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,798 |
| 语言 | Python |
| Forks | 10,601 |
| Issues | 4,118 |
| 许可证 | The Unlicense |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 84,987 |
| 语言 | Python |
| Forks | 7,148 |
| Issues | 474 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,731 |
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
| Stars | 148,093 |
| 语言 | JavaScript |
| Forks | 26,771 |
| Issues | 186 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### FortAwesome/Font-Awesome

**描述**: The iconic SVG, font, and CSS toolkit

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,395 |
| 语言 | JavaScript |
| Forks | 12,244 |
| Issues | 315 |
| Topics | css, font, fontawesome, icons, svg-icons, svg-sprites, webfont |
| 许可证 | Other |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,746 |
| 语言 | JavaScript |
| Forks | 4,464 |
| Issues | 93 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,919 |
| 语言 | JavaScript |
| Forks | 3,966 |
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
| Stars | 61,581 |
| 语言 | JavaScript |
| Forks | 7,125 |
| Issues | 123 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |
