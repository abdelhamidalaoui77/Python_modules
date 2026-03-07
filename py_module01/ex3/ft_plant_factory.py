class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []

    print("=== Plant Factory Output ===")

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"Total plants created: {len(plants)}")
