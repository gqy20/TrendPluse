"""通知模块

提供多种通知渠道的抽象和实现。
"""

from trendpluse.notifiers.base import BaseNotifier
from trendpluse.notifiers.feishu import FeishuNotifier
from trendpluse.notifiers.summary import ReportSummarizer

__all__ = ["BaseNotifier", "FeishuNotifier", "ReportSummarizer"]
