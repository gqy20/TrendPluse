# TrendPulse MVP 技术方案 v2.0

> 基于开源包调研的完善版本

## 一、竞品分析：现有 GitHub 分析工具

### 1.1 已有开源方案调研

| 工具 | Star 数 | 功能定位 | 与我们的差异 |
|------|---------|----------|--------------|
| **OSS Insight** | 11k+ | 全面的 GitHub 数据分析平台 | ✅ 数据驱动，无 AI 分析；🎯 我们聚焦趋势信号提取 |
| **PR-Agent** | 8k+ | AI 驱动的 PR 代码审查 | ✅ 单 PR 深度分析；🎯 我们做多事件聚合 |
| **RepoSense** | 1.5k+ | 代码贡献可视化分析 | ✅ 贡献度统计；🎯 我们做技术趋势分析 |
| **git-cliff** | 3k+ | 从 commits 生成 changelog | ✅ 基于提交消息；🎯 我们基于 AI 理解 |
| **conventional-changelog** | 8k+ | Conventional Commits 规范 | ✅ 需要规范遵守；🎯 我们理解任意描述 |
| **Weekly-Report-Generator** | <500 | 个人周报生成 | ✅ 面向个人；🎯 我们面向组织/项目 |
| **github-org-metrics** | <500 | 组织级别指标分析 | ✅ 统计指标；🎯 我们做趋势洞察 |

### 1.2 差异化定位

```
现有工具的分类：

┌─────────────────────────────────────────────────────────────┐
│  数据统计类                                                  │
│  - OSS Insight: 大数据分析平台                              │
│  - RepoSense: 贡献度可视化                                  │
│  - github-org-metrics: 组织指标                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Changelog 生成类                                            │
│  - git-cliff: 基于 commits 生成                             │
│  - conventional-changelog: 规范驱动                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  AI 代码审查类                                               │
│  - PR-Agent: 单 PR 深度分析                                 │
│  - CodeSpect: 自动化代码审查                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TrendPulse (我们)                                          │
│  ✅ AI 驱动的趋势信号提取                                   │
│  ✅ 跨事件的聚合分析（工程 + 研究）                         │
│  ✅ 结构化输出 + 可浏览站点                                  │
└─────────────────────────────────────────────────────────────┘
```

### 1.3 可借鉴的设计

**从 OSS Insight 借鉴**：
- 数据可视化展示方式
- GitHub API 高效查询模式
- 静态站点生成架构

**从 PR-Agent 借鉴**：
- AI Prompt 模板设计
- 结构化输出验证机制
- 重试和降级策略

**从 git-cliff 借鉴**：
- 模板引擎使用（Jinja2）
- 增量更新策略
- Markdown 输出格式

---

## 二、开源包选型

### 2.1 核心依赖

| 功能 | 包名 | 版本 | 说明 |
|------|------|------|------|
| **GitHub API** | `PyGithub` | >=2.5.0 | 成熟的 GitHub REST API 客户端，类型完善 |
| **Claude API** | `instructor` | >=1.6.0 | 结构化输出神器，基于 Pydantic，内置重试和验证 |
| **Claude SDK** | `anthropic` | >=0.45.0 | 官方 SDK（instructor 依赖） |
| **配置管理** | `pydantic-settings` | >=2.6.0 | 官方配置管理，支持环境变量 |
| **模板引擎** | `jinja2` | >=3.1.0 | 生成 Markdown 报告 |
| **日志系统** | `rich` | >=13.0.0 | 终端美化 + logging handler |
| **重试机制** | `tenacity` | >=9.0.0 | 优雅的重试装饰器 |
| **异步 HTTP** | `aiohttp` | >=3.10.0 | 异步请求（可选） |

### 2.2 为什么选择 instructor？

```python
# 原方案：直接使用 anthropic SDK
response = client.beta.messages.parse(
    model=settings.anthropic_model,
    output_format=DailyReport,  # Beta 功能
    ...
)

# 新方案：使用 instructor
import instructor
from anthropic import Anthropic

# 自动处理重试、验证、错误恢复
client = instructor.from_anthropic(Anthropic())
report = client.messages.create(
    model=settings.anthropic_model,
    response_model=DailyReport,  # 稳定可靠
    messages=[...]
)
```

