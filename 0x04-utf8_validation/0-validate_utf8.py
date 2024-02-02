#!/usr/bin/python3
"""0x04. UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Write a method that determines if a given
    data set represents a valid UTF-8 encoding."""
    count = 0
    for dat in data:
        if count == 0:
            if dat >= 0b11110000:
                count = 3
            elif dat >= 0b11100000:
                count = 2
            elif dat >= 0b11000000:
                count = 1
            elif dat >= 0b10000000:
                return False
        else:
            if dat < 0b10000000 or dat >= 0b11000000:
                return False
            count -= 1

    return count == 0
