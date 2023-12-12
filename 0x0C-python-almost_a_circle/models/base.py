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
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create from dict """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as f:
                dicts = Base.from_json_string(f.read())
                out = [cls.create(**dict_ins) for dict_ins in dicts]
                return out
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw with a turtle """
        import turtle
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(0)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()