**优势**：
- ✅ 不依赖 Beta 功能，更稳定
- ✅ 自动重试和验证
- ✅ 支持多种模型（OpenAI、Anthropic、本地）
- ✅ 更好的错误处理

---

## 三、从现有工具借鉴的设计模式

### 3.1 PR-Agent 的 AI 分析模式

PR-Agent (qodo-ai/pr-agent) 是一个非常成熟的 AI PR 分析工具，我们可以借鉴：

**1. 多级分析策略**
```python
# 从 PR-Agent 借鉴：根据 PR 大小选择分析深度
def analyze_pr(pr: PullRequest) -> Analysis:
    # 小 PR：快速总结
    if pr.additions + pr.deletions < 100:
        return quick_summary(pr)

    # 中等 PR：详细分析
    elif pr.additions + pr.deletions < 500:
        return detailed_analysis(pr)

    # 大 PR：分段分析
    else:
        return segmented_analysis(pr)
```

**2. Prompt 模板化**
```python
# 从 PR-Agent 借鉴：使用 Jinja2 管理 Prompt
ANALYSIS_PROMPTS = {
    "summary": "templates/prompts/summary.md.j2",
    "review": "templates/prompts/review.md.j2",
    "trend": "templates/prompts/trend_analysis.md.j2",
}

def get_prompt(type: str, **context) -> str:
    template = env.get_template(ANALYSIS_PROMPTS[type])
    return template.render(**context)
```

### 3.2 git-cliff 的模板引擎使用

git-cliff 是一个强大的 changelog 生成器，其模板设计值得学习：

**1. 多格式输出支持**
```python
# 从 git-cliff 借鉴：一个模板引擎，多种输出
class ReportRenderer:
    def render(self, report: DailyReport, format: str = "markdown") -> str:
        if format == "markdown":
            return self._render_markdown(report)
        elif format == "json":
            return report.model_dump_json(indent=2)
        elif format == "html":
            return self._render_html(report)

    def _render_markdown(self, report: DailyReport) -> str:
        return self.md_template.render(report=report)

    def _render_html(self, report: DailyReport) -> str:
        return self.html_template.render(report=report)
```

**2. 增量更新策略**
```python
# 从 git-cliff 借鉴：只处理新的变更
def get_new_events_since_last_run() -> list[Event]:
    last_run_file = Path("data/last_run.txt")
    if last_run_file.exists():
        last_run = datetime.fromisoformat(last_run_file.read_text())
    else:
        last_run = datetime.now() - timedelta(days=1)

    events = fetch_events(since=last_run)
    return events
```

### 3.3 OSS Insight 的数据可视化

OSS Insight 使用 TiDB 处理海量 GitHub 数据，我们可以借鉴其展示方式：

**1. 信号分类展示**
```markdown
# 从 OSS Insight 借鉴：清晰的分类展示
## 工程趋势信号

### 🚀 新能力
- [5/5] Structured Output Support
- [4/5] Streaming Response API

### 🔧 工具链
- [3/5] New CLI Tool
- [2/5] Improved Error Messages

## 研究趋势信号

### 🧪 Agent Workflows
- [5/5] Multi-Agent Collaboration
- [4/5] Tool Use Patterns

### 📊 Eval Systems
- [3/5] New Benchmarks
```

**2. 时间线视图**
```python
# 从 OSS Insight 借鉴：按时间组织
def organize_by_timeline(signals: list[Signal]) -> dict[str, list[Signal]]:
    """将信号按时间分组"""
    timeline = {}
    for signal in signals:
        date = signal.date[:7]  # YYYY-MM
        if date not in timeline:
            timeline[date] = []
        timeline[date].append(signal)
    return timeline
```

---

## 四、项目结构（uv + src layout）

