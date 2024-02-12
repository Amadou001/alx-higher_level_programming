#!/usr/bin/python3
"""
Matrix division

Use of matrix_divided
"""
def matrix_divided(matrix, div):
    """
    Matrix division:

        Args:
            matrix: list of floats or integers
            div(divisor): float or integer
    """
    new_row = []
    new_matrix = []
    length_first_row = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        row_length = len(row)
        if row_length != length_first_row:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                result = element / div
                new_row.append(round(result, 2))
        new_matrix.append(new_row)
        new_row = []



    return new_matrix

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
