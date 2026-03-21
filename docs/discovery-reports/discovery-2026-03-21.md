# 项目发现报告 (2026-03-21)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 136 |
| 去重移除 | 29 |
| 已在监控 | 24 |


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
| 🌐 Web 框架 | 13 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
| 📁 其他 | 65 |

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
| Stars | 128,132 |
| 语言 | Python |
| Forks | 18,113 |
| Issues | 324 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最活跃的开源 AI 聊天界面项目之一，拥有 12.8万+ Stars，支持 Ollama、OpenAI 等多种后端，提供开箱即用的自托管方案，是个人和企业快速部署私有化 AI 助手的最佳选择。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库构建，增强 AI 回答准确性
- 支持 MCP（Model Context Protocol）：可与外部工具和数据源无缝集成
- 完全自托管：数据隐私可控，适合私有化部署，提供认证和权限管理
- 现代化 Web UI：用户友好的聊天界面，支持多用户协作和会话管理

**适用场景**:
- 企业私有化 AI 助手：在公司内部部署，连接本地 Ollama 模型，保障数据安全与隐私
- 个人 AI 学习与研究：搭建本地 LLM 平台，低成本体验和测试各类开源模型
- AI 应用开发测试：作为 LLM 应用的前端界面，快速验证 Prompt 和 RAG 方案



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,709 |
| 语言 | Python |
| Forks | 8,476 |
| Issues | 3,141 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款顶级的开源 RAG 引擎，将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型提供卓越的上下文层，75K+ Stars 证明了其在 AI 社区的领先地位和广泛认可。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供智能化的文档理解和上下文检索能力
- 支持多种主流 LLM 后端（OpenAI、Ollama、DeepSeek），具备极强的生态兼容性
- 内置高级文档解析器和文档理解引擎，支持复杂文档的深度处理
- 支持 GraphRAG 和 MCP 协议，适用于复杂知识图谱和多智能体场景
- 集成了 Deep Research 和 Context Engineering 等前沿技术，提升 LLM 推理深度

**适用场景**:
- 企业知识库问答系统：构建基于私有文档的智能问答和知识检索平台
- 智能文档处理场景：自动化解析和理解复杂业务文档（合同、报告、技术文档等）
- Agent 工作流开发：构建具备深度检索和推理能力的 AI Agent 应用



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,059 |
| 语言 | TypeScript |
| Forks | 6,543 |
| Issues | 228 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一个专为 AI 时代打造的网页数据提取利器，能将任意网站内容智能转换为 LLM 可直接使用的 markdown 或结构化数据，拥有近 10 万 Stars 验证其价值。对于需要构建 RAG 应用、AI Agent 或数据驱动型产品的团队，它能大幅降低数据采集和处理成本，是连接 Web 数据与大语言模型的理想桥梁。

**技术亮点**:
- 🧠 LLM-Ready 输出格式：自动将复杂 HTML 转换为干净的 Markdown 或结构化 JSON，直接喂给大模型无需二次处理
- 🕷️ 智能爬虫引擎：支持动态渲染页面、JS 执行、深度爬取，能处理传统爬虫难以应对的现代 Web 应用
- 🔌 开箱即用的 Web Data API：提供 RESTful API 接口，支持批量抓取、增量更新、自定义 Schema 提取
- 🔒 企业级稳定性：支持代理轮换、速率限制、反爬绕过，确保大规模数据采集的稳定性
- 🛠️ TypeScript 生态：类型安全、易于集成到现代前端/Node.js 技术栈

**适用场景**:
- 🤖 RAG 应用与 AI Agent：为 GPT/Claude 等大模型提供实时网页知识库，构建智能问答和决策系统
- 📊 商业情报与竞品监控：自动化抓取行业网站、电商价格、新闻资讯，生成结构化数据用于分析
- 💾 训练数据与微调数据集构建：批量采集网页内容，为 LLM 微调或知识蒸馏准备高质量语料



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,678 |
| 语言 | JavaScript |
| Forks | 12,267 |
| Issues | 41 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的 AI 智能体增强框架，通过整合技能系统、直觉机制、记忆管理和安全防护，显著提升 Claude Code、Cursor 等 AI 编程助手的开发效率和代码质量，是追求 AI 辅助开发极致体验的必备工具。

**技术亮点**:
- 多维度智能体增强系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）三大核心模块，让 AI 助手具备持续学习和上下文感知能力
- 跨平台兼容架构：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，实现一次配置多平台复用
- 研究驱动开发模式：内置 Research-first 开发方法论，确保 AI 生成代码基于最佳实践和最新技术方案
- MCP 协议深度集成：通过 Model Context Protocol 实现与外部工具和数据源的无缝连接，扩展 AI 助手能力边界
- 企业级安全防护：内置安全审计和代码检测机制，保障 AI 生成代码的安全性和合规性

**适用场景**:
- 企业研发团队：标准化 AI 辅助开发流程，提升团队协作效率和代码质量一致性
- 个人开发者/独立创作者：快速构建高质量项目原型，显著缩短从想法到产品的开发周期
- AI 应用开发者：作为基础框架快速搭建具备记忆、技能和安全能力的智能体应用



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,164 |
| 语言 | Go |
| Forks | 3,765 |
| Issues | 144 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI API 的完全免费开源替代方案，专为本地自托管设计，无需 GPU 即可在消费级硬件上运行大语言模型，提供与 OpenAI 兼容的 API 接口，支持文本生成、图像、音频、视频等多模态能力，非常适合注重隐私和成本控制的场景。

**技术亮点**:
- 零 GPU 依赖，支持在普通消费级硬件上运行 GGUF、Transformers、Diffusers 等多种模型格式
- OpenAI API 兼容，支持 drop-in replacement 无缝迁移现有应用
- 全栈多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、TTS 等
- 分布式与 P2P 去中心化推理架构，支持 libp2p 协议进行节点通信
- 集成 MCP（Model Context Protocol）与 Agent 能力，支持智能体开发

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护、无法使用云服务的金融机构、医疗等敏感行业
- 个人开发者学习与实验：在个人电脑上低成本体验和开发 AI 应用，无需购买昂贵 GPU
- 边缘设备与离线场景：需要在无网络或弱网环境下运行的 IoT 设备、移动应用等



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,055 |
| 语言 | TypeScript |
| Forks | 14,820 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 74K+ stars 的明星级 AI Agent 平台，它重新定义了人与 AI 的协作方式，将 Agent 作为工作交互的基本单元。项目支持多 Agent 协作、可视化团队设计，并兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，是构建智能化工作流的理想选择。

