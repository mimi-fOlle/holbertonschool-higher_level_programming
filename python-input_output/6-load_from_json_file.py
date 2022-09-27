#!/usr/bin/python3
""" Module: 6-load_from_json_file """


import json


def load_from_json_file(filename):
    """
    Create an Object from a 'JSON file'
    """
    with open(filename, encoding='utf-8') as a_file:
        return (json.load(a_file))
