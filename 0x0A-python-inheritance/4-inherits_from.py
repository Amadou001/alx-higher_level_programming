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
    # Base case: if obj is an instance of a_class, return True
    if isinstance(obj, a_class):
        return True

    # Recursive case: check if any of the base classes inherit from a_class
    for base_class in obj.__class__.__bases__:
        if inherits_from(base_class, a_class):
            return True

    # If no base class inherits from a_class, return False
    return False
