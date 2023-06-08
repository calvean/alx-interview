#!/usr/bin/env python3
""" rotate 2d matrix module """
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: The 2D matrix to be rotated.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)

    """ Transpose the matrix """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    """ Reverse each row """
    for i in range(n):
        matrix[i] = matrix[i][::-1]
