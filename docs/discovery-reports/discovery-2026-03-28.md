# 项目发现报告 (2026-03-28)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 131 |
| 去重移除 | 29 |
| 已在监控 | 26 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 25 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 17 |
| ⚙️ DevOps/基础设施 | 13 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 9 |
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
| Stars | 129,070 |
| 语言 | Python |
| Forks | 18,265 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 支持，可完全自托管部署，既适合个人用户快速搭建 AI 对话界面，也适合企业私有化部署以保护数据隐私。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，支持 OpenAI 兼容接口，灵活性强
- RAG 检索增强生成：内置文档检索和知识库功能，可基于私有文档进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展工具和功能集成
- 完全自托管：可私有化部署，无需依赖云服务，数据完全自主控制
- 现代化 Web UI：响应式设计，支持实时对话、代码高亮、Markdown 渲染等

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 开发者本地 LLM 调试：为使用 Ollama 或其他本地 LLM 的开发者提供友好的调试界面
- 知识库问答系统：利用 RAG 功能构建基于私有文档的智能问答和知识检索系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,450 |
| 语言 | Python |
| Forks | 8,563 |
| Issues | 3,175 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（Stars 76,450+），创新性地将 RAG 与 Agent 能力深度融合，配合 Deep Research、GraphRAG、MCP 等前沿特性，为构建企业级智能问答系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能代理能力结合，支持复杂推理和多步任务执行
- 高级文档理解引擎：支持多种格式文档的智能解析与语义提取，提供精准的上下文检索
- Deep Research 深度研究能力：支持深入分析和综合研究任务，适用于复杂知识探索场景
- GraphRAG 图增强检索：集成知识图谱能力，提升关系型信息的检索和推理效果
- 多 LLM 支持与 MCP 协议：兼容 OpenAI、Ollama、DeepSeek 等主流模型，支持 Model Context Protocol 标准

**适用场景**:
- 企业级知识库问答系统：构建私有知识库的智能问答、文档检索和数据分析服务
- 智能文档处理与分析：实现合同审查、报告生成、技术文档问答等复杂文档理解任务
- 深度研究辅助工具：支持学术研究、市场调研、竞品分析等需要多源信息整合的深度研究场景



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,890 |
| 语言 | TypeScript |
| Forks | 6,672 |
| Issues | 239 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前最专业的 AI 网页数据提取工具，能够将任意网站完整转换为 LLM 可直接使用的 markdown 或结构化数据，拥有接近 10 万星标验证的稳定性，特别适合需要大规模采集 AI 训练数据或构建 RAG 系统的场景。

**技术亮点**:
- 专为 AI/LLM 优化的数据提取管道，将网页自动清洗转换为高质量 markdown 格式，保留关键信息并去除噪音
- 支持整站爬取 (crawl) 和单页提取 (scrape) 两种模式，可灵活处理从单个页面到大规模网站的数据采集需求
- 提供结构化数据输出能力，可将非结构化网页转换为 JSON 等结构化格式，便于下游 AI 任务处理
- TypeScript/Node.js 原生实现，提供完善的 SDK 和 API 接口，支持快速集成到现有 AI 应用中
- 内置反爬虫对抗能力，支持 JavaScript 渲染页面的抓取，兼容现代 SPA 应用

**适用场景**:
- RAG (检索增强生成) 系统：快速从网站、文档库构建 AI 可理解的知识库数据源
- AI 训练数据采集：为 LLM 微调或 RLHF 收集高质量的网页文本数据，支持批量抓取和格式转换
- 竞品分析/市场调研：自动化采集多个网站的结构化信息，用于商业智能分析
- AI Agent 数据获取：为 AI Agent 提供实时网页信息查询能力，支持自动化数据收集工作流



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,384 |
| 语言 | JavaScript |
| Forks | 14,891 |
| Issues | 146 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编程助手生态的性能优化框架，通过模块化的 Skills、Instincts、Memory 等机制，为 Claude Code、Cursor 等主流 AI 编码工具提供企业级的扩展能力，是当前 LLM 编程工具链中最具系统性且 Stars 突破 11 万的开源项目。

**技术亮点**:
- 多 Agent 引擎适配：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的 API 接口规范
- Memory 系统：实现持久化上下文管理，优化长对话场景下的 token 利用率和响应质量
- Skills 插件机制：提供可扩展的技能库架构，支持开发者自定义工作流和工具链集成
- Security 安全层：内置代码执行权限控制和沙箱机制，防止恶意提示词注入和安全漏洞
- Research-First 开发范式：强调基于实验验证的性能调优方法论，包含基准测试和 A/B 测试框架

**适用场景**:
- 企业级 AI 编程助手定制：团队可基于该项目构建内部代码审查自动化流水线或定制化代码生成工作流
- AI Agent 性能优化研究：开发者可利用其基准测试框架评估不同提示词策略和模型配置的实际效果
- 开发工具链集成：通过 MCP (Model Context Protocol) 协议将 AI 能力无缝接入现有 IDE 和 CI/CD 环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,523 |
| 语言 | Go |
| Forks | 3,812 |
| Issues | 151 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI是当前最成熟的本地化AI部署解决方案，支持运行LLM、图像生成、语音合成等多模态模型，无需GPU即可在各类硬件上运行，特别适合需要在本地环境或边缘设备上部署AI能力的企业，既能保障数据隐私又能降低云计算成本。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型，提供统一的API接口
- 无GPU运行能力：通过优化推理实现CPU高效运行，降低AI部署的硬件门槛
- Go语言高性能架构：利用Go的并发优势实现高吞吐量，支持分布式部署和横向扩展
- 丰富的模型兼容性：支持gguf/ggml格式模型，兼容OpenAI API规范便于迁移集成
- 去中心化设计：基于libp2p实现分布式架构，支持在去中心化网络中运行AI任务

