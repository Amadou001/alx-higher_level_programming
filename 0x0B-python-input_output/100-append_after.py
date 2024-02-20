#!/usr/bin/python3
"""____MODULE_____"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, after each line
    containing a specific string (see example):"""

    # Open the file for reading and writing
    with open(filename, 'r+') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Iterate over the lines and search for the search string
        for i, line in enumerate(lines):
            if search_string in line:
                # Insert the new string after the line
                # containing the search string
                lines.insert(i + 1, new_string + '\n')

        # Move the file pointer to the beginning of the file
        file.seek(0)

        # Write the modified lines back to the file
        file.writelines(lines)
