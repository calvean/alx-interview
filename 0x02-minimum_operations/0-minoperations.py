#!/usr/bin/env python3
""" minOperations module """



def minOperations(n: int) -> int:
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    if n == 1:
        return 0
    num_ops = 0
    current_h = 1
    clipboard = 0
    while current_h < n:
        if n % current_h == 0:
            clipboard = current_h
            num_ops += 1
        current_h += clipboard
        num_ops += 1
    return num_ops
