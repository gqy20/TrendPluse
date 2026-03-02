# 项目发现报告 (2026-03-02)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 140 |
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
| Stars | 125,468 |
| 语言 | Python |
| Forks | 17,765 |
| Issues | 270 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是当前最流行的开源LLM界面之一，拥有超过12.5万颗星，完美解决了自部署大模型缺乏友好交互界面的痛点。它不仅支持Ollama、OpenAI API等多种后端，还集成了RAG、MCP等高级功能，是构建私有化AI助手平台的最佳选择。

**技术亮点**:
- 🚀 多后端支持 - 同时支持Ollama本地部署和OpenAI API，灵活适配不同模型来源
- 🔍 内置RAG能力 - 原生集成检索增强生成功能，可直接上传文档进行知识库对话
- 🌐 完全自托管 - 可完全部署在本地/私有环境，数据隐私安全，适合企业内网使用
- 🔌 MCP协议支持 - 支持Model Context Protocol，可扩展连接更多AI工具和服务
- 💬 现代化Web界面 - 提供类似ChatGPT的友好交互体验，支持多会话管理和对话历史

**适用场景**:
- 🏢 企业私有化部署 - 适合需要在本地/私有云部署AI助手的企业，保护数据隐私不外泄
- 👨‍💻 个人开发者实验 - 适合AI爱好者在本地运行Ollama等模型，并通过友好界面进行测试和开发
- 🎓 教育与研究机构 - 适合学校和研究机构搭建内部AI教学和研究平台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,039 |
| 语言 | Python |
| Forks | 8,236 |
| Issues | 3,014 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的开源 RAG 引擎，成功融合了先进的检索增强生成技术与 Agent 能力，为 LLM 提供卓越的上下文理解层。凭借 7.4 万+ stars 的广泛认可，它支持深度研究、图检索、多模型集成等前沿特性，是构建企业级智能问答和知识管理系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，创建强大的 LLM 上下文引擎
- 内置文档解析和理解引擎，支持复杂文档处理
- 集成 GraphRAG 技术，实现知识图谱增强的检索
- 支持 MCP 协议和主流 LLM（OpenAI、DeepSeek、Ollama 等）
- 具备深度研究（deep-research）和智能工作流编排能力

**适用场景**:
- 企业知识库构建：搭建智能文档管理和问答系统，实现企业内部知识的高效检索与复用
- 智能客服与助手：开发基于企业文档的 AI 客服系统，提供精准的上下文感知服务
- AI 搜索引擎：构建具备深度理解和推理能力的垂直领域搜索引擎



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 87,403 |
| 语言 | TypeScript |
| Forks | 6,204 |
| Issues | 200 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是专为 AI 应用打造的全栈网页数据提取解决方案，具有 87k+ stars 的超高人气。它能够将任何网站转化为 LLM 就绪的 Markdown 或结构化数据，完美解决 AI 应用开发中的数据获取和预处理痛点，是构建 AI Agent 和 RAG 应用的理想基础设施。

**技术亮点**:
- LLM 就绪的输出格式 - 将网页自动转换为 Markdown 或结构化 JSON 数据，无需额外清洗即可直接输入大模型
- 强大的网页爬取能力 - 支持处理 JavaScript 渲染页面、反爬虫机制和复杂的网站结构
- 一站式数据提取 - 集爬取、抓取、HTML 转 Markdown、数据清洗于一体，大幅简化开发流程
- AI Agent 友好设计 - 提供 API 接口，易于集成到 AI 智能体、搜索和数据提取工作流中
- TypeScript 编写的高性能架构 - 提供 Node.js SDK 和 REST API，支持灵活部署和扩展

**适用场景**:
- 企业级 AI 应用开发 - 为 RAG 系统、知识库构建、AI 搜索引擎等提供高质量网页数据源
- AI Agent 智能体开发 - 为 AI 代理提供网页浏览、数据抓取和信息提取能力
- Web 数据分析与监控 - 企业监控竞品动态、市场趋势变化或进行舆情分析
- 个人开发者快速原型 - 无需处理复杂的爬虫逻辑，快速集成网页数据功能到 AI 项目中



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,107 |
| 语言 | JavaScript |
| Forks | 7,046 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code、Codex 等 AI 代理系统的性能优化工具集，整合了技能库、记忆系统、安全防护和研究优先的开发方法论。凭借超过 5.7 万颗星和 MIT 许可证，该项目为开发者提供了完整的 AI 代理增强方案，显著提升 Claude Code 等工具的生产力表现。

**技术亮点**:
- 集成 MCP (Model Context Protocol) 协议支持，实现高效的模型上下文管理
- 构建多维度 AI Agent 能力体系：技能、直觉、记忆、安全和研究
- 支持 Claude Code、Codex、Cowork 等多种 Anthropic AI 生态产品
- 研究优先的开发模式，持续优化 AI 代理的表现和响应质量
- 完整的开发者工具链，提升 AI 辅助编程的工作流效率

**适用场景**:
- 企业级开发团队：集成 AI 代理优化系统，提升团队使用 Claude Code 的协作效率和代码质量
- 个人开发者/自由职业者：通过增强的 AI 代理能力，加速日常开发任务和问题解决流程
- AI 应用研究者：基于项目提供的研究优先方法论，探索和实验 AI 代理的新功能和性能优化方案



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,283 |
| 语言 | JavaScript |
| Forks | 5,972 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能完备的"全栈式"AI应用解决方案，打破了开发者需要集成多个分散工具的痛点。它将 RAG、AI Agent、无代码构建器、MCP 协议支持等核心能力整合在单一应用中，支持本地 LLM（如 Ollama、LM Studio）和云端模型，为企业级和个人开发者提供了开箱即用的 AI 部署能力。作为拥有 5.5 万+ stars 的开源项目，它降低了 AI 应用开发的门槛，是构建私有化智能问答、客服机器人、知识库助手的理想选择。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库集成，可实现高质量的知识库问答
- No-code Agent 构建器，可视化拖拽即可创建自定义 AI 智能体，降低开发门槛
- 完整的 MCP（Model Context Protocol）兼容性，可无缝连接各类 MCP 服务和工具
- 支持多种本地 LLM 引擎（Ollama、LM Studio、LocalAI）及云端模型（DeepSeek、Kimi、Llama3、Qwen3 等），灵活部署
- 多模态能力支持，可处理文本、图片等多种输入格式，扩展应用场景

**适用场景**:
- 企业内部知识库助手：搭建私有化智能问答系统，员工可通过自然语言快速检索公司文档、技术手册等资源
- 无代码 AI 应用开发：非技术人员也能快速搭建定制化 AI Agent，如智能客服、数据分析助手、内容生成工具等
- 本地化 AI 部署：对数据隐私要求高的场景，可完全在本地运行 LLM 和 RAG，无需将敏感数据发送至云端



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,186 |
| 语言 | Go |
| Forks | 3,612 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源项目，作为 OpenAI、Claude 等商业 AI 服务的免费替代方案，能够在普通消费级硬件上本地运行，无需 GPU。它支持多种主流模型格式（gguf、transformers、diffusers），并提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到本地化 AI 解决方案，同时保护数据隐私和安全性。

