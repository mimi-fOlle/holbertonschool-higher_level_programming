#!/usr/bin/python3
"""
Module: 2-matrix_divided

Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide by given number 'div', rounded to 2 decimal places
    Return a new matrix
    """
    new = []
    Type_err = "matrix must be a matrix (list of lists) of integers/floats"
    size = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(matrix, list):
            if not isinstance(list, (int, float)):
                raise TypeError(Type_err)

        new.append(list(map(lambda x: round(x/div, 2), row)))

        if size != len(row):
            raise TypeError(
                  "Each row of the matrix must have the same size")

    return (new)
