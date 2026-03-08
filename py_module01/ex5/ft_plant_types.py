
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade = 1.56 * self.trunk_diameter
        return f"{self.name} provides {shade:.0f} square meters of shade"


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition_info(self) -> str:
        return f"{self.name} is rich in {self.nutritional_value}"


if __name__ == "__main__":
    f1 = Flower("Rose", 25, 30, "red")
    t1 = Tree("Oak", 500, 1825, 50)
    v1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    print("=== Garden Plant Types ===\n")

    print(f"{f1.name} ({f1.__class__.__name__}): {f1.height}cm,"
          f" {f1.age} days, {f1.color} color")
    print(f1.bloom())
    print()

    print(f"{t1.name} ({t1.__class__.__name__}): {t1.height}cm,"
          f" {t1.age} days, {t1.trunk_diameter}cm diameter")
    print(t1.produce_shade())
    print()

    print(f"{v1.name} ({v1.__class__.__name__}): {v1.height}cm,"
          f" {v1.age} days, {v1.harvest_season} harvest")
    print(v1.get_nutrition_info())
