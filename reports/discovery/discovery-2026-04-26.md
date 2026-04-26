# 项目发现报告 (2026-04-26)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 129 |
| 去重移除 | 33 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 28 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 22 |
| 🧠 机器学习框架 | 9 |
| 🛠️ 开发工具 | 14 |
| ⚙️ DevOps/基础设施 | 15 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
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
| Stars | 134,256 |
| 语言 | Python |
| Forks | 19,073 |
| Issues | 276 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最流行的开源 LLM 界面项目，提供开箱即用的 Web UI，支持 Ollama、OpenAI API 等多种后端，允许用户完全自托管，适合需要私有化部署 AI 能力的团队和个人。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的对话界面
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答
- 支持 MCP（Model Context Protocol）扩展，可连接外部工具和数据源
- 基于 Python 开发，支持 Docker 一键部署，提供完整的 REST API
- 支持多用户系统、角色权限管理，适合企业团队协作使用

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护，不想将敏感数据发送给第三方 API 的企业
- 个人开发者/极客：本地运行 Ollama 或其他开源 LLM，打造个性化 AI 助手
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答应用



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,115 |
| 语言 | Python |
| Forks | 17,521 |
| Issues | 7,220 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源组织 NousResearch 打造的高人气 AI Agent 框架（118K+ Stars），支持 OpenAI、Anthropic Claude 等多主流 LLM 提供商，采用模块化架构设计便于扩展，为开发者提供了生产级的 Agent 开发基础设施，适合构建复杂的多步骤任务自动化解决方案。

**技术亮点**:
- 多 LLM 提供商集成：原生支持 OpenAI GPT、Anthropic Claude、ChatGPT 等多种主流大语言模型，可灵活切换或组合使用
- 模块化工具系统：提供可扩展的工具调用框架，支持自定义工具集成，实现 Agent 与外部系统的无缝对接
- 生产级架构设计：具备完善的错误处理、日志记录、状态管理等企业级特性，确保 Agent 运行的稳定性
- MIT 开源许可证：完全开源且许可证友好，允许商业使用和二次开发，降低企业采用门槛
- 活跃社区生态：依托 NousResearch 组织的持续维护和社区贡献，项目保持高频迭代更新

**适用场景**:
- 企业级智能自动化：构建多步骤业务流程自动化，如客户服务机器人、数据分析报告生成、文档处理等工作流
- 开发者快速原型开发：个人开发者可快速搭建 AI Agent 原型，验证产品思路并快速迭代
- 多模型编排场景：需要整合多个 LLM 能力实现复杂推理或多模态任务的企业应用开发



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 167,520 |
| 语言 | JavaScript |
| Forks | 25,974 |
| Issues | 167 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合工具链项目，通过 Skills、Instincts、Memory、Security 和 Research-First Development 五大核心模块，为 Claude Code、Cursor 等主流 AI 编程工具提供增强能力，项目获得高达 167,520 Stars，证明了其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 多模型支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程助手，提供统一的任务编排和性能优化接口
- MCP 协议集成：基于 Model Context Protocol 实现标准化上下文管理，提升 AI 助手的理解能力和响应质量
- 安全沙箱机制：内置安全防护层，在保持高效的同时确保代码执行和权限控制的安全性
- 记忆系统设计：通过持久化记忆模块让 AI 助手能够跨会话学习和积累项目特定知识
- Research-First 开发理念：采用研究驱动的开发方法，持续优化 agent 性能基准和评估体系

**适用场景**:
- 企业级 AI 辅助开发：团队可在内部部署定制化 AI 编程工作流，结合安全机制保障代码质量
- 个人开发者提效：通过 Skills 和 Instincts 扩展能力，让 AI 助手更精准地适配个人编码习惯
- AI Agent 性能调优：研究者可基于该框架探索不同 AI 模型的性能边界，优化任务执行效率



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,842 |
| 语言 | Go |
| Forks | 4,026 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，无需 GPU 且兼容 OpenAI API，为企业和开发者提供了经济高效的私有化 AI 部署解决方案。

**技术亮点**:
- 多模态模型支持：同时支持文本生成（LLM）、图像生成（Stable Diffusion）、音频/语音合成（TTS、MusicGen）、目标检测等多种模型类型
- 跨硬件兼容性：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有的 AI 应用可零成本迁移
- Go 语言实现：利用 Go 的并发特性和高效性能，支持跨平台部署（Linux、Windows、macOS）
- 去中心化架构：支持 libp2p 分布式部署模式，适合构建去中心化 AI 服务网络

**适用场景**:
- 企业私有化 AI 部署：为对数据隐私有要求的企业提供本地运行的 AI 服务，支持敏感数据的本地处理
- 开发测试与成本优化：开发者可在本地环境进行 AI 应用开发测试，无需依赖云服务 API，显著降低开发和调试成本
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 能力，适合智能硬件、机器人等场景
- 个人 AI 助手：个人用户可在本地构建私有 AI 助手，支持语音交互、文档处理等多种功能



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,677 |
| 语言 | TypeScript |
| Forks | 15,001 |
| Issues | 739 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 协作平台，拥有超过 75K Stars 的高人气，支持多模型集成和多 Agent 协作编排，适合构建企业级 AI 工作流和团队协作场景。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，提供 Agent 团队设计能力，将 Agent 作为工作交互的基本单元
- 多模型统一集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种主流大语言模型，提供统一调用接口
- MCP (Model Context Protocol) 支持：内置 MCP 协议支持，可扩展连接各种外部工具和数据源
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保持类型安全，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库功能，支持 RAG (检索增强生成)，可构建私有知识问答系统

**适用场景**:
- 企业级 AI 工作流自动化：使用多 Agent 协作构建复杂的业务流程自动化，如客户服务、数据分析、内容生成等场景
- 个人开发者 AI 助手搭建：开发者可基于 LobeHub 快速构建个人 AI 助手、工作流工具和自动化脚本
- 团队协作与知识管理：构建团队共享的 AI Agent 知识库，支持多人协作编辑和共享 Agent 配置



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,634 |
| 语言 | Python |
| Forks | 8,635 |
| Issues | 993 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 学术会议验证的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供了从基础监督微调到高级 RLHF 的完整训练范式，且拥有 7 万+ 的社区星标，是目前最成熟、应用最广泛的开源 LLM 微调解决方案。

