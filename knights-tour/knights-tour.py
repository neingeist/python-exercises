#!/usr/bin/python
# vim:set fileencoding=utf-8:

"""
A backtracking Knight's Tour solver.
"""

from __future__ import division, print_function
import numpy as np
import random
import sys


visual = True


def clear_board(n):
    ANSI_CPL = "\033[%dF"  # CPL = Cursor Previous Line
    ANSI_EL = "\033[2K"  # EL = Erase Line
    print(n*(ANSI_CPL % 1 + ANSI_EL), end='')


def print_board(board, clear=False):
    if clear:
        n = board.shape[0]
        clear_board(n)

    print(board)


def next_moves(position, n):
    offsets = [(r, c) for r in range(-2, 2+1) for c in range(-2, 2+1)
               if abs(r*c) == 2]

    moves = [tuple(np.add(position, offset)) for offset in offsets]
    moves = [move for move in moves
             if all(coord in range(0, n) for coord in move)]

    return moves


def possible_next_moves(position, n, board):
    return [move for move in next_moves(position, n) if board[move] == 0]


def ordered_possible_next_moves(position, n, board):
    # Warnsdorf's Rule
    moves = sorted([(len(possible_next_moves(move, n, board)), move)
                    for move in possible_next_moves(position, n, board)])
    return [move[1] for move in moves]


def set_next_knight(board, position, k):
    n = board.shape[0]

    assert board[position] == 0
    board[position] = k

    if visual and random.random() < 0.001:
        print_board(board, clear=True)

    if 0 not in board:
        # Solved
        return board

    for move in ordered_possible_next_moves(position, n, board):

        ret = set_next_knight(board, move, k+1)
        if ret is not None:
            board = ret
            return board

    # dead end ⇒ backtrack
    board[position] = 0
    return None


def main():
    np.set_printoptions(linewidth=999)  # if n>19 or so

    print(__doc__)

    for n in range(1, 31+1):
        print('\nn = {}\n'.format(n))
        board = np.zeros((n, n), dtype=np.int)
        print_board(board)
        board = set_next_knight(board, (0, 0), 1)
        if board is not None:
            print_board(board, clear=True)
        else:
            clear_board(n)
            print('No solution')


main()
