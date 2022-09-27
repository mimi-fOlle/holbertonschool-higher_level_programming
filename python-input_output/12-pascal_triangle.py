#!/usr/bin/python3
""" Module: 12-pascal_triangle """


def pascal_triangle(n):
    """
    Create a pascal's Triangle
    """
    matrix = []

    for row in range(n):
        tmp = [0] * (row + 1)
        tmp[0] = 1
        tmp[row] = 1

        if row > 1:
            tmp[1] = row
            tmp[row - 1] = row

        while 0 in tmp:
            idx = tmp.index(0)
            nmb = matrix[row - 1][idx] + matrix[row - 1][idx - 1]
            tmp[idx] = nmb

        matrix.append(tmp)
    return (matrix)
