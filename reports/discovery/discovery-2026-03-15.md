# 项目发现报告 (2026-03-15)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 200 |
| 通过质量评估 | 200 |
| 高优先级 | 134 |
| 去重移除 | 32 |
| 已在监控 | 21 |


### 📋 分类分布

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 27 |
| 🔍 RAG/检索 | 17 |
| 💬 LLM 界面 | 26 |
| 🧠 机器学习框架 | 12 |
| 🛠️ 开发工具 | 18 |
| ⚙️ DevOps/基础设施 | 16 |
| 📈 监控/观测 | 2 |
| 🌐 Web 框架 | 14 |
| 📊 数据/基础设施 | 4 |
| 📚 学习资源 | 8 |
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
| Stars | 127,305 |
| 语言 | Python |
| Forks | 17,992 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前 GitHub 上最受欢迎的开源 AI 聊天界面项目（12.7万+ Stars），它提供了一个功能完善、可自托管的统一前端，能够无缝对接 Ollama、OpenAI 等多种 LLM 后端服务，让用户无需依赖第三方平台即可搭建专属的 AI 助手系统。其开箱即用的特性和活跃的社区支持，使其成为企业和个人部署私有化 AI 服务的首选方案。

**技术亮点**:
- 统一 API 接口层 - 同时支持 Ollama、OpenAI API 等多种 LLM 后端，实现一键切换模型供应商
- RAG（检索增强生成）能力 - 内置文档上传和知识库管理，支持基于私有数据的智能问答
- MCP（Model Context Protocol）支持 - 兼容 Anthropic 的模型上下文协议，便于工具调用和外部系统集成
- 完全自托管架构 - 基于 Python 开发，支持 Docker 一键部署，数据完全本地化，满足隐私合规需求
- 功能丰富的 WebUI - 提供用户权限管理、对话历史、多模型对比、Prompt 模板等企业级功能

**适用场景**:
- 企业内部 AI 知识库 - 结合 RAG 能力，基于公司文档、手册构建智能问答系统，同时确保敏感数据不外泄
- 个人 AI 助手搭建 - 在本地或私有服务器部署，调用 Ollama 本地模型或 OpenAI API，打造专属的 ChatGPT 替代品
- AI 应用开发测试 - 作为 LLM 应用的统一前端，方便开发者在多个模型间进行对比测试和 Prompt 调优



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,048 |
| 语言 | Python |
| Forks | 8,394 |
| Issues | 3,096 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，将检索增强生成与智能 Agent 能力深度融合，为 LLM 提供高质量的上下文层。75K+ Stars 证明了其社区活跃度和实用性，是构建企业级 AI 知识库和智能问答系统的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅支持传统检索增强生成，还具备智能体工作流（Agentic Workflow），可执行复杂的多步推理任务
- 强大的文档理解能力：内置深度文档解析器，支持多种格式文档的结构化理解和知识抽取
- GraphRAG 图谱增强：结合知识图谱技术，提升复杂查询的语义理解和推理能力
- 广泛兼容性：支持 OpenAI、DeepSeek、Ollama 等多种 LLM 后端，以及 MCP 协议，易于集成
- Deep Research 深度研究能力：支持长上下文和多轮检索，适合需要深度分析的场景

**适用场景**:
- 企业知识库构建：快速搭建内部文档问答系统，支持多格式文档解析和精准检索
- AI 客服与智能助手：构建具备知识检索能力的对话机器人，提供准确的产品和服务信息
- 研究与文档分析：学术论文、法律文档、技术文档的深度理解和问答



### firecrawl/firecrawl

**描述**: 🔥 The Web Data API for AI - Turn entire websites into LLM-ready markdown or structured data

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in TypeScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 93,430 |
| 语言 | TypeScript |
| Forks | 6,441 |
| Issues | 210 |
| Topics | ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown, llm, markdown, scraper, scraping, web-crawler, web-data, web-data-extraction, web-scraper, web-scraping, web-search, webscraping |
| 许可证 | GNU Affero General Public License v3.0 |

---

Firecrawl 是目前 GitHub 上最受关注的 AI 数据采集工具（93K+ Stars），专门为 AI 应用设计。它能将任意网站自动转换为 LLM 可直接使用的 markdown 或结构化数据，解决了 AI 应用开发中最头疼的数据准备问题，是构建 RAG 系统、AI Agent 和知识库的必备基础设施。

**技术亮点**:
- 支持将复杂网站自动转换为 LLM-ready 的 Markdown 或结构化数据，无需手动清洗
- 提供 Web Data API，支持爬取、提取、搜索等多种数据获取模式
- 支持 AI Agents 集成，可与主流 LLM 框架无缝对接
- 内置智能爬虫和 AI Scraping 能力，支持动态渲染的 JavaScript 网站
- 提供完整的 HTML-to-Markdown 转换和 Web Data Extraction 功能

**适用场景**:
- 企业级 RAG 知识库构建：快速将内部文档、网站、博客等转化为向量数据库的数据源
- AI Agent 开发：为自主 Agent 提供实时网页数据获取和结构化提取能力
- 竞品监控与市场分析：自动化采集和解析行业网站数据，生成结构化报告



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,050 |
| 语言 | JavaScript |
| Forks | 9,663 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有77k+ stars的超热门项目，专注于AI代码助手的性能优化和增强。它通过技能系统、记忆机制、安全防护和研究驱动的开发模式，为Claude Code、Cursor等主流AI编码工具提供了强大的代理增强框架，显著提升AI编程效率和代码质量。

**技术亮点**:
- 多代理增强架构：整合Skills（技能）、Instincts（直觉）、Memory（记忆）三大核心系统，打造具备学习能力的AI代码助手
- 跨平台兼容性：支持Claude Code、Codex、Opencode、Cursor等多种AI编码工具，提供统一的性能优化方案
- 安全与MCP协议支持：内置安全机制并支持Model Context Protocol，确保AI代理在企业环境中的安全可控运行
- 研究驱动开发模式（Research-first）：强调先分析后行动的开发方法论，提高AI生成代码的准确性和可靠性

**适用场景**:
- 个人开发者：提升日常编程效率，利用AI代理的记忆和技能系统加速代码编写和调试
- 企业研发团队：在Claude Code或Cursor等工具中部署统一的AI增强框架，提高团队整体开发效率和代码质量
- AI应用开发者：学习先进的代理架构设计，构建具备记忆和技能系统的智能编程助手



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,656 |
| 语言 | Go |
| Forks | 3,703 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 推理平台，作为 OpenAI、Claude 等商业服务的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行多种 AI 模型（gguf、transformers、diffusers 等），非常适合注重数据隐私和成本控制的开发者及企业。

**技术亮点**:
- 无 GPU 依赖：在消费级 CPU 硬件上即可高效运行大语言模型和生成式 AI
- 多模态支持：集成文本生成、图像生成、音频/视频生成、语音克隆、TTS 等全栈 AI 能力
- 分布式与去中心化：基于 libp2p 和 P2P 技术实现分布式推理和去中心化部署
- OpenAI API 兼容：提供 drop-in 替换接口，可无缝对接现有 OpenAI 生态应用
- 多模型格式支持：兼容 gguf、transformers、diffusers、llama、mamba 等主流模型架构

**适用场景**:
- 企业私有化 AI 部署：满足数据不出域、合规性要求高的企业场景，如金融、医疗等行业
- 个人开发者 AI 应用开发：低成本构建本地 AI 应用，无需支付 API 费用，适合学习实验和原型开发
- 边缘计算和离线场景：在网络受限或无网络环境下使用 AI 能力，支持 IoT 设备和本地服务集成



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,694 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 650 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个 73K+ Star 的多智能体协作平台，通过创新的 Agent Harness 技术将 AI 智能体作为工作交互的核心单元，支持团队级智能体设计、多智能体协作和知识库管理，是当前最成熟的 AI Agent 应用框架之一。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的智能体团队工作流
- 集成主流大模型（ChatGPT、Claude、DeepSeek、Gemini、GPT），具备强大的模型兼容性
- 支持 MCP 协议和知识库管理，实现智能体的上下文记忆和知识沉淀
- 采用 TypeScript 技术栈，提供类型安全和良好的开发者体验
- 创新性的 Agent Harness 架构，将智能体作为工作交互的基本单元

