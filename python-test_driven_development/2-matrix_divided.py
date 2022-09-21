#!/usr/bin/python3
""" module """


def matrix_divided(matrix, div):
    """ matrix_divided """
    new_matrix = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    for idx, row in enumerate(matrix):
        if len(row) != length:
            raise TypeError("Each row of the matrix "
                            "must have the same size")
        new_matrix.append([])
        for j in row:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_matrix[idx].append(round(j / div, 2))
    return new_matrix
