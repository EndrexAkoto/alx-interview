#!/usr/bin/python3
"""Solves the N queens problem"""

import sys


if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if (n < 4):
    print("N must be at least 4")
    exit(1)


def n_queens(n):
    """Solves the N queens puzzle"""

    columns = set()
    down_diag = set()
    up_diag = set()

    result = []

    def backtrack(board, row):
        """performing backtrack algorithm"""
        if row == n:
            new_board = [[i, board[i]] for i in range(n)]
            result.append(new_board)
            return
        for col in range(n):
            if col in columns or \
                (row + col) in down_diag or \
                    (row - col) in up_diag:
                continue

            columns.add(col)
            down_diag.add(col + row)
            up_diag.add(row - col)
            board[row] = col
            backtrack(board, row + 1)
            columns.remove(col)
            down_diag.remove(col + row)
            up_diag.remove(row - col)

    backtrack([None] * n, 0)
    return result


solutions = n_queens(n)
for s in solutions:
    print(s)