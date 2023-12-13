#!/usr/bin/python3
""" RECTANGLE CLASS """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ rectangle initiator """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area calculator """
        return self.__width * self.__height

    def __str__(self):
        """ str definition """
        return "[{}] {}/{}".\
            format(Rectangle.__name__, self.__width, self.__height)