**技术亮点**:
- 多 Agent 协作能力：支持多个 AI Agent 智能体协同工作，实现复杂任务的自动化处理
- 模型生态丰富：深度集成 OpenAI、Claude、Gemini、GPT、DeepSeek 等多种主流大语言模型
- MCP 协议支持：内置知识库和 MCP（Model Context Protocol）协议，增强 Agent 上下文理解能力
- 可视化团队设计：提供低代码的 Agent 团队编排工具，支持拖拽式工作流搭建
- 全栈 TypeScript 架构：采用 TypeScript 全栈开发，确保类型安全和开发体验

**适用场景**:
- 企业智能助手构建：为企业搭建多职能 AI 团队，如客服、数据分析、内容创作等协作场景
- 个人知识管理：结合知识库功能，打造个性化的 AI 第二大脑，提升学习和工作效率
- AI 应用快速原型开发：开发者可基于平台快速验证和部署多 Agent 应用，缩短产品上市周期



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,843 |
| 语言 | Python |
| Forks | 8,390 |
| Issues | 931 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个ACL 2024 收录的统一高效微调框架，支持100多种大语言模型和视觉语言模型，是目前GitHub上最热门的LLM微调工具之一（近6.9万Stars）。它将LoRA、QLoRA、全量微调、RLHF等多种微调方法整合到统一界面，极大降低了模型微调的技术门槛和工程复杂度。

**技术亮点**:
- 支持100+ LLMs和VLMs的统一微调，包括Llama、Qwen、DeepSeek、Gemma等主流模型
- 集成多种微调技术：LoRA、QLoRA、全量微调、RLHF、指令微调等
- 支持量化训练（Quantization）和MoE架构，降低显存需求和训练成本
- 提供WebUI和CLI双模式，无需编码即可完成模型微调
- 兼容PEFT和Transformers生态，易于集成到现有工作流

**适用场景**:
- 企业快速定制私有领域大模型，如法律、医疗、金融等行业专属LLM
- 个人开发者或研究者在消费级GPU上低成本微调和实验各类开源模型
- 构建对话机器人和AI Agent，通过指令微调和RLHF提升模型交互能力



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,349 |
| 语言 | Python |
| Forks | 9,842 |
| Issues | 349 |
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
| Stars | 39,023 |
| 语言 | JavaScript |
| Forks | 2,840 |
| Issues | 154 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,218 |
| 语言 | TypeScript |
| Forks | 5,655 |
| Issues | 62 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,828 |
| 语言 | TypeScript |
| Forks | 7,058 |
| Issues | 453 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,486 |
| 语言 | Java |
| Forks | 15,844 |
| Issues | 54 |
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
| Stars | 38,805 |
| 语言 | Python |
| Forks | 6,152 |
| Issues | 150 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,540 |
| 语言 | Python |
| Forks | 2,076 |
| Issues | 93 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 103,044 |
| 语言 | Python |
| Forks | 15,022 |
| Issues | 11 |
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
| Stars | 56,563 |
| 语言 | JavaScript |
| Forks | 6,112 |
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
| Stars | 69,502 |
| 语言 | Python |
| Forks | 8,712 |
| Issues | 330 |
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
| Stars | 57,311 |
| 语言 | Python |
| Forks | 4,821 |
| Issues | 1,022 |
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
| Stars | 42,151 |
| 语言 | TypeScript |
| Forks | 3,136 |
| Issues | 439 |
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
| Stars | 81,782 |
| 语言 | Python |
| Forks | 9,627 |
| Issues | 222 |
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
| Stars | 50,948 |
| 语言 | TypeScript |
| Forks | 23,977 |
| Issues | 806 |
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
| Stars | 180,337 |
| 语言 | TypeScript |
| Forks | 56,007 |
| Issues | 1,448 |
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
| Stars | 146,001 |
| 语言 | Python |
| Forks | 8,626 |
| Issues | 895 |
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
| Stars | 54,610 |
| 语言 | Jupyter Notebook |
| Forks | 18,894 |
| Issues | 4 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,043 |
| 语言 | MDX |
| Forks | 7,689 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,258 |
| 语言 | TypeScript |
| Forks | 3,593 |
| Issues | 285 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,477 |
| 语言 | Jupyter Notebook |
| Forks | 5,373 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,638 |
| 语言 | Python |
| Forks | 4,754 |
| Issues | 352 |
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
| Stars | 128,132 |
| 语言 | Python |
| Forks | 18,113 |
| Issues | 324 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最活跃的开源 AI 聊天界面项目之一，拥有 12.8万+ Stars，支持 Ollama、OpenAI 等多种后端，提供开箱即用的自托管方案，是个人和企业快速部署私有化 AI 助手的最佳选择。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库构建，增强 AI 回答准确性
- 支持 MCP（Model Context Protocol）：可与外部工具和数据源无缝集成
- 完全自托管：数据隐私可控，适合私有化部署，提供认证和权限管理
- 现代化 Web UI：用户友好的聊天界面，支持多用户协作和会话管理

**适用场景**:
- 企业私有化 AI 助手：在公司内部部署，连接本地 Ollama 模型，保障数据安全与隐私
- 个人 AI 学习与研究：搭建本地 LLM 平台，低成本体验和测试各类开源模型
- AI 应用开发测试：作为 LLM 应用的前端界面，快速验证 Prompt 和 RAG 方案



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,709 |
| 语言 | Python |
| Forks | 8,476 |
| Issues | 3,141 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款顶级的开源 RAG 引擎，将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型提供卓越的上下文层，75K+ Stars 证明了其在 AI 社区的领先地位和广泛认可。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供智能化的文档理解和上下文检索能力
- 支持多种主流 LLM 后端（OpenAI、Ollama、DeepSeek），具备极强的生态兼容性
- 内置高级文档解析器和文档理解引擎，支持复杂文档的深度处理
- 支持 GraphRAG 和 MCP 协议，适用于复杂知识图谱和多智能体场景
- 集成了 Deep Research 和 Context Engineering 等前沿技术，提升 LLM 推理深度

