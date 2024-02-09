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
