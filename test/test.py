# class MyError(Exception):
#     counter: int = 0

#     def __init__(self, msg) -> None:
#         super().__init__(msg)
#         MyError.counter += 1


# def func():
#     raise MyError("hello")


# try:
#     func()
# except MyError as e:
#     print(e.counter)

# try:
#     func()
# except MyError as e:
#     print(e.counter)
