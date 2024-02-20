#!/usr/bin/python3
"""____MODULE______"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    (UTF8) and returns the number of characters added:
    """

    with open(filename, 'a') as file:
        byte_written = file.write(text)

    return byte_written
