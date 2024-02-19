#!/usr/bin/python3
"""
______MODULE______
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """
    def area(self):
        """
        area method that raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value:

            Args:
                name: always a string
                value: integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
