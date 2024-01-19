#!/usr/bin/python3
"""0x02. Minimum Operations"""


def minOperations(n: int) -> int:
    """0. Minimum Operations"""
    valueInFile = 1
    allOperations = 0
    operation = 0

    while True:
        if not valueInFile * 2 >= n:
            operation = valueInFile
            valueInFile += operation
            allOperations += 2
        else:
            valueInFile += operation
            allOperations += 1

        if valueInFile == n:
            break
    return allOperations
