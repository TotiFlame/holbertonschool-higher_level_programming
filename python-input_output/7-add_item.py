#!/usr/bin/python3
""" add item"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json") is False:
    lst = []
    for i in range(1, len(sys.argv)):
        lst.append(sys.argv[i])
    save_to_json_file(lst, "add_item.json")
else:
    lstJs = []
    lstJs = load_from_json_file("add_item.json")
    for i in range(1, len(sys.argv)):
        lstJs.append(sys.argv[i])
    save_to_json_file(lstJs, "add_item.json")
