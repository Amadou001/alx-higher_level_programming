#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx = len(new_list) - 1
    while idx >= 0:
        if new_list[idx] == search:
            new_list[idx] = replace
        idx -= 1
    return new_list
