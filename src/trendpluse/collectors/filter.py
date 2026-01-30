"""事件筛选器

从 GH Archive 事件中筛选出值得深入分析的候选事件。
"""


class EventFilter:
    """事件筛选器

    从原始事件中筛选出：
    - 已合并的 PR（带特定标签）
    - 高质量的 open PR（可选）
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
        enable_open_prs: bool = False,
        open_pr_min_changed_files: int = 3,
    ):
        """初始化筛选器

        Args:
            labels: 候选标签列表，None 表示使用默认标签
            max_count: 最大返回数量
            enable_open_prs: 是否包含 open PR（默认 False，只包含已合并的）
            open_pr_min_changed_files: open PR 最小改动文件数（默认 3）
        """
        self.labels = set(labels) if labels else self.CANDIDATE_LABELS
        self.max_count = max_count
        self.enable_open_prs = enable_open_prs
        self.open_pr_min_changed_files = open_pr_min_changed_files

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

                # 已合并的 PR 直接通过
                if pr.get("merged", False):
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
                    continue

                # open PR 筛选（如果启用）
                if self.enable_open_prs and pr.get("state") == "open":
                    # 排除 draft PR
                    if pr.get("draft", False):
                        continue

                    # 检查改动规模
                    changed_files = pr.get("changed_files", 0)
                    if changed_files < self.open_pr_min_changed_files:
                        continue

                    # 检查标签（如果有标签，必须匹配候选标签）
                    pr_labels = pr.get("labels", [])
                    if pr_labels:
                        pr_label_names = {label.get("name") for label in pr_labels}
                        if not (self.labels & pr_label_names):
                            continue

                    candidates.append(event)

        # 限制数量
        return candidates[: self.max_count]
