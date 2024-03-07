#!/usr/bin/python3
"""
0-pascal_triangle

A function that retuns a list of integers
that represents a Pascal's Triangle of n
"""


def binomial_coeff(n, k):
    val = 1
    if (k > n - k):
        k = n - k

    for i in range(k):
        val = val * (n - i)
        val = val // (i + 1)

    return val


def pascal_triangle(n):

    triangle = []

    if n <= 0:
        return triangle

    for line in range(n):
        row = []
        for i in range(line + 1):
            row.append(binomial_coeff(line, i))
        triangle.append(row)

    return triangle