**技术亮点**:
- 统一微调框架：支持 Llama3、Gemma、Qwen、DeepSeek 等 100+ 主流 LLMs 及视觉语言模型，一套代码适配多种架构
- 高效微调技术栈：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低显存占用和计算成本
- 多样化训练范式：支持监督微调（SFT）、奖励模型训练、PPO/DPO 强化学习等多种 RLHF 技术
- 量化与部署：内置 AWQ/GPTQ 等量化方案，支持模型压缩后的快速部署
- 易用性与可扩展性：提供 Web UI 和 CLI 界面，支持自定义数据集和训练策略，模块化设计便于二次开发

**适用场景**:
- 企业级 LLM 定制：金融、医疗、教育等行业可基于开源基座模型微调专属领域助手，保护数据隐私的同时降低成本
- 学术研究与算法实验：研究者可快速复现 SFT、RLHF 等训练流程，聚焦算法创新而非工程实现
- 个人开发者与 AI 爱好者：借助预置模板和可视化界面，非专业团队也能完成模型微调任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,874 |
| 语言 | TypeScript |
| Forks | 5,781 |
| Issues | 6 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个极具创新性的 Claude Code 记忆增强插件，通过 AI 自动压缩编码会话历史并注入未来上下文，解决了 AI 编程助手缺乏长期记忆的核心痛点，Stars 高达 67,874 说明其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 智能上下文压缩：利用 Claude Agent SDK 实现 AI 驱动的会话摘要压缩，自动提取关键代码变更和决策
- 向量检索增强：集成 ChromaDB 向量数据库 + RAG 技术，支持语义化记忆检索，精准匹配历史上下文
- 多存储架构：结合 SQLite 本地持久化 + Embeddings 语义索引，兼顾数据安全与快速检索
- 无缝插件生态：专为 Claude Code 设计的插件架构，开箱即用，自动后台运行
- 记忆持久化：实现真正的长期记忆系统，让 AI 能够跨会话记住项目结构、代码习惯和问题解决方案

**适用场景**:
- 个人开发者：在长期项目中保持 AI 助手的上下文连贯性，避免重复解释项目背景和编码规范
- 企业级开发：团队成员共享项目记忆，新成员加入时 AI 可快速继承项目上下文和开发规范
- 复杂代码库维护：需要 AI 记住之前的技术选型、已解决的问题和代码修改历史，提升问题解决效率



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,213 |
| 语言 | HTML |
| Forks | 4,761 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个拥有 48k+ Stars 的 Claude Code 最佳实践开源项目，系统性地梳理了从 vibe coding 到 agentic engineering 的进阶路径，提供了大量实用的 Claude Code 命令、技巧和工作流，适合希望深度掌握 AI 编程工具的开发者。

**技术亮点**:
- 完整的方法论体系：从基础的 vibe coding 实践逐步过渡到高级的 agentic engineering，覆盖 AI 辅助编程的完整学习曲线
- 丰富的 Claude Code 命令和技能库：包含大量经过实践验证的命令模板和使用技巧，帮助开发者高效使用 Claude Code
- Context Engineering 最佳实践：深入探讨如何通过上下文工程提升 AI 编程的准确性和效率
- Agentic Workflow 实现方案：提供 AI 代理工作流的设计模式和实现思路，支持复杂任务的自动化执行
- 多场景覆盖：涵盖 AI Agents、Claude Code Agents、Skill 开发等多个维度的最佳实践

**适用场景**:
- 企业级 AI 编程转型：帮助开发团队系统性地引入 Claude Code，建立规范的 AI 辅助开发流程和最佳实践
- 个人开发者效率提升：为希望深度掌握 Claude Code 的开发者提供丰富的命令模板、快捷键和工作流建议
- AI 编程技能培训：作为内部培训材料，帮助团队成员快速从传统编码过渡到 AI 辅助开发模式



### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,739 |
| 语言 | Python |
| Forks | 9,997 |
| Issues | 353 |
| Topics | ai, ai-agent, chatgpt-on-wechat, claude, deepseek, dingtalk, feishu-bot, gemini, kimi, linkai, llm, mcp, multi-agent, openai, openclaw, python3, qwen, skills, wechat, weixin |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,983 |
| 语言 | Java |
| Forks | 15,952 |
| Issues | 14 |
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
| Stars | 40,826 |
| 语言 | Python |
| Forks | 4,898 |
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
| Stars | 39,055 |
| 语言 | Python |
| Forks | 6,191 |
| Issues | 71 |
| Topics | agents, ai, analytics, artificial-inteligence, bigquery, business-intelligence, databases, hacktoberfest, llms, mcp, mssql, mysql, postgresql, rag |
| 许可证 | Other |


### firecrawl/firecrawl

**描述**: 🔥 The API to search, scrape, and interact with the web for AI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 112,410 |
| 语言 | TypeScript |
| Forks | 7,163 |
| Issues | 295 |
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
| Stars | 59,037 |
| 语言 | JavaScript |
| Forks | 6,378 |
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
| Stars | 72,116 |
| 语言 | Python |
| Forks | 9,104 |
| Issues | 411 |
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
| Stars | 54,261 |
| 语言 | TypeScript |
| Forks | 4,411 |
| Issues | 658 |
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
| Stars | 107,628 |
| 语言 | Python |
| Forks | 15,838 |
| Issues | 11 |
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
| Stars | 90,436 |
| 语言 | Python |
| Forks | 10,333 |
| Issues | 224 |
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
| Stars | 52,294 |
| 语言 | TypeScript |
| Forks | 24,225 |
| Issues | 825 |
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
| Stars | 185,677 |
| 语言 | TypeScript |
| Forks | 57,143 |
| Issues | 1,579 |
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
| Stars | 155,232 |
| 语言 | Java |
| Forks | 46,152 |
| Issues | 64 |
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
| Stars | 147,379 |
| 语言 | Python |
| Forks | 8,853 |
| Issues | 958 |
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
| Stars | 59,582 |
| 语言 | Jupyter Notebook |
| Forks | 20,181 |
| Issues | 3 |
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
| Stars | 56,452 |
| 语言 | Python |
| Forks | 6,077 |
| Issues | 560 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,666 |
| 语言 | TypeScript |
| Forks | 9,319 |
| Issues | 108 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,999 |
| 语言 | TypeScript |
| Forks | 3,699 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


### ruvnet/ruflo

