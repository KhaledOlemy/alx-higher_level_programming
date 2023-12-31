#!/usr/bin/python3
"""class Square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or
                not all(isinstance(n, int) for n in value) or
                len(value) != 2 or any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):

        if self.__size == 0:
            print("")
        else:
            print(self.__position[1]*"\n", end="")
            for i in range(self.__size):
                print(self.__position[0]*" ", end="")
                print("#"*self.__size)
