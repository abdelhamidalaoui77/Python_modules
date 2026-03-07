
class Plant:
    def __init__(self, name: str, height: int, curr_age: int) -> None:
        self.name = name
        self.height = height
        self.curr_age = curr_age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.curr_age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.curr_age} days old"


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Cactus", 15, 120)
    current_height = p1.height
    current_height2 = p2.height
    print("=== Day 1 ===")
    print(p1.get_info())
    for i in range(6):
        p1.grow()
        p1.age()
    print("=== Day 7 ===")
    print(p1.get_info())
    print(f"Growth this week: +{p1.height - current_height}cm")
    print()
    print("=== Day 1 ===")
    print(p2.get_info())
    for i in range(6):
        p2.grow()
        p2.age()
    print("=== Day 7 ===")
    print(p2.get_info())
    print(f"Growth this week: +{p2.height - current_height2}cm")
