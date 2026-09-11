# 项目发现报告 (2026-09-11)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 118 |
| 去重移除 | 43 |
| 已在监控 | 29 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 15 |
| 💬 LLM 界面 | 22 |
| 🧠 机器学习框架 | 7 |
| 🛠️ 开发工具 | 15 |
| ⚙️ DevOps/基础设施 | 12 |
| 📈 监控/观测 | 5 |
| 🌐 Web 框架 | 8 |
| 📊 数据/基础设施 | 5 |
| 📚 学习资源 | 14 |
| 📁 其他 | 54 |

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


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 244,578 |
| 语言 | Python |
| Forks | 50,688 |
| Issues | 42,103 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, hermes, hermes-agent, llm, nous-research, openai |
| 许可证 | MIT License |

---

Hermes-Agent 是一个拥有 24.4 万+ Stars 的高热度 AI Agent 项目，由 Nous Research 打造，被定位为"与你一同成长的智能体"。它以 MIT 许可开放源码，同时适配 OpenAI、Anthropic、Claude Code 等主流大模型生态，是当前 AI Agent 领域最具影响力且持续迭代的标杆项目之一。

**技术亮点**:
- 多模型无缝兼容：同时支持 OpenAI、Anthropic、ChatGPT、Claude Code、Codex 等主流 LLM 平台，开发者无需锁定单一供应商即可自由切换模型后端
- 自主成长机制：项目核心理念为 'The agent that grows with you'，具备通过对话和任务经验持续改进自身能力的学习架构
- 企业级许可证友好：采用 MIT License，允许商业使用、修改和再分发，极大降低了企业集成和二次开发的门槛
- 基于 Nous Research 的 Hermes 系列模型技术积累，在 Agent 推理、工具调用和长上下文理解方面具备技术优势
- 活跃生态与社区：超高 Star 数印证了项目的稳定性、社区活跃度和实际生产环境验证

**适用场景**:
- 企业级智能助手开发：可作为企业自有 AI 助手的内核，通过 MIT 协议自由接入内部系统，构建单聊代码生成、文档撰写、数据分析等内网智能体
- 个人开发者效率工具：作为个人编程助手，接入 Claude Code / Codex 等工具链，实现代码审查、自动化测试编写、技术调研等日常开发工作流的智能化提升
- AI 产品原型快速验证：借助其对多模型厂商的无缝支持，可在不同 LLM 后端间快速切换对比效果，低成本完成 AI 产品的 MVP 验证与迭代



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,668 |
| 语言 | Python |
| Forks | 22,190 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有超过 15 万 Star 的明星级自托管 AI 交互界面项目，它以极低的部署门槛和出色的用户体验，将 Ollama、OpenAI API 等多种 LLM 后端统一整合到一个现代化 Web 界面中，同时内置 RAG、MCP 等高级能力，是目前社区最受欢迎的 LLM 前端解决方案之一。

**技术亮点**:
- 统一后端支持：原生适配 Ollama、OpenAI API 等多种 LLM 提供方，支持通过 OpenAPI 扩展第三方模型服务，实现多模型统一管理
- 内置 RAG 能力：集成检索增强生成，支持文档上传、向量检索与上下文增强，让用户可以直接与私有知识库对话
- MCP 协议支持：支持 Model Context Protocol，可扩展接入外部工具和服务，增强了 AI 应用的互操作性
- 自托管架构：基于 Python 构建，支持 Docker 一键部署，数据完全掌握在用户手中，兼顾隐私与灵活性
- 现代化 UI 设计：提供直观友好的 Web 界面，涵盖聊天、模型管理、用户管理等完整功能模块，开箱即用

**适用场景**:
- 企业知识问答平台：利用内置 RAG 功能，企业可搭建私有化知识库问答系统，保护敏感数据不外泄
- 个人开发者 AI 工具集：开发者可快速部署统一的 LLM 聊天界面，集中管理本地 Ollama 模型和云 API，提升开发调试效率
- 团队协作 AI 工作台：为团队提供统一的自托管 AI 入口，支持多用户管理和模型切换，适合中小型团队降低 AI 使用门槛



### Graphify-Labs/graphify

**描述**: Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,005 |
| 语言 | Python |
| Forks | 11,326 |
| Issues | 1,326 |
| Topics | ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor, developer-tools, gemini, graphrag, knowledge-graph, leiden, llm, mcp, openclaw, rag, skills, tree-sitter |
| 许可证 | Apache License 2.0 |

---

Graphify 将任意代码库（包含文档、SQL Schema、配置文件、PDF）转换为可查询的知识图谱，通过本地确定性的 AST 解析实现零向量库依赖，为 AI 编码助手提供结构化的代码语义理解能力，是当前知识图谱与 AI Agent 结合领域极具创新性的开源项目。

**技术亮点**:
- 基于 Tree-sitter 的本地确定性 AST 解析，不依赖向量数据库即可构建精确的代码结构知识图谱，每条边都有明确的语义解释
- 原生支持 Claude Code、Cursor、Codex、Gemini CLI 等多种主流 AI 编码工具，以 /graphify skill 的形式无缝集成
- 内置 Leiden 社区发现算法用于图聚类，并结合 GraphRAG 与 MCP 协议，提供标准化的知识图谱查询接口
- 覆盖代码、文档、SQL Schema、配置文件和 PDF 等多类型知识源，实现全栈代码库的一站式知识提取

**适用场景**:
- 企业级大型代码库的智能代码搜索与理解：开发者在接手不熟悉的项目或进行代码评审时，可通过自然语言查询快速定位模块间依赖关系、函数调用链和数据流
- AI Agent 与编码助手的上下文增强：为 Claude Code 等工具提供精准的代码结构知识，提升 AI 生成代码的准确性，减少幻觉和上下文窗口浪费
- 个人开发者知识管理：将个人项目中的技术文档、SQL Schema、配置和笔记整合成可查询的知识图谱，建立个人代码知识资产库



### TauricResearch/TradingAgents

**描述**: TradingAgents: Multi-Agents LLM Financial Trading Framework

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,682 |
| 语言 | Python |
| Forks | 20,073 |
| Issues | 371 |
| Topics | agent, finance, llm, multiagent, trading |
| 许可证 | Apache License 2.0 |

---

TradingAgents 是一个基于多智能体 LLM 框架的金融交易系统，凭借超过 10 万 Stars 的社区认可度，它展示了如何利用多个大语言模型智能体协同工作来完成复杂的金融分析与交易决策，为量化交易和 AI 金融领域提供了极具参考价值的开源实现。

**技术亮点**:
- 多智能体架构：通过多个 LLM Agent 分工协作，模拟真实交易团队的分析、决策与执行流程
- 金融领域深度集成：融合市场数据分析、情绪分析、技术面分析等多维度信息源，构建完整交易决策链路
- 基于 Apache License 2.0 开源：提供完整的框架和示例代码，方便开发者二次开发与定制
- Python 生态：充分利用 Python 在金融数据处理和机器学习领域的成熟生态
- 可扩展的设计：灵活支持接入不同的 LLM 后端和金融数据源，适应多种交易场景

**适用场景**:
- 个人量化交易者：利用多智能体框架实现自动化交易策略的研究与部署，体验 AI 驱动的智能交易决策
- 企业金融科技团队：作为基础框架，用于构建内部智能投研系统和交易辅助工具，提升团队分析效率
- AI/金融领域研究者：研究多智能体 LLM 在金融决策中的应用，探索 Agent 协作模式与 prompt 工程最佳实践



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,688 |
| 语言 | TypeScript |
| Forks | 8,245 |
| Issues | 191 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是构建跨会话 AI 智能体记忆层的核心基础设施，通过自动捕获、AI 压缩和智能注入机制，完美解决了大语言模型"每次会话即失忆"的痛点。93K+ Stars 的超高关注度印证了它在多 Agent 生态（Claude Code、Codex、Gemini、Copilot 等）中的实战价值，并且基于 Apache 2.0 开源协议，可以放心用于生产环境。

**技术亮点**:
- 全面支持 8+ 主流 AI Agent 框架（Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode），实现跨工具的统一记忆层
- 基于 RAG 架构：使用 embeddings + ChromaDB/SQLite 实现向量化存储与语义检索，并集成 mem0、OpenMemory、SuperMemory 等主流记忆引擎
- 自动压缩机制：捕获会话全量数据后通过 AI 智能压缩，降低存储成本同时保留关键上下文信息
- 上下文注入引擎：在会话启动时自动检索相关历史记忆并注入当前会话，实现真正的持久化上下文
- TypeScript 构建，与 Claude Agent SDK 深度集成，支持 Claude Code 插件和 Skills 扩展

**适用场景**:
- 个人开发者：让 AI 编码助手（Claude Code、Copilot、Codex 等）跨会话记住项目上下文、技术决策和偏好设置，避免每次重新解释需求，大幅提升编码效率
- AI Agent 应用开发者：作为长短期记忆层接入自研 Agent 系统，实现跨会话的对话历史、用户画像和行为模式的持久化与召回
- 企业团队协作：建立团队级共享记忆库，让多个 AI Agent 在不同会话中协同工作时保持一致的项目认知和上下文，减少重复劳动和信息断层



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 256,464 |
| 语言 | JavaScript |
| Forks | 38,376 |
| Issues | 190 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

该项目的核心定位是Agent（智能体）性能优化的配置系统，它在Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具之上构建了统一的技能、记忆、安全与研发优化层，大幅提升AI Agent的实际生产力。在AI编码工具爆发式增长的当下，这一跨工具的统一优化方案具有极强的实用价值和生态潜力。

**技术亮点**:
- 跨平台Agent适配层：实现了对Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具的统一优化配置，屏蔽底层工具差异，实现一处配置处处生效
- 模块化架构设计：通过Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）四大核心模块的独立设计，实现了Agent能力的可插拔、可组合式管理
- 研究优先的研发理念：项目坚持research-first的开发方法论，确保每个优化模块都经过实证验证，而非盲目堆砌功能
- MCP（Model Context Protocol）集成：充分利用MCP这一开放的Agent工具协议生态，实现与外部工具和服务的无缝衔接，拓展Agent能力边界
- 高性能Harness优化：专注Agent执行效率的深度调优，而非仅提供表面配置，从系统层面提升Agent的响应速度和工作流吞吐量

**适用场景**:
- 企业级AI开发团队：需要统一管理团队中多个AI编码工具（Claude Code、Cursor等）的配置、技能和记忆，实现标准化和可复制的Agent工作流部署，同时满足企业安全合规要求
- 个人开发者高效编码：希望在多个AI编码环境中保持一致的技能库、提示词记忆和快捷键配置，避免每次切换工具时重复学习成本，最大化日常开发效率
- AI Agent框架研究者：关注Agent性能优化方法论，需要参考跨工具Harness优化、MCP集成、记忆机制设计等前沿实践的开源实现



### DietrichGebert/ponytail

**描述**: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,765 |
| 语言 | JavaScript |
| Forks | 7,274 |
| Issues | 256 |
| Topics | agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm, prompt-engineering, yagni |
| 许可证 | MIT License |

---

这是一个理念独特且极具哲学深度的AI Agent工具，它颠覆了传统"写更多代码"的思维，通过提示工程让AI代理像最懒惰的资深开发者一样思考——追求最少代码、最优方案。凭借13.5万+的Star和广泛的AI Agent生态支持（Claude Code、Cursor等），它代表了YAGNI原则在LLM编程时代的完美落地。

**技术亮点**:
- 基于YAGNI（You Aren't Gonna Need It）原则的提示词工程，引导AI Agent优先考虑不写代码的解决方案
- 为Claude Code、Cursor Rules等主流AI编程工具提供即插即用的agent-skills规则配置
- 轻量级JavaScript实现，将懒惰式开发哲学转化为具体的提示词模板和工程规则
- 深度优化prompt engineering策略，让AI从功能堆砌转向精准解决当前问题
- 聚焦agent-skills生态，与Claude Code Plugin生态无缝集成

**适用场景**:
- 个人开发者使用Claude Code或Cursor进行日常开发时，让AI助手在生成代码前先思考这个功能是否真的需要，避免过度工程化
- 企业AI开发团队将该项目作为Prompt规范基线，统一全团队的AI编程最佳实践，减少不必要代码量并提升代码库可维护性
- 学习AI Agent提示词工程的最佳实践案例，理解如何通过简洁的规则塑造AI的行为模式



### Mintplex-Labs/anything-llm

**描述**: Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,934 |
| 语言 | JavaScript |
| Forks | 7,309 |
| Issues | 310 |
| Topics | agent-computer, agent-harness, agent-orchestration, agentic-ai, ai-agents, computer-use, hermes-agent, llm, local-ai, localai, multimodal, no-code, open-claw, rag, self-hosted-ai, vector-database |
| 许可证 | MIT License |

---

AnythingLLM 是一个拥有 65,934 星标、以本地优先为核心的全栈 AI 代理与 RAG 平台，支持多模态、Agent 编排和自托管，让企业或个人开发者无需租赁第三方智能服务，即可完全掌控自己的 AI 能力，是当前开源社区中最全面的本地 AI 一体化解方案之一。

**技术亮点**:
- 本地优先架构：支持完全自托管，内置向量数据库和 RAG 管道，数据不出本地，保障隐私与合规
- 多模态与 Agent 编排：支持 agent-computer 和 computer-use，内置 hermes-agent，可实现视觉理解、电脑操作等多模态 AI 代理能力
- 多元化 RAG 支持：集成多种向量数据库，支持文档问答、知识库检索，并提供 no-code 界面降低使用门槛
- 灵活的模型接入：兼容多种主流 LLM 提供商及本地模型，可与 LocalAI 等本地推理引擎无缝对接
- MIT 开源许可证：完全开放源码，允许商用和二次开发，企业可根据需求深度定制

**适用场景**:
- 企业内部知识库助手：快速搭建基于公司文档的智能问答系统，支持多格式文档上传和向量检索，数据完全在本地处理，满足企业数据安全与合规要求
- 个人本地 AI 工作站：在个人电脑或 NAS 上部署本地 AI 助手，集成 RAG 记忆和多模态能力，无需付费订阅云端服务，实现「Own it」的目标
- AI Agent 开发平台：利用 agent-orchestration 和 agent-harness 能力，构建可编排的多代理自动化工作流，适用于 RPA、智能客服和自动化办公等场景



### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,875 |
| 语言 | JavaScript |
| Forks | 10,659 |
| Issues | 53 |
| Topics | ai, ai-agents, ai-prompts, anthropic, chatbot, chatgpt, claude, claude-code, codex, cursor, gemini, generative-ai, google, grok, llm, openai, prompt, prompt-engineering, system-prompt, system-prompts |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这个项目是AI领域极其稀缺的"系统提示词泄漏"资源库，收集了包括Anthropic Claude、OpenAI GPT、Google Gemini、xAI Grok等顶级大模型的官方系统提示词，拥有64.8K+ Stars，是研究大模型内部设计和prompt engineering的必读资料。

**技术亮点**:
- 覆盖多家顶级AI公司（Anthropic、OpenAI、Google、xAI）的最新模型系统提示词，包括Claude Fable 5.1、GPT-6-Astra等前沿模型
- 持续定期更新，确保提示词资料与最新模型版本保持同步
- 涵盖多种AI产品形态：聊天机器人（ChatGPT、Claude）、代码助手（Codex、Cursor）、设计工具（Claude Design、Antigravity）等
- 采用JavaScript组织形式呈现，便于开发者解析和处理数据
- 基于Creative Commons Zero许可发布，可自由使用、修改和分发，无版权限制

**适用场景**:
- Prompt Engineering研究者：分析和逆向工程顶级大模型的系统提示词设计逻辑，学习如何构建高质量的AI提示词
- AI产品开发者：借鉴官方提示词设计模式，优化自家AI产品的系统提示词，提升模型输出质量和行为控制能力
- 安全研究人员：分析系统提示词泄漏事件，研究AI安全边界和prompt injection防护策略



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,530 |
| 语言 | Go |
| Forks | 10,700 |
| Issues | 1,550 |
| Topics | agent-harness, agentic-ai, agentic-nagive, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-engineering, context-management, harness-engineering, knowledge-compilation, rag, retrieval-augmented-generation, search-harness |
| 许可证 | Apache License 2.0 |


### netdata/netdata

**描述**: The fastest path to AI-powered full stack observability, even for lean teams.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,485 |
| 语言 | Go |
| Forks | 6,622 |
| Issues | 393 |
| Topics | ai, alerting, cncf, data-visualization, database, devops, docker, grafana, influxdb, kubernetes, linux, machine-learning, mcp, mongodb, monitoring, mysql, netdata, observability, postgresql, prometheus |
| 许可证 | GNU General Public License v3.0 |


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,055 |
| 语言 | Go |
| Forks | 4,439 |
| Issues | 189 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |


### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,410 |
| 语言 | TypeScript |
| Forks | 15,878 |
| Issues | 925 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, fable, gemini, glm, gpt, knowledge-base, loop-engineering, mcp, openai, skills |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,446 |
| 语言 | Python |
| Forks | 9,744 |
| Issues | 201 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### headroomlabs-ai/headroom

**描述**: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,587 |
| 语言 | Python |
| Forks | 5,482 |
| Issues | 643 |
| Topics | agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain, llm, mcp, openai, prompt-engineering, proxy, python, rag, token-optimization, tokens, typescript |
| 许可证 | Apache License 2.0 |


### jeecgboot/JeecgBoot

**描述**: 【低代码v2.0，一句话即可生成整个系统】企业级AI低代码平台，一键生成前后端代码甚至整个系统。 AI Skills 一句话画流程、设计表单、生成报表、大屏。内置 AI应用平台涵盖：AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领AI低代码「Skills 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，解决 Java 项目 90% 重复工作，提高效率又不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,744 |
| 语言 | Java |
| Forks | 16,181 |
| Issues | 43 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### bojieli/ai-agent-book

**描述**: 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,908 |
| 语言 | Python |
| Forks | 5,131 |
| Issues | 22 |
| Topics | agent, agent-memory, ai-agent, book, coding-agent, context-engineering, large-language-models, llm, mcp, multi-agent, multimodal, rag, reinforcement-learning |
| 许可证 | Apache License 2.0 |


### koala73/worldmonitor

**描述**: Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,077 |
| 语言 | TypeScript |
| Forks | 13,046 |
| Issues | 337 |
| Topics | agent, ai, dashboard, geopolitics, mcp, mcp-server, monitoring, news, opensource, osint, palantir, situation |
| 许可证 | GNU Affero General Public License v3.0 |


### Snailclimb/JavaGuide

**描述**: Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 158,457 |
| 语言 | JavaScript |
| Forks | 46,140 |
| Issues | 18 |
| Topics | agent, ai, context-engineering, deepseek, interview, java, mcp, mysql, redis, redisson, skills, springai, system-design |
| 许可证 | Apache License 2.0 |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,231 |
| 语言 | Python |
| Forks | 20,192 |
| Issues | 11 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### firecrawl/firecrawl

**描述**: The context API to search, scrape, and interact with the web at scale. 🔥

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 179,192 |
| 语言 | TypeScript |
| Forks | 9,750 |
| Issues | 623 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |


### browser-use/browser-use

**描述**: Agents that use the browser.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 114,250 |
| 语言 | Python |
| Forks | 12,558 |
| Issues | 406 |
| Topics | ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python |
| 许可证 | MIT License |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 204,034 |
| 语言 | TypeScript |
| Forks | 60,641 |
| Issues | 1,137 |
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
| Stars | 154,596 |
| 语言 | Python |
| Forks | 10,067 |
| Issues | 1,049 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### farion1231/cc-switch

**描述**: A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,366 |
| 语言 | Rust |
| Forks | 9,128 |
| Issues | 2,657 |
| Topics | ai-tools, claude-code, codex, desktop-app, grok, grokbuild, hermes, hermes-agent, mcp, open-source, openclaw, openclaw-ui, opencode, pi, provider-management, rust, skills, skills-management, tauri, wsl-support |
| 许可证 | MIT License |


### Leonxlnx/taste-skill

**描述**: Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,266 |
| 语言 | JavaScript |
| Forks | 5,888 |
| Issues | 63 |
| Topics | agent, ai, claude, claude-code, codex, coding, design, frontend, lowcode, nocode, skill, skills, vibecoding |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,567 |
| 语言 | Python |
| Forks | 12,322 |
| Issues | 44 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,460 |
| 语言 | TypeScript |
| Forks | 24,998 |
| Issues | 1,040 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### deepseek-ai/deepseek-harness

**描述**: DeepSeek Harness: Everything is a Plugin.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 220,492 |
| 语言 | TypeScript |
| Forks | 26,119 |
| Issues | 0 |
| Topics | ai-agents, cordis, dsh, dsh-plugin |
| 许可证 | MIT License |


### Panniantong/Agent-Reach

**描述**: Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,472 |
| 语言 | Python |
| Forks | 6,855 |
| Issues | 133 |
| Topics | agent-infrastructure, ai-agent, ai-search, automation, bilibili, claude-code, cli, cursor, free-api, llm-tools, mcp, python, reddit-scraper, twitter-scraper, web-scraper, xiaohongshu, youtube-transcript |
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
| Stars | 151,668 |
| 语言 | Python |
| Forks | 22,190 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有超过 15 万 Star 的明星级自托管 AI 交互界面项目，它以极低的部署门槛和出色的用户体验，将 Ollama、OpenAI API 等多种 LLM 后端统一整合到一个现代化 Web 界面中，同时内置 RAG、MCP 等高级能力，是目前社区最受欢迎的 LLM 前端解决方案之一。

**技术亮点**:
- 统一后端支持：原生适配 Ollama、OpenAI API 等多种 LLM 提供方，支持通过 OpenAPI 扩展第三方模型服务，实现多模型统一管理
- 内置 RAG 能力：集成检索增强生成，支持文档上传、向量检索与上下文增强，让用户可以直接与私有知识库对话
- MCP 协议支持：支持 Model Context Protocol，可扩展接入外部工具和服务，增强了 AI 应用的互操作性
- 自托管架构：基于 Python 构建，支持 Docker 一键部署，数据完全掌握在用户手中，兼顾隐私与灵活性
- 现代化 UI 设计：提供直观友好的 Web 界面，涵盖聊天、模型管理、用户管理等完整功能模块，开箱即用

