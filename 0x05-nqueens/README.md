# 0x05-nqueens

This is a Python module that solves the N Queens problem and prints all possible solutions. The module uses a backtracking algorithm to find all valid solutions.

## Usage

To use this module, run:

    `./0-nqueens.py N`

*    Replace N with the desired number of queens and the size of the chessboard.

    Note: The value of N must be an integer greater than or equal to 4.

Example

Here's an example of running the module with N = 4:

```
$ python 0-nqueens.py 4
[[1, 0], [3, 1], [0, 2], [2, 3]]
[[2, 0], [0, 1], [3, 2], [1, 3]]
```
In this example, there are two valid solutions for placing 4 queens on a 4 x 4 chessboard.
Implementation Details

The module consists of the following components:

*    `solve_nqueens(N)`: This function takes the number of queens N as an argument and solves the N Queens problem.

*    `is_safe(queens, row, col)`: This helper function checks if it is safe to place a queen at a given position on the chessboard.

*    `backtrack(queens)`: This recursive function performs backtracking to find all valid solutions to the N Queens problem.

## Author

Calvin Sharara - [Github](https://github.com/calvean)

## License
Public Domain. No copy write protection. 
