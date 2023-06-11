#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return None

    for i in matrix:
        for j in i:
            print("{}".format(j), end=' ')
        print()
