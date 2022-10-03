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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json list """
        if list_dictionaries is None:
            return "[]"
        x = json.dumps(list_dictionaries)
        return x

    @classmethod
    def save_to_file(cls, list_objs):
        #print(cls.__name__ + ".json" + list_objs)
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write("[]")
            return
        with open(cls.__name__ + ".json", "w") as f:
            json_str = ""
            for item in list_objs:
                json_str += cls.to_json_string(item.to_dictionary())
            f.write(json_str)
