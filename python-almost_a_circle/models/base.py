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

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of JSON string representation json_string """
        if json_string is None or json_string is []:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes already set """
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(3, 5)
            if cls.__name__ == "Square":
                dummy = cls(6)
            dummy.update(**dictionary)
            return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """

        filename = "{}.json".format(cls.__name__)
        list_dict = []
        with open(filename, mode='r') as a_file:
            if a_file is None:
                return ([])
            list_dict = cls.from_json_string(a_file.read())

        instance = []
        for i in list_dict:
            new = cls.create(**i)
            instance.append(new)
        return (instance)
