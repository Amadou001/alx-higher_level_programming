#!/usr/bin/python3
"""
____MODULE______
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The specified class to check against.

    Returns:
        bool: True if obj is an instance of a class
        that inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
