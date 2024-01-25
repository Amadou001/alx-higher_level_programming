#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = set()
    for element1 in set_1:
        if element1 not in set_2:
            my_list.add(element1)
    for element2 in set_2:
        if element2 not in set_1:
            my_list.add(element2)
    return my_list
