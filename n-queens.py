#!/usr/bin/env python3
# vim:set fileencoding=utf-8:
"""
Place n queens on a n×n chess board.

This program finds the solution by enumerating all permutations of the tuple
(1,2,...,n) as representations of the board state and checking these for
validness.

We're encoding the row of the queen as the position in the tuple, so there
can't be any queens using the same row. The column of a queen is the value of
the tuple element. As we're using only permutations of (1,2,...,n), there can't
be any queens on the same column. All that is left to do then is to check the
diagonals.

"""

from __future__ import division, print_function
from itertools import permutations


def solve(n):

    def valid(positions):
        # redundant check of rows and columns
        assert set(positions) == set(range(1, n+1))

        # check the diagonals
        # note that it only checks in the forward direction, checking in
        # the backward direction is unncessary.
        return (all(positions[row]+k != positions[row+k] and
                    positions[row]-k != positions[row+k]
                    for row in range(0, n-1) for k in range(1, n-row)))

    solutions = []
    for positions in permutations(range(1, n+1)):
        if valid(positions):
            solutions.append(positions)
    return solutions


def fundamental(solutions):

    def rotate90(solution):
        n = len(solution)
        rotated = [0]*n
        for k, p in enumerate(list(solution)):
            rotated[p-1] = n-k
        return tuple(rotated)

    def mirror(solution):
        n = len(solution)
        return tuple([n-p+1 for p in solution])

    def power(f, k):
        if k == 0:
            return lambda x: x  # identity
        else:
            return lambda x: power(f, k-1)(f(x))

    def variants(solution):
        return [variant
                for s in [power(rotate90, k)(solution) for k in range(4)]
                for variant in [s, mirror(s)]]

    fundamental_solutions = []
    for solution in solutions:
        if all(variant not in fundamental_solutions
                for variant in variants(solution)):
            fundamental_solutions.append(solution)
    return(fundamental_solutions)


def board(positions):
    n = len(positions)
    return ['·'*(c-1) + '♛' + '·'*(n-c) for c in positions]


def paste(list_of_lists_of_lines):
    return '\n'.join('\t'.join(lines)
                     for lines in zip(*list_of_lists_of_lines))


def main():
    print(__doc__)

    print('Number of solutions (and fundamental solutions) for different n:\n')
    for n in range(1, 11):
        solutions = solve(n)
        print('{} => {} ({})'.format(n, len(solutions),
                                     len(fundamental(solutions))))
    print()

    print('Fundamental solutions for n=8:\n')
    solutions = fundamental(solve(8))
    per_row = 5
    for prow in [solutions[i:i+per_row]
                 for i in range(0, len(solutions), per_row)]:
        print(paste(board(s) for s in prow))
        print()


main()
