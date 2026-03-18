"""Issue Agent 执行器。

使用单轮分析替代三轮分析，减少 CLI 子进程启动开销。
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any, cast

from pydantic import ValidationError

from trendpluse.models.issue_agent import (
    ISSUE_AGENT_CATEGORY_VALUES,
    IssueAgentBatchResult,
    IssueAgentCategory,
    IssueAgentPainPoint,
    IssueAgentReport,
    IssueAgentSourceIssue,
    RepoIssueSignalReport,
)

logger = logging.getLogger(__name__)

# 默认超时配置
DEFAULT_TOTAL_TIMEOUT_SECONDS = 900.0  # 单文件总超时 15 分钟
DEFAULT_STDERR_TAIL_LINES = 20


class IssueAgentRunner:
    """使用 Claude Agent SDK 分析 Issue 文件。

    使用单轮分析替代三轮，减少 CLI 子进程启动开销。
    """

    def __init__(
        self,
        model: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_seconds: float = 1.0,
        review_confidence_threshold: float = 0.6,
        total_timeout_seconds: float = DEFAULT_TOTAL_TIMEOUT_SECONDS,
        stderr_tail_lines: int = DEFAULT_STDERR_TAIL_LINES,
        max_concurrency: int = 4,
        max_turns: int = 50,
        max_budget_usd: float = 10.0,
    ) -> None:
        self.model = model
        self.retry_max_attempts = max(1, retry_max_attempts)
        self.retry_wait_seconds = max(0.0, retry_wait_seconds)
        self.review_confidence_threshold = min(
            1.0, max(0.0, review_confidence_threshold)
        )
        self.total_timeout_seconds = max(0.0, total_timeout_seconds)
        self.stderr_tail_lines = max(1, stderr_tail_lines)
        self.max_concurrency = max(1, max_concurrency)
        self.max_turns = max(1, max_turns)
        self.max_budget_usd = max(0.1, max_budget_usd)

    async def analyze_file(self, input_path: Path, output_path: Path) -> str:
        """分析单个 JSONL 文件并写入 JSON 结果。"""
        input_path = input_path.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        last_exc: Exception | None = None
        for attempt in range(1, self.retry_max_attempts + 1):
            try:
                validated = await self._run_with_total_timeout(
                    self._run_single_round_analysis(input_path)
                )
                repo_report = self._build_repo_signal_report(
                    input_path=input_path,
                    report=validated,
                )
                normalized_text = json.dumps(
                    self._serialize_repo_signal_report(repo_report),
                    ensure_ascii=False,
                    indent=2,
                )
                output_path.write_text(normalized_text, encoding="utf-8")
                return normalized_text
            except ValidationError as exc:
                logger.warning(
                    "Issue Agent 输出校验失败，准备重试: attempt=%d/%d, error=%s",
                    attempt,
                    self.retry_max_attempts,
                    exc,
                )
                last_exc = exc
                if attempt >= self.retry_max_attempts:
                    break
                if self.retry_wait_seconds > 0:
                    await asyncio.sleep(self.retry_wait_seconds)
            except Exception as exc:
                last_exc = exc
                if attempt >= self.retry_max_attempts:
                    break
                logger.warning(
                    "Issue Agent 分析失败，准备重试: attempt=%d/%d, kind=%s, error=%s",
                    attempt,
                    self.retry_max_attempts,
                    self._classify_exception(exc),
                    self._format_exception_message(exc),
                )
                if self.retry_wait_seconds > 0:
                    await asyncio.sleep(self.retry_wait_seconds)
        assert last_exc is not None
        raise RuntimeError(
            "Issue Agent 在 "
            f"{self.retry_max_attempts} 次尝试后仍失败"
            f"（kind={self._classify_exception(last_exc)}）: "
            f"{self._format_exception_message(last_exc)}"
        ) from last_exc

    async def _run_single_round_analysis(self, input_path: Path) -> IssueAgentReport:
        """执行单轮分析，合并三轮逻辑为一步完成。

        流程整合：
        1. 候选抽取（高召回）
        2. 归一化合并（按根因）
        3. 证据审核（保留判定）
        """
        prompt = self._build_analysis_prompt(input_path)
        response_text = await self._run_agent_query(prompt)
        response_data = self._parse_json_like_text(response_text)
        if not isinstance(response_data, dict):
            raise ValueError("输出不是合法 JSON 对象")

        pain_points = response_data.get("pain_points")
        if not isinstance(pain_points, list):
            raise ValueError("缺少 pain_points 字段")

        report = self._build_report_from_reviewed_points(pain_points)
        logger.info(
            "Issue Agent 单轮分析完成: file=%s, total=%d, kept=%d",
            input_path.name,
            len(pain_points),
            len(report.top_pain_points),
        )
        return report

    def _build_analysis_prompt(self, input_path: Path) -> str:
        """构建单轮分析提示词，合并三轮逻辑。

        将候选抽取、归一化合并、证据审核整合为一步完成。
        """
        return f"""你是用户痛点分析专家。请对以下 JSONL 文件执行完整的痛点分析流程。

