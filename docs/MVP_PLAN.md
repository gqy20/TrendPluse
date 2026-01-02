# TrendPulse MVP 技术方案

## 一、MVP 范围定义

### 1.1 核心目标（Must Have）

- ✅ 每日自动追踪 Anthropic GitHub 仓库更新
- ✅ 提取结构化的趋势信号（工程 + 研究）
- ✅ 生成可浏览的静态站点
- ✅ 历史数据归档

### 1.2 范围限制（MVP 不做）

- ❌ 周报聚合
- ❌ 趋势图表
- ❌ 自动发现新仓库
- ❌ 多组织扩展
- ❌ Agent SDK 复杂工作流

---

## 二、技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Actions Cron                      │
│                    (每天 00:00 UTC 运行)                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 1: Fetcher                                          │
│  - 拉取 GitHub PR/Release/Commit                           │
│  - 保存原始数据到 data/snapshots/                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 2: Preprocessor                                     │
│  - 筛选候选事件（merged PR + releases）                    │
│  - 抽取 diff/描述摘要                                      │
│  - Token 预算控制                                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 3: Analyzer (Anthropic Structured Outputs)          │
│  - 调用 Claude API 分析信号                                │
│  - 输出结构化 JSON                                        │
│  - 生成 Markdown 报告                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Stage 4: Docs Builder                                     │
│  - 生成 MkDocs 目录结构                                    │
│  - 更新导航索引                                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  GitHub Pages                                              │
│  - 自动部署                                                │
│  - 历史归档                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## 三、数据模型

### 3.1 输入：GitHub 事件

```python
# data/snapshots/2026-01-02/events.json
{
  "date": "2026-01-02",
  "repos": [
    {
      "name": "anthropics/anthropic-sdk-python",
      "events": [
        {
          "type": "pull_request",
          "number": 123,
          "title": "Add structured output support",
          "state": "merged",
          "merged_at": "2026-01-02T10:30:00Z",
          "labels": ["feature", "enhancement"],
          "author": "username",
          "body": "PR描述...",
          "diff_summary": "核心变更摘要（前500字符）",
          "url": "https://github.com/..."
        },
        {
          "type": "release",
          "tag_name": "v0.10.0",
          "name": "Stable Release",
          "body": "Release notes...",
          "url": "https://github.com/..."
        }
      ]
    }
  ]
}
```

### 3.2 输出：信号模型

```python
# models/signal.py
from pydantic import BaseModel, Field
from typing import List, Literal

class Signal(BaseModel):
    """单条趋势信号"""
    id: str = Field(description="唯一标识")
    title: str = Field(description="信号标题")
    type: Literal["capability", "abstraction", "workflow", "eval", "safety", "performance"]
    category: Literal["engineering", "research"]
    impact_score: int = Field(ge=1, le=5, description="影响评分 1-5")
    why_it_matters: str = Field(description="1-2句话说明重要性")
    sources: List[str] = Field(description="PR/Release链接")
    related_repos: List[str] = Field(description="相关仓库名称")

class DailyReport(BaseModel):
    """每日分析报告"""
    date: str
    summary_brief: str = Field(description="当日总览（2-3句话）")
    engineering_signals: List[Signal]
    research_signals: List[Signal]
    stats: dict = Field(default_factory=lambda: {
        "total_prs_analyzed": 0,
        "total_releases": 0,
        "high_impact_signals": 0
    })
```

### 3.3 生成内容结构

```markdown
# docs/daily/2026-01-02.md

## Daily Brief

今日总览内容...

## Engineering Signals

### [5/5] Structured Output Support Added

**Why it matters**: 这使得...

**Sources**: [PR #123](...)

## Research Signals

...

## Raw Events

...
```

---

## 四、核心代码实现

### 4.1 目录结构