**技术亮点**:
- 🚀 多模态 AI 能力：支持文本、音频、视频、图像生成、语音克隆、目标检测等多种 AI 任务
- 🔌 API 兼容性：提供 OpenAI API 的直接替换接口，实现零成本迁移和集成
- 💻 硬件友好：无需 GPU，可在消费级硬件上运行，支持 CPU 推理
- 🌐 分布式架构：基于 libp2p 实现 P2P 和去中心化推理，支持分布式计算
- 🎯 模型生态广泛：支持 Llama、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求高的行业，可在本地环境部署 AI 能力，避免数据外泄
- 👨‍💻 个人开发者实验：在个人电脑上测试和开发 AI 应用，无需支付昂贵的 API 调用费用
- 🔒 离线场景应用：无网络环境或需要本地推理的边缘计算场景，如 IoT 设备、内网系统



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,896 |
| 语言 | TypeScript |
| Forks | 14,708 |
| Issues | 802 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，在 GitHub 上获得了超过 7.2 万颗星，是构建、管理和部署 AI Agent 生态系统的顶级开源项目。它独特地将 Agent 作为工作交互单元，提供了从单智能体到多智能体协作的完整解决方案，特别适合需要快速搭建智能助手团队的开发者和企业。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的 Agent 团队工作流
- 集成了主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等）和 MCP 协议
- TypeScript 构建，提供类型安全和现代化的开发体验
- 零门槛的智能体团队设计，降低 AI 应用开发门槛
- 内置知识库功能，支持 Agent 与企业知识库的深度整合

**适用场景**:
- 企业级 AI 助手团队构建：快速搭建客服、销售、技术支持等多个智能体协作系统
- 个人开发者 AI 应用开发：快速原型开发和部署个性化 AI Agent
- 知识库智能问答：结合企业知识库构建智能的文档检索和问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,026 |
| 语言 | MDX |
| Forks | 7,563 |
| Issues | 245 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个专注于提示工程（Prompt Engineering）的综合性知识库项目，由知名 AI 研究机构 dair-ai 维护，涵盖提示工程、上下文工程、RAG 和 AI Agents 等前沿技术。该项目获得了超过 7 万星标，提供了从入门指南到学术论文、实战代码的全方位资源，是学习大语言模型应用开发的权威参考资料。

**技术亮点**:
- 覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 集成多种学习资源：指南文档、学术论文、实战教程、可交互的 Notebook 代码示例
- 紧跟技术前沿，涵盖 ChatGPT、OpenAI、LLMs、生成式 AI 等热门技术栈
- 采用 MDX 格式组织内容，结构清晰便于学习查阅和技术分享
- 开源且社区活跃，持续更新最新的 AI 代理和检索增强生成技术

**适用场景**:
- 个人开发者学习：大语言模型应用开发初学者，系统学习提示工程技巧和最佳实践
- 企业 AI 应用开发：技术团队构建 RAG 系统和 AI Agents 的技术参考和解决方案指南
- 教育培训机构：高校或培训机构作为 AI 工程化课程的教材和实验资源库



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,757 |
| 语言 | Python |
| Forks | 8,262 |
| Issues | 912 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的 LLM 微调框架之一，支持 100+ 种大语言模型和视觉语言模型的高效微调。其最大的独特价值在于提供统一的 Web UI 和命令行接口，让开发者无需编写代码即可完成从数据预处理、模型训练到评估部署的全流程，特别在 ACL 2024 发表后已成为学术和工业界的首选微调工具之一。

**技术亮点**:
- 统一框架支持 100+ LLMs & VLMs：集成主流模型如 LLaMA、Gemma、Qwen、DeepSeek 等，避免碎片化适配
- 全栈微调方法：涵盖 LoRA、QLoRA、全量微调及 MoE 架构，支持多种 PEFT 技术的高效训练
- 零代码操作体验：提供可视化 Web UI，内置数据集管理、训练监控、模型对比等完整工具链
- RLHF 与指令调优一体化：支持监督微调和人类反馈强化学习，满足不同对齐需求
- 模型量化与推理优化：支持量化训练和高效推理部署，显著降低资源门槛

**适用场景**:
- 企业级 AI 应用定制：企业基于自有领域数据快速微调垂直行业模型（如客服、医疗、金融等），Web UI 降低技术门槛，提升 ROI
- 学术研究与实验：研究人员快速验证新算法、对比不同模型性能，统一框架节省大量工程适配时间
- 个人开发者 AI 创业：独立开发者低成本微调个性化模型（如角色扮演、教育助手），QLoRA 降本增效快速 MVP 验证



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,313 |
| 语言 | Java |
| Forks | 15,821 |
| Issues | 58 |
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
| Stars | 41,748 |
| 语言 | Python |
| Forks | 9,790 |
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
| Stars | 34,256 |
| 语言 | TypeScript |
| Forks | 6,916 |
| Issues | 429 |
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
| Stars | 32,777 |
| 语言 | Python |
| Forks | 1,986 |
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
| Stars | 32,276 |
| 语言 | TypeScript |
| Forks | 2,194 |
| Issues | 68 |
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
| Stars | 27,231 |
| 语言 | TypeScript |
| Forks | 6,941 |
| Issues | 161 |
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
| Stars | 38,614 |
| 语言 | Python |
| Forks | 6,118 |
| Issues | 192 |
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
| Stars | 31,005 |
| 语言 | Jupyter Notebook |
| Forks | 5,051 |
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
| Stars | 99,090 |
| 语言 | Python |
| Forks | 14,397 |
| Issues | 5 |
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
| Stars | 68,411 |
| 语言 | Python |
| Forks | 8,533 |
| Issues | 362 |
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
| Stars | 36,184 |
| 语言 | TypeScript |
| Forks | 2,736 |
| Issues | 267 |
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
| Stars | 79,385 |
| 语言 | Python |
| Forks | 9,384 |
| Issues | 225 |
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
| Stars | 49,476 |
| 语言 | TypeScript |
| Forks | 23,771 |
| Issues | 783 |
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
| Stars | 177,223 |
| 语言 | TypeScript |
| Forks | 55,345 |
| Issues | 1,408 |
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
| Stars | 145,197 |
| 语言 | Python |
| Forks | 8,505 |
| Issues | 1,085 |
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
| Stars | 52,463 |
| 语言 | Jupyter Notebook |
| Forks | 18,278 |
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
| Stars | 29,184 |
| 语言 | TypeScript |
| Forks | 3,085 |
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
| Stars | 29,959 |
| 语言 | Python |
| Forks | 3,282 |
| Issues | 7 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 3,925 |
| Issues | 230 |
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
| Stars | 125,468 |
| 语言 | Python |
| Forks | 17,765 |
| Issues | 270 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是当前最流行的开源LLM界面之一，拥有超过12.5万颗星，完美解决了自部署大模型缺乏友好交互界面的痛点。它不仅支持Ollama、OpenAI API等多种后端，还集成了RAG、MCP等高级功能，是构建私有化AI助手平台的最佳选择。

