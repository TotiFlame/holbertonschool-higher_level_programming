#!/usr/bin/python3
def common_elements(set_1, set_2):
    for f_set in set_1:
        for s_set in set_2:
            if f_set == s_set:
                return f_set
