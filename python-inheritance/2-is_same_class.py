#!/usr/bin/python3
""" Module: 2-is_same_class """


def is_same_class(obj, a_class):
    """ If the object is exactly an instance of the specified class
        return True; otherwise False.
    """
    if type(obj) is a_class:
        return (True)
    return (False)