**适用场景**:
- 企业级 AI 助手团队构建：企业可搭建多角色智能体协作系统，如客服+技术支持+销售智能体协同工作
- 个人知识管理与 AI 工作流：个人用户可构建专属 AI 助手，结合知识库实现智能笔记、代码辅助等场景
- AI 应用快速原型开发：开发者可基于框架快速搭建多智能体应用，适用于智能客服、项目协作、自动化工作流等场景



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,667 |
| 语言 | MDX |
| Forks | 7,659 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是GitHub上最受欢迎的提示工程综合指南，涵盖从基础提示技巧到前沿AI智能体和RAG技术的完整知识体系。项目整合了教程、论文、Jupyter笔记本等多种资源，是开发者快速掌握大语言模型应用开发技能的权威学习资料库。

**技术亮点**:
- 系统化覆盖提示工程、上下文工程、RAG和AI Agents四大核心技术领域
- 提供可交互的MDX文档和Jupyter笔记本，理论结合实践便于动手学习
- 跟踪最新学术研究论文，保持技术内容的前沿性和时效性
- 涵盖OpenAI、ChatGPT等主流LLM平台的实用技巧和最佳实践
- 开源MIT许可证，支持社区协作和内容持续迭代更新

**适用场景**:
- 企业AI团队学习提示工程技术，提升LLM应用开发质量和效率
- 个人开发者系统掌握AI Agent和RAG技术，快速上手大模型应用开发
- 研究人员和学者获取提示工程领域最新论文和研究资源



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,459 |
| 语言 | Python |
| Forks | 8,350 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个ACL 2024收录的统一大模型微调框架，支持100多种主流LLM和VLM模型，提供了从LoRA、QLoRA到RLHF的全栈微调方案，是目前GitHub上最受欢迎的LLM微调工具之一（68K+ Stars），大大降低了企业级大模型定制化的技术门槛。

**技术亮点**:
- 支持100+主流大模型统一微调：包括Llama3、Qwen、DeepSeek、Gemma、Mistral等主流开源模型，实现一套代码适配多模型
- 全栈微调技术支持：集成LoRA、QLoRA、Full、Freeze等多种PEFT微调方法，以及RLHF强化学习对齐技术
- 高效量化与训练优化：支持4/8-bit量化训练、MOE混合专家模型微调，显著降低显存需求和训练成本
- VLM多模态支持：不仅支持纯文本LLM，还支持视觉语言模型(VLM)的统一微调流程
- 开箱即用的WebUI界面：提供无需代码的Web操作界面，支持模型训练、评估、导出的全流程可视化管理

**适用场景**:
- 企业私有化模型定制：企业可基于开源模型（如Qwen、DeepSeek）使用内部数据进行领域适配，打造行业专属AI助手
- 学术研究与模型实验：研究人员可快速对比不同微调方法（LoRA vs Full vs RLHF）在各类NLP任务上的效果
- 个人开发者学习与实践：通过WebUI零门槛体验大模型微调全流程，适合AI爱好者和初学者入门学习



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,401 |
| 语言 | Java |
| Forks | 15,839 |
| Issues | 55 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个45k+ stars的成熟开源项目，将低代码开发与AI能力深度结合，独创"低代码+零代码"双模驱动模式。它不仅提供强大的代码生成器实现前后端一键生成，还集成了完整的AI应用开发生态（包括AI助手、知识库、RAG、流程编排、MCP等），让开发者既能快速构建业务系统，又能轻松开发AI应用，显著提升开发效率的同时保持架构灵活性。

**技术亮点**:
- 采用主流技术栈：基于 SpringBoot3 + Vue3 + Ant Design Vue，集成 MyBatis-Plus、Flowable/Activiti 工作流引擎，架构现代化且生态完善
- 强大的一键代码生成器：支持前后端代码自动生成，无需手写代码即可完成CRUD功能开发，显著降低开发成本
- 完整的AI能力集成：深度整合 LangChain4j、Spring AI、DeepSeek 等AI框架，支持AI聊天助手、知识库(RAG)、AI流程编排(AIFlow)、MCP协议和插件扩展
- 双模开发模式：低代码模式满足快速交付需求，零代码模式支持业务人员自主配置，灵活适应不同场景
- 微服务架构支持：基于 SpringCloud 实现分布式架构，支持企业级大规模应用部署

**适用场景**:
- 企业内部管理系统快速开发：如OA办公、ERP、CRM等业务系统，利用代码生成器快速搭建基础功能，节省80%以上开发工作量
- AI应用开发平台：构建企业级AI助手、智能客服、知识问答系统，利用现成的RAG、Agent、流程编排能力快速落地AI场景
- 中小型软件公司/团队的项目交付：作为项目脚手架快速启动新项目，复用已集成的用户权限、工作流、AI等通用能力，专注于业务逻辑开发



### zhayujie/chatgpt-on-wechat

**描述**: CowAgent是基于大模型的超级AI助理，能主动思考和任务规划、访问操作系统和外部资源、创造和执行Skills、拥有长期记忆并不断成长。同时支持飞书、钉钉、企业微信应用、微信公众号、网页等接入，可选择OpenAI/Claude/Gemini/DeepSeek/ Qwen/GLM/Kimi/LinkAI，能处理文本、语音、图片和文件，可快速搭建个人AI助手和企业数字员工。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 42,217 |
| 语言 | Python |
| Forks | 9,823 |
| Issues | 354 |
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
| Stars | 35,393 |
| 语言 | TypeScript |
| Forks | 2,518 |
| Issues | 111 |
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
| Stars | 34,661 |
| 语言 | TypeScript |
| Forks | 7,009 |
| Issues | 457 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### mindsdb/mindsdb

**描述**: Query Engine for AI Analytics: Build self-reasoning agents across all your live data

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 38,754 |
| 语言 | Python |
| Forks | 6,142 |
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
| Stars | 33,006 |
| 语言 | TypeScript |
| Forks | 3,553 |
| Issues | 277 |
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
| Stars | 32,089 |
| 语言 | Jupyter Notebook |
| Forks | 5,268 |
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
| Stars | 102,213 |
| 语言 | Python |
| Forks | 14,886 |
| Issues | 7 |
| Topics | agents, llms, python, rag |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,268 |
| 语言 | JavaScript |
| Forks | 6,081 |
| Issues | 305 |
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
| Stars | 69,158 |
| 语言 | Python |
| Forks | 8,665 |
| Issues | 344 |
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
| Stars | 40,191 |
| 语言 | TypeScript |
| Forks | 3,032 |
| Issues | 375 |
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
| Stars | 80,850 |
| 语言 | Python |
| Forks | 9,557 |
| Issues | 242 |
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
| Stars | 50,770 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 814 |
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
| Stars | 179,274 |
| 语言 | TypeScript |
| Forks | 55,806 |
| Issues | 1,436 |
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
| Stars | 145,691 |
| 语言 | Python |
| Forks | 8,588 |
| Issues | 893 |
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
| Stars | 54,055 |
| 语言 | Jupyter Notebook |
| Forks | 18,753 |
| Issues | 5 |
| Topics | agentic-ai, agentic-framework, agentic-rag, ai-agents, ai-agents-framework, autogen, generative-ai, semantic-kernel |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,406 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,299 |
| 语言 | Python |
| Forks | 3,436 |
| Issues | 6 |
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
| Stars | 44,338 |
| 语言 | Python |
| Forks | 4,473 |
| Issues | 308 |
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
| Stars | 127,305 |
| 语言 | Python |
| Forks | 17,992 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前 GitHub 上最受欢迎的开源 AI 聊天界面项目（12.7万+ Stars），它提供了一个功能完善、可自托管的统一前端，能够无缝对接 Ollama、OpenAI 等多种 LLM 后端服务，让用户无需依赖第三方平台即可搭建专属的 AI 助手系统。其开箱即用的特性和活跃的社区支持，使其成为企业和个人部署私有化 AI 服务的首选方案。

