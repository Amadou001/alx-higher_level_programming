#!/usr/bin/python3
"""Integer Addition

Use add_integer function to perform the task
"""


def add_integer(a, b=98):
    """
    Adds two numbers

        Args:
            a(int or float):
            b(int or float): optional

        Returns: the sum in type int

    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
