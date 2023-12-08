#!/usr/bin/python3
""" STUDENT CLASS WITH JSON FUN """


class Student:
    """ STUDENT CLASS """

    def __init__(self, first_name, last_name, age):
        """ Student initiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Student to json """
        return self.__dict__