**适用场景**:
- 企业知识库问答系统：构建基于私有文档的智能问答和知识检索平台
- 智能文档处理场景：自动化解析和理解复杂业务文档（合同、报告、技术文档等）
- Agent 工作流开发：构建具备深度检索和推理能力的 AI Agent 应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,055 |
| 语言 | TypeScript |
| Forks | 14,820 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 74K+ stars 的明星级 AI Agent 平台，它重新定义了人与 AI 的协作方式，将 Agent 作为工作交互的基本单元。项目支持多 Agent 协作、可视化团队设计，并兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，是构建智能化工作流的理想选择。

**技术亮点**:
- 多 Agent 协作能力：支持多个 AI Agent 智能体协同工作，实现复杂任务的自动化处理
- 模型生态丰富：深度集成 OpenAI、Claude、Gemini、GPT、DeepSeek 等多种主流大语言模型
- MCP 协议支持：内置知识库和 MCP（Model Context Protocol）协议，增强 Agent 上下文理解能力
- 可视化团队设计：提供低代码的 Agent 团队编排工具，支持拖拽式工作流搭建
- 全栈 TypeScript 架构：采用 TypeScript 全栈开发，确保类型安全和开发体验

**适用场景**:
- 企业智能助手构建：为企业搭建多职能 AI 团队，如客服、数据分析、内容创作等协作场景
- 个人知识管理：结合知识库功能，打造个性化的 AI 第二大脑，提升学习和工作效率
- AI 应用快速原型开发：开发者可基于平台快速验证和部署多 Agent 应用，缩短产品上市周期



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,023 |
| 语言 | JavaScript |
| Forks | 2,840 |
| Issues | 154 |
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
| Stars | 45,486 |
| 语言 | Java |
| Forks | 15,844 |
| Issues | 54 |
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
| Stars | 38,805 |
| 语言 | Python |
| Forks | 6,152 |
| Issues | 150 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,540 |
| 语言 | Python |
| Forks | 2,076 |
| Issues | 93 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### Shubhamsaboo/awesome-llm-apps

**描述**: Collection of awesome LLM apps with AI Agents and RAG using OpenAI, Anthropic, Gemini and opensource models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 103,044 |
| 语言 | Python |
| Forks | 15,022 |
| Issues | 11 |
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
| Stars | 99,410 |
| 语言 | TypeScript |
| Forks | 11,848 |
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
| Stars | 56,563 |
| 语言 | JavaScript |
| Forks | 6,112 |
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
| Stars | 50,948 |
| 语言 | TypeScript |
| Forks | 23,977 |
| Issues | 806 |
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
| Stars | 72,757 |
| 语言 | Python |
| Forks | 10,007 |
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
| Stars | 43,442 |
| 语言 | Go |
| Forks | 3,910 |
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
| Stars | 31,662 |
| 语言 | Python |
| Forks | 3,340 |
| Issues | 80 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,043 |
| 语言 | MDX |
| Forks | 7,689 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,258 |
| 语言 | TypeScript |
| Forks | 3,593 |
| Issues | 285 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,477 |
| 语言 | Jupyter Notebook |
| Forks | 5,373 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
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
| Stars | 128,132 |
| 语言 | Python |
| Forks | 18,113 |
| Issues | 324 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前最活跃的开源 AI 聊天界面项目之一，拥有 12.8万+ Stars，支持 Ollama、OpenAI 等多种后端，提供开箱即用的自托管方案，是个人和企业快速部署私有化 AI 助手的最佳选择。

**技术亮点**:
- 支持多后端架构：兼容 Ollama、OpenAI API 等多种 LLM 提供商，灵活切换模型
- 内置 RAG（检索增强生成）能力：支持文档上传和知识库构建，增强 AI 回答准确性
- 支持 MCP（Model Context Protocol）：可与外部工具和数据源无缝集成
- 完全自托管：数据隐私可控，适合私有化部署，提供认证和权限管理
- 现代化 Web UI：用户友好的聊天界面，支持多用户协作和会话管理

**适用场景**:
- 企业私有化 AI 助手：在公司内部部署，连接本地 Ollama 模型，保障数据安全与隐私
- 个人 AI 学习与研究：搭建本地 LLM 平台，低成本体验和测试各类开源模型
- AI 应用开发测试：作为 LLM 应用的前端界面，快速验证 Prompt 和 RAG 方案



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,709 |
| 语言 | Python |
| Forks | 8,476 |
| Issues | 3,141 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是一款顶级的开源 RAG 引擎，将前沿的检索增强生成技术与 Agent 能力深度融合，为大语言模型提供卓越的上下文层，75K+ Stars 证明了其在 AI 社区的领先地位和广泛认可。

**技术亮点**:
- 融合 RAG 与 Agent 能力，提供智能化的文档理解和上下文检索能力
- 支持多种主流 LLM 后端（OpenAI、Ollama、DeepSeek），具备极强的生态兼容性
- 内置高级文档解析器和文档理解引擎，支持复杂文档的深度处理
- 支持 GraphRAG 和 MCP 协议，适用于复杂知识图谱和多智能体场景
- 集成了 Deep Research 和 Context Engineering 等前沿技术，提升 LLM 推理深度

**适用场景**:
- 企业知识库问答系统：构建基于私有文档的智能问答和知识检索平台
- 智能文档处理场景：自动化解析和理解复杂业务文档（合同、报告、技术文档等）
- Agent 工作流开发：构建具备深度检索和推理能力的 AI Agent 应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,678 |
| 语言 | JavaScript |
| Forks | 12,267 |
| Issues | 41 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的 AI 智能体增强框架，通过整合技能系统、直觉机制、记忆管理和安全防护，显著提升 Claude Code、Cursor 等 AI 编程助手的开发效率和代码质量，是追求 AI 辅助开发极致体验的必备工具。

