"""GitHub API 详情获取单元测试"""
from unittest.mock import Mock, patch

import pytest

from trendpluse.collectors.github_api import GitHubDetailFetcher


class TestGitHubDetailFetcher:
    """测试 GitHub 详情获取器"""

    @patch("trendpluse.collectors.github_api.Github")
    def test_init_with_token(self, mock_github):
        """测试：使用 token 初始化"""
        # Arrange & Act
        fetcher = GitHubDetailFetcher(token="test_token")

        # Assert
        assert fetcher is not None
        mock_github.assert_called_once_with(login_or_token="test_token")

    @patch("trendpluse.collectors.github_api.Github")
    def test_fetch_pr_details(self, mock_github_class):
        """测试：获取 PR 详情"""
        # Arrange
        mock_pr = Mock()
        mock_pr.number = 123
        mock_pr.title = "Add feature X"
        mock_pr.body = "This implements feature X"
        mock_pr.user.login = "alice"
        mock_pr.created_at.isoformat.return_value = "2026-01-01T00:00:00Z"
        mock_pr.closed_at.isoformat.return_value = "2026-01-02T00:00:00Z"
        mock_pr.html_url = "https://github.com/owner/repo/pull/123"
        mock_pr.state = "closed"
        mock_pr.merged = True
        mock_pr.merge_commit_sha = "abc123"
        mock_pr.additions = 100
        mock_pr.deletions = 50
        mock_pr.changed_files = 5

        mock_repo = Mock()
        mock_repo.get_pull.return_value = mock_pr

        mock_github = Mock()
        mock_github.get_repo.return_value = mock_repo
        mock_github_class.return_value = mock_github

        fetcher = GitHubDetailFetcher(token="test_token")

        # Act
        details = fetcher.fetch_pr_details("owner/repo", 123)

        # Assert
        assert details["number"] == 123
        assert details["title"] == "Add feature X"
        assert details["author"] == "alice"
        assert details["merged"] is True
        mock_github.get_repo.assert_called_once_with("owner/repo")
        mock_repo.get_pull.assert_called_once_with(123)

    @patch("trendpluse.collectors.github_api.Github")
    def test_fetch_release_details(self, mock_github_class):
        """测试：获取 Release 详情"""
        # Arrange
        mock_release = Mock()
        mock_release.tag_name = "v1.0.0"
        mock_release.name = "First release"
        mock_release.body = "Release notes here"
        mock_release.html_url = "https://github.com/owner/repo/releases/tag/v1.0.0"
        mock_release.created_at.isoformat.return_value = "2026-01-01T00:00:00Z"
        mock_release.published_at.isoformat.return_value = "2026-01-02T00:00:00Z"
        mock_release.author.login = "bob"

        mock_repo = Mock()
        mock_repo.get_release.return_value = mock_release

        mock_github = Mock()
        mock_github.get_repo.return_value = mock_repo
        mock_github_class.return_value = mock_github

        fetcher = GitHubDetailFetcher(token="test_token")

        # Act
        details = fetcher.fetch_release_details("owner/repo", "v1.0.0")

        # Assert
        assert details["tag_name"] == "v1.0.0"
        assert details["name"] == "First release"
        assert details["author"] == "bob"
        mock_github.get_repo.assert_called_once_with("owner/repo")
        mock_repo.get_release.assert_called_once_with("v1.0.0")

    @patch("trendpluse.collectors.github_api.Github")
    def test_fetch_pr_comments(self, mock_github_class):
        """测试：获取 PR 评论"""
        # Arrange
        mock_comment = Mock()
        mock_comment.user.login = "charlie"
        mock_comment.body = "Looks good!"
        mock_comment.created_at.isoformat.return_value = "2026-01-01T00:00:00Z"

        mock_pr = Mock()
        mock_pr.get_comments.return_value = [mock_comment]

        mock_repo = Mock()
        mock_repo.get_pull.return_value = mock_pr

        mock_github = Mock()
        mock_github.get_repo.return_value = mock_repo
        mock_github_class.return_value = mock_github

        fetcher = GitHubDetailFetcher(token="test_token")

        # Act
        comments = fetcher.fetch_pr_comments("owner/repo", 123)

        # Assert
        assert len(comments) == 1
        assert comments[0]["author"] == "charlie"
        assert comments[0]["body"] == "Looks good!"

    @patch("trendpluse.collectors.github_api.Github")
    def test_fetch_multiple_pr_details(self, mock_github_class):
        """测试：批量获取 PR 详情"""
        # Arrange
        mock_pr_1 = Mock()
        mock_pr_1.number = 1
        mock_pr_1.title = "PR 1"
        mock_pr_1.body = "Body 1"
        mock_pr_1.user.login = "alice"
        mock_pr_1.created_at.isoformat.return_value = "2026-01-01T00:00:00Z"
        mock_pr_1.closed_at.isoformat.return_value = "2026-01-02T00:00:00Z"
        mock_pr_1.html_url = "https://github.com/owner/repo/pull/1"
        mock_pr_1.state = "closed"
        mock_pr_1.merged = True
        mock_pr_1.merge_commit_sha = "sha1"
        mock_pr_1.additions = 10
        mock_pr_1.deletions = 5
        mock_pr_1.changed_files = 2

        mock_pr_2 = Mock()
        mock_pr_2.number = 2
        mock_pr_2.title = "PR 2"
        mock_pr_2.body = "Body 2"
        mock_pr_2.user.login = "bob"
        mock_pr_2.created_at.isoformat.return_value = "2026-01-01T00:00:00Z"
        mock_pr_2.closed_at.isoformat.return_value = "2026-01-02T00:00:00Z"
        mock_pr_2.html_url = "https://github.com/owner/repo/pull/2"
        mock_pr_2.state = "closed"
        mock_pr_2.merged = True
        mock_pr_2.merge_commit_sha = "sha2"
        mock_pr_2.additions = 20
        mock_pr_2.deletions = 10
        mock_pr_2.changed_files = 3

        mock_repo = Mock()
        mock_repo.get_pull.side_effect = [mock_pr_1, mock_pr_2]

        mock_github = Mock()
        mock_github.get_repo.return_value = mock_repo
        mock_github_class.return_value = mock_github

        fetcher = GitHubDetailFetcher(token="test_token")

        candidates = [
            {
                "type": "PullRequestEvent",
                "repo": {"name": "owner/repo"},
                "payload": {"pull_request": {"number": 1}},
            },
            {
                "type": "PullRequestEvent",
                "repo": {"name": "owner/repo"},
                "payload": {"pull_request": {"number": 2}},
            },
        ]

        # Act
        details_list = fetcher.fetch_multiple_pr_details(candidates)

        # Assert
        assert len(details_list) == 2
        assert details_list[0]["number"] == 1
        assert details_list[1]["number"] == 2

    @patch("trendpluse.collectors.github_api.Github")
    def test_rate_limit_handling(self, mock_github_class):
        """测试：处理 API 速率限制"""
        # Arrange
        from github.GithubException import RateLimitExceededException

        mock_repo = Mock()
        mock_repo.get_pull.side_effect = RateLimitExceededException(
            403, {"message": "API rate limit exceeded"}, {}
        )

        mock_github = Mock()
        mock_github.get_repo.return_value = mock_repo
        mock_github_class.return_value = mock_github

        fetcher = GitHubDetailFetcher(token="test_token")

        # Act & Assert
        with pytest.raises(Exception):  # 应该抛出异常或处理
            fetcher.fetch_pr_details("owner/repo", 123)
