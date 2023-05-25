#!/usr/bin/python3
""" 0-nqueens Module """
import sys


def solve_nqueens(N):
    """
    Solves the N Queens problem and prints all possible solutions.

    Args:
        N: The number of queens and the size of the chessboard.
    """

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def is_safe(board, row, col):
        """
        Checks if queen can be placed at
        given position without attacking other queen.

        Args:
            board: current state of chessboard.
            row: row index of position to be checked.
            col: column index of position to be checked.

        Returns:
            bool: True if the position is safe, False otherwise.
        """

        for j in range(col):
            if board[row][j] == 'Q':
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < N and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        return True

    def solve(board, col):
        """
        Recursive function to solve N Queens problem.

        Args:
            board: current state of the chessboard.
            col: current column index being processed.
        """

        if col == N:
            solutions.append([''.join(row) for row in board])
            return

        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, col + 1)
                board[row][col] = '.'

    solve(board, 0)

    for solution in solutions:
        print('\n'.join(solution))
        print()

    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
