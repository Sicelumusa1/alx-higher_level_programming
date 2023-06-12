#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        print()
        return None

    if len(matrix) == 1 or len(matrix[0]) == 0:
        print()
        return None

    for i in matrix:
        for j, element in enumerate(i):
            print("{:d}".format(element), end='')
            if j != len(i) - 1:
                print(' ', end='')
        print()
