"""AI 趋势信号分析器

支持 Anthropic Claude 和智谱 AI (GLM) + Instructor 提取结构化趋势信号。
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.config import DEFAULT_ANTHROPIC_BASE_URL, DEFAULT_ANTHROPIC_MODEL
from trendpluse.logger import get_logger
from trendpluse.models.signal import DailyReport, Signal

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

    def analyze_pr(self, pr_details: dict) -> Signal:
        """分析单个 PR 提取信号

        Args:
            pr_details: PR 详情字典

        Returns:
            提取的信号
        """
        # 构建 Prompt
        prompt = f"""分析以下 GitHub PR，提取趋势信号。

PR 标题: {pr_details.get("title", "")}
PR 描述: {pr_details.get("body", "")}
仓库: {pr_details.get("repo_name", "")}
作者: {pr_details.get("author", "")}
链接: {pr_details.get("url", "")}

请提取关键信息并返回结构化信号。
"""

        # 使用带重试机制的 LLM 调用
        signal = self._call_llm_for_signal(prompt)

        # 确保 ID 格式
        if not signal.id:
            signal.id = (
                f"{pr_details.get('repo_name', 'unknown')}-"
                f"{pr_details.get('number', 0)}"
            )

        # 确保源包含 PR URL
        if not signal.sources:
            signal.sources = [pr_details.get("url", "")]

        # 确保相关仓库
        if not signal.related_repos:
            repo_name = pr_details.get("repo_name")
            if repo_name:
                signal.related_repos = [repo_name]

        return signal  # type: ignore[no-any-return]

    def _call_llm_for_signal(self, prompt: str) -> Signal:
        """调用 LLM 提取 PR 信号（带重试机制）

        Args:
            prompt: 分析提示词

        Returns:
            提取的信号

        Raises:
            RETRYABLE_ERRORS: 可重试的错误（超时、速率限制）
            Exception: 其他错误向上传播
        """

        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=Signal,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
            )

        return self._run_with_llm_retry(_call)  # type: ignore[no-any-return]

    def analyze_prs(self, pr_list: list[dict], max_workers: int = 3) -> list[Signal]:
        """批量分析多个 PR（并行处理）

        Args:
            pr_list: PR 详情列表
            max_workers: 最大并行线程数（默认 3）

        Returns:
            信号列表
        """
        # 处理空列表
        if not pr_list:
            return []

        # 单个 PR 时直接调用，避免线程池开销
        if len(pr_list) == 1:
            pr = pr_list[0]
            try:
                return [self.analyze_pr(pr)]
            except Exception as e:
                repo_name = pr.get("repo_name", "unknown")
                number = pr.get("number", 0)
                logger.debug(f"TrendAnalyzer: 分析 PR {repo_name}#{number} 失败: {e}")
                return []

        # 并行处理多个 PRs
        signals = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任务
            future_to_pr: dict = {}
            for pr in pr_list:
                future = executor.submit(self.analyze_pr, pr)
                future_to_pr[future] = pr

            # 收集结果
            for future in as_completed(future_to_pr):
                pr = future_to_pr[future]
                try:
                    signal = future.result()
                    signals.append(signal)
                except Exception as e:
                    # 单个失败不影响其他 PRs
                    repo_name = pr.get("repo_name", "unknown")
                    number = pr.get("number", 0)
                    logger.debug(
                        f"TrendAnalyzer: 分析 PR {repo_name}#{number} 失败: {e}"
                    )

        return signals

    def aggregate_and_generate_report(
        self,
        pr_signals: list[Signal],
        commit_signals: list[Signal],
        release_signals: list[Signal],
        date: str,
    ) -> DailyReport:
        """跨类型聚合信号并生成高层次趋势报告（使用强一致性机制）

        Args:
            pr_signals: PR 信号列表
            commit_signals: Commit 技术点信号列表
            release_signals: Release 信号列表
            date: 日期

        Returns:
            每日报告，包含聚合后的高层次趋势
        """
        # 步骤 1: 构建 ID 到 Signal 的映射（用于后处理解析）
        signal_map: dict[str, Signal] = {}
        for idx, signal in enumerate(pr_signals):
            signal_map[f"pr-{idx}"] = signal
        for idx, signal in enumerate(commit_signals):
            signal_map[f"commit-{idx}"] = signal
        for idx, signal in enumerate(release_signals):
            signal_map[f"release-{idx}"] = signal

        # 步骤 2: 使用带 ID 的格式化函数，确保 LLM 能看到完整信息
        prompt = f"""分析以下多种类型的 GitHub 活动，识别高层次的技术趋势。

日期: {date}

## 数据统计
- PR 信号: {len(pr_signals)} 个
- Commit 技术点: {len(commit_signals)} 个
- Release 信号: {len(release_signals)} 个

## PR 信号
{self._format_signals_with_ids(pr_signals, "pr") if pr_signals else "无"}

## Commit 技术点
{self._format_signals_with_ids(commit_signals, "commit") if commit_signals else "无"}

## Release 信号
{self._format_signals_with_ids(release_signals, "release") if release_signals else "无"}

## 分析要求

请识别**跨类型的模式和趋势**，例如：
- 多个项目同时推出相似功能（可能同时出现在 PR 和 Commit 中）
- 技术方向的集体演进（多个相关变更指向同一趋势）
- 重要版本发布与相关 PR/Commit 的关联

## 输出要求

