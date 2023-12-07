#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or len(matrix) == 0 or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    counts = []
    row_len = 0
    for row in matrix:
        col_len = 0
        for col in row:
            if not (isinstance(col, int) or isinstance(col, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            col_len += 1
        counts.append(col_len)
        row_len += 1
    if len(list(set(counts))) != 1:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]
    return new_matrix

