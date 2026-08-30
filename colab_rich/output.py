"""文字、標題和訊息輸出功能。"""

from rich.text import Text

from .console import console as _console


def print_text(message: object) -> None:
    """顯示一般文字。"""
    _console.print(str(message), markup=False)


def title(message: object) -> None:
    """顯示一個清楚的標題。"""
    _console.rule(str(message), style="bold blue")


def _message(prefix: str, message: object, color: str) -> None:
    """以指定顏色顯示訊息；文字內容不會被當成 Rich 標記處理。"""
    line = Text()
    line.append(f"{prefix} ", style=f"bold {color}")
    line.append(str(message))
    _console.print(line)


def success(message: object) -> None:
    """顯示成功訊息。"""
    _message("✓", message, "green")


def info(message: object) -> None:
    """顯示一般提示。"""
    _message("ℹ", message, "cyan")


def warning(message: object) -> None:
    """顯示警告訊息。"""
    _message("!", message, "yellow")


def error(message: object) -> None:
    """顯示錯誤訊息。"""
    _message("✗", message, "red")
