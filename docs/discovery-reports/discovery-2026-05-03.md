# 项目发现报告 (2026-05-03)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 120 |
| 去重移除 | 32 |
| 已在监控 | 24 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 26 |
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
| Stars | 135,356 |
| 语言 | Python |
| Forks | 19,255 |
| Issues | 339 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的开源 LLM Web 界面解决方案，通过支持 Ollama 和 OpenAI API 等多后端、RAG 检索增强生成以及 MCP 协议，为用户提供了开箱即用的私有化 AI 部署体验，特别适合需要数据隐私控制和快速搭建本地 AI 助手的企业和开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互接口
- 自托管部署：支持完全私有化部署，保障数据隐私和安全，无需依赖第三方服务
- RAG 检索增强生成：内置知识库功能，支持文档向量化检索，提升问答准确率
- MCP 协议支持：兼容 Model Context Protocol，可扩展连接各种外部工具和数据源
- 现代化 Web UI：提供直观的响应式界面，支持会话管理、多模型切换等功能

**适用场景**:
- 企业内部 AI 助手：企业可基于 open-webui 快速搭建私有化 AI 知识库问答系统，用于客服、内部知识检索等场景
- 个人开发者本地 LLM 开发：开发者可在本地运行开源大模型，通过友好的 Web 界面进行调试、测试和日常使用
- 多模型统一管理：技术团队可统一管理多个 LLM 后端（本地 Ollama + 云端 OpenAI），根据需求灵活切换，降低 API 成本



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 130,998 |
| 语言 | Python |
| Forks | 19,836 |
| Issues | 8,082 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是 NousResearch 团队开源的 AI Agent 框架，支持 Claude、GPT-4 等多种主流大模型，拥有超过 13 万 Stars 的社区认可度，能够帮助开发者快速构建智能助手和自动化代理应用。

**技术亮点**:
- 支持多模型后端集成：同时支持 Anthropic Claude、OpenAI GPT 系列和 Codex 等多种大语言模型 API
- 采用模块化架构设计：各功能组件解耦，便于扩展和自定义新的工具/能力
- 内置 Code Execution 能力：支持代码编写和自动化执行，实现复杂的编程任务自动化
- 基于 Python 开发：充分利用 Python 丰富的 AI/ML 生态，集成便捷
- 活跃的开源社区：由 NousResearch 团队维护，社区贡献活跃，项目持续迭代更新

**适用场景**:
- 企业智能助手：构建内部知识库问答、客户服务自动化、文档处理等企业级 AI 应用
- 开发者工具集成：作为编程助手或自动化脚本的核心引擎，提升开发效率
- 个人效率工具：帮助个人用户完成日程管理、邮件处理、信息检索等日常任务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 172,598 |
| 语言 | JavaScript |
| Forks | 26,738 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，通过 Skills、instincts、memory 和 security 四大核心模块显著提升 AI Agent 的开发效率和稳定性，172K+ Stars 已证明其在开发者社区的高度认可。

**技术亮点**:
- 四大核心模块架构：Skills（技能系统）、Instincts（本能反应）、Memory（记忆管理）、Security（安全机制），形成完整的 Agent 优化体系
- 支持多种主流 AI 编程工具：Claude Code、Codex、Opencode、Cursor 等，实现跨平台统一优化
- 基于 MCP（Model Context Protocol）协议开发，确保与 AI 模型的深度集成和标准化通信
- Research-first 开发理念，强调以研究驱动的方法论来优化 Agent 性能
- 企业级安全机制设计，为团队协作提供可靠的 AI 辅助开发环境

**适用场景**:
- 企业开发团队使用：大规模部署 AI 代码助手，通过统一框架标准化团队的 AI 开发流程，提升整体开发效率
- 个人开发者效率提升：构建个人专属的 AI 编程助手配置，实现智能代码补全、自动重构和上下文感知开发
- AI Agent 研究与实验：研究人员可在该框架基础上快速原型验证新的 AI 代理优化策略



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,030 |
| 语言 | Go |
| Forks | 4,048 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLMs、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，为开发者和企业提供了隐私保护、低成本的本地 AI 解决方案，特别适合需要数据主权和离线部署的场景。

**技术亮点**:
- 多模态支持：同时支持文本生成、图像生成、语音合成、目标检测等多种 AI 模型类型
- 硬件无关性：无需 GPU 即可在 CPU 上运行各类模型，降低部署门槛
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络互联
- API 优先设计：提供 RESTful API 接口，易于与现有系统集成，支持 MCP 协议

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业可本地运行 AI 服务，数据不出内网
- 边缘计算场景：在没有强大 GPU 服务器的边缘设备上部署 AI 能力
- 开发测试环境：开发者本地快速验证模型效果，降低实验成本
- 去中心化应用：基于 libp2p 构建分布式 AI 服务网络



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,980 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 正在重新定义人机协作范式 —— 它不仅是一个 Agent 平台，更是一个完整的 AI 协作生态系统。通过支持 MCP 协议和多模型集成（OpenAI、Claude、DeepSeek、Gemini 等），开发者可以快速构建复杂的多 Agent 工作流，将 AI 能力无缝融入实际业务场景。

**技术亮点**:
- 多智能体协作框架：原生支持多 Agent 协同工作，提供 Agent 团队设计能力，让复杂任务可以通过多个专业 Agent 分工合作完成
- MCP 协议完整实现：遵循 Model Context Protocol 标准，实现标准化的 AI 模型上下文管理，支持工具调用和资源扩展
- 多模型统一接入：一站式集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的接口抽象和灵活切换能力
- 知识库深度集成：内置 RAG 能力，支持向量检索和知识管理，使 Agent 能够基于私有知识库进行精准问答和推理
- 现代化技术栈：基于 TypeScript + React 构建，提供完整的类型安全保证和良好的开发体验

**适用场景**:
- 企业智能助手搭建：构建内部知识问答、流程自动化、客服机器人等企业级 AI 应用
- 开发者 AI 工作流：使用 LobeHub 编排多个 Agent 完成代码生成、代码审查、数据分析等开发任务
- 团队协作与知识管理：打造团队专属的 AI 知识库，支持多 Agent 分工处理文档、调研、报告等协作任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,472 |
| 语言 | TypeScript |
| Forks | 6,132 |
| Issues | 77 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 和向量数据库技术为 Claude Code 打造了真正的长期记忆系统，让 AI 代理能够记住之前的编码决策、使用的技术和解决过的问题，显著提升跨会话的开发效率和上下文连贯性。项目拥有超过 7 万 Stars，说明其在 AI 辅助编程领域的实用价值和社区认可度极高。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义化的记忆存储和检索
- 使用 Claude Agent SDK 进行 AI 驱动的上下文压缩，自动提取关键信息并减少 token 消耗
- 支持 SQLite 本地存储，记忆数据完全归用户所有，保障隐私安全
- 通过 Embeddings 技术将编码上下文转换为向量表示，实现高效的语义相似度匹配
- 作为 Claude Code 官方插件架构，无缝集成到现有开发工作流中