```
trendpluse/
├── .github/
│   └── workflows/
│       └── daily.yml          # GitHub Actions
├── src/
│   └── trendpluse/
│       ├── __init__.py
│       ├── main.py            # CLI 入口
│       ├── config.py          # 配置管理
│       ├── logger.py          # Rich 日志系统
│       ├── models/
│       │   ├── __init__.py
│       │   └── signal.py      # Pydantic 数据模型
│       ├── github/
│       │   ├── __init__.py
│       │   ├── client.py      # PyGithub 封装
│       │   └── models.py      # GitHub 数据模型
│       ├── analyzer/
│       │   ├── __init__.py
│       │   ├── claude.py      # Instructor 分析器
│       │   └── prompts.py     # Prompt 模板
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── fetch.py       # Stage 1: 拉取
│       │   ├── filter.py      # Stage 2: 筛选
│       │   ├── analyze.py     # Stage 3: 分析
│       │   └── render.py      # Stage 4: 渲染
│       └── utils/
│           ├── __init__.py
│           ├── retry.py       # Tenacity 重试配置
│           └── templates.py   # Jinja2 模板管理
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # pytest fixtures
│   ├── test_github.py         # GitHub API 测试
│   ├── test_analyzer.py       # 分析器测试（mock）
│   └── test_pipeline.py       # 端到端测试
├── data/
│   ├── snapshots/             # 原始数据
│   ├── processed/             # 处理后数据
│   └── fallback/              # 降级数据
├── reports/
│   └── daily/                 # 每日报告（JSON + Markdown）
├── docs/                      # MkDocs 源
├── templates/                 # Jinja2 模板
│   └── daily_report.md.j2
├── scripts/                   # 辅助脚本
│   └── mock_data.py           # 生成测试数据
├── pyproject.toml             # uv 项目配置
├── uv.lock                    # uv 锁文件
├── .env.example               # 环境变量示例
├── Makefile                   # 常用命令
├── mkdocs.yml
└── README.md
```

---

## 五、核心代码实现（基于开源包）

### 5.1 配置管理（pydantic-settings）

```python
# src/trendpluse/config.py
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """配置管理，支持环境变量和 .env"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="TRENDPULSE_",
        extra="ignore",
    )

    # GitHub 配置
    github_token: str = Field(description="GitHub Personal Access Token")
    github_repos: list[str] = Field(
        default=["anthropics/anthropic-sdk-python"],
        description="要追踪的仓库列表"
    )
    github_base_url: str = "https://api.github.com"

    # Anthropic 配置
    anthropic_api_key: str = Field(description="Anthropic API Key")
    anthropic_model: str = "claude-sonnet-4-5"
    anthropic_max_tokens: int = 8000
    anthropic_timeout: int = 120

    # 筛选规则
    candidate_labels: list[str] = [
        "feature", "enhancement", "eval", "tooling",
        "agent", "workflow", "safety"
    ]
    max_candidates: int = 20
    days_to_lookback: int = 1  # 查看过去几天的数据

    # 成本控制
    daily_token_budget: int = 100_000
    max_retries: int = 3

    # 输出配置
    output_dir: str = "reports/daily"
    snapshot_dir: str = "data/snapshots"

    @field_validator("github_repos")
    @classmethod
    def validate_repos(cls, v: list[str]) -> list[str]:
        """验证仓库格式"""
        for repo in v:
            if "/" not in repo or len(repo.split("/")) != 2:
                raise ValueError(f"Invalid repo format: {repo}")
        return v

settings = Settings()
```

### 5.2 日志系统（rich）

```python
# src/trendpluse/logger.py
import logging
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler

def setup_logger(name: str = "trendpluse", level: str = "INFO") -> logging.Logger:
    """配置 Rich 日志系统"""

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # 清除现有 handlers
    logger.handlers.clear()

    # Rich 终端输出
    console = Console()
    handler = RichHandler(
        console=console,
        show_time=True,
        show_path=True,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
    )
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)

    # 文件输出（可选）
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / f"{name}.log")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()
```

### 5.3 GitHub 客户端（PyGithub）

