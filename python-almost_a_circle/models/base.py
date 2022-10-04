#!/usr/bin/python3
""" base """
import json


class Base:
    """
    This class will be the base of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries is {}:
            return ("[]")
        return (json.dumps(list_dictionaries))
