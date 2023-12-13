#!/usr/bin/python3
""" SQUARE """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class"""
    def __init__(self, size):
        """ square initiation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
