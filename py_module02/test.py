try:
    print("A")
    raise ValueError("error")
    print("B")
except ValueError:
    print("C")
print("D")
