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

## `print_text(message)`

顯示普通文字。

```python
from colab_rich import print_text

print_text("你好，Colab！")
```

- `message` 可以是文字、數字或其他 Python 資料。
- 內容會按照原本的文字顯示。

---

## `title(message)`

顯示一個有分隔線的標題。

```python
from colab_rich import title

title("第一部分：資料輸入")
```

- `message` 是標題內容。
- 適合用來分開程式不同部分的輸出。

---

## `success(message)`、`info(message)`、`warning(message)` 和 `error(message)`

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

---

## `table(headers, rows)`

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

## `show_progress(current, total, label='進度')`

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

`current` 必須介乎 `0` 和 `total` 之間。

---

## `markdown(message)`

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

## `panel(message, title='')`

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

---

## `code(source, language='python')`

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

---

## `bullet_list(items)`

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

## `columns(items)`

將簡短項目並排顯示。

```python
from colab_rich import columns

columns(["紅色", "綠色", "藍色"])
```

這個功能適合顯示短文字。太長的句子可能不適合並排顯示。

---

## `show_json(data)`

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
