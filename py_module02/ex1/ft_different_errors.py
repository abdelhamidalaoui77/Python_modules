
def garden_operations() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        print()
    print("Testing ZeroDivisionError...")
    try:
        15 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        print()
    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
        print()
    print("Testing KeyError...")
    try:
        plants = {"tomato": 1}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
