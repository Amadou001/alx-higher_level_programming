#!/usr/bin/python3
"""Module for defining a square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """String representation of the square"""
        square_str = ""
        if self.__size == 0:
            return square_str

        square_str += "\n" * self.__position[1]

        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"

        return square_str

    def __repr__(self):
        """Representation of the square"""
        return self.__str__()
