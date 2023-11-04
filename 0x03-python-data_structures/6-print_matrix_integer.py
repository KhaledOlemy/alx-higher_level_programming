#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listie in matrix:
        for i in range(len(listie)):
            if i != len(listie) - 1:
                print("{:d} ".format(listie[i]), end="")
            else:
                print("{:d}".format(listie[i]), end="")
        print("\n", end="")
