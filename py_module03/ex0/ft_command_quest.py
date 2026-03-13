import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
        print()
    else:
        args = sys.argv[1:]
        print(f"Arguments received: {len(args)}")
        i = 1
        for argument in args:
            print(f"Argument {i}: {argument}")
            i += 1
        print(f"Total arguments: {len(sys.argv)}")
        print()
