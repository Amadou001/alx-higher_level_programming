#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0, position=(0, 0)):
        """constructor.
        Args:
            size(int): size of  the square's side
            position(tuple): position of the surface representation
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Function that retrieves the private instance position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Function that sets the value of the private instance position

            Args:
                value: tuple of two positive integers
        """
        for i in value:
            if isinstance(i, int) and i >= 0:
                continue
            else:
                raise TypeError("position must be a tuple\
                                 of 2 positive integers")
        self.__position = value

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
                if self.__position[1] <= 1:
                    for k in range(self.__position[0]):
                        print(end=" ")
                    for j in range(self.__size):
                        print("#", end="")
                else:
                    for j in range(self.__size):
                        print("#", end="")
                print()