**技术亮点**:
- 🚀 多后端支持 - 同时支持Ollama本地部署和OpenAI API，灵活适配不同模型来源
- 🔍 内置RAG能力 - 原生集成检索增强生成功能，可直接上传文档进行知识库对话
- 🌐 完全自托管 - 可完全部署在本地/私有环境，数据隐私安全，适合企业内网使用
- 🔌 MCP协议支持 - 支持Model Context Protocol，可扩展连接更多AI工具和服务
- 💬 现代化Web界面 - 提供类似ChatGPT的友好交互体验，支持多会话管理和对话历史

**适用场景**:
- 🏢 企业私有化部署 - 适合需要在本地/私有云部署AI助手的企业，保护数据隐私不外泄
- 👨‍💻 个人开发者实验 - 适合AI爱好者在本地运行Ollama等模型，并通过友好界面进行测试和开发
- 🎓 教育与研究机构 - 适合学校和研究机构搭建内部AI教学和研究平台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,039 |
| 语言 | Python |
| Forks | 8,236 |
| Issues | 3,014 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的开源 RAG 引擎，成功融合了先进的检索增强生成技术与 Agent 能力，为 LLM 提供卓越的上下文理解层。凭借 7.4 万+ stars 的广泛认可，它支持深度研究、图检索、多模型集成等前沿特性，是构建企业级智能问答和知识管理系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，创建强大的 LLM 上下文引擎
- 内置文档解析和理解引擎，支持复杂文档处理
- 集成 GraphRAG 技术，实现知识图谱增强的检索
- 支持 MCP 协议和主流 LLM（OpenAI、DeepSeek、Ollama 等）
- 具备深度研究（deep-research）和智能工作流编排能力

**适用场景**:
- 企业知识库构建：搭建智能文档管理和问答系统，实现企业内部知识的高效检索与复用
- 智能客服与助手：开发基于企业文档的 AI 客服系统，提供精准的上下文感知服务
- AI 搜索引擎：构建具备深度理解和推理能力的垂直领域搜索引擎



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,283 |
| 语言 | JavaScript |
| Forks | 5,972 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能完备的"全栈式"AI应用解决方案，打破了开发者需要集成多个分散工具的痛点。它将 RAG、AI Agent、无代码构建器、MCP 协议支持等核心能力整合在单一应用中，支持本地 LLM（如 Ollama、LM Studio）和云端模型，为企业级和个人开发者提供了开箱即用的 AI 部署能力。作为拥有 5.5 万+ stars 的开源项目，它降低了 AI 应用开发的门槛，是构建私有化智能问答、客服机器人、知识库助手的理想选择。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库集成，可实现高质量的知识库问答
- No-code Agent 构建器，可视化拖拽即可创建自定义 AI 智能体，降低开发门槛
- 完整的 MCP（Model Context Protocol）兼容性，可无缝连接各类 MCP 服务和工具
- 支持多种本地 LLM 引擎（Ollama、LM Studio、LocalAI）及云端模型（DeepSeek、Kimi、Llama3、Qwen3 等），灵活部署
- 多模态能力支持，可处理文本、图片等多种输入格式，扩展应用场景

**适用场景**:
- 企业内部知识库助手：搭建私有化智能问答系统，员工可通过自然语言快速检索公司文档、技术手册等资源
- 无代码 AI 应用开发：非技术人员也能快速搭建定制化 AI Agent，如智能客服、数据分析助手、内容生成工具等
- 本地化 AI 部署：对数据隐私要求高的场景，可完全在本地运行 LLM 和 RAG，无需将敏感数据发送至云端



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,896 |
| 语言 | TypeScript |
| Forks | 14,708 |
| Issues | 802 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，在 GitHub 上获得了超过 7.2 万颗星，是构建、管理和部署 AI Agent 生态系统的顶级开源项目。它独特地将 Agent 作为工作交互单元，提供了从单智能体到多智能体协作的完整解决方案，特别适合需要快速搭建智能助手团队的开发者和企业。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的 Agent 团队工作流
- 集成了主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等）和 MCP 协议
- TypeScript 构建，提供类型安全和现代化的开发体验
- 零门槛的智能体团队设计，降低 AI 应用开发门槛
- 内置知识库功能，支持 Agent 与企业知识库的深度整合

**适用场景**:
- 企业级 AI 助手团队构建：快速搭建客服、销售、技术支持等多个智能体协作系统
- 个人开发者 AI 应用开发：快速原型开发和部署个性化 AI Agent
- 知识库智能问答：结合企业知识库构建智能的文档检索和问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,026 |
| 语言 | MDX |
| Forks | 7,563 |
| Issues | 245 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个专注于提示工程（Prompt Engineering）的综合性知识库项目，由知名 AI 研究机构 dair-ai 维护，涵盖提示工程、上下文工程、RAG 和 AI Agents 等前沿技术。该项目获得了超过 7 万星标，提供了从入门指南到学术论文、实战代码的全方位资源，是学习大语言模型应用开发的权威参考资料。

**技术亮点**:
- 覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 集成多种学习资源：指南文档、学术论文、实战教程、可交互的 Notebook 代码示例
- 紧跟技术前沿，涵盖 ChatGPT、OpenAI、LLMs、生成式 AI 等热门技术栈
- 采用 MDX 格式组织内容，结构清晰便于学习查阅和技术分享
- 开源且社区活跃，持续更新最新的 AI 代理和检索增强生成技术

**适用场景**:
- 个人开发者学习：大语言模型应用开发初学者，系统学习提示工程技巧和最佳实践
- 企业 AI 应用开发：技术团队构建 RAG 系统和 AI Agents 的技术参考和解决方案指南
- 教育培训机构：高校或培训机构作为 AI 工程化课程的教材和实验资源库



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,313 |
| 语言 | Java |
| Forks | 15,821 |
| Issues | 58 |
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
| Stars | 32,777 |
| 语言 | Python |
| Forks | 1,986 |
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
| Stars | 32,276 |
| 语言 | TypeScript |
| Forks | 2,194 |
| Issues | 68 |
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
| Stars | 27,231 |
| 语言 | TypeScript |
| Forks | 6,941 |
| Issues | 161 |
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
| Stars | 38,614 |
| 语言 | Python |
| Forks | 6,118 |
| Issues | 192 |
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
| Stars | 31,005 |
| 语言 | Jupyter Notebook |
| Forks | 5,051 |
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
| Stars | 99,090 |
| 语言 | Python |
| Forks | 14,397 |
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
| Stars | 98,427 |
| 语言 | TypeScript |
| Forks | 11,693 |
| Issues | 961 |
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
| Stars | 49,476 |
| 语言 | TypeScript |
| Forks | 23,771 |
| Issues | 783 |
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
| Stars | 71,436 |
| 语言 | Python |
| Forks | 9,879 |
| Issues | 260 |
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
| Stars | 43,085 |
| 语言 | Go |
| Forks | 3,867 |
| Issues | 1,022 |
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
| Stars | 31,176 |
| 语言 | Python |
| Forks | 3,284 |
| Issues | 65 |
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
| Stars | 29,184 |
| 语言 | TypeScript |
| Forks | 3,085 |
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
| Stars | 125,468 |
| 语言 | Python |
| Forks | 17,765 |
| Issues | 270 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI是当前最流行的开源LLM界面之一，拥有超过12.5万颗星，完美解决了自部署大模型缺乏友好交互界面的痛点。它不仅支持Ollama、OpenAI API等多种后端，还集成了RAG、MCP等高级功能，是构建私有化AI助手平台的最佳选择。

