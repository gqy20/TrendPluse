# 项目发现报告 (2026-03-14)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
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
| Stars | 127,176 |
| 语言 | Python |
| Forks | 17,982 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源 AI 聊天界面之一，拥有超过 12 万 Star，核心价值在于提供了类似 ChatGPT 的完整 Web UI 体验，同时支持本地部署和私有化，让用户可以用自己的 API Key 或本地模型构建专属的 AI 助手平台，兼顾了易用性与数据隐私。

**技术亮点**:
- 多模型后端支持：无缝对接 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换不同模型
- RAG（检索增强生成）内置支持：支持上传文档并与 AI 对话，实现知识库问答功能
- MCP（Model Context Protocol）协议支持：支持 Anthropic 推出的模型上下文协议，增强 AI 与外部工具的交互能力
- 完全自托管与私有化部署：基于 Python 开发，支持 Docker 一键部署，数据完全掌握在自己手中
- 现代化 Web UI 设计：提供类似 ChatGPT 的流畅交互体验，支持多用户、对话历史、Markdown 渲染等功能

**适用场景**:
- 企业内部 AI 助手平台：搭建私有化 ChatGPT 替代方案，保护敏感数据不被外部服务获取
- 个人/团队知识库问答：结合 RAG 功能，上传文档资料构建专属智能问答系统
- 本地大模型体验前端：配合 Ollama 在本地运行开源模型，实现完全离线的 AI 对话体验
- AI 应用开发原型验证：快速搭建 LLM 应用的交互界面，用于测试和演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,994 |
| 语言 | Python |
| Forks | 8,380 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（近 7.5 万 Stars），其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供高质量的上下文层。相比传统 RAG 方案，它集成了深度文档理解、GraphRAG、MCP 协议等先进特性，是构建企业级智能知识库和 AI 搜索应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 智能工作流编排
- 深度文档理解引擎，具备强大的 Document Parser 能力，可处理复杂文档结构
- 支持 GraphRAG 图谱增强检索，提升复杂推理场景的准确性
- 兼容 OpenAI、Ollama、DeepSeek 等多种 LLM 后端，灵活适配不同模型
- 支持 MCP 协议和 Deep Research 模式，适合构建深度研究型 AI 应用

**适用场景**:
- 企业知识库构建：快速搭建基于私有文档的智能问答和知识管理系统
- AI 搜索与深度研究：构建具备深度推理能力的智能搜索和研报生成工具
- 文档理解与自动化处理：对合同、报告等复杂文档进行结构化解析和信息提取



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,969 |
| 语言 | TypeScript |
| Forks | 6,425 |
| Issues | 208 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个专为 AI 应用设计的网页数据提取 API，能将任意网站自动转换为 LLM 友好的 Markdown 或结构化数据，解决了 AI 开发中最繁琐的数据采集和清洗难题，让开发者能够快速构建基于实时网页数据的智能应用。

**技术亮点**:
- 一站式网页数据提取：支持将完整网站（多页面）自动爬取并转换为干净的 Markdown 格式，无需手动处理 HTML 解析
- LLM 原生设计：输出格式专为大型语言模型优化，可直接用于 RAG、Agent 和其他 AI 应用场景
- 智能数据结构化：支持将非结构化网页内容转换为结构化 JSON 数据，便于后续分析和处理
- AI 增强能力：集成 AI 搜索、AI 抓取和 AI 代理功能，支持智能内容提取和语义理解
- TypeScript 全栈实现：提供类型安全的 API 接口，便于与现代前端和 Node.js 生态系统集成

**适用场景**:
- RAG（检索增强生成）应用：为 AI 助手、客服机器人提供实时、准确的网页知识库数据源
- 企业数据采集与分析：自动化监控竞品网站、行业资讯、价格变动等信息，构建商业智能系统
- AI Agent 工具链：为自主智能体提供网页浏览和信息提取能力，支持复杂任务自动化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,711 |
| 语言 | JavaScript |
| Forks | 9,461 |
| Issues | 16 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为AI编程助手（如Claude Code、Cursor等）打造的综合性性能优化系统，集成了技能、直觉、记忆、安全和研究驱动开发等核心能力。该项目获得了超过7.5万Stars，证明了其在AI辅助开发领域的巨大价值和社区认可度，是目前最全面的AI Agent开发框架之一。

**技术亮点**:
- 集成Skills（技能）、Instincts（直觉）、Memory（记忆）三大AI Agent核心能力模块，实现更智能的上下文理解和任务执行
- 支持多平台兼容，涵盖Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- 内置安全机制，为AI Agent提供安全边界和防护措施
- 支持MCP协议，实现AI模型间的高效通信与工具集成
- 研究驱动开发方法论，提供结构化的开发流程和最佳实践

**适用场景**:
- 企业级AI辅助开发：团队需要统一AI编程工具的使用规范和性能优化
- 个人开发者提升AI编程效率：优化Claude Code或Cursor等工具的响应质量和准确性
- 构建自定义AI Agent：开发者需要快速搭建具备记忆、技能和安全能力的智能代理



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,602 |
| 语言 | Go |
| Forks | 3,690 |
| Issues | 142 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，最大的价值在于完全免费开源且无需 GPU 就能在消费级硬件上运行，同时提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到自托管方案，兼顾了隐私保护和成本控制。

**技术亮点**:
- OpenAI API 兼容的 Drop-in 替代方案，支持无缝迁移
- 支持多种模型格式（GGUF、Transformers、Diffusers）和模型架构（LLaMA、Mistral、RWKV、Mamba等）
- 无 GPU 依赖，可在普通消费级 CPU 硬件上高效运行
- 支持多模态生成：文本、图像、音频、视频、语音克隆等全方位 AI 能力
- 去中心化和分布式推理架构，支持 P2P 和 MCP 协议

**适用场景**:
- 企业内部 AI 服务部署：在私有环境中运行 LLM 和多模态模型，确保数据安全和隐私合规
- 个人开发者本地开发测试：零成本搭建 OpenAI 兼容的本地 AI 环境，无需付费 API 调用
- 边缘设备和嵌入式场景：在资源受限的硬件上部署 AI 能力，如树莓派或老旧服务器



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,648 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 640 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的开源 AI Agent 协作平台，以 73K+ stars 的超高人气证明了其在 AI 社区的影响力。它提供了从单 Agent 到多 Agent 协作的完整解决方案，支持多种主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等），为企业和个人打造智能化工作流提供了强大且灵活的基础设施。

