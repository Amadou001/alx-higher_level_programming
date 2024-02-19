#!/usr/bin/python3
'''Module for Rectangle class.'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a square.'''

    def __init__(self, size):
        '''Constructor.

            Args:
                size: size of the side of the square
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area of square.'''
        return self.__size ** 2
