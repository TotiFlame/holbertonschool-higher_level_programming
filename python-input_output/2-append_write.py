#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """ Module """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

    f.closed
    return len(text)