**技术亮点**:
- 🚀 多后端支持 - 同时支持Ollama本地部署和OpenAI API，灵活适配不同模型来源
- 🔍 内置RAG能力 - 原生集成检索增强生成功能，可直接上传文档进行知识库对话
- 🌐 完全自托管 - 可完全部署在本地/私有环境，数据隐私安全，适合企业内网使用
- 🔌 MCP协议支持 - 支持Model Context Protocol，可扩展连接更多AI工具和服务
- 💬 现代化Web界面 - 提供类似ChatGPT的友好交互体验，支持多会话管理和对话历史

**适用场景**:
- 🏢 企业私有化部署 - 适合需要在本地/私有云部署AI助手的企业，保护数据隐私不外泄
- 👨‍💻 个人开发者实验 - 适合AI爱好者在本地运行Ollama等模型，并通过友好界面进行测试和开发
- 🎓 教育与研究机构 - 适合学校和研究机构搭建内部AI教学和研究平台



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,039 |
| 语言 | Python |
| Forks | 8,236 |
| Issues | 3,014 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款领先的开源 RAG 引擎，成功融合了先进的检索增强生成技术与 Agent 能力，为 LLM 提供卓越的上下文理解层。凭借 7.4 万+ stars 的广泛认可，它支持深度研究、图检索、多模型集成等前沿特性，是构建企业级智能问答和知识管理系统的理想选择。

**技术亮点**:
- 融合 RAG 与 Agent 能力，创建强大的 LLM 上下文引擎
- 内置文档解析和理解引擎，支持复杂文档处理
- 集成 GraphRAG 技术，实现知识图谱增强的检索
- 支持 MCP 协议和主流 LLM（OpenAI、DeepSeek、Ollama 等）
- 具备深度研究（deep-research）和智能工作流编排能力

**适用场景**:
- 企业知识库构建：搭建智能文档管理和问答系统，实现企业内部知识的高效检索与复用
- 智能客服与助手：开发基于企业文档的 AI 客服系统，提供精准的上下文感知服务
- AI 搜索引擎：构建具备深度理解和推理能力的垂直领域搜索引擎



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,107 |
| 语言 | JavaScript |
| Forks | 7,046 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code、Codex 等 AI 代理系统的性能优化工具集，整合了技能库、记忆系统、安全防护和研究优先的开发方法论。凭借超过 5.7 万颗星和 MIT 许可证，该项目为开发者提供了完整的 AI 代理增强方案，显著提升 Claude Code 等工具的生产力表现。

**技术亮点**:
- 集成 MCP (Model Context Protocol) 协议支持，实现高效的模型上下文管理
- 构建多维度 AI Agent 能力体系：技能、直觉、记忆、安全和研究
- 支持 Claude Code、Codex、Cowork 等多种 Anthropic AI 生态产品
- 研究优先的开发模式，持续优化 AI 代理的表现和响应质量
- 完整的开发者工具链，提升 AI 辅助编程的工作流效率

**适用场景**:
- 企业级开发团队：集成 AI 代理优化系统，提升团队使用 Claude Code 的协作效率和代码质量
- 个人开发者/自由职业者：通过增强的 AI 代理能力，加速日常开发任务和问题解决流程
- AI 应用研究者：基于项目提供的研究优先方法论，探索和实验 AI 代理的新功能和性能优化方案



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,283 |
| 语言 | JavaScript |
| Forks | 5,972 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能完备的"全栈式"AI应用解决方案，打破了开发者需要集成多个分散工具的痛点。它将 RAG、AI Agent、无代码构建器、MCP 协议支持等核心能力整合在单一应用中，支持本地 LLM（如 Ollama、LM Studio）和云端模型，为企业级和个人开发者提供了开箱即用的 AI 部署能力。作为拥有 5.5 万+ stars 的开源项目，它降低了 AI 应用开发的门槛，是构建私有化智能问答、客服机器人、知识库助手的理想选择。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库集成，可实现高质量的知识库问答
- No-code Agent 构建器，可视化拖拽即可创建自定义 AI 智能体，降低开发门槛
- 完整的 MCP（Model Context Protocol）兼容性，可无缝连接各类 MCP 服务和工具
- 支持多种本地 LLM 引擎（Ollama、LM Studio、LocalAI）及云端模型（DeepSeek、Kimi、Llama3、Qwen3 等），灵活部署
- 多模态能力支持，可处理文本、图片等多种输入格式，扩展应用场景

**适用场景**:
- 企业内部知识库助手：搭建私有化智能问答系统，员工可通过自然语言快速检索公司文档、技术手册等资源
- 无代码 AI 应用开发：非技术人员也能快速搭建定制化 AI Agent，如智能客服、数据分析助手、内容生成工具等
- 本地化 AI 部署：对数据隐私要求高的场景，可完全在本地运行 LLM 和 RAG，无需将敏感数据发送至云端



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,896 |
| 语言 | TypeScript |
| Forks | 14,708 |
| Issues | 802 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，在 GitHub 上获得了超过 7.2 万颗星，是构建、管理和部署 AI Agent 生态系统的顶级开源项目。它独特地将 Agent 作为工作交互单元，提供了从单智能体到多智能体协作的完整解决方案，特别适合需要快速搭建智能助手团队的开发者和企业。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的 Agent 团队工作流
- 集成了主流 AI 模型（ChatGPT、Claude、Gemini、DeepSeek 等）和 MCP 协议
- TypeScript 构建，提供类型安全和现代化的开发体验
- 零门槛的智能体团队设计，降低 AI 应用开发门槛
- 内置知识库功能，支持 Agent 与企业知识库的深度整合