**技术亮点**:
- 🤖 多智能体协作引擎：支持 Agent 之间协同工作，实现复杂任务的自动化分工与协作
- 🔌 多模型适配架构：统一接口对接 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换模型策略
- 📚 知识库集成（Knowledge Base）：支持 RAG 检索增强生成，让 Agent 具备领域知识能力
- ⚡ MCP 协议支持：集成 Model Context Protocol，实现 Agent 与外部工具/数据源的标准化交互
- 🎨 可视化 Agent 设计：提供低代码的 Agent 团队编排能力，降低多 Agent 系统的构建门槛

**适用场景**:
- 🏢 企业智能客服与助手：构建具备企业知识库的多 Agent 系统，实现客户服务、内部问答、流程自动化等场景
- 👨‍💻 开发者 Agent 工作流：个人开发者可搭建专属 AI 助手团队，协同完成代码编写、文档生成、数据分析等任务
- 🔬 研究与原型验证：快速搭建多 Agent 协作原型，验证 AI Agent 在特定业务场景的可行性与效果



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,617 |
| 语言 | MDX |
| Forks | 7,650 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71K+ Stars的提示工程领域最全面的指南资源库，系统性地覆盖了从Prompt Engineering到RAG再到AI Agents的完整技术栈，由DAIR.AI团队精心维护，是AI从业者快速掌握大语言模型应用开发的必备知识库。

**技术亮点**:
- 涵盖提示工程(Prompt Engineering)、上下文工程(Context Engineering)、检索增强生成(RAG)和AI智能体(AI Agents)的完整知识体系
- 提供Jupyter Notebook实践教程，结合理论与代码实战，便于动手学习
- MDX格式编写，支持Markdown与React组件混合，呈现丰富的交互式文档体验
- 集成最新的生成式AI论文、教程和资源，紧跟LLM领域前沿发展
- 开源MIT许可证，社区驱动持续更新，涵盖OpenAI、ChatGPT等主流模型技术

**适用场景**:
- 企业AI团队构建LLM应用时，作为提示工程和RAG技术的标准化培训教材和参考手册
- 个人开发者或研究者系统学习提示工程技术、掌握AI Agent开发最佳实践的完整学习路径
- AI产品经理和技术决策者了解LLM应用架构设计，评估Prompt Engineering和RAG方案的技术参考



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,400 |
| 语言 | Python |
| Forks | 8,350 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 收录的明星项目，以统一的 WebUI 界面一站式支持 100+ 大语言模型和视觉语言模型的高效微调，极大地降低了 LLM 定制化的技术门槛和工程成本。

**技术亮点**:
- 支持 100+ 主流大语言模型（LLaMA、Qwen、ChatGLM、DeepSeek、Gemma等）的统一微调框架，兼容性极强
- 集成了 LoRA、QLoRA、全量微调等多种高效微调方法，支持模型量化（4bit/8bit），大幅降低显存需求
- 提供完整的训练流程：支持预训练、指令微调、RLHF（人类反馈强化学习）全链路
- 内置 WebUI 可视化界面，无需代码即可完成模型微调和推理部署
- 支持 MoE（混合专家）架构和 Agent 应用开发，紧跟前沿技术趋势

**适用场景**:
- 企业级私有化大模型定制：在垂直领域数据上微调专属模型，如金融、医疗、法律等行业应用
- 个人开发者快速实验：低成本微调开源模型用于个人项目、学术研究或原型验证
- 多模态应用开发：基于 VLM（视觉语言模型）微调构建图文理解、文档分析等应用



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,398 |
| 语言 | Java |
| Forks | 15,838 |
| Issues | 35 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

这是一个成熟的企业级AI低代码平台，独创"低代码+零代码"双模驱动模式，集成完整的AI应用生态（包括AI聊天助手、知识库、流程编排、MCP等），通过强大的代码生成器实现前后端一键生成，让开发者既能快速交付又不失灵活性，是传统企业数字化转型和AI应用落地的理想选择。

**技术亮点**:
- 基于SpringBoot3 + Vue3 + SpringCloud微服务架构，技术栈先进且成熟稳定
- 深度集成AI能力：支持LangChain4j、Spring AI、DeepSeek等主流AI框架，提供RAG知识库、AI流程编排(AI Flow)、MCP协议支持
- 强大的代码生成器：整合MyBatis-Plus，实现前后端代码一键生成，显著提升开发效率
- 双模开发模式：低代码快速开发与零代码可视化构建并存，满足不同技术水平的开发者需求
- 集成Flowable/Activiti工作流引擎，支持复杂业务流程自动化与AI Agent协作

**适用场景**:
- 企业内部管理系统快速开发：如ERP、CRM、OA等业务系统的快速搭建与定制
- AI应用构建与落地：构建企业知识库问答、智能客服、AI助手、业务流程智能化等场景
- 创业公司/中小企业快速MVP开发：利用代码生成器和低代码能力，快速验证业务想法并上线产品
- 传统项目现代化改造：将老旧系统迁移至SpringBoot3+Vue3架构，并逐步融入AI能力



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,206 |
| 语言 | Python |
| Forks | 9,826 |
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
| Stars | 34,847 |
| 语言 | TypeScript |
| Forks | 2,463 |
| Issues | 107 |
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
| Stars | 34,635 |
| 语言 | TypeScript |
| Forks | 7,005 |
| Issues | 457 |
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
| Stars | 38,732 |
| 语言 | Python |
| Forks | 6,140 |
| Issues | 184 |
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
| Stars | 32,950 |
| 语言 | TypeScript |
| Forks | 3,551 |
| Issues | 276 |
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
| Stars | 31,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,245 |
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
| Stars | 102,084 |
| 语言 | Python |
| Forks | 14,861 |
| Issues | 5 |
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
| Stars | 56,209 |
| 语言 | JavaScript |
| Forks | 6,080 |
| Issues | 299 |
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
| Stars | 69,109 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 341 |
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
| Stars | 39,972 |
| 语言 | TypeScript |
| Forks | 3,015 |
| Issues | 370 |
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
| Stars | 80,771 |
| 语言 | Python |
| Forks | 9,543 |
| Issues | 235 |
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
| Stars | 50,746 |
| 语言 | TypeScript |
| Forks | 23,962 |
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
| Stars | 31,231 |
| 语言 | Python |
| Forks | 3,424 |
| Issues | 6 |
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
| Stars | 179,119 |
| 语言 | TypeScript |
| Forks | 55,777 |
| Issues | 1,420 |
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
| Stars | 145,660 |
| 语言 | Python |
| Forks | 8,585 |
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
| Stars | 53,980 |
| 语言 | Jupyter Notebook |
| Forks | 18,722 |
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
| Stars | 33,390 |
| 语言 | Python |
| Forks | 2,062 |
| Issues | 99 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 44,024 |
| 语言 | Python |
| Forks | 4,430 |
| Issues | 299 |
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
| Stars | 127,176 |
| 语言 | Python |
| Forks | 17,982 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源 AI 聊天界面之一，拥有超过 12 万 Star，核心价值在于提供了类似 ChatGPT 的完整 Web UI 体验，同时支持本地部署和私有化，让用户可以用自己的 API Key 或本地模型构建专属的 AI 助手平台，兼顾了易用性与数据隐私。

