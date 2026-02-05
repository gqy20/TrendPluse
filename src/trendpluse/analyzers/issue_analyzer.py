"""Issue 分析器

使用 AI 对 Issue 进行分类、情绪分析和痛点提取。
"""

from typing import Literal

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.logger import get_logger
from trendpluse.models.issue import BatchIssueAnalysis, IssueAnalysis, IssueInfo
from trendpluse.models.signal import Signal

logger = get_logger(__name__)


class IssueAnalyzer(BaseLLMAnalyzer):
    """Issue 分析器

    使用 AI 对 Issue 进行分类、情绪分析和痛点提取。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        """初始化分析器

        Args:
            api_key: API Key
            model: 模型名称
            base_url: API Base URL
        """
        super().__init__(
            api_key,
            model,
            base_url,
            use_instructor=True,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    def analyze(self, issue: IssueInfo) -> IssueAnalysis:
        """分析单个 Issue

        Args:
            issue: Issue 信息

        Returns:
            分析结果
        """
        # 构建 Prompt
        prompt = f"""分析以下 GitHub Issue，提取关键信息。

Issue 标题: {issue.title}
Issue 内容: {issue.body or "(无内容)"}
仓库: {issue.repo}
状态: {issue.state}
标签: {", ".join(issue.labels)}
评论数: {issue.comments}
链接: {issue.url}

请分析并返回结构化数据，包括：
1. 分类: bug_report / feature_request / question / discussion
2. 情绪: positive / neutral / negative
3. 痛点: 用户遇到的问题（如果适用）
4. 功能需求: 用户想要的功能（如果是 feature_request）
5. 优先级: low / medium / high / critical
6. 技术标签: 相关技术栈关键词

