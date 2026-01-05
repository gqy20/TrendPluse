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
        # JSON 2.0: elements 在 body 下
        assert "body" in card["card"]
        assert "elements" in card["card"]["body"]

        # 验证标题（header 不包含日期）
        assert card["card"]["header"]["title"]["content"] == "📊 TrendPulse 每日报告"

        # 验证 body 中的醒目日期标题
        elements = card["card"]["body"]["elements"]
        assert any(
            "📈 2026-01-04 每日趋势" in el.get("text", {}).get("content", "")
            for el in elements
        )

        # 验证摘要元素
        assert any(
            "今日发现了 2 个高影响趋势信号" in el.get("text", {}).get("content", "")
            for el in elements
        )

        # 验证高影响信号
        assert any("🚀" in el.get("text", {}).get("content", "") for el in elements)

        # 验证版本发布（去重后只显示最新版本 v1.1.0）
        assert any("v1.1.0" in el.get("text", {}).get("content", "") for el in elements)

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
        # JSON 2.0: elements 在 body 下
        assert len(card["card"]["body"]["elements"]) > 0

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
        # JSON 2.0: elements 在 body 下
        elements = card["card"]["body"]["elements"]
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

    def test_format_releases_deduplicates_same_repo(self):
        """测试：同一仓库的多个版本只显示一次（显示最新版本）"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        # 同一仓库有 3 个版本，应该只显示最新的 v1.2.0
        releases = ReleasesData(
            total_count=3,
            unique_repos_count=1,
            releases=[
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.0.0",
                    author="user1",
                    date="2026-01-03",
                    summary="First release",
                    assets_count=1,
                    url="https://github.com/owner/repo/releases/tag/v1.0.0",
                ),
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.1.0",
                    author="user2",
                    date="2026-01-04",
                    summary="Second release",
                    assets_count=2,
                    url="https://github.com/owner/repo/releases/tag/v1.1.0",
                ),
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.2.0",
                    author="user3",
                    date="2026-01-05",
                    summary="Third release",
                    assets_count=3,
                    url="https://github.com/owner/repo/releases/tag/v1.2.0",
                ),
            ],
        )

        report = DailyReport(
            date="2026-01-05",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            releases=releases,
            stats={
                "total_prs_analyzed": 0,
                "total_releases": 3,
                "high_impact_signals": 0,
            },
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        elements = card["card"]["body"]["elements"]
        content_parts = [
            el.get("text", {}).get("content", "")
            for el in elements
            if el.get("tag") == "div"
        ]
        combined_content = " ".join(content_parts)

        # 应该只显示最新版本 v1.2.0
        # 提取版本发布部分进行验证
        import re

        release_section_match = re.search(
            r"### 🎯 版本发布.*?(?=###|\Z)", combined_content, re.DOTALL
        )
        assert release_section_match is not None
        release_section = release_section_match.group(0)

        # 只显示最新版本 v1.2.0
        assert "v1.2.0" in release_section
        # 不应该显示旧版本
        assert "v1.0.0" not in release_section
        assert "v1.1.0" not in release_section
        # 统计应该显示 "1个仓库" 而不是 "3个"
        assert "1个仓库" in release_section
        # 应该包含链接
        assert "](https://github.com/owner/repo/releases/tag/v1.2.0)" in release_section

    def test_format_releases_includes_links(self):
        """测试：版本发布包含可点击链接"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        releases = ReleasesData(
            total_count=2,
            unique_repos_count=2,
            releases=[
                ReleaseInfo(
                    repo="owner/repo1",
                    version="v2.0.0",
                    author="user1",
                    date="2026-01-04",
                    summary="Test release",
                    assets_count=1,
                    url="https://github.com/owner/repo1/releases/tag/v2.0.0",
                ),
                ReleaseInfo(
                    repo="owner/repo2",
                    version="v1.5.0",
                    author="user2",
                    date="2026-01-04",
                    summary="Test release",
                    assets_count=1,
                    url="https://github.com/owner/repo2/releases/tag/v1.5.0",
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
            releases=releases,
            stats={
                "total_prs_analyzed": 0,
                "total_releases": 2,
                "high_impact_signals": 0,
            },
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        elements = card["card"]["body"]["elements"]
        content_parts = [
            el.get("text", {}).get("content", "")
            for el in elements
            if el.get("tag") == "div"
        ]
        combined_content = " ".join(content_parts)

        # 飞书 Markdown 链接语法：[text](url)
        assert (
            "[owner/repo1](https://github.com/owner/repo1/releases/tag/v2.0.0)"
            in combined_content
        )
        assert (
            "[owner/repo2](https://github.com/owner/repo2/releases/tag/v1.5.0)"
            in combined_content
        )
