#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in list(a_dictionary.values()):
        for item in a_dictionary:
            if a_dictionary[item] == value:
                del a_dictionary[item]
                break
    return a_dictionary
