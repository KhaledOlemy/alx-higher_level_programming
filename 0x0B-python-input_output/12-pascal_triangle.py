#!/usr/bin/python3
""" PASCAL TRIANGLE """


def pascal_triangle(n):
    """ pascal triangle """
    pass
    prev = None
    matrix = []
    for i in range(1, n+1):
        out = [1] * i
        if i == 1 or i == 2:
            prev = out
            matrix.append(out)
            continue
        for j in range(1, len(out) - 1):
            out[j] = prev[j - 1] + prev[j]
        prev = out
        matrix.append(out)
        continue
    return matrix
