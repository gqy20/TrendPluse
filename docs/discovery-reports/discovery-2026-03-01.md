# 项目发现报告 (2026-03-01)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 138 |
| 去重移除 | 32 |
| 已在监控 | 20 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 18 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 13 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 17 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 63 |

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


## 🤖 AI Agents (28 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,325 |
| 语言 | Python |
| Forks | 17,750 |
| Issues | 256 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互界面项目，拥有 12.5 万+ Stars 的高人气，支持 Ollama、OpenAI API 等多种大模型后端，并提供 RAG、MCP 等企业级功能。它是目前最成熟的 LLM Web UI 解决方案之一，既适合个人开发者快速搭建 AI 应用，也适合企业构建私有化 AI 平台。

**技术亮点**:
- 🔌 多后端支持：统一集成 Ollama、OpenAI API、MCP (Model Context Protocol) 等多种大模型接口
- 🔍 内置 RAG 能力：支持检索增强生成，可直接对接本地知识库实现智能问答
- 🏠 完全自托管：可私有化部署，数据完全可控，适合对数据安全要求高的场景
- 🎨 现代化 Web UI：提供类似 ChatGPT 的友好交互界面，支持多会话管理
- ⚙️ Python 技术栈：基于 Python 构建，易于二次开发和扩展定制

**适用场景**:
- 🏢 企业私有化 AI 平台：搭建企业内部 LLM 服务，保护敏感数据不外泄，支持接入本地部署的开源模型（如通过 Ollama）
- 👨‍💻 个人开发者 AI 工具集：快速构建个人 AI 助手、知识库问答系统，支持多种模型切换对比
- 🎓 教育与研究场景：为学生或研究人员提供统一的 LLM 实验环境，便于教学演示和模型效果对比



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,960 |
| 语言 | Python |
| Forks | 8,224 |
| Issues | 3,013 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个领先的开源 RAG 引擎，它将检索增强生成技术与 Agent 能力创新性融合，为大语言模型构建了卓越的上下文层。该项目在 GitHub 上获得了超过 7.3 万颗星，具备强大的文档解析、知识图谱集成和深度研究能力，是企业构建 AI 应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 技术，提供智能化的检索增强生成能力
- 支持 GraphRAG 知识图谱检索，实现更精准的语义理解和上下文关联
- 内置强大的文档解析器，支持复杂文档的深度理解和结构化提取
- 集成主流 LLM 生态（OpenAI、DeepSeek、Ollama 等），提供灵活的模型接入能力
- 支持 MCP (Model Context Protocol) 和深度研究工作流，构建端到端的 AI 解决方案

**适用场景**:
- 企业级知识管理系统：构建基于企业文档的智能问答和知识检索平台
- 智能客服与助手：结合文档理解和 Agent 能力，打造能处理复杂任务的 AI 助手
- 深度研究与分析系统：利用 GraphRAG 和深度研究能力，进行跨文档的知识发现和关联分析



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,003 |
| 语言 | TypeScript |
| Forks | 6,193 |
| Issues | 197 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用设计的 Web 数据抓取和转换 API，能将整个网站智能转换为 LLM 可直接使用的 Markdown 或结构化数据。凭借 8.7 万+ 星标和专为 AI 场景优化的设计，它是构建 AI Agent、知识库和 RAG 应用的理想数据获取工具，填补了传统爬虫与 AI 应用之间的关键鸿沟。

**技术亮点**:
- 🤖 AI-Native 设计：专门为大语言模型优化，输出纯净的 Markdown 或结构化数据，直接可用于 LLM 上下文
- 🌐 全站抓取能力：支持将整个网站（包括多页面、JavaScript 渲染内容）完整抓取并转换为统一格式
- 🔄 智能数据处理：内置 HTML 到 Markdown 的高质量转换引擎，保留文档结构和语义信息
- 🔌 开箱即用的 API：提供简洁的 REST API，支持异步任务、批量处理和网页搜索集成
- ⚡ 多场景支持：集成了 web-scraping、web-crawler、web-search 等多种数据获取模式

**适用场景**:
- 🤖 AI Agent 和 Copilot 开发：为 AI 助手提供实时网页数据读取能力，支持 RAG 知识库构建
- 📚 企业知识库管理：将公司内网文档站点转换为 AI 可索引的结构化数据，用于企业智能问答系统
- 🔍 内容聚合与分析平台：批量抓取竞品网站、行业资讯站点，为市场分析和内容监控提供数据支持



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,957 |
| 语言 | JavaScript |
| Forks | 6,876 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为Claude Code、Codex等AI Agent设计的综合性能优化系统，集成了技能管理、记忆机制、安全防护和研究驱动开发等多个核心模块。作为获得5.5万+星标的热门项目，它为开发者提供了构建高效、安全AI助手的完整解决方案，显著提升AI编程助手的生产力和智能化水平。

**技术亮点**:
- ⚡ 多维度性能优化系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）等核心能力模块
- 🔒 企业级安全机制：内置安全防护体系，确保AI Agent在生产环境中的安全可控运行
- 🧠 研究驱动开发（Research-first）：采用前沿研究方法持续优化Agent性能和智能水平
- 🔌 MCP协议支持：兼容Model Context Protocol，实现与其他工具和服务的无缝集成
- 🛠️ 多平台兼容：支持Claude Code、Codex、Cowork等多种AI编程平台

**适用场景**:
- 🏢 企业级AI辅助开发：为开发团队提供增强版的Claude Code，提升代码编写、调试和项目开发效率
- 👨‍💻 个人开发者生产力工具：个人开发者可利用该系统构建定制化的AI编程助手，优化日常开发工作流
- 🔬 AI Agent研究与实验：研究者和AI工程师可基于此框架进行Agent性能优化实验和新特性开发



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,237 |
| 语言 | JavaScript |
| Forks | 5,968 |
| Issues | 302 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款集成了 RAG、AI Agents、No-code 构建器和 MCP 兼容性的全栈 AI 应用平台，支持本地和云端 LLM 部署。其独特价值在于提供开箱即用的企业级 AI 能力，同时保持开源和高度可定制，适合快速构建生产级 AI 应用。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库和网页抓取，实现智能文档问答
- 支持多种 LLM 后端：Ollama、LM Studio、LocalAI、DeepSeek、Kimi、Llama3、Qwen3 等，灵活切换模型
- No-code Agent 构建器 + MCP (Model Context Protocol) 兼容，轻松创建自定义 AI 智能体和集成外部工具
- 支持多模态 AI 能力，可处理文本、图像等多种媒体类型的输入输出
- 提供 Desktop 和 Docker 双部署方式，满足个人开发者和企业级部署需求

**适用场景**:
- 企业知识库搭建：利用 RAG 技术构建内部文档问答系统，员工可快速检索和查询公司知识
- 个人开发者 AI 助手：本地部署私有 AI Agent，集成代码生成、数据分析、自动化工作流等能力
- AI 产品快速原型开发：通过 No-code 构建器快速验证 AI 应用 idea，无需编码即可创建自定义智能体



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,167 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 153 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 模型部署平台，作为 OpenAI、Claude 等商业 API 的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行。其独特的价值在于提供了"开箱即用"的 drop-in 替换能力，同时支持文本、图像、音频、视频等多种 AI 生成任务，并集成了分布式推理、P2P 网络和 MCP 协议等前沿特性，是企业与个人开发者构建私有化 AI 服务的理想选择。