**适用场景**:
- 企业级 AI 助手团队构建：快速搭建客服、销售、技术支持等多个智能体协作系统
- 个人开发者 AI 应用开发：快速原型开发和部署个性化 AI Agent
- 知识库智能问答：结合企业知识库构建智能的文档检索和问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,026 |
| 语言 | MDX |
| Forks | 7,563 |
| Issues | 245 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个专注于提示工程（Prompt Engineering）的综合性知识库项目，由知名 AI 研究机构 dair-ai 维护，涵盖提示工程、上下文工程、RAG 和 AI Agents 等前沿技术。该项目获得了超过 7 万星标，提供了从入门指南到学术论文、实战代码的全方位资源，是学习大语言模型应用开发的权威参考资料。

**技术亮点**:
- 覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 集成多种学习资源：指南文档、学术论文、实战教程、可交互的 Notebook 代码示例
- 紧跟技术前沿，涵盖 ChatGPT、OpenAI、LLMs、生成式 AI 等热门技术栈
- 采用 MDX 格式组织内容，结构清晰便于学习查阅和技术分享
- 开源且社区活跃，持续更新最新的 AI 代理和检索增强生成技术

**适用场景**:
- 个人开发者学习：大语言模型应用开发初学者，系统学习提示工程技巧和最佳实践
- 企业 AI 应用开发：技术团队构建 RAG 系统和 AI Agents 的技术参考和解决方案指南
- 教育培训机构：高校或培训机构作为 AI 工程化课程的教材和实验资源库



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,699 |
| 语言 | HTML |
| Forks | 19,682 |
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
| Stars | 86,711 |
| 语言 | Jupyter Notebook |
| Forks | 13,160 |
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
| Stars | 41,748 |
| 语言 | Python |
| Forks | 9,790 |
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
| Stars | 34,256 |
| 语言 | TypeScript |
| Forks | 6,916 |
| Issues | 429 |
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
| Stars | 32,777 |
| 语言 | Python |
| Forks | 1,986 |
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
| Stars | 32,276 |
| 语言 | TypeScript |
| Forks | 2,194 |
| Issues | 68 |
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
| Stars | 27,231 |
| 语言 | TypeScript |
| Forks | 6,941 |
| Issues | 161 |
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
| Stars | 68,411 |
| 语言 | Python |
| Forks | 8,533 |
| Issues | 362 |
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
| Stars | 36,184 |
| 语言 | TypeScript |
| Forks | 2,736 |
| Issues | 267 |
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
| Stars | 49,476 |
| 语言 | TypeScript |
| Forks | 23,771 |
| Issues | 783 |
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
| Stars | 33,504 |
| 语言 | HTML |
| Forks | 5,333 |
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
| Stars | 71,691 |
| 语言 | Python |
| Forks | 13,859 |
| Issues | 3,553 |
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
| Stars | 36,184 |
| 语言 | Python |
| Forks | 3,545 |
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
| Stars | 145,197 |
| 语言 | Python |
| Forks | 8,505 |
| Issues | 1,085 |
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
| Stars | 163,860 |
| 语言 | Go |
| Forks | 14,734 |
| Issues | 2,535 |
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
| Stars | 46,224 |
| 语言 | Rust |
| Forks | 9,058 |
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
| Stars | 29,959 |
| 语言 | Python |
| Forks | 3,282 |
| Issues | 7 |
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
| Stars | 38,728 |
| 语言 | TypeScript |
| Forks | 3,918 |
| Issues | 1,053 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 3,925 |
| Issues | 230 |
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
| Stars | 89,503 |
| 语言 | Python |
| Forks | 5,245 |
| Issues | 439 |
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
| Stars | 71,026 |
| 语言 | MDX |
| Forks | 7,563 |
| Issues | 245 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个专注于提示工程（Prompt Engineering）的综合性知识库项目，由知名 AI 研究机构 dair-ai 维护，涵盖提示工程、上下文工程、RAG 和 AI Agents 等前沿技术。该项目获得了超过 7 万星标，提供了从入门指南到学术论文、实战代码的全方位资源，是学习大语言模型应用开发的权威参考资料。

**技术亮点**:
- 覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 集成多种学习资源：指南文档、学术论文、实战教程、可交互的 Notebook 代码示例
- 紧跟技术前沿，涵盖 ChatGPT、OpenAI、LLMs、生成式 AI 等热门技术栈
- 采用 MDX 格式组织内容，结构清晰便于学习查阅和技术分享
- 开源且社区活跃，持续更新最新的 AI 代理和检索增强生成技术

**适用场景**:
- 个人开发者学习：大语言模型应用开发初学者，系统学习提示工程技巧和最佳实践
- 企业 AI 应用开发：技术团队构建 RAG 系统和 AI Agents 的技术参考和解决方案指南
- 教育培训机构：高校或培训机构作为 AI 工程化课程的教材和实验资源库



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,757 |
| 语言 | Python |
| Forks | 8,262 |
| Issues | 912 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最全面的 LLM 微调框架之一，支持 100+ 种大语言模型和视觉语言模型的高效微调。其最大的独特价值在于提供统一的 Web UI 和命令行接口，让开发者无需编写代码即可完成从数据预处理、模型训练到评估部署的全流程，特别在 ACL 2024 发表后已成为学术和工业界的首选微调工具之一。

**技术亮点**:
- 统一框架支持 100+ LLMs & VLMs：集成主流模型如 LLaMA、Gemma、Qwen、DeepSeek 等，避免碎片化适配
- 全栈微调方法：涵盖 LoRA、QLoRA、全量微调及 MoE 架构，支持多种 PEFT 技术的高效训练
- 零代码操作体验：提供可视化 Web UI，内置数据集管理、训练监控、模型对比等完整工具链
- RLHF 与指令调优一体化：支持监督微调和人类反馈强化学习，满足不同对齐需求
- 模型量化与推理优化：支持量化训练和高效推理部署，显著降低资源门槛

**适用场景**:
- 企业级 AI 应用定制：企业基于自有领域数据快速微调垂直行业模型（如客服、医疗、金融等），Web UI 降低技术门槛，提升 ROI
- 学术研究与实验：研究人员快速验证新算法、对比不同模型性能，统一框架节省大量工程适配时间
- 个人开发者 AI 创业：独立开发者低成本微调个性化模型（如角色扮演、教育助手），QLoRA 降本增效快速 MVP 验证



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,417 |
| 语言 | Python |
| Forks | 6,095 |
| Issues | 67 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是一个功能强大的开源金融数据平台，凭借62k+星标成为Python量化金融领域最受欢迎的项目。它提供统一接口访问全球金融数据（股票、期权、加密货币、经济指标等），特别适合AI智能体集成，是金融分析师、量化开发者和数据科学家的必备工具。

**技术亮点**:
- 统一API接口：整合多个数据源，提供一致的Python接口访问股票、期权、加密货币、固定收益等多种金融数据
- AI友好架构：专为AI智能体设计，支持机器学习模型训练和量化策略回测的完整数据管道
- 多资产类别覆盖：涵盖传统金融（股票、衍生品、固定收益）和加密货币领域
- 开源可扩展：基于Python构建，社区活跃，支持自定义插件和工作流集成
- 专业级数据质量：提供机构级别的金融数据清洗和标准化处理

