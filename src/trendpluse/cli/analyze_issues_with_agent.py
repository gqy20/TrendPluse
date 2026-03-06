"""使用 Claude Agent SDK 分析 Issue 文件。

示例：
  uv run trendpluse-analyze-issues --input data/issues/2026-02-05 \\
      --output data/issues/2026-02-05/analysis
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from trendpluse.workflows.issue_agent_runner import IssueAgentRunner


def _iter_input_files(input_path: Path) -> list[Path]:
    if input_path.is_file():
        return [input_path]
    return sorted(input_path.glob("*.jsonl"))


async def _run(input_path: Path, output_path: Path, model: str | None) -> None:
    runner = IssueAgentRunner(model=model)
    files = _iter_input_files(input_path)
    if not files:
        raise SystemExit(f"未找到可分析的 jsonl 文件: {input_path}")

    for file_path in files:
        if output_path.is_dir() or output_path.suffix == "":
            output_path.mkdir(parents=True, exist_ok=True)
            out_file = output_path / f"{file_path.stem}.analysis.json"
        else:
            out_file = output_path
        await runner.analyze_file(file_path, out_file)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Issue JSONL 文件或目录")
    parser.add_argument("--output", required=True, help="输出 JSON 文件或目录")
    parser.add_argument("--model", default=None, help="Claude 模型名称（可选）")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    asyncio.run(_run(input_path, output_path, args.model))


if __name__ == "__main__":
    main()
