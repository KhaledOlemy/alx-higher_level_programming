#!/usr/bin/python3
""" This file represents rectangle operations"""


class Rectangle:
    """ This class Rectangle represents a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.checker(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.checker(value, "height")
        self.__height = value

    def checker(self, value, w_h):
        if not isinstance(value, int):
            raise TypeError(f"{w_h} must be an integer")
        if value < 0:
            raise ValueError(f"{w_h} must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
