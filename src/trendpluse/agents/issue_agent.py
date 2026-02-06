"""Issue 分析 Agent（Claude Agent SDK）"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from trendpluse.models.issue_agent import IssueAgentReport

logger = logging.getLogger(__name__)


class IssueAgentRunner:
    """使用 Claude Agent SDK 分析 Issue 文件"""

    def __init__(
        self,
        model: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_seconds: float = 1.0,
    ) -> None:
        self.model = model
        self.retry_max_attempts = max(1, retry_max_attempts)
        self.retry_wait_seconds = max(0.0, retry_wait_seconds)

    async def analyze_file(self, input_path: Path, output_path: Path) -> str:
        """分析单个 JSONL 文件并写入 JSON 结果。"""
        input_path = input_path.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        prompt = (
            "你是一个 Issue 分析专家。请读取下面路径的 JSONL 文件，"
            "按 repo 聚合痛点并输出结构化 JSON：\n\n"
            f"文件路径: {input_path}\n\n"
            "要求：\n"
            "- 过滤公告/发布/推广类问题\n"
            "- 合并语义相近的痛点主题\n"
            "- 输出字段：top_pain_points（数组，元素含 topic/count/"
            "affected_repos/sample_urls）\n"
            "- 只输出 JSON，不要附加说明\n"
        )

        last_exc: Exception | None = None
        for attempt in range(1, self.retry_max_attempts + 1):
            try:
                response_text = await self._run_agent_query(prompt)
                validated = self._normalize_and_validate_output(response_text)
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

    async def analyze_directory(self, input_dir: Path, output_dir: Path) -> int:
        """分析目录下所有 JSONL 文件。

        Returns:
            成功写入的分析文件数量。
        """
        files = sorted(input_dir.glob("*.jsonl"))
        if not files:
            return 0

        output_dir.mkdir(parents=True, exist_ok=True)
        success_count = 0
        for input_path in files:
            output_path = output_dir / f"{input_path.stem}.analysis.json"
            await self.analyze_file(input_path, output_path)
            success_count += 1
        return success_count

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
