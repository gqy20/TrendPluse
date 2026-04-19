# 项目发现报告 (2026-04-19)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 135 |
| 去重移除 | 32 |
| 已在监控 | 25 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 23 |
| 🧠 机器学习框架 | 10 |
| 🛠️ 开发工具 | 16 |
| ⚙️ DevOps/基础设施 | 12 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 12 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 7 |
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


## 🤖 AI Agents (30 个项目) { #ai-agents }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,670 |
| 语言 | Python |
| Forks | 18,832 |
| Issues | 233 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完整的自托管 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，配备 RAG 检索增强生成和 MCP 协议扩展能力，星标数超过 13 万，是目前最受欢迎的开源 LLM Web 界面解决方案。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、兼容 OpenAPI 的多种 LLM 服务商
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 AI 回答准确性
- MCP 协议支持：集成 Model Context Protocol，可扩展连接多种外部工具和数据源
- 完整的 Web 界面：现代化响应式 UI，支持聊天、代码高亮、文件处理等多模态交互
- 自托管部署：提供 Docker 一键部署方案，支持本地运行，数据完全自主掌控

**适用场景**:
- 个人开发者：本地运行开源 LLM 模型（如 Llama、Qwen），构建私有 AI 助手
- 企业场景：部署私有化 AI 对话系统，处理敏感数据，满足合规要求
- 知识库问答：上传文档构建 RAG 应用，实现基于企业知识库的智能问答服务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,753 |
| 语言 | Python |
| Forks | 14,500 |
| Issues | 5,644 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源 AI 组织 NousResearch 打造的智能代理框架，支持 Claude、GPT 等多模型集成，Stars 超过 10 万证明了其社区认可度和稳定性，适合构建企业级 AI 应用和个人 AI 助手开发。

**技术亮点**:
- 多模型集成支持：支持 Anthropic Claude、OpenAI GPT 等主流大语言模型，可灵活切换和扩展
- NousResearch 技术背书：项目源于活跃的开源 AI 研究社区，持续更新维护质量有保障
- MIT 开源许可：允许商业使用和二次开发，降低企业采用门槛
- Python 原生实现：便于与现有 Python 生态集成，支持快速开发和部署
- Agent 核心框架：提供构建智能代理所需的基础架构和工具链

**适用场景**:
- 企业级 AI 助手/自动化客服：构建支持多模型切换的智能客服系统，提升客户响应效率
- 个人开发者 AI 应用开发：快速搭建基于大语言模型的 AI 助手、代码生成工具等应用原型
- 自动化任务执行：利用 Agent 框架实现复杂任务的自动化分解与执行，如 Claude Code 辅助编程



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,488 |
| 语言 | Python |
| Forks | 8,861 |
| Issues | 3,016 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 平台之一，它将深度文档理解与 Agent 能力完美融合，支持 GraphRAG 和 Deep Research 等高级特性，配合多 LLM 后端支持（OpenAI/DeepSeek/Ollama），能够为企业和开发者提供生产级的知识库问答和深度研究解决方案，特别适合需要处理复杂非结构化文档并构建智能助手的场景。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力实现复杂推理和多步检索，支持动态规划查询路径，大幅提升检索准确性和上下文理解深度
- 深度文档理解引擎：支持多种文档格式（PDF、Word、Excel、PPT等），具备布局分析、表格识别、图表解析等高级能力，确保结构化信息的精准提取
- GraphRAG 支持：集成图增强检索能力，能够捕捉实体关系和语义关联，提升复杂问题的回答质量和溯源能力
- 多 LLM 后端兼容：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并提供 MCP 协议支持，便于集成到现有 AI 生态系统
- Deep Research 能力：内置深度研究模式，支持多轮迭代探索和综合分析，适合构建研究助手和决策支持系统

**适用场景**:
- 企业级知识库问答系统：构建支持复杂文档理解的企业知识库，支持多模态文档处理，应用于客服机器人、内部知识检索、合规文档分析等场景
- 智能文档处理与分析平台：利用深度文档理解能力，实现合同审查、财报分析、研究报告摘要等复杂文档任务的自动化处理
- AI Agent 驱动的研究助手：结合 Agent 和 Deep Research 能力，构建能够进行多步推理、网络搜索、信息整合的深度研究辅助工具，适用于学术研究和市场分析场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,075 |
| 语言 | JavaScript |
| Forks | 25,046 |
| Issues | 127 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

affaan-m/everything-claude-code 是一个JavaScript项目，拥有 161,075 Stars。The agent harness performance optimization system. Skills, instincts, memory, security, and research...

**技术亮点**:
- 活跃的开源社区 (161,075 Stars)
- 使用 JavaScript 开发

**适用场景**:
- JavaScript 开发项目



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,570 |
| 语言 | Go |
| Forks | 3,968 |
| Issues | 172 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案之一，支持 Llama、Mamba、Stable Diffusion 等主流模型的一站式部署，无需 GPU 即可运行，适合构建私有化 AI 服务和数据隐私敏感场景。

**技术亮点**:
- 基于 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，性能表现优异
- 支持多种模型类型：LLM（大语言模型）、图像生成、语音合成、目标检测、音乐生成等，覆盖主流 AI 应用场景
- 支持 CPU 推理，可在消费级硬件上运行大幅降低部署门槛，同时支持 GPU 加速
- 提供 RESTful API 接口，与 OpenAI API 兼容，便于现有应用快速迁移集成
- 支持 libp2p 去中心化网络和分布式部署模式，适合边缘计算和去中心化应用场景

**适用场景**:
- 私有化 AI 部署：企业可在本地服务器运行 AI 模型，确保敏感数据不离开本地网络，满足金融、医疗等行业的合规要求
- 个人开发者与爱好者：无需购买昂贵 GPU，即可在普通电脑上运行 Llama 等开源大语言模型进行开发测试
- 边缘计算与物联网：在资源受限的边缘设备上部署 AI 推理能力，实现本地化的智能决策和响应



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,358 |
| 语言 | TypeScript |
| Forks | 14,945 |
| Issues | 696 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 平台，支持多模型（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，提供了开箱即用的多 Agent 协作框架，特别适合需要快速搭建企业级 AI 助手或构建复杂 Agent 团队应用的开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现了标准化的工具调用和上下文管理规范
- 多 Agent 协作框架：支持设计和管理多个 Agent 协同工作，将 Agent 作为基本工作单元
- 知识库集成：内置 RAG 能力，支持文档解析和向量检索
- 现代化技术栈：基于 TypeScript/React 构建，提供完整的前后端解决方案

