#!/usr/bin/python3
""" Module: rectangle """


from models.base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__hgith = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        return (self.height)

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        return (self.x)

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        return (self.y)

    @y.setter
    def y(self, value):
        self.y = value
