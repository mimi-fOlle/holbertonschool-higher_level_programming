#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in matrix:
        new.append([y ** 2 for y in x])
    return (new)