**适用场景**:
- 企业本地AI部署：需要数据隐私合规（如医疗、金融）的场景，在本地服务器运行AI推理避免数据外传
- 边缘设备与IoT：在资源受限的硬件上部署轻量级AI能力，如智能终端、嵌入式系统
- 开发者本地开发测试：快速在本地环境验证AI应用原型，支持完整的OpenAI兼容API便于开发调试



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,435 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 683 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多 Agent 协作、MCP 协议和多模型集成（GPT/Claude/DeepSeek/Gemini），Stars 高达 74k+ 证明其成熟度和社区认可度，非常适合构建企业级智能助手和多 Agent 协作系统。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的 API 接口抽象
- 多 Agent 协作框架：支持多 Agent 协同工作，Agent 可作为工作交互的基本单元，支持复杂的协作流程设计
- MCP 协议支持：内置 Model Context Protocol 支持，可扩展工具和资源集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，Agent 可基于私有知识进行问答
- 现代化 TypeScript 技术栈：基于 React + TypeScript 开发，提供完整的 UI 组件库和 API 接口，便于二次开发

**适用场景**:
- 企业智能助手开发：构建支持多模型切换的企业级 AI 助手，支持知识库问答和业务流程自动化
- 多 Agent 协作系统：设计和管理多个专业化 Agent 团队，实现复杂任务的分解与协同处理
- AI 应用快速原型开发：利用现成的组件库和 API 接口，快速搭建 AI Chatbot、知识库问答等应用



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,183 |
| 语言 | Python |
| Forks | 8,431 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 录用的微调框架，统一支持 100+ 大语言模型和视觉语言模型的高效微调，提供开箱即用的 LoRA/QLoRA/RLHF 等多种微调方案，大幅降低了 LLM 微调的工程门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs（包括 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等）和 VLMs，一套代码库覆盖主流开源模型
- 多种微调范式：集成 LoRA、QLoRA、Full-parameter、RLHF（DPO/KTO/ORPO）等先进微调技术，支持参数高效微调
- 优化加速技术：采用 Flash Attention、DeepSpeed ZeRO、混合精度训练等手段，显著降低显存占用和训练时间
- 实验管理功能：内置 TensorBoard、OpenAI 格式日志输出，支持多实验对比和超参数搜索
- 易用性设计：提供 Web UI 和 CLI 两种交互方式，支持 YAML 配置文件快速启动训练

**适用场景**:
- 企业私有化部署：基于 LlamaFactory 对开源大模型（如 Qwen、DeepSeek）进行领域适配微调，构建专属 AI 助手或行业垂直应用
- 学术研究与模型实验：研究人员快速验证不同微调算法（LoRA vs QLoRA vs DPO）在各类模型上的效果差异，降低科研实验成本
- 个人开发者学习与原型开发：利用 QLoRA 在消费级 GPU（24GB VRAM）上微调 7B 模型，无需专业集群即可上手实践



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,608 |
| 语言 | Python |
| Forks | 9,864 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,902 |
| 语言 | TypeScript |
| Forks | 3,122 |
| Issues | 215 |
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
| Stars | 35,029 |
| 语言 | TypeScript |
| Forks | 7,116 |
| Issues | 467 |
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
| Stars | 45,604 |
| 语言 | Java |
| Forks | 15,856 |
| Issues | 81 |
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
| Stars | 38,856 |
| 语言 | Python |
| Forks | 6,167 |
| Issues | 110 |
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
| Stars | 33,663 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,461 |
| 语言 | TypeScript |
| Forks | 3,628 |
| Issues | 283 |
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
| Stars | 32,787 |
| 语言 | Jupyter Notebook |
| Forks | 5,433 |
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
| Stars | 103,854 |
| 语言 | Python |
| Forks | 15,156 |
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
| Stars | 56,963 |
| 语言 | JavaScript |
| Forks | 6,162 |
| Issues | 303 |
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
| Stars | 70,036 |
| 语言 | Python |
| Forks | 8,772 |
| Issues | 350 |
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
| Stars | 44,370 |
| 语言 | TypeScript |
| Forks | 3,301 |
| Issues | 342 |
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
| Stars | 84,844 |
| 语言 | Python |
| Forks | 9,824 |
| Issues | 201 |
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
| Stars | 51,179 |
| 语言 | TypeScript |
| Forks | 23,994 |
| Issues | 823 |
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
| Stars | 181,483 |
| 语言 | TypeScript |
| Forks | 56,255 |
| Issues | 1,428 |
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
| Stars | 146,339 |
| 语言 | Python |
| Forks | 8,666 |
| Issues | 933 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,369 |
| 语言 | MDX |
| Forks | 7,744 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,709 |
| 语言 | TypeScript |
| Forks | 6,458 |
| Issues | 84 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,829 |
| 语言 | Rust |
| Forks | 2,077 |
| Issues | 472 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


### microsoft/ai-agents-for-beginners

**描述**: 12 Lessons to Get Started Building AI Agents

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,219 |
| 语言 | Jupyter Notebook |
| Forks | 19,074 |
| Issues | 13 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
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
| Stars | 129,070 |
| 语言 | Python |
| Forks | 18,265 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 支持，可完全自托管部署，既适合个人用户快速搭建 AI 对话界面，也适合企业私有化部署以保护数据隐私。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，支持 OpenAI 兼容接口，灵活性强
- RAG 检索增强生成：内置文档检索和知识库功能，可基于私有文档进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展工具和功能集成
- 完全自托管：可私有化部署，无需依赖云服务，数据完全自主控制
- 现代化 Web UI：响应式设计，支持实时对话、代码高亮、Markdown 渲染等

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 开发者本地 LLM 调试：为使用 Ollama 或其他本地 LLM 的开发者提供友好的调试界面
- 知识库问答系统：利用 RAG 功能构建基于私有文档的智能问答和知识检索系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,450 |
| 语言 | Python |
| Forks | 8,563 |
| Issues | 3,175 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（Stars 76,450+），创新性地将 RAG 与 Agent 能力深度融合，配合 Deep Research、GraphRAG、MCP 等前沿特性，为构建企业级智能问答系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能代理能力结合，支持复杂推理和多步任务执行
- 高级文档理解引擎：支持多种格式文档的智能解析与语义提取，提供精准的上下文检索
- Deep Research 深度研究能力：支持深入分析和综合研究任务，适用于复杂知识探索场景
- GraphRAG 图增强检索：集成知识图谱能力，提升关系型信息的检索和推理效果
- 多 LLM 支持与 MCP 协议：兼容 OpenAI、Ollama、DeepSeek 等主流模型，支持 Model Context Protocol 标准

