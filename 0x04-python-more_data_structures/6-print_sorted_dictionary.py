#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = dict(sorted(a_dictionary.items()))
    for element, value in b_dictionary.items():
        print("{} : {}".format(element, value))
