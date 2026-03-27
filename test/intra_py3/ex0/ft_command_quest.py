import sys


def check_argv(argv: list) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if len(argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(argv) - 1}")
    i = 1
    for arg in argv[1:]:
        print(f"Argument {i}: {arg}")
        i = i + 1
    print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    check_argv(sys.argv)
