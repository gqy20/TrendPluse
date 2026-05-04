# 项目发现报告 (2026-05-04)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 121 |
| 去重移除 | 32 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 14 |
| 💬 LLM 界面 | 21 |
| 🧠 机器学习框架 | 8 |
| 🛠️ 开发工具 | 16 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
| 📁 其他 | 68 |

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
| Stars | 135,489 |
| 语言 | Python |
| Forks | 19,278 |
| Issues | 336 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，适合需要自托管、注重数据隐私的企业和开发者快速搭建私有化 AI 应用。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAI 兼容 API 等多种 LLM 服务，灵活性高
- RAG 检索增强生成：内置知识库功能，支持文档导入和向量检索，提升回答准确性
- MCP (Model Context Protocol)：支持模型上下文协议，实现高级 AI 功能扩展
- 自托管部署：完全开源可私有部署，数据不离开本地，满足企业级安全合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、参数配置等丰富功能

**适用场景**:
- 企业内部 AI 助手：企业可私有化部署，搭建内部知识库问答系统，处理敏感文档和数据
- 个人开发者 AI 实验平台：开发者可快速本地部署，体验和测试不同 LLM 模型，降低 AI 开发门槛
- 隐私敏感场景：医疗、金融、法律等行业需要本地化部署 AI 应用，确保数据合规



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,531 |
| 语言 | Python |
| Forks | 20,139 |
| Issues | 8,150 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名AI研究团队 NousResearch 开发的智能代理框架，支持 Anthropic Claude、OpenAI GPT 等多模型集成，拥有超过13万 Stars 的高人气，采用 MIT 许可证开源，适合构建企业级 AI 应用。

**技术亮点**:
- 支持多模型集成：兼容 Claude、GPT-4、Codex 等主流大语言模型
- 模块化架构设计：便于扩展和定制不同类型的 AI 代理
- MIT 开源许可证：可自由用于商业项目
- 活跃的社区生态：13万+ Stars，拥有丰富的社区资源
- 专注于 AI Agent 场景：支持代码生成、对话交互等多种代理能力

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、自动化工作流等商业解决方案
- 个人开发者快速原型：利用开源框架快速搭建 AI 代理应用
- 多模型集成研究：探索不同 LLM 在代理任务中的协作与优化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,222 |
| 语言 | JavaScript |
| Forks | 26,845 |
| Issues | 153 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数高达 17 万+ 的热门 AI Agent 性能优化框架，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 等创新机制显著提升 AI agent 的开发效率和智能化水平，是目前最完善的 AI 代码助手增强方案之一。

**技术亮点**:
- 多平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供统一的优化接口
- Skills 系统：模块化的技能库机制，让 AI agent 快速获取特定领域的专业能力
- Instincts 本能系统：通过内置的本能反应机制，提升 AI agent 的决策速度和准确性
- Memory 持久记忆：支持长期上下文记忆，使 AI agent 能够跨会话学习和积累经验
- Security 安全模块：内置多层安全防护，确保 AI 操作的可控性和数据安全

**适用场景**:
- 企业级 AI 开发平台：团队可基于此框架构建统一的 AI 辅助开发规范和安全策略，提升整体开发效率
- 个人开发者增强：个人开发者可快速为现有的 AI 编程工具添加自定义技能和记忆能力，打造个性化的 AI 助手
- AI Agent 研究与实验：研究人员可在此框架基础上进行 AI Agent 能力扩展、安全机制优化等方向的实验和研究



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,042 |
| 语言 | Go |
| Forks | 4,052 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是企业部署私有化 AI 的理想选择，提供 OpenAI 兼容 API 接口，支持本地运行 100+ 开源模型（LLM、图像、语音等），无需 GPU 即可部署完整 AI 应用栈，大幅降低成本并保障数据隐私。

**技术亮点**:
- 多模型统一推理引擎：支持 LLMs、语音合成(TTS)、语音识别、图像生成、音乐生成、目标检测等多种模型类型的统一推理
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有 OpenAI 应用可零成本迁移到本地部署
- 去中心化架构：集成 libp2p 协议支持，支持分布式和去中心化部署模式
- 零 GPU 依赖：可在 CPU 环境下运行模型，降低硬件门槛，减少 AI 部署成本
- Go 语言高性能：采用 Go 语言开发，具有优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有严格要求的企业，在本地运行 AI 模型处理敏感数据
- 个人开发者/小团队：资源有限但需要部署 AI 能力的开发者，无需购买昂贵 GPU 即可运行 AI 模型
- 离线/边缘计算场景：需要在没有网络连接的环境（如工厂、医疗设备、IoT 边缘节点）中运行 AI 推理



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,024 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 757 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度活跃的 AI Agent 开发平台，拥有 76k+ Stars，专注于多智能体协作和 Agent 团队编排，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合构建企业级 AI 工作流和智能助手应用。

**技术亮点**:
- 多模型统一接入层：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型的统一接口封装，降低多模型切换成本
- 多智能体协作框架：提供 Agent Team 设计能力，支持多 Agent 协同工作、任务分解与结果聚合
- Model Context Protocol (MCP) 原生支持：标准化 AI 模型与外部工具/数据的连接协议，便于扩展生态集成
- TypeScript 全栈架构：前后端均使用 TypeScript 开发，保证类型安全和代码可维护性
- 知识库增强系统：内置 RAG 能力，支持向量检索和知识管理，提升 Agent 问答准确率

**适用场景**:
- 企业智能助手：构建支持多部门 Agent 协作的企业知识问答和业务流程自动化系统
- 个人 AI 工作站：个人开发者利用 Agent 团队进行代码开发、内容创作、数据分析等任务
- 垂直领域 AI 应用：基于 MCP 协议快速集成第三方工具（如数据库、API、云服务），构建金融、医疗、教育等行业的智能解决方案



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,948 |
| 语言 | TypeScript |
| Forks | 6,177 |
| Issues | 66 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的长程记忆系统，解决了 AI 编码助手无法跨会话保持上下文的核心痛点。通过自动捕获、压缩和检索历史操作，实现真正的持续学习体验，71,948 Stars 已充分验证其巨大的实用价值和社区认可度。

**技术亮点**:
- 智能压缩引擎：利用 Claude Agent SDK 对历史会话进行 AI 压缩，提取关键信息而非简单存储
- RAG + 向量检索架构：基于 ChromaDB 构建向量数据库，结合 Embeddings 技术实现语义级记忆检索
- 多存储层设计：结合 SQLite 本地持久化与向量数据库，实现结构化数据与语义记忆的双轨存储
- 插件化无缝集成：作为 Claude Code 官方插件运行，无需切换工作流
- 长期记忆能力：突破单次会话的上下文限制，支持跨天、周、月的项目连续性

