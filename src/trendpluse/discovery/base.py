"""项目发现器基类

定义所有发现器的抽象基类。
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from trendpluse.models.discovery import DiscoveredProject


class BaseDiscoverer(ABC):
    """发现器基类

    所有项目发现器必须继承此类并实现 discover() 方法。
    """

    def __init__(self, github_token: str) -> None:
        """初始化发现器

        Args:
            github_token: GitHub 访问令牌
        """
        self.github_token = github_token

    @abstractmethod
    def discover(self) -> "list[DiscoveredProject]":
        """发现项目

        子类必须实现此方法，返回发现的项目列表。

        Returns:
            发现的项目列表
        """
        raise NotImplementedError