```
trendpulse/
├── .github/
│   └── workflows/
│       └── daily.yml          # GitHub Actions 配置
├── src/
│   ├── __init__.py
│   ├── config.py              # 配置管理
│   ├── models/
│   │   └── signal.py          # Pydantic 模型
│   ├── stages/
│   │   ├── fetcher.py         # Stage 1
│   │   ├── preprocessor.py    # Stage 2
│   │   ├── analyzer.py        # Stage 3
│   │   └── docs_builder.py    # Stage 4
│   ├── main.py                # Pipeline 入口
│   └── utils/
│       ├── github_api.py
│       └── claude_client.py
├── data/
│   ├── snapshots/             # 原始数据
│   └── processed/             # 处理后数据
├── reports/
│   └── daily/                 # JSON + Markdown 报告
├── docs/                      # MkDocs 源
├── mkdocs.yml
├── requirements.txt
└── README.md
```

### 4.2 配置管理

```python
# src/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # GitHub
    github_token: str
    repos: list[str] = [
        "anthropics/anthropic-sdk-python",
        "anthropics/claude-agent-sdk-python",
        "anthropics/evals",
    ]

    # Anthropic
    anthropic_api_key: str
    anthropic_model: str = "claude-sonnet-4-5"
    max_tokens_per_request: int = 8000

    # 筛选规则
    candidate_labels: list[str] = [
        "feature", "enhancement", "eval", "tooling",
        "agent", "workflow", "safety"
    ]
    max_candidates: int = 20

    # 成本控制
    daily_token_budget: int = 100_000

    class Config:
        env_file = ".env"

settings = Settings()
```

### 4.3 Stage 3: Analyzer（核心）

```python
# src/stages/analyzer.py
import json
from anthropic import Anthropic
from ..models.signal import DailyReport, Signal
from ..config import settings

class Analyzer:
    def __init__(self):
        self.client = Anthropic(api_key=settings.anthropic_api_key)

    def analyze(self, candidates: list[dict]) -> DailyReport:
        """分析候选事件，提取信号"""

        # 构建 prompt
        prompt = self._build_prompt(candidates)

        try:
            # 使用结构化输出
            response = self.client.beta.messages.parse(
                model=settings.anthropic_model,
                max_tokens=settings.max_tokens_per_request,
                betas=["structured-outputs-2025-11-13"],
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                output_format=DailyReport,
            )

            return response.parsed_output

        except Exception as e:
            # 降级：保存原始数据
            self._fallback_save(candidates, e)
            raise

    def _build_prompt(self, candidates: list[dict]) -> str:
        """构建分析 prompt"""
        return f"""你是 Anthropic 技术趋势分析专家。分析以下 GitHub 更新，提取趋势信号。

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

{json.dumps(candidates, ensure_ascii=False, indent=2)}

# 输出要求

- 每天输出 5-15 条高质量信号
- 优先选择影响大的事件
- why_it_matters 用 1-2 句话解释价值
- 所有来源必须来自输入事件
"""

    def _fallback_save(self, candidates: list[dict], error: Exception):
        """降级保存"""
        from datetime import datetime
        import os

        fallback_dir = "data/fallback"
        os.makedirs(fallback_dir, exist_ok=True)

        with open(f"{fallback_dir}/error_{datetime.now().isoformat()}.json", "w") as f:
            json.dump({
                "error": str(error),
                "candidates": candidates
            }, f, indent=2)
```

### 4.4 Pipeline 主流程

```python
# src/main.py
import asyncio
from datetime import datetime
from pathlib import Path

from .stages.fetcher import Fetcher
from .stages.preprocessor import Preprocessor
from .stages.analyzer import Analyzer
from .stages.docs_builder import DocsBuilder
from .utils.logger import get_logger

logger = get_logger(__name__)

async def run_pipeline(date: str = None):
    """执行每日分析流程"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    logger.info(f"Starting pipeline for {date}")

    # Stage 1: Fetch
    logger.info("Stage 1: Fetching from GitHub...")
    fetcher = Fetcher()
    raw_events = await fetcher.fetch_all()

    # Stage 2: Preprocess
    logger.info("Stage 2: Filtering candidates...")
    preprocessor = Preprocessor()
    candidates = preprocessor.filter_candidates(raw_events)

    logger.info(f"Found {len(candidates)} candidate events")

    # Stage 3: Analyze
    logger.info("Stage 3: Analyzing with Claude...")
    analyzer = Analyzer()
    try:
        report = analyzer.analyze(candidates)
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise

    # Stage 4: Build Docs
    logger.info("Stage 4: Building documentation...")
    builder = DocsBuilder()
    builder.build_daily(date, report)
    builder.update_index()

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    asyncio.run(run_pipeline())
```

