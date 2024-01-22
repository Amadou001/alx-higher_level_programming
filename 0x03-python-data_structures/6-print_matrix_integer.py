#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        x_idx = len(x) - 1
        i = 0
        while i <= x_idx:
            if i == x_idx:
                print("{:d}".format(x[i]))
            else:
                print("{:d}".format(x[i]), end=' ')
            i += 1
