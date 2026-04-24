# 项目发现报告 (2026-04-24)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 132 |
| 去重移除 | 33 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 16 |
| 💬 LLM 界面 | 24 |
| 🧠 机器学习框架 | 9 |
| 🛠️ 开发工具 | 15 |
| ⚙️ DevOps/基础设施 | 14 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 11 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
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
| Stars | 133,905 |
| 语言 | Python |
| Forks | 19,000 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持多种 LLM 后端（Ollama、OpenAI API 等），提供 RAG 检索增强生成、MCP 协议支持等企业级功能，同时界面美观易用，非常适合希望自托管 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 和 OpenAI API，可灵活切换不同的 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持基于私有知识库的智能问答
- MCP 协议支持：集成 Model Context Protocol 协议，可扩展连接多种外部工具和数据源
- 完全自托管：支持 Docker 一键部署，数据完全自主控制，满足隐私合规要求
- 丰富的 Web UI 功能：支持多用户管理、对话分组、模型参数配置、代码高亮等企业级特性

**适用场景**:
- 企业私有 AI 助手：企业可基于内部知识库部署私有 AI 对话系统，用于客服、文档检索、员工培训等场景
- 个人开发者本地 LLM 调试：配合 Ollama 在本地运行各种开源大模型，提供友好的调试界面
- 科研机构知识库问答：利用 RAG 功能构建领域专属的知识库问答系统，支持上传 PDF、文档等参考资料



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,958 |
| 语言 | Python |
| Forks | 16,847 |
| Issues | 6,769 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名AI研究组织 NousResearch 打造的多功能AI Agent框架，拥有超过11万Stars的高人气，支持Claude、GPT等多种主流LLM后端，提供统一的Agent开发接口和灵活的工具调用机制，非常适合构建复杂的企业级AI应用和个人开发者快速原型开发。

**技术亮点**:
- 多LLM后端集成：支持OpenAI GPT、Anthropic Claude等多个主流大语言模型，提供统一的抽象接口便于切换和比较不同模型效果
- 灵活的Agent架构：采用模块化设计，支持自定义工具、插件系统和行为策略，可根据需求扩展Agent能力
- 强大的工具调用能力：内置ReAct、Function Calling等Agent推理范式，支持复杂任务的分解和执行
- 丰富的生态集成：与Codex、Claude Code等专业工具深度集成，覆盖编程、数据库查询、多轮对话等场景
- 生产级代码质量：由专业AI研究团队维护，代码经过大规模实际应用验证，文档完善且持续更新

**适用场景**:
- 企业级AI应用开发：构建客服机器人、知识库问答系统、业务流程自动化等企业应用，利用多后端支持实现高可用部署
- 个人开发者快速原型：通过统一的Agent开发接口快速验证AI应用想法，结合LangChain等框架加速开发周期
- AI编程助手：基于支持的Codex和Claude Code集成，构建代码生成、代码审查、自动化测试等开发效率提升工具



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,933 |
| 语言 | Python |
| Forks | 8,930 |
| Issues | 2,982 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将先进的 RAG 技术与 Agent 能力深度融合，为大语言模型提供了卓越的上下文理解和检索能力。作为 Apache 2.0 许可的开源项目，它拥有活跃的社区生态和成熟的文档理解能力，能够高效处理复杂的企业级知识检索场景，是构建生产级 RAG 应用的理想选择。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，支持多跳推理和复杂任务规划
- 深度文档理解：内置先进的文档解析引擎，支持多种格式（PDF、Word、Excel等）的结构化信息提取
- GraphRAG 支持：集成图检索增强生成能力，能够捕捉实体关系和语义关联，提升复杂查询效果
- MCP 协议兼容：支持 Model Context Protocol，便于与各类 LLM 和工具生态集成
- Deep Research 能力：内置深度研究工作流，支持复杂问题的多轮检索和推理分析

**适用场景**:
- 企业知识库问答：构建智能客服、内部知识检索、政策文件查询等场景
- 复杂文档分析与研究：支持长文档摘要、多文档关联分析、深度研究报告生成
- RAG 应用开发与部署：为开发者提供完整的 RAG 流水线框架，支持快速构建和部署生产级应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,158 |
| 语言 | JavaScript |
| Forks | 25,787 |
| Issues | 160 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理设计的性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大模块显著提升 AI Agent 的开发效率和安全性，拥有超过 16 万 Stars 的社区认可度。

**技术亮点**:
- Skills 系统：模块化的 AI 技能扩展机制，支持自定义技能库以增强代理能力
- Instincts 本能层：内置的决策优化逻辑，让 AI 代理具备更智能的默认行为模式
- Memory 记忆管理：持久化上下文和会话状态，解决长对话中的信息丢失问题
- Security 安全框架：专为 AI Agent 设计的权限控制和沙箱机制，防止恶意代码执行
- MCP 协议支持：兼容 Model Context Protocol，实现跨平台 AI 工具的无缝集成

**适用场景**:
- 企业级 AI 编程助手部署：为企业开发团队提供统一的 AI 编码规范和安全审计
- 个人开发者效率提升：通过自定义 Skills 和 Memory 管理，打造个性化的 AI 编程搭档
- AI Agent 安全审计：利用 Security 模块对 AI 生成的代码进行权限控制和风险评估



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,785 |
| 语言 | Go |
| Forks | 4,010 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源 AI 引擎，支持 LLM、图像、音频、视频等多模态模型，且可在无 GPU 的普通硬件上运行，极大降低了私有化 AI 部署的门槛，拥有 45k+ Stars 证明其社区认可度高。

**技术亮点**:
- 多模态模型支持：同时支持文本生成(LLM/Llama/Mamba)、图像生成(Stable Diffusion)、音频合成(TTS/MusicGen)、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现 CPU 运行，无需昂贵 GPU 即可部署，降低了 AI 应用门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信和去中心化 AI 推理
- API 优先设计：提供统一的 REST API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- Go 语言实现：利用 Go 的并发优势实现高效推理，支持 MCP 协议扩展生态

**适用场景**:
- 企业私有化 AI 部署：在本地服务器运行 AI 模型，确保数据隐私和可控性，适合金融、医疗等敏感数据场景
- 边缘计算与 IoT：部署在资源受限的边缘设备上实现本地 AI 推理，降低网络延迟和带宽成本
- 个人开发者与学习者：在普通电脑上运行开源大模型，无需云服务订阅即可体验 AI 技术



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,597 |
| 语言 | TypeScript |
| Forks | 14,983 |
| Issues | 719 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub是目前最成熟的开源多Agent协作平台之一，其75K+ Stars的高人气证明了其在开发者社区的认可度，项目提供了从单Agent到多Agent团队的完整解决方案，特别适合需要构建复杂AI工作流的开发者和企业。