**适用场景**:
- 个人开发者：让 AI 记住之前项目的技术选型、代码规范和常见问题解决方案，避免重复解释和错误重犯
- 团队协作：沉淀团队的编码最佳实践和项目特定知识，新成员加入时 AI 能快速提供上下文相关的建议
- 长期项目维护：AI 能够记住项目的演进历史、之前的 bug 修复方案和架构决策理由，提升代码修改的一致性和质量



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 70,865 |
| 语言 | Python |
| Forks | 8,657 |
| Issues | 994 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 学术验证的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供从数据处理到模型训练的一站式解决方案，特别适合需要快速定制化部署 LLM 的企业和研究者。

**技术亮点**:
- 统一框架支持 100+ 主流 LLMs（Llama3, Qwen, DeepSeek, Gemma 等）和 VLMs，降低多模型管理复杂度
- 集成 LoRA/QLoRA/PEFT 等主流高效微调技术，显著降低 GPU 显存占用，支持消费级显卡训练
- 支持 RLHF（DPO/KTO）、SFT 等多种训练范式，可实现指令微调和人类偏好对齐
- 内置量化模块支持 4-bit/8-bit 推理，配合 QLoRA 可在 24GB 显存内微调 70B 参数模型
- 提供可视化训练监控和模型导出功能，支持 Transformers 和 vLLM 部署

**适用场景**:
- 企业私有化部署：利用 LoRA/QLoRA 技术快速将通用 LLM 定制为企业领域模型（如客服、医疗、金融），控制部署成本
- 学术研究与实验：支持多种微调方法对比、RLHF 训练流程研究，适合论文复现和算法创新
- 个人开发者/创业者：无需深度优化经验，即可基于预训练模型快速构建 AI 应用（Agent、知识库问答等）



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,716 |
| 语言 | HTML |
| Forks | 5,039 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
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
| Stars | 42,350 |
| 语言 | Python |
| Forks | 5,123 |
| Issues | 99 |
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
| Stars | 39,093 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 72 |
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
| Stars | 38,546 |
| 语言 | TypeScript |
| Forks | 4,385 |
| Issues | 495 |
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
| Stars | 114,630 |
| 语言 | TypeScript |
| Forks | 7,234 |
| Issues | 304 |
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
| Stars | 59,463 |
| 语言 | JavaScript |
| Forks | 6,419 |
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
| Stars | 72,555 |
| 语言 | Python |
| Forks | 9,176 |
| Issues | 410 |
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
| Stars | 55,590 |
| 语言 | TypeScript |
| Forks | 4,514 |
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
| Stars | 108,556 |
| 语言 | Python |
| Forks | 16,028 |
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
| Stars | 91,880 |
| 语言 | Python |
| Forks | 10,448 |
| Issues | 236 |
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
| Stars | 52,506 |
| 语言 | TypeScript |
| Forks | 24,254 |
| Issues | 829 |
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
| Stars | 186,576 |
| 语言 | TypeScript |
| Forks | 57,311 |
| Issues | 1,580 |
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
| Stars | 155,383 |
| 语言 | Java |
| Forks | 46,156 |
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
| Stars | 147,658 |
| 语言 | Python |
| Forks | 8,899 |
| Issues | 948 |
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
| Stars | 60,407 |
| 语言 | Jupyter Notebook |
| Forks | 20,449 |
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
| Stars | 57,725 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 570 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 57,937 |
| 语言 | TypeScript |
| Forks | 9,510 |
| Issues | 113 |
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
| Stars | 58,409 |
| 语言 | Rust |
| Forks | 3,792 |
| Issues | 714 |
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
| Stars | 135,356 |
| 语言 | Python |
| Forks | 19,255 |
| Issues | 339 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的开源 LLM Web 界面解决方案，通过支持 Ollama 和 OpenAI API 等多后端、RAG 检索增强生成以及 MCP 协议，为用户提供了开箱即用的私有化 AI 部署体验，特别适合需要数据隐私控制和快速搭建本地 AI 助手的企业和开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互接口
- 自托管部署：支持完全私有化部署，保障数据隐私和安全，无需依赖第三方服务
- RAG 检索增强生成：内置知识库功能，支持文档向量化检索，提升问答准确率
- MCP 协议支持：兼容 Model Context Protocol，可扩展连接各种外部工具和数据源
- 现代化 Web UI：提供直观的响应式界面，支持会话管理、多模型切换等功能

**适用场景**:
- 企业内部 AI 助手：企业可基于 open-webui 快速搭建私有化 AI 知识库问答系统，用于客服、内部知识检索等场景
- 个人开发者本地 LLM 开发：开发者可在本地运行开源大模型，通过友好的 Web 界面进行调试、测试和日常使用
- 多模型统一管理：技术团队可统一管理多个 LLM 后端（本地 Ollama + 云端 OpenAI），根据需求灵活切换，降低 API 成本



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,980 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 正在重新定义人机协作范式 —— 它不仅是一个 Agent 平台，更是一个完整的 AI 协作生态系统。通过支持 MCP 协议和多模型集成（OpenAI、Claude、DeepSeek、Gemini 等），开发者可以快速构建复杂的多 Agent 工作流，将 AI 能力无缝融入实际业务场景。

**技术亮点**:
- 多智能体协作框架：原生支持多 Agent 协同工作，提供 Agent 团队设计能力，让复杂任务可以通过多个专业 Agent 分工合作完成
- MCP 协议完整实现：遵循 Model Context Protocol 标准，实现标准化的 AI 模型上下文管理，支持工具调用和资源扩展
- 多模型统一接入：一站式集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的接口抽象和灵活切换能力
- 知识库深度集成：内置 RAG 能力，支持向量检索和知识管理，使 Agent 能够基于私有知识库进行精准问答和推理
- 现代化技术栈：基于 TypeScript + React 构建，提供完整的类型安全保证和良好的开发体验

