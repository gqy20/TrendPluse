"""测试飞书通知脚本的辅助函数"""

import json


class TestFindReportJson:
    """测试报告 JSON 文件查找功能"""

    def test_find_json_in_reports_directory(self, tmp_path, monkeypatch):
        """测试：在 reports/ 目录中找到 JSON 文件"""
        # Arrange
        report_date = "2026-01-05"
        reports_dir = tmp_path / "reports"
        reports_dir.mkdir()
        json_file = reports_dir / f"report-{report_date}.json"
        json_file.write_text('{"date": "2026-01-05"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from scripts.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result == json_file
        assert result.exists()

    def test_find_json_in_current_directory(self, tmp_path, monkeypatch):
        """测试：在当前目录找到 JSON 文件（GitHub Actions artifact 下载后的场景）"""
        # Arrange
        report_date = "2026-01-05"
        json_file = tmp_path / f"report-{report_date}.json"
        json_file.write_text('{"date": "2026-01-05"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from scripts.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result == json_file
        assert result.exists()

    def test_find_json_prefers_reports_directory(self, tmp_path, monkeypatch):
        """测试：两个位置都存在时，优先使用 reports/ 目录"""
        # Arrange
        report_date = "2026-01-05"
        reports_dir = tmp_path / "reports"
        reports_dir.mkdir()
        reports_json = reports_dir / f"report-{report_date}.json"
        reports_json.write_text('{"location": "reports"}', encoding="utf-8")

        root_json = tmp_path / f"report-{report_date}.json"
        root_json.write_text('{"location": "root"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from scripts.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result == reports_json
        content = json.loads(result.read_text(encoding="utf-8"))
        assert content["location"] == "reports"

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
        from scripts.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result == json_file
        assert result.exists()

    def test_find_json_in_downloaded_artifact_structure(self, tmp_path, monkeypatch):
        """测试：在下载后的 artifact 子目录中找到 JSON 文件"""
        # Arrange
        report_date = "2026-01-05"
        artifact_dir = (
            tmp_path / "reports" / "trend-report-2026-01-05" / "reports" / "daily"
        )
        artifact_dir.mkdir(parents=True)
        json_file = artifact_dir / f"report-{report_date}.json"
        json_file.write_text('{"date": "2026-01-05"}', encoding="utf-8")

        monkeypatch.chdir(tmp_path)

        # Act
        from scripts.send_feishu_notification import find_report_json

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
        from scripts.send_feishu_notification import find_report_json

        result = find_report_json(report_date)

        # Assert
        assert result is None
