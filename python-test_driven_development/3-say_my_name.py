#!/usr/bin/python3
"""
function that print a name
"""
def say_my_name(first_name, last_name=""):
    """
    prints "my name is <first name> <last name>"

    args:
        first_name: the first name (should be a string)
        last_name: the last name (should be a string, optional)

    raises:
        type error: if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
