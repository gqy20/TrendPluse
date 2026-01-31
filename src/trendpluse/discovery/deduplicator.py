"""项目去重器

合并来自不同来源的重复项目。
"""

from collections import defaultdict

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)


class Deduplicator:
    """项目去重器

    基于仓库名称 (owner/repo) 去重，保留质量分数最高的版本。
    同时合并发现来源信息到 discovery_reason 中。
    """

    def deduplicate(
        self,
        projects: list[DiscoveredProject],
        return_count: bool = False,
    ) -> list[DiscoveredProject]:
        """去重项目列表

        Args:
            projects: 候选项目列表
            return_count: 如果为 True，返回 (列表, 去重数量) 元组（内部使用）

        Returns:
            去重后的项目列表
        """
        if not projects:
            return []

        # 按仓库名称分组
        grouped = defaultdict(list)
        for project in projects:
            grouped[project.repo].append(project)

        # 每组保留质量分数最高的
        deduplicated = []
        for repo, repo_projects in grouped.items():
            if len(repo_projects) == 1:
                deduplicated.append(repo_projects[0])
            else:
                # 多个版本，选择质量分数最高的
                best = max(repo_projects, key=lambda p: p.quality_score)

                # 收集所有来源信息
                sources = set()
                reasons = []
                for p in repo_projects:
                    sources.add(p.discovery_source)
                    if p.discovery_reason and p.discovery_reason not in reasons:
                        reasons.append(p.discovery_reason)

                # 在 discovery_reason 中记录所有来源
                if len(sources) > 1:
                    source_info = ", ".join(sorted(sources))
                    if best.discovery_reason:
                        best.discovery_reason = (
                            f"[{source_info}] {best.discovery_reason}"
                        )
                    else:
                        best.discovery_reason = f"[{source_info}]"

                deduplicated.append(best)

        removed_count = len(projects) - len(deduplicated)
        logger.info(
            f"去重完成: {len(projects)} -> {len(deduplicated)} "
            f"(移除 {removed_count} 个重复)"
        )

        return deduplicated

    def deduplicate_with_count(
        self,
        projects: list[DiscoveredProject],
    ) -> tuple[list[DiscoveredProject], int]:
        """去重项目列表并返回计数

        Args:
            projects: 候选项目列表

        Returns:
            (去重后的项目列表, 去重数量) 元组
        """
        result = self.deduplicate(projects)
        removed_count = len(projects) - len(result)
        return result, removed_count