**技术亮点**:
- 多模型后端支持：无缝对接 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换不同模型
- RAG（检索增强生成）内置支持：支持上传文档并与 AI 对话，实现知识库问答功能
- MCP（Model Context Protocol）协议支持：支持 Anthropic 推出的模型上下文协议，增强 AI 与外部工具的交互能力
- 完全自托管与私有化部署：基于 Python 开发，支持 Docker 一键部署，数据完全掌握在自己手中
- 现代化 Web UI 设计：提供类似 ChatGPT 的流畅交互体验，支持多用户、对话历史、Markdown 渲染等功能

**适用场景**:
- 企业内部 AI 助手平台：搭建私有化 ChatGPT 替代方案，保护敏感数据不被外部服务获取
- 个人/团队知识库问答：结合 RAG 功能，上传文档资料构建专属智能问答系统
- 本地大模型体验前端：配合 Ollama 在本地运行开源模型，实现完全离线的 AI 对话体验
- AI 应用开发原型验证：快速搭建 LLM 应用的交互界面，用于测试和演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,994 |
| 语言 | Python |
| Forks | 8,380 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（近 7.5 万 Stars），其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供高质量的上下文层。相比传统 RAG 方案，它集成了深度文档理解、GraphRAG、MCP 协议等先进特性，是构建企业级智能知识库和 AI 搜索应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 智能工作流编排
- 深度文档理解引擎，具备强大的 Document Parser 能力，可处理复杂文档结构
- 支持 GraphRAG 图谱增强检索，提升复杂推理场景的准确性
- 兼容 OpenAI、Ollama、DeepSeek 等多种 LLM 后端，灵活适配不同模型
- 支持 MCP 协议和 Deep Research 模式，适合构建深度研究型 AI 应用

**适用场景**:
- 企业知识库构建：快速搭建基于私有文档的智能问答和知识管理系统
- AI 搜索与深度研究：构建具备深度推理能力的智能搜索和研报生成工具
- 文档理解与自动化处理：对合同、报告等复杂文档进行结构化解析和信息提取



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,648 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 640 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的开源 AI Agent 协作平台，以 73K+ stars 的超高人气证明了其在 AI 社区的影响力。它提供了从单 Agent 到多 Agent 协作的完整解决方案，支持多种主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等），为企业和个人打造智能化工作流提供了强大且灵活的基础设施。

**技术亮点**:
- 🤖 多智能体协作引擎：支持 Agent 之间协同工作，实现复杂任务的自动化分工与协作
- 🔌 多模型适配架构：统一接口对接 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换模型策略
- 📚 知识库集成（Knowledge Base）：支持 RAG 检索增强生成，让 Agent 具备领域知识能力
- ⚡ MCP 协议支持：集成 Model Context Protocol，实现 Agent 与外部工具/数据源的标准化交互
- 🎨 可视化 Agent 设计：提供低代码的 Agent 团队编排能力，降低多 Agent 系统的构建门槛

**适用场景**:
- 🏢 企业智能客服与助手：构建具备企业知识库的多 Agent 系统，实现客户服务、内部问答、流程自动化等场景
- 👨‍💻 开发者 Agent 工作流：个人开发者可搭建专属 AI 助手团队，协同完成代码编写、文档生成、数据分析等任务
- 🔬 研究与原型验证：快速搭建多 Agent 协作原型，验证 AI Agent 在特定业务场景的可行性与效果



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,617 |
| 语言 | MDX |
| Forks | 7,650 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71K+ Stars的提示工程领域最全面的指南资源库，系统性地覆盖了从Prompt Engineering到RAG再到AI Agents的完整技术栈，由DAIR.AI团队精心维护，是AI从业者快速掌握大语言模型应用开发的必备知识库。

**技术亮点**:
- 涵盖提示工程(Prompt Engineering)、上下文工程(Context Engineering)、检索增强生成(RAG)和AI智能体(AI Agents)的完整知识体系
- 提供Jupyter Notebook实践教程，结合理论与代码实战，便于动手学习
- MDX格式编写，支持Markdown与React组件混合，呈现丰富的交互式文档体验
- 集成最新的生成式AI论文、教程和资源，紧跟LLM领域前沿发展
- 开源MIT许可证，社区驱动持续更新，涵盖OpenAI、ChatGPT等主流模型技术

**适用场景**:
- 企业AI团队构建LLM应用时，作为提示工程和RAG技术的标准化培训教材和参考手册
- 个人开发者或研究者系统学习提示工程技术、掌握AI Agent开发最佳实践的完整学习路径
- AI产品经理和技术决策者了解LLM应用架构设计，评估Prompt Engineering和RAG方案的技术参考



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,398 |
| 语言 | Java |
| Forks | 15,838 |
| Issues | 35 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

这是一个成熟的企业级AI低代码平台，独创"低代码+零代码"双模驱动模式，集成完整的AI应用生态（包括AI聊天助手、知识库、流程编排、MCP等），通过强大的代码生成器实现前后端一键生成，让开发者既能快速交付又不失灵活性，是传统企业数字化转型和AI应用落地的理想选择。

**技术亮点**:
- 基于SpringBoot3 + Vue3 + SpringCloud微服务架构，技术栈先进且成熟稳定
- 深度集成AI能力：支持LangChain4j、Spring AI、DeepSeek等主流AI框架，提供RAG知识库、AI流程编排(AI Flow)、MCP协议支持
- 强大的代码生成器：整合MyBatis-Plus，实现前后端代码一键生成，显著提升开发效率
- 双模开发模式：低代码快速开发与零代码可视化构建并存，满足不同技术水平的开发者需求
- 集成Flowable/Activiti工作流引擎，支持复杂业务流程自动化与AI Agent协作

