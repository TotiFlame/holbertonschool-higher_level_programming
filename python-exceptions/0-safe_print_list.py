#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    if x == 0:
        return 0
    try:
        for i in range(0, x):
            print(f"{my_list[i]}", end="")
        print()
    except Exception:
        print()
        return i
    return i + 1