**适用场景**:
- 企业级知识库问答系统：构建私有知识库的智能问答、文档检索和数据分析服务
- 智能文档处理与分析：实现合同审查、报告生成、技术文档问答等复杂文档理解任务
- 深度研究辅助工具：支持学术研究、市场调研、竞品分析等需要多源信息整合的深度研究场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,435 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 683 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多 Agent 协作、MCP 协议和多模型集成（GPT/Claude/DeepSeek/Gemini），Stars 高达 74k+ 证明其成熟度和社区认可度，非常适合构建企业级智能助手和多 Agent 协作系统。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的 API 接口抽象
- 多 Agent 协作框架：支持多 Agent 协同工作，Agent 可作为工作交互的基本单元，支持复杂的协作流程设计
- MCP 协议支持：内置 Model Context Protocol 支持，可扩展工具和资源集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，Agent 可基于私有知识进行问答
- 现代化 TypeScript 技术栈：基于 React + TypeScript 开发，提供完整的 UI 组件库和 API 接口，便于二次开发

**适用场景**:
- 企业智能助手开发：构建支持多模型切换的企业级 AI 助手，支持知识库问答和业务流程自动化
- 多 Agent 协作系统：设计和管理多个专业化 Agent 团队，实现复杂任务的分解与协同处理
- AI 应用快速原型开发：利用现成的组件库和 API 接口，快速搭建 AI Chatbot、知识库问答等应用



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,902 |
| 语言 | TypeScript |
| Forks | 3,122 |
| Issues | 215 |
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
| Stars | 45,604 |
| 语言 | Java |
| Forks | 15,856 |
| Issues | 81 |
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
| Stars | 38,856 |
| 语言 | Python |
| Forks | 6,167 |
| Issues | 110 |
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
| Stars | 33,663 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,461 |
| 语言 | TypeScript |
| Forks | 3,628 |
| Issues | 283 |
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
| Stars | 32,787 |
| 语言 | Jupyter Notebook |
| Forks | 5,433 |
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
| Stars | 103,854 |
| 语言 | Python |
| Forks | 15,156 |
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
| Stars | 99,760 |
| 语言 | TypeScript |
| Forks | 11,917 |
| Issues | 988 |
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
| Stars | 56,963 |
| 语言 | JavaScript |
| Forks | 6,162 |
| Issues | 303 |
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
| Stars | 51,179 |
| 语言 | TypeScript |
| Forks | 23,994 |
| Issues | 823 |
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
| Stars | 73,239 |
| 语言 | Python |
| Forks | 10,044 |
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
| Stars | 43,480 |
| 语言 | Go |
| Forks | 3,917 |
| Issues | 1,094 |
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
| Stars | 31,826 |
| 语言 | Python |
| Forks | 3,353 |
| Issues | 85 |
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
| Stars | 72,369 |
| 语言 | MDX |
| Forks | 7,744 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
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
| Stars | 129,070 |
| 语言 | Python |
| Forks | 18,265 |
| Issues | 269 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完善的开源 AI 界面，支持 Ollama、OpenAI API 等多种后端，提供 RAG 和 MCP 支持，可完全自托管部署，既适合个人用户快速搭建 AI 对话界面，也适合企业私有化部署以保护数据隐私。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，支持 OpenAI 兼容接口，灵活性强
- RAG 检索增强生成：内置文档检索和知识库功能，可基于私有文档进行问答
- MCP 协议支持：支持 Model Context Protocol，便于扩展工具和功能集成
- 完全自托管：可私有化部署，无需依赖云服务，数据完全自主控制
- 现代化 Web UI：响应式设计，支持实时对话、代码高亮、Markdown 渲染等

**适用场景**:
- 企业私有化 AI 助手：适合需要在内部部署 AI 对话系统、保护数据隐私的企业
- 开发者本地 LLM 调试：为使用 Ollama 或其他本地 LLM 的开发者提供友好的调试界面
- 知识库问答系统：利用 RAG 功能构建基于私有文档的智能问答和知识检索系统



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,450 |
| 语言 | Python |
| Forks | 8,563 |
| Issues | 3,175 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最热门的开源 RAG 引擎之一（Stars 76,450+），创新性地将 RAG 与 Agent 能力深度融合，配合 Deep Research、GraphRAG、MCP 等前沿特性，为构建企业级智能问答系统提供了开箱即用的完整解决方案。

**技术亮点**:
- RAG + Agent 融合架构：将检索增强生成与智能代理能力结合，支持复杂推理和多步任务执行
- 高级文档理解引擎：支持多种格式文档的智能解析与语义提取，提供精准的上下文检索
- Deep Research 深度研究能力：支持深入分析和综合研究任务，适用于复杂知识探索场景
- GraphRAG 图增强检索：集成知识图谱能力，提升关系型信息的检索和推理效果
- 多 LLM 支持与 MCP 协议：兼容 OpenAI、Ollama、DeepSeek 等主流模型，支持 Model Context Protocol 标准

**适用场景**:
- 企业级知识库问答系统：构建私有知识库的智能问答、文档检索和数据分析服务
- 智能文档处理与分析：实现合同审查、报告生成、技术文档问答等复杂文档理解任务
- 深度研究辅助工具：支持学术研究、市场调研、竞品分析等需要多源信息整合的深度研究场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,384 |
| 语言 | JavaScript |
| Forks | 14,891 |
| Issues | 146 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编程助手生态的性能优化框架，通过模块化的 Skills、Instincts、Memory 等机制，为 Claude Code、Cursor 等主流 AI 编码工具提供企业级的扩展能力，是当前 LLM 编程工具链中最具系统性且 Stars 突破 11 万的开源项目。

**技术亮点**:
- 多 Agent 引擎适配：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的 API 接口规范
- Memory 系统：实现持久化上下文管理，优化长对话场景下的 token 利用率和响应质量
- Skills 插件机制：提供可扩展的技能库架构，支持开发者自定义工作流和工具链集成
- Security 安全层：内置代码执行权限控制和沙箱机制，防止恶意提示词注入和安全漏洞
- Research-First 开发范式：强调基于实验验证的性能调优方法论，包含基准测试和 A/B 测试框架

