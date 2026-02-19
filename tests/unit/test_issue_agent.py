"""Issue Agent 解析测试"""

import pytest

from trendpluse.agents.issue_agent import IssueAgentRunner


class DummyText:
    def __init__(self, text: str) -> None:
        self.text = text


def test_extract_text_blocks_handles_multiple_types() -> None:
    runner = IssueAgentRunner(model=None)
    content = [
        "A",
        {"type": "text", "text": "B"},
        DummyText("C"),
        {"type": "tool_use", "id": "x"},
    ]
    text = runner._extract_text_blocks(content)
    assert text == "ABC"


def test_normalize_and_validate_output_accepts_fenced_json() -> None:
    runner = IssueAgentRunner(model=None)
    text = """
这里是说明文字
```json
{
  "top_pain_points": [
    {"topic":"安装失败","count":2,"affected_repos":["a/b"],"sample_urls":["u1"]}
  ]
}
```
"""
    report = runner._normalize_and_validate_output(text)
    assert len(report.top_pain_points) == 1
    assert report.top_pain_points[0].topic == "安装失败"


@pytest.mark.asyncio
async def test_analyze_file_retries_on_invalid_then_success(tmp_path) -> None:
    class _RetryRunner(IssueAgentRunner):
        def __init__(self) -> None:
            super().__init__(model=None, retry_max_attempts=2, retry_wait_seconds=0)
            self.calls = 0

        async def _run_agent_query(self, prompt: str) -> str:
            del prompt
            self.calls += 1
            if self.calls == 1:
                return "not json"
            return (
                '{"top_pain_points":[{"topic":"崩溃","count":1,'
                '"affected_repos":["a/b"],"sample_urls":["u"]}]}'
            )

    runner = _RetryRunner()
    output_path = tmp_path / "x.analysis.json"
    input_path = tmp_path / "x.jsonl"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")
    text = await runner.analyze_file(input_path, output_path)
    assert runner.calls == 2
    assert "top_pain_points" in text


@pytest.mark.asyncio
async def test_analyze_file_raises_after_retry_exhausted(tmp_path) -> None:
    class _FailRunner(IssueAgentRunner):
        def __init__(self) -> None:
            super().__init__(model=None, retry_max_attempts=2, retry_wait_seconds=0)

        async def _run_agent_query(self, prompt: str) -> str:
            del prompt
            return "still invalid"

    runner = _FailRunner()
    output_path = tmp_path / "x.analysis.json"
    input_path = tmp_path / "x.jsonl"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")
    with pytest.raises(RuntimeError, match="仍未通过校验"):
        await runner.analyze_file(input_path, output_path)


@pytest.mark.asyncio
async def test_analyze_directory_continues_when_single_file_fails(tmp_path) -> None:
    class _PartialFailRunner(IssueAgentRunner):
        async def analyze_file(self, input_path, output_path):  # type: ignore[override]
            if input_path.name == "bad.jsonl":
                raise RuntimeError("boom")
            output_path.write_text('{"top_pain_points":[]}', encoding="utf-8")
            return '{"top_pain_points":[]}'

    runner = _PartialFailRunner(model=None)
    input_dir = tmp_path / "in"
    output_dir = tmp_path / "out"
    input_dir.mkdir()
    (input_dir / "a.jsonl").write_text(
        '{"repo":"a/b","issue_id":1}\n',
        encoding="utf-8",
    )
    (input_dir / "bad.jsonl").write_text(
        '{"repo":"a/b","issue_id":2}\n', encoding="utf-8"
    )
    (input_dir / "c.jsonl").write_text(
        '{"repo":"a/b","issue_id":3}\n',
        encoding="utf-8",
    )

    result = await runner.analyze_directory(input_dir, output_dir)

    assert result.expected_files == 3
    assert result.succeeded_files == 2
    assert result.failed_files == 1
    assert "bad.jsonl" in result.failed_samples
    assert (output_dir / "a.analysis.json").exists()
    assert (output_dir / "c.analysis.json").exists()
