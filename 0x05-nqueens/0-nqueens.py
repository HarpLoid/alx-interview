#!/usr/bin/python3
"""Module - NQueens"""
import sys


def solve_queens_problem(n):
    """Solve NQueens problems"""

    def is_valid_position(pos, state):
        """validates position"""
        for i in range(len(state)):
            if (
                state[i] == pos or
                state[i] - i == pos - len(state) or
                state[i] + i == pos + len(state)
            ):
                return False
        return True

    def place_queens(n, index, state, solutions):
        """doc doc doc"""
        if index == n:
            solutions.append(state[:])
            return

        for i in range(n):
            if is_valid_position(i, state):
                state.append(i)
                place_queens(n, index + 1, state, solutions)
                state.pop()

    solutions = []
    place_queens(n, 0, [], solutions)
    return solutions


def main():
    """doc doc doc"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()