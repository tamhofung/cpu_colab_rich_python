"""適合初學者的簡單進度列。"""

from .console import console as _console


def show_progress(current: int, total: int, label: str = "進度") -> None:
    """顯示目前進度和百分比。

    這個函式適合放在簡單的 ``for`` loop 中使用：

    >>> for number in range(1, 4):
    ...     show_progress(number, 3)
    """
    if total <= 0:
        raise ValueError("total 必須大於 0。")
    if current < 0 or current > total:
        raise ValueError("current 必須介乎 0 和 total 之間。")

    percentage = current / total * 100
    bar_length = 20
    filled = round(current / total * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    _console.print(f"{label}: [{bar}] {percentage:>5.1f}%")
