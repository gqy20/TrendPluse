"""事件筛选器

从 GH Archive 事件中筛选出值得深入分析的候选事件。
"""
from typing import Any


class EventFilter:
    """事件筛选器

    从原始事件中筛选出：
    - 已合并的 PR（带特定标签）
    - Release 事件
    """

    # 候选标签：这些标签表明 PR 可能具有重要趋势信号
    CANDIDATE_LABELS = {
        "feature",
        "enhancement",
        "eval",
        "tooling",
        "agent",
        "workflow",
        "safety",
    }

    def __init__(
        self,
        labels: list[str] | None = None,
        max_count: int = 20,
    ):
        """初始化筛选器

        Args:
            labels: 候选标签列表，None 表示使用默认标签
            max_count: 最大返回数量
        """
        self.labels = set(labels) if labels else self.CANDIDATE_LABELS
        self.max_count = max_count

    def filter_candidates(self, events: list[dict]) -> list[dict]:
        """筛选候选事件

        Args:
            events: 原始事件列表

        Returns:
            候选事件列表
        """
        if not events:
            return []

        candidates = []

        for event in events:
            event_type = event.get("type")

            # Release 事件直接包含
            if event_type == "ReleaseEvent":
                candidates.append(event)
                continue

            # PR 事件需要筛选条件
            if event_type == "PullRequestEvent":
                pr = event.get("payload", {}).get("pull_request", {})

                # 必须已合并
                if not pr.get("merged", False):
                    continue

                # 检查标签匹配
                pr_labels = pr.get("labels", [])

                # 如果没有标签，直接包含
                if not pr_labels:
                    candidates.append(event)
                    continue

                # 如果有标签，检查是否匹配候选标签
                pr_label_names = {label.get("name") for label in pr_labels}
                if self.labels & pr_label_names:  # 交集非空
                    candidates.append(event)

        # 限制数量
        return candidates[: self.max_count]
