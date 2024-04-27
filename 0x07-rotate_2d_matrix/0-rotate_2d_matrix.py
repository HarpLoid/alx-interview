#!/usr/bin/python3
"""
Module - Rotate Matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix in place
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
