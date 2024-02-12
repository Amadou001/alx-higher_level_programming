#!/usr/bin/python3
"""
Definition of a rectangle
"""


class Rectangle:
    """
    Class for defining a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Constructor:
            Args:
                width(integer, optional): width of the rectangle
                height(integer, optinal): height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the value of the private attribute __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the private attribute __width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the private attribute __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the private attribute __height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        String representation of the rectangle object
        """
        string_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return string_rectangle
        for i in range(self.__height):
            if i == 0:
                string_rectangle += str(self.print_symbol) * self.__width
                continue
            string_rectangle += "\n" + str(self.print_symbol) * self.__width
        return string_rectangle

    def __repr__(self):
        """
        String representation of the rectangle object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletion of the rectangle object
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
