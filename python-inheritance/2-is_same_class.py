#!/usr/bin/python3
""" Module: 2-is_same_class """


def is_same_class(obj, a_class):
    """ If the object is exactly an instance of the specified class
        return True; otherwise False.
    """
    return (isinstance(obj, a_class))
