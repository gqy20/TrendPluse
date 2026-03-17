# 项目发现报告 (2026-03-17)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 31 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 26 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 66 |

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


## 🤖 AI Agents (26 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,576 |
| 语言 | Python |
| Forks | 18,035 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 界面工具，支持多种主流 LLM 后端（Ollama、OpenAI API 等），让用户无需编码即可快速搭建私有化 AI 助手平台。其超过 12 万 Star 的超高人气证明了它在 AI 应用落地领域的巨大价值和可靠性。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 服务，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库问答，增强 AI 响应准确性
- 支持 MCP（Model Context Protocol）协议：实现与外部工具和数据源的无缝集成
- 完全自托管与隐私保护：可私有化部署，数据完全掌控，适合对隐私要求高的场景
- 现代化的 Web UI 设计：用户友好的聊天界面，支持多用户、权限管理和对话历史

**适用场景**:
- 企业内部 AI 助手平台：自建私有化 ChatGPT 替代方案，保护敏感数据不外泄
- 开发者本地 LLM 调试与测试：结合 Ollama 快速搭建本地 AI 开发环境，支持 RAG 和多模型对比
- 团队知识库问答系统：上传企业文档构建专属知识库，实现智能文档检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,264 |
| 语言 | Python |
| Forks | 8,427 |
| Issues | 3,110 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，将前沿的检索增强生成技术与 Agent 智能体能力深度融合，为大语言模型提供高质量上下文层。75k+ Stars 和丰富的功能生态使其成为企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 和智能体协作，实现更复杂的推理和任务执行
- 深度集成 DeepSeek、OpenAI、Ollama 等主流 LLM，以及 MCP 协议，生态兼容性强
- 内置强大的文档解析和文档理解能力，支持复杂文档结构化提取与知识库构建
- 支持 GraphRAG 图检索技术，提升多跳推理和复杂语义关联能力
- 提供 AI 搜索和深度研究功能，适用于知识密集型场景的上下文工程

**适用场景**:
- 企业知识库搭建：快速构建基于私有文档的智能问答系统，支持多格式文档解析
- AI Agent 应用开发：构建具备知识检索能力的智能体，完成复杂业务流程自动化
- 深度研究与报告生成：结合 RAG 和推理能力，自动从海量文档中提取信息并生成分析报告



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 94,362 |
| 语言 | TypeScript |
| Forks | 6,484 |
| Issues | 219 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一款专为 AI 应用设计的网页数据提取工具，能够将任何网站内容转换为 LLM 可直接使用的 Markdown 或结构化数据，解决了 AI 开发中最棘手的网页数据预处理问题。其 9.4 万+ Stars 证明了其在 AI 爬虫领域的领先地位和社区认可度。

**技术亮点**:
- 支持将完整网站（包括多页面爬取）转换为 LLM-ready 的 Markdown 格式，无需额外数据清洗
- 提供 Web Data API 接口，支持结构化数据提取，可直接对接各类 AI 应用和 Agent
- 内置智能爬虫能力，支持动态网页渲染、JavaScript 执行等复杂场景
- 提供 HTML 到 Markdown 的高质量转换，保留网页结构和语义信息
- 集成 AI 搜索和 AI Scraping 能力，支持智能化内容提取和过滤

**适用场景**:
- 构建 RAG（检索增强生成）应用：为 LLM 提供实时网页知识库，增强模型回答能力
- AI Agent 数据采集：为自动化 AI 代理提供网页数据抓取和处理能力
- 企业数据管道：批量抓取竞品网站、行业资讯等，转化为结构化数据用于分析和训练
- 知识库构建：将文档网站、博客等内容转换为统一格式的知识数据



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,798 |
| 语言 | JavaScript |
| Forks | 10,745 |
| Issues | 59 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具影响力的 AI Agent 性能优化系统，通过提供技能、本能、记忆和安全机制，显著提升 Claude Code、Cursor 等 AI 编程工具的开发效率和代码质量。8万+ Stars 证明了其在 AI 辅助开发领域的领先地位和社区认可度。

**技术亮点**:
- Agent Harness 性能优化框架 - 系统性提升 AI Agent 的响应质量和执行效率
- 多维度能力体系 - 集成 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块
- 研究优先的开发方法论 - Research-first development 确保代码决策基于最佳实践
- MCP (Model Context Protocol) 支持 - 标准化 AI 模型上下文交互
- 跨平台兼容性 - 支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具

**适用场景**:
- 企业级 AI 辅助开发团队 - 标准化和优化多开发者的 AI 工具使用体验，提升整体代码质量和开发效率
- 个人开发者效率提升 - 利用记忆和技能系统，让 AI 助手更懂你的编码风格和项目上下文
- AI Agent 研究与定制 - 作为框架学习和二次开发，构建特定领域的 AI 编程助手



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,784 |
| 语言 | Go |
| Forks | 3,714 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的完全开源替代品，支持在消费级硬件上无 GPU 运行大语言模型和多模态生成（文本、图像、音频、视频），非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- OpenAI API 兼容的本地部署方案，支持 gguf、transformers、diffusers 等多种模型格式
- 零 GPU 依赖，在消费级 CPU 硬件上即可高效运行 LLM、Stable Diffusion、音频生成等模型
- 支持分布式和去中心化推理（P2P/libp2p），实现跨节点的模型协同计算
- 全栈多模态支持：文本生成、图像生成、音频生成、视频生成、语音克隆、目标检测
- 内置 MCP 协议支持，便于构建 AI Agent 和工具链集成

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保敏感数据不离开内网，满足合规要求
- 成本优化场景：无需购买昂贵 GPU 或支付云 API 费用，使用现有硬件即可搭建 AI 能力
- 边缘计算和离线环境：在网络受限或无网络环境下部署 AI 应用，如工业现场、科研机构



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,848 |
| 语言 | TypeScript |
| Forks | 14,794 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的开源 AI Agent 工作空间平台，以 73K+ Stars 证明了其在开发者社区的广泛认可。它将多智能体协作、知识库管理和 MCP 协议支持融为一体，为用户提供了一个"工作与生活的终极空间"，让 AI Agent 成为真正的工作伙伴而非简单工具。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 之间的协同工作，实现复杂任务的分工与配合
- 广泛模型兼容性：同时支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换不同 AI 模型
- MCP 协议集成：原生支持 Model Context Protocol，实现模型与外部工具的无缝连接
- 知识库管理：内置知识库功能，支持文档上传、向量化存储和智能检索，增强 AI 的上下文理解能力
- TypeScript 全栈技术：采用现代化 TypeScript 技术栈，提供类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 工作流：适合企业构建内部 AI 助手系统，支持团队协作、知识管理和多场景自动化
- 个人 AI 工作空间：个人用户可搭建专属 AI Agent 平台，整合多种 AI 模型提升工作与生活效率
- Agent 开发与实验：开发者可用于学习、测试和快速原型设计 Multi-Agent 系统，探索 AI 协作模式



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,800 |
| 语言 | MDX |
| Forks | 7,667 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程学习资源库，涵盖了从基础的 Prompt Engineering 到前沿的 RAG 和 AI Agents 的完整知识体系。7万+ Stars 证明了其在 AI 社区的广泛认可度，是开发者快速掌握大模型应用开发技巧的权威指南。

