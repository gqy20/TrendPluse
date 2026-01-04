"""通知模块

提供多种通知渠道的抽象和实现。
"""

from trendpluse.notifiers.base import BaseNotifier
from trendpluse.notifiers.feishu import FeishuNotifier

__all__ = ["BaseNotifier", "FeishuNotifier"]
