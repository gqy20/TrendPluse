"""GitHub Collector 基类

提供统一的 GitHub 客户端初始化和时区处理逻辑。
同时支持 REST API (PyGithub) 和 GraphQL API。
"""

from abc import ABC
from datetime import UTC, datetime
from typing import Any, cast

from github import Github
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


class BaseGitHubCollector(ABC):
    """GitHub Collector 基类

    提供统一的 GitHub 客户端初始化和时区处理逻辑。
    子类可以继承此类复用这些功能。

    Attributes:
        client: GitHub REST API 客户端 (PyGithub)
        graphql_client: GitHub GraphQL API 客户端
        token: GitHub API token（如果有）
    """

    def __init__(self, token: str = ""):
        """初始化 GitHub Collector 基类

        Args:
            token: GitHub API token（可选，无 token 时有严格的速率限制）
        """
        self.token = token

        # 初始化 REST API 客户端
        if token:
            self.client = Github(login_or_token=token)
        else:
            # 无 token 时仍然可以访问公开仓库，但有速率限制
            self.client = Github()

        # 初始化 GraphQL 客户端
        self.graphql_client = self._create_graphql_client(token)

    def _create_graphql_client(self, token: str) -> Client:
        """创建 GraphQL 客户端

        Args:
            token: GitHub API token

        Returns:
            GraphQL 客户端
        """
        if token:
            transport = RequestsHTTPTransport(
                url="https://api.github.com/graphql",
                headers={"Authorization": f"Bearer {token}"},
            )
        else:
            # 无 token 时的匿名请求
            transport = RequestsHTTPTransport(url="https://api.github.com/graphql")

        return Client(transport=transport, fetch_schema_from_transport=False)

    def execute_query(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        """执行 GraphQL 查询

        Args:
            query: GraphQL 查询字符串
            variables: 查询变量

        Returns:
            查询结果字典

        Raises:
            Exception: 查询失败时抛出异常
        """
        result = self.graphql_client.execute(gql(query), variable_values=variables)
        return result

    def get_rate_limit(self) -> dict[str, Any]:
        """获取当前 GraphQL API 速率限制状态

        Returns:
            速率限制信息字典，包含:
            - limit: 每小时总点数
            - remaining: 剩余点数
            - used: 已使用点数
            - resetAt: 重置时间
        """
        query = """
        query {
            viewer {
                login
            }
            rateLimit {
                limit
                remaining
                used
                resetAt
            }
        }
        """
        result = self.execute_query(query, {})
        rate_limit = result.get("rateLimit", {})
        return cast(dict[str, Any], rate_limit)

    def is_rate_limit_low(self, threshold: int = 100) -> bool:
        """检查速率限制是否接近阈值

        Args:
            threshold: 剩余点数阈值，低于此值返回 True

        Returns:
            True 如果剩余点数低于阈值，否则 False
        """
        rate_limit = self.get_rate_limit()
        return rate_limit["remaining"] < threshold

    @staticmethod
    def ensure_timezone_aware(dt: datetime) -> datetime:
        """确保 datetime 对象有时区信息

        如果 datetime 对象没有时区信息，则添加 UTC 时区。

        Args:
            dt: datetime 对象

        Returns:
            带有时区信息的 datetime 对象

        Example:
            >>> naive_dt = datetime(2026, 1, 12, 12, 0, 0)
            >>> aware_dt = BaseGitHubCollector.ensure_timezone_aware(naive_dt)
            >>> assert aware_dt.tzinfo == timezone.utc
        """
        if dt.tzinfo is None:
            return dt.replace(tzinfo=UTC)
        return dt
