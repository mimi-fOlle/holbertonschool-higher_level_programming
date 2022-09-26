#!/usr/bin/python3
""" Module: 11-square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class Square inherits from Rectangle """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__size, self.__size))
