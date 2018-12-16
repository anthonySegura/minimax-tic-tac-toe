__author__ = 'Anthony'

import numpy as np
from board import Board
from minimax import MinimaxTree

PLAYERS = ['X', 'O']
board = Board(np.array([
    ['-', '-', '-'],
    ['-', 'O', '-'],
    ['-', '-', '-']
]))

IA_Player = MinimaxTree(board)
best_move = IA_Player.find_best_move()

print(board.place(PLAYERS[0], best_move))

