#!/usr/bin/python3
""" base """
import json
import os


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
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        x = json.dumps(list_dictionaries)
        return x

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It takes a class and a list of objects of that class,
        and saves the list of objects to a file in JSON format
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            with open(file_name, "w") as f:
                f.write("[]")
            return
        json_str = "["
        for num, item in enumerate(list_objs):
            if num != 0:
                json_str += ", "
            json_str += (cls.to_json_string(item.to_dictionary()))
        json_str += "]"
        with open(file_name, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)
