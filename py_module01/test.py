class Person:
    def __init__(name, age):
        name.age = age

    def get_info(name):
        print(f"you are {name.age} years old")


p1 = Person(25)
p1.get_info()
