# colab-rich

一個專為 Google Colab 和 Python 初學者設計的簡單 Rich 工具。

你可以用幾個簡單的函式，顯示漂亮的標題、訊息、表格和進度列，也可以在 Google Colab 建立簡單按鈕和輸入元件，而不需要先學習 Rich 或 ipywidgets 的複雜用法。

## 安裝

在 Google Colab 的 cell 中執行：

```python
!pip install git+https://github.com/tamhofung/cpu_colab_rich_python.git
```

在自己的 Python 專案中使用 `pip` 安裝：

```bash
python -m pip install git+https://github.com/tamhofung/cpu_colab_rich_python.git
```

### 使用 uv

如果電腦已經安裝 [uv](https://docs.astral.sh/uv/)，可以直接從 GitHub 加入專案：

```bash
uv add "colab-rich @ git+https://github.com/tamhofung/cpu_colab_rich_python.git"
```

然後使用 `uv run` 執行 Python：

```bash
uv run python your_program.py
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

執行後的預期輸出：

```text
──────────────────────────────── 我的第一個報告 ────────────────────────────────
┏━━━━━━┳━━━━━━┓
┃ 姓名 ┃ 分數 ┃
┡━━━━━━╇━━━━━━┩
│ 小明 │ 90   │
│ 小華 │ 85   │
└──────┴──────┘
✓ 完成！
```

GitHub 會顯示上面的純文字預覽；在 Google Colab、Jupyter 或支援顏色的 terminal 執行時，標題、表頭和成功訊息還會顯示 Rich 色彩。

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

## 自訂外觀

所有函式都有簡單的預設值，也可以只調整需要的部分：

```python
from colab_rich import bullet_list, code, panel, show_progress, table, title

title("靠左的標題", style="bold green", align="left")
panel("不會佔滿整行", "提示", border_style="yellow", expand=False)
code("const answer = 42;", "javascript", line_numbers=False)
bullet_list(["早餐", "午餐", "晚餐"], bullet="→")
table(["項目", "狀態"], [["測試", "完成"]], title="工作清單", show_lines=True)
show_progress(7, 10, "下載中", width=30, show_count=True)
```

## API 參考

這份 API 參考直接放在 README，因此可以在 GitHub 專案首頁閱讀。標有 `*` 後面的參數必須使用名稱傳入，例如 `code(source, theme="github-dark")`。

### 輸出

#### `print_text(message, style=None)`

顯示一般文字，不會把內容當作 Rich markup。`style` 可使用 Rich 樣式，例如 `"bold red"`。

#### `title(message, style="bold blue", align="center")`

顯示分隔線標題。`align` 可設為 `"left"`、`"center"` 或 `"right"`。

#### `success(message, prefix="✓")`

#### `info(message, prefix="ℹ")`

#### `warning(message, prefix="!")`

#### `error(message, prefix="✗")`

顯示不同顏色的狀態訊息。使用 `prefix` 可以更換訊息前面的符號：

```python
success("所有測試通過", prefix="OK")
warning("磁碟空間不多", prefix="注意")
```

### 表格和進度

#### `table(headers, rows, title=None, *, header_style="bold magenta", show_lines=False, expand=False)`

顯示表格。`headers` 是欄位名稱；`rows` 是資料列，每列的項目數必須與欄位數相同。

- `title`：表格上方的標題。
- `header_style`：表頭的 Rich 樣式。
- `show_lines`：是否在資料列之間畫線。
- `expand`：是否讓表格使用整行寬度。

#### `show_progress(current, total, label="進度", *, width=20, complete="█", remaining="░", show_count=False)`

顯示單次進度狀態。`width` 控制進度列長度；`complete` 和 `remaining` 必須各是一個字元；`show_count=True` 會同時顯示例如 `7/10` 的數量。

### 格式化內容

#### `markdown(message, code_theme="monokai")`

顯示 Markdown，`code_theme` 控制 Markdown 程式碼區塊的色彩主題。

#### `panel(message, title="", border_style="cyan", *, expand=True)`

在框線中顯示內容。可以設定標題、框線樣式，以及是否使用整行寬度。

#### `code(source, language="python", *, theme="monokai", line_numbers=True, word_wrap=False)`

顯示有語法顏色的程式碼。支援 Pygments 認識的語言與主題。

#### `bullet_list(items, bullet="•", bullet_style="bold green")`

逐行顯示項目清單，可自訂符號和符號樣式。

#### `columns(items, *, equal=True, expand=False)`

並排顯示簡短項目。`equal` 控制欄寬是否相同，`expand` 控制是否使用整行寬度。

#### `show_json(data, *, indent=2, sort_keys=False)`

顯示 JSON 資料。`indent` 控制縮排空格，`sort_keys=True` 會按 key 排序。不能轉換成 JSON 的資料會產生 `TypeError`。

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

- `button(label, action=None, *, style="primary", tooltip=None, disabled=False)`：建立按鈕；`action` 是按下後執行的零參數函式。
- `text_box(label, value="", *, placeholder="", disabled=False)`：建立文字輸入框。
- `select_box(label, options, *, value=None, disabled=False)`：建立下拉選單；`value` 可指定預設選項。
- `check_box(label, value=False, *, disabled=False)`：建立核取方塊。

文字框、下拉選單和核取方塊可使用 `.value` 讀取或更新目前值。`disabled=True` 可以暫停使用元件。

README 已包含完整 API。需要獨立文件時，也可以閱讀 [Markdown API 文件](docs/API.md) 或 [HTML API 文件](docs/API.html)。

## 第一版的範圍

這個專案第一版只簡化 Rich 的常用輸出功能。Textual 是另一個建立互動式 terminal app 的工具，目前不在本專案的第一版範圍內。

## 開發者安裝

使用 `uv`：

```bash
git clone https://github.com/tamhofung/cpu_colab_rich_python.git
cd cpu_colab_rich_python
uv sync
uv run python main.py
uv run python -m unittest discover -s tests -v
```

或使用 `pip`：

```bash
pip install -e .
python -m unittest discover -s tests -v
python main.py
```

## License

目前專案仍在早期開發階段。