```python
# src/trendpluse/github/client.py
from datetime import datetime, timedelta
from typing import Any

from github import Github, GithubException
from tenacity import retry, stop_after_attempt, wait_exponential

from ..config import settings
from ..logger import logger
from .models import RepoEvent, PullRequestEvent, ReleaseEvent

class GitHubClient:
    """GitHub API 客户端封装"""

    def __init__(self, token: str | None = None):
        token = token or settings.github_token
        self.client = Github(token, per_page=100)
        self._rate_limit_remain: int | None = None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry_error_callback=lambda _: None,
    )
    def get_events(
        self,
        repos: list[str] | None = None,
        days: int = 1,
    ) -> list[RepoEvent]:
        """获取指定仓库的最近事件"""

        repos = repos or settings.github_repos
        since = datetime.now() - timedelta(days=days)

        logger.info(f"Fetching events from {len(repos)} repos since {since}")

        all_events: list[RepoEvent] = []

        for repo_name in repos:
            try:
                repo = self.client.get_repo(repo_name)
                events = self._fetch_repo_events(repo, since)
                all_events.extend(events)
                logger.info(f"Found {len(events)} events in {repo_name}")

            except GithubException as e:
                logger.error(f"Failed to fetch {repo_name}: {e}")
                continue

        return all_events

    def _fetch_repo_events(
        self,
        repo: Any,  # github.Repository.Repository
        since: datetime,
    ) -> list[RepoEvent]:
        """获取单个仓库的事件"""

        events: list[RepoEvent] = []

        # 获取已合并的 PR
        pulls = repo.get_pulls(
            state="closed",
            sort="updated",
            direction="desc",
        )
        for pull in pulls:
            if pull.merged_at and pull.merged_at > since:
                events.append(
                    PullRequestEvent(
                        number=pull.number,
                        title=pull.title,
                        body=pull.body or "",
                        state="merged",
                        merged_at=pull.merged_at.isoformat(),
                        author=pull.user.login,
                        labels=[label.name for label in pull.labels],
                        url=pull.html_url,
                        diff_summary=self._get_diff_summary(pull),
                    )
                )

        # 获取 Releases
        releases = repo.get_releases()
        for release in releases:
            if release.created_at > since:
                events.append(
                    ReleaseEvent(
                        tag_name=release.tag_name,
                        name=release.title or release.tag_name,
                        body=release.body or "",
                        url=release.html_url,
                        created_at=release.created_at.isoformat(),
                    )
                )

        return events

    def _get_diff_summary(self, pull: Any) -> str:
        """获取 PR 的 diff 摘要（前 2000 字符）"""
        try:
            # 使用 Files API 获取变更文件
            files = pull.get_files()
            summary_parts = []
            total_chars = 0
            max_chars = 2000

            for file in files:
                if total_chars >= max_chars:
                    break
                file_summary = f"\n- {file.filename}: {file.status} (+{file.additions}, -{file.deletions})"
                if total_chars + len(file_summary) > max_chars:
                    summary_parts.append(f"\n- ... ({len(list(files))} files changed)")
                    break
                summary_parts.append(file_summary)
                total_chars += len(file_summary)

            return "".join(summary_parts)[:max_chars]

        except Exception as e:
            logger.warning(f"Failed to get diff for PR #{pull.number}: {e}")
            return ""
```

### 5.4 分析器（instructor）

```python
# src/trendpluse/analyzer/claude.py
from anthropic import Anthropic
from instructor import from_anthropic

from ..config import settings
from ..logger import logger
from ..models.signal import DailyReport
from .prompts import build_analysis_prompt

class ClaudeAnalyzer:
    """基于 Instructor 的 Claude 分析器"""

    def __init__(self, api_key: str | None = None):
        api_key = api_key or settings.anthropic_api_key

        # 创建 instructor 客户端（自动处理重试和验证）
        self.client = from_anthropic(
            Anthropic(api_key=api_key),
            mode=instructor.Mode.JSON,
        )

    def analyze(self, candidates: list[dict]) -> DailyReport:
        """分析候选事件，提取趋势信号"""

        logger.info(f"Analyzing {len(candidates)} candidates with Claude")

        try:
            # 使用 instructor 的结构化输出
            report: DailyReport = self.client.messages.create(
                model=settings.anthropic_model,
                response_model=DailyReport,
                max_tokens=settings.anthropic_max_tokens,
                messages=[{
                    "role": "user",
                    "content": build_analysis_prompt(candidates),
                }],
            )

            logger.info(
                f"Generated {len(report.engineering_signals) + len(report.research_signals)} signals"
            )
            return report

        except Exception as e:
            logger.error(f"Analysis failed: {e}")
            raise

    def estimate_tokens(self, candidates: list[dict]) -> int:
        """估算 token 消耗"""
        # 粗略估算：每个字符约 0.25 tokens
        text = str(candidates)
        return int(len(text) * 0.25)
```

### 5.5 Prompt 模板（Jinja2）

