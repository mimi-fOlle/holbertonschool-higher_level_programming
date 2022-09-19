#!/usr/bin/python3
""" This is where module documentation should be """


class Square():
    """ A class Square that defines a square by:
        - Property def size(self): to retrieve it
        - Property setter def size(self, value): to set it
        - Instantiation with optional size: def __init__(self, size=0)
        - Public instance method: def area(self):
        - Public instance method: def my_print(self):
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
        """ for retrieving the data """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ for changing the data """
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

    def my_print(self):
        """ Prints in stdout the square with "#" character """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
