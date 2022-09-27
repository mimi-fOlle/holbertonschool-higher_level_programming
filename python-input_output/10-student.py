#!/usr/bin/python3
""" Method: 10-student """


class Student:
    """
    To define a student by:
    - first_name
    - last_name
    - age
    - Public method to retrieves a dict representation of a student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}

        if not isinstance(attrs, list):
            if not isinstance(list, str):
                return (self.__dict__)
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return (my_dict)
