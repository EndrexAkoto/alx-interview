#!/usr/bin/python3
"""Module for the canUnlockAll function"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened using keys.

    Args:
    - boxes (List[List[int]]): List where box with keys to other boxes is

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    keys = {i: box for i, box in enumerate(boxes)}
    keys_set = {0}
    can_open = True

    for key, value in keys.items():
        for val in value:
            if val != key:
                keys_set.add(val)

    for key in keys:
        if key not in keys_set:
            can_open = False

    return can_open