**适用场景**:
- 企业知识问答平台：利用内置 RAG 功能，企业可搭建私有化知识库问答系统，保护敏感数据不外泄
- 个人开发者 AI 工具集：开发者可快速部署统一的 LLM 聊天界面，集中管理本地 Ollama 模型和云 API，提升开发调试效率
- 团队协作 AI 工作台：为团队提供统一的自托管 AI 入口，支持多用户管理和模型切换，适合中小型团队降低 AI 使用门槛



### Graphify-Labs/graphify

**描述**: Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,005 |
| 语言 | Python |
| Forks | 11,326 |
| Issues | 1,326 |
| Topics | ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor, developer-tools, gemini, graphrag, knowledge-graph, leiden, llm, mcp, openclaw, rag, skills, tree-sitter |
| 许可证 | Apache License 2.0 |

---

Graphify 将任意代码库（包含文档、SQL Schema、配置文件、PDF）转换为可查询的知识图谱，通过本地确定性的 AST 解析实现零向量库依赖，为 AI 编码助手提供结构化的代码语义理解能力，是当前知识图谱与 AI Agent 结合领域极具创新性的开源项目。

**技术亮点**:
- 基于 Tree-sitter 的本地确定性 AST 解析，不依赖向量数据库即可构建精确的代码结构知识图谱，每条边都有明确的语义解释
- 原生支持 Claude Code、Cursor、Codex、Gemini CLI 等多种主流 AI 编码工具，以 /graphify skill 的形式无缝集成
- 内置 Leiden 社区发现算法用于图聚类，并结合 GraphRAG 与 MCP 协议，提供标准化的知识图谱查询接口
- 覆盖代码、文档、SQL Schema、配置文件和 PDF 等多类型知识源，实现全栈代码库的一站式知识提取

**适用场景**:
- 企业级大型代码库的智能代码搜索与理解：开发者在接手不熟悉的项目或进行代码评审时，可通过自然语言查询快速定位模块间依赖关系、函数调用链和数据流
- AI Agent 与编码助手的上下文增强：为 Claude Code 等工具提供精准的代码结构知识，提升 AI 生成代码的准确性，减少幻觉和上下文窗口浪费
- 个人开发者知识管理：将个人项目中的技术文档、SQL Schema、配置和笔记整合成可查询的知识图谱，建立个人代码知识资产库



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,688 |
| 语言 | TypeScript |
| Forks | 8,245 |
| Issues | 191 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是构建跨会话 AI 智能体记忆层的核心基础设施，通过自动捕获、AI 压缩和智能注入机制，完美解决了大语言模型"每次会话即失忆"的痛点。93K+ Stars 的超高关注度印证了它在多 Agent 生态（Claude Code、Codex、Gemini、Copilot 等）中的实战价值，并且基于 Apache 2.0 开源协议，可以放心用于生产环境。

**技术亮点**:
- 全面支持 8+ 主流 AI Agent 框架（Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode），实现跨工具的统一记忆层
- 基于 RAG 架构：使用 embeddings + ChromaDB/SQLite 实现向量化存储与语义检索，并集成 mem0、OpenMemory、SuperMemory 等主流记忆引擎
- 自动压缩机制：捕获会话全量数据后通过 AI 智能压缩，降低存储成本同时保留关键上下文信息
- 上下文注入引擎：在会话启动时自动检索相关历史记忆并注入当前会话，实现真正的持久化上下文
- TypeScript 构建，与 Claude Agent SDK 深度集成，支持 Claude Code 插件和 Skills 扩展

**适用场景**:
- 个人开发者：让 AI 编码助手（Claude Code、Copilot、Codex 等）跨会话记住项目上下文、技术决策和偏好设置，避免每次重新解释需求，大幅提升编码效率
- AI Agent 应用开发者：作为长短期记忆层接入自研 Agent 系统，实现跨会话的对话历史、用户画像和行为模式的持久化与召回
- 企业团队协作：建立团队级共享记忆库，让多个 AI Agent 在不同会话中协同工作时保持一致的项目认知和上下文，减少重复劳动和信息断层



### Mintplex-Labs/anything-llm

**描述**: Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,934 |
| 语言 | JavaScript |
| Forks | 7,309 |
| Issues | 310 |
| Topics | agent-computer, agent-harness, agent-orchestration, agentic-ai, ai-agents, computer-use, hermes-agent, llm, local-ai, localai, multimodal, no-code, open-claw, rag, self-hosted-ai, vector-database |
| 许可证 | MIT License |

---

AnythingLLM 是一个拥有 65,934 星标、以本地优先为核心的全栈 AI 代理与 RAG 平台，支持多模态、Agent 编排和自托管，让企业或个人开发者无需租赁第三方智能服务，即可完全掌控自己的 AI 能力，是当前开源社区中最全面的本地 AI 一体化解方案之一。

**技术亮点**:
- 本地优先架构：支持完全自托管，内置向量数据库和 RAG 管道，数据不出本地，保障隐私与合规
- 多模态与 Agent 编排：支持 agent-computer 和 computer-use，内置 hermes-agent，可实现视觉理解、电脑操作等多模态 AI 代理能力
- 多元化 RAG 支持：集成多种向量数据库，支持文档问答、知识库检索，并提供 no-code 界面降低使用门槛
- 灵活的模型接入：兼容多种主流 LLM 提供商及本地模型，可与 LocalAI 等本地推理引擎无缝对接
- MIT 开源许可证：完全开放源码，允许商用和二次开发，企业可根据需求深度定制

**适用场景**:
- 企业内部知识库助手：快速搭建基于公司文档的智能问答系统，支持多格式文档上传和向量检索，数据完全在本地处理，满足企业数据安全与合规要求
- 个人本地 AI 工作站：在个人电脑或 NAS 上部署本地 AI 助手，集成 RAG 记忆和多模态能力，无需付费订阅云端服务，实现「Own it」的目标
- AI Agent 开发平台：利用 agent-orchestration 和 agent-harness 能力，构建可编排的多代理自动化工作流，适用于 RPA、智能客服和自动化办公等场景



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,530 |
| 语言 | Go |
| Forks | 10,700 |
| Issues | 1,550 |
| Topics | agent-harness, agentic-ai, agentic-nagive, agentic-retrieval, agentic-search, ai, ai-agents, context-engine, context-engineering, context-management, harness-engineering, knowledge-compilation, rag, retrieval-augmented-generation, search-harness |
| 许可证 | Apache License 2.0 |


### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,410 |
| 语言 | TypeScript |
| Forks | 15,878 |
| Issues | 925 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, fable, gemini, glm, gpt, knowledge-base, loop-engineering, mcp, openai, skills |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,446 |
| 语言 | Python |
| Forks | 9,744 |
| Issues | 201 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### headroomlabs-ai/headroom

**描述**: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,587 |
| 语言 | Python |
| Forks | 5,482 |
| Issues | 643 |
| Topics | agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain, llm, mcp, openai, prompt-engineering, proxy, python, rag, token-optimization, tokens, typescript |
| 许可证 | Apache License 2.0 |


### jeecgboot/JeecgBoot

**描述**: 【低代码v2.0，一句话即可生成整个系统】企业级AI低代码平台，一键生成前后端代码甚至整个系统。 AI Skills 一句话画流程、设计表单、生成报表、大屏。内置 AI应用平台涵盖：AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领AI低代码「Skills 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，解决 Java 项目 90% 重复工作，提高效率又不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,744 |
| 语言 | Java |
| Forks | 16,181 |
| Issues | 43 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### bojieli/ai-agent-book

**描述**: 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,908 |
| 语言 | Python |
| Forks | 5,131 |
| Issues | 22 |
| Topics | agent, agent-memory, ai-agent, book, coding-agent, context-engineering, large-language-models, llm, mcp, multi-agent, multimodal, rag, reinforcement-learning |
| 许可证 | Apache License 2.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,066 |
| 语言 | TypeScript |
| Forks | 13,742 |
| Issues | 1,128 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Shubhamsaboo/awesome-llm-apps

**描述**: 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 96/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 137,231 |
| 语言 | Python |
| Forks | 20,192 |
| Issues | 11 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,062 |
| 语言 | Go |
| Forks | 4,244 |
| Issues | 1,409 |
| Topics | anns, cloud-native, diskann, distributed, embedding-database, embedding-similarity, embedding-store, faiss, golang, hnsw, image-search, llm, nearest-neighbor-search, rag, vector-database, vector-search, vector-similarity, vector-store |
| 许可证 | Apache License 2.0 |


### Egonex-AI/Understand-Anything

**描述**: Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,061 |
| 语言 | TypeScript |
| Forks | 6,898 |
| Issues | 303 |
| Topics | antigravity-skills, business-knowledge, claude-code, claude-skills, codebase-analysis, codex, codex-skills, developer-tools-ai-agent, gemini-cli-skills, karpathy-llm-wiki, knowledge-base, knowledge-graph, memory, opencode-skills, pi-agent, understandcode, vibe-coding |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,460 |
| 语言 | TypeScript |
| Forks | 24,998 |
| Issues | 1,040 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


## 💬 LLM 界面 (22 个项目) { #llm-界面 }


### 🌟 高优先级


### NousResearch/hermes-agent

**描述**: The agent that grows with you

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 244,578 |
| 语言 | Python |
| Forks | 50,688 |
| Issues | 42,103 |
| Topics | ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex, hermes, hermes-agent, llm, nous-research, openai |
| 许可证 | MIT License |

---

Hermes-Agent 是一个拥有 24.4 万+ Stars 的高热度 AI Agent 项目，由 Nous Research 打造，被定位为"与你一同成长的智能体"。它以 MIT 许可开放源码，同时适配 OpenAI、Anthropic、Claude Code 等主流大模型生态，是当前 AI Agent 领域最具影响力且持续迭代的标杆项目之一。

**技术亮点**:
- 多模型无缝兼容：同时支持 OpenAI、Anthropic、ChatGPT、Claude Code、Codex 等主流 LLM 平台，开发者无需锁定单一供应商即可自由切换模型后端
- 自主成长机制：项目核心理念为 'The agent that grows with you'，具备通过对话和任务经验持续改进自身能力的学习架构
- 企业级许可证友好：采用 MIT License，允许商业使用、修改和再分发，极大降低了企业集成和二次开发的门槛
- 基于 Nous Research 的 Hermes 系列模型技术积累，在 Agent 推理、工具调用和长上下文理解方面具备技术优势
- 活跃生态与社区：超高 Star 数印证了项目的稳定性、社区活跃度和实际生产环境验证

**适用场景**:
- 企业级智能助手开发：可作为企业自有 AI 助手的内核，通过 MIT 协议自由接入内部系统，构建单聊代码生成、文档撰写、数据分析等内网智能体
- 个人开发者效率工具：作为个人编程助手，接入 Claude Code / Codex 等工具链，实现代码审查、自动化测试编写、技术调研等日常开发工作流的智能化提升
- AI 产品原型快速验证：借助其对多模型厂商的无缝支持，可在不同 LLM 后端间快速切换对比效果，低成本完成 AI 产品的 MVP 验证与迭代



### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,668 |
| 语言 | Python |
| Forks | 22,190 |
| Issues | 301 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是一个拥有超过 15 万 Star 的明星级自托管 AI 交互界面项目，它以极低的部署门槛和出色的用户体验，将 Ollama、OpenAI API 等多种 LLM 后端统一整合到一个现代化 Web 界面中，同时内置 RAG、MCP 等高级能力，是目前社区最受欢迎的 LLM 前端解决方案之一。

