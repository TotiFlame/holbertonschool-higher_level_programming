#!/usr/bin/python3
""" my_list """


class MyList(list):
    """ module """

    def print_sorted(self):
        list = self.copy()
        list.sort()
        print(list)
        return self