**技术亮点**:
- 多维度智能体增强系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）三大核心模块，让 AI 助手具备持续学习和上下文感知能力
- 跨平台兼容架构：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，实现一次配置多平台复用
- 研究驱动开发模式：内置 Research-first 开发方法论，确保 AI 生成代码基于最佳实践和最新技术方案
- MCP 协议深度集成：通过 Model Context Protocol 实现与外部工具和数据源的无缝连接，扩展 AI 助手能力边界
- 企业级安全防护：内置安全审计和代码检测机制，保障 AI 生成代码的安全性和合规性

**适用场景**:
- 企业研发团队：标准化 AI 辅助开发流程，提升团队协作效率和代码质量一致性
- 个人开发者/独立创作者：快速构建高质量项目原型，显著缩短从想法到产品的开发周期
- AI 应用开发者：作为基础框架快速搭建具备记忆、技能和安全能力的智能体应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,055 |
| 语言 | TypeScript |
| Forks | 14,820 |
| Issues | 654 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个拥有 74K+ stars 的明星级 AI Agent 平台，它重新定义了人与 AI 的协作方式，将 Agent 作为工作交互的基本单元。项目支持多 Agent 协作、可视化团队设计，并兼容 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，是构建智能化工作流的理想选择。

**技术亮点**:
- 多 Agent 协作能力：支持多个 AI Agent 智能体协同工作，实现复杂任务的自动化处理
- 模型生态丰富：深度集成 OpenAI、Claude、Gemini、GPT、DeepSeek 等多种主流大语言模型
- MCP 协议支持：内置知识库和 MCP（Model Context Protocol）协议，增强 Agent 上下文理解能力
- 可视化团队设计：提供低代码的 Agent 团队编排工具，支持拖拽式工作流搭建
- 全栈 TypeScript 架构：采用 TypeScript 全栈开发，确保类型安全和开发体验

**适用场景**:
- 企业智能助手构建：为企业搭建多职能 AI 团队，如客服、数据分析、内容创作等协作场景
- 个人知识管理：结合知识库功能，打造个性化的 AI 第二大脑，提升学习和工作效率
- AI 应用快速原型开发：开发者可基于平台快速验证和部署多 Agent 应用，缩短产品上市周期



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,527 |
| 语言 | HTML |
| Forks | 20,195 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源项目，为AI提示词工程提供了最全面的社区驱动资源库。它支持完全自托管，让组织能够在保证隐私的前提下建立自己的提示词库，是企业AI应用落地的实用工具。

**技术亮点**:
- 基于 Next.js + TypeScript 技术栈构建，提供现代化的Web界面体验
- 支持完全自托管部署，满足企业级隐私保护和数据安全需求
- 采用 Creative Commons Zero 许可证，实现真正意义上的开源共享
- 覆盖 ChatGPT、Claude、Gemini 等主流LLM平台的提示词，具备良好的兼容性
- 社区驱动的持续更新机制，保持与AI技术发展同步

**适用场景**:
- 企业内部建立私有提示词库，沉淀AI应用最佳实践并保护商业机密
- 个人开发者学习提示词工程技巧，快速掌握与各类AI模型的高效交互方法
- 团队协作共享高质量提示词模板，提升AI辅助开发和内容创作的效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,906 |
| 语言 | Jupyter Notebook |
| Forks | 13,572 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个近9万Star的现象级教程项目，通过Jupyter Notebook手把手教你用PyTorch从零实现一个ChatGPT风格的大语言模型，非常适合想深入理解LLM底层原理的开发者。项目将复杂的Transformer架构拆解为可执行的步骤，兼具理论深度和实践价值。

**技术亮点**:
- 从零实现：不依赖高级框架，逐步构建GPT架构的每个组件（注意力机制、Transformer层等）
- 基于PyTorch的完整LLM实现：涵盖数据处理、模型训练、推理生成的完整pipeline
- 交互式学习：使用Jupyter Notebook，每一步都可运行、可视化和调试
- 配套书籍教程：项目与Sebastian Raschka的《Build a Large Language Model》书籍配套，学习资源丰富
- 涵盖现代LLM核心技术：包括Transformer架构、tokenizer、预训练、微调等关键环节

**适用场景**:
- LLM原理学习：适合想从底层理解大语言模型工作机制的学生和开发者
- 企业AI团队培训：可作为内部培训教材，帮助团队成员建立扎实的LLM技术基础
- 自定义模型开发：为需要从零构建或深度定制LLM的研究者和工程师提供参考实现



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企微、QQ、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,349 |
| 语言 | Python |
| Forks | 9,842 |
| Issues | 349 |
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
| Stars | 39,023 |
| 语言 | JavaScript |
| Forks | 2,840 |
| Issues | 154 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,218 |
| 语言 | TypeScript |
| Forks | 5,655 |
| Issues | 62 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### danny-avila/LibreChat

**描述**: Enhanced ChatGPT Clone: Features Agents, MCP, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,828 |
| 语言 | TypeScript |
| Forks | 7,058 |
| Issues | 453 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,540 |
| 语言 | Python |
| Forks | 2,076 |
| Issues | 93 |
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
| Stars | 56,563 |
| 语言 | JavaScript |
| Forks | 6,112 |
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
| Stars | 69,502 |
| 语言 | Python |
| Forks | 8,712 |
| Issues | 330 |
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
| Stars | 57,311 |
| 语言 | Python |
| Forks | 4,821 |
| Issues | 1,022 |
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
| Stars | 42,151 |
| 语言 | TypeScript |
| Forks | 3,136 |
| Issues | 439 |
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
| Stars | 50,948 |
| 语言 | TypeScript |
| Forks | 23,977 |
| Issues | 806 |
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
| Stars | 34,773 |
| 语言 | HTML |
| Forks | 5,594 |
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
| Stars | 73,872 |
| 语言 | Python |
| Forks | 14,608 |
| Issues | 3,802 |
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
| Stars | 39,062 |
| 语言 | TypeScript |
| Forks | 3,952 |
| Issues | 1,084 |
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
| Stars | 146,001 |
| 语言 | Python |
| Forks | 8,626 |
| Issues | 895 |
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
| Stars | 165,784 |
| 语言 | Go |
| Forks | 15,095 |
| Issues | 2,695 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,043 |
| 语言 | MDX |
| Forks | 7,689 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,770 |
| 语言 | Rust |
| Forks | 9,166 |
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
| Stars | 91,329 |
| 语言 | Python |
| Forks | 5,416 |
| Issues | 480 |
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
| Stars | 47,297 |
| 语言 | Python |
| Forks | 4,593 |
| Issues | 83 |
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
| Stars | 36,825 |
| 语言 | Python |
| Forks | 2,569 |
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
| Stars | 46,638 |
| 语言 | Python |
| Forks | 4,754 |
| Issues | 352 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


