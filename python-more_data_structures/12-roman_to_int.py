#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    char = 0
    if roman_string is None:
        return 0
    if type(roman_string) == int:
        return 0
    while char < len(roman_string):
        first_num = sum(roman_string[char])
        if (char + 1) < len(roman_string):
            second_num = sum(roman_string[char + 1])
            if first_num < second_num:
                res += (second_num) - (first_num)
                char += 2
            else:
                res += first_num
                char += 1
        else:
            res += first_num
            char += 1
    return res


def sum(number):
    if number == 'I':
        return 1
    if number == 'V':
        return 5
    if number == 'X':
        return 10
    if number == 'L':
        return 50
    if number == 'C':
        return 100
    if number == 'D':
        return 500
    if number == 'M':
        return 1000
    return -1
