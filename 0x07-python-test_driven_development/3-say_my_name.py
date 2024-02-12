#!/usr/bin/python3
"""
Module for printing a fullname
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the first name and last name:

        Args:
            first_name(string):
            last_name(string): optional
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
