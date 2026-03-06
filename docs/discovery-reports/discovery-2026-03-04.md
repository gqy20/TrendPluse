# 项目发现报告 (2026-03-04)

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
| Stars | 125,730 |
| 语言 | Python |
| Forks | 17,791 |
| Issues | 299 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大且用户友好的自托管 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 12.5 万 Stars。它的独特价值在于提供开箱即用的企业级 AI 应用平台，集成了 RAG、MCP 协议等前沿特性，让个人开发者和企业都能快速搭建私有化 AI 服务。

**技术亮点**:
- 支持多 LLM 后端集成：兼容 Ollama、OpenAI API 等多种大模型服务，灵活切换
- 内置 RAG 能力：原生支持检索增强生成，可连接私有知识库实现智能问答
- MCP 协议支持：集成 Model Context Protocol，实现 AI 工具链的可扩展性
- 完全自托管部署：支持本地化部署，数据隐私可控，适合企业内网环境
- 现代化 Web UI：提供类似 ChatGPT 的直观交互界面，降低 AI 使用门槛

**适用场景**:
- 企业私有 AI 助手部署：企业可在内网部署，连接内部文档和知识库，为员工提供智能助手服务
- 个人开发者 AI 实验环境：支持本地运行 Ollama 等开源模型，供开发者测试和开发 AI 应用
- 教育与学习平台：学校和研究机构可搭建教学用 AI 界面，为学生提供安全的 AI 学习环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,163 |
| 语言 | Python |
| Forks | 8,252 |
| Issues | 3,025 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一款领先的开源检索增强生成（RAG）引擎，独特之处在于将RAG技术与Agent能力深度融合，为大语言模型构建了卓越的上下文层。该项目拥有74k+ stars，集成了GraphRAG、深度研究、MCP协议等前沿技术，是企业级AI应用开发的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，打造智能上下文层，提升LLM理解准确性
- 内置强大文档解析器，支持复杂文档理解和上下文工程
- 集成GraphRAG技术，实现知识图谱与检索增强的完美结合
- 支持多种LLM后端（OpenAI、Ollama、DeepSeek等）和MCP协议
- 具备深度研究（Deep-Research）和AI搜索能力，适合复杂知识推理场景

**适用场景**:
- 企业级智能客服系统：构建基于企业知识库的AI问答助手，准确理解并回答用户复杂问题
- 文档智能分析平台：自动解析、理解和检索海量文档，为业务决策提供智能支持
- AI Agent工作流开发：快速开发具备深度研究和知识检索能力的智能Agent应用



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 88,150 |
| 语言 | TypeScript |
| Forks | 6,224 |
| Issues | 200 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是一款专为 AI 应用打造的高性能网页数据 API，能够将整个网站转换为 LLM 友好的 Markdown 或结构化数据。其独特价值在于解决了 AI 开发者获取高质量网页数据的痛点，支持智能爬取、数据提取和格式转换，8.8万+ Star 充分证明了其在 AI 社区的影响力和实用性。

**技术亮点**:
- 🤖 AI-Native 设计：专为 LLM 优化，自动将网页转换为高质量的 Markdown 格式，无需额外清洗
- 🔥 全站点爬取：支持递归爬取整个网站，智能处理动态内容和 JavaScript 渲染
- 📊 结构化数据提取：可将网页内容转换为结构化 JSON 数据，便于 AI Agent 和 RAG 应用直接使用
- ⚡ 高性能 API：提供 RESTful API 接口，支持大规模并发请求和异步任务处理
- 🛡️ 智能反爬虫处理：内置代理池和请求优化策略，提高爬取成功率和稳定性

**适用场景**:
- 🏢 **企业 AI 应用开发**：构建 RAG 系统、知识库问答、AI Agent 等，需要高质量网页数据作为知识源
- 🔍 **数据采集与分析**：竞品分析、市场调研、舆情监控等需要批量获取和处理网站内容的场景
- 🔬 **个人开发者/初创公司**：快速搭建 AI 原型产品，无需从零开发爬虫基础设施，专注于核心业务逻辑



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,200 |
| 语言 | JavaScript |
| Forks | 7,460 |
| Issues | 28 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 Claude Code 及相关 AI Agent 性能优化的系统级项目，涵盖技能、记忆、安全和研究优先开发等核心能力。作为获得 6 万+ stars 的明星项目，它为开发者提供了构建高性能 AI Agent 的完整工具链，在 Anthropic 生态中具有重要的技术参考价值和实用意义。

**技术亮点**:
- Agent 性能优化系统，针对 Claude Code、Codex、Cowork 等多场景优化
- 集成 MCP (Model Context Protocol) 架构，支持与 LLM 的深度集成
- 具备记忆机制和技能管理系统，提升 Agent 的持续学习与适应能力
- 研究优先的开发方法，注重安全性和开发者工具生态
- 基于 JavaScript 生态，MIT 许可证，便于二次开发和集成

**适用场景**:
- 企业开发团队构建定制化 AI Coding Agent，优化内部开发流程
- 个人开发者学习 Claude Code Agent 架构，提升 AI 辅助编程效率
- 研究机构探索 LLM Agent 的性能优化和安全边界



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,405 |
| 语言 | JavaScript |
| Forks | 5,988 |
| Issues | 305 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，集成了 RAG、智能体构建、MCP 兼容性等企业级功能。它支持本地 LLM（如 Ollama、LM Studio）和云端模型（DeepSeek、Kimi、Llama3 等），提供了从数据接入到智能体部署的一站式解决方案，是企业和个人开发者快速搭建 AI 应用的理想选择。

**技术亮点**:
- 内置 RAG 引擎，支持向量数据库和网页抓取，实现智能文档检索与增强生成
- 零代码智能体构建器，可视化管理 AI Agent，支持 MCP 协议和 MCP 服务器集成
- 多模态支持，兼容本地 LLM（Ollama、LocalAI）和云端模型（DeepSeek、Kimi、Qwen3、Llama3、Moonshot 等）
- 灵活部署方式，支持桌面应用和 Docker 容器化部署
- 支持自定义 AI 智能体和工作流编排，适应复杂业务场景

**适用场景**:
- 企业知识库搭建：利用 RAG 能力快速构建内部文档问答系统，支持私有化部署保障数据安全
- AI 智能客服与助手：通过 No-code 构建器快速定制行业专属客服机器人，集成 MCP 扩展业务能力
- 开发者本地 AI 实验室：在本地环境运行 Llama3、Qwen3 等开源模型，进行 AI 应用原型开发与测试



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,237 |
| 语言 | Go |
| Forks | 3,627 |
| Issues | 145 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源大模型本地部署的标杆项目，提供 OpenAI/Claude 的完全替代方案。其独特价值在于无需 GPU、支持消费级硬件，同时兼容 OpenAI API 格式，实现了本地优先的隐私保护和成本控制。