**适用场景**:
- 企业级 AI 助手平台：快速构建支持多模型的企业内部 AI 助手，支持知识库问答和业务流程自动化
- Agent 团队编排：设计复杂的多 Agent 协作系统，让不同专业 Agent 协同完成复杂任务
- AI 应用开发框架：作为底层框架开发各类 AI 原生应用，支持自定义 Agent 行为和工具集成



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,318 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 979 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的 LLM 微调框架之一，ACL 2024 录用证明了其学术价值，通过统一接口支持 100+ 模型的 LoRA/QLoRA/RLHF 等多种微调方式，极大降低了大型模型定制化的门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，包括 LLaMA3、Qwen、Gemma、DeepSeek 等主流模型
- 多种高效微调技术：集成 LoRA、QLoRA、PEFT、量化等技术，显著降低 GPU 显存占用
- 完整训练流程支持：涵盖预训练、SFT、RLHF（DPO/KTO）、DPO 等全链路训练范式
- 多模态能力支持：不仅支持语言模型，还支持视觉-语言模型（VLM）的微调
- 优化训练效率：采用梯度检查点、混合精度、Flash Attention 等技术提升训练速度

**适用场景**:
- 企业定制化场景：企业可基于 LlamaFactory 快速将通用大模型微调为符合业务需求的垂直领域模型（如客服、金融、医疗）
- 个人开发者研究：个人开发者无需深入理解底层细节，即可进行 LLM 微调实验和研究
- 模型推理优化：结合量化技术，将微调后的模型压缩部署到资源受限的环境中，降低推理成本



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,162 |
| 语言 | TypeScript |
| Forks | 5,290 |
| Issues | 158 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 向量数据库技术为 Claude Code 打造长期记忆系统，解决了 AI 编程助手无法跨会话保留上下文的核心痛点，让开发者能够在多轮开发中保持上下文连贯性，大幅提升 AI 辅助编程的效率和质量。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，实现语义级别的记忆检索和上下文注入
- 集成向量数据库（ChromaDB）进行高效 embedding 存储和相似度搜索
- 使用 Claude agent-sdk 进行智能记忆压缩和上下文提炼，降低 token 消耗
- 支持 SQLite 本地存储，保证数据隐私的同时实现持久化记忆
- 与 Claude Code 深度集成，作为官方插件无缝嵌入开发工作流

**适用场景**:
- 长期项目开发：需要跨越数周甚至数月维护的大型代码库，保持架构决策和设计模式的连续性
- 团队协作场景：帮助新成员快速理解项目历史和之前的 AI 交互上下文，加速 onboarding
- 个人开发者：构建个人代码知识库，让 AI 记住偏好设置、代码风格和项目约定



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,802 |
| 语言 | TypeScript |
| Forks | 9,025 |
| Issues | 96 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,535 |
| 语言 | HTML |
| Forks | 4,566 |
| Issues | 10 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,517 |
| 语言 | Python |
| Forks | 9,956 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,089 |
| 语言 | Python |
| Forks | 7,051 |
| Issues | 967 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,885 |
| 语言 | Java |
| Forks | 15,921 |
| Issues | 9 |
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
| Stars | 39,013 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,487 |
| 语言 | Python |
| Forks | 4,568 |
| Issues | 92 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 110,798 |
| 语言 | TypeScript |
| Forks | 7,063 |
| Issues | 281 |
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
| Stars | 58,603 |
| 语言 | JavaScript |
| Forks | 6,341 |
| Issues | 341 |
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
| Stars | 71,495 |
| 语言 | Python |
| Forks | 8,996 |
| Issues | 417 |
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
| Stars | 52,784 |
| 语言 | TypeScript |
| Forks | 4,250 |
| Issues | 559 |
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
| Stars | 106,411 |
| 语言 | Python |
| Forks | 15,602 |
| Issues | 2 |
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
| Stars | 88,633 |
| 语言 | Python |
| Forks | 10,164 |
| Issues | 216 |
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
| Stars | 52,058 |
| 语言 | TypeScript |
| Forks | 24,174 |
| Issues | 812 |
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
| Stars | 184,721 |
| 语言 | TypeScript |
| Forks | 56,963 |
| Issues | 1,519 |
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
| Stars | 155,067 |
| 语言 | Java |
| Forks | 46,149 |
| Issues | 63 |
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
| Stars | 147,124 |
| 语言 | Python |
| Forks | 8,802 |
| Issues | 932 |
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
| Stars | 56,972 |
| 语言 | Jupyter Notebook |
| Forks | 19,735 |
| Issues | 12 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,159 |
| 语言 | Python |
| Forks | 2,154 |
| Issues | 97 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,857 |
| 语言 | TypeScript |
| Forks | 3,672 |
| Issues | 293 |
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
| Stars | 33,768 |
| 语言 | Jupyter Notebook |
| Forks | 5,586 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,198 |
| 语言 | Rust |
| Forks | 3,016 |
| Issues | 545 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
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
| Stars | 132,670 |
| 语言 | Python |
| Forks | 18,832 |
| Issues | 233 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完整的自托管 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，配备 RAG 检索增强生成和 MCP 协议扩展能力，星标数超过 13 万，是目前最受欢迎的开源 LLM Web 界面解决方案。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、兼容 OpenAPI 的多种 LLM 服务商
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 AI 回答准确性
- MCP 协议支持：集成 Model Context Protocol，可扩展连接多种外部工具和数据源
- 完整的 Web 界面：现代化响应式 UI，支持聊天、代码高亮、文件处理等多模态交互
- 自托管部署：提供 Docker 一键部署方案，支持本地运行，数据完全自主掌控

