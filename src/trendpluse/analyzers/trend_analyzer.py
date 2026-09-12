"""AI 趋势信号分析器

支持 Anthropic Claude 和智谱 AI (GLM) + Instructor 提取结构化趋势信号。
"""

import asyncio
from typing import cast

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.config import DEFAULT_ANTHROPIC_BASE_URL, DEFAULT_ANTHROPIC_MODEL
from trendpluse.logger import get_logger
from trendpluse.models.signal import DailyReport, ReportStats, Signal
from trendpluse.models.source import AnalysisMaterial
from trendpluse.prompts import render_prompt

logger = get_logger(__name__)


class TrendAnalyzer(BaseLLMAnalyzer):
    """基于 AI 的趋势信号分析器

    使用 instructor 模式，支持结构化输出（直接返回 Pydantic 模型）。
    """

    def __init__(
        self,
        api_key: str,
        model: str = DEFAULT_ANTHROPIC_MODEL,
        base_url: str = DEFAULT_ANTHROPIC_BASE_URL,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ):
        """初始化分析器

        Args:
            api_key: API Key (智谱AI 或 Anthropic)
            model: 模型名称 (glm-4.7, claude-sonnet-4-20250514 等)
            base_url: API Base URL
        """
        # 使用 instructor 模式（默认）
        super().__init__(
            api_key=api_key,
            model=model,
            base_url=base_url,
            use_instructor=True,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    def _build_material_prompt(self, material: AnalysisMaterial) -> str:
        """基于分析材料构建提示词。"""
        return render_prompt(
            "trend_analyzer.pr_signal_extraction",
            number=material.source_ref.external_id,
            title=material.title,
            body=material.body,
            repo=material.source_ref.repo,
            author=material.author,
            url=material.source_ref.url,
        )

    def _build_aggregation_prompt(
        self,
        *,
        date: str,
        pr_signals: list[Signal],
        commit_signals: list[Signal],
        release_signals: list[Signal],
    ) -> str:
        """构建跨类型聚合提示词（同步/异步共用）。"""
        return render_prompt(
            "trend_analyzer.aggregation",
            date=date,
            pr_count=len(pr_signals),
            commit_count=len(commit_signals),
            release_count=len(release_signals),
            pr_text=(
                self._format_signals_with_ids(pr_signals, "pr") if pr_signals else "无"
            ),
            commit_text=(
                self._format_signals_with_ids(commit_signals, "commit")
                if commit_signals
                else "无"
            ),
            release_text=(
                self._format_signals_with_ids(release_signals, "release")
                if release_signals
                else "无"
            ),
        )

    def _apply_material_defaults(
        self, signal: Signal, material: AnalysisMaterial
    ) -> Signal:
        """用材料信息补齐信号默认字段。"""
        if not signal.id:
            signal.id = (
                f"{material.source_ref.repo or 'unknown'}-"
                f"{material.source_ref.external_id or '0'}"
            )

        if not signal.sources:
            signal.sources = [material.source_ref.url]

        if not signal.related_repos and material.source_ref.repo:
            signal.related_repos = [material.source_ref.repo]

        return signal

    async def analyze_material_async(self, material: AnalysisMaterial) -> Signal:
        prompt = self._build_material_prompt(material)

        signal = await self._call_llm_for_signal_async(prompt)
        return self._apply_material_defaults(signal, material)  # type: ignore[no-any-return]

    async def _call_llm_for_signal_async(self, prompt: str) -> Signal:
        async def _call():
            return await self._structured_create_async(
                response_model=Signal,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
            )

        return await self._run_with_llm_retry_async(_call)  # type: ignore[no-any-return]

    async def analyze_materials_async(
        self, materials: list[AnalysisMaterial], max_workers: int = 5
    ) -> list[Signal]:
        if not materials:
            return []

        if len(materials) == 1:
            material = materials[0]
            try:
                return [await self.analyze_material_async(material)]
            except Exception as e:
                repo_name = material.source_ref.repo
                number = material.source_ref.external_id
                logger.debug(
                    f"TrendAnalyzer: 异步分析 PR {repo_name}#{number} 失败: {e}"
                )
                return []

        semaphore = asyncio.Semaphore(max_workers)

        async def _run(material: AnalysisMaterial):
            async with semaphore:
                return await self.analyze_material_async(material)

        tasks = [_run(material) for material in materials]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        signals: list[Signal] = []
        for material, result in zip(materials, results):
            if isinstance(result, Exception):
                repo_name = material.source_ref.repo
                number = material.source_ref.external_id
                logger.debug(
                    f"TrendAnalyzer: 异步分析 PR {repo_name}#{number} 失败: {result}"
                )
                continue
            signals.append(cast(Signal, result))

        self._log_category_distribution("PR", signals)
        return signals

    @staticmethod
    def _log_category_distribution(source: str, signals: list[Signal]) -> None:
        """打印上游信号 category 分布（research 分类触发的可观测性）。"""
        if not signals:
            return
        counts: dict[str, int] = {}
        for signal in signals:
            counts[signal.category] = counts.get(signal.category, 0) + 1
        distribution = " ".join(
            f"{category}={count}" for category, count in sorted(counts.items())
        )
        logger.info(
            "%s 信号 category 分布: %s (total=%d)", source, distribution, len(signals)
        )

    async def aggregate_and_generate_report_async(
        self,
        pr_signals: list[Signal],
        commit_signals: list[Signal],
        release_signals: list[Signal],
        date: str,
    ) -> DailyReport:
        signal_map: dict[str, Signal] = {}
        for idx, signal in enumerate(pr_signals):
            signal_map[f"pr-{idx}"] = signal
        for idx, signal in enumerate(commit_signals):
            signal_map[f"commit-{idx}"] = signal
        for idx, signal in enumerate(release_signals):
            signal_map[f"release-{idx}"] = signal

        prompt = self._build_aggregation_prompt(
            date=date,
            pr_signals=pr_signals,
            commit_signals=commit_signals,
            release_signals=release_signals,
        )

        async def _call():
            return await self._structured_create_async(
                response_model=DailyReport,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=3000,
            )

        report = await self._run_with_llm_retry_async(_call)

        report.date = date
        report.stats = ReportStats()
        report.stats.total_prs_analyzed = len(pr_signals)
        report.stats.total_commits_analyzed = len(commit_signals)
        report.stats.total_releases = len(release_signals)
        report.stats.high_impact_signals = len(
            self.filter_high_impact(report.engineering_signals, threshold=4)
        )

        report = self._resolve_sources_from_ids(report, signal_map)
        report.commit_signals = []

        return report  # type: ignore[no-any-return]

    def filter_high_impact(
        self, signals: list[Signal], threshold: int = 4
    ) -> list[Signal]:
        """筛选高影响信号

        Args:
            signals: 信号列表
            threshold: 影响评分阈值

        Returns:
            高影响信号列表
        """
        return [s for s in signals if s.impact_score >= threshold]

    def _format_signals_with_ids(self, signals: list[Signal], prefix: str) -> str:
        """格式化信号列表为文本（带 ID 引用）

        用于强一致性方案：每个信号都有唯一 ID，方便 LLM 引用和后处理溯源。

        Args:
            signals: 信号列表
            prefix: ID 前缀（pr/commit/release）

        Returns:
            格式化文本
        """
        if not signals:
            return "无"

        lines = []
        for idx, signal in enumerate(signals):
            sig_id = f"{prefix}-{idx}"

            # 格式化来源链接
            sources_text = "\n    ".join(signal.sources) if signal.sources else "无"
            # 格式化相关仓库
            repos_text = (
                ", ".join(signal.related_repos) if signal.related_repos else "无"
            )

            lines.append(
                f"[{sig_id}] {signal.title} "
                f"(评分: {signal.impact_score}, 类型: {signal.type})\n"
                f"  {signal.why_it_matters}\n"
                f"  相关仓库: {repos_text}\n"
                f"  来源:\n    {sources_text}"
            )

        return "\n".join(lines)

    def _resolve_sources_from_ids(
        self,
        report: "DailyReport",
        signal_map: dict[str, Signal],
    ) -> "DailyReport":
        """根据 source_signal_ids 解析 sources（确定性）

        这是确保强一致性的关键方法：
        - 不依赖 LLM 正确传递 sources
        - 通过 ID 查找原始信号，提取其 sources
        - 确保最终结果 100% 包含正确的 URL

        Args:
            report: LLM 返回的报告
            signal_map: ID 到 Signal 的映射

        Returns:
            补充了 sources 的报告
        """

        for signal in [
            *report.engineering_signals,
            *report.research_signals,
        ]:
            # 检查是否有 source_signal_ids 字段
            signal_ids = getattr(signal, "source_signal_ids", None)

            if signal_ids:
                # 根据 IDs 查找原始 sources（确定性操作）
                resolved_sources: list[str] = []
                resolved_repos: set[str] = set()
                valid_ids: list[str] = []

                for sig_id in signal_ids:
                    if sig_id in signal_map:
                        original_signal = signal_map[sig_id]
                        # 收集 sources
                        resolved_sources.extend(original_signal.sources)
                        # 收集 repos
                        resolved_repos.update(original_signal.related_repos)
                        valid_ids.append(sig_id)
                    else:
                        from trendpluse.logger import get_logger

                        logger = get_logger(__name__)
                        logger.warning(
                            f"聚合信号引用了不存在的 ID: {sig_id}，已从引用中剔除"
                        )

                # 去除悬空 ID，避免脏引用进入前端与历史索引
                signal.source_signal_ids = valid_ids

                # 去重并设置
                signal.sources = list(set(resolved_sources))
                signal.related_repos = list(resolved_repos)

                # 验证
                if not signal.sources:
                    from trendpluse.logger import get_logger

                    logger = get_logger(__name__)
                    logger.warning(f"聚合信号 '{signal.id}' 没有解析到任何 sources")
            else:
                # Fallback: LLM 没有返回 source_signal_ids
                from trendpluse.logger import get_logger

                logger = get_logger(__name__)
                logger.warning(f"聚合信号 '{signal.id}' 缺少 source_signal_ids 字段")
                # 尝试从 LLM 返回的 sources 中验证
                if signal.sources:
                    # 如果有 signal_map，验证 sources
                    if signal_map:
                        valid_sources = self._validate_sources(
                            signal.sources, signal_map
                        )
                        signal.sources = valid_sources
                    # 如果没有 signal_map，保留 LLM 返回的 sources
                    # (这种情况在测试 mock 时可能出现)
                # else: sources 保持为空

        return report

    def _validate_sources(
        self, sources: list[str], signal_map: dict[str, Signal]
    ) -> list[str]:
        """验证 sources 是否来自原始信号集合

        Args:
            sources: LLM 返回的 sources
            signal_map: 原始信号映射

        Returns:
            验证通过的 sources 列表
        """
        # 收集所有有效的 sources
        valid_set = set()
        for signal in signal_map.values():
            valid_set.update(signal.sources)

        # 过滤出有效的 sources
        validated = [s for s in sources if s in valid_set]

        if len(validated) < len(sources):
            from trendpluse.logger import get_logger

            logger = get_logger(__name__)
            invalid = set(sources) - valid_set
            logger.warning(f"发现无效的 sources: {invalid}，已过滤")

        return validated
