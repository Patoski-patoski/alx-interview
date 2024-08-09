#!/usr/bin/python3
"""Minimum Number of Operations to Reach a Number
"""


def minOperations(n: int) -> int:
    """
    Function to calculate the minimum number of operations needed to reach a
    number `n` starting from 1.

    The operation is defined as: Add 1 to the number on the paper, then copy
    the number on the paper.

    Args:
    n (int): The target number to reach.

    Returns:
    int: The minimum number of operations needed to reach `n`.
    """

    # Initialize the minimum operations counter
    min_operations = 0

    # Initialize the divisor
    divisor = 2

    # While n is greater than 1
    while n > 1:

        # While n is divisible by the divisor
        while n % divisor == 0:

            # Add the divisor to the minimum operations counter
            min_operations += divisor

            # Divide n by the divisor
            n /= divisor

        # Increment the divisor
        divisor += 1

    # Return the minimum operations counter
    return min_operations


# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
#
# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