**技术亮点**:
- 系统化覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 提供可交互的学习资源，包含 Jupyter notebooks 和实践代码示例
- 整合了最新学术论文和技术文档，保持与 AI 前沿技术同步
- 采用 MDX 格式，支持代码和文档混合编写，便于学习与实践结合
- 涵盖 LLM 全栈技术栈，从 ChatGPT 使用到深度学习应用一应俱全

**适用场景**:
- 企业 AI 应用开发团队学习 RAG 和 Agent 技术架构设计
- 个人开发者快速提升 Prompt 编写技巧和大模型应用能力
- 技术团队搭建基于 LLM 的产品时的技术选型和最佳实践参考



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,594 |
| 语言 | Python |
| Forks | 8,359 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

这是一个ACL 2024收录的明星级项目，Star数高达6.8万+，提供统一高效的微调解决方案，支持100+主流LLM和VLM模型（包括Llama3、Qwen、DeepSeek、Gemma等），大大降低了大模型微调的技术门槛和开发成本。

**技术亮点**:
- 支持100+大语言模型和视觉语言模型的统一微调框架，覆盖面极广
- 集成多种先进微调技术：LoRA、QLoRA、PEFT、量化微调、RLHF对齐训练
- 支持前沿模型架构：MoE混合专家模型、Agent智能体、多模态VLM
- 提供指令微调、偏好对齐、增量预训练等全流程训练能力
- 高效的内存优化和训练加速，支持消费级显卡微调大模型

**适用场景**:
- 企业级场景：快速微调开源大模型（如Llama3、Qwen、DeepSeek）适配垂直领域业务，构建行业专属AI应用
- 学术研究场景：低成本实验对比不同大模型的微调效果，支持论文复现和创新算法验证
- 个人开发者场景：在消费级GPU上定制个性化AI助手、角色扮演机器人、知识增强问答系统



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,424 |
| 语言 | Java |
| Forks | 15,843 |
| Issues | 54 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 能力的企业级低代码平台，通过"零代码+代码生成"双模式显著提升开发效率，内置 AI 聊天、知识库、流程编排和大模型集成能力，能够解决 Java 项目 80% 的重复工作，特别适合需要快速交付且兼顾灵活性的企业应用开发场景。

**技术亮点**:
- 双模式开发：零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行
- AI 能力全面集成：内置 AI 聊天助手、AI 大模型、知识库（RAG）、AI 流程编排（AIFlow），兼容主流大模型
- 现代化技术栈：基于 SpringBoot3、SpringCloud、Vue3、MyBatis-Plus、Ant Design 等主流框架构建
- MCP 与插件体系：支持 MCP 协议和插件扩展，具备良好的生态兼容性和可扩展性
- 工作流引擎支持：集成 Flowable/Activiti 流程引擎，支持复杂业务流程编排

**适用场景**:
- 企业快速开发：需要快速搭建管理系统、ERP、CRM 等企业级应用的团队
- AI 应用落地：希望将 AI 大模型能力集成到业务系统中的企业和开发者
- 低代码平台选型：寻找开源、可扩展且支持代码生成的低代码解决方案的技术团队



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,257 |
| 语言 | Python |
| Forks | 9,831 |
| Issues | 359 |
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
| Stars | 37,580 |
| 语言 | TypeScript |
| Forks | 2,687 |
| Issues | 114 |
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
| Stars | 34,717 |
| 语言 | TypeScript |
| Forks | 7,022 |
| Issues | 454 |
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
| Stars | 33,459 |
| 语言 | Python |
| Forks | 2,065 |
| Issues | 94 |
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
| Stars | 38,774 |
| 语言 | Python |
| Forks | 6,145 |
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
| Stars | 33,072 |
| 语言 | TypeScript |
| Forks | 3,560 |
| Issues | 280 |
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
| Stars | 32,217 |
| 语言 | Jupyter Notebook |
| Forks | 5,317 |
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
| Stars | 102,576 |
| 语言 | Python |
| Forks | 14,954 |
| Issues | 4 |
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
| Stars | 56,372 |
| 语言 | JavaScript |
| Forks | 6,087 |
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
| Stars | 69,300 |
| 语言 | Python |
| Forks | 8,681 |
| Issues | 340 |
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
| Stars | 40,823 |
| 语言 | TypeScript |
| Forks | 3,067 |
| Issues | 392 |
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
| Stars | 81,098 |
| 语言 | Python |
| Forks | 9,586 |
| Issues | 211 |
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
| Stars | 50,837 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 811 |
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
| Stars | 179,655 |
| 语言 | TypeScript |
| Forks | 55,892 |
| Issues | 1,429 |
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
| Stars | 145,781 |
| 语言 | Python |
| Forks | 8,598 |
| Issues | 883 |
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
| Stars | 54,262 |
| 语言 | Jupyter Notebook |
| Forks | 18,794 |
| Issues | 2 |
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
| Stars | 45,154 |
| 语言 | Python |
| Forks | 4,578 |
| Issues | 324 |
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
| Stars | 127,576 |
| 语言 | Python |
| Forks | 18,035 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 界面工具，支持多种主流 LLM 后端（Ollama、OpenAI API 等），让用户无需编码即可快速搭建私有化 AI 助手平台。其超过 12 万 Star 的超高人气证明了它在 AI 应用落地领域的巨大价值和可靠性。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 服务，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库问答，增强 AI 响应准确性
- 支持 MCP（Model Context Protocol）协议：实现与外部工具和数据源的无缝集成
- 完全自托管与隐私保护：可私有化部署，数据完全掌控，适合对隐私要求高的场景
- 现代化的 Web UI 设计：用户友好的聊天界面，支持多用户、权限管理和对话历史

