#!/usr/bin/python3
""" SQUARE FILE """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ square initiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ square str """
        out = "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
        return out

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, val):
        """ size setter """
        self.checker("size", val)
        self.width = val
        self.height = val

    def checker(self, varname, value):
        """ Checker for errors """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if varname == "size":
            if value <= 0:
                raise ValueError("width must be > 0")
