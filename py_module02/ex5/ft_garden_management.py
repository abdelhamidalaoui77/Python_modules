class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[plant_name] = {"water": 5, "sun": 8}
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> None:
        if plant_name not in self.plants:
            raise PlantError(f"{plant_name} not found in garden")

        water = self.plants[plant_name]["water"]
        sun = self.plants[plant_name]["sun"]

        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print()
    print("Watering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Watering error: {e}")

    print()
    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato")

        manager.plants["lettuce"]["water"] = 15
        manager.check_plant_health("lettuce")

    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
