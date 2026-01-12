"""Release 数据采集单元测试"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, Mock, patch

from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.models.signal import ReleaseInfo, ReleasesData


class TestReleaseCollector:
    """测试 Release 数据采集器"""

    def test_init_without_token(self):
        """测试：无 token 初始化采集器"""
        # Arrange & Act
        with patch("trendpluse.collectors.base.Github"):
            ReleaseCollector(token="")

        # Assert - 简单验证没有抛出异常

    @patch("trendpluse.collectors.base.Github")
    def test_init_with_token(self, mock_github):
        """测试：带 token 初始化采集器"""
        # Arrange & Act
        ReleaseCollector(token="test_token")

        # Assert
        mock_github.assert_called_once_with(login_or_token="test_token")

    @patch("trendpluse.collectors.base.Github")
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
        releases_data, detailed_releases = collector.collect_releases(
            repos=repos, since=since
        )

        # Assert
        assert isinstance(releases_data, ReleasesData)
        assert hasattr(releases_data, "total_count")
        assert hasattr(releases_data, "unique_repos_count")
        assert hasattr(releases_data, "releases")
        assert isinstance(detailed_releases, list)

    @patch("trendpluse.collectors.base.Github")
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
        releases_data, detailed_releases = collector.collect_releases(
            repos=repos, since=since
        )

        # Assert - 应该只返回新 release
        assert releases_data.total_count == 1
        assert len(detailed_releases) == 1
        assert detailed_releases[0]["tag_name"] == "v2.0.0"

    @patch("trendpluse.collectors.base.Github")
    def test_collect_releases_excludes_prerelease_when_configured(self, mock_github):
        """测试：当配置时应该排除预发布版本"""
        # Arrange
        stable_release = Mock()
        stable_release.created_at = datetime.now(UTC)
        stable_release.prerelease = False
        stable_release.tag_name = "v1.0.0"
        stable_release.title = "Stable Release"
        stable_release.body = "Stable"
        stable_release.html_url = "https://github.com/test/test/releases/v1.0.0"
        stable_release.assets = []
        stable_release.author = Mock()
        stable_release.author.login = "testuser"
        stable_release.published_at = datetime.now(UTC)

        pre_release = Mock()
        pre_release.created_at = datetime.now(UTC)
        pre_release.prerelease = True
        pre_release.tag_name = "v1.0.0-beta"
        pre_release.title = "Pre-release"
        pre_release.body = "Beta"
        pre_release.html_url = "https://github.com/test/test/releases/v1.0.0-beta"
        pre_release.assets = []
        pre_release.author = Mock()
        pre_release.author.login = "testuser"
        pre_release.published_at = datetime.now(UTC)

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = [stable_release, pre_release]

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["anthropics/skills"]
        since = datetime.now(UTC) - timedelta(hours=1)

        # Act
        releases_data, detailed_releases = collector.collect_releases(
            repos=repos, since=since, include_prereleases=False
        )

        # Assert
        assert releases_data.total_count == 1
        assert detailed_releases[0]["prerelease"] is False

    @patch("trendpluse.collectors.base.Github")
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
        releases_data, detailed_releases = collector.collect_releases(
            repos=repos, since=since
        )

        # Assert
        assert isinstance(releases_data, ReleasesData)
        assert releases_data.total_count == 0

    @patch("trendpluse.collectors.base.Github")
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
        parsed = collector._parse_version("1.0.0-alpha")
        assert parsed is not None and parsed["is_prerelease"] is True
        assert collector._parse_version("invalid") is None

    @patch("trendpluse.collectors.base.Github")
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
        releases_data, _ = collector.collect_releases(repos=repos, since=since)

        # Assert - 应该按日期降序（最新的在前）
        assert len(releases_data.releases) == 3
        assert releases_data.releases[0].version == "v1.0.0"  # 最新的
        assert releases_data.releases[2].version == "v1.0.2"  # 最旧的


class TestReleaseCollectorStructuredData:
    """ReleaseCollector 结构化数据返回测试"""

    @patch("trendpluse.collectors.base.Github")
    def test_collect_releases_returns_structured_data(self, mock_github):
        """测试：collect_releases 返回 ReleasesData 和 detailed_releases"""
        # Arrange
        mock_release = Mock()
        mock_release.created_at = datetime.now(UTC)
        mock_release.prerelease = False
        mock_release.tag_name = "v1.0.0"
        mock_release.title = "Test Release"
        mock_release.body = "Test release body"
        mock_release.html_url = "https://github.com/test/repo/releases/v1.0.0"
        mock_release.assets = []
        mock_release.author = Mock()
        mock_release.author.login = "testuser"
        mock_release.published_at = datetime.now(UTC)

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = [mock_release]

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["test/repo"]
        since = datetime.now(UTC) - timedelta(hours=1)

        # Act
        result = collector.collect_releases(repos=repos, since=since)

        # Assert - 返回值应该是元组 (ReleasesData, list)
        assert isinstance(result, tuple)
        assert len(result) == 2

        releases_data, detailed_releases = result

        # 验证 ReleasesData 结构
        assert isinstance(releases_data, ReleasesData)
        assert hasattr(releases_data, "total_count")
        assert hasattr(releases_data, "unique_repos_count")
        assert hasattr(releases_data, "releases")

        # 验证 detailed_releases
        assert isinstance(detailed_releases, list)

    @patch("trendpluse.collectors.base.Github")
    def test_releases_data_contains_release_infos(self, mock_github):
        """测试：ReleasesData 包含 ReleaseInfo 列表"""
        # Arrange
        mock_release = Mock()
        mock_release.created_at = datetime.now(UTC)
        mock_release.prerelease = False
        mock_release.tag_name = "v1.0.0"
        mock_release.title = "Test Release"
        mock_release.body = "Test release body"
        mock_release.html_url = "https://github.com/test/repo/releases/v1.0.0"
        mock_release.assets = []
        mock_release.author = Mock()
        mock_release.author.login = "testuser"
        mock_release.published_at = datetime.now(UTC)

        mock_repo = MagicMock()
        mock_repo.get_releases.return_value = [mock_release]

        mock_client = MagicMock()
        mock_client.get_repo.return_value = mock_repo
        mock_github.return_value = mock_client

        collector = ReleaseCollector(token="test_token")
        repos = ["test/repo"]
        since = datetime.now(UTC) - timedelta(hours=1)

        # Act
        releases_data, _ = collector.collect_releases(repos=repos, since=since)

        # Assert
        assert len(releases_data.releases) > 0
        release_info = releases_data.releases[0]
        assert isinstance(release_info, ReleaseInfo)
        assert release_info.repo == "test/repo"
        assert hasattr(release_info, "version")
        assert hasattr(release_info, "author")
        assert hasattr(release_info, "date")
        assert hasattr(release_info, "summary")
        assert hasattr(release_info, "url")
