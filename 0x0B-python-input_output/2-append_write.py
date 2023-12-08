#!/usr/bin/python3
""" APPENDING TO A FILE """


def append_write(filename="", text=""):
    """ append a file """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
