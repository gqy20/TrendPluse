"""发现报告生成器

生成 Markdown 和 JSON 格式的项目发现报告。
"""

import json
from pathlib import Path

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveryReport

logger = get_logger(__name__)


class DiscoveryReporter:
    """发现报告生成器

    支持生成 Markdown 和 JSON 格式的报告。
    """

    def generate_markdown(self, report: DiscoveryReport) -> str:
        """生成 Markdown 报告

        Args:
            report: 发现报告数据

        Returns:
            Markdown 格式报告
        """
        lines = [
            f"# 项目发现报告 ({report.date})",
            "",
            "## 发现概览",
            "",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| 总发现数 | {report.total_discovered} |",
            f"| 通过质量评估 | {report.passed_quality} |",
            f"| 高优先级 | {report.high_priority} |",
            f"| 去重移除 | {report.duplicates_removed} |",
            f"| 已在监控 | {report.already_monitored} |",
        ]

        # 按优先级分组
        high_priority = [
            p for p in report.candidates if p.recommendation_priority == "high"
        ]
        medium_priority = [
            p for p in report.candidates if p.recommendation_priority == "medium"
        ]
        low_priority = [
            p for p in report.candidates if p.recommendation_priority == "low"
        ]

        # 高优先级推荐
        if high_priority:
            lines.extend(["", "## 🌟 高优先级推荐"])
            for i, project in enumerate(high_priority, 1):
                lines.extend(self._format_project(project, i))

        # 中优先级推荐
        if medium_priority:
            lines.extend(["", "## ⭐ 中优先级推荐"])
            for i, project in enumerate(medium_priority, 1):
                lines.extend(self._format_project(project, i))

        # 低优先级
        if low_priority:
            lines.extend(["", "## 低优先级"])
            for i, project in enumerate(low_priority, 1):
                lines.extend(self._format_project(project, i))

        return "\n".join(lines)

    def _format_project(
        self,
        project,
        index: int,
    ) -> list[str]:
        """格式化单个项目信息

        Args:
            project: 项目对象
            index: 序号

        Returns:
            格式化的文本行列表
        """
        # 转义描述中的 HTML 特殊字符，避免 Markdown 解析错误
        description = project.description.replace("<", "&lt;").replace(">", "&gt;")

        lines = [
            "",
            f"### {index}. {project.repo}",
            "",
            f"**描述**: {description}",
            "",
            f"**发现来源**: {project.discovery_source}",
            "",
            f"**发现原因**: {project.discovery_reason}",
            "",
            f"**质量评分**: {project.quality_score:.0f}/100",
            "",
            f"**活跃度**: {project.activity_level}",
            "",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| Stars | {project.stars:,} |",
            f"| 语言 | {project.language} |",
            f"| Forks | {project.forks:,} |",
            f"| Issues | {project.open_issues:,} |",
        ]

        if project.topics:
            lines.append(f"| Topics | {', '.join(project.topics)} |")

        if project.license:
            lines.append(f"| 许可证 | {project.license} |")

        # 添加 AI 分析的项目亮点
        if project.highlight:
            lines.extend(["", "---", ""])
            lines.append(project.highlight.format_as_markdown())

        lines.append("")
        return lines

    def generate_json(self, report: DiscoveryReport) -> dict:
        """生成 JSON 格式报告

        Args:
            report: 发现报告数据

        Returns:
            JSON 可序列化的字典
        """
        return {
            "date": report.date,
            "total_discovered": report.total_discovered,
            "passed_quality": report.passed_quality,
            "high_priority": report.high_priority,
            "duplicates_removed": report.duplicates_removed,
            "already_monitored": report.already_monitored,
            "candidates": [p.model_dump(mode="json") for p in report.candidates],
        }

    def save_markdown(
        self,
        report: DiscoveryReport,
        output_path: Path,
    ) -> None:
        """保存 Markdown 报告到文件

        Args:
            report: 发现报告数据
            output_path: 输出文件路径
        """
        markdown = self.generate_markdown(report)
        output_path.write_text(markdown, encoding="utf-8")
        logger.info(f"Markdown 报告已保存: {output_path}")

    def save_json(
        self,
        report: DiscoveryReport,
        output_path: Path,
    ) -> None:
        """保存 JSON 报告到文件

        Args:
            report: 发现报告数据
            output_path: 输出文件路径
        """
        json_data = self.generate_json(report)
        output_path.write_text(
            json.dumps(json_data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        logger.info(f"JSON 报告已保存: {output_path}")