**技术亮点**:
- 🤖 多模型引擎支持：兼容 gguf、transformers、diffusers 等多种模型格式，支持 LLaMA、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流模型
- 💻 零 GPU 依赖设计：完全优化的 CPU 推理能力，可在消费级硬件上高效运行，大幅降低部署成本
- 🌐 分布式与 P2P 架构：基于 libp2p 实现去中心化推理网络，支持分布式计算资源调度，提升大规模推理效率
- 🎯 OpenAI API 兼容：提供 drop-in 替换能力，无需修改现有代码即可迁移至私有化部署
- 🎨 全模态 AI 能力：支持文本生成、图像生成、音频生成（TTS、MusicGen、Voice Cloning）、视频生成、目标检测等多种 AI 任务

**适用场景**:
- 🏢 企业私有化 AI 部署：金融、医疗、政府等对数据安全敏感的行业，可在内网部署完整的 AI 服务，避免数据外泄风险，同时大幅降低 API 调用成本
- 👨‍💻 个人开发者 AI 应用开发：开发者可在本地快速搭建 AI 开发测试环境，无需依赖云端 API，支持离线开发和调试
- 🌍 边缘计算与离线场景：适用于无网络或弱网络环境下的 AI 应用，如离线智能助手、本地语音交互系统等



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,838 |
| 语言 | TypeScript |
| Forks | 14,694 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个颠覆性的 AI 智能体协作平台，重新定义了人机协作方式。它不仅仅是工具，更是一个生态系统，让多智能体协作变得前所未有的简单和高效，在 72k+ Stars 的验证下，已成为 AI Agent 领域的事实标准平台之一。

**技术亮点**:
- 多智能体协作系统：支持多个 Agent 同时协作，实现复杂任务的分工与配合
- 可视化 Agent 团队设计器：零代码拖拽式构建 Agent 团队，降低技术门槛
- 全模型生态支持：无缝集成 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型
- MCP（Model Context Protocol）集成：提供标准化知识库连接能力
- TypeScript 全栈开发：类型安全的代码架构，确保企业级应用稳定性

**适用场景**:
- 企业级 AI 助手团队：构建客服、销售、技术支持等多角色 AI 团队，提供 24/7 智能服务
- 个人知识管理助手：搭建个人 Agent 生态，实现笔记整理、信息检索、内容创作等自动化工作流
- 开发者工具链集成：为开发团队构建代码审查、文档生成、问题排查等智能辅助系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,971 |
| 语言 | MDX |
| Forks | 7,555 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程开源指南（71k+ Stars），由AI社区组织Dair.AI维护，系统性地涵盖了从基础的Prompt Engineering到前沿的RAG和AI Agents技术的完整知识体系。该项目不仅提供了理论知识，还包含实践案例、论文资源和学习路径，是开发者快速掌握大模型应用开发技术的权威入门指南。

**技术亮点**:
- 📚 知识体系全面：覆盖提示工程、上下文工程、RAG检索增强生成、AI智能体等核心技术领域
- 🎓 多维度学习资源：包含指南文档、学术论文、互动课程、Jupyter笔记本等多种形式的学习材料
- 🚀 紧跟技术前沿：涵盖ChatGPT、OpenAI、LLMs、生成式AI等最新技术栈和工具
- 💡 实践导向：提供可运行的notebooks和案例代码，帮助开发者快速上手实践
- 🔄 持续更新维护：由专业AI组织Dair.AI维护，紧跟大模型技术发展动态

**适用场景**:
- 🏢 企业开发者：快速掌握RAG和AI Agents技术，构建企业级智能应用和知识库系统
- 👨‍💻 个人学习者：系统性学习提示工程方法论，提升与大模型交互的效率和效果
- 🎓 研究人员：获取相关领域最新论文和技术趋势，进行学术研究和技术探索



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,702 |
| 语言 | Python |
| Forks | 8,257 |
| Issues | 909 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个业界领先的大模型微调统一框架，以ACL 2024学术认可为基础，提供从训练到部署的一站式解决方案。其最大价值在于将复杂的LLM微调过程标准化、可视化，降低了企业和个人开发者使用LoRA、QLoRA、RLHF等先进技术的门槛，支持100+主流模型（包括DeepSeek、Qwen、Gemma、Llama3等），在GitHub获得6.7万+星标，是当前最活跃和实用的微调工具之一。

**技术亮点**:
- 支持100+种大语言模型和视觉语言模型，覆盖LLaMA系列、Qwen、DeepSeek、Gemma、GPT等主流开源模型
- 提供多种高效微调方法：LoRA、QLoRA、量化训练、MoE（混合专家）和RLHF（人类反馈强化学习）
- 集成GUI可视化界面和命令行工具，支持指令微调、Agent训练等多种训练范式
- 基于Transformers和PEFT构建，提供从数据预处理、模型训练到评估导出的完整工作流
- 开源友好（Apache 2.0许可），持续更新紧跟最新模型和技术发展

**适用场景**:
- 企业级场景：快速微调行业专用大模型，如金融、医疗、法律等垂直领域的知识增强和指令对齐
- 个人开发者/研究人员：低成本进行模型实验和研究，使用LoRA/QLoRA在消费级显卡上完成大模型微调
- AI应用开发：构建智能Agent系统，通过指令微调和RLHF优化模型的交互能力和任务执行能力



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,304 |
| 语言 | Java |
| Forks | 15,825 |
| Issues | 54 |
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
| Stars | 41,675 |
| 语言 | Python |
| Forks | 9,781 |
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
| Stars | 34,227 |
| 语言 | TypeScript |
| Forks | 6,913 |
| Issues | 423 |
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
| Stars | 32,721 |
| 语言 | Python |
| Forks | 1,983 |
| Issues | 88 |
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
| Stars | 31,998 |
| 语言 | TypeScript |
| Forks | 2,180 |
| Issues | 62 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,605 |
| 语言 | Python |
| Forks | 6,116 |
| Issues | 191 |
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
| Stars | 30,927 |
| 语言 | Jupyter Notebook |
| Forks | 5,040 |
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
| Stars | 98,611 |
| 语言 | Python |
| Forks | 14,350 |
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
| Stars | 68,366 |
| 语言 | Python |
| Forks | 8,529 |
| Issues | 360 |
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
| Stars | 35,779 |
| 语言 | TypeScript |
| Forks | 2,710 |
| Issues | 277 |
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
| Stars | 79,273 |
| 语言 | Python |
| Forks | 9,373 |
| Issues | 237 |
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
| Stars | 49,448 |
| 语言 | TypeScript |
| Forks | 23,764 |
| Issues | 779 |
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
| Stars | 177,007 |
| 语言 | TypeScript |
| Forks | 55,302 |
| Issues | 1,416 |
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
| Stars | 145,172 |
| 语言 | Python |
| Forks | 8,499 |
| Issues | 1,073 |
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
| Stars | 51,958 |
| 语言 | Jupyter Notebook |
| Forks | 18,186 |
| Issues | 1 |
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
| Stars | 29,159 |
| 语言 | TypeScript |
| Forks | 3,084 |
| Issues | 234 |
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
| Stars | 29,841 |
| 语言 | Python |
| Forks | 3,268 |
| Issues | 6 |
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
| Stars | 39,130 |
| 语言 | Python |
| Forks | 3,882 |
| Issues | 229 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


