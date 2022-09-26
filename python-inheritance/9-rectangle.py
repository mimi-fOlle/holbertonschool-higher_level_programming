#!/usr/bin/python3
""" Module: 9-rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[{}] {:d}/{:d}".format(Rectangle.__name__,
                                        self.__width, self.__height))
