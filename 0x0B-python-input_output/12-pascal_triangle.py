#!/usr/bin/python3
"""____MODULE_____"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal triangle of n"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate value using Pascal's triangle formula
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
        triangle.append(row)

    return triangle