## 🔍 RAG/检索 (18 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,325 |
| 语言 | Python |
| Forks | 17,750 |
| Issues | 256 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互界面项目，拥有 12.5 万+ Stars 的高人气，支持 Ollama、OpenAI API 等多种大模型后端，并提供 RAG、MCP 等企业级功能。它是目前最成熟的 LLM Web UI 解决方案之一，既适合个人开发者快速搭建 AI 应用，也适合企业构建私有化 AI 平台。

**技术亮点**:
- 🔌 多后端支持：统一集成 Ollama、OpenAI API、MCP (Model Context Protocol) 等多种大模型接口
- 🔍 内置 RAG 能力：支持检索增强生成，可直接对接本地知识库实现智能问答
- 🏠 完全自托管：可私有化部署，数据完全可控，适合对数据安全要求高的场景
- 🎨 现代化 Web UI：提供类似 ChatGPT 的友好交互界面，支持多会话管理
- ⚙️ Python 技术栈：基于 Python 构建，易于二次开发和扩展定制

**适用场景**:
- 🏢 企业私有化 AI 平台：搭建企业内部 LLM 服务，保护敏感数据不外泄，支持接入本地部署的开源模型（如通过 Ollama）
- 👨‍💻 个人开发者 AI 工具集：快速构建个人 AI 助手、知识库问答系统，支持多种模型切换对比
- 🎓 教育与研究场景：为学生或研究人员提供统一的 LLM 实验环境，便于教学演示和模型效果对比



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,960 |
| 语言 | Python |
| Forks | 8,224 |
| Issues | 3,013 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个领先的开源 RAG 引擎，它将检索增强生成技术与 Agent 能力创新性融合，为大语言模型构建了卓越的上下文层。该项目在 GitHub 上获得了超过 7.3 万颗星，具备强大的文档解析、知识图谱集成和深度研究能力，是企业构建 AI 应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 技术，提供智能化的检索增强生成能力
- 支持 GraphRAG 知识图谱检索，实现更精准的语义理解和上下文关联
- 内置强大的文档解析器，支持复杂文档的深度理解和结构化提取
- 集成主流 LLM 生态（OpenAI、DeepSeek、Ollama 等），提供灵活的模型接入能力
- 支持 MCP (Model Context Protocol) 和深度研究工作流，构建端到端的 AI 解决方案

**适用场景**:
- 企业级知识管理系统：构建基于企业文档的智能问答和知识检索平台
- 智能客服与助手：结合文档理解和 Agent 能力，打造能处理复杂任务的 AI 助手
- 深度研究与分析系统：利用 GraphRAG 和深度研究能力，进行跨文档的知识发现和关联分析



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,237 |
| 语言 | JavaScript |
| Forks | 5,968 |
| Issues | 302 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款集成了 RAG、AI Agents、No-code 构建器和 MCP 兼容性的全栈 AI 应用平台，支持本地和云端 LLM 部署。其独特价值在于提供开箱即用的企业级 AI 能力，同时保持开源和高度可定制，适合快速构建生产级 AI 应用。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库和网页抓取，实现智能文档问答
- 支持多种 LLM 后端：Ollama、LM Studio、LocalAI、DeepSeek、Kimi、Llama3、Qwen3 等，灵活切换模型
- No-code Agent 构建器 + MCP (Model Context Protocol) 兼容，轻松创建自定义 AI 智能体和集成外部工具
- 支持多模态 AI 能力，可处理文本、图像等多种媒体类型的输入输出
- 提供 Desktop 和 Docker 双部署方式，满足个人开发者和企业级部署需求

**适用场景**:
- 企业知识库搭建：利用 RAG 技术构建内部文档问答系统，员工可快速检索和查询公司知识
- 个人开发者 AI 助手：本地部署私有 AI Agent，集成代码生成、数据分析、自动化工作流等能力
- AI 产品快速原型开发：通过 No-code 构建器快速验证 AI 应用 idea，无需编码即可创建自定义智能体



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,838 |
| 语言 | TypeScript |
| Forks | 14,694 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个颠覆性的 AI 智能体协作平台，重新定义了人机协作方式。它不仅仅是工具，更是一个生态系统，让多智能体协作变得前所未有的简单和高效，在 72k+ Stars 的验证下，已成为 AI Agent 领域的事实标准平台之一。

**技术亮点**:
- 多智能体协作系统：支持多个 Agent 同时协作，实现复杂任务的分工与配合
- 可视化 Agent 团队设计器：零代码拖拽式构建 Agent 团队，降低技术门槛
- 全模型生态支持：无缝集成 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型
- MCP（Model Context Protocol）集成：提供标准化知识库连接能力
- TypeScript 全栈开发：类型安全的代码架构，确保企业级应用稳定性

**适用场景**:
- 企业级 AI 助手团队：构建客服、销售、技术支持等多角色 AI 团队，提供 24/7 智能服务
- 个人知识管理助手：搭建个人 Agent 生态，实现笔记整理、信息检索、内容创作等自动化工作流
- 开发者工具链集成：为开发团队构建代码审查、文档生成、问题排查等智能辅助系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,971 |
| 语言 | MDX |
| Forks | 7,555 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程开源指南（71k+ Stars），由AI社区组织Dair.AI维护，系统性地涵盖了从基础的Prompt Engineering到前沿的RAG和AI Agents技术的完整知识体系。该项目不仅提供了理论知识，还包含实践案例、论文资源和学习路径，是开发者快速掌握大模型应用开发技术的权威入门指南。

**技术亮点**:
- 📚 知识体系全面：覆盖提示工程、上下文工程、RAG检索增强生成、AI智能体等核心技术领域
- 🎓 多维度学习资源：包含指南文档、学术论文、互动课程、Jupyter笔记本等多种形式的学习材料
- 🚀 紧跟技术前沿：涵盖ChatGPT、OpenAI、LLMs、生成式AI等最新技术栈和工具
- 💡 实践导向：提供可运行的notebooks和案例代码，帮助开发者快速上手实践
- 🔄 持续更新维护：由专业AI组织Dair.AI维护，紧跟大模型技术发展动态

**适用场景**:
- 🏢 企业开发者：快速掌握RAG和AI Agents技术，构建企业级智能应用和知识库系统
- 👨‍💻 个人学习者：系统性学习提示工程方法论，提升与大模型交互的效率和效果
- 🎓 研究人员：获取相关领域最新论文和技术趋势，进行学术研究和技术探索



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,304 |
| 语言 | Java |
| Forks | 15,825 |
| Issues | 54 |
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
| Stars | 32,721 |
| 语言 | Python |
| Forks | 1,983 |
| Issues | 88 |
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
| Stars | 31,998 |
| 语言 | TypeScript |
| Forks | 2,180 |
| Issues | 62 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,605 |
| 语言 | Python |
| Forks | 6,116 |
| Issues | 191 |
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
| Stars | 30,927 |
| 语言 | Jupyter Notebook |
| Forks | 5,040 |
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
| Stars | 98,611 |
| 语言 | Python |
| Forks | 14,350 |
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
| Stars | 98,353 |
| 语言 | TypeScript |
| Forks | 11,673 |
| Issues | 1,007 |
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
| Stars | 49,448 |
| 语言 | TypeScript |
| Forks | 23,764 |
| Issues | 779 |
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
| Stars | 71,394 |
| 语言 | Python |
| Forks | 9,877 |
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
| Stars | 43,059 |
| 语言 | Go |
| Forks | 3,860 |
| Issues | 1,027 |
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
| Stars | 31,153 |
| 语言 | Python |
| Forks | 3,280 |
| Issues | 64 |
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
| Stars | 29,159 |
| 语言 | TypeScript |
| Forks | 3,084 |
| Issues | 234 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
| 许可证 | MIT License |


