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

    """If total is 0 or less, no coins needed"""
    if total <= 0:
        return 0

    """ Create array for coins needed for each amount """
    coins.sort(reverse=True)

    max_coins_needed = total + 1
    dp = [max_coins_needed] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[total] == max_coins_needed:
        return -1
    else:
        return dp[total]
