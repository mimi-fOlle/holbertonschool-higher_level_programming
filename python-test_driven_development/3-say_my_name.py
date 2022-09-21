#!/usr/bin/python3
"""
Module: 3-say_my_name

Prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Print the given string/strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name is None and last_name is not None:
        print("My name is {}".format(last_name))

    if first_name is not None and last_name is None:
        print("My name is {}".format(first_name))

    print("My name is {:s} {:s}".format(first_name, last_name))
