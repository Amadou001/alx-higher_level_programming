#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element_printed = 0
    for n in range(x):
        try:
            print(my_list[n], end="")
            element_printed += 1
        except IndexError:
            pass

    print()
    return element_printed
