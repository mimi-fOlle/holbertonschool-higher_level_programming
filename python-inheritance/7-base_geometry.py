#!/usr/bin/python3
""" Module: 7-base_geometry """


class BaseGeometry:
    """ a class base on 6-base_geometry """

    def area(self):
        raise Exception("area() is not implemented")
        return (self.area)

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
