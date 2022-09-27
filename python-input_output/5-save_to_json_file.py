#!/usr/bin/python3
""" Module: 5-save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation
    """
    js_string = json.dumps(my_obj)
    with open(filename, mode='w') as a_file:
        a_file.write(js_string)
