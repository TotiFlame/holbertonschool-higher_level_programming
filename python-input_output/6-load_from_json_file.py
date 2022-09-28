#!/usr/bin/python3
""" load from json file """
import json


def load_from_json_file(filename):
    """ Module """
    with open(filename) as f:
        obj = json.load(f)
    return obj
