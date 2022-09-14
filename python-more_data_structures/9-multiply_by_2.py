#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for value in new:
        new[value] *= 2
    return (new)
