#!/usr/bin/python3
""" 
    Module: 7-add_item (add all args to a Python list and save to a file)
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
filename = "add_item.json"

if filename is not None:
    my_list = load_from_json_file(filename)

for args in sys.argv[1:]:
    my_list.append(args)
    save_to_json_file(my_list, "add_item.json")
