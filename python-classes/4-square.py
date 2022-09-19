#!/usr/bin/python3
""" This is where module documentation should be """


class Square:
    """ A class Square that defines a square by:
        - Property def size(self): to retrieve it
        - Property setter def size(self, value): to set it
        - Instantiation with optional size: def __init__(self, size=0)
        - Public instance method: def area(self):
    """
    def __init__(self, size=0):
        """ Initialize instance of Square
            Parameters
            ----------
            size : zero or positive number """
        self.__size = size
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Return
            ------
            The current square area """
        return (self.__size * self.__size)