**适用场景**:
- 企业智能助手搭建：构建内部知识问答、流程自动化、客服机器人等企业级 AI 应用
- 开发者 AI 工作流：使用 LobeHub 编排多个 Agent 完成代码生成、代码审查、数据分析等开发任务
- 团队协作与知识管理：打造团队专属的 AI 知识库，支持多 Agent 分工处理文档、调研、报告等协作任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,472 |
| 语言 | TypeScript |
| Forks | 6,132 |
| Issues | 77 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 和向量数据库技术为 Claude Code 打造了真正的长期记忆系统，让 AI 代理能够记住之前的编码决策、使用的技术和解决过的问题，显著提升跨会话的开发效率和上下文连贯性。项目拥有超过 7 万 Stars，说明其在 AI 辅助编程领域的实用价值和社区认可度极高。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义化的记忆存储和检索
- 使用 Claude Agent SDK 进行 AI 驱动的上下文压缩，自动提取关键信息并减少 token 消耗
- 支持 SQLite 本地存储，记忆数据完全归用户所有，保障隐私安全
- 通过 Embeddings 技术将编码上下文转换为向量表示，实现高效的语义相似度匹配
- 作为 Claude Code 官方插件架构，无缝集成到现有开发工作流中

**适用场景**:
- 个人开发者：让 AI 记住之前项目的技术选型、代码规范和常见问题解决方案，避免重复解释和错误重犯
- 团队协作：沉淀团队的编码最佳实践和项目特定知识，新成员加入时 AI 能快速提供上下文相关的建议
- 长期项目维护：AI 能够记住项目的演进历史、之前的 bug 修复方案和架构决策理由，提升代码修改的一致性和质量



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
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
| Stars | 42,350 |
| 语言 | Python |
| Forks | 5,123 |
| Issues | 99 |
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
| Stars | 39,093 |
| 语言 | Python |
| Forks | 6,192 |
| Issues | 72 |
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
| Stars | 101,795 |
| 语言 | TypeScript |
| Forks | 12,272 |
| Issues | 987 |
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
| Stars | 59,463 |
| 语言 | JavaScript |
| Forks | 6,419 |
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
| Stars | 108,556 |
| 语言 | Python |
| Forks | 16,028 |
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
| Stars | 77,009 |
| 语言 | Python |
| Forks | 10,356 |
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
| Stars | 52,506 |
| 语言 | TypeScript |
| Forks | 24,254 |
| Issues | 829 |
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
| Stars | 41,691 |
| 语言 | Python |
| Forks | 4,570 |
| Issues | 204 |
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
| Stars | 44,103 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,061 |
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
| Stars | 34,698 |
| 语言 | Python |
| Forks | 4,912 |
| Issues | 226 |
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
| Stars | 135,356 |
| 语言 | Python |
| Forks | 19,255 |
| Issues | 339 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

open-webui 是目前最完整的开源 LLM Web 界面解决方案，通过支持 Ollama 和 OpenAI API 等多后端、RAG 检索增强生成以及 MCP 协议，为用户提供了开箱即用的私有化 AI 部署体验，特别适合需要数据隐私控制和快速搭建本地 AI 助手的企业和开发者。

**技术亮点**:
- 多后端支持：同时兼容 Ollama 本地模型和 OpenAI API，提供统一的 AI 交互接口
- 自托管部署：支持完全私有化部署，保障数据隐私和安全，无需依赖第三方服务
- RAG 检索增强生成：内置知识库功能，支持文档向量化检索，提升问答准确率
- MCP 协议支持：兼容 Model Context Protocol，可扩展连接各种外部工具和数据源
- 现代化 Web UI：提供直观的响应式界面，支持会话管理、多模型切换等功能

**适用场景**:
- 企业内部 AI 助手：企业可基于 open-webui 快速搭建私有化 AI 知识库问答系统，用于客服、内部知识检索等场景
- 个人开发者本地 LLM 开发：开发者可在本地运行开源大模型，通过友好的 Web 界面进行调试、测试和日常使用
- 多模型统一管理：技术团队可统一管理多个 LLM 后端（本地 Ollama + 云端 OpenAI），根据需求灵活切换，降低 API 成本



### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 130,998 |
| 语言 | Python |
| Forks | 19,836 |
| Issues | 8,082 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, clawdbot, codex, hermes, hermes-agent, llm, moltbot, nous-research, openai, openclaw |
| 许可证 | MIT License |

---

Hermes-agent 是 NousResearch 团队开源的 AI Agent 框架，支持 Claude、GPT-4 等多种主流大模型，拥有超过 13 万 Stars 的社区认可度，能够帮助开发者快速构建智能助手和自动化代理应用。

**技术亮点**:
- 支持多模型后端集成：同时支持 Anthropic Claude、OpenAI GPT 系列和 Codex 等多种大语言模型 API
- 采用模块化架构设计：各功能组件解耦，便于扩展和自定义新的工具/能力
- 内置 Code Execution 能力：支持代码编写和自动化执行，实现复杂的编程任务自动化
- 基于 Python 开发：充分利用 Python 丰富的 AI/ML 生态，集成便捷
- 活跃的开源社区：由 NousResearch 团队维护，社区贡献活跃，项目持续迭代更新

**适用场景**:
- 企业智能助手：构建内部知识库问答、客户服务自动化、文档处理等企业级 AI 应用
- 开发者工具集成：作为编程助手或自动化脚本的核心引擎，提升开发效率
- 个人效率工具：帮助个人用户完成日程管理、邮件处理、信息检索等日常任务



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 172,598 |
| 语言 | JavaScript |
| Forks | 26,738 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，通过 Skills、instincts、memory 和 security 四大核心模块显著提升 AI Agent 的开发效率和稳定性，172K+ Stars 已证明其在开发者社区的高度认可。

**技术亮点**:
- 四大核心模块架构：Skills（技能系统）、Instincts（本能反应）、Memory（记忆管理）、Security（安全机制），形成完整的 Agent 优化体系
- 支持多种主流 AI 编程工具：Claude Code、Codex、Opencode、Cursor 等，实现跨平台统一优化
- 基于 MCP（Model Context Protocol）协议开发，确保与 AI 模型的深度集成和标准化通信
- Research-first 开发理念，强调以研究驱动的方法论来优化 Agent 性能
- 企业级安全机制设计，为团队协作提供可靠的 AI 辅助开发环境

