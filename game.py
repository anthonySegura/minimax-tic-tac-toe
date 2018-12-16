__author__ = 'Anthony'

import numpy as np
from board import Board
from minimax import MinimaxTree

PLAYERS = ['X', 'O']
board = Board(np.array([
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]))

IA_Player = MinimaxTree(board)
print(board.place(PLAYERS[0], IA_Player.find_best_move()))

