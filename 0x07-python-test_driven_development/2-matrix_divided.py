#!/usr/bin/python3
"""Defines a matrix division function"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (list): nested lis of integers or floats
        div (int/float): the dividing number (denominator)

    Raises:
        TypeError: if not a matrix(list of list) of integers/floats
        TypeError: if each row does not have same size
        TypeError: if div is not integer/float
        ZeroDivisionError: if div is equal to 0
    Return:
        new_matrix (nested list): matrix with divided elements
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
