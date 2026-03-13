import sys

print("script name", sys.argv[0])


if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])
    first_arg = sys.argv[1]
    print("First argument:", first_arg)
else:
    print("No arguments provided.")
