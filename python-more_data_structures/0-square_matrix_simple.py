#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    return_m = []
    for i in range(0, len(matrix)):
        new_matrix = list(map(lambda x: x * x, matrix[i]))
        return_m.append(new_matrix)
    return return_m