**技术亮点**:
- 统一 API 接口层 - 同时支持 Ollama、OpenAI API 等多种 LLM 后端，实现一键切换模型供应商
- RAG（检索增强生成）能力 - 内置文档上传和知识库管理，支持基于私有数据的智能问答
- MCP（Model Context Protocol）支持 - 兼容 Anthropic 的模型上下文协议，便于工具调用和外部系统集成
- 完全自托管架构 - 基于 Python 开发，支持 Docker 一键部署，数据完全本地化，满足隐私合规需求
- 功能丰富的 WebUI - 提供用户权限管理、对话历史、多模型对比、Prompt 模板等企业级功能

**适用场景**:
- 企业内部 AI 知识库 - 结合 RAG 能力，基于公司文档、手册构建智能问答系统，同时确保敏感数据不外泄
- 个人 AI 助手搭建 - 在本地或私有服务器部署，调用 Ollama 本地模型或 OpenAI API，打造专属的 ChatGPT 替代品
- AI 应用开发测试 - 作为 LLM 应用的统一前端，方便开发者在多个模型间进行对比测试和 Prompt 调优



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,048 |
| 语言 | Python |
| Forks | 8,394 |
| Issues | 3,096 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，将检索增强生成与智能 Agent 能力深度融合，为 LLM 提供高质量的上下文层。75K+ Stars 证明了其社区活跃度和实用性，是构建企业级 AI 知识库和智能问答系统的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅支持传统检索增强生成，还具备智能体工作流（Agentic Workflow），可执行复杂的多步推理任务
- 强大的文档理解能力：内置深度文档解析器，支持多种格式文档的结构化理解和知识抽取
- GraphRAG 图谱增强：结合知识图谱技术，提升复杂查询的语义理解和推理能力
- 广泛兼容性：支持 OpenAI、DeepSeek、Ollama 等多种 LLM 后端，以及 MCP 协议，易于集成
- Deep Research 深度研究能力：支持长上下文和多轮检索，适合需要深度分析的场景

**适用场景**:
- 企业知识库构建：快速搭建内部文档问答系统，支持多格式文档解析和精准检索
- AI 客服与智能助手：构建具备知识检索能力的对话机器人，提供准确的产品和服务信息
- 研究与文档分析：学术论文、法律文档、技术文档的深度理解和问答



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,694 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 650 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个 73K+ Star 的多智能体协作平台，通过创新的 Agent Harness 技术将 AI 智能体作为工作交互的核心单元，支持团队级智能体设计、多智能体协作和知识库管理，是当前最成熟的 AI Agent 应用框架之一。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的智能体团队工作流
- 集成主流大模型（ChatGPT、Claude、DeepSeek、Gemini、GPT），具备强大的模型兼容性
- 支持 MCP 协议和知识库管理，实现智能体的上下文记忆和知识沉淀
- 采用 TypeScript 技术栈，提供类型安全和良好的开发者体验
- 创新性的 Agent Harness 架构，将智能体作为工作交互的基本单元

**适用场景**:
- 企业级 AI 助手团队构建：企业可搭建多角色智能体协作系统，如客服+技术支持+销售智能体协同工作
- 个人知识管理与 AI 工作流：个人用户可构建专属 AI 助手，结合知识库实现智能笔记、代码辅助等场景
- AI 应用快速原型开发：开发者可基于框架快速搭建多智能体应用，适用于智能客服、项目协作、自动化工作流等场景



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,667 |
| 语言 | MDX |
| Forks | 7,659 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是GitHub上最受欢迎的提示工程综合指南，涵盖从基础提示技巧到前沿AI智能体和RAG技术的完整知识体系。项目整合了教程、论文、Jupyter笔记本等多种资源，是开发者快速掌握大语言模型应用开发技能的权威学习资料库。

**技术亮点**:
- 系统化覆盖提示工程、上下文工程、RAG和AI Agents四大核心技术领域
- 提供可交互的MDX文档和Jupyter笔记本，理论结合实践便于动手学习
- 跟踪最新学术研究论文，保持技术内容的前沿性和时效性
- 涵盖OpenAI、ChatGPT等主流LLM平台的实用技巧和最佳实践
- 开源MIT许可证，支持社区协作和内容持续迭代更新

**适用场景**:
- 企业AI团队学习提示工程技术，提升LLM应用开发质量和效率
- 个人开发者系统掌握AI Agent和RAG技术，快速上手大模型应用开发
- 研究人员和学者获取提示工程领域最新论文和研究资源



### jeecgboot/JeecgBoot

**描述**: 【AI低代码平台】“低代码+零代码”双模驱动AI智能平台  AI low-code platform empowers enterprises to quickly develop low-code solutions and build AI applications.  助力企业快速实现低代码开发和构建AI应用！ AI应用平台涵盖：AI应用、AI模型、AI聊天助手、知识库、AI流程编排、MCP和插件，聊天式业务操作等。 强大代码生成器：实现前后端一键生成，无需手写代码! 显著提升效率节省成本，又不失灵活~

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 45,401 |
| 语言 | Java |
| Forks | 15,839 |
| Issues | 55 |
| Topics | activiti, agent, ai, aiflow, ant-design-vue, antd, codegenerator, deepseek, flowable, langchain4j, llm, low-code, mcp, mybatis-plus, rag, spring-ai, springboot, springboot3, springcloud, vue3 |
| 许可证 | Apache License 2.0 |

---

JeecgBoot 是一个45k+ stars的成熟开源项目，将低代码开发与AI能力深度结合，独创"低代码+零代码"双模驱动模式。它不仅提供强大的代码生成器实现前后端一键生成，还集成了完整的AI应用开发生态（包括AI助手、知识库、RAG、流程编排、MCP等），让开发者既能快速构建业务系统，又能轻松开发AI应用，显著提升开发效率的同时保持架构灵活性。

**技术亮点**:
- 采用主流技术栈：基于 SpringBoot3 + Vue3 + Ant Design Vue，集成 MyBatis-Plus、Flowable/Activiti 工作流引擎，架构现代化且生态完善
- 强大的一键代码生成器：支持前后端代码自动生成，无需手写代码即可完成CRUD功能开发，显著降低开发成本
- 完整的AI能力集成：深度整合 LangChain4j、Spring AI、DeepSeek 等AI框架，支持AI聊天助手、知识库(RAG)、AI流程编排(AIFlow)、MCP协议和插件扩展
- 双模开发模式：低代码模式满足快速交付需求，零代码模式支持业务人员自主配置，灵活适应不同场景
- 微服务架构支持：基于 SpringCloud 实现分布式架构，支持企业级大规模应用部署

**适用场景**:
- 企业内部管理系统快速开发：如OA办公、ERP、CRM等业务系统，利用代码生成器快速搭建基础功能，节省80%以上开发工作量
- AI应用开发平台：构建企业级AI助手、智能客服、知识问答系统，利用现成的RAG、Agent、流程编排能力快速落地AI场景
- 中小型软件公司/团队的项目交付：作为项目脚手架快速启动新项目，复用已集成的用户权限、工作流、AI等通用能力，专注于业务逻辑开发



### thedotmack/claude-mem

**描述**: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 35,393 |
| 语言 | TypeScript |
| Forks | 2,518 |
| Issues | 111 |
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
| Stars | 38,754 |
| 语言 | Python |
| Forks | 6,142 |
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
| Stars | 33,006 |
| 语言 | TypeScript |
| Forks | 3,553 |
| Issues | 277 |
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
| Stars | 32,089 |
| 语言 | Jupyter Notebook |
| Forks | 5,268 |
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
| Stars | 102,213 |
| 语言 | Python |
| Forks | 14,886 |
| Issues | 7 |
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
| Stars | 99,021 |
| 语言 | TypeScript |
| Forks | 11,802 |
| Issues | 941 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,268 |
| 语言 | JavaScript |
| Forks | 6,081 |
| Issues | 305 |
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
| Stars | 50,770 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 814 |
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
| Stars | 72,339 |
| 语言 | Python |
| Forks | 9,965 |
| Issues | 244 |
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
| Stars | 43,319 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,034 |
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
| Stars | 31,486 |
| 语言 | Python |
| Forks | 3,322 |
| Issues | 78 |
| Topics | gpt, gpt-4, gpt4, graphrag, llm, llms, rag |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,406 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


## 💬 LLM 界面 (26 个项目) { #llm-界面 }


### 🌟 高优先级


### open-webui/open-webui

