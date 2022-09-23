#!/usr/bin/python3
""" Module: 4-rectangle """


class Rectangle:
    """
    A class to define a rectangle by:
    - Private instance attribute: width
    - Private instance attribute: height
    - Public instance method to return the rectangle area
    - Public instance method to return the rectangel perimeter
    - Print the rectangle with the character #
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)

        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i < self.__height - 1:
                string += '\n'
        return (string)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
