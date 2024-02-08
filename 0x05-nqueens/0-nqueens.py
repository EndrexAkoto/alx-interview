#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
# Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

 # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

# Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row, N, solutions):
    if row == N:
 # Convert board to coordinates and add to solutions
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0

def print_solutions(N):
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    try:
        N = int(sys.argv[1])
        print_solutions(N)
    except ValueError:
        print("N must be a number")
        exit(1)
