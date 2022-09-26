#!/usr/bin/python3
""" Module: 1-my_list """


class MyList(list):
    """ MyList class inherits from list """

    def print_sorted(self):
        """ method to print the sorted list """
        print(sorted(self))
