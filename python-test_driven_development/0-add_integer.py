#!/usr/bin/python3
"""
this module provides the `add_integer` function
the `add_integer` function adds two integers or floats
if floats are provided, they are cast to integers
"""


def add_integer(a, b=98):
    """
    adds two integers or floats after casting to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