**描述**: User-friendly AI Interface (Supports Ollama, OpenAI API, ...)

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 127,305 |
| 语言 | Python |
| Forks | 17,992 |
| Issues | 308 |
| Topics | ai, llm, llm-ui, llm-webui, llms, mcp, ollama, ollama-webui, open-webui, openai, openapi, rag, self-hosted, ui, webui |
| 许可证 | Other |

---

Open WebUI 是目前 GitHub 上最受欢迎的开源 AI 聊天界面项目（12.7万+ Stars），它提供了一个功能完善、可自托管的统一前端，能够无缝对接 Ollama、OpenAI 等多种 LLM 后端服务，让用户无需依赖第三方平台即可搭建专属的 AI 助手系统。其开箱即用的特性和活跃的社区支持，使其成为企业和个人部署私有化 AI 服务的首选方案。

**技术亮点**:
- 统一 API 接口层 - 同时支持 Ollama、OpenAI API 等多种 LLM 后端，实现一键切换模型供应商
- RAG（检索增强生成）能力 - 内置文档上传和知识库管理，支持基于私有数据的智能问答
- MCP（Model Context Protocol）支持 - 兼容 Anthropic 的模型上下文协议，便于工具调用和外部系统集成
- 完全自托管架构 - 基于 Python 开发，支持 Docker 一键部署，数据完全本地化，满足隐私合规需求
- 功能丰富的 WebUI - 提供用户权限管理、对话历史、多模型对比、Prompt 模板等企业级功能

**适用场景**:
- 企业内部 AI 知识库 - 结合 RAG 能力，基于公司文档、手册构建智能问答系统，同时确保敏感数据不外泄
- 个人 AI 助手搭建 - 在本地或私有服务器部署，调用 Ollama 本地模型或 OpenAI API，打造专属的 ChatGPT 替代品
- AI 应用开发测试 - 作为 LLM 应用的统一前端，方便开发者在多个模型间进行对比测试和 Prompt 调优



### infiniflow/ragflow

**描述**: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Python

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 75,048 |
| 语言 | Python |
| Forks | 8,394 |
| Issues | 3,096 |
| Topics | agent, agentic, agentic-ai, agentic-workflow, ai, ai-search, context-engineering, context-retrieval, deep-research, deepseek, deepseek-r1, document-parser, document-understanding, graphrag, llm, mcp, ollama, openai, rag, retrieval-augmented-generation |
| 许可证 | Apache License 2.0 |

---

RAGFlow 是目前最成熟的开源 RAG 引擎之一，将检索增强生成与智能 Agent 能力深度融合，为 LLM 提供高质量的上下文层。75K+ Stars 证明了其社区活跃度和实用性，是构建企业级 AI 知识库和智能问答系统的首选方案。

**技术亮点**:
- 融合 RAG 与 Agent 能力：不仅支持传统检索增强生成，还具备智能体工作流（Agentic Workflow），可执行复杂的多步推理任务
- 强大的文档理解能力：内置深度文档解析器，支持多种格式文档的结构化理解和知识抽取
- GraphRAG 图谱增强：结合知识图谱技术，提升复杂查询的语义理解和推理能力
- 广泛兼容性：支持 OpenAI、DeepSeek、Ollama 等多种 LLM 后端，以及 MCP 协议，易于集成
- Deep Research 深度研究能力：支持长上下文和多轮检索，适合需要深度分析的场景

**适用场景**:
- 企业知识库构建：快速搭建内部文档问答系统，支持多格式文档解析和精准检索
- AI 客服与智能助手：构建具备知识检索能力的对话机器人，提供准确的产品和服务信息
- 研究与文档分析：学术论文、法律文档、技术文档的深度理解和问答



### affaan-m/everything-claude-code

**描述**: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 77,050 |
| 语言 | JavaScript |
| Forks | 9,663 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有77k+ stars的超热门项目，专注于AI代码助手的性能优化和增强。它通过技能系统、记忆机制、安全防护和研究驱动的开发模式，为Claude Code、Cursor等主流AI编码工具提供了强大的代理增强框架，显著提升AI编程效率和代码质量。

**技术亮点**:
- 多代理增强架构：整合Skills（技能）、Instincts（直觉）、Memory（记忆）三大核心系统，打造具备学习能力的AI代码助手
- 跨平台兼容性：支持Claude Code、Codex、Opencode、Cursor等多种AI编码工具，提供统一的性能优化方案
- 安全与MCP协议支持：内置安全机制并支持Model Context Protocol，确保AI代理在企业环境中的安全可控运行
- 研究驱动开发模式（Research-first）：强调先分析后行动的开发方法论，提高AI生成代码的准确性和可靠性

**适用场景**:
- 个人开发者：提升日常编程效率，利用AI代理的记忆和技能系统加速代码编写和调试
- 企业研发团队：在Claude Code或Cursor等工具中部署统一的AI增强框架，提高团队整体开发效率和代码质量
- AI应用开发者：学习先进的代理架构设计，构建具备记忆和技能系统的智能编程助手



### lobehub/lobehub

**描述**: The ultimate space for work and life — to find, build, and collaborate with agent teammates that grow with you. We are taking agent harness to the next level — enabling multi-agent collaboration, effortless agent team design, and introducing agents as the unit of work interaction.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 73,694 |
| 语言 | TypeScript |
| Forks | 14,792 |
| Issues | 650 |
| Topics | agent, agent-collaboration, agent-harness, ai, chatgpt, claude, deepseek, gemini, gpt, knowledge-base, mcp, openai |
| 许可证 | Other |

---

LobeHub 是一个 73K+ Star 的多智能体协作平台，通过创新的 Agent Harness 技术将 AI 智能体作为工作交互的核心单元，支持团队级智能体设计、多智能体协作和知识库管理，是当前最成熟的 AI Agent 应用框架之一。

**技术亮点**:
- 支持多智能体协作（Multi-Agent Collaboration），可构建复杂的智能体团队工作流
- 集成主流大模型（ChatGPT、Claude、DeepSeek、Gemini、GPT），具备强大的模型兼容性
- 支持 MCP 协议和知识库管理，实现智能体的上下文记忆和知识沉淀
- 采用 TypeScript 技术栈，提供类型安全和良好的开发者体验
- 创新性的 Agent Harness 架构，将智能体作为工作交互的基本单元

**适用场景**:
- 企业级 AI 助手团队构建：企业可搭建多角色智能体协作系统，如客服+技术支持+销售智能体协同工作
- 个人知识管理与 AI 工作流：个人用户可构建专属 AI 助手，结合知识库实现智能笔记、代码辅助等场景
- AI 应用快速原型开发：开发者可基于框架快速搭建多智能体应用，适用于智能客服、项目协作、自动化工作流等场景



### dair-ai/Prompt-Engineering-Guide

**描述**: 🐙 Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 71,667 |
| 语言 | MDX |
| Forks | 7,659 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是GitHub上最受欢迎的提示工程综合指南，涵盖从基础提示技巧到前沿AI智能体和RAG技术的完整知识体系。项目整合了教程、论文、Jupyter笔记本等多种资源，是开发者快速掌握大语言模型应用开发技能的权威学习资料库。

**技术亮点**:
- 系统化覆盖提示工程、上下文工程、RAG和AI Agents四大核心技术领域
- 提供可交互的MDX文档和Jupyter笔记本，理论结合实践便于动手学习
- 跟踪最新学术研究论文，保持技术内容的前沿性和时效性
- 涵盖OpenAI、ChatGPT等主流LLM平台的实用技巧和最佳实践
- 开源MIT许可证，支持社区协作和内容持续迭代更新

