import importlib
import io
import unittest
from unittest.mock import patch

from rich.console import Console

from colab_rich import (
    bullet_list,
    button,
    check_box,
    code,
    columns,
    error,
    info,
    markdown,
    panel,
    print_text,
    select_box,
    show_json,
    show_progress,
    success,
    table,
    text_box,
    title,
    warning,
)
import colab_rich.display as display_module
import colab_rich.output as output_module
import colab_rich.progress as progress_module

table_module = importlib.import_module("colab_rich.table")


class WidgetTests(unittest.TestCase):
    def test_button_without_action_is_a_button(self):
        from ipywidgets import Button

        widget = button("按我")
        self.assertIsInstance(widget, Button)
        self.assertEqual(widget.description, "按我")

    def test_button_runs_a_simple_action(self):
        from ipywidgets import VBox

        called = []

        def action():
            called.append(True)

        widget = button("執行", action)
        self.assertIsInstance(widget, VBox)
        button_widget = widget.children[0]
        button_widget._click_handlers.callbacks[0](button_widget)
        self.assertEqual(called, [True])

    def test_text_box_has_label_and_value(self):
        widget = text_box("姓名", "小明", placeholder="請輸入姓名", disabled=True)
        self.assertEqual(widget.description, "姓名")
        self.assertEqual(widget.value, "小明")
        self.assertEqual(widget.placeholder, "請輸入姓名")
        self.assertTrue(widget.disabled)

    def test_select_box_has_options(self):
        widget = select_box("顏色", ["紅色", "藍色"], value="藍色")
        self.assertEqual(widget.description, "顏色")
        self.assertEqual(tuple(widget.options), ("紅色", "藍色"))
        self.assertEqual(widget.value, "藍色")

    def test_select_box_rejects_empty_options(self):
        with self.assertRaisesRegex(ValueError, "至少需要一個選項"):
            select_box("顏色", [])

    def test_select_box_rejects_unknown_value(self):
        with self.assertRaisesRegex(ValueError, "options 內"):
            select_box("顏色", ["紅色", "藍色"], value="綠色")

    def test_check_box_has_boolean_value(self):
        widget = check_box("已完成", True)
        self.assertEqual(widget.description, "已完成")
        self.assertTrue(widget.value)


class OutputTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.output_patch = patch.object(output_module, "_console", self.test_console)
        self.output_patch.start()

    def tearDown(self):
        self.output_patch.stop()

    def test_print_text_does_not_interpret_markup(self):
        print_text("[不是 Rich 標記]", style="bold")
        self.assertIn("[不是 Rich 標記]", self.stream.getvalue())

    def test_message_functions_show_the_message(self):
        info("提示")
        success("完成")
        warning("注意")
        error("錯誤")
        output = self.stream.getvalue()
        for message in ("提示", "完成", "注意", "錯誤"):
            self.assertIn(message, output)

    def test_title_shows_the_title(self):
        title("測試標題", style="green", align="left")
        self.assertIn("測試標題", self.stream.getvalue())

    def test_title_rejects_unknown_alignment(self):
        with self.assertRaisesRegex(ValueError, "align 必須"):
            title("測試標題", align="top")


class DisplayTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.console_patch = patch.object(display_module, "_console", self.test_console)
        self.console_patch.start()

    def tearDown(self):
        self.console_patch.stop()

    def test_markdown_shows_text(self):
        markdown("# 標題")
        self.assertIn("標題", self.stream.getvalue())

    def test_panel_shows_title_and_message(self):
        panel("重要內容", "注意", border_style="red", expand=False)
        output = self.stream.getvalue()
        self.assertIn("注意", output)
        self.assertIn("重要內容", output)

    def test_code_shows_source(self):
        code("print('你好')", line_numbers=False, word_wrap=True)
        self.assertIn("print", self.stream.getvalue())

    def test_bullet_list_shows_all_items(self):
        bullet_list(["第一項", "第二項"], bullet="-")
        output = self.stream.getvalue()
        self.assertIn("第一項", output)
        self.assertIn("第二項", output)

    def test_columns_shows_all_items(self):
        columns(["A", "B", "C"])
        output = self.stream.getvalue()
        for item in ("A", "B", "C"):
            self.assertIn(item, output)

    def test_show_json_shows_data(self):
        show_json({"姓名": "小明", "分數": 90}, indent=4, sort_keys=True)
        output = self.stream.getvalue()
        self.assertIn("小明", output)
        self.assertIn("90", output)

    def test_show_json_rejects_negative_indent(self):
        with self.assertRaisesRegex(ValueError, "indent 不可以"):
            show_json({}, indent=-1)


class TableTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.console_patch = patch.object(table_module, "_console", self.test_console)
        self.console_patch.start()

    def tearDown(self):
        self.console_patch.stop()

    def test_table_shows_headers_and_rows(self):
        table(
            ["姓名", "分數"],
            [["小明", 90], ["小華", 85]],
            "成績表",
            show_lines=True,
        )
        output = self.stream.getvalue()
        for value in ("成績表", "姓名", "分數", "小明", "90", "小華", "85"):
            self.assertIn(value, output)

    def test_table_rejects_empty_headers(self):
        with self.assertRaisesRegex(ValueError, "至少需要一個欄位"):
            table([], [])

    def test_table_rejects_wrong_number_of_values(self):
        with self.assertRaisesRegex(ValueError, "第 1 列"):
            table(["姓名", "分數"], [["小明"]])


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.console_patch = patch.object(progress_module, "_console", self.test_console)
        self.console_patch.start()

    def tearDown(self):
        self.console_patch.stop()

    def test_progress_shows_percentage(self):
        show_progress(5, 10, width=10, complete="#", remaining="-", show_count=True)
        output = self.stream.getvalue()
        self.assertIn("50.0%", output)
        self.assertIn("5/10", output)

    def test_progress_rejects_invalid_total(self):
        with self.assertRaisesRegex(ValueError, "total 必須大於 0"):
            show_progress(1, 0)

    def test_progress_rejects_invalid_current(self):
        with self.assertRaisesRegex(ValueError, "current 必須介乎"):
            show_progress(11, 10)

    def test_progress_rejects_invalid_width_and_characters(self):
        with self.assertRaisesRegex(ValueError, "width 必須大於 0"):
            show_progress(1, 10, width=0)
        with self.assertRaisesRegex(ValueError, "一個字元"):
            show_progress(1, 10, complete="##")


if __name__ == "__main__":
    unittest.main()
