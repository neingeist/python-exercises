#!/usr/bin/python
# vim:set fileencoding=utf-8:

"""
A backtracking Sudoku solver.
"""

from __future__ import division, print_function
import numpy as np
import time


puzzle = [3,  7,  0,  0,  0,  4,  9,  5,  1,
          0,  0,  2,  5,  0,  0,  0,  0,  8,
          0,  0,  0,  0,  0,  0,  0,  0,  7,
          0,  0,  0,  0,  0,  3,  0,  2,  0,
          0,  1,  0,  0,  2,  0,  0,  4,  0,
          0,  5,  0,  9,  0,  0,  0,  0,  0,
          8,  0,  0,  0,  0,  0,  0,  0,  0,
          7,  0,  0,  0,  0,  5,  3,  0,  0,
          5,  9,  4,  6,  0,  0,  0,  7,  2]
puzzle = np.array(puzzle).reshape(9, 9)

visual = True


def valid():
    rows = np.vsplit(puzzle, 9)
    cols = np.hsplit(puzzle, 9)
    grids = [grid for h in np.hsplit(puzzle, 3) for grid in np.vsplit(h, 3)]

    units = rows + cols + grids
    return all(np.max(np.bincount(unit[unit != 0])) == 1 for unit in units)


def print_puzzle(clear=True):
    ANSI_CPL = "\033[%dF"  # CPL = Cursor Previous Line

    if clear:
        print(ANSI_CPL % 10)

    for row in np.vsplit(puzzle, 9):
        for element in row[0]:
            if element != 0:
                print(element, end=' ')
            else:
                print('‧', end=' ')
        print()


def set_next_number():
    position = find_first(puzzle == 0)
    for number in range(1, 10):
        puzzle[position] = number
        if valid():
            if visual:
                print_puzzle()
                time.sleep(0.005)
            if 0 not in puzzle:
                # Solved
                return True
            else:
                if set_next_number():
                    return True

    # dead end ⇒ backtrack
    puzzle[position] = 0
    return False


def find_first(condition):
    return tuple(p[0] for p in np.where(condition))


print(__doc__)
print_puzzle(clear=False)

if set_next_number():
    print_puzzle()
