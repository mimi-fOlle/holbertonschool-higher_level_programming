#!/usr/bin/python3
""" Module: 10-square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[{}] {}/{}".format(Rectangle.__name__,
                                    self.__size, self.__size))
