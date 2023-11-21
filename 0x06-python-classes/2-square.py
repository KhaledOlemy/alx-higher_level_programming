#!/usr/bin/python3
"""class Square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
