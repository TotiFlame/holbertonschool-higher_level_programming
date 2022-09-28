#!/usr/bin/python3
""" save to json file """
import json


def save_to_json_file(my_obj, filename):
    """ Module """
    jsonStr = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(jsonStr)
    f.closed
