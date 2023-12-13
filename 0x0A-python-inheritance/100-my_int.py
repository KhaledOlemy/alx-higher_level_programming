#!/usr/bin/python3
""" MYINT CLASS INVERTED """


class MyInt(int):
    """ MyInt class"""

    def __eq__(self, value):
        """ eq inverted """
        return super().__ne__(value)

    def __ne__(self, value):
        """ ne inverted """
        return super().__eq__(value)
