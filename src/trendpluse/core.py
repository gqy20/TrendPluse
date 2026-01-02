"""trendpluse 核心功能模块"""


def greet(name: str = "World") -> str:
    """
    生成问候消息

    参数:
        name: 要问候的名字，默认为 "World"

    返回:
        问候字符串

    示例:
        >>> greet()
        'Hello, World!'
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    两个整数相加

    参数:
        a: 第一个整数
        b: 第二个整数

    返回:
        a 和 b 的和

    示例:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b
