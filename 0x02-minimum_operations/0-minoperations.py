#!/usr/bin/python3
"""0-minoperations.py """


def minOperations(n: int) -> int:
    """Minimum Operations:  a method that calculates the fewest number of
       operations needed to result in exactly n H characters in the file.

    Args:
        n (int): a number used for minimum operation

    Returns:
        int: minimum steps or 0
    """

    if not n or n < 1:
        return 0

    div = 2
    operation = 0
    while n > 1:
        if n % div == 0:
            n = n // div
            operation += div
        else:
            div += 1
    return operation
