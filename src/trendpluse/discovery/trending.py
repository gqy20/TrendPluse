"""GitHub Trending 项目采集器

使用 GitHub Search API 模拟 Trending 功能，发现热门项目。
"""

from datetime import datetime, timedelta
from typing import Literal

from github import Github

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)


class TrendingCollector:
    """采集 GitHub Trending 项目

    使用 GitHub Search API 组合搜索条件模拟 Trending 效果。
    """

    def __init__(self, github_token: str) -> None:
        """初始化 Trending 采集器

        Args:
            github_token: GitHub 访问令牌
        """
        self.github_token = github_token
        self.client = Github(github_token)

    def discover(
        self,
        languages: list[str] | None = None,
        days: int = 7,
        min_stars: int = 1000,
        max_results: int = 30,
    ) -> list[DiscoveredProject]:
        """发现 Trending 项目

        Args:
            languages: 编程语言列表，默认 ["python", "typescript", "go"]
            days: 回溯天数，默认 7 天
            min_stars: 最低 star 数，默认 1000
            max_results: 每种语言最多返回结果数，默认 30

        Returns:
            发现的项目列表
        """
        if languages is None:
            languages = ["python", "typescript", "go"]

        candidates = []
        since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        for lang in languages:
            query = f"language:{lang} stars:>{min_stars} pushed:>={since}"

            logger.debug(f"搜索 Trending 项目: {query}")

            try:
                repos = self.client.search_repositories(
                    query=query,
                    sort="stars",
                    order="desc",
                )

                # 限制每种语言的结果数量
                count = 0
                for repo in repos:
                    if count >= max_results:
                        break
                    project = self._convert_to_discovered(repo, "trending")
                    candidates.append(project)
                    count += 1

            except Exception as e:
                logger.error(f"搜索 {lang} Trending 项目失败: {e}")
                continue

        logger.info(f"发现 {len(candidates)} 个 Trending 候选项目")
        return candidates

    def _convert_to_discovered(
        self,
        repo,
        source: Literal["trending", "keyword", "related"],
    ) -> DiscoveredProject:
        """转换 GitHub Repository 对象为 DiscoveredProject

        Args:
            repo: PyGithub Repository 对象
            source: 发现来源

        Returns:
            DiscoveredProject 对象
        """
        # 处理 license
        license_name = None
        if repo.license:
            license_name = repo.license.name if repo.license.name else None

        # 处理 topics
        topics = []
        try:
            if repo.topics:
                topics = list(repo.topics)
        except Exception:
            # get_topics() 可能失败，返回空列表
            try:
                topics = list(repo.get_topics()) if repo.get_topics else []
            except Exception:
                topics = []

        return DiscoveredProject(
            repo=repo.full_name,
            name=repo.name,
            description=repo.description or "",
            stars=repo.stargazers_count,
            language=repo.language or "Unknown",
            topics=topics,
            license=license_name,
            open_issues=repo.open_issues_count,
            forks=repo.forks_count,
            watchers=repo.watchers_count,
            last_commit_at=repo.pushed_at,
            discovery_source=source,
            discovery_reason=f"Trending in {repo.language or 'Unknown'}",
        )