**适用场景**:
- 企业级 AI 编程助手定制：团队可基于该项目构建内部代码审查自动化流水线或定制化代码生成工作流
- AI Agent 性能优化研究：开发者可利用其基准测试框架评估不同提示词策略和模型配置的实际效果
- 开发工具链集成：通过 MCP (Model Context Protocol) 协议将 AI 能力无缝接入现有 IDE 和 CI/CD 环境



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,435 |
| 语言 | TypeScript |
| Forks | 14,841 |
| Issues | 683 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 开发平台，支持多 Agent 协作、MCP 协议和多模型集成（GPT/Claude/DeepSeek/Gemini），Stars 高达 74k+ 证明其成熟度和社区认可度，非常适合构建企业级智能助手和多 Agent 协作系统。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的 API 接口抽象
- 多 Agent 协作框架：支持多 Agent 协同工作，Agent 可作为工作交互的基本单元，支持复杂的协作流程设计
- MCP 协议支持：内置 Model Context Protocol 支持，可扩展工具和资源集成
- 知识库集成：内置知识库功能，支持 RAG 增强检索，Agent 可基于私有知识进行问答
- 现代化 TypeScript 技术栈：基于 React + TypeScript 开发，提供完整的 UI 组件库和 API 接口，便于二次开发

**适用场景**:
- 企业智能助手开发：构建支持多模型切换的企业级 AI 助手，支持知识库问答和业务流程自动化
- 多 Agent 协作系统：设计和管理多个专业化 Agent 团队，实现复杂任务的分解与协同处理
- AI 应用快速原型开发：利用现成的组件库和 API 接口，快速搭建 AI Chatbot、知识库问答等应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,470 |
| 语言 | HTML |
| Forks | 20,291 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是全球最大的开源 AI 提示词聚合平台之一，拥有超过 15 万星标，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署满足企业隐私需求，是 AI 应用开发者和内容创作者的重要资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和类型安全保证
- 超过 150 万条精选提示词，涵盖写作、编程、教育等多领域应用场景
- 支持多种主流 AI 平台（ChatGPT、Claude、Gemini、GPT-4 等）的提示词格式
- 采用 Creative Commons Zero v1.0 Universal 许可证，完全开源可商用
- 支持企业私有化部署，提供完整的隐私保护和定制化能力

**适用场景**:
- 企业自托管：组织可部署私有化提示词管理系统，保护内部数据隐私，适合金融、医疗等敏感行业
- 个人效率提升：内容创作者、教育工作者可通过优质提示词库快速获取适用于 ChatGPT/Claude 的高效工作模板
- 开发者集成：AI 应用开发者可将提示词库作为功能模块集成到自有产品中，加速开发周期



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,411 |
| 语言 | Jupyter Notebook |
| Forks | 13,648 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka（AI 研究权威）亲自主导的从零构建 LLM 教育项目，通过 Jupyter Notebook 逐步讲解 ChatGPT 核心架构（Attention、Feed-Forward、Embedding 等），是理解大模型内部原理的最佳实践资源，适合想深入掌握 LLM 而非仅调 API 的开发者。

**技术亮点**:
- 纯 PyTorch 从零实现 Transformer 架构，包括 Multi-Head Self-Attention、Positional Encoding、GELU 激活等核心组件
- 完整的 ChatGPT 风格训练流程：SFT 有监督微调、RLHF（奖励模型 + PPO）、DPO 等前沿技术
- 逐行代码 + 详细注释的 Jupyter Notebook 形式，每个概念配有可视化解释和数学推导
- 涵盖 tokenizer 实现、BPE 编码、数据加载、分布式训练等工程细节
- 包含 GPT-2 模型权重的加载和微调实践，理论与代码深度结合

**适用场景**:
- AI/ML 学习者：系统理解 Transformer、Attention 机制、LLM 训练流程的原理
- 教育机构：作为大模型课程的教学素材或实验项目
- 企业研发：参考项目架构快速验证新想法或定制化 LLM 应用



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,608 |
| 语言 | Python |
| Forks | 9,864 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,902 |
| 语言 | TypeScript |
| Forks | 3,122 |
| Issues | 215 |
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
| Stars | 35,029 |
| 语言 | TypeScript |
| Forks | 7,116 |
| Issues | 467 |
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
| Stars | 33,663 |
| 语言 | Python |
| Forks | 2,086 |
| Issues | 88 |
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
| Stars | 56,963 |
| 语言 | JavaScript |
| Forks | 6,162 |
| Issues | 303 |
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
| Stars | 70,036 |
| 语言 | Python |
| Forks | 8,772 |
| Issues | 350 |
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
| Stars | 44,370 |
| 语言 | TypeScript |
| Forks | 3,301 |
| Issues | 342 |
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
| Stars | 51,179 |
| 语言 | TypeScript |
| Forks | 23,994 |
| Issues | 823 |
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
| Stars | 35,151 |
| 语言 | HTML |
| Forks | 5,658 |
| Issues | 18 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,569 |
| 语言 | Python |
| Forks | 14,892 |
| Issues | 3,957 |
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
| Stars | 53,419 |
| 语言 | Python |
| Forks | 5,164 |
| Issues | 67 |
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
| Stars | 39,168 |
| 语言 | TypeScript |
| Forks | 3,962 |
| Issues | 1,085 |
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
| Stars | 146,339 |
| 语言 | Python |
| Forks | 8,666 |
| Issues | 933 |
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
| Stars | 166,350 |
| 语言 | Go |
| Forks | 15,205 |
| Issues | 2,744 |
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
| Stars | 72,369 |
| 语言 | MDX |
| Forks | 7,744 |
| Issues | 252 |
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
| Stars | 47,288 |
| 语言 | Rust |
| Forks | 9,356 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,709 |
| 语言 | TypeScript |
| Forks | 6,458 |
| Issues | 84 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,956 |
| 语言 | Python |
| Forks | 2,582 |
| Issues | 64 |
| Topics | api, chatgpt, claude, deepseek, gemini, gpt, grok |
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
| Stars | 92,743 |
| 语言 | Python |
| Forks | 5,578 |
| Issues | 491 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


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
| Stars | 69,183 |
| 语言 | Python |
| Forks | 8,431 |
| Issues | 934 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是首个被 ACL 2024 录用的微调框架，统一支持 100+ 大语言模型和视觉语言模型的高效微调，提供开箱即用的 LoRA/QLoRA/RLHF 等多种微调方案，大幅降低了 LLM 微调的工程门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs（包括 LLaMA、Qwen、DeepSeek、Gemma、Mistral 等）和 VLMs，一套代码库覆盖主流开源模型
- 多种微调范式：集成 LoRA、QLoRA、Full-parameter、RLHF（DPO/KTO/ORPO）等先进微调技术，支持参数高效微调
- 优化加速技术：采用 Flash Attention、DeepSpeed ZeRO、混合精度训练等手段，显著降低显存占用和训练时间
- 实验管理功能：内置 TensorBoard、OpenAI 格式日志输出，支持多实验对比和超参数搜索
- 易用性设计：提供 Web UI 和 CLI 两种交互方式，支持 YAML 配置文件快速启动训练