## 💬 LLM 界面 (26 个项目)


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 125,325 |
| 语言 | Python |
| Forks | 17,750 |
| Issues | 256 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 交互界面项目，拥有 12.5 万+ Stars 的高人气，支持 Ollama、OpenAI API 等多种大模型后端，并提供 RAG、MCP 等企业级功能。它是目前最成熟的 LLM Web UI 解决方案之一，既适合个人开发者快速搭建 AI 应用，也适合企业构建私有化 AI 平台。

**技术亮点**:
- 🔌 多后端支持：统一集成 Ollama、OpenAI API、MCP (Model Context Protocol) 等多种大模型接口
- 🔍 内置 RAG 能力：支持检索增强生成，可直接对接本地知识库实现智能问答
- 🏠 完全自托管：可私有化部署，数据完全可控，适合对数据安全要求高的场景
- 🎨 现代化 Web UI：提供类似 ChatGPT 的友好交互界面，支持多会话管理
- ⚙️ Python 技术栈：基于 Python 构建，易于二次开发和扩展定制

**适用场景**:
- 🏢 企业私有化 AI 平台：搭建企业内部 LLM 服务，保护敏感数据不外泄，支持接入本地部署的开源模型（如通过 Ollama）
- 👨‍💻 个人开发者 AI 工具集：快速构建个人 AI 助手、知识库问答系统，支持多种模型切换对比
- 🎓 教育与研究场景：为学生或研究人员提供统一的 LLM 实验环境，便于教学演示和模型效果对比



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,960 |
| 语言 | Python |
| Forks | 8,224 |
| Issues | 3,013 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一个领先的开源 RAG 引擎，它将检索增强生成技术与 Agent 能力创新性融合，为大语言模型构建了卓越的上下文层。该项目在 GitHub 上获得了超过 7.3 万颗星，具备强大的文档解析、知识图谱集成和深度研究能力，是企业构建 AI 应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 技术，提供智能化的检索增强生成能力
- 支持 GraphRAG 知识图谱检索，实现更精准的语义理解和上下文关联
- 内置强大的文档解析器，支持复杂文档的深度理解和结构化提取
- 集成主流 LLM 生态（OpenAI、DeepSeek、Ollama 等），提供灵活的模型接入能力
- 支持 MCP (Model Context Protocol) 和深度研究工作流，构建端到端的 AI 解决方案

**适用场景**:
- 企业级知识管理系统：构建基于企业文档的智能问答和知识检索平台
- 智能客服与助手：结合文档理解和 Agent 能力，打造能处理复杂任务的 AI 助手
- 深度研究与分析系统：利用 GraphRAG 和深度研究能力，进行跨文档的知识发现和关联分析



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,957 |
| 语言 | JavaScript |
| Forks | 6,876 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为Claude Code、Codex等AI Agent设计的综合性能优化系统，集成了技能管理、记忆机制、安全防护和研究驱动开发等多个核心模块。作为获得5.5万+星标的热门项目，它为开发者提供了构建高效、安全AI助手的完整解决方案，显著提升AI编程助手的生产力和智能化水平。

**技术亮点**:
- ⚡ 多维度性能优化系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）等核心能力模块
- 🔒 企业级安全机制：内置安全防护体系，确保AI Agent在生产环境中的安全可控运行
- 🧠 研究驱动开发（Research-first）：采用前沿研究方法持续优化Agent性能和智能水平
- 🔌 MCP协议支持：兼容Model Context Protocol，实现与其他工具和服务的无缝集成
- 🛠️ 多平台兼容：支持Claude Code、Codex、Cowork等多种AI编程平台

**适用场景**:
- 🏢 企业级AI辅助开发：为开发团队提供增强版的Claude Code，提升代码编写、调试和项目开发效率
- 👨‍💻 个人开发者生产力工具：个人开发者可利用该系统构建定制化的AI编程助手，优化日常开发工作流
- 🔬 AI Agent研究与实验：研究者和AI工程师可基于此框架进行Agent性能优化实验和新特性开发



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,237 |
| 语言 | JavaScript |
| Forks | 5,968 |
| Issues | 302 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款集成了 RAG、AI Agents、No-code 构建器和 MCP 兼容性的全栈 AI 应用平台，支持本地和云端 LLM 部署。其独特价值在于提供开箱即用的企业级 AI 能力，同时保持开源和高度可定制，适合快速构建生产级 AI 应用。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库和网页抓取，实现智能文档问答
- 支持多种 LLM 后端：Ollama、LM Studio、LocalAI、DeepSeek、Kimi、Llama3、Qwen3 等，灵活切换模型
- No-code Agent 构建器 + MCP (Model Context Protocol) 兼容，轻松创建自定义 AI 智能体和集成外部工具
- 支持多模态 AI 能力，可处理文本、图像等多种媒体类型的输入输出
- 提供 Desktop 和 Docker 双部署方式，满足个人开发者和企业级部署需求

**适用场景**:
- 企业知识库搭建：利用 RAG 技术构建内部文档问答系统，员工可快速检索和查询公司知识
- 个人开发者 AI 助手：本地部署私有 AI Agent，集成代码生成、数据分析、自动化工作流等能力
- AI 产品快速原型开发：通过 No-code 构建器快速验证 AI 应用 idea，无需编码即可创建自定义智能体



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,838 |
| 语言 | TypeScript |
| Forks | 14,694 |
| Issues | 822 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个颠覆性的 AI 智能体协作平台，重新定义了人机协作方式。它不仅仅是工具，更是一个生态系统，让多智能体协作变得前所未有的简单和高效，在 72k+ Stars 的验证下，已成为 AI Agent 领域的事实标准平台之一。

**技术亮点**:
- 多智能体协作系统：支持多个 Agent 同时协作，实现复杂任务的分工与配合
- 可视化 Agent 团队设计器：零代码拖拽式构建 Agent 团队，降低技术门槛
- 全模型生态支持：无缝集成 ChatGPT、Claude、Gemini、DeepSeek 等主流 AI 模型
- MCP（Model Context Protocol）集成：提供标准化知识库连接能力
- TypeScript 全栈开发：类型安全的代码架构，确保企业级应用稳定性

**适用场景**:
- 企业级 AI 助手团队：构建客服、销售、技术支持等多角色 AI 团队，提供 24/7 智能服务
- 个人知识管理助手：搭建个人 Agent 生态，实现笔记整理、信息检索、内容创作等自动化工作流
- 开发者工具链集成：为开发团队构建代码审查、文档生成、问题排查等智能辅助系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,971 |
| 语言 | MDX |
| Forks | 7,555 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程开源指南（71k+ Stars），由AI社区组织Dair.AI维护，系统性地涵盖了从基础的Prompt Engineering到前沿的RAG和AI Agents技术的完整知识体系。该项目不仅提供了理论知识，还包含实践案例、论文资源和学习路径，是开发者快速掌握大模型应用开发技术的权威入门指南。

**技术亮点**:
- 📚 知识体系全面：覆盖提示工程、上下文工程、RAG检索增强生成、AI智能体等核心技术领域
- 🎓 多维度学习资源：包含指南文档、学术论文、互动课程、Jupyter笔记本等多种形式的学习材料
- 🚀 紧跟技术前沿：涵盖ChatGPT、OpenAI、LLMs、生成式AI等最新技术栈和工具
- 💡 实践导向：提供可运行的notebooks和案例代码，帮助开发者快速上手实践
- 🔄 持续更新维护：由专业AI组织Dair.AI维护，紧跟大模型技术发展动态