**适用场景**:
- 企业AI团队学习提示工程技术，提升LLM应用开发质量和效率
- 个人开发者系统掌握AI Agent和RAG技术，快速上手大模型应用开发
- 研究人员和学者获取提示工程领域最新论文和研究资源



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,666 |
| 语言 | HTML |
| Forks | 20,074 |
| Issues | 31 |
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
| Stars | 88,143 |
| 语言 | Jupyter Notebook |
| Forks | 13,451 |
| Issues | 3 |
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
| Stars | 42,217 |
| 语言 | Python |
| Forks | 9,823 |
| Issues | 354 |
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
| Stars | 35,393 |
| 语言 | TypeScript |
| Forks | 2,518 |
| Issues | 111 |
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
| Stars | 34,661 |
| 语言 | TypeScript |
| Forks | 7,009 |
| Issues | 457 |
| Topics | ai, anthropic, artifacts, aws, azure, chatgpt, chatgpt-clone, claude, clone, deepseek, gemini, google, gpt-5, librechat, mcp, o1, openai, responses-api, vision, webui |
| 许可证 | MIT License |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,268 |
| 语言 | JavaScript |
| Forks | 6,081 |
| Issues | 305 |
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
| Stars | 69,158 |
| 语言 | Python |
| Forks | 8,665 |
| Issues | 344 |
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
| Stars | 40,191 |
| 语言 | TypeScript |
| Forks | 3,032 |
| Issues | 375 |
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
| Stars | 50,770 |
| 语言 | TypeScript |
| Forks | 23,964 |
| Issues | 814 |
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
| Stars | 34,354 |
| 语言 | HTML |
| Forks | 5,521 |
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
| Stars | 73,182 |
| 语言 | Python |
| Forks | 14,378 |
| Issues | 3,702 |
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
| Stars | 41,946 |
| 语言 | Python |
| Forks | 4,064 |
| Issues | 71 |
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
| Stars | 145,691 |
| 语言 | Python |
| Forks | 8,588 |
| Issues | 893 |
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
| Stars | 165,159 |
| 语言 | Go |
| Forks | 14,981 |
| Issues | 2,646 |
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
| Stars | 46,649 |
| 语言 | Rust |
| Forks | 9,125 |
| Issues | 0 |
| Topics | chatgpt, claude, desktop, gemini, hight-performance, linux, macos, no-electron, package, rust, tauri, windows, youtube |
| 许可证 | MIT License |


### khoj-ai/khoj

**描述**: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 90/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 33,406 |
| 语言 | Python |
| Forks | 2,061 |
| Issues | 100 |
| Topics | agent, ai, assistant, chat, chatgpt, emacs, image-generation, llama3, llamacpp, llm, obsidian, obsidian-md, offline-llm, productivity, rag, research, self-hosted, semantic-search, stt, whatsapp-ai |
| 许可证 | GNU Affero General Public License v3.0 |


### wshobson/agents

**描述**: Intelligent automation and multi-agent orchestration for Claude Code

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 86/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 31,299 |
| 语言 | Python |
| Forks | 3,436 |
| Issues | 6 |
| Topics | agents, anthropic, anthropic-claude, automation, claude, claude-code, claude-code-cli, claude-code-commands, claude-code-plugin, claude-code-plugins, claude-code-skills, claude-code-subagents, claude-skills, claudecode, claudecode-config, claudecode-subagents, orchestration, sub-agents, subagents, workflows |
| 许可证 | MIT License |


### microsoft/markitdown

**描述**: Python tool for converting files and office documents to Markdown.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 90,764 |
| 语言 | Python |
| Forks | 5,357 |
| Issues | 471 |
| Topics | autogen, autogen-extension, langchain, markdown, microsoft-office, openai, pdf |
| 许可证 | MIT License |


### chatboxai/chatbox

**描述**: Powerful AI Client

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 38,967 |
| 语言 | TypeScript |
| Forks | 3,941 |
| Issues | 1,074 |
| Topics | assistant, chatbot, chatgpt, claude, copilot, deepseek, gemini, gpt, gpt-5, ollama, openai |
| 许可证 | GNU General Public License v3.0 |


### chatanywhere/GPT_API_free

**描述**: Free ChatGPT&DeepSeek API Key，免费ChatGPT&DeepSeek API。免费接入DeepSeek API和GPT4 API，支持 gpt | deepseek | claude | gemini | grok 等排名靠前的常用大模型。

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 83/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 36,664 |
| 语言 | Python |
| Forks | 2,562 |
| Issues | 62 |
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
| Stars | 44,338 |
| 语言 | Python |
| Forks | 4,473 |
| Issues | 308 |
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
| Stars | 71,667 |
| 语言 | MDX |
| Forks | 7,659 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是GitHub上最受欢迎的提示工程综合指南，涵盖从基础提示技巧到前沿AI智能体和RAG技术的完整知识体系。项目整合了教程、论文、Jupyter笔记本等多种资源，是开发者快速掌握大语言模型应用开发技能的权威学习资料库。

**技术亮点**:
- 系统化覆盖提示工程、上下文工程、RAG和AI Agents四大核心技术领域
- 提供可交互的MDX文档和Jupyter笔记本，理论结合实践便于动手学习
- 跟踪最新学术研究论文，保持技术内容的前沿性和时效性
- 涵盖OpenAI、ChatGPT等主流LLM平台的实用技巧和最佳实践
- 开源MIT许可证，支持社区协作和内容持续迭代更新

**适用场景**:
- 企业AI团队学习提示工程技术，提升LLM应用开发质量和效率
- 个人开发者系统掌握AI Agent和RAG技术，快速上手大模型应用开发
- 研究人员和学者获取提示工程领域最新论文和研究资源



### hiyouga/LlamaFactory

**描述**: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 68,459 |
| 语言 | Python |
| Forks | 8,350 |
| Issues | 930 |
| Topics | agent, ai, deepseek, fine-tuning, gemma, gpt, instruction-tuning, large-language-models, llama, llama3, llm, lora, moe, nlp, peft, qlora, quantization, qwen, rlhf, transformers |
| 许可证 | Apache License 2.0 |

---

LlamaFactory是一个ACL 2024收录的统一大模型微调框架，支持100多种主流LLM和VLM模型，提供了从LoRA、QLoRA到RLHF的全栈微调方案，是目前GitHub上最受欢迎的LLM微调工具之一（68K+ Stars），大大降低了企业级大模型定制化的技术门槛。

**技术亮点**:
- 支持100+主流大模型统一微调：包括Llama3、Qwen、DeepSeek、Gemma、Mistral等主流开源模型，实现一套代码适配多模型
- 全栈微调技术支持：集成LoRA、QLoRA、Full、Freeze等多种PEFT微调方法，以及RLHF强化学习对齐技术
- 高效量化与训练优化：支持4/8-bit量化训练、MOE混合专家模型微调，显著降低显存需求和训练成本
- VLM多模态支持：不仅支持纯文本LLM，还支持视觉语言模型(VLM)的统一微调流程
- 开箱即用的WebUI界面：提供无需代码的Web操作界面，支持模型训练、评估、导出的全流程可视化管理

**适用场景**:
- 企业私有化模型定制：企业可基于开源模型（如Qwen、DeepSeek）使用内部数据进行领域适配，打造行业专属AI助手
- 学术研究与模型实验：研究人员可快速对比不同微调方法（LoRA vs Full vs RLHF）在各类NLP任务上的效果
- 个人开发者学习与实践：通过WebUI零门槛体验大模型微调全流程，适合AI爱好者和初学者入门学习



### OpenBB-finance/OpenBB

**描述**: Financial data platform for analysts, quants and AI agents.

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 63,122 |
| 语言 | Python |
| Forks | 6,197 |
| Issues | 64 |
| Topics | ai, crypto, derivatives, economics, equity, finance, fixed-income, machine-learning, openbb, options, python, quantitative-finance, stocks |
| 许可证 | Other |

---

OpenBB 是目前 GitHub 上最受欢迎的开源金融数据分析平台，拥有超过6.3万星标。它为分析师、量化交易员和AI代理提供统一的金融数据接入层，打破了传统金融数据被商业平台垄断的局面，让个人投资者和中小团队也能免费获取高质量的金融数据分析能力。

**技术亮点**:
- 统一API接口整合多源金融数据（股票、加密货币、期权、固定收益、宏观经济等），支持Python编程
- 专为AI代理优化的数据平台架构，支持机器学习模型训练和量化分析工作流
- 模块化设计，涵盖权益、衍生品、加密货币等多个金融领域的专业数据
- 活跃的开源社区维护，代码质量高且持续迭代更新
- 支持可扩展的数据源插件系统，方便集成自定义数据提供商