**技术亮点**:
- 统一后端支持：原生适配 Ollama、OpenAI API 等多种 LLM 提供方，支持通过 OpenAPI 扩展第三方模型服务，实现多模型统一管理
- 内置 RAG 能力：集成检索增强生成，支持文档上传、向量检索与上下文增强，让用户可以直接与私有知识库对话
- MCP 协议支持：支持 Model Context Protocol，可扩展接入外部工具和服务，增强了 AI 应用的互操作性
- 自托管架构：基于 Python 构建，支持 Docker 一键部署，数据完全掌握在用户手中，兼顾隐私与灵活性
- 现代化 UI 设计：提供直观友好的 Web 界面，涵盖聊天、模型管理、用户管理等完整功能模块，开箱即用

**适用场景**:
- 企业知识问答平台：利用内置 RAG 功能，企业可搭建私有化知识库问答系统，保护敏感数据不外泄
- 个人开发者 AI 工具集：开发者可快速部署统一的 LLM 聊天界面，集中管理本地 Ollama 模型和云 API，提升开发调试效率
- 团队协作 AI 工作台：为团队提供统一的自托管 AI 入口，支持多用户管理和模型切换，适合中小型团队降低 AI 使用门槛



### thedotmack/claude-mem

**描述**: Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,688 |
| 语言 | TypeScript |
| Forks | 8,245 |
| Issues | 191 |
| Topics | ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk, claude-agents, claude-code, claude-code-plugin, claude-skills, embeddings, long-term-memory, mem0, memory-engine, openmemory, rag, sqlite, supermemory |
| 许可证 | Apache License 2.0 |

---

claude-mem 是构建跨会话 AI 智能体记忆层的核心基础设施，通过自动捕获、AI 压缩和智能注入机制，完美解决了大语言模型"每次会话即失忆"的痛点。93K+ Stars 的超高关注度印证了它在多 Agent 生态（Claude Code、Codex、Gemini、Copilot 等）中的实战价值，并且基于 Apache 2.0 开源协议，可以放心用于生产环境。

**技术亮点**:
- 全面支持 8+ 主流 AI Agent 框架（Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode），实现跨工具的统一记忆层
- 基于 RAG 架构：使用 embeddings + ChromaDB/SQLite 实现向量化存储与语义检索，并集成 mem0、OpenMemory、SuperMemory 等主流记忆引擎
- 自动压缩机制：捕获会话全量数据后通过 AI 智能压缩，降低存储成本同时保留关键上下文信息
- 上下文注入引擎：在会话启动时自动检索相关历史记忆并注入当前会话，实现真正的持久化上下文
- TypeScript 构建，与 Claude Agent SDK 深度集成，支持 Claude Code 插件和 Skills 扩展

**适用场景**:
- 个人开发者：让 AI 编码助手（Claude Code、Copilot、Codex 等）跨会话记住项目上下文、技术决策和偏好设置，避免每次重新解释需求，大幅提升编码效率
- AI Agent 应用开发者：作为长短期记忆层接入自研 Agent 系统，实现跨会话的对话历史、用户画像和行为模式的持久化与召回
- 企业团队协作：建立团队级共享记忆库，让多个 AI Agent 在不同会话中协同工作时保持一致的项目认知和上下文，减少重复劳动和信息断层



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 256,464 |
| 语言 | JavaScript |
| Forks | 38,376 |
| Issues | 190 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

该项目的核心定位是Agent（智能体）性能优化的配置系统，它在Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具之上构建了统一的技能、记忆、安全与研发优化层，大幅提升AI Agent的实际生产力。在AI编码工具爆发式增长的当下，这一跨工具的统一优化方案具有极强的实用价值和生态潜力。

**技术亮点**:
- 跨平台Agent适配层：实现了对Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具的统一优化配置，屏蔽底层工具差异，实现一处配置处处生效
- 模块化架构设计：通过Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）四大核心模块的独立设计，实现了Agent能力的可插拔、可组合式管理
- 研究优先的研发理念：项目坚持research-first的开发方法论，确保每个优化模块都经过实证验证，而非盲目堆砌功能
- MCP（Model Context Protocol）集成：充分利用MCP这一开放的Agent工具协议生态，实现与外部工具和服务的无缝衔接，拓展Agent能力边界
- 高性能Harness优化：专注Agent执行效率的深度调优，而非仅提供表面配置，从系统层面提升Agent的响应速度和工作流吞吐量

**适用场景**:
- 企业级AI开发团队：需要统一管理团队中多个AI编码工具（Claude Code、Cursor等）的配置、技能和记忆，实现标准化和可复制的Agent工作流部署，同时满足企业安全合规要求
- 个人开发者高效编码：希望在多个AI编码环境中保持一致的技能库、提示词记忆和快捷键配置，避免每次切换工具时重复学习成本，最大化日常开发效率
- AI Agent框架研究者：关注Agent性能优化方法论，需要参考跨工具Harness优化、MCP集成、记忆机制设计等前沿实践的开源实现



### DietrichGebert/ponytail

**描述**: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,765 |
| 语言 | JavaScript |
| Forks | 7,274 |
| Issues | 256 |
| Topics | agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm, prompt-engineering, yagni |
| 许可证 | MIT License |

---

这是一个理念独特且极具哲学深度的AI Agent工具，它颠覆了传统"写更多代码"的思维，通过提示工程让AI代理像最懒惰的资深开发者一样思考——追求最少代码、最优方案。凭借13.5万+的Star和广泛的AI Agent生态支持（Claude Code、Cursor等），它代表了YAGNI原则在LLM编程时代的完美落地。

**技术亮点**:
- 基于YAGNI（You Aren't Gonna Need It）原则的提示词工程，引导AI Agent优先考虑不写代码的解决方案
- 为Claude Code、Cursor Rules等主流AI编程工具提供即插即用的agent-skills规则配置
- 轻量级JavaScript实现，将懒惰式开发哲学转化为具体的提示词模板和工程规则
- 深度优化prompt engineering策略，让AI从功能堆砌转向精准解决当前问题
- 聚焦agent-skills生态，与Claude Code Plugin生态无缝集成

**适用场景**:
- 个人开发者使用Claude Code或Cursor进行日常开发时，让AI助手在生成代码前先思考这个功能是否真的需要，避免过度工程化
- 企业AI开发团队将该项目作为Prompt规范基线，统一全团队的AI编程最佳实践，减少不必要代码量并提升代码库可维护性
- 学习AI Agent提示词工程的最佳实践案例，理解如何通过简洁的规则塑造AI的行为模式



### career-ops-hq/career-ops

**描述**: Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,284 |
| 语言 | JavaScript |
| Forks | 13,444 |
| Issues | 512 |
| Topics | ai, ai-agent, anthropic, ats, automation, beginner-friendly, career, careerops, claude, claude-code, cli, first-timers-only, golang, good-first-issue, interview-prep, job-application, job-hunting, job-search, open-source, resume |
| 许可证 | MIT License |

---

这是一个将 AI 智能体能力深度整合到求职全流程的开源项目，利用 AI 自动扫描招聘网站、评估职位并生成结构化报告，同时支持在本地 AI 编码工具（如 Claude Code、Codex 等）中运行，兼具自动化效率和隐私保护的双重优势，对求职者极具实用价值。

**技术亮点**:
- 基于 AI Agent 架构，实现从职位扫描、评估到简历定制（A-H 报告）的端到端自动化流水线
- 采用 Global 1-5 评分体系评估职位匹配度，输出结构化 A-H 报告，兼顾可读性与可操作性
- 深度集成 Claude Code、Codex、OpenCode、Antigravity 等 AI 编码 CLI，实现本地化运行
- 支持多招聘网站扫描，内置跨平台职位聚合能力
- MIT 开源许可 + 对 beginner-friendly 友好，设有 good-first-issue 标签，社区参与门槛低

**适用场景**:
- 个人求职者：批量扫描多个招聘渠道，快速筛选匹配职位并生成结构化评分报告，节省海量时间和精力
- 求职者自动化工作流：在 AI 编码 CLI 中持续追踪求职申请进度，自动定制简历版本并管理申请状态
- 开发者/技术团队：作为开源 AI Agent 参考项目，学习如何构建本地化的 AI 自动化工作流，也可 fork 后二次开发针对特定行业或地区定制功能



### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,875 |
| 语言 | JavaScript |
| Forks | 10,659 |
| Issues | 53 |
| Topics | ai, ai-agents, ai-prompts, anthropic, chatbot, chatgpt, claude, claude-code, codex, cursor, gemini, generative-ai, google, grok, llm, openai, prompt, prompt-engineering, system-prompt, system-prompts |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这个项目是AI领域极其稀缺的"系统提示词泄漏"资源库，收集了包括Anthropic Claude、OpenAI GPT、Google Gemini、xAI Grok等顶级大模型的官方系统提示词，拥有64.8K+ Stars，是研究大模型内部设计和prompt engineering的必读资料。

**技术亮点**:
- 覆盖多家顶级AI公司（Anthropic、OpenAI、Google、xAI）的最新模型系统提示词，包括Claude Fable 5.1、GPT-6-Astra等前沿模型
- 持续定期更新，确保提示词资料与最新模型版本保持同步
- 涵盖多种AI产品形态：聊天机器人（ChatGPT、Claude）、代码助手（Codex、Cursor）、设计工具（Claude Design、Antigravity）等
- 采用JavaScript组织形式呈现，便于开发者解析和处理数据
- 基于Creative Commons Zero许可发布，可自由使用、修改和分发，无版权限制

**适用场景**:
- Prompt Engineering研究者：分析和逆向工程顶级大模型的系统提示词设计逻辑，学习如何构建高质量的AI提示词
- AI产品开发者：借鉴官方提示词设计模式，优化自家AI产品的系统提示词，提升模型输出质量和行为控制能力
- 安全研究人员：分析系统提示词泄漏事件，研究AI安全边界和prompt injection防护策略



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,024 |
| 语言 | Go |
| Forks | 6,082 |
| Issues | 125 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | Other |


### lobehub/lobehub

**描述**: 🤯 LobeHub is your Chief Agent Operator, organizing your agents into 7×24 operations by hiring, scheduling, and reporting on your entire AI team.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,410 |
| 语言 | TypeScript |
| Forks | 15,878 |
| Issues | 925 |
| Topics | agent, agent-collaboration, agent-harness, ai, cao, chatgpt, chief-agent-operator, claude, deepseek, fable, gemini, glm, gpt, knowledge-base, loop-engineering, mcp, openai, skills |
| 许可证 | Other |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,992 |
| 语言 | HTML |
| Forks | 21,861 |
| Issues | 77 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### headroomlabs-ai/headroom

**描述**: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,587 |
| 语言 | Python |
| Forks | 5,482 |
| Issues | 643 |
| Topics | agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain, llm, mcp, openai, prompt-engineering, proxy, python, rag, token-optimization, tokens, typescript |
| 许可证 | Apache License 2.0 |


### QuantumNous/new-api

**描述**: A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatible, Claude-compatible, or Gemini-compatible formats. A centralized gateway for personal and enterprise model management.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 99/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,922 |
| 语言 | Go |
| Forks | 11,459 |
| Issues | 1,380 |
| Topics | ai-gateway, claude, deepseek, gemini, newapi, openai, rerank |
| 许可证 | GNU Affero General Public License v3.0 |


