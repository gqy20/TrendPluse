# Issue #37 技术方案设计文档

> **功能**: 自动发现并添加热门项目到监控列表
> **Issue**: [#37](https://github.com/gqy20/TrendPluse/issues/37)
> **创建日期**: 2026-01-31
> **预计工作量**: 6-7 小时
> **状态**: 历史方案文档，当前仓库实现已演进，结构以 `src/trendpluse/app/discovery.py`、`src/trendpluse/cli/discover_projects.py` 和 `src/trendpluse/discovery/` 实际代码为准

---

## 目录

- [一、背景与需求](#section-1-background)
- [二、技术方案概述](#section-2-solution)
- [三、数据源分析](#section-3-data-sources)
- [四、文件结构设计](#section-4-file-structure)
- [五、核心数据模型](#section-5-data-models)
- [六、质量评分算法](#section-6-scoring)
- [七、模块实现细节](#section-7-implementation)
- [八、代码量评估](#section-8-estimation)
- [九、实施步骤](#section-9-rollout)
- [十、风险与缓解](#section-10-risks)

---

## 一、背景与需求 { #section-1-background }

### 1.1 问题陈述

当前项目监控的仓库列表（`config.py` 中的 `github_repos`）是静态配置的，缺乏动态发现热门项目的能力。随着 AI 领域快速发展，新项目层出不穷，静态列表容易遗漏有价值的追踪目标。

### 1.2 功能范围

#### P0（必须实现）

- [x] **Trending 采集器**：爬取 GitHub Trending 发现热门项目
- [x] **关键词发现器**：基于关键词搜索发现新项目
- [x] **项目质量评估**：评估项目活跃度、社区活跃度、质量分数
- [x] **去重与过滤**：合并多来源结果，过滤低质量项目

#### P1（期望实现）

- [ ] **相关项目发现**：从已监控项目的关联中发现新项目
- [ ] **自动 PR 生成**：为高质量候选项目自动创建 PR 建议添加
- [ ] **通知机制**：发现重要项目时发送飞书通知

#### P2（可选）

- [ ] **Star 增长榜**：发现近期 star 增长最快的项目
- [ ] **手动审核流程**：支持人工确认后再添加到监控
- [ ] **发现历史记录**：记录每次发现的结果，便于追溯

---

## 二、技术方案概述 { #section-2-solution }

### 2.1 核心架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Discovery Pipeline                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐         │
│  │  Trending    │───▶│  Keyword     │───▶│   Related    │         │
│  │  Collector   │    │  Searcher    │    │  Discoverer  │         │
│  └──────────────┘    └──────────────┘    └──────────────┘         │
│         │                   │                   │                  │
│         └───────────────────┴───────────────────┘                  │
│                             ▼                                       │
│                   ┌──────────────┐                                │
│                   │   Candidate  │                                │
│                   │     Pool     │                                │
│                   └──────────────┘                                │
│                             ▼                                       │
│                   ┌──────────────┐                                │
│                   │  Quality     │                                │
│                   │  Evaluator   │                                │
│                   └──────────────┘                                │
│                             ▼                                       │
│                   ┌──────────────┐                                │
│                   │   Deduplic-  │                                │
│                   │    ator      │                                │
│                   └──────────────┘                                │
│                             ▼                                       │
│                   ┌──────────────┐                                │
│                   │   Report     │                                │
│                   │  Generator   │                                │
│                   └──────────────┘                                │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 数据流

```
GitHub API / Trending
        │
        ▼
  ┌──────────┐
  │ Collector │ ──▶ Raw Repository Data
  └──────────┘
        │
        ▼
  ┌──────────┐
  │Evaluator │ ──▶ Scored Projects (0-100)
  └──────────┘
        │
        ▼
  ┌──────────┐
  │Deduplic  │ ──▶ Unique Projects
  └──────────┘
        │
        ▼
  ┌──────────┐
  │ Reporter  │ ──▶ Markdown + JSON Report
  └──────────┘
```

---

## 三、数据源分析 { #section-3-data-sources }

### 3.1 GitHub Trending 方案对比

| 方案 | 优点 | 缺点 | 推荐度 |
|------|------|------|--------|
| **爬取 `github.com/trending`** | 数据完整、实时 | 需要解析 HTML、易变 | ⭐⭐⭐ |
| `github-trending-api` (第三方) | 有现成封装 | 依赖外部服务 | ⭐⭐ |
| **GitHub Search API** | 官方稳定、无反爬 | 无 Trending 排序 | ⭐⭐⭐⭐ |

**推荐方案**：使用 **GitHub Search API** 组合搜索条件模拟 Trending

### 3.2 核心查询示例

```python
# 模拟 Trending 查询
search_params = {
    "q": "language:python stars:>1000 pushed:2026-01-24",  # 7天内活跃
    "sort": "stars",
    "order": "desc",
    "per_page": 100
}
```

### 3.3 关键词搜索

```python
KEYWORDS = [
    "AI agent", "LLM", "Claude", "RAG", "vector database",
    "autonomous", "agents", "multi-agent"
]

# 组合搜索
q = f"language:python {keyword} stars:>500 pushed:>2026-01-01"
```

### 3.4 相关项目发现

- 从已监控项目的 `stargazers` 发现重叠
- 从项目的 `topics` 标签发现相似项目
- 从项目的 `contributors` 发现其他项目

---

## 四、文件结构设计 { #section-4-file-structure }

> 以下结构为设计阶段方案，包含已删除或已重组的路径（例如 `scripts/discover_projects.py`、`discovery/base.py`）。请勿将本节视为当前代码结构。

```
src/trendpluse/
├── discovery/                    # 新增模块
│   ├── __init__.py              # 公共 API 导出
│   ├── base.py                  # BaseDiscoverer 基类
│   ├── trending.py              # TrendingCollector
│   ├── keyword_searcher.py      # KeywordSearcher
│   ├── related_discoverer.py    # RelatedDiscoverer
│   ├── evaluator.py             # QualityEvaluator
│   ├── deduplicator.py          # Deduplicator
│   └── reporter.py              # DiscoveryReporter
├── models/
│   └── discovery.py             # 新增数据模型
├── config.py                    # 扩展 DiscoveryConfig
│
scripts/
├── discover_projects.py         # 发现脚本入口
│
data/
└── discovery/                   # 发现记录存储
    ├── candidates/              # 候选项目缓存
    └── reports/                 # 发现报告
│
tests/
├── test_discovery_base.py
├── test_discovery_trending.py
├── test_discovery_evaluator.py
├── test_discovery_deduplicator.py
├── test_discovery_reporter.py
└── test_discovery_integration.py
│
.github/workflows/
└── discover-projects.yml        # 定时发现 CI
```

---

## 五、核心数据模型 { #section-5-data-models }

### 5.1 DiscoveredProject

```python
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal

class DiscoveredProject(BaseModel):
    """发现的热门项目"""

    # 基本信息
    repo: str = Field(description="仓库名称 owner/repo")
    name: str = Field(description="项目名称")
    description: str = Field(description="项目描述")
    stars: int = Field(description="当前 star 数", ge=0)

    # 增长指标
    stars_growth_7d: int = Field(default=0, description="7天增长")
    stars_growth_30d: int = Field(default=0, description="30天增长")

    # 技术信息
    language: str = Field(description="主要语言")
    topics: list[str] = Field(default_factory=list, description="主题标签")
    license: str | None = Field(default=None, description="许可证")

    # 活跃度指标
    open_issues: int = Field(default=0, description="开放 Issue 数")
    forks: int = Field(default=0, description="Fork 数")
    watchers: int = Field(default=0, description="Watchers 数")
    last_commit_at: datetime | None = Field(default=None, description="最后提交时间")

    # 质量评估
    quality_score: float = Field(ge=0, le=100, description="质量评分 0-100")
    activity_level: Literal["high", "medium", "low"] = Field(default="medium")
    community_score: float = Field(ge=0, le=100, description="社区活跃度")

    # 发现元数据
    discovery_source: Literal["trending", "keyword", "related"] = Field(
        description="发现来源"
    )
    discovery_time: datetime = Field(default_factory=datetime.now)
    discovery_reason: str = Field(description="发现原因/关键词")

    # 推荐信息
    recommended: bool = Field(default=False, description="是否推荐添加")
    recommendation_priority: Literal["high", "medium", "low"] = Field(
        default="medium"
    )
```

### 5.2 DiscoveryReport

```python
class DiscoveryReport(BaseModel):
    """发现报告"""

    date: str = Field(description="报告日期 YYYY-MM-DD")
    total_discovered: int = Field(description="总发现数")
    passed_quality: int = Field(description="通过质量评估数")
    high_priority: int = Field(description="高优先级推荐数")
    candidates: list[DiscoveredProject] = Field(description="候选项目列表")

    # 去重信息
    duplicates_removed: int = Field(default=0, description="去重移除数")
    already_monitored: int = Field(default=0, description="已在监控列表数")

    # 来源统计
    source_breakdown: dict[str, int] = Field(
        default_factory=dict,
        description="各来源发现数量"
    )
```

### 5.3 DiscoveryConfig

```python
class DiscoveryConfig(BaseSettings):
    """项目发现配置"""

    # 发现开关
    enable_discovery: bool = Field(
        default=True,
        description="是否启用项目自动发现"
    )

    # Trending 配置
    trending_languages: list[str] = ["python", "typescript", "go"]
    trending_period_days: int = 7
    trending_min_stars: int = 1000

    # 关键词配置
    search_keywords: list[str] = Field(
        default=[
            "AI agent",
            "LLM",
            "Claude",
            "RAG",
            "vector database",
            "autonomous",
            "multi-agent",
        ]
    )
    keyword_min_stars: int = 500

    # 质量阈值
    min_quality_score: float = 60.0
    min_activity_days: int = 30  # 最后活跃天数阈值

    # 去重配置
    enable_deduplication: bool = True
    similarity_threshold: float = 0.8  # 相似度阈值

    # 输出配置
    discovery_output_dir: str = "data/discovery"
    discovery_retention_days: int = 90
```

---

## 六、质量评分算法 { #section-6-scoring }

### 6.1 评分维度

| 维度 | 权重 | 指标 |
|------|------|------|
| **Star 数量** | 20% | 对数曲线，10000+ 满分 |
| **活跃度** | 30% | 最后提交时间、commit 频率 |
| **社区健康度** | 20% | forks、contributors、issues |
| **代码质量** | 15% | license、README、文档 |
| **相关性** | 15% | topics 匹配、关键词匹配 |

### 6.2 评分算法

```python
def calculate_quality_score(
    project: dict,
    monitored_repos: list[str]
) -> float:
    """计算项目质量评分 (0-100)"""

    score = 0.0

    # 1. Star 分数 (对数曲线)
    stars = project.get("stargazers_count", 0)
    if stars >= 10000:
        score += 20
    elif stars >= 5000:
        score += 15
    elif stars >= 1000:
        score += 10
    elif stars >= 500:
        score += 5

    # 2. 活跃度 (30分)
    last_push = project.get("pushed_at")
    if last_push:
        from datetime import datetime, timedelta
        days_since = (datetime.now() - last_push).days
        if days_since <= 7:
            score += 30
        elif days_since <= 30:
            score += 20
        elif days_since <= 90:
            score += 10

    # 3. 社区健康度 (20分)
    forks = project.get("forks_count", 0)
    watchers = project.get("watchers_count", 0)
    open_issues = project.get("open_issues_count", 0)

    if forks >= 100:
        score += 10
    elif forks >= 50:
        score += 7
    elif forks >= 10:
        score += 4

    if watchers >= 50:
        score += 10
    elif watchers >= 20:
        score += 7
    elif watchers >= 5:
        score += 4

    # 4. 代码质量 (15分)
    if project.get("license"):
        score += 5
    if project.get("description"):
        score += 5
    if project.get("has_readme"):
        score += 5

    # 5. 相关性 (15分)
    topics = project.get("topics", [])
    relevant_topics = set(["agent", "ai", "llm", "rag", "claude"])
    if any(t.lower() in relevant_topics for t in topics):
        score += 15

    return min(score, 100.0)
```

---

## 七、模块实现细节 { #section-7-implementation }

### 7.1 BaseDiscoverer 基类

```python
# src/trendpluse/discovery/base.py

from abc import ABC, abstractmethod
from typing import List
from trendpluse.models.discovery import DiscoveredProject

class BaseDiscoverer(ABC):
    """发现器基类"""

    def __init__(self, github_token: str):
        self.github_token = github_token

    @abstractmethod
    def discover(self) -> List[DiscoveredProject]:
        """发现项目

        Returns:
            发现的项目列表
        """
        raise NotImplementedError
```

### 7.2 TrendingCollector

```python
# src/trendpluse/discovery/trending.py

from datetime import datetime, timedelta
from github import Github
from trendpluse.discovery.base import BaseDiscoverer
from trendpluse.models.discovery import DiscoveredProject

class TrendingCollector(BaseDiscoverer):
    """采集 GitHub Trending 项目"""

    def __init__(self, github_token: str):
        super().__init__(github_token)
        self.client = Github(github_token)

    def discover(
        self,
        languages: list[str] = None,
        days: int = 7
    ) -> list[DiscoveredProject]:
        """发现 Trending 项目

        Args:
            languages: 编程语言列表
            days: 回溯天数

        Returns:
            发现的项目列表
        """
        if languages is None:
            languages = ["python", "typescript", "go"]

        candidates = []
        since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        for lang in languages:
            query = f"language:{lang} stars:>1000 pushed:>={since}"

            repos = self.client.search_repositories(
                query=query,
                sort="stars",
                order="desc"
            )

            for repo in repos[:30]:
                project = self._convert_to_discovered(repo, "trending")
                candidates.append(project)

        return candidates

    def _convert_to_discovered(
        self,
        repo,
        source: str
    ) -> DiscoveredProject:
        """转换 GitHub Repository 对象"""
        return DiscoveredProject(
            repo=repo.full_name,
            name=repo.name,
            description=repo.description or "",
            stars=repo.stargazers_count,
            language=repo.language or "Unknown",
            topics=list(repo.get_topics()) if repo.topics else [],
            license=repo.license.name if repo.license else None,
            open_issues=repo.open_issues_count,
            forks=repo.forks_count,
            watchers=repo.watchers_count,
            last_commit_at=repo.pushed_at,
            discovery_source=source,
            discovery_reason=f"Trending in {repo.language}"
        )
```

### 7.3 QualityEvaluator

```python
# src/trendpluse/discovery/evaluator.py

from trendpluse.models.discovery import DiscoveredProject

class QualityEvaluator:
    """质量评估器"""

    def __init__(self, config: DiscoveryConfig):
        self.config = config

    def evaluate(
        self,
        candidates: list[DiscoveredProject]
    ) -> list[DiscoveredProject]:
        """批量评估项目质量

        Args:
            candidates: 候选项目列表

        Returns:
            评估后的项目列表（quality_score 已填充）
        """
        results = []
        for project in candidates:
            score = self._calculate_score(project)
            project.quality_score = score
            project.activity_level = self._get_activity_level(project)
            project.recommended = score >= self.config.min_quality_score

            # 设置推荐优先级
            if score >= 80:
                project.recommendation_priority = "high"
            elif score >= 60:
                project.recommendation_priority = "medium"
            else:
                project.recommendation_priority = "low"

            results.append(project)

        return results

    def _calculate_score(self, project: DiscoveredProject) -> float:
        """计算质量评分"""
        score = 0.0

        # Star 分数
        if project.stars >= 10000:
            score += 20
        elif project.stars >= 5000:
            score += 15
        elif project.stars >= 1000:
            score += 10
        elif project.stars >= 500:
            score += 5

        # 活跃度分数
        if project.last_commit_at:
            from datetime import datetime
            days_since = (datetime.now() - project.last_commit_at).days
            if days_since <= 7:
                score += 30
            elif days_since <= 30:
                score += 20
            elif days_since <= 90:
                score += 10

        # ... 其他维度

        return min(score, 100.0)

    def _get_activity_level(
        self,
        project: DiscoveredProject
    ) -> Literal["high", "medium", "low"]:
        """获取活跃度等级"""
        if project.last_commit_at:
            from datetime import datetime
            days_since = (datetime.now() - project.last_commit_at).days
            if days_since <= 7:
                return "high"
            elif days_since <= 30:
                return "medium"
        return "low"
```

### 7.4 DiscoveryReporter

```python
# src/trendpluse/discovery/reporter.py

from pathlib import Path
from datetime import datetime
from trendpluse.models.discovery import DiscoveryReport, DiscoveredProject

class DiscoveryReporter:
    """发现报告生成器"""

    def generate_markdown(
        self,
        report: DiscoveryReport
    ) -> str:
        """生成 Markdown 报告

        Args:
            report: 发现报告数据

        Returns:
            Markdown 格式报告
        """
        lines = [
            f"# 项目发现报告 ({report.date})\n",
            "## 发现概览\n",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| 总发现数 | {report.total_discovered} |",
            f"| 通过质量评估 | {report.passed_quality} |",
            f"| 高优先级 | {report.high_priority} |",
            f"| 去重移除 | {report.duplicates_removed} |",
            f"| 已在监控 | {report.already_monitored} |\n",
        ]

        # 高优先级推荐
        high_priority = [
            p for p in report.candidates
            if p.recommendation_priority == "high"
        ]

        if high_priority:
            lines.extend([
                "## 高优先级推荐\n",
            ])

            for i, project in enumerate(high_priority, 1):
                lines.extend([
                    f"### 🌟 {i}. {project.repo}",
                    f"**发现来源**: {project.discovery_source}  ",
                    f"**推荐理由**: {project.discovery_reason}  ",
                    f"**质量评分**: {project.quality_score:.0f}/100\n",
                    f"| 指标 | 数值 |",
                    f"|------|------|",
                    f"| Stars | {project.stars:,} |",
                    f"| 语言 | {project.language} |",
                    f"| 活跃度 | {project.activity_level} |",
                    f"| [查看项目](https://github.com/{project.repo})\n",
                ])

        # 所有候选项目
        lines.extend([
            "## 所有候选项目\n",
            "| 项目 | Stars | 语言 | 质量分 | 活跃度 |",
            "|------|-------|------|--------|--------|",
        ])

        for project in report.candidates:
            emoji = {"high": "🔥", "medium": "⚡", "low": "📌"}
            lines.append(
                f"| [{project.repo}]({project.repo}) "
                f"| {project.stars:,} "
                f"| {project.language} "
                f"| {project.quality_score:.0f} "
                f"| {emoji.get(project.activity_level, '📌')} |"
            )

        return "\n".join(lines)

    def save_report(
        self,
        report: DiscoveryReport,
        output_dir: str = "data/discovery/reports"
    ) -> str:
        """保存报告到文件

        Args:
            report: 发现报告
            output_dir: 输出目录

        Returns:
            保存的文件路径
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # 保存 Markdown
        md_content = self.generate_markdown(report)
        md_file = output_path / f"discovery-{report.date}.md"
        md_file.write_text(md_content, encoding="utf-8")

        # 保存 JSON
        import json
        json_file = output_path / f"discovery-{report.date}.json"
        json_file.write_text(
            json.dumps(report.model_dump(), indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        return str(md_file)
```

---

## 八、代码量评估 { #section-8-estimation }

### 8.1 源代码预估

| 模块 | 文件 | 预估行数 |
|------|------|----------|
| **数据模型** | `models/discovery.py` | **120** |
| **发现器基类** | `discovery/base.py` | **80** |
| **Trending 采集器** | `discovery/trending.py` | **180** |
| **关键词搜索器** | `discovery/keyword_searcher.py` | **150** |
| **相关项目发现器** | `discovery/related_discoverer.py` | **200** |
| **质量评估器** | `discovery/evaluator.py` | **250** |
| **去重器** | `discovery/deduplicator.py` | **120** |
| **报告生成器** | `discovery/reporter.py` | **180** |
| **模块导出** | `discovery/__init__.py` | **30** |
| **主入口脚本** | `trendpluse.cli.discover_projects` | **150** |
| **配置扩展** | `config.py` (追加) | **80** |
| **源代码小计** | | ****1,540 行*** | |

### 8.2 测试代码预估 (按 1.87:1 比例)

| 模块 | 文件 | 预估行数 |
|------|------|----------|
| **基类测试** | `tests/test_discovery_base.py` | **150** |
| **Trending 测试** | `tests/test_discovery_trending.py` | **340** |
| **评估器测试** | `tests/test_discovery_evaluator.py` | **470** |
| **去重器测试** | `tests/test_discovery_deduplicator.py` | **225** |
| **报告器测试** | `tests/test_discovery_reporter.py` | **340** |
| **集成测试** | `tests/test_discovery_integration.py` | **400** |
| **测试代码小计** | | ****1,925 行*** | |

### 8.3 总代码量汇总

```
┌─────────────────────────────────────────────────────────────┐
│                    代码量统计                                │
├─────────────────────────────────────────────────────────────┤
│  源代码:           1,540 行                                  │
│  测试代码:         1,925 行                                  │
│  配置/CI:             55 行                                  │
├─────────────────────────────────────────────────────────────┤
│  总计:             3,520 行                                  │
└─────────────────────────────────────────────────────────────┘
```

### 8.4 占现有项目比例

| 维度 | 现有项目 | 新增代码 | 占比 |
|------|----------|----------|------|
| 源代码 | 6,408 行 | 1,540 行 | **+24%** |
| 测试代码 | 12,019 行 | 1,925 行 | **+16%** |
| 总计 | 18,427 行 | 3,520 行 | **+19%** |

---

## 九、实施步骤 { #section-9-rollout }

### 9.1 Phase 1: 基础框架 (0.5h)

```bash
# 1. 创建模块结构
mkdir -p src/trendpluse/discovery data/discovery/{candidates,reports}

# 2. 创建测试文件
touch tests/unit/test_discovery_base.py

# 3. 实现数据模型
# - src/trendpluse/models/discovery.py
# - src/trendpluse/discovery/base.py
```

**任务清单**:
- [ ] 创建目录结构
- [ ] 实现 `DiscoveredProject` 模型
- [ ] 实现 `DiscoveryReport` 模型
- [ ] 实现 `DiscoveryConfig` 配置
- [ ] 实现 `BaseDiscoverer` 基类
- [ ] 编写基础测试

### 9.2 Phase 2: Trending 采集器 (1h)

```python
# src/trendpluse/discovery/trending.py

class TrendingCollector(BaseDiscoverer):
    """采集 GitHub Trending 项目"""

    def discover(
        self,
        languages: list[str] = None,
        days: int = 7
    ) -> list[DiscoveredProject]:
        # 实现逻辑
        pass
```

**任务清单**:
- [ ] 实现 `TrendingCollector.discover()`
- [ ] 实现 `_convert_to_discovered()`
- [ ] Mock GitHub API 测试
- [ ] 验证输出格式

### 9.3 Phase 3: 关键词搜索器 (1h)

**任务清单**:
- [ ] 实现 `KeywordSearcher`
- [ ] 多关键词并行搜索
- [ ] 结果聚合与去重
- [ ] 单元测试

### 9.4 Phase 4: 质量评估器 (1h)

**任务清单**:
- [ ] 实现 `QualityEvaluator`
- [ ] 多维度评分算法
- [ ] 活跃度等级判断
- [ ] 边界情况测试

### 9.5 Phase 5: 去重与报告 (1h)

**任务清单**:
- [ ] 实现 `Deduplicator`
- [ ] 实现 `DiscoveryReporter`
- [ ] Markdown 模板
- [ ] JSON 输出格式

### 9.6 Phase 6: 主脚本与 CI (0.5h)

**任务清单**:
- [ ] 实现 `trendpluse.cli.discover_projects`
- [ ] 创建 `.github/workflows/discover-projects.yml`
- [ ] 集成测试
- [ ] 文档更新

### 9.7 Phase 7: 测试完善 (2.5h)

**任务清单**:
- [ ] 补充单元测试
- [ ] 集成测试
- [ ] 边界测试
- [ ] 测试覆盖率 > 80%

---

## 十、风险与缓解 { #section-10-risks }

### 10.1 技术风险

| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|----------|
| GitHub API 限流 | 中 | 中 | 使用缓存、分页处理、重试机制 |
| 质量评分不准 | 高 | 中 | 人工抽检、阈值调整、A/B 测试 |
| 误添加低质项目 | 中 | 低 | 人工审核 PR、分级推荐 |
| 发现重复项目 | 低 | 低 | 多维度去重逻辑 |

### 10.2 运维风险

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 定时任务延迟 | 低 | 监控告警、手动触发 |
| 报告存储增长 | 中 | 定期清理、保留策略 |
| 错误报告生成 | 中 | 容错处理、降级方案 |

### 10.3 数据质量保障

```python
# 数据校验示例
from pydantic import validator

class DiscoveredProject(BaseModel):
    # ...

    @validator('stars')
    def validate_stars(cls, v):
        """确保 star 数非负"""
        if v < 0:
            raise ValueError('stars cannot be negative')
        return v

    @validator('quality_score')
    def validate_score(cls, v):
        """确保质量分在 0-100 范围内"""
        if not 0 <= v <= 100:
            raise ValueError('quality_score must be between 0 and 100')
        return v
```

---

## 十一、API 限制与成本

| 资源 | 限制 | 说明 |
|------|------|------|
| GitHub Search API | 30次/分钟 (认证) | 足够使用 |
| GraphQL API | 5000点/小时 | 高级查询 |
| 成本 | $0 | 完全免费 ✅ |

### 11.1 API 使用估算

```
单次发现流程:
- Trending 查询: 3 languages × 1 query = 3 次
- 关键词搜索: 7 keywords × 1 query = 7 次
- 项目详情: ~100 repos × 1 query = 100 次

总计: ~110 次/周
限额: 30次/分钟 × 60分钟 × 24小时 = 43,200 次/天

结论: 完全在限额内 ✅
```

---

## 十二、输出示例

### 12.1 发现报告 (Markdown)

```markdown
# 项目发现报告 (2026-01-31)

## 发现概览

| 指标 | 数值 |
|------|------|
| 总发现数 | 12 |
| 通过质量评估 | 8 |
| 高优先级 | 3 |
| 去重移除 | 2 |
| 已在监控 | 2 |

## 高优先级推荐

### 🌟 1. auto-gpt/next-gen-agent

**发现来源**: trending (Python)
**推荐理由**: 今日 Trending 第一，Star 增长 500+
**质量评分**: 85/100

| 指标 | 数值 |
|------|------|
| Stars | 12,500 |
| 语言 | Python |
| 活跃度 | high |

[查看项目](https://github.com/auto-gpt/next-gen-agent)

---

## 所有候选项目

| 项目 | Stars | 语言 | 质量分 | 活跃度 |
|------|-------|------|--------|--------|
| [auto-gpt/next-gen-agent](...) | 12,500 | Python | 85 | 🔥 |
| [anthropic/claude-cookbooks](...) | 8,200 | Python | 78 | 🔥 |
| ...
```

### 12.2 发现报告 (JSON)

```json
{
  "date": "2026-01-31",
  "total_discovered": 12,
  "passed_quality": 8,
  "high_priority": 3,
  "duplicates_removed": 2,
  "already_monitored": 2,
  "source_breakdown": {
    "trending": 6,
    "keyword": 4,
    "related": 2
  },
  "candidates": [
    {
      "repo": "auto-gpt/next-gen-agent",
      "name": "next-gen-agent",
      "description": "Next generation AI agent framework",
      "stars": 12500,
      "language": "Python",
      "quality_score": 85.0,
      "activity_level": "high",
      "recommendation_priority": "high",
      "discovery_source": "trending",
      "discovery_reason": "Trending in Python",
      ...
    }
  ]
}
```

---

## 十三、附录

### 13.1 参考项目

- [github-trending-api](https://github.com/huchenme/github-trending-api) - Trending API
- [gitpoap](https://gitpoap.io) - GitHub 项目发现

### 13.2 相关 Issues

- #38: Prometheus 指标和 LLM 成本追踪
- #39: Issue 分析功能
- #40: Discussions 分析功能
- #41: 安全漏洞追踪

### 13.3 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0 | 2026-01-31 | 初始版本 |

---

**文档状态**: ✅ 设计完成
**下一步**: 开始 Phase 1 实施
**负责人**: @gqy20
