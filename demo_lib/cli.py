def main() -> None:
    print("demo-cli 命令行工具启动成功！")
    from demo_lib import add, hello

    print(hello())
    print(f"10 + 20 = {add(10, 20)}")


if __name__ == "__main__":
    main()
