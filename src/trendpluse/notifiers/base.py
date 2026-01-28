"""通知器抽象基类

定义所有通知器的通用接口。
"""

from abc import ABC, abstractmethod


class BaseNotifier(ABC):
    """通知器抽象基类

    所有通知器实现必须继承此类并实现 send 方法。
    """

    @abstractmethod
    def send(self, title: str, content: str, url: str | None = None) -> bool:
        """发送通知

        Args:
            title: 通知标题
            content: 通知内容
            url: 可选的跳转链接

        Returns:
            是否发送成功
        """
        ...