**适用场景**:
- 个人开发者：本地运行开源 LLM 模型（如 Llama、Qwen），构建私有 AI 助手
- 企业场景：部署私有化 AI 对话系统，处理敏感数据，满足合规要求
- 知识库问答：上传文档构建 RAG 应用，实现基于企业知识库的智能问答服务



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,488 |
| 语言 | Python |
| Forks | 8,861 |
| Issues | 3,016 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 平台之一，它将深度文档理解与 Agent 能力完美融合，支持 GraphRAG 和 Deep Research 等高级特性，配合多 LLM 后端支持（OpenAI/DeepSeek/Ollama），能够为企业和开发者提供生产级的知识库问答和深度研究解决方案，特别适合需要处理复杂非结构化文档并构建智能助手的场景。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力实现复杂推理和多步检索，支持动态规划查询路径，大幅提升检索准确性和上下文理解深度
- 深度文档理解引擎：支持多种文档格式（PDF、Word、Excel、PPT等），具备布局分析、表格识别、图表解析等高级能力，确保结构化信息的精准提取
- GraphRAG 支持：集成图增强检索能力，能够捕捉实体关系和语义关联，提升复杂问题的回答质量和溯源能力
- 多 LLM 后端兼容：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并提供 MCP 协议支持，便于集成到现有 AI 生态系统
- Deep Research 能力：内置深度研究模式，支持多轮迭代探索和综合分析，适合构建研究助手和决策支持系统

**适用场景**:
- 企业级知识库问答系统：构建支持复杂文档理解的企业知识库，支持多模态文档处理，应用于客服机器人、内部知识检索、合规文档分析等场景
- 智能文档处理与分析平台：利用深度文档理解能力，实现合同审查、财报分析、研究报告摘要等复杂文档任务的自动化处理
- AI Agent 驱动的研究助手：结合 Agent 和 Deep Research 能力，构建能够进行多步推理、网络搜索、信息整合的深度研究辅助工具，适用于学术研究和市场分析场景



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,358 |
| 语言 | TypeScript |
| Forks | 14,945 |
| Issues | 696 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 平台，支持多模型（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，提供了开箱即用的多 Agent 协作框架，特别适合需要快速搭建企业级 AI 助手或构建复杂 Agent 团队应用的开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现了标准化的工具调用和上下文管理规范
- 多 Agent 协作框架：支持设计和管理多个 Agent 协同工作，将 Agent 作为基本工作单元
- 知识库集成：内置 RAG 能力，支持文档解析和向量检索
- 现代化技术栈：基于 TypeScript/React 构建，提供完整的前后端解决方案

**适用场景**:
- 企业级 AI 助手平台：快速构建支持多模型的企业内部 AI 助手，支持知识库问答和业务流程自动化
- Agent 团队编排：设计复杂的多 Agent 协作系统，让不同专业 Agent 协同完成复杂任务
- AI 应用开发框架：作为底层框架开发各类 AI 原生应用，支持自定义 Agent 行为和工具集成



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,162 |
| 语言 | TypeScript |
| Forks | 5,290 |
| Issues | 158 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 向量数据库技术为 Claude Code 打造长期记忆系统，解决了 AI 编程助手无法跨会话保留上下文的核心痛点，让开发者能够在多轮开发中保持上下文连贯性，大幅提升 AI 辅助编程的效率和质量。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，实现语义级别的记忆检索和上下文注入
- 集成向量数据库（ChromaDB）进行高效 embedding 存储和相似度搜索
- 使用 Claude agent-sdk 进行智能记忆压缩和上下文提炼，降低 token 消耗
- 支持 SQLite 本地存储，保证数据隐私的同时实现持久化记忆
- 与 Claude Code 深度集成，作为官方插件无缝嵌入开发工作流

**适用场景**:
- 长期项目开发：需要跨越数周甚至数月维护的大型代码库，保持架构决策和设计模式的连续性
- 团队协作场景：帮助新成员快速理解项目历史和之前的 AI 交互上下文，加速 onboarding
- 个人开发者：构建个人代码知识库，让 AI 记住偏好设置、代码风格和项目约定



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,885 |
| 语言 | Java |
| Forks | 15,921 |
| Issues | 9 |
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
| Stars | 39,013 |
| 语言 | Python |
| Forks | 6,194 |
| Issues | 62 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,487 |
| 语言 | Python |
| Forks | 4,568 |
| Issues | 92 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,125 |
| 语言 | TypeScript |
| Forks | 12,125 |
| Issues | 952 |
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
| Stars | 58,603 |
| 语言 | JavaScript |
| Forks | 6,341 |
| Issues | 341 |
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
| Stars | 106,411 |
| 语言 | Python |
| Forks | 15,602 |
| Issues | 2 |
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
| Stars | 75,935 |
| 语言 | Python |
| Forks | 10,258 |
| Issues | 232 |
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
| Stars | 52,058 |
| 语言 | TypeScript |
| Forks | 24,174 |
| Issues | 812 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,865 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,118 |
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
| Stars | 33,828 |
| 语言 | Python |
| Forks | 4,798 |
| Issues | 209 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,159 |
| 语言 | Python |
| Forks | 2,154 |
| Issues | 97 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,857 |
| 语言 | TypeScript |
| Forks | 3,672 |
| Issues | 293 |
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
| Stars | 33,768 |
| 语言 | Jupyter Notebook |
| Forks | 5,586 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


## 💬 LLM 界面 (23 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,670 |
| 语言 | Python |
| Forks | 18,832 |
| Issues | 233 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一款功能完整的自托管 AI 界面，支持 Ollama 和 OpenAI API 等多种后端，配备 RAG 检索增强生成和 MCP 协议扩展能力，星标数超过 13 万，是目前最受欢迎的开源 LLM Web 界面解决方案。

**技术亮点**:
- 多后端支持：同时兼容 Ollama、OpenAI API、兼容 OpenAPI 的多种 LLM 服务商
- RAG 检索增强生成：内置知识库功能，支持文档上传和向量检索，提升 AI 回答准确性
- MCP 协议支持：集成 Model Context Protocol，可扩展连接多种外部工具和数据源
- 完整的 Web 界面：现代化响应式 UI，支持聊天、代码高亮、文件处理等多模态交互
- 自托管部署：提供 Docker 一键部署方案，支持本地运行，数据完全自主掌控

**适用场景**:
- 个人开发者：本地运行开源 LLM 模型（如 Llama、Qwen），构建私有 AI 助手
- 企业场景：部署私有化 AI 对话系统，处理敏感数据，满足合规要求
- 知识库问答：上传文档构建 RAG 应用，实现基于企业知识库的智能问答服务



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 101,753 |
| 语言 | Python |
| Forks | 14,500 |
| Issues | 5,644 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源 AI 组织 NousResearch 打造的智能代理框架，支持 Claude、GPT 等多模型集成，Stars 超过 10 万证明了其社区认可度和稳定性，适合构建企业级 AI 应用和个人 AI 助手开发。

