#!/usr/bin/python3
def best_score(a_dictionary):
    val = 0
    ret_key = ""
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if val < value:
            val = value
            ret_key = key
    return ret_key
