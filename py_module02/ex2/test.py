# try:
#     while True:
#         pass
# except Exception:
#     print("handled")


# try:
#     while True:
#         pass
# except BaseException:
#     print("handled")
# print(type(isinstance))
# print(BaseException)

try:
    raise ValueError("A")
except Exception:
    print("1")
except ValueError:
    print("2")