#!/usr/bin/python3
""" This is where module documentation should be """


class Square():
    """ Defines a class Square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

        Type_err = "position must be a tuple of 2 positive integers"
        if isinstance(position, tuple) and len(position) == 2:
            if isinstance(position[0], int) and isinstance(position[1], int):
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(Type_err)
            else:
                raise TypeError(Type_err)
        else:
            raise TypeError(Type_err)

    def area(self):
        """ Return
            ------
            The current square area """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ for retrieving the data """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ for setting the data """
        self.__size = value
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ for retrieving the data """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ for setting the data """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ Prints in stdout the square with "#" character """
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
        for y in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
