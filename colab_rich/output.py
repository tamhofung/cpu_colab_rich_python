"""文字、標題和訊息輸出功能。"""

from rich.text import Text

from .console import console as _console


def print_text(message: object, style: str | None = None) -> None:
    """顯示一般文字，可選擇 Rich 顏色或樣式。"""
    _console.print(Text(str(message), style=style))


def title(message: object, style: str = "bold blue", align: str = "center") -> None:
    """顯示一個清楚的標題。

    ``align`` 可以是 ``"left"``、``"center"`` 或 ``"right"``。
    """
    if align not in {"left", "center", "right"}:
        raise ValueError("align 必須是 left、center 或 right。")
    _console.rule(str(message), style=style, align=align)


def _message(prefix: str, message: object, color: str) -> None:
    """以指定顏色顯示訊息；文字內容不會被當成 Rich 標記處理。"""
    line = Text()
    line.append(f"{prefix} ", style=f"bold {color}")
    line.append(str(message))
    _console.print(line)


def success(message: object, prefix: str = "✓") -> None:
    """顯示成功訊息。"""
    _message(prefix, message, "green")


def info(message: object, prefix: str = "ℹ") -> None:
    """顯示一般提示。"""
    _message(prefix, message, "cyan")


def warning(message: object, prefix: str = "!") -> None:
    """顯示警告訊息。"""
    _message(prefix, message, "yellow")


def error(message: object, prefix: str = "✗") -> None:
    """顯示錯誤訊息。"""
    _message(prefix, message, "red")
