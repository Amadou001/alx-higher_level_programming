#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element_printed = 0
    for i in range(x):
        try:
               print("{:d}".format(my_list[i]), end="")
               element_printed += 1
        except (IndexError,ValueError, TypeError):
             pass
    print()
    return element_printed