### 4.5 GitHub Actions 配置

```yaml
# .github/workflows/daily.yml
name: Daily Trend Analysis

on:
  schedule:
    - cron: '0 0 * * *'  # 每天 00:00 UTC
  workflow_dispatch:      # 支持手动触发

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run pipeline
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          python -m src.main

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

---

## 五、成本估算

### 5.1 Token 消耗估算

| 项目 | 每日量 | 单价 | 月成本 |
|------|--------|------|--------|
| 输入 Tokens | ~30k | $3/MT | $2.7 |
| 输出 Tokens | ~10k | $15/MT | $4.5 |
| **总计** | **40k** | - | **~$7/月** |

### 5.2 成本控制措施

```python
# 1. 预算限制
MAX_TOKEN_BUDGET = 100_000  # 每天

# 2. 候选事件限制
MAX_CANDIDATES = 20  # 只分析前 20 个

# 3. Diff 抽样
DIFF_MAX_LENGTH = 2000  # 每个事件最多 2000 字符

# 4. 提前终止检查
if estimated_tokens > MAX_TOKEN_BUDGET:
    logger.warning("Token budget exceeded, using fallback")
    return generate_simple_report(candidates)
```

---

## 六、降级策略

### 6.1 三级降级

| 级别 | 触发条件 | 行为 |
|------|---------|------|
| **Level 1** | Claude API 超时 | 重试 1 次 |
| **Level 2** | 结构化输出失败 | 降级到普通 prompt + 手动解析 |
| **Level 3** | 完全失败 | 输出原始事件列表 |

### 6.2 降级代码

```python
def analyze_with_fallback(candidates):
    """带降级的分析"""

    # 尝试结构化输出
    try:
        return analyzer.analyze(candidates)
    except ValidationError:
        pass

    # Level 2: 普通 prompt
    try:
        response = client.messages.create(...)
        return parse_manually(response)
    except Exception:
        pass

    # Level 3: 原始输出
    return generate_raw_report(candidates)
```

---

## 七、开发里程碑

### Week 1: 基础设施
- [x] 项目结构搭建
- [ ] GitHub API 集成（Fetcher）
- [ ] 测试：能拉取并保存原始数据

### Week 2: 分析能力
- [ ] Preprocessor 实现
- [ ] Analyzer + 结构化输出
- [ ] 测试：能生成正确的 JSON

### Week 3: 站点生成
- [ ] Docs Builder + MkDocs
- [ ] GitHub Actions 配置
- [ ] 测试：能自动发布站点

### Week 4: 优化
- [ ] 成本优化
- [ ] 错误处理完善
- [ ] README 文档

---

## 八、监控与可观测性

### 8.1 关键指标

```python
# 每日记录
metrics = {
    "date": "2026-01-02",
    "input_tokens": 32547,
    "output_tokens": 8234,
    "cost_usd": 0.23,
    "candidates_analyzed": 18,
    "signals_extracted": 12,
    "pipeline_duration_sec": 45,
}
```

### 8.2 告警规则

- 成本超过 $10/天 → 告警
- 失败率 > 5% → 告警
- 信号数 < 3 或 > 30 → 检查质量

---

## 九、后续扩展（v1.1+）

- [ ] 周报聚合
- [ ] 信号去重与归因
- [ ] 趋势图表
- [ ] RSS 订阅
- [ ] 自动发现新仓库

---

## 十、快速开始

```bash
# 1. 克隆项目
git clone https://github.com/yourname/trendpulse.git
cd trendpulse

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API keys

# 4. 运行测试
python -m src.main --dry-run

# 5. 本地构建文档
mkdocs serve

# 6. 推送 GitHub，Actions 自动运行
git push
```
