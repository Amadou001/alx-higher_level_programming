#!/usr/bin/python3
"""Square module"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Constructor

            Args:
                size(int , optional): size of the square side
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the private attribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private attribute __size

            Args:
                value(int): positive integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Not equal"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """Greater than"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Greater than or equal"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """less than"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Less than or equal"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
