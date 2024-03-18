#!/usr/bin/python3
"""
this module defines the function isWinner
"""


def primeNumbers(n):
    """this function return an array of prime numbers
    smaller or equal to n using Sieve of Eratosthenes"""
    result = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            result.append(p)
    return result


def isWinner(x, nums):
    """Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing
    that number and its multiples from the set.
    The player that cannot make a move loses the game.
    They play x rounds of the game,
    where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """

    if x != len(nums):
        return None

    Ben = 0
    Maria = 0

    for num in nums:
        primes = primeNumbers(num)
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    return "Ben" if Ben > Maria else "Maria"
