#!/usr/bin/python3
""" 0-prime_game module """


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds to be played.
        nums (list): An array of 'n' for each round.

    Returns:
        str or None: The name of the player with the most wins.
                     Returns None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    n = max(nums)

    # Sieve of Eratosthenes to efficiently generate prime numbers
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False

    # Pre-compute the cumulative count of prime numbers
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c

    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1

    # Determine the winner based on the count of wins for player 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
