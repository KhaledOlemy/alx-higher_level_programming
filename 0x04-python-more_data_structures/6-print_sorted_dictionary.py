#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(a_dictionary.items()))
    for item in a_dictionary:
        print("{}: {}".format(item, a_dictionary[item]))
