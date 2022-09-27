#!/usr/bin/python3
""" Module: 0-read_file """


def read_file(filename=""):
    """
    to read a text and print it to stdout
    """
    with open(filename, encoding='utf-8') as a_file:
        print("{}".format(a_file.read()), end="")
