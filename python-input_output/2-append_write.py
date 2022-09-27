#!/usr/bin/python3
""" Module: 2-append_write """


def append_write(filename="", text=""):
    """
    Append a string at the end of a text and return the numbers of characters"
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return (a_file.write(text))
