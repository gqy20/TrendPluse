"""Issue 数据模型测试

测试 IssueInfo 和 IssueData 数据模型。
"""

from datetime import UTC, datetime

from trendpluse.models.issue import IssueData, IssueInfo, UserPainPoint


class TestIssueInfo:
    """IssueInfo 数据模型测试"""

    def test_create_minimal_issue(self):
        """测试创建最小 Issue 对象"""
        # Arrange & Act
        now = datetime.now(UTC)
        issue = IssueInfo(
            repo="anthropics/claude-code",
            issue_id=123,
            title="Test Issue",
            body=None,
            state="open",
            author="testuser",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=[],
            url="https://github.com/anthropics/claude-code/issues/123",
            last_comment_days=0,
            is_recently_active=False,
        )

        # Assert
        assert issue.repo == "anthropics/claude-code"
        assert issue.issue_id == 123
        assert issue.title == "Test Issue"
        assert issue.body is None
        assert issue.state == "open"
        assert issue.author == "testuser"
        assert issue.comments == 0
        assert issue.labels == []
        assert issue.last_comment_days == 0
        assert issue.is_recently_active is False

    def test_issue_with_all_fields(self):
        """测试包含所有字段的 Issue"""
        # Arrange
        now = datetime.now(UTC)
        created = now.replace(hour=10)
        updated = now.replace(hour=12)
        closed = now.replace(hour=14)

        # Act
        issue = IssueInfo(
            repo="openai/openai-python",
            issue_id=456,
            title="Feature Request: Add support for X",
            body="Please add support for feature X",
            state="closed",
            author="featureuser",
            created_at=created,
            updated_at=updated,
            closed_at=closed,
            comments=10,
            labels=["enhancement", "feature"],
            url="https://github.com/openai/openai-python/issues/456",
            last_comment_days=2,
            is_recently_active=True,
        )

        # Assert
        assert issue.issue_id == 456
        assert issue.state == "closed"
        assert issue.comments == 10
        assert issue.labels == ["enhancement", "feature"]
        assert issue.last_comment_days == 2
        assert issue.is_recently_active is True
        assert issue.closed_at == closed

    def test_issue_labels_default_to_empty_list(self):
        """测试 labels 默认为空列表"""
        # Arrange & Act
        now = datetime.now(UTC)
        issue = IssueInfo(
            repo="a/a",
            issue_id=1,
            title="Test",
            body=None,
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=[],
            url="https://example.com",
            last_comment_days=0,
            is_recently_active=False,
        )

        # Assert
        assert issue.labels == []

    def test_issue_body_nullable(self):
        """测试 body 字段可为 None"""
        # Arrange & Act
        now = datetime.now(UTC)
        issue = IssueInfo(
            repo="a/a",
            issue_id=1,
            title="No body issue",
            body=None,
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=[],
            url="https://example.com",
            last_comment_days=0,
            is_recently_active=False,
        )

        # Assert
        assert issue.body is None


class TestIssueData:
    """IssueData 汇总数据模型测试"""

    def test_create_empty_issue_data(self):
        """测试创建空的 IssueData"""
        # Arrange & Act
        data = IssueData(
            total_count=0,
            bug_reports=0,
            feature_requests=0,
            questions=0,
            discussions=0,
        )

        # Assert
        assert data.total_count == 0
        assert data.bug_reports == 0
        assert data.feature_requests == 0
        assert data.questions == 0
        assert data.discussions == 0
        assert data.sentiment_distribution == {}
        assert data.top_pain_points == []

    def test_create_issue_data_with_pain_points(self):
        """测试创建包含痛点的 IssueData"""
        # Arrange
        pain_point = UserPainPoint(
            topic="Performance issue",
            count=10,
            avg_sentiment=-0.5,
            affected_repos=["repo1", "repo2"],
            sample_urls=["https://example.com/1"],
        )

        # Act
        data = IssueData(
            total_count=100,
            bug_reports=40,
            feature_requests=30,
            questions=20,
            discussions=10,
            sentiment_distribution={"positive": 10, "neutral": 50, "negative": 40},
            top_pain_points=[pain_point],
        )

        # Assert
        assert data.total_count == 100
        assert data.bug_reports == 40
        assert data.feature_requests == 30
        assert data.questions == 20
        assert data.discussions == 10
        assert len(data.top_pain_points) == 1
        assert data.top_pain_points[0].topic == "Performance issue"

    def test_sentiment_distribution_default(self):
        """测试 sentiment_distribution 默认为空字典"""
        # Arrange & Act
        data = IssueData(
            total_count=0,
            bug_reports=0,
            feature_requests=0,
            questions=0,
            discussions=0,
        )

        # Assert
        assert data.sentiment_distribution == {}

    def test_top_pain_points_default(self):
        """测试 top_pain_points 默认为空列表"""
        # Arrange & Act
        data = IssueData(
            total_count=0,
            bug_reports=0,
            feature_requests=0,
            questions=0,
            discussions=0,
        )

        # Assert
        assert data.top_pain_points == []


class TestUserPainPoint:
    """UserPainPoint 数据模型测试"""

    def test_create_pain_point(self):
        """测试创建用户痛点对象"""
        # Arrange & Act
        pain = UserPainPoint(
            topic="Memory leak",
            count=15,
            avg_sentiment=-0.7,
            affected_repos=["repo1", "repo2", "repo3"],
            sample_urls=["url1", "url2"],
        )

        # Assert
        assert pain.topic == "Memory leak"
        assert pain.count == 15
        assert pain.avg_sentiment == -0.7
        assert len(pain.affected_repos) == 3
        assert len(pain.sample_urls) == 2

    def test_pain_point_with_negative_sentiment(self):
        """测试负面情绪的痛点"""
        # Arrange & Act
        pain = UserPainPoint(
            topic="Crash on startup",
            count=20,
            avg_sentiment=-0.9,
            affected_repos=["repo1"],
            sample_urls=["url1"],
        )

        # Assert
        assert pain.avg_sentiment == -0.9
        assert pain.count == 20

    def test_pain_point_with_positive_sentiment(self):
        """测试正面情绪的痛点"""
        # Arrange & Act
        pain = UserPainPoint(
            topic="Feature request",
            count=5,
            avg_sentiment=0.5,
            affected_repos=["repo1"],
            sample_urls=["url1"],
        )

        # Assert
        assert pain.avg_sentiment == 0.5
