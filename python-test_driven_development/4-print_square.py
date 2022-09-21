#!/usr/bin/python3
"""
Module: 4-print_square

Prints a square with the character #
"""


def print_square(size):
    """
    Print the square with given size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    i = 0
    j = 0
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
