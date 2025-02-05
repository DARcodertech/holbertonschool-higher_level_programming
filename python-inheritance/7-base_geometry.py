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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
