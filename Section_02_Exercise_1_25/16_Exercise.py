"""
Exercise No. 16

Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by
all positive lower integers.

Example:
    factorial(3) -> 6

    factorial(5) -> 120

    factorial(13) -> 6227020800

Notes:
    Assume all inputs are greater than or equal to 0.
"""


def factorial(num):
    return 1 if num < 2 else num * factorial(num - 1)


print(factorial(3))