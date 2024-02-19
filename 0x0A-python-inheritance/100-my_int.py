#!/usr/bin/python3
"""
Rebel version of int class
"""


class MyInt(int):
    """rebel version of an integer"""

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""

        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""

        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""

        return int(self) == other
