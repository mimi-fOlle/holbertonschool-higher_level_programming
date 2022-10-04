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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON string representation of list_objs to a file """
        list_dt = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                js_dt = json.loads(cls.to_json_string(item))
                list_dt.append(js_dt)
            with open(filename, mode='w') as a_file:
                json.dump(list_dt, a_file)
        else:
            list_objs = []
