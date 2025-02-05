#!/usr/bin/python3
"""
class that is square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that is square"""
    def __init__(self, size):
        """initialize a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return a square"""
        return self.__size ** 2

    def __str__(self):
        """return a square"""
        return f"[Square] {self.__size}/{self.__size}"
