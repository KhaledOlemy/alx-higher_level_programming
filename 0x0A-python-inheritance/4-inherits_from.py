#!/usr/bin/python3
""" INHERITS FROM """


def inherits_from(obj, a_class):
    """ does obj inherit from a_class """
    return issubclass(obj, a_class) and type(obj) != a_class
