#!/usr/bin/python3
""" students """


class Student():
    """ Module """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for atr in attrs:
                for key, value in self.__dict__.items():
                    if atr == key:
                        new_dict[key] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
