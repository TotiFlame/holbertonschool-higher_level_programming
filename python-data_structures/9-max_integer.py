#!/usr/bin/python3
def max_integer(my_list=[]):
    j = my_list[0]
    for i in my_list:
        if j < i:
            j = i
    return j
