"""簡單、適合 Google Colab 的互動元件。"""

from collections.abc import Iterable


def _get_widgets():
    """載入 ipywidgets，並提供適合初學者的錯誤訊息。"""
    try:
        import ipywidgets as widgets
    except ImportError as exc:
        raise ImportError(
            "互動元件需要 ipywidgets。請重新安裝 colab-rich，"
            "或執行：pip install ipywidgets"
        ) from exc
    return widgets


def button(label: object, action=None):
    """建立按鈕。

    ``action`` 是按下按鈕後執行的零參數函式，例如：

    >>> def say_hello():
    ...     print("你好！")
    >>> display(button("按我", say_hello))
    """
    widgets = _get_widgets()
    if action is not None and not callable(action):
        raise TypeError("action 必須是一個函式，或使用 None。")

    button_widget = widgets.Button(
        description=str(label),
        button_style="primary",
        tooltip=f"按下 {label}",
    )

    if action is None:
        return button_widget

    output = widgets.Output()

    def on_click(_button) -> None:
        from IPython.display import clear_output

        with output:
            clear_output(wait=True)
            action()

    button_widget.on_click(on_click)
    return widgets.VBox([button_widget, output])


def text_box(label: object, value: object = ""):
    """建立單行文字輸入框。"""
    widgets = _get_widgets()
    return widgets.Text(description=str(label), value=str(value))


def select_box(label: object, options: Iterable[object]):
    """建立下拉選單。"""
    widgets = _get_widgets()
    if isinstance(options, str):
        options = [options]

    option_list = list(options)
    if not option_list:
        raise ValueError("下拉選單至少需要一個選項。")

    return widgets.Dropdown(description=str(label), options=option_list)


def check_box(label: object, value: bool = False):
    """建立核取方塊。"""
    widgets = _get_widgets()
    return widgets.Checkbox(description=str(label), value=bool(value))
