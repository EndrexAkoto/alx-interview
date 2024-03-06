#!/usr/bin/python3
"""
this module defines the function makeChange
"""


def makeChange(coins, total):
    """
    this function takes as arguments
        coins: list of coins
        total: the amount to meet using these coins
    and return the fewest number of coins needed to reach total
    """

    if total <= 0:
        return 0

    number_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            number_coins += 1

    if total == 0:
        return number_coins
    return -1