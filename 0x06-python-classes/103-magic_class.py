#!/usr/bin/python3
import math
"""MagicClass of a circle"""


class MagicClass:
    """MagicClass for a circle"""
    def __init__(self, radius=0):
        """Initializes a MagicClass instance"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Disassembly of area:"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Disassembly of circumference:"""
        return (2 * math.pi * self.__radius)
