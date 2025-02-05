#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """class that are base geometry"""

    def area(self):
        """area that raise a exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if integer"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """init a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
