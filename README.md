# colab-rich

一個專為 Google Colab 和 Python 初學者設計的簡單 Rich 工具。

你可以用幾個簡單的函式，顯示漂亮的標題、訊息、表格和進度列，也可以在 Google Colab 建立簡單按鈕和輸入元件，而不需要先學習 Rich 或 ipywidgets 的複雜用法。

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

## 顯示更多內容

### Markdown

```python
from colab_rich import markdown

markdown("""
# 今日報告

這是 **重要文字**。

- 第一點
- 第二點
""")
```

### 面板

```python
from colab_rich import panel

panel("請記得檢查答案。", "小提示")
```

### 程式碼

```python
from colab_rich import code

code("print('你好！')")
```

### 項目清單和並排項目

```python
from colab_rich import bullet_list, columns

bullet_list(["第一項", "第二項", "第三項"])
columns(["紅色", "綠色", "藍色"])
```

### JSON 資料

```python
from colab_rich import show_json

show_json({"姓名": "小明", "分數": 90})
```

完整的函式、參數和例子請參考 [繁體中文 HTML API 文件](docs/API.html)。

如果你想在 GitHub 直接閱讀純文字版本，也可以查看 [Markdown API 文件](docs/API.md)。

要在本機預覽 HTML 文件，可以在專案根目錄執行：

```bash
python -m http.server 8000
```

然後在瀏覽器開啟 <http://localhost:8000/docs/API.html>。

## Google Colab 互動元件

`colab-rich` 也包含幾個簡單的 Google Colab widget。需要按鈕執行的工作，可以寫成普通的零參數函式：

```python
from IPython.display import display
from colab_rich import button, success

def say_hello():
    success("你好！你按下了按鈕。")

display(button("按我", say_hello))
```

文字輸入框、下拉選單和核取方塊的值，可以使用 `.value` 讀取：

```python
from IPython.display import display
from colab_rich import button, select_box, success, text_box

name = text_box("你的名字")
color = select_box("喜歡的顏色", ["紅色", "綠色", "藍色"])

def show_answer():
    success(f"{name.value} 喜歡 {color.value}。")

display(name)
display(color)
display(button("顯示答案", show_answer))
```

可用的基本元件：

- `button(label, action=None)`：建立按鈕；`action` 是按下後執行的函式。
- `text_box(label, value="")`：建立文字輸入框。
- `select_box(label, options)`：建立下拉選單。
- `check_box(label, value=False)`：建立核取方塊。

完整的函式、參數和例子請參考 [繁體中文 HTML API 文件](docs/API.html)。

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
