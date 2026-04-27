"""StructuredQuery 单元测试。"""

from __future__ import annotations

import asyncio
from typing import Literal
from unittest.mock import MagicMock, patch

import pytest
from pydantic import BaseModel, Field

from trendpluse.analyzers.structured_query import QueryResult, StructuredQuery

# ============ 测试模型 ============


class SampleOutput(BaseModel):
    """测试用输出模型。"""

    name: str = Field(description="名称")
    value: int = Field(ge=0, description="数值")
    status: Literal["active", "inactive"] = Field(description="状态")


class ComplexOutput(BaseModel):
    """复杂输出模型。"""

    title: str
    items: list[str] = Field(default_factory=list)
    metadata: dict[str, str] = Field(default_factory=dict)


# ============ QueryResult 测试 ============


class TestQueryResult:
    """QueryResult 数据类测试。"""

    def test_create_query_result(self):
        """能创建包含 output 和 session_id 的 QueryResult。"""
        output = SampleOutput(name="test", value=42, status="active")
        result = QueryResult(output=output, session_id="sess-123")

        assert result.output == output
        assert result.session_id == "sess-123"

    def test_generic_type(self):
        """泛型类型正确。"""
        output = SampleOutput(name="test", value=1, status="inactive")
        result: QueryResult[SampleOutput] = QueryResult(
            output=output, session_id="sess"
        )

        # output 被正确推断为 SampleOutput 类型
        assert result.output.name == "test"
        assert result.output.value == 1


# ============ StructuredQuery 初始化测试 ============


class TestStructuredQueryInit:
    """StructuredQuery 初始化测试。"""

    def test_create_with_required_params(self):
        """只传必需参数时可以创建。"""
        agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

        assert agent.output_model == SampleOutput
        assert agent.model is None
        assert agent.allowed_tools == ["Read"]
        assert agent.max_turns == 50
        assert agent.max_budget_usd == 10.0

    def test_create_with_all_params(self):
        """传入所有参数时可以创建。"""

        def stderr_handler(x: str) -> None:
            return None

        agent = StructuredQuery[SampleOutput](
            output_model=SampleOutput,
            model="sonnet",
            allowed_tools=["Read", "Glob"],
            max_turns=30,
            max_budget_usd=5.0,
            stderr_callback=stderr_handler,
        )

        assert agent.model == "sonnet"
        assert agent.allowed_tools == ["Read", "Glob"]
        assert agent.max_turns == 30
        assert agent.max_budget_usd == 5.0
        assert agent.stderr_callback == stderr_handler

    def test_allowed_tools_default_to_read(self):
        """allowed_tools 默认为 ["Read"]。"""
        agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
        assert agent.allowed_tools == ["Read"]


# ============ _build_output_format 测试 ============


class TestBuildOutputFormat:
    """output_format 生成测试。"""

    def test_generates_json_schema_type(self):
        """生成包含 type: json_schema 的格式。"""
        agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
        fmt = agent._build_output_format()

        assert fmt["type"] == "json_schema"
        assert "schema" in fmt

    def test_schema_from_model(self):
        """schema 来自模型的 JSON Schema。"""
        agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
        fmt = agent._build_output_format()

        schema = fmt["schema"]
        assert schema["type"] == "object"
        assert "properties" in schema
        assert "name" in schema["properties"]
        assert "value" in schema["properties"]
        assert "status" in schema["properties"]


# ============ Mock 辅助函数 ============


def create_mock_result_message(
    session_id: str = "test-session",
    structured_output: str | dict | None = None,
    result: str | None = None,
    num_turns: int = 1,
    duration_ms: int = 1000,
    total_cost_usd: float = 0.01,
) -> MagicMock:
    """创建模拟 ResultMessage（spec 约束以支持 isinstance 检查）。"""
    from claude_agent_sdk import ResultMessage as RealResultMessage

    # 使用 spec= 以保持 isinstance 检查正常工作
    msg = MagicMock(spec=RealResultMessage)
    msg.session_id = session_id
    msg.structured_output = structured_output
    msg.result = result
    msg.num_turns = num_turns
    msg.duration_ms = duration_ms
    msg.duration_api_ms = 500
    msg.total_cost_usd = total_cost_usd
    msg.usage = {"input_tokens": 100, "output_tokens": 50}
    return msg


# ============ query_async 测试 ============


