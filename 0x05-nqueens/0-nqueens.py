#!/usr/bin/python3
"""
N Queens Problem: Placing N queens on an N×N
chessboard such that no two queens threaten each other.
"""

import sys


def diagonals(results, N):
    """
    Generate a list of diagonals occupied by queens.
    """
    diagonals = []
    for i in results:
        # up-left
        it_row = i[0]
        it_col = i[1]
        while 0 <= it_col < N and 0 <= it_row < N:
            if [it_row, it_col] not in diagonals:
                diagonals.append([it_row, it_col])
            it_row -= 1
            it_col -= 1

        # up-right
        it_row = i[0]
        it_col = i[1]
        while 0 <= it_col < N and 0 <= it_row < N:
            if [it_row, it_col] not in diagonals:
                diagonals.append([it_row, it_col])
            it_row -= 1
            it_col += 1

        # down-left
        it_row = i[0]
        it_col = i[1]
        while 0 <= it_col < N and 0 <= it_row < N:
            if [it_row, it_col] not in diagonals:
                diagonals.append([it_row, it_col])
            it_row += 1
            it_col -= 1

        # down-right
        it_row = i[0]
        it_col = i[1]
        while 0 <= it_col < N and 0 <= it_row < N:
            if [it_row, it_col] not in diagonals:
                diagonals.append([it_row, it_col])
            it_row += 1
            it_col += 1

    return diagonals


def isSafe(row, col, results, N):
    """
    Check if placing a queen at the specified position is safe.
    """
    # Check columns
    for _row in range(N):
        if [_row, col] in results:
            return False

    return not [row, col] in diagonals(results, N)


def chess(N):
    """
    Solve the N Queens problem and print the solutions.
    """
    result = []
    row = 0
    col = 0

    while row < N:
        while col < N:
            if isSafe(row, col, result, N):
                result.append([row, col])
                break
            col += 1

        if len(result) != (row + 1):
            row -= 1
            if row < 0:
                break
            col = result[row][1] + 1
            del result[row]
            continue
        elif len(result) == N:
            print(result)
            col += 1
            del result[row]
            continue
        row += 1
        col = 0


def start():
    """
    Entry point of the N Queens program.
    """
    args = sys.argv

    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(args[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess(N)


if __name__ == "__main__":
    start()
