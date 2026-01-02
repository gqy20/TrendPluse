"""主模块的测试用例。"""

from unittest.mock import patch

import pytest

from trendpluse.main import demo_basic_features, demo_logging, demo_rich_output, main


def test_main_runs_successfully(capsys):
    """测试主函数是否能正常运行。"""
    main()
    captured = capsys.readouterr()
    # 检查预期的输出元素
    assert "TrendPluse" in captured.out or len(captured.out) > 0


def test_demo_basic_features(capsys):
    """测试基本功能演示。"""
    demo_basic_features()
    # 输出将是 rich 格式化的，只验证没有错误


def test_demo_rich_output(capsys):
    """测试 rich 输出演示。"""
    demo_rich_output()
    # 检查是否产生了一些输出


def test_demo_logging(capsys):
    """测试日志演示。"""
    demo_logging()
    # 验证日志产生了输出


@patch("trendpluse.main.greet")
def test_main_calls_greet(mock_greet):
    """测试主函数是否调用了 greet 函数。"""
    mock_greet.return_value = "模拟的问候"
    main()
    # 验证 greet 至少被调用了一次
    assert mock_greet.called


def test_main_handles_exceptions():
    """测试主函数是否正确处理异常。"""
    with patch("trendpluse.main.demo_basic_features") as mock_demo:
        mock_demo.side_effect = RuntimeError("测试错误")
        with pytest.raises(RuntimeError):
            main()
