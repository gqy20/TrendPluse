"""数据采集器模块"""

from trendpluse.collectors.base import BaseGitHubCollector
from trendpluse.collectors.issue_snapshot import IssueSnapshot

__all__ = ["BaseGitHubCollector", "IssueSnapshot"]
