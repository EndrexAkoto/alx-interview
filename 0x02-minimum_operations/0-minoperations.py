#!/usr/bin/python3
"""
Calculates  few number needed, result in exactly n H characters in  file
"""


def minOperations(n):
    """
    Calculates fewest number of operations needed 

    :param n: The target number of H characters.
    :type n: int
    :return: The minimum number of operations.
    :rtype: int
    """

    if n <= 1:
        return 0

    # Initialize array to store minimum operations for each value
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to reach 1 H
    dp[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Check all factors of i
        for j in range(1, i):
            if i % j == 0:
                # Update min operations based on copying from previous value
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]


if __name__ == "__main__":

    # Testing the function with the given examples
    n1 = 4
    print("Min operations reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min operations reach {} char: {}".format(n2, minOperations(n2)))
