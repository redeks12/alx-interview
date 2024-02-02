#!/usr/bin/python3
"""0x04. UTF-8 Validation"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Write a method that determines if a given
    data set represents a valid UTF-8 encoding."""
    for dat in data:
        if dat > 0b11111111:
            return False

    return True