**适用场景**:
- 企业内部管理系统快速开发：如ERP、CRM、OA等业务系统的快速搭建与定制
- AI应用构建与落地：构建企业知识库问答、智能客服、AI助手、业务流程智能化等场景
- 创业公司/中小企业快速MVP开发：利用代码生成器和低代码能力，快速验证业务想法并上线产品
- 传统项目现代化改造：将老旧系统迁移至SpringBoot3+Vue3架构，并逐步融入AI能力



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,847 |
| 语言 | TypeScript |
| Forks | 2,463 |
| Issues | 107 |
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
| Stars | 38,732 |
| 语言 | Python |
| Forks | 6,140 |
| Issues | 184 |
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
| Stars | 32,950 |
| 语言 | TypeScript |
| Forks | 3,551 |
| Issues | 276 |
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
| Stars | 31,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,245 |
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
| Stars | 102,084 |
| 语言 | Python |
| Forks | 14,861 |
| Issues | 5 |
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
| Stars | 98,963 |
| 语言 | TypeScript |
| Forks | 11,796 |
| Issues | 939 |
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
| Stars | 56,209 |
| 语言 | JavaScript |
| Forks | 6,080 |
| Issues | 299 |
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
| Stars | 50,746 |
| 语言 | TypeScript |
| Forks | 23,962 |
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
| Stars | 72,282 |
| 语言 | Python |
| Forks | 9,958 |
| Issues | 247 |
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
| Stars | 43,292 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,037 |
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
| Stars | 31,455 |
| 语言 | Python |
| Forks | 3,319 |
| Issues | 77 |
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
| Stars | 33,390 |
| 语言 | Python |
| Forks | 2,062 |
| Issues | 99 |
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
| Stars | 127,176 |
| 语言 | Python |
| Forks | 17,982 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最流行的开源 AI 聊天界面之一，拥有超过 12 万 Star，核心价值在于提供了类似 ChatGPT 的完整 Web UI 体验，同时支持本地部署和私有化，让用户可以用自己的 API Key 或本地模型构建专属的 AI 助手平台，兼顾了易用性与数据隐私。

**技术亮点**:
- 多模型后端支持：无缝对接 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换不同模型
- RAG（检索增强生成）内置支持：支持上传文档并与 AI 对话，实现知识库问答功能
- MCP（Model Context Protocol）协议支持：支持 Anthropic 推出的模型上下文协议，增强 AI 与外部工具的交互能力
- 完全自托管与私有化部署：基于 Python 开发，支持 Docker 一键部署，数据完全掌握在自己手中
- 现代化 Web UI 设计：提供类似 ChatGPT 的流畅交互体验，支持多用户、对话历史、Markdown 渲染等功能

**适用场景**:
- 企业内部 AI 助手平台：搭建私有化 ChatGPT 替代方案，保护敏感数据不被外部服务获取
- 个人/团队知识库问答：结合 RAG 功能，上传文档资料构建专属智能问答系统
- 本地大模型体验前端：配合 Ollama 在本地运行开源模型，实现完全离线的 AI 对话体验
- AI 应用开发原型验证：快速搭建 LLM 应用的交互界面，用于测试和演示



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,994 |
| 语言 | Python |
| Forks | 8,380 |
| Issues | 3,093 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最热门的开源 RAG 引擎之一（近 7.5 万 Stars），其独特之处在于将前沿的 RAG 技术与 Agent 能力深度融合，为 LLM 提供高质量的上下文层。相比传统 RAG 方案，它集成了深度文档理解、GraphRAG、MCP 协议等先进特性，是构建企业级智能知识库和 AI 搜索应用的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 智能工作流编排
- 深度文档理解引擎，具备强大的 Document Parser 能力，可处理复杂文档结构
- 支持 GraphRAG 图谱增强检索，提升复杂推理场景的准确性
- 兼容 OpenAI、Ollama、DeepSeek 等多种 LLM 后端，灵活适配不同模型
- 支持 MCP 协议和 Deep Research 模式，适合构建深度研究型 AI 应用

**适用场景**:
- 企业知识库构建：快速搭建基于私有文档的智能问答和知识管理系统
- AI 搜索与深度研究：构建具备深度推理能力的智能搜索和研报生成工具
- 文档理解与自动化处理：对合同、报告等复杂文档进行结构化解析和信息提取



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,711 |
| 语言 | JavaScript |
| Forks | 9,461 |
| Issues | 16 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为AI编程助手（如Claude Code、Cursor等）打造的综合性性能优化系统，集成了技能、直觉、记忆、安全和研究驱动开发等核心能力。该项目获得了超过7.5万Stars，证明了其在AI辅助开发领域的巨大价值和社区认可度，是目前最全面的AI Agent开发框架之一。

**技术亮点**:
- 集成Skills（技能）、Instincts（直觉）、Memory（记忆）三大AI Agent核心能力模块，实现更智能的上下文理解和任务执行
- 支持多平台兼容，涵盖Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- 内置安全机制，为AI Agent提供安全边界和防护措施
- 支持MCP协议，实现AI模型间的高效通信与工具集成
- 研究驱动开发方法论，提供结构化的开发流程和最佳实践

**适用场景**:
- 企业级AI辅助开发：团队需要统一AI编程工具的使用规范和性能优化
- 个人开发者提升AI编程效率：优化Claude Code或Cursor等工具的响应质量和准确性
- 构建自定义AI Agent：开发者需要快速搭建具备记忆、技能和安全能力的智能代理



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,648 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 640 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的开源 AI Agent 协作平台，以 73K+ stars 的超高人气证明了其在 AI 社区的影响力。它提供了从单 Agent 到多 Agent 协作的完整解决方案，支持多种主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等），为企业和个人打造智能化工作流提供了强大且灵活的基础设施。

**技术亮点**:
- 🤖 多智能体协作引擎：支持 Agent 之间协同工作，实现复杂任务的自动化分工与协作
- 🔌 多模型适配架构：统一接口对接 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换模型策略
- 📚 知识库集成（Knowledge Base）：支持 RAG 检索增强生成，让 Agent 具备领域知识能力
- ⚡ MCP 协议支持：集成 Model Context Protocol，实现 Agent 与外部工具/数据源的标准化交互
- 🎨 可视化 Agent 设计：提供低代码的 Agent 团队编排能力，降低多 Agent 系统的构建门槛

**适用场景**:
- 🏢 企业智能客服与助手：构建具备企业知识库的多 Agent 系统，实现客户服务、内部问答、流程自动化等场景
- 👨‍💻 开发者 Agent 工作流：个人开发者可搭建专属 AI 助手团队，协同完成代码编写、文档生成、数据分析等任务
- 🔬 研究与原型验证：快速搭建多 Agent 协作原型，验证 AI Agent 在特定业务场景的可行性与效果



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,617 |
| 语言 | MDX |
| Forks | 7,650 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71K+ Stars的提示工程领域最全面的指南资源库，系统性地覆盖了从Prompt Engineering到RAG再到AI Agents的完整技术栈，由DAIR.AI团队精心维护，是AI从业者快速掌握大语言模型应用开发的必备知识库。

