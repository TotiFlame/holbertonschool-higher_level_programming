#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return None
    if x > len(my_list):
        ite = len(my_list)
    else:
        ite = x
    for i in range(0, ite):
        print(f"{my_list[i]}", end="")
    print()
    return i + 1
    