**适用场景**:
- 复杂长期项目开发：如大型前端重构、后端系统迁移等跨周期任务，避免每次重新解释项目背景
- 个人开发者知识积累：构建个人代码记忆库，让 AI 助手记住你的代码风格和架构决策



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,917 |
| 语言 | Python |
| Forks | 8,662 |
| Issues | 995 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效大模型微调框架，支持100+ LLMs和VLMs，集成LoRA、QLoRA、RLHF等多种微调方法，让研究者和开发者能够以最低门槛完成大模型定制化训练。

**技术亮点**:
- 支持100+开源大语言模型和视觉语言模型统一微调，覆盖Llama3、Qwen、Gemma、DeepSeek等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、RLHF等，大幅降低显存占用和计算成本
- 内置模型量化支持，支持GPTQ、AWQ等多种量化方式，可在消费级GPU上微调百亿参数模型
- 提供Web界面和命令行双模式，开箱即用，无需复杂配置即可启动训练
- 模块化架构设计，支持自定义数据集、训练策略和评估指标，便于二次开发

**适用场景**:
- 企业垂直场景定制：基于LlamaFactory快速微调领域大模型，应用于客服、文档分析、代码生成等业务场景
- 学术研究与算法验证：低成本实验LoRA、RLHF等微调方法，支持快速迭代和新算法探索
- 个人开发者模型优化：在个人GPU上微调开源模型，打造个性化AI助手或特定任务模型



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,935 |
| 语言 | HTML |
| Forks | 5,066 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,003 |
| 语言 | Python |
| Forks | 10,043 |
| Issues | 356 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,071 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 16 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,498 |
| 语言 | Python |
| Forks | 5,138 |
| Issues | 101 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,096 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 71 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, self-learning swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 41,038 |
| 语言 | TypeScript |
| Forks | 4,598 |
| Issues | 506 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,050 |
| 语言 | TypeScript |
| Forks | 7,249 |
| Issues | 305 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,506 |
| 语言 | JavaScript |
| Forks | 6,425 |
| Issues | 343 |
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
| Stars | 72,614 |
| 语言 | Python |
| Forks | 9,181 |
| Issues | 421 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,757 |
| 语言 | TypeScript |
| Forks | 4,526 |
| Issues | 681 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,700 |
| 语言 | Python |
| Forks | 16,062 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### browser-use/browser-use

