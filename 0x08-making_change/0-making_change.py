#!/usr/bin/python3
""" Make Change Module """


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of coin values.
        total (int): The target total.

    Returns:
        int: number of coins needed.
             else Returns -1.

    Raises:
        None

    """

    memo = {}

    def makeChangeHelper(remaining):
        """  Dictionary to store previously calculated results """
        if remaining in memo:
            return memo[remaining]

        if remaining == 0:
            return 0

        if remaining < 0:
            return -1

        min_coins = float('inf')

        for coin in coins:
            result = makeChangeHelper(remaining - coin)
            if result >= 0 and result < min_coins:
                min_coins = result + 1

        memo[remaining] = -1 if min_coins == float('inf') else min_coins
        return memo[remaining]

    return makeChangeHelper(total)
