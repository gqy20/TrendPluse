"""Markdown 格式化器单元测试"""

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    ReleaseInfo,
    ReleasesData,
    RepoActivity,
)


class TestMarkdownFormatterActivity:
    """测试 MarkdownFormatter 对 ActivityData 的渲染"""

    def test_render_activity_with_structured_data(self):
        """测试：使用结构化 ActivityData 渲染活跃度信息"""
        # Arrange
        from trendpluse.reporters.markdown_reporter import MarkdownReporter

        formatter = MarkdownReporter()

        activity = ActivityData(
            total_commits=100,
            active_repos_count=5,
            top_repos=[
                RepoActivity(
                    repo="owner/repo1",
                    commits=50,
                    top_contributors=["user1", "user2"],
                ),
                RepoActivity(
                    repo="owner/repo2",
                    commits=30,
                    top_contributors=["user3"],
                ),
            ],
        )

        # Act
        result = formatter._render_activity(activity)

        # Assert
        assert "## 📈 仓库活跃度" in result
        assert "**总 Commit 数**: 100" in result
        assert "**活跃仓库数**: 5" in result
        assert "owner/repo1" in result


class TestMarkdownFormatterReleases:
    """测试 MarkdownFormatter 对 ReleasesData 的渲染"""

    def test_render_releases_with_structured_data(self):
        """测试：使用结构化 ReleasesData 渲染版本发布信息"""
        # Arrange
        from trendpluse.reporters.markdown_reporter import MarkdownReporter

        formatter = MarkdownReporter()

        releases = ReleasesData(
            total_count=2,
            unique_repos_count=1,
            releases=[
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.0.0",
                    author="test-user",
                    date="2026-01-04",
                    summary="Test release",
                    assets_count=5,
                    url="https://github.com/owner/repo/releases/tag/v1.0.0",
                ),
                ReleaseInfo(
                    repo="owner/repo",
                    version="v1.1.0",
                    author="test-user",
                    date="2026-01-05",
                    summary="Another release",
                    assets_count=3,
                    url="https://github.com/owner/repo/releases/tag/v1.1.0",
                ),
            ],
        )

        # Act
        result = formatter._render_releases(releases)

        # Assert
        assert "## 🎯 版本发布动态" in result
        assert "**新发布版本**: 2 个" in result
        assert "**涉及仓库**: 1 个" in result
        assert "v1.0.0" in result
        assert "test-user" in result


class TestMarkdownFormatterFullReport:
    """测试完整的 MarkdownReporter 报告生成"""

    def test_render_full_report_with_structured_data(self):
        """测试：使用结构化数据渲染完整报告"""
        # Arrange
        from trendpluse.reporters.markdown_reporter import MarkdownReporter

        formatter = MarkdownReporter()

        activity = ActivityData(
            total_commits=50,
            active_repos_count=2,
            top_repos=[
                RepoActivity(
                    repo="test/repo",
                    commits=30,
                    top_contributors=[],
                )
            ],
        )

        releases = ReleasesData(
            total_count=1,
            unique_repos_count=1,
            releases=[
                ReleaseInfo(
                    repo="test/repo",
                    version="v1.0.0",
                    author="user",
                    date="2026-01-04",
                    summary="Test",
                    assets_count=1,
                    url="https://github.com/test/repo/releases/tag/v1.0.0",
                )
            ],
        )

        report = DailyReport(
            date="2026-01-04",
            summary_brief="Test summary",
            engineering_signals=[],
            research_signals=[],
            commit_signals=[],
            release_signals=[],
            activity=activity,
            releases=releases,
        )

        # Act
        result = formatter.render_report(report)

        # Assert
        assert "# TrendPulse 每日报告 - 2026-01-04" in result
        assert "## 📈 仓库活跃度" in result
        assert "## 🎯 版本发布动态" in result
        assert "v1.0.0" in result
