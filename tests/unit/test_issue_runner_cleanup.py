"""Issue Runner 清理旧兼容测试。"""

import pytest

from trendpluse.analyzers.issue_agent_runner import IssueAgentRunner


@pytest.mark.asyncio
async def test_issue_runner_no_longer_accepts_top_pain_points_round3(tmp_path) -> None:
    class _LegacyRound3Runner(IssueAgentRunner):
        async def _run_agent_query(self, prompt: str) -> str:
            if "[ROUND1]" in prompt:
                return '{"candidate_pain_points":[]}'
            if "[ROUND2]" in prompt:
                return '{"merged_pain_points":[]}'
            return '{"top_pain_points":[]}'

    runner = _LegacyRound3Runner(model=None, retry_max_attempts=1, retry_wait_seconds=0)
    input_path = tmp_path / "x.jsonl"
    output_path = tmp_path / "x.analysis.json"
    input_path.write_text('{"repo":"a/b","issue_id":1}\n', encoding="utf-8")

    with pytest.raises(RuntimeError, match="validation_error"):
        await runner.analyze_file(input_path, output_path)