**适用场景**:
- 量化交易策略研究和回测：个人量化交易员可利用免费金融数据进行策略开发、历史回测和信号分析
- 金融科技产品开发：初创公司和中小团队可基于OpenBB构建金融分析工具、投资组合管理平台等商业产品
- 学术研究和教育：高校金融工程课程和研究人员可用于金融建模、市场分析和机器学习算法验证



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,666 |
| 语言 | HTML |
| Forks | 20,074 |
| Issues | 31 |
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
| Stars | 88,143 |
| 语言 | Jupyter Notebook |
| Forks | 13,451 |
| Issues | 3 |
| Topics | ai, artificial-intelligence, chatbot, chatgpt, deep-learning, from-scratch, generative-ai, gpt, language-model, large-language-models, llm, machine-learning, neural-networks, python, pytorch, transformers |
| 许可证 | Other |


### ItzCrazyKns/Vane

**描述**: Vane is an AI-powered answering engine.

**发现来源**: keyword

**发现原因**: Keyword: RAG

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 33,006 |
| 语言 | TypeScript |
| Forks | 3,553 |
| Issues | 277 |
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
| Stars | 32,089 |
| 语言 | Jupyter Notebook |
| Forks | 5,268 |
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
| Stars | 157,845 |
| 语言 | Python |
| Forks | 32,487 |
| Issues | 2,307 |
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
| Stars | 73,182 |
| 语言 | Python |
| Forks | 14,378 |
| Issues | 3,702 |
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
| Stars | 105,921 |
| 语言 | Python |
| Forks | 12,171 |
| Issues | 3,833 |
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
| Stars | 98,276 |
| 语言 | Python |
| Forks | 27,210 |
| Issues | 18,065 |
| Topics | autograd, deep-learning, gpu, machine-learning, neural-network, numpy, python, tensor |
| 许可证 | Other |


### AUTOMATIC1111/stable-diffusion-webui

**描述**: Stable Diffusion web UI

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 80/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 161,758 |
| 语言 | Python |
| Forks | 30,176 |
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
| Stars | 77,050 |
| 语言 | JavaScript |
| Forks | 9,663 |
| Issues | 82 |
| Topics | ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity |
| 许可证 | MIT License |

---

这是一个拥有77k+ stars的超热门项目，专注于AI代码助手的性能优化和增强。它通过技能系统、记忆机制、安全防护和研究驱动的开发模式，为Claude Code、Cursor等主流AI编码工具提供了强大的代理增强框架，显著提升AI编程效率和代码质量。

**技术亮点**:
- 多代理增强架构：整合Skills（技能）、Instincts（直觉）、Memory（记忆）三大核心系统，打造具备学习能力的AI代码助手
- 跨平台兼容性：支持Claude Code、Codex、Opencode、Cursor等多种AI编码工具，提供统一的性能优化方案
- 安全与MCP协议支持：内置安全机制并支持Model Context Protocol，确保AI代理在企业环境中的安全可控运行
- 研究驱动开发模式（Research-first）：强调先分析后行动的开发方法论，提高AI生成代码的准确性和可靠性

**适用场景**:
- 个人开发者：提升日常编程效率，利用AI代理的记忆和技能系统加速代码编写和调试
- 企业研发团队：在Claude Code或Cursor等工具中部署统一的AI增强框架，提高团队整体开发效率和代码质量
- AI应用开发者：学习先进的代理架构设计，构建具备记忆和技能系统的智能编程助手



### mudler/LocalAI

**描述**: :robot: The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. Drop-in replacement,  running on consumer-grade hardware. No GPU required. Runs gguf, transformers, diffusers and many more. Features: Generate Text, MCP, Audio, Video, Images, Voice Cloning, Distributed, P2P and decentralized inference

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in Go

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 43,656 |
| 语言 | Go |
| Forks | 3,703 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 推理平台，作为 OpenAI、Claude 等商业服务的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行多种 AI 模型（gguf、transformers、diffusers 等），非常适合注重数据隐私和成本控制的开发者及企业。

**技术亮点**:
- 无 GPU 依赖：在消费级 CPU 硬件上即可高效运行大语言模型和生成式 AI
- 多模态支持：集成文本生成、图像生成、音频/视频生成、语音克隆、TTS 等全栈 AI 能力
- 分布式与去中心化：基于 libp2p 和 P2P 技术实现分布式推理和去中心化部署
- OpenAI API 兼容：提供 drop-in 替换接口，可无缝对接现有 OpenAI 生态应用
- 多模型格式支持：兼容 gguf、transformers、diffusers、llama、mamba 等主流模型架构

**适用场景**:
- 企业私有化 AI 部署：满足数据不出域、合规性要求高的企业场景，如金融、医疗等行业
- 个人开发者 AI 应用开发：低成本构建本地 AI 应用，无需支付 API 费用，适合学习实验和原型开发
- 边缘计算和离线场景：在网络受限或无网络环境下使用 AI 能力，支持 IoT 设备和本地服务集成



### OpenHands/OpenHands

**描述**: 🙌 OpenHands: AI-Driven Development

**发现来源**: keyword

**发现原因**: Keyword: AI agent

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 69,158 |
| 语言 | Python |
| Forks | 8,665 |
| Issues | 344 |
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
| Stars | 40,191 |
| 语言 | TypeScript |
| Forks | 3,032 |
| Issues | 375 |
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
| Stars | 179,274 |
| 语言 | TypeScript |
| Forks | 55,806 |
| Issues | 1,436 |
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
| Stars | 151,343 |
| 语言 | Python |
| Forks | 12,260 |
| Issues | 2,365 |
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
| Stars | 96,222 |
| 语言 | Python |
| Forks | 8,861 |
| Issues | 160 |
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
| Stars | 73,738 |
| 语言 | Python |
| Forks | 8,751 |
| Issues | 200 |
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
| Stars | 182,682 |
| 语言 | TypeScript |
| Forks | 38,516 |
| Issues | 15,255 |
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
| Stars | 93,823 |
| 语言 | TypeScript |
| Forks | 9,397 |
| Issues | 295 |
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
| Stars | 78,463 |
| 语言 | TypeScript |
| Forks | 5,686 |
| Issues | 705 |
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
| Stars | 76,656 |
| 语言 | TypeScript |
| Forks | 6,548 |
| Issues | 173 |
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
| Stars | 75,659 |
| 语言 | JavaScript |
| Forks | 7,272 |
| Issues | 708 |
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
| Stars | 78,616 |
| 语言 | Go |
| Forks | 2,728 |
| Issues | 314 |
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
| Stars | 74,286 |
| 语言 | Go |
| Forks | 2,605 |
| Issues | 929 |
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
| Stars | 36,664 |
| 语言 | Python |
| Forks | 2,562 |
| Issues | 62 |
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
| Stars | 54,453 |
| 语言 | JavaScript |
| Forks | 4,029 |
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
| Stars | 410,605 |
| 语言 | Python |
| Forks | 44,357 |
| Issues | 992 |
| Topics | api, apis, dataset, development, free, list, lists, open-source, public, public-api, public-apis, resources, software |
| 许可证 | MIT License |


## ⚙️ DevOps/基础设施 (16 个项目) { #devops-基础设施 }


### 🌟 高优先级


### code-yeongyu/oh-my-openagent

**描述**: omo; the best agent harness - previously oh-my-opencode

**发现来源**: keyword

**发现原因**: Keyword: Claude

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 40,191 |
| 语言 | TypeScript |
| Forks | 3,032 |
| Issues | 375 |
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
| Stars | 179,274 |
| 语言 | TypeScript |
| Forks | 55,806 |
| Issues | 1,436 |
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
| Stars | 51,646 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 227 |
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
| Stars | 121,154 |
| 语言 | Go |
| Forks | 42,681 |
| Issues | 2,642 |
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
| Stars | 71,524 |
| 语言 | Go |
| Forks | 18,920 |
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
| Stars | 54,299 |
| 语言 | Go |
| Forks | 6,478 |
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
| Stars | 47,584 |
| 语言 | Go |
| Forks | 5,072 |
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
| Stars | 31,299 |
| 语言 | Python |
| Forks | 3,436 |
| Issues | 6 |
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
| Stars | 93,823 |
| 语言 | TypeScript |
| Forks | 9,397 |
| Issues | 295 |
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
| Stars | 84,295 |
| 语言 | TypeScript |
| Forks | 5,294 |
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
| Stars | 75,321 |
| 语言 | TypeScript |
| Forks | 6,397 |
| Issues | 448 |
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
| Stars | 84,101 |
| 语言 | JavaScript |
| Forks | 7,528 |
| Issues | 707 |
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
| Stars | 62,183 |
| 语言 | Go |
| Forks | 5,883 |
| Issues | 782 |
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
| Stars | 57,893 |
| 语言 | Go |
| Forks | 4,197 |
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
| Stars | 44,338 |
| 语言 | Python |
| Forks | 4,473 |
| Issues | 308 |
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
| Stars | 69,362 |
| 语言 | Go |
| Forks | 1,880 |
| Issues | 293 |
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
| Stars | 84,101 |
| 语言 | JavaScript |
| Forks | 7,528 |
| Issues | 707 |
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
| Stars | 63,189 |
| 语言 | Go |
| Forks | 10,245 |
| Issues | 763 |
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
| Stars | 43,656 |
| 语言 | Go |
| Forks | 3,703 |
| Issues | 146 |
| Topics | agents, ai, api, audio-generation, decentralized, distributed, image-generation, libp2p, llama, llm, mamba, mcp, musicgen, object-detection, rerank, stable-diffusion, text-generation, tts |
| 许可证 | MIT License |

