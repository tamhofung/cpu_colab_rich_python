"""適合初學者的簡單進度列。"""

from rich.text import Text

from .console import console as _console


def show_progress(
    current: int,
    total: int,
    label: str = "進度",
    *,
    width: int = 20,
    complete: str = "█",
    remaining: str = "░",
    show_count: bool = False,
) -> None:
    """顯示目前進度和百分比。

    這個函式適合放在簡單的 ``for`` loop 中使用：

    >>> for number in range(1, 4):
    ...     show_progress(number, 3)
    """
    if total <= 0:
        raise ValueError("total 必須大於 0。")
    if current < 0 or current > total:
        raise ValueError("current 必須介乎 0 和 total 之間。")
    if width <= 0:
        raise ValueError("width 必須大於 0。")
    if len(complete) != 1 or len(remaining) != 1:
        raise ValueError("complete 和 remaining 必須各是一個字元。")

    percentage = current / total * 100
    filled = round(current / total * width)
    bar = complete * filled + remaining * (width - filled)
    count = f" ({current}/{total})" if show_count else ""
    _console.print(Text(f"{label}: [{bar}] {percentage:>5.1f}%{count}"))
