#!/usr/bin/python3
""" Unlock Boxes """


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    unlocked = set([0])
    keys = set(boxes[0])
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])
    return len(unlocked) == len(boxes)
