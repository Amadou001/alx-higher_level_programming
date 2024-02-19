#!/usr/bin/python3
"""
___Module_____
"""


def is_same_class(obj, a_class):
    """
     returns True if the object is exactly an instance
     of the specified class ; otherwise False.

        Args:
            obj: the object
            a_class: the specified class
    """
    return type(obj) is a_class
