#!/usr/bin/python3
""" RECTANGLE FILE """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle initiation """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width property """

        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """

        self.__width = width

    @property
    def height(self):
        """ height property """

        return self.__height

    @height.setter
    def width(self, height):
        """ height setter """

        self.__height = height

    @property
    def x(self):
        """ x property """

        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """

        self.__x = x

    @property
    def y(self):
        """ y property """

        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """

        self.__y = y