**适用场景**:
- 企业开发团队使用：大规模部署 AI 代码助手，通过统一框架标准化团队的 AI 开发流程，提升整体开发效率
- 个人开发者效率提升：构建个人专属的 AI 编程助手配置，实现智能代码补全、自动重构和上下文感知开发
- AI Agent 研究与实验：研究人员可在该框架基础上快速原型验证新的 AI 代理优化策略



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,980 |
| 语言 | TypeScript |
| Forks | 15,067 |
| Issues | 771 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 正在重新定义人机协作范式 —— 它不仅是一个 Agent 平台，更是一个完整的 AI 协作生态系统。通过支持 MCP 协议和多模型集成（OpenAI、Claude、DeepSeek、Gemini 等），开发者可以快速构建复杂的多 Agent 工作流，将 AI 能力无缝融入实际业务场景。

**技术亮点**:
- 多智能体协作框架：原生支持多 Agent 协同工作，提供 Agent 团队设计能力，让复杂任务可以通过多个专业 Agent 分工合作完成
- MCP 协议完整实现：遵循 Model Context Protocol 标准，实现标准化的 AI 模型上下文管理，支持工具调用和资源扩展
- 多模型统一接入：一站式集成 OpenAI GPT、Claude、DeepSeek、Gemini 等主流大模型，提供统一的接口抽象和灵活切换能力
- 知识库深度集成：内置 RAG 能力，支持向量检索和知识管理，使 Agent 能够基于私有知识库进行精准问答和推理
- 现代化技术栈：基于 TypeScript + React 构建，提供完整的类型安全保证和良好的开发体验

**适用场景**:
- 企业智能助手搭建：构建内部知识问答、流程自动化、客服机器人等企业级 AI 应用
- 开发者 AI 工作流：使用 LobeHub 编排多个 Agent 完成代码生成、代码审查、数据分析等开发任务
- 团队协作与知识管理：打造团队专属的 AI 知识库，支持多 Agent 分工处理文档、调研、报告等协作任务



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,472 |
| 语言 | TypeScript |
| Forks | 6,132 |
| Issues | 77 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Other |

---

claude-mem 通过 RAG 和向量数据库技术为 Claude Code 打造了真正的长期记忆系统，让 AI 代理能够记住之前的编码决策、使用的技术和解决过的问题，显著提升跨会话的开发效率和上下文连贯性。项目拥有超过 7 万 Stars，说明其在 AI 辅助编程领域的实用价值和社区认可度极高。

**技术亮点**:
- 基于 RAG（检索增强生成）架构，结合 ChromaDB 向量数据库实现语义化的记忆存储和检索
- 使用 Claude Agent SDK 进行 AI 驱动的上下文压缩，自动提取关键信息并减少 token 消耗
- 支持 SQLite 本地存储，记忆数据完全归用户所有，保障隐私安全
- 通过 Embeddings 技术将编码上下文转换为向量表示，实现高效的语义相似度匹配
- 作为 Claude Code 官方插件架构，无缝集成到现有开发工作流中

**适用场景**:
- 个人开发者：让 AI 记住之前项目的技术选型、代码规范和常见问题解决方案，避免重复解释和错误重犯
- 团队协作：沉淀团队的编码最佳实践和项目特定知识，新成员加入时 AI 能快速提供上下文相关的建议
- 长期项目维护：AI 能够记住项目的演进历史、之前的 bug 修复方案和架构决策理由，提升代码修改的一致性和质量



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,455 |
| 语言 | HTML |
| Forks | 21,067 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 是目前最大的开源提示词聚合平台，拥有超过16万Stars，前身即为知名的 Awesome ChatGPT Prompts 项目。其核心优势在于支持 ChatGPT、Claude、Gemini 等多主流 LLM 平台，提供完整的企业级自托管方案，在充分利用社区智慧的同时保障数据隐私，非常适合企业和个人开发者构建 AI 应用。

**技术亮点**:
- 现代化全栈架构：基于 Next.js + TypeScript 构建，提供 SSR/SSG 能力，确保优秀的 SEO 和首屏加载性能
- 多 LLM 平台兼容：原生支持 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，一套提示词可跨平台复用
- 社区驱动的提示词库：采用开源协作模式的海量高质量提示词集合，覆盖写作、编程、分析等数十个场景类别
- 企业级自托管支持：提供完整的私有部署方案，组织可在自有基础设施上运行，完全掌控数据，满足合规要求
- 隐私优先设计：数据不出本地，支持完全离线使用，适合对数据安全有严格要求的金融、医疗等敏感行业

**适用场景**:
- 企业 AI 应用集成：企业可自托管提示词库，为内部 AI 助手或客服机器人提供经过验证的高质量提示词，降低开发成本
- 个人开发者快速开发 AI 应用：开发者可直接复用社区验证的提示词，快速原型验证和 MVP 构建
- AI 学习与研究：研究人员和学生可研究开源提示词工程实践，学习如何编写有效的 prompt 来优化 LLM 输出效果



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,966 |
| 语言 | Python |
| Forks | 2,868 |
| Issues | 177 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个将创意meme与实用价值完美结合的项目，通过"穴居人语言"方式实现65%的token削减，对于高频使用LLM的开发者来说能显著降低成本且不影响输出质量，52k+ stars证明了其有效性。

**技术亮点**:
- 创新的token压缩策略：通过语言简化技巧显著减少API调用成本
- 专注于Claude生态：深度集成Claude Code的prompt工程最佳实践
- 幽默且实用的设计理念：将meme文化融入技术实现，提升开发者体验
- 基于Python的轻量级实现：易于集成到现有工作流中
- MIT开源许可：允许商业和个人项目自由使用与修改

**适用场景**:
- 高频LLM API调用场景：需要频繁使用Claude API的企业应用，可显著降低运营成本
- 个人开发者工具链：优化日常编码辅助体验，在保持效率的同时减少开支
- AI研究和实验：在进行大规模prompt测试或模型交互实验时节省费用
- 开发团队成本优化：团队成员共享使用，统一LLM交互规范以实现成本控制



### shanraisshan/claude-code-best-practice

