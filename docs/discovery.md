# 项目发现历史

自动发现的 GitHub 热门项目报告，每天自动更新。

## 最新报告

### [2026-01-31](discovery-reports/discovery-2026-01-31.md)

**发现概览**:<br/>
- 总发现数: 200<br/>
- 通过质量评估: 200<br/>
- 高优先级: 134<br/>
- 去重移除: 36<br/>
- 已在监控: 19<br/>

**高优先级推荐 Top 5**:

1. **[open-webui/open-webui](https://github.com/open-webui/open-webui)** - 122,465 ⭐
   - 用户友好的 AI 界面，支持 Ollama、OpenAI API

2. **[f/prompts.chat](https://github.com/f/prompts.chat)** - 144,131 ⭐
   - Awesome ChatGPT Prompts，分享和发现 AI 提示词

3. **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** - 78,617 ⭐
   - Web 数据 API，将网站转换为 LLM 可用的 Markdown

4. **[infiniflow/ragflow](https://github.com/infiniflow/ragflow)** - 72,488 ⭐
   - 开源 RAG 引擎，融合 Agent 能力

5. **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** - 54,014 ⭐
   - 一体化 AI 应用平台，内置 RAG 和 AI Agents<br/>


## 历史报告

| 日期 | 总发现 | 高优先级 | 报告 |
|------|--------|----------|------|
| 2026-01-31 | 200 | 134 | [查看](discovery-reports/discovery-2026-01-31.md) |

## 关于发现功能

### 发现来源

项目通过以下方式自动发现：

1. **GitHub Trending** - 爬取各语言的 Trending 页面
2. **关键词搜索** - 基于 AI 相关关键词搜索

### 质量评估

每个发现的项目会经过多维度质量评估：

- **Stars 指标**: 项目受欢迎程度
- **活跃度指标**: 最近提交时间
- **社区指标**: Forks 和 Watchers 数量
- **代码质量**: License 和 Open Issues 比例
- **相关性**: 与 AI/LLM 主题的相关度

**总质量分**: 0-100 分，动态计算 ≥60 分为推荐

### 项目分类

发现的项目会自动分类到以下技术类别：

| 分类 | 图标 | 关键词示例 |
|------|------|-----------|
| AI Agents | 🤖 | agent, multi-agent, mcp, agentic |
| RAG/检索 | 🔍 | rag, retrieval, vector, embeddings, graphrag |
| LLM 界面 | 💬 | llm-ui, webui, chatbot, openai, ollama |
| 机器学习框架 | 🧠 | deep-learning, pytorch, tensorflow, nlp |
| 开发工具 | 🛠️ | cli, sdk, ide, developer-tools |
| DevOps/基础设施 | ⚙️ | devops, kubernetes, docker, ci-cd |
| 监控/观测 | 📈 | monitoring, metrics, observability, logging |
| Web 框架 | 🌐 | backend, api, rest, graphql, framework |
| 数据/基础设施 | 📊 | database, vector-database, data-pipeline |
| 学习资源 | 📚 | awesome-list, tutorial, prompt-engineering |

### 推荐优先级

使用**动态阈值**算法，根据项目质量分数分布自动确定优先级阈值：

- **高优先级** (high): 前 30% 的项目（当前阈值: ≥80）
- **中优先级** (medium): 前 70% 的项目（当前阈值: ≥75）
- **低优先级** (low): 其他通过质量评估的项目

### 运行方式

```bash
# 本地运行发现
uv run python scripts/discover_projects.py

# 自定义参数
uv run python scripts/discover_projects.py \
  --days 7 \
  --min-quality 60.0 \
  --languages python typescript go \
  --keywords "AI agent" "LLM" "Claude" "RAG"
```

### 自动运行

项目发现通过 GitHub Actions 每天自动运行。

- **运行时间**: 每天 UTC 19:00 (北京时间凌晨 3:00)
- **回溯天数**: 默认 30 天
- **最低质量分**: 默认 60.0

查看工作流: [discover-projects.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-projects.yml)
