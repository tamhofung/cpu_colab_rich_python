"""Markdown、面板、程式碼和其他簡單顯示功能。"""

import json
from collections.abc import Iterable

from rich.columns import Columns
from rich.json import JSON
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from .console import console as _console


def markdown(message: object) -> None:
    """以 Markdown 格式顯示文字。"""
    _console.print(Markdown(str(message)))


def panel(message: object, title: str = "") -> None:
    """在有框線的面板中顯示重點內容。"""
    _console.print(Panel(Text(str(message)), title=title, border_style="cyan"))


def code(source: object, language: str = "python") -> None:
    """以語法顏色顯示程式碼。"""
    _console.print(Syntax(str(source), language, theme="monokai", line_numbers=True))


def bullet_list(items: Iterable[object]) -> None:
    """將每個項目顯示成一行簡單清單。"""
    for item in items:
        line = Text()
        line.append("• ", style="bold green")
        line.append(str(item))
        _console.print(line)


def columns(items: Iterable[object]) -> None:
    """將簡短項目並排顯示。"""
    renderable_items = [Text(str(item)) for item in items]
    _console.print(Columns(renderable_items, equal=True, expand=False))


def show_json(data: object) -> None:
    """以容易閱讀的方式顯示 dictionary、list 等 JSON 資料。"""
    try:
        text = json.dumps(data, ensure_ascii=False, indent=2)
    except TypeError as exc:
        raise TypeError("data 必須是可以轉換成 JSON 的資料。") from exc

    _console.print(JSON(text))
