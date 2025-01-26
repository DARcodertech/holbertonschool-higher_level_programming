#!/usr/bin/python3
"""
function that print square
"""


def print_square(size):
    """
    prints a square with the character '#'

    args:
        size (int): the size length of the square

    raises:
        typeError: if size is not an integer or if it's a float less than 0
        valueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