**适用场景**:
- 企业内部 AI 助手平台：自建私有化 ChatGPT 替代方案，保护敏感数据不外泄
- 开发者本地 LLM 调试与测试：结合 Ollama 快速搭建本地 AI 开发环境，支持 RAG 和多模型对比
- 团队知识库问答系统：上传企业文档构建专属知识库，实现智能文档检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,264 |
| 语言 | Python |
| Forks | 8,427 |
| Issues | 3,110 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，将前沿的检索增强生成技术与 Agent 智能体能力深度融合，为大语言模型提供高质量上下文层。75k+ Stars 和丰富的功能生态使其成为企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 和智能体协作，实现更复杂的推理和任务执行
- 深度集成 DeepSeek、OpenAI、Ollama 等主流 LLM，以及 MCP 协议，生态兼容性强
- 内置强大的文档解析和文档理解能力，支持复杂文档结构化提取与知识库构建
- 支持 GraphRAG 图检索技术，提升多跳推理和复杂语义关联能力
- 提供 AI 搜索和深度研究功能，适用于知识密集型场景的上下文工程

**适用场景**:
- 企业知识库搭建：快速构建基于私有文档的智能问答系统，支持多格式文档解析
- AI Agent 应用开发：构建具备知识检索能力的智能体，完成复杂业务流程自动化
- 深度研究与报告生成：结合 RAG 和推理能力，自动从海量文档中提取信息并生成分析报告



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,848 |
| 语言 | TypeScript |
| Forks | 14,794 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的开源 AI Agent 工作空间平台，以 73K+ Stars 证明了其在开发者社区的广泛认可。它将多智能体协作、知识库管理和 MCP 协议支持融为一体，为用户提供了一个"工作与生活的终极空间"，让 AI Agent 成为真正的工作伙伴而非简单工具。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 之间的协同工作，实现复杂任务的分工与配合
- 广泛模型兼容性：同时支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换不同 AI 模型
- MCP 协议集成：原生支持 Model Context Protocol，实现模型与外部工具的无缝连接
- 知识库管理：内置知识库功能，支持文档上传、向量化存储和智能检索，增强 AI 的上下文理解能力
- TypeScript 全栈技术：采用现代化 TypeScript 技术栈，提供类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 工作流：适合企业构建内部 AI 助手系统，支持团队协作、知识管理和多场景自动化
- 个人 AI 工作空间：个人用户可搭建专属 AI Agent 平台，整合多种 AI 模型提升工作与生活效率
- Agent 开发与实验：开发者可用于学习、测试和快速原型设计 Multi-Agent 系统，探索 AI 协作模式



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,800 |
| 语言 | MDX |
| Forks | 7,667 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程学习资源库，涵盖了从基础的 Prompt Engineering 到前沿的 RAG 和 AI Agents 的完整知识体系。7万+ Stars 证明了其在 AI 社区的广泛认可度，是开发者快速掌握大模型应用开发技巧的权威指南。

**技术亮点**:
- 系统化覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 提供可交互的学习资源，包含 Jupyter notebooks 和实践代码示例
- 整合了最新学术论文和技术文档，保持与 AI 前沿技术同步
- 采用 MDX 格式，支持代码和文档混合编写，便于学习与实践结合
- 涵盖 LLM 全栈技术栈，从 ChatGPT 使用到深度学习应用一应俱全

**适用场景**:
- 企业 AI 应用开发团队学习 RAG 和 Agent 技术架构设计
- 个人开发者快速提升 Prompt 编写技巧和大模型应用能力
- 技术团队搭建基于 LLM 的产品时的技术选型和最佳实践参考



### jeecgboot/JeecgBoot

**描述**: JeecgBoot 是一款 AI 驱动的低代码开发平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,424 |
| 语言 | Java |
| Forks | 15,843 |
| Issues | 54 |
| Topics | activiti, agent, ai, aiflow, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一款融合 AI 能力的企业级低代码平台，通过"零代码+代码生成"双模式显著提升开发效率，内置 AI 聊天、知识库、流程编排和大模型集成能力，能够解决 Java 项目 80% 的重复工作，特别适合需要快速交付且兼顾灵活性的企业应用开发场景。

**技术亮点**:
- 双模式开发：零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行
- AI 能力全面集成：内置 AI 聊天助手、AI 大模型、知识库（RAG）、AI 流程编排（AIFlow），兼容主流大模型
- 现代化技术栈：基于 SpringBoot3、SpringCloud、Vue3、MyBatis-Plus、Ant Design 等主流框架构建
- MCP 与插件体系：支持 MCP 协议和插件扩展，具备良好的生态兼容性和可扩展性
- 工作流引擎支持：集成 Flowable/Activiti 流程引擎，支持复杂业务流程编排