**描述**: from vibe coding to agentic engineering - practice makes claude perfect

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 50,716 |
| 语言 | HTML |
| Forks | 5,039 |
| Issues | 12 |
| Topics | agentic-ai, agentic-coding, agentic-engineering, agentic-workflow, ai, ai-agents, anthropic, best-practices, boris, claude, claude-ai, claude-code, claude-code-agents, claude-code-best-practices, claude-code-commands, claude-code-skills, context-engineering, pakistan, pakistani-developer, vibe-coding |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configuration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,463 |
| 语言 | JavaScript |
| Forks | 6,419 |
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
| Stars | 72,555 |
| 语言 | Python |
| Forks | 9,176 |
| Issues | 410 |
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
| Stars | 55,590 |
| 语言 | TypeScript |
| Forks | 4,514 |
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
| Stars | 52,506 |
| 语言 | TypeScript |
| Forks | 24,254 |
| Issues | 829 |
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
| Stars | 78,932 |
| 语言 | Python |
| Forks | 16,376 |
| Issues | 4,737 |
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
| Stars | 147,658 |
| 语言 | Python |
| Forks | 8,899 |
| Issues | 948 |
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
| Stars | 57,725 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 570 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 170,614 |
| 语言 | Go |
| Forks | 15,952 |
| Issues | 3,153 |
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
| Stars | 91,865 |
| 语言 | Jupyter Notebook |
| Forks | 14,178 |
| Issues | 6 |
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
| Stars | 57,937 |
| 语言 | TypeScript |
| Forks | 9,510 |
| Issues | 113 |
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
| Stars | 48,375 |
| 语言 | Rust |
| Forks | 9,687 |
| Issues | 3 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 73,556 |
| 语言 | Python |
| Forks | 7,589 |
| Issues | 138 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
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
| Stars | 119,844 |
| 语言 | Python |
| Forks | 7,967 |
| Issues | 622 |
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
| Stars | 70,865 |
| 语言 | Python |
| Forks | 8,657 |
| Issues | 994 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory 是由 ACL 2024 学术验证的统一微调框架，支持 100+ 大语言模型和视觉语言模型，提供从数据处理到模型训练的一站式解决方案，特别适合需要快速定制化部署 LLM 的企业和研究者。

**技术亮点**:
- 统一框架支持 100+ 主流 LLMs（Llama3, Qwen, DeepSeek, Gemma 等）和 VLMs，降低多模型管理复杂度
- 集成 LoRA/QLoRA/PEFT 等主流高效微调技术，显著降低 GPU 显存占用，支持消费级显卡训练
- 支持 RLHF（DPO/KTO）、SFT 等多种训练范式，可实现指令微调和人类偏好对齐
- 内置量化模块支持 4-bit/8-bit 推理，配合 QLoRA 可在 24GB 显存内微调 70B 参数模型
- 提供可视化训练监控和模型导出功能，支持 Transformers 和 vLLM 部署

**适用场景**:
- 企业私有化部署：利用 LoRA/QLoRA 技术快速将通用 LLM 定制为企业领域模型（如客服、医疗、金融），控制部署成本
- 学术研究与实验：支持多种微调方法对比、RLHF 训练流程研究，适合论文复现和算法创新
- 个人开发者/创业者：无需深度优化经验，即可基于预训练模型快速构建 AI 应用（Agent、知识库问答等）



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 66,928 |
| 语言 | Python |
| Forks | 6,698 |
| Issues | 78 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是一个功能全面的开源金融数据平台，整合了股票、加密货币、期权、固收等多类资产数据，并原生支持 AI 代理和机器学习集成，拥有超过 66k GitHub Stars，是量化分析师和金融 AI 应用开发者的首选工具。

**技术亮点**:
- 多资产类别数据集成：统一对接股票、加密货币、期权、固收、外汇等多个市场的实时和历史数据
- AI 与机器学习原生支持：内置 AI 代理框架，支持自然语言查询金融数据，便于构建智能投研应用
- 量化金融工具链：提供回测、因子分析、技术指标计算等完整的量化研究功能
- 模块化 Python 架构：基于 Python 生态，支持扩展和自定义数据源、分析模块
- 企业级数据管道：提供从数据获取、清洗到可视化的完整工作流

**适用场景**:
- 量化交易研究：分析师可快速获取多市场数据，进行回测和策略验证
- 金融 AI 应用开发：开发者可基于平台构建智能投顾、风险评估等 AI 驱动应用
- 投资组合分析与风险管理：支持固收、衍生品等复杂金融产品的分析与建模
- 金融数据新闻与报告自动化：自动化抓取和可视化金融数据，用于报告生成



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 161,455 |
| 语言 | HTML |
| Forks | 21,067 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 是目前最大的开源提示词聚合平台，拥有超过16万Stars，前身即为知名的 Awesome ChatGPT Prompts 项目。其核心优势在于支持 ChatGPT、Claude、Gemini 等多主流 LLM 平台，提供完整的企业级自托管方案，在充分利用社区智慧的同时保障数据隐私，非常适合企业和个人开发者构建 AI 应用。

**技术亮点**:
- 现代化全栈架构：基于 Next.js + TypeScript 构建，提供 SSR/SSG 能力，确保优秀的 SEO 和首屏加载性能
- 多 LLM 平台兼容：原生支持 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，一套提示词可跨平台复用
- 社区驱动的提示词库：采用开源协作模式的海量高质量提示词集合，覆盖写作、编程、分析等数十个场景类别
- 企业级自托管支持：提供完整的私有部署方案，组织可在自有基础设施上运行，完全掌控数据，满足合规要求
- 隐私优先设计：数据不出本地，支持完全离线使用，适合对数据安全有严格要求的金融、医疗等敏感行业

**适用场景**:
- 企业 AI 应用集成：企业可自托管提示词库，为内部 AI 助手或客服机器人提供经过验证的高质量提示词，降低开发成本
- 个人开发者快速开发 AI 应用：开发者可直接复用社区验证的提示词，快速原型验证和 MVP 构建
- AI 学习与研究：研究人员和学生可研究开源提示词工程实践，学习如何编写有效的 prompt 来优化 LLM 输出效果



### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 160,214 |
| 语言 | Python |
| Forks | 33,097 |
| Issues | 2,360 |
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
| Stars | 78,932 |
| 语言 | Python |
| Forks | 16,376 |
| Issues | 4,737 |
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
| Stars | 111,201 |
| 语言 | Python |
| Forks | 12,981 |
| Issues | 4,004 |
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
| Stars | 99,600 |
| 语言 | Python |
| Forks | 27,647 |
| Issues | 18,514 |
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
| Stars | 91,865 |
| 语言 | Jupyter Notebook |
| Forks | 14,178 |
| Issues | 6 |
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
| Stars | 172,598 |
| 语言 | JavaScript |
| Forks | 26,738 |
| Issues | 158 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个为 Claude Code、Cursor 等主流 AI 编程工具提供性能优化框架的开源项目，通过 Skills、instincts、memory 和 security 四大核心模块显著提升 AI Agent 的开发效率和稳定性，172K+ Stars 已证明其在开发者社区的高度认可。