## 🧠 机器学习框架 (12 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,843 |
| 语言 | Python |
| Forks | 8,390 |
| Issues | 931 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个ACL 2024 收录的统一高效微调框架，支持100多种大语言模型和视觉语言模型，是目前GitHub上最热门的LLM微调工具之一（近6.9万Stars）。它将LoRA、QLoRA、全量微调、RLHF等多种微调方法整合到统一界面，极大降低了模型微调的技术门槛和工程复杂度。

**技术亮点**:
- 支持100+ LLMs和VLMs的统一微调，包括Llama、Qwen、DeepSeek、Gemma等主流模型
- 集成多种微调技术：LoRA、QLoRA、全量微调、RLHF、指令微调等
- 支持量化训练（Quantization）和MoE架构，降低显存需求和训练成本
- 提供WebUI和CLI双模式，无需编码即可完成模型微调
- 兼容PEFT和Transformers生态，易于集成到现有工作流

**适用场景**:
- 企业快速定制私有领域大模型，如法律、医疗、金融等行业专属LLM
- 个人开发者或研究者在消费级GPU上低成本微调和实验各类开源模型
- 构建对话机器人和AI Agent，通过指令微调和RLHF提升模型交互能力



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,386 |
| 语言 | Python |
| Forks | 6,230 |
| Issues | 66 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是全球最受欢迎的开源金融数据分析平台，将多维度金融数据（股票、加密货币、期权、宏观经济等）整合到统一的 Python 接口中，为量化分析师和 AI 应用提供专业级数据基础设施，解决了金融数据来源分散、API 成本高昂的痛点。

**技术亮点**:
- 统一数据接口架构 - 支持股票、加密货币、期权、衍生品、固定收益等多种金融资产类别的数据获取
- AI Agent 原生支持 - 专为 AI 和机器学习应用优化的数据管道，可直接对接大语言模型
- 模块化扩展系统 - 开放式架构允许用户自定义数据源和功能扩展
- Python 优先设计 - 提供完整的 Python SDK，便于量化分析和算法交易集成
- 多数据源聚合 - 整合多个金融数据提供商，提供标准化数据输出

**适用场景**:
- 量化交易策略研发 - 适合对冲基金和量化团队进行多资产类别的因子研究和回测
- 金融科技产品开发 - 创业公司可基于此快速构建投资分析、投顾机器人等金融应用
- 学术研究与教学 - 高校和研究机构用于金融工程、计量经济学课程的教学与实证研究



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 153,527 |
| 语言 | HTML |
| Forks | 20,195 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源项目，为AI提示词工程提供了最全面的社区驱动资源库。它支持完全自托管，让组织能够在保证隐私的前提下建立自己的提示词库，是企业AI应用落地的实用工具。

**技术亮点**:
- 基于 Next.js + TypeScript 技术栈构建，提供现代化的Web界面体验
- 支持完全自托管部署，满足企业级隐私保护和数据安全需求
- 采用 Creative Commons Zero 许可证，实现真正意义上的开源共享
- 覆盖 ChatGPT、Claude、Gemini 等主流LLM平台的提示词，具备良好的兼容性
- 社区驱动的持续更新机制，保持与AI技术发展同步

**适用场景**:
- 企业内部建立私有提示词库，沉淀AI应用最佳实践并保护商业机密
- 个人开发者学习提示词工程技巧，快速掌握与各类AI模型的高效交互方法
- 团队协作共享高质量提示词模板，提升AI辅助开发和内容创作的效率



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,906 |
| 语言 | Jupyter Notebook |
| Forks | 13,572 |
| Issues | 4 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

这是一个近9万Star的现象级教程项目，通过Jupyter Notebook手把手教你用PyTorch从零实现一个ChatGPT风格的大语言模型，非常适合想深入理解LLM底层原理的开发者。项目将复杂的Transformer架构拆解为可执行的步骤，兼具理论深度和实践价值。

**技术亮点**:
- 从零实现：不依赖高级框架，逐步构建GPT架构的每个组件（注意力机制、Transformer层等）
- 基于PyTorch的完整LLM实现：涵盖数据处理、模型训练、推理生成的完整pipeline
- 交互式学习：使用Jupyter Notebook，每一步都可运行、可视化和调试
- 配套书籍教程：项目与Sebastian Raschka的《Build a Large Language Model》书籍配套，学习资源丰富
- 涵盖现代LLM核心技术：包括Transformer架构、tokenizer、预训练、微调等关键环节

**适用场景**:
- LLM原理学习：适合想从底层理解大语言模型工作机制的学生和开发者
- 企业AI团队培训：可作为内部培训教材，帮助团队成员建立扎实的LLM技术基础
- 自定义模型开发：为需要从零构建或深度定制LLM的研究者和工程师提供参考实现



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,201 |
| 语言 | Python |
| Forks | 32,559 |
| Issues | 2,290 |
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
| Stars | 73,872 |
| 语言 | Python |
| Forks | 14,608 |
| Issues | 3,802 |
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
| Stars | 106,546 |
| 语言 | Python |
| Forks | 12,264 |
| Issues | 3,864 |
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
| Stars | 98,470 |
| 语言 | Python |
| Forks | 27,264 |
| Issues | 18,051 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,043 |
| 语言 | MDX |
| Forks | 7,689 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,258 |
| 语言 | TypeScript |
| Forks | 3,593 |
| Issues | 285 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### patchy631/ai-engineering-hub