**技术亮点**:
- 多模型集成支持：支持 Anthropic Claude、OpenAI GPT 等主流大语言模型，可灵活切换和扩展
- NousResearch 技术背书：项目源于活跃的开源 AI 研究社区，持续更新维护质量有保障
- MIT 开源许可：允许商业使用和二次开发，降低企业采用门槛
- Python 原生实现：便于与现有 Python 生态集成，支持快速开发和部署
- Agent 核心框架：提供构建智能代理所需的基础架构和工具链

**适用场景**:
- 企业级 AI 助手/自动化客服：构建支持多模型切换的智能客服系统，提升客户响应效率
- 个人开发者 AI 应用开发：快速搭建基于大语言模型的 AI 助手、代码生成工具等应用原型
- 自动化任务执行：利用 Agent 框架实现复杂任务的自动化分解与执行，如 Claude Code 辅助编程



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,488 |
| 语言 | Python |
| Forks | 8,861 |
| Issues | 3,016 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是当前最成熟的开源 RAG 平台之一，它将深度文档理解与 Agent 能力完美融合，支持 GraphRAG 和 Deep Research 等高级特性，配合多 LLM 后端支持（OpenAI/DeepSeek/Ollama），能够为企业和开发者提供生产级的知识库问答和深度研究解决方案，特别适合需要处理复杂非结构化文档并构建智能助手的场景。

**技术亮点**:
- RAG + Agent 融合架构：通过 Agent 能力实现复杂推理和多步检索，支持动态规划查询路径，大幅提升检索准确性和上下文理解深度
- 深度文档理解引擎：支持多种文档格式（PDF、Word、Excel、PPT等），具备布局分析、表格识别、图表解析等高级能力，确保结构化信息的精准提取
- GraphRAG 支持：集成图增强检索能力，能够捕捉实体关系和语义关联，提升复杂问题的回答质量和溯源能力
- 多 LLM 后端兼容：原生支持 OpenAI、DeepSeek、Ollama 等主流 LLM 提供商，并提供 MCP 协议支持，便于集成到现有 AI 生态系统
- Deep Research 能力：内置深度研究模式，支持多轮迭代探索和综合分析，适合构建研究助手和决策支持系统

**适用场景**:
- 企业级知识库问答系统：构建支持复杂文档理解的企业知识库，支持多模态文档处理，应用于客服机器人、内部知识检索、合规文档分析等场景
- 智能文档处理与分析平台：利用深度文档理解能力，实现合同审查、财报分析、研究报告摘要等复杂文档任务的自动化处理
- AI Agent 驱动的研究助手：结合 Agent 和 Deep Research 能力，构建能够进行多步推理、网络搜索、信息整合的深度研究辅助工具，适用于学术研究和市场分析场景



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,075 |
| 语言 | JavaScript |
| Forks | 25,046 |
| Issues | 127 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

affaan-m/everything-claude-code 是一个JavaScript项目，拥有 161,075 Stars。The agent harness performance optimization system. Skills, instincts, memory, security, and research...

**技术亮点**:
- 活跃的开源社区 (161,075 Stars)
- 使用 JavaScript 开发

**适用场景**:
- JavaScript 开发项目



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,358 |
| 语言 | TypeScript |
| Forks | 14,945 |
| Issues | 696 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 平台，支持多模型（GPT/Claude/Gemini/DeepSeek）和 MCP 协议，提供了开箱即用的多 Agent 协作框架，特别适合需要快速搭建企业级 AI 助手或构建复杂 Agent 团队应用的开发者。

**技术亮点**:
- 多模型统一接入：支持 OpenAI GPT、Claude、Gemini、DeepSeek 等主流大模型，提供标准化的 API 抽象层
- MCP (Model Context Protocol) 协议支持：实现了标准化的工具调用和上下文管理规范
- 多 Agent 协作框架：支持设计和管理多个 Agent 协同工作，将 Agent 作为基本工作单元
- 知识库集成：内置 RAG 能力，支持文档解析和向量检索
- 现代化技术栈：基于 TypeScript/React 构建，提供完整的前后端解决方案

**适用场景**:
- 企业级 AI 助手平台：快速构建支持多模型的企业内部 AI 助手，支持知识库问答和业务流程自动化
- Agent 团队编排：设计复杂的多 Agent 协作系统，让不同专业 Agent 协同完成复杂任务
- AI 应用开发框架：作为底层框架开发各类 AI 原生应用，支持自定义 Agent 行为和工具集成



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,162 |
| 语言 | TypeScript |
| Forks | 5,290 |
| Issues | 158 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG + 向量数据库技术为 Claude Code 打造长期记忆系统，解决了 AI 编程助手无法跨会话保留上下文的核心痛点，让开发者能够在多轮开发中保持上下文连贯性，大幅提升 AI 辅助编程的效率和质量。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，实现语义级别的记忆检索和上下文注入
- 集成向量数据库（ChromaDB）进行高效 embedding 存储和相似度搜索
- 使用 Claude agent-sdk 进行智能记忆压缩和上下文提炼，降低 token 消耗
- 支持 SQLite 本地存储，保证数据隐私的同时实现持久化记忆
- 与 Claude Code 深度集成，作为官方插件无缝嵌入开发工作流

**适用场景**:
- 长期项目开发：需要跨越数周甚至数月维护的大型代码库，保持架构决策和设计模式的连续性
- 团队协作场景：帮助新成员快速理解项目历史和之前的 AI 交互上下文，加速 onboarding
- 个人开发者：构建个人代码知识库，让 AI 记住偏好设置、代码风格和项目约定



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,110 |
| 语言 | HTML |
| Forks | 20,958 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 拥有超过 16 万 Star，是最受欢迎的 AI Prompts 社区平台，前身是知名的 Awesome ChatGPT Prompts 项目。作为完全开源免费的平台，它提供丰富的社区共享提示词，支持企业自托管部署，在提升大模型生产力的同时保障数据隐私，适合个人开发者和企业团队使用。

**技术亮点**:
- 采用 Next.js + TypeScript 现代化技术栈，具备良好的可维护性和扩展性
- 支持完全自托管部署，企业可将服务部署在私有环境，确保敏感数据不出内网
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流大语言模型，覆盖面广泛
- 活跃的开源社区持续更新和维护丰富的提示词资源库
- 采用开放许可证，零成本使用，可自由定制和二次开发