**技术亮点**:
- 四大核心模块架构：Skills（技能系统）、Instincts（本能反应）、Memory（记忆管理）、Security（安全机制），形成完整的 Agent 优化体系
- 支持多种主流 AI 编程工具：Claude Code、Codex、Opencode、Cursor 等，实现跨平台统一优化
- 基于 MCP（Model Context Protocol）协议开发，确保与 AI 模型的深度集成和标准化通信
- Research-first 开发理念，强调以研究驱动的方法论来优化 Agent 性能
- 企业级安全机制设计，为团队协作提供可靠的 AI 辅助开发环境

**适用场景**:
- 企业开发团队使用：大规模部署 AI 代码助手，通过统一框架标准化团队的 AI 开发流程，提升整体开发效率
- 个人开发者效率提升：构建个人专属的 AI 编程助手配置，实现智能代码补全、自动重构和上下文感知开发
- AI Agent 研究与实验：研究人员可在该框架基础上快速原型验证新的 AI 代理优化策略



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,030 |
| 语言 | Go |
| Forks | 4,048 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLMs、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，为开发者和企业提供了隐私保护、低成本的本地 AI 解决方案，特别适合需要数据主权和离线部署的场景。

**技术亮点**:
- 多模态支持：同时支持文本生成、图像生成、语音合成、目标检测等多种 AI 模型类型
- 硬件无关性：无需 GPU 即可在 CPU 上运行各类模型，降低部署门槛
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络互联
- API 优先设计：提供 RESTful API 接口，易于与现有系统集成，支持 MCP 协议

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业可本地运行 AI 服务，数据不出内网
- 边缘计算场景：在没有强大 GPU 服务器的边缘设备上部署 AI 能力
- 开发测试环境：开发者本地快速验证模型效果，降低实验成本
- 去中心化应用：基于 libp2p 构建分布式 AI 服务网络



### jeecgboot/JeecgBoot

**描述**: AI低代码平台，支持「低代码 + 零代码」双模式：零代码 5 分钟搭建业务系统，低代码模式一键生成前后端代码。 内置AI 应用，支持AI聊天、知识库、流程编排、MCP与插件，支持各种模型。Skills能力实现：一句话画流程图、设计表单、生成系统。 引领 AI生成→在线配置→代码生成→手工合并的开发模式，解决Java项目80%的重复工作，快速提高效率，又不失灵活性。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,070 |
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
| Stars | 72,555 |
| 语言 | Python |
| Forks | 9,176 |
| Issues | 410 |
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
| Stars | 55,590 |
| 语言 | TypeScript |
| Forks | 4,514 |
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
| Stars | 186,576 |
| 语言 | TypeScript |
| Forks | 57,311 |
| Issues | 1,580 |
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
| Stars | 57,725 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 570 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 430,617 |
| 语言 | Python |
| Forks | 47,007 |
| Issues | 1,317 |
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
| Stars | 160,374 |
| 语言 | Python |
| Forks | 13,303 |
| Issues | 2,507 |
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
| Stars | 97,856 |
| 语言 | Python |
| Forks | 9,189 |
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
| Stars | 82,854 |
| 语言 | Python |
| Forks | 9,663 |
| Issues | 279 |
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
| Stars | 184,518 |
| 语言 | TypeScript |
| Forks | 39,670 |
| Issues | 17,000 |
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
| Stars | 94,229 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 307 |
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
| Stars | 79,085 |
| 语言 | TypeScript |
| Forks | 5,848 |
| Issues | 771 |
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
| Stars | 79,980 |
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
| Stars | 77,372 |
| 语言 | Go |
| Forks | 2,806 |
| Issues | 958 |
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
| Stars | 55,590 |
| 语言 | TypeScript |
| Forks | 4,514 |
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
| Stars | 186,576 |
| 语言 | TypeScript |
| Forks | 57,311 |
| Issues | 1,580 |
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
| Stars | 57,725 |
| 语言 | Python |
| Forks | 6,247 |
| Issues | 570 |
| Topics | agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio, cursor, developer-tools, gemini-cli, mcp, openai-codex, rube, saas, skill, workflow-automation |


### etcd-io/etcd

**描述**: Distributed reliable key-value store for the most critical data of a distributed system

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,681 |
| 语言 | Go |
| Forks | 10,330 |
| Issues | 239 |
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
| Stars | 122,051 |
| 语言 | Go |
| Forks | 43,020 |
| Issues | 2,701 |
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
| Stars | 71,534 |
| 语言 | Go |
| Forks | 18,924 |
| Issues | 3,834 |
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
| Stars | 55,324 |
| 语言 | Go |
| Forks | 6,652 |
| Issues | 2,769 |
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
| Stars | 47,507 |
| 语言 | Go |
| Forks | 5,056 |
| Issues | 988 |
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
| Stars | 94,229 |
| 语言 | TypeScript |
| Forks | 9,410 |
| Issues | 307 |
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
| Stars | 78,139 |
| 语言 | TypeScript |
| Forks | 6,836 |
| Issues | 425 |
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
| Stars | 86,158 |
| 语言 | JavaScript |
| Forks | 7,761 |
| Issues | 730 |
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
| Stars | 70,134 |
| 语言 | Go |
| Forks | 1,919 |
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
| Stars | 62,968 |
| 语言 | Go |
| Forks | 5,954 |
| Issues | 786 |
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
| Stars | 59,348 |
| 语言 | Go |
| Forks | 4,326 |
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
| Stars | 60,850 |
| 语言 | Go |
| Forks | 7,465 |
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
| Stars | 86,158 |
| 语言 | JavaScript |
| Forks | 7,761 |
| Issues | 730 |
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
| Stars | 63,882 |
| 语言 | Go |
| Forks | 10,371 |
| Issues | 767 |
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
| Stars | 46,030 |
| 语言 | Go |
| Forks | 4,048 |
| Issues | 154 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源本地 AI 引擎，支持运行 LLMs、图像生成、语音合成等多种模型，无需 GPU 即可在普通硬件上运行，为开发者和企业提供了隐私保护、低成本的本地 AI 解决方案，特别适合需要数据主权和离线部署的场景。

