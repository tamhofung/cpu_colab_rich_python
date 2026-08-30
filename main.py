from colab_rich import success, table, title


def main() -> None:
    title("colab-rich 示範")
    table(
        ["姓名", "分數"],
        [
            ["小明", 90],
            ["小華", 85],
        ],
    )
    success("示範完成！")


if __name__ == "__main__":
    main()
