#!/usr/bin/python3
"""
______MODULE________
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
