#!/usr/bin/python3
""" Unlock Boxes """


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    n = len(boxes)
    keys = set(boxes[0])
    opened = set([0])

    while keys:
        key = keys.pop()
        if key in opened:
            continue
        opened.add(key)
        keys.update(set(boxes[key]) - opened)

    return len(opened) == n
