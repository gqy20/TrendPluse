"""日报历史索引构建与读取。"""

from __future__ import annotations

import json
from pathlib import Path

from trendpluse.models.daily_summary import DailyHistoryEntry, DailyHistoryIndex


def load_daily_history_index(index_path: Path) -> DailyHistoryIndex:
    """从 JSON 文件加载历史日报索引。"""
    if not index_path.exists():
        return DailyHistoryIndex()
    content = index_path.read_text(encoding="utf-8")
    return DailyHistoryIndex.model_validate_json(content)


class DailyHistoryIndexBuilder:
    """从日报 JSON 生成轻量历史索引。"""

    def __init__(self, *, reports_dir: Path, index_path: Path) -> None:
        self.reports_dir = reports_dir
        self.index_path = index_path

    def build(self) -> DailyHistoryIndex:
        """扫描历史日报并持久化索引。"""
        entries: list[DailyHistoryEntry] = []
        if self.reports_dir.exists():
            for json_path in sorted(self.reports_dir.glob("report-*.json")):
                entry = self._build_entry(json_path)
                if entry is not None:
                    entries.append(entry)

        result = DailyHistoryIndex(total_reports=len(entries), entries=entries)
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.index_path.write_text(
            result.model_dump_json(indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return result

    def _build_entry(self, json_path: Path) -> DailyHistoryEntry | None:
        """从单日报文件提取索引条目。"""
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            return None

        activity = data.get("activity") or {}
        top_repos = [
            item.get("repo", "")
            for item in activity.get("top_repos", [])
            if isinstance(item, dict) and item.get("repo")
        ]
        stats = data.get("stats") or {}
        issue_insights = data.get("issue_insights") or {}
        return DailyHistoryEntry(
            date=str(data.get("date", "")),
            summary_brief=str(data.get("summary_brief", "")),
            engineering_titles=self._extract_titles(data.get("engineering_signals")),
            research_titles=self._extract_titles(data.get("research_signals")),
            release_titles=self._extract_titles(data.get("release_signals")),
            top_repos=top_repos,
            high_impact_signals=int(stats.get("high_impact_signals", 0) or 0),
            signal_count=int(stats.get("total_signals", 0) or 0),
            issue_summary_brief=issue_insights.get("summary_brief"),
        )

    @staticmethod
    def _extract_titles(signals: object) -> list[str]:
        """提取信号标题列表。"""
        if not isinstance(signals, list):
            return []
        return [
            str(item.get("title"))
            for item in signals
            if isinstance(item, dict) and item.get("title")
        ]
