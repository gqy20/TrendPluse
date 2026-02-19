"""Issue 分析 Agent（Claude Agent SDK）"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from trendpluse.models.issue_agent import IssueAgentPainPoint, IssueAgentReport

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class IssueAgentBatchResult:
    """Issue Agent 批量分析统计。"""

    expected_files: int
    succeeded_files: int
    failed_files: int
    failed_samples: list[str]


class IssueAgentRunner:
    """使用 Claude Agent SDK 分析 Issue 文件"""

    def __init__(
        self,
        model: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_seconds: float = 1.0,
        review_confidence_threshold: float = 0.6,
    ) -> None:
        self.model = model
        self.retry_max_attempts = max(1, retry_max_attempts)
        self.retry_wait_seconds = max(0.0, retry_wait_seconds)
        self.review_confidence_threshold = min(
            1.0, max(0.0, review_confidence_threshold)
        )

    async def analyze_file(self, input_path: Path, output_path: Path) -> str:
        """分析单个 JSONL 文件并写入 JSON 结果。"""
        input_path = input_path.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        last_exc: Exception | None = None
        for attempt in range(1, self.retry_max_attempts + 1):
            try:
                validated = await self._run_three_round_analysis(input_path)
                normalized_text = json.dumps(
                    validated.model_dump(), ensure_ascii=False, indent=2
                )
                output_path.write_text(normalized_text, encoding="utf-8")
                return normalized_text
            except (ValidationError, ValueError) as exc:
                last_exc = exc
                if attempt >= self.retry_max_attempts:
                    break
                logger.warning(
                    "Issue Agent 输出校验失败，准备重试: attempt=%d/%d, error=%s",
                    attempt,
                    self.retry_max_attempts,
                    exc,
                )
                if self.retry_wait_seconds > 0:
                    await asyncio.sleep(self.retry_wait_seconds)
        assert last_exc is not None
        raise RuntimeError(
            f"Issue Agent 输出在 {self.retry_max_attempts} 次尝试后仍未通过校验"
        ) from last_exc

    async def _run_three_round_analysis(self, input_path: Path) -> IssueAgentReport:
        round1_prompt = self._build_round1_prompt(input_path)
        round1_text = await self._run_agent_query(round1_prompt)
        round1_data = self._parse_round_payload(round1_text, "candidate_pain_points")

        round2_prompt = self._build_round2_prompt(input_path, round1_data)
        round2_text = await self._run_agent_query(round2_prompt)
        round2_data = self._parse_round_payload(round2_text, "merged_pain_points")

        round3_prompt = self._build_round3_prompt(input_path, round2_data)
        round3_text = await self._run_agent_query(round3_prompt)
        round3_data = self._parse_json_like_text(round3_text)
        if not isinstance(round3_data, dict):
            raise ValueError("ROUND3 输出不是合法 JSON 对象")

        if "top_pain_points" in round3_data:
            return IssueAgentReport.model_validate(round3_data)

        reviewed = round3_data.get("reviewed_pain_points")
        if not isinstance(reviewed, list):
            raise ValueError("ROUND3 缺少 reviewed_pain_points 字段")

        return self._build_report_from_reviewed_points(reviewed)

    def _build_round1_prompt(self, input_path: Path) -> str:
        return (
            "[ROUND1] 你是 Issue 质量分析器。读取 JSONL 并做高召回抽取。\n\n"
            f"文件路径: {input_path}\n\n"
            "输出 JSON 字段：candidate_pain_points（数组），每项至少包含\n"
            "topic/count/affected_repos/sample_urls。\n"
            "要求：保留可能的候选痛点，宁可多，不要解释文字。"
        )

    def _build_round2_prompt(
        self, input_path: Path, round1_data: dict[str, Any]
    ) -> str:
        payload = json.dumps(round1_data, ensure_ascii=False)
        return (
            "[ROUND2] 你是 Issue 主题归一化分析器。请合并语义相近主题。\n\n"
            f"文件路径: {input_path}\n"
            f"ROUND1结果: {payload}\n\n"
            "输出 JSON 字段：merged_pain_points（数组），每项包含\n"
            "topic/count/affected_repos/sample_urls，可选 aliases。"
        )

    def _build_round3_prompt(
        self, input_path: Path, round2_data: dict[str, Any]
    ) -> str:
        payload = json.dumps(round2_data, ensure_ascii=False)
        return (
            "[ROUND3] 你是 Issue 审稿器。请对主题做保留判定和置信度打分。\n\n"
            f"文件路径: {input_path}\n"
            f"ROUND2结果: {payload}\n\n"
            "输出 JSON 字段：reviewed_pain_points（数组），每项包含\n"
            "topic/count/affected_repos/sample_urls/confidence/priority/keep，"
            "可选 review_reason。\n"
            "priority 仅允许 P0/P1/P2。"
        )

    def _parse_round_payload(self, text: str, key: str) -> dict[str, Any]:
        parsed = self._parse_json_like_text(text)
        if not isinstance(parsed, dict):
            raise ValueError(f"{key} 输出不是合法 JSON 对象")
        value = parsed.get(key)
        if not isinstance(value, list):
            raise ValueError(f"缺少字段: {key}")
        return parsed

    def _build_report_from_reviewed_points(
        self, reviewed_points: list[Any]
    ) -> IssueAgentReport:
        points: list[IssueAgentPainPoint] = []
        for raw in reviewed_points:
            if not isinstance(raw, dict):
                continue
            keep = bool(raw.get("keep", True))
            confidence_value = raw.get("confidence")
            confidence = (
                float(confidence_value)
                if isinstance(confidence_value, (int, float))
                else None
            )
            if not keep:
                continue
            if confidence is not None and confidence < self.review_confidence_threshold:
                continue

            topic = str(raw.get("topic", "")).strip()
            if not topic:
                continue

            count_raw = raw.get("count", 1)
            count = count_raw if isinstance(count_raw, int) and count_raw > 0 else 1

            affected_repos = raw.get("affected_repos")
            repos = (
                [str(item) for item in affected_repos if isinstance(item, str)]
                if isinstance(affected_repos, list)
                else []
            )

            sample_urls = raw.get("sample_urls")
            urls = (
                [str(item) for item in sample_urls if isinstance(item, str)]
                if isinstance(sample_urls, list)
                else []
            )

            aliases_raw = raw.get("aliases")
            aliases = (
                [str(item) for item in aliases_raw if isinstance(item, str)]
                if isinstance(aliases_raw, list)
                else []
            )

            priority_raw = raw.get("priority")
            priority = (
                str(priority_raw)
                if isinstance(priority_raw, str) and priority_raw in {"P0", "P1", "P2"}
                else None
            )
            review_reason = (
                str(raw.get("review_reason"))
                if isinstance(raw.get("review_reason"), str)
                else None
            )

            points.append(
                IssueAgentPainPoint(
                    topic=topic,
                    count=count,
                    affected_repos=repos,
                    sample_urls=urls,
                    aliases=aliases,
                    confidence=confidence,
                    priority=priority,
                    review_reason=review_reason,
                )
            )

        points.sort(key=lambda item: item.count, reverse=True)
        return IssueAgentReport(top_pain_points=points[:5])

    async def analyze_directory(
        self, input_dir: Path, output_dir: Path
    ) -> IssueAgentBatchResult:
        """分析目录下所有 JSONL 文件。

        Returns:
            批量分析统计。
        """
        files = sorted(input_dir.glob("*.jsonl"))
        if not files:
            return IssueAgentBatchResult(
                expected_files=0,
                succeeded_files=0,
                failed_files=0,
                failed_samples=[],
            )

        output_dir.mkdir(parents=True, exist_ok=True)
        success_count = 0
        failed_count = 0
        failed_samples: list[str] = []
        for input_path in files:
            output_path = output_dir / f"{input_path.stem}.analysis.json"
            try:
                await self.analyze_file(input_path, output_path)
                success_count += 1
            except Exception as exc:
                failed_count += 1
                if len(failed_samples) < 5:
                    failed_samples.append(input_path.name)
                logger.warning(
                    "Issue Agent 单文件分析失败: file=%s, error=%s",
                    input_path.name,
                    exc,
                )
        return IssueAgentBatchResult(
            expected_files=len(files),
            succeeded_files=success_count,
            failed_files=failed_count,
            failed_samples=failed_samples,
        )

    async def _run_agent_query(self, prompt: str) -> str:
        try:
            from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, query
        except Exception as exc:  # pragma: no cover - 仅在缺少依赖时触发
            raise RuntimeError(
                "未安装 claude-agent-sdk，请先安装依赖后再运行。"
            ) from exc

        options = ClaudeAgentOptions(
            model=self.model,
            allowed_tools=["Read"],
        )

        text_chunks: list[str] = []
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, AssistantMessage):
                text_chunks.append(self._extract_text_blocks(message.content))

        return "".join(text_chunks).strip()

    def _extract_text_blocks(self, content: Iterable[object]) -> str:
        parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
                continue
            if isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(str(block.get("text", "")))
                continue
            if hasattr(block, "text"):
                parts.append(str(getattr(block, "text")))
        return "".join(parts)

    def _normalize_and_validate_output(self, text: str) -> IssueAgentReport:
        parsed = self._parse_json_like_text(text)
        if not isinstance(parsed, dict):
            raise ValueError("Agent 输出不是合法 JSON 对象")
        return IssueAgentReport.model_validate(parsed)

    def _parse_json_like_text(self, text: str) -> dict[str, Any] | None:
        stripped = text.strip()
        if not stripped:
            return None

        direct = self._try_parse_json(stripped)
        if direct is not None:
            return direct

        fenced_match = re.search(
            r"```(?:json)?\s*(\{.*?\})\s*```",
            stripped,
            flags=re.DOTALL | re.IGNORECASE,
        )
        if fenced_match:
            fenced = self._try_parse_json(fenced_match.group(1))
            if fenced is not None:
                return fenced

        obj_text = self._extract_first_json_object(stripped)
        if obj_text:
            return self._try_parse_json(obj_text)
        return None

    def _try_parse_json(self, raw: str) -> dict[str, Any] | None:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return None
        if isinstance(data, dict):
            return data
        return None

    def _extract_first_json_object(self, text: str) -> str | None:
        start = text.find("{")
        if start < 0:
            return None
        depth = 0
        in_string = False
        escaped = False
        for idx in range(start, len(text)):
            ch = text[idx]
            if in_string:
                if escaped:
                    escaped = False
                elif ch == "\\":
                    escaped = True
                elif ch == '"':
                    in_string = False
                continue
            if ch == '"':
                in_string = True
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return text[start : idx + 1]
        return None