**适用场景**:
- 企业快速开发：需要快速搭建管理系统、ERP、CRM 等企业级应用的团队
- AI 应用落地：希望将 AI 大模型能力集成到业务系统中的企业和开发者
- 低代码平台选型：寻找开源、可扩展且支持代码生成的低代码解决方案的技术团队



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 37,580 |
| 语言 | TypeScript |
| Forks | 2,687 |
| Issues | 114 |
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
| Stars | 33,459 |
| 语言 | Python |
| Forks | 2,065 |
| Issues | 94 |
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
| Stars | 38,774 |
| 语言 | Python |
| Forks | 6,145 |
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
| Stars | 33,072 |
| 语言 | TypeScript |
| Forks | 3,560 |
| Issues | 280 |
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
| Stars | 32,217 |
| 语言 | Jupyter Notebook |
| Forks | 5,317 |
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
| Stars | 102,576 |
| 语言 | Python |
| Forks | 14,954 |
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
| Stars | 99,159 |
| 语言 | TypeScript |
| Forks | 11,819 |
| Issues | 936 |
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
| Stars | 56,372 |
| 语言 | JavaScript |
| Forks | 6,087 |
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
| Stars | 50,837 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 811 |
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
| Stars | 72,479 |
| 语言 | Python |
| Forks | 9,989 |
| Issues | 250 |
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
| Stars | 43,375 |
| 语言 | Go |
| Forks | 3,905 |
| Issues | 1,071 |
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
| Stars | 31,554 |
| 语言 | Python |
| Forks | 3,325 |
| Issues | 80 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


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
| Stars | 127,576 |
| 语言 | Python |
| Forks | 18,035 |
| Issues | 298 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大的自托管 AI 界面工具，支持多种主流 LLM 后端（Ollama、OpenAI API 等），让用户无需编码即可快速搭建私有化 AI 助手平台。其超过 12 万 Star 的超高人气证明了它在 AI 应用落地领域的巨大价值和可靠性。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 服务，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库问答，增强 AI 响应准确性
- 支持 MCP（Model Context Protocol）协议：实现与外部工具和数据源的无缝集成
- 完全自托管与隐私保护：可私有化部署，数据完全掌控，适合对隐私要求高的场景
- 现代化的 Web UI 设计：用户友好的聊天界面，支持多用户、权限管理和对话历史

**适用场景**:
- 企业内部 AI 助手平台：自建私有化 ChatGPT 替代方案，保护敏感数据不外泄
- 开发者本地 LLM 调试与测试：结合 Ollama 快速搭建本地 AI 开发环境，支持 RAG 和多模型对比
- 团队知识库问答系统：上传企业文档构建专属知识库，实现智能文档检索和问答



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,264 |
| 语言 | Python |
| Forks | 8,427 |
| Issues | 3,110 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最活跃的开源 RAG 引擎之一，将前沿的检索增强生成技术与 Agent 智能体能力深度融合，为大语言模型提供高质量上下文层。75k+ Stars 和丰富的功能生态使其成为企业级 RAG 解决方案的首选。

**技术亮点**:
- 融合 RAG 与 Agent 能力，支持 Agentic Workflow 和智能体协作，实现更复杂的推理和任务执行
- 深度集成 DeepSeek、OpenAI、Ollama 等主流 LLM，以及 MCP 协议，生态兼容性强
- 内置强大的文档解析和文档理解能力，支持复杂文档结构化提取与知识库构建
- 支持 GraphRAG 图检索技术，提升多跳推理和复杂语义关联能力
- 提供 AI 搜索和深度研究功能，适用于知识密集型场景的上下文工程

**适用场景**:
- 企业知识库搭建：快速构建基于私有文档的智能问答系统，支持多格式文档解析
- AI Agent 应用开发：构建具备知识检索能力的智能体，完成复杂业务流程自动化
- 深度研究与报告生成：结合 RAG 和推理能力，自动从海量文档中提取信息并生成分析报告



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,798 |
| 语言 | JavaScript |
| Forks | 10,745 |
| Issues | 59 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具影响力的 AI Agent 性能优化系统，通过提供技能、本能、记忆和安全机制，显著提升 Claude Code、Cursor 等 AI 编程工具的开发效率和代码质量。8万+ Stars 证明了其在 AI 辅助开发领域的领先地位和社区认可度。

**技术亮点**:
- Agent Harness 性能优化框架 - 系统性提升 AI Agent 的响应质量和执行效率
- 多维度能力体系 - 集成 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块
- 研究优先的开发方法论 - Research-first development 确保代码决策基于最佳实践
- MCP (Model Context Protocol) 支持 - 标准化 AI 模型上下文交互
- 跨平台兼容性 - 支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具

**适用场景**:
- 企业级 AI 辅助开发团队 - 标准化和优化多开发者的 AI 工具使用体验，提升整体代码质量和开发效率
- 个人开发者效率提升 - 利用记忆和技能系统，让 AI 助手更懂你的编码风格和项目上下文
- AI Agent 研究与定制 - 作为框架学习和二次开发，构建特定领域的 AI 编程助手



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,848 |
| 语言 | TypeScript |
| Forks | 14,794 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能强大的开源 AI Agent 工作空间平台，以 73K+ Stars 证明了其在开发者社区的广泛认可。它将多智能体协作、知识库管理和 MCP 协议支持融为一体，为用户提供了一个"工作与生活的终极空间"，让 AI Agent 成为真正的工作伙伴而非简单工具。

**技术亮点**:
- 多智能体协作架构：支持多个 AI Agent 之间的协同工作，实现复杂任务的分工与配合
- 广泛模型兼容性：同时支持 OpenAI、Claude、Gemini、DeepSeek 等主流 LLM，灵活切换不同 AI 模型
- MCP 协议集成：原生支持 Model Context Protocol，实现模型与外部工具的无缝连接
- 知识库管理：内置知识库功能，支持文档上传、向量化存储和智能检索，增强 AI 的上下文理解能力
- TypeScript 全栈技术：采用现代化 TypeScript 技术栈，提供类型安全和优秀的开发体验

**适用场景**:
- 企业级 AI 工作流：适合企业构建内部 AI 助手系统，支持团队协作、知识管理和多场景自动化
- 个人 AI 工作空间：个人用户可搭建专属 AI Agent 平台，整合多种 AI 模型提升工作与生活效率
- Agent 开发与实验：开发者可用于学习、测试和快速原型设计 Multi-Agent 系统，探索 AI 协作模式



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,800 |
| 语言 | MDX |
| Forks | 7,667 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程学习资源库，涵盖了从基础的 Prompt Engineering 到前沿的 RAG 和 AI Agents 的完整知识体系。7万+ Stars 证明了其在 AI 社区的广泛认可度，是开发者快速掌握大模型应用开发技巧的权威指南。

**技术亮点**:
- 系统化覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 提供可交互的学习资源，包含 Jupyter notebooks 和实践代码示例
- 整合了最新学术论文和技术文档，保持与 AI 前沿技术同步
- 采用 MDX 格式，支持代码和文档混合编写，便于学习与实践结合
- 涵盖 LLM 全栈技术栈，从 ChatGPT 使用到深度学习应用一应俱全

