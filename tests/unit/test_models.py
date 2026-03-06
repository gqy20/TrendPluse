"""数据模型单元测试"""

import pytest
from pydantic import ValidationError

from trendpluse.models.signal import DailyReport, Signal


class TestSignal:
    """测试 Signal 模型"""

    def test_valid_signal_minimal(self):
        """测试：创建有效的最小信号"""
        # Arrange & Act
        signal = Signal(
            id="test-signal-1",
            title="Test Signal",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="This is a test signal",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        # Assert
        assert signal.id == "test-signal-1"
        assert signal.title == "Test Signal"
        assert signal.type == "capability"
        assert signal.category == "engineering"
        assert signal.impact_score == 5

    def test_signal_invalid_impact_score_too_low(self):
        """测试：impact_score < 1 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="engineering",
                impact_score=0,  # 无效
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "impact_score" in str(exc_info.value)

    def test_signal_invalid_impact_score_too_high(self):
        """测试：impact_score > 5 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="engineering",
                impact_score=6,  # 无效
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "impact_score" in str(exc_info.value)

    def test_signal_invalid_type(self):
        """测试：无效的 type 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="invalid_type",  # 无效
                category="engineering",
                impact_score=3,
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "type" in str(exc_info.value)

    def test_signal_invalid_category(self):
        """测试：无效的 category 应该失败"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            Signal(
                id="test",
                title="Test",
                type="capability",
                category="invalid_category",  # 无效
                impact_score=3,
                why_it_matters="Test",
                sources=["https://github.com/test/repo/pull/1"],
                related_repos=["test/repo"],
            )

        assert "category" in str(exc_info.value)


class TestDailyReport:
    """测试 DailyReport 模型"""

    def test_valid_daily_report_minimal(self):
        """测试：创建有效的最小日报"""
        # Arrange & Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test summary",
            engineering_signals=[],
            research_signals=[],
        )

        # Assert
        assert report.date == "2026-01-02"
        assert report.summary_brief == "Test summary"
        assert len(report.engineering_signals) == 0
        assert len(report.research_signals) == 0

    def test_daily_report_with_signals(self):
        """测试：包含信号的日报"""
        # Arrange
        signal = Signal(
            id="test-1",
            title="Test Signal",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="Test",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        # Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test summary",
            engineering_signals=[signal],
            research_signals=[],
        )

        # Assert
        assert len(report.engineering_signals) == 1
        assert report.engineering_signals[0].id == "test-1"

    def test_daily_report_default_stats(self):
        """测试：stats 应该有默认值"""
        # Arrange & Act
        report = DailyReport(
            date="2026-01-02",
            summary_brief="Test",
            engineering_signals=[],
            research_signals=[],
        )

        # Assert
        assert report.stats.total_prs_analyzed == 0
        assert report.stats.total_releases == 0
        assert report.stats.high_impact_signals == 0


class TestRepoActivity:
    """测试 RepoActivity 模型"""

    def test_valid_repo_activity(self):
        """测试：创建有效的仓库活跃度数据"""
        # Arrange & Act & Assert
        # 这个测试会失败，因为 RepoActivity 模型还不存在
        from trendpluse.models.signal import RepoActivity

        activity = RepoActivity(
            repo="test/repo",
            commits=10,
            top_contributors=["user1", "user2"],
        )

        assert activity.repo == "test/repo"
        assert activity.commits == 10
        assert len(activity.top_contributors) == 2


class TestReleaseInfo:
    """测试 ReleaseInfo 模型"""

    def test_valid_release_info(self):
        """测试：创建有效的版本发布信息"""
        # Arrange & Act & Assert
        # 这个测试会失败，因为 ReleaseInfo 模型还不存在
        from trendpluse.models.signal import ReleaseInfo

        release = ReleaseInfo(
            repo="test/repo",
            version="v1.0.0",
            author="test-user",
            date="2026-01-04",
            summary="Test release",
            assets_count=5,
            url="https://github.com/test/repo/releases/tag/v1.0.0",
        )

        assert release.repo == "test/repo"
        assert release.version == "v1.0.0"
        assert release.author == "test-user"
        assert release.date == "2026-01-04"


class TestActivityData:
    """测试 ActivityData 模型"""

    def test_valid_activity_data(self):
        """测试：创建有效的活跃度汇总数据"""
        # Arrange & Act & Assert
        # 这个测试会失败，因为 ActivityData 模型还不存在
        from trendpluse.models.signal import ActivityData, RepoActivity

        activities = [
            RepoActivity(repo="repo1", commits=10, top_contributors=[]),
            RepoActivity(repo="repo2", commits=5, top_contributors=[]),
        ]

        activity_data = ActivityData(
            total_commits=15,
            active_repos_count=2,
            top_repos=activities,
        )

        assert activity_data.total_commits == 15
        assert len(activity_data.top_repos) == 2


class TestReleasesData:
    """测试 ReleasesData 模型"""

    def test_valid_releases_data(self):
        """测试：创建有效的版本发布汇总数据"""
        # Arrange & Act & Assert
        # 这个测试会失败，因为 ReleasesData 模型还不存在
        from trendpluse.models.signal import ReleaseInfo, ReleasesData

        releases = [
            ReleaseInfo(
                repo="repo1",
                version="v1.0.0",
                author="user1",
                date="2026-01-04",
                summary="Test",
                assets_count=1,
                url="https://github.com/repo1/releases/tag/v1.0.0",
            ),
        ]

        releases_data = ReleasesData(
            total_count=1,
            unique_repos_count=1,
            releases=releases,
        )

        assert releases_data.total_count == 1
        assert len(releases_data.releases) == 1
