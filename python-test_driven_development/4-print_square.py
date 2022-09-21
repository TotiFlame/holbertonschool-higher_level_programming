#!/usr/bin/python3
""" module """


def print_square(size):
    """ print_square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        if i != 0:
            print("")
        for j in range(size):
            print("#", end="")
    print()