**适用场景**:
- 量化交易策略开发：为个人开发者或量化团队构建、测试和优化交易算法提供全面的历史和实时金融数据
- AI金融智能体构建：为AI Agent提供结构化金融数据接口，实现自动化投资分析和决策支持
- 金融研究与报告生成：帮助分析师快速获取经济指标、市场数据，生成专业的投资研究报告



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,699 |
| 语言 | HTML |
| Forks | 19,682 |
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
| Stars | 86,711 |
| 语言 | Jupyter Notebook |
| Forks | 13,160 |
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
| Stars | 31,005 |
| 语言 | Jupyter Notebook |
| Forks | 5,051 |
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
| Stars | 157,273 |
| 语言 | Python |
| Forks | 32,266 |
| Issues | 2,277 |
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
| Stars | 71,691 |
| 语言 | Python |
| Forks | 13,859 |
| Issues | 3,553 |
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
| Stars | 161,451 |
| 语言 | Python |
| Forks | 30,100 |
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
| Stars | 104,693 |
| 语言 | Python |
| Forks | 11,981 |
| Issues | 3,779 |
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
| Stars | 97,888 |
| 语言 | Python |
| Forks | 27,038 |
| Issues | 18,076 |
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
| Stars | 29,184 |
| 语言 | TypeScript |
| Forks | 3,085 |
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
| Stars | 75,952 |
| 语言 | Unknown |
| Forks | 8,760 |
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
| Stars | 57,107 |
| 语言 | JavaScript |
| Forks | 7,046 |
| Issues | 24 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个针对 Claude Code、Codex 等 AI 代理系统的性能优化工具集，整合了技能库、记忆系统、安全防护和研究优先的开发方法论。凭借超过 5.7 万颗星和 MIT 许可证，该项目为开发者提供了完整的 AI 代理增强方案，显著提升 Claude Code 等工具的生产力表现。

**技术亮点**:
- 集成 MCP (Model Context Protocol) 协议支持，实现高效的模型上下文管理
- 构建多维度 AI Agent 能力体系：技能、直觉、记忆、安全和研究
- 支持 Claude Code、Codex、Cowork 等多种 Anthropic AI 生态产品
- 研究优先的开发模式，持续优化 AI 代理的表现和响应质量
- 完整的开发者工具链，提升 AI 辅助编程的工作流效率

**适用场景**:
- 企业级开发团队：集成 AI 代理优化系统，提升团队使用 Claude Code 的协作效率和代码质量
- 个人开发者/自由职业者：通过增强的 AI 代理能力，加速日常开发任务和问题解决流程
- AI 应用研究者：基于项目提供的研究优先方法论，探索和实验 AI 代理的新功能和性能优化方案



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,186 |
| 语言 | Go |
| Forks | 3,612 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源项目，作为 OpenAI、Claude 等商业 AI 服务的免费替代方案，能够在普通消费级硬件上本地运行，无需 GPU。它支持多种主流模型格式（gguf、transformers、diffusers），并提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到本地化 AI 解决方案，同时保护数据隐私和安全性。

**技术亮点**:
- 🚀 多模态 AI 能力：支持文本、音频、视频、图像生成、语音克隆、目标检测等多种 AI 任务
- 🔌 API 兼容性：提供 OpenAI API 的直接替换接口，实现零成本迁移和集成
- 💻 硬件友好：无需 GPU，可在消费级硬件上运行，支持 CPU 推理
- 🌐 分布式架构：基于 libp2p 实现 P2P 和去中心化推理，支持分布式计算
- 🎯 模型生态广泛：支持 Llama、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求高的行业，可在本地环境部署 AI 能力，避免数据外泄
- 👨‍💻 个人开发者实验：在个人电脑上测试和开发 AI 应用，无需支付昂贵的 API 调用费用
- 🔒 离线场景应用：无网络环境或需要本地推理的边缘计算场景，如 IoT 设备、内网系统



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,411 |
| 语言 | Python |
| Forks | 8,533 |
| Issues | 362 |
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
| Stars | 36,184 |
| 语言 | TypeScript |
| Forks | 2,736 |
| Issues | 267 |
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
| Stars | 177,223 |
| 语言 | TypeScript |
| Forks | 55,345 |
| Issues | 1,408 |
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
| Stars | 149,268 |
| 语言 | Python |
| Forks | 12,099 |
| Issues | 2,346 |
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
| Stars | 95,764 |
| 语言 | Python |
| Forks | 8,773 |
| Issues | 155 |
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
| Stars | 73,293 |
| 语言 | Python |
| Forks | 8,691 |
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
| Stars | 182,213 |
| 语言 | TypeScript |
| Forks | 38,238 |
| Issues | 14,464 |
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
| Stars | 93,688 |
| 语言 | TypeScript |
| Forks | 9,376 |
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
| Stars | 77,984 |
| 语言 | TypeScript |
| Forks | 5,605 |
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
| Stars | 76,437 |
| 语言 | TypeScript |
| Forks | 6,532 |
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
| Stars | 75,632 |
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
| Stars | 78,258 |
| 语言 | Go |
| Forks | 2,699 |
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
| Stars | 73,335 |
| 语言 | Go |
| Forks | 2,553 |
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
| Stars | 42,855 |
| 语言 | Go |
| Forks | 8,005 |
| Issues | 947 |
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
| Stars | 402,865 |
| 语言 | Python |
| Forks | 43,343 |
| Issues | 903 |
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
| Stars | 36,184 |
| 语言 | TypeScript |
| Forks | 2,736 |
| Issues | 267 |
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
| Stars | 177,223 |
| 语言 | TypeScript |
| Forks | 55,345 |
| Issues | 1,408 |
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
| Stars | 51,596 |
| 语言 | Go |
| Forks | 10,328 |
| Issues | 223 |
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
| Stars | 120,868 |
| 语言 | Go |
| Forks | 42,570 |
| Issues | 2,674 |
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
| Stars | 71,462 |
| 语言 | Go |
| Forks | 18,913 |
| Issues | 3,793 |
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
| Stars | 54,004 |
| 语言 | Go |
| Forks | 6,415 |
| Issues | 2,839 |
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
| Stars | 47,542 |
| 语言 | Go |
| Forks | 5,067 |
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
| Stars | 29,959 |
| 语言 | Python |
| Forks | 3,282 |
| Issues | 7 |
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
| Stars | 93,688 |
| 语言 | TypeScript |
| Forks | 9,376 |
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
| Stars | 83,330 |
| 语言 | TypeScript |
| Forks | 5,219 |
| Issues | 602 |
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
| Stars | 74,821 |
| 语言 | TypeScript |
| Forks | 6,341 |
| Issues | 406 |
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
| Stars | 83,470 |
| 语言 | JavaScript |
| Forks | 7,464 |
| Issues | 696 |
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
| Stars | 69,089 |
| 语言 | Go |
| Forks | 1,864 |
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
| Stars | 62,005 |
| 语言 | Go |
| Forks | 5,849 |
| Issues | 775 |
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
| Stars | 57,412 |
| 语言 | Go |
| Forks | 4,147 |
| Issues | 44 |
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
| Stars | 39,643 |
| 语言 | Python |
| Forks | 3,925 |
| Issues | 230 |
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
| Stars | 60,406 |
| 语言 | Go |
| Forks | 7,162 |
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
| Stars | 83,470 |
| 语言 | JavaScript |
| Forks | 7,464 |
| Issues | 696 |
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
| Stars | 62,997 |
| 语言 | Go |
| Forks | 10,211 |
| Issues | 757 |
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
| Stars | 43,186 |
| 语言 | Go |
| Forks | 3,612 |
| Issues | 148 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个革命性的开源项目，作为 OpenAI、Claude 等商业 AI 服务的免费替代方案，能够在普通消费级硬件上本地运行，无需 GPU。它支持多种主流模型格式（gguf、transformers、diffusers），并提供与 OpenAI API 兼容的接口，让开发者可以零成本切换到本地化 AI 解决方案，同时保护数据隐私和安全性。

