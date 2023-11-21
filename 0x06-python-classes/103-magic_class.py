#!/usr/bin/python3
import math
"""MagicClass of a circle"""


class MagicClass:
    """MagicClass for a circle"""
    def __init__(self, radius=0):
        """Initializes a MagicClass instance
        Args:
            radius: radius of MagicClass instance circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the instance of MagicClass circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the instance of MagicClass circle"""
        return (2 * math.pi * self.__radius)
