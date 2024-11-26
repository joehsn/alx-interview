#!/usr/bin/python3
""" 0x08. Making Change task's module.
"""

def makeChange(coins, total):
    """ Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): Total amount to achieve.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
