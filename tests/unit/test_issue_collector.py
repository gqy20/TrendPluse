"""IssueCollector 采集器测试

测试 Issue 采集功能，包括快照去重、时间窗口过滤等。
"""

# mypy: disable-error-code="import-untyped"
from datetime import UTC, datetime, timedelta

from freezegun import freeze_time
from github import GithubException

from trendpluse.collectors.issues import IssueCollector


class TestIssueCollector:
    """IssueCollector 采集器测试"""

    def test_create_collector(self):
        """测试创建采集器"""
        # Arrange & Act
        collector = IssueCollector(token="test_token")

        # Assert
        assert collector.token == "test_token"
        assert collector.CREATE_WINDOW_DAYS == 90
        assert collector.ACTIVE_WINDOW_DAYS == 3

    def test_create_collector_with_custom_snapshot_dir(self, temp_dir):
        """测试创建带自定义快照目录的采集器"""
        # Arrange & Act
        collector = IssueCollector(
            token="test_token", snapshot_dir=str(temp_dir / "snapshots")
        )

        # Assert
        assert collector.snapshot.snapshot_dir == temp_dir / "snapshots"

    def test_fetch_empty_repos_list(self):
        """测试空仓库列表"""
        # Arrange
        collector = IssueCollector(token="test_token")

        # Act
        issues, stats = collector.fetch_issues(repos=[], snapshot_date="2026-01-31")

        # Assert
        assert issues == []
        assert stats["total_fetched"] == 0

    @freeze_time("2026-01-31")
    def test_should_analyze_recent_created_issue(self, mock_github):
        """测试最近创建的 Issue 应该被分析"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)
        recent_issue = mock_github.create_issue(
            created_at=now - timedelta(days=30),  # 90天内创建
            updated_at=now - timedelta(days=1),
        )

        # Act
        should = collector._should_analyze(recent_issue, now)

        # Assert
        assert should is True

    @freeze_time("2026-01-31")
    def test_should_analyze_old_issue_with_recent_activity(self, mock_github):
        """测试旧 Issue 但最近有回复的应该被分析"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)
        old_issue = mock_github.create_issue(
            created_at=now - timedelta(days=100),  # 超过90天
            updated_at=now - timedelta(days=1),  # 但3天内有更新
        )

        # Act
        should = collector._should_analyze(old_issue, now)

        # Assert
        assert should is True

    @freeze_time("2026-01-31")
    def test_should_not_analyze_old_issue_without_recent_activity(self, mock_github):
        """测试旧 Issue 且最近无回复的不应该被分析"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)
        old_issue = mock_github.create_issue(
            created_at=now - timedelta(days=100),  # 超过90天
            updated_at=now - timedelta(days=10),  # 超过3天无更新
        )

        # Act
        should = collector._should_analyze(old_issue, now)

        # Assert
        assert should is False

    @freeze_time("2026-01-31")
    def test_should_analyze_exactly_90_days_old(self, mock_github):
        """测试刚好90天的 Issue 应该被分析"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)
        issue = mock_github.create_issue(
            created_at=now - timedelta(days=90),  # 刚好90天
            updated_at=now - timedelta(days=1),
        )

        # Act
        should = collector._should_analyze(issue, now)

        # Assert
        assert should is True

    @freeze_time("2026-01-31")
    def test_should_analyze_exactly_3_days_since_update(self, mock_github):
        """测试刚好3天前更新的 Issue 应该被分析"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)
        issue = mock_github.create_issue(
            created_at=now - timedelta(days=100),
            updated_at=now - timedelta(days=3),  # 刚好3天
        )

        # Act
        should = collector._should_analyze(issue, now)

        # Assert
        assert should is True

    def test_fetch_issues_filters_by_snapshot(self, temp_dir, mock_github):
        """测试通过快照过滤已分析的 Issue"""
        # Arrange
        collector = IssueCollector(token="test_token", snapshot_dir=str(temp_dir))

        # 保存快照：已分析了 issue #123
        collector.save_snapshot(
            "2026-01-31",
            [{"repo": "anthropics/claude-code", "issue_id": 123, "categories": []}],
        )

        # Mock 返回两个 Issues
        mock_github.mock_repo_issues(
            [
                mock_github.create_issue(number=123, title="Old Issue"),
                mock_github.create_issue(number=456, title="New Issue"),
            ]
        )

        # Act
        issues, stats = collector.fetch_issues(
            repos=["anthropics/claude-code"], snapshot_date="2026-01-31"
        )

        # Assert - 只返回新 Issue，旧的被过滤
        assert len(issues) == 1
        assert issues[0].issue_id == 456
        assert stats["total_fetched"] == 1
        assert stats["filtered_by_duplicate"] == 1

    def test_fetch_issues_with_empty_snapshot_date(self, mock_github):
        """测试空快照日期时不过滤"""
        # Arrange
        collector = IssueCollector(token="test_token")

        mock_github.mock_repo_issues(
            [
                mock_github.create_issue(number=123, title="Issue 1"),
                mock_github.create_issue(number=456, title="Issue 2"),
            ]
        )

        # Act
        issues, stats = collector.fetch_issues(
            repos=["anthropics/claude-code"], snapshot_date=""
        )

        # Assert - 返回所有 Issues
        assert len(issues) == 2
        assert stats["filtered_by_duplicate"] == 0

    def test_skip_pull_requests(self, mock_github):
        """测试跳过 Pull Request"""
        # Arrange
        collector = IssueCollector(token="test_token")

        # 创建一个 Issue 和一个 PR
        regular_issue = mock_github.create_issue(number=1, title="Regular Issue")
        pr_issue = mock_github.create_issue(number=2, title="PR Issue")
        pr_issue.pull_request = "pr_object"  # 标记为 PR

        mock_github.mock_repo_issues([regular_issue, pr_issue])

        # Act
        issues, stats = collector.fetch_issues(
            repos=["anthropics/claude-code"], snapshot_date=""
        )

        # Assert - 只返回普通 Issue，PR 被跳过
        assert len(issues) == 1
        assert issues[0].issue_id == 1

    def test_handle_github_api_error(self, mock_github):
        """测试处理 GitHub API 错误"""
        # Arrange
        collector = IssueCollector(token="test_token")

        # Mock 抛出异常
        def error_side_effect(*args, **kwargs):
            raise GithubException(403, {"message": "Rate limit exceeded"})

        mock_github.mock_repo.get_issues.side_effect = error_side_effect

        # Act
        issues, stats = collector.fetch_issues(
            repos=["anthropics/claude-code"], snapshot_date=""
        )

        # Assert - 返回空列表，不崩溃
        assert issues == []
        assert stats["total_fetched"] == 0

    def test_calculate_last_comment_days(self):
        """测试计算最后评论距今天数"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)

        # Mock Issue
        issue = type("Issue", (), {"updated_at": now - timedelta(days=5)})()

        # Act
        days = collector._get_last_comment_days(issue, now)

        # Assert
        assert days == 5

    def test_save_snapshot(self, temp_dir):
        """测试保存快照"""
        # Arrange
        collector = IssueCollector(token="test_token", snapshot_dir=str(temp_dir))
        analyzed_issues = [
            {"repo": "anthropics/claude-code", "issue_id": 123, "categories": ["bug"]},
            {
                "repo": "openai/openai-python",
                "issue_id": 456,
                "categories": ["feature"],
            },
        ]

        # Act
        collector.save_snapshot("2026-01-31", analyzed_issues)

        # Assert - 验证文件存在
        snapshot_path = temp_dir / "2026-01-31.json"
        assert snapshot_path.exists()

        # 验证内容
        loaded_ids = collector.snapshot.load_analyzed_ids("2026-01-31")
        assert loaded_ids == {
            ("anthropics/claude-code", 123),
            ("openai/openai-python", 456),
        }

    @freeze_time("2026-01-31")
    def test_convert_github_issue_to_issue_info(self, mock_github):
        """测试转换 GitHub Issue 对象为 IssueInfo"""
        # Arrange
        collector = IssueCollector(token="test_token")
        now = datetime.now(UTC)

        github_issue = mock_github.create_issue(
            number=123,
            title="Test Issue",
            body="Issue body",
            state="open",
            created_at=now - timedelta(days=10),
            updated_at=now - timedelta(days=1),
        )

        # Act
        issue_info = collector._convert_to_issue_info(
            github_issue, "anthropics/claude-code", now
        )

        # Assert
        assert issue_info.repo == "anthropics/claude-code"
        assert issue_info.issue_id == 123
        assert issue_info.title == "Test Issue"
        assert issue_info.body == "Issue body"
        assert issue_info.state == "open"
        assert issue_info.last_comment_days == 1
        assert issue_info.is_recently_active is True  # 1天 <= 3天