文件路径: {input_path}

## 分析步骤（内部执行，一步完成）

1. **候选抽取**：识别所有用户痛点（高召回）
2. **归一化合并**：按根因合并相似主题
3. **证据审核**：判断是否保留并给出优先级

## 痛点定义

用户在真实使用中反复遇到的问题，通常会导致：
- 主流程失败/阻断
- 体验显著下降
- 明显成本损失
- 关键功能不可用

## 排除项

- 单条安全公告（无用户影响证据）
- 纯功能请求
- 路线图讨论
- 无用户影响证据的维护事项

## 输出格式

输出 JSON，包含 `pain_points` 数组，每项包含：
- topic: 痛点主题（必须落到用户可感知的具体场景）
- count: 该主题去重后的 issue 数量（硬约束，不允许估算）
- affected_repos: 受影响仓库列表
- sample_urls: 样例链接列表
- source_issues: 来源 issue 详情（repo, issue_number, title, url, labels, evidence）
- aliases: 可选，相似主题别名
- confidence: 置信度 (0.0-1.0)
- priority: 优先级 (P0/P1/P2)
- keep: 是否保留 (true/false)
- review_reason: 审核理由（解释为什么是用户痛点）

## 保留规则

keep=true 必须有明确用户影响证据（阻断、崩溃、反复失败、计费异常、关键功能不可用）。
如果仅因"安全关键词"被识别但缺乏用户影响证据，必须 keep=false。

## 优先级规则

- P0: 高频(count>=3) + 主流程阻断 + 有样例链接支撑
- P1: 影响明显但非阻断
- P2: 低频或边缘改进项

若 count < 3 且仅单仓问题，默认不得标记为 P0
（除非 review_reason 明确给出强用户影响证据）。

## 硬约束

1. 必须从文件中读取 issue 数据进行分析
2. count 必须等于该主题去重后的 issue 数量，不允许估算
3. 禁止把"Security vulnerabilities"等泛化大类作为最终主题
4. review_reason 必须解释"为什么是用户痛点"，而非只强调技术严重性