class TestQueryAsync:
    """异步查询测试。"""

    @pytest.mark.asyncio
    async def test_query_returns_query_result(self):
        """query_async 返回 QueryResult。"""
        mock_result = create_mock_result_message(
            structured_output='{"name": "test", "value": 42, "status": "active"}'
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
            result = await agent.query_async("测试 prompt")

        assert isinstance(result, QueryResult)
        assert isinstance(result.output, SampleOutput)
        assert result.output.name == "test"
        assert result.output.value == 42
        assert result.output.status == "active"
        assert result.session_id == "test-session"

    @pytest.mark.asyncio
    async def test_query_with_dict_structured_output(self):
        """支持 dict 类型的 structured_output。"""
        mock_result = create_mock_result_message(
            structured_output={"name": "dict_test", "value": 100, "status": "inactive"}
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
            result = await agent.query_async("测试")

        assert result.output.name == "dict_test"
        assert result.output.value == 100

    @pytest.mark.asyncio
    async def test_query_passes_options_correctly(self):
        """选项正确传递给 SDK。"""
        mock_result = create_mock_result_message(
            structured_output='{"name": "t", "value": 1, "status": "active"}'
        )
        captured_options = None

        async def capture_query(prompt: str, options):
            nonlocal captured_options
            captured_options = options
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", capture_query):
            agent = StructuredQuery[SampleOutput](
                output_model=SampleOutput,
                model="opus",
                allowed_tools=["Read", "Glob", "Grep"],
                max_turns=25,
                max_budget_usd=3.0,
            )
            await agent.query_async("测试")

        assert captured_options is not None
        assert captured_options.model == "opus"
        assert captured_options.allowed_tools == ["Read", "Glob", "Grep"]
        assert captured_options.max_turns == 25
        assert captured_options.max_budget_usd == 3.0

    @pytest.mark.asyncio
    async def test_query_uses_output_format(self):
        """使用正确的 output_format。"""
        mock_result = create_mock_result_message(
            structured_output='{"title": "Test", "items": [], "metadata": {}}'
        )
        captured_options = None

        async def capture_query(prompt: str, options):
            nonlocal captured_options
            captured_options = options
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", capture_query):
            agent = StructuredQuery[ComplexOutput](output_model=ComplexOutput)
            await agent.query_async("测试")

        assert captured_options is not None
        assert captured_options.output_format["type"] == "json_schema"
        assert "schema" in captured_options.output_format

    @pytest.mark.asyncio
    async def test_query_raises_on_empty_structured_output(self):
        """structured_output 为空时抛出 RuntimeError。"""
        mock_result = create_mock_result_message(structured_output=None, result=None)

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

            with pytest.raises(RuntimeError, match="SDK 返回空 structured_output"):
                await agent.query_async("测试")

    @pytest.mark.asyncio
    async def test_query_raises_when_no_result_message(self):
        """未收到 ResultMessage 时抛出 RuntimeError。"""

        # 空生成器
        async def empty_generator(prompt, options):
            return
            yield  # 让它成为生成器

        with patch(
            "trendpluse.analyzers.structured_query.query",
            empty_generator,
        ):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

            with pytest.raises(RuntimeError, match="未收到 ResultMessage"):
                await agent.query_async("测试")


# ============ query 同步封装测试 ============


class TestQuerySync:
    """同步查询封装测试。"""

    def test_query_raises_when_event_loop_exists(self):
        """检测到运行中的事件循环时抛出错误。"""
        mock_result = create_mock_result_message(
            structured_output='{"name": "sync_test", "value": 99, "status": "active"}'
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

            # 在已有事件循环中调用 sync 方法会报错
            async def run_test():
                return agent.query("测试")

            async def main():
                with pytest.raises(RuntimeError, match="检测到正在运行的事件循环"):
                    await run_test()

            asyncio.run(main())

    def test_query_works_without_event_loop(self):
        """无事件循环时同步调用正常。"""
        mock_result = create_mock_result_message(
            structured_output=(
                '{"name": "sync_no_loop", "value": 50, "status": "inactive"}'
            )
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)
            result = agent.query("测试")

        assert result.output.name == "sync_no_loop"
        assert result.output.value == 50


# ============ 错误处理测试 ============


class TestErrorHandling:
    """错误处理测试。"""

    @pytest.mark.asyncio
    async def test_invalid_json_raises_validation_error(self):
        """无效 JSON 抛出验证错误。"""
        mock_result = create_mock_result_message(
            structured_output='{"name": "test", "value": "not_an_int"}'
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

            # value 应该是 int，传入 string 应该失败
            with pytest.raises(Exception):  # ValidationError
                await agent.query_async("测试")

    @pytest.mark.asyncio
    async def test_missing_required_field_raises(self):
        """缺少必需字段时抛出错误。"""
        mock_result = create_mock_result_message(
            structured_output='{"name": "only_name"}'
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[SampleOutput](output_model=SampleOutput)

            with pytest.raises(Exception):
                await agent.query_async("测试")


# ============ 集成场景测试 ============


class TestIntegration:
    """集成场景测试。"""

    @pytest.mark.asyncio
    async def test_complex_output_with_nested_data(self):
        """复杂嵌套数据解析。"""
        mock_result = create_mock_result_message(
            structured_output=(
                '{"title": "Complex", "items": ["a", "b"], "metadata": {"k": "v"}}'
            )
        )

        async def mock_query(prompt, options):
            yield mock_result

        with patch("trendpluse.analyzers.structured_query.query", mock_query):
            agent = StructuredQuery[ComplexOutput](output_model=ComplexOutput)
            result = await agent.query_async("测试")

        assert result.output.title == "Complex"
        assert result.output.items == ["a", "b"]
        assert result.output.metadata == {"k": "v"}
