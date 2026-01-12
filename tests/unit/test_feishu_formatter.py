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

    @staticmethod
    def _get_all_card_content(elements: list) -> list[str]:
        """提取卡片中所有元素的内容（包括折叠面板内的内容和标题）

        Args:
            elements: 卡片元素列表

        Returns:
            所有元素的内容列表
        """
        contents: list[str] = []

        for el in elements:
            tag = el.get("tag")

            # 直接的 div 元素
            if tag == "div":
                content = el.get("text", {}).get("content", "")
                contents.append(content)

            # 折叠面板元素 - 递归提取内部内容和标题
            elif tag == "collapsible_panel":
                # 添加面板标题
                header = el.get("header", {})
                title = header.get("title", {})
                title_content = title.get("content", "")
                if title_content:
                    contents.append(title_content)

                # 添加面板内部内容
                panel_elements = el.get("elements", [])
                for panel_el in panel_elements:
                    if panel_el.get("tag") == "div":
                        content = panel_el.get("text", {}).get("content", "")
                        contents.append(content)

        return contents

    @staticmethod
    def _content_contains(elements: list, text: str) -> bool:
        """检查卡片中是否包含指定文本（包括折叠面板内）

        Args:
            elements: 卡片元素列表
            text: 要查找的文本

        Returns:
            是否包含该文本
        """
        contents = TestFeishuFormatter._get_all_card_content(elements)
        return any(text in content for content in contents)

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
        # header 是可选的，不再强制检查
        # JSON 2.0: elements 在 body 下
        assert "body" in card["card"]
        assert "elements" in card["card"]["body"]

        # 验证 body 中的醒目主标题和日期（主标题使用 #，日期使用普通文本）
        elements = card["card"]["body"]["elements"]
        assert any(
            "# 📊 TrendPulse 每日报告" in el.get("text", {}).get("content", "")
            for el in elements
        )
        assert any(
            "📅 2026-01-04" in el.get("text", {}).get("content", "") for el in elements
        )

        # 验证摘要元素
        assert any(
            "今日发现了 2 个高影响趋势信号" in el.get("text", {}).get("content", "")
            for el in elements
        )

        # 验证高影响信号（注意：工程信号现在在折叠面板中）
        assert self._content_contains(elements, "Test Signal 1")

        # 验证版本发布（去重后只显示最新版本 v1.1.0）
        # 注意：版本发布现在在折叠面板中，需要使用辅助函数检查
        assert self._content_contains(elements, "v1.1.0")

        # 验证活跃仓库
        # 注意：活跃度现在在折叠面板中，需要使用辅助函数检查
        assert self._content_contains(elements, "owner/repo1")

        # 验证统计信息
        # 注意：统计信息现在在折叠面板中，需要使用辅助函数检查
        assert self._content_contains(elements, "10")

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

        # 验证包含 TOP 3 仓库（注意：活跃度现在在折叠面板中）
        assert self._content_contains(elements, "owner/repo1")
        assert self._content_contains(elements, "owner/repo2")
        assert self._content_contains(elements, "owner/repo3")

    def test_format_releases_shows_all_versions(self):
        """测试：版本发布显示所有版本（与 MarkdownReporter 一致）"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        # 同一仓库有 3 个版本，都应该显示（最多 5 个）
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

        # 应该显示所有版本（注意：版本发布现在在折叠面板中）
        assert self._content_contains(elements, "v1.0.0")
        assert self._content_contains(elements, "v1.1.0")
        assert self._content_contains(elements, "v1.2.0")
        # 验证总览统计
        assert self._content_contains(elements, "**新发布版本**: 3 个")
        assert self._content_contains(elements, "**涉及仓库**: 1 个")
        # 验证包含发布者和时间信息
        assert self._content_contains(elements, "user1")
        assert self._content_contains(elements, "2026-01-03")

    def test_format_releases_includes_detailed_info(self):
        """测试：版本发布包含详细信息（发布者、时间、摘要、链接）"""
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
                    summary="Test release with some details",
                    assets_count=1,
                    url="https://github.com/owner/repo1/releases/tag/v2.0.0",
                ),
                ReleaseInfo(
                    repo="owner/repo2",
                    version="v1.5.0",
                    author="user2",
                    date="2026-01-04",
                    summary="Another test release",
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

        # 验证包含详细信息（注意：版本发布现在在折叠面板中）
        # 仓库链接
        assert self._content_contains(
            elements, "[owner/repo1](https://github.com/owner/repo1)"
        )
        assert self._content_contains(
            elements, "[owner/repo2](https://github.com/owner/repo2)"
        )
        # 版本号
        assert self._content_contains(elements, "v2.0.0")
        assert self._content_contains(elements, "v1.5.0")
        # 发布者
        assert self._content_contains(elements, "user1")
        assert self._content_contains(elements, "user2")
        # 时间
        assert self._content_contains(elements, "2026-01-04")
        # 摘要
        assert self._content_contains(elements, "Test release")
        # 资产信息
        assert self._content_contains(elements, "**资产**")
        # 查看详情链接
        assert self._content_contains(elements, "查看详情")

    def test_format_card_includes_release_signals(self):
        """测试：卡片包含 Release 信号部分（与 Markdown 一致）"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        release_signals = [
            Signal(
                id="release-sig-1",
                title="Major Version Update",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="重要版本更新",
                sources=["https://github.com/test/repo/releases/tag/v2.0.0"],
                related_repos=["test/repo"],
            ),
        ]

        report = DailyReport(
            date="2026-01-05",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=release_signals,
            stats={"total_prs_analyzed": 0, "high_impact_signals": 1},
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

        # 应该包含 Release 信号标题（使用粗体而非标题）
        assert "**🎯 Release 信号**" in combined_content

    def test_format_card_includes_breaking_changes(self):
        """测试：卡片包含 Breaking Changes 部分（与 Markdown 一致）"""
        # Arrange
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        breaking_changes = [
            {
                "repo": "test/repo",
                "tag_name": "v2.0.0",
                "changes": [
                    {"category": "API", "description": "移除旧 API", "impact": "high"},
                    {
                        "category": "Config",
                        "description": "配置格式变更",
                        "impact": "medium",
                    },
                ],
            }
        ]

        report = DailyReport(
            date="2026-01-05",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            breaking_changes=breaking_changes,
            stats={"total_prs_analyzed": 0},
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

        # 应该包含 Breaking Changes 标题（使用粗体而非标题）
        assert "**⚠️ Breaking Changes**" in combined_content
        # 应该包含变更内容
        assert "移除旧 API" in combined_content
        # 应该包含影响级别表情
        assert "🔴" in combined_content or "🟡" in combined_content

    def test_format_activity_includes_overview(self):
        """测试：活跃度部分包含总览指标（与 Markdown 一致）"""
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
            ],
        )

        report = DailyReport(
            date="2026-01-05",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            activity=activity,
            stats={"total_prs_analyzed": 0},
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        elements = card["card"]["body"]["elements"]

        # 应该包含总览指标（注意：活跃度现在在折叠面板中）
        assert self._content_contains(elements, "**总 Commit 数**: 150")
        assert self._content_contains(elements, "**活跃仓库数**: 3")
        assert self._content_contains(elements, "**新贡献者数**: 1")

    def test_format_releases_includes_ai_summary(self):
        """测试：版本发布包含 AI 总结（与 Markdown 一致）"""
        # Arrange
        from trendpluse.models.signal import ReleaseSummary
        from trendpluse.notifiers.formatters import FeishuFormatter

        formatter = FeishuFormatter()

        releases = ReleasesData(
            total_count=1,
            unique_repos_count=1,
            releases=[
                ReleaseInfo(
                    repo="owner/repo",
                    version="v2.0.0",
                    author="user1",
                    date="2026-01-05",
                    summary="Original summary",
                    assets_count=5,
                    url="https://github.com/owner/repo/releases/tag/v2.0.0",
                    ai_summary=ReleaseSummary(
                        change_type="feature",
                        key_changes=["新功能 A", "新功能 B", "性能优化"],
                        summary_cn="这是一个重要版本更新",
                        impact_level=5,
                    ),
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
            stats={"total_prs_analyzed": 0},
        )

        # Act
        card = formatter.format_card(report)

        # Assert
        elements = card["card"]["body"]["elements"]

        # 应该包含 AI 总结内容（注意：版本发布现在在折叠面板中）
        assert self._content_contains(elements, "新功能 A")
        assert self._content_contains(elements, "这是一个重要版本更新")
        # 应该包含变更类型
        assert self._content_contains(elements, "变更类型") or self._content_contains(
            elements, "feature"
        )
