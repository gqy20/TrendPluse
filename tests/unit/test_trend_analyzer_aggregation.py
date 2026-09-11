"""TrendAnalyzer 跨类型聚合测试

测试重构后的行为：
1. TrendAnalyzer 可以同时处理 PR/Commit/Release 信号
2. 能够识别跨类型的模式并生成高层次趋势
3. 生成的趋势信号包含多个来源
"""

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import Signal
from trendpluse.models.source import AnalysisMaterial


class TestTrendAnalyzerCrossTypeAggregation:
    """测试 TrendAnalyzer 跨类型聚合功能"""

    def test_aggregates_pr_commit_and_release_signals(self):
        """测试：能够聚合 PR、Commit、Release 三种信号类型"""
        # Arrange
        analyzer = TrendAnalyzer(
            api_key="test-key",
        )

        # 模拟三种类型的信号
        pr_signals = [
            Signal(
                id="pr-1",
                title="Claude Code 新增 Agent 协作功能",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="支持多 Agent 并行任务",
                sources=["https://github.com/anthropic/claude-code/pull/123"],
                related_repos=["anthropic/claude-code"],
            )
        ]

        commit_signals = [
            Signal(
                id="commit-1",
                title="Cline 添加 Agent 记忆管理",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="改进上下文保持",
                sources=["https://github.com/cline/cline/commit/abc123"],
                related_repos=["cline/cline"],
            ),
            Signal(
                id="commit-2",
                title="Swarm 增加 Agent 示例",
                type="capability",
                category="engineering",
                impact_score=3,
                why_it_matters="提供更多参考实现",
                sources=["https://github.com/openai/swarm/commit/def456"],
                related_repos=["openai/swarm"],
            ),
        ]

        release_signals = [
            Signal(
                id="release-1",
                title="AutoGPT v0.5 发布",
                type="release",
                category="engineering",
                impact_score=5,
                why_it_matters="重要版本更新",
                sources=[
                    "https://github.com/significant-gravitas/autogpt/releases/tag/v0.5.0"
                ],
                related_repos=["significant-gravitas/autogpt"],
            )
        ]

        # Act
        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_response = MagicMock()
            mock_response.date = "2026-01-04"
            mock_response.summary_brief = "今日 AI Agent 领域有 5 个重要更新"
            mock_response.engineering_signals = [
                Signal(
                    id="trend-1",
                    title="AI Agent 工具链快速演进",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="多个主流 Agent 项目同时更新",
                    sources=[
                        "https://github.com/anthropic/claude-code/pull/123",
                        "https://github.com/cline/cline/commit/abc123",
                        "https://github.com/openai/swarm/commit/def456",
                        "https://github.com/significant-gravitas/autogpt/releases/tag/v0.5.0",
                    ],
                    related_repos=[
                        "anthropic/claude-code",
                        "cline/cline",
                        "openai/swarm",
                        "significant-gravitas/autogpt",
                    ],
                )
            ]
            mock_response.research_signals = []
            mock_response.commit_signals = []
            mock_response.stats = {
                "total_prs_analyzed": 1,
                "high_impact_signals": 1,
            }
            mock_create.return_value = (
                mock_response,
                SimpleNamespace(usage=None, model=None),
            )

            report = analyzer.aggregate_and_generate_report(
                pr_signals=pr_signals,
                commit_signals=commit_signals,
                release_signals=release_signals,
                date="2026-01-04",
            )

        # Assert
        assert report.date == "2026-01-04"
        assert len(report.engineering_signals) == 1

        # 验证聚合后的信号包含多个来源
        trend = report.engineering_signals[0]
        assert trend.title == "AI Agent 工具链快速演进"
        assert len(trend.sources) == 4
        assert "claude-code/pull/123" in trend.sources[0]
        assert "cline/cline/commit/abc123" in trend.sources[1]
        assert "swarm/commit/def456" in trend.sources[2]
        assert "autogpt/releases/tag/v0.5.0" in trend.sources[3]

    def test_method_exists_and_accepts_three_signal_types(self):
        """测试：新方法存在且接受三种信号类型"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        # Act & Assert - 方法应该存在
        assert hasattr(analyzer, "aggregate_and_generate_report")

        # 方法签名应该接受这些参数
        import inspect

        sig = inspect.signature(analyzer.aggregate_and_generate_report)
        params = list(sig.parameters.keys())
        assert "pr_signals" in params
        assert "commit_signals" in params
        assert "release_signals" in params
        assert "date" in params

    def test_generates_trend_from_only_commit_signals(self):
        """测试：只有 commit 信号时也能生成趋势"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        commit_signals = [
            Signal(
                id="commit-1",
                title="项目 A 添加功能 X",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/a/repo/commit/123"],
                related_repos=["a/repo"],
            ),
            Signal(
                id="commit-2",
                title="项目 B 添加功能 X",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/b/repo/commit/456"],
                related_repos=["b/repo"],
            ),
        ]

        # Mock LLM 响应
        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_response = MagicMock()
            mock_response.date = "2026-01-04"
            mock_response.summary_brief = "多项目采用相似功能"
            mock_response.engineering_signals = [
                Signal(
                    id="trend-1",
                    title="功能 X 被多个项目采用",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="跨项目采用",
                    sources=[
                        "https://github.com/a/repo/commit/123",
                        "https://github.com/b/repo/commit/456",
                    ],
                    related_repos=["a/repo", "b/repo"],
                )
            ]
            mock_response.research_signals = []
            mock_response.commit_signals = []
            mock_response.stats = {}
            mock_create.return_value = (
                mock_response,
                SimpleNamespace(usage=None, model=None),
            )

            # Act
            report = analyzer.aggregate_and_generate_report(
                pr_signals=[],
                commit_signals=commit_signals,
                release_signals=[],
                date="2026-01-04",
            )

        # Assert
        assert len(report.engineering_signals) == 1
        assert len(report.engineering_signals[0].sources) == 2


