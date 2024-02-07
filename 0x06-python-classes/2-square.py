#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """constructor.
        Args:
            size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