**技术亮点**:
- 涵盖提示工程(Prompt Engineering)、上下文工程(Context Engineering)、检索增强生成(RAG)和AI智能体(AI Agents)的完整知识体系
- 提供Jupyter Notebook实践教程，结合理论与代码实战，便于动手学习
- MDX格式编写，支持Markdown与React组件混合，呈现丰富的交互式文档体验
- 集成最新的生成式AI论文、教程和资源，紧跟LLM领域前沿发展
- 开源MIT许可证，社区驱动持续更新，涵盖OpenAI、ChatGPT等主流模型技术

**适用场景**:
- 企业AI团队构建LLM应用时，作为提示工程和RAG技术的标准化培训教材和参考手册
- 个人开发者或研究者系统学习提示工程技术、掌握AI Agent开发最佳实践的完整学习路径
- AI产品经理和技术决策者了解LLM应用架构设计，评估Prompt Engineering和RAG方案的技术参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,410 |
| 语言 | HTML |
| Forks | 20,031 |
| Issues | 29 |
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
| Stars | 88,034 |
| 语言 | Jupyter Notebook |
| Forks | 13,432 |
| Issues | 2 |
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
| Stars | 42,206 |
| 语言 | Python |
| Forks | 9,826 |
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
| Stars | 34,847 |
| 语言 | TypeScript |
| Forks | 2,463 |
| Issues | 107 |
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
| Stars | 34,635 |
| 语言 | TypeScript |
| Forks | 7,005 |
| Issues | 457 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,209 |
| 语言 | JavaScript |
| Forks | 6,080 |
| Issues | 299 |
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
| Stars | 69,109 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 341 |
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
| Stars | 39,972 |
| 语言 | TypeScript |
| Forks | 3,015 |
| Issues | 370 |
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
| Stars | 50,746 |
| 语言 | TypeScript |
| Forks | 23,962 |
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
| Stars | 31,231 |
| 语言 | Python |
| Forks | 3,424 |
| Issues | 6 |
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
| Stars | 34,307 |
| 语言 | HTML |
| Forks | 5,510 |
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
| Stars | 73,082 |
| 语言 | Python |
| Forks | 14,355 |
| Issues | 3,670 |
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
| Stars | 41,350 |
| 语言 | Python |
| Forks | 4,011 |
| Issues | 70 |
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
| Stars | 145,660 |
| 语言 | Python |
| Forks | 8,585 |
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
| Stars | 165,048 |
| 语言 | Go |
| Forks | 14,970 |
| Issues | 2,641 |
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
| Stars | 46,636 |
| 语言 | Rust |
| Forks | 9,123 |
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
| Stars | 33,390 |
| 语言 | Python |
| Forks | 2,062 |
| Issues | 99 |
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
| Stars | 90,739 |
| 语言 | Python |
| Forks | 5,359 |
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
| Stars | 38,949 |
| 语言 | TypeScript |
| Forks | 3,940 |
| Issues | 1,073 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,633 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 62 |
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
| Stars | 44,024 |
| 语言 | Python |
| Forks | 4,430 |
| Issues | 299 |
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
| Stars | 71,617 |
| 语言 | MDX |
| Forks | 7,650 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71K+ Stars的提示工程领域最全面的指南资源库，系统性地覆盖了从Prompt Engineering到RAG再到AI Agents的完整技术栈，由DAIR.AI团队精心维护，是AI从业者快速掌握大语言模型应用开发的必备知识库。

**技术亮点**:
- 涵盖提示工程(Prompt Engineering)、上下文工程(Context Engineering)、检索增强生成(RAG)和AI智能体(AI Agents)的完整知识体系
- 提供Jupyter Notebook实践教程，结合理论与代码实战，便于动手学习
- MDX格式编写，支持Markdown与React组件混合，呈现丰富的交互式文档体验
- 集成最新的生成式AI论文、教程和资源，紧跟LLM领域前沿发展
- 开源MIT许可证，社区驱动持续更新，涵盖OpenAI、ChatGPT等主流模型技术

**适用场景**:
- 企业AI团队构建LLM应用时，作为提示工程和RAG技术的标准化培训教材和参考手册
- 个人开发者或研究者系统学习提示工程技术、掌握AI Agent开发最佳实践的完整学习路径
- AI产品经理和技术决策者了解LLM应用架构设计，评估Prompt Engineering和RAG方案的技术参考



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,400 |
| 语言 | Python |
| Forks | 8,350 |
| Issues | 929 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 收录的明星项目，以统一的 WebUI 界面一站式支持 100+ 大语言模型和视觉语言模型的高效微调，极大地降低了 LLM 定制化的技术门槛和工程成本。

**技术亮点**:
- 支持 100+ 主流大语言模型（LLaMA、Qwen、ChatGLM、DeepSeek、Gemma等）的统一微调框架，兼容性极强
- 集成了 LoRA、QLoRA、全量微调等多种高效微调方法，支持模型量化（4bit/8bit），大幅降低显存需求
- 提供完整的训练流程：支持预训练、指令微调、RLHF（人类反馈强化学习）全链路
- 内置 WebUI 可视化界面，无需代码即可完成模型微调和推理部署
- 支持 MoE（混合专家）架构和 Agent 应用开发，紧跟前沿技术趋势

**适用场景**:
- 企业级私有化大模型定制：在垂直领域数据上微调专属模型，如金融、医疗、法律等行业应用
- 个人开发者快速实验：低成本微调开源模型用于个人项目、学术研究或原型验证
- 多模态应用开发：基于 VLM（视觉语言模型）微调构建图文理解、文档分析等应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,052 |
| 语言 | Python |
| Forks | 6,187 |
| Issues | 64 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个专为金融分析师、量化交易者和AI智能体打造的开源金融数据平台，拥有63K+ Stars证明了其强大的社区认可度。它打破了传统金融数据平台的封闭性，将股票、加密货币、期权、衍生品、宏观经济等多维度金融数据整合到统一的Python接口中，让个人投资者和小型团队也能以零成本获取专业级金融数据分析能力。

