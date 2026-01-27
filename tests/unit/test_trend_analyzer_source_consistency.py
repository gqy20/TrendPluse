"""TrendAnalyzer 强一致性测试 - source_signal_ids 机制

测试新的强一致性方案：
1. 聚合信号包含 source_signal_ids 字段
2. 后处理根据 IDs 解析正确的 sources
3. 确保 100% 一致性（不依赖 LLM 正确传递）
"""

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import DailyReport, Signal


class TestTrendAnalyzerSourceConsistency:
    """测试 TrendAnalyzer 的强一致性机制"""

    def test_format_signals_with_ids_includes_ids(self):
        """测试：_format_signals_with_ids 包含信号 ID"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        signals = [
            Signal(
                id="original-1",
                title="测试信号",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/test/repo/commit/abc123"],
                related_repos=["test/repo"],
            )
        ]

        # Act
        result = analyzer._format_signals_with_ids(signals, "commit")

        # Assert
        # 应该包含 [commit-0] ID 标记
        assert "[commit-0]" in result
        # 应该包含原始 sources
        assert "https://github.com/test/repo/commit/abc123" in result
        # 应该包含相关仓库
        assert "test/repo" in result

    def test_format_signals_with_ids_empty_list(self):
        """测试：空信号列表返回'无'"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        # Act
        result = analyzer._format_signals_with_ids([], "commit")

        # Assert
        assert result == "无"

    def test_resolve_sources_from_ids_preserves_all_sources(self):
        """测试：_resolve_sources_from_ids 保留所有原始 sources"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        # 创建原始信号映射
        signal_map: dict[str, Signal] = {
            "commit-0": Signal(
                id="commit-0",
                title="Commit 1",
                type="commit",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/a/repo/commit/abc123"],
                related_repos=["a/repo"],
            ),
            "commit-1": Signal(
                id="commit-1",
                title="Commit 2",
                type="commit",
                category="engineering",
                impact_score=3,
                why_it_matters="测试",
                sources=["https://github.com/b/repo/commit/def456"],
                related_repos=["b/repo"],
            ),
        }

        # 创建模拟报告（带 source_signal_ids）
        from trendpluse.models.signal import DailyReport

        mock_report = DailyReport(
            date="2026-01-04",
            summary_brief="测试报告",
            engineering_signals=[
                Signal(
                    id="trend-1",
                    title="聚合趋势",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="聚合信号",
                    sources=[],  # 初始为空，由后处理填充
                    related_repos=[],
                    # 新字段：source_signal_ids
                    source_signal_ids=["commit-0", "commit-1"],
                )
            ],
            stats={},
        )

        # Act
        resolved_report = analyzer._resolve_sources_from_ids(mock_report, signal_map)

        # Assert
        trend = resolved_report.engineering_signals[0]

        # 应该包含两个 commit 的 sources
        assert len(trend.sources) == 2
        assert "https://github.com/a/repo/commit/abc123" in trend.sources
        assert "https://github.com/b/repo/commit/def456" in trend.sources

        # 应该包含两个相关仓库
        assert len(trend.related_repos) == 2
        assert "a/repo" in trend.related_repos
        assert "b/repo" in trend.related_repos

    def test_resolve_sources_from_ids_handles_missing_id(self):
        """测试：_resolve_sources_from_ids 处理缺失的 ID"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        signal_map = {
            "commit-0": Signal(
                id="commit-0",
                title="Commit 1",
                type="commit",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/a/repo/commit/abc123"],
                related_repos=["a/repo"],
            ),
        }

        from trendpluse.models.signal import DailyReport

        mock_report = DailyReport(
            date="2026-01-04",
            summary_brief="测试报告",
            engineering_signals=[
                Signal(
                    id="trend-1",
                    title="聚合趋势",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="聚合信号",
                    sources=[],
                    related_repos=[],
                    # 引用了不存在的 ID
                    source_signal_ids=["commit-0", "commit-999"],
                )
            ],
            stats={},
        )

        # Act
        resolved_report = analyzer._resolve_sources_from_ids(mock_report, signal_map)

        # Assert
        trend = resolved_report.engineering_signals[0]

        # 应该只包含有效的 ID 的 sources
        assert len(trend.sources) == 1
        assert "https://github.com/a/repo/commit/abc123" in trend.sources

    def test_resolve_sources_from_ids_handles_empty_ids(self):
        """测试：_resolve_sources_from_ids 处理空的 ID 列表"""
        # Arrange
        analyzer = TrendAnalyzer(api_key="test-key")

        signal_map: dict[str, Signal] = {}

        from trendpluse.models.signal import DailyReport

        mock_report = DailyReport(
            date="2026-01-04",
            summary_brief="测试报告",
            engineering_signals=[
                Signal(
                    id="trend-1",
                    title="聚合趋势",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="聚合信号",
                    sources=["https://github.com/test/repo/pull/1"],  # LLM 返回的
                    related_repos=["test/repo"],
                    # 没有 source_signal_ids
                )
            ],
            stats={},
        )

        # Act
        resolved_report = analyzer._resolve_sources_from_ids(mock_report, signal_map)

        # Assert
        # 当没有 source_signal_ids 时，应该尝试验证 LLM 返回的 sources
        trend = resolved_report.engineering_signals[0]
        assert len(trend.sources) == 1

    def test_aggregate_and_generate_report_builds_signal_map(self):
        """测试：aggregate_and_generate_report 正确构建 signal_map"""
        # Arrange
        from unittest.mock import patch

        analyzer = TrendAnalyzer(api_key="test-key")

        pr_signals: list[Signal] = [
            Signal(
                id="pr-1",
                title="PR 信号",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )
        ]

        commit_signals: list[Signal] = [
            Signal(
                id="commit-1",
                title="Commit 信号",
                type="commit",
                category="engineering",
                impact_score=3,
                why_it_matters="测试",
                sources=["https://github.com/test/repo/commit/abc123"],
                related_repos=["test/repo"],
            )
        ]

        release_signals: list[Signal] = []

        # Mock LLM 响应，返回带有 source_signal_ids 的聚合信号
        mock_report = DailyReport(
            date="2026-01-05",
            summary_brief="测试聚合",
            engineering_signals=[
                Signal(
                    id="trend-1",
                    title="聚合趋势",
                    type="capability",
                    category="engineering",
                    impact_score=5,
                    why_it_matters="聚合信号",
                    sources=[],
                    related_repos=[],
                    source_signal_ids=["pr-0", "commit-0"],
                )
            ],
            stats={},
        )

        # Mock client.chat.completions.create 返回我们的 mock_report
        with patch.object(
            analyzer.client.chat.completions, "create", return_value=mock_report
        ):
            # Act
            result = analyzer.aggregate_and_generate_report(
                pr_signals=pr_signals,
                commit_signals=commit_signals,
                release_signals=release_signals,
                date="2026-01-05",
            )

        # Assert
        # 应该调用 LLM
        assert result.date == "2026-01-05"
        assert len(result.engineering_signals) == 1

        # 验证 sources 已通过后处理正确解析
        trend = result.engineering_signals[0]
        assert len(trend.sources) == 2
        assert "https://github.com/test/repo/pull/1" in trend.sources
        assert "https://github.com/test/repo/commit/abc123" in trend.sources

        # 验证 related_repos 也正确解析
        assert "test/repo" in trend.related_repos