**技术亮点**:
- 【零 GPU 依赖】纯 CPU 运行推理，支持消费级硬件，大幅降低部署门槛和硬件成本
- 【多模型生态】统一支持 gguf、transformers、diffusers 等多种格式，覆盖 LLaMA、Mistral、Stable Diffusion、RWKV、Mamba 等主流模型
- 【OpenAI API 兼容】Drop-in replacement 设计，无需修改现有代码即可迁移，支持文本、图像、音频、视频生成及 TTS、语音克隆
- 【分布式与 P2P】基于 libp2p 实现去中心化推理和分布式计算，支持 MCP 协议和负载均衡
- 【全栈生成能力】集成文本生成、图像生成、音频生成、目标检测、Rerank 等多种 AI 任务，支持音乐生成 MusicGen 等特色功能

**适用场景**:
- 【企业/组织数据隐私场景】金融、医疗、政府等对数据敏感的行业，可在本地服务器部署 LLM 和生成式 AI，避免数据外泄，符合合规要求
- 【开发者本地开发调试】AI 应用开发者可在无 GPU 环境下本地测试和调试应用，利用 OpenAI API 兼容性快速集成，降低云 API 调用成本
- 【边缘设备与离线环境】工业边缘计算、离线部署场景，在资源受限设备上运行 AI 能力，结合 P2P 分布式推理提升性能



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,046 |
| 语言 | TypeScript |
| Forks | 14,724 |
| Issues | 734 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，拥有 73K+ Stars，致力于重新定义人机交互方式。它提供了完整的 Agent 生态系统，支持多智能体协同工作，是构建 AI 助手和智能体团队的理想选择。

**技术亮点**:
- 基于 TypeScript 的现代化架构，类型安全且易于维护
- 支持多智能体协作(Multi-agent Collaboration)，可构建智能体团队
- 集成多种主流 AI 模型(OpenAI/GPT、Claude、Gemini、DeepSeek等)
- 提供 MCP(Model Context Protocol)支持和知识库功能
- 可视化的智能体团队设计工具，降低开发门槛

**适用场景**:
- 企业级 AI 智能体团队构建：为企业打造专业的 AI 助手团队，提升协作效率
- 个人开发者 AI 助手开发：快速开发和定制个性化 AI 智能体
- 知识库与智能问答系统：构建基于知识库的智能客服或内部问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,114 |
| 语言 | MDX |
| Forks | 7,572 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程(Prompt Engineering)开源指南项目，由dair-ai维护，获得71k+星标。项目整合了从基础prompt技巧到前沿AI Agents、RAG技术的完整知识体系，是开发者掌握与大语言模型交互技能的首选学习资源，尤其适合需要系统性学习prompt工程和构建AI应用的从业者。

**技术亮点**:
- 涵盖prompt工程全栈知识：从基础提示技巧到context engineering、RAG检索增强生成、AI Agents等前沿技术
- 提供丰富的实战资源：包含论文、教程、Jupyter notebooks和完整课程，理论结合实践
- 紧跟技术趋势：覆盖ChatGPT、OpenAI、LLMs等主流技术栈，涵盖generative-ai和deep-learning领域
- MDX格式内容：使用现代化文档格式，便于阅读和集成到各类知识管理系统
- 多语言模型支持：不仅限于OpenAI，还涵盖各类LLMs和AI框架的工程实践

**适用场景**:
- AI开发者学习：个人开发者或企业工程师系统学习prompt工程和AI应用开发技能，从入门到精通
- 团队知识库建设：企业团队作为内部培训教材和知识参考，统一团队对prompt engineering的理解和实践标准
- AI产品研发：构建基于LLMs的应用时参考最佳实践，包括RAG系统优化、Agent设计等关键技术实现



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,878 |
| 语言 | Python |
| Forks | 8,273 |
| Issues | 913 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 论文的工业级大模型微调工具，支持 100+ 种 LLM 和 VLM 的高效微调。它统一了主流微调技术（LoRA、QLoRA、全量微调等），提供图形化界面、命令行和 API 三种使用方式，已成为 GitHub 上最受欢迎的 LLM 微调框架之一（67K+ stars），特别适合需要快速部署和多模型支持的开发者与团队。

**技术亮点**:
- 支持 100+ 种大语言模型和多模态模型，包括 Llama3、Gemma、Qwen、DeepSeek、Mistral 等主流模型
- 集成多种高效微调方法：LoRA、QLoRA、全量微调、MoE、PEFT 等，显著降低训练成本
- 提供 RLHF（人类反馈强化学习）和指令调优（Instruction-tuning）功能，完整覆盖模型对齐流程
- 支持多模态视觉-语言模型（VLM）微调，扩展了传统纯文本模型的边界
- 提供 GUI、CLI 和 API 三种交互方式，内置量化、Agent 集成和训练监控工具

**适用场景**:
- 企业 AI 应用开发：快速微调开源大模型以适配特定业务场景（如客服、文档分析、代码助手），降低 API 调用成本并保护数据隐私
- 学术研究与实验：研究人员可使用统一框架对比不同微调方法（如 LoRA vs QLoRA）和模型架构，加速论文实验和模型迭代
- 个人开发者 AI 项目：通过 GUI 界面快速上手，在消费级 GPU 上微调小型模型（如 Qwen、Gemma），构建个人 AI 助手或垂直领域应用



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,333 |
| 语言 | Java |
| Forks | 15,827 |
| Issues | 59 |
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
| Stars | 41,864 |
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
| Stars | 34,333 |
| 语言 | TypeScript |
| Forks | 6,933 |
| Issues | 427 |
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
| Stars | 32,984 |
| 语言 | Python |
| Forks | 2,012 |
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
| Stars | 32,901 |
| 语言 | TypeScript |
| Forks | 2,239 |
| Issues | 72 |
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
| Stars | 38,628 |
| 语言 | Python |
| Forks | 6,119 |
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
| Stars | 31,123 |
| 语言 | Jupyter Notebook |
| Forks | 5,066 |
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
| Stars | 99,557 |
| 语言 | Python |
| Forks | 14,475 |
| Issues | 6 |
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
| Stars | 68,543 |
| 语言 | Python |
| Forks | 8,552 |
| Issues | 350 |
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
| Stars | 36,855 |
| 语言 | TypeScript |
| Forks | 2,777 |
| Issues | 312 |
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
| Stars | 79,583 |
| 语言 | Python |
| Forks | 9,408 |
| Issues | 229 |
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
| Stars | 49,965 |
| 语言 | TypeScript |
| Forks | 23,840 |
| Issues | 789 |
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
| Stars | 177,562 |
| 语言 | TypeScript |
| Forks | 55,417 |
| Issues | 1,407 |
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
| Stars | 145,250 |
| 语言 | Python |
| Forks | 8,506 |
| Issues | 910 |
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
| Stars | 52,902 |
| 语言 | Jupyter Notebook |
| Forks | 18,397 |
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
| Stars | 30,704 |
| 语言 | TypeScript |
| Forks | 3,244 |
| Issues | 236 |
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
| Stars | 30,210 |
| 语言 | Python |
| Forks | 3,311 |
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
| Stars | 40,649 |
| 语言 | Python |
| Forks | 4,040 |
| Issues | 245 |
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
| Stars | 125,730 |
| 语言 | Python |
| Forks | 17,791 |
| Issues | 299 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大且用户友好的自托管 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 12.5 万 Stars。它的独特价值在于提供开箱即用的企业级 AI 应用平台，集成了 RAG、MCP 协议等前沿特性，让个人开发者和企业都能快速搭建私有化 AI 服务。

