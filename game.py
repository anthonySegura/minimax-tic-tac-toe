__author__ = 'Anthony'

# TODO: - Interfaz gráfica con QT
#

import numpy as np
from board import Board
from minimax import MinimaxTree

PLAYERS = ['X', 'O']
board = Board([
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
])

IA_Player = MinimaxTree(board)
best_move = IA_Player.find_best_move()
board.play(PLAYERS[0], best_move)
print(board)

