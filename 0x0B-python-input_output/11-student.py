#!/usr/bin/python3
""" STUDENT CLASS WITH JSON FUN """


class Student:
    """ STUDENT CLASS """

    def __init__(self, first_name, last_name, age):
        """ Student initiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Student to json of certain attributes"""
        out_dict = dict(self.__dict__)
        if attrs is not None:
            attr_not_in = [i for i in list(out_dict.keys()) if i not in attrs]
            for attr in attr_not_in:
                del out_dict[attr]
        return out_dict

    def reload_from_json(self, json):
        out_dict = dict(self.__dict__)
        for key in json:
            out_dict[key] = json[key]
        self.__dict__ = out_dict
        return out_dict