**技术亮点**:
- 多Agent协作框架：支持多个AI Agent之间的协同工作，实现了Agent团队设计和工作编排能力
- 多模型集成：原生支持OpenAI GPT、Claude、DeepSeek、Gemini等主流大模型，提供统一的调用接口
- MCP协议支持：实现了Model Context Protocol标准，便于扩展Agent能力和第三方集成
- 知识库集成：内置RAG能力，支持Agent访问和利用结构化知识，提升回答准确性
- 现代化全栈架构：基于TypeScript/React技术栈，提供完整的Web界面和API服务

**适用场景**:
- 企业AI助手搭建：利用多Agent协作能力构建企业内部智能助手，实现客服、文档处理、数据分析等任务的自动化
- AI工作流自动化：通过Agent团队编排实现复杂业务流程的自动化执行，适合需要多步骤处理的场景
- 个人开发者AI应用开发：提供即用的Agent框架和UI组件，大幅降低AI应用开发门槛



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,567 |
| 语言 | Python |
| Forks | 8,624 |
| Issues | 989 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是统一的大模型高效微调框架，支持100+ LLMs和VLMs的一站式微调，集成了LoRA、QLoRA、RLHF等主流技术，被ACL 2024接收，提供从预训练到指令微调的完整流程，让研究者和开发者能以极低门槛在消费级GPU上微调专属大模型。

**技术亮点**:
- 支持100+大语言模型和视觉语言模型的统一微调框架（LLaMA3、Qwen、DeepSeek、Gemma等）
- 集成LoRA、QLoRA、Freeze、RLHF（PPO/DPO/KTO）等参数高效微调方法
- 提供预训练、指令微调、奖励模型训练、SFT等端到端解决方案
- 支持AWQ、GPTQ等量化技术，大幅降低显存占用
- 兼容MoE混合专家架构，支持多模态视觉语言模型微调

**适用场景**:
- 企业AI应用：快速微调私有化大模型，定制客服、文档分析、代码生成等垂直场景模型
- 学术研究与实验：低成本验证新微调算法、训练策略和模型架构
- 个人开发者学习：在消费级GPU（RTX 3090/4090）上实践大模型微调技术



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,965 |
| 语言 | TypeScript |
| Forks | 5,681 |
| Issues | 154 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

该项目将长期记忆能力引入 AI 编码助手，解决了 Claude Code 等工具缺乏跨会话上下文记忆的核心痛点，通过 RAG 技术和向量数据库实现智能上下文召回，大幅提升 AI 辅助编码的连续性和效率。

**技术亮点**:
- 基于 Claude Agent-SDK 实现 AI 驱动的会话压缩，自动提取关键编码决策和操作
- 集成 ChromaDB 向量数据库，利用 Embeddings 技术实现语义级别的上下文检索
- 采用 RAG（检索增强生成）架构，将历史会话作为知识库注入 AI 响应
- 结合 SQLite 持久化存储与语义搜索，平衡查询性能与数据可靠性
- 作为 Claude Code 原生插件设计，无缝集成到开发工作流中

**适用场景**:
- 个人开发者维护项目上下文：长时间项目开发中，AI 能自动记住之前的架构决策、已解决的 bug 和代码逻辑，避免重复解释
- 复杂代码库导航：当项目规模较大时，帮助 AI 在新会话中快速理解项目结构和历史修改脉络
- 团队知识沉淀：自动记录和归纳编码会话中的最佳实践和技术决策，形成可检索的项目知识库



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,859 |
| 语言 | HTML |
| Forks | 4,715 |
| Issues | 8 |
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
| Stars | 43,691 |
| 语言 | Python |
| Forks | 9,986 |
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
| Stars | 45,968 |
| 语言 | Java |
| Forks | 15,945 |
| Issues | 17 |
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
| Stars | 40,398 |
| 语言 | Python |
| Forks | 4,841 |
| Issues | 98 |
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
| Stars | 39,046 |
| 语言 | Python |
| Forks | 6,193 |
| Issues | 69 |
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
| Stars | 112,024 |
| 语言 | TypeScript |
| Forks | 7,134 |
| Issues | 293 |
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
| Stars | 58,933 |
| 语言 | JavaScript |
| Forks | 6,362 |
| Issues | 352 |
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
| Stars | 72,001 |
| 语言 | Python |
| Forks | 9,076 |
| Issues | 408 |
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
| Stars | 53,957 |
| 语言 | TypeScript |
| Forks | 4,379 |
| Issues | 636 |
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
| Stars | 107,326 |
| 语言 | Python |
| Forks | 15,781 |
| Issues | 9 |
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
| Stars | 89,991 |
| 语言 | Python |
| Forks | 10,274 |
| Issues | 228 |
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
| Stars | 52,239 |
| 语言 | TypeScript |
| Forks | 24,213 |
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
| Stars | 185,448 |
| 语言 | TypeScript |
| Forks | 57,092 |
| Issues | 1,567 |
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
| Stars | 155,196 |
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
| Stars | 147,335 |
| 语言 | Python |
| Forks | 8,844 |
| Issues | 955 |
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
| Stars | 59,184 |
| 语言 | Jupyter Notebook |
| Forks | 20,088 |
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
| Stars | 56,072 |
| 语言 | Python |
| Forks | 6,019 |
| Issues | 549 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 56,246 |
| 语言 | TypeScript |
| Forks | 9,250 |
| Issues | 108 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 34,233 |
| 语言 | Python |
| Forks | 2,169 |
| Issues | 99 |
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
| Stars | 33,944 |
| 语言 | TypeScript |
| Forks | 3,680 |
| Issues | 295 |
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
| Stars | 33,135 |
| 语言 | TypeScript |
| Forks | 3,743 |
| Issues | 484 |
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
| Stars | 50,635 |
| 语言 | Rust |
| Forks | 3,255 |
| Issues | 576 |
| Topics | ai-tools, claude-code, codex, desktop-app, mcp, minimax, omo, open-source, openclaw, openclaw-ui, opencode, provider-management, rust, skills, skills-management, tauri, typescript, wsl-support |
| 许可证 | MIT License |


## 🔍 RAG/检索 (16 个项目) { #rag-检索 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,905 |
| 语言 | Python |
| Forks | 19,000 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持多种 LLM 后端（Ollama、OpenAI API 等），提供 RAG 检索增强生成、MCP 协议支持等企业级功能，同时界面美观易用，非常适合希望自托管 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 和 OpenAI API，可灵活切换不同的 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持基于私有知识库的智能问答
- MCP 协议支持：集成 Model Context Protocol 协议，可扩展连接多种外部工具和数据源
- 完全自托管：支持 Docker 一键部署，数据完全自主控制，满足隐私合规要求
- 丰富的 Web UI 功能：支持多用户管理、对话分组、模型参数配置、代码高亮等企业级特性

