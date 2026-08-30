"""簡單表格功能。"""

from collections.abc import Iterable, Sequence

from rich.table import Table

from .console import console as _console


def table(headers: Sequence[object], rows: Iterable[Sequence[object]]) -> None:
    """顯示表格。

    Args:
        headers: 欄位名稱，例如 ``["姓名", "分數"]``。
        rows: 每一列的資料，例如 ``[["小明", 90], ["小華", 85]]``。
    """
    header_list = [str(header) for header in headers]
    if not header_list:
        raise ValueError("表格至少需要一個欄位名稱。")

    row_list = [list(row) for row in rows]
    for row_number, row in enumerate(row_list, start=1):
        if len(row) != len(header_list):
            raise ValueError(
                f"第 {row_number} 列有 {len(row)} 個資料，"
                f"但需要 {len(header_list)} 個。"
            )

    rich_table = Table(show_header=True, header_style="bold magenta")
    for header in header_list:
        rich_table.add_column(header)

    for row in row_list:
        rich_table.add_row(*(str(value) for value in row))

    _console.print(rich_table)
