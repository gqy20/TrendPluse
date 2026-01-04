"""TrendAnalyzer 跨类型聚合测试

测试重构后的行为：
1. TrendAnalyzer 可以同时处理 PR/Commit/Release 信号
2. 能够识别跨类型的模式并生成高层次趋势
3. 生成的趋势信号包含多个来源
"""

from unittest.mock import MagicMock, patch

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import Signal


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
        with patch.object(analyzer.client.chat.completions, "create") as mock_create:
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
            mock_create.return_value = mock_response

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
        with patch.object(analyzer.client.chat.completions, "create") as mock_create:
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
            mock_create.return_value = mock_response

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
