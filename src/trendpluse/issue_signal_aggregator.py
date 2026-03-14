"""Issue 仓库级信号的全局汇总。"""

from __future__ import annotations

import json
from typing import Any

from pydantic import BaseModel, Field

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.models.issue_agent import IssueAgentReport


class IssueGlobalSummaryResponse(BaseModel):
    """Issue 全局汇总结果。"""

    summary_brief: str = Field(description="全局摘要")
    global_highlights: list[str] = Field(default_factory=list, description="全局亮点")


class IssueGlobalSummarizer(BaseLLMAnalyzer):
    """基于仓库级 Issue 信号生成全局摘要。"""

    response_model = IssueGlobalSummaryResponse

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ) -> None:
        super().__init__(
            api_key=api_key,
            model=model,
            base_url=base_url,
            use_instructor=True,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    def summarize(self, report: IssueAgentReport) -> IssueAgentReport:
        """生成全局摘要与亮点。"""
        if not report.repo_reports or not report.top_pain_points:
            return report.model_copy(
                update={
                    "summary_brief": self._build_fallback_summary(report),
                    "global_highlights": [],
                }
            )

        try:
            response = self._call_llm_for_summary(report)
            return report.model_copy(
                update={
                    "summary_brief": response.summary_brief,
                    "global_highlights": response.global_highlights,
                }
            )
        except Exception:
            return report.model_copy(
                update={
                    "summary_brief": self._build_fallback_summary(report),
                    "global_highlights": self._build_fallback_highlights(report),
                }
            )

    def _call_llm_for_summary(
        self,
        report: IssueAgentReport,
    ) -> IssueGlobalSummaryResponse:
        prompt = self._build_prompt(report)
        system_prompt = (
            "你是资深技术情报分析师。请基于给定的仓库级 Issue 信号，"
            "总结跨仓库共性问题。所有输出必须使用中文，简洁、可读、可追溯。"
        )

        def _call() -> IssueGlobalSummaryResponse:
            response = self.client.chat.completions.create(
                model=self.model,
                response_model=self.response_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1200,
            )
            return response

        response = self._run_with_llm_retry(_call)
        return response

    def _build_prompt(self, report: IssueAgentReport) -> str:
        payload: dict[str, Any] = {
            "repo_reports": [
                {
                    "repo": repo_report.repo,
                    "signals": [
                        {
                            "id": signal.id,
                            "topic": signal.topic,
                            "summary": signal.summary,
                            "priority": signal.priority,
                            "confidence": signal.confidence,
                            "count": signal.count,
                            "source_issues": [
                                {
                                    "repo": issue.repo,
                                    "issue_number": issue.issue_number,
                                    "title": issue.title,
                                    "url": issue.url,
                                }
                                for issue in signal.source_issues[:3]
                            ],
                        }
                        for signal in repo_report.signals[:5]
                    ],
                }
                for repo_report in report.repo_reports[:20]
            ],
            "global_candidates": [
                {
                    "topic": item.topic,
                    "priority": item.priority,
                    "confidence": item.confidence,
                    "count": item.count,
                    "affected_repos": item.affected_repos,
                }
                for item in report.top_pain_points[:10]
            ],
        }
        payload_text = json.dumps(payload, ensure_ascii=False, indent=2)
        return f"""
请基于以下仓库级 Issue 信号，生成一份全局汇总。

输入数据：
{payload_text}

输出要求：
1. `summary_brief`：2 句话以内，总结今天最重要的跨仓库 issue 问题。
2. `global_highlights`：返回 2-4 条亮点，每条一句话。
3. 必须聚焦“跨仓库共性问题”或“高影响单仓问题”，不要泛泛而谈。
4. 所有输出必须使用中文。
""".strip()

    def _build_fallback_summary(self, report: IssueAgentReport) -> str:
        repo_count = len(report.repo_reports)
        global_count = len(report.top_pain_points)
        if global_count == 0:
            return f"Issue Agent 已分析 {repo_count} 个仓库，未识别出跨仓库共性问题。"
        top_topic = report.top_pain_points[0].topic
        return (
            f"Issue Agent 汇总了 {repo_count} 个仓库，"
            f"识别出 {global_count} 个跨仓库问题，"
            f"其中最高优先级问题为“{top_topic}”。"
        )

    def _build_fallback_highlights(self, report: IssueAgentReport) -> list[str]:
        highlights: list[str] = []
        for item in report.top_pain_points[:3]:
            repo_span = len(item.affected_repos)
            issue_count = item.count
            highlights.append(
                f"{item.topic}：影响 {repo_span} 个仓库，累计 {issue_count} 个 issue"
            )
        return highlights
