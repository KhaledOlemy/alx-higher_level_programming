#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    mat = [list(map(lambda x: x**2, item)) for item in matrix]
    return mat
