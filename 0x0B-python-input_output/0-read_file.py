#!/usr/bin/python3
"""
______MODULE_______
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout:
    """

    with open(filename, 'r') as file:
        for line in file:
            print(line)
