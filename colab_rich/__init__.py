"""簡單、適合 Google Colab 的 Rich 輸出工具。"""

from .output import error, info, print_text, success, title, warning
from .progress import show_progress
from .table import table

__all__ = [
    "error",
    "info",
    "print_text",
    "show_progress",
    "success",
    "table",
    "title",
    "warning",
]