```python
# src/trendpluse/analyzer/prompts.py
from jinja2 import Template

ANALYSIS_PROMPT_TEMPLATE = Template("""
你是 Anthropic 技术趋势分析专家。分析以下 GitHub 更新，提取趋势信号。

# 分析目标

1. **工程趋势信号**：SDK API 新能力、新抽象、工具链变化
2. **研究趋势信号**：agent workflow、eval 体系、新范式

# 评分标准

- **5 分**：重大新能力/范式变化（如新增 structured output）
- **4 分**：重要功能增强
- **3 分**：有意义的功能迭代
- **2 分**：小幅改进
- **1 分**：细节优化

# 待分析事件

分析日期：{{ date }}
事件数量：{{ candidates|length }}

{% for event in candidates %}
## [{{ loop.index }}] {{ event.title }}

- **类型**: {{ event.type }}
- **仓库**: {{ event.repo }}
- **作者**: {{ event.author }}
- **时间**: {{ event.created_at }}

### 描述

{{ event.body }}

### 变更摘要

{{ event.diff_summary }}

### 来源

{{ event.url }}

{% endfor %}

# 输出要求

- 每天输出 5-15 条高质量信号
- 优先选择影响大的事件
- why_it_matters 用 1-2 句话解释价值
- 所有来源必须来自输入事件
- 避免重复和低价值信号
""")

def build_analysis_prompt(candidates: list[dict], date: str | None = None) -> str:
    """构建分析 prompt"""
    from datetime import datetime

    date = date or datetime.now().strftime("%Y-%m-%d")
    return ANALYSIS_PROMPT_TEMPLATE.render(
        date=date,
        candidates=candidates,
    )
```

### 5.6 报告渲染（Jinja2）

```python
# src/trendpluse/pipeline/render.py
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..config import settings
from ..logger import logger
from ..models.signal import DailyReport

class ReportRenderer:
    """Markdown 报告渲染器"""

    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(),
        )
        self.template = self.env.get_template("daily_report.md.j2")

    def render(self, report: DailyReport, date: str | None = None) -> str:
        """渲染 Markdown 报告"""
        date = date or datetime.now().strftime("%Y-%m-%d")
        return self.template.render(
            date=date,
            report=report,
        )

    def save(self, report: DailyReport, date: str | None = None) -> Path:
        """保存报告到文件"""
        date = date or datetime.now().strftime("%Y-%m-%d")
        output_dir = Path(settings.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # 渲染 Markdown
        markdown = self.render(report, date)

        # 保存 Markdown
        md_path = output_dir / f"{date}.md"
        md_path.write_text(markdown, encoding="utf-8")
        logger.info(f"Saved markdown report to {md_path}")

        # 保存 JSON
        import json
        json_path = output_dir / f"{date}.json"
        json_path.write_text(
            report.model_dump_json(indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        logger.info(f"Saved JSON report to {json_path}")

        return md_path
```

### 5.7 重试机制（tenacity）

```python
# src/trendpluse/utils/retry.py
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from ..logger import logger

def custom_retry(fn):
    """自定义重试装饰器"""

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError)),
        before_sleep=lambda _: logger.warning("Retrying due to error..."),
    )
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper
```

---

## 六、Pipeline 主流程

```python
# src/trendpluse/pipeline/__init__.py
from datetime import datetime
from pathlib import Path

from ..github.client import GitHubClient
from ..analyzer.claude import ClaudeAnalyzer
from ..config import settings
from ..logger import logger
from .filter import filter_candidates
from .render import ReportRenderer

async def run_daily_pipeline(date: str | None = None) -> Path:
    """执行每日分析流程"""

    date = date or datetime.now().strftime("%Y-%m-%d")
    logger.info(f"[bold]Starting TrendPulse pipeline for {date}[/bold]")

    # 幂等性检查
    report_path = Path(settings.output_dir) / f"{date}.md"
    if report_path.exists():
        logger.warning(f"Report for {date} already exists, skipping")
        return report_path

    # Stage 1: Fetch
    logger.info("Stage 1: Fetching from GitHub...")
    github_client = GitHubClient()
    events = github_client.get_events(days=settings.days_to_lookback)
    logger.info(f"Found {len(events)} total events")

    # Stage 2: Filter
    logger.info("Stage 2: Filtering candidates...")
    candidates = filter_candidates(
        events,
        labels=settings.candidate_labels,
        max_count=settings.max_candidates,
    )
    logger.info(f"Filtered to {len(candidates)} candidates")

    # Stage 3: Analyze
    logger.info("Stage 3: Analyzing with Claude...")
    analyzer = ClaudeAnalyzer()

    # Token 预算检查
    estimated_tokens = analyzer.estimate_tokens(candidates)
    if estimated_tokens > settings.daily_token_budget:
        logger.warning(
            f"Estimated tokens ({estimated_tokens}) exceed budget "
            f"({settings.daily_token_budget}), using fallback"
        )
        # TODO: 实现降级逻辑

    report = analyzer.analyze(candidates)

    # Stage 4: Render
    logger.info("Stage 4: Rendering report...")
    renderer = ReportRenderer()
    output_path = renderer.save(report, date)

    logger.info(f"[bold green]Pipeline completed![/bold green] Report: {output_path}")
    return output_path
```

