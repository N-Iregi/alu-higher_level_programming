#!/usr/bin/python3
"""Write a class Square that defines a square"""

class Square:
    """Write a class Square that defines a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # area method(public instance method)
    def area(self):
        return self.__size ** 2
