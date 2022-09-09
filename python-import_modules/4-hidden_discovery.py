#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for lett in list:
        if lett.startswith("__", 0) is False:
            print("{}".format(lett))
