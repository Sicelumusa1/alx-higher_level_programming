#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
        return None
    if len(matrix) == 1 or len(matrix[0]) == 0:
        return None
    new_matrix = []
    for x in matrix:
        row = []
        for y in x:
            row.append(y**2)
        new_matrix.append(row) 
    return new_matrix
