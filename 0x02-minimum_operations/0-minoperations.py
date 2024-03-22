#!/usr/bin/python3
"""
Module - Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    next = 'H'
    body = 'H'
    ops = 0
    while (len(body) < n):
        if n % len(body) == 0:
            ops += 2
            next = body
            body += body
        else:
            ops += 1
            body += next
    if len(body) != n:
        return 0
    return ops
