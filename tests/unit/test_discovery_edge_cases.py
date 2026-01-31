"""发现模块边界测试

补充边界和异常情况的测试。
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import Mock, patch

import pytest  # noqa: F401 (used for @pytest.mark)

from trendpluse.discovery.deduplicator import Deduplicator
from trendpluse.discovery.evaluator import QualityEvaluator
from trendpluse.discovery.keyword_searcher import KeywordSearcher
from trendpluse.discovery.trending import TrendingCollector
from trendpluse.models.discovery import DiscoveredProject


class TestEdgeCases:
    """边界情况测试"""

    def test_deduplicator_handles_empty_discovery_reason(self):
        """测试去重处理空的 discovery_reason"""
        evaluator = QualityEvaluator()
        deduplicator = Deduplicator()

        # 创建两个重复项目，第二个没有 discovery_reason
        project1 = DiscoveredProject(
            repo="owner/repo1",
            name="repo1",
            description="First",
            stars=1000,
            language="Python",
            topics=["ai"],
            license="MIT",
            open_issues=10,
            forks=50,
            watchers=20,
            last_commit_at=datetime.now(UTC) - timedelta(days=5),
            discovery_source="trending",
            discovery_reason="Trending",
        )

        project2 = DiscoveredProject(
            repo="owner/repo1",
            name="repo1",
            description="Second",
            stars=1100,
            language="Python",
            topics=["ai"],
            license="MIT",
            open_issues=12,
            forks=55,
            watchers=22,
            last_commit_at=datetime.now(UTC) - timedelta(days=3),
            discovery_source="keyword",
            discovery_reason="",  # 空 reason
        )

        evaluated = evaluator.evaluate([project1, project2])
        result = deduplicator.deduplicate(evaluated)

        assert len(result) == 1
        # 应该在 reason 中包含来源信息
        assert "[" in result[0].discovery_reason

    def test_evaluator_relevance_score_breaks_at_15(self):
        """测试相关性分数在 15 时提前退出"""
        evaluator = QualityEvaluator()

        # 创建包含多个相关关键词的项目
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="An AI agent framework with LLM and Claude support",
            stars=1000,
            language="Python",
            topics=["agent", "ai", "llm", "claude", "rag"],
            license="MIT",
            open_issues=10,
            forks=50,
            watchers=20,
            last_commit_at=datetime.now(UTC),
            discovery_source="keyword",
            discovery_reason="AI",
        )

        # 相关性分数应该在 15 以下封顶
        relevance_score = evaluator._calculate_relevance_score(project)
        assert relevance_score == 15

    def test_keyword_searcher_handles_topics_exception(self):
        """测试关键词搜索器处理 topics 异常"""
        with patch("trendpluse.discovery.keyword_searcher.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            # 创建一个会抛出异常的 repo 对象
            mock_repo = Mock()
            mock_repo.full_name = "owner/repo"
            mock_repo.name = "repo"
            mock_repo.description = "Test"
            mock_repo.stargazers_count = 1000
            mock_repo.language = "Python"
            mock_repo.license = None
            mock_repo.open_issues_count = 5
            mock_repo.forks_count = 10
            mock_repo.watchers_count = 5
            mock_repo.pushed_at = datetime.now(UTC)

            # topics 属性抛出异常
            type(mock_repo).topics = property(
                lambda self: (_ for _ in ()).throw(Exception("error"))
            )
            mock_repo.get_topics = Mock(return_value=["ai"])

            mock_search_result = Mock()
            mock_search_result.__iter__ = Mock(return_value=iter([mock_repo]))
            mock_client.search_repositories.return_value = mock_search_result

            searcher = KeywordSearcher(github_token="test_token")
            results = searcher.search()

            assert len(results) == 1
            # 应该回退到 get_topics 方法
            assert results[0].topics == ["ai"]

    def test_keyword_searcher_handles_all_topics_exceptions(self):
        """测试关键词搜索器处理所有 topics 方法异常"""
        with patch("trendpluse.discovery.keyword_searcher.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            mock_repo = Mock()
            mock_repo.full_name = "owner/repo"
            mock_repo.name = "repo"
            mock_repo.description = "Test"
            mock_repo.stargazers_count = 1000
            mock_repo.language = "Python"
            mock_repo.license = None
            mock_repo.open_issues_count = 5
            mock_repo.forks_count = 10
            mock_repo.watchers_count = 5
            mock_repo.pushed_at = datetime.now(UTC)

            # topics 和 get_topics 都抛出异常
            type(mock_repo).topics = property(
                lambda self: (_ for _ in ()).throw(Exception("error"))
            )
            mock_repo.get_topics = Mock(side_effect=Exception("error"))

            mock_search_result = Mock()
            mock_search_result.__iter__ = Mock(return_value=iter([mock_repo]))
            mock_client.search_repositories.return_value = mock_search_result

            searcher = KeywordSearcher(github_token="test_token")
            results = searcher.search()

            assert len(results) == 1
            # topics 应该是空列表
            assert results[0].topics == []

    def test_trending_uses_default_languages(self):
        """测试 Trending 使用默认语言列表"""
        with patch("trendpluse.discovery.trending.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            mock_search_result = Mock()
            mock_search_result.__iter__ = Mock(return_value=iter([]))
            mock_client.search_repositories.return_value = mock_search_result

            collector = TrendingCollector(github_token="test_token")
            # 不传 languages 参数
            collector.discover(languages=None, days=7)

            # 应该搜索 3 种语言
            assert mock_client.search_repositories.call_count == 3

    def test_trending_handles_search_errors_gracefully(self):
        """测试 Trending 优雅处理搜索错误"""
        with patch("trendpluse.discovery.trending.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            # 第一次搜索抛出异常
            call_count = [0]

            def mock_search(*args, **kwargs):
                call_count[0] += 1
                if call_count[0] == 1:
                    raise Exception("API Error")
                mock_result = Mock()
                mock_result.__iter__ = Mock(return_value=iter([]))
                return mock_result

            mock_client.search_repositories.side_effect = mock_search

            collector = TrendingCollector(github_token="test_token")
            # 不使用 results 变量，只调用discover
            collector.discover(languages=["python", "typescript"], days=7)

            # 第二个语言应该成功
            assert mock_client.search_repositories.call_count == 2

    def test_trending_handles_topics_exception(self):
        """测试 Trending 处理 topics 异常"""
        with patch("trendpluse.discovery.trending.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            mock_repo = Mock()
            mock_repo.full_name = "owner/repo"
            mock_repo.name = "repo"
            mock_repo.description = "Test"
            mock_repo.stargazers_count = 1000
            mock_repo.language = "Python"
            mock_repo.license = Mock()
            mock_repo.license.name = "MIT"
            mock_repo.open_issues_count = 5
            mock_repo.forks_count = 10
            mock_repo.watchers_count = 5
            mock_repo.pushed_at = datetime.now(UTC)

            # topics 属性抛出异常
            type(mock_repo).topics = property(
                lambda self: (_ for _ in ()).throw(Exception("error"))
            )
            mock_repo.get_topics = Mock(return_value=["ai"])

            mock_search_result = Mock()
            mock_search_result.__iter__ = Mock(return_value=iter([mock_repo]))
            mock_client.search_repositories.return_value = mock_search_result

            collector = TrendingCollector(github_token="test_token")
            results = collector.discover(languages=["python"], days=7)

            assert len(results) == 1
            assert results[0].topics == ["ai"]

    def test_trending_handles_all_topics_methods_exception(self):
        """测试 Trending 处理所有 topics 方法异常"""
        with patch("trendpluse.discovery.trending.Github") as mock_github:
            mock_client = Mock()
            mock_github.return_value = mock_client

            mock_repo = Mock()
            mock_repo.full_name = "owner/repo"
            mock_repo.name = "repo"
            mock_repo.description = "Test"
            mock_repo.stargazers_count = 1000
            mock_repo.language = "Python"
            mock_repo.license = Mock()
            mock_repo.license.name = "MIT"
            mock_repo.open_issues_count = 5
            mock_repo.forks_count = 10
            mock_repo.watchers_count = 5
            mock_repo.pushed_at = datetime.now(UTC)

            # topics 和 get_topics 都抛出异常
            type(mock_repo).topics = property(
                lambda self: (_ for _ in ()).throw(Exception("error"))
            )
            mock_repo.get_topics = Mock(side_effect=Exception("error"))

            mock_search_result = Mock()
            mock_search_result.__iter__ = Mock(return_value=iter([mock_repo]))
            mock_client.search_repositories.return_value = mock_search_result

            collector = TrendingCollector(github_token="test_token")
            results = collector.discover(languages=["python"], days=7)

            assert len(results) == 1
            # topics 应该是空列表
            assert results[0].topics == []

    def test_evaluator_calculate_relevance_description_exact_match(self):
        """测试相关性计算 - 描述精确匹配"""
        evaluator = QualityEvaluator()

        # 描述中包含多个关键词
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="AI agent LLM Claude agent agent agent",  # 多个关键词
            stars=1000,
            language="Python",
            topics=["agent"],
            license="MIT",
            open_issues=10,
            forks=50,
            watchers=20,
            last_commit_at=datetime.now(UTC),
            discovery_source="keyword",
            discovery_reason="AI",
        )

        score = evaluator._calculate_relevance_score(project)

        # topic 5 分 + 描述中至少 5 个 agent 关键词 (5*3=15) 但上限 15 分
        assert score == 15

    def test_large_scale_deduplication(self):
        """测试大规模去重性能"""
        evaluator = QualityEvaluator()
        deduplicator = Deduplicator()

        # 创建 100 个项目，包含一些重复
        projects = []
        for i in range(100):
            if i % 3 == 0:
                # 每 3 个有一个重复
                repo = "owner/repo1"
            else:
                repo = f"owner/repo{i}"

            projects.append(
                DiscoveredProject(
                    repo=repo,
                    name=repo.split("/")[1],
                    description=f"Project {i}",
                    stars=100 + i * 10,
                    language="Python",
                    topics=[],
                    license="MIT",
                    open_issues=5,
                    forks=10,
                    watchers=5,
                    last_commit_at=datetime.now(UTC) - timedelta(days=i % 30),
                    discovery_source="keyword",
                    discovery_reason=f"Keyword{i}",
                )
            )

        evaluated = evaluator.evaluate(projects)
        result = deduplicator.deduplicate(evaluated)

        # 100 个项目，33 个 owner/repo1 重复
        # 去重后应该剩余 68 个 (100 - 32 重复)
        assert len(result) < 100
        assert len(result) > 50

    def test_evaluator_all_zero_scores(self):
        """测试所有维度都是 0 分的情况"""
        evaluator = QualityEvaluator()

        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="",  # 无描述
            stars=10,  # 低 star
            language="Unknown",
            topics=[],  # 无 topics
            license=None,  # 无 license
            open_issues=0,
            forks=0,
            watchers=0,
            last_commit_at=datetime.now(UTC) - timedelta(days=365),  # 很久没更新
            discovery_source="keyword",
            discovery_reason="Test",
        )

        evaluated = evaluator.evaluate([project])
        assert evaluated[0].quality_score >= 0
        assert evaluated[0].recommendation_priority == "low"

    def test_evaluator_perfect_scores(self):
        """测试所有维度都是满分的情况"""
        evaluator = QualityEvaluator()

        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="AI agent LLM Claude",  # 相关描述
            stars=20000,  # 高 star
            language="Python",
            topics=["agent", "ai", "llm", "claude", "rag"],  # 相关 topics
            license="MIT",
            open_issues=50,
            forks=500,
            watchers=200,
            last_commit_at=datetime.now(UTC),  # 最近更新
            discovery_source="trending",
            discovery_reason="Trending",
        )

        evaluated = evaluator.evaluate([project])
        # 应该获得很高的分数
        assert evaluated[0].quality_score >= 80
        assert evaluated[0].recommendation_priority == "high"
