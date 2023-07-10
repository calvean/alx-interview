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

    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
