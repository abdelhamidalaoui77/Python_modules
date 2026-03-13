
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_age(age)
        self.set_height(height)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def func2(self):
        self.__height += 1

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age



sp1 = SecurePlant("Tree", 100, 345)
print(sp1.name, sp1.get_height(), sp1.get_age())
sp1.set_height(102)
# sp1.func2()
print(sp1.get_height())


class sss(SecurePlant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def func(self):
        self.set_height(self.get_height() + 1)


ss1 = sss("ssss", 8, 12, "red")
ss1.set_height(15)
ss1.func()
print(ss1.name, ss1.get_height(), ss1.color)

# if __name__ == "__main__":
#     print("=== Garden Security System ===")
#     sp1 = SecurePlant("Rose", 25, 30)

#     print(f"Plant created: {sp1.name}")
#     print(f"Height updated: {sp1.get_height()} [OK]")
#     print(f"Age updated: {sp1.get_age()} [OK]")
#     print()
#     sp1.set_height(-5)
#     print()
#     print(f"Current plant: {sp1.name} ({sp1.get_height()}cm,", end=" ")
#     print(f"{sp1.get_age()} days)")