**适用场景**:
- 企业私有 AI 助手：企业可基于内部知识库部署私有 AI 对话系统，用于客服、文档检索、员工培训等场景
- 个人开发者本地 LLM 调试：配合 Ollama 在本地运行各种开源大模型，提供友好的调试界面
- 科研机构知识库问答：利用 RAG 功能构建领域专属的知识库问答系统，支持上传 PDF、文档等参考资料



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,933 |
| 语言 | Python |
| Forks | 8,930 |
| Issues | 2,982 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将先进的 RAG 技术与 Agent 能力深度融合，为大语言模型提供了卓越的上下文理解和检索能力。作为 Apache 2.0 许可的开源项目，它拥有活跃的社区生态和成熟的文档理解能力，能够高效处理复杂的企业级知识检索场景，是构建生产级 RAG 应用的理想选择。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，支持多跳推理和复杂任务规划
- 深度文档理解：内置先进的文档解析引擎，支持多种格式（PDF、Word、Excel等）的结构化信息提取
- GraphRAG 支持：集成图检索增强生成能力，能够捕捉实体关系和语义关联，提升复杂查询效果
- MCP 协议兼容：支持 Model Context Protocol，便于与各类 LLM 和工具生态集成
- Deep Research 能力：内置深度研究工作流，支持复杂问题的多轮检索和推理分析

**适用场景**:
- 企业知识库问答：构建智能客服、内部知识检索、政策文件查询等场景
- 复杂文档分析与研究：支持长文档摘要、多文档关联分析、深度研究报告生成
- RAG 应用开发与部署：为开发者提供完整的 RAG 流水线框架，支持快速构建和部署生产级应用



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,597 |
| 语言 | TypeScript |
| Forks | 14,983 |
| Issues | 719 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub是目前最成熟的开源多Agent协作平台之一，其75K+ Stars的高人气证明了其在开发者社区的认可度，项目提供了从单Agent到多Agent团队的完整解决方案，特别适合需要构建复杂AI工作流的开发者和企业。

**技术亮点**:
- 多Agent协作框架：支持多个AI Agent之间的协同工作，实现了Agent团队设计和工作编排能力
- 多模型集成：原生支持OpenAI GPT、Claude、DeepSeek、Gemini等主流大模型，提供统一的调用接口
- MCP协议支持：实现了Model Context Protocol标准，便于扩展Agent能力和第三方集成
- 知识库集成：内置RAG能力，支持Agent访问和利用结构化知识，提升回答准确性
- 现代化全栈架构：基于TypeScript/React技术栈，提供完整的Web界面和API服务

**适用场景**:
- 企业AI助手搭建：利用多Agent协作能力构建企业内部智能助手，实现客服、文档处理、数据分析等任务的自动化
- AI工作流自动化：通过Agent团队编排实现复杂业务流程的自动化执行，适合需要多步骤处理的场景
- 个人开发者AI应用开发：提供即用的Agent框架和UI组件，大幅降低AI应用开发门槛



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,965 |
| 语言 | TypeScript |
| Forks | 5,681 |
| Issues | 154 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

该项目将长期记忆能力引入 AI 编码助手，解决了 Claude Code 等工具缺乏跨会话上下文记忆的核心痛点，通过 RAG 技术和向量数据库实现智能上下文召回，大幅提升 AI 辅助编码的连续性和效率。

**技术亮点**:
- 基于 Claude Agent-SDK 实现 AI 驱动的会话压缩，自动提取关键编码决策和操作
- 集成 ChromaDB 向量数据库，利用 Embeddings 技术实现语义级别的上下文检索
- 采用 RAG（检索增强生成）架构，将历史会话作为知识库注入 AI 响应
- 结合 SQLite 持久化存储与语义搜索，平衡查询性能与数据可靠性
- 作为 Claude Code 原生插件设计，无缝集成到开发工作流中

