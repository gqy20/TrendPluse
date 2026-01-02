"""核心模块的测试用例。"""

import pytest

from trendpluse.core import add, greet


class TestGreet:
    """greet 函数的测试用例。"""

    def test_greet_default(self):
        """测试使用默认参数的 greet 函数。"""
        assert greet() == "Hello, World!"

    def test_greet_with_name(self):
        """测试使用自定义名称的 greet 函数。"""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_empty_string(self):
        """测试使用空字符串的 greet 函数。"""
        assert greet("") == "Hello, !"

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Bob", "Hello, Bob!"),
            ("Charlie", "Hello, Charlie!"),
            ("测试", "Hello, 测试!"),
        ],
    )
    def test_greet_parametrized(self, name, expected):
        """使用参数化测试多个名称的 greet 函数。"""
        assert greet(name) == expected


class TestAdd:
    """add 函数的测试用例。"""

    def test_add_positive_numbers(self):
        """测试两个正数相加。"""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """测试两个负数相加。"""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """测试正数和负数相加。"""
        assert add(-1, 1) == 0

    def test_add_zero(self):
        """测试与零相加。"""
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (1, 1, 2),
            (10, 20, 30),
            (-5, 5, 0),
            (100, 200, 300),
        ],
    )
    def test_add_parametrized(self, a, b, expected):
        """使用多种数值组合测试 add 函数。"""
        assert add(a, b) == expected
