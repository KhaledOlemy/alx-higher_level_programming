#!/usr/bin/python3
""" PRINT SORTED """


class MyList(list):
    """ MyList class """

    def __init__(self):
        """ mylist init """
        super().__init__()

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
