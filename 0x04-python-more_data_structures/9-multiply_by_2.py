#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for element, value in new_dictionary.items():
        new_dictionary[element] = value * 2
    return new_dictionary
