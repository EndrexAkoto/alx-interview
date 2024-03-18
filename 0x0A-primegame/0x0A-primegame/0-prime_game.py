#!/usr/bin/python3

def sieve(max_n):
    """Sieve of Eratosthenes algorithm to find all primes up to max_n."""
    prime = [True for _ in range(max_n + 1)]
    p = 2
    while (p * p <= max_n):
        if (prime[p] == True):
            for i in range(p * p, max_n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return [p for p in range(max_n + 1) if prime[p]]

def simulate_game(n, primes):
    """Simulate a single game and return True if Maria wins, False otherwise."""
    # Initially, no numbers are removed. A player wins if the other player cannot move.
    remaining = n - sum(1 for p in primes if p <= n)
    # Maria starts, so if the number of remaining rounds after removing primes and their multiples is odd, Maria wins.
    return remaining % 2 == 1

def isWinner(x, nums):
    """Determine the overall winner of x rounds of the game."""
    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0

    for n in nums:
        if simulate_game(n, primes):
            maria_wins += 1

    ben_wins = x - maria_wins  # Total rounds minus Maria's wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
git add .
