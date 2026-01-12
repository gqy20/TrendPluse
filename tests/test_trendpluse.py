"""测试包本身的基本属性。"""

from trendpluse import __version__


def test_version():
    """测试版本号是否已定义。"""
    assert __version__ == "0.1.0"