### nextlevelbuilder/ui-ux-pro-max-skill

**描述**: An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 126,904 |
| 语言 | Python |
| Forks | 13,551 |
| Issues | 84 |
| Topics | ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai, html5, kiro, landing-page, mobile-ui, qoder, react, tailwindcss, trae, ui-design, uikit, windsurf-ai |
| 许可证 | MIT License |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,519 |
| 语言 | Python |
| Forks | 22,074 |
| Issues | 7,898 |
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
| Stars | 154,596 |
| 语言 | Python |
| Forks | 10,067 |
| Issues | 1,049 |
| Topics | agents, chatgpt, generative-ai, large-language-models, multiagent, react-flow |
| 许可证 | MIT License |


### router-for-me/CLIProxyAPI

**描述**: Wrap Antigravity, ChatGPT Codex, Claude Code, Grok Build as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 3.1 Pro, GPT 5.6 Series, Grok 4.5, Claude model through API

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 51,443 |
| 语言 | Go |
| Forks | 7,801 |
| Issues | 612 |
| Topics | antigravity, claude-code, cluade, codex, gemini, openai |
| 许可证 | MIT License |


### Leonxlnx/taste-skill

**描述**: Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 86,266 |
| 语言 | JavaScript |
| Forks | 5,888 |
| Issues | 63 |
| Topics | agent, ai, claude, claude-code, codex, coding, design, frontend, lowcode, nocode, skill, skills, vibecoding |
| 许可证 | MIT License |


### ollama/ollama

**描述**: Get up and running with Kimi-K2.6, GLM-5.2, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 180,693 |
| 语言 | Go |
| Forks | 17,817 |
| Issues | 3,964 |
| Topics | deepseek, gemma, gemma3, glm, go, golang, gpt-oss, llama, llama3, llm, llms, minimax, mistral, ollama, qwen |
| 许可证 | MIT License |


### ruvnet/RuView

**描述**: π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,056 |
| 语言 | Rust |
| Forks | 12,334 |
| Issues | 689 |
| Topics | awesome, claude, densepose, esp32, firmware, home-assistant, home-automation, iot, monitoring, networking, npm, pose-estimation, react, rf, self-learning, skills, spatial-intelligence, typescript, wifi, wifi-security |
| 许可证 | MIT License |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,567 |
| 语言 | Python |
| Forks | 12,322 |
| Issues | 44 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### FlowiseAI/Flowise

**描述**: Build AI Agents, Visually

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 55,460 |
| 语言 | TypeScript |
| Forks | 24,998 |
| Issues | 1,040 |
| Topics | agentic-ai, agentic-workflow, agents, artificial-intelligence, chatbot, chatgpt, javascript, langchain, large-language-models, low-code, multiagent-systems, no-code, openai, rag, react, typescript, workflow-automation |
| 许可证 | Other |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 182,668 |
| 语言 | Python |
| Forks | 13,429 |
| Issues | 633 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


## 🧠 机器学习框架 (7 个项目) { #机器学习框架 }


### 🌟 高优先级


### netdata/netdata

**描述**: The fastest path to AI-powered full stack observability, even for lean teams.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,485 |
| 语言 | Go |
| Forks | 6,622 |
| Issues | 393 |
| Topics | ai, alerting, cncf, data-visualization, database, devops, docker, grafana, influxdb, kubernetes, linux, machine-learning, mcp, mongodb, monitoring, mysql, netdata, observability, postgresql, prometheus |
| 许可证 | GNU General Public License v3.0 |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,992 |
| 语言 | HTML |
| Forks | 21,861 |
| Issues | 77 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### rasbt/LLMs-from-scratch

**描述**: Implement a ChatGPT-like LLM in PyTorch from scratch, step by step

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,784 |
| 语言 | Jupyter Notebook |
| Forks | 16,059 |
| Issues | 1 |
| Topics | ai, artificial-intelligence, attention-mechanism, deep-learning, finetuning, from-scratch, generative-ai, gpt, instruction-tuning, language-model, large-language-models, llm, machine-learning, natural-language-processing, pretraining, python, pytorch, tokenizer, transformers |
| 许可证 | Other |


### huggingface/transformers

**描述**: 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 165,129 |
| 语言 | Python |
| Forks | 34,517 |
| Issues | 2,402 |
| Topics | audio, deep-learning, deepseek, gemma, glm, hacktoberfest, llm, machine-learning, model-hub, natural-language-processing, nlp, pretrained-models, python, pytorch, pytorch-transformers, qwen, speech-recognition, transformer, vlm |
| 许可证 | Apache License 2.0 |


### vllm-project/vllm

**描述**: A high-throughput and memory-efficient inference and serving engine for LLMs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,519 |
| 语言 | Python |
| Forks | 22,074 |
| Issues | 7,898 |
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
| Stars | 132,586 |
| 语言 | Python |
| Forks | 15,645 |
| Issues | 4,865 |
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
| Stars | 102,931 |
| 语言 | Python |
| Forks | 29,198 |
| Issues | 17,722 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


## 🛠️ 开发工具 (15 个项目) { #开发工具 }


### 🌟 高优先级


### Graphify-Labs/graphify

**描述**: Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 117,005 |
| 语言 | Python |
| Forks | 11,326 |
| Issues | 1,326 |
| Topics | ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor, developer-tools, gemini, graphrag, knowledge-graph, leiden, llm, mcp, openclaw, rag, skills, tree-sitter |
| 许可证 | Apache License 2.0 |

---

Graphify 将任意代码库（包含文档、SQL Schema、配置文件、PDF）转换为可查询的知识图谱，通过本地确定性的 AST 解析实现零向量库依赖，为 AI 编码助手提供结构化的代码语义理解能力，是当前知识图谱与 AI Agent 结合领域极具创新性的开源项目。

**技术亮点**:
- 基于 Tree-sitter 的本地确定性 AST 解析，不依赖向量数据库即可构建精确的代码结构知识图谱，每条边都有明确的语义解释
- 原生支持 Claude Code、Cursor、Codex、Gemini CLI 等多种主流 AI 编码工具，以 /graphify skill 的形式无缝集成
- 内置 Leiden 社区发现算法用于图聚类，并结合 GraphRAG 与 MCP 协议，提供标准化的知识图谱查询接口
- 覆盖代码、文档、SQL Schema、配置文件和 PDF 等多类型知识源，实现全栈代码库的一站式知识提取

**适用场景**:
- 企业级大型代码库的智能代码搜索与理解：开发者在接手不熟悉的项目或进行代码评审时，可通过自然语言查询快速定位模块间依赖关系、函数调用链和数据流
- AI Agent 与编码助手的上下文增强：为 Claude Code 等工具提供精准的代码结构知识，提升 AI 生成代码的准确性，减少幻觉和上下文窗口浪费
- 个人开发者知识管理：将个人项目中的技术文档、SQL Schema、配置和笔记整合成可查询的知识图谱，建立个人代码知识资产库



### affaan-m/ECC

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 256,464 |
| 语言 | JavaScript |
| Forks | 38,376 |
| Issues | 190 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

该项目的核心定位是Agent（智能体）性能优化的配置系统，它在Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具之上构建了统一的技能、记忆、安全与研发优化层，大幅提升AI Agent的实际生产力。在AI编码工具爆发式增长的当下，这一跨工具的统一优化方案具有极强的实用价值和生态潜力。

**技术亮点**:
- 跨平台Agent适配层：实现了对Claude Code、Codex、Opencode、Cursor等多款主流AI编码工具的统一优化配置，屏蔽底层工具差异，实现一处配置处处生效
- 模块化架构设计：通过Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）四大核心模块的独立设计，实现了Agent能力的可插拔、可组合式管理
- 研究优先的研发理念：项目坚持research-first的开发方法论，确保每个优化模块都经过实证验证，而非盲目堆砌功能
- MCP（Model Context Protocol）集成：充分利用MCP这一开放的Agent工具协议生态，实现与外部工具和服务的无缝衔接，拓展Agent能力边界
- 高性能Harness优化：专注Agent执行效率的深度调优，而非仅提供表面配置，从系统层面提升Agent的响应速度和工作流吞吐量

**适用场景**:
- 企业级AI开发团队：需要统一管理团队中多个AI编码工具（Claude Code、Cursor等）的配置、技能和记忆，实现标准化和可复制的Agent工作流部署，同时满足企业安全合规要求
- 个人开发者高效编码：希望在多个AI编码环境中保持一致的技能库、提示词记忆和快捷键配置，避免每次切换工具时重复学习成本，最大化日常开发效率
- AI Agent框架研究者：关注Agent性能优化方法论，需要参考跨工具Harness优化、MCP集成、记忆机制设计等前沿实践的开源实现



### DietrichGebert/ponytail

**描述**: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,765 |
| 语言 | JavaScript |
| Forks | 7,274 |
| Issues | 256 |
| Topics | agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm, prompt-engineering, yagni |
| 许可证 | MIT License |

---

这是一个理念独特且极具哲学深度的AI Agent工具，它颠覆了传统"写更多代码"的思维，通过提示工程让AI代理像最懒惰的资深开发者一样思考——追求最少代码、最优方案。凭借13.5万+的Star和广泛的AI Agent生态支持（Claude Code、Cursor等），它代表了YAGNI原则在LLM编程时代的完美落地。

**技术亮点**:
- 基于YAGNI（You Aren't Gonna Need It）原则的提示词工程，引导AI Agent优先考虑不写代码的解决方案
- 为Claude Code、Cursor Rules等主流AI编程工具提供即插即用的agent-skills规则配置
- 轻量级JavaScript实现，将懒惰式开发哲学转化为具体的提示词模板和工程规则
- 深度优化prompt engineering策略，让AI从功能堆砌转向精准解决当前问题
- 聚焦agent-skills生态，与Claude Code Plugin生态无缝集成

**适用场景**:
- 个人开发者使用Claude Code或Cursor进行日常开发时，让AI助手在生成代码前先思考这个功能是否真的需要，避免过度工程化
- 企业AI开发团队将该项目作为Prompt规范基线，统一全团队的AI编程最佳实践，减少不必要代码量并提升代码库可维护性
- 学习AI Agent提示词工程的最佳实践案例，理解如何通过简洁的规则塑造AI的行为模式



### career-ops-hq/career-ops

**描述**: Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,284 |
| 语言 | JavaScript |
| Forks | 13,444 |
| Issues | 512 |
| Topics | ai, ai-agent, anthropic, ats, automation, beginner-friendly, career, careerops, claude, claude-code, cli, first-timers-only, golang, good-first-issue, interview-prep, job-application, job-hunting, job-search, open-source, resume |
| 许可证 | MIT License |

---

这是一个将 AI 智能体能力深度整合到求职全流程的开源项目，利用 AI 自动扫描招聘网站、评估职位并生成结构化报告，同时支持在本地 AI 编码工具（如 Claude Code、Codex 等）中运行，兼具自动化效率和隐私保护的双重优势，对求职者极具实用价值。

**技术亮点**:
- 基于 AI Agent 架构，实现从职位扫描、评估到简历定制（A-H 报告）的端到端自动化流水线
- 采用 Global 1-5 评分体系评估职位匹配度，输出结构化 A-H 报告，兼顾可读性与可操作性
- 深度集成 Claude Code、Codex、OpenCode、Antigravity 等 AI 编码 CLI，实现本地化运行
- 支持多招聘网站扫描，内置跨平台职位聚合能力
- MIT 开源许可 + 对 beginner-friendly 友好，设有 good-first-issue 标签，社区参与门槛低