**描述**: In-depth tutorials on LLMs, RAGs and real-world AI agent applications.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 32,477 |
| 语言 | Jupyter Notebook |
| Forks | 5,373 |
| Issues | 124 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,926 |
| 语言 | Python |
| Forks | 30,194 |
| Issues | 2,469 |
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
| Stars | 93,678 |
| 语言 | JavaScript |
| Forks | 12,267 |
| Issues | 41 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个高性能的 AI 智能体增强框架，通过整合技能系统、直觉机制、记忆管理和安全防护，显著提升 Claude Code、Cursor 等 AI 编程助手的开发效率和代码质量，是追求 AI 辅助开发极致体验的必备工具。

**技术亮点**:
- 多维度智能体增强系统：集成技能（Skills）、直觉（Instincts）、记忆（Memory）三大核心模块，让 AI 助手具备持续学习和上下文感知能力
- 跨平台兼容架构：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，实现一次配置多平台复用
- 研究驱动开发模式：内置 Research-first 开发方法论，确保 AI 生成代码基于最佳实践和最新技术方案
- MCP 协议深度集成：通过 Model Context Protocol 实现与外部工具和数据源的无缝连接，扩展 AI 助手能力边界
- 企业级安全防护：内置安全审计和代码检测机制，保障 AI 生成代码的安全性和合规性

**适用场景**:
- 企业研发团队：标准化 AI 辅助开发流程，提升团队协作效率和代码质量一致性
- 个人开发者/独立创作者：快速构建高质量项目原型，显著缩短从想法到产品的开发周期
- AI 应用开发者：作为基础框架快速搭建具备记忆、技能和安全能力的智能体应用



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,164 |
| 语言 | Go |
| Forks | 3,765 |
| Issues | 144 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI API 的完全免费开源替代方案，专为本地自托管设计，无需 GPU 即可在消费级硬件上运行大语言模型，提供与 OpenAI 兼容的 API 接口，支持文本生成、图像、音频、视频等多模态能力，非常适合注重隐私和成本控制的场景。

