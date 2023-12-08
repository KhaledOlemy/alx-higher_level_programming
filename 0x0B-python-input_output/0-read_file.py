#!/usr/bin/python3
""" reading a file """


def read_file(filename=""):
    """ read a file """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
