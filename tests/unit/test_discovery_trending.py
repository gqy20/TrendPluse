"""TrendingCollector 测试

测试 GitHub Trending 项目采集功能。
"""

from datetime import datetime, timedelta
from unittest.mock import Mock, patch

import pytest

from trendpluse.discovery.trending import TrendingCollector
from trendpluse.models.discovery import DiscoveredProject


class TestTrendingCollector:
    """TrendingCollector 测试"""

    @pytest.fixture
    def mock_github(self):
        """Mock GitHub 客户端"""
        with patch("trendpluse.discovery.trending.Github") as mock:
            yield mock

    @pytest.fixture
    def sample_repo(self):
        """示例 GitHub 仓库对象"""
        repo = Mock()
        repo.full_name = "test-owner/test-repo"
        repo.name = "test-repo"
        repo.description = "A test repository"
        repo.stargazers_count = 5000
        repo.language = "Python"
        repo.topics = ["ai", "ml", "agent"]
        repo.license = Mock()
        repo.license.name = "MIT"
        repo.open_issues_count = 25
        repo.forks_count = 100
        repo.watchers_count = 50
        repo.pushed_at = datetime.now() - timedelta(days=2)
        return repo

    def test_init_with_token(self):
        """测试初始化"""
        collector = TrendingCollector(github_token="test_token")

        assert collector.github_token == "test_token"

    def test_discover_returns_list(self, mock_github, sample_repo):
        """测试 discover 返回列表"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        collector = TrendingCollector(github_token="test_token")
        results = collector.discover(languages=["python"], days=7)

        assert isinstance(results, list)
        assert len(results) == 1

    def test_discover_with_multiple_languages(self, mock_github, sample_repo):
        """测试多语言发现"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        collector = TrendingCollector(github_token="test_token")
        collector.discover(languages=["python", "typescript", "go"])

        # 应该调用 3 次 search
        assert mock_client.search_repositories.call_count == 3

    def test_convert_to_discovered_project(self, mock_github, sample_repo):
        """测试转换为 DiscoveredProject"""
        mock_github.return_value = Mock()

        collector = TrendingCollector(github_token="test_token")
        project = collector._convert_to_discovered(sample_repo, "trending")

        assert isinstance(project, DiscoveredProject)
        assert project.repo == "test-owner/test-repo"
        assert project.name == "test-repo"
        assert project.stars == 5000
        assert project.language == "Python"
        assert project.discovery_source == "trending"
        assert "Trending" in project.discovery_reason

    def test_discover_limits_results(self, mock_github, sample_repo):
        """测试结果数量限制"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        # 创建 40 个模拟仓库
        repos = []
        for i in range(40):
            repo = Mock()
            repo.full_name = f"owner/repo{i}"
            repo.name = f"repo{i}"
            repo.description = f"Repository {i}"
            repo.stargazers_count = 1000 + i * 100
            repo.language = "Python"
            repo.topics = []
            repo.license = None
            repo.open_issues_count = 10
            repo.forks_count = 20
            repo.watchers_count = 10
            repo.pushed_at = datetime.now() - timedelta(days=1)
            repos.append(repo)

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter(repos))
        mock_client.search_repositories.return_value = mock_search_result

        collector = TrendingCollector(github_token="test_token")
        results = collector.discover(languages=["python"], days=7)

        # 默认限制为 30
        assert len(results) == 30

    def test_search_query_construction(self, mock_github):
        """测试搜索查询构造"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        # 不返回任何结果
        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([]))
        mock_client.search_repositories.return_value = mock_search_result

        collector = TrendingCollector(github_token="test_token")
        collector.discover(languages=["python"], days=7)

        # 验证搜索参数
        call_args = mock_client.search_repositories.call_args
        args = call_args[0]  # 位置参数元组
        kwargs = call_args[1]  # 关键字参数字典

        query = args[0] if args else kwargs.get("query", "")

        assert "language:python" in query
        assert "stars:>1000" in query
        assert "pushed:>=" in query
        assert kwargs["sort"] == "stars"
        assert kwargs["order"] == "desc"

    def test_handles_missing_license(self, mock_github, sample_repo):
        """测试处理无许可证的项目"""
        sample_repo.license = None
        mock_github.return_value = Mock()

        collector = TrendingCollector(github_token="test_token")
        project = collector._convert_to_discovered(sample_repo, "trending")

        assert project.license is None

    def test_handles_empty_topics(self, mock_github, sample_repo):
        """测试处理空 topics 的项目"""
        sample_repo.topics = []
        mock_github.return_value = Mock()

        collector = TrendingCollector(github_token="test_token")
        project = collector._convert_to_discovered(sample_repo, "trending")

        assert project.topics == []

    def test_handles_none_topics(self, mock_github, sample_repo):
        """测试处理 None topics 的项目"""
        sample_repo.topics = None
        # 模拟 get_topics 返回空集合
        sample_repo.get_topics.return_value = set()
        mock_github.return_value = Mock()

        collector = TrendingCollector(github_token="test_token")
        project = collector._convert_to_discovered(sample_repo, "trending")

        assert project.topics == []


@pytest.mark.integration
@pytest.mark.skip(reason="需要真实 GitHub API，在 CI 中运行")
class TestTrendingCollectorIntegration:
    """TrendingCollector 集成测试"""

    @pytest.fixture
    def real_github_token(self):
        """获取真实的 GitHub token"""
        import os

        token = os.getenv("GITHUB_TOKEN")
        if not token:
            pytest.skip("GITHUB_TOKEN not set")
        return token

    def test_discover_real_repos(self, real_github_token):
        """测试发现真实仓库"""
        collector = TrendingCollector(github_token=real_github_token)
        results = collector.discover(languages=["python"], days=30)

        assert isinstance(results, list)
        assert len(results) > 0

        # 验证结果格式
        for project in results:
            assert isinstance(project, DiscoveredProject)
            assert "/" in project.repo
            assert project.stars > 0
            assert project.discovery_source == "trending"
