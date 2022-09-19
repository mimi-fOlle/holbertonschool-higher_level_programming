#!/usr/bin/python3
""" There is where the module documentation should be """


class Square():
    """ A class Square that defines a square by:
        - Private instace attribute: size
        - Instantiation with size (no type/value verification)
    """
    def __init__(self, size=0):
        self.__size = size
