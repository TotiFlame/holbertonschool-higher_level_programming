#!/usr/bin/python3
""" module """


def add_integer(a, b=98):
    """ add_integer"""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return (a + b)