**适用场景**:
- 个人用户可寻找和收藏高质量 prompts，提升与 AI 对话的效果和效率
- 企业可自托管平台，为团队提供统一的提示词管理方案，保护内部数据隐私
- 开发者可参考项目结构和 prompts 设计模式，构建自己的 AI 应用或提示词工程系统



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,087 |
| 语言 | Jupyter Notebook |
| Forks | 13,999 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,802 |
| 语言 | TypeScript |
| Forks | 9,025 |
| Issues | 96 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,535 |
| 语言 | HTML |
| Forks | 4,566 |
| Issues | 10 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,517 |
| 语言 | Python |
| Forks | 9,956 |
| Issues | 352 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### HKUDS/nanobot

**描述**: "🐈 nanobot: The Ultra-Lightweight Personal AI Agent"

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,089 |
| 语言 | Python |
| Forks | 7,051 |
| Issues | 967 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, llm, nanobot, openai, openclaw |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 58,603 |
| 语言 | JavaScript |
| Forks | 6,341 |
| Issues | 341 |
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
| Stars | 71,495 |
| 语言 | Python |
| Forks | 8,996 |
| Issues | 417 |
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
| Stars | 52,784 |
| 语言 | TypeScript |
| Forks | 4,250 |
| Issues | 559 |
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
| Stars | 52,058 |
| 语言 | TypeScript |
| Forks | 24,174 |
| Issues | 812 |
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
| Stars | 77,324 |
| 语言 | Python |
| Forks | 15,821 |
| Issues | 4,387 |
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
| Stars | 147,124 |
| 语言 | Python |
| Forks | 8,802 |
| Issues | 932 |
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
| Stars | 169,438 |
| 语言 | Go |
| Forks | 15,693 |
| Issues | 3,006 |
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
| Stars | 47,916 |
| 语言 | Rust |
| Forks | 9,565 |
| Issues | 2 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,159 |
| 语言 | Python |
| Forks | 2,154 |
| Issues | 97 |
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
| Stars | 112,544 |
| 语言 | Python |
| Forks | 7,281 |
| Issues | 613 |
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
| Stars | 67,768 |
| 语言 | Python |
| Forks | 6,921 |
| Issues | 116 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


## 🧠 机器学习框架 (10 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,318 |
| 语言 | Python |
| Forks | 8,604 |
| Issues | 979 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是目前最完善的 LLM 微调框架之一，ACL 2024 录用证明了其学术价值，通过统一接口支持 100+ 模型的 LoRA/QLoRA/RLHF 等多种微调方式，极大降低了大型模型定制化的门槛。

**技术亮点**:
- 统一微调框架：支持 100+ LLMs 和 VLMs，包括 LLaMA3、Qwen、Gemma、DeepSeek 等主流模型
- 多种高效微调技术：集成 LoRA、QLoRA、PEFT、量化等技术，显著降低 GPU 显存占用
- 完整训练流程支持：涵盖预训练、SFT、RLHF（DPO/KTO）、DPO 等全链路训练范式
- 多模态能力支持：不仅支持语言模型，还支持视觉-语言模型（VLM）的微调
- 优化训练效率：采用梯度检查点、混合精度、Flash Attention 等技术提升训练速度

**适用场景**:
- 企业定制化场景：企业可基于 LlamaFactory 快速将通用大模型微调为符合业务需求的垂直领域模型（如客服、金融、医疗）
- 个人开发者研究：个人开发者无需深入理解底层细节，即可进行 LLM 微调实验和研究
- 模型推理优化：结合量化技术，将微调后的模型压缩部署到资源受限的环境中，降低推理成本



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,103 |
| 语言 | Python |
| Forks | 6,590 |
| Issues | 75 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，融合了 AI/机器学习能力，支持股票、加密货币、期权、固收等多资产类别分析，为量化交易和金融研究提供了端到端的解决方案。

**技术亮点**:
- 支持多资产类别覆盖：股票、加密货币、衍生品、期权、固定收益等金融产品
- 集成 AI/机器学习能力，支持智能化的金融数据分析和预测建模
- 提供丰富的数据源集成，聚合多渠道金融数据
- 模块化架构设计，支持自定义扩展和插件开发
- 提供 CLI、SDK 和 API 多种接入方式，便于开发者集成

**适用场景**:
- 量化交易策略开发：用于回测、因子分析、风险管理等量化研究工作
- 投资组合分析与资产管理：构建投资组合、绩效归因、风险评估
- 金融数据研究与分析：为分析师提供统一的数据查询和可视化工具



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,110 |
| 语言 | HTML |
| Forks | 20,958 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 拥有超过 16 万 Star，是最受欢迎的 AI Prompts 社区平台，前身是知名的 Awesome ChatGPT Prompts 项目。作为完全开源免费的平台，它提供丰富的社区共享提示词，支持企业自托管部署，在提升大模型生产力的同时保障数据隐私，适合个人开发者和企业团队使用。

**技术亮点**:
- 采用 Next.js + TypeScript 现代化技术栈，具备良好的可维护性和扩展性
- 支持完全自托管部署，企业可将服务部署在私有环境，确保敏感数据不出内网
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流大语言模型，覆盖面广泛
- 活跃的开源社区持续更新和维护丰富的提示词资源库
- 采用开放许可证，零成本使用，可自由定制和二次开发

**适用场景**:
- 个人用户可寻找和收藏高质量 prompts，提升与 AI 对话的效果和效率
- 企业可自托管平台，为团队提供统一的提示词管理方案，保护内部数据隐私
- 开发者可参考项目结构和 prompts 设计模式，构建自己的 AI 应用或提示词工程系统



### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,087 |
| 语言 | Jupyter Notebook |
| Forks | 13,999 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,619 |
| 语言 | Python |
| Forks | 32,934 |
| Issues | 2,359 |
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
| Stars | 77,324 |
| 语言 | Python |
| Forks | 15,821 |
| Issues | 4,387 |
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
| Stars | 109,280 |
| 语言 | Python |
| Forks | 12,703 |
| Issues | 4,007 |
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
| Stars | 99,263 |
| 语言 | Python |
| Forks | 27,525 |
| Issues | 18,479 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,857 |
| 语言 | TypeScript |
| Forks | 3,672 |
| Issues | 293 |
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
| Stars | 33,768 |
| 语言 | Jupyter Notebook |
| Forks | 5,586 |
| Issues | 126 |
| Topics | agents, ai, llms, machine-learning, mcp, rag |
| 许可证 | MIT License |


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
| Stars | 161,075 |
| 语言 | JavaScript |
| Forks | 25,046 |
| Issues | 127 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

