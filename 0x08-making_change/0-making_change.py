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

    remaining = total
    coin_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining > 0:
        if coin_index >= num_coins:
            return -1

        if remaining - sorted_coins[coin_index] >= 0:
            remaining -= sorted_coins[coin_index]
            coin_count += 1
        else:
            coin_index += 1

    return coin_count
