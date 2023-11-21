#!/usr/bin/python3
"""class Square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        condition = not isinstance(value, tuple) or not all(isinstance(n, int) for n in value)
        condition = condition or len(value) != 2 or any(i < 0 for i in value)
        if condition:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        print(self.__position[1]*"\n", end="")
        if self.__size == 0:
            print(self.__position[0]*" ", end="")
            print("")
        else:
            for i in range(self.__size):
                print(self.__position[0]*" ", end="")
                print("#"*self.__size)
