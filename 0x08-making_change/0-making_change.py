#!/usr/bin/python3
"""Module for making change.
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break

        num_coins += total // coin
        total %= coin

    return num_coins if total == 0 else -1