**适用场景**:
- 个人求职者：批量扫描多个招聘渠道，快速筛选匹配职位并生成结构化评分报告，节省海量时间和精力
- 求职者自动化工作流：在 AI 编码 CLI 中持续追踪求职申请进度，自动定制简历版本并管理申请状态
- 开发者/技术团队：作为开源 AI Agent 参考项目，学习如何构建本地化的 AI 自动化工作流，也可 fork 后二次开发针对特定行业或地区定制功能



### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,055 |
| 语言 | Go |
| Forks | 4,439 |
| Issues | 189 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |


### jeecgboot/JeecgBoot

**描述**: 【低代码v2.0，一句话即可生成整个系统】企业级AI低代码平台，一键生成前后端代码甚至整个系统。 AI Skills 一句话画流程、设计表单、生成报表、大屏。内置 AI应用平台涵盖：AI聊天、知识库、流程编排、MCP插件等，兼容主流大模型。引领AI低代码「Skills 生成 → 在线配置 → 代码生成 → 手工合并->AI修改」开发模式，解决 Java 项目 90% 重复工作，提高效率又不失灵活。

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 47,744 |
| 语言 | Java |
| Forks | 16,181 |
| Issues | 43 |
| Topics | activiti, agent, ai, antd, claude-code, cli, codegenerator, codex, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, skills, spring-ai, springboot, springcloud, vue3 |
| 许可证 | Apache License 2.0 |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 204,034 |
| 语言 | TypeScript |
| Forks | 60,641 |
| Issues | 1,137 |
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
| Stars | 478,991 |
| 语言 | Python |
| Forks | 52,852 |
| Issues | 1,940 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### microsoft/vscode

**描述**: Visual Studio Code

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 192,019 |
| 语言 | TypeScript |
| Forks | 42,108 |
| Issues | 20,947 |
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
| Stars | 95,576 |
| 语言 | TypeScript |
| Forks | 9,570 |
| Issues | 257 |
| Topics | automation, chrome, chromium, developer-tools, firefox, headless-chrome, node-module, testing, web |
| 许可证 | Apache License 2.0 |


### junegunn/fzf

**描述**: :cherry_blossom: A command-line fuzzy finder

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 82,921 |
| 语言 | Go |
| Forks | 2,868 |
| Issues | 328 |
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
| Stars | 82,246 |
| 语言 | Go |
| Forks | 3,031 |
| Issues | 1,034 |
| Topics | cli, git, terminal |
| 许可证 | MIT License |


### Panniantong/Agent-Reach

