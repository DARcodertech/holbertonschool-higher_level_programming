#!/usr/bin/python3
"""
a class Square that defines a square
"""

class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0):
        """return self size"""
        self.size = size

    @property
    def size(self):
        """size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """verify if there is error"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return size * 2"""
        return self.__size ** 2
