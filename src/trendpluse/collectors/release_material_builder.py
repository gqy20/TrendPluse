"""Release 分析材料构建器。"""

from typing import Any

from trendpluse.models.source import AnalysisMaterial


class ReleaseMaterialBuilder:
    """将 release 明细转换为统一分析材料。"""

    @staticmethod
    def build(detailed_releases: list[dict[str, Any]]) -> list[AnalysisMaterial]:
        """将 release 明细转换为分析材料。"""
        return [
            AnalysisMaterial.from_release_details(release)
            for release in detailed_releases
        ]
