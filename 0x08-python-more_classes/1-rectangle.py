#!/usr/bin/python3
""" This file represents rectangle operations"""


class Rectangle:
    """ This class Rectangle represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.checker(width)
        self.__width = width
        self.checker(height)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.checker(value)
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.checker(value)
        self.__width = value

    def checker(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
