#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    :param n: The target number of H characters.
    :type n: int
    :return: The minimum number of operations.
    :rtype: int
    """

    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each value
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed to reach 1 H
    dp[1] = 0

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Check all factors of i
        for j in range(1, i):
            if i % j == 0:
                # Update minimum operations based on copying from a previous value
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

if __name__ == "__main__":

    # Testing the function with the given examples
    n1 = 4
    print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))