重要格式要求：
- 如果字段不存在或不适用，请返回 JSON null（不是字符串 "null"/"None"/"N/A"）
- 只返回结构化结果，不要附带额外说明文字
"""

        analysis = self._call_llm_for_analysis(prompt)
        return analysis

    def _call_llm_for_analysis(self, prompt: str) -> IssueAnalysis:  # type: ignore[no-any-return]
        """调用 LLM 分析 Issue

        Args:
            prompt: 分析提示词

        Returns:
            分析结果
        """

        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=IssueAnalysis,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
            )

        return self._run_with_llm_retry(_call)

    def analyze_batch(
        self,
        issues: list[IssueInfo],
        max_workers: int = 3,
    ) -> dict[str, IssueAnalysis]:
        """批量分析 Issues

        Args:
            issues: Issue 列表
            max_workers: 最大并行数

        Returns:
            {issue_key: 分析结果} 字典，格式为 "repo#issue_id"
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        results = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_issue = {
                executor.submit(self.analyze, issue): issue for issue in issues
            }

            for future in as_completed(future_to_issue):
                issue = future_to_issue[future]
                try:
                    analysis = future.result()
                    key = f"{issue.repo}#{issue.issue_id}"
                    results[key] = analysis
                except Exception as e:
                    logger.debug(f"分析 Issue {issue.repo}#{issue.issue_id} 失败: {e}")

        return results

    def extract_signals(
        self,
        issues: list[IssueInfo],
        analyses: dict[str, IssueAnalysis],
    ) -> list[Signal]:
        """从 Issue 分析结果中提取趋势信号

        Args:
            issues: Issue 列表
            analyses: 分析结果字典

        Returns:
            信号列表
        """
        signals = []

        for issue in issues:
            key = f"{issue.repo}#{issue.issue_id}"
            analysis = analyses.get(key)

            if not analysis:
                continue

            # 只将高价值的 Issue 转换为信号
            if not self._is_high_value_issue(issue, analysis):
                continue

            signal = self._create_signal(issue, analysis)
            if signal:
                signals.append(signal)

        return signals

    def _is_high_value_issue(self, issue: IssueInfo, analysis: IssueAnalysis) -> bool:
        """判断是否为高价值 Issue

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            True 如果是高价值 Issue
        """
        # 高优先级功能请求
        if analysis.category == "feature_request" and analysis.priority in (
            "high",
            "critical",
        ):
            return True

        # 有讨论价值的（评论数 >= 5）
        if issue.comments >= 5:
            return True

        # 负面情绪的 Bug（用户痛点）
        if analysis.category == "bug_report" and analysis.sentiment == "negative":
            return True

        return False

    def _create_signal(
        self, issue: IssueInfo, analysis: IssueAnalysis
    ) -> Signal | None:  # type: ignore[no-any-return]
        """创建信号对象

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            信号对象，如果不适合则返回 None
        """
        # 确定信号类型
        signal_type: Literal[
            "capability",
            "abstraction",
            "workflow",
            "eval",
            "safety",
            "performance",
            "commit",
            "release",
        ] = {
            "bug_report": "workflow",
            "feature_request": "capability",
            "question": "abstraction",
            "discussion": "abstraction",
        }.get(analysis.category, "workflow")  # type: ignore[assignment]

        # 构建描述
        if analysis.pain_point:
            description = f"用户痛点: {analysis.pain_point}"
        elif analysis.feature_description:
            description = f"功能需求: {analysis.feature_description}"
        else:
            description = issue.title

        return Signal(
            id=f"issue-{issue.repo.replace('/', '-')}-{issue.issue_id}",
            title=issue.title,
            type=signal_type,
            category="engineering",  # Issue 主要反映工程问题
            impact_score=self._calculate_impact_score(issue, analysis),
            why_it_matters=description,
            sources=[issue.url],
            related_repos=[issue.repo],
        )

    def _calculate_impact_score(self, issue: IssueInfo, analysis: IssueAnalysis) -> int:
        """计算影响评分 (1-5)

        评分规则：
        - 特殊规则：critical + comments>=10 = 5（最高分）
        - 基础分：0 评论=1，有评论=2
        - 评论数加分：>=20:+1, >=10:+0.5, >=5:+0, <5:0
        - 优先级加分：critical:+2, high:+1, medium:+0.5, low:0
        - 负面情绪加分：low:+0.5
        - 四舍五入，限制在 1-5

        Args:
            issue: Issue 信息
            analysis: 分析结果

        Returns:
            影响评分 1-5
        """
        # 特殊规则：critical + 高评论数 = 最高分
        if analysis.priority == "critical" and issue.comments >= 10:
            return 5

        # 基础分：有评论的至少 2 分
        score = 2.0 if issue.comments > 0 else 1.0

        # 评论数加分（额外）
        if issue.comments >= 20:
            score += 1
        elif issue.comments >= 10:
            score += 0.5

        # 优先级加分
        priority_score = {
            "low": 0,
            "medium": 0.5,
            "high": 1,
            "critical": 2,
        }
        score += priority_score.get(analysis.priority, 0)

        # 负面情绪加分（仅 low）
        if analysis.sentiment == "negative" and analysis.priority == "low":
            score += 0.5

        # 四舍五入并限制范围
        rounded = int(score + 0.5)
        return max(1, min(5, rounded))

    # ========== 批量分析方法 ==========

    def build_batch_prompt(self, issues: list[IssueInfo]) -> str:
        """构建批量分析的 Prompt

        Args:
            issues: Issue 列表（2-20 个为宜）

        Returns:
            批量分析 Prompt
        """
        parts = [
            f"分析以下 {len(issues)} 个 GitHub Issues，",
            "为每个 Issue 返回结构化数据。\n",
        ]

        for i, issue in enumerate(issues, 1):
            # 精简 Issue 信息，减少 token 消耗
            content_preview = (
                (issue.body[:200] + "...")
                if issue.body and len(issue.body) > 200
                else (issue.body or "(无内容)")
            )

            parts.append(f"""
## Issue {i}
- **标题**: {issue.title}
- **内容**: {content_preview}
- **仓库**: {issue.repo}
- **状态**: {issue.state}
- **标签**: {", ".join(issue.labels)}
- **评论数**: {issue.comments}
""")

        parts.append(f"""
请返回一个数组，包含所有 {len(issues)} 个 Issue 的分析结果。
数组中的第 N 个元素对应第 N 个 Issue。

结果格式要求:
- 每个结果包含: category, sentiment, sentiment_score, pain_point,
  affected_area, feature_description, priority, tech_tags
- 如果某个 Issue 无法分析，该位置返回 null
- 确保 results 数组长度与输入 Issues 数量一致
- 字段为空时必须返回 JSON null（不是字符串 "null"/"None"/"N/A"）

返回格式示例:
[
  {{
    "category": "bug_report",
    "sentiment": "negative",
    "sentiment_score": -0.5,
    "pain_point": "用户描述的问题",
    "affected_area": "受影响的功能模块",
    "feature_description": null,
    "priority": "high",
    "tech_tags": ["python", "api"]
  }},
  ...
]
""")

        return "\n".join(parts)

    def analyze_batch_optimized(
        self,
        issues: list[IssueInfo],
        batch_size: int = 5,
        max_workers: int = 3,
    ) -> dict[str, IssueAnalysis]:
        """批量分析 Issues（优化版本）

        使用真正的批量分析，一次 AI 调用处理多个 Issues。

        Args:
            issues: Issue 列表
            batch_size: 每批处理的 Issue 数量（默认 5）
            max_workers: 并发批次数（默认 3）

        Returns:
            {issue_key: 分析结果} 字典

        Raises:
            ValueError: batch_size 必须大于 0
        """
        if not issues:
            return {}

        if batch_size <= 0:
            raise ValueError(f"batch_size 必须大于 0，当前值: {batch_size}")

        all_results = {}
        failed_issues = []

        # 分批处理
        batch_count = (len(issues) + batch_size - 1) // batch_size
        logger.info(
            f"开始批量分析: {len(issues)} 个 Issues, {batch_count} 批, "
            f"每批 {batch_size} 个"
        )

        for i in range(0, len(issues), batch_size):
            batch = issues[i : i + batch_size]
            batch_num = i // batch_size + 1

            try:
                # 批量分析
                batch_result = self._analyze_one_batch(batch)

                # 处理结果
                for j, analysis in enumerate(batch_result.results):
                    issue = batch[j]
                    key = f"{issue.repo}#{issue.issue_id}"

                    if analysis is not None:
                        all_results[key] = analysis
                    else:
                        failed_issues.append(issue)

                # 记录统计
                logger.debug(
                    f"批次 {batch_num}/{batch_count}: "
                    f"{batch_result.success_count}/{len(batch)} 成功"
                )

            except Exception as e:
                # 整批失败，标记所有为待重试
                logger.warning(
                    f"批次 {batch_num}/{batch_count} 分析失败: {e}，"
                    f"将单独重试 {len(batch)} 个 Issues"
                )
                failed_issues.extend(batch)

        # 第二轮：单独重试失败的 Issues
        if failed_issues:
            logger.info(f"单独重试 {len(failed_issues)} 个失败的 Issues")
            retry_results = self._retry_failed_singly(failed_issues)
            all_results.update(retry_results)

        # 统计
        success_rate = len(all_results) / len(issues) * 100 if issues else 0
        logger.info(
            f"批量分析完成: {len(all_results)}/{len(issues)} 成功 ({success_rate:.1f}%)"
        )

        return all_results

    def _analyze_one_batch(
        self,
        issues: list[IssueInfo],
    ) -> BatchIssueAnalysis:  # type: ignore[no-any-return]
        """分析一批 Issues

        Args:
            issues: Issue 列表（2-20 个为宜）

        Returns:
            批量分析结果
        """
        prompt = self.build_batch_prompt(issues)

        # 调用 LLM 批量分析
        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=BatchIssueAnalysis,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4000,  # 批量分析需要更多 tokens
            )

        return self._run_with_llm_retry(_call)

    def _retry_failed_singly(
        self,
        issues: list[IssueInfo],
    ) -> dict[str, IssueAnalysis]:
        """单独重试失败的 Issues

        Args:
            issues: 失败的 Issue 列表

        Returns:
            {issue_key: 分析结果} 字典
        """
        results = {}

        for issue in issues:
            try:
                analysis = self.analyze(issue)
                key = f"{issue.repo}#{issue.issue_id}"
                results[key] = analysis
            except Exception as e:
                logger.debug(f"单独重试失败 {issue.repo}#{issue.issue_id}: {e}")

        return results
