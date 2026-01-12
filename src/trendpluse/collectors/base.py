"""GitHub Collector 基类

提供统一的 GitHub 客户端初始化和时区处理逻辑。
"""

from abc import ABC
from datetime import UTC, datetime

from github import Github


class BaseGitHubCollector(ABC):
    """GitHub Collector 基类

    提供统一的 GitHub 客户端初始化和时区处理逻辑。
    子类可以继承此类复用这些功能。

    Attributes:
        client: GitHub API 客户端
        token: GitHub API token（如果有）
    """

    def __init__(self, token: str = ""):
        """初始化 GitHub Collector 基类

        Args:
            token: GitHub API token（可选，无 token 时有严格的速率限制）
        """
        self.token = token
        if token:
            self.client = Github(login_or_token=token)
        else:
            # 无 token 时仍然可以访问公开仓库，但有速率限制
            self.client = Github()

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