**技术亮点**:
- 多模态支持：同时支持文本生成、图像生成、语音合成、目标检测等多种 AI 模型类型
- 硬件无关性：无需 GPU 即可在 CPU 上运行各类模型，降低部署门槛
- 丰富的模型支持：兼容 llama、mamba、stable-diffusion、musicgen 等主流开源模型
- 去中心化架构：基于 libp2p 实现分布式部署，支持 P2P 网络互联
- API 优先设计：提供 RESTful API 接口，易于与现有系统集成，支持 MCP 协议

**适用场景**:
- 企业私有化部署：对数据隐私有严格要求的企业可本地运行 AI 服务，数据不出内网
- 边缘计算场景：在没有强大 GPU 服务器的边缘设备上部署 AI 能力
- 开发测试环境：开发者本地快速验证模型效果，降低实验成本
- 去中心化应用：基于 libp2p 构建分布式 AI 服务网络



### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 430,617 |
| 语言 | Python |
| Forks | 47,007 |
| Issues | 1,317 |
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
| Stars | 97,856 |
| 语言 | Python |
| Forks | 9,189 |
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
| Stars | 87,391 |
| 语言 | Python |
| Forks | 33,908 |
| Issues | 435 |
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
| Stars | 100,061 |
| 语言 | TypeScript |
| Forks | 27,257 |
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
| Stars | 79,085 |
| 语言 | TypeScript |
| Forks | 5,848 |
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
| Stars | 68,985 |
| 语言 | JavaScript |
| Forks | 23,229 |
| Issues | 210 |
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
| Forks | 10,205 |
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
| Stars | 51,836 |
| 语言 | JavaScript |
| Forks | 4,710 |
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
| Stars | 72,057 |
| 语言 | Go |
| Forks | 4,712 |
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
| Stars | 58,104 |
| 语言 | Go |
| Forks | 3,341 |
| Issues | 19 |
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
| Stars | 88,438 |
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
| Stars | 101,795 |
| 语言 | TypeScript |
| Forks | 12,272 |
| Issues | 987 |
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
| Stars | 59,463 |
| 语言 | JavaScript |
| Forks | 6,419 |
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
| Stars | 44,103 |
| 语言 | Go |
| Forks | 3,985 |
| Issues | 1,061 |
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
| Stars | 51,681 |
| 语言 | Go |
| Forks | 10,330 |
| Issues | 239 |
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
| Stars | 161,455 |
| 语言 | HTML |
| Forks | 21,067 |
| Issues | 44 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |

---

f/prompts.chat 是目前最大的开源提示词聚合平台，拥有超过16万Stars，前身即为知名的 Awesome ChatGPT Prompts 项目。其核心优势在于支持 ChatGPT、Claude、Gemini 等多主流 LLM 平台，提供完整的企业级自托管方案，在充分利用社区智慧的同时保障数据隐私，非常适合企业和个人开发者构建 AI 应用。

**技术亮点**:
- 现代化全栈架构：基于 Next.js + TypeScript 构建，提供 SSR/SSG 能力，确保优秀的 SEO 和首屏加载性能
- 多 LLM 平台兼容：原生支持 OpenAI GPT-4、Anthropic Claude、Google Gemini 等主流大语言模型，一套提示词可跨平台复用
- 社区驱动的提示词库：采用开源协作模式的海量高质量提示词集合，覆盖写作、编程、分析等数十个场景类别
- 企业级自托管支持：提供完整的私有部署方案，组织可在自有基础设施上运行，完全掌控数据，满足合规要求
- 隐私优先设计：数据不出本地，支持完全离线使用，适合对数据安全有严格要求的金融、医疗等敏感行业

**适用场景**:
- 企业 AI 应用集成：企业可自托管提示词库，为内部 AI 助手或客服机器人提供经过验证的高质量提示词，降低开发成本
- 个人开发者快速开发 AI 应用：开发者可直接复用社区验证的提示词，快速原型验证和 MVP 构建
- AI 学习与研究：研究人员和学生可研究开源提示词工程实践，学习如何编写有效的 prompt 来优化 LLM 输出效果



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 52,966 |
| 语言 | Python |
| Forks | 2,868 |
| Issues | 177 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | MIT License |

---

这是一个将创意meme与实用价值完美结合的项目，通过"穴居人语言"方式实现65%的token削减，对于高频使用LLM的开发者来说能显著降低成本且不影响输出质量，52k+ stars证明了其有效性。

**技术亮点**:
- 创新的token压缩策略：通过语言简化技巧显著减少API调用成本
- 专注于Claude生态：深度集成Claude Code的prompt工程最佳实践
- 幽默且实用的设计理念：将meme文化融入技术实现，提升开发者体验
- 基于Python的轻量级实现：易于集成到现有工作流中
- MIT开源许可：允许商业和个人项目自由使用与修改

**适用场景**:
- 高频LLM API调用场景：需要频繁使用Claude API的企业应用，可显著降低运营成本
- 个人开发者工具链：优化日常编码辅助体验，在保持效率的同时减少开支
- AI研究和实验：在进行大规模prompt测试或模型交互实验时节省费用
- 开发团队成本优化：团队成员共享使用，统一LLM交互规范以实现成本控制



### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,350 |
| 语言 | Python |
| Forks | 5,123 |
| Issues | 99 |
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
| Stars | 57,937 |
| 语言 | TypeScript |
| Forks | 9,510 |
| Issues | 113 |
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
| Stars | 89,842 |
| 语言 | TypeScript |
| Forks | 10,039 |
| Issues | 2,272 |
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
| Stars | 87,784 |
| 语言 | TypeScript |
| Forks | 8,925 |
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
| Stars | 171,711 |
| 语言 | Go |
| Forks | 13,184 |
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
| Stars | 127,673 |
| 语言 | JavaScript |
| Forks | 12,481 |
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
| Stars | 136,621 |
| 语言 | Unknown |
| Forks | 34,116 |
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
| Stars | 79,560 |
| 语言 | Python |
| Forks | 9,034 |
| Issues | 3,002 |
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
| Stars | 56,762 |
| 语言 | Shell |
| Forks | 4,826 |
| Issues | 10 |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 92,585 |
| 语言 | Python |
| Forks | 13,457 |
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
| Stars | 92,306 |
| 语言 | Python |
| Forks | 7,995 |
| Issues | 650 |
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
| Stars | 115,837 |
| 语言 | TypeScript |
| Forks | 6,071 |
| Issues | 40 |
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
| Stars | 115,476 |
| 语言 | TypeScript |
| Forks | 8,426 |
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
| Stars | 88,617 |
| 语言 | TypeScript |
| Forks | 13,052 |
| Issues | 500 |
| 许可证 | MIT License |


