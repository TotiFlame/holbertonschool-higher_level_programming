#!/usr/bin/python3
def uppercase(str):
    for i in str:
        charcito = ord(i)
        if charcito >= 97 and charcito <= 122:
            charcito = charcito - 32
        print("{}".format(chr(charcito)), end="")
    print("")
