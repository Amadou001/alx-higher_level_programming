#!/usr/bin/python3
"""
____MODULE_____
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The specified class or its subclass to check against.

    Returns:
        bool: True if obj is an instance of a_class
        or its subclass, False otherwise.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
