"""Release 数据采集单元测试"""

from datetime import datetime, timedelta, UTC
from unittest.mock import Mock, patch, MagicMock

from trendpluse.collectors.releases import ReleaseCollector


class TestReleaseCollector:
    """测试 Release 数据采集器"""

    def test_init_without_token(self):
        """测试：无 token 初始化采集器"""
        # Arrange & Act
        with patch("trendpluse.collectors.releases.Github"):
            collector = ReleaseCollector(token="")

        # Assert
        assert collector is not None
        assert collector.client is not None

    @patch("trendpluse.collectors.releases.Github")
    def test_init_with_token(self, mock_github):
        """测试：带 token 初始化采集器"""
        # Arrange & Act
        collector = ReleaseCollector(token="test_token")

        # Assert
        mock_github.assert_called_once_with(login_or_token="test_token")

    @patch("trendpluse.collectors.releases.Github")
    def test_collect_releases_returns_dict_with_expected_keys(self, mock_github):
        """测试：collect_releases 应返回包含预期键的字典"""
        # Arrange
        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = []

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["anthropics/skills"]
        since = datetime.now(UTC)

        # Act
        result = collector.collect_releases(repos=repos, since=since)

        # Assert
        assert isinstance(result, dict)
        assert "total_releases" in result
        assert "repos_with_releases" in result
        assert "repo_releases" in result
        assert "detailed_releases" in result
        assert "period_start" in result
        assert "period_end" in result

    @patch("trendpluse.collectors.releases.Github")
    def test_collect_releases_filters_by_date(self, mock_github):
        """测试：应该按日期过滤 releases"""
        # Arrange
        # 创建两个 mock release，一个在时间范围内，一个不在
        old_release = Mock()
        old_release.created_at = datetime(2025, 1, 1, tzinfo=UTC)
        old_release.tag_name = "v1.0.0"
        old_release.title = "Old Release"
        old_release.body = "Old release"
        old_release.prerelease = False
        old_release.author = Mock()
        old_release.author.login = "testuser"
        old_release.html_url = "https://github.com/test/test/releases/v1.0.0"
        old_release.assets = []

        new_release = Mock()
        new_release.created_at = datetime.now(UTC)
        new_release.tag_name = "v2.0.0"
        new_release.title = "New Release"
        new_release.body = "New release"
        new_release.prerelease = False
        new_release.author = Mock()
        new_release.author.login = "testuser"
        new_release.html_url = "https://github.com/test/test/releases/v2.0.0"
        new_release.assets = []

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = [old_release, new_release]

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["anthropics/skills"]
        since = datetime.now(UTC) - timedelta(hours=1)

        # Act
        result = collector.collect_releases(repos=repos, since=since)

        # Assert - 应该只返回新 release
        assert result["total_releases"] == 1
        assert len(result["detailed_releases"]) == 1
        assert result["detailed_releases"][0]["tag_name"] == "v2.0.0"

    @patch("trendpluse.collectors.releases.Github")
    def test_collect_releases_excludes_prerelease_when_configured(self, mock_github):
        """测试：当配置时应该排除预发布版本"""
        # Arrange
        stable_release = Mock()
        stable_release.created_at = datetime.now(UTC)
        stable_release.prerelease = False

        pre_release = Mock()
        pre_release.created_at = datetime.now(UTC)
        pre_release.prerelease = True

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = [stable_release, pre_release]

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["anthropics/skills"]
        since = datetime.now(UTC) - timedelta(hours=1)

        # Act
        result = collector.collect_releases(
            repos=repos, since=since, include_prereleases=False
        )

        # Assert
        assert result["total_releases"] == 1
        assert result["detailed_releases"][0]["prerelease"] is False

    @patch("trendpluse.collectors.releases.Github")
    def test_collect_releases_handles_api_errors_gracefully(self, mock_github):
        """测试：应该优雅处理 API 错误"""
        # Arrange
        mock_client = MagicMock()
        mock_client.get_repo.side_effect = Exception("API Error")
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["anthropics/skills"]
        since = datetime.now(UTC)

        # Act - 不应该抛出异常
        result = collector.collect_releases(repos=repos, since=since)

        # Assert
        assert isinstance(result, dict)
        assert result["total_releases"] == 0

    @patch("trendpluse.collectors.releases.Github")
    def test_parse_version_extract_major_minor_patch(self, mock_github):
        """测试：应该正确解析版本号"""
        # Arrange
        mock_github.return_value = MagicMock()

        collector = ReleaseCollector(token="test_token")

        # Act & Assert
        assert collector._parse_version("v1.2.3") == {
            "major": 1,
            "minor": 2,
            "patch": 3,
            "is_prerelease": False,
        }
        assert collector._parse_version("2.0.0") == {
            "major": 2,
            "minor": 0,
            "patch": 0,
            "is_prerelease": False,
        }
        assert collector._parse_version("1.0.0-alpha")["is_prerelease"] is True
        assert collector._parse_version("invalid") is None

    @patch("trendpluse.collectors.releases.Github")
    def test_collect_releases_sorts_by_date_descending(self, mock_github):
        """测试：结果应该按日期降序排列"""
        # Arrange
        releases = []
        for i in range(3):
            release = Mock()
            release.created_at = datetime.now(UTC) - timedelta(hours=i)
            release.tag_name = f"v1.0.{i}"
            release.title = f"Release {i}"
            release.body = f"Body {i}"
            release.prerelease = False
            release.author = Mock()
            release.author.login = "testuser"
            release.html_url = f"https://github.com/test/test/v1.0.{i}"
            release.assets = []
            releases.append(release)

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = releases

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["test/repo"]
        since = datetime.now(UTC) - timedelta(days=1)

        # Act
        result = collector.collect_releases(repos=repos, since=since)

        # Assert - 应该按日期降序（最新的在前）
        detailed_releases = result["detailed_releases"]
        assert len(detailed_releases) == 3
        assert detailed_releases[0]["tag_name"] == "v1.0.0"  # 最新的
        assert detailed_releases[2]["tag_name"] == "v1.0.2"  # 最旧的
