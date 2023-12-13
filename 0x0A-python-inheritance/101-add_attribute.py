#!/usr/bin/python3
""" ADD ATTRIBUTE """


def add_attribute(object, attribute, value):
    """ add attribute to object """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