**适用场景**:
- 企业 AI 应用开发团队学习 RAG 和 Agent 技术架构设计
- 个人开发者快速提升 Prompt 编写技巧和大模型应用能力
- 技术团队搭建基于 LLM 的产品时的技术选型和最佳实践参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,075 |
| 语言 | HTML |
| Forks | 20,136 |
| Issues | 34 |
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
| Stars | 42,257 |
| 语言 | Python |
| Forks | 9,831 |
| Issues | 359 |
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
| Stars | 37,580 |
| 语言 | TypeScript |
| Forks | 2,687 |
| Issues | 114 |
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
| Stars | 34,717 |
| 语言 | TypeScript |
| Forks | 7,022 |
| Issues | 454 |
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
| Stars | 33,459 |
| 语言 | Python |
| Forks | 2,065 |
| Issues | 94 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,372 |
| 语言 | JavaScript |
| Forks | 6,087 |
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
| Stars | 69,300 |
| 语言 | Python |
| Forks | 8,681 |
| Issues | 340 |
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
| Stars | 40,823 |
| 语言 | TypeScript |
| Forks | 3,067 |
| Issues | 392 |
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
| Stars | 50,837 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 811 |
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
| Stars | 34,514 |
| 语言 | HTML |
| Forks | 5,549 |
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
| Stars | 73,457 |
| 语言 | Python |
| Forks | 14,462 |
| Issues | 3,746 |
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
| Stars | 43,910 |
| 语言 | Python |
| Forks | 4,232 |
| Issues | 76 |
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
| Stars | 39,000 |
| 语言 | TypeScript |
| Forks | 3,944 |
| Issues | 1,076 |
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
| Stars | 145,781 |
| 语言 | Python |
| Forks | 8,598 |
| Issues | 883 |
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
| Stars | 165,382 |
| 语言 | Go |
| Forks | 15,022 |
| Issues | 2,669 |
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
| Stars | 88,477 |
| 语言 | Jupyter Notebook |
| Forks | 13,506 |
| Issues | 4 |
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
| Stars | 46,704 |
| 语言 | Rust |
| Forks | 9,133 |
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
| Stars | 90,875 |
| 语言 | Python |
| Forks | 5,371 |
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
| Stars | 36,722 |
| 语言 | Python |
| Forks | 2,567 |
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
| Stars | 45,154 |
| 语言 | Python |
| Forks | 4,578 |
| Issues | 324 |
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
| Stars | 71,800 |
| 语言 | MDX |
| Forks | 7,667 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程学习资源库，涵盖了从基础的 Prompt Engineering 到前沿的 RAG 和 AI Agents 的完整知识体系。7万+ Stars 证明了其在 AI 社区的广泛认可度，是开发者快速掌握大模型应用开发技巧的权威指南。

**技术亮点**:
- 系统化覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 提供可交互的学习资源，包含 Jupyter notebooks 和实践代码示例
- 整合了最新学术论文和技术文档，保持与 AI 前沿技术同步
- 采用 MDX 格式，支持代码和文档混合编写，便于学习与实践结合
- 涵盖 LLM 全栈技术栈，从 ChatGPT 使用到深度学习应用一应俱全

**适用场景**:
- 企业 AI 应用开发团队学习 RAG 和 Agent 技术架构设计
- 个人开发者快速提升 Prompt 编写技巧和大模型应用能力
- 技术团队搭建基于 LLM 的产品时的技术选型和最佳实践参考



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,594 |
| 语言 | Python |
| Forks | 8,359 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

这是一个ACL 2024收录的明星级项目，Star数高达6.8万+，提供统一高效的微调解决方案，支持100+主流LLM和VLM模型（包括Llama3、Qwen、DeepSeek、Gemma等），大大降低了大模型微调的技术门槛和开发成本。

**技术亮点**:
- 支持100+大语言模型和视觉语言模型的统一微调框架，覆盖面极广
- 集成多种先进微调技术：LoRA、QLoRA、PEFT、量化微调、RLHF对齐训练
- 支持前沿模型架构：MoE混合专家模型、Agent智能体、多模态VLM
- 提供指令微调、偏好对齐、增量预训练等全流程训练能力
- 高效的内存优化和训练加速，支持消费级显卡微调大模型

**适用场景**:
- 企业级场景：快速微调开源大模型（如Llama3、Qwen、DeepSeek）适配垂直领域业务，构建行业专属AI应用
- 学术研究场景：低成本实验对比不同大模型的微调效果，支持论文复现和创新算法验证
- 个人开发者场景：在消费级GPU上定制个性化AI助手、角色扮演机器人、知识增强问答系统



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,238 |
| 语言 | Python |
| Forks | 6,214 |
| Issues | 66 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB是目前GitHub上最受关注的开源金融数据平台，拥有超过6.3万Stars，它将多源金融数据整合到统一的Python接口中，支持股票、加密货币、期权、衍生品、固定收益等多种资产类别。其独特价值在于为量化分析师、金融研究员和AI开发者提供了一站式的金融数据接入解决方案，大幅降低了金融数据分析的技术门槛。

**技术亮点**:
- 统一的Python API整合多源金融数据，覆盖股票、加密货币、期权、衍生品、固定收益等全资产类别
- 支持机器学习和AI Agent集成，可直接对接LLM进行智能金融分析
- 模块化架构设计，支持经济学数据、权益类资产、衍生品等多维度数据查询
- 开源生态活跃（63K+ Stars），社区驱动持续迭代，提供丰富的扩展能力
- 跨平台兼容性强，支持Jupyter Notebook、命令行终端和程序化调用多种使用方式

