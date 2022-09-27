#!/usr/bin/python3
""" Module: 1-write_file """


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return (a_file.write(text))