仅输出 JSON，不要解释文字。"""

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

            summary = (
                str(raw.get("summary"))
                if isinstance(raw.get("summary"), str)
                and str(raw.get("summary")).strip()
                else None
            )
            if summary is None:
                raise ValueError("缺少 summary 字段")

            category = (
                str(raw.get("category"))
                if isinstance(raw.get("category"), str)
                and str(raw.get("category")).strip()
                else None
            )
            if category is None:
                raise ValueError("缺少 category 字段")
            if category not in ISSUE_AGENT_CATEGORY_VALUES:
                raise ValueError(f"非法 category 字段: {category}")
            normalized_category = cast(IssueAgentCategory, category)

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
            source_issues_raw = raw.get("source_issues")
            source_issues = self._parse_source_issues(
                source_issues_raw=source_issues_raw,
                fallback_repo=repos[0] if repos else "",
                fallback_urls=urls,
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
                    summary=summary,
                    category=normalized_category,
                    count=count,
                    affected_repos=repos,
                    sample_urls=urls,
                    aliases=aliases,
                    confidence=confidence,
                    priority=priority,
                    review_reason=review_reason,
                    source_issues=source_issues,
                )
            )

        points.sort(key=lambda item: item.count, reverse=True)
        return IssueAgentReport(top_pain_points=points[:5])

    async def analyze_directory(
        self, input_dir: Path, output_dir: Path
    ) -> IssueAgentBatchResult:
        """分析目录下所有 JSONL 文件。"""
        files = sorted(input_dir.glob("*.jsonl"))
        if not files:
            return IssueAgentBatchResult(
                expected_files=0,
                succeeded_files=0,
                failed_files=0,
                failed_samples=[],
            )

        output_dir.mkdir(parents=True, exist_ok=True)
        semaphore = asyncio.Semaphore(self.max_concurrency)

        async def _analyze_single(
            input_path: Path,
        ) -> tuple[Path, Exception | None]:
            output_path = output_dir / f"{input_path.stem}.analysis.json"
            async with semaphore:
                try:
                    await self.analyze_file(input_path, output_path)
                    return input_path, None
                except Exception as exc:
                    return input_path, exc

        results = await asyncio.gather(*[_analyze_single(path) for path in files])

        success_count = 0
        failed_count = 0
        failed_samples: list[str] = []
        for input_path, exc in results:
            if exc is None:
                success_count += 1
                continue

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
            from claude_agent_sdk import (
                AssistantMessage,
                ClaudeAgentOptions,
                ResultMessage,
                query,
            )
        except Exception as exc:  # pragma: no cover - 仅在缺少依赖时触发
            raise RuntimeError(
                "未安装 claude-agent-sdk，请先安装依赖后再运行。"
            ) from exc

        options = ClaudeAgentOptions(
            model=self.model,
            allowed_tools=["Read"],
            output_format=self._build_output_format(),
            stderr=self._build_stderr_handler(),
            max_turns=self.max_turns,
            max_budget_usd=self.max_budget_usd,
        )

        text_chunks: list[str] = []
        result_text: str | None = None
        structured_output: Any = None
        try:
            async for message in query(prompt=prompt, options=options):
                if isinstance(message, AssistantMessage):
                    text_chunks.append(self._extract_text_blocks(message.content))
                elif isinstance(message, ResultMessage):
                    if message.structured_output is not None:
                        structured_output = message.structured_output
                    if isinstance(message.result, str) and message.result.strip():
                        result_text = message.result.strip()
        except Exception as exc:
            raise RuntimeError(self._build_cli_error_message(exc)) from exc

        if structured_output is not None:
            if isinstance(structured_output, str):
                return structured_output
            return json.dumps(structured_output, ensure_ascii=False)

        if result_text:
            return result_text

        return "".join(text_chunks).strip()

    def _build_output_format(self) -> dict[str, Any]:
        """构建单轮分析的结构化输出 schema。"""
        return {
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {"pain_points": self._pain_point_array_schema()},
                "required": ["pain_points"],
                "additionalProperties": False,
            },
        }

    def _pain_point_array_schema(self) -> dict[str, Any]:
        """构建痛点数组 schema，包含所有审核字段。"""
        properties: dict[str, Any] = {
            "id": {"type": "string"},
            "repo": {"type": "string"},
            "topic": {"type": "string"},
            "summary": {"type": "string"},
            "category": {
                "type": "string",
                "enum": list(ISSUE_AGENT_CATEGORY_VALUES),
            },
            "count": {"type": "integer", "minimum": 1},
            "affected_repos": {
                "type": "array",
                "items": {"type": "string"},
            },
            "sample_urls": {
                "type": "array",
                "items": {"type": "string"},
            },
            "aliases": {
                "type": "array",
                "items": {"type": "string"},
            },
            "source_issues": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "repo": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "title": {"type": "string"},
                        "url": {"type": "string"},
                        "labels": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "evidence": {"type": "string"},
                    },
                    "required": ["repo", "url"],
                    "additionalProperties": False,
                },
            },
            "confidence": {
                "type": "number",
                "minimum": 0,
                "maximum": 1,
            },
            "priority": {
                "type": "string",
                "enum": ["P0", "P1", "P2"],
            },
            "keep": {"type": "boolean"},
            "review_reason": {"type": "string"},
        }
        required = [
            "topic",
            "summary",
            "category",
            "count",
            "affected_repos",
            "sample_urls",
            "confidence",
            "priority",
            "keep",
        ]

        return {
            "type": "array",
            "items": {
                "type": "object",
                "properties": properties,
                "required": required,
                "additionalProperties": False,
            },
        }

    def _parse_source_issues(
        self,
        *,
        source_issues_raw: Any,
        fallback_repo: str,
        fallback_urls: list[str],
    ) -> list[IssueAgentSourceIssue]:
        """解析来源 issue，兼容旧格式 sample_urls。"""
        results: list[IssueAgentSourceIssue] = []
        if isinstance(source_issues_raw, list):
            for item in source_issues_raw:
                if not isinstance(item, dict):
                    continue
                url = item.get("url")
                repo = item.get("repo") or fallback_repo
                if not isinstance(url, str) or not url.strip():
                    continue
                issue_number = item.get("issue_number")
                results.append(
                    IssueAgentSourceIssue(
                        repo=str(repo),
                        issue_number=issue_number
                        if isinstance(issue_number, int)
                        else None,
                        title=str(item.get("title", "")),
                        url=url,
                        labels=[
                            str(label)
                            for label in item.get("labels", [])
                            if isinstance(label, str)
                        ]
                        if isinstance(item.get("labels"), list)
                        else [],
                        evidence=str(item.get("evidence"))
                        if isinstance(item.get("evidence"), str)
                        else None,
                    )
                )

        if results:
            return results

        return [
            IssueAgentSourceIssue(repo=fallback_repo or "", url=url)
            for url in fallback_urls
        ]

    def _build_repo_signal_report(
        self,
        *,
        input_path: Path,
        report: IssueAgentReport,
    ) -> RepoIssueSignalReport:
        """构建单仓库 Issue 信号报告。"""
        repo = self._infer_repo_from_jsonl(input_path)
        snapshot_date = input_path.parent.name
        signals = [
            item.model_copy(
                update={
                    "id": item.id or f"{input_path.stem}-{index}",
                    "repo": item.repo or repo,
                    "summary": item.summary or item.review_reason or item.topic,
                    "source_issues": item.source_issues
                    or [
                        IssueAgentSourceIssue(repo=repo, url=url)
                        for url in item.sample_urls
                    ],
                }
            )
            for index, item in enumerate(report.top_pain_points, start=1)
        ]
        issue_count = self._count_jsonl_lines(input_path)
        return RepoIssueSignalReport(
            repo=repo,
            snapshot_date=snapshot_date,
            signals=signals,
            expected_issue_count=issue_count,
            analyzed_issue_count=issue_count,
            quality_score=1.0,
            quality_status="good",
            errors=[],
        )

    def _serialize_repo_signal_report(
        self,
        report: RepoIssueSignalReport,
    ) -> dict[str, Any]:
        """序列化仓库级报告。"""
        return report.model_dump()

    def _infer_repo_from_jsonl(self, input_path: Path) -> str:
        """从 JSONL 首行读取 repo，失败时回退到文件名。"""
        try:
            with input_path.open("r", encoding="utf-8") as handle:
                for line in handle:
                    stripped = line.strip()
                    if not stripped:
                        continue
                    payload = json.loads(stripped)
                    repo = payload.get("repo")
                    if isinstance(repo, str) and repo.strip():
                        return repo.strip()
                    break
        except Exception:
            pass
        return input_path.stem.replace("__", "/")

    def _count_jsonl_lines(self, input_path: Path) -> int:
        """统计 JSONL 非空行数。"""
        try:
            with input_path.open("r", encoding="utf-8") as handle:
                return sum(1 for line in handle if line.strip())
        except OSError:
            return 0

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

    def _parse_json_like_text(self, text: str) -> dict[str, Any] | None:
        stripped = text.strip()
        if not stripped:
            return None

        direct = self._try_parse_json(stripped)
        if direct is not None:
            return direct

        fenced_match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", stripped, re.DOTALL)
        if fenced_match:
            parsed = self._try_parse_json(fenced_match.group(1).strip())
            if parsed is not None:
                return parsed

        json_start = stripped.find("{")
        json_end = stripped.rfind("}")
        if json_start != -1 and json_end != -1 and json_end > json_start:
            candidate = stripped[json_start : json_end + 1]
            parsed = self._try_parse_json(candidate)
            if parsed is not None:
                return parsed

        return None

    def _try_parse_json(self, text: str) -> dict[str, Any] | None:
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            return None
        return parsed if isinstance(parsed, dict) else None

    async def _run_with_total_timeout(self, coroutine: Any) -> IssueAgentReport:
        """为单文件分析增加总超时保护。"""
        if self.total_timeout_seconds <= 0:
            return await coroutine
        try:
            async with asyncio.timeout(self.total_timeout_seconds):
                return await coroutine
        except TimeoutError as exc:
            raise TimeoutError(
                f"Issue Agent 单文件分析总超时 ({self.total_timeout_seconds:.0f}s)"
            ) from exc

    def _build_stderr_handler(self) -> Any:
        """构建 SDK stderr 回调，保存最近几行诊断信息。"""
        stderr_lines: list[str] = []

        def _handle(message: str) -> None:
            cleaned = message.strip()
            if not cleaned:
                return
            stderr_lines.append(cleaned)
            if len(stderr_lines) > self.stderr_tail_lines:
                del stderr_lines[0 : len(stderr_lines) - self.stderr_tail_lines]
            logger.debug("Issue Agent SDK stderr: %s", cleaned)

        self._last_stderr_lines = stderr_lines
        return _handle

    def _build_cli_error_message(self, exc: Exception) -> str:
        """拼装带 stderr 摘要的 CLI 错误消息。"""
        base = str(exc).strip() or exc.__class__.__name__
        stderr_tail = self._get_stderr_tail()
        if not stderr_tail:
            return base
        return f"{base}; stderr_tail={stderr_tail}"

    def _get_stderr_tail(self) -> str:
        """获取最近的 stderr 摘要。"""
        stderr_lines = getattr(self, "_last_stderr_lines", [])
        if not isinstance(stderr_lines, list) or not stderr_lines:
            return ""
        return " | ".join(str(line) for line in stderr_lines[-self.stderr_tail_lines :])

    def _classify_exception(self, exc: Exception) -> str:
        """将异常归类为稳定的失败类别。"""
        if isinstance(exc, TimeoutError):
            return "timeout"
        if isinstance(exc, ValidationError | ValueError):
            return "validation_error"

        message = str(exc).lower()
        if "exit code" in message or "command failed" in message:
            return "process_error"
        if "canceled" in message or "cancelled" in message:
            return "cancelled"
        return "unknown"

    def _format_exception_message(self, exc: Exception) -> str:
        """生成适合日志的异常信息。"""
        message = str(exc).strip() or exc.__class__.__name__
        if len(message) > 500:
            return message[:500] + "..."
        return message
