"""SDK 结构化输出统一封装。"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, TypeVar

from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


@dataclass
class QueryResult[T: BaseModel]:
    """查询结果封装。"""

    output: T
    session_id: str


class StructuredQuery[T: BaseModel]:
    """结构化输出封装，依赖 SDK 内置 ReAsk 重试。"""

    def __init__(
        self,
        output_model: type[T],
        *,
        model: str | None = None,
        allowed_tools: list[str] | None = None,
        max_turns: int = 50,
        max_budget_usd: float = 10.0,
        stderr_callback: Callable[[str], None] | None = None,
    ) -> None:
        self.output_model = output_model
        self.model = model
        self.allowed_tools = allowed_tools or ["Read"]
        self.max_turns = max_turns
        self.max_budget_usd = max_budget_usd
        self.stderr_callback = stderr_callback

    async def query_async(self, prompt: str) -> QueryResult[T]:
        """单次查询，依赖 SDK 内置 ReAsk 重试。"""
        options = ClaudeAgentOptions(
            model=self.model,
            allowed_tools=self.allowed_tools,
            output_format=self._build_output_format(),
            max_turns=self.max_turns,
            max_budget_usd=self.max_budget_usd,
            stderr=self.stderr_callback,
        )

        result_message: ResultMessage | None = None
        async for message in query(prompt=prompt, options=options):
            if isinstance(message, ResultMessage):
                result_message = message

        if result_message is None:
            raise RuntimeError("未收到 ResultMessage")

        if result_message.structured_output is None:
            raise RuntimeError(
                f"{self.output_model.__name__}: SDK 返回空 structured_output"
            )

        output = (
            self.output_model.model_validate_json(result_message.structured_output)
            if isinstance(result_message.structured_output, str)
            else self.output_model.model_validate(result_message.structured_output)
        )

        return QueryResult(output=output, session_id=result_message.session_id)

    def query(self, prompt: str) -> QueryResult[T]:
        """同步封装。"""
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            pass
        else:
            raise RuntimeError("检测到正在运行的事件循环，请改用 query_async()。")
        return asyncio.run(self.query_async(prompt))

    def _build_output_format(self) -> dict[str, Any]:
        """从 Pydantic 模型自动生成 output_format。"""
        return {
            "type": "json_schema",
            "schema": self.output_model.model_json_schema(),
        }
