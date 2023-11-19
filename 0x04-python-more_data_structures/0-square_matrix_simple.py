#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    mat = [[j**2 for j in matrix[i]] for i in range(len(matrix))]
    return mat
