#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    len = len(sys.argv)
    if len == 1:
        print("0")
    else:
        for i in range(1, len):
            sum += int(sys.argv[i])
        print("{}".format(sum))