class TestResearchSignalAggregation:
    """research 信号聚合与强一致性回填测试"""

    def test_research_signal_sources_resolved_from_ids(self):
        """research 趋势的 sources 也必须被强一致性机制回填。"""
        analyzer = TrendAnalyzer(api_key="test-key")

        pr_signals = [
            Signal(
                id="pr-0",
                title="实现新注意力机制的论文代码",
                type="capability",
                category="research",
                impact_score=4,
                why_it_matters="论文实现",
                sources=["https://github.com/owner/repo/pull/42"],
                related_repos=["owner/repo"],
            )
        ]

        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_response = MagicMock()
            mock_response.date = "2026-01-04"
            mock_response.summary_brief = "研究趋势"
            mock_response.engineering_signals = []
            # LLM 返回的 research 趋势：带 source_signal_ids 但 sources 为空
            mock_response.research_signals = [
                Signal(
                    id="research-trend-1",
                    title="新注意力机制落地",
                    type="capability",
                    category="research",
                    impact_score=4,
                    why_it_matters="多篇实现指向同一机制",
                    sources=[],
                    related_repos=[],
                    source_signal_ids=["pr-0"],
                )
            ]
            mock_response.commit_signals = []
            mock_response.stats = {}
            mock_create.return_value = (
                mock_response,
                SimpleNamespace(usage=None, model=None),
            )

            report = analyzer.aggregate_and_generate_report(
                pr_signals=pr_signals,
                commit_signals=[],
                release_signals=[],
                date="2026-01-04",
            )

        assert len(report.research_signals) == 1
        trend = report.research_signals[0]
        assert trend.sources == ["https://github.com/owner/repo/pull/42"]
        assert trend.related_repos == ["owner/repo"]

    def test_aggregation_prompt_requires_research_aggregation(self):
        """聚合 prompt 必须要求保留 research 信号，禁止"可为空"暗示。"""
        analyzer = TrendAnalyzer(api_key="test-key")
        prompt = analyzer._build_aggregation_prompt(
            date="2026-01-04",
            pr_signals=[],
            commit_signals=[],
            release_signals=[],
        )
        assert "目前可为空" not in prompt
        assert "存在 research 信号时必须聚合，不得丢弃" in prompt

    def test_category_criteria_present_in_extraction_prompts(self):
        """上游提取 prompt 必须包含 category 判定标准。"""
        analyzer = TrendAnalyzer(api_key="test-key")
        pr_prompt = analyzer._build_material_prompt(
            AnalysisMaterial.from_pr_details(
                {
                    "repo_name": "owner/repo",
                    "number": 1,
                    "title": "t",
                    "body": "b",
                }
            )
        )
        assert "category 判定标准" in pr_prompt
        assert "防止过度分类" in pr_prompt

    def test_dangling_source_signal_ids_removed(self):
        """悬空 ID（LLM 幻觉）必须从 source_signal_ids 剔除，不进前端与历史索引。"""
        analyzer = TrendAnalyzer(api_key="test-key")

        pr_signals = [
            Signal(
                id="pr-0",
                title="真实信号",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="真实存在",
                sources=["https://github.com/owner/repo/pull/1"],
                related_repos=["owner/repo"],
            )
        ]

        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_response = MagicMock()
            mock_response.date = "2026-01-04"
            mock_response.summary_brief = "总览"
            mock_response.engineering_signals = [
                Signal(
                    id="trend-1",
                    title="趋势",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="混合引用",
                    sources=[],
                    related_repos=[],
                    # pr-0 真实存在，pr-418 是 LLM 幻觉
                    source_signal_ids=["pr-0", "pr-418"],
                )
            ]
            mock_response.research_signals = []
            mock_response.commit_signals = []
            mock_response.stats = {}
            mock_create.return_value = (
                mock_response,
                SimpleNamespace(usage=None, model=None),
            )

            report = analyzer.aggregate_and_generate_report(
                pr_signals=pr_signals,
                commit_signals=[],
                release_signals=[],
                date="2026-01-04",
            )

        trend = report.engineering_signals[0]
        assert trend.source_signal_ids == ["pr-0"]
        assert trend.sources == ["https://github.com/owner/repo/pull/1"]

    def test_all_dangling_source_signal_ids_emptied(self):
        """全部引用悬空时清空列表，sources 为空并告警，不产生脏引用。"""
        analyzer = TrendAnalyzer(api_key="test-key")

        with patch.object(
            analyzer.client.chat.completions, "create_with_completion"
        ) as mock_create:
            mock_response = MagicMock()
            mock_response.date = "2026-01-04"
            mock_response.summary_brief = "总览"
            mock_response.engineering_signals = [
                Signal(
                    id="trend-1",
                    title="纯幻觉趋势",
                    type="capability",
                    category="engineering",
                    impact_score=4,
                    why_it_matters="全部悬空",
                    sources=[],
                    related_repos=[],
                    source_signal_ids=["pr-999", "commit-888"],
                )
            ]
            mock_response.research_signals = []
            mock_response.commit_signals = []
            mock_response.stats = {}
            mock_create.return_value = (
                mock_response,
                SimpleNamespace(usage=None, model=None),
            )

            report = analyzer.aggregate_and_generate_report(
                pr_signals=[],
                commit_signals=[],
                release_signals=[],
                date="2026-01-04",
            )

        trend = report.engineering_signals[0]
        assert trend.source_signal_ids == []
        assert trend.sources == []
