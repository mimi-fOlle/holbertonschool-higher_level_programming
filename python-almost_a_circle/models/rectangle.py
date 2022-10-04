#!/usr/bin/python3
""" Module: rectangle """
from models.base import Base


class Rectangle(Base):
    """
    the class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Return private attribute """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setting private attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Return private attribute """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setting private attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Return private attribute """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Setting private attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Return private attribute """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Setting private attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ Print in stdout the Rectangle instance with the character # """
        for space_y in range(self.y):
            print()
        for i in range(self.height):
            for space_x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ Return [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
               format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update Rectangle attribute """
        att = ("id", "width", "height", "x", "y")
        if args is not None and len(args) != 0:
            for i, j in enumerate(args):
                setattr(self, att[i], j)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle """
        dt = {'x': self.x, 'y': self.y, 'id': self.id,
              'height': self.height, 'width': self.width}
        return (dt)
