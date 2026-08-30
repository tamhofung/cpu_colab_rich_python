import importlib
import io
import unittest
from unittest.mock import patch

from rich.console import Console

from colab_rich import error, info, print_text, show_progress, success, table, title, warning
import colab_rich.output as output_module
import colab_rich.progress as progress_module

table_module = importlib.import_module("colab_rich.table")


class OutputTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.output_patch = patch.object(output_module, "_console", self.test_console)
        self.output_patch.start()

    def tearDown(self):
        self.output_patch.stop()

    def test_print_text_does_not_interpret_markup(self):
        print_text("[不是 Rich 標記]")
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
        title("測試標題")
        self.assertIn("測試標題", self.stream.getvalue())


class TableTests(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()
        self.test_console = Console(file=self.stream, force_terminal=False, color_system=None)
        self.console_patch = patch.object(table_module, "_console", self.test_console)
        self.console_patch.start()

    def tearDown(self):
        self.console_patch.stop()

    def test_table_shows_headers_and_rows(self):
        table(["姓名", "分數"], [["小明", 90], ["小華", 85]])
        output = self.stream.getvalue()
        for value in ("姓名", "分數", "小明", "90", "小華", "85"):
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
        show_progress(5, 10)
        self.assertIn("50.0%", self.stream.getvalue())

    def test_progress_rejects_invalid_total(self):
        with self.assertRaisesRegex(ValueError, "total 必須大於 0"):
            show_progress(1, 0)

    def test_progress_rejects_invalid_current(self):
        with self.assertRaisesRegex(ValueError, "current 必須介乎"):
            show_progress(11, 10)


if __name__ == "__main__":
    unittest.main()