**适用场景**:
- 🏢 企业开发者：快速掌握RAG和AI Agents技术，构建企业级智能应用和知识库系统
- 👨‍💻 个人学习者：系统性学习提示工程方法论，提升与大模型交互的效率和效果
- 🎓 研究人员：获取相关领域最新论文和技术趋势，进行学术研究和技术探索



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,474 |
| 语言 | HTML |
| Forks | 19,651 |
| Issues | 18 |
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
| Stars | 86,562 |
| 语言 | Jupyter Notebook |
| Forks | 13,142 |
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
| Stars | 41,675 |
| 语言 | Python |
| Forks | 9,781 |
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
| Stars | 34,227 |
| 语言 | TypeScript |
| Forks | 6,913 |
| Issues | 423 |
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
| Stars | 32,721 |
| 语言 | Python |
| Forks | 1,983 |
| Issues | 88 |
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
| Stars | 31,998 |
| 语言 | TypeScript |
| Forks | 2,180 |
| Issues | 62 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### labring/FastGPT

**描述**: FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 27,217 |
| 语言 | TypeScript |
| Forks | 6,939 |
| Issues | 158 |
| Topics | agent, claude, deepseek, llm, mcp, nextjs, openai, qwen, rag, workflow |
| 许可证 | Other |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,366 |
| 语言 | Python |
| Forks | 8,529 |
| Issues | 360 |
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
| Stars | 35,779 |
| 语言 | TypeScript |
| Forks | 2,710 |
| Issues | 277 |
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
| Stars | 49,448 |
| 语言 | TypeScript |
| Forks | 23,764 |
| Issues | 779 |
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
| Stars | 33,373 |
| 语言 | HTML |
| Forks | 5,302 |
| Issues | 31 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,579 |
| 语言 | Python |
| Forks | 13,817 |
| Issues | 3,505 |
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
| Stars | 35,878 |
| 语言 | Python |
| Forks | 3,517 |
| Issues | 60 |
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
| Stars | 145,172 |
| 语言 | Python |
| Forks | 8,499 |
| Issues | 1,073 |
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
| Stars | 163,771 |
| 语言 | Go |
| Forks | 14,717 |
| Issues | 2,529 |
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
| Stars | 46,033 |
| 语言 | Rust |
| Forks | 9,044 |
| Issues | 0 |
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
| Stars | 29,841 |
| 语言 | Python |
| Forks | 3,268 |
| Issues | 6 |
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
| Stars | 38,712 |
| 语言 | TypeScript |
| Forks | 3,914 |
| Issues | 1,054 |
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
| Stars | 39,130 |
| 语言 | Python |
| Forks | 3,882 |
| Issues | 229 |
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
| Stars | 88,873 |
| 语言 | Python |
| Forks | 5,213 |
| Issues | 436 |
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
| Stars | 70,971 |
| 语言 | MDX |
| Forks | 7,555 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程开源指南（71k+ Stars），由AI社区组织Dair.AI维护，系统性地涵盖了从基础的Prompt Engineering到前沿的RAG和AI Agents技术的完整知识体系。该项目不仅提供了理论知识，还包含实践案例、论文资源和学习路径，是开发者快速掌握大模型应用开发技术的权威入门指南。

**技术亮点**:
- 📚 知识体系全面：覆盖提示工程、上下文工程、RAG检索增强生成、AI智能体等核心技术领域
- 🎓 多维度学习资源：包含指南文档、学术论文、互动课程、Jupyter笔记本等多种形式的学习材料
- 🚀 紧跟技术前沿：涵盖ChatGPT、OpenAI、LLMs、生成式AI等最新技术栈和工具
- 💡 实践导向：提供可运行的notebooks和案例代码，帮助开发者快速上手实践
- 🔄 持续更新维护：由专业AI组织Dair.AI维护，紧跟大模型技术发展动态

**适用场景**:
- 🏢 企业开发者：快速掌握RAG和AI Agents技术，构建企业级智能应用和知识库系统
- 👨‍💻 个人学习者：系统性学习提示工程方法论，提升与大模型交互的效率和效果
- 🎓 研究人员：获取相关领域最新论文和技术趋势，进行学术研究和技术探索



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,702 |
| 语言 | Python |
| Forks | 8,257 |
| Issues | 909 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个业界领先的大模型微调统一框架，以ACL 2024学术认可为基础，提供从训练到部署的一站式解决方案。其最大价值在于将复杂的LLM微调过程标准化、可视化，降低了企业和个人开发者使用LoRA、QLoRA、RLHF等先进技术的门槛，支持100+主流模型（包括DeepSeek、Qwen、Gemma、Llama3等），在GitHub获得6.7万+星标，是当前最活跃和实用的微调工具之一。

**技术亮点**:
- 支持100+种大语言模型和视觉语言模型，覆盖LLaMA系列、Qwen、DeepSeek、Gemma、GPT等主流开源模型
- 提供多种高效微调方法：LoRA、QLoRA、量化训练、MoE（混合专家）和RLHF（人类反馈强化学习）
- 集成GUI可视化界面和命令行工具，支持指令微调、Agent训练等多种训练范式
- 基于Transformers和PEFT构建，提供从数据预处理、模型训练到评估导出的完整工作流
- 开源友好（Apache 2.0许可），持续更新紧跟最新模型和技术发展

**适用场景**:
- 企业级场景：快速微调行业专用大模型，如金融、医疗、法律等垂直领域的知识增强和指令对齐
- 个人开发者/研究人员：低成本进行模型实验和研究，使用LoRA/QLoRA在消费级显卡上完成大模型微调
- AI应用开发：构建智能Agent系统，通过指令微调和RLHF优化模型的交互能力和任务执行能力



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,363 |
| 语言 | Python |
| Forks | 6,082 |
| Issues | 65 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是金融数据领域的"瑞士军刀"，为分析师、量化交易者和 AI 智能体提供统一的数据访问平台。凭借 62,000+ GitHub Stars 和覆盖股票、加密货币、固定收益等全品类金融数据的 Python 开源工具，它打破了传统金融数据的高昂壁垒，让金融数据访问变得民主化、标准化和程序化。

**技术亮点**:
- 全栈金融数据覆盖：整合股票、期权、衍生品、加密货币、固定收益、宏观经济等跨资产类别数据源
- Python 优先架构：提供简洁的 Python API，无缝集成数据科学栈（Pandas、NumPy、机器学习框架）
- AI 原生设计：专为 AI 智能体和机器学习模型优化，支持自动化量化交易策略开发
- 开源与可扩展性：基于 MIT 等宽松许可证，支持自定义数据源接入和插件化扩展
- 量化分析工具箱：内置技术指标计算、回测框架、数据可视化等专业金融工程功能