affaan-m/everything-claude-code 是一个JavaScript项目，拥有 161,075 Stars。The agent harness performance optimization system. Skills, instincts, memory, security, and research...

**技术亮点**:
- 活跃的开源社区 (161,075 Stars)
- 使用 JavaScript 开发

**适用场景**:
- JavaScript 开发项目



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,570 |
| 语言 | Go |
| Forks | 3,968 |
| Issues | 172 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案之一，支持 Llama、Mamba、Stable Diffusion 等主流模型的一站式部署，无需 GPU 即可运行，适合构建私有化 AI 服务和数据隐私敏感场景。

**技术亮点**:
- 基于 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，性能表现优异
- 支持多种模型类型：LLM（大语言模型）、图像生成、语音合成、目标检测、音乐生成等，覆盖主流 AI 应用场景
- 支持 CPU 推理，可在消费级硬件上运行大幅降低部署门槛，同时支持 GPU 加速
- 提供 RESTful API 接口，与 OpenAI API 兼容，便于现有应用快速迁移集成
- 支持 libp2p 去中心化网络和分布式部署模式，适合边缘计算和去中心化应用场景

**适用场景**:
- 私有化 AI 部署：企业可在本地服务器运行 AI 模型，确保敏感数据不离开本地网络，满足金融、医疗等行业的合规要求
- 个人开发者与爱好者：无需购买昂贵 GPU，即可在普通电脑上运行 Llama 等开源大语言模型进行开发测试
- 边缘计算与物联网：在资源受限的边缘设备上部署 AI 推理能力，实现本地化的智能决策和响应



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,495 |
| 语言 | Python |
| Forks | 8,996 |
| Issues | 417 |
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
| Stars | 52,784 |
| 语言 | TypeScript |
| Forks | 4,250 |
| Issues | 559 |
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
| Stars | 184,721 |
| 语言 | TypeScript |
| Forks | 56,963 |
| Issues | 1,519 |
| Topics | ai, apis, automation, cli, data-flow, development, integration-framework, integrations, ipaas, low-code, low-code-platform, mcp, mcp-client, mcp-server, n8n, no-code, self-hosted, typescript, workflow, workflow-automation |
| 许可证 | Other |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,398 |
| 语言 | Python |
| Forks | 9,098 |
| Issues | 179 |
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
| Stars | 81,389 |
| 语言 | Python |
| Forks | 9,462 |
| Issues | 259 |
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
| Stars | 184,025 |
| 语言 | TypeScript |
| Forks | 39,273 |
| Issues | 16,446 |
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
| Stars | 94,156 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 301 |
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
| Stars | 78,974 |
| 语言 | TypeScript |
| Forks | 5,813 |
| Issues | 771 |
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
| Stars | 77,190 |
| 语言 | TypeScript |
| Forks | 6,623 |
| Issues | 138 |
| Topics | browser-ide, dev-tools, development-environment, ide, remote-work, vscode, vscode-remote |
| 许可证 | MIT License |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,631 |
| 语言 | Go |
| Forks | 2,784 |
| Issues | 311 |
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
| Stars | 76,697 |
| 语言 | Go |
| Forks | 2,764 |
| Issues | 961 |
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
| Stars | 43,921 |
| 语言 | Go |
| Forks | 8,291 |
| Issues | 967 |
| Topics | cli, git, github-api-v4, golang |
| 许可证 | MIT License |


### ⭐ 中优先级


### yt-dlp/yt-dlp

