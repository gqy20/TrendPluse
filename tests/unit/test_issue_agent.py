"""Issue Agent 解析测试"""

import pytest

from trendpluse.workflows.issue_agent_runner import IssueAgentRunner


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
            self.calls += 1
            if "[ROUND1]" in prompt and self.calls == 1:
                return "not json"
            if "[ROUND1]" in prompt:
                return (
                    '{"candidate_pain_points":[{"topic":"崩溃","count":1,'
                    '"affected_repos":["a/b"],"sample_urls":["u"]}]}'
                )
            if "[ROUND2]" in prompt:
                return (
                    '{"merged_pain_points":[{"topic":"崩溃","count":1,'
                    '"affected_repos":["a/b"],"sample_urls":["u"]}]}'
                )
            return (
                '{"reviewed_pain_points":[{"topic":"崩溃","count":1,'
                '"affected_repos":["a/b"],"sample_urls":["u"],'
                '"confidence":0.9,"priority":"P1","keep":true}]}'
            )

    runner = _RetryRunner()
    output_path = tmp_path / "x.analysis.json"
    input_path = tmp_path / "x.jsonl"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")
    text = await runner.analyze_file(input_path, output_path)
    assert runner.calls == 4
    assert "top_pain_points" in text


@pytest.mark.asyncio
async def test_analyze_file_raises_after_retry_exhausted(tmp_path) -> None:
    class _FailRunner(IssueAgentRunner):
        def __init__(self) -> None:
            super().__init__(model=None, retry_max_attempts=2, retry_wait_seconds=0)

        async def _run_agent_query(self, prompt: str) -> str:
            if "[ROUND1]" in prompt:
                return (
                    '{"candidate_pain_points":[{"topic":"x","count":1,'
                    '"affected_repos":["a/b"],"sample_urls":["u"]}]}'
                )
            if "[ROUND2]" in prompt:
                return (
                    '{"merged_pain_points":[{"topic":"x","count":1,'
                    '"affected_repos":["a/b"],"sample_urls":["u"]}]}'
                )
            return "still invalid"

    runner = _FailRunner()
    output_path = tmp_path / "x.analysis.json"
    input_path = tmp_path / "x.jsonl"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")
    with pytest.raises(RuntimeError, match="仍未通过校验"):
        await runner.analyze_file(input_path, output_path)


@pytest.mark.asyncio
async def test_analyze_file_three_round_review_filters_low_confidence(tmp_path) -> None:
    class _ThreeRoundRunner(IssueAgentRunner):
        def __init__(self) -> None:
            super().__init__(
                model=None,
                retry_max_attempts=1,
                retry_wait_seconds=0,
            )
            self.prompts: list[str] = []

        async def _run_agent_query(self, prompt: str) -> str:
            self.prompts.append(prompt)
            if "[ROUND1]" in prompt:
                return """
{
  "candidate_pain_points": [
    {"topic":"CLI崩溃","count":5,"affected_repos":["a/b"],"sample_urls":["u1"]},
    {"topic":"文档建议","count":2,"affected_repos":["c/d"],"sample_urls":["u2"]}
  ]
}
"""
            if "[ROUND2]" in prompt:
                return """
{
  "merged_pain_points": [
    {"topic":"CLI稳定性问题","count":6,"affected_repos":["a/b"],"sample_urls":["u1","u3"]},
    {"topic":"文档改进建议","count":2,"affected_repos":["c/d"],"sample_urls":["u2"]}
  ]
}
"""
            return """
{
  "reviewed_pain_points": [
    {"topic":"CLI稳定性问题","count":6,"affected_repos":["a/b"],"sample_urls":["u1"],"confidence":0.92,"priority":"P0","keep":true,"review_reason":"崩溃影响主流程"},
    {"topic":"文档改进建议","count":2,"affected_repos":["c/d"],"sample_urls":["u2"],"confidence":0.45,"priority":"P2","keep":true,"review_reason":"低影响"}
  ]
}
"""

    runner = _ThreeRoundRunner()
    output_path = tmp_path / "x.analysis.json"
    input_path = tmp_path / "x.jsonl"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")
    text = await runner.analyze_file(input_path, output_path)

    assert len(runner.prompts) == 3
    assert any("[ROUND1]" in p for p in runner.prompts)
    assert any("[ROUND2]" in p for p in runner.prompts)
    assert any("[ROUND3]" in p for p in runner.prompts)
    assert "CLI稳定性问题" in text
    assert "文档改进建议" not in text


@pytest.mark.asyncio
async def test_analyze_directory_continues_when_single_file_fails(tmp_path) -> None:
    class _PartialFailRunner(IssueAgentRunner):
        async def analyze_file(self, input_path, output_path):
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
