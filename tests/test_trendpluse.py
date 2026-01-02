"""测试包本身的基本属性。"""

from trendpluse import __version__, add, greet


def test_version():
    """测试版本号是否已定义。"""
    assert __version__ == "0.1.0"


def test_exports():
    """测试预期的函数是否已导出。"""
    assert callable(greet)
    assert callable(add)
