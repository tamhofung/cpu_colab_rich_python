# colab-rich API 文件

`colab-rich` 是一個把 Rich 常用功能變成簡單函式的工具，適合在 Google Colab 使用，也適合剛學 Python 的同學。

## 匯入函式

可以一次匯入需要的函式：

```python
from colab_rich import title, success, table
```

也可以匯入全部第一版功能：

```python
from colab_rich import (
    bullet_list,
    code,
    columns,
    error,
    info,
    markdown,
    panel,
    print_text,
    show_json,
    show_progress,
    success,
    table,
    title,
    warning,
)
```

---

## `print_text(message, style=None)`

顯示普通文字。

```python
from colab_rich import print_text

print_text("你好，Colab！")
```

- `message` 可以是文字、數字或其他 Python 資料。
- 內容會按照原本的文字顯示。
- `style` 可設定 Rich 顏色或樣式，例如 `"bold red"`。

---

## `title(message, style='bold blue', align='center')`

顯示一個有分隔線的標題。

```python
from colab_rich import title

title("第一部分：資料輸入")
```

- `message` 是標題內容。
- 適合用來分開程式不同部分的輸出。
- `style` 控制標題樣式；`align` 可以是 `left`、`center` 或 `right`。

---

## `success(message, prefix='✓')`、`info()`、`warning()` 和 `error()`

顯示不同種類的訊息。

```python
from colab_rich import error, info, success, warning

info("程式正在開始")
success("資料已經儲存")
warning("還有一項資料未輸入")
error("找不到檔案")
```

每個函式都只需要一個參數：

```python
success("答案正確！")
```

四個函式都可用 `prefix` 更換前方符號。

---

## `table(headers, rows, title=None, *, header_style='bold magenta', show_lines=False, expand=False)`

顯示整齊的表格。

```python
from colab_rich import table

table(
    ["姓名", "年齡", "分數"],
    [
        ["小明", 14, 90],
        ["小華", 15, 85],
    ],
)
```

參數：

- `headers`：欄位名稱，例如 `['姓名', '分數']`。
- `rows`：資料列。每一列的資料數量必須和欄位數量相同。
- `title`：可選的表格標題。
- `header_style`、`show_lines`、`expand`：控制表頭樣式、列分隔線和表格寬度。

正確例子：

```python
table(
    ["水果", "數量"],
    [["蘋果", 3], ["香蕉", 5]],
)
```

每列資料數量不同會產生錯誤：

```python
# 不正確：第二列只有一項資料
# table(["姓名", "分數"], [["小明", 90], ["小華"]])
```

---

## `show_progress(current, total, label='進度', *, width=20, complete='█', remaining='░', show_count=False)`

顯示簡單的進度列，適合放在 `for` loop 中。

```python
from colab_rich import show_progress

for number in range(1, 6):
    show_progress(number, 5)
```

可以自訂進度文字：

```python
show_progress(3, 10, "下載中")
```

參數：

- `current`：目前完成的數量。
- `total`：總數量，必須大於 0。
- `label`：進度列前面的文字，可以省略。
- `width`：進度列的字元寬度。
- `complete`、`remaining`：已完成及未完成部分使用的單一字元。
- `show_count`：是否顯示目前數量和總數。

`current` 必須介乎 `0` 和 `total` 之間。

---

## `markdown(message, code_theme='monokai')`

將 Markdown 文字顯示成格式化內容。

```python
from colab_rich import markdown

markdown("""
# 今日報告

這是 **重要文字**。

- 第一點
- 第二點
""")
```

適合顯示報告標題、重點和簡單清單。

---

## `panel(message, title='', border_style='cyan', *, expand=True)`

在框線中顯示一段重點內容。

```python
from colab_rich import panel

panel("請記得在交功課前檢查答案。", "小提示")
```

如果不需要小標題：

```python
panel("這是一段重要內容。")
```

參數：

- `message`：面板內的內容。
- `title`：面板上方的小標題，可以省略。
- `border_style`：框線的 Rich 樣式。
- `expand`：面板是否使用整行寬度。

---

## `code(source, language='python', *, theme='monokai', line_numbers=True, word_wrap=False)`

以語法顏色顯示程式碼。

```python
from colab_rich import code

code("""name = '小明'
print(name)
""")
```

