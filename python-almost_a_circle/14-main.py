#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    json_dictionary = Base.from_json_string(None)
    print(json_dictionary)