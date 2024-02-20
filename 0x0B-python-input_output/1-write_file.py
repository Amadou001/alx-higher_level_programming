#!/usr/bin/python3
"""___MODULE______"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, 'w') as file:
        bite_written = file.write(text)

    return bite_written
