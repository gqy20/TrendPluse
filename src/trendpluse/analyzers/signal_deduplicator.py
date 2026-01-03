"""信号去重器

使用大模型判断信号是否重复，基于语义而非简单字符串匹配。
"""

import hashlib
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from trendpluse.models.signal import Signal


class SignalDeduplicator:
    """信号去重器

    使用大模型分析信号内容，判断是否与历史信号重复。
    """

    def __init__(
        self,
        llm_client,
        lookback_days: int = 7,
        history_path: str = "data/signal_history.json",
    ):
        """初始化去重器

        Args:
            llm_client: Anthropic 客户端
            lookback_days: 历史信号时间窗口（天）
            history_path: 历史信号存储路径
        """
        self.llm_client = llm_client
        self.lookback_days = lookback_days
        self.history_path_str = history_path
        self.history_path = Path(history_path)
        self.history_path.parent.mkdir(parents=True, exist_ok=True)

    def compute_fingerprint(self, signal: Signal) -> str:
        """计算信号指纹

        用于快速过滤明显相同或不同的信号。

        Args:
            signal: 信号对象

        Returns:
            信号指纹（MD5 hash）
        """
        # 标准化标题：小写 + 去除空格和标点
        normalized_title = signal.title.lower()
        normalized_title = "".join(c for c in normalized_title if c.isalnum())

        # 指纹 = 仓库 + 类型 + 标准化标题
        repo = signal.related_repos[0] if signal.related_repos else "unknown"
        fingerprint_data = f"{repo}:{signal.type}:{normalized_title}"

        return hashlib.md5(fingerprint_data.encode()).hexdigest()

    def deduplicate(self, signals: list[Signal]) -> list[Signal]:
        """对信号列表去重

        Args:
            signals: 原始信号列表

        Returns:
            去重后的信号列表
        """
        # 加载历史信号
        history = self._load_history()

        # 过滤旧信号
        recent_history = self._filter_old_signals(history)

        # 去重
        unique_signals = []
        seen_signals = set()  # 记录已处理的信号指纹

        for signal in signals:
            fingerprint = self.compute_fingerprint(signal)

            # 检查是否在当前批次中已存在
            if fingerprint in seen_signals:
                continue

            # 检查是否与历史重复
            if not self._is_duplicate(signal, recent_history):
                unique_signals.append(signal)
                seen_signals.add(fingerprint)

        # 保存到历史
        self._save_history(unique_signals)

        return unique_signals

    def _is_duplicate(self, signal: Signal, history: list[Signal]) -> bool:
        """判断信号是否重复

        Args:
            signal: 待判断的信号
            history: 历史信号列表

        Returns:
            True 如果重复，False 否则
        """
        fingerprint = self.compute_fingerprint(signal)

        # 阶段 1: 快速指纹匹配
        for existing in history:
            if self.compute_fingerprint(existing) == fingerprint:
                return True

        # 阶段 2: 查找相似标题（编辑距离 <= 2）
        similar_signals = self._find_similar_signals(signal, history)
        if similar_signals:
            # 阶段 3: LLM 深度判断
            return self._llm_check_duplicate(signal, similar_signals)

        return False

    def _find_similar_signals(
        self, signal: Signal, history: list[Signal]
    ) -> list[Signal]:
        """查找标题相似的信号

        Args:
            signal: 待判断的信号
            history: 历史信号列表

        Returns:
            相似信号列表
        """
        similar = []
        for existing in history:
            # 计算编辑距离
            distance = self._edit_distance(signal.title, existing.title)
            if distance <= 2:  # 标题相似
                similar.append(existing)
        return similar

    def _edit_distance(self, s1: str, s2: str) -> int:
        """计算编辑距离（Levenshtein 距离）

        Args:
            s1: 字符串 1
            s2: 字符串 2

        Returns:
            编辑距离
        """
        if len(s1) < len(s2):
            return self._edit_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row: list[int] = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row: list[int] = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def _llm_check_duplicate(self, signal: Signal, history: list[Signal]) -> bool:
        """使用 LLM 判断是否重复

        Args:
            signal: 待判断的信号
            history: 相似的历史信号列表

        Returns:
            True 如果 LLM 判断为重复，False 否则
        """
        # 构建对比 Prompt
        history_text = "\n".join(
            f"- {s.title} (类型: {s.type}, 重要性: {s.why_it_matters})"
            for s in history[:3]  # 只对比最相似的 3 个
        )

        prompt = f"""你是一个技术趋势分析专家。判断以下新信号是否与历史信号重复。

## 新信号
标题: {signal.title}
类型: {signal.type}
重要性: {signal.why_it_matters}

## 历史信号（相似标题）
{history_text}

## 判断标准
- 如果描述的是同一个技术趋势/特性，判定为"重复"
- 如果是不同的改进或新特性，判定为"不重复"
- 标题微调但本质相同 → 重复
- 类型或特性不同 → 不重复

## 回答格式
只回答一个词：
- DUPLICATE（重复）
- UNIQUE（不重复）
"""

        # 调用 LLM
        message = self.llm_client.messages.create(
            model="glm-4.7",
            max_tokens=10,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )

        response = message.content[0].text.strip().upper()

        return "DUPLICATE" in response

    def _load_history(self) -> list[Signal]:
        """加载历史信号

        Returns:
            历史信号列表
        """
        data = self._load_history_dict()

        signals = []
        for item in data.get("signals", []):
            # 提取 timestamp
            timestamp = item.pop("timestamp", None)
            signal = Signal(**item)
            # 存储 timestamp 在内部字典中
            signal._timestamp = timestamp  # type: ignore[attr-defined]
            signals.append(signal)

        return signals

    def _save_history(self, new_signals: list[Signal]) -> None:
        """保存信号到历史

        Args:
            new_signals: 新的信号列表
        """
        # 加载现有历史
        history = self._load_history_dict()

        # 添加时间戳并保存
        timestamp = datetime.now(UTC).isoformat()
        for signal in new_signals:
            signal_dict = signal.model_dump()
            signal_dict["timestamp"] = timestamp
            history["signals"].append(signal_dict)

        # 更新元数据
        history["last_updated"] = timestamp
        history["count"] = len(history["signals"])

        # 保存
        with open(self.history_path, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

    def _load_history_dict(self) -> dict[str, Any]:
        """加载历史信号字典

        Returns:
            历史信号字典
        """
        if not self.history_path.exists():
            return {"signals": [], "last_updated": None, "count": 0}

        try:
            with open(self.history_path) as f:
                data: dict[str, Any] = json.load(f)
                return data
        except (json.JSONDecodeError, KeyError, TypeError):
            return {"signals": [], "last_updated": None, "count": 0}

    def _filter_old_signals(self, signals: list[Signal]) -> list[Signal]:
        """过滤超过时间窗口的旧信号

        Args:
            signals: 信号列表

        Returns:
            过滤后的信号列表
        """
        cutoff_time = datetime.now(UTC) - timedelta(days=self.lookback_days)

        filtered = []
        for signal in signals:
            # 如果没有 _timestamp，视为最近
            timestamp_str = getattr(signal, "_timestamp", None)
            if timestamp_str is None:
                filtered.append(signal)
                continue

            try:
                timestamp = datetime.fromisoformat(timestamp_str)
                if timestamp >= cutoff_time:
                    filtered.append(signal)
            except (ValueError, TypeError):
                # 解析失败，保留
                filtered.append(signal)

        return filtered
