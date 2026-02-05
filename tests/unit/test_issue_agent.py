"""Issue Agent 解析测试"""

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