**技术亮点**:
- 零 GPU 依赖，支持在普通消费级硬件上运行 GGUF、Transformers、Diffusers 等多种模型格式
- OpenAI API 兼容，支持 drop-in replacement 无缝迁移现有应用
- 全栈多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、TTS 等
- 分布式与 P2P 去中心化推理架构，支持 libp2p 协议进行节点通信
- 集成 MCP（Model Context Protocol）与 Agent 能力，支持智能体开发

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护、无法使用云服务的金融机构、医疗等敏感行业
- 个人开发者学习与实验：在个人电脑上低成本体验和开发 AI 应用，无需购买昂贵 GPU
- 边缘设备与离线场景：需要在无网络或弱网环境下运行的 IoT 设备、移动应用等



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,502 |
| 语言 | Python |
| Forks | 8,712 |
| Issues | 330 |
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
| Stars | 42,151 |
| 语言 | TypeScript |
| Forks | 3,136 |
| Issues | 439 |
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
| Stars | 180,337 |
| 语言 | TypeScript |
| Forks | 56,007 |
| Issues | 1,448 |
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
| Stars | 412,989 |
| 语言 | Python |
| Forks | 44,691 |
| Issues | 1,039 |
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
| Stars | 152,406 |
| 语言 | Python |
| Forks | 12,365 |
| Issues | 2,386 |
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
| Stars | 96,449 |
| 语言 | Python |
| Forks | 8,896 |
| Issues | 163 |
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
| Stars | 73,948 |
| 语言 | Python |
| Forks | 8,777 |
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
| Stars | 182,929 |
| 语言 | TypeScript |
| Forks | 38,662 |
| Issues | 15,463 |
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
| Stars | 93,887 |
| 语言 | TypeScript |
| Forks | 9,397 |
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
| Stars | 78,561 |
| 语言 | TypeScript |
| Forks | 5,714 |
| Issues | 725 |
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
| Stars | 76,764 |
| 语言 | TypeScript |
| Forks | 6,569 |
| Issues | 167 |
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
| Stars | 75,672 |
| 语言 | JavaScript |
| Forks | 7,271 |
| Issues | 707 |
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
| Stars | 78,853 |
| 语言 | Go |
| Forks | 2,733 |
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
| Stars | 74,812 |
| 语言 | Go |
| Forks | 2,627 |
| Issues | 940 |
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
| Stars | 36,825 |
| 语言 | Python |
| Forks | 2,569 |
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
| Stars | 54,630 |
| 语言 | JavaScript |
| Forks | 4,042 |
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
| Stars | 42,151 |
| 语言 | TypeScript |
| Forks | 3,136 |
| Issues | 439 |
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
| Stars | 180,337 |
| 语言 | TypeScript |
| Forks | 56,007 |
| Issues | 1,448 |
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
| Stars | 51,709 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 215 |
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
| Stars | 121,289 |
| 语言 | Go |
| Forks | 42,714 |
| Issues | 2,613 |
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
| Stars | 71,554 |
| 语言 | Go |
| Forks | 18,915 |
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
| Stars | 54,400 |
| 语言 | Go |
| Forks | 6,486 |
| Issues | 2,865 |
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
| Stars | 47,592 |
| 语言 | Go |
| Forks | 5,070 |
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
| Stars | 93,887 |
| 语言 | TypeScript |
| Forks | 9,397 |
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
| Stars | 75,636 |
| 语言 | TypeScript |
| Forks | 6,439 |
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
| Stars | 84,315 |
| 语言 | JavaScript |
| Forks | 7,550 |
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
| Stars | 62,317 |
| 语言 | Go |
| Forks | 5,883 |
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
| Stars | 58,097 |
| 语言 | Go |
| Forks | 4,203 |
| Issues | 20 |
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
| Stars | 46,638 |
| 语言 | Python |
| Forks | 4,754 |
| Issues | 352 |
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
| Stars | 69,467 |
| 语言 | Go |
| Forks | 1,886 |
| Issues | 303 |
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
| Stars | 84,315 |
| 语言 | JavaScript |
| Forks | 7,550 |
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
| Stars | 63,271 |
| 语言 | Go |
| Forks | 10,254 |
| Issues | 748 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (13 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,164 |
| 语言 | Go |
| Forks | 3,765 |
| Issues | 144 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是 OpenAI API 的完全免费开源替代方案，专为本地自托管设计，无需 GPU 即可在消费级硬件上运行大语言模型，提供与 OpenAI 兼容的 API 接口，支持文本生成、图像、音频、视频等多模态能力，非常适合注重隐私和成本控制的场景。

**技术亮点**:
- 零 GPU 依赖，支持在普通消费级硬件上运行 GGUF、Transformers、Diffusers 等多种模型格式
- OpenAI API 兼容，支持 drop-in replacement 无缝迁移现有应用
- 全栈多模态能力：支持文本生成、图像生成、音频/视频生成、语音克隆、TTS 等
- 分布式与 P2P 去中心化推理架构，支持 libp2p 协议进行节点通信
- 集成 MCP（Model Context Protocol）与 Agent 能力，支持智能体开发

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护、无法使用云服务的金融机构、医疗等敏感行业
- 个人开发者学习与实验：在个人电脑上低成本体验和开发 AI 应用，无需购买昂贵 GPU
- 边缘设备与离线场景：需要在无网络或弱网环境下运行的 IoT 设备、移动应用等



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 412,989 |
| 语言 | Python |
| Forks | 44,691 |
| Issues | 1,039 |
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
| Stars | 96,449 |
| 语言 | Python |
| Forks | 8,896 |
| Issues | 163 |
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
| Stars | 87,121 |
| 语言 | Python |
| Forks | 33,777 |
| Issues | 432 |
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
| Stars | 100,148 |
| 语言 | TypeScript |
| Forks | 27,136 |
| Issues | 1,100 |
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
| Stars | 78,561 |
| 语言 | TypeScript |
| Forks | 5,714 |
| Issues | 725 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,672 |
| 语言 | JavaScript |
| Forks | 7,271 |
| Issues | 707 |
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
| Stars | 55,949 |
| 语言 | JavaScript |
| Forks | 10,216 |
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
| Stars | 88,304 |
| 语言 | Go |
| Forks | 8,574 |
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
| Stars | 71,012 |
| 语言 | Go |
| Forks | 4,685 |
| Issues | 249 |
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
| Stars | 56,979 |
| 语言 | Go |
| Forks | 3,198 |
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
| Stars | 36,825 |
| 语言 | Python |
| Forks | 2,569 |
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
| Stars | 68,918 |
| 语言 | JavaScript |
| Forks | 22,882 |
| Issues | 198 |
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
| Stars | 99,410 |
| 语言 | TypeScript |
| Forks | 11,848 |
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
| Stars | 56,563 |
| 语言 | JavaScript |
| Forks | 6,112 |
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
| Stars | 43,442 |
| 语言 | Go |
| Forks | 3,910 |
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
| Stars | 51,709 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 215 |
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
| Stars | 153,527 |
| 语言 | HTML |
| Forks | 20,195 |
| Issues | 38 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是一个拥有超过15万星标的顶级开源项目，为AI提示词工程提供了最全面的社区驱动资源库。它支持完全自托管，让组织能够在保证隐私的前提下建立自己的提示词库，是企业AI应用落地的实用工具。

**技术亮点**:
- 基于 Next.js + TypeScript 技术栈构建，提供现代化的Web界面体验
- 支持完全自托管部署，满足企业级隐私保护和数据安全需求
- 采用 Creative Commons Zero 许可证，实现真正意义上的开源共享
- 覆盖 ChatGPT、Claude、Gemini 等主流LLM平台的提示词，具备良好的兼容性
- 社区驱动的持续更新机制，保持与AI技术发展同步

**适用场景**:
- 企业内部建立私有提示词库，沉淀AI应用最佳实践并保护商业机密
- 个人开发者学习提示词工程技巧，快速掌握与各类AI模型的高效交互方法
- 团队协作共享高质量提示词模板，提升AI辅助开发和内容创作的效率



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,218 |
| 语言 | TypeScript |
| Forks | 5,655 |
| Issues | 62 |
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
| Stars | 34,773 |
| 语言 | HTML |
| Forks | 5,594 |
| Issues | 17 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,043 |
| 语言 | MDX |
| Forks | 7,689 |
| Issues | 248 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,492 |
| 语言 | TypeScript |
| Forks | 9,936 |
| Issues | 2,201 |
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
| Stars | 86,854 |
| 语言 | TypeScript |
| Forks | 8,752 |
| Issues | 1,611 |
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
| Stars | 127,173 |
| 语言 | JavaScript |
| Forks | 12,456 |
| Issues | 6 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### jaywcjlove/awesome-mac

**描述**:  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy search and use.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,608 |
| 语言 | JavaScript |
| Forks | 7,517 |
| Issues | 226 |
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
| Stars | 167,910 |
| 语言 | Go |
| Forks | 13,072 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (65 个项目) { #其他 }


### 🌟 高优先级


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,032 |
| 语言 | Shell |
| Forks | 8,670 |
| Issues | 84 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,339 |
| 语言 | Python |
| Forks | 6,368 |
| Issues | 33 |
| 许可证 | Apache License 2.0 |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,331 |
| 语言 | Python |
| Forks | 6,717 |
| Issues | 625 |
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
| Stars | 132,514 |
| 语言 | Unknown |
| Forks | 33,528 |
| Issues | 132 |
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
| Stars | 384,373 |
| 语言 | Python |
| Forks | 66,046 |
| Issues | 75 |
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
| Stars | 113,150 |
| 语言 | TypeScript |
| Forks | 5,746 |
| Issues | 336 |
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
| Stars | 104,377 |
| 语言 | TypeScript |
| Forks | 7,602 |
| Issues | 194 |
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
| Stars | 48,001 |
| 语言 | Go |
| Forks | 10,254 |
| Issues | 1,893 |
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
| Stars | 98,853 |
| 语言 | C++ |
| Forks | 15,689 |
| Issues | 1,289 |
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
| Stars | 61,789 |
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
| Stars | 37,876 |
| 语言 | JavaScript |
| Forks | 3,070 |
| Issues | 6 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,804 |
| 语言 | TypeScript |
| Forks | 4,245 |
| Issues | 132 |
| 许可证 | MIT License |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 339,713 |
| 语言 | Python |
| Forks | 54,970 |
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
| Stars | 288,324 |
| 语言 | Python |
| Forks | 27,458 |
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
| Stars | 218,932 |
| 语言 | Python |
| Forks | 50,232 |
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
| Stars | 85,507 |
| 语言 | Python |
| Forks | 37,024 |
| Issues | 3,578 |
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
| Stars | 85,428 |
| 语言 | Python |
| Forks | 7,173 |
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
| Stars | 77,693 |
| 语言 | Python |
| Forks | 45,222 |
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
| Stars | 76,248 |
| 语言 | Python |
| Forks | 16,774 |
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
| Stars | 438,670 |
| 语言 | TypeScript |
| Forks | 43,723 |
| Issues | 235 |
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
| Stars | 351,379 |
| 语言 | TypeScript |
| Forks | 43,829 |
| Issues | 29 |
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
| Stars | 138,273 |
| 语言 | TypeScript |
| Forks | 16,472 |
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
| Stars | 119,280 |
| 语言 | TypeScript |
| Forks | 12,949 |
| Issues | 2,864 |
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
| Stars | 110,314 |
| 语言 | TypeScript |
| Forks | 8,275 |
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
| Stars | 108,232 |
| 语言 | TypeScript |
| Forks | 13,309 |
| Issues | 5,499 |
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
| Stars | 97,767 |
| 语言 | TypeScript |
| Forks | 54,578 |
| Issues | 1,372 |
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
| Stars | 95,358 |
| 语言 | TypeScript |
| Forks | 5,162 |
| Issues | 677 |
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
| Stars | 94,169 |
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
| Stars | 83,024 |
| 语言 | TypeScript |
| Forks | 7,577 |
| Issues | 32 |
| 许可证 | Other |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 81,707 |
| 语言 | TypeScript |
| Forks | 10,006 |
| Issues | 550 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,278 |
| 语言 | TypeScript |
| Forks | 7,951 |
| Issues | 678 |
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
| Stars | 244,120 |
| 语言 | JavaScript |
| Forks | 50,842 |
| Issues | 1,187 |
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
| Stars | 116,376 |
| 语言 | JavaScript |
| Forks | 35,129 |
| Issues | 2,551 |
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
| Stars | 111,483 |
| 语言 | JavaScript |
| Forks | 36,303 |
| Issues | 583 |
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
| Stars | 108,653 |
| 语言 | JavaScript |
| Forks | 11,560 |
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
| Stars | 98,060 |
| 语言 | JavaScript |
| Forks | 32,695 |
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
| Stars | 95,444 |
| 语言 | JavaScript |
| Forks | 15,270 |
| Issues | 48 |
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
| Stars | 86,131 |
| 语言 | JavaScript |
| Forks | 4,818 |
| Issues | 969 |
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
| Stars | 78,826 |
| 语言 | JavaScript |
| Forks | 31,580 |
| Issues | 268 |
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
| Stars | 70,819 |
| 语言 | JavaScript |
| Forks | 16,810 |
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
| Stars | 66,033 |
| 语言 | JavaScript |
| Forks | 9,336 |
| Issues | 202 |
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
| Stars | 62,231 |
| 语言 | JavaScript |
| Forks | 3,980 |
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
| Stars | 59,947 |
| 语言 | JavaScript |
| Forks | 5,618 |
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
| Stars | 59,873 |
| 语言 | JavaScript |
| Forks | 20,472 |
| Issues | 98 |
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
| Stars | 57,402 |
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
| Stars | 53,004 |
| 语言 | JavaScript |
| Forks | 10,599 |
| Issues | 473 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,104 |
| 语言 | JavaScript |
| Forks | 11,384 |
| Issues | 374 |
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
| Stars | 133,128 |
| 语言 | Go |
| Forks | 18,873 |
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
| Stars | 105,470 |
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
| Stars | 87,190 |
| 语言 | Go |
| Forks | 8,218 |
| Issues | 258 |
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
| Stars | 80,995 |
| 语言 | Go |
| Forks | 4,969 |
| Issues | 409 |
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
| Stars | 68,672 |
| 语言 | Go |
| Forks | 3,222 |
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
| Stars | 56,164 |
| 语言 | Go |
| Forks | 4,988 |
| Issues | 1,150 |
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
| Stars | 50,944 |
| 语言 | Go |
| Forks | 21,869 |
| Issues | 376 |
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
| Stars | 50,276 |
| 语言 | Go |
| Forks | 1,591 |
| Issues | 263 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,194 |
| 语言 | Go |
| Forks | 7,973 |
| Issues | 566 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 80,234 |
| 语言 | Python |
| Forks | 11,712 |
| Issues | 101 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
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
| Stars | 139,927 |
| 语言 | Python |
| Forks | 10,603 |
| Issues | 4,120 |
| 许可证 | The Unlicense |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,123 |
| 语言 | JavaScript |
| Forks | 26,765 |
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
| Stars | 67,292 |
| 语言 | JavaScript |
| Forks | 11,975 |
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
| Stars | 66,290 |
| 语言 | JavaScript |
| Forks | 9,193 |
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
| Stars | 61,577 |
| 语言 | JavaScript |
| Forks | 7,127 |
| Issues | 135 |
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
| Stars | 46,969 |
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
| Stars | 45,574 |
| 语言 | Go |
| Forks | 3,779 |
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
| Stars | 146,943 |
| 语言 | Python |
| Forks | 11,249 |
| Issues | 304 |
| Topics | awesome, github, hellogithub, python |
