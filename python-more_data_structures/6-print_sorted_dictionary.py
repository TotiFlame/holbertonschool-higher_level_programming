#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, value in sorted(a_dictionary.items()):
        print(f"{i}: {value}")