---

LocalAI 是一个功能强大的开源 AI 推理平台，作为 OpenAI、Claude 等商业服务的免费替代方案，支持完全本地化部署，无需 GPU 即可在消费级硬件上运行多种 AI 模型（gguf、transformers、diffusers 等），非常适合注重数据隐私和成本控制的开发者及企业。

**技术亮点**:
- 无 GPU 依赖：在消费级 CPU 硬件上即可高效运行大语言模型和生成式 AI
- 多模态支持：集成文本生成、图像生成、音频/视频生成、语音克隆、TTS 等全栈 AI 能力
- 分布式与去中心化：基于 libp2p 和 P2P 技术实现分布式推理和去中心化部署
- OpenAI API 兼容：提供 drop-in 替换接口，可无缝对接现有 OpenAI 生态应用
- 多模型格式支持：兼容 gguf、transformers、diffusers、llama、mamba 等主流模型架构

**适用场景**:
- 企业私有化 AI 部署：满足数据不出域、合规性要求高的企业场景，如金融、医疗等行业
- 个人开发者 AI 应用开发：低成本构建本地 AI 应用，无需支付 API 费用，适合学习实验和原型开发
- 边缘计算和离线场景：在网络受限或无网络环境下使用 AI 能力，支持 IoT 设备和本地服务集成



### fastapi/fastapi

**描述**: FastAPI framework, high performance, easy to learn, fast to code, ready for production

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 96,222 |
| 语言 | Python |
| Forks | 8,861 |
| Issues | 160 |
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
| Stars | 87,045 |
| 语言 | Python |
| Forks | 33,753 |
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
| Stars | 100,087 |
| 语言 | TypeScript |
| Forks | 27,128 |
| Issues | 1,134 |
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
| Stars | 78,463 |
| 语言 | TypeScript |
| Forks | 5,686 |
| Issues | 705 |
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
| Stars | 74,928 |
| 语言 | TypeScript |
| Forks | 8,256 |
| Issues | 56 |
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
| Stars | 75,659 |
| 语言 | JavaScript |
| Forks | 7,272 |
| Issues | 708 |
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
| Stars | 55,947 |
| 语言 | JavaScript |
| Forks | 10,228 |
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
| Stars | 88,241 |
| 语言 | Go |
| Forks | 8,574 |
| Issues | 643 |
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
| Stars | 70,820 |
| 语言 | Go |
| Forks | 4,675 |
| Issues | 241 |
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
| Stars | 56,755 |
| 语言 | Go |
| Forks | 3,178 |
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
| Stars | 36,664 |
| 语言 | Python |
| Forks | 2,562 |
| Issues | 62 |
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
| Stars | 410,605 |
| 语言 | Python |
| Forks | 44,357 |
| Issues | 992 |
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
| Stars | 68,887 |
| 语言 | JavaScript |
| Forks | 22,836 |
| Issues | 191 |
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
| Stars | 99,021 |
| 语言 | TypeScript |
| Forks | 11,802 |
| Issues | 941 |
| Topics | ai, alternative, auth, database, deno, embeddings, example, firebase, nextjs, oauth2, pgvector, postgis, postgres, postgresql, postgrest, realtime, supabase, vectors, websockets |
| 许可证 | Apache License 2.0 |


### Mintplex-Labs/anything-llm

**描述**: The all-in-one AI productivity accelerator. On device and privacy first with no annoying setup or configration.

**发现来源**: trending

**发现原因**: [keyword, trending] Trending in JavaScript

**质量评分**: 98/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 56,268 |
| 语言 | JavaScript |
| Forks | 6,081 |
| Issues | 305 |
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
| Stars | 43,319 |
| 语言 | Go |
| Forks | 3,902 |
| Issues | 1,034 |
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
| Stars | 51,646 |
| 语言 | Go |
| Forks | 10,344 |
| Issues | 227 |
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
| Stars | 71,667 |
| 语言 | MDX |
| Forks | 7,659 |
| Issues | 247 |
| Topics | agent, agents, ai-agents, chatgpt, deep-learning, generative-ai, language-model, llms, openai, prompt-engineering, rag |
| 许可证 | MIT License |

---

这是GitHub上最受欢迎的提示工程综合指南，涵盖从基础提示技巧到前沿AI智能体和RAG技术的完整知识体系。项目整合了教程、论文、Jupyter笔记本等多种资源，是开发者快速掌握大语言模型应用开发技能的权威学习资料库。

**技术亮点**:
- 系统化覆盖提示工程、上下文工程、RAG和AI Agents四大核心技术领域
- 提供可交互的MDX文档和Jupyter笔记本，理论结合实践便于动手学习
- 跟踪最新学术研究论文，保持技术内容的前沿性和时效性
- 涵盖OpenAI、ChatGPT等主流LLM平台的实用技巧和最佳实践
- 开源MIT许可证，支持社区协作和内容持续迭代更新

**适用场景**:
- 企业AI团队学习提示工程技术，提升LLM应用开发质量和效率
- 个人开发者系统掌握AI Agent和RAG技术，快速上手大模型应用开发
- 研究人员和学者获取提示工程领域最新论文和研究资源



### f/prompts.chat

**描述**: f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy.

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 100/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 152,666 |
| 语言 | HTML |
| Forks | 20,074 |
| Issues | 31 |
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
| Stars | 34,354 |
| 语言 | HTML |
| Forks | 5,521 |
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
| Stars | 89,449 |
| 语言 | TypeScript |
| Forks | 9,924 |
| Issues | 2,188 |
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
| Stars | 86,673 |
| 语言 | TypeScript |
| Forks | 8,732 |
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
| Stars | 127,092 |
| 语言 | JavaScript |
| Forks | 12,452 |
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
| Stars | 100,233 |
| 语言 | JavaScript |
| Forks | 7,497 |
| Issues | 217 |
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
| Stars | 167,414 |
| 语言 | Go |
| Forks | 13,058 |
| Issues | 173 |
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
| Stars | 131,223 |
| 语言 | Unknown |
| Forks | 33,315 |
| Issues | 128 |
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
| Stars | 314,736 |
| 语言 | TypeScript |
| Forks | 60,156 |
| Issues | 14,192 |
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
| Stars | 46,031 |
| 语言 | Shell |
| Forks | 6,876 |
| Issues | 47 |
| 许可证 | MIT License |


### unclecode/crawl4ai

**描述**: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN

**发现来源**: keyword

**发现原因**: Keyword: LLM

**质量评分**: 91/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 61,990 |
| 语言 | Python |
| Forks | 6,326 |
| Issues | 26 |
| 许可证 | Apache License 2.0 |


### hacksider/Deep-Live-Cam

