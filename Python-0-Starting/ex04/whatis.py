import sys

if len(sys.argv) == 1:
    sys.exit(0)

try:
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"
except AssertionError as e:
    print(e)
    sys.exit(1)

is_val_int = True

try:
    val = int(sys.argv[1])
except ValueError:
    is_val_int = False

try:
    assert is_val_int, "AssertionError: argument is not an integer"
except AssertionError as e:
    print(e)
    sys.exit(1)

if (val % 2 == 0):
    print('I\'m Even.')
else:
    print('I\'m Odd.')