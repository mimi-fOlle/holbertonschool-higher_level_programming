#!/usr/bin/python3
""" This is where module documentation should be """


class Square():
    """ A class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0):
        - size must be an integer, otherwise raise a TypeError with message
        - if size is less than 0, raise a ValueError with message
        - Public instance method: def area(self)
    """
    def __init__(self, size=0):
        """ Initialize instance attribute """
        self.__size = size
        
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Return: The current square area """
        return (self.__size * self.__size)