**描述**: real time face swap and one-click video deepfake with only a single image

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 90/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 80,036 |
| 语言 | Python |
| Forks | 11,676 |
| Issues | 105 |
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
| Stars | 77,003 |
| 语言 | Python |
| Forks | 6,553 |
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
| Stars | 384,045 |
| 语言 | Python |
| Forks | 66,029 |
| Issues | 69 |
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
| Stars | 112,920 |
| 语言 | TypeScript |
| Forks | 5,722 |
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
| Stars | 102,959 |
| 语言 | TypeScript |
| Forks | 7,489 |
| Issues | 184 |
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
| Stars | 47,930 |
| 语言 | Go |
| Forks | 10,251 |
| Issues | 1,897 |
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
| Stars | 98,027 |
| 语言 | C++ |
| Forks | 15,521 |
| Issues | 1,276 |
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
| Stars | 59,386 |
| 语言 | Python |
| Forks | 1,607 |
| Issues | 38 |
| Topics | batch-processing, data-analytics, data-pipelines, data-processing, dataflow, etl, etl-framework, iot-analytics, kafka, machine-learning-algorithms, pathway, python, real-time, rust, stream-processing, streaming, time-series-analysis |
| 许可证 | Other |


### donnemartin/system-design-primer

**描述**: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 338,955 |
| 语言 | Python |
| Forks | 54,891 |
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
| Stars | 287,308 |
| 语言 | Python |
| Forks | 27,396 |
| Issues | 20 |
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
| Stars | 218,680 |
| 语言 | Python |
| Forks | 50,198 |
| Issues | 885 |
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
| Stars | 85,356 |
| 语言 | Python |
| Forks | 36,996 |
| Issues | 3,617 |
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
| Stars | 85,275 |
| 语言 | Python |
| Forks | 7,163 |
| Issues | 475 |
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
| Stars | 77,690 |
| 语言 | Python |
| Forks | 45,237 |
| Issues | 1,283 |
| 许可证 | Other |


### swisskyrepo/PayloadsAllTheThings

**描述**: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 76,062 |
| 语言 | Python |
| Forks | 16,754 |
| Issues | 15 |
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
| Stars | 438,218 |
| 语言 | TypeScript |
| Forks | 43,623 |
| Issues | 245 |
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
| Stars | 350,948 |
| 语言 | TypeScript |
| Forks | 43,784 |
| Issues | 25 |
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
| Stars | 118,811 |
| 语言 | TypeScript |
| Forks | 12,874 |
| Issues | 2,836 |
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
| Stars | 109,586 |
| 语言 | TypeScript |
| Forks | 8,191 |
| Issues | 1,776 |
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
| Stars | 108,166 |
| 语言 | TypeScript |
| Forks | 13,297 |
| Issues | 5,488 |
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
| Stars | 97,715 |
| 语言 | TypeScript |
| Forks | 54,560 |
| Issues | 1,360 |
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
| Stars | 94,797 |
| 语言 | TypeScript |
| Forks | 5,105 |
| Issues | 647 |
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
| Stars | 94,058 |
| 语言 | TypeScript |
| Forks | 5,113 |
| Issues | 98 |
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
| Stars | 81,148 |
| 语言 | TypeScript |
| Forks | 9,913 |
| Issues | 504 |
| 许可证 | Other |


### vitejs/vite

**描述**: Next generation frontend tooling. It's fast!

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 78,999 |
| 语言 | TypeScript |
| Forks | 7,916 |
| Issues | 650 |
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
| Stars | 243,934 |
| 语言 | JavaScript |
| Forks | 50,789 |
| Issues | 1,177 |
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
| Stars | 138,321 |
| 语言 | JavaScript |
| Forks | 30,649 |
| Issues | 3,474 |
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
| Stars | 116,254 |
| 语言 | JavaScript |
| Forks | 35,059 |
| Issues | 2,538 |
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
| Stars | 111,377 |
| 语言 | JavaScript |
| Forks | 36,308 |
| Issues | 587 |
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
| Forks | 11,553 |
| Issues | 341 |
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
| Stars | 98,024 |
| 语言 | JavaScript |
| Forks | 32,713 |
| Issues | 1,733 |
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
| Stars | 95,426 |
| 语言 | JavaScript |
| Forks | 15,251 |
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
| Stars | 86,053 |
| 语言 | JavaScript |
| Forks | 4,801 |
| Issues | 977 |
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
| Stars | 78,735 |
| 语言 | JavaScript |
| Forks | 31,535 |
| Issues | 271 |
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
| Stars | 70,740 |
| 语言 | JavaScript |
| Forks | 16,800 |
| Issues | 886 |
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
| Stars | 66,029 |
| 语言 | JavaScript |
| Forks | 9,325 |
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
| Stars | 62,116 |
| 语言 | JavaScript |
| Forks | 3,976 |
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
| Stars | 59,870 |
| 语言 | JavaScript |
| Forks | 20,468 |
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
| Stars | 59,839 |
| 语言 | JavaScript |
| Forks | 5,609 |
| Issues | 64 |
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
| Stars | 57,398 |
| 语言 | JavaScript |
| Forks | 12,305 |
| Issues | 23 |
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
| Stars | 133,059 |
| 语言 | Go |
| Forks | 18,861 |
| Issues | 9,873 |
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
| Stars | 105,235 |
| 语言 | Go |
| Forks | 14,948 |
| Issues | 44 |
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
| Stars | 87,096 |
| 语言 | Go |
| Forks | 8,205 |
| Issues | 259 |
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
| Stars | 80,840 |
| 语言 | Go |
| Forks | 4,961 |
| Issues | 408 |
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
| Stars | 68,688 |
| 语言 | Go |
| Forks | 3,220 |
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
| Stars | 56,044 |
| 语言 | Go |
| Forks | 4,972 |
| Issues | 1,141 |
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
| Stars | 50,921 |
| 语言 | Go |
| Forks | 21,850 |
| Issues | 375 |
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
| Stars | 50,131 |
| 语言 | Go |
| Forks | 1,588 |
| Issues | 257 |
| 许可证 | MIT License |


### AlistGo/alist

**描述**: 🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs. / 一个支持多存储的文件列表/WebDAV程序，使用 Gin 和 Solidjs。

**发现来源**: trending

**发现原因**: Trending in Go

**质量评分**: 85/100

**活跃度**: high

| 指标 | 数值 |
|------|------|
| Stars | 49,175 |
| 语言 | Go |
| Forks | 7,982 |
| Issues | 568 |
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
| Stars | 46,951 |
| 语言 | Go |
| Forks | 8,881 |
| Issues | 8 |
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
| Stars | 45,461 |
| 语言 | Go |
| Forks | 3,765 |
| Issues | 91 |
| Topics | go, management, node, node-version-manager, nodejs, nvm, switch, version, version-manager, versioning, windows |
| 许可证 | MIT License |


### ⭐ 中优先级


### ytdl-org/youtube-dl

**描述**: Command-line program to download videos from YouTube.com and other video sites

**发现来源**: trending

**发现原因**: Trending in Python

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 139,873 |
| 语言 | Python |
| Forks | 10,602 |
| Issues | 4,119 |
| 许可证 | The Unlicense |


### realworld-apps/realworld

**描述**: "The mother of all demo apps" — Exemplary fullstack Medium.com clone powered by React, Angular, Node, Django, and many more

**发现来源**: trending

**发现原因**: Trending in TypeScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 83,000 |
| 语言 | TypeScript |
| Forks | 7,579 |
| Issues | 37 |
| 许可证 | MIT License |


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
| Forks | 31,114 |
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
| Stars | 148,119 |
| 语言 | JavaScript |
| Forks | 26,772 |
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
| Stars | 67,262 |
| 语言 | JavaScript |
| Forks | 11,983 |
| Issues | 538 |
| Topics | canvas, chart, graph, html5, html5-charts, javascript |
| 许可证 | MIT License |


### juliangarnier/anime

**描述**: JavaScript animation engine

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,855 |
| 语言 | JavaScript |
| Forks | 4,472 |
| Issues | 94 |
| Topics | animation, anime, canvas, css, javascript, javascript-library, svg |
| 许可证 | MIT License |


### leonardomso/33-js-concepts

**描述**: 📜 33 JavaScript concepts every developer should know.

**发现来源**: trending

**发现原因**: Trending in JavaScript

**质量评分**: 75/100

**活跃度**: medium

| 指标 | 数值 |
|------|------|
| Stars | 66,281 |
| 语言 | JavaScript |
| Forks | 9,189 |
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
| Stars | 61,579 |
| 语言 | JavaScript |
| Forks | 7,128 |
| Issues | 132 |
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
| Stars | 146,211 |
| 语言 | Python |
| Forks | 11,226 |
| Issues | 293 |
| Topics | awesome, github, hellogithub, python |
