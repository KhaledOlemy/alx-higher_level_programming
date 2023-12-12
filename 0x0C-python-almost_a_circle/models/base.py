#!/usr/bin/python3
""" BASE CLASS """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ save to json string """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to a file """
        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            if not list_objs:
                f.write("[]")
            else:
                dicts = []
                for i in list_objs:
                    dicts.append(i.to_dictionary())
                f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """ json loads """
        return json.loads(json_string)