**描述**: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,070 |
| 语言 | Python |
| Forks | 10,457 |
| Issues | 235 |
| Topics | ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,528 |
| 语言 | TypeScript |
| Forks | 24,259 |
| Issues | 830 |
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
| Stars | 186,682 |
| 语言 | TypeScript |
| Forks | 57,344 |
| Issues | 1,457 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 155,396 |
| 语言 | Java |
| Forks | 46,156 |
| Issues | 62 |
| Topics | agent, context-engineering, interview, java, jvm, mcp, mysql, redis, redisson, skills, spring, system, system-design |
| 许可证 | Apache License 2.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,681 |
| 语言 | Python |
| Forks | 8,903 |
| Issues | 950 |
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
| Stars | 60,496 |
| 语言 | Jupyter Notebook |
| Forks | 20,480 |
| Issues | 4 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,913 |
| 语言 | Python |
| Forks | 6,268 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,055 |
| 语言 | TypeScript |
| Forks | 9,527 |
| Issues | 114 |
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
| Stars | 59,014 |
| 语言 | Rust |
| Forks | 3,841 |
| Issues | 725 |
| Topics | ai-tools, claude-code, codex, desktop-app, hermes, hermes-agent, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (14 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,489 |
| 语言 | Python |
| Forks | 19,278 |
| Issues | 336 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，适合需要自托管、注重数据隐私的企业和开发者快速搭建私有化 AI 应用。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAI 兼容 API 等多种 LLM 服务，灵活性高
- RAG 检索增强生成：内置知识库功能，支持文档导入和向量检索，提升回答准确性
- MCP (Model Context Protocol)：支持模型上下文协议，实现高级 AI 功能扩展
- 自托管部署：完全开源可私有部署，数据不离开本地，满足企业级安全合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、参数配置等丰富功能

**适用场景**:
- 企业内部 AI 助手：企业可私有化部署，搭建内部知识库问答系统，处理敏感文档和数据
- 个人开发者 AI 实验平台：开发者可快速本地部署，体验和测试不同 LLM 模型，降低 AI 开发门槛
- 隐私敏感场景：医疗、金融、法律等行业需要本地化部署 AI 应用，确保数据合规



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,024 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 757 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度活跃的 AI Agent 开发平台，拥有 76k+ Stars，专注于多智能体协作和 Agent 团队编排，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合构建企业级 AI 工作流和智能助手应用。

**技术亮点**:
- 多模型统一接入层：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型的统一接口封装，降低多模型切换成本
- 多智能体协作框架：提供 Agent Team 设计能力，支持多 Agent 协同工作、任务分解与结果聚合
- Model Context Protocol (MCP) 原生支持：标准化 AI 模型与外部工具/数据的连接协议，便于扩展生态集成
- TypeScript 全栈架构：前后端均使用 TypeScript 开发，保证类型安全和代码可维护性
- 知识库增强系统：内置 RAG 能力，支持向量检索和知识管理，提升 Agent 问答准确率

**适用场景**:
- 企业智能助手：构建支持多部门 Agent 协作的企业知识问答和业务流程自动化系统
- 个人 AI 工作站：个人开发者利用 Agent 团队进行代码开发、内容创作、数据分析等任务
- 垂直领域 AI 应用：基于 MCP 协议快速集成第三方工具（如数据库、API、云服务），构建金融、医疗、教育等行业的智能解决方案



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,948 |
| 语言 | TypeScript |
| Forks | 6,177 |
| Issues | 66 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的长程记忆系统，解决了 AI 编码助手无法跨会话保持上下文的核心痛点。通过自动捕获、压缩和检索历史操作，实现真正的持续学习体验，71,948 Stars 已充分验证其巨大的实用价值和社区认可度。

**技术亮点**:
- 智能压缩引擎：利用 Claude Agent SDK 对历史会话进行 AI 压缩，提取关键信息而非简单存储
- RAG + 向量检索架构：基于 ChromaDB 构建向量数据库，结合 Embeddings 技术实现语义级记忆检索
- 多存储层设计：结合 SQLite 本地持久化与向量数据库，实现结构化数据与语义记忆的双轨存储
- 插件化无缝集成：作为 Claude Code 官方插件运行，无需切换工作流
- 长期记忆能力：突破单次会话的上下文限制，支持跨天、周、月的项目连续性

**适用场景**:
- 复杂长期项目开发：如大型前端重构、后端系统迁移等跨周期任务，避免每次重新解释项目背景
- 个人开发者知识积累：构建个人代码记忆库，让 AI 助手记住你的代码风格和架构决策



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,071 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 16 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,498 |
| 语言 | Python |
| Forks | 5,138 |
| Issues | 101 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### mindsdb/mindsdb

**描述**: AI Data Vault - A query engine for AI Agents to securely query data from any datasource

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 39,096 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 71 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,839 |
| 语言 | TypeScript |
| Forks | 12,291 |
| Issues | 995 |
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
| Stars | 59,506 |
| 语言 | JavaScript |
| Forks | 6,425 |
| Issues | 343 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agent & RAG apps you can actually run — clone, customize, ship.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 108,700 |
| 语言 | Python |
| Forks | 16,062 |
| Issues | 4 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,053 |
| 语言 | Python |
| Forks | 10,363 |
| Issues | 204 |
| Topics | ai4science, chineseocr, document-parsing, document-translation, kie, ocr, paddleocr-vl, pdf-extractor-rag, pdf-parser, pdf2markdown, pp-ocr, pp-structure, rag |
| 许可证 | Apache License 2.0 |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,528 |
| 语言 | TypeScript |
| Forks | 24,259 |
| Issues | 830 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### safishamsi/graphify

**描述**: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,590 |
| 语言 | Python |
| Forks | 4,658 |
| Issues | 218 |
| Topics | antigravity, claude-code, codex, gemini, graphrag, knowledge-graph, leiden, openclaw, rag, skills, tree-sitter |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,108 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,070 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### HKUDS/LightRAG

**描述**: [EMNLP2025] "LightRAG: Simple and Fast Retrieval-Augmented Generation"

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 34,734 |
| 语言 | Python |
| Forks | 4,920 |
| Issues | 230 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


## 💬 LLM 界面 (21 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,489 |
| 语言 | Python |
| Forks | 19,278 |
| Issues | 336 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是一个功能完备的开源 AI 界面，支持 Ollama、OpenAI API 等多种 LLM 后端，提供 RAG 和 MCP 等高级功能，适合需要自托管、注重数据隐私的企业和开发者快速搭建私有化 AI 应用。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、OpenAI 兼容 API 等多种 LLM 服务，灵活性高
- RAG 检索增强生成：内置知识库功能，支持文档导入和向量检索，提升回答准确性
- MCP (Model Context Protocol)：支持模型上下文协议，实现高级 AI 功能扩展
- 自托管部署：完全开源可私有部署，数据不离开本地，满足企业级安全合规要求
- 现代化 Web UI：提供直观的图形界面，支持对话管理、模型切换、参数配置等丰富功能

**适用场景**:
- 企业内部 AI 助手：企业可私有化部署，搭建内部知识库问答系统，处理敏感文档和数据
- 个人开发者 AI 实验平台：开发者可快速本地部署，体验和测试不同 LLM 模型，降低 AI 开发门槛
- 隐私敏感场景：医疗、金融、法律等行业需要本地化部署 AI 应用，确保数据合规



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,531 |
| 语言 | Python |
| Forks | 20,139 |
| Issues | 8,150 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名AI研究团队 NousResearch 开发的智能代理框架，支持 Anthropic Claude、OpenAI GPT 等多模型集成，拥有超过13万 Stars 的高人气，采用 MIT 许可证开源，适合构建企业级 AI 应用。

**技术亮点**:
- 支持多模型集成：兼容 Claude、GPT-4、Codex 等主流大语言模型
- 模块化架构设计：便于扩展和定制不同类型的 AI 代理
- MIT 开源许可证：可自由用于商业项目
- 活跃的社区生态：13万+ Stars，拥有丰富的社区资源
- 专注于 AI Agent 场景：支持代码生成、对话交互等多种代理能力

**适用场景**:
- 企业级 AI 应用开发：构建智能客服、自动化工作流等商业解决方案
- 个人开发者快速原型：利用开源框架快速搭建 AI 代理应用
- 多模型集成研究：探索不同 LLM 在代理任务中的协作与优化



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,222 |
| 语言 | JavaScript |
| Forks | 26,845 |
| Issues | 153 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数高达 17 万+ 的热门 AI Agent 性能优化框架，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 等创新机制显著提升 AI agent 的开发效率和智能化水平，是目前最完善的 AI 代码助手增强方案之一。

**技术亮点**:
- 多平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供统一的优化接口
- Skills 系统：模块化的技能库机制，让 AI agent 快速获取特定领域的专业能力
- Instincts 本能系统：通过内置的本能反应机制，提升 AI agent 的决策速度和准确性
- Memory 持久记忆：支持长期上下文记忆，使 AI agent 能够跨会话学习和积累经验
- Security 安全模块：内置多层安全防护，确保 AI 操作的可控性和数据安全

**适用场景**:
- 企业级 AI 开发平台：团队可基于此框架构建统一的 AI 辅助开发规范和安全策略，提升整体开发效率
- 个人开发者增强：个人开发者可快速为现有的 AI 编程工具添加自定义技能和记忆能力，打造个性化的 AI 助手
- AI Agent 研究与实验：研究人员可在此框架基础上进行 AI Agent 能力扩展、安全机制优化等方向的实验和研究



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,024 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 757 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个高度活跃的 AI Agent 开发平台，拥有 76k+ Stars，专注于多智能体协作和 Agent 团队编排，支持 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，适合构建企业级 AI 工作流和智能助手应用。

**技术亮点**:
- 多模型统一接入层：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型的统一接口封装，降低多模型切换成本
- 多智能体协作框架：提供 Agent Team 设计能力，支持多 Agent 协同工作、任务分解与结果聚合
- Model Context Protocol (MCP) 原生支持：标准化 AI 模型与外部工具/数据的连接协议，便于扩展生态集成
- TypeScript 全栈架构：前后端均使用 TypeScript 开发，保证类型安全和代码可维护性
- 知识库增强系统：内置 RAG 能力，支持向量检索和知识管理，提升 Agent 问答准确率

**适用场景**:
- 企业智能助手：构建支持多部门 Agent 协作的企业知识问答和业务流程自动化系统
- 个人 AI 工作站：个人开发者利用 Agent 团队进行代码开发、内容创作、数据分析等任务
- 垂直领域 AI 应用：基于 MCP 协议快速集成第三方工具（如数据库、API、云服务），构建金融、医疗、教育等行业的智能解决方案



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,948 |
| 语言 | TypeScript |
| Forks | 6,177 |
| Issues | 66 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个为 Claude Code 打造的长程记忆系统，解决了 AI 编码助手无法跨会话保持上下文的核心痛点。通过自动捕获、压缩和检索历史操作，实现真正的持续学习体验，71,948 Stars 已充分验证其巨大的实用价值和社区认可度。

**技术亮点**:
- 智能压缩引擎：利用 Claude Agent SDK 对历史会话进行 AI 压缩，提取关键信息而非简单存储
- RAG + 向量检索架构：基于 ChromaDB 构建向量数据库，结合 Embeddings 技术实现语义级记忆检索
- 多存储层设计：结合 SQLite 本地持久化与向量数据库，实现结构化数据与语义记忆的双轨存储
- 插件化无缝集成：作为 Claude Code 官方插件运行，无需切换工作流
- 长期记忆能力：突破单次会话的上下文限制，支持跨天、周、月的项目连续性

**适用场景**:
- 复杂长期项目开发：如大型前端重构、后端系统迁移等跨周期任务，避免每次重新解释项目背景
- 个人开发者知识积累：构建个人代码记忆库，让 AI 助手记住你的代码风格和架构决策



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,538 |
| 语言 | HTML |
| Forks | 21,071 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最全面、最活跃的开源提示词分享平台，拥有超过16万stars的庞大社区支持，支持ChatGPT/Claude/Gemini等多模型，企业可完全自托管以确保数据隐私，适合AI应用开发和团队协作。

**技术亮点**:
- 基于Next.js + TypeScript构建，采用现代化全栈架构，性能和可维护性优秀
- 支持多AI模型集成（ChatGPT、Claude、Gemini等），提示词跨平台通用
- 开源可自托管部署，企业级隐私保护，无需担心数据泄露
- 社区驱动的提示词收集与评审机制，内容质量有保障
- 完整的提示词管理功能，支持收藏、分类和分享协作

**适用场景**:
- 企业自建AI助手平台：金融机构、医疗健康等隐私敏感行业可完全私有化部署，保护内部数据安全
- AI应用开发者参考学习：快速获取高质量提示词范本，加速产品开发和prompt工程优化
- 团队知识管理与协作：团队成员共享和复用优质提示词，提升AI使用效率和一致性



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,705 |
| 语言 | Python |
| Forks | 2,914 |
| Issues | 177 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

一个极具创意的 token 优化方案，通过"穴居人语言"风格将 LLM token 消耗降低 65%，在保持功能完整性的同时显著降低成本，适合高频使用 Claude Code 的开发者。

**技术亮点**:
- 创新的提示工程方法：通过独特的语言风格压缩技术实现 token 用量优化
- 深度集成 Claude Code 平台：作为官方 skill 直接在开发工作流中无缝使用
- 显著的成本效益：官方宣称可节省 65% 的 token 消耗
- 简洁高效的方案：基于少即是多的设计理念，化繁为简
- 开源 MIT 许可证：允许自由使用和二次开发

**适用场景**:
- 企业级 LLM 应用成本优化：对于需要频繁调用 Claude API 的团队，可显著降低 API 使用成本
- 个人开发者效率提升：日常使用 Claude Code 时减少 token 消耗，提高对话效率
- 资源受限环境：在 token 限制严格的场景下，帮助完成更复杂的任务



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,935 |
| 语言 | HTML |
| Forks | 5,066 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,003 |
| 语言 | Python |
| Forks | 10,043 |
| Issues | 356 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,506 |
| 语言 | JavaScript |
| Forks | 6,425 |
| Issues | 343 |
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
| Stars | 72,614 |
| 语言 | Python |
| Forks | 9,181 |
| Issues | 421 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,757 |
| 语言 | TypeScript |
| Forks | 4,526 |
| Issues | 681 |
| Topics | ai, ai-agents, amp, anthropic, chatgpt, claude, claude-code, claude-skills, cursor, gemini, ide, openai, opencode, orchestration, tui, typescript |
| 许可证 | Other |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,528 |
| 语言 | TypeScript |
| Forks | 24,259 |
| Issues | 830 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,012 |
| 语言 | Python |
| Forks | 16,394 |
| Issues | 4,766 |
| Topics | amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving, model-serving, moe, openai, pytorch, qwen, qwen3, tpu, transformer |
| 许可证 | Apache License 2.0 |


### langflow-ai/langflow

**描述**: Langflow is a powerful tool for building and deploying AI-powered agents and workflows.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 147,681 |
| 语言 | Python |
| Forks | 8,903 |
| Issues | 950 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,913 |
| 语言 | Python |
| Forks | 6,268 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,679 |
| 语言 | Go |
| Forks | 15,974 |
| Issues | 3,160 |
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
| Stars | 91,910 |
| 语言 | Jupyter Notebook |
| Forks | 14,193 |
| Issues | 8 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,055 |
| 语言 | TypeScript |
| Forks | 9,527 |
| Issues | 114 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### tw93/Pake

**描述**: 🤱🏻 Turn any webpage into a desktop app with one command.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,420 |
| 语言 | Rust |
| Forks | 9,697 |
| Issues | 3 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
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
| Stars | 120,312 |
| 语言 | Python |
| Forks | 8,016 |
| Issues | 624 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (8 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,917 |
| 语言 | Python |
| Forks | 8,662 |
| Issues | 995 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个统一的高效大模型微调框架，支持100+ LLMs和VLMs，集成LoRA、QLoRA、RLHF等多种微调方法，让研究者和开发者能够以最低门槛完成大模型定制化训练。

**技术亮点**:
- 支持100+开源大语言模型和视觉语言模型统一微调，覆盖Llama3、Qwen、Gemma、DeepSeek等主流模型
- 集成多种高效微调技术：LoRA、QLoRA、PEFT、RLHF等，大幅降低显存占用和计算成本
- 内置模型量化支持，支持GPTQ、AWQ等多种量化方式，可在消费级GPU上微调百亿参数模型
- 提供Web界面和命令行双模式，开箱即用，无需复杂配置即可启动训练
- 模块化架构设计，支持自定义数据集、训练策略和评估指标，便于二次开发

**适用场景**:
- 企业垂直场景定制：基于LlamaFactory快速微调领域大模型，应用于客服、文档分析、代码生成等业务场景
- 学术研究与算法验证：低成本实验LoRA、RLHF等微调方法，支持快速迭代和新算法探索
- 个人开发者模型优化：在个人GPU上微调开源模型，打造个性化AI助手或特定任务模型



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,994 |
| 语言 | Python |
| Forks | 6,705 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是最全面的开源金融数据平台之一，提供从股票、加密货币到期权、固定收益的一站式数据访问能力，并且原生集成AI/ML支持，特别适合需要快速构建量化策略或金融分析工具的团队。

**技术亮点**:
- 统一数据接口层：封装多个数据源（Yahoo Finance、CoinGecko、FRED等），提供一致的API调用体验，大幅降低数据获取复杂度
- 丰富的金融分析工具：内置技术指标、蜡烛图分析、期权定价模型（Greeks、Black-Scholes）等常用分析功能
- AI代理原生支持：提供专门面向AI代理的数据访问接口，支持LLM驱动的金融分析和自动化交易决策
- 模块化架构设计：支持功能扩展和自定义数据源集成，便于企业级定制开发
- 完整的Python生态系统集成：与pandas、numpy、matplotlib等主流数据科学生态无缝对接

**适用场景**:
- 量化投资研究：量化研究员快速获取多资产数据、进行策略回测和因子分析
- 金融数据分析平台：构建面向分析师的一站式数据仪表板和报告生成系统
- AI驱动的金融应用：开发基于大语言模型的智能投顾、财报分析、风险预警等AI应用



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,538 |
| 语言 | HTML |
| Forks | 21,071 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最全面、最活跃的开源提示词分享平台，拥有超过16万stars的庞大社区支持，支持ChatGPT/Claude/Gemini等多模型，企业可完全自托管以确保数据隐私，适合AI应用开发和团队协作。

**技术亮点**:
- 基于Next.js + TypeScript构建，采用现代化全栈架构，性能和可维护性优秀
- 支持多AI模型集成（ChatGPT、Claude、Gemini等），提示词跨平台通用
- 开源可自托管部署，企业级隐私保护，无需担心数据泄露
- 社区驱动的提示词收集与评审机制，内容质量有保障
- 完整的提示词管理功能，支持收藏、分类和分享协作

**适用场景**:
- 企业自建AI助手平台：金融机构、医疗健康等隐私敏感行业可完全私有化部署，保护内部数据安全
- AI应用开发者参考学习：快速获取高质量提示词范本，加速产品开发和prompt工程优化
- 团队知识管理与协作：团队成员共享和复用优质提示词，提升AI使用效率和一致性



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,239 |
| 语言 | Python |
| Forks | 33,103 |
| Issues | 2,348 |
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
| Stars | 79,012 |
| 语言 | Python |
| Forks | 16,394 |
| Issues | 4,766 |
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
| Stars | 111,323 |
| 语言 | Python |
| Forks | 13,003 |
| Issues | 4,008 |
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
| Stars | 99,605 |
| 语言 | Python |
| Forks | 27,651 |
| Issues | 18,511 |
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
| Stars | 91,910 |
| 语言 | Jupyter Notebook |
| Forks | 14,193 |
| Issues | 8 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


## 🛠️ 开发工具 (16 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 173,222 |
| 语言 | JavaScript |
| Forks | 26,845 |
| Issues | 153 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个 Star 数高达 17 万+ 的热门 AI Agent 性能优化框架，支持 Claude Code、Codex、Cursor 等主流 AI 编程工具，通过 Skills/Instincts/Memory 等创新机制显著提升 AI agent 的开发效率和智能化水平，是目前最完善的 AI 代码助手增强方案之一。

**技术亮点**:
- 多平台兼容：支持 Claude Code、Codex、Opencode、Cursor 等主流 AI 编程工具，提供统一的优化接口
- Skills 系统：模块化的技能库机制，让 AI agent 快速获取特定领域的专业能力
- Instincts 本能系统：通过内置的本能反应机制，提升 AI agent 的决策速度和准确性
- Memory 持久记忆：支持长期上下文记忆，使 AI agent 能够跨会话学习和积累经验
- Security 安全模块：内置多层安全防护，确保 AI 操作的可控性和数据安全

**适用场景**:
- 企业级 AI 开发平台：团队可基于此框架构建统一的 AI 辅助开发规范和安全策略，提升整体开发效率
- 个人开发者增强：个人开发者可快速为现有的 AI 编程工具添加自定义技能和记忆能力，打造个性化的 AI 助手
- AI Agent 研究与实验：研究人员可在此框架基础上进行 AI Agent 能力扩展、安全机制优化等方向的实验和研究



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,042 |
| 语言 | Go |
| Forks | 4,052 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是企业部署私有化 AI 的理想选择，提供 OpenAI 兼容 API 接口，支持本地运行 100+ 开源模型（LLM、图像、语音等），无需 GPU 即可部署完整 AI 应用栈，大幅降低成本并保障数据隐私。

**技术亮点**:
- 多模型统一推理引擎：支持 LLMs、语音合成(TTS)、语音识别、图像生成、音乐生成、目标检测等多种模型类型的统一推理
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有 OpenAI 应用可零成本迁移到本地部署
- 去中心化架构：集成 libp2p 协议支持，支持分布式和去中心化部署模式
- 零 GPU 依赖：可在 CPU 环境下运行模型，降低硬件门槛，减少 AI 部署成本
- Go 语言高性能：采用 Go 语言开发，具有优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有严格要求的企业，在本地运行 AI 模型处理敏感数据
- 个人开发者/小团队：资源有限但需要部署 AI 能力的开发者，无需购买昂贵 GPU 即可运行 AI 模型
- 离线/边缘计算场景：需要在没有网络连接的环境（如工厂、医疗设备、IoT 边缘节点）中运行 AI 推理



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,071 |
| 语言 | Java |
| Forks | 15,961 |
| Issues | 16 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,614 |
| 语言 | Python |
| Forks | 9,181 |
| Issues | 421 |
| Topics | agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm, openai |
| 许可证 | Other |


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,757 |
| 语言 | TypeScript |
| Forks | 4,526 |
| Issues | 681 |
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
| Stars | 186,682 |
| 语言 | TypeScript |
| Forks | 57,344 |
| Issues | 1,457 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,913 |
| 语言 | Python |
| Forks | 6,268 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 431,273 |
| 语言 | Python |
| Forks | 47,090 |
| Issues | 1,318 |
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
| Stars | 160,536 |
| 语言 | Python |
| Forks | 13,317 |
| Issues | 2,501 |
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
| Stars | 97,884 |
| 语言 | Python |
| Forks | 9,194 |
| Issues | 185 |
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
| Stars | 82,903 |
| 语言 | Python |
| Forks | 9,668 |
| Issues | 270 |
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
| Stars | 184,557 |
| 语言 | TypeScript |
| Forks | 39,656 |
| Issues | 17,119 |
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
| Stars | 94,233 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 304 |
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
| Stars | 79,101 |
| 语言 | TypeScript |
| Forks | 5,851 |
| Issues | 701 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,001 |
| 语言 | Go |
| Forks | 2,798 |
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
| Stars | 77,407 |
| 语言 | Go |
| Forks | 2,810 |
| Issues | 953 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (15 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 55,757 |
| 语言 | TypeScript |
| Forks | 4,526 |
| Issues | 681 |
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
| Stars | 186,682 |
| 语言 | TypeScript |
| Forks | 57,344 |
| Issues | 1,457 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### ComposioHQ/awesome-claude-skills

**描述**: A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,913 |
| 语言 | Python |
| Forks | 6,268 |
| Issues | 571 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,683 |
| 语言 | Go |
| Forks | 10,332 |
| Issues | 241 |
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
| Stars | 122,065 |
| 语言 | Go |
| Forks | 42,989 |
| Issues | 2,685 |
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
| Stars | 71,540 |
| 语言 | Go |
| Forks | 18,924 |
| Issues | 3,814 |
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
| Stars | 55,356 |
| 语言 | Go |
| Forks | 6,656 |
| Issues | 2,777 |
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
| Stars | 47,511 |
| 语言 | Go |
| Forks | 5,056 |
| Issues | 982 |
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
| Stars | 94,233 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 304 |
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
| Stars | 78,175 |
| 语言 | TypeScript |
| Forks | 6,840 |
| Issues | 427 |
| Topics | docker, hacktoberfest, java, pdf, pdf-converter, pdf-editor, pdf-manipulation, pdf-merger, pdf-ocr, pdf-tools, pdf-web-apps, pdfmerger, self-hosted |
| 许可证 | Other |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,197 |
| 语言 | JavaScript |
| Forks | 7,766 |
| Issues | 731 |
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
| Stars | 70,158 |
| 语言 | Go |
| Forks | 1,918 |
| Issues | 325 |
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
| Stars | 62,975 |
| 语言 | Go |
| Forks | 5,955 |
| Issues | 784 |
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
| Stars | 59,360 |
| 语言 | Go |
| Forks | 4,328 |
| Issues | 23 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,859 |
| 语言 | Go |
| Forks | 7,472 |
| Issues | 81 |
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
| Stars | 86,197 |
| 语言 | JavaScript |
| Forks | 7,766 |
| Issues | 731 |
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
| Stars | 63,898 |
| 语言 | Go |
| Forks | 10,368 |
| Issues | 768 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (12 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,042 |
| 语言 | Go |
| Forks | 4,052 |
| Issues | 156 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是企业部署私有化 AI 的理想选择，提供 OpenAI 兼容 API 接口，支持本地运行 100+ 开源模型（LLM、图像、语音等），无需 GPU 即可部署完整 AI 应用栈，大幅降低成本并保障数据隐私。

**技术亮点**:
- 多模型统一推理引擎：支持 LLMs、语音合成(TTS)、语音识别、图像生成、音乐生成、目标检测等多种模型类型的统一推理
- OpenAI API 兼容：提供与 OpenAI API 完全兼容的接口，现有 OpenAI 应用可零成本迁移到本地部署
- 去中心化架构：集成 libp2p 协议支持，支持分布式和去中心化部署模式
- 零 GPU 依赖：可在 CPU 环境下运行模型，降低硬件门槛，减少 AI 部署成本
- Go 语言高性能：采用 Go 语言开发，具有优秀的并发处理能力和跨平台兼容性

**适用场景**:
- 企业私有化 AI 部署：适合对数据隐私有严格要求的企业，在本地运行 AI 模型处理敏感数据
- 个人开发者/小团队：资源有限但需要部署 AI 能力的开发者，无需购买昂贵 GPU 即可运行 AI 模型
- 离线/边缘计算场景：需要在没有网络连接的环境（如工厂、医疗设备、IoT 边缘节点）中运行 AI 推理



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 431,273 |
| 语言 | Python |
| Forks | 47,090 |
| Issues | 1,318 |
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
| Stars | 97,884 |
| 语言 | Python |
| Forks | 9,194 |
| Issues | 185 |
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
| Stars | 87,399 |
| 语言 | Python |
| Forks | 33,874 |
| Issues | 430 |
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
| Stars | 100,065 |
| 语言 | TypeScript |
| Forks | 27,209 |
| Issues | 1,146 |
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
| Stars | 79,101 |
| 语言 | TypeScript |
| Forks | 5,851 |
| Issues | 701 |
| Topics | api, api-client, api-rest, api-testing, developer-tools, graphql, http, http-client, pwa, rest, rest-api, spa, testing, testing-tools, tools, vue, vuejs, websocket |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,989 |
| 语言 | JavaScript |
| Forks | 23,231 |
| Issues | 209 |
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
| Forks | 10,203 |
| Issues | 369 |
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
| Stars | 51,840 |
| 语言 | JavaScript |
| Forks | 4,713 |
| Issues | 1,472 |
| Topics | angular, ast, css, flow, formatter, graphql, html, javascript, json, jsx, less, markdown, prettier, printer, scss, typescript, vue, yaml |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 72,087 |
| 语言 | Go |
| Forks | 4,713 |
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
| Stars | 58,125 |
| 语言 | Go |
| Forks | 3,341 |
| Issues | 18 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,440 |
| 语言 | Go |
| Forks | 8,595 |
| Issues | 683 |
| Topics | framework, gin, go, middleware, performance, router, server |
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
| Stars | 101,839 |
| 语言 | TypeScript |
| Forks | 12,291 |
| Issues | 995 |
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
| Stars | 59,506 |
| 语言 | JavaScript |
| Forks | 6,425 |
| Issues | 343 |
| Topics | ai-agents, custom-ai-agents, deepseek, kimi, llama3, llm, lmstudio, local-llm, localai, mcp, mcp-servers, moonshot, multimodal, no-code, ollama, qwen3, rag, vector-database, web-scraping |
| 许可证 | MIT License |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 44,108 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,070 |
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
| Stars | 51,683 |
| 语言 | Go |
| Forks | 10,332 |
| Issues | 241 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (8 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,538 |
| 语言 | HTML |
| Forks | 21,071 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是目前最全面、最活跃的开源提示词分享平台，拥有超过16万stars的庞大社区支持，支持ChatGPT/Claude/Gemini等多模型，企业可完全自托管以确保数据隐私，适合AI应用开发和团队协作。

**技术亮点**:
- 基于Next.js + TypeScript构建，采用现代化全栈架构，性能和可维护性优秀
- 支持多AI模型集成（ChatGPT、Claude、Gemini等），提示词跨平台通用
- 开源可自托管部署，企业级隐私保护，无需担心数据泄露
- 社区驱动的提示词收集与评审机制，内容质量有保障
- 完整的提示词管理功能，支持收藏、分类和分享协作

**适用场景**:
- 企业自建AI助手平台：金融机构、医疗健康等隐私敏感行业可完全私有化部署，保护内部数据安全
- AI应用开发者参考学习：快速获取高质量提示词范本，加速产品开发和prompt工程优化
- 团队知识管理与协作：团队成员共享和复用优质提示词，提升AI使用效率和一致性



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 53,705 |
| 语言 | Python |
| Forks | 2,914 |
| Issues | 177 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

一个极具创意的 token 优化方案，通过"穴居人语言"风格将 LLM token 消耗降低 65%，在保持功能完整性的同时显著降低成本，适合高频使用 Claude Code 的开发者。

**技术亮点**:
- 创新的提示工程方法：通过独特的语言风格压缩技术实现 token 用量优化
- 深度集成 Claude Code 平台：作为官方 skill 直接在开发工作流中无缝使用
- 显著的成本效益：官方宣称可节省 65% 的 token 消耗
- 简洁高效的方案：基于少即是多的设计理念，化繁为简
- 开源 MIT 许可证：允许自由使用和二次开发

**适用场景**:
- 企业级 LLM 应用成本优化：对于需要频繁调用 Claude API 的团队，可显著降低 API 使用成本
- 个人开发者效率提升：日常使用 Claude Code 时减少 token 消耗，提高对话效率
- 资源受限环境：在 token 限制严格的场景下，帮助完成更复杂的任务



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,498 |
| 语言 | Python |
| Forks | 5,138 |
| Issues | 101 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 58,055 |
| 语言 | TypeScript |
| Forks | 9,527 |
| Issues | 114 |
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
| Stars | 89,847 |
| 语言 | TypeScript |
| Forks | 10,037 |
| Issues | 2,274 |
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
| Stars | 87,802 |
| 语言 | TypeScript |
| Forks | 8,927 |
| Issues | 1,659 |
| Topics | diagrams, diagrams-as-code, documentation, flowchart, javascript, mindmap, typescript, uml-diagrams |
| 许可证 | MIT License |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 171,801 |
| 语言 | Go |
| Forks | 13,187 |
| Issues | 183 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


### ⭐ 中优先级


### Chalarangelo/30-seconds-of-code

**描述**: Coding articles to level up your development skills

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 127,689 |
| 语言 | JavaScript |
| Forks | 12,479 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


## 📁 其他 (68 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 136,675 |
| 语言 | Unknown |
| Forks | 34,127 |
| Issues | 136 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,645 |
| 语言 | Python |
| Forks | 9,053 |
| Issues | 3,006 |
| Topics | llm-app |
| 许可证 | Apache License 2.0 |


### mattpocock/skills

**描述**: Skills for Real Engineers. Straight from my .claude directory.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,784 |
| 语言 | Shell |
| Forks | 5,066 |
| Issues | 12 |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,609 |
| 语言 | Python |
| Forks | 13,461 |
| Issues | 116 |
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
| Stars | 92,460 |
| 语言 | Python |
| Forks | 8,011 |
| Issues | 588 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### iptv-org/iptv

**描述**: Collection of publicly available IPTV channels from all over the world

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 115,913 |
| 语言 | TypeScript |
| Forks | 6,083 |
| Issues | 7 |
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
| Stars | 115,638 |
| 语言 | TypeScript |
| Forks | 8,438 |
| Issues | 303 |
| Topics | clash, clash-meta, clash-verge, linux, mac, mihomo, tauri-app, windows |
| 许可证 | GNU General Public License v3.0 |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,103 |
| 语言 | TypeScript |
| Forks | 13,126 |
| Issues | 505 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,902 |
| 语言 | JavaScript |
| Forks | 5,099 |
| Issues | 43 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。 欢迎参加飞书AI先锋诗活动  https://bytedance.aiforce.cloud/app/app_4jvnd48x7khm1

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,385 |
| 语言 | JavaScript |
| Forks | 10,363 |
| Issues | 135 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,325 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 1,895 |
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
| Stars | 108,247 |
| 语言 | C++ |
| Forks | 17,749 |
| Issues | 1,576 |
| Topics | ggml |
| 许可证 | MIT License |


### pathwaycom/pathway

**描述**: Python ETL framework for stream processing, real-time analytics, LLM pipelines, and RAG.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,350 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### abhigyanpatwari/GitNexus

**描述**: GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creator that runs entirely in your browser. Drop in a GitHub repo or ZIP file, and get an interactive knowledge graph wit a built in Graph RAG Agent. Perfect for code exploration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,565 |
| 语言 | TypeScript |
| Forks | 4,042 |
| Issues | 369 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 295,967 |
| 语言 | Python |
| Forks | 27,816 |
| Issues | 16 |
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
| Stars | 220,732 |
| 语言 | Python |
| Forks | 50,524 |
| Issues | 951 |
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
| Stars | 86,920 |
| 语言 | Python |
| Forks | 37,417 |
| Issues | 3,783 |
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
| Stars | 77,667 |
| 语言 | Python |
| Forks | 45,106 |
| Issues | 1,286 |
| 许可证 | Other |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 444,146 |
| 语言 | TypeScript |
| Forks | 44,451 |
| Issues | 182 |
| Topics | careers, certification, community, curriculum, d3, education, freecodecamp, javascript, learn-to-code, math, nodejs, nonprofits, programming, react, teachers |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### nilbuild/developer-roadmap

**描述**: Interactive roadmaps, guides and other educational content to help developers grow in their careers.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 354,158 |
| 语言 | TypeScript |
| Forks | 44,012 |
| Issues | 15 |
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
| Stars | 122,485 |
| 语言 | TypeScript |
| Forks | 13,509 |
| Issues | 3,025 |
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
| Stars | 113,529 |
| 语言 | TypeScript |
| Forks | 8,718 |
| Issues | 1,851 |
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
| Stars | 108,735 |
| 语言 | TypeScript |
| Forks | 13,379 |
| Issues | 5,032 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 99,667 |
| 语言 | TypeScript |
| Forks | 5,535 |
| Issues | 698 |
| Topics | backup-tool, flutter, google-photos, google-photos-alternative, javascript, mobile-app, nestjs, nodejs, photo-gallery, photos, photos-management, self-hosted, svelte, sveltekit, typescript, videos |
| 许可证 | GNU Affero General Public License v3.0 |


### ant-design/ant-design

**描述**: An enterprise-class UI design language and React UI library

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,928 |
| 语言 | TypeScript |
| Forks | 54,589 |
| Issues | 1,364 |
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
| Stars | 94,838 |
| 语言 | TypeScript |
| Forks | 5,216 |
| Issues | 90 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,387 |
| 语言 | TypeScript |
| Forks | 8,120 |
| Issues | 748 |
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
| Stars | 244,839 |
| 语言 | JavaScript |
| Forks | 51,026 |
| Issues | 1,266 |
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
| Stars | 117,029 |
| 语言 | JavaScript |
| Forks | 35,504 |
| Issues | 2,657 |
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
| Stars | 112,302 |
| 语言 | JavaScript |
| Forks | 36,355 |
| Issues | 509 |
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
| Stars | 109,044 |
| 语言 | JavaScript |
| Forks | 11,662 |
| Issues | 156 |
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
| Stars | 98,274 |
| 语言 | JavaScript |
| Forks | 32,652 |
| Issues | 1,539 |
| Topics | design-system, material-design, material-ui, react, react-components |
| 许可证 | MIT License |


### sveltejs/svelte

**描述**: web development for the rest of us

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,470 |
| 语言 | JavaScript |
| Forks | 4,899 |
| Issues | 999 |
| Topics | compiler, template, ui |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,786 |
| 语言 | JavaScript |
| Forks | 4,553 |
| Issues | 101 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### webpack/webpack

**描述**: A bundler for javascript and friends. Packs many modules into a few bundled assets. Code Splitting allows for loading parts of the application on demand. Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images, JSON, Coffeescript, LESS, ... and your custom stuff.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,778 |
| 语言 | JavaScript |
| Forks | 9,355 |
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
| Stars | 64,371 |
| 语言 | JavaScript |
| Forks | 4,091 |
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
| Stars | 59,842 |
| 语言 | JavaScript |
| Forks | 20,456 |
| Issues | 92 |
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
| Stars | 57,441 |
| 语言 | JavaScript |
| Forks | 12,309 |
| Issues | 28 |
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
| Stars | 53,244 |
| 语言 | JavaScript |
| Forks | 10,607 |
| Issues | 445 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,733 |
| 语言 | JavaScript |
| Forks | 11,524 |
| Issues | 238 |
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
| Stars | 133,732 |
| 语言 | Go |
| Forks | 18,990 |
| Issues | 10,081 |
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
| Stars | 106,284 |
| 语言 | Go |
| Forks | 15,032 |
| Issues | 40 |
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
| Stars | 87,895 |
| 语言 | Go |
| Forks | 8,252 |
| Issues | 241 |
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
| Stars | 83,530 |
| 语言 | Go |
| Forks | 5,145 |
| Issues | 388 |
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
| Stars | 68,586 |
| 语言 | Go |
| Forks | 3,228 |
| Issues | 12 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,998 |
| 语言 | Go |
| Forks | 5,072 |
| Issues | 1,174 |
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
| Stars | 51,016 |
| 语言 | Go |
| Forks | 21,891 |
| Issues | 412 |
| Topics | blockchain, ethereum, geth, go, p2p |
| 许可证 | GNU Lesser General Public License v3.0 |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 92,466 |
| 语言 | Shell |
| Forks | 15,213 |
| Issues | 120 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,750 |
| 语言 | Python |
| Forks | 11,800 |
| Issues | 353 |
| Topics | awesome, github, hellogithub, python |


### ⭐ 中优先级


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 78/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 387,670 |
| 语言 | Python |
| Forks | 66,218 |
| Issues | 79 |
| Topics | books, education, hacktoberfest, list, resource |
| 许可证 | Creative Commons Attribution 4.0 International |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 76/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 111,282 |
| 语言 | Unknown |
| Forks | 11,091 |
| Issues | 84 |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 98,877 |
| 语言 | Python |
| Forks | 12,140 |
| Issues | 122 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,564 |
| 语言 | Python |
| Forks | 7,259 |
| Issues | 488 |
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
| Stars | 77,459 |
| 语言 | Python |
| Forks | 16,918 |
| Issues | 27 |
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
| Stars | 139,322 |
| 语言 | TypeScript |
| Forks | 16,554 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 85,019 |
| 语言 | TypeScript |
| Forks | 10,586 |
| Issues | 403 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,369 |
| 语言 | TypeScript |
| Forks | 7,606 |
| Issues | 35 |
| 许可证 | Other |


### airbnb/javascript

**描述**: JavaScript Style Guide

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 148,110 |
| 语言 | JavaScript |
| Forks | 26,693 |
| Issues | 160 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### microsoft/Web-Dev-For-Beginners

**描述**: 24 Lessons, 12 Weeks, Get Started as a Web Developer

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 95,709 |
| 语言 | JavaScript |
| Forks | 15,453 |
| Issues | 51 |
| Topics | css, curriculum, education, html, javascript, learning, microsoft-for-beginners, tutorials |
| 许可证 | MIT License |


### hakimel/reveal.js

**描述**: The HTML Presentation Framework

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 71,118 |
| 语言 | JavaScript |
| Forks | 16,797 |
| Issues | 896 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 67,394 |
| 语言 | JavaScript |
| Forks | 11,954 |
| Issues | 559 |
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
| Stars | 66,361 |
| 语言 | JavaScript |
| Forks | 9,183 |
| Issues | 3 |
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
| Stars | 61,262 |
| 语言 | JavaScript |
| Forks | 7,154 |
| Issues | 141 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 60,864 |
| 语言 | JavaScript |
| Forks | 5,658 |
| Issues | 68 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### jesseduffield/lazydocker

**描述**: The lazier way to manage everything docker

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 50,897 |
| 语言 | Go |
| Forks | 1,608 |
| Issues | 273 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 49,423 |
| 语言 | Go |
| Forks | 7,944 |
| Issues | 567 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,862 |
| 语言 | Go |
| Forks | 8,856 |
| Issues | 17 |
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
| Stars | 46,207 |
| 语言 | Go |
| Forks | 3,811 |
| Issues | 82 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