---

## 七、本地测试模式

### 7.1 Mock 数据生成

```python
# scripts/mock_data.py
from datetime import datetime, timedelta
from ..trendpluse.github.models import PullRequestEvent

def generate_mock_events(count: int = 10) -> list[PullRequestEvent]:
    """生成模拟事件用于本地测试"""

    events = []
    for i in range(count):
        events.append(
            PullRequestEvent(
                number=100 + i,
                title=f"Mock PR #{i}",
                body=f"This is a mock pull request for testing.",
                state="merged",
                merged_at=(datetime.now() - timedelta(hours=i)).isoformat(),
                author="test-user",
                labels=["feature", "enhancement"],
                url=f"https://github.com/test/repo/pull/{100+i}",
                diff_summary="- src/test.py: modified (+10, -5)",
            )
        )

    return events
```

### 5.2 本地运行命令

```bash
# 使用 uv 运行
uv run python -m trendpluse.main --date 2026-01-02

# 使用 mock 数据（不调用 API）
uv run python -m trendpluse.main --mock

# 预览报告
uv run mkdocs serve
```

---

## 八、Makefile

```makefile
# Makefile
.PHONY: install check format test run clean

install:
	uv sync

dev:
	uv sync --extra dev --extra docs

check:
	uv run ruff check src tests
	uv run mypy src

format:
	uv run ruff format src tests

test:
	uv run pytest tests/ -v

test-cov:
	uv run pytest tests/ --cov=src/trendpluse --cov-report=html

run:
	uv run python -m trendpluse.main

mock:
	uv run python -m trendpluse.main --mock

docs:
	uv run mkdocs build

docs-serve:
	uv run mkdocs serve

clean:
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov logs
```

---

## 九、改进总结

### 9.1 相比原方案的改进

| 方面 | 原方案 | 新方案 |
|------|--------|--------|
| **结构化输出** | Beta API（不稳定） | instructor（稳定可靠） |
| **重试机制** | 未实现 | tenacity 装饰器 |
| **日志系统** | 未实现 | rich + logging |
| **配置管理** | pydantic-settings（一致） | ✅ |
| **模板引擎** | 未实现 | Jinja2 |
| **GitHub 客户端** | 未实现 | PyGithub |
| **测试支持** | 未实现 | pytest + mock |
| **包管理** | requirements.txt | uv + pyproject.toml |

### 9.2 新增功能

1. ✅ **幂等性保障**：检查报告是否已存在
2. ✅ **Token 预算检查**：分析前估算成本
3. ✅ **本地测试模式**：mock 数据，不消耗 API
4. ✅ **完善的重试机制**：tenacity 装饰器
5. ✅ **Rich 日志系统**：美观的终端输出
6. ✅ **模板化管理**：Prompt 和报告都用 Jinja2

---

## 十、快速开始

```bash
# 1. 克隆项目
git clone https://github.com/yourname/trendpluse.git
cd trendpluse

# 2. 使用 uv 安装
uv sync --extra dev --extra docs

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API keys

# 4. 本地测试（使用 mock 数据）
uv run python -m trendpluse.main --mock

# 5. 运行真实流程
uv run python -m trendpluse.main

# 6. 预览报告
uv run mkdocs serve
```

---

## 十一、依赖版本锁定

使用 uv 自动生成 `uv.lock`，确保可重现构建：

```bash
uv lock
```

这将锁定所有传递依赖的精确版本，保证 CI/CD 环境与本地一致。
