"""Issue 分析 Agent（Claude Agent SDK）"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path


class IssueAgentRunner:
    """使用 Claude Agent SDK 分析 Issue 文件"""

    def __init__(self, model: str | None = None) -> None:
        self.model = model

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

        response_text = await self._run_agent_query(prompt)
        output_path.write_text(response_text, encoding="utf-8")
        return response_text

    async def _run_agent_query(self, prompt: str) -> str:
        try:
            from claude_agent_sdk import (  # type: ignore
                AssistantMessage,
                ClaudeAgentOptions,
                query,
            )
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