**技术亮点**:
- 一站式多资产类别数据聚合 - 整合股票(equity)、加密货币(crypto)、期权(options)、衍生品(derivatives)、固收(fixed-income)、宏观经济(economics)等多维度金融数据源
- AI Agent原生设计 - 专门为AI智能体优化的数据接口，支持大语言模型和机器学习模型直接调用，实现智能金融分析
- Python生态深度集成 - 纯Python构建，与pandas、numpy等数据科学生态无缝对接，支持量化金融(quantitative-finance)和机器学习(machine-learning)工作流
- 模块化可扩展架构 - 开放式架构设计，用户可自定义数据源接入和扩展分析功能，灵活适配不同投资策略需求

**适用场景**:
- 个人量化交易者构建自动化交易策略 - 使用Python脚本获取实时市场数据、技术指标计算、回测验证，无需购买昂贵的Bloomberg或Wind终端
- 金融科技创业团队快速搭建投资分析产品 - 利用OpenBB作为底层数据引擎，快速开发面向C端用户的智能投顾、基金筛选、股票分析等应用
- 学术研究与金融数据分析 - 经济学研究员和学生获取宏观经济数据、历史行情数据，进行学术研究和论文撰写



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,410 |
| 语言 | HTML |
| Forks | 20,031 |
| Issues | 29 |
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
| Stars | 88,034 |
| 语言 | Jupyter Notebook |
| Forks | 13,432 |
| Issues | 2 |
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
| Stars | 32,950 |
| 语言 | TypeScript |
| Forks | 3,551 |
| Issues | 276 |
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
| Stars | 31,986 |
| 语言 | Jupyter Notebook |
| Forks | 5,245 |
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
| Stars | 157,811 |
| 语言 | Python |
| Forks | 32,471 |
| Issues | 2,299 |
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
| Stars | 73,082 |
| 语言 | Python |
| Forks | 14,355 |
| Issues | 3,670 |
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
| Stars | 105,840 |
| 语言 | Python |
| Forks | 12,160 |
| Issues | 3,819 |
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
| Stars | 98,251 |
| 语言 | Python |
| Forks | 27,205 |
| Issues | 18,050 |
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
| Stars | 161,710 |
| 语言 | Python |
| Forks | 30,164 |
| Issues | 2,471 |
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
| Stars | 75,711 |
| 语言 | JavaScript |
| Forks | 9,461 |
| Issues | 16 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为AI编程助手（如Claude Code、Cursor等）打造的综合性性能优化系统，集成了技能、直觉、记忆、安全和研究驱动开发等核心能力。该项目获得了超过7.5万Stars，证明了其在AI辅助开发领域的巨大价值和社区认可度，是目前最全面的AI Agent开发框架之一。

**技术亮点**:
- 集成Skills（技能）、Instincts（直觉）、Memory（记忆）三大AI Agent核心能力模块，实现更智能的上下文理解和任务执行
- 支持多平台兼容，涵盖Claude Code、Codex、Opencode、Cursor等主流AI编程工具
- 内置安全机制，为AI Agent提供安全边界和防护措施
- 支持MCP协议，实现AI模型间的高效通信与工具集成
- 研究驱动开发方法论，提供结构化的开发流程和最佳实践

**适用场景**:
- 企业级AI辅助开发：团队需要统一AI编程工具的使用规范和性能优化
- 个人开发者提升AI编程效率：优化Claude Code或Cursor等工具的响应质量和准确性
- 构建自定义AI Agent：开发者需要快速搭建具备记忆、技能和安全能力的智能代理



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,602 |
| 语言 | Go |
| Forks | 3,690 |
| Issues | 142 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，最大的价值在于完全免费开源且无需 GPU 就能在消费级硬件上运行，同时提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到自托管方案，兼顾了隐私保护和成本控制。

**技术亮点**:
- OpenAI API 兼容的 Drop-in 替代方案，支持无缝迁移
- 支持多种模型格式（GGUF、Transformers、Diffusers）和模型架构（LLaMA、Mistral、RWKV、Mamba等）
- 无 GPU 依赖，可在普通消费级 CPU 硬件上高效运行
- 支持多模态生成：文本、图像、音频、视频、语音克隆等全方位 AI 能力
- 去中心化和分布式推理架构，支持 P2P 和 MCP 协议

**适用场景**:
- 企业内部 AI 服务部署：在私有环境中运行 LLM 和多模态模型，确保数据安全和隐私合规
- 个人开发者本地开发测试：零成本搭建 OpenAI 兼容的本地 AI 环境，无需付费 API 调用
- 边缘设备和嵌入式场景：在资源受限的硬件上部署 AI 能力，如树莓派或老旧服务器



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,109 |
| 语言 | Python |
| Forks | 8,659 |
| Issues | 341 |
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
| Stars | 39,972 |
| 语言 | TypeScript |
| Forks | 3,015 |
| Issues | 370 |
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
| Stars | 179,119 |
| 语言 | TypeScript |
| Forks | 55,777 |
| Issues | 1,420 |
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
| Stars | 151,175 |
| 语言 | Python |
| Forks | 12,250 |
| Issues | 2,364 |
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
| Stars | 96,200 |
| 语言 | Python |
| Forks | 8,859 |
| Issues | 159 |
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
| Stars | 73,691 |
| 语言 | Python |
| Forks | 8,747 |
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
| Stars | 182,635 |
| 语言 | TypeScript |
| Forks | 38,502 |
| Issues | 15,193 |
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
| Stars | 93,816 |
| 语言 | TypeScript |
| Forks | 9,396 |
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
| Stars | 78,448 |
| 语言 | TypeScript |
| Forks | 5,684 |
| Issues | 705 |
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
| Stars | 76,637 |
| 语言 | TypeScript |
| Forks | 6,549 |
| Issues | 173 |
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
| Stars | 75,654 |
| 语言 | JavaScript |
| Forks | 7,271 |
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
| Stars | 78,587 |
| 语言 | Go |
| Forks | 2,728 |
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
| Stars | 74,196 |
| 语言 | Go |
| Forks | 2,599 |
| Issues | 926 |
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
| Stars | 36,633 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 62 |
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
| Stars | 54,437 |
| 语言 | JavaScript |
| Forks | 4,025 |
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
| Stars | 410,158 |
| 语言 | Python |
| Forks | 44,314 |
| Issues | 988 |
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
| Stars | 39,972 |
| 语言 | TypeScript |
| Forks | 3,015 |
| Issues | 370 |
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
| Stars | 31,231 |
| 语言 | Python |
| Forks | 3,424 |
| Issues | 6 |
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
| Stars | 179,119 |
| 语言 | TypeScript |
| Forks | 55,777 |
| Issues | 1,420 |
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
| Stars | 51,608 |
| 语言 | Go |
| Forks | 10,343 |
| Issues | 226 |
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
| Stars | 121,127 |
| 语言 | Go |
| Forks | 42,681 |
| Issues | 2,649 |
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
| Stars | 71,521 |
| 语言 | Go |
| Forks | 18,922 |
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
| Stars | 54,289 |
| 语言 | Go |
| Forks | 6,475 |
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
| Stars | 93,816 |
| 语言 | TypeScript |
| Forks | 9,396 |
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
| Stars | 84,234 |
| 语言 | TypeScript |
| Forks | 5,288 |
| Issues | 610 |
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
| Stars | 75,291 |
| 语言 | TypeScript |
| Forks | 6,394 |
| Issues | 441 |
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
| Stars | 84,051 |
| 语言 | JavaScript |
| Forks | 7,523 |
| Issues | 706 |
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
| Stars | 62,169 |
| 语言 | Go |
| Forks | 5,882 |
| Issues | 781 |
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
| Stars | 57,859 |
| 语言 | Go |
| Forks | 4,196 |
| Issues | 22 |
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
| Stars | 44,024 |
| 语言 | Python |
| Forks | 4,430 |
| Issues | 299 |
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
| Stars | 47,580 |
| 语言 | Go |
| Forks | 5,072 |
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
| Stars | 69,346 |
| 语言 | Go |
| Forks | 1,878 |
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
| Stars | 60,484 |
| 语言 | Go |
| Forks | 7,249 |
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
| Stars | 84,051 |
| 语言 | JavaScript |
| Forks | 7,523 |
| Issues | 706 |
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
| Stars | 63,168 |
| 语言 | Go |
| Forks | 10,243 |
| Issues | 760 |
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
| Stars | 43,602 |
| 语言 | Go |
| Forks | 3,690 |
| Issues | 142 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，最大的价值在于完全免费开源且无需 GPU 就能在消费级硬件上运行，同时提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到自托管方案，兼顾了隐私保护和成本控制。

