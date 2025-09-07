#!/usr/bin/python3
"""Write a class that defines a square"""


class Square:
    """write a class that defines a square"""
    def __init__(self, size=0):
        """initialize square with args:
        1. size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
