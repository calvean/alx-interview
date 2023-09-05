#0x0A-primegame

Prime Game is a game where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers. The chosen number and its multiples are then removed from the set. The player who cannot make a move loses the game. This program determines the winner of each game in a series of rounds.

##Functionality

The isWinner(x, nums) function accepts two parameters:

*    x (int): The number of rounds to be played.
*    nums (list): An array of n values for each round.

The function returns the name of the player with the most wins. If the winner cannot be determined, it returns None.

##Example

```
x = 3
nums = [4, 5, 1]

winner = isWinner(x, nums)
print(winner)  # Output: Ben
```

In this example, there are three rounds of the game with nums being [4, 5, 1]. The game progresses as follows:

*    First round (n = 4): Maria picks 2 and removes 2, 4, leaving 1, 3. Ben picks 3 and removes 3, leaving 1. Ben wins because there are no prime numbers left for Maria to choose.
*    Second round (n = 5): Maria picks 2 and removes 2, 4, leaving 1, 3, 5. Ben picks 3 and removes 3, leaving 1, 5. Maria picks 5 and removes 5, leaving 1. Maria wins because there are no prime numbers left for Ben to choose.
*    Third round (n = 1): Ben wins because there are no prime numbers for Maria to choose.

Therefore, Ben has the most wins, and the output is "Ben".

##Optimization

The code has been optimized using the Sieve of Eratosthenes algorithm to efficiently generate prime numbers. It pre-computes the cumulative count of prime numbers up to the maximum value in nums to determine the number of wins for Maria. The winner is then determined based on the count of wins.

##Requirements

    Python 3.x

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
