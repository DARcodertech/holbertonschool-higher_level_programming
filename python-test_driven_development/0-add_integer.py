#!/usr/bin/python3
"""
    add two integers and calculate it
"""
def add_integer(a, b=98):
    """
    adds two integers

    args:
        a: The first number must be an integer or a float
        b: The second number must be an integer or a float

    returns:
        The sum of a and b, as an integer

    raises:
        TypeError: If either a or b is not an integer or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return(a + b)
