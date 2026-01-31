"""发现报告生成器

生成 Markdown 和 JSON 格式的项目发现报告。
"""

import json
from collections import defaultdict
from collections.abc import Collection
from pathlib import Path

from trendpluse.discovery.classifier import ProjectClassifier
from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveryReport

logger = get_logger(__name__)


class DiscoveryReporter:
    """发现报告生成器

    支持生成 Markdown 和 JSON 格式的报告。
    """

    # 分类显示顺序和图标
    CATEGORY_ICONS = {
        "AI Agents": "🤖",
        "RAG/检索": "🔍",
        "LLM 界面": "💬",
        "开发工具": "🛠️",
        "数据/基础设施": "📊",
        "学习资源": "📚",
        "其他": "📁",
    }

    def generate_markdown(self, report: DiscoveryReport) -> str:
        """生成 Markdown 报告

        Args:
            report: 发现报告数据

        Returns:
            Markdown 格式报告
        """
        # 对所有项目进行分类
        classifier = ProjectClassifier()
        classified = classifier.classify_batch(report.candidates)
        category_stats = classifier.get_category_stats(classified)

        # 按分类和优先级组织项目
        projects_by_category_and_priority = self._organize_projects(
            report.candidates, classified
        )

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
            "",
        ]

        # 添加分类统计
        if category_stats:
            lines.extend(self._format_category_stats(category_stats))

        # 添加快速导航
        lines.extend(self._generate_navigation(projects_by_category_and_priority))

        # 按分类和优先级展示项目
        for category in self._get_category_order(category_stats.keys()):
            if category not in projects_by_category_and_priority:
                continue

            icon = self.CATEGORY_ICONS.get(category, "📁")
            count = category_stats.get(category, 0)
            lines.extend(["", f"## {icon} {category} ({count} 个项目)", ""])

            # 先显示高优先级
            if "high" in projects_by_category_and_priority[category]:
                lines.extend(["", "### 🌟 高优先级", ""])
                for project in projects_by_category_and_priority[category]["high"]:
                    lines.extend(self._format_project(project))

            # 再显示中优先级
            if "medium" in projects_by_category_and_priority[category]:
                lines.extend(["", "### ⭐ 中优先级", ""])
                for project in projects_by_category_and_priority[category]["medium"]:
                    lines.extend(self._format_project(project))

            # 低优先级（可选，通常省略）
            if "low" in projects_by_category_and_priority[category]:
                lines.extend(["", "### 低优先级", ""])
                for project in projects_by_category_and_priority[category]["low"]:
                    lines.extend(self._format_project(project))

        return "\n".join(lines)

    def _organize_projects(
        self, candidates: list, classified: dict[str, list[str]]
    ) -> dict[str, dict[str, list]]:
        """按分类和优先级组织项目

        Args:
            candidates: 项目列表
            classified: 分类结果

        Returns:
            {category: {priority: [projects]}} 嵌套字典
        """
        organized: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))

        for project in candidates:
            categories = classified.get(project.repo, ["其他"])
            priority = project.recommendation_priority

            for category in categories:
                organized[category][priority].append(project)

        # 对每个分类内的项目按质量分数排序
        for category in organized:
            for priority in organized[category]:
                organized[category][priority].sort(
                    key=lambda p: p.quality_score, reverse=True
                )

        return organized

    def _get_category_order(self, categories: Collection[str]) -> list[str]:
        """获取分类显示顺序

        Args:
            categories: 现有分类集合

        Returns:
            排序后的分类列表
        """
        # 预定义的显示顺序
        order = [
            "AI Agents",
            "RAG/检索",
            "LLM 界面",
            "开发工具",
            "数据/基础设施",
            "学习资源",
        ]

        # 先添加预定义的且存在的分类
        result = [c for c in order if c in categories]

        # 再添加其他分类
        for category in categories:
            if category not in order:
                result.append(category)

        return result

    def _format_category_stats(self, stats: dict[str, int]) -> list[str]:
        """格式化分类统计

        Args:
            stats: 分类统计字典

        Returns:
            格式化的文本行列表
        """
        lines = [
            "",
            "### 📋 分类分布",
            "",
            "| 分类 | 数量 |",
            "|------|------|",
        ]

        for category in self._get_category_order(stats.keys()):
            icon = self.CATEGORY_ICONS.get(category, "📁")
            count = stats[category]
            lines.append(f"| {icon} {category} | {count} |")

        return lines

    def _generate_navigation(
        self, projects_by_category: dict[str, dict[str, list]]
    ) -> list[str]:
        """生成快速导航目录

        Args:
            projects_by_category: 按分类组织的项目

        Returns:
            格式化的导航文本行列表
        """
        lines = [
            "",
            "## 📑 快速导航",
            "",
        ]

        # 按分类的导航
        categories = list(projects_by_category.keys())
        if categories:
            lines.append("### 按技术分类")
            for category in self._get_category_order(categories):
                icon = self.CATEGORY_ICONS.get(category, "📁")
                lines.append(
                    f"- [{icon} {category}](#{category.lower().replace('/', '-')})"
                )
            lines.append("")

        return lines

    def _format_project(self, project) -> list[str]:
        """格式化单个项目信息

        Args:
            project: 项目对象

        Returns:
            格式化的文本行列表
        """
        # 转义描述中的 HTML 特殊字符，避免 Markdown 解析错误
        description = project.description.replace("<", "&lt;").replace(">", "&gt;")

        lines = [
            "",
            f"### {project.repo}",
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
