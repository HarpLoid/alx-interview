#!/usr/bin/python3
"""
0-pascal_triangle

A function that retuns a list of integers
that represents a Pascal's Triangle of n
"""


def pascal_triangle(n):
    """Pascal Triangle array

    Args:
        n (int): number of rows

    Returns:
        array: pascal triangle array
    """

    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])
    for line in range(1, n):
        row = [1]
        for i in range(1, line):
            val = triangle[line - 1][i - 1] + triangle[line - 1][i]
            row.append(val)
        row.append(1)
        triangle.append(row)

    return triangle
