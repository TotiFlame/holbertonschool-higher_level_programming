#!/usr/bin/python3
""" base """
import json
import os.path


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
        """
        If the string is empty, return an empty list,
        otherwise return the list of the string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy instance of the class,
        update it with the dictionary, and return it.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        ins_list = []
        if os.path.exists(file_name):
            return []
        with open(file_name, "r") as file:
            current = cls.from_json_string(file.read())
            for i in current:
                ins_list.append(cls.create(**i))
        return ins_list
