#!/usr/bin/python3
def no_c(my_string):
    out = []
    if not my_string:
        return my_string
    for letter in my_string:
        if letter != "c" and letter != "C":
            out.append(letter)
    return "".join(out)
