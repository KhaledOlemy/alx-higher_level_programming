#!/usr/bin/python3
""" RECTANGLE FILE """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ rectangle initiation """
        self.checker("width", width)
        self.__width = width
        self.checker("height", height)
        self.__height = height
        self.checker("x", x)
        self.__x = x
        self.checker("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.checker("width", width)
        self.__width = width

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.checker("height", height)
        self.__height = height

    @property
    def x(self):
        """ x property """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.checker("x", x)
        self.__x = x

    @property
    def y(self):
        """ y property """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.checker("y", y)
        self.__y = y

    def checker(self, varname, value):
        """ Checker for errors """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(varname))
        if varname in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(varname))
        if varname in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(varname))

    def area(self):
        """ area calculator """
        return self.__width * self.__height

    def display(self):
        """ display a triangle """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            line = "#"*self.__width
            line = " "*self.__x + line
            print(line)

    def __str__(self):
        """ rectangle str """
        out = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return out

    def update(self, *args, **kwargs):
        """ update rectangle """
        net_args = [self.id, self.__width, self.__height, self.__x, self.__y]
        if args:
            if len(args) == 0:
                pass
            elif len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            else:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.__width = val
                elif key == "height":
                    self.__height = val
                elif key == "x":
                    self.__x = val
                elif key == "y":
                    self.__y = val

    def to_dictionary(self):
        """ rectangle dict """
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
