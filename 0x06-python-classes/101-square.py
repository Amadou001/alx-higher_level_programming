#!/usr/bin/python3
"""Module for defining a square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor method
        
            Args:
                size(optional, int): size of the square
                position(optional tuple): tuple of positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Function that retrieves the private instance attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function that sets the value of __size private attribute
        
        Args: 
            value (int): positive integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Function that retrieves the value of __position private instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """Function that sets the value of __position attribute
        
        Args:
            value: tuple of positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or\
            not all(isinstance(x, int) for x in value) or\
            not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Function that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the area by using # and spaces"""
        if self.__size == 0:
            print()
        else:
                if self.__position[1] > 0:
                    for j in range(self.__size):
                        print("#" * self.__size)
                else:
                    for j in range(self.__size):
                        print(" " * self.__position[0], "#" * self.__size)

    def __str__(self):
         """Prints the area by using # and spaces"""
         string_square = ""
         if self.__size == 0:
             string_square = "\n"
         else:
                 if self.__position[1] > 1:
                     for i in range(self.__size):
                         string_square += "#" * self.__size + "\n"
                 else:
                     for i in range(self.__size):
                         string_square += " " * self.__position[0] + "#" * self.__size + "\n"
         return string_square

                     
                     
        

        

