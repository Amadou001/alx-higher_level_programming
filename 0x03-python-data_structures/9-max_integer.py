#!/usr/bin/python3
def max_integer(my_list=[]):
    list_length = len(my_list)
    if list_length == 0:
        return None
    max_number = my_list[0]
    for i in range(1, list_length - 1):
        if max_number < my_list[i]:
            max_number = my_list[i]
    return max_number
