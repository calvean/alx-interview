#!/usr/bin/python3
""" 0-prime_game module """


def isWinner(x, nums):
    """
    Determine the winner of each game in a series of rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): An array of 'n' for each round.

    Returns:
        str or None: The name of the player with the most wins
                     Else None.
    """

    def is_prime(num):
        """
        Check if a number is prime.

        Args:
            num (int): The number to be checked.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """
        Simulate a single round of the game.

        Args:
            n (int): The value of 'n' for the current round.

        Returns:
            int: The winner of the game (0 for Maria, 1 for Ben).

        """
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        turn = 0

        while primes:
            if turn == 0:
                prime = primes[0]
                primes = [num for num in primes if num % prime != 0]
                turn = 1
            else:
                prime = primes[0]
                primes = [num for num in primes if num % prime != 0]
                turn = 0

        return 1 - turn

    maria_wins = 0
    ben_wins = 0

    """ Play each round and keep track of the winner """
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