### gsd-build/get-shit-done

**描述**: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,652 |
| 语言 | JavaScript |
| Forks | 5,076 |
| Issues | 28 |
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
| Stars | 51,382 |
| 语言 | JavaScript |
| Forks | 10,362 |
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
| Stars | 48,318 |
| 语言 | Go |
| Forks | 10,334 |
| Issues | 1,889 |
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
| Stars | 108,107 |
| 语言 | C++ |
| Forks | 17,726 |
| Issues | 1,577 |
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
| Stars | 63,354 |
| 语言 | Python |
| Forks | 1,632 |
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
| Stars | 35,150 |
| 语言 | TypeScript |
| Forks | 3,996 |
| Issues | 367 |
| 许可证 | Other |


### vinta/awesome-python

**描述**: An opinionated list of Python frameworks, libraries, tools, and resources

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 295,790 |
| 语言 | Python |
| Forks | 27,808 |
| Issues | 21 |
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
| Stars | 86,911 |
| 语言 | Python |
| Forks | 37,412 |
| Issues | 3,775 |
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
| Forks | 45,107 |
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
| Stars | 444,085 |
| 语言 | TypeScript |
| Forks | 44,447 |
| Issues | 193 |
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
| Stars | 354,092 |
| 语言 | TypeScript |
| Forks | 44,001 |
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
| Stars | 122,420 |
| 语言 | TypeScript |
| Forks | 13,501 |
| Issues | 3,023 |
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
| Stars | 113,475 |
| 语言 | TypeScript |
| Forks | 8,714 |
| Issues | 1,853 |
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
| Stars | 108,727 |
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
| Stars | 99,599 |
| 语言 | TypeScript |
| Forks | 5,529 |
| Issues | 693 |
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
| Stars | 97,922 |
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
| Stars | 94,830 |
| 语言 | TypeScript |
| Forks | 5,215 |
| Issues | 93 |
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
| Stars | 80,369 |
| 语言 | TypeScript |
| Forks | 8,120 |
| Issues | 743 |
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
| Stars | 244,824 |
| 语言 | JavaScript |
| Forks | 51,064 |
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
| Stars | 117,020 |
| 语言 | JavaScript |
| Forks | 35,537 |
| Issues | 2,669 |
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
| Stars | 112,290 |
| 语言 | JavaScript |
| Forks | 36,355 |
| Issues | 505 |
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
| Stars | 109,042 |
| 语言 | JavaScript |
| Forks | 11,662 |
| Issues | 165 |
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
| Stars | 98,266 |
| 语言 | JavaScript |
| Forks | 32,656 |
| Issues | 1,603 |
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
| Stars | 86,460 |
| 语言 | JavaScript |
| Forks | 4,900 |
| Issues | 998 |
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
| Stars | 67,769 |
| 语言 | JavaScript |
| Forks | 4,552 |
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
| Stars | 65,775 |
| 语言 | JavaScript |
| Forks | 9,356 |
| Issues | 204 |
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
| Stars | 64,332 |
| 语言 | JavaScript |
| Forks | 4,088 |
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
| Stars | 59,840 |
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
| Stars | 57,438 |
| 语言 | JavaScript |
| Forks | 12,310 |
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
| Stars | 53,236 |
| 语言 | JavaScript |
| Forks | 10,608 |
| Issues | 443 |
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
| Forks | 11,525 |
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
| Stars | 133,721 |
| 语言 | Go |
| Forks | 19,030 |
| Issues | 10,077 |
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
| Stars | 106,262 |
| 语言 | Go |
| Forks | 15,029 |
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
| Stars | 87,878 |
| 语言 | Go |
| Forks | 8,251 |
| Issues | 240 |
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
| Stars | 83,470 |
| 语言 | Go |
| Forks | 5,145 |
| Issues | 384 |
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
| Stars | 68,587 |
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
| Stars | 56,992 |
| 语言 | Go |
| Forks | 5,069 |
| Issues | 1,176 |
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
| Stars | 51,013 |
| 语言 | Go |
| Forks | 21,891 |
| Issues | 407 |
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
| Stars | 91,201 |
| 语言 | Shell |
| Forks | 14,922 |
| Issues | 119 |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 154,576 |
| 语言 | Python |
| Forks | 11,783 |
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
| Stars | 387,587 |
| 语言 | Python |
| Forks | 66,214 |
| Issues | 78 |
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
| Stars | 108,502 |
| 语言 | Unknown |
| Forks | 10,797 |
| Issues | 80 |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 220,680 |
| 语言 | Python |
| Forks | 50,519 |
| Issues | 949 |
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
| Stars | 98,828 |
| 语言 | Python |
| Forks | 12,136 |
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
| Stars | 86,537 |
| 语言 | Python |
| Forks | 7,256 |
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
| Stars | 77,440 |
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
| Stars | 139,299 |
| 语言 | TypeScript |
| Forks | 16,552 |
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
| Stars | 84,964 |
| 语言 | TypeScript |
| Forks | 10,576 |
| Issues | 400 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,364 |
| 语言 | TypeScript |
| Forks | 7,605 |
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
| Stars | 148,112 |
| 语言 | JavaScript |
| Forks | 26,697 |
| Issues | 159 |
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
| Stars | 95,705 |
| 语言 | JavaScript |
| Forks | 15,447 |
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
| Stars | 71,113 |
| 语言 | JavaScript |
| Forks | 16,798 |
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
| Stars | 67,399 |
| 语言 | JavaScript |
| Forks | 11,955 |
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
| Stars | 66,357 |
| 语言 | JavaScript |
| Forks | 9,185 |
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
| Stars | 61,260 |
| 语言 | JavaScript |
| Forks | 7,155 |
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
| Stars | 60,847 |
| 语言 | JavaScript |
| Forks | 5,659 |
| Issues | 69 |
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
| Stars | 50,887 |
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
| Stars | 49,418 |
| 语言 | Go |
| Forks | 7,945 |
| Issues | 568 |
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
| Stars | 46,865 |
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
| Stars | 46,204 |
| 语言 | Go |
| Forks | 3,808 |
| Issues | 81 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |
