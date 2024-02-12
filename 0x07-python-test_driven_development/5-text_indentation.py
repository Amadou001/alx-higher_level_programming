#!/usr/bin/python3
"""
Module for printing 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new
    lines after each of these characters: ., ? and :

            Args:
                text: string
    """
    flag = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for character in text:
        if flag in ['.', '?', ':']:
            flag = ""
            continue
        print(character, end='')
        if character in ['.', '?', ':']:
            print("\n\n", end='')
            flag = character

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