**技术亮点**:
- OpenAI API 兼容的 Drop-in 替代方案，支持无缝迁移
- 支持多种模型格式（GGUF、Transformers、Diffusers）和模型架构（LLaMA、Mistral、RWKV、Mamba等）
- 无 GPU 依赖，可在普通消费级 CPU 硬件上高效运行
- 支持多模态生成：文本、图像、音频、视频、语音克隆等全方位 AI 能力
- 去中心化和分布式推理架构，支持 P2P 和 MCP 协议

**适用场景**:
- 企业内部 AI 服务部署：在私有环境中运行 LLM 和多模态模型，确保数据安全和隐私合规
- 个人开发者本地开发测试：零成本搭建 OpenAI 兼容的本地 AI 环境，无需付费 API 调用
- 边缘设备和嵌入式场景：在资源受限的硬件上部署 AI 能力，如树莓派或老旧服务器



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,200 |
| 语言 | Python |
| Forks | 8,859 |
| Issues | 159 |
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
| Stars | 87,038 |
| 语言 | Python |
| Forks | 33,747 |
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
| Stars | 100,083 |
| 语言 | TypeScript |
| Forks | 27,125 |
| Issues | 1,129 |
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
| Stars | 78,448 |
| 语言 | TypeScript |
| Forks | 5,684 |
| Issues | 705 |
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
| Stars | 74,915 |
| 语言 | TypeScript |
| Forks | 8,255 |
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
| Stars | 75,654 |
| 语言 | JavaScript |
| Forks | 7,271 |
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
| Stars | 55,945 |
| 语言 | JavaScript |
| Forks | 10,228 |
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
| Stars | 88,230 |
| 语言 | Go |
| Forks | 8,573 |
| Issues | 644 |
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
| Stars | 70,793 |
| 语言 | Go |
| Forks | 4,675 |
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
| Stars | 56,740 |
| 语言 | Go |
| Forks | 3,177 |
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
| Stars | 36,633 |
| 语言 | Python |
| Forks | 2,563 |
| Issues | 62 |
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
| Stars | 410,158 |
| 语言 | Python |
| Forks | 44,314 |
| Issues | 988 |
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
| Stars | 68,879 |
| 语言 | JavaScript |
| Forks | 22,825 |
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
| Stars | 98,963 |
| 语言 | TypeScript |
| Forks | 11,796 |
| Issues | 939 |
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
| Stars | 56,209 |
| 语言 | JavaScript |
| Forks | 6,080 |
| Issues | 299 |
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
| Stars | 43,292 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,037 |
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
| Stars | 51,608 |
| 语言 | Go |
| Forks | 10,343 |
| Issues | 226 |
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
| Stars | 71,617 |
| 语言 | MDX |
| Forks | 7,650 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个拥有71K+ Stars的提示工程领域最全面的指南资源库，系统性地覆盖了从Prompt Engineering到RAG再到AI Agents的完整技术栈，由DAIR.AI团队精心维护，是AI从业者快速掌握大语言模型应用开发的必备知识库。

**技术亮点**:
- 涵盖提示工程(Prompt Engineering)、上下文工程(Context Engineering)、检索增强生成(RAG)和AI智能体(AI Agents)的完整知识体系
- 提供Jupyter Notebook实践教程，结合理论与代码实战，便于动手学习
- MDX格式编写，支持Markdown与React组件混合，呈现丰富的交互式文档体验
- 集成最新的生成式AI论文、教程和资源，紧跟LLM领域前沿发展
- 开源MIT许可证，社区驱动持续更新，涵盖OpenAI、ChatGPT等主流模型技术

