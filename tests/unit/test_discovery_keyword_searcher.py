"""KeywordSearcher 测试

测试基于关键词搜索发现 GitHub 项目。
"""

from datetime import datetime, timedelta
from unittest.mock import Mock, patch

import pytest

from trendpluse.discovery.keyword_searcher import KeywordSearcher
from trendpluse.models.discovery import DiscoveredProject


class TestKeywordSearcher:
    """KeywordSearcher 测试"""

    @pytest.fixture
    def mock_github(self):
        """Mock GitHub 客户端"""
        with patch("trendpluse.discovery.keyword_searcher.Github") as mock:
            yield mock

    @pytest.fixture
    def sample_repo(self):
        """示例 GitHub 仓库对象"""
        repo = Mock()
        repo.full_name = "openai/agent-framework"
        repo.name = "agent-framework"
        repo.description = "An AI agent framework"
        repo.stargazers_count = 2500
        repo.language = "Python"
        repo.topics = ["agent", "ai"]
        repo.license = Mock()
        repo.license.name = "Apache-2.0"
        repo.open_issues_count = 15
        repo.forks_count = 50
        repo.watchers_count = 30
        repo.pushed_at = datetime.now() - timedelta(days=5)
        return repo

    def test_init_with_token(self):
        """测试初始化"""
        searcher = KeywordSearcher(github_token="test_token")

        assert searcher.github_token == "test_token"

    def test_init_with_keywords(self):
        """测试初始化带关键词"""
        keywords = ["AI agent", "LLM", "RAG"]
        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=keywords,
        )

        assert searcher.keywords == keywords

    def test_search_single_keyword(self, mock_github, sample_repo):
        """测试搜索单个关键词"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["AI agent"],
        )
        results = searcher.search()

        assert isinstance(results, list)
        assert len(results) == 1
        assert results[0].discovery_source == "keyword"

    def test_search_multiple_keywords(self, mock_github, sample_repo):
        """测试搜索多个关键词"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["AI agent", "LLM", "RAG"],
        )
        searcher.search()

        # 应该调用 3 次搜索
        assert mock_client.search_repositories.call_count == 3

    def test_search_uses_custom_min_stars(self, mock_github, sample_repo):
        """测试使用自定义最小 star 数"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["AI agent"],
            min_stars=500,
        )
        searcher.search()

        call_args = mock_client.search_repositories.call_args
        args = call_args[0]
        query = args[0] if args else call_args[1].get("query", "")

        assert "stars:>500" in query

    def test_search_query_construction(self, mock_github):
        """测试搜索查询构造"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["Claude"],
        )
        searcher.search(days=30)

        call_args = mock_client.search_repositories.call_args
        args = call_args[0]
        query = args[0] if args else call_args[1].get("query", "")

        # 验证查询包含关键词和时间范围
        assert "Claude" in query
        assert "pushed:>=" in query

    def test_aggregates_results_from_multiple_keywords(self, mock_github, sample_repo):
        """测试聚合多个关键词的结果"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        # 每次搜索返回不同的结果
        repo1 = Mock()
        repo1.full_name = "owner/repo1"
        repo1.name = "repo1"
        repo1.description = "Test 1"
        repo1.stargazers_count = 1000
        repo1.language = "Python"
        repo1.topics = []
        repo1.license = None
        repo1.open_issues_count = 5
        repo1.forks_count = 10
        repo1.watchers_count = 5
        repo1.pushed_at = datetime.now() - timedelta(days=1)

        repo2 = Mock()
        repo2.full_name = "owner/repo2"
        repo2.name = "repo2"
        repo2.description = "Test 2"
        repo2.stargazers_count = 2000
        repo2.language = "TypeScript"
        repo2.topics = []
        repo2.license = None
        repo2.open_issues_count = 8
        repo2.forks_count = 15
        repo2.watchers_count = 8
        repo2.pushed_at = datetime.now() - timedelta(days=2)

        # 第一次搜索返回 repo1，第二次返回 repo2
        call_count = [0]

        def mock_search(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                mock_result = Mock()
                mock_result.__iter__ = Mock(return_value=iter([repo1]))
                return mock_result
            else:
                mock_result = Mock()
                mock_result.__iter__ = Mock(return_value=iter([repo2]))
                return mock_result

        mock_client.search_repositories.side_effect = mock_search

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["keyword1", "keyword2"],
        )
        results = searcher.search()

        # 应该聚合两个搜索的结果
        assert len(results) == 2

    def test_handles_search_errors_gracefully(self, mock_github, sample_repo):
        """测试优雅处理搜索错误"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        # 第一次搜索成功，第二次失败，第三次成功
        call_count = [0]

        def mock_search(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 2:
                raise Exception("API Error")
            mock_result = Mock()
            mock_result.__iter__ = Mock(return_value=iter([sample_repo]))
            return mock_result

        mock_client.search_repositories.side_effect = mock_search

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["keyword1", "keyword2", "keyword3"],
        )
        results = searcher.search()

        # 应该跳过失败的搜索，返回成功的结果
        assert len(results) == 2

    def test_limits_results_per_keyword(self, mock_github):
        """测试每个关键词的结果数量限制"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        # 创建 50 个模拟仓库
        repos = []
        for i in range(50):
            repo = Mock()
            repo.full_name = f"owner/repo{i}"
            repo.name = f"repo{i}"
            repo.description = f"Repository {i}"
            repo.stargazers_count = 1000 + i * 10
            repo.language = "Python"
            repo.topics = []
            repo.license = None
            repo.open_issues_count = 5
            repo.forks_count = 10
            repo.watchers_count = 5
            repo.pushed_at = datetime.now() - timedelta(days=1)
            repos.append(repo)

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter(repos))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["AI agent"],
            max_results=20,
        )
        results = searcher.search()

        # 默认限制为 20
        assert len(results) == 20

    def test_sets_discovery_reason_with_keyword(self, mock_github, sample_repo):
        """测试设置发现原因为关键词"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(
            github_token="test_token",
            keywords=["Claude AI"],
        )
        results = searcher.search()

        assert results[0].discovery_reason == "Keyword: Claude AI"

    def test_default_keywords(self, mock_github, sample_repo):
        """测试默认关键词列表"""
        mock_client = Mock()
        mock_github.return_value = mock_client

        mock_search_result = Mock()
        mock_search_result.__iter__ = Mock(return_value=iter([sample_repo]))
        mock_client.search_repositories.return_value = mock_search_result

        searcher = KeywordSearcher(github_token="test_token")
        searcher.search()

        # 验证使用了默认关键词
        assert mock_client.search_repositories.call_count > 0


@pytest.mark.integration
@pytest.mark.skip(reason="需要真实 GitHub API，在 CI 中运行")
class TestKeywordSearcherIntegration:
    """KeywordSearcher 集成测试"""

    @pytest.fixture
    def real_github_token(self):
        """获取真实的 GitHub token"""
        import os

        token = os.getenv("GITHUB_TOKEN")
        if not token:
            pytest.skip("GITHUB_TOKEN not set")
        return token

    def test_search_real_repos(self, real_github_token):
        """测试搜索真实仓库"""
        searcher = KeywordSearcher(
            github_token=real_github_token,
            keywords=["Claude"],
            min_stars=100,
        )
        results = searcher.search(days=90)

        assert isinstance(results, list)
        assert len(results) > 0

        # 验证结果格式
        for project in results:
            assert isinstance(project, DiscoveredProject)
            assert "/" in project.repo
            assert project.stars >= 100
            assert project.discovery_source == "keyword"
