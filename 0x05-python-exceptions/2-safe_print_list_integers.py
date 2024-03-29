#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integers_printed = 0
    for i in range(x):
        try:
            value = my_list[i]
            print("{:d}".format(value), end="")
            integers_printed += 1
        except (IndexError, ValueError, TypeError):
            pass
    print()
    return integers_printed
