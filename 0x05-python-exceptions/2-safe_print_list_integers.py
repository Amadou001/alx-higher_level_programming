#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0

    for i in range(x):
        try:
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                integers_printed += 1
        except (IndexError, ValueError, TypeError):
            pass  # Handles the case where the index is out of range or the value is not an integer

    print()  # Adds a newline after printing integers
    return integers_printed
