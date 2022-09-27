#!/usr/bin/python3
""" Module: 5-save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation
    """
    with open(filename, mode='w') as a_file:
        json.dump(my_obj, a_file)
