#!/usr/bin/python3
""" inherits_from """


from fcntl import F_SEAL_SEAL


def inherits_from(obj, a_class):
    """ function """
    if isinstance(obj, a_class):
        return True
    else:
        return False