**适用场景**:
- 量化交易策略研发：个人开发者或量化团队可快速获取多资产历史数据，构建和回测交易策略
- 金融 AI 应用开发：为金融科技公司和 AI 创业者提供标准化数据接口，训练预测模型和开发智能投顾系统
- 投资研究与分析：分析师可用该平台进行跨市场资产分析、风险评估和报告自动化生成



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,474 |
| 语言 | HTML |
| Forks | 19,651 |
| Issues | 18 |
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
| Stars | 86,562 |
| 语言 | Jupyter Notebook |
| Forks | 13,142 |
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
| Stars | 30,927 |
| 语言 | Jupyter Notebook |
| Forks | 5,040 |
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
| Stars | 157,177 |
| 语言 | Python |
| Forks | 32,251 |
| Issues | 2,309 |
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
| Stars | 71,579 |
| 语言 | Python |
| Forks | 13,817 |
| Issues | 3,505 |
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
| Stars | 161,411 |
| 语言 | Python |
| Forks | 30,094 |
| Issues | 2,462 |
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
| Stars | 104,578 |
| 语言 | Python |
| Forks | 11,970 |
| Issues | 3,781 |
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
| Stars | 97,858 |
| 语言 | Python |
| Forks | 27,025 |
| Issues | 18,052 |
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
| Stars | 29,159 |
| 语言 | TypeScript |
| Forks | 3,084 |
| Issues | 234 |
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
| Stars | 75,892 |
| 语言 | Unknown |
| Forks | 8,753 |
| Issues | 76 |
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
| Stars | 55,957 |
| 语言 | JavaScript |
| Forks | 6,876 |
| Issues | 23 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为Claude Code、Codex等AI Agent设计的综合性能优化系统，集成了技能管理、记忆机制、安全防护和研究驱动开发等多个核心模块。作为获得5.5万+星标的热门项目，它为开发者提供了构建高效、安全AI助手的完整解决方案，显著提升AI编程助手的生产力和智能化水平。

**技术亮点**:
- ⚡ 多维度性能优化系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）等核心能力模块
- 🔒 企业级安全机制：内置安全防护体系，确保AI Agent在生产环境中的安全可控运行
- 🧠 研究驱动开发（Research-first）：采用前沿研究方法持续优化Agent性能和智能水平
- 🔌 MCP协议支持：兼容Model Context Protocol，实现与其他工具和服务的无缝集成
- 🛠️ 多平台兼容：支持Claude Code、Codex、Cowork等多种AI编程平台

**适用场景**:
- 🏢 企业级AI辅助开发：为开发团队提供增强版的Claude Code，提升代码编写、调试和项目开发效率
- 👨‍💻 个人开发者生产力工具：个人开发者可利用该系统构建定制化的AI编程助手，优化日常开发工作流
- 🔬 AI Agent研究与实验：研究者和AI工程师可基于此框架进行Agent性能优化实验和新特性开发



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,167 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 153 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 模型部署平台，作为 OpenAI、Claude 等商业 API 的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行。其独特的价值在于提供了"开箱即用"的 drop-in 替换能力，同时支持文本、图像、音频、视频等多种 AI 生成任务，并集成了分布式推理、P2P 网络和 MCP 协议等前沿特性，是企业与个人开发者构建私有化 AI 服务的理想选择。

**技术亮点**:
- 🤖 多模型引擎支持：兼容 gguf、transformers、diffusers 等多种模型格式，支持 LLaMA、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流模型
- 💻 零 GPU 依赖设计：完全优化的 CPU 推理能力，可在消费级硬件上高效运行，大幅降低部署成本
- 🌐 分布式与 P2P 架构：基于 libp2p 实现去中心化推理网络，支持分布式计算资源调度，提升大规模推理效率
- 🎯 OpenAI API 兼容：提供 drop-in 替换能力，无需修改现有代码即可迁移至私有化部署
- 🎨 全模态 AI 能力：支持文本生成、图像生成、音频生成（TTS、MusicGen、Voice Cloning）、视频生成、目标检测等多种 AI 任务

**适用场景**:
- 🏢 企业私有化 AI 部署：金融、医疗、政府等对数据安全敏感的行业，可在内网部署完整的 AI 服务，避免数据外泄风险，同时大幅降低 API 调用成本
- 👨‍💻 个人开发者 AI 应用开发：开发者可在本地快速搭建 AI 开发测试环境，无需依赖云端 API，支持离线开发和调试
- 🌍 边缘计算与离线场景：适用于无网络或弱网络环境下的 AI 应用，如离线智能助手、本地语音交互系统等



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,366 |
| 语言 | Python |
| Forks | 8,529 |
| Issues | 360 |
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
| Stars | 35,779 |
| 语言 | TypeScript |
| Forks | 2,710 |
| Issues | 277 |
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
| Stars | 177,007 |
| 语言 | TypeScript |
| Forks | 55,302 |
| Issues | 1,416 |
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
| Stars | 149,135 |
| 语言 | Python |
| Forks | 12,087 |
| Issues | 2,339 |
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
| Stars | 95,725 |
| 语言 | Python |
| Forks | 8,766 |
| Issues | 154 |
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
| Stars | 73,264 |
| 语言 | Python |
| Forks | 8,686 |
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
| Stars | 182,183 |
| 语言 | TypeScript |
| Forks | 38,226 |
| Issues | 14,431 |
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
| Stars | 93,682 |
| 语言 | TypeScript |
| Forks | 9,378 |
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
| Stars | 77,961 |
| 语言 | TypeScript |
| Forks | 5,603 |
| Issues | 661 |
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
| Stars | 76,423 |
| 语言 | TypeScript |
| Forks | 6,530 |
| Issues | 189 |
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
| Stars | 75,629 |
| 语言 | JavaScript |
| Forks | 7,268 |
| Issues | 705 |
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
| Stars | 78,237 |
| 语言 | Go |
| Forks | 2,698 |
| Issues | 320 |
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
| Stars | 73,269 |
| 语言 | Go |
| Forks | 2,549 |
| Issues | 908 |
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
| Stars | 42,827 |
| 语言 | Go |
| Forks | 8,002 |
| Issues | 974 |
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
| Stars | 401,820 |
| 语言 | Python |
| Forks | 43,079 |
| Issues | 897 |
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
| Stars | 35,779 |
| 语言 | TypeScript |
| Forks | 2,710 |
| Issues | 277 |
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
| Stars | 177,007 |
| 语言 | TypeScript |
| Forks | 55,302 |
| Issues | 1,416 |
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
| Stars | 51,587 |
| 语言 | Go |
| Forks | 10,327 |
| Issues | 218 |
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
| Stars | 120,847 |
| 语言 | Go |
| Forks | 42,565 |
| Issues | 2,673 |
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
| Stars | 71,457 |
| 语言 | Go |
| Forks | 18,911 |
| Issues | 3,792 |
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
| Stars | 53,986 |
| 语言 | Go |
| Forks | 6,415 |
| Issues | 2,834 |
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
| Stars | 47,540 |
| 语言 | Go |
| Forks | 5,066 |
| Issues | 964 |
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
| Stars | 29,841 |
| 语言 | Python |
| Forks | 3,268 |
| Issues | 6 |
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
| Stars | 93,682 |
| 语言 | TypeScript |
| Forks | 9,378 |
| Issues | 293 |
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
| Stars | 83,259 |
| 语言 | TypeScript |
| Forks | 5,211 |
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
| Stars | 74,703 |
| 语言 | TypeScript |
| Forks | 6,335 |
| Issues | 417 |
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
| Stars | 83,420 |
| 语言 | JavaScript |
| Forks | 7,459 |
| Issues | 697 |
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
| Stars | 69,077 |
| 语言 | Go |
| Forks | 1,863 |
| Issues | 289 |
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
| Stars | 61,990 |
| 语言 | Go |
| Forks | 5,850 |
| Issues | 773 |
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
| Stars | 57,381 |
| 语言 | Go |
| Forks | 4,146 |
| Issues | 42 |
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
| Stars | 39,130 |
| 语言 | Python |
| Forks | 3,882 |
| Issues | 229 |
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
| Stars | 60,401 |
| 语言 | Go |
| Forks | 7,155 |
| Issues | 79 |
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
| Stars | 83,420 |
| 语言 | JavaScript |
| Forks | 7,459 |
| Issues | 697 |
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
| Stars | 62,982 |
| 语言 | Go |
| Forks | 10,208 |
| Issues | 759 |
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
| Stars | 43,167 |
| 语言 | Go |
| Forks | 3,608 |
| Issues | 153 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 模型部署平台，作为 OpenAI、Claude 等商业 API 的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行。其独特的价值在于提供了"开箱即用"的 drop-in 替换能力，同时支持文本、图像、音频、视频等多种 AI 生成任务，并集成了分布式推理、P2P 网络和 MCP 协议等前沿特性，是企业与个人开发者构建私有化 AI 服务的理想选择。

