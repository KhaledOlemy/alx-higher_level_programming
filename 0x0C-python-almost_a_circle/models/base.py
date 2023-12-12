#!/usr/bin/python3
""" BASE CLASS """


class Base:
    """ BASE class intiation """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init to handle duplications """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects