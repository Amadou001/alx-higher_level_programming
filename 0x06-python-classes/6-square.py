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
        self.size = size
        self.position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) for x in value) or \
           not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function that returns the area of the squre"""
        return self.__size ** 2

    def my_print(self):
        """Function that prints the area with the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] <= 0:
                    for k in range(self.__position[0]):
                        print(end=" ")
                    for j in range(self.__size):
                        print("#", end="")
                else:
                    for j in range(self.__size):
                        print("#", end="")
                print()
