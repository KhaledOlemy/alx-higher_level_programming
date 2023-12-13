#!/usr/bin/python3
""" PRINT SORTED """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(list(self)))
        return (sorted(list(self)))
