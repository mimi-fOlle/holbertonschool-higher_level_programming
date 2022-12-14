#!/usr/bin/python3
"""
Module: 0-add_integer
"""


def add_integer(a, b=98):
    """
    Given two integers and return the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
