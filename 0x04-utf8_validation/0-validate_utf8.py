#!/usr/bin/python3
"""UTF8 validation."""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """a method that determines if a given data set represents a valid UTF-8
       encoding.

    Args:
        data (List[int]): _description_: List of integers

    Returns:
        bool: _description_: True if data is a valid UTF-8 encoding,
        else return False
    """
    i = 0
    while i < len(data):
        leading_byte = data[i]
        if leading_byte >> 7 & 1 == 0:
            bytes = 1
        elif leading_byte >> 5 & 1 == 0:
            bytes = 2
        elif leading_byte >> 4 & 1 == 0:
            bytes = 3
        elif leading_byte >> 3 & 1 == 0:
            bytes = 4
        else:
            return False

        if i + bytes > len(data):
            return False

        for j in range(1, bytes):
            if (data[i + j] >> 6 & 1) != 0:
                return False

        i += bytes
    return True
