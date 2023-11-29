#!/usr/bin/python3
""" This file represents rectangle operations"""


class Rectangle:
    """ This class Rectangle represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        out_str = []
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                out_str.append(self.__width * str(self.print_symbol))
                if i != self.__height - 1:
                    out_str.append("\n")
        out_str = ''.join(out_str)
        return out_str

    def __repr__(self):
        out_cmd = f"Rectangle({self.__width}, {self.__height})"
        return out_cmd

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError(f"{rect_1} must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError(f"{rect_2} must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
