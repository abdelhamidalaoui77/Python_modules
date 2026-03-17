def counter():
    for i in range(5):
        yield i


counter()
for value in counter():
    print(value)
