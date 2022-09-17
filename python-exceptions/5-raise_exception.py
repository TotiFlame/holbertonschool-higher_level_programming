#!/usr/bin/python3
def raise_exception():
    try:
        print("{:s}".format(123))
    except Exception:
        raise Exception
