#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """constructor.
        Args:
            size(int): size of  the square's side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Function that retrieves the private instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function that sets the value of the private instance size

            Args:
                value:(int) new value of the size
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Function that returns the area of the squre"""
        return self.__size * self.__size

    def my_print(self):
        """Function that prints the area with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
