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