返回一份 DailyReport，只包含以下字段：
1. date: 日期字符串
2. summary_brief: 当日总览（2-3 句话）
3. engineering_signals: 聚合后的高层次工程趋势列表
4. research_signals: 聚合后的高层次研究趋势列表（目前可为空列表）
5. stats: 统计信息字典

**以下字段由代码自动填充，无需返回**：
- activity: 仓库活跃度数据（代码采集）
- releases: Release 数据（代码采集）
- breaking_changes: 不兼容变更（代码检测）
- monitored_repos: 监控仓库列表（代码配置）

重要：
- **source_signal_ids 字段必须填写**，用于后续溯源
- ID 格式为 "类型-索引"，例如 "pr-0", "commit-1", "release-2"
- **所有文本内容必须使用中文**（title、why_it_matters、summary_brief 等）
- 只返回真正有价值的跨类型趋势
- 如果没有发现明显的跨类型模式，返回空信号列表但保留 summary
"""

        # 步骤 3: 调用 LLM 聚合信号
        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=DailyReport,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=3000,
            )

        report = self._run_with_llm_retry(_call)

        # 确保日期正确
        report.date = date

        # 确保统计数据正确
        if not report.stats:
            report.stats = {}
        report.stats["total_prs_analyzed"] = len(pr_signals)
        report.stats["total_commits_analyzed"] = len(commit_signals)
        report.stats["total_releases"] = len(release_signals)
        report.stats["high_impact_signals"] = len(
            self.filter_high_impact(report.engineering_signals, threshold=4)
        )

        # 步骤 4: 使用强一致性机制解析 sources（确定性后处理）
        # 这是确保 100% 正确性的关键步骤
        report = self._resolve_sources_from_ids(report, signal_map)

        # 清空低层次信号（已被聚合到高层次趋势中）
        # 注意：只清空 commit_signals，因为它们被聚合到 engineering/research_signals
        # release_signals 应该保留，因为它们是独立的分析结果
        report.commit_signals = []

        return report  # type: ignore[no-any-return]

    def generate_report(self, signals: list[Signal], date: str) -> DailyReport:
        """生成每日报告

        Args:
            signals: 信号列表
            date: 日期

        Returns:
            每日报告
        """
        # 分类信号
        categorized = self.categorize_signals(signals)

        # 筛选高影响信号
        high_impact_count = len(self.filter_high_impact(signals, threshold=4))

        # 构建 Prompt
        prompt = f"""基于以下信号生成每日趋势报告。

日期: {date}
工程信号数量: {len(categorized["engineering"])}
研究信号数量: {len(categorized["research"])}
高影响信号数量: {high_impact_count}

工程信号:
{self._format_signals(categorized["engineering"])}

研究信号:
{self._format_signals(categorized["research"])}

## 输出要求

返回 DailyReport，只包含：
- date: 日期字符串
- summary_brief: 当日总览（2-3 句话）
- engineering_signals: 工程信号列表
- research_signals: 研究信号列表（目前可为空）
- stats: 统计信息

**无需返回以下字段**（由代码自动填充）：
- activity, releases, breaking_changes, monitored_repos
"""

        def _call():
            return self.client.chat.completions.create(
                model=self.model,
                response_model=DailyReport,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000,
            )

        report = self._run_with_llm_retry(_call)

        # 确保日期正确
        report.date = date

        # 确保统计数据正确
        if not report.stats:
            report.stats = {}
        report.stats["total_prs_analyzed"] = len(signals)
        report.stats["high_impact_signals"] = high_impact_count

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

    def categorize_signals(self, signals: list[Signal]) -> dict[str, list[Signal]]:
        """按类型分类信号

        Args:
            signals: 信号列表

        Returns:
            分类后的信号字典
        """
        categorized: dict[str, list[Signal]] = {
            "engineering": [],
            "research": [],
        }

        for signal in signals:
            categorized[signal.category].append(signal)

        return categorized

    def _format_signals(self, signals: list[Signal]) -> str:
        """格式化信号列表为文本

        包含完整信息（sources、related_repos），以便 LLM 在聚合时保留原始链接。

        Args:
            signals: 信号列表

        Returns:
            格式化文本
        """
        if not signals:
            return "无"

        lines = []
        for signal in signals:
            # 格式化来源链接
            sources_text = "\n    ".join(signal.sources) if signal.sources else "无"
            # 格式化相关仓库
            repos_text = (
                ", ".join(signal.related_repos) if signal.related_repos else "无"
            )

            lines.append(
                f"- {signal.title} (评分: {signal.impact_score}, "
                f"类型: {signal.type})\n  {signal.why_it_matters}\n"
                f"  相关仓库: {repos_text}\n  来源:\n    {sources_text}"
            )

        return "\n".join(lines)

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

        for signal in report.engineering_signals:
            # 检查是否有 source_signal_ids 字段
            signal_ids = getattr(signal, "source_signal_ids", None)

            if signal_ids:
                # 根据 IDs 查找原始 sources（确定性操作）
                resolved_sources: list[str] = []
                resolved_repos: set[str] = set()

                for sig_id in signal_ids:
                    if sig_id in signal_map:
                        original_signal = signal_map[sig_id]
                        # 收集 sources
                        resolved_sources.extend(original_signal.sources)
                        # 收集 repos
                        resolved_repos.update(original_signal.related_repos)
                    else:
                        from trendpluse.logger import get_logger

                        logger = get_logger(__name__)
                        logger.warning(f"聚合信号引用了不存在的 ID: {sig_id}")

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
