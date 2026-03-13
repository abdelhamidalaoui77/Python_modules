
def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    try:
        plants = ["tomato", "lettuce", "carrots"]
        water_plants(plants)
        print("Watering completed successfully!")
        print()
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing with error...")
    try:
        plants = ["tomato", None, "carrots"]
        water_plants(plants)
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
