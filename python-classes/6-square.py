#!/usr/bin/python3
"""
a class Square that defines a square
"""


class Square:
    """a class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """return a position"""
        return self.__position

    @position.setter
    def position(self, value):
        """verify if condition are meet in position"""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return multpkcation of size"""
        return self.__size * self.__size

    def my_print(self):
        """print position with size"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
