#!/usr/bin/python3
""" base """
import json


class Base():
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ json list """
        if list_dictionaries is None:
            return "[]"
        x = json.dumps(list_dictionaries)
        return x
