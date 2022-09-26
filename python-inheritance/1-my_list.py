#!/usr/bin/python3
""" my_list """


class MyList(list):
    """ module """

    def print_sorted(self):
        lista = self.copy()
        lista.sort()
        print(lista)
