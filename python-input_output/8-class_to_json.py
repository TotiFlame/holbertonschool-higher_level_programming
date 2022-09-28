#!/usr/bin/python3
""" class to json """
import json


def class_to_json(obj):
    jsObj = json.dumps(obj.__dict__)
    return jsObj
