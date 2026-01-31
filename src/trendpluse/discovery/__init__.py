"""项目发现模块

自动发现热门 GitHub 项目的模块。
"""

from trendpluse.discovery.base import BaseDiscoverer
from trendpluse.discovery.trending import TrendingCollector

__all__ = ["BaseDiscoverer", "TrendingCollector"]