**描述**: Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,472 |
| 语言 | Python |
| Forks | 6,855 |
| Issues | 133 |
| Topics | agent-infrastructure, ai-agent, ai-search, automation, bilibili, claude-code, cli, cursor, free-api, llm-tools, mcp, python, reddit-scraper, twitter-scraper, web-scraper, xiaohongshu, youtube-transcript |
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
| Stars | 190,483 |
| 语言 | Python |
| Forks | 16,535 |
| Issues | 2,646 |
| Topics | cli, downloader, python, sponsorblock, youtube-dl, youtube-downloader, yt-dlp |
| 许可证 | The Unlicense |


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 102,258 |
| 语言 | Python |
| Forks | 9,872 |
| Issues | 81 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (12 个项目) { #devops-基础设施 }


### 🌟 高优先级


### career-ops-hq/career-ops

**描述**: Open-source AI job search: scan job portals, evaluate listings into a structured A-H report with a global 1-5 score, tailor your CV, track applications — runs locally in your AI coding CLI (Claude Code, Codex, OpenCode, Antigravity…)

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,284 |
| 语言 | JavaScript |
| Forks | 13,444 |
| Issues | 512 |
| Topics | ai, ai-agent, anthropic, ats, automation, beginner-friendly, career, careerops, claude, claude-code, cli, first-timers-only, golang, good-first-issue, interview-prep, job-application, job-hunting, job-search, open-source, resume |
| 许可证 | MIT License |

---

这是一个将 AI 智能体能力深度整合到求职全流程的开源项目，利用 AI 自动扫描招聘网站、评估职位并生成结构化报告，同时支持在本地 AI 编码工具（如 Claude Code、Codex 等）中运行，兼具自动化效率和隐私保护的双重优势，对求职者极具实用价值。

**技术亮点**:
- 基于 AI Agent 架构，实现从职位扫描、评估到简历定制（A-H 报告）的端到端自动化流水线
- 采用 Global 1-5 评分体系评估职位匹配度，输出结构化 A-H 报告，兼顾可读性与可操作性
- 深度集成 Claude Code、Codex、OpenCode、Antigravity 等 AI 编码 CLI，实现本地化运行
- 支持多招聘网站扫描，内置跨平台职位聚合能力
- MIT 开源许可 + 对 beginner-friendly 友好，设有 good-first-issue 标签，社区参与门槛低

**适用场景**:
- 个人求职者：批量扫描多个招聘渠道，快速筛选匹配职位并生成结构化评分报告，节省海量时间和精力
- 求职者自动化工作流：在 AI 编码 CLI 中持续追踪求职申请进度，自动定制简历版本并管理申请状态
- 开发者/技术团队：作为开源 AI Agent 参考项目，学习如何构建本地化的 AI 自动化工作流，也可 fork 后二次开发针对特定行业或地区定制功能



### netdata/netdata

**描述**: The fastest path to AI-powered full stack observability, even for lean teams.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,485 |
| 语言 | Go |
| Forks | 6,622 |
| Issues | 393 |
| Topics | ai, alerting, cncf, data-visualization, database, devops, docker, grafana, influxdb, kubernetes, linux, machine-learning, mcp, mongodb, monitoring, mysql, netdata, observability, postgresql, prometheus |
| 许可证 | GNU General Public License v3.0 |


### n8n-io/n8n

**描述**: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 204,034 |
| 语言 | TypeScript |
| Forks | 60,641 |
| Issues | 1,137 |
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
| Stars | 52,249 |
| 语言 | Go |
| Forks | 10,495 |
| Issues | 339 |
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
| Stars | 127,345 |
| 语言 | Go |
| Forks | 44,039 |
| Issues | 3,029 |
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
| Stars | 72,082 |
| 语言 | Go |
| Forks | 19,219 |
| Issues | 3,896 |
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
| Stars | 57,954 |
| 语言 | Go |
| Forks | 7,133 |
| Issues | 2,456 |
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
| Stars | 95,576 |
| 语言 | TypeScript |
| Forks | 9,570 |
| Issues | 257 |
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
| Stars | 91,277 |
| 语言 | JavaScript |
| Forks | 8,395 |
| Issues | 804 |
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
| Stars | 64,815 |
| 语言 | Go |
| Forks | 6,195 |
| Issues | 918 |
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
| Stars | 62,917 |
| 语言 | Go |
| Forks | 4,739 |
| Issues | 67 |
| Topics | docker, foss, go, markdown, memo, microblog, note-taking, notecard, own-your-data, react, self-hosted, social-network, sqlite |
| 许可证 | MIT License |


### Panniantong/Agent-Reach

**描述**: Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 81/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,472 |
| 语言 | Python |
| Forks | 6,855 |
| Issues | 133 |
| Topics | agent-infrastructure, ai-agent, ai-search, automation, bilibili, claude-code, cli, cursor, free-api, llm-tools, mcp, python, reddit-scraper, twitter-scraper, web-scraper, xiaohongshu, youtube-transcript |
| 许可证 | MIT License |


## 📈 监控/观测 (5 个项目) { #监控-观测 }


### 🌟 高优先级


### netdata/netdata

**描述**: The fastest path to AI-powered full stack observability, even for lean teams.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,485 |
| 语言 | Go |
| Forks | 6,622 |
| Issues | 393 |
| Topics | ai, alerting, cncf, data-visualization, database, devops, docker, grafana, influxdb, kubernetes, linux, machine-learning, mcp, mongodb, monitoring, mysql, netdata, observability, postgresql, prometheus |
| 许可证 | GNU General Public License v3.0 |


### koala73/worldmonitor

**描述**: Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 86,077 |
| 语言 | TypeScript |
| Forks | 13,046 |
| Issues | 337 |
| Topics | agent, ai, dashboard, geopolitics, mcp, mcp-server, monitoring, news, opensource, osint, palantir, situation |
| 许可证 | GNU Affero General Public License v3.0 |


### ruvnet/RuView

**描述**: π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,056 |
| 语言 | Rust |
| Forks | 12,334 |
| Issues | 689 |
| Topics | awesome, claude, densepose, esp32, firmware, home-assistant, home-automation, iot, monitoring, networking, npm, pose-estimation, react, rf, self-learning, skills, spatial-intelligence, typescript, wifi, wifi-security |
| 许可证 | MIT License |


### louislam/uptime-kuma

**描述**: A fancy self-hosted monitoring tool

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,277 |
| 语言 | JavaScript |
| Forks | 8,395 |
| Issues | 804 |
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
| Stars | 66,048 |
| 语言 | Go |
| Forks | 10,831 |
| Issues | 887 |
| Topics | alerting, graphing, hacktoberfest, metrics, monitoring, prometheus, time-series |
| 许可证 | Apache License 2.0 |


## 🌐 Web 框架 (8 个项目) { #web-框架 }


### 🌟 高优先级


### mudler/LocalAI

**描述**: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,055 |
| 语言 | Go |
| Forks | 4,439 |
| Issues | 189 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |


### public-apis/public-apis

**描述**: A collective list of free APIs

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 478,991 |
| 语言 | Python |
| Forks | 52,852 |
| Issues | 1,940 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


### angular/angular

**描述**: Deliver web apps with confidence 🚀

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 100,995 |
| 语言 | TypeScript |
| Forks | 27,451 |
| Issues | 1,166 |
| Topics | angular, javascript, pwa, typescript, web, web-framework, web-performance |
| 许可证 | MIT License |


### expressjs/express

**描述**: Fast, unopinionated, minimalist web framework for node.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,453 |
| 语言 | JavaScript |
| Forks | 24,969 |
| Issues | 230 |
| Topics | express, javascript, nodejs, server |
| 许可证 | MIT License |


### caddyserver/caddy

**描述**: Fast and extensible multi-platform HTTP/1-2-3 web server with automatic HTTPS

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,659 |
| 语言 | Go |
| Forks | 4,952 |
| Issues | 276 |
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
| Stars | 61,017 |
| 语言 | Go |
| Forks | 3,680 |
| Issues | 19 |
| Topics | authentication, backend, golang, realtime |
| 许可证 | MIT License |


### ⭐ 中优先级


### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 102,258 |
| 语言 | Python |
| Forks | 9,872 |
| Issues | 81 |
| Topics | api, async, asyncio, fastapi, framework, json, json-schema, openapi, openapi3, pydantic, python, python-types, python3, redoc, rest, starlette, swagger, swagger-ui, uvicorn, web |
| 许可证 | MIT License |


### gin-gonic/gin

**描述**: Gin is a high-performance HTTP web framework written in Go. It provides a Martini-like API but with significantly better performance—up to 40 times faster—thanks to httprouter. Gin is designed for building REST APIs, web applications, and microservices.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 89,201 |
| 语言 | Go |
| Forks | 8,692 |
| Issues | 770 |
| Topics | framework, gin, go, middleware, performance, router, server |
| 许可证 | MIT License |


## 📊 数据/基础设施 (5 个项目) { #数据-基础设施 }


### 🌟 高优先级


### Mintplex-Labs/anything-llm

**描述**: Stop renting your intelligence. Own it with AnythingLLM. Everything you need for a powerful local-first agent experience 

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 65,934 |
| 语言 | JavaScript |
| Forks | 7,309 |
| Issues | 310 |
| Topics | agent-computer, agent-harness, agent-orchestration, agentic-ai, ai-agents, computer-use, hermes-agent, llm, local-ai, localai, multimodal, no-code, open-claw, rag, self-hosted-ai, vector-database |
| 许可证 | MIT License |

---

AnythingLLM 是一个拥有 65,934 星标、以本地优先为核心的全栈 AI 代理与 RAG 平台，支持多模态、Agent 编排和自托管，让企业或个人开发者无需租赁第三方智能服务，即可完全掌控自己的 AI 能力，是当前开源社区中最全面的本地 AI 一体化解方案之一。

**技术亮点**:
- 本地优先架构：支持完全自托管，内置向量数据库和 RAG 管道，数据不出本地，保障隐私与合规
- 多模态与 Agent 编排：支持 agent-computer 和 computer-use，内置 hermes-agent，可实现视觉理解、电脑操作等多模态 AI 代理能力
- 多元化 RAG 支持：集成多种向量数据库，支持文档问答、知识库检索，并提供 no-code 界面降低使用门槛
- 灵活的模型接入：兼容多种主流 LLM 提供商及本地模型，可与 LocalAI 等本地推理引擎无缝对接
- MIT 开源许可证：完全开放源码，允许商用和二次开发，企业可根据需求深度定制

**适用场景**:
- 企业内部知识库助手：快速搭建基于公司文档的智能问答系统，支持多格式文档上传和向量检索，数据完全在本地处理，满足企业数据安全与合规要求
- 个人本地 AI 工作站：在个人电脑或 NAS 上部署本地 AI 助手，集成 RAG 记忆和多模态能力，无需付费订阅云端服务，实现「Own it」的目标
- AI Agent 开发平台：利用 agent-orchestration 和 agent-harness 能力，构建可编排的多代理自动化工作流，适用于 RPA、智能客服和自动化办公等场景



### netdata/netdata

**描述**: The fastest path to AI-powered full stack observability, even for lean teams.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,485 |
| 语言 | Go |
| Forks | 6,622 |
| Issues | 393 |
| Topics | ai, alerting, cncf, data-visualization, database, devops, docker, grafana, influxdb, kubernetes, linux, machine-learning, mcp, mongodb, monitoring, mysql, netdata, observability, postgresql, prometheus |
| 许可证 | GNU General Public License v3.0 |


### supabase/supabase

**描述**: The Postgres development platform. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,066 |
| 语言 | TypeScript |
| Forks | 13,742 |
| Issues | 1,128 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### milvus-io/milvus

**描述**: Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 95/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 46,062 |
| 语言 | Go |
| Forks | 4,244 |
| Issues | 1,409 |
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
| Stars | 52,249 |
| 语言 | Go |
| Forks | 10,495 |
| Issues | 339 |
| Topics | cncf, consensus, database, distributed-database, distributed-systems, etcd, go, key-value, kubernetes, raft |
| 许可证 | Apache License 2.0 |


## 📚 学习资源 (14 个项目) { #学习资源 }


### 🌟 高优先级


### DietrichGebert/ponytail

**描述**: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,765 |
| 语言 | JavaScript |
| Forks | 7,274 |
| Issues | 256 |
| Topics | agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm, prompt-engineering, yagni |
| 许可证 | MIT License |

---

这是一个理念独特且极具哲学深度的AI Agent工具，它颠覆了传统"写更多代码"的思维，通过提示工程让AI代理像最懒惰的资深开发者一样思考——追求最少代码、最优方案。凭借13.5万+的Star和广泛的AI Agent生态支持（Claude Code、Cursor等），它代表了YAGNI原则在LLM编程时代的完美落地。

**技术亮点**:
- 基于YAGNI（You Aren't Gonna Need It）原则的提示词工程，引导AI Agent优先考虑不写代码的解决方案
- 为Claude Code、Cursor Rules等主流AI编程工具提供即插即用的agent-skills规则配置
- 轻量级JavaScript实现，将懒惰式开发哲学转化为具体的提示词模板和工程规则
- 深度优化prompt engineering策略，让AI从功能堆砌转向精准解决当前问题
- 聚焦agent-skills生态，与Claude Code Plugin生态无缝集成

**适用场景**:
- 个人开发者使用Claude Code或Cursor进行日常开发时，让AI助手在生成代码前先思考这个功能是否真的需要，避免过度工程化
- 企业AI开发团队将该项目作为Prompt规范基线，统一全团队的AI编程最佳实践，减少不必要代码量并提升代码库可维护性
- 学习AI Agent提示词工程的最佳实践案例，理解如何通过简洁的规则塑造AI的行为模式



### asgeirtj/system_prompts_leaks

**描述**: Extracted system prompts from Anthropic - Claude Fable 5.1, Opus 5, Claude Design, Claude Code. OpenAI - ChatGPT GPT-6-Astra, Codex. Google - Gemini 3.8 Flash, 3.1 Pro, Antigravity. xAI - Grok, Grok Bot, Cursor, Kimi and more! Updated regularly.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 64,875 |
| 语言 | JavaScript |
| Forks | 10,659 |
| Issues | 53 |
| Topics | ai, ai-agents, ai-prompts, anthropic, chatbot, chatgpt, claude, claude-code, codex, cursor, gemini, generative-ai, google, grok, llm, openai, prompt, prompt-engineering, system-prompt, system-prompts |
| 许可证 | Creative Commons Zero v1.0 Universal |

---

这个项目是AI领域极其稀缺的"系统提示词泄漏"资源库，收集了包括Anthropic Claude、OpenAI GPT、Google Gemini、xAI Grok等顶级大模型的官方系统提示词，拥有64.8K+ Stars，是研究大模型内部设计和prompt engineering的必读资料。

**技术亮点**:
- 覆盖多家顶级AI公司（Anthropic、OpenAI、Google、xAI）的最新模型系统提示词，包括Claude Fable 5.1、GPT-6-Astra等前沿模型
- 持续定期更新，确保提示词资料与最新模型版本保持同步
- 涵盖多种AI产品形态：聊天机器人（ChatGPT、Claude）、代码助手（Codex、Cursor）、设计工具（Claude Design、Antigravity）等
- 采用JavaScript组织形式呈现，便于开发者解析和处理数据
- 基于Creative Commons Zero许可发布，可自由使用、修改和分发，无版权限制

**适用场景**:
- Prompt Engineering研究者：分析和逆向工程顶级大模型的系统提示词设计逻辑，学习如何构建高质量的AI提示词
- AI产品开发者：借鉴官方提示词设计模式，优化自家AI产品的系统提示词，提升模型输出质量和行为控制能力
- 安全研究人员：分析系统提示词泄漏事件，研究AI安全边界和prompt injection防护策略



### JuliusBrussee/caveman

**描述**: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 105,024 |
| 语言 | Go |
| Forks | 6,082 |
| Issues | 125 |
| Topics | ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering, skill, tokens |
| 许可证 | Other |


### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 169,992 |
| 语言 | HTML |
| Forks | 21,861 |
| Issues | 77 |
| Topics | ai, artificial-intelligence, awesome-list, chatgpt, chatgpt-prompts, claude, gemini, gpt, gpt-4, llm, machine-learning, nextjs, open-source, openai, prompt-engineering, prompts, prompts-chat, typescript |
| 许可证 | Other |


### datawhalechina/hello-agents

**描述**: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,446 |
| 语言 | Python |
| Forks | 9,744 |
| Issues | 201 |
| Topics | agent, llm, rag, tutorial |
| 许可证 | Other |


### headroomlabs-ai/headroom

**描述**: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,587 |
| 语言 | Python |
| Forks | 5,482 |
| Issues | 643 |
| Topics | agent, ai, anthropic, claude-code, compression, context-engineering, context-window, cursor, fastapi, langchain, llm, mcp, openai, prompt-engineering, proxy, python, rag, token-optimization, tokens, typescript |
| 许可证 | Apache License 2.0 |


### shareAI-lab/learn-claude-code

**描述**: Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 76,567 |
| 语言 | Python |
| Forks | 12,322 |
| Issues | 44 |
| Topics | agent, agent-development, ai-agent, claude, claude-code, educational, llm, python, teaching, tutorial |
| 许可证 | MIT License |


### byoungd/up

**描述**: An advanced guide which might benefit you a lot 🎉 . 韩先凯的人生进阶指南 人生进阶指南 离谱的人生 人生进阶 AI学习 AI指南 韩先凯的AI学习指南 英语学习指南/英语学习教程/英语学习/学英语

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 62,649 |
| 语言 | JavaScript |
| Forks | 6,344 |
| Issues | 32 |
| Topics | chinese, english-learning, tutorial |
| 许可证 | Other |


### practical-tutorials/project-based-learning

**描述**: Curated list of project-based tutorials

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 282,992 |
| 语言 | Python |
| Forks | 36,222 |
| Issues | 254 |
| Topics | beginner-project, cpp, golang, javascript, project, python, tutorial, webdevelopment |
| 许可证 | MIT License |


### storybookjs/storybook

**描述**: Storybook is the industry standard workshop for building, documenting, and testing UI components in isolation

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 91,041 |
| 语言 | TypeScript |
| Forks | 10,441 |
| Issues | 1,818 |
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
| Stars | 90,209 |
| 语言 | TypeScript |
| Forks | 9,249 |
| Issues | 1,784 |
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
| Stars | 129,045 |
| 语言 | JavaScript |
| Forks | 12,478 |
| Issues | 6 |
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
| Stars | 183,840 |
| 语言 | Go |
| Forks | 13,555 |
| Issues | 233 |
| Topics | awesome, awesome-list, go, golang, golang-library, hacktoberfest |
| 许可证 | MIT License |


### ⭐ 中优先级


### vinta/awesome-python

**描述**: The definitive list that answers "I want to do X in Python, which tool should I use?"

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 320,049 |
| 语言 | Python |
| Forks | 28,716 |
| Issues | 22 |
| Topics | awesome, awesome-list, python, python-frameworks, python-libraries, python-tools |
| 许可证 | Other |


## 📁 其他 (54 个项目) { #其他 }


### 🌟 高优先级


### earendil-works/pi

**描述**: AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 94/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 104,143 |
| 语言 | TypeScript |
| Forks | 13,041 |
| Issues | 206 |
| 许可证 | MIT License |


### harry0703/MoneyPrinterTurbo

**描述**: 利用 AI 大模型和自动化工作流，根据主题或关键词一键生成高清短视频。Generate HD short videos from a topic or keyword with an automated AI workflow.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 122,487 |
| 语言 | Python |
| Forks | 18,927 |
| Issues | 26 |
| Topics | ai-video-generator, content-creation, ffmpeg, instagram-reels, llm, python, short-video, subtitles, text-to-speech, tiktok, video-automation, video-workflow, workflow-automation, youtube-shorts |
| 许可证 | MIT License |


### obra/superpowers

**描述**: An agentic skills framework & software development methodology that works.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 285,329 |
| 语言 | Shell |
| Forks | 25,515 |
| Issues | 356 |
| Topics | ai, brainstorming, coding, obra, sdlc, skills, subagent-driven-development, superpowers |
| 许可证 | MIT License |


### zylon-ai/private-gpt

**描述**: Complete API layer for private AI applications on local models: RAG, skills, tools, MCP, text-to-sql, and more. Works with any OpenAI-compatible inference server.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 93/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 57,503 |
| 语言 | Python |
| Forks | 7,617 |
| Issues | 7 |
| Topics | ai, ai-tools, on-premise |
| 许可证 | Apache License 2.0 |


### nexu-io/open-design

**描述**: 🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode & 20+ CLIs via BYOK.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 95,605 |
| 语言 | TypeScript |
| Forks | 11,081 |
| Issues | 1,016 |
| Topics | agent-skills, ai-design, byok, claude-code-for-design, claude-design, codex-design, coding-agents, cursor-design, deepseek, deepseek-harness, design-systems, desktop-app, dsh, dsh-plugin, figma-alternative, hermes-agent, local-first, prototyping, ui-generator, vibe-coding |
| 许可证 | Apache License 2.0 |


### addyosmani/agent-skills

**描述**: Production-grade engineering skills for AI coding agents.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,560 |
| 语言 | JavaScript |
| Forks | 9,951 |
| Issues | 135 |
| Topics | agent-skills, antigravity, claude-code, codex, cursor, skills |
| 许可证 | MIT License |


### multica-ai/multica

**描述**: Make humans and AI agents work as one team — open-source and self-hostable.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,606 |
| 语言 | Go |
| Forks | 6,405 |
| Issues | 1,552 |
| 许可证 | Other |


### msitarzewski/agency-agents

**描述**: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 151,717 |
| 语言 | Shell |
| Forks | 24,430 |
| Issues | 144 |
| 许可证 | MIT License |


### github/spec-kit

**描述**: 💫 Toolkit to help you get started with Spec-Driven Development

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 135,730 |
| 语言 | Python |
| Forks | 12,199 |
| Issues | 307 |
| Topics | ai, copilot, development, engineering, prd, spec, spec-driven |
| 许可证 | MIT License |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,616 |
| 语言 | Python |
| Forks | 14,099 |
| Issues | 43 |
| Topics | ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam, faceswap, fake-webcam, gan, real-time-deepfake, realtime, realtime-deepfake, realtime-face-changer, video-deepfake, webcam, webcamera |
| 许可证 | GNU Affero General Public License v3.0 |


### EbookFoundation/free-programming-books

**描述**: :books: Freely available programming books

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 396,544 |
| 语言 | Python |
| Forks | 66,758 |
| Issues | 86 |
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
| Stars | 138,359 |
| 语言 | TypeScript |
| Forks | 8,040 |
| Issues | 173 |
| Topics | iptv, m3u, playlist, streams, tv |
| 许可证 | The Unlicense |


### garrytan/gstack

**描述**: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 132,612 |
| 语言 | TypeScript |
| Forks | 19,820 |
| Issues | 881 |
| 许可证 | MIT License |


### pbakaus/impeccable

**描述**: The design language that makes your AI harness better at design.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,324 |
| 语言 | JavaScript |
| Forks | 4,124 |
| Issues | 24 |
| 许可证 | Apache License 2.0 |


### hashicorp/terraform

**描述**: Terraform enables you to safely and predictably create, change, and improve infrastructure. It is a source-available tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 88/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,639 |
| 语言 | Go |
| Forks | 10,612 |
| Issues | 1,919 |
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
| Stars | 127,881 |
| 语言 | C++ |
| Forks | 23,034 |
| Issues | 2,484 |
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
| Stars | 62,298 |
| 语言 | Python |
| Forks | 1,684 |
| Issues | 36 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### TheAlgorithms/Python

**描述**: All Algorithms implemented in Python

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 224,488 |
| 语言 | Python |
| Forks | 51,053 |
| Issues | 556 |
| Topics | algorithm, algorithm-competitions, algorithms-implemented, algos, community-driven, education, hacktoberfest, interview, learn, practice, python, searches, sorting-algorithms, sorts |
| 许可证 | MIT License |


### 3b1b/manim

**描述**: Animation engine for explanatory math videos

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,757 |
| 语言 | Python |
| Forks | 7,699 |
| Issues | 499 |
| Topics | 3b1b-videos, animation, explanatory-math-videos, python |
| 许可证 | MIT License |


### freeCodeCamp/freeCodeCamp

**描述**: freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 455,322 |
| 语言 | TypeScript |
| Forks | 46,164 |
| Issues | 227 |
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
| Stars | 366,920 |
| 语言 | TypeScript |
| Forks | 44,925 |
| Issues | 3 |
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
| Stars | 131,622 |
| 语言 | TypeScript |
| Forks | 15,217 |
| Issues | 3,453 |
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
| Stars | 123,588 |
| 语言 | TypeScript |
| Forks | 10,147 |
| Issues | 1,978 |
| Topics | base-ui, components, laravel, nextjs, radix-ui, react, react-aria, react-aria-components, shadcn, tailwindcss, tanstack, ui, vite |
| 许可证 | MIT License |


### immich-app/immich

**描述**: High performance self-hosted photo and video management solution.

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 113,857 |
| 语言 | TypeScript |
| Forks | 6,881 |
| Issues | 738 |
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
| Stars | 99,480 |
| 语言 | TypeScript |
| Forks | 54,701 |
| Issues | 1,075 |
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
| Stars | 97,503 |
| 语言 | TypeScript |
| Forks | 5,609 |
| Issues | 68 |
| Topics | css, css-framework, functional-css, postcss, responsive, tailwindcss, utility-classes |
| 许可证 | MIT License |


### react/react

**描述**: The library for web and native user interfaces.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 250,047 |
| 语言 | JavaScript |
| Forks | 51,329 |
| Issues | 1,367 |
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
| Stars | 121,591 |
| 语言 | JavaScript |
| Forks | 36,719 |
| Issues | 1,214 |
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
| Stars | 115,419 |
| 语言 | JavaScript |
| Forks | 36,547 |
| Issues | 380 |
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
| Stars | 109,221 |
| 语言 | JavaScript |
| Forks | 11,848 |
| Issues | 92 |
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
| Stars | 99,025 |
| 语言 | JavaScript |
| Forks | 32,539 |
| Issues | 1,463 |
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
| Stars | 88,098 |
| 语言 | JavaScript |
| Forks | 5,237 |
| Issues | 1,066 |
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
| Stars | 72,287 |
| 语言 | JavaScript |
| Forks | 17,031 |
| Issues | 915 |
| Topics | presentations, slides, slideshow |
| 许可证 | MIT License |


### gorhill/uBlock

**描述**: uBlock Origin - An efficient blocker for Chromium and Firefox. Fast and lean.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,758 |
| 语言 | JavaScript |
| Forks | 4,344 |
| Issues | 15 |
| Topics | blocker, browser-extension, chromium, firefox, javascript, ublock, ublock-origin |
| 许可证 | GNU General Public License v3.0 |


### chartjs/Chart.js

**描述**: Simple HTML5 Charts using the <canvas> tag

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 67,691 |
| 语言 | JavaScript |
| Forks | 11,933 |
| Issues | 582 |
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
| Stars | 66,526 |
| 语言 | JavaScript |
| Forks | 9,134 |
| Issues | 6 |
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
| Stars | 65,949 |
| 语言 | JavaScript |
| Forks | 9,543 |
| Issues | 137 |
| Topics | amd, build-tool, commonjs, compiler, es2015, es6, esm, javascript, javascript-compiler, javascript-modules, loaders, module-bundler, plugins, web, web-performance, webpack |
| 许可证 | MIT License |


### jgraph/drawio-desktop

**描述**: Official electron build of draw.io

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,049 |
| 语言 | JavaScript |
| Forks | 5,762 |
| Issues | 3 |
| Topics | diagram-editor, electron-app, graphics, javascript-applications |
| 许可证 | Apache License 2.0 |


### lodash/lodash

**描述**: A modern JavaScript utility library delivering modularity, performance, & extras.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,280 |
| 语言 | JavaScript |
| Forks | 7,188 |
| Issues | 105 |
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
| Stars | 59,780 |
| 语言 | JavaScript |
| Forks | 20,384 |
| Issues | 100 |
| Topics | jquery |
| 许可证 | MIT License |


### golang/go

**描述**: The Go programming language

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 138,423 |
| 语言 | Go |
| Forks | 19,357 |
| Issues | 10,121 |
| Topics | go, golang, language, programming-language |
| 许可证 | BSD 3-Clause "New" or "Revised" License |


### microsoft/TypeScript

**描述**: TypeScript is a superset of JavaScript that compiles to clean JavaScript output.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 111,001 |
| 语言 | Go |
| Forks | 13,814 |
| Issues | 5,057 |
| Topics | javascript, language, typechecker, typescript |
| 许可证 | Apache License 2.0 |


### fatedier/frp

**描述**: A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 109,349 |
| 语言 | Go |
| Forks | 15,206 |
| Issues | 54 |
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
| Stars | 89,791 |
| 语言 | Go |
| Forks | 8,371 |
| Issues | 230 |
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
| Stars | 88,474 |
| 语言 | Go |
| Forks | 5,465 |
| Issues | 382 |
| Topics | go, p2p, peer-to-peer, synchronization |
| 许可证 | Mozilla Public License 2.0 |


### rclone/rclone

**描述**: "rsync for cloud storage" - Google Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic, Wasabi, Google Cloud Storage, Azure Blob, Azure Files, Yandex Files

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 59,709 |
| 语言 | Go |
| Forks | 5,383 |
| Issues | 1,256 |
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
| Stars | 51,339 |
| 语言 | Go |
| Forks | 22,138 |
| Issues | 435 |
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
| Stars | 50,160 |
| 语言 | Go |
| Forks | 7,938 |
| Issues | 568 |
| Topics | file-server, gin, golang, onedrive, solidjs, webdav |
| 许可证 | GNU Affero General Public License v3.0 |


### ⭐ 中优先级


### openai/whisper

**描述**: Robust Speech Recognition via Large-Scale Weak Supervision

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 108,909 |
| 语言 | Python |
| Forks | 13,195 |
| Issues | 148 |
| 许可证 | MIT License |


### modelcontextprotocol/servers

**描述**: Model Context Protocol Servers

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 90,252 |
| 语言 | TypeScript |
| Forks | 11,622 |
| Issues | 513 |
| 许可证 | Other |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 84,206 |
| 语言 | TypeScript |
| Forks | 7,658 |
| Issues | 28 |
| 许可证 | Other |


### anuraghazra/github-readme-stats

**描述**: :zap: Dynamically generated stats for your github readmes

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 79,838 |
| 语言 | JavaScript |
| Forks | 37,656 |
| Issues | 292 |
| Topics | dynamic, profile-readme, readme-generator, readme-stats, serverless |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 72,785 |
| 语言 | JavaScript |
| Forks | 4,921 |
| Issues | 118 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### 521xueweihan/HelloGitHub

**描述**: :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 70/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 176,056 |
| 语言 | Python |
| Forks | 12,766 |
| Issues | 722 |
| Topics | awesome, github, hellogithub, python |
