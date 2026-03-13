
def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp


def test_temperature_input() -> None:
    test_cases = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
    print()

    for test in test_cases:
        print(f"Testing temperature: {test}")
        try:
            check_temperature(test)
        except ValueError as e:
            print(f"Error: {e}")
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
