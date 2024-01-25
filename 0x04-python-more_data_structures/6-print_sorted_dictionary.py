#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for element, value in sorted(a_dictionary.items()):
        print("{}: {}".format(element, value))
