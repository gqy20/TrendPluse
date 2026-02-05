"""Issue 质量分析器

使用 LLM 判定 Issue 是否应纳入趋势分析，并生成归一化主题。
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.logger import get_logger
from trendpluse.models.issue import IssueInfo, IssueQualityDecision

logger = get_logger(__name__)


class IssueQualityAnalyzer(BaseLLMAnalyzer):
    """Issue 质量分析器（LLM）"""

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        super().__init__(
            api_key,
            model,
            base_url,
            use_instructor=True,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    def analyze(self, issue: IssueInfo) -> IssueQualityDecision:
        prompt = f"""请判断以下 GitHub Issue 是否应该纳入趋势分析，并输出结构化结果。

Issue 标题: {issue.title}
Issue 内容: {issue.body or "(无内容)"}
仓库: {issue.repo}
状态: {issue.state}
标签: {", ".join(issue.labels)}
评论数: {issue.comments}
链接: {issue.url}

判断标准：
1. 仅保留真实用户问题、Bug、功能请求、问题咨询。
2. 排除公告/发布说明/推广/招聘/教程/文档整理/重复或无关内容。
3. 如果保留，生成一个不超过 12 字的中文主题（痛点/需求）。

输出字段：
- include: true/false
- reason: 简短原因（可为 null）
- normalized_topic: 中文主题（不适用时为 null）

重要格式要求：
- 如果字段不存在或不适用，请返回 JSON null（不是字符串 "null"/"None"/"N/A"）
- 只返回结构化结果，不要附带额外说明文字
"""

        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=IssueQualityDecision,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
            )

        return self._run_with_llm_retry(_call)

    def evaluate(
        self, issues: list[IssueInfo], max_workers: int = 5
    ) -> dict[str, IssueQualityDecision]:
        if not issues:
            return {}

        results: dict[str, IssueQualityDecision] = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_issue = {
                executor.submit(self.analyze, issue): issue for issue in issues
            }
            for future in as_completed(future_to_issue):
                issue = future_to_issue[future]
                try:
                    decision = future.result()
                except Exception as exc:
                    logger.debug(
                        f"Issue 质量判定失败: {issue.repo}#{issue.issue_id} {exc}"
                    )
                    continue
                key = f"{issue.repo}#{issue.issue_id}"
                results[key] = decision
        return results
