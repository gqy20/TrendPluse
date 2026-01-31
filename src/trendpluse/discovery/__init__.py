"""项目发现模块

自动发现热门 GitHub 项目的模块。
"""

from trendpluse.discovery.base import BaseDiscoverer
from trendpluse.discovery.classifier import ProjectClassifier
from trendpluse.discovery.deduplicator import Deduplicator
from trendpluse.discovery.dynamic_evaluator import DynamicThresholdEvaluator
from trendpluse.discovery.evaluator import QualityEvaluator
from trendpluse.discovery.highlight_analyzer import ProjectHighlightAnalyzer
from trendpluse.discovery.keyword_searcher import KeywordSearcher
from trendpluse.discovery.reporter import DiscoveryReporter
from trendpluse.discovery.trending import TrendingCollector

__all__ = [
    "BaseDiscoverer",
    "TrendingCollector",
    "KeywordSearcher",
    "QualityEvaluator",
    "DynamicThresholdEvaluator",
    "Deduplicator",
    "DiscoveryReporter",
    "ProjectHighlightAnalyzer",
    "ProjectClassifier",
]
