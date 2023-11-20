#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out_mat = []
    for item in matrix:
        mat = list(map(lambda x: x**2, item))
        out_mat.append(mat)
    return out_mat
