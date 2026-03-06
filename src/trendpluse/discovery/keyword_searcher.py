"""关键词搜索发现器

基于关键词搜索发现 GitHub 项目。
"""

from datetime import datetime, timedelta
from typing import Literal

from github import Github

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)

# 默认搜索关键词
DEFAULT_KEYWORDS = [
    "AI agent",
    "LLM",
    "Claude",
    "RAG",
    "vector database",
    "autonomous",
    "multi-agent",
]


class KeywordSearcher:
    """基于关键词搜索发现项目

    使用 GitHub Search API 根据关键词搜索相关项目。
    """

    def __init__(
        self,
        github_token: str,
        keywords: list[str] | None = None,
        min_stars: int = 500,
        max_results: int = 20,
    ) -> None:
        """初始化关键词搜索器

        Args:
            github_token: GitHub 访问令牌
            keywords: 搜索关键词列表，默认使用 DEFAULT_KEYWORDS
            min_stars: 最低 star 数，默认 500
            max_results: 每个关键词最多返回结果数，默认 20
        """
        self.github_token = github_token
        self.client = Github(github_token)
        self.keywords = keywords if keywords is not None else DEFAULT_KEYWORDS[:]
        self.min_stars = min_stars
        self.max_results = max_results

    def discover(self, days: int = 30) -> list[DiscoveredProject]:
        """发现项目。

        Args:
            days: 回溯天数，默认 30 天

        Returns:
            发现的项目列表
        """
        return self.search(days=days)

    def search(
        self,
        days: int = 30,
    ) -> list[DiscoveredProject]:
        """搜索项目

        Args:
            days: 回溯天数，默认 30 天

        Returns:
            发现的项目列表
        """
        candidates = []
        since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        for keyword in self.keywords:
            query = f"{keyword} stars:>{self.min_stars} pushed:>={since}"

            logger.debug(f"搜索关键词: {keyword}")

            try:
                repos = self.client.search_repositories(
                    query=query,
                    sort="stars",
                    order="desc",
                )

                # 限制结果数量
                count = 0
                for repo in repos:
                    if count >= self.max_results:
                        break
                    project = self._convert_to_discovered(
                        repo,
                        "keyword",
                        keyword,
                    )
                    candidates.append(project)
                    count += 1

            except Exception as e:
                logger.error(f"搜索关键词 '{keyword}' 失败: {e}")
                continue

        logger.info(f"通过关键词发现 {len(candidates)} 个候选项目")
        return candidates

    def _convert_to_discovered(
        self,
        repo,
        source: Literal["trending", "keyword", "related"],
        keyword: str,
    ) -> DiscoveredProject:
        """转换 GitHub Repository 对象为 DiscoveredProject

        Args:
            repo: PyGithub Repository 对象
            source: 发现来源
            keyword: 匹配的关键词

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
            discovery_reason=f"Keyword: {keyword}",
        )