顯示其他語言時，可以指定語言名稱：

```python
code("print('Hello')", "python")
code("console.log('Hello');", "javascript")
```

常見的語言名稱包括 `python`、`javascript`、`html` 和 `css`。
也可以設定色彩 `theme`、行號和自動換行。

---

## `bullet_list(items, bullet='•', bullet_style='bold green')`

將 list 中的每一項顯示成項目清單。

```python
from colab_rich import bullet_list

bullet_list([
    "開啟 Google Colab",
    "輸入程式碼",
    "執行程式",
])
```

`items` 可以是 list，也可以是其他可以逐項閱讀的資料。

---

## `columns(items, *, equal=True, expand=False)`

將簡短項目並排顯示。

```python
from colab_rich import columns

columns(["紅色", "綠色", "藍色"])
```

這個功能適合顯示短文字。太長的句子可能不適合並排顯示。

---

## `show_json(data, *, indent=2, sort_keys=False)`

將 dictionary 或 list 以容易閱讀的 JSON 樣式顯示。

```python
from colab_rich import show_json

student = {
    "name": "小明",
    "score": 90,
    "passed": True,
}

show_json(student)
```

也可以顯示 list：

```python
show_json(["Python", "Math", "English"])
```

資料必須是可以轉成 JSON 的基本 Python 資料，例如：

- dictionary
- list
- string
- number
- `True`、`False`
- `None`

---

## Google Colab 互動元件

以下元件直接使用 Google Colab 支援的 `ipywidgets`。先匯入 Colab 的 `display` 函式：

```python
from IPython.display import display
```

### `button(label, action=None, *, style='primary', tooltip=None, disabled=False)`

建立一個按鈕。`action` 是按下按鈕後執行的零參數函式。

```python
from colab_rich import button, success

def say_hello():
    success("你好！你按下了按鈕。")

display(button("按我", say_hello))
```

預期畫面：

```text
[ 按我 ]
```

按下按鈕後，結果會顯示在按鈕下面：

```text
✓ 你好！你按下了按鈕。
```

如果暫時不需要動作，可以省略 `action`：

```python
display(button("這是一個按鈕"))
```

### `text_box(label, value='', *, placeholder='', disabled=False)`

建立單行文字輸入框。使用 `.value` 讀取學生輸入的文字。

```python
from IPython.display import display
from colab_rich import text_box

name = text_box("你的名字")
display(name)

# 讀取輸入的文字
print(name.value)
```

預期畫面：

```text
你的名字: [                    ]
```

### `select_box(label, options, *, value=None, disabled=False)`

建立下拉選單。`options` 是選項 list，使用 `.value` 讀取目前選擇。

```python
from IPython.display import display
from colab_rich import select_box

color = select_box("選擇顏色", ["紅色", "綠色", "藍色"])
display(color)

print(color.value)
```

預期畫面：

```text
選擇顏色: [紅色        ▼]
```

### `check_box(label, value=False, *, disabled=False)`

建立核取方塊。勾選狀態可以從 `.value` 讀取，結果是 `True` 或 `False`。

```python
from IPython.display import display
from colab_rich import check_box

finished = check_box("我已完成練習")
display(finished)

print(finished.value)
```

預期畫面：

```text
☐ 我已完成練習
```

### 互動元件完整例子

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

`button()` 會處理按鈕需要的 event 細節，所以 `show_answer()` 不需要接收任何參數。

---

## 完整小例子

```python
from colab_rich import (
    bullet_list,
    code,
    markdown,
    show_json,
    success,
    table,
    title,
)

title("Python 小報告")

markdown("這是一個 **學生資料** 報告。")

table(
    ["姓名", "分數"],
    [["小明", 90], ["小華", 85]],
)

bullet_list(["兩位同學已完成測驗", "平均分數是 87.5"])

code("print('報告完成！')")
show_json({"average": 87.5, "passed": True})
success("報告完成！")
```

## 初學者提示

1. 先學習 `title()`、`success()` 和 `table()`。
2. 熟悉後再嘗試 `markdown()`、`panel()` 和 `code()`。
3. 每個函式都可以單獨使用，不需要建立 class。
4. Textual 暫時不是這個 library 的一部分；本 library 現階段專注於在 Colab 顯示內容。
