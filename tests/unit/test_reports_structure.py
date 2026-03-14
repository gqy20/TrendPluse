"""reports 目录结构测试

测试按类型隔离的报告目录结构。
"""

from trendpluse.app.generate_report_index import (
    extract_discovery_report_info,
    generate_discovery_index,
    generate_index,
    sync_discovery_reports_to_docs,
    sync_reports_to_docs,
)


class TestReportsDirectoryStructure:
    """报告目录结构测试"""

    def test_reports_has_subdirectories(self, tmp_path):
        """测试 reports 目录包含子目录"""
        daily_dir = tmp_path / "daily"
        weekly_dir = tmp_path / "weekly"
        discovery_dir = tmp_path / "discovery"

        daily_dir.mkdir()
        weekly_dir.mkdir()
        discovery_dir.mkdir()

        assert daily_dir.exists()
        assert weekly_dir.exists()
        assert discovery_dir.exists()

    def test_sync_daily_reports_to_docs(self, tmp_path):
        """测试同步日报到 docs 目录"""
        # 创建源目录结构
        reports_dir = tmp_path / "reports"
        daily_dir = reports_dir / "daily"
        daily_dir.mkdir(parents=True)

        # 创建测试日报文件
        test_report = daily_dir / "report-2026-01-31.md"
        test_report.write_text("# TrendPulse 每日报告 - 2026-01-31\n\n测试内容")

        docs_reports_dir = tmp_path / "docs" / "reports"

        # 执行同步
        sync_reports_to_docs(reports_dir, docs_reports_dir)

        # 验证文件已同步
        synced_file = docs_reports_dir / "report-2026-01-31.md"
        assert synced_file.exists()
        assert "TrendPulse 每日报告" in synced_file.read_text()

    def test_sync_weekly_reports_to_docs(self, tmp_path):
        """测试同步周报到 docs 目录"""
        reports_dir = tmp_path / "reports"
        weekly_dir = reports_dir / "weekly"
        weekly_dir.mkdir(parents=True)

        test_report = weekly_dir / "weekly-2026-W04.md"
        test_report.write_text("# TrendPulse 周报\n\n测试周报")

        docs_reports_dir = tmp_path / "docs" / "reports"
        sync_reports_to_docs(reports_dir, docs_reports_dir)

        synced_file = docs_reports_dir / "weekly-2026-W04.md"
        assert synced_file.exists()

    def test_sync_discovery_reports_to_docs(self, tmp_path):
        """测试同步发现报告到 docs 目录

        发现报告被复制到 docs/discovery-reports/ 子目录。
        """
        reports_dir = tmp_path / "reports"
        discovery_dir = reports_dir / "discovery"
        discovery_dir.mkdir(parents=True)

        test_report = discovery_dir / "discovery-2026-01-31.md"
        test_report.write_text("# 项目发现报告\n\n测试发现内容")

        docs_dir = tmp_path / "docs"
        docs_dir.mkdir(parents=True)
        sync_discovery_reports_to_docs(reports_dir, docs_dir)

        # 验证文件被复制到 docs/discovery-reports/ 子目录
        synced_file = docs_dir / "discovery-reports" / "discovery-2026-01-31.md"
        assert synced_file.exists()
        # 验证文件未被复制到 docs 根目录
        root_file = docs_dir / "discovery-2026-01-31.md"
        assert not root_file.exists()

    def test_generate_index_reads_from_subdirectories(self, tmp_path):
        """测试生成索引从子目录读取报告"""
        reports_dir = tmp_path / "reports"
        daily_dir = reports_dir / "daily"
        weekly_dir = reports_dir / "weekly"

        daily_dir.mkdir(parents=True)
        weekly_dir.mkdir(parents=True)

        # 创建测试日报
        (daily_dir / "report-2026-01-31.md").write_text(
            "# TrendPulse 每日报告 - 2026-01-31\n\n> 测试日报"
        )

        # 创建测试周报
        (weekly_dir / "weekly-2026-W04.md").write_text(
            "# TrendPulse 周报 (2026-W04: 2026-01-20 ~ 2026-01-26)\n\n> 测试周报"
        )

        output_path = tmp_path / "index.md"
        generate_index(reports_dir, output_path)

        assert output_path.exists()
        content = output_path.read_text()
        assert "2026-01-31" in content
        assert "2026-W04" in content
        assert "最新日报" in content
        assert "最近日报" in content
        assert "最近周报" in content

    def test_generate_index_includes_daily_metrics_table(self, tmp_path):
        """测试生成索引包含日报指标摘要"""
        reports_dir = tmp_path / "reports"
        daily_dir = reports_dir / "daily"
        weekly_dir = reports_dir / "weekly"
        daily_dir.mkdir(parents=True)
        weekly_dir.mkdir(parents=True)

        (daily_dir / "report-2026-02-01.md").write_text(
            "\n".join(
                [
                    "# TrendPulse 每日报告 - 2026-02-01",
                    "",
                    "> 测试摘要",
                    "",
                    "## 📊 统计信息",
                    "",
                    "- **分析 PR 数**: 12",
                    "- **高影响信号数**: 4",
                    "- **Release 数**: 2",
                    "- **涉及仓库数**: 7",
                    "- **分析 Commit 数**: 20",
                    "- **Breaking Changes 数**: 1",
                ]
            ),
            encoding="utf-8",
        )

        output_path = tmp_path / "index.md"
        generate_index(reports_dir, output_path)

        content = output_path.read_text(encoding="utf-8")
        assert "| 分析 PR 数 | 12 | 高影响信号 | 4 |" in content
        assert "| 涉及仓库数 | 7 | Release 数 | 2 |" in content
        assert "| Commit 数 | 20 | Breaking Changes | 1 |" in content

    def test_generate_index_skips_latest_items_in_history_tables(self, tmp_path):
        """测试历史表格不重复展示最新日报和最新周报。"""
        reports_dir = tmp_path / "reports"
        daily_dir = reports_dir / "daily"
        weekly_dir = reports_dir / "weekly"
        daily_dir.mkdir(parents=True)
        weekly_dir.mkdir(parents=True)

        (daily_dir / "report-2026-02-02.md").write_text(
            "# TrendPulse 每日报告 - 2026-02-02\n\n> 第二份日报",
            encoding="utf-8",
        )
        (daily_dir / "report-2026-02-01.md").write_text(
            "# TrendPulse 每日报告 - 2026-02-01\n\n> 第一份日报",
            encoding="utf-8",
        )
        (weekly_dir / "weekly-2026-W05.md").write_text(
            "# TrendPulse 周报 (2026-W05: 2026-01-27 ~ 2026-02-02)\n\n> 第二份周报",
            encoding="utf-8",
        )
        (weekly_dir / "weekly-2026-W04.md").write_text(
            "# TrendPulse 周报 (2026-W04: 2026-01-20 ~ 2026-01-26)\n\n> 第一份周报",
            encoding="utf-8",
        )

        output_path = tmp_path / "index.md"
        generate_index(reports_dir, output_path)

        content = output_path.read_text(encoding="utf-8")
        assert "### [2026-02-02](report-2026-02-02.md)" in content
        assert "| 2026-02-01 | 0 | 0 | 0 | [查看](report-2026-02-01.md) |" in content
        assert (
            "| 2026-02-02 | 0 | 0 | 0 | [查看](report-2026-02-02.md) |" not in content
        )
        assert "### [2026-W05](weekly-2026-W05.md)" in content
        assert (
            "| 2026-W04 | 2026-01-20 ~ 2026-01-26 | [查看](weekly-2026-W04.md) |"
            in content
        )
        assert (
            "| 2026-W05 | 2026-01-27 ~ 2026-02-02 | [查看](weekly-2026-W05.md) |"
            not in content
        )

    def test_extract_discovery_report_info_parses_top_projects(self, tmp_path):
        """测试发现报告解析能提取高优先级项目与分类分布"""
        report_path = tmp_path / "discovery-2026-03-06.md"
        report_path.write_text(
            "\n".join(
                [
                    "# 项目发现报告 (2026-03-06)",
                    "",
                    "## 发现概览",
                    "",
                    "| 指标 | 数值 |",
                    "|------|------|",
                    "| 总发现数 | 200 |",
                    "| 通过质量评估 | 180 |",
                    "| 高优先级 | 120 |",
                    "| 去重移除 | 40 |",
                    "| 已在监控 | 20 |",
                    "",
                    "### 📋 分类分布",
                    "",
                    "| 分类 | 数量 |",
                    "|------|------|",
                    "| 🤖 AI Agents | 30 |",
                    "| 🔍 RAG/检索 | 18 |",
                    "",
                    "## 🌟 高优先级推荐",
                    "",
                    "### open-webui/open-webui",
                    "",
                    "| 指标 | 数值 |",
                    "|------|------|",
                    "| Stars | 125,952 |",
                    "",
                    "### infiniflow/ragflow",
                    "",
                    "| 指标 | 数值 |",
                    "|------|------|",
                    "| Stars | 74,273 |",
                ]
            ),
            encoding="utf-8",
        )

        info = extract_discovery_report_info(report_path)

        assert info is not None
        assert info["stats"]["high_priority"] == "120"
        assert info["top_projects"][0]["repo"] == "open-webui/open-webui"
        assert info["top_projects"][0]["stars"] == 125952
        assert info["category_distribution"][0]["name"] == "🤖 AI Agents"

    def test_generate_discovery_index_includes_top_projects(self, tmp_path):
        """测试发现索引包含高优先级推荐与分类分布"""
        reports_dir = tmp_path / "reports"
        discovery_dir = reports_dir / "discovery"
        discovery_dir.mkdir(parents=True)

        (discovery_dir / "discovery-2026-03-06.md").write_text(
            "\n".join(
                [
                    "# 项目发现报告 (2026-03-06)",
                    "",
                    "## 发现概览",
                    "",
                    "| 指标 | 数值 |",
                    "|------|------|",
                    "| 总发现数 | 200 |",
                    "| 通过质量评估 | 180 |",
                    "| 高优先级 | 120 |",
                    "| 去重移除 | 40 |",
                    "| 已在监控 | 20 |",
                    "",
                    "### 📋 分类分布",
                    "",
                    "| 分类 | 数量 |",
                    "|------|------|",
                    "| 🤖 AI Agents | 30 |",
                    "",
                    "## 🌟 高优先级推荐",
                    "",
                    "### open-webui/open-webui",
                    "",
                    "| 指标 | 数值 |",
                    "|------|------|",
                    "| Stars | 125,952 |",
                ]
            ),
            encoding="utf-8",
        )

        docs_dir = tmp_path / "docs"
        docs_dir.mkdir(parents=True)

        generate_discovery_index(reports_dir, docs_dir)

        content = (docs_dir / "discovery.md").read_text(encoding="utf-8")
        assert "本期概览" in content
        assert "高优先级推荐 Top 5" in content
        assert "open-webui/open-webui" in content
        assert "分类分布 Top 5" in content
        assert "关于发现功能" not in content
