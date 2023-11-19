#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    return [[j**2 for j in matrix[i]] for i in range(len(matrix))]
