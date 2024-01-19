#!/usr/bin/python3
"""0x02. Minimum Operations"""


def minOperations(n: int) -> int:
    """0. Minimum Operations"""
    valueInFile = 1
    if n % 2 == 0:
        allOperations = 0
    else:
        allOperations = 1
    copyVal = 1
    pasteVal = 1
    copy = 0
    paste = 0

    # while True:
    #     if not valueInFile % 2 == 0:
    while True:
        if n % 2 == 0:
            if valueInFile * 2 <= n:
                copyVal = valueInFile
                pasteVal = copyVal
                valueInFile += pasteVal
                allOperations += 2
            else:
                valueInFile += pasteVal
                allOperations += 1
        else:
            valueInFile += pasteVal
            allOperations += 1

        if valueInFile == n:
            break
    return allOperations
