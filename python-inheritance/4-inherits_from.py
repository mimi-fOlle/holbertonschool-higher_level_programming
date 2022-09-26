#!/usr/bin/python3
""" Module: 4-inherits_from """


def inherits_from(obj, a_class):
    """ If the object is an instance of a class that inherited
        (directly or indirectly) from the specified class,
        return True, otherwise False.
    """

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
