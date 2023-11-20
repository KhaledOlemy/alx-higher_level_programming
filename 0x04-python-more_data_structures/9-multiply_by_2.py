#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for item in new_dict:
        new_dict[item] = new_dict[item] * 2
    return new_dict
