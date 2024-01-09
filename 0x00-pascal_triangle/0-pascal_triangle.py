#!/usr/bin/python3
"""You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to 
n - 1 and each box may contain keys to the other boxes
."""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing the Pascal’s triangle of n:
    ."""

    tri = [[1], [1, 1]]
    if n <= 0:
        return []

    for i in range(2, n):
        tri.append([1])
        it = tri[i - 1]

        for j in range(1, len(it)):
            tri[i].append(it[j] + it[j - 1])
        tri[i].append(1)

    return tri
