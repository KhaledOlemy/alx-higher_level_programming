#!/usr/bin/python3
""" This file represents rectangle operations"""


class Rectangle:
    """ This class Rectangle represents a rectangle"""
    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if self.checker(value) == 0:
            self._Rectangle__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if self.checker(value) == 0:
            self._Rectangle__height = value

    def checker(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
            return 1
        if val < 0:
            raise ValueError("width must be >= 0")
            return 1
        return 0
