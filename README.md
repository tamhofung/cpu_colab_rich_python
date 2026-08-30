# colab-rich

一個專為 Google Colab 和 Python 初學者設計的簡單 Rich 工具。

你可以用幾個簡單的函式，顯示漂亮的標題、訊息、表格和進度列，而不需要先學習 Rich 的複雜用法。

## 安裝

在 Google Colab 的 cell 中執行：

```python
!pip install colab-rich
```

在自己的 Python 專案中執行：

```bash
pip install colab-rich
```

## 快速開始

```python
from colab_rich import title, success, table

title("我的第一個報告")

table(
    ["姓名", "分數"],
    [
        ["小明", 90],
        ["小華", 85],
    ],
)

success("完成！")
```

## 顯示文字和訊息

```python
from colab_rich import error, info, print_text, success, warning

print_text("這是普通文字")
info("這是提示")
success("這是成功訊息")
warning("這是警告")
error("這是錯誤訊息")
```

每個函式只需要一個訊息：

```python
success("答案正確！")
```

## 顯示表格

第一個參數是欄位名稱，第二個參數是資料。每一列資料都應該有相同數量的項目。

```python
from colab_rich import table

table(
    ["水果", "數量"],
    [
        ["蘋果", 3],
        ["香蕉", 5],
    ],
)
```

## 顯示進度

`show_progress()` 適合放在簡單的 `for` loop 裡：

```python
from colab_rich import show_progress

for number in range(1, 6):
    show_progress(number, 5)
```

也可以自訂文字：

```python
show_progress(3, 10, "下載中")
```

`current` 不可以小於 0，`total` 必須大於 0，而且 `current` 不可以大於 `total`。

## 第一版的範圍

這個專案第一版只簡化 Rich 的常用輸出功能。Textual 是另一個建立互動式 terminal app 的工具，目前不在本專案的第一版範圍內。

## 開發者安裝

```bash
pip install -e .
python -m unittest discover -s tests -v
python main.py
```

## License

目前專案仍在早期開發階段。
