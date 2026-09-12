"""事件筛选器

从 GH Archive 事件中筛选出值得深入分析的候选事件。

只做**配置级过滤**（merged 状态/标签/改动规模——语义明确的路由规则），
不做数量截断：重要性判断交给下游 AI（SDK agent 读全量文件自行取舍）。
数量异常时仅告警不丢数据。
"""

from trendpluse.logger import get_logger

logger = get_logger(__name__)


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

    # 单日候选数异常熔断阈值（正常日 <50）。超过只告警不截断——
    # 通常是监控仓库异常（被刷 PR 等），需要人来判断而非静默丢数据
    ANOMALY_THRESHOLD = 2000

    def __init__(
        self,
        labels: list[str] | None = None,
        enable_open_prs: bool = False,
        open_pr_min_changed_files: int = 3,
    ):
        """初始化筛选器

        Args:
            labels: 候选标签列表，None 表示使用默认标签
            enable_open_prs: 是否包含 open PR（默认 False，只包含已合并的）
            open_pr_min_changed_files: open PR 最小改动文件数（默认 3）
        """
        self.labels = set(labels) if labels else self.CANDIDATE_LABELS
        self.enable_open_prs = enable_open_prs
        self.open_pr_min_changed_files = open_pr_min_changed_files

    def filter_candidates(self, events: list[dict]) -> list[dict]:
        """筛选候选事件（配置级过滤，无数量截断）

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

                    # 检查改动规模（采集层仅对 open PR 读取，可能为 None）
                    changed_files = pr.get("changed_files") or 0
                    if changed_files < self.open_pr_min_changed_files:
                        continue

                    # 检查标签（如果有标签，必须匹配候选标签）
                    pr_labels = pr.get("labels", [])
                    if pr_labels:
                        pr_label_names = {label.get("name") for label in pr_labels}
                        if not (self.labels & pr_label_names):
                            continue

                    candidates.append(event)

        # 不做数量截断：重要性判断由下游 AI 基于全量信息做出。
        # 仅在数量异常（可能是刷量/配置错误）时告警。
        if len(candidates) > self.ANOMALY_THRESHOLD:
            logger.warning(
                "候选事件数量异常: %d 个（阈值 %d），可能是监控仓库被刷量"
                "或配置错误，请人工核查（不截断，全量透传下游）",
                len(candidates),
                self.ANOMALY_THRESHOLD,
            )
        return candidates
