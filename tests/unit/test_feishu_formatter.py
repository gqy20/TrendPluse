"""Feishu 格式化器单元测试"""

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleaseInfo,
    ReleasesData,
    RepoActivity,
    Signal,
)


class TestFeishuFormatter:
    """测试 FeishuFormatter 对 DailyReport 的格式化"""

    def test_format_card_with_structured_data(self):
        """测试：使用结构化数据生成飞书卡片"""
        # Arrange
        # 这个测试会失败，因为 FeishuFormatter 类还不存在
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        activity = ActivityData(
            total_commits=100,
            active_repos_count=5,
            new_contributors=2,
            top_repos=[
                RepoActivity(
                    repo="owner/repo1",
                    commits=50,
                    new_contributors=1,
                    top_contributors=[],
                ),
                RepoActivity(
                    repo="owner/repo2",
                    commits=30,
                    new_contributors=0,
                    top_contributors=[],
                ),
                RepoActivity(
                    repo="owner/repo3",
                    commits=20,
                    new_contributors=1,
                    top_contributors=[],
                ),
            ],
        )

        releases = ReleasesData(
            total_count=2,
            unique_repos_count=1,
            releases=[
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.0.0",
                    author="user1",
                    date="2026-01-04",
                    summary="Test release 1",
                    assets_count=5,
                    url="https://github.com/owner/repo/releases/tag/v1.0.0",
                ),
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.1.0",
                    author="user2",
                    date="2026-01-05",
                    summary="Test release 2",
                    assets_count=3,
                    url="https://github.com/owner/repo/releases/tag/v1.1.0",
                ),
            ],
        )

        signals = [
            Signal(
                id="sig-1",
                title="Test Signal 1",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="Important test signal",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="sig-2",
                title="Test Signal 2",
                type="safety",
                category="engineering",
                impact_score=4,
                why_it_matters="Security improvement",
                sources=["https://github.com/test/repo/pull/2"],
                related_repos=["test/repo"],
            ),
        ]

        report = DailyReport(
            date="2026-01-04",
            summary_brief="今日发现了 2 个高影响趋势信号。",
            engineering_signals=signals,
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            activity=activity,
            releases=releases,
            stats={
                "total_prs_analyzed": 10,
                "total_releases": 2,
                "high_impact_signals": 2,
                "total_commits_analyzed": 100,
            },
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        assert card["msg_type"] == "interactive"
        assert "card" in card
        assert "header" in card["card"]
        assert "elements" in card["card"]

        # 验证标题
        assert (
            card["card"]["header"]["title"]["content"]
            == "📊 TrendPulse 每日报告 - 2026-01-04"
        )

        # 验证摘要元素
        elements = card["card"]["elements"]
        assert any(
            "今日发现了 2 个高影响趋势信号" in el.get("text", {}).get("content", "")
            for el in elements
        )

        # 验证高影响信号
        assert any("🚀" in el.get("text", {}).get("content", "") for el in elements)

        # 验证版本发布
        assert any("v1.0.0" in el.get("text", {}).get("content", "") for el in elements)

        # 验证活跃仓库
        assert any(
            "owner/repo1" in el.get("text", {}).get("content", "") for el in elements
        )

        # 验证统计信息
        assert any("10" in el.get("text", {}).get("content", "") for el in elements)

    def test_format_card_with_minimal_data(self):
        """测试：最小数据集也能生成有效卡片"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        report = DailyReport(
            date="2026-01-04",
            summary_brief="今日暂无信号。",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            stats={
                "total_prs_analyzed": 0,
                "total_releases": 0,
                "high_impact_signals": 0,
                "total_commits_analyzed": 0,
            },
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        assert card["msg_type"] == "interactive"
        assert "card" in card
        assert len(card["card"]["elements"]) > 0

    def test_format_card_includes_top_repos(self):
        """测试：卡片包含 TOP 3 活跃仓库"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        activity = ActivityData(
            total_commits=150,
            active_repos_count=3,
            new_contributors=1,
            top_repos=[
                RepoActivity(
                    repo="owner/repo1",
                    commits=80,
                    new_contributors=1,
                    top_contributors=[],
                ),
                RepoActivity(
                    repo="owner/repo2",
                    commits=50,
                    new_contributors=0,
                    top_contributors=[],
                ),
                RepoActivity(
                    repo="owner/repo3",
                    commits=20,
                    new_contributors=0,
                    top_contributors=[],
                ),
            ],
        )

        report = DailyReport(
            date="2026-01-04",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            activity=activity,
            stats={
                "total_prs_analyzed": 0,
                "total_releases": 0,
                "high_impact_signals": 0,
                "total_commits_analyzed": 150,
            },
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        elements = card["card"]["elements"]
        content_parts = [
            el.get("text", {}).get("content", "")
            for el in elements
            if el.get("tag") == "div"
        ]

        # 验证包含 TOP 3 仓库
        combined_content = " ".join(content_parts)
        assert "owner/repo1" in combined_content
        assert "owner/repo2" in combined_content
        assert "owner/repo3" in combined_content
