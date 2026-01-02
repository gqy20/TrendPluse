"""AI 趋势信号分析器

支持 Anthropic Claude 和智谱 AI (GLM) + Instructor 提取结构化趋势信号。
"""

import anthropic
import instructor

from trendpluse.models.signal import DailyReport, Signal


class TrendAnalyzer:
    """基于 AI 的趋势信号分析器"""

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str = "https://open.bigmodel.cn/api/anthropic",
    ):
        """初始化分析器

        Args:
            api_key: API Key (智谱AI 或 Anthropic)
            model: 模型名称 (glm-4.7, claude-sonnet-4-20250514 等)
            base_url: API Base URL
        """
        self.model = model
        # 使用 Anthropic 客户端 (支持智谱AI Anthropic兼容端点)
        self.client = instructor.from_anthropic(
            anthropic.Anthropic(api_key=api_key, base_url=base_url)
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

        signal = self.client.chat.completions.create(
            model=self.model,
            response_model=Signal,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
        )

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
        if not signal.related_repos and pr_details.get("repo_name"):
            signal.related_repos = [pr_details.get("repo_name")]

        return signal

    def analyze_prs(self, pr_list: list[dict]) -> list[Signal]:
        """批量分析多个 PR

        Args:
            pr_list: PR 详情列表

        Returns:
            信号列表
        """
        signals = []

        for pr in pr_list:
            try:
                signal = self.analyze_pr(pr)
                signals.append(signal)
            except Exception as e:
                repo_name = pr.get("repo_name", "unknown")
                number = pr.get("number", 0)
                print(f"分析 PR {repo_name}#{number} 失败: {e}")
                continue

        return signals

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

请生成一份简洁的每日报告。
"""

        report = self.client.chat.completions.create(
            model=self.model,
            response_model=DailyReport,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
        )

        # 确保日期正确
        report.date = date

        # 确保统计数据正确
        if not report.stats:
            report.stats = {}
        report.stats["total_prs_analyzed"] = len(signals)
        report.stats["high_impact_signals"] = high_impact_count

        return report

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
        categorized = {
            "engineering": [],
            "research": [],
        }

        for signal in signals:
            categorized[signal.category].append(signal)

        return categorized

    def _format_signals(self, signals: list[Signal]) -> str:
        """格式化信号列表为文本

        Args:
            signals: 信号列表

        Returns:
            格式化文本
        """
        if not signals:
            return "无"

        lines = []
        for signal in signals:
            lines.append(
                f"- {signal.title} (评分: {signal.impact_score}, "
                f"类型: {signal.type})\n  {signal.why_it_matters}"
            )

        return "\n".join(lines)
