#!/usr/bin/python3
""" from json to string """
import json


def from_json_string(my_str):
    """ Module """
    s = json.loads(my_str)
    return s
