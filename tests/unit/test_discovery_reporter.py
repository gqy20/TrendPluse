"""DiscoveryReporter 测试

测试报告生成功能。
"""

from datetime import datetime

import pytest

from trendpluse.discovery.reporter import DiscoveryReporter
from trendpluse.models.discovery import DiscoveredProject, DiscoveryReport


class TestDiscoveryReporter:
    """DiscoveryReporter 测试"""

    @pytest.fixture
    def sample_report(self):
        """示例发现报告"""
        projects = [
            DiscoveredProject(
                repo="owner/repo1",
                name="repo1",
                description="High quality project",
                stars=5000,
                language="Python",
                topics=["ai", "ml"],
                license="MIT",
                open_issues=20,
                forks=200,
                watchers=100,
                last_commit_at=datetime.now(),
                discovery_source="trending",
                discovery_reason="Trending",
                quality_score=85.0,
                activity_level="high",
                recommended=True,
                recommendation_priority="high",
            ),
            DiscoveredProject(
                repo="owner/repo2",
                name="repo2",
                description="Medium quality project",
                stars=2000,
                language="TypeScript",
                topics=["web"],
                license="Apache-2.0",
                open_issues=10,
                forks=50,
                watchers=25,
                last_commit_at=datetime.now(),
                discovery_source="keyword",
                discovery_reason="Keyword: web",
                quality_score=65.0,
                activity_level="medium",
                recommended=True,
                recommendation_priority="medium",
            ),
        ]

        return DiscoveryReport(
            date="2025-01-31",
            total_discovered=2,
            passed_quality=2,
            high_priority=1,
            duplicates_removed=0,
            already_monitored=0,
            candidates=projects,
        )

    def test_generate_markdown_creates_valid_content(self, sample_report):
        """测试生成有效的 Markdown 内容"""
        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(sample_report)

        assert isinstance(markdown, str)
        assert len(markdown) > 0
        assert "# 项目发现报告" in markdown
        assert "## 发现概览" in markdown

    def test_markdown_includes_summary_table(self, sample_report):
        """测试 Markdown 包含概览表格"""
        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(sample_report)

        assert "| 总发现数 |" in markdown
        assert "| 通过质量评估 |" in markdown
        assert "| 高优先级 |" in markdown
        assert "2" in markdown  # 总发现数

    def test_markdown_includes_high_priority_section(self, sample_report):
        """测试 Markdown 包含高优先级推荐部分"""
        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(sample_report)

        assert "##" in markdown and "高优先级" in markdown
        assert "owner/repo1" in markdown

    def test_markdown_includes_project_details(self, sample_report):
        """测试 Markdown 包含项目详情"""
        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(sample_report)

        assert "Stars" in markdown
        assert "5,000" in markdown or "5000" in markdown
        assert "Python" in markdown
        assert "TypeScript" in markdown

    def test_generate_json_creates_valid_dict(self, sample_report):
        """测试生成有效的 JSON 字典"""
        reporter = DiscoveryReporter()
        json_data = reporter.generate_json(sample_report)

        assert isinstance(json_data, dict)
        assert "date" in json_data
        assert "candidates" in json_data
        assert json_data["total_discovered"] == 2

    def test_json_includes_all_report_fields(self, sample_report):
        """测试 JSON 包含所有报告字段"""
        reporter = DiscoveryReporter()
        json_data = reporter.generate_json(sample_report)

        expected_fields = [
            "date",
            "total_discovered",
            "passed_quality",
            "high_priority",
            "duplicates_removed",
            "already_monitored",
            "candidates",
        ]
        for field in expected_fields:
            assert field in json_data

    def test_json_serializes_projects_correctly(self, sample_report):
        """测试 JSON 正确序列化项目"""
        reporter = DiscoveryReporter()
        json_data = reporter.generate_json(sample_report)

        assert len(json_data["candidates"]) == 2
        assert json_data["candidates"][0]["repo"] == "owner/repo1"
        assert json_data["candidates"][0]["quality_score"] == 85.0

    def test_save_markdown_to_file(self, sample_report, tmp_path):
        """测试保存 Markdown 到文件"""
        reporter = DiscoveryReporter()
        output_file = tmp_path / "report.md"

        reporter.save_markdown(sample_report, output_file)

        assert output_file.exists()
        content = output_file.read_text()
        assert "# 项目发现报告" in content

    def test_save_json_to_file(self, sample_report, tmp_path):
        """测试保存 JSON 到文件"""
        reporter = DiscoveryReporter()
        output_file = tmp_path / "report.json"

        reporter.save_json(sample_report, output_file)

        assert output_file.exists()
        import json

        data = json.loads(output_file.read_text())
        assert data["total_discovered"] == 2

    def test_generate_markdown_with_empty_candidates(self):
        """测试空候选列表生成 Markdown"""
        empty_report = DiscoveryReport(
            date="2025-01-31",
            total_discovered=0,
            passed_quality=0,
            high_priority=0,
            duplicates_removed=0,
            already_monitored=0,
            candidates=[],
        )

        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(empty_report)

        assert "# 项目发现报告" in markdown
        assert "0" in markdown  # 总发现数为 0

    def test_markdown_includes_all_priority_sections(self, sample_report):
        """测试 Markdown 包含所有优先级部分"""
        reporter = DiscoveryReporter()
        markdown = reporter.generate_markdown(sample_report)

        # 应该有高优先级和中优先级部分
        assert "##" in markdown and "高优先级" in markdown
        assert "owner/repo1" in markdown