**技术亮点**:
- 🤖 多模型引擎支持：兼容 gguf、transformers、diffusers 等多种模型格式，支持 LLaMA、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流模型
- 💻 零 GPU 依赖设计：完全优化的 CPU 推理能力，可在消费级硬件上高效运行，大幅降低部署成本
- 🌐 分布式与 P2P 架构：基于 libp2p 实现去中心化推理网络，支持分布式计算资源调度，提升大规模推理效率
- 🎯 OpenAI API 兼容：提供 drop-in 替换能力，无需修改现有代码即可迁移至私有化部署
- 🎨 全模态 AI 能力：支持文本生成、图像生成、音频生成（TTS、MusicGen、Voice Cloning）、视频生成、目标检测等多种 AI 任务

**适用场景**:
- 🏢 企业私有化 AI 部署：金融、医疗、政府等对数据安全敏感的行业，可在内网部署完整的 AI 服务，避免数据外泄风险，同时大幅降低 API 调用成本
- 👨‍💻 个人开发者 AI 应用开发：开发者可在本地快速搭建 AI 开发测试环境，无需依赖云端 API，支持离线开发和调试
- 🌍 边缘计算与离线场景：适用于无网络或弱网络环境下的 AI 应用，如离线智能助手、本地语音交互系统等



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,725 |
| 语言 | Python |
| Forks | 8,766 |
| Issues | 154 |
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
| Stars | 86,951 |
| 语言 | Python |
| Forks | 33,706 |
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
| Stars | 100,035 |
| 语言 | TypeScript |
| Forks | 27,095 |
| Issues | 1,120 |
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
| Stars | 77,961 |
| 语言 | TypeScript |
| Forks | 5,603 |
| Issues | 661 |
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
| Stars | 74,814 |
| 语言 | TypeScript |
| Forks | 8,232 |
| Issues | 51 |
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
| Stars | 75,629 |
| 语言 | JavaScript |
| Forks | 7,268 |
| Issues | 705 |
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
| Stars | 68,838 |
| 语言 | JavaScript |
| Forks | 22,683 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,224 |
| Issues | 346 |
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
| Stars | 88,166 |
| 语言 | Go |
| Forks | 8,559 |
| Issues | 640 |
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
| Stars | 70,485 |
| 语言 | Go |
| Forks | 4,654 |
| Issues | 257 |
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
| Stars | 56,475 |
| 语言 | Go |
| Forks | 3,155 |
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
| Stars | 401,820 |
| 语言 | Python |
| Forks | 43,079 |
| Issues | 897 |
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
| Stars | 55,237 |
| 语言 | JavaScript |
| Forks | 5,968 |
| Issues | 302 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一款集成了 RAG、AI Agents、No-code 构建器和 MCP 兼容性的全栈 AI 应用平台，支持本地和云端 LLM 部署。其独特价值在于提供开箱即用的企业级 AI 能力，同时保持开源和高度可定制，适合快速构建生产级 AI 应用。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库和网页抓取，实现智能文档问答
- 支持多种 LLM 后端：Ollama、LM Studio、LocalAI、DeepSeek、Kimi、Llama3、Qwen3 等，灵活切换模型
- No-code Agent 构建器 + MCP (Model Context Protocol) 兼容，轻松创建自定义 AI 智能体和集成外部工具
- 支持多模态 AI 能力，可处理文本、图像等多种媒体类型的输入输出
- 提供 Desktop 和 Docker 双部署方式，满足个人开发者和企业级部署需求

**适用场景**:
- 企业知识库搭建：利用 RAG 技术构建内部文档问答系统，员工可快速检索和查询公司知识
- 个人开发者 AI 助手：本地部署私有 AI Agent，集成代码生成、数据分析、自动化工作流等能力
- AI 产品快速原型开发：通过 No-code 构建器快速验证 AI 应用 idea，无需编码即可创建自定义智能体



### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,353 |
| 语言 | TypeScript |
| Forks | 11,673 |
| Issues | 1,007 |
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
| Stars | 43,059 |
| 语言 | Go |
| Forks | 3,860 |
| Issues | 1,027 |
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
| Stars | 51,587 |
| 语言 | Go |
| Forks | 10,327 |
| Issues | 218 |
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
| Stars | 70,971 |
| 语言 | MDX |
| Forks | 7,555 |
| Issues | 244 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前GitHub上最受欢迎的提示工程开源指南（71k+ Stars），由AI社区组织Dair.AI维护，系统性地涵盖了从基础的Prompt Engineering到前沿的RAG和AI Agents技术的完整知识体系。该项目不仅提供了理论知识，还包含实践案例、论文资源和学习路径，是开发者快速掌握大模型应用开发技术的权威入门指南。

**技术亮点**:
- 📚 知识体系全面：覆盖提示工程、上下文工程、RAG检索增强生成、AI智能体等核心技术领域
- 🎓 多维度学习资源：包含指南文档、学术论文、互动课程、Jupyter笔记本等多种形式的学习材料
- 🚀 紧跟技术前沿：涵盖ChatGPT、OpenAI、LLMs、生成式AI等最新技术栈和工具
- 💡 实践导向：提供可运行的notebooks和案例代码，帮助开发者快速上手实践
- 🔄 持续更新维护：由专业AI组织Dair.AI维护，紧跟大模型技术发展动态

**适用场景**:
- 🏢 企业开发者：快速掌握RAG和AI Agents技术，构建企业级智能应用和知识库系统
- 👨‍💻 个人学习者：系统性学习提示工程方法论，提升与大模型交互的效率和效果
- 🎓 研究人员：获取相关领域最新论文和技术趋势，进行学术研究和技术探索



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,474 |
| 语言 | HTML |
| Forks | 19,651 |
| Issues | 18 |
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
| Stars | 33,373 |
| 语言 | HTML |
| Forks | 5,302 |
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
| Stars | 89,340 |
| 语言 | TypeScript |
| Forks | 9,876 |
| Issues | 2,236 |
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
| Stars | 86,369 |
| 语言 | TypeScript |
| Forks | 8,667 |
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
| Stars | 126,907 |
| 语言 | JavaScript |
| Forks | 12,443 |
| Issues | 2 |
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
| Stars | 99,401 |
| 语言 | JavaScript |
| Forks | 7,441 |
| Issues | 195 |
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
| Stars | 166,299 |
| 语言 | Go |
| Forks | 12,996 |
| Issues | 172 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (63 个项目)


### 🌟 高优先级