**描述**: 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 89/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,533 |
| 语言 | TypeScript |
| Forks | 3,796 |
| Issues | 489 |
| Topics | agentic-ai, agentic-engineering, agentic-framework, agentic-rag, agentic-workflow, agents, ai-assistant, ai-tools, anthropic-claude, autonomous-agents, claude-code, claude-code-skills, codex, huggingface, mcp-server, model-context-protocol, multi-agent, multi-agent-systems, swarm, swarm-intelligence |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,865 |
| 语言 | Rust |
| Forks | 3,357 |
| Issues | 618 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (15 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,256 |
| 语言 | Python |
| Forks | 19,073 |
| Issues | 276 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最流行的开源 LLM 界面项目，提供开箱即用的 Web UI，支持 Ollama、OpenAI API 等多种后端，允许用户完全自托管，适合需要私有化部署 AI 能力的团队和个人。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的对话界面
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答
- 支持 MCP（Model Context Protocol）扩展，可连接外部工具和数据源
- 基于 Python 开发，支持 Docker 一键部署，提供完整的 REST API
- 支持多用户系统、角色权限管理，适合企业团队协作使用

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护，不想将敏感数据发送给第三方 API 的企业
- 个人开发者/极客：本地运行 Ollama 或其他开源 LLM，打造个性化 AI 助手
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,677 |
| 语言 | TypeScript |
| Forks | 15,001 |
| Issues | 739 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 协作平台，拥有超过 75K Stars 的高人气，支持多模型集成和多 Agent 协作编排，适合构建企业级 AI 工作流和团队协作场景。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，提供 Agent 团队设计能力，将 Agent 作为工作交互的基本单元
- 多模型统一集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种主流大语言模型，提供统一调用接口
- MCP (Model Context Protocol) 支持：内置 MCP 协议支持，可扩展连接各种外部工具和数据源
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保持类型安全，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库功能，支持 RAG (检索增强生成)，可构建私有知识问答系统

**适用场景**:
- 企业级 AI 工作流自动化：使用多 Agent 协作构建复杂的业务流程自动化，如客户服务、数据分析、内容生成等场景
- 个人开发者 AI 助手搭建：开发者可基于 LobeHub 快速构建个人 AI 助手、工作流工具和自动化脚本
- 团队协作与知识管理：构建团队共享的 AI Agent 知识库，支持多人协作编辑和共享 Agent 配置



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,874 |
| 语言 | TypeScript |
| Forks | 5,781 |
| Issues | 6 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个极具创新性的 Claude Code 记忆增强插件，通过 AI 自动压缩编码会话历史并注入未来上下文，解决了 AI 编程助手缺乏长期记忆的核心痛点，Stars 高达 67,874 说明其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 智能上下文压缩：利用 Claude Agent SDK 实现 AI 驱动的会话摘要压缩，自动提取关键代码变更和决策
- 向量检索增强：集成 ChromaDB 向量数据库 + RAG 技术，支持语义化记忆检索，精准匹配历史上下文
- 多存储架构：结合 SQLite 本地持久化 + Embeddings 语义索引，兼顾数据安全与快速检索
- 无缝插件生态：专为 Claude Code 设计的插件架构，开箱即用，自动后台运行
- 记忆持久化：实现真正的长期记忆系统，让 AI 能够跨会话记住项目结构、代码习惯和问题解决方案

**适用场景**:
- 个人开发者：在长期项目中保持 AI 助手的上下文连贯性，避免重复解释项目背景和编码规范
- 企业级开发：团队成员共享项目记忆，新成员加入时 AI 可快速继承项目上下文和开发规范
- 复杂代码库维护：需要 AI 记住之前的技术选型、已解决的问题和代码修改历史，提升问题解决效率



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,983 |
| 语言 | Java |
| Forks | 15,952 |
| Issues | 14 |
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
| Stars | 40,826 |
| 语言 | Python |
| Forks | 4,898 |
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
| Stars | 39,055 |
| 语言 | Python |
| Forks | 6,191 |
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
| Stars | 101,460 |
| 语言 | TypeScript |
| Forks | 12,188 |
| Issues | 958 |
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
| Stars | 59,037 |
| 语言 | JavaScript |
| Forks | 6,378 |
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
| Stars | 107,628 |
| 语言 | Python |
| Forks | 15,838 |
| Issues | 11 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### PaddlePaddle/PaddleOCR

**描述**: Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,615 |
| 语言 | Python |
| Forks | 10,323 |
| Issues | 240 |
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
| Stars | 52,294 |
| 语言 | TypeScript |
| Forks | 24,225 |
| Issues | 825 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,998 |
| 语言 | Go |
| Forks | 3,980 |
| Issues | 1,096 |
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
| Stars | 34,300 |
| 语言 | Python |
| Forks | 4,849 |
| Issues | 213 |
| Topics | genai, gpt, gpt-4, graphrag, knowledge-graph, large-language-models, llm, rag, retrieval-augmented-generation |
| 许可证 | MIT License |


### microsoft/graphrag

**描述**: A modular graph-based Retrieval-Augmented Generation (RAG) system

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 32,520 |
| 语言 | Python |
| Forks | 3,428 |
| Issues | 104 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,999 |
| 语言 | TypeScript |
| Forks | 3,699 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (22 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 134,256 |
| 语言 | Python |
| Forks | 19,073 |
| Issues | 276 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最流行的开源 LLM 界面项目，提供开箱即用的 Web UI，支持 Ollama、OpenAI API 等多种后端，允许用户完全自托管，适合需要私有化部署 AI 能力的团队和个人。

**技术亮点**:
- 支持多种 LLM 后端集成（Ollama、OpenAI API、Azure OpenAI 等），提供统一的对话界面
- 内置 RAG（检索增强生成）功能，支持文档上传和知识库问答
- 支持 MCP（Model Context Protocol）扩展，可连接外部工具和数据源
- 基于 Python 开发，支持 Docker 一键部署，提供完整的 REST API
- 支持多用户系统、角色权限管理，适合企业团队协作使用

**适用场景**:
- 企业内部私有化部署：需要数据隐私保护，不想将敏感数据发送给第三方 API 的企业
- 个人开发者/极客：本地运行 Ollama 或其他开源 LLM，打造个性化 AI 助手
- 知识库问答系统：利用 RAG 功能构建基于自有文档的智能问答应用



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 118,115 |
| 语言 | Python |
| Forks | 17,521 |
| Issues | 7,220 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是由知名开源组织 NousResearch 打造的高人气 AI Agent 框架（118K+ Stars），支持 OpenAI、Anthropic Claude 等多主流 LLM 提供商，采用模块化架构设计便于扩展，为开发者提供了生产级的 Agent 开发基础设施，适合构建复杂的多步骤任务自动化解决方案。

**技术亮点**:
- 多 LLM 提供商集成：原生支持 OpenAI GPT、Anthropic Claude、ChatGPT 等多种主流大语言模型，可灵活切换或组合使用
- 模块化工具系统：提供可扩展的工具调用框架，支持自定义工具集成，实现 Agent 与外部系统的无缝对接
- 生产级架构设计：具备完善的错误处理、日志记录、状态管理等企业级特性，确保 Agent 运行的稳定性
- MIT 开源许可证：完全开源且许可证友好，允许商业使用和二次开发，降低企业采用门槛
- 活跃社区生态：依托 NousResearch 组织的持续维护和社区贡献，项目保持高频迭代更新

**适用场景**:
- 企业级智能自动化：构建多步骤业务流程自动化，如客户服务机器人、数据分析报告生成、文档处理等工作流
- 开发者快速原型开发：个人开发者可快速搭建 AI Agent 原型，验证产品思路并快速迭代
- 多模型编排场景：需要整合多个 LLM 能力实现复杂推理或多模态任务的企业应用开发



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 167,520 |
| 语言 | JavaScript |
| Forks | 25,974 |
| Issues | 167 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合工具链项目，通过 Skills、Instincts、Memory、Security 和 Research-First Development 五大核心模块，为 Claude Code、Cursor 等主流 AI 编程工具提供增强能力，项目获得高达 167,520 Stars，证明了其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 多模型支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程助手，提供统一的任务编排和性能优化接口
- MCP 协议集成：基于 Model Context Protocol 实现标准化上下文管理，提升 AI 助手的理解能力和响应质量
- 安全沙箱机制：内置安全防护层，在保持高效的同时确保代码执行和权限控制的安全性
- 记忆系统设计：通过持久化记忆模块让 AI 助手能够跨会话学习和积累项目特定知识
- Research-First 开发理念：采用研究驱动的开发方法，持续优化 agent 性能基准和评估体系

**适用场景**:
- 企业级 AI 辅助开发：团队可在内部部署定制化 AI 编程工作流，结合安全机制保障代码质量
- 个人开发者提效：通过 Skills 和 Instincts 扩展能力，让 AI 助手更精准地适配个人编码习惯
- AI Agent 性能调优：研究者可基于该框架探索不同 AI 模型的性能边界，优化任务执行效率



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,677 |
| 语言 | TypeScript |
| Forks | 15,001 |
| Issues | 739 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个功能完备的 AI Agent 协作平台，拥有超过 75K Stars 的高人气，支持多模型集成和多 Agent 协作编排，适合构建企业级 AI 工作流和团队协作场景。

**技术亮点**:
- 多 Agent 协作框架：支持多个 AI Agent 协同工作，提供 Agent 团队设计能力，将 Agent 作为工作交互的基本单元
- 多模型统一集成：同时支持 OpenAI GPT、Claude、DeepSeek、Gemini 等多种主流大语言模型，提供统一调用接口
- MCP (Model Context Protocol) 支持：内置 MCP 协议支持，可扩展连接各种外部工具和数据源
- TypeScript 全栈架构：采用 TypeScript 开发，从前端到后端保持类型安全，便于二次开发和定制
- 知识库与 RAG 能力：内置知识库功能，支持 RAG (检索增强生成)，可构建私有知识问答系统

**适用场景**:
- 企业级 AI 工作流自动化：使用多 Agent 协作构建复杂的业务流程自动化，如客户服务、数据分析、内容生成等场景
- 个人开发者 AI 助手搭建：开发者可基于 LobeHub 快速构建个人 AI 助手、工作流工具和自动化脚本
- 团队协作与知识管理：构建团队共享的 AI Agent 知识库，支持多人协作编辑和共享 Agent 配置



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,874 |
| 语言 | TypeScript |
| Forks | 5,781 |
| Issues | 6 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

这是一个极具创新性的 Claude Code 记忆增强插件，通过 AI 自动压缩编码会话历史并注入未来上下文，解决了 AI 编程助手缺乏长期记忆的核心痛点，Stars 高达 67,874 说明其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 智能上下文压缩：利用 Claude Agent SDK 实现 AI 驱动的会话摘要压缩，自动提取关键代码变更和决策
- 向量检索增强：集成 ChromaDB 向量数据库 + RAG 技术，支持语义化记忆检索，精准匹配历史上下文
- 多存储架构：结合 SQLite 本地持久化 + Embeddings 语义索引，兼顾数据安全与快速检索
- 无缝插件生态：专为 Claude Code 设计的插件架构，开箱即用，自动后台运行
- 记忆持久化：实现真正的长期记忆系统，让 AI 能够跨会话记住项目结构、代码习惯和问题解决方案

**适用场景**:
- 个人开发者：在长期项目中保持 AI 助手的上下文连贯性，避免重复解释项目背景和编码规范
- 企业级开发：团队成员共享项目记忆，新成员加入时 AI 可快速继承项目上下文和开发规范
- 复杂代码库维护：需要 AI 记住之前的技术选型、已解决的问题和代码修改历史，提升问题解决效率



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,775 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词社区项目，前身为Awesome ChatGPT Prompts，支持多种主流AI模型（ChatGPT、Claude、Gemini等），提供开源自托管部署方案，既适合个人用户发现优质提示词，也满足企业级隐私保护需求。

**技术亮点**:
- 基于Next.js和TypeScript构建现代化Web应用，具有良好的可维护性和扩展性
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 完全开源且支持自托管部署，企业可完全控制数据和隐私
- 采用TypeScript开发，提供完整的类型安全保证
- 社区驱动的提示词共享与发现机制，持续更新高质量提示词库

**适用场景**:
- 个人用户：发现、收藏和使用社区分享的优质AI提示词，提升工作效率
- 企业自托管：部署私有化提示词管理平台，保护商业机密和数据隐私
- AI开发者：学习提示词工程最佳实践，构建自己的提示词库和工具



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 48,213 |
| 语言 | HTML |
| Forks | 4,761 |
| Issues | 9 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |

---

这是一个拥有 48k+ Stars 的 Claude Code 最佳实践开源项目，系统性地梳理了从 vibe coding 到 agentic engineering 的进阶路径，提供了大量实用的 Claude Code 命令、技巧和工作流，适合希望深度掌握 AI 编程工具的开发者。

**技术亮点**:
- 完整的方法论体系：从基础的 vibe coding 实践逐步过渡到高级的 agentic engineering，覆盖 AI 辅助编程的完整学习曲线
- 丰富的 Claude Code 命令和技能库：包含大量经过实践验证的命令模板和使用技巧，帮助开发者高效使用 Claude Code
- Context Engineering 最佳实践：深入探讨如何通过上下文工程提升 AI 编程的准确性和效率
- Agentic Workflow 实现方案：提供 AI 代理工作流的设计模式和实现思路，支持复杂任务的自动化执行
- 多场景覆盖：涵盖 AI Agents、Claude Code Agents、Skill 开发等多个维度的最佳实践

**适用场景**:
- 企业级 AI 编程转型：帮助开发团队系统性地引入 Claude Code，建立规范的 AI 辅助开发流程和最佳实践
- 个人开发者效率提升：为希望深度掌握 Claude Code 的开发者提供丰富的命令模板、快捷键和工作流建议
- AI 编程技能培训：作为内部培训材料，帮助团队成员快速从传统编码过渡到 AI 辅助开发模式



### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择DeepSeek/OpenAI/Claude/Gemini/ MiniMax/Qwen/GLM/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,739 |
| 语言 | Python |
| Forks | 9,997 |
| Issues | 353 |
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
| Stars | 59,037 |
| 语言 | JavaScript |
| Forks | 6,378 |
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
| Stars | 72,116 |
| 语言 | Python |
| Forks | 9,104 |
| Issues | 411 |
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
| Stars | 54,261 |
| 语言 | TypeScript |
| Forks | 4,411 |
| Issues | 658 |
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
| Stars | 52,294 |
| 语言 | TypeScript |
| Forks | 24,225 |
| Issues | 825 |
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
| Stars | 78,206 |
| 语言 | Python |
| Forks | 16,114 |
| Issues | 4,489 |
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
| Stars | 147,379 |
| 语言 | Python |
| Forks | 8,853 |
| Issues | 958 |
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
| Stars | 56,452 |
| 语言 | Python |
| Forks | 6,077 |
| Issues | 560 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,058 |
| 语言 | Go |
| Forks | 15,817 |
| Issues | 3,069 |
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
| Stars | 91,504 |
| 语言 | Jupyter Notebook |
| Forks | 14,092 |
| Issues | 5 |
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
| Stars | 56,666 |
| 语言 | TypeScript |
| Forks | 9,319 |
| Issues | 108 |
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
| Stars | 48,164 |
| 语言 | Rust |
| Forks | 9,637 |
| Issues | 3 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,059 |
| 语言 | Python |
| Forks | 2,477 |
| Issues | 161 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,358 |
| 语言 | Python |
| Forks | 7,697 |
| Issues | 639 |
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
| Stars | 70,799 |
| 语言 | Python |
| Forks | 7,276 |
| Issues | 133 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


## 🧠 机器学习框架 (9 个项目) { #机器学习框架 }


### 🌟 高优先级


### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,634 |
| 语言 | Python |
| Forks | 8,635 |
| Issues | 993 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是一个经过 ACL 2024 学术会议验证的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供了从基础监督微调到高级 RLHF 的完整训练范式，且拥有 7 万+ 的社区星标，是目前最成熟、应用最广泛的开源 LLM 微调解决方案。

**技术亮点**:
- 统一微调框架：支持 Llama3、Gemma、Qwen、DeepSeek 等 100+ 主流 LLMs 及视觉语言模型，一套代码适配多种架构
- 高效微调技术栈：集成 LoRA、QLoRA、PEFT 等参数高效微调方法，大幅降低显存占用和计算成本
- 多样化训练范式：支持监督微调（SFT）、奖励模型训练、PPO/DPO 强化学习等多种 RLHF 技术
- 量化与部署：内置 AWQ/GPTQ 等量化方案，支持模型压缩后的快速部署
- 易用性与可扩展性：提供 Web UI 和 CLI 界面，支持自定义数据集和训练策略，模块化设计便于二次开发

**适用场景**:
- 企业级 LLM 定制：金融、医疗、教育等行业可基于开源基座模型微调专属领域助手，保护数据隐私的同时降低成本
- 学术研究与算法实验：研究者可快速复现 SFT、RLHF 等训练流程，聚焦算法创新而非工程实现
- 个人开发者与 AI 爱好者：借助预置模板和可视化界面，非专业团队也能完成模型微调任务



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,548 |
| 语言 | Python |
| Forks | 6,646 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是拥有 66k+ Stars 的成熟开源金融数据平台，集成 AI Agent 和机器学习能力，专为量化分析师和金融从业者提供从数据获取到智能投研的一站式解决方案

**技术亮点**:
- 多源金融数据统一接入：整合股票、加密货币、期权、固收、外汇等多元化数据源，提供标准化 API
- AI 与机器学习深度集成：内置 AI Agent 框架，支持自然语言查询和 ML 预测模型开发
- 专业量化金融工具库：提供技术指标、衍生品分析、经济数据计算等完整工具集
- 模块化可扩展架构：Python 原生设计，支持自定义数据源和分析模块定制
- 交互式可视化与报告生成：内置图表可视化和自动化投研报告输出功能

**适用场景**:
- 量化交易策略开发：回测、因子分析、衍生品定价和风险管理
- AI 智能投研：自然语言查询金融数据，自动生成投资研究报告
- 金融数据科学研究：ML/AI 模型预测、情绪分析和市场异常检测



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,775 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词社区项目，前身为Awesome ChatGPT Prompts，支持多种主流AI模型（ChatGPT、Claude、Gemini等），提供开源自托管部署方案，既适合个人用户发现优质提示词，也满足企业级隐私保护需求。

**技术亮点**:
- 基于Next.js和TypeScript构建现代化Web应用，具有良好的可维护性和扩展性
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 完全开源且支持自托管部署，企业可完全控制数据和隐私
- 采用TypeScript开发，提供完整的类型安全保证
- 社区驱动的提示词共享与发现机制，持续更新高质量提示词库

**适用场景**:
- 个人用户：发现、收藏和使用社区分享的优质AI提示词，提升工作效率
- 企业自托管：部署私有化提示词管理平台，保护商业机密和数据隐私
- AI开发者：学习提示词工程最佳实践，构建自己的提示词库和工具



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,948 |
| 语言 | Python |
| Forks | 33,019 |
| Issues | 2,353 |
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
| Stars | 78,206 |
| 语言 | Python |
| Forks | 16,114 |
| Issues | 4,489 |
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
| Stars | 110,189 |
| 语言 | Python |
| Forks | 12,854 |
| Issues | 3,985 |
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
| Stars | 99,454 |
| 语言 | Python |
| Forks | 27,598 |
| Issues | 18,567 |
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
| Stars | 91,504 |
| 语言 | Jupyter Notebook |
| Forks | 14,092 |
| Issues | 5 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,999 |
| 语言 | TypeScript |
| Forks | 3,699 |
| Issues | 299 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 🛠️ 开发工具 (14 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 167,520 |
| 语言 | JavaScript |
| Forks | 25,974 |
| Issues | 167 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专注于 AI 编程助手性能优化的综合工具链项目，通过 Skills、Instincts、Memory、Security 和 Research-First Development 五大核心模块，为 Claude Code、Cursor 等主流 AI 编程工具提供增强能力，项目获得高达 167,520 Stars，证明了其在开发者社区的广泛认可和实用价值。

**技术亮点**:
- 多模型支持框架：兼容 Claude Code、Codex、Opencode、Cursor 等多种 AI 编程助手，提供统一的任务编排和性能优化接口
- MCP 协议集成：基于 Model Context Protocol 实现标准化上下文管理，提升 AI 助手的理解能力和响应质量
- 安全沙箱机制：内置安全防护层，在保持高效的同时确保代码执行和权限控制的安全性
- 记忆系统设计：通过持久化记忆模块让 AI 助手能够跨会话学习和积累项目特定知识
- Research-First 开发理念：采用研究驱动的开发方法，持续优化 agent 性能基准和评估体系

**适用场景**:
- 企业级 AI 辅助开发：团队可在内部部署定制化 AI 编程工作流，结合安全机制保障代码质量
- 个人开发者提效：通过 Skills 和 Instincts 扩展能力，让 AI 助手更精准地适配个人编码习惯
- AI Agent 性能调优：研究者可基于该框架探索不同 AI 模型的性能边界，优化任务执行效率



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,842 |
| 语言 | Go |
| Forks | 4,026 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，无需 GPU 且兼容 OpenAI API，为企业和开发者提供了经济高效的私有化 AI 部署解决方案。

**技术亮点**:
- 多模态模型支持：同时支持文本生成（LLM）、图像生成（Stable Diffusion）、音频/语音合成（TTS、MusicGen）、目标检测等多种模型类型
- 跨硬件兼容性：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有的 AI 应用可零成本迁移
- Go 语言实现：利用 Go 的并发特性和高效性能，支持跨平台部署（Linux、Windows、macOS）
- 去中心化架构：支持 libp2p 分布式部署模式，适合构建去中心化 AI 服务网络

**适用场景**:
- 企业私有化 AI 部署：为对数据隐私有要求的企业提供本地运行的 AI 服务，支持敏感数据的本地处理
- 开发测试与成本优化：开发者可在本地环境进行 AI 应用开发测试，无需依赖云服务 API，显著降低开发和调试成本
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 能力，适合智能硬件、机器人等场景
- 个人 AI 助手：个人用户可在本地构建私有 AI 助手，支持语音交互、文档处理等多种功能



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,983 |
| 语言 | Java |
| Forks | 15,952 |
| Issues | 14 |
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
| Stars | 72,116 |
| 语言 | Python |
| Forks | 9,104 |
| Issues | 411 |
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
| Stars | 54,261 |
| 语言 | TypeScript |
| Forks | 4,411 |
| Issues | 658 |
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
| Stars | 185,677 |
| 语言 | TypeScript |
| Forks | 57,143 |
| Issues | 1,579 |
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
| Stars | 158,731 |
| 语言 | Python |
| Forks | 13,130 |
| Issues | 2,492 |
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
| Stars | 97,668 |
| 语言 | Python |
| Forks | 9,158 |
| Issues | 174 |
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
| Stars | 82,278 |
| 语言 | Python |
| Forks | 9,589 |
| Issues | 266 |
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
| Stars | 184,293 |
| 语言 | TypeScript |
| Forks | 39,456 |
| Issues | 16,677 |
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
| Stars | 94,196 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 311 |
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
| Stars | 79,039 |
| 语言 | TypeScript |
| Forks | 5,830 |
| Issues | 789 |
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
| Stars | 79,802 |
| 语言 | Go |
| Forks | 2,791 |
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
| Stars | 77,054 |
| 语言 | Go |
| Forks | 2,789 |
| Issues | 952 |
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
| Stars | 54,261 |
| 语言 | TypeScript |
| Forks | 4,411 |
| Issues | 658 |
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
| Stars | 185,677 |
| 语言 | TypeScript |
| Forks | 57,143 |
| Issues | 1,579 |
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
| Stars | 56,452 |
| 语言 | Python |
| Forks | 6,077 |
| Issues | 560 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,645 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 235 |
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
| Stars | 121,940 |
| 语言 | Go |
| Forks | 42,919 |
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
| Stars | 71,495 |
| 语言 | Go |
| Forks | 18,921 |
| Issues | 3,801 |
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
| Stars | 55,117 |
| 语言 | Go |
| Forks | 6,618 |
| Issues | 2,764 |
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
| Stars | 47,495 |
| 语言 | Go |
| Forks | 5,050 |
| Issues | 983 |
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
| Stars | 94,196 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 311 |
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
| Stars | 77,850 |
| 语言 | TypeScript |
| Forks | 6,797 |
| Issues | 422 |
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
| Stars | 85,947 |
| 语言 | JavaScript |
| Forks | 7,730 |
| Issues | 726 |
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
| Stars | 62,880 |
| 语言 | Go |
| Forks | 5,939 |
| Issues | 776 |
| Topics | consul, docker, etcd, go, golang, kubernetes, letsencrypt, load-balancer, marathon, mesos, microservice, reverse-proxy, traefik, zookeeper |
| 许可证 | MIT License |


### minio/minio

**描述**: MinIO is a high-performance, S3 compatible object store, open sourced under GNU AGPLv3 license.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 60,799 |
| 语言 | Go |
| Forks | 7,414 |
| Issues | 82 |
| Topics | amazon-s3, cloud, cloudnative, cloudstorage, go, k8s, kubernetes, multi-cloud, multi-cloud-kubernetes, objectstorage, s3, storage |
| 许可证 | GNU Affero General Public License v3.0 |


### usememos/memos

**描述**: Open-source, self-hosted note-taking tool built for quick capture. Markdown-native, lightweight, and fully yours.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,197 |
| 语言 | Go |
| Forks | 4,306 |
| Issues | 24 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### ⭐ 中优先级


### nektos/act

**描述**: Run your GitHub Actions locally 🚀

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 70,039 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 321 |
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
| Stars | 85,947 |
| 语言 | JavaScript |
| Forks | 7,730 |
| Issues | 726 |
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
| Stars | 63,788 |
| 语言 | Go |
| Forks | 10,365 |
| Issues | 751 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (11 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,842 |
| 语言 | Go |
| Forks | 4,026 |
| Issues | 161 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持在任意硬件上运行 LLM、图像生成、语音合成等多种 AI 模型，无需 GPU 且兼容 OpenAI API，为企业和开发者提供了经济高效的私有化 AI 部署解决方案。

**技术亮点**:
- 多模态模型支持：同时支持文本生成（LLM）、图像生成（Stable Diffusion）、音频/语音合成（TTS、MusicGen）、目标检测等多种模型类型
- 跨硬件兼容性：可在 CPU 上运行，无需昂贵 GPU，大幅降低 AI 部署门槛
- OpenAI API 兼容：提供与 OpenAI API 兼容的接口，现有的 AI 应用可零成本迁移
- Go 语言实现：利用 Go 的并发特性和高效性能，支持跨平台部署（Linux、Windows、macOS）
- 去中心化架构：支持 libp2p 分布式部署模式，适合构建去中心化 AI 服务网络

**适用场景**:
- 企业私有化 AI 部署：为对数据隐私有要求的企业提供本地运行的 AI 服务，支持敏感数据的本地处理
- 开发测试与成本优化：开发者可在本地环境进行 AI 应用开发测试，无需依赖云服务 API，显著降低开发和调试成本
- 边缘计算与物联网：在资源受限的边缘设备上部署轻量级 AI 能力，适合智能硬件、机器人等场景
- 个人 AI 助手：个人用户可在本地构建私有 AI 助手，支持语音交互、文档处理等多种功能



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,668 |
| 语言 | Python |
| Forks | 9,158 |
| Issues | 174 |
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
| Stars | 87,340 |
| 语言 | Python |
| Forks | 33,831 |
| Issues | 438 |
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
| Stars | 100,055 |
| 语言 | TypeScript |
| Forks | 27,186 |
| Issues | 1,137 |
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
| Stars | 79,039 |
| 语言 | TypeScript |
| Forks | 5,830 |
| Issues | 789 |
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
| Stars | 68,981 |
| 语言 | JavaScript |
| Forks | 23,174 |
| Issues | 208 |
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
| Stars | 55,955 |
| 语言 | JavaScript |
| Forks | 10,208 |
| Issues | 368 |
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
| Stars | 51,828 |
| 语言 | JavaScript |
| Forks | 4,707 |
| Issues | 1,469 |
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
| Stars | 88,382 |
| 语言 | Go |
| Forks | 8,582 |
| Issues | 679 |
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
| Stars | 71,856 |
| 语言 | Go |
| Forks | 4,704 |
| Issues | 237 |
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
| Stars | 57,985 |
| 语言 | Go |
| Forks | 3,331 |
| Issues | 18 |
| Topics | authentication, backend, golang, realtime |
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
| Stars | 101,460 |
| 语言 | TypeScript |
| Forks | 12,188 |
| Issues | 958 |
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
| Stars | 59,037 |
| 语言 | JavaScript |
| Forks | 6,378 |
| Issues | 341 |
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
| Stars | 43,998 |
| 语言 | Go |
| Forks | 3,980 |
| Issues | 1,096 |
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
| Stars | 51,645 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 235 |
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
| Stars | 160,775 |
| 语言 | HTML |
| Forks | 21,023 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

这是一个拥有超过16万Stars的热门AI提示词社区项目，前身为Awesome ChatGPT Prompts，支持多种主流AI模型（ChatGPT、Claude、Gemini等），提供开源自托管部署方案，既适合个人用户发现优质提示词，也满足企业级隐私保护需求。

**技术亮点**:
- 基于Next.js和TypeScript构建现代化Web应用，具有良好的可维护性和扩展性
- 支持多AI模型集成，包括ChatGPT、Claude、Gemini、GPT-4等主流LLM平台
- 完全开源且支持自托管部署，企业可完全控制数据和隐私
- 采用TypeScript开发，提供完整的类型安全保证
- 社区驱动的提示词共享与发现机制，持续更新高质量提示词库

**适用场景**:
- 个人用户：发现、收藏和使用社区分享的优质AI提示词，提升工作效率
- 企业自托管：部署私有化提示词管理平台，保护商业机密和数据隐私
- AI开发者：学习提示词工程最佳实践，构建自己的提示词库和工具



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,826 |
| 语言 | Python |
| Forks | 4,898 |
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
| Stars | 56,666 |
| 语言 | TypeScript |
| Forks | 9,319 |
| Issues | 108 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 47,059 |
| 语言 | Python |
| Forks | 2,477 |
| Issues | 161 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 89,801 |
| 语言 | TypeScript |
| Forks | 10,031 |
| Issues | 2,269 |
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
| Stars | 87,634 |
| 语言 | TypeScript |
| Forks | 8,910 |
| Issues | 1,645 |
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
| Stars | 127,587 |
| 语言 | JavaScript |
| Forks | 12,479 |
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
| Stars | 171,067 |
| 语言 | Go |
| Forks | 13,171 |
| Issues | 180 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


## 📁 其他 (66 个项目) { #其他 }


### 🌟 高优先级


### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 79,040 |
| 语言 | Python |
| Forks | 8,945 |
| Issues | 2,984 |
| Topics | llm-app |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,326 |
| 语言 | Python |
| Forks | 13,407 |
| Issues | 110 |
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
| Stars | 90,972 |
| 语言 | Python |
| Forks | 7,858 |
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
| Stars | 136,151 |
| 语言 | Unknown |
| Forks | 34,069 |
| Issues | 136 |
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
| Stars | 386,075 |
| 语言 | Python |
| Forks | 66,129 |
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
| Stars | 115,184 |
| 语言 | TypeScript |
| Forks | 6,005 |
| Issues | 27 |
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
| Stars | 113,635 |
| 语言 | TypeScript |
| Forks | 8,306 |
| Issues | 299 |
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
| Stars | 83,946 |
| 语言 | TypeScript |
| Forks | 12,270 |
| Issues | 453 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,536 |
| 语言 | JavaScript |
| Forks | 4,878 |
| Issues | 5 |
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
| Stars | 48,259 |
| 语言 | Go |
| Forks | 10,326 |
| Issues | 1,898 |
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
| Stars | 106,741 |
| 语言 | C++ |
| Forks | 17,396 |
| Issues | 1,533 |
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
| Stars | 63,401 |
| 语言 | Python |
| Forks | 1,632 |
| Issues | 28 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### forrestchang/andrej-karpathy-skills

**描述**: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 86/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,265 |
| 语言 | Unknown |
| Forks | 8,617 |
| Issues | 73 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 294,497 |
| 语言 | Python |
| Forks | 27,775 |
| Issues | 19 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### home-assistant/core

**描述**: :house_with_garden: Open source home automation that puts local control and privacy first.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,425 |
| 语言 | Python |
| Forks | 37,355 |
| Issues | 3,794 |
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
| Stars | 77,669 |
| 语言 | Python |
| Forks | 45,116 |
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
| Stars | 77,243 |
| 语言 | Python |
| Forks | 16,889 |
| Issues | 26 |
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
| Stars | 443,625 |
| 语言 | TypeScript |
| Forks | 44,390 |
| Issues | 177 |
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
| Stars | 353,680 |
| 语言 | TypeScript |
| Forks | 43,969 |
| Issues | 14 |
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
| Stars | 121,997 |
| 语言 | TypeScript |
| Forks | 13,439 |
| Issues | 3,014 |
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
| Stars | 113,042 |
| 语言 | TypeScript |
| Forks | 8,647 |
| Issues | 1,850 |
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
| Stars | 108,672 |
| 语言 | TypeScript |
| Forks | 13,371 |
| Issues | 5,036 |
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
| Stars | 98,672 |
| 语言 | TypeScript |
| Forks | 5,488 |
| Issues | 691 |
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
| Stars | 97,852 |
| 语言 | TypeScript |
| Forks | 54,595 |
| Issues | 1,365 |
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
| Stars | 94,767 |
| 语言 | TypeScript |
| Forks | 5,211 |
| Issues | 100 |
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
| Stars | 80,240 |
| 语言 | TypeScript |
| Forks | 8,097 |
| Issues | 721 |
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
| Stars | 244,706 |
| 语言 | JavaScript |
| Forks | 50,985 |
| Issues | 1,246 |
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
| Stars | 116,916 |
| 语言 | JavaScript |
| Forks | 35,435 |
| Issues | 2,649 |
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
| Stars | 112,190 |
| 语言 | JavaScript |
| Forks | 36,344 |
| Issues | 519 |
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
| Stars | 109,027 |
| 语言 | JavaScript |
| Forks | 11,654 |
| Issues | 194 |
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
| Stars | 98,239 |
| 语言 | JavaScript |
| Forks | 32,655 |
| Issues | 1,537 |
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
| Stars | 95,679 |
| 语言 | JavaScript |
| Forks | 15,407 |
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
| Stars | 86,428 |
| 语言 | JavaScript |
| Forks | 4,896 |
| Issues | 999 |
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
| Stars | 71,071 |
| 语言 | JavaScript |
| Forks | 16,806 |
| Issues | 894 |
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
| Stars | 65,786 |
| 语言 | JavaScript |
| Forks | 9,361 |
| Issues | 210 |
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
| Stars | 63,010 |
| 语言 | JavaScript |
| Forks | 4,030 |
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
| Stars | 61,259 |
| 语言 | JavaScript |
| Forks | 7,150 |
| Issues | 141 |
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
| Stars | 60,701 |
| 语言 | JavaScript |
| Forks | 5,658 |
| Issues | 65 |
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
| Stars | 59,841 |
| 语言 | JavaScript |
| Forks | 20,457 |
| Issues | 89 |
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
| Stars | 57,433 |
| 语言 | JavaScript |
| Forks | 12,306 |
| Issues | 26 |
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
| Stars | 53,194 |
| 语言 | JavaScript |
| Forks | 10,601 |
| Issues | 446 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,681 |
| 语言 | JavaScript |
| Forks | 11,512 |
| Issues | 248 |
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
| Stars | 133,643 |
| 语言 | Go |
| Forks | 18,947 |
| Issues | 9,974 |
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
| Stars | 106,111 |
| 语言 | Go |
| Forks | 15,020 |
| Issues | 37 |
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
| Stars | 87,786 |
| 语言 | Go |
| Forks | 8,249 |
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
| Stars | 83,159 |
| 语言 | Go |
| Forks | 5,125 |
| Issues | 383 |
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
| Stars | 68,610 |
| 语言 | Go |
| Forks | 3,226 |
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
| Stars | 56,868 |
| 语言 | Go |
| Forks | 5,057 |
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
| Stars | 50,999 |
| 语言 | Go |
| Forks | 21,895 |
| Issues | 414 |
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
| Stars | 50,810 |
| 语言 | Go |
| Forks | 1,607 |
| Issues | 273 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,370 |
| 语言 | Go |
| Forks | 7,949 |
| Issues | 565 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### v2ray/v2ray-core

**描述**: A platform for building proxies to bypass network restrictions.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,849 |
| 语言 | Go |
| Forks | 8,855 |
| Issues | 17 |
| Topics | golang, http-proxy, proxy, shadowsocks, socks, socks5, v2ray, vmess |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 87,310 |
| 语言 | Shell |
| Forks | 14,059 |
| Issues | 111 |
| 许可证 | MIT License |


### ⭐ 中优先级


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,242 |
| 语言 | Python |
| Forks | 50,424 |
| Issues | 930 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 98,448 |
| 语言 | Python |
| Forks | 12,102 |
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
| Stars | 86,316 |
| 语言 | Python |
| Forks | 7,245 |
| Issues | 487 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,033 |
| 语言 | TypeScript |
| Forks | 16,527 |
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
| Stars | 84,562 |
| 语言 | TypeScript |
| Forks | 10,512 |
| Issues | 390 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,273 |
| 语言 | TypeScript |
| Forks | 7,597 |
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
| Stars | 148,131 |
| 语言 | JavaScript |
| Forks | 26,710 |
| Issues | 159 |
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
| Stars | 79,173 |
| 语言 | JavaScript |
| Forks | 32,640 |
| Issues | 279 |
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
| Stars | 67,389 |
| 语言 | JavaScript |
| Forks | 11,956 |
| Issues | 554 |
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
| Stars | 66,343 |
| 语言 | JavaScript |
| Forks | 9,193 |
| Issues | 2 |
| Topics | angular, concepts, es6, es6-javascript, hacktoberfest, javascript, javascript-closures, javascript-engines, javascript-programming, nodejs, primitive-types, programming, react |
| 许可证 | MIT License |


### chinese-poetry/chinese-poetry

**描述**: The most comprehensive database of Chinese poetry 🧶最全中华古诗词数据库,  唐宋两朝近一万四千古诗人,  接近5.5万首唐诗加26万宋诗.  两宋时期1564位词人，21050首词。

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 51,317 |
| 语言 | JavaScript |
| Forks | 10,354 |
| Issues | 134 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### coreybutler/nvm-windows

**描述**: A node.js version management utility for Windows. Ironically written in Go.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 46,111 |
| 语言 | Go |
| Forks | 3,799 |
| Issues | 84 |
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
| Stars | 153,255 |
| 语言 | Python |
| Forks | 11,692 |
| Issues | 346 |
| Topics | awesome, github, hellogithub, python |