**适用场景**:
- 企业私有化部署：基于 LlamaFactory 对开源大模型（如 Qwen、DeepSeek）进行领域适配微调，构建专属 AI 助手或行业垂直应用
- 学术研究与模型实验：研究人员快速验证不同微调算法（LoRA vs QLoRA vs DPO）在各类模型上的效果差异，降低科研实验成本
- 个人开发者学习与原型开发：利用 QLoRA 在消费级 GPU（24GB VRAM）上微调 7B 模型，无需专业集群即可上手实践



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,702 |
| 语言 | Python |
| Forks | 6,278 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据分析平台，汇聚63,000+ Stars，提供从股票、期权到加密货币的全品类金融数据访问，并深度集成AI/机器学习能力，非常适合需要快速构建量化策略或金融AI应用的开发者。

**技术亮点**:
- 统一数据API架构：聚合多个权威金融数据源，提供标准化的数据访问接口，简化数据获取流程
- 全面的金融工具覆盖：支持股票、期权、加密货币、固定收益、衍生品等多元化资产类别
- AI/ML深度集成：内置机器学习模型和AI代理支持，可用于金融预测、情绪分析和自动化交易
- 量化分析工具链：提供技术指标计算、因子分析、回测框架等专业量化研究功能
- 模块化可扩展设计：支持自定义数据源、指标和插件，便于企业级定制和二次开发

**适用场景**:
- 量化投资研究：量化分析师可用于策略回测、因子挖掘和技术分析，快速验证交易想法
- 金融数据中台建设：企业可基于OpenBB构建统一的金融数据服务平台，为内部团队或客户提供数据API
- AI金融应用开发：开发者可将其作为数据后端，构建智能投顾、交易机器人和金融问答系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,470 |
| 语言 | HTML |
| Forks | 20,291 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是全球最大的开源 AI 提示词聚合平台之一，拥有超过 15 万星标，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署满足企业隐私需求，是 AI 应用开发者和内容创作者的重要资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和类型安全保证
- 超过 150 万条精选提示词，涵盖写作、编程、教育等多领域应用场景
- 支持多种主流 AI 平台（ChatGPT、Claude、Gemini、GPT-4 等）的提示词格式
- 采用 Creative Commons Zero v1.0 Universal 许可证，完全开源可商用
- 支持企业私有化部署，提供完整的隐私保护和定制化能力

**适用场景**:
- 企业自托管：组织可部署私有化提示词管理系统，保护内部数据隐私，适合金融、医疗等敏感行业
- 个人效率提升：内容创作者、教育工作者可通过优质提示词库快速获取适用于 ChatGPT/Claude 的高效工作模板
- 开发者集成：AI 应用开发者可将提示词库作为功能模块集成到自有产品中，加速开发周期



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,411 |
| 语言 | Jupyter Notebook |
| Forks | 13,648 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |

---

Sebastian Raschka（AI 研究权威）亲自主导的从零构建 LLM 教育项目，通过 Jupyter Notebook 逐步讲解 ChatGPT 核心架构（Attention、Feed-Forward、Embedding 等），是理解大模型内部原理的最佳实践资源，适合想深入掌握 LLM 而非仅调 API 的开发者。

**技术亮点**:
- 纯 PyTorch 从零实现 Transformer 架构，包括 Multi-Head Self-Attention、Positional Encoding、GELU 激活等核心组件
- 完整的 ChatGPT 风格训练流程：SFT 有监督微调、RLHF（奖励模型 + PPO）、DPO 等前沿技术
- 逐行代码 + 详细注释的 Jupyter Notebook 形式，每个概念配有可视化解释和数学推导
- 涵盖 tokenizer 实现、BPE 编码、数据加载、分布式训练等工程细节
- 包含 GPT-2 模型权重的加载和微调实践，理论与代码深度结合

**适用场景**:
- AI/ML 学习者：系统理解 Transformer、Attention 机制、LLM 训练流程的原理
- 教育机构：作为大模型课程的教学素材或实验项目
- 企业研发：参考项目架构快速验证新想法或定制化 LLM 应用



### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,461 |
| 语言 | TypeScript |
| Forks | 3,628 |
| Issues | 283 |
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
| Stars | 32,787 |
| 语言 | Jupyter Notebook |
| Forks | 5,433 |
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
| Stars | 158,502 |
| 语言 | Python |
| Forks | 32,653 |
| Issues | 2,313 |
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
| Stars | 74,569 |
| 语言 | Python |
| Forks | 14,892 |
| Issues | 3,957 |
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
| Stars | 107,187 |
| 语言 | Python |
| Forks | 12,360 |
| Issues | 3,908 |
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
| Stars | 98,613 |
| 语言 | Python |
| Forks | 27,331 |
| Issues | 18,107 |
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
| Stars | 72,369 |
| 语言 | MDX |
| Forks | 7,744 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 162,008 |
| 语言 | Python |
| Forks | 30,206 |
| Issues | 2,472 |
| Topics | ai, ai-art, deep-learning, diffusion, gradio, image-generation, image2image, img2img, pytorch, stable-diffusion, text2image, torch, txt2img, unstable, upscaling, web |
| 许可证 | GNU Affero General Public License v3.0 |


## 🛠️ 开发工具 (17 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,384 |
| 语言 | JavaScript |
| Forks | 14,891 |
| Issues | 146 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

everything-claude-code 是一个面向 AI 编程助手生态的性能优化框架，通过模块化的 Skills、Instincts、Memory 等机制，为 Claude Code、Cursor 等主流 AI 编码工具提供企业级的扩展能力，是当前 LLM 编程工具链中最具系统性且 Stars 突破 11 万的开源项目。

**技术亮点**:
- 多 Agent 引擎适配：统一支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编码工具的 API 接口规范
- Memory 系统：实现持久化上下文管理，优化长对话场景下的 token 利用率和响应质量
- Skills 插件机制：提供可扩展的技能库架构，支持开发者自定义工作流和工具链集成
- Security 安全层：内置代码执行权限控制和沙箱机制，防止恶意提示词注入和安全漏洞
- Research-First 开发范式：强调基于实验验证的性能调优方法论，包含基准测试和 A/B 测试框架

**适用场景**:
- 企业级 AI 编程助手定制：团队可基于该项目构建内部代码审查自动化流水线或定制化代码生成工作流
- AI Agent 性能优化研究：开发者可利用其基准测试框架评估不同提示词策略和模型配置的实际效果
- 开发工具链集成：通过 MCP (Model Context Protocol) 协议将 AI 能力无缝接入现有 IDE 和 CI/CD 环境



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,523 |
| 语言 | Go |
| Forks | 3,812 |
| Issues | 151 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI是当前最成熟的本地化AI部署解决方案，支持运行LLM、图像生成、语音合成等多模态模型，无需GPU即可在各类硬件上运行，特别适合需要在本地环境或边缘设备上部署AI能力的企业，既能保障数据隐私又能降低云计算成本。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型，提供统一的API接口
- 无GPU运行能力：通过优化推理实现CPU高效运行，降低AI部署的硬件门槛
- Go语言高性能架构：利用Go的并发优势实现高吞吐量，支持分布式部署和横向扩展
- 丰富的模型兼容性：支持gguf/ggml格式模型，兼容OpenAI API规范便于迁移集成
- 去中心化设计：基于libp2p实现分布式架构，支持在去中心化网络中运行AI任务

**适用场景**:
- 企业本地AI部署：需要数据隐私合规（如医疗、金融）的场景，在本地服务器运行AI推理避免数据外传
- 边缘设备与IoT：在资源受限的硬件上部署轻量级AI能力，如智能终端、嵌入式系统
- 开发者本地开发测试：快速在本地环境验证AI应用原型，支持完整的OpenAI兼容API便于开发调试



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,036 |
| 语言 | Python |
| Forks | 8,772 |
| Issues | 350 |
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
| Stars | 44,370 |
| 语言 | TypeScript |
| Forks | 3,301 |
| Issues | 342 |
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
| Stars | 181,483 |
| 语言 | TypeScript |
| Forks | 56,255 |
| Issues | 1,428 |
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
| Stars | 153,710 |
| 语言 | Python |
| Forks | 12,470 |
| Issues | 2,417 |
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
| Stars | 96,648 |
| 语言 | Python |
| Forks | 8,955 |
| Issues | 167 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


### microsoft/vscode

**描述**: Visual Studio Code

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 183,151 |
| 语言 | TypeScript |
| Forks | 38,796 |
| Issues | 15,627 |
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
| Stars | 93,963 |
| 语言 | TypeScript |
| Forks | 9,406 |
| Issues | 299 |
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
| Stars | 78,674 |
| 语言 | TypeScript |
| Forks | 5,739 |
| Issues | 733 |
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
| Stars | 76,877 |
| 语言 | TypeScript |
| Forks | 6,568 |
| Issues | 169 |
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
| Stars | 75,687 |
| 语言 | JavaScript |
| Forks | 7,272 |
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
| Stars | 79,065 |
| 语言 | Go |
| Forks | 2,742 |
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
| Stars | 75,149 |
| 语言 | Go |
| Forks | 2,648 |
| Issues | 948 |
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
| Stars | 36,956 |
| 语言 | Python |
| Forks | 2,582 |
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
| Stars | 54,743 |
| 语言 | JavaScript |
| Forks | 4,065 |
| Issues | 1,416 |
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
| Stars | 417,023 |
| 语言 | Python |
| Forks | 45,252 |
| Issues | 1,111 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
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
| Stars | 44,370 |
| 语言 | TypeScript |
| Forks | 3,301 |
| Issues | 342 |
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
| Stars | 181,483 |
| 语言 | TypeScript |
| Forks | 56,255 |
| Issues | 1,428 |
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
| Stars | 51,698 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 217 |
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
| Stars | 121,378 |
| 语言 | Go |
| Forks | 42,748 |
| Issues | 2,655 |
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
| Stars | 71,572 |
| 语言 | Go |
| Forks | 18,911 |
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
| Stars | 54,555 |
| 语言 | Go |
| Forks | 6,502 |
| Issues | 2,873 |
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
| Stars | 93,963 |
| 语言 | TypeScript |
| Forks | 9,406 |
| Issues | 299 |
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
| Stars | 75,869 |
| 语言 | TypeScript |
| Forks | 6,462 |
| Issues | 443 |
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
| Stars | 84,599 |
| 语言 | JavaScript |
| Forks | 7,566 |
| Issues | 711 |
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
| Stars | 69,589 |
| 语言 | Go |
| Forks | 1,894 |
| Issues | 308 |
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
| Stars | 62,386 |
| 语言 | Go |
| Forks | 5,893 |
| Issues | 777 |
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
| Stars | 58,294 |
| 语言 | Go |
| Forks | 4,219 |
| Issues | 33 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### gogs/gogs

**描述**: Gogs is a painless self-hosted Git service

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,603 |
| 语言 | Go |
| Forks | 5,069 |
| Issues | 970 |
| Topics | docker, git, go, gogs, mysql, postgresql, raspberry-pi, self-hosted, source-code-management, sqlite3, version-control |
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
| Stars | 84,599 |
| 语言 | JavaScript |
| Forks | 7,566 |
| Issues | 711 |
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
| Stars | 63,294 |
| 语言 | Go |
| Forks | 10,274 |
| Issues | 761 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (14 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,523 |
| 语言 | Go |
| Forks | 3,812 |
| Issues | 151 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI是当前最成熟的本地化AI部署解决方案，支持运行LLM、图像生成、语音合成等多模态模型，无需GPU即可在各类硬件上运行，特别适合需要在本地环境或边缘设备上部署AI能力的企业，既能保障数据隐私又能降低云计算成本。

**技术亮点**:
- 多模态统一推理引擎：支持文本生成（Llama/Mamba）、图像生成（Stable Diffusion）、语音合成（TTS/MusicGen）、目标检测等多种模型，提供统一的API接口
- 无GPU运行能力：通过优化推理实现CPU高效运行，降低AI部署的硬件门槛
- Go语言高性能架构：利用Go的并发优势实现高吞吐量，支持分布式部署和横向扩展
- 丰富的模型兼容性：支持gguf/ggml格式模型，兼容OpenAI API规范便于迁移集成
- 去中心化设计：基于libp2p实现分布式架构，支持在去中心化网络中运行AI任务

**适用场景**:
- 企业本地AI部署：需要数据隐私合规（如医疗、金融）的场景，在本地服务器运行AI推理避免数据外传
- 边缘设备与IoT：在资源受限的硬件上部署轻量级AI能力，如智能终端、嵌入式系统
- 开发者本地开发测试：快速在本地环境验证AI应用原型，支持完整的OpenAI兼容API便于开发调试



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,648 |
| 语言 | Python |
| Forks | 8,955 |
| Issues | 167 |
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
| Forks | 33,802 |
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
| Stars | 100,123 |
| 语言 | TypeScript |
| Forks | 27,146 |
| Issues | 1,116 |
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
| Stars | 78,674 |
| 语言 | TypeScript |
| Forks | 5,739 |
| Issues | 733 |
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
| Stars | 75,687 |
| 语言 | JavaScript |
| Forks | 7,272 |
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
| Stars | 55,955 |
| 语言 | JavaScript |
| Forks | 10,214 |
| Issues | 366 |
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
| Stars | 51,740 |
| 语言 | JavaScript |
| Forks | 4,690 |
| Issues | 1,465 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,322 |
| 语言 | Go |
| Forks | 8,574 |
| Issues | 654 |
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
| Stars | 71,147 |
| 语言 | Go |
| Forks | 4,692 |
| Issues | 245 |
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
| Stars | 57,183 |
| 语言 | Go |
| Forks | 3,223 |
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
| Stars | 36,956 |
| 语言 | Python |
| Forks | 2,582 |
| Issues | 64 |
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
| Stars | 417,023 |
| 语言 | Python |
| Forks | 45,252 |
| Issues | 1,111 |
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
| Stars | 68,872 |
| 语言 | JavaScript |
| Forks | 22,939 |
| Issues | 196 |
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
| Stars | 99,760 |
| 语言 | TypeScript |
| Forks | 11,917 |
| Issues | 988 |
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
| Stars | 56,963 |
| 语言 | JavaScript |
| Forks | 6,162 |
| Issues | 303 |
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
| Stars | 43,480 |
| 语言 | Go |
| Forks | 3,917 |
| Issues | 1,094 |
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
| Stars | 51,698 |
| 语言 | Go |
| Forks | 10,341 |
| Issues | 217 |
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
| Stars | 154,470 |
| 语言 | HTML |
| Forks | 20,291 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这是全球最大的开源 AI 提示词聚合平台之一，拥有超过 15 万星标，支持 ChatGPT、Claude、Gemini 等多平台，可自托管部署满足企业隐私需求，是 AI 应用开发者和内容创作者的重要资源库。

**技术亮点**:
- 基于 Next.js + TypeScript 构建，提供现代化的开发体验和类型安全保证
- 超过 150 万条精选提示词，涵盖写作、编程、教育等多领域应用场景
- 支持多种主流 AI 平台（ChatGPT、Claude、Gemini、GPT-4 等）的提示词格式
- 采用 Creative Commons Zero v1.0 Universal 许可证，完全开源可商用
- 支持企业私有化部署，提供完整的隐私保护和定制化能力

**适用场景**:
- 企业自托管：组织可部署私有化提示词管理系统，保护内部数据隐私，适合金融、医疗等敏感行业
- 个人效率提升：内容创作者、教育工作者可通过优质提示词库快速获取适用于 ChatGPT/Claude 的高效工作模板
- 开发者集成：AI 应用开发者可将提示词库作为功能模块集成到自有产品中，加速开发周期



### asgeirtj/system_prompts_leaks

**描述**: Collection of extracted System Prompts from popular chatbots like ChatGPT, Claude & Gemini

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,151 |
| 语言 | HTML |
| Forks | 5,658 |
| Issues | 18 |
| Topics | ai, anthropic, chatbots, chatgpt, claude, gemini, generative-ai, google-deepmind, large-language-models, llm, openai, prompt-engineering, prompt-injection, prompts |


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,369 |
| 语言 | MDX |
| Forks | 7,744 |
| Issues | 252 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 41,709 |
| 语言 | TypeScript |
| Forks | 6,458 |
| Issues | 84 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,554 |
| 语言 | TypeScript |
| Forks | 9,961 |
| Issues | 2,209 |
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
| Stars | 86,948 |
| 语言 | TypeScript |
| Forks | 8,783 |
| Issues | 1,629 |
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
| Stars | 127,254 |
| 语言 | JavaScript |
| Forks | 12,469 |
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
| Stars | 101,037 |
| 语言 | JavaScript |
| Forks | 7,536 |
| Issues | 232 |
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
| Stars | 168,479 |
| 语言 | Go |
| Forks | 13,100 |
| Issues | 171 |
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
| Stars | 133,538 |
| 语言 | Unknown |
| Forks | 33,679 |
| Issues | 142 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,827 |
| 语言 | Shell |
| Forks | 9,781 |
| Issues | 86 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,790 |
| 语言 | Python |
| Forks | 6,402 |
| Issues | 48 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 84,137 |
| 语言 | Python |
| Forks | 12,286 |
| Issues | 104 |
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
| Stars | 83,147 |
| 语言 | Python |
| Forks | 7,117 |
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
| Stars | 384,662 |
| 语言 | Python |
| Forks | 66,061 |
| Issues | 85 |
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
| Stars | 113,959 |
| 语言 | TypeScript |
| Forks | 5,820 |
| Issues | 307 |
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
| Stars | 105,994 |
| 语言 | TypeScript |
| Forks | 7,695 |
| Issues | 208 |
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
| Forks | 10,258 |
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
| Stars | 99,718 |
| 语言 | C++ |
| Forks | 15,956 |
| Issues | 1,297 |
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
| Stars | 63,061 |
| 语言 | Python |
| Forks | 1,628 |
| Issues | 31 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 15 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,725 |
| 语言 | TypeScript |
| Forks | 6,950 |
| Issues | 249 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,910 |
| 语言 | JavaScript |
| Forks | 3,539 |
| Issues | 57 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 289,435 |
| 语言 | Python |
| Forks | 27,508 |
| Issues | 22 |
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
| Stars | 219,088 |
| 语言 | Python |
| Forks | 50,257 |
| Issues | 902 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,787 |
| 语言 | Python |
| Forks | 11,938 |
| Issues | 117 |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,893 |
| 语言 | Python |
| Forks | 37,094 |
| Issues | 3,462 |
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
| Stars | 85,597 |
| 语言 | Python |
| Forks | 7,187 |
| Issues | 477 |
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
| Forks | 45,193 |
| Issues | 1,281 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 438,950 |
| 语言 | TypeScript |
| Forks | 43,806 |
| Issues | 229 |
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
| Stars | 351,789 |
| 语言 | TypeScript |
| Forks | 43,870 |
| Issues | 38 |
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
| Stars | 119,700 |
| 语言 | TypeScript |
| Forks | 13,033 |
| Issues | 2,909 |
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
| Stars | 110,940 |
| 语言 | TypeScript |
| Forks | 8,348 |
| Issues | 1,795 |
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
| Stars | 108,347 |
| 语言 | TypeScript |
| Forks | 13,309 |
| Issues | 5,005 |
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
| Stars | 97,775 |
| 语言 | TypeScript |
| Forks | 54,581 |
| Issues | 1,355 |
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
| Stars | 95,852 |
| 语言 | TypeScript |
| Forks | 5,206 |
| Issues | 665 |
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
| Stars | 94,208 |
| 语言 | TypeScript |
| Forks | 5,135 |
| Issues | 100 |
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
| Stars | 83,048 |
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
| Stars | 82,345 |
| 语言 | TypeScript |
| Forks | 10,112 |
| Issues | 611 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,391 |
| 语言 | TypeScript |
| Forks | 7,965 |
| Issues | 691 |
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
| Stars | 244,240 |
| 语言 | JavaScript |
| Forks | 50,875 |
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
| Stars | 116,451 |
| 语言 | JavaScript |
| Forks | 35,193 |
| Issues | 2,583 |
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
| Stars | 111,629 |
| 语言 | JavaScript |
| Forks | 36,317 |
| Issues | 575 |
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
| Stars | 108,657 |
| 语言 | JavaScript |
| Forks | 11,569 |
| Issues | 355 |
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
| Stars | 98,021 |
| 语言 | JavaScript |
| Forks | 32,690 |
| Issues | 1,717 |
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
| Stars | 95,474 |
| 语言 | JavaScript |
| Forks | 15,305 |
| Issues | 52 |
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
| Stars | 86,134 |
| 语言 | JavaScript |
| Forks | 4,832 |
| Issues | 978 |
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
| Stars | 70,875 |
| 语言 | JavaScript |
| Forks | 16,812 |
| Issues | 890 |
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
| Stars | 66,302 |
| 语言 | JavaScript |
| Forks | 9,194 |
| Issues | 2 |
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
| Stars | 65,990 |
| 语言 | JavaScript |
| Forks | 9,361 |
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
| Stars | 62,375 |
| 语言 | JavaScript |
| Forks | 3,988 |
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
| Stars | 61,576 |
| 语言 | JavaScript |
| Forks | 7,125 |
| Issues | 134 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,081 |
| 语言 | JavaScript |
| Forks | 5,633 |
| Issues | 64 |
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
| Stars | 59,868 |
| 语言 | JavaScript |
| Forks | 20,471 |
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
| Stars | 57,415 |
| 语言 | JavaScript |
| Forks | 12,302 |
| Issues | 12 |
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
| Stars | 53,048 |
| 语言 | JavaScript |
| Forks | 10,605 |
| Issues | 469 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,174 |
| 语言 | JavaScript |
| Forks | 11,398 |
| Issues | 362 |
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
| Stars | 133,184 |
| 语言 | Go |
| Forks | 18,884 |
| Issues | 9,912 |
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
| Stars | 87,325 |
| 语言 | Go |
| Forks | 8,225 |
| Issues | 263 |
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
| Stars | 81,229 |
| 语言 | Go |
| Forks | 4,976 |
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
| Stars | 68,663 |
| 语言 | Go |
| Forks | 3,225 |
| Issues | 6 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,316 |
| 语言 | Go |
| Forks | 4,997 |
| Issues | 1,160 |
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
| Stars | 50,967 |
| 语言 | Go |
| Forks | 21,884 |
| Issues | 384 |
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
| Stars | 49,236 |
| 语言 | Go |
| Forks | 7,968 |
| Issues | 559 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,777 |
| 语言 | Python |
| Forks | 11,258 |
| Issues | 311 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 340,488 |
| 语言 | Python |
| Forks | 55,079 |
| Issues | 520 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,415 |
| 语言 | Python |
| Forks | 16,793 |
| Issues | 19 |
| Topics | bounty, bugbounty, bypass, cheatsheet, enumeration, hacking, hacktoberfest, methodology, payload, payloads, penetration-testing, pentest, privilege-escalation, redteam, security, vulnerability, web-application |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,416 |
| 语言 | TypeScript |
| Forks | 16,485 |
| Issues | 45 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 78,919 |
| 语言 | JavaScript |
| Forks | 31,745 |
| Issues | 267 |
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
| Stars | 67,316 |
| 语言 | JavaScript |
| Forks | 11,970 |
| Issues | 540 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 105,656 |
| 语言 | Go |
| Forks | 14,962 |
| Issues | 49 |
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
| Stars | 50,419 |
| 语言 | Go |
| Forks | 1,592 |
| Issues | 266 |
| 许可证 | MIT License |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,976 |
| 语言 | Go |
| Forks | 8,869 |
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
| Stars | 45,705 |
| 语言 | Go |
| Forks | 3,777 |
| Issues | 82 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
