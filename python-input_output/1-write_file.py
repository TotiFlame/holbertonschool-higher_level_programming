#!/usr/bin/python3
""" Write  file """


def write_file(filename="", text=""):
    """ Module """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    f.closed
    return len(text)
