"""reports 目录结构测试

测试按类型隔离的报告目录结构。
"""

from trendpluse.app.generate_report_index import (
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
