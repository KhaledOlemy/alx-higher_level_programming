#!/usr/bin/python3
""" PRINT SORTED """


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ print sorted list """

        return (sorted(list(self)))
