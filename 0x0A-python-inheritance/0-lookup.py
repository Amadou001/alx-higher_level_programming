#!/usr/bin/python3
"""
Module lookup
"""

def lookup(obj):
    """
    returns the list of available attributes and methods of an object:
        Args:
            obj: the object
    """
    return dir(obj)
