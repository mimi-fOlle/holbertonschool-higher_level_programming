#!/usr/bin/python3
"""
Module: 0-add_integer

Add two given numbers: a(int/float) and b(int/float)
"""


def add_integer(a, b=98):
    """
    Given two integers and return the sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if a is None:
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
