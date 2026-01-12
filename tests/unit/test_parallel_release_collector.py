"""并行 ReleaseCollector 单元测试

测试使用并行方式采集 Release 数据。
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock, patch

import pytest

from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.models.signal import ReleasesData


class TestParallelReleaseCollector:
    """并行 ReleaseCollector 测试"""

    @pytest.fixture
    def collector(self):
        """创建 ReleaseCollector 实例"""
        return ReleaseCollector(token="test-token")

    @pytest.fixture
    def mock_release_factory(self):
        """创建 mock release 工厂函数"""

        def _make_release(tag: str, hours_ago: int = 1):
            release = Mock()
            release.created_at = datetime.now(UTC) - timedelta(hours=hours_ago)
            release.prerelease = False
            release.tag_name = tag
            release.title = f"Release {tag}"
            release.body = f"Body for {tag}"
            release.html_url = f"https://github.com/test/repo/releases/{tag}"
            release.assets = []
            release.author = Mock()
            release.author.login = "testuser"
            release.published_at = datetime.now(UTC) - timedelta(hours=hours_ago)
            return release

        return _make_release

    @pytest.fixture
    def mock_repo_factory(self, mock_release_factory):
        """创建 mock repository 工厂函数"""

        def _make_repo(repo_name: str, num_releases: int = 2):
            repo = Mock()
            releases = [
                mock_release_factory(f"v1.0.{i}", i) for i in range(num_releases)
            ]
            repo.get_releases.return_value = releases
            return repo

        return _make_repo

    def test_collect_releases_parallel_handles_multiple_repos(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应正确处理多个仓库"""
        # Arrange
        repos = [f"test/repo{i}" for i in range(3)]
        since = datetime.now(UTC) - timedelta(hours=5)

        mock_repos = {repo: mock_repo_factory(repo, 3) for repo in repos}

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = lambda name: mock_repos[name]

            # Act
            releases_data, detailed_releases = collector.collect_releases_parallel(
                repos, since
            )

        # Assert
        assert isinstance(releases_data, ReleasesData)
        assert releases_data.total_count == 9  # 3 repos * 3 releases
        assert releases_data.unique_repos_count == 3

    def test_collect_releases_parallel_filters_by_date(
        self, collector, mock_release_factory
    ):
        """测试：并行采集应按日期过滤"""
        # Arrange
        repos = ["test/repo"]
        since = datetime.now(UTC) - timedelta(hours=2)

        # 创建一些旧的和新的 releases
        old_release = mock_release_factory("v0.9.0", 5)  # 5 小时前
        new_release = mock_release_factory("v1.0.0", 1)  # 1 小时前

        mock_repo = Mock()
        mock_repo.get_releases.return_value = [old_release, new_release]

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            releases_data, detailed_releases = collector.collect_releases_parallel(
                repos, since
            )

        # Assert - 只应该返回新的 release
        assert releases_data.total_count == 1
        assert detailed_releases[0]["tag_name"] == "v1.0.0"

    def test_collect_releases_parallel_handles_api_errors(
        self, collector, mock_repo_factory
    ):
        """测试：并行采集应优雅处理 API 错误"""
        # Arrange
        repos = ["test/good", "test/bad", "test/also-good"]
        since = datetime.now(UTC) - timedelta(hours=5)

        mock_repos = {
            "test/good": mock_repo_factory("test/good", 2),
            "test/also-good": mock_repo_factory("test/also-good", 1),
        }

        def side_effect(name):
            if name == "test/bad":
                raise Exception("API Error")
            return mock_repos[name]

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.side_effect = side_effect

            # Act - 不应该抛出异常
            releases_data, detailed_releases = collector.collect_releases_parallel(
                repos, since
            )

        # Assert - 只有两个成功的仓库
        assert releases_data.total_count == 3  # 2 + 1 releases

    def test_collect_releases_parallel_excludes_prerelease_when_configured(
        self, collector, mock_release_factory
    ):
        """测试：当配置时应排除预发布版本"""
        # Arrange
        repos = ["test/repo"]
        since = datetime.now(UTC) - timedelta(hours=5)

        stable_release = mock_release_factory("v1.0.0", 1)
        stable_release.prerelease = False

        pre_release = mock_release_factory("v1.0.0-beta", 1)
        pre_release.prerelease = True

        mock_repo = Mock()
        mock_repo.get_releases.return_value = [stable_release, pre_release]

        with patch.object(collector, "client") as mock_client:
            mock_client.get_repo.return_value = mock_repo

            # Act
            releases_data, detailed_releases = collector.collect_releases_parallel(
                repos, since, include_prereleases=False
            )

        # Assert
        assert releases_data.total_count == 1
        assert detailed_releases[0]["prerelease"] is False
