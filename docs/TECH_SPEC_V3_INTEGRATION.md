# TrendPulse 技术方案 v3.0 - 基于现有项目的集成方案

> 站在巨人的肩膀上，而不是重新造轮子

---

## 一、核心发现：可以复用的基础设施

### 1.1 GH Archive - 海量 GitHub 数据源

**发现**：[GH Archive](https://www.gharchive.org/) 是一个自 2011 年以来记录所有公开 GitHub 事件的项目！

```
数据规模：
- 自 2011 年以来的所有公开 GitHub 事件
- 每小时生成一个 JSON/GZ 文件
- 可通过 BigQuery 直接查询
- 完全免费！
```

**这意味着**：
- ✅ 不需要自己抓取 GitHub API
- ✅ 不用担心速率限制
- ✅ 历史数据立即可用
- ✅ 可以回溯分析任何时间段

### 1.2 OSS Insight Lite - 开箱即用的数据管道

**发现**：[OSS Insight Lite](https://github.com/pingcap/ossinsight-lite) 是一个轻量级的 GitHub 分析平台！

```
架构：
GitHub Actions → TiDB Serverless → Vercel
     ↓               ↓                ↓
  数据采集        数据存储         前端展示
```

**我们可以**：
- Fork OSS Insight Lite
- 复用其 GitHub Actions 数据采集流程
- 复用其数据模型和 SQL 查询
- 在此基础上添加 AI 分析功能

### 1.3 PR-Agent - 成熟的 AI 分析引擎

**发现**：[PR-Agent](https://github.com/qodo-ai/pr-agent) 可以作为 Python 库使用！

```python
# PR-Agent 的使用方式
from pr_agent.agent.pr_agent import PRAgent

agent = PRAgent()
result = agent.analyze_pr(
    repo_url="anthropics/anthropic-sdk-python",
    pr_number=123,
    commands=["/review", "/describe"]
)
```

**我们可以**：
- 直接调用 PR-Agent 的分析能力
- 扩展其 Prompt 模板，添加"趋势分析"模式
- 复用其重试、降级机制

### 1.4 LlamaIndex - Agent 框架

**发现**：[LlamaIndex](https://github.com/run-llama/llama_index) 有现成的 GitHub 分析例子！

```python
# LlamaIndex 的 GitHub Issue 分析
from llama_index.core.readers.github_reader import GitHubRepositoryIssuesReader

reader = GitHubRepositoryIssuesReader()
documents = reader.load_data(
    owner="anthropics",
    repo="anthropic-sdk-python",
)
```

---

## 二、集成方案对比

### 方案 A：基于 OSS Insight Lite 扩展（推荐 ⭐⭐⭐⭐⭐）

```
┌─────────────────────────────────────────────────────────────┐
│                    Fork OSS Insight Lite                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  复用现有的数据采集层                                        │
│  - GitHub Actions workflow                                  │
│  - GH Archive 数据集成                                      │
│  - TiDB Serverless 存储                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  新增：AI 分析层（Python）                                   │
│  - 使用 PR-Agent 的分析能力                                 │
│  - 使用 Instructor + Claude 提取趋势信号                    │
│  - 定时任务写入 TiDB                                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  扩展前端展示                                                │
│  - 添加"趋势信号"页面                                       │
│  - 添加 AI 洞察卡片                                         │
└─────────────────────────────────────────────────────────────┘
```

**优势**：
- ✅ **最小开发量**：复用 80% 的基础设施
- ✅ **开箱即用**：数据采集、存储、展示都已就绪
- ✅ **可扩展**：TiDB 支持复杂查询
- ✅ **零成本**：TiDB Serverless 免费额度足够

**实现步骤**：
1. Fork `pingcap/ossinsight-lite`
2. 修改 GitHub Actions，添加 AI 分析任务
3. 新建 Python 服务，调用 PR-Agent + Claude
4. 扩展前端，添加趋势信号展示

---

### 方案 B：独立服务 + GH Archive（推荐 ⭐⭐⭐⭐）

```
┌─────────────────────────────────────────────────────────────┐
│  数据层：直接查询 GH Archive                                │
│  - BigQuery SQL 查询                                        │
│  - 或下载 JSON 文件到本地                                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  AI 分析层：Python 服务                                     │
│  - 使用 PyGithub 获取 PR 详情                               │
│  - 使用 Instructor + Claude 分析                            │
│  - 使用 PR-Agent 的 Prompt 模板                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  展示层：MkDocs 静态站点                                     │
│  - GitHub Pages 部署                                        │
│  - Markdown + Jinja2                                        │
└─────────────────────────────────────────────────────────────┘
```

**优势**：
- ✅ **完全自主**：不依赖复杂的基础设施
- ✅ **简单部署**：只需 Python + GitHub Pages
- ✅ **成本低**：GH Archive 免费，GitHub Pages 免费

**实现步骤**：
1. 使用 BigQuery API 查询 GH Archive
2. 使用 PyGithub 获取详细的 PR/Release 数据
3. 使用 Instructor 提取趋势信号
4. 使用 MkDocs 生成静态站点

---

### 方案 C：LlamaIndex Agent 框架（推荐 ⭐⭐⭐）

```
┌─────────────────────────────────────────────────────────────┐
│  LlamaIndex Workflows                                       │
│  - GitHub Reader                                            │
│  - Multi-Agent 协作                                         │
│  - Claude Agent                                             │
└─────────────────────────────────────────────────────────────┘
```

**优势**：
- ✅ **Agent 编排**：LlamaIndex 提供成熟的 Agent 框架
- ✅ **可扩展**：易于添加新的分析任务
- ✅ **社区支持**：活跃的开源社区

**劣势**：
- ❌ **学习曲线**：需要理解 LlamaIndex 的概念
- ❌ **过度设计**：对于简单分析可能太复杂

---

## 三、推荐方案：方案 B（独立服务 + GH Archive）

### 为什么选择方案 B？

1. **简单直接**：不需要 fork 复杂的项目
2. **完全自主**：可以完全控制实现细节
3. **易于维护**：代码量少，依赖清晰
4. **快速迭代**：MVP 可以快速上线

### 架构设计

```
trendpulse/
├── data/
│   ├── collectors/           # 数据采集
│   │   ├── gh_archive.py     # GH Archive 查询
│   │   └── github_api.py     # GitHub API 详情获取
│   └── storage/              # 本地存储（可选）
├── analyzers/                # AI 分析
│   ├── pr_agent_wrapper.py   # PR-Agent 封装
│   ├── claude_analyzer.py    # Claude 分析器
│   └── signal_extractor.py   # 信号提取器
├── reports/                  # 报告生成
│   └── markdown_renderer.py  # Markdown 渲染
├── web/                      # 前端
│   └── mkdocs/               # MkDocs 配置
└── workflows/                # GitHub Actions
    └── daily_analysis.yml    # 每日分析流程
```

### 核心代码框架

#### 3.1 数据采集（GH Archive）

```python
# data/collectors/gh_archive.py
from google.cloud import bigquery
from datetime import datetime, timedelta

class GHArchiveCollector:
    """从 GH Archive 收集数据"""

    def __init__(self):
        self.client = bigquery.Client()

    def fetch_events(
        self,
        repos: list[str],
        since: datetime,
    ) -> list[dict]:
        """查询 GH Archive 的 BigQuery 数据集"""

        query = f"""
        SELECT
            type,
            repo.name,
            payload,
            created_at,
        FROM
            `githubarchive.day.{{date}}`
        WHERE
            repo.name IN UNNEST(@repos)
            AND type IN ('PullRequestEvent', 'ReleaseEvent')
            AND created_at > @since
        """

        job = self.client.query(
            query,
            job_config_params={
                "repos": repos,
                "since": since.isoformat(),
            }
        )

        return list(job.result())
```

#### 3.2 AI 分析（集成 PR-Agent）

```python
# analyzers/pr_agent_wrapper.py
from pr_agent.agent.pr_agent import PRAgent
from instructor import from_anthropic
from anthropic import Anthropic

class TrendAnalyzer:
    """趋势分析器，结合 PR-Agent 和 Claude"""

    def __init__(self):
        self.pr_agent = PRAgent()
        self.claude = from_anthropic(Anthropic())

    def analyze_prs(self, prs: list[dict]) -> list[Signal]:
        """分析多个 PR，提取趋势信号"""

        # 步骤 1：使用 PR-Agent 快速分析每个 PR
        pr_summaries = []
        for pr in prs:
            summary = self.pr_agent.analyze(
                repo_url=pr["repo"]["name"],
                pr_number=pr["payload"]["number"],
                commands=["/describe", "/summarize"]
            )
            pr_summaries.append(summary)

        # 步骤 2：使用 Claude 聚合分析，提取趋势
        signals = self.claude.messages.create(
            model="claude-sonnet-4-5",
            response_model=list[Signal],
            messages=[{
                "role": "user",
                "content": self._build_trend_prompt(pr_summaries),
            }]
        )

        return signals

    def _build_trend_prompt(self, summaries: list[dict]) -> str:
        """构建趋势分析 Prompt"""
        return f"""你是 Anthropic 技术趋势分析专家。以下是一批 PR 的摘要：

{summaries}

请分析这些变更，提取 5-10 个最重要的趋势信号。

关注点：
1. 新能力（如新的 API、新的功能）
2. 抽象层的改进（如更好的封装、新的模式）
3. 工具链变化（如 CLI 工具、开发体验）
4. Agent workflow 相关
5. Eval 和测试相关
6. 性能和安全性
"""
```

#### 3.3 报告生成（复用 git-cliff 思路）

```python
# reports/markdown_renderer.py
from jinja2 import Environment, FileSystemLoader

class ReportRenderer:
    """Markdown 报告渲染器（借鉴 git-cliff）"""

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader("templates"),
            autoescape=False,
        )

    def render_daily(self, signals: list[Signal], date: str) -> str:
        """渲染每日报告"""

        template = self.env.get_template("daily.md.j2")

        # 按类型分组
        engineering = [s for s in signals if s.category == "engineering"]
        research = [s for s in signals if s.category == "research"]

        return template.render(
            date=date,
            engineering_signals=engineering,
            research_signals=research,
        )
```

### 模板示例

```markdown
<!-- templates/daily.md.j2 -->
# {{ date }} - Anthropic 技术趋势

## 工程信号

{% for signal in engineering_signals %}
### [{{ signal.impact_score }}/5] {{ signal.title }}

**Why it matters**: {{ signal.why_it_matters }}

**Sources**:
{% for source in signal.sources %}
- [{{ source }}]({{ source }})
{% endfor %}

{% endfor %}

## 研究信号

{% for signal in research_signals %}
### [{{ signal.impact_score }}/5] {{ signal.title }}

**Why it matters**: {{ signal.why_it_matters }}

**Sources**:
{% for source in signal.sources %}
- [{{ source }}]({{ source }})
{% endfor %}

{% endfor %}
```

---

## 四、实施路线图

### Phase 1: MVP（2 周）

- [ ] 使用 BigQuery 查询 GH Archive
- [ ] 使用 PyGithub 获取 PR 详情
- [ ] 使用 Instructor + Claude 分析
- [ ] 使用 MkDocs 生成静态站点

### Phase 2: 集成 PR-Agent（1 周）

- [ ] 封装 PR-Agent API
- [ ] 添加快速分析模式
- [ ] 优化 Prompt

### Phase 3: 优化（1 周）

- [ ] 添加缓存机制
- [ ] 添加重试和降级
- [ ] 优化成本

---

## 五、技术栈总结

| 层级 | 技术选择 | 说明 |
|------|----------|------|
| **数据源** | GH Archive (BigQuery) | 免费的历史数据 |
| **API** | PyGithub | 获取详细信息 |
| **AI 分析** | PR-Agent + Instructor | 双引擎 |
| **模型** | Claude Sonnet 4.5 | 理解能力强 |
| **报告** | Jinja2 + MkDocs | 灵活的模板 |
| **部署** | GitHub Actions + Pages | 零成本 |

---

## 六、与原方案的对比

| 方面 | 原方案（v1.0） | 新方案（v3.0 集成） |
|------|----------------|---------------------|
| **数据源** | 自己抓取 GitHub API | GH Archive（无需抓取） |
| **重试机制** | 手动实现 | PR-Agent 内置 |
| **AI 分析** | 从零开始 | 复用 PR-Agent |
| **基础设施** | 需要搭建 | 直接使用 GH Archive |
| **开发量** | ~2000 行代码 | ~500 行代码 |
| **上线时间** | 4-6 周 | 2-3 周 |

---

## 七、快速开始

```bash
# 1. 克隆项目模板（基于方案 B）
git clone https://github.com/yourname/trendpulse.git
cd trendpulse

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 BigQuery（可选，用于 GH Archive）
gcloud auth application-default login

# 4. 配置 Claude API
export ANTHROPIC_API_KEY=your-key

# 5. 运行分析
python -m trendpulse.main --date 2026-01-02

# 6. 构建站点
mkdocs build
```

---

## 八、参考资源

- [GH Archive](https://www.gharchive.org/)
- [OSS Insight Lite](https://github.com/pingcap/ossinsight-lite)
- [PR-Agent](https://github.com/qodo-ai/pr-agent)
- [LlamaIndex GitHub Reader](https://developers.llamaindex.ai/python/examples/usecases/github_issue_analysis/)
