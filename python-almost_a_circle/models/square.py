#!/usr/bin/python3
""" Module: square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return [Square] (<id>) <x>/<y> - <size> """
        return "[Square] ({}) {}/{} - {}".\
               format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Public method to assign attributes """
        attr = ("id", "size", "x", "y")
        for i, j in enumerate(args):
            setattr(self, attr[i], j)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of a Square """
        dt = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return (dt)
