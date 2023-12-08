#!/usr/bin/python3
""" writing to a file """


def write_file(filename="", text=""):
    """ write a file """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
