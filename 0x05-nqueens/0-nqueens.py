#!/usr/bin/python3
"""
0. N queens task's module.
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem and print each solution
    """
    def backtrack(row, board):
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    board = [-1] * N
    backtrack(0, board)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