**技术亮点**:
- 支持多 LLM 后端集成：兼容 Ollama、OpenAI API 等多种大模型服务，灵活切换
- 内置 RAG 能力：原生支持检索增强生成，可连接私有知识库实现智能问答
- MCP 协议支持：集成 Model Context Protocol，实现 AI 工具链的可扩展性
- 完全自托管部署：支持本地化部署，数据隐私可控，适合企业内网环境
- 现代化 Web UI：提供类似 ChatGPT 的直观交互界面，降低 AI 使用门槛

**适用场景**:
- 企业私有 AI 助手部署：企业可在内网部署，连接内部文档和知识库，为员工提供智能助手服务
- 个人开发者 AI 实验环境：支持本地运行 Ollama 等开源模型，供开发者测试和开发 AI 应用
- 教育与学习平台：学校和研究机构可搭建教学用 AI 界面，为学生提供安全的 AI 学习环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,163 |
| 语言 | Python |
| Forks | 8,252 |
| Issues | 3,025 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一款领先的开源检索增强生成（RAG）引擎，独特之处在于将RAG技术与Agent能力深度融合，为大语言模型构建了卓越的上下文层。该项目拥有74k+ stars，集成了GraphRAG、深度研究、MCP协议等前沿技术，是企业级AI应用开发的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，打造智能上下文层，提升LLM理解准确性
- 内置强大文档解析器，支持复杂文档理解和上下文工程
- 集成GraphRAG技术，实现知识图谱与检索增强的完美结合
- 支持多种LLM后端（OpenAI、Ollama、DeepSeek等）和MCP协议
- 具备深度研究（Deep-Research）和AI搜索能力，适合复杂知识推理场景

**适用场景**:
- 企业级智能客服系统：构建基于企业知识库的AI问答助手，准确理解并回答用户复杂问题
- 文档智能分析平台：自动解析、理解和检索海量文档，为业务决策提供智能支持
- AI Agent工作流开发：快速开发具备深度研究和知识检索能力的智能Agent应用



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,405 |
| 语言 | JavaScript |
| Forks | 5,988 |
| Issues | 305 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，集成了 RAG、智能体构建、MCP 兼容性等企业级功能。它支持本地 LLM（如 Ollama、LM Studio）和云端模型（DeepSeek、Kimi、Llama3 等），提供了从数据接入到智能体部署的一站式解决方案，是企业和个人开发者快速搭建 AI 应用的理想选择。

**技术亮点**:
- 内置 RAG 引擎，支持向量数据库和网页抓取，实现智能文档检索与增强生成
- 零代码智能体构建器，可视化管理 AI Agent，支持 MCP 协议和 MCP 服务器集成
- 多模态支持，兼容本地 LLM（Ollama、LocalAI）和云端模型（DeepSeek、Kimi、Qwen3、Llama3、Moonshot 等）
- 灵活部署方式，支持桌面应用和 Docker 容器化部署
- 支持自定义 AI 智能体和工作流编排，适应复杂业务场景

**适用场景**:
- 企业知识库搭建：利用 RAG 能力快速构建内部文档问答系统，支持私有化部署保障数据安全
- AI 智能客服与助手：通过 No-code 构建器快速定制行业专属客服机器人，集成 MCP 扩展业务能力
- 开发者本地 AI 实验室：在本地环境运行 Llama3、Qwen3 等开源模型，进行 AI 应用原型开发与测试



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,046 |
| 语言 | TypeScript |
| Forks | 14,724 |
| Issues | 734 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，拥有 73K+ Stars，致力于重新定义人机交互方式。它提供了完整的 Agent 生态系统，支持多智能体协同工作，是构建 AI 助手和智能体团队的理想选择。

**技术亮点**:
- 基于 TypeScript 的现代化架构，类型安全且易于维护
- 支持多智能体协作(Multi-agent Collaboration)，可构建智能体团队
- 集成多种主流 AI 模型(OpenAI/GPT、Claude、Gemini、DeepSeek等)
- 提供 MCP(Model Context Protocol)支持和知识库功能
- 可视化的智能体团队设计工具，降低开发门槛

**适用场景**:
- 企业级 AI 智能体团队构建：为企业打造专业的 AI 助手团队，提升协作效率
- 个人开发者 AI 助手开发：快速开发和定制个性化 AI 智能体
- 知识库与智能问答系统：构建基于知识库的智能客服或内部问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,114 |
| 语言 | MDX |
| Forks | 7,572 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程(Prompt Engineering)开源指南项目，由dair-ai维护，获得71k+星标。项目整合了从基础prompt技巧到前沿AI Agents、RAG技术的完整知识体系，是开发者掌握与大语言模型交互技能的首选学习资源，尤其适合需要系统性学习prompt工程和构建AI应用的从业者。

**技术亮点**:
- 涵盖prompt工程全栈知识：从基础提示技巧到context engineering、RAG检索增强生成、AI Agents等前沿技术
- 提供丰富的实战资源：包含论文、教程、Jupyter notebooks和完整课程，理论结合实践
- 紧跟技术趋势：覆盖ChatGPT、OpenAI、LLMs等主流技术栈，涵盖generative-ai和deep-learning领域
- MDX格式内容：使用现代化文档格式，便于阅读和集成到各类知识管理系统
- 多语言模型支持：不仅限于OpenAI，还涵盖各类LLMs和AI框架的工程实践

**适用场景**:
- AI开发者学习：个人开发者或企业工程师系统学习prompt工程和AI应用开发技能，从入门到精通
- 团队知识库建设：企业团队作为内部培训教材和知识参考，统一团队对prompt engineering的理解和实践标准
- AI产品研发：构建基于LLMs的应用时参考最佳实践，包括RAG系统优化、Agent设计等关键技术实现



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,333 |
| 语言 | Java |
| Forks | 15,827 |
| Issues | 59 |
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
| Stars | 32,984 |
| 语言 | Python |
| Forks | 2,012 |
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
| Stars | 32,901 |
| 语言 | TypeScript |
| Forks | 2,239 |
| Issues | 72 |
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
| Stars | 38,628 |
| 语言 | Python |
| Forks | 6,119 |
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
| Stars | 31,123 |
| 语言 | Jupyter Notebook |
| Forks | 5,066 |
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
| Stars | 99,557 |
| 语言 | Python |
| Forks | 14,475 |
| Issues | 6 |
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
| Stars | 98,530 |
| 语言 | TypeScript |
| Forks | 11,711 |
| Issues | 965 |
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
| Stars | 49,965 |
| 语言 | TypeScript |
| Forks | 23,840 |
| Issues | 789 |
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
| Stars | 71,560 |
| 语言 | Python |
| Forks | 9,891 |
| Issues | 264 |
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
| Stars | 43,127 |
| 语言 | Go |
| Forks | 3,870 |
| Issues | 1,033 |
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
| Stars | 31,222 |
| 语言 | Python |
| Forks | 3,288 |
| Issues | 68 |
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
| Stars | 30,704 |
| 语言 | TypeScript |
| Forks | 3,244 |
| Issues | 236 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai |
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
| Stars | 125,730 |
| 语言 | Python |
| Forks | 17,791 |
| Issues | 299 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能强大且用户友好的自托管 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，拥有超过 12.5 万 Stars。它的独特价值在于提供开箱即用的企业级 AI 应用平台，集成了 RAG、MCP 协议等前沿特性，让个人开发者和企业都能快速搭建私有化 AI 服务。

