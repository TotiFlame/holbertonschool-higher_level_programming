#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("")
    for i in matrix:
        for j, elem in enumerate(i):
            print("{:d}".format(elem), end='')
            if j != len(i) - 1:
                print('', end=' ')
        print()