**描述**: A feature-rich command-line audio/video downloader

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 157,690 |
| 语言 | Python |
| Forks | 13,013 |
| Issues | 2,462 |
| Topics | cli, downloader, python, sponsorblock, youtube-dl, youtube-downloader, yt-dlp |
| 许可证 | The Unlicense |


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,592 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 715 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (12 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,784 |
| 语言 | TypeScript |
| Forks | 4,250 |
| Issues | 559 |
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
| Stars | 184,721 |
| 语言 | TypeScript |
| Forks | 56,963 |
| Issues | 1,519 |
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
| Stars | 51,652 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 229 |
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
| Stars | 121,775 |
| 语言 | Go |
| Forks | 42,877 |
| Issues | 2,769 |
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
| Stars | 71,504 |
| 语言 | Go |
| Forks | 18,915 |
| Issues | 3,795 |
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
| Stars | 54,988 |
| 语言 | Go |
| Forks | 6,589 |
| Issues | 2,823 |
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
| Stars | 47,517 |
| 语言 | Go |
| Forks | 5,044 |
| Issues | 981 |
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
| Stars | 94,156 |
| 语言 | TypeScript |
| Forks | 9,413 |
| Issues | 301 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 85,471 |
| 语言 | JavaScript |
| Forks | 7,655 |
| Issues | 723 |
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
| Stars | 69,934 |
| 语言 | Go |
| Forks | 1,917 |
| Issues | 320 |
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
| Stars | 62,776 |
| 语言 | Go |
| Forks | 5,927 |
| Issues | 762 |
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
| Stars | 58,986 |
| 语言 | Go |
| Forks | 4,280 |
| Issues | 19 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
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
| Stars | 85,471 |
| 语言 | JavaScript |
| Forks | 7,655 |
| Issues | 723 |
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
| Stars | 63,652 |
| 语言 | Go |
| Forks | 10,337 |
| Issues | 753 |
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
| Stars | 45,570 |
| 语言 | Go |
| Forks | 3,968 |
| Issues | 172 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是目前最成熟的本地 AI 推理开源解决方案之一，支持 Llama、Mamba、Stable Diffusion 等主流模型的一站式部署，无需 GPU 即可运行，适合构建私有化 AI 服务和数据隐私敏感场景。

**技术亮点**:
- 基于 Go 语言开发，具备优秀的并发处理能力和跨平台兼容性，性能表现优异
- 支持多种模型类型：LLM（大语言模型）、图像生成、语音合成、目标检测、音乐生成等，覆盖主流 AI 应用场景
- 支持 CPU 推理，可在消费级硬件上运行大幅降低部署门槛，同时支持 GPU 加速
- 提供 RESTful API 接口，与 OpenAI API 兼容，便于现有应用快速迁移集成
- 支持 libp2p 去中心化网络和分布式部署模式，适合边缘计算和去中心化应用场景

**适用场景**:
- 私有化 AI 部署：企业可在本地服务器运行 AI 模型，确保敏感数据不离开本地网络，满足金融、医疗等行业的合规要求
- 个人开发者与爱好者：无需购买昂贵 GPU，即可在普通电脑上运行 Llama 等开源大语言模型进行开发测试
- 边缘计算与物联网：在资源受限的边缘设备上部署 AI 推理能力，实现本地化的智能决策和响应



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,398 |
| 语言 | Python |
| Forks | 9,098 |
| Issues | 179 |
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
| Stars | 87,283 |
| 语言 | Python |
| Forks | 33,816 |
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
| Stars | 100,068 |
| 语言 | TypeScript |
| Forks | 27,172 |
| Issues | 1,118 |
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
| Stars | 78,974 |
| 语言 | TypeScript |
| Forks | 5,813 |
| Issues | 771 |
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
| Stars | 68,944 |
| 语言 | JavaScript |
| Forks | 23,154 |
| Issues | 211 |
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
| Stars | 55,959 |
| 语言 | JavaScript |
| Forks | 10,207 |
| Issues | 364 |
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
| Stars | 51,808 |
| 语言 | JavaScript |
| Forks | 4,706 |
| Issues | 1,463 |
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
| Stars | 71,679 |
| 语言 | Go |
| Forks | 4,696 |
| Issues | 243 |
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
| Stars | 57,717 |
| 语言 | Go |
| Forks | 3,298 |
| Issues | 16 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### typicode/json-server

**描述**: Get a full fake REST API with zero coding in less than 30 seconds (seriously)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 75,592 |
| 语言 | JavaScript |
| Forks | 7,283 |
| Issues | 715 |
| Topics | api, fake, frontend, json, mock, rest, test |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 88,350 |
| 语言 | Go |
| Forks | 8,573 |
| Issues | 674 |
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
| Stars | 101,125 |
| 语言 | TypeScript |
| Forks | 12,125 |
| Issues | 952 |
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
| Stars | 58,603 |
| 语言 | JavaScript |
| Forks | 6,341 |
| Issues | 341 |
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
| Stars | 43,865 |
| 语言 | Go |
| Forks | 3,964 |
| Issues | 1,118 |
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
| Stars | 51,652 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 229 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (7 个项目) { #学习资源 }


### 🌟 高优先级


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,110 |
| 语言 | HTML |
| Forks | 20,958 |
| Issues | 45 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 拥有超过 16 万 Star，是最受欢迎的 AI Prompts 社区平台，前身是知名的 Awesome ChatGPT Prompts 项目。作为完全开源免费的平台，它提供丰富的社区共享提示词，支持企业自托管部署，在提升大模型生产力的同时保障数据隐私，适合个人开发者和企业团队使用。

**技术亮点**:
- 采用 Next.js + TypeScript 现代化技术栈，具备良好的可维护性和扩展性
- 支持完全自托管部署，企业可将服务部署在私有环境，确保敏感数据不出内网
- 涵盖 ChatGPT、Claude、Gemini、GPT-4 等主流大语言模型，覆盖面广泛
- 活跃的开源社区持续更新和维护丰富的提示词资源库
- 采用开放许可证，零成本使用，可自由定制和二次开发

**适用场景**:
- 个人用户可寻找和收藏高质量 prompts，提升与 AI 对话的效果和效率
- 企业可自托管平台，为团队提供统一的提示词管理方案，保护内部数据隐私
- 开发者可参考项目结构和 prompts 设计模式，构建自己的 AI 应用或提示词工程系统



### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,802 |
| 语言 | TypeScript |
| Forks | 9,025 |
| Issues | 96 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,487 |
| 语言 | Python |
| Forks | 4,568 |
| Issues | 92 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,738 |
| 语言 | TypeScript |
| Forks | 10,024 |
| Issues | 2,245 |
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
| Stars | 87,474 |
| 语言 | TypeScript |
| Forks | 8,883 |
| Issues | 1,648 |
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
| Stars | 127,511 |
| 语言 | JavaScript |
| Forks | 12,474 |
| Issues | 1 |
| Topics | astro, awesome-list, css, education, es6-javascript, git, html, javascript, learn-to-code, learning-resources, nodejs, programming, snippets |
| 许可证 | Creative Commons Attribution 4.0 International |


### avelino/awesome-go

**描述**: A curated list of awesome Go frameworks, libraries and software

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,423 |
| 语言 | Go |
| Forks | 13,163 |
| Issues | 181 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (65 个项目) { #其他 }


### 🌟 高优先级


### x1xhlol/system-prompts-and-models-of-ai-tools

**描述**: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,538 |
| 语言 | Unknown |
| Forks | 34,011 |
| Issues | 146 |
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
| Stars | 83,269 |
| 语言 | Shell |
| Forks | 13,302 |
| Issues | 99 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,281 |
| 语言 | Python |
| Forks | 6,586 |
| Issues | 71 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,184 |
| 语言 | Python |
| Forks | 13,287 |
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
| Stars | 89,363 |
| 语言 | Python |
| Forks | 7,683 |
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
| Stars | 385,724 |
| 语言 | Python |
| Forks | 66,114 |
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
| Stars | 114,943 |
| 语言 | TypeScript |
| Forks | 5,966 |
| Issues | 89 |
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
| Stars | 111,830 |
| 语言 | TypeScript |
| Forks | 8,156 |
| Issues | 273 |
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
| Stars | 77,324 |
| 语言 | TypeScript |
| Forks | 11,034 |
| Issues | 347 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 54,919 |
| 语言 | JavaScript |
| Forks | 4,612 |
| Issues | 60 |
| Topics | claude-code, context-engineering, meta-prompting, spec-driven-development |
| 许可证 | MIT License |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,170 |
| 语言 | Go |
| Forks | 10,290 |
| Issues | 1,891 |
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
| Stars | 104,985 |
| 语言 | C++ |
| Forks | 17,054 |
| Issues | 1,529 |
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
| Stars | 63,472 |
| 语言 | Python |
| Forks | 1,627 |
| Issues | 35 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,871 |
| 语言 | Unknown |
| Forks | 5,286 |
| Issues | 63 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 293,264 |
| 语言 | Python |
| Forks | 27,719 |
| Issues | 17 |
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
| Stars | 219,862 |
| 语言 | Python |
| Forks | 50,368 |
| Issues | 931 |
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
| Stars | 98,035 |
| 语言 | Python |
| Forks | 12,067 |
| Issues | 121 |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,127 |
| 语言 | Python |
| Forks | 7,220 |
| Issues | 485 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,108 |
| 语言 | Python |
| Forks | 37,279 |
| Issues | 3,664 |
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
| Stars | 77,668 |
| 语言 | Python |
| Forks | 45,137 |
| Issues | 1,279 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,003 |
| 语言 | Python |
| Forks | 16,863 |
| Issues | 23 |
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
| Stars | 443,204 |
| 语言 | TypeScript |
| Forks | 44,331 |
| Issues | 210 |
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
| Stars | 353,205 |
| 语言 | TypeScript |
| Forks | 43,957 |
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
| Stars | 121,435 |
| 语言 | TypeScript |
| Forks | 13,340 |
| Issues | 2,992 |
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
| Stars | 112,619 |
| 语言 | TypeScript |
| Forks | 8,587 |
| Issues | 1,825 |
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
| Stars | 108,588 |
| 语言 | TypeScript |
| Forks | 13,351 |
| Issues | 5,021 |
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
| Stars | 98,183 |
| 语言 | TypeScript |
| Forks | 5,424 |
| Issues | 687 |
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
| Stars | 97,819 |
| 语言 | TypeScript |
| Forks | 54,590 |
| Issues | 1,362 |
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
| Stars | 94,622 |
| 语言 | TypeScript |
| Forks | 5,202 |
| Issues | 111 |
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
| Stars | 84,102 |
| 语言 | TypeScript |
| Forks | 10,437 |
| Issues | 400 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 83,198 |
| 语言 | TypeScript |
| Forks | 7,591 |
| Issues | 35 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,003 |
| 语言 | TypeScript |
| Forks | 8,072 |
| Issues | 715 |
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
| Stars | 244,581 |
| 语言 | JavaScript |
| Forks | 50,968 |
| Issues | 1,235 |
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
| Stars | 148,117 |
| 语言 | JavaScript |
| Forks | 26,713 |
| Issues | 160 |
| Topics | arrow-functions, es2015, es2016, es2017, es2018, es6, eslint, javascript, linting, naming-conventions, style-guide, style-linter, styleguide, tc39 |
| 许可证 | MIT License |


### nodejs/node

**描述**: Node.js JavaScript runtime ✨🐢🚀✨

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 116,813 |
| 语言 | JavaScript |
| Forks | 35,392 |
| Issues | 2,633 |
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
| Stars | 112,061 |
| 语言 | JavaScript |
| Forks | 36,324 |
| Issues | 534 |
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
| Stars | 109,028 |
| 语言 | JavaScript |
| Forks | 11,637 |
| Issues | 269 |
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
| Stars | 98,189 |
| 语言 | JavaScript |
| Forks | 32,669 |
| Issues | 1,573 |
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
| Stars | 95,629 |
| 语言 | JavaScript |
| Forks | 15,374 |
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
| Stars | 86,350 |
| 语言 | JavaScript |
| Forks | 4,889 |
| Issues | 992 |
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
| Stars | 71,031 |
| 语言 | JavaScript |
| Forks | 16,801 |
| Issues | 893 |
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
| Stars | 67,364 |
| 语言 | JavaScript |
| Forks | 11,957 |
| Issues | 551 |
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
| Stars | 66,332 |
| 语言 | JavaScript |
| Forks | 9,190 |
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
| Stars | 65,819 |
| 语言 | JavaScript |
| Forks | 9,361 |
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
| Stars | 62,860 |
| 语言 | JavaScript |
| Forks | 4,018 |
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
| Stars | 60,541 |
| 语言 | JavaScript |
| Forks | 5,654 |
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
| Stars | 59,829 |
| 语言 | JavaScript |
| Forks | 20,466 |
| Issues | 93 |
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
| Stars | 57,426 |
| 语言 | JavaScript |
| Forks | 12,302 |
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
| Stars | 53,156 |
| 语言 | JavaScript |
| Forks | 10,600 |
| Issues | 450 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,561 |
| 语言 | JavaScript |
| Forks | 11,477 |
| Issues | 241 |
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
| Stars | 133,534 |
| 语言 | Go |
| Forks | 18,935 |
| Issues | 9,985 |
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
| Stars | 106,027 |
| 语言 | Go |
| Forks | 15,002 |
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
| Stars | 87,680 |
| 语言 | Go |
| Forks | 8,238 |
| Issues | 248 |
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
| Stars | 81,872 |
| 语言 | Go |
| Forks | 4,997 |
| Issues | 393 |
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
| Stars | 68,620 |
| 语言 | Go |
| Forks | 3,217 |
| Issues | 21 |
| 许可证 | MIT License |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,733 |
| 语言 | Go |
| Forks | 5,042 |
| Issues | 1,173 |
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
| Stars | 50,990 |
| 语言 | Go |
| Forks | 21,886 |
| Issues | 401 |
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
| Stars | 50,708 |
| 语言 | Go |
| Forks | 1,603 |
| Issues | 268 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,329 |
| 语言 | Go |
| Forks | 7,949 |
| Issues | 557 |
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
| Stars | 46,013 |
| 语言 | Go |
| Forks | 3,795 |
| Issues | 83 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### ⭐ 中优先级


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 343,338 |
| 语言 | Python |
| Forks | 55,459 |
| Issues | 530 |
| Topics | design, design-patterns, design-system, development, interview, interview-practice, interview-questions, programming, python, system, web, web-application, webapp |
| 许可证 | Other |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 138,900 |
| 语言 | TypeScript |
| Forks | 16,508 |
| Issues | 44 |
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
| Stars | 79,088 |
| 语言 | JavaScript |
| Forks | 32,581 |
| Issues | 279 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 61,317 |
| 语言 | JavaScript |
| Forks | 7,140 |
| Issues | 142 |
| Topics | javascript, lodash, modules, utilities |
| 许可证 | Other |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 151,956 |
| 语言 | Python |
| Forks | 11,567 |
| Issues | 331 |
| Topics | awesome, github, hellogithub, python |