**适用场景**:
- 企业AI团队构建LLM应用时，作为提示工程和RAG技术的标准化培训教材和参考手册
- 个人开发者或研究者系统学习提示工程技术、掌握AI Agent开发最佳实践的完整学习路径
- AI产品经理和技术决策者了解LLM应用架构设计，评估Prompt Engineering和RAG方案的技术参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,410 |
| 语言 | HTML |
| Forks | 20,031 |
| Issues | 29 |
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
| Stars | 34,307 |
| 语言 | HTML |
| Forks | 5,510 |
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
| Stars | 89,446 |
| 语言 | TypeScript |
| Forks | 9,925 |
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
| Stars | 86,645 |
| 语言 | TypeScript |
| Forks | 8,729 |
| Issues | 1,610 |
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
| Stars | 127,080 |
| 语言 | JavaScript |
| Forks | 12,452 |
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
| Stars | 100,164 |
| 语言 | JavaScript |
| Forks | 7,495 |
| Issues | 221 |
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
| Stars | 167,334 |
| 语言 | Go |
| Forks | 13,049 |
| Issues | 171 |
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
| Stars | 130,977 |
| 语言 | Unknown |
| Forks | 33,252 |
| Issues | 129 |
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
| Stars | 312,760 |
| 语言 | TypeScript |
| Forks | 59,605 |
| Issues | 13,673 |
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
| Stars | 43,222 |
| 语言 | Shell |
| Forks | 6,474 |
| Issues | 35 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,942 |
| 语言 | Python |
| Forks | 6,320 |
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
| Stars | 80,018 |
| 语言 | Python |
| Forks | 11,670 |
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
| Stars | 76,763 |
| 语言 | Python |
| Forks | 6,535 |
| Issues | 636 |
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
| Stars | 383,988 |
| 语言 | Python |
| Forks | 66,019 |
| Issues | 70 |
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
| Stars | 112,880 |
| 语言 | TypeScript |
| Forks | 5,721 |
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
| Stars | 102,766 |
| 语言 | TypeScript |
| Forks | 7,477 |
| Issues | 180 |
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
| Stars | 47,920 |
| 语言 | Go |
| Forks | 10,249 |
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
| Stars | 97,919 |
| 语言 | C++ |
| Forks | 15,496 |
| Issues | 1,272 |
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
| Stars | 59,393 |
| 语言 | Python |
| Forks | 1,606 |
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
| Stars | 338,828 |
| 语言 | Python |
| Forks | 54,876 |
| Issues | 520 |
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
| Stars | 287,121 |
| 语言 | Python |
| Forks | 27,393 |
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
| Stars | 218,640 |
| 语言 | Python |
| Forks | 50,188 |
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
| Stars | 85,338 |
| 语言 | Python |
| Forks | 36,991 |
| Issues | 3,618 |
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
| Stars | 85,247 |
| 语言 | Python |
| Forks | 7,165 |
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
| Stars | 77,689 |
| 语言 | Python |
| Forks | 45,243 |
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
| Stars | 76,045 |
| 语言 | Python |
| Forks | 16,751 |
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
| Stars | 438,128 |
| 语言 | TypeScript |
| Forks | 43,614 |
| Issues | 244 |
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
| Stars | 350,895 |
| 语言 | TypeScript |
| Forks | 43,783 |
| Issues | 23 |
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
| Stars | 118,722 |
| 语言 | TypeScript |
| Forks | 12,863 |
| Issues | 2,832 |
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
| Stars | 109,508 |
| 语言 | TypeScript |
| Forks | 8,178 |
| Issues | 1,788 |
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
| Stars | 108,152 |
| 语言 | TypeScript |
| Forks | 13,297 |
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
| Stars | 97,702 |
| 语言 | TypeScript |
| Forks | 54,558 |
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
| Stars | 94,717 |
| 语言 | TypeScript |
| Forks | 5,098 |
| Issues | 644 |
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
| Stars | 94,031 |
| 语言 | TypeScript |
| Forks | 5,112 |
| Issues | 96 |
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
| Stars | 81,078 |
| 语言 | TypeScript |
| Forks | 9,894 |
| Issues | 506 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,938 |
| 语言 | TypeScript |
| Forks | 7,907 |
| Issues | 639 |
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
| Stars | 243,917 |
| 语言 | JavaScript |
| Forks | 50,779 |
| Issues | 1,175 |
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
| Stars | 138,291 |
| 语言 | JavaScript |
| Forks | 30,645 |
| Issues | 3,461 |
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
| Stars | 116,242 |
| 语言 | JavaScript |
| Forks | 35,048 |
| Issues | 2,530 |
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
| Stars | 111,358 |
| 语言 | JavaScript |
| Forks | 36,308 |
| Issues | 582 |
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
| Stars | 108,650 |
| 语言 | JavaScript |
| Forks | 11,554 |
| Issues | 343 |
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
| Stars | 98,013 |
| 语言 | JavaScript |
| Forks | 32,713 |
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
| Stars | 95,423 |
| 语言 | JavaScript |
| Forks | 15,247 |
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
| Stars | 86,047 |
| 语言 | JavaScript |
| Forks | 4,801 |
| Issues | 975 |
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
| Stars | 78,720 |
| 语言 | JavaScript |
| Forks | 31,526 |
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
| Stars | 70,732 |
| 语言 | JavaScript |
| Forks | 16,802 |
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
| Stars | 66,015 |
| 语言 | JavaScript |
| Forks | 9,322 |
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
| Stars | 62,097 |
| 语言 | JavaScript |
| Forks | 3,975 |
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
| Stars | 59,868 |
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
| Stars | 59,824 |
| 语言 | JavaScript |
| Forks | 5,608 |
| Issues | 64 |
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
| Stars | 57,402 |
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
| Stars | 133,044 |
| 语言 | Go |
| Forks | 18,860 |
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
| Stars | 105,202 |
| 语言 | Go |
| Forks | 14,947 |
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
| Stars | 87,085 |
| 语言 | Go |
| Forks | 8,205 |
| Issues | 259 |
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
| Stars | 80,806 |
| 语言 | Go |
| Forks | 4,960 |
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
| Stars | 68,690 |
| 语言 | Go |
| Forks | 3,221 |
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
| Stars | 56,026 |
| 语言 | Go |
| Forks | 4,971 |
| Issues | 1,144 |
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
| Stars | 50,917 |
| 语言 | Go |
| Forks | 21,849 |
| Issues | 374 |
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
| Stars | 46,952 |
| 语言 | Go |
| Forks | 8,882 |
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
| Stars | 45,445 |
| 语言 | Go |
| Forks | 3,765 |
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
| Stars | 139,869 |
| 语言 | Python |
| Forks | 10,602 |
| Issues | 4,119 |
| 许可证 | The Unlicense |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 82,994 |
| 语言 | TypeScript |
| Forks | 7,579 |
| Issues | 37 |
| 许可证 | MIT License |


### trekhleb/javascript-algorithms

**描述**: 📝 Algorithms and data structures implemented in JavaScript with explanations and links to further readings

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 195,761 |
| 语言 | JavaScript |
| Forks | 31,114 |
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
| Stars | 148,117 |
| 语言 | JavaScript |
| Forks | 26,773 |
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
| Stars | 67,261 |
| 语言 | JavaScript |
| Forks | 11,983 |
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
| Stars | 66,849 |
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
| Stars | 66,282 |
| 语言 | JavaScript |
| Forks | 9,190 |
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
| Issues | 131 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,169 |
| 语言 | Go |
| Forks | 7,981 |
| Issues | 574 |
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
| Stars | 146,086 |
| 语言 | Python |
| Forks | 11,220 |
| Issues | 293 |
| Topics | awesome, github, hellogithub, python |
