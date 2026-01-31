"""Issue 分析快照管理

确保同一 Issue 只被分析一次，使用基于 ID 的精确去重。

快照格式（按 Issue #39 要求）:
```json
{
  "date": "2026-01-28",
  "analyzed_count": 100,
  "analyzed_issues": [
    {"repo": "owner/repo", "issue_id": 1234, "categories": ["bug"]}
  ]
}
```
"""

import json
from pathlib import Path
from typing import Any


class IssueSnapshot:
    """Issue 分析快照管理器

    管理已分析的 Issue IDs，防止重复分析同一 Issue。
    """

    def __init__(self, snapshot_dir: str = "data/issue_snapshots"):
        """初始化快照管理器

        Args:
            snapshot_dir: 快照存储目录
        """
        self.snapshot_dir = Path(snapshot_dir)
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)

    def load_analyzed_ids(self, date: str) -> set[tuple[str, int]]:
        """加载已分析的 Issue IDs

        Args:
            date: 快照日期 (YYYY-MM-DD)，空字符串返回空集合

        Returns:
            {(repo, issue_id), ...} 集合
        """
        # 空日期直接返回空集合
        if not date:
            return set()

        snapshot_path = self.snapshot_dir / f"{date}.json"

        if not snapshot_path.exists():
            return set()

        with open(snapshot_path) as f:
            data = json.load(f)

        # 按 Issue #39 要求的格式解析
        return {
            (item["repo"], item["issue_id"]) for item in data.get("analyzed_issues", [])
        }

    def save(
        self,
        date: str,
        analyzed_issues: list[dict[str, Any]],
    ) -> None:
        """保存快照

        Args:
            date: 快照日期 (YYYY-MM-DD)
            analyzed_issues: 已分析的 Issue 列表
                [{"repo": "owner/repo", "issue_id": 1234, "categories": ["bug"]}, ...]
        """
        snapshot_path = self.snapshot_dir / f"{date}.json"

        snapshot_data = {
            "date": date,
            "analyzed_count": len(analyzed_issues),
            "analyzed_issues": analyzed_issues,
        }

        with open(snapshot_path, "w") as f:
            json.dump(snapshot_data, f, indent=2, ensure_ascii=False)

    def get_available_dates(self) -> list[str]:
        """获取所有可用的快照日期

        Returns:
            日期字符串列表 (YYYY-MM-DD)，按日期倒序排序
        """
        if not self.snapshot_dir.exists():
            return []

        dates = []
        for path in self.snapshot_dir.glob("*.json"):
            # 只处理 JSON 文件，文件名即为日期
            dates.append(path.stem)  # 文件名不含 .json

        # 按日期倒序排列
        return sorted(dates, reverse=True)
