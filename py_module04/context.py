#  Class-based
# By defining a class with the __enter__ and __exit__ methods:

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  # The returned value is assigned to the 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        # Returning None or False re-raises any exception that occurred

# Function-based (using contextlib)


# For simpler cases, Python's contextlib module provides the @contextmanager
# decorator, allowing you to use a generator function

from contextlib import contextmanager


@contextmanager
def managed_file(name, mode):
    try:
        f = open(name, mode)
        yield f  # Execution pauses and returns 'f' to the 'with' block
    finally:
        f.close()  # Code after yield runs when the 'with' block exits


with managed_file('output.txt', 'w') as f:
    f.write('Hello, context manager!')
