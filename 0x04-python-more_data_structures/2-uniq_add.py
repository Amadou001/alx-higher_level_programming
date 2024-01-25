#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set()
    num_sum = 0
    for number in my_list:
        my_set.add(number)
    new_list = list(my_set)
    for x in new_list:
        num_sum +=  x
    return num_sum