**适用场景**:
- 量化交易策略开发：适合量化研究员和交易员进行多资产类别的数据获取、回测和策略验证
- 金融AI应用开发：为AI Agent和机器学习模型提供标准化的金融数据输入，构建智能投研助手
- 企业级金融数据分析平台：金融机构和投资公司可基于OpenBB构建内部的统一数据中台，整合多源数据提升研究效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,075 |
| 语言 | HTML |
| Forks | 20,136 |
| Issues | 34 |
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
| Stars | 33,072 |
| 语言 | TypeScript |
| Forks | 3,560 |
| Issues | 280 |
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
| Stars | 32,217 |
| 语言 | Jupyter Notebook |
| Forks | 5,317 |
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
| Stars | 157,984 |
| 语言 | Python |
| Forks | 32,516 |
| Issues | 2,327 |
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
| Stars | 73,457 |
| 语言 | Python |
| Forks | 14,462 |
| Issues | 3,746 |
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
| Stars | 106,159 |
| 语言 | Python |
| Forks | 12,206 |
| Issues | 3,844 |
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
| Stars | 98,355 |
| 语言 | Python |
| Forks | 27,234 |
| Issues | 18,074 |
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
| Stars | 88,477 |
| 语言 | Jupyter Notebook |
| Forks | 13,506 |
| Issues | 4 |
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
| Stars | 161,841 |
| 语言 | Python |
| Forks | 30,184 |
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
| Stars | 82,798 |
| 语言 | JavaScript |
| Forks | 10,745 |
| Issues | 59 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个极具影响力的 AI Agent 性能优化系统，通过提供技能、本能、记忆和安全机制，显著提升 Claude Code、Cursor 等 AI 编程工具的开发效率和代码质量。8万+ Stars 证明了其在 AI 辅助开发领域的领先地位和社区认可度。

**技术亮点**:
- Agent Harness 性能优化框架 - 系统性提升 AI Agent 的响应质量和执行效率
- 多维度能力体系 - 集成 Skills（技能）、Instincts（本能）、Memory（记忆）、Security（安全）四大核心模块
- 研究优先的开发方法论 - Research-first development 确保代码决策基于最佳实践
- MCP (Model Context Protocol) 支持 - 标准化 AI 模型上下文交互
- 跨平台兼容性 - 支持 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程工具

**适用场景**:
- 企业级 AI 辅助开发团队 - 标准化和优化多开发者的 AI 工具使用体验，提升整体代码质量和开发效率
- 个人开发者效率提升 - 利用记忆和技能系统，让 AI 助手更懂你的编码风格和项目上下文
- AI Agent 研究与定制 - 作为框架学习和二次开发，构建特定领域的 AI 编程助手



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,784 |
| 语言 | Go |
| Forks | 3,714 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的完全开源替代品，支持在消费级硬件上无 GPU 运行大语言模型和多模态生成（文本、图像、音频、视频），非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- OpenAI API 兼容的本地部署方案，支持 gguf、transformers、diffusers 等多种模型格式
- 零 GPU 依赖，在消费级 CPU 硬件上即可高效运行 LLM、Stable Diffusion、音频生成等模型
- 支持分布式和去中心化推理（P2P/libp2p），实现跨节点的模型协同计算
- 全栈多模态支持：文本生成、图像生成、音频生成、视频生成、语音克隆、目标检测
- 内置 MCP 协议支持，便于构建 AI Agent 和工具链集成

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保敏感数据不离开内网，满足合规要求
- 成本优化场景：无需购买昂贵 GPU 或支付云 API 费用，使用现有硬件即可搭建 AI 能力
- 边缘计算和离线环境：在网络受限或无网络环境下部署 AI 应用，如工业现场、科研机构



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,300 |
| 语言 | Python |
| Forks | 8,681 |
| Issues | 340 |
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
| Stars | 40,823 |
| 语言 | TypeScript |
| Forks | 3,067 |
| Issues | 392 |
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
| Stars | 179,655 |
| 语言 | TypeScript |
| Forks | 55,892 |
| Issues | 1,429 |
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
| Stars | 151,737 |
| 语言 | Python |
| Forks | 12,293 |
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
| Stars | 96,301 |
| 语言 | Python |
| Forks | 8,874 |
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
| Stars | 73,803 |
| 语言 | Python |
| Forks | 8,762 |
| Issues | 198 |
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
| Stars | 182,774 |
| 语言 | TypeScript |
| Forks | 38,560 |
| Issues | 15,405 |
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
| Stars | 93,856 |
| 语言 | TypeScript |
| Forks | 9,402 |
| Issues | 296 |
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
| Stars | 78,491 |
| 语言 | TypeScript |
| Forks | 5,699 |
| Issues | 719 |
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
| Stars | 76,694 |
| 语言 | TypeScript |
| Forks | 6,551 |
| Issues | 175 |
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
| Stars | 75,663 |
| 语言 | JavaScript |
| Forks | 7,274 |
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
| Stars | 78,698 |
| 语言 | Go |
| Forks | 2,736 |
| Issues | 316 |
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
| Stars | 74,513 |
| 语言 | Go |
| Forks | 2,616 |
| Issues | 932 |
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
| Stars | 36,722 |
| 语言 | Python |
| Forks | 2,567 |
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
| Stars | 54,511 |
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
| Stars | 411,494 |
| 语言 | Python |
| Forks | 44,483 |
| Issues | 1,008 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,823 |
| 语言 | TypeScript |
| Forks | 3,067 |
| Issues | 392 |
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
| Stars | 179,655 |
| 语言 | TypeScript |
| Forks | 55,892 |
| Issues | 1,429 |
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
| Stars | 51,680 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 224 |
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
| Stars | 121,214 |
| 语言 | Go |
| Forks | 42,690 |
| Issues | 2,632 |
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
| Stars | 71,538 |
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
| Stars | 54,337 |
| 语言 | Go |
| Forks | 6,486 |
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
| Stars | 47,585 |
| 语言 | Go |
| Forks | 5,070 |
| Issues | 963 |
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
| Stars | 93,856 |
| 语言 | TypeScript |
| Forks | 9,402 |
| Issues | 296 |
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
| Stars | 84,420 |
| 语言 | TypeScript |
| Forks | 5,305 |
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
| Stars | 75,428 |
| 语言 | TypeScript |
| Forks | 6,413 |
| Issues | 438 |
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
| Stars | 84,185 |
| 语言 | JavaScript |
| Forks | 7,542 |
| Issues | 709 |
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
| Stars | 62,231 |
| 语言 | Go |
| Forks | 5,884 |
| Issues | 775 |
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
| Stars | 57,975 |
| 语言 | Go |
| Forks | 4,206 |
| Issues | 24 |
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
| Stars | 45,154 |
| 语言 | Python |
| Forks | 4,578 |
| Issues | 324 |
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
| Stars | 69,400 |
| 语言 | Go |
| Forks | 1,879 |
| Issues | 295 |
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
| Stars | 84,185 |
| 语言 | JavaScript |
| Forks | 7,542 |
| Issues | 709 |
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
| Stars | 63,224 |
| 语言 | Go |
| Forks | 10,248 |
| Issues | 753 |
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
| Stars | 43,784 |
| 语言 | Go |
| Forks | 3,714 |
| Issues | 145 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的本地化 AI 解决方案，作为 OpenAI API 的完全开源替代品，支持在消费级硬件上无 GPU 运行大语言模型和多模态生成（文本、图像、音频、视频），非常适合注重数据隐私和成本控制的场景。

