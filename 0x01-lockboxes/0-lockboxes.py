#!/usr/bin/python3
"""Unlock boxes"""


def canUnlockAll(boxes):
    """Function which checks if it can unlock all the boxes
    """

    x = [0]
    for a in x:
        for boxKey in boxes[a]:
            if boxKey not in x and boxKey < len(boxes):
                x.append(boxKey)
    if len(x) == len(boxes):
        return True
    return False