**技术亮点**:
- 🚀 多模态 AI 能力：支持文本、音频、视频、图像生成、语音克隆、目标检测等多种 AI 任务
- 🔌 API 兼容性：提供 OpenAI API 的直接替换接口，实现零成本迁移和集成
- 💻 硬件友好：无需 GPU，可在消费级硬件上运行，支持 CPU 推理
- 🌐 分布式架构：基于 libp2p 实现 P2P 和去中心化推理，支持分布式计算
- 🎯 模型生态广泛：支持 Llama、Mistral、Gemma、Stable Diffusion、RWKV、Mamba 等主流开源模型

**适用场景**:
- 🏢 企业私有化部署：金融、医疗等对数据隐私要求高的行业，可在本地环境部署 AI 能力，避免数据外泄
- 👨‍💻 个人开发者实验：在个人电脑上测试和开发 AI 应用，无需支付昂贵的 API 调用费用
- 🔒 离线场景应用：无网络环境或需要本地推理的边缘计算场景，如 IoT 设备、内网系统



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,764 |
| 语言 | Python |
| Forks | 8,773 |
| Issues | 155 |
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
| Stars | 86,968 |
| 语言 | Python |
| Forks | 33,708 |
| Issues | 421 |
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
| Stars | 100,044 |
| 语言 | TypeScript |
| Forks | 27,094 |
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
| Stars | 77,984 |
| 语言 | TypeScript |
| Forks | 5,605 |
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
| Stars | 74,826 |
| 语言 | TypeScript |
| Forks | 8,231 |
| Issues | 49 |
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
| Stars | 75,632 |
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
| Stars | 68,841 |
| 语言 | JavaScript |
| Forks | 22,693 |
| Issues | 191 |
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
| Stars | 55,948 |
| 语言 | JavaScript |
| Forks | 10,223 |
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
| Stars | 88,175 |
| 语言 | Go |
| Forks | 8,561 |
| Issues | 641 |
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
| Stars | 70,505 |
| 语言 | Go |
| Forks | 4,656 |
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
| Stars | 56,497 |
| 语言 | Go |
| Forks | 3,158 |
| Issues | 23 |
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
| Stars | 402,865 |
| 语言 | Python |
| Forks | 43,343 |
| Issues | 903 |
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
| Stars | 55,283 |
| 语言 | JavaScript |
| Forks | 5,972 |
| Issues | 297 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能完备的"全栈式"AI应用解决方案，打破了开发者需要集成多个分散工具的痛点。它将 RAG、AI Agent、无代码构建器、MCP 协议支持等核心能力整合在单一应用中，支持本地 LLM（如 Ollama、LM Studio）和云端模型，为企业级和个人开发者提供了开箱即用的 AI 部署能力。作为拥有 5.5 万+ stars 的开源项目，它降低了 AI 应用开发的门槛，是构建私有化智能问答、客服机器人、知识库助手的理想选择。

**技术亮点**:
- 内置 RAG（检索增强生成）引擎，支持向量化数据库集成，可实现高质量的知识库问答
- No-code Agent 构建器，可视化拖拽即可创建自定义 AI 智能体，降低开发门槛
- 完整的 MCP（Model Context Protocol）兼容性，可无缝连接各类 MCP 服务和工具
- 支持多种本地 LLM 引擎（Ollama、LM Studio、LocalAI）及云端模型（DeepSeek、Kimi、Llama3、Qwen3 等），灵活部署
- 多模态能力支持，可处理文本、图片等多种输入格式，扩展应用场景

**适用场景**:
- 企业内部知识库助手：搭建私有化智能问答系统，员工可通过自然语言快速检索公司文档、技术手册等资源
- 无代码 AI 应用开发：非技术人员也能快速搭建定制化 AI Agent，如智能客服、数据分析助手、内容生成工具等
- 本地化 AI 部署：对数据隐私要求高的场景，可完全在本地运行 LLM 和 RAG，无需将敏感数据发送至云端



### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,427 |
| 语言 | TypeScript |
| Forks | 11,693 |
| Issues | 961 |
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
| Stars | 43,085 |
| 语言 | Go |
| Forks | 3,867 |
| Issues | 1,022 |
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
| Stars | 51,596 |
| 语言 | Go |
| Forks | 10,328 |
| Issues | 223 |
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
| Stars | 71,026 |
| 语言 | MDX |
| Forks | 7,563 |
| Issues | 245 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是一个专注于提示工程（Prompt Engineering）的综合性知识库项目，由知名 AI 研究机构 dair-ai 维护，涵盖提示工程、上下文工程、RAG 和 AI Agents 等前沿技术。该项目获得了超过 7 万星标，提供了从入门指南到学术论文、实战代码的全方位资源，是学习大语言模型应用开发的权威参考资料。

**技术亮点**:
- 覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 集成多种学习资源：指南文档、学术论文、实战教程、可交互的 Notebook 代码示例
- 紧跟技术前沿，涵盖 ChatGPT、OpenAI、LLMs、生成式 AI 等热门技术栈
- 采用 MDX 格式组织内容，结构清晰便于学习查阅和技术分享
- 开源且社区活跃，持续更新最新的 AI 代理和检索增强生成技术

**适用场景**:
- 个人开发者学习：大语言模型应用开发初学者，系统学习提示工程技巧和最佳实践
- 企业 AI 应用开发：技术团队构建 RAG 系统和 AI Agents 的技术参考和解决方案指南
- 教育培训机构：高校或培训机构作为 AI 工程化课程的教材和实验资源库



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 149,699 |
| 语言 | HTML |
| Forks | 19,682 |
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
| Stars | 33,504 |
| 语言 | HTML |
| Forks | 5,333 |
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
| Stars | 89,344 |
| 语言 | TypeScript |
| Forks | 9,880 |
| Issues | 2,235 |
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
| Stars | 86,400 |
| 语言 | TypeScript |
| Forks | 8,670 |
| Issues | 1,625 |
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
| Stars | 126,922 |
| 语言 | JavaScript |
| Forks | 12,442 |
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
| Stars | 99,437 |
| 语言 | JavaScript |
| Forks | 7,446 |
| Issues | 198 |
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
| Stars | 166,381 |
| 语言 | Go |
| Forks | 12,997 |
| Issues | 171 |
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
| Stars | 40,539 |
| 语言 | TypeScript |
| Forks | 3,740 |
| Issues | 667 |
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
| Stars | 247,346 |
| 语言 | TypeScript |
| Forks | 47,746 |
| Issues | 10,144 |
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
| Stars | 61,244 |
| 语言 | Python |
| Forks | 6,260 |
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
| Stars | 79,755 |
| 语言 | Python |
| Forks | 11,627 |
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
| Stars | 73,328 |
| 语言 | Python |
| Forks | 6,290 |
| Issues | 637 |
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
| Stars | 127,212 |
| 语言 | Unknown |
| Forks | 32,529 |
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
| Stars | 383,510 |
| 语言 | Python |
| Forks | 66,005 |
| Issues | 74 |
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
| Stars | 112,313 |
| 语言 | TypeScript |
| Forks | 5,662 |
| Issues | 319 |
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
| Stars | 99,893 |
| 语言 | TypeScript |
| Forks | 7,273 |
| Issues | 166 |
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
| Stars | 47,852 |
| 语言 | Go |
| Forks | 10,228 |
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
| Stars | 96,357 |
| 语言 | C++ |
| Forks | 15,181 |
| Issues | 1,168 |
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
| Stars | 59,533 |
| 语言 | Python |
| Forks | 1,608 |
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
| Stars | 285,242 |
| 语言 | Python |
| Forks | 27,272 |
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
| Stars | 218,271 |
| 语言 | Python |
| Forks | 50,124 |
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
| Stars | 85,088 |
| 语言 | Python |
| Forks | 36,882 |
| Issues | 3,462 |
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
| Stars | 77,689 |
| 语言 | Python |
| Forks | 45,264 |
| Issues | 1,278 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,646 |
| 语言 | Python |
| Forks | 16,699 |
| Issues | 13 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### python/cpython

**描述**: The Python programming language

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,779 |
| 语言 | Python |
| Forks | 34,155 |
| Issues | 9,305 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 437,685 |
| 语言 | TypeScript |
| Forks | 43,496 |
| Issues | 321 |
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
| Stars | 350,025 |
| 语言 | TypeScript |
| Forks | 43,725 |
| Issues | 44 |
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
| Stars | 117,833 |
| 语言 | TypeScript |
| Forks | 12,704 |
| Issues | 2,838 |
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
| Stars | 107,995 |
| 语言 | TypeScript |
| Forks | 13,244 |
| Issues | 5,476 |
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
| Stars | 107,581 |
| 语言 | TypeScript |
| Forks | 7,990 |
| Issues | 1,778 |
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
| Stars | 97,648 |
| 语言 | TypeScript |
| Forks | 54,537 |
| Issues | 1,375 |
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
| Stars | 93,882 |
| 语言 | TypeScript |
| Forks | 4,993 |
| Issues | 679 |
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
| Stars | 93,873 |
| 语言 | TypeScript |
| Forks | 5,092 |
| Issues | 83 |
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
| Stars | 82,895 |
| 语言 | TypeScript |
| Forks | 7,566 |
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
| Stars | 79,882 |
| 语言 | TypeScript |
| Forks | 9,723 |
| Issues | 407 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,531 |
| 语言 | TypeScript |
| Forks | 7,867 |
| Issues | 633 |
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
| Stars | 243,440 |
| 语言 | JavaScript |
| Forks | 50,623 |
| Issues | 1,146 |
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
| Stars | 148,090 |
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
| Stars | 138,083 |
| 语言 | JavaScript |
| Forks | 30,525 |
| Issues | 3,422 |
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
| Stars | 116,026 |
| 语言 | JavaScript |
| Forks | 34,900 |
| Issues | 2,505 |
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
| Stars | 111,136 |
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
| Stars | 108,578 |
| 语言 | JavaScript |
| Forks | 11,539 |
| Issues | 340 |
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
| Stars | 97,987 |
| 语言 | JavaScript |
| Forks | 32,718 |
| Issues | 1,729 |
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
| Stars | 95,372 |
| 语言 | JavaScript |
| Forks | 15,186 |
| Issues | 66 |
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
| Stars | 85,951 |
| 语言 | JavaScript |
| Forks | 4,786 |
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
| Stars | 78,574 |
| 语言 | JavaScript |
| Forks | 31,152 |
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
| Stars | 70,660 |
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
| Stars | 67,205 |
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
| Stars | 66,263 |
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
| Stars | 66,014 |
| 语言 | JavaScript |
| Forks | 9,293 |
| Issues | 207 |
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
| Stars | 61,870 |
| 语言 | JavaScript |
| Forks | 3,962 |
| Issues | 18 |
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
| Stars | 61,574 |
| 语言 | JavaScript |
| Forks | 7,127 |
| Issues | 118 |
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
| Stars | 59,845 |
| 语言 | JavaScript |
| Forks | 20,476 |
| Issues | 98 |
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
| Stars | 59,615 |
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
| Stars | 57,395 |
| 语言 | JavaScript |
| Forks | 12,311 |
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
| Stars | 132,834 |
| 语言 | Go |
| Forks | 18,832 |
| Issues | 9,820 |
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
| Stars | 104,809 |
| 语言 | Go |
| Forks | 14,918 |
| Issues | 36 |
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
| Stars | 86,865 |
| 语言 | Go |
| Forks | 8,198 |
| Issues | 269 |
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
| Stars | 80,460 |
| 语言 | Go |
| Forks | 4,947 |
| Issues | 401 |
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
| Stars | 68,718 |
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
| Stars | 55,808 |
| 语言 | Go |
| Forks | 4,941 |
| Issues | 1,126 |
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
| Stars | 50,880 |
| 语言 | Go |
| Forks | 21,824 |
| Issues | 386 |
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
| Stars | 49,092 |
| 语言 | Go |
| Forks | 7,984 |
| Issues | 584 |
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
| Stars | 45,163 |
| 语言 | Go |
| Forks | 3,738 |
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
| Stars | 144,443 |
| 语言 | Python |
| Forks | 11,143 |
| Issues | 281 |
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
| Stars | 139,763 |
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
| Stars | 84,934 |
| 语言 | Python |
| Forks | 7,147 |
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
| Stars | 195,703 |
| 语言 | JavaScript |
| Forks | 31,120 |
| Issues | 392 |
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
| Stars | 76,382 |
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
| Stars | 66,693 |
| 语言 | JavaScript |
| Forks | 4,464 |
| Issues | 92 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |
