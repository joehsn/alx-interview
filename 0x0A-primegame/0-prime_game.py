#!/usr/bin/python3
""" 0. Prime Game module.
"""


def isWinner(x, nums):
    """ Determines the winner of a series of games between
    Maria and Ben.

    Parameters:
        x (int): The number of rounds to play.
        nums (list of int): An array of integers where each
        element represents
                            the value of n for a round.

    Returns:
        str: The name of the player ("Maria" or "Ben") who wins
        the most rounds.
             If there is a tie, returns None.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