**技术亮点**:
- OpenAI API 兼容的本地部署方案，支持 gguf、transformers、diffusers 等多种模型格式
- 零 GPU 依赖，在消费级 CPU 硬件上即可高效运行 LLM、Stable Diffusion、音频生成等模型
- 支持分布式和去中心化推理（P2P/libp2p），实现跨节点的模型协同计算
- 全栈多模态支持：文本生成、图像生成、音频生成、视频生成、语音克隆、目标检测
- 内置 MCP 协议支持，便于构建 AI Agent 和工具链集成

**适用场景**:
- 企业私有化部署：在本地服务器运行 AI 服务，确保敏感数据不离开内网，满足合规要求
- 成本优化场景：无需购买昂贵 GPU 或支付云 API 费用，使用现有硬件即可搭建 AI 能力
- 边缘计算和离线环境：在网络受限或无网络环境下部署 AI 应用，如工业现场、科研机构



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,301 |
| 语言 | Python |
| Forks | 8,874 |
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
| Stars | 87,080 |
| 语言 | Python |
| Forks | 33,756 |
| Issues | 433 |
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
| Stars | 100,122 |
| 语言 | TypeScript |
| Forks | 27,138 |
| Issues | 1,122 |
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
| Stars | 78,491 |
| 语言 | TypeScript |
| Forks | 5,699 |
| Issues | 719 |
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
| Stars | 74,956 |
| 语言 | TypeScript |
| Forks | 8,257 |
| Issues | 37 |
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
| Stars | 75,663 |
| 语言 | JavaScript |
| Forks | 7,274 |
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
| Stars | 55,945 |
| 语言 | JavaScript |
| Forks | 10,225 |
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
| Stars | 88,282 |
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
| Stars | 70,891 |
| 语言 | Go |
| Forks | 4,679 |
| Issues | 242 |
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
| Stars | 56,789 |
| 语言 | Go |
| Forks | 3,180 |
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
| Stars | 36,722 |
| 语言 | Python |
| Forks | 2,567 |
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
| Stars | 411,494 |
| 语言 | Python |
| Forks | 44,483 |
| Issues | 1,008 |
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
| Stars | 68,903 |
| 语言 | JavaScript |
| Forks | 22,843 |
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
| Stars | 99,159 |
| 语言 | TypeScript |
| Forks | 11,819 |
| Issues | 936 |
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
| Stars | 56,372 |
| 语言 | JavaScript |
| Forks | 6,087 |
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
| Stars | 43,375 |
| 语言 | Go |
| Forks | 3,905 |
| Issues | 1,071 |
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
| Stars | 51,680 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 224 |
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
| Stars | 71,800 |
| 语言 | MDX |
| Forks | 7,667 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程学习资源库，涵盖了从基础的 Prompt Engineering 到前沿的 RAG 和 AI Agents 的完整知识体系。7万+ Stars 证明了其在 AI 社区的广泛认可度，是开发者快速掌握大模型应用开发技巧的权威指南。

**技术亮点**:
- 系统化覆盖 Prompt Engineering、Context Engineering、RAG 和 AI Agents 四大核心技术领域
- 提供可交互的学习资源，包含 Jupyter notebooks 和实践代码示例
- 整合了最新学术论文和技术文档，保持与 AI 前沿技术同步
- 采用 MDX 格式，支持代码和文档混合编写，便于学习与实践结合
- 涵盖 LLM 全栈技术栈，从 ChatGPT 使用到深度学习应用一应俱全