**技术亮点**:
- 支持多 LLM 后端集成：兼容 Ollama、OpenAI API 等多种大模型服务，灵活切换
- 内置 RAG 能力：原生支持检索增强生成，可连接私有知识库实现智能问答
- MCP 协议支持：集成 Model Context Protocol，实现 AI 工具链的可扩展性
- 完全自托管部署：支持本地化部署，数据隐私可控，适合企业内网环境
- 现代化 Web UI：提供类似 ChatGPT 的直观交互界面，降低 AI 使用门槛

**适用场景**:
- 企业私有 AI 助手部署：企业可在内网部署，连接内部文档和知识库，为员工提供智能助手服务
- 个人开发者 AI 实验环境：支持本地运行 Ollama 等开源模型，供开发者测试和开发 AI 应用
- 教育与学习平台：学校和研究机构可搭建教学用 AI 界面，为学生提供安全的 AI 学习环境



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 74,163 |
| 语言 | Python |
| Forks | 8,252 |
| Issues | 3,025 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow是一款领先的开源检索增强生成（RAG）引擎，独特之处在于将RAG技术与Agent能力深度融合，为大语言模型构建了卓越的上下文层。该项目拥有74k+ stars，集成了GraphRAG、深度研究、MCP协议等前沿技术，是企业级AI应用开发的理想选择。

**技术亮点**:
- 融合RAG与Agent能力，打造智能上下文层，提升LLM理解准确性
- 内置强大文档解析器，支持复杂文档理解和上下文工程
- 集成GraphRAG技术，实现知识图谱与检索增强的完美结合
- 支持多种LLM后端（OpenAI、Ollama、DeepSeek等）和MCP协议
- 具备深度研究（Deep-Research）和AI搜索能力，适合复杂知识推理场景

**适用场景**:
- 企业级智能客服系统：构建基于企业知识库的AI问答助手，准确理解并回答用户复杂问题
- 文档智能分析平台：自动解析、理解和检索海量文档，为业务决策提供智能支持
- AI Agent工作流开发：快速开发具备深度研究和知识检索能力的智能Agent应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,200 |
| 语言 | JavaScript |
| Forks | 7,460 |
| Issues | 28 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 Claude Code 及相关 AI Agent 性能优化的系统级项目，涵盖技能、记忆、安全和研究优先开发等核心能力。作为获得 6 万+ stars 的明星项目，它为开发者提供了构建高性能 AI Agent 的完整工具链，在 Anthropic 生态中具有重要的技术参考价值和实用意义。

**技术亮点**:
- Agent 性能优化系统，针对 Claude Code、Codex、Cowork 等多场景优化
- 集成 MCP (Model Context Protocol) 架构，支持与 LLM 的深度集成
- 具备记忆机制和技能管理系统，提升 Agent 的持续学习与适应能力
- 研究优先的开发方法，注重安全性和开发者工具生态
- 基于 JavaScript 生态，MIT 许可证，便于二次开发和集成

**适用场景**:
- 企业开发团队构建定制化 AI Coding Agent，优化内部开发流程
- 个人开发者学习 Claude Code Agent 架构，提升 AI 辅助编程效率
- 研究机构探索 LLM Agent 的性能优化和安全边界



### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,405 |
| 语言 | JavaScript |
| Forks | 5,988 |
| Issues | 305 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，集成了 RAG、智能体构建、MCP 兼容性等企业级功能。它支持本地 LLM（如 Ollama、LM Studio）和云端模型（DeepSeek、Kimi、Llama3 等），提供了从数据接入到智能体部署的一站式解决方案，是企业和个人开发者快速搭建 AI 应用的理想选择。

**技术亮点**:
- 内置 RAG 引擎，支持向量数据库和网页抓取，实现智能文档检索与增强生成
- 零代码智能体构建器，可视化管理 AI Agent，支持 MCP 协议和 MCP 服务器集成
- 多模态支持，兼容本地 LLM（Ollama、LocalAI）和云端模型（DeepSeek、Kimi、Qwen3、Llama3、Moonshot 等）
- 灵活部署方式，支持桌面应用和 Docker 容器化部署
- 支持自定义 AI 智能体和工作流编排，适应复杂业务场景

**适用场景**:
- 企业知识库搭建：利用 RAG 能力快速构建内部文档问答系统，支持私有化部署保障数据安全
- AI 智能客服与助手：通过 No-code 构建器快速定制行业专属客服机器人，集成 MCP 扩展业务能力
- 开发者本地 AI 实验室：在本地环境运行 Llama3、Qwen3 等开源模型，进行 AI 应用原型开发与测试



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,046 |
| 语言 | TypeScript |
| Forks | 14,724 |
| Issues | 734 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个领先的多智能体协作平台，拥有 73K+ Stars，致力于重新定义人机交互方式。它提供了完整的 Agent 生态系统，支持多智能体协同工作，是构建 AI 助手和智能体团队的理想选择。

**技术亮点**:
- 基于 TypeScript 的现代化架构，类型安全且易于维护
- 支持多智能体协作(Multi-agent Collaboration)，可构建智能体团队
- 集成多种主流 AI 模型(OpenAI/GPT、Claude、Gemini、DeepSeek等)
- 提供 MCP(Model Context Protocol)支持和知识库功能
- 可视化的智能体团队设计工具，降低开发门槛

**适用场景**:
- 企业级 AI 智能体团队构建：为企业打造专业的 AI 助手团队，提升协作效率
- 个人开发者 AI 助手开发：快速开发和定制个性化 AI 智能体
- 知识库与智能问答系统：构建基于知识库的智能客服或内部问答系统



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,114 |
| 语言 | MDX |
| Forks | 7,572 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程(Prompt Engineering)开源指南项目，由dair-ai维护，获得71k+星标。项目整合了从基础prompt技巧到前沿AI Agents、RAG技术的完整知识体系，是开发者掌握与大语言模型交互技能的首选学习资源，尤其适合需要系统性学习prompt工程和构建AI应用的从业者。

**技术亮点**:
- 涵盖prompt工程全栈知识：从基础提示技巧到context engineering、RAG检索增强生成、AI Agents等前沿技术
- 提供丰富的实战资源：包含论文、教程、Jupyter notebooks和完整课程，理论结合实践
- 紧跟技术趋势：覆盖ChatGPT、OpenAI、LLMs等主流技术栈，涵盖generative-ai和deep-learning领域
- MDX格式内容：使用现代化文档格式，便于阅读和集成到各类知识管理系统
- 多语言模型支持：不仅限于OpenAI，还涵盖各类LLMs和AI框架的工程实践

