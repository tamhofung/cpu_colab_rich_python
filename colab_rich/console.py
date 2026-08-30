"""內部的 Colab、Jupyter 和 terminal 輸出設定。"""

import os
import sys

from rich.console import Console


def is_colab() -> bool:
    """判斷目前是否在 Google Colab 執行。"""
    return (
        "google.colab" in sys.modules
        or bool(os.environ.get("COLAB_RELEASE_TAG"))
        or bool(os.environ.get("COLAB_GPU"))
    )


def make_console() -> Console:
    """建立適合目前環境的 Rich Console。"""
    return Console(force_jupyter=True if is_colab() else None)


console = make_console()
