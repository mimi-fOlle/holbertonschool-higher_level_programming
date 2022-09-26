#!/usr/bin/python3
""" Module: 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ If the object is an instance of the specified class, or
        if the object is an instance of a class that inherited from
        the specified class, return True, otherwise False.
    """

    return (isinstance(obj, a_class))