**适用场景**:
- AI开发者学习：个人开发者或企业工程师系统学习prompt工程和AI应用开发技能，从入门到精通
- 团队知识库建设：企业团队作为内部培训教材和知识参考，统一团队对prompt engineering的理解和实践标准
- AI产品研发：构建基于LLMs的应用时参考最佳实践，包括RAG系统优化、Agent设计等关键技术实现



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,020 |
| 语言 | HTML |
| Forks | 19,724 |
| Issues | 20 |
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
| Stars | 87,054 |
| 语言 | Jupyter Notebook |
| Forks | 13,212 |
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
| Stars | 41,864 |
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
| Stars | 34,333 |
| 语言 | TypeScript |
| Forks | 6,933 |
| Issues | 427 |
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
| Stars | 32,984 |
| 语言 | Python |
| Forks | 2,012 |
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
| Stars | 32,901 |
| 语言 | TypeScript |
| Forks | 2,239 |
| Issues | 72 |
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
| Stars | 68,543 |
| 语言 | Python |
| Forks | 8,552 |
| Issues | 350 |
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
| Stars | 36,855 |
| 语言 | TypeScript |
| Forks | 2,777 |
| Issues | 312 |
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
| Stars | 49,965 |
| 语言 | TypeScript |
| Forks | 23,840 |
| Issues | 789 |
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
| Stars | 33,713 |
| 语言 | HTML |
| Forks | 5,382 |
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
| Stars | 71,962 |
| 语言 | Python |
| Forks | 13,955 |
| Issues | 3,491 |
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
| Stars | 36,978 |
| 语言 | Python |
| Forks | 3,606 |
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
| Stars | 145,250 |
| 语言 | Python |
| Forks | 8,506 |
| Issues | 910 |
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
| Stars | 164,080 |
| 语言 | Go |
| Forks | 14,763 |
| Issues | 2,554 |
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
| Stars | 46,391 |
| 语言 | Rust |
| Forks | 9,076 |
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
| Stars | 30,210 |
| 语言 | Python |
| Forks | 3,311 |
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
| Stars | 38,761 |
| 语言 | TypeScript |
| Forks | 3,922 |
| Issues | 1,055 |
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
| Stars | 40,649 |
| 语言 | Python |
| Forks | 4,040 |
| Issues | 245 |
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
| Stars | 90,071 |
| 语言 | Python |
| Forks | 5,284 |
| Issues | 445 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (13 个项目) { #机器学习框架 }


### 🌟 高优先级


### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,114 |
| 语言 | MDX |
| Forks | 7,572 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程(Prompt Engineering)开源指南项目，由dair-ai维护，获得71k+星标。项目整合了从基础prompt技巧到前沿AI Agents、RAG技术的完整知识体系，是开发者掌握与大语言模型交互技能的首选学习资源，尤其适合需要系统性学习prompt工程和构建AI应用的从业者。

**技术亮点**:
- 涵盖prompt工程全栈知识：从基础提示技巧到context engineering、RAG检索增强生成、AI Agents等前沿技术
- 提供丰富的实战资源：包含论文、教程、Jupyter notebooks和完整课程，理论结合实践
- 紧跟技术趋势：覆盖ChatGPT、OpenAI、LLMs等主流技术栈，涵盖generative-ai和deep-learning领域
- MDX格式内容：使用现代化文档格式，便于阅读和集成到各类知识管理系统
- 多语言模型支持：不仅限于OpenAI，还涵盖各类LLMs和AI框架的工程实践

**适用场景**:
- AI开发者学习：个人开发者或企业工程师系统学习prompt工程和AI应用开发技能，从入门到精通
- 团队知识库建设：企业团队作为内部培训教材和知识参考，统一团队对prompt engineering的理解和实践标准
- AI产品研发：构建基于LLMs的应用时参考最佳实践，包括RAG系统优化、Agent设计等关键技术实现



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,878 |
| 语言 | Python |
| Forks | 8,273 |
| Issues | 913 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是 ACL 2024 论文的工业级大模型微调工具，支持 100+ 种 LLM 和 VLM 的高效微调。它统一了主流微调技术（LoRA、QLoRA、全量微调等），提供图形化界面、命令行和 API 三种使用方式，已成为 GitHub 上最受欢迎的 LLM 微调框架之一（67K+ stars），特别适合需要快速部署和多模型支持的开发者与团队。

**技术亮点**:
- 支持 100+ 种大语言模型和多模态模型，包括 Llama3、Gemma、Qwen、DeepSeek、Mistral 等主流模型
- 集成多种高效微调方法：LoRA、QLoRA、全量微调、MoE、PEFT 等，显著降低训练成本
- 提供 RLHF（人类反馈强化学习）和指令调优（Instruction-tuning）功能，完整覆盖模型对齐流程
- 支持多模态视觉-语言模型（VLM）微调，扩展了传统纯文本模型的边界
- 提供 GUI、CLI 和 API 三种交互方式，内置量化、Agent 集成和训练监控工具

**适用场景**:
- 企业 AI 应用开发：快速微调开源大模型以适配特定业务场景（如客服、文档分析、代码助手），降低 API 调用成本并保护数据隐私
- 学术研究与实验：研究人员可使用统一框架对比不同微调方法（如 LoRA vs QLoRA）和模型架构，加速论文实验和模型迭代
- 个人开发者 AI 项目：通过 GUI 界面快速上手，在消费级 GPU 上微调小型模型（如 Qwen、Gemma），构建个人 AI 助手或垂直领域应用



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,548 |
| 语言 | Python |
| Forks | 6,115 |
| Issues | 59 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个**全功能金融数据平台**，为金融分析师、量化交易者和 AI 智能体提供统一的数据访问接口。该项目整合了股票、加密货币、衍生品、固收等多种资产类别的数据源，拥有超过 6.2 万颗星，是金融科技领域最受关注的开源项目之一，尤其适合构建 AI 驱动的金融分析应用。

**技术亮点**:
- 统一 API 设计：提供一致的接口访问多种金融数据源（股票、加密货币、期权、固收等）
- AI 原生架构：专为 AI 智能体和机器学习模型设计的数据管道，便于集成 LLM 和量化算法
- Python 优先：纯 Python 实现，无缝集成 NumPy、Pandas、Scikit-learn 等数据科学生态
- 量化金融工具集：内置技术指标、回测框架、风险管理等量化分析功能
- 开源可扩展：模块化设计支持自定义数据源和策略，适合二次开发

**适用场景**:
- 金融数据分析与研究：个人/机构分析师进行市场研究、财报分析、资产定价等
- 量化交易策略开发：交易员构建回测系统、算法交易策略、风险管理模型
- AI 金融应用开发：开发者构建智能投顾、金融聊天机器人、自动化分析报告生成系统



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,020 |
| 语言 | HTML |
| Forks | 19,724 |
| Issues | 20 |
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
| Stars | 87,054 |
| 语言 | Jupyter Notebook |
| Forks | 13,212 |
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
| Stars | 31,123 |
| 语言 | Jupyter Notebook |
| Forks | 5,066 |
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
| Stars | 157,382 |
| 语言 | Python |
| Forks | 32,281 |
| Issues | 2,260 |
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
| Stars | 71,962 |
| 语言 | Python |
| Forks | 13,955 |
| Issues | 3,491 |
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
| Stars | 161,480 |
| 语言 | Python |
| Forks | 30,116 |
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
| Stars | 104,853 |
| 语言 | Python |
| Forks | 12,012 |
| Issues | 3,784 |
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
| Stars | 97,960 |
| 语言 | Python |
| Forks | 27,065 |
| Issues | 18,087 |
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
| Stars | 30,704 |
| 语言 | TypeScript |
| Forks | 3,244 |
| Issues | 236 |
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
| Stars | 76,056 |
| 语言 | Unknown |
| Forks | 8,775 |
| Issues | 77 |
| Topics | course, large-language-models, llm, machine-learning, roadmap |
| 许可证 | Apache License 2.0 |


## 🛠️ 开发工具 (17 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Cowork, and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,200 |
| 语言 | JavaScript |
| Forks | 7,460 |
| Issues | 28 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 Claude Code 及相关 AI Agent 性能优化的系统级项目，涵盖技能、记忆、安全和研究优先开发等核心能力。作为获得 6 万+ stars 的明星项目，它为开发者提供了构建高性能 AI Agent 的完整工具链，在 Anthropic 生态中具有重要的技术参考价值和实用意义。

**技术亮点**:
- Agent 性能优化系统，针对 Claude Code、Codex、Cowork 等多场景优化
- 集成 MCP (Model Context Protocol) 架构，支持与 LLM 的深度集成
- 具备记忆机制和技能管理系统，提升 Agent 的持续学习与适应能力
- 研究优先的开发方法，注重安全性和开发者工具生态
- 基于 JavaScript 生态，MIT 许可证，便于二次开发和集成

**适用场景**:
- 企业开发团队构建定制化 AI Coding Agent，优化内部开发流程
- 个人开发者学习 Claude Code Agent 架构，提升 AI 辅助编程效率
- 研究机构探索 LLM Agent 的性能优化和安全边界



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,237 |
| 语言 | Go |
| Forks | 3,627 |
| Issues | 145 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源大模型本地部署的标杆项目，提供 OpenAI/Claude 的完全替代方案。其独特价值在于无需 GPU、支持消费级硬件，同时兼容 OpenAI API 格式，实现了本地优先的隐私保护和成本控制。

**技术亮点**:
- 【零 GPU 依赖】纯 CPU 运行推理，支持消费级硬件，大幅降低部署门槛和硬件成本
- 【多模型生态】统一支持 gguf、transformers、diffusers 等多种格式，覆盖 LLaMA、Mistral、Stable Diffusion、RWKV、Mamba 等主流模型
- 【OpenAI API 兼容】Drop-in replacement 设计，无需修改现有代码即可迁移，支持文本、图像、音频、视频生成及 TTS、语音克隆
- 【分布式与 P2P】基于 libp2p 实现去中心化推理和分布式计算，支持 MCP 协议和负载均衡
- 【全栈生成能力】集成文本生成、图像生成、音频生成、目标检测、Rerank 等多种 AI 任务，支持音乐生成 MusicGen 等特色功能

**适用场景**:
- 【企业/组织数据隐私场景】金融、医疗、政府等对数据敏感的行业，可在本地服务器部署 LLM 和生成式 AI，避免数据外泄，符合合规要求
- 【开发者本地开发调试】AI 应用开发者可在无 GPU 环境下本地测试和调试应用，利用 OpenAI API 兼容性快速集成，降低云 API 调用成本
- 【边缘设备与离线环境】工业边缘计算、离线部署场景，在资源受限设备上运行 AI 能力，结合 P2P 分布式推理提升性能



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,543 |
| 语言 | Python |
| Forks | 8,552 |
| Issues | 350 |
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
| Stars | 36,855 |
| 语言 | TypeScript |
| Forks | 2,777 |
| Issues | 312 |
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
| Stars | 177,562 |
| 语言 | TypeScript |
| Forks | 55,417 |
| Issues | 1,407 |
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
| Stars | 149,570 |
| 语言 | Python |
| Forks | 12,113 |
| Issues | 2,351 |
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
| Stars | 95,866 |
| 语言 | Python |
| Forks | 8,780 |
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
| Stars | 73,352 |
| 语言 | Python |
| Forks | 8,699 |
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
| Stars | 182,293 |
| 语言 | TypeScript |
| Forks | 38,275 |
| Issues | 14,516 |
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
| Stars | 93,699 |
| 语言 | TypeScript |
| Forks | 9,377 |
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
| Stars | 78,103 |
| 语言 | TypeScript |
| Forks | 5,610 |
| Issues | 669 |
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
| Stars | 76,470 |
| 语言 | TypeScript |
| Forks | 6,535 |
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
| Stars | 75,635 |
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
| Stars | 78,302 |
| 语言 | Go |
| Forks | 2,701 |
| Issues | 318 |
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
| Stars | 73,495 |
| 语言 | Go |
| Forks | 2,556 |
| Issues | 913 |
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
| Stars | 42,902 |
| 语言 | Go |
| Forks | 8,016 |
| Issues | 922 |
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
| Stars | 404,126 |
| 语言 | Python |
| Forks | 43,593 |
| Issues | 921 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (17 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-opencode

**描述**: the best agent harness

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 36,855 |
| 语言 | TypeScript |
| Forks | 2,777 |
| Issues | 312 |
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
| Stars | 177,562 |
| 语言 | TypeScript |
| Forks | 55,417 |
| Issues | 1,407 |
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
| Stars | 51,605 |
| 语言 | Go |
| Forks | 10,330 |
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
| Stars | 120,920 |
| 语言 | Go |
| Forks | 42,589 |
| Issues | 2,669 |
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
| Stars | 71,475 |
| 语言 | Go |
| Forks | 18,915 |
| Issues | 3,791 |
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
| Stars | 54,068 |
| 语言 | Go |
| Forks | 6,422 |
| Issues | 2,845 |
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
| Stars | 47,544 |
| 语言 | Go |
| Forks | 5,067 |
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
| Stars | 30,210 |
| 语言 | Python |
| Forks | 3,311 |
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
| Stars | 93,699 |
| 语言 | TypeScript |
| Forks | 9,377 |
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
| Stars | 83,471 |
| 语言 | TypeScript |
| Forks | 5,225 |
| Issues | 600 |
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
| Stars | 74,936 |
| 语言 | TypeScript |
| Forks | 6,350 |
| Issues | 409 |
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
| Stars | 83,576 |
| 语言 | JavaScript |
| Forks | 7,475 |
| Issues | 702 |
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
| Stars | 69,127 |
| 语言 | Go |
| Forks | 1,869 |
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
| Stars | 62,031 |
| 语言 | Go |
| Forks | 5,855 |
| Issues | 768 |
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
| Stars | 57,464 |
| 语言 | Go |
| Forks | 4,154 |
| Issues | 20 |
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
| Stars | 40,649 |
| 语言 | Python |
| Forks | 4,040 |
| Issues | 245 |
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
| Stars | 60,423 |
| 语言 | Go |
| Forks | 7,178 |
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
| Stars | 83,576 |
| 语言 | JavaScript |
| Forks | 7,475 |
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
| Stars | 63,038 |
| 语言 | Go |
| Forks | 10,211 |
| Issues | 750 |
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
| Stars | 43,237 |
| 语言 | Go |
| Forks | 3,627 |
| Issues | 145 |
| Topics | ai, api, audio-generation, decentralized, distributed, gemma, image-generation, libp2p, llama, llm, mamba, mcp, mistral, musicgen, object-detection, rerank, rwkv, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是开源大模型本地部署的标杆项目，提供 OpenAI/Claude 的完全替代方案。其独特价值在于无需 GPU、支持消费级硬件，同时兼容 OpenAI API 格式，实现了本地优先的隐私保护和成本控制。

**技术亮点**:
- 【零 GPU 依赖】纯 CPU 运行推理，支持消费级硬件，大幅降低部署门槛和硬件成本
- 【多模型生态】统一支持 gguf、transformers、diffusers 等多种格式，覆盖 LLaMA、Mistral、Stable Diffusion、RWKV、Mamba 等主流模型
- 【OpenAI API 兼容】Drop-in replacement 设计，无需修改现有代码即可迁移，支持文本、图像、音频、视频生成及 TTS、语音克隆
- 【分布式与 P2P】基于 libp2p 实现去中心化推理和分布式计算，支持 MCP 协议和负载均衡
- 【全栈生成能力】集成文本生成、图像生成、音频生成、目标检测、Rerank 等多种 AI 任务，支持音乐生成 MusicGen 等特色功能

**适用场景**:
- 【企业/组织数据隐私场景】金融、医疗、政府等对数据敏感的行业，可在本地服务器部署 LLM 和生成式 AI，避免数据外泄，符合合规要求
- 【开发者本地开发调试】AI 应用开发者可在无 GPU 环境下本地测试和调试应用，利用 OpenAI API 兼容性快速集成，降低云 API 调用成本
- 【边缘设备与离线环境】工业边缘计算、离线部署场景，在资源受限设备上运行 AI 能力，结合 P2P 分布式推理提升性能



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,866 |
| 语言 | Python |
| Forks | 8,780 |
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
| Forks | 33,712 |
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
| Stars | 100,063 |
| 语言 | TypeScript |
| Forks | 27,096 |
| Issues | 1,114 |
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
| Stars | 78,103 |
| 语言 | TypeScript |
| Forks | 5,610 |
| Issues | 669 |
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
| Stars | 74,855 |
| 语言 | TypeScript |
| Forks | 8,234 |
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
| Stars | 75,635 |
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
| Stars | 68,864 |
| 语言 | JavaScript |
| Forks | 22,724 |
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
| Forks | 10,222 |
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
| Stars | 88,189 |
| 语言 | Go |
| Forks | 8,570 |
| Issues | 642 |
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
| Stars | 70,567 |
| 语言 | Go |
| Forks | 4,659 |
| Issues | 236 |
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
| Stars | 56,541 |
| 语言 | Go |
| Forks | 3,161 |
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
| Stars | 404,126 |
| 语言 | Python |
| Forks | 43,593 |
| Issues | 921 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## 📊 数据/基础设施 (4 个项目) { #数据-基础设施 }


### 🌟 高优先级


### Mintplex-Labs/anything-llm

**描述**: The all-in-one Desktop & Docker AI application with built-in RAG, AI agents, No-code agent builder, MCP compatibility,  and more.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,405 |
| 语言 | JavaScript |
| Forks | 5,988 |
| Issues | 305 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |

---

AnythingLLM 是一个功能全面的 AI 应用平台，集成了 RAG、智能体构建、MCP 兼容性等企业级功能。它支持本地 LLM（如 Ollama、LM Studio）和云端模型（DeepSeek、Kimi、Llama3 等），提供了从数据接入到智能体部署的一站式解决方案，是企业和个人开发者快速搭建 AI 应用的理想选择。

**技术亮点**:
- 内置 RAG 引擎，支持向量数据库和网页抓取，实现智能文档检索与增强生成
- 零代码智能体构建器，可视化管理 AI Agent，支持 MCP 协议和 MCP 服务器集成
- 多模态支持，兼容本地 LLM（Ollama、LocalAI）和云端模型（DeepSeek、Kimi、Qwen3、Llama3、Moonshot 等）
- 灵活部署方式，支持桌面应用和 Docker 容器化部署
- 支持自定义 AI 智能体和工作流编排，适应复杂业务场景

**适用场景**:
- 企业知识库搭建：利用 RAG 能力快速构建内部文档问答系统，支持私有化部署保障数据安全
- AI 智能客服与助手：通过 No-code 构建器快速定制行业专属客服机器人，集成 MCP 扩展业务能力
- 开发者本地 AI 实验室：在本地环境运行 Llama3、Qwen3 等开源模型，进行 AI 应用原型开发与测试



### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 98,530 |
| 语言 | TypeScript |
| Forks | 11,711 |
| Issues | 965 |
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
| Stars | 43,127 |
| 语言 | Go |
| Forks | 3,870 |
| Issues | 1,033 |
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
| Stars | 51,605 |
| 语言 | Go |
| Forks | 10,330 |
| Issues | 216 |
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
| Stars | 71,114 |
| 语言 | MDX |
| Forks | 7,572 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是目前最全面的提示工程(Prompt Engineering)开源指南项目，由dair-ai维护，获得71k+星标。项目整合了从基础prompt技巧到前沿AI Agents、RAG技术的完整知识体系，是开发者掌握与大语言模型交互技能的首选学习资源，尤其适合需要系统性学习prompt工程和构建AI应用的从业者。

**技术亮点**:
- 涵盖prompt工程全栈知识：从基础提示技巧到context engineering、RAG检索增强生成、AI Agents等前沿技术
- 提供丰富的实战资源：包含论文、教程、Jupyter notebooks和完整课程，理论结合实践
- 紧跟技术趋势：覆盖ChatGPT、OpenAI、LLMs等主流技术栈，涵盖generative-ai和deep-learning领域
- MDX格式内容：使用现代化文档格式，便于阅读和集成到各类知识管理系统
- 多语言模型支持：不仅限于OpenAI，还涵盖各类LLMs和AI框架的工程实践

**适用场景**:
- AI开发者学习：个人开发者或企业工程师系统学习prompt工程和AI应用开发技能，从入门到精通
- 团队知识库建设：企业团队作为内部培训教材和知识参考，统一团队对prompt engineering的理解和实践标准
- AI产品研发：构建基于LLMs的应用时参考最佳实践，包括RAG系统优化、Agent设计等关键技术实现



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 150,020 |
| 语言 | HTML |
| Forks | 19,724 |
| Issues | 20 |
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
| Stars | 33,713 |
| 语言 | HTML |
| Forks | 5,382 |
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
| Stars | 89,353 |
| 语言 | TypeScript |
| Forks | 9,886 |
| Issues | 2,241 |
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
| Stars | 86,467 |
| 语言 | TypeScript |
| Forks | 8,685 |
| Issues | 1,624 |
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
| Stars | 126,941 |
| 语言 | JavaScript |
| Forks | 12,444 |
| Issues | 3 |
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
| Stars | 99,512 |
| 语言 | JavaScript |
| Forks | 7,447 |
| Issues | 201 |
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
| Stars | 166,547 |
| 语言 | Go |
| Forks | 13,005 |
| Issues | 173 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (62 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,849 |
| 语言 | Unknown |
| Forks | 32,644 |
| Issues | 124 |
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
| Stars | 259,893 |
| 语言 | TypeScript |
| Forks | 49,793 |
| Issues | 10,935 |
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
| Stars | 61,360 |
| 语言 | Python |
| Forks | 6,265 |
| Issues | 272 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,819 |
| 语言 | Python |
| Forks | 11,631 |
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
| Stars | 74,010 |
| 语言 | Python |
| Forks | 6,327 |
| Issues | 627 |
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
| Stars | 383,591 |
| 语言 | Python |
| Forks | 66,012 |
| Issues | 76 |
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
| Stars | 112,397 |
| 语言 | TypeScript |
| Forks | 5,668 |
| Issues | 301 |
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
| Stars | 100,364 |
| 语言 | TypeScript |
| Forks | 7,302 |
| Issues | 169 |
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
| Stars | 47,870 |
| 语言 | Go |
| Forks | 10,233 |
| Issues | 1,908 |
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
| Stars | 96,656 |
| 语言 | C++ |
| Forks | 15,226 |
| Issues | 1,193 |
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
| Stars | 59,518 |
| 语言 | Python |
| Forks | 1,609 |
| Issues | 34 |
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
| Stars | 28,931 |
| 语言 | TypeScript |
| Forks | 2,217 |
| Issues | 806 |
| 许可证 | MIT License |


### vinta/awesome-python

**描述**: An opinionated list of awesome Python frameworks, libraries, software and resources.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 285,569 |
| 语言 | Python |
| Forks | 27,289 |
| Issues | 17 |
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
| Stars | 218,326 |
| 语言 | Python |
| Forks | 50,125 |
| Issues | 926 |
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
| Stars | 85,125 |
| 语言 | Python |
| Forks | 36,897 |
| Issues | 3,453 |
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
| Stars | 77,688 |
| 语言 | Python |
| Forks | 45,259 |
| Issues | 1,280 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,713 |
| 语言 | Python |
| Forks | 16,709 |
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
| Stars | 437,776 |
| 语言 | TypeScript |
| Forks | 43,514 |
| Issues | 294 |
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
| Stars | 350,175 |
| 语言 | TypeScript |
| Forks | 43,733 |
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
| Stars | 117,992 |
| 语言 | TypeScript |
| Forks | 12,724 |
| Issues | 2,841 |
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
| Stars | 108,013 |
| 语言 | TypeScript |
| Forks | 13,253 |
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
| Stars | 107,703 |
| 语言 | TypeScript |
| Forks | 8,003 |
| Issues | 1,768 |
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
| Stars | 97,665 |
| 语言 | TypeScript |
| Forks | 54,548 |
| Issues | 1,379 |
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
| Stars | 94,020 |
| 语言 | TypeScript |
| Forks | 5,006 |
| Issues | 650 |
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
| Stars | 93,909 |
| 语言 | TypeScript |
| Forks | 5,097 |
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
| Stars | 82,905 |
| 语言 | TypeScript |
| Forks | 7,570 |
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
| Stars | 80,102 |
| 语言 | TypeScript |
| Forks | 9,754 |
| Issues | 415 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,582 |
| 语言 | TypeScript |
| Forks | 7,872 |
| Issues | 638 |
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
| Stars | 243,603 |
| 语言 | JavaScript |
| Forks | 50,650 |
| Issues | 1,139 |
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
| Stars | 138,147 |
| 语言 | JavaScript |
| Forks | 30,553 |
| Issues | 3,402 |
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
| Stars | 116,063 |
| 语言 | JavaScript |
| Forks | 34,929 |
| Issues | 2,493 |
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
| Stars | 111,168 |
| 语言 | JavaScript |
| Forks | 36,276 |
| Issues | 600 |
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
| Stars | 108,579 |
| 语言 | JavaScript |
| Forks | 11,538 |
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
| Stars | 98,003 |
| 语言 | JavaScript |
| Forks | 32,716 |
| Issues | 1,728 |
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
| Stars | 95,375 |
| 语言 | JavaScript |
| Forks | 15,192 |
| Issues | 69 |
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
| Stars | 85,989 |
| 语言 | JavaScript |
| Forks | 4,790 |
| Issues | 972 |
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
| Stars | 78,603 |
| 语言 | JavaScript |
| Forks | 31,245 |
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
| Stars | 70,663 |
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
| Stars | 67,211 |
| 语言 | JavaScript |
| Forks | 11,993 |
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
| Stars | 66,260 |
| 语言 | JavaScript |
| Forks | 9,183 |
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
| Stars | 66,018 |
| 语言 | JavaScript |
| Forks | 9,301 |
| Issues | 205 |
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
| Stars | 59,850 |
| 语言 | JavaScript |
| Forks | 20,476 |
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
| Stars | 59,654 |
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
| Stars | 57,394 |
| 语言 | JavaScript |
| Forks | 12,311 |
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
| Stars | 132,879 |
| 语言 | Go |
| Forks | 18,840 |
| Issues | 9,821 |
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
| Stars | 104,871 |
| 语言 | Go |
| Forks | 14,917 |
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
| Stars | 86,906 |
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
| Stars | 80,510 |
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
| Stars | 68,711 |
| 语言 | Go |
| Forks | 3,214 |
| Issues | 17 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,847 |
| 语言 | Go |
| Forks | 4,942 |
| Issues | 1,124 |
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
| Stars | 50,894 |
| 语言 | Go |
| Forks | 21,827 |
| Issues | 385 |
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
| Stars | 49,100 |
| 语言 | Go |
| Forks | 7,983 |
| Issues | 587 |
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
| Stars | 45,210 |
| 语言 | Go |
| Forks | 3,742 |
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
| Stars | 144,742 |
| 语言 | Python |
| Forks | 11,162 |
| Issues | 282 |
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
| Stars | 139,783 |
| 语言 | Python |
| Forks | 10,599 |
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
| Stars | 84,971 |
| 语言 | Python |
| Forks | 7,146 |
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
| Stars | 195,721 |
| 语言 | JavaScript |
| Forks | 31,118 |
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
| Stars | 148,086 |
| 语言 | JavaScript |
| Forks | 26,768 |
| Issues | 185 |
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
| Stars | 76,391 |
| 语言 | JavaScript |
| Forks | 12,245 |
| Issues | 316 |
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
| Stars | 66,735 |
| 语言 | JavaScript |
| Forks | 4,465 |
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
| Stars | 61,904 |
| 语言 | JavaScript |
| Forks | 3,967 |
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
| Stars | 61,580 |
| 语言 | JavaScript |
| Forks | 7,126 |
| Issues | 121 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |
