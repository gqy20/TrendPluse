"""测试飞书通知脚本的辅助函数"""


class TestFindReportJson:
    """测试报告 JSON 文件查找功能"""

    def test_find_json_in_reports_daily_directory(self, tmp_path, monkeypatch):
        """测试：在 reports/daily 目录中找到 JSON 文件"""
        # Arrange
        report_date = "2026-01-05"
        reports_daily_dir = tmp_path / "reports" / "daily"
        reports_daily_dir.mkdir(parents=True)
        json_file = reports_daily_dir / f"report-{report_date}.json"
        json_file.write_text('{"date": "2026-01-05"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from trendpluse.cli.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result == json_file
        assert result.exists()

    def test_find_json_returns_none_when_not_found(self, tmp_path, monkeypatch):
        """测试：文件不存在时返回 None"""
        # Arrange
        report_date = "2026-01-05"
        monkeypatch.chdir(tmp_path)

        # Act
        from trendpluse.cli.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result is None