### CherryHQ/cherry-studio

**描述**: AI productivity studio with smart chat, autonomous agents, and 300+ assistants. Unified access to frontier LLMs

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,457 |
| 语言 | TypeScript |
| Forks | 3,734 |
| Issues | 661 |
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
| Stars | 242,693 |
| 语言 | TypeScript |
| Forks | 46,929 |
| Issues | 9,936 |
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
| Stars | 61,189 |
| 语言 | Python |
| Forks | 6,256 |
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
| Stars | 79,731 |
| 语言 | Python |
| Forks | 11,624 |
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
| Stars | 72,986 |
| 语言 | Python |
| Forks | 6,263 |
| Issues | 631 |
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
| Stars | 126,788 |
| 语言 | Unknown |
| Forks | 32,457 |
| Issues | 134 |
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
| Stars | 383,448 |
| 语言 | Python |
| Forks | 65,992 |
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
| Stars | 112,267 |
| 语言 | TypeScript |
| Forks | 5,655 |
| Issues | 373 |
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
| Stars | 99,640 |
| 语言 | TypeScript |
| Forks | 7,262 |
| Issues | 167 |
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
| Stars | 47,843 |
| 语言 | Go |
| Forks | 10,229 |
| Issues | 1,909 |
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
| Stars | 96,235 |
| 语言 | C++ |
| Forks | 15,145 |
| Issues | 1,159 |
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
| Stars | 59,552 |
| 语言 | Python |
| Forks | 1,609 |
| Issues | 33 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 285,082 |
| 语言 | Python |
| Forks | 27,263 |
| Issues | 21 |
| Topics | awesome, collections, python, python-framework, python-library, python-resources |
| 许可证 | Other |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,073 |
| 语言 | Python |
| Forks | 36,881 |
| Issues | 3,450 |
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
| Stars | 77,691 |
| 语言 | Python |
| Forks | 45,268 |
| Issues | 1,278 |
| 许可证 | Other |


### python/cpython

**描述**: The Python programming language

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,763 |
| 语言 | Python |
| Forks | 34,148 |
| Issues | 9,309 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 437,637 |
| 语言 | TypeScript |
| Forks | 43,488 |
| Issues | 322 |
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
| Stars | 349,938 |
| 语言 | TypeScript |
| Forks | 43,717 |
| Issues | 40 |
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
| Stars | 117,755 |
| 语言 | TypeScript |
| Forks | 12,696 |
| Issues | 2,830 |
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
| Stars | 107,982 |
| 语言 | TypeScript |
| Forks | 13,241 |
| Issues | 5,477 |
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
| Stars | 107,517 |
| 语言 | TypeScript |
| Forks | 7,980 |
| Issues | 1,775 |
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
| Stars | 97,639 |
| 语言 | TypeScript |
| Forks | 54,528 |
| Issues | 1,373 |
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
| Stars | 93,850 |
| 语言 | TypeScript |
| Forks | 5,090 |
| Issues | 79 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,795 |
| 语言 | TypeScript |
| Forks | 4,988 |
| Issues | 692 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,890 |
| 语言 | TypeScript |
| Forks | 7,565 |
| Issues | 42 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,773 |
| 语言 | TypeScript |
| Forks | 9,708 |
| Issues | 400 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,506 |
| 语言 | TypeScript |
| Forks | 7,862 |
| Issues | 631 |
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
| Stars | 243,394 |
| 语言 | JavaScript |
| Forks | 50,618 |
| Issues | 1,144 |
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
| Stars | 148,088 |
| 语言 | JavaScript |
| Forks | 26,762 |
| Issues | 186 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### vercel/next.js

**描述**: The React Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,071 |
| 语言 | JavaScript |
| Forks | 30,519 |
| Issues | 3,412 |
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
| Stars | 116,011 |
| 语言 | JavaScript |
| Forks | 34,893 |
| Issues | 2,512 |
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
| Stars | 111,128 |
| 语言 | JavaScript |
| Forks | 36,283 |
| Issues | 607 |
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
| Stars | 108,576 |
| 语言 | JavaScript |
| Forks | 11,539 |
| Issues | 342 |
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
| Stars | 97,983 |
| 语言 | JavaScript |
| Forks | 32,721 |
| Issues | 1,730 |
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
| Stars | 95,360 |
| 语言 | JavaScript |
| Forks | 15,182 |
| Issues | 65 |
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
| Stars | 85,939 |
| 语言 | JavaScript |
| Forks | 4,784 |
| Issues | 970 |
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
| Stars | 78,569 |
| 语言 | JavaScript |
| Forks | 31,107 |
| Issues | 269 |
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
| Stars | 70,653 |
| 语言 | JavaScript |
| Forks | 16,799 |
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
| Stars | 67,201 |
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
| Stars | 66,265 |
| 语言 | JavaScript |
| Forks | 9,185 |
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
| Stars | 66,012 |
| 语言 | JavaScript |
| Forks | 9,287 |
| Issues | 211 |
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
| Stars | 61,842 |
| 语言 | JavaScript |
| Forks | 3,959 |
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
| Stars | 61,571 |
| 语言 | JavaScript |
| Forks | 7,126 |
| Issues | 116 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


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
| Forks | 20,478 |
| Issues | 99 |
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
| Stars | 59,602 |
| 语言 | JavaScript |
| Forks | 5,594 |
| Issues | 62 |
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
| Stars | 57,394 |
| 语言 | JavaScript |
| Forks | 12,312 |
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
| Stars | 132,815 |
| 语言 | Go |
| Forks | 18,833 |
| Issues | 9,818 |
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
| Stars | 104,779 |
| 语言 | Go |
| Forks | 14,913 |
| Issues | 38 |
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
| Stars | 86,846 |
| 语言 | Go |
| Forks | 8,198 |
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
| Stars | 80,428 |
| 语言 | Go |
| Forks | 4,947 |
| Issues | 403 |
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
| Stars | 68,720 |
| 语言 | Go |
| Forks | 3,213 |
| Issues | 15 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,798 |
| 语言 | Go |
| Forks | 4,937 |
| Issues | 1,125 |
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
| Stars | 50,875 |
| 语言 | Go |
| Forks | 21,816 |
| Issues | 380 |
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
| Stars | 49,082 |
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
| Stars | 45,127 |
| 语言 | Go |
| Forks | 3,733 |
| Issues | 99 |
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
| Stars | 144,298 |
| 语言 | Python |
| Forks | 11,141 |
| Issues | 279 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 218,243 |
| 语言 | Python |
| Forks | 50,114 |
| Issues | 920 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,753 |
| 语言 | Python |
| Forks | 10,602 |
| Issues | 4,119 |
| 许可证 | The Unlicense |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 84,918 |
| 语言 | Python |
| Forks | 7,148 |
| Issues | 473 |
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
| Stars | 75,616 |
| 语言 | Python |
| Forks | 16,695 |
| Issues | 15 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,701 |
| 语言 | JavaScript |
| Forks | 31,119 |
| Issues | 391 |
| Topics | algorithm, algorithms, computer-science, data-structures, interview, interview-preparation, javascript, javascript-algorithms |
| 许可证 | MIT License |


### FortAwesome/Font-Awesome

**描述**: The iconic SVG, font, and CSS toolkit

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,380 |
| 语言 | JavaScript |
| Forks | 12,242 |
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
| Stars | 66,686 |
| 语言 | JavaScript |
| Forks | 4,464 |
| Issues | 92 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |
