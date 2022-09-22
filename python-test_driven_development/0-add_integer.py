#!/usr/bin/python3
"""
Module: 0-add_integer

Add two given numbers: a(int/float) and b(int/float)
"""


def add_integer(a, b=98):
    """
    Given two integers and return the sum
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a is float('inf') or b is float('inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if a is float('nan') or b is float('nan'):
        raise ValueError("cannot convert float NaN to integer")

    return int(a + b)
