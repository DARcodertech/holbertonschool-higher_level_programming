#!/usr/bin/python3
"""
class that are base geometry
"""


class BaseGeometry:
    """class that are base geometry"""

    def area(self):
        """area that raise a exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
