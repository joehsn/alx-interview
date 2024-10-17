#!/usr/bin/python3

"""
    0x02. Minimum Operations
"""


def minOperations(n):
    """
        Calculates the minimum number of operations
        needed to achieve exactly `n`
    """
    if n < 2:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