**适用场景**:
- 个人开发者维护项目上下文：长时间项目开发中，AI 能自动记住之前的架构决策、已解决的 bug 和代码逻辑，避免重复解释
- 复杂代码库导航：当项目规模较大时，帮助 AI 在新会话中快速理解项目结构和历史修改脉络
- 团队知识沉淀：自动记录和归纳编码会话中的最佳实践和技术决策，形成可检索的项目知识库



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,968 |
| 语言 | Java |
| Forks | 15,945 |
| Issues | 17 |
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
| Stars | 40,398 |
| 语言 | Python |
| Forks | 4,841 |
| Issues | 98 |
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
| Stars | 39,046 |
| 语言 | Python |
| Forks | 6,193 |
| Issues | 69 |
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
| Stars | 101,369 |
| 语言 | TypeScript |
| Forks | 12,171 |
| Issues | 951 |
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
| Stars | 58,933 |
| 语言 | JavaScript |
| Forks | 6,362 |
| Issues | 352 |
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
| Stars | 107,326 |
| 语言 | Python |
| Forks | 15,781 |
| Issues | 9 |
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
| Stars | 76,462 |
| 语言 | Python |
| Forks | 10,311 |
| Issues | 238 |
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
| Stars | 52,239 |
| 语言 | TypeScript |
| Forks | 24,213 |
| Issues | 823 |
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
| Stars | 43,964 |
| 语言 | Go |
| Forks | 3,974 |
| Issues | 1,119 |
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
| Stars | 34,204 |
| 语言 | Python |
| Forks | 4,834 |
| Issues | 214 |
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
| Stars | 34,233 |
| 语言 | Python |
| Forks | 2,169 |
| Issues | 99 |
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
| Stars | 33,944 |
| 语言 | TypeScript |
| Forks | 3,680 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 💬 LLM 界面 (24 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 133,905 |
| 语言 | Python |
| Forks | 19,000 |
| Issues | 244 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个功能完备的开源 AI 界面，支持多种 LLM 后端（Ollama、OpenAI API 等），提供 RAG 检索增强生成、MCP 协议支持等企业级功能，同时界面美观易用，非常适合希望自托管 AI 助手的企业和个人开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 和 OpenAI API，可灵活切换不同的 LLM 提供商
- RAG 检索增强生成：内置文档处理和向量检索能力，支持基于私有知识库的智能问答
- MCP 协议支持：集成 Model Context Protocol 协议，可扩展连接多种外部工具和数据源
- 完全自托管：支持 Docker 一键部署，数据完全自主控制，满足隐私合规要求
- 丰富的 Web UI 功能：支持多用户管理、对话分组、模型参数配置、代码高亮等企业级特性

**适用场景**:
- 企业私有 AI 助手：企业可基于内部知识库部署私有 AI 对话系统，用于客服、文档检索、员工培训等场景
- 个人开发者本地 LLM 调试：配合 Ollama 在本地运行各种开源大模型，提供友好的调试界面
- 科研机构知识库问答：利用 RAG 功能构建领域专属的知识库问答系统，支持上传 PDF、文档等参考资料



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,958 |
| 语言 | Python |
| Forks | 16,847 |
| Issues | 6,769 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes Agent 是由知名AI研究组织 NousResearch 打造的多功能AI Agent框架，拥有超过11万Stars的高人气，支持Claude、GPT等多种主流LLM后端，提供统一的Agent开发接口和灵活的工具调用机制，非常适合构建复杂的企业级AI应用和个人开发者快速原型开发。

**技术亮点**:
- 多LLM后端集成：支持OpenAI GPT、Anthropic Claude等多个主流大语言模型，提供统一的抽象接口便于切换和比较不同模型效果
- 灵活的Agent架构：采用模块化设计，支持自定义工具、插件系统和行为策略，可根据需求扩展Agent能力
- 强大的工具调用能力：内置ReAct、Function Calling等Agent推理范式，支持复杂任务的分解和执行
- 丰富的生态集成：与Codex、Claude Code等专业工具深度集成，覆盖编程、数据库查询、多轮对话等场景
- 生产级代码质量：由专业AI研究团队维护，代码经过大规模实际应用验证，文档完善且持续更新

**适用场景**:
- 企业级AI应用开发：构建客服机器人、知识库问答系统、业务流程自动化等企业应用，利用多后端支持实现高可用部署
- 个人开发者快速原型：通过统一的Agent开发接口快速验证AI应用想法，结合LangChain等框架加速开发周期
- AI编程助手：基于支持的Codex和Claude Code集成，构建代码生成、代码审查、自动化测试等开发效率提升工具



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,933 |
| 语言 | Python |
| Forks | 8,930 |
| Issues | 2,982 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-understanding, graphrag, harness, llm, mcp, ollama, openai, openclaw, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 将先进的 RAG 技术与 Agent 能力深度融合，为大语言模型提供了卓越的上下文理解和检索能力。作为 Apache 2.0 许可的开源项目，它拥有活跃的社区生态和成熟的文档理解能力，能够高效处理复杂的企业级知识检索场景，是构建生产级 RAG 应用的理想选择。

**技术亮点**:
- RAG + Agent 融合架构：创新性地将检索增强生成与 Agent 能力结合，支持多跳推理和复杂任务规划
- 深度文档理解：内置先进的文档解析引擎，支持多种格式（PDF、Word、Excel等）的结构化信息提取
- GraphRAG 支持：集成图检索增强生成能力，能够捕捉实体关系和语义关联，提升复杂查询效果
- MCP 协议兼容：支持 Model Context Protocol，便于与各类 LLM 和工具生态集成
- Deep Research 能力：内置深度研究工作流，支持复杂问题的多轮检索和推理分析

**适用场景**:
- 企业知识库问答：构建智能客服、内部知识检索、政策文件查询等场景
- 复杂文档分析与研究：支持长文档摘要、多文档关联分析、深度研究报告生成
- RAG 应用开发与部署：为开发者提供完整的 RAG 流水线框架，支持快速构建和部署生产级应用



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,158 |
| 语言 | JavaScript |
| Forks | 25,787 |
| Issues | 160 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理设计的性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大模块显著提升 AI Agent 的开发效率和安全性，拥有超过 16 万 Stars 的社区认可度。

**技术亮点**:
- Skills 系统：模块化的 AI 技能扩展机制，支持自定义技能库以增强代理能力
- Instincts 本能层：内置的决策优化逻辑，让 AI 代理具备更智能的默认行为模式
- Memory 记忆管理：持久化上下文和会话状态，解决长对话中的信息丢失问题
- Security 安全框架：专为 AI Agent 设计的权限控制和沙箱机制，防止恶意代码执行
- MCP 协议支持：兼容 Model Context Protocol，实现跨平台 AI 工具的无缝集成

**适用场景**:
- 企业级 AI 编程助手部署：为企业开发团队提供统一的 AI 编码规范和安全审计
- 个人开发者效率提升：通过自定义 Skills 和 Memory 管理，打造个性化的 AI 编程搭档
- AI Agent 安全审计：利用 Security 模块对 AI 生成的代码进行权限控制和风险评估



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,597 |
| 语言 | TypeScript |
| Forks | 14,983 |
| Issues | 719 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub是目前最成熟的开源多Agent协作平台之一，其75K+ Stars的高人气证明了其在开发者社区的认可度，项目提供了从单Agent到多Agent团队的完整解决方案，特别适合需要构建复杂AI工作流的开发者和企业。

**技术亮点**:
- 多Agent协作框架：支持多个AI Agent之间的协同工作，实现了Agent团队设计和工作编排能力
- 多模型集成：原生支持OpenAI GPT、Claude、DeepSeek、Gemini等主流大模型，提供统一的调用接口
- MCP协议支持：实现了Model Context Protocol标准，便于扩展Agent能力和第三方集成
- 知识库集成：内置RAG能力，支持Agent访问和利用结构化知识，提升回答准确性
- 现代化全栈架构：基于TypeScript/React技术栈，提供完整的Web界面和API服务

**适用场景**:
- 企业AI助手搭建：利用多Agent协作能力构建企业内部智能助手，实现客服、文档处理、数据分析等任务的自动化
- AI工作流自动化：通过Agent团队编排实现复杂业务流程的自动化执行，适合需要多步骤处理的场景
- 个人开发者AI应用开发：提供即用的Agent框架和UI组件，大幅降低AI应用开发门槛



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,965 |
| 语言 | TypeScript |
| Forks | 5,681 |
| Issues | 154 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

该项目将长期记忆能力引入 AI 编码助手，解决了 Claude Code 等工具缺乏跨会话上下文记忆的核心痛点，通过 RAG 技术和向量数据库实现智能上下文召回，大幅提升 AI 辅助编码的连续性和效率。

**技术亮点**:
- 基于 Claude Agent-SDK 实现 AI 驱动的会话压缩，自动提取关键编码决策和操作
- 集成 ChromaDB 向量数据库，利用 Embeddings 技术实现语义级别的上下文检索
- 采用 RAG（检索增强生成）架构，将历史会话作为知识库注入 AI 响应
- 结合 SQLite 持久化存储与语义搜索，平衡查询性能与数据可靠性
- 作为 Claude Code 原生插件设计，无缝集成到开发工作流中

**适用场景**:
- 个人开发者维护项目上下文：长时间项目开发中，AI 能自动记住之前的架构决策、已解决的 bug 和代码逻辑，避免重复解释
- 复杂代码库导航：当项目规模较大时，帮助 AI 在新会话中快速理解项目结构和历史修改脉络
- 团队知识沉淀：自动记录和归纳编码会话中的最佳实践和技术决策，形成可检索的项目知识库



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,555 |
| 语言 | HTML |
| Forks | 21,006 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

一个拥有超过 16 万星标的巨型提示词社区平台，支持 ChatGPT、Claude、Gemini 等多款主流 AI 模型，提供开源自托管部署方案，适合企业和个人在保护隐私的前提下高效管理和复用优质提示词资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，提供良好的开发体验和类型安全
- 支持多 AI 模型生态（ChatGPT/Claude/Gemini），统一管理不同模型的提示词格式
- 开源可自托管部署，支持 Docker 等方式快速私有化部署，适合企业内网使用
- 精心设计的提示词分类和搜索系统，便于社区发现和复用优质内容
- API 驱动的架构设计，支持与现有系统集成和自动化工作流

**适用场景**:
- 企业团队：内部知识库和提示词管理，敏感业务场景下的私有化部署，避免数据外泄
- AI 开发者：探索和学习各种场景下的最佳提示词实践，提升 prompt engineering 技能
- 内容创作者：寻找灵感并复用经过社区验证的高质量提示词，提升创作效率



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,859 |
| 语言 | HTML |
| Forks | 4,715 |
| Issues | 8 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,722 |
| 语言 | Python |
| Forks | 2,388 |
| Issues | 147 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### zhayujie/CowAgent

**描述**: CowAgent (chatgpt-on-wechat) 是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、通过长期记忆和知识库不断成长，比OpenClaw更轻量和便捷。同时支持微信、飞书、钉钉、企微、QQ、公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助理和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,691 |
| 语言 | Python |
| Forks | 9,986 |
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
| Stars | 58,933 |
| 语言 | JavaScript |
| Forks | 6,362 |
| Issues | 352 |
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
| Stars | 72,001 |
| 语言 | Python |
| Forks | 9,076 |
| Issues | 408 |
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
| Stars | 53,957 |
| 语言 | TypeScript |
| Forks | 4,379 |
| Issues | 636 |
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
| Stars | 52,239 |
| 语言 | TypeScript |
| Forks | 24,213 |
| Issues | 823 |
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
| Stars | 78,019 |
| 语言 | Python |
| Forks | 16,037 |
| Issues | 4,444 |
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
| Stars | 147,335 |
| 语言 | Python |
| Forks | 8,844 |
| Issues | 955 |
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
| Stars | 56,072 |
| 语言 | Python |
| Forks | 6,019 |
| Issues | 549 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,902 |
| 语言 | Go |
| Forks | 15,777 |
| Issues | 3,052 |
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
| Stars | 91,357 |
| 语言 | Jupyter Notebook |
| Forks | 14,062 |
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
| Stars | 56,246 |
| 语言 | TypeScript |
| Forks | 9,250 |
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
| Stars | 48,122 |
| 语言 | Rust |
| Forks | 9,621 |
| Issues | 1 |
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
| Stars | 34,233 |
| 语言 | Python |
| Forks | 2,169 |
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
| Stars | 116,522 |
| 语言 | Python |
| Forks | 7,625 |
| Issues | 638 |
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
| Stars | 70,065 |
| 语言 | Python |
| Forks | 7,167 |
| Issues | 122 |
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
| Stars | 70,567 |
| 语言 | Python |
| Forks | 8,624 |
| Issues | 989 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是统一的大模型高效微调框架，支持100+ LLMs和VLMs的一站式微调，集成了LoRA、QLoRA、RLHF等主流技术，被ACL 2024接收，提供从预训练到指令微调的完整流程，让研究者和开发者能以极低门槛在消费级GPU上微调专属大模型。

**技术亮点**:
- 支持100+大语言模型和视觉语言模型的统一微调框架（LLaMA3、Qwen、DeepSeek、Gemma等）
- 集成LoRA、QLoRA、Freeze、RLHF（PPO/DPO/KTO）等参数高效微调方法
- 提供预训练、指令微调、奖励模型训练、SFT等端到端解决方案
- 支持AWQ、GPTQ等量化技术，大幅降低显存占用
- 兼容MoE混合专家架构，支持多模态视觉语言模型微调

**适用场景**:
- 企业AI应用：快速微调私有化大模型，定制客服、文档分析、代码生成等垂直场景模型
- 学术研究与实验：低成本验证新微调算法、训练策略和模型架构
- 个人开发者学习：在消费级GPU（RTX 3090/4090）上实践大模型微调技术



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,458 |
| 语言 | Python |
| Forks | 6,633 |
| Issues | 74 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是量化金融领域最受欢迎的开源平台之一，提供涵盖股票、加密货币、期权、衍生品等多资产类别的统一数据接口和高级分析工具，尤其适合需要快速构建量化策略和 AI 驱动交易系统的开发者。

**技术亮点**:
- 统一数据抽象层：集成多个主流金融数据源（Yahoo Finance、Alpha Vantage、Bloomberg等），提供标准化的 API 接口，支持股票、债券、期权、加密货币等多资产类别数据获取
- 模块化架构设计：采用高度解耦的 extension 机制，用户可通过插件系统灵活扩展数据源、图表库和分析工具，支持自定义指标和回测引擎
- AI/ML 深度集成：内置机器学习模型用于情绪分析、预测建模和因子挖掘，支持与 LangChain、AutoGPT 等 AI 框架无缝集成，构建智能投研助手
- 丰富的量化分析工具：提供专业技术指标库、事件研究、回测框架、因子分析和风险度量功能，满足从数据探索到策略验证的全流程需求
- 交互式可视化能力：基于 Plotly 的动态图表系统，支持 K 线图、技术指标叠加、期权定价曲面等专业金融可视化，支持 Jupyter Notebook 和 CLI 多端输出

**适用场景**:
- 量化研究与策略开发：量化分析师可快速获取多市场数据、计算技术指标、进行因子分析和策略回测，大幅缩短从想法到验证的周期
- AI 量化交易代理：开发者可基于 OpenBB 构建自动化交易系统，利用其标准化的数据 API 和 AI 集成能力，为 AI 代理提供实时市场分析和决策支持
- 投资组合风险分析：机构或个人投资者可使用该平台进行资产配置优化、风险度量（如 VaR、CVaR）和业绩归因分析



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,555 |
| 语言 | HTML |
| Forks | 21,006 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

一个拥有超过 16 万星标的巨型提示词社区平台，支持 ChatGPT、Claude、Gemini 等多款主流 AI 模型，提供开源自托管部署方案，适合企业和个人在保护隐私的前提下高效管理和复用优质提示词资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，提供良好的开发体验和类型安全
- 支持多 AI 模型生态（ChatGPT/Claude/Gemini），统一管理不同模型的提示词格式
- 开源可自托管部署，支持 Docker 等方式快速私有化部署，适合企业内网使用
- 精心设计的提示词分类和搜索系统，便于社区发现和复用优质内容
- API 驱动的架构设计，支持与现有系统集成和自动化工作流

**适用场景**:
- 企业团队：内部知识库和提示词管理，敏感业务场景下的私有化部署，避免数据外泄
- AI 开发者：探索和学习各种场景下的最佳提示词实践，提升 prompt engineering 技能
- 内容创作者：寻找灵感并复用经过社区验证的高质量提示词，提升创作效率



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 159,879 |
| 语言 | Python |
| Forks | 33,003 |
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
| Stars | 78,019 |
| 语言 | Python |
| Forks | 16,037 |
| Issues | 4,444 |
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
| Stars | 109,940 |
| 语言 | Python |
| Forks | 12,812 |
| Issues | 3,978 |
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
| Stars | 99,416 |
| 语言 | Python |
| Forks | 27,585 |
| Issues | 18,568 |
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
| Stars | 91,357 |
| 语言 | Jupyter Notebook |
| Forks | 14,062 |
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
| Stars | 33,944 |
| 语言 | TypeScript |
| Forks | 3,680 |
| Issues | 295 |
| Topics | ai-agents, ai-search-engine, answering-engine, artificial-intelligence, llm, machine-learning, open-source-ai-search-engine, perplexica, rag, search-engine, searxng, searxng-copilot, self-hosted-ai, vane |
| 许可证 | MIT License |


## 🛠️ 开发工具 (15 个项目) { #开发工具 }


### 🌟 高优先级


### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 166,158 |
| 语言 | JavaScript |
| Forks | 25,787 |
| Issues | 160 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个专为 AI 编程代理设计的性能优化系统，通过 Skills、Instincts、Memory 和 Security 四大模块显著提升 AI Agent 的开发效率和安全性，拥有超过 16 万 Stars 的社区认可度。

**技术亮点**:
- Skills 系统：模块化的 AI 技能扩展机制，支持自定义技能库以增强代理能力
- Instincts 本能层：内置的决策优化逻辑，让 AI 代理具备更智能的默认行为模式
- Memory 记忆管理：持久化上下文和会话状态，解决长对话中的信息丢失问题
- Security 安全框架：专为 AI Agent 设计的权限控制和沙箱机制，防止恶意代码执行
- MCP 协议支持：兼容 Model Context Protocol，实现跨平台 AI 工具的无缝集成

**适用场景**:
- 企业级 AI 编程助手部署：为企业开发团队提供统一的 AI 编码规范和安全审计
- 个人开发者效率提升：通过自定义 Skills 和 Memory 管理，打造个性化的 AI 编程搭档
- AI Agent 安全审计：利用 Security 模块对 AI 生成的代码进行权限控制和风险评估



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,785 |
| 语言 | Go |
| Forks | 4,010 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源 AI 引擎，支持 LLM、图像、音频、视频等多模态模型，且可在无 GPU 的普通硬件上运行，极大降低了私有化 AI 部署的门槛，拥有 45k+ Stars 证明其社区认可度高。

**技术亮点**:
- 多模态模型支持：同时支持文本生成(LLM/Llama/Mamba)、图像生成(Stable Diffusion)、音频合成(TTS/MusicGen)、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现 CPU 运行，无需昂贵 GPU 即可部署，降低了 AI 应用门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信和去中心化 AI 推理
- API 优先设计：提供统一的 REST API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- Go 语言实现：利用 Go 的并发优势实现高效推理，支持 MCP 协议扩展生态

**适用场景**:
- 企业私有化 AI 部署：在本地服务器运行 AI 模型，确保数据隐私和可控性，适合金融、医疗等敏感数据场景
- 边缘计算与 IoT：部署在资源受限的边缘设备上实现本地 AI 推理，降低网络延迟和带宽成本
- 个人开发者与学习者：在普通电脑上运行开源大模型，无需云服务订阅即可体验 AI 技术



### jeecgboot/JeecgBoot

**描述**: 一款 AI 驱动的低代码平台，提供"零代码"与"代码生成"双模式——零代码模式一句话搭建系统，代码生成模式自动输出前后端代码与建表 SQL，生成即可运行。平台内置 AI 聊天助手、AI大模型、知识库、AI流程编排、MCP 与插件体系，兼容主流大模型，支持一句话生成流程图、设计表单、聊天式业务操作，解决 Java 项目 80% 重复工作，高效且不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,968 |
| 语言 | Java |
| Forks | 15,945 |
| Issues | 17 |
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
| Stars | 72,001 |
| 语言 | Python |
| Forks | 9,076 |
| Issues | 408 |
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
| Stars | 53,957 |
| 语言 | TypeScript |
| Forks | 4,379 |
| Issues | 636 |
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
| Stars | 185,448 |
| 语言 | TypeScript |
| Forks | 57,092 |
| Issues | 1,567 |
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
| Stars | 158,425 |
| 语言 | Python |
| Forks | 13,113 |
| Issues | 2,484 |
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
| Stars | 97,613 |
| 语言 | Python |
| Forks | 9,148 |
| Issues | 171 |
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
| Stars | 81,854 |
| 语言 | Python |
| Forks | 9,532 |
| Issues | 257 |
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
| Stars | 184,225 |
| 语言 | TypeScript |
| Forks | 39,402 |
| Issues | 16,638 |
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
| Stars | 94,188 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 306 |
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
| Stars | 79,024 |
| 语言 | TypeScript |
| Forks | 5,827 |
| Issues | 777 |
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
| Stars | 79,766 |
| 语言 | Go |
| Forks | 2,789 |
| Issues | 312 |
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
| Stars | 76,984 |
| 语言 | Go |
| Forks | 2,784 |
| Issues | 960 |
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
| Stars | 44,030 |
| 语言 | Go |
| Forks | 8,326 |
| Issues | 978 |
| Topics | cli, git, github-api-v4, golang |
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
| Stars | 53,957 |
| 语言 | TypeScript |
| Forks | 4,379 |
| Issues | 636 |
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
| Stars | 185,448 |
| 语言 | TypeScript |
| Forks | 57,092 |
| Issues | 1,567 |
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
| Stars | 56,072 |
| 语言 | Python |
| Forks | 6,019 |
| Issues | 549 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, gemini-cli, mcp, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,629 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 236 |
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
| Stars | 121,902 |
| 语言 | Go |
| Forks | 42,911 |
| Issues | 2,695 |
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
| Stars | 71,487 |
| 语言 | Go |
| Forks | 18,920 |
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
| Stars | 55,089 |
| 语言 | Go |
| Forks | 6,612 |
| Issues | 2,761 |
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
| Stars | 47,489 |
| 语言 | Go |
| Forks | 5,050 |
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
| Stars | 94,188 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 306 |
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
| Stars | 77,766 |
| 语言 | TypeScript |
| Forks | 6,783 |
| Issues | 414 |
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
| Stars | 85,848 |
| 语言 | JavaScript |
| Forks | 7,723 |
| Issues | 728 |
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
| Stars | 70,022 |
| 语言 | Go |
| Forks | 1,920 |
| Issues | 321 |
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
| Stars | 62,855 |
| 语言 | Go |
| Forks | 5,937 |
| Issues | 770 |
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
| Stars | 59,148 |
| 语言 | Go |
| Forks | 4,298 |
| Issues | 27 |
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
| Stars | 85,848 |
| 语言 | JavaScript |
| Forks | 7,723 |
| Issues | 728 |
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
| Stars | 63,765 |
| 语言 | Go |
| Forks | 10,356 |
| Issues | 748 |
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
| Stars | 45,785 |
| 语言 | Go |
| Forks | 4,010 |
| Issues | 170 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能完备的开源 AI 引擎，支持 LLM、图像、音频、视频等多模态模型，且可在无 GPU 的普通硬件上运行，极大降低了私有化 AI 部署的门槛，拥有 45k+ Stars 证明其社区认可度高。

**技术亮点**:
- 多模态模型支持：同时支持文本生成(LLM/Llama/Mamba)、图像生成(Stable Diffusion)、音频合成(TTS/MusicGen)、目标检测等多种 AI 任务
- 硬件无关性：通过优化实现 CPU 运行，无需昂贵 GPU 即可部署，降低了 AI 应用门槛
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络通信和去中心化 AI 推理
- API 优先设计：提供统一的 REST API 接口，兼容 OpenAI API 规范，便于现有应用快速迁移集成
- Go 语言实现：利用 Go 的并发优势实现高效推理，支持 MCP 协议扩展生态

**适用场景**:
- 企业私有化 AI 部署：在本地服务器运行 AI 模型，确保数据隐私和可控性，适合金融、医疗等敏感数据场景
- 边缘计算与 IoT：部署在资源受限的边缘设备上实现本地 AI 推理，降低网络延迟和带宽成本
- 个人开发者与学习者：在普通电脑上运行开源大模型，无需云服务订阅即可体验 AI 技术



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 97,613 |
| 语言 | Python |
| Forks | 9,148 |
| Issues | 171 |
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
| Stars | 87,323 |
| 语言 | Python |
| Forks | 33,827 |
| Issues | 431 |
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
| Stars | 100,049 |
| 语言 | TypeScript |
| Forks | 27,184 |
| Issues | 1,126 |
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
| Stars | 79,024 |
| 语言 | TypeScript |
| Forks | 5,827 |
| Issues | 777 |
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
| Stars | 68,973 |
| 语言 | JavaScript |
| Forks | 23,166 |
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
| Stars | 55,956 |
| 语言 | JavaScript |
| Forks | 10,212 |
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
| Stars | 51,820 |
| 语言 | JavaScript |
| Forks | 4,708 |
| Issues | 1,468 |
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
| Stars | 88,370 |
| 语言 | Go |
| Forks | 8,580 |
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
| Stars | 71,809 |
| 语言 | Go |
| Forks | 4,703 |
| Issues | 244 |
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
| Stars | 57,912 |
| 语言 | Go |
| Forks | 3,325 |
| Issues | 16 |
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
| Stars | 101,369 |
| 语言 | TypeScript |
| Forks | 12,171 |
| Issues | 951 |
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
| Stars | 58,933 |
| 语言 | JavaScript |
| Forks | 6,362 |
| Issues | 352 |
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
| Stars | 43,964 |
| 语言 | Go |
| Forks | 3,974 |
| Issues | 1,119 |
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
| Stars | 51,629 |
| 语言 | Go |
| Forks | 10,325 |
| Issues | 236 |
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
| Stars | 160,555 |
| 语言 | HTML |
| Forks | 21,006 |
| Issues | 42 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

一个拥有超过 16 万星标的巨型提示词社区平台，支持 ChatGPT、Claude、Gemini 等多款主流 AI 模型，提供开源自托管部署方案，适合企业和个人在保护隐私的前提下高效管理和复用优质提示词资源。

**技术亮点**:
- 基于 Next.js + TypeScript 的现代化全栈架构，提供良好的开发体验和类型安全
- 支持多 AI 模型生态（ChatGPT/Claude/Gemini），统一管理不同模型的提示词格式
- 开源可自托管部署，支持 Docker 等方式快速私有化部署，适合企业内网使用
- 精心设计的提示词分类和搜索系统，便于社区发现和复用优质内容
- API 驱动的架构设计，支持与现有系统集成和自动化工作流

**适用场景**:
- 企业团队：内部知识库和提示词管理，敏感业务场景下的私有化部署，避免数据外泄
- AI 开发者：探索和学习各种场景下的最佳提示词实践，提升 prompt engineering 技能
- 内容创作者：寻找灵感并复用经过社区验证的高质量提示词，提升创作效率



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,722 |
| 语言 | Python |
| Forks | 2,388 |
| Issues | 147 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,398 |
| 语言 | Python |
| Forks | 4,841 |
| Issues | 98 |
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
| Stars | 56,246 |
| 语言 | TypeScript |
| Forks | 9,250 |
| Issues | 108 |
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
| Stars | 89,791 |
| 语言 | TypeScript |
| Forks | 10,028 |
| Issues | 2,261 |
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
| Stars | 87,618 |
| 语言 | TypeScript |
| Forks | 8,903 |
| Issues | 1,633 |
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
| Stars | 127,565 |
| 语言 | JavaScript |
| Forks | 12,480 |
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
| Stars | 170,888 |
| 语言 | Go |
| Forks | 13,177 |
| Issues | 180 |
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
| Stars | 135,996 |
| 语言 | Unknown |
| Forks | 34,053 |
| Issues | 138 |
| Topics | ai, bolt, cluely, copilot, cursor, cursorai, devin, github-copilot, lovable, open-source, perplexity, replit, system-prompts, trae, trae-ai, trae-ide, v0, vscode, windsurf, windsurf-ai |
| 许可证 | GNU General Public License v3.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,204 |
| 语言 | Python |
| Forks | 13,394 |
| Issues | 108 |
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
| Stars | 90,694 |
| 语言 | Python |
| Forks | 7,821 |
| Issues | 626 |
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
| Stars | 385,984 |
| 语言 | Python |
| Forks | 66,123 |
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
| Stars | 115,118 |
| 语言 | TypeScript |
| Forks | 5,999 |
| Issues | 15 |
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
| Stars | 113,168 |
| 语言 | TypeScript |
| Forks | 8,277 |
| Issues | 297 |
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
| Stars | 82,445 |
| 语言 | TypeScript |
| Forks | 11,955 |
| Issues | 429 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,047 |
| 语言 | JavaScript |
| Forks | 4,829 |
| Issues | 42 |
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
| Stars | 48,245 |
| 语言 | Go |
| Forks | 10,324 |
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
| Stars | 106,257 |
| 语言 | C++ |
| Forks | 17,317 |
| Issues | 1,530 |
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
| Stars | 63,417 |
| 语言 | Python |
| Forks | 1,631 |
| Issues | 29 |
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
| Stars | 83,290 |
| 语言 | Unknown |
| Forks | 7,946 |
| Issues | 72 |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 294,195 |
| 语言 | Python |
| Forks | 27,767 |
| Issues | 23 |
| Topics | awesome, collections, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,269 |
| 语言 | Python |
| Forks | 7,243 |
| Issues | 487 |
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
| Stars | 86,184 |
| 语言 | Python |
| Forks | 37,326 |
| Issues | 3,760 |
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
| Forks | 45,120 |
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
| Stars | 77,161 |
| 语言 | Python |
| Forks | 16,881 |
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
| Stars | 443,490 |
| 语言 | TypeScript |
| Forks | 44,377 |
| Issues | 181 |
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
| Stars | 353,532 |
| 语言 | TypeScript |
| Forks | 43,963 |
| Issues | 10 |
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
| Stars | 121,874 |
| 语言 | TypeScript |
| Forks | 13,425 |
| Issues | 3,009 |
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
| Stars | 112,942 |
| 语言 | TypeScript |
| Forks | 8,633 |
| Issues | 1,839 |
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
| Stars | 108,657 |
| 语言 | TypeScript |
| Forks | 13,361 |
| Issues | 5,028 |
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
| Stars | 98,540 |
| 语言 | TypeScript |
| Forks | 5,467 |
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
| Stars | 97,840 |
| 语言 | TypeScript |
| Forks | 54,599 |
| Issues | 1,366 |
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
| Stars | 94,739 |
| 语言 | TypeScript |
| Forks | 5,209 |
| Issues | 104 |
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
| Stars | 84,468 |
| 语言 | TypeScript |
| Forks | 10,487 |
| Issues | 379 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,186 |
| 语言 | TypeScript |
| Forks | 8,089 |
| Issues | 712 |
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
| Stars | 244,655 |
| 语言 | JavaScript |
| Forks | 50,974 |
| Issues | 1,243 |
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
| Stars | 116,885 |
| 语言 | JavaScript |
| Forks | 35,424 |
| Issues | 2,641 |
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
| Stars | 112,164 |
| 语言 | JavaScript |
| Forks | 36,340 |
| Issues | 521 |
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
| Stars | 109,029 |
| 语言 | JavaScript |
| Forks | 11,653 |
| Issues | 232 |
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
| Stars | 98,227 |
| 语言 | JavaScript |
| Forks | 32,665 |
| Issues | 1,533 |
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
| Stars | 95,662 |
| 语言 | JavaScript |
| Forks | 15,400 |
| Issues | 47 |
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
| Stars | 86,414 |
| 语言 | JavaScript |
| Forks | 4,895 |
| Issues | 997 |
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
| Stars | 71,064 |
| 语言 | JavaScript |
| Forks | 16,808 |
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
| Stars | 65,785 |
| 语言 | JavaScript |
| Forks | 9,362 |
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
| Stars | 62,969 |
| 语言 | JavaScript |
| Forks | 4,023 |
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
| Stars | 61,256 |
| 语言 | JavaScript |
| Forks | 7,149 |
| Issues | 140 |
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
| Stars | 60,681 |
| 语言 | JavaScript |
| Forks | 5,657 |
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
| Stars | 59,837 |
| 语言 | JavaScript |
| Forks | 20,459 |
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
| Stars | 57,428 |
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
| Stars | 53,187 |
| 语言 | JavaScript |
| Forks | 10,603 |
| Issues | 448 |
| 许可证 | Apache License 2.0 |


### TryGhost/Ghost

**描述**: Independent technology for modern publishing, memberships, subscriptions and newsletters.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,646 |
| 语言 | JavaScript |
| Forks | 11,507 |
| Issues | 243 |
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
| Stars | 133,632 |
| 语言 | Go |
| Forks | 18,945 |
| Issues | 9,960 |
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
| Stars | 87,756 |
| 语言 | Go |
| Forks | 8,249 |
| Issues | 239 |
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
| Stars | 83,046 |
| 语言 | Go |
| Forks | 5,113 |
| Issues | 386 |
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
| Stars | 68,612 |
| 语言 | Go |
| Forks | 3,219 |
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
| Stars | 56,832 |
| 语言 | Go |
| Forks | 5,055 |
| Issues | 1,168 |
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
| Stars | 50,996 |
| 语言 | Go |
| Forks | 21,897 |
| Issues | 412 |
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
| Stars | 50,790 |
| 语言 | Go |
| Forks | 1,607 |
| Issues | 271 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,357 |
| 语言 | Go |
| Forks | 7,944 |
| Issues | 563 |
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
| Stars | 46,841 |
| 语言 | Go |
| Forks | 8,855 |
| Issues | 18 |
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
| Stars | 46,089 |
| 语言 | Go |
| Forks | 3,797 |
| Issues | 84 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,396 |
| 语言 | Shell |
| Forks | 13,877 |
| Issues | 109 |
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
| Stars | 220,151 |
| 语言 | Python |
| Forks | 50,410 |
| Issues | 928 |
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
| Stars | 98,326 |
| 语言 | Python |
| Forks | 12,087 |
| Issues | 121 |
| 许可证 | MIT License |


### yangshun/tech-interview-handbook

**描述**: Curated coding interview preparation materials for busy software engineers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,014 |
| 语言 | TypeScript |
| Forks | 16,524 |
| Issues | 44 |
| Topics | algorithm, algorithm-interview, algorithm-interview-questions, algorithms, behavioral-interviews, coding-interviews, interview-practice, interview-preparation, interview-questions, system-design |
| 许可证 | MIT License |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,259 |
| 语言 | TypeScript |
| Forks | 7,598 |
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
| Stars | 148,129 |
| 语言 | JavaScript |
| Forks | 26,712 |
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
| Stars | 79,152 |
| 语言 | JavaScript |
| Forks | 32,623 |
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
| Stars | 67,386 |
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
| Stars | 66,341 |
| 语言 | JavaScript |
| Forks | 9,192 |
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
| Stars | 51,313 |
| 语言 | JavaScript |
| Forks | 10,352 |
| Issues | 134 |
| Topics | chinese, chinese-poetry, ci, json, poetry, tangshi |
| 许可证 | MIT License |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 106,077 |
| 语言 | Go |
| Forks | 15,019 |
| Issues | 37 |
| Topics | expose, firewall, frp, go, http-proxy, nat, p2p, proxy, reverse-proxy, tunnel |
| 许可证 | Apache License 2.0 |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 152,876 |
| 语言 | Python |
| Forks | 11,651 |
| Issues | 344 |
| Topics | awesome, github, hellogithub, python |
