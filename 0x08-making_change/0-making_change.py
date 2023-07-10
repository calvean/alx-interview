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
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
