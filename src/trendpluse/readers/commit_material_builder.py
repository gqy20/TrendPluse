"""Commit 分析材料构建器。"""

from typing import Any

from trendpluse.models.source import AnalysisMaterial


class CommitMaterialBuilder:
    """将 commit 明细转换为统一分析材料。"""

    @staticmethod
    def build(detailed_commits: list[dict[str, Any]]) -> list[AnalysisMaterial]:
        """将 commit 明细转换为分析材料。"""
        return [
            AnalysisMaterial.from_commit_details(commit) for commit in detailed_commits
        ]
