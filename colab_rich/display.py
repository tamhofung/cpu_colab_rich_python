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


def markdown(message: object, code_theme: str = "monokai") -> None:
    """以 Markdown 格式顯示文字。"""
    _console.print(Markdown(str(message), code_theme=code_theme))


def panel(
    message: object,
    title: str = "",
    border_style: str = "cyan",
    *,
    expand: bool = True,
) -> None:
    """在有框線的面板中顯示重點內容。"""
    _console.print(
        Panel(
            Text(str(message)),
            title=title or None,
            border_style=border_style,
            expand=expand,
        )
    )


def code(
    source: object,
    language: str = "python",
    *,
    theme: str = "monokai",
    line_numbers: bool = True,
    word_wrap: bool = False,
) -> None:
    """以語法顏色顯示程式碼。"""
    _console.print(
        Syntax(
            str(source),
            language,
            theme=theme,
            line_numbers=line_numbers,
            word_wrap=word_wrap,
        )
    )


def bullet_list(
    items: Iterable[object], bullet: str = "•", bullet_style: str = "bold green"
) -> None:
    """將每個項目顯示成一行簡單清單。"""
    for item in items:
        line = Text()
        line.append(f"{bullet} ", style=bullet_style)
        line.append(str(item))
        _console.print(line)


def columns(
    items: Iterable[object], *, equal: bool = True, expand: bool = False
) -> None:
    """將簡短項目並排顯示。"""
    renderable_items = [Text(str(item)) for item in items]
    _console.print(Columns(renderable_items, equal=equal, expand=expand))


def show_json(data: object, *, indent: int = 2, sort_keys: bool = False) -> None:
    """以容易閱讀的方式顯示 dictionary、list 等 JSON 資料。"""
    try:
        if indent < 0:
            raise ValueError("indent 不可以小於 0。")
        text = json.dumps(
            data, ensure_ascii=False, indent=indent, sort_keys=sort_keys
        )
    except TypeError as exc:
        raise TypeError("data 必須是可以轉換成 JSON 的資料。") from exc

    _console.print(JSON(text))
