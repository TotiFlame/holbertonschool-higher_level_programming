#!/usr/bin/python3
def text_indentation(text):
    space = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    for idx, char in enumerate(text):
        if char == "." or char == "?" or char == ":":
            space = 1
            print(f"{char}")
            print()
        if space == 1:
            if text[idx + 1] == " ":
                continue
            else:
                space = 0
        else:
            print(f"{char}", end="")