**适用场景**:
- 企业 AI 应用开发团队学习 RAG 和 Agent 技术架构设计
- 个人开发者快速提升 Prompt 编写技巧和大模型应用能力
- 技术团队搭建基于 LLM 的产品时的技术选型和最佳实践参考



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,075 |
| 语言 | HTML |
| Forks | 20,136 |
| Issues | 34 |
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
| Stars | 34,514 |
| 语言 | HTML |
| Forks | 5,549 |
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
| Stars | 89,469 |
| 语言 | TypeScript |
| Forks | 9,930 |
| Issues | 2,198 |
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
| Stars | 86,740 |
| 语言 | TypeScript |
| Forks | 8,738 |
| Issues | 1,608 |
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
| Stars | 127,112 |
| 语言 | JavaScript |
| Forks | 12,459 |
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
| Stars | 100,354 |
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
| Stars | 167,582 |
| 语言 | Go |
| Forks | 13,066 |
| Issues | 172 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (66 个项目) { #其他 }


### 🌟 高优先级


### openclaw/openclaw

**描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞 

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 320,042 |
| 语言 | TypeScript |
| Forks | 61,452 |
| Issues | 14,364 |
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
| Stars | 51,363 |
| 语言 | Shell |
| Forks | 7,655 |
| Issues | 57 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,122 |
| 语言 | Python |
| Forks | 6,341 |
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
| Stars | 80,105 |
| 语言 | Python |
| Forks | 11,689 |
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
| Stars | 77,823 |
| 语言 | Python |
| Forks | 6,600 |
| Issues | 632 |
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
| Stars | 131,702 |
| 语言 | Unknown |
| Forks | 33,396 |
| Issues | 129 |
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
| Stars | 384,162 |
| 语言 | Python |
| Forks | 66,030 |
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
| Stars | 112,998 |
| 语言 | TypeScript |
| Forks | 5,734 |
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
| Stars | 103,481 |
| 语言 | TypeScript |
| Forks | 7,526 |
| Issues | 189 |
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
| Stars | 47,957 |
| 语言 | Go |
| Forks | 10,250 |
| Issues | 1,894 |
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
| Stars | 98,364 |
| 语言 | C++ |
| Forks | 15,573 |
| Issues | 1,285 |
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
| Stars | 60,280 |
| 语言 | Python |
| Forks | 1,609 |
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
| Stars | 31,715 |
| 语言 | JavaScript |
| Forks | 2,662 |
| Issues | 217 |
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
| Stars | 339,210 |
| 语言 | Python |
| Forks | 54,927 |
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
| Stars | 287,637 |
| 语言 | Python |
| Forks | 27,420 |
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
| Stars | 218,785 |
| 语言 | Python |
| Forks | 50,221 |
| Issues | 889 |
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
| Stars | 85,404 |
| 语言 | Python |
| Forks | 36,996 |
| Issues | 3,587 |
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
| Stars | 85,333 |
| 语言 | Python |
| Forks | 7,165 |
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
| Stars | 77,687 |
| 语言 | Python |
| Forks | 45,232 |
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
| Stars | 76,117 |
| 语言 | Python |
| Forks | 16,760 |
| Issues | 18 |
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
| Stars | 438,409 |
| 语言 | TypeScript |
| Forks | 43,675 |
| Issues | 231 |
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
| Stars | 351,074 |
| 语言 | TypeScript |
| Forks | 43,796 |
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
| Stars | 118,980 |
| 语言 | TypeScript |
| Forks | 12,902 |
| Issues | 2,844 |
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
| Stars | 109,844 |
| 语言 | TypeScript |
| Forks | 8,228 |
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
| Stars | 108,185 |
| 语言 | TypeScript |
| Forks | 13,304 |
| Issues | 5,485 |
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
| Stars | 97,749 |
| 语言 | TypeScript |
| Forks | 54,574 |
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
| Stars | 95,008 |
| 语言 | TypeScript |
| Forks | 5,130 |
| Issues | 660 |
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
| Stars | 94,103 |
| 语言 | TypeScript |
| Forks | 5,123 |
| Issues | 97 |
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
| Stars | 83,007 |
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
| Stars | 81,339 |
| 语言 | TypeScript |
| Forks | 9,943 |
| Issues | 520 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,118 |
| 语言 | TypeScript |
| Forks | 7,922 |
| Issues | 659 |
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
| Stars | 244,008 |
| 语言 | JavaScript |
| Forks | 50,811 |
| Issues | 1,172 |
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
| Stars | 138,366 |
| 语言 | JavaScript |
| Forks | 30,658 |
| Issues | 3,471 |
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
| Stars | 116,306 |
| 语言 | JavaScript |
| Forks | 35,086 |
| Issues | 2,531 |
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
| Stars | 111,402 |
| 语言 | JavaScript |
| Forks | 36,310 |
| Issues | 589 |
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
| Stars | 108,656 |
| 语言 | JavaScript |
| Forks | 11,560 |
| Issues | 347 |
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
| Stars | 98,050 |
| 语言 | JavaScript |
| Forks | 32,707 |
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
| Stars | 95,428 |
| 语言 | JavaScript |
| Forks | 15,258 |
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
| Stars | 86,092 |
| 语言 | JavaScript |
| Forks | 4,808 |
| Issues | 968 |
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
| Stars | 70,765 |
| 语言 | JavaScript |
| Forks | 16,806 |
| Issues | 887 |
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
| Stars | 66,038 |
| 语言 | JavaScript |
| Forks | 9,331 |
| Issues | 199 |
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
| Stars | 62,140 |
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
| Stars | 59,886 |
| 语言 | JavaScript |
| Forks | 5,612 |
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
| Forks | 20,467 |
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
| Stars | 52,993 |
| 语言 | JavaScript |
| Forks | 10,599 |
| Issues | 483 |
| 许可证 | Apache License 2.0 |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,085 |
| 语言 | Go |
| Forks | 18,862 |
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
| Stars | 105,323 |
| 语言 | Go |
| Forks | 14,955 |
| Issues | 47 |
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
| Stars | 87,125 |
| 语言 | Go |
| Forks | 8,211 |
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
| Stars | 80,901 |
| 语言 | Go |
| Forks | 4,967 |
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
| Stars | 68,682 |
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
| Stars | 56,088 |
| 语言 | Go |
| Forks | 4,976 |
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
| Stars | 50,926 |
| 语言 | Go |
| Forks | 21,859 |
| Issues | 373 |
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
| Stars | 50,175 |
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
| Stars | 49,169 |
| 语言 | Go |
| Forks | 7,975 |
| Issues | 566 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### opendatalab/MinerU

**描述**: Transforms complex documents like PDFs into LLM-ready markdown/JSON for your Agentic workflows.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,417 |
| 语言 | Python |
| Forks | 4,678 |
| Issues | 194 |
| Topics | ai4science, document-analysis, extract-data, layout-analysis, ocr, parser, pdf, pdf-converter, pdf-extractor-llm, pdf-extractor-pretrain, pdf-extractor-rag, pdf-parser, python |
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
| Stars | 139,894 |
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
| Stars | 195,773 |
| 语言 | JavaScript |
| Forks | 31,116 |
| Issues | 396 |
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
| Stars | 148,122 |
| 语言 | JavaScript |
| Forks | 26,772 |
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
| Stars | 78,763 |
| 语言 | JavaScript |
| Forks | 31,551 |
| Issues | 272 |
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
| Stars | 67,267 |
| 语言 | JavaScript |
| Forks | 11,978 |
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
| Stars | 66,285 |
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
| Stars | 61,583 |
| 语言 | JavaScript |
| Forks | 7,128 |
| Issues | 132 |
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
| Stars | 46,957 |
| 语言 | Go |
| Forks | 8,878 |
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
| Stars | 45,499 |
| 语言 | Go |
| Forks | 3,771 |
| Issues | 92 |
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
| Stars | 146,470 |
| 语言 | Python |
| Forks | 11,240 |
| Issues | 298 |
| Topics | awesome, github, hellogithub, python |